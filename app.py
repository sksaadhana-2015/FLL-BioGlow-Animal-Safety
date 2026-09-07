import pandas as pd
import folium
from folium import plugins
import json
from datetime import datetime
from collections import Counter
import statistics

# Load the sample data
df = pd.read_csv('sample_data.csv')

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

class AnimalSafetyTracker:
    def __init__(self, data_file='sample_data.csv'):
        self.df = pd.read_csv(data_file)
        self.df['date'] = pd.to_datetime(self.df['date'])
        
    def get_statistics(self):
        """Calculate statistics about animal accidents"""
        stats = {
            'total_incidents': len(self.df),
            'total_deaths': len(self.df[self.df['severity'] == 'Death']),
            'total_injuries': len(self.df[self.df['severity'] == 'Injury']),
            'animals_by_type': self.df['animal_type'].value_counts().to_dict(),
            'incidents_by_severity': self.df['severity'].value_counts().to_dict(),
            'date_range': {
                'start': self.df['date'].min().strftime('%Y-%m-%d'),
                'end': self.df['date'].max().strftime('%Y-%m-%d')
            }
        }
        return stats
    
    def get_frequency_analysis(self):
        """Analyze how often deaths occur"""
        deaths_df = self.df[self.df['severity'] == 'Death']
        deaths_df = deaths_df.sort_values('date')
        
        if len(deaths_df) > 1:
            # Calculate days between incidents
            date_diffs = deaths_df['date'].diff().dt.days.dropna()
            
            frequency = {
                'total_deaths': len(deaths_df),
                'average_days_between_deaths': round(date_diffs.mean(), 2),
                'min_days_between_deaths': int(date_diffs.min()),
                'max_days_between_deaths': int(date_diffs.max()),
                'death_events_by_month': deaths_df.groupby(deaths_df['date'].dt.to_period('M')).size().to_dict()
            }
        else:
            frequency = {
                'total_deaths': len(deaths_df),
                'average_days_between_deaths': 'N/A',
                'min_days_between_deaths': 'N/A',
                'max_days_between_deaths': 'N/A'
            }
        
        return frequency
    
    def get_hotspots(self):
        """Identify accident hotspots by location"""
        hotspots = self.df.groupby('location_description').agg({
            'latitude': 'first',
            'longitude': 'first',
            'incident_type': 'count',
            'animal_type': lambda x: list(x.unique()),
            'severity': lambda x: list(x)
        }).rename(columns={'incident_type': 'incident_count'})
        
        hotspots = hotspots.sort_values('incident_count', ascending=False)
        return hotspots
    
    def create_waze_map(self, output_file='waze_map.html'):
        """Create an interactive map with accident locations"""
        # Calculate center of Des Moines
        center_lat = self.df['latitude'].mean()
        center_lon = self.df['longitude'].mean()
        
        # Create folium map (similar to Waze visualization)
        m = folium.Map(
            location=[center_lat, center_lon],
            zoom_start=12,
            tiles='OpenStreetMap'
        )
        
        # Color coding for severity
        severity_colors = {
            'Death': 'red',
            'Injury': 'orange'
        }
        
        # Animal emoji mapping
        animal_emojis = {
            'Deer': '🦌',
            'Raccoon': '🦝',
            'Opossum': '🐭',
            'Coyote': '🐺',
            'Squirrel': '🐿️',
            'Fox': '🦊'
        }
        
        # Add markers for each incident
        for idx, row in self.df.iterrows():
            severity = row['severity']
            animal = row['animal_type']
            emoji = animal_emojis.get(animal, '🐾')
            
            popup_text = f"""
            <b>Animal Vehicle Accident</b><br>
            Date: {row['date'].strftime('%Y-%m-%d')}<br>
            Animal: {emoji} {animal}<br>
            Severity: <span style='color:{severity_colors[severity]}'><b>{severity}</b></span><br>
            Location: {row['location_description']}<br>
            Type: {row['incident_type']}
            """
            
            folium.CircleMarker(
                location=[row['latitude'], row['longitude']],
                radius=8,
                popup=folium.Popup(popup_text, max_width=250),
                color=severity_colors[severity],
                fill=True,
                fillColor=severity_colors[severity],
                fillOpacity=0.7,
                weight=2
            ).add_to(m)
        
        # Add a heatmap layer
        heat_data = [[row['latitude'], row['longitude']] for idx, row in self.df.iterrows()]
        plugins.HeatMap(heat_data, radius=15, blur=20, max_zoom=1).add_to(m)
        
        # Add legend
        legend_html = '''
        <div style="position: fixed; 
                    bottom: 50px; right: 50px; width: 250px; height: 180px; 
                    background-color: white; border:2px solid grey; z-index:9999; 
                    font-size:14px; padding: 10px; border-radius: 5px;">
        <p style="margin: 0; font-weight: bold;">Legend</p>
        <p style="margin: 5px 0;"><i class="fa fa-circle" style="color:red"></i> Death</p>
        <p style="margin: 5px 0;"><i class="fa fa-circle" style="color:orange"></i> Injury</p>
        <p style="margin: 5px 0; font-size: 12px; color: gray;">🦌 = Deer | 🦝 = Raccoon</p>
        <p style="margin: 5px 0; font-size: 12px; color: gray;">🐺 = Coyote | 🦊 = Fox</p>
        <p style="margin: 5px 0; font-size: 12px; color: gray;">🐿️ = Squirrel | 🐭 = Opossum</p>
        <p style="margin: 5px 0; font-size: 12px; color: gray;">Red = Heatmap intensity</p>
        </div>
        '''
        
        m.get_root().html.add_child(folium.Element(legend_html))
        
        # Save the map
        m.save(output_file)
        print(f"✅ Map created and saved to {output_file}")
        return m
    
    def get_animal_type_statistics(self):
        """Get detailed statistics by animal type"""
        animal_stats = {}
        
        for animal in self.df['animal_type'].unique():
            animal_df = self.df[self.df['animal_type'] == animal]
            animal_stats[animal] = {
                'total_incidents': len(animal_df),
                'deaths': len(animal_df[animal_df['severity'] == 'Death']),
                'injuries': len(animal_df[animal_df['severity'] == 'Injury']),
                'locations': animal_df['location_description'].unique().tolist()
            }
        
        return animal_stats
    
    def print_report(self):
        """Print a comprehensive report"""
        print("\n" + "="*70)
        print("🌿 FLL BioGlow - Animal Vehicle Accident Tracker Report 🌿")
        print("="*70)
        print(f"📍 Location: Des Moines, Iowa")
        print("="*70)
        
        # General Statistics
        stats = self.get_statistics()
        print("\n📊 GENERAL STATISTICS:")
        print(f"  Total Incidents: {stats['total_incidents']}")
        print(f"  Total Deaths: {stats['total_deaths']}")
        print(f"  Total Injuries: {stats['total_injuries']}")
        print(f"  Date Range: {stats['date_range']['start']} to {stats['date_range']['end']}")
        
        # Frequency Analysis
        freq = self.get_frequency_analysis()
        print("\n📈 FREQUENCY ANALYSIS:")
        print(f"  Total Deaths: {freq['total_deaths']}")
        if freq['average_days_between_deaths'] != 'N/A':
            print(f"  Average Days Between Deaths: {freq['average_days_between_deaths']} days")
            print(f"  Shortest Gap Between Deaths: {freq['min_days_between_deaths']} days")
            print(f"  Longest Gap Between Deaths: {freq['max_days_between_deaths']} days")
        
        # Animals Involved
        print("\n🦌 ANIMALS INVOLVED:")
        animal_stats = self.get_animal_type_statistics()
        for animal, data in sorted(animal_stats.items(), key=lambda x: x[1]['total_incidents'], reverse=True):
            print(f"  {animal}: {data['total_incidents']} incidents ({data['deaths']} deaths, {data['injuries']} injuries)")
        
        # Hotspots
        print("\n🔴 TOP ACCIDENT HOTSPOTS:")
        hotspots = self.get_hotspots().head(5)
        for idx, (location, row) in enumerate(hotspots.iterrows(), 1):
            print(f"  {idx}. {location}: {row['incident_count']} incidents")
        
        print("\n" + "="*70)
        print("✅ Map has been generated: waze_map.html")
        print("="*70 + "\n")

def main():
    # Create tracker instance
    tracker = AnimalSafetyTracker('sample_data.csv')
    
    # Print comprehensive report
    tracker.print_report()
    
    # Create the interactive map
    tracker.create_waze_map('waze_map.html')
    
    # Save statistics to JSON
    stats = {
        'general_statistics': tracker.get_statistics(),
        'frequency_analysis': tracker.get_frequency_analysis(),
        'animal_statistics': tracker.get_animal_type_statistics(),
        'hotspots': tracker.get_hotspots().to_dict()
    }
    
    with open('statistics.json', 'w') as f:
        json.dump(stats, f, indent=2, default=str)
    
    print("📁 Statistics saved to statistics.json")

if __name__ == "__main__":
    main()
