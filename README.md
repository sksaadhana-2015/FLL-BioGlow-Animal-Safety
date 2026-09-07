# 🌿 FLL BioGlow - Animal Vehicle Accident Tracker 🌿

An innovative application that tracks and visualizes animal-vehicle accidents in Des Moines, Iowa. This project combines data analysis with interactive mapping to help protect local wildlife.

## 📋 Project Overview

This application tracks:
- **Animal Deaths** from vehicle accidents
- **Animal Injuries** from vehicle accidents
- **Accident Frequency** and patterns
- **Animal Species** involved in accidents
- **Geographic Hotspots** where accidents occur most frequently

## 🎯 Features

✅ **Interactive Waze-Style Map** - Visualize all accident locations on an interactive map
✅ **Heatmap Layer** - See accident hotspots at a glance
✅ **Frequency Analysis** - Understand how often accidents occur
✅ **Animal Statistics** - Track which species are most affected
✅ **Location Filtering** - Identify dangerous areas
✅ **Comprehensive Reports** - Detailed data analysis
✅ **JSON Export** - Save statistics for further analysis

## 📊 Data Included

The application includes sample data from **January 2024 to June 2025** for Des Moines, IA featuring:
- 🦌 Deer
- 🦝 Raccoon
- 🐭 Opossum
- 🐺 Coyote
- 🐿️ Squirrel
- 🦊 Fox

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/sksaadhana-2015/FLL-BioGlow-Animal-Safety.git
cd FLL-BioGlow-Animal-Safety
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

### Running the Application

```bash
python app.py
```

This will:
1. 📊 Display a comprehensive report in your terminal
2. 🗺️ Generate an interactive map file: `waze_map.html`
3. 📁 Save statistics to: `statistics.json`

## 📖 Using the Application

### View the Interactive Map
1. Run `python app.py`
2. Open `waze_map.html` in your web browser
3. Zoom in/out to explore accident locations
4. Click on any dot to see details about that incident

### Map Features
- **Red Dots** = Animal Deaths (most severe)
- **Orange Dots** = Animal Injuries
- **Heatmap Layer** = Shows concentration of accidents
- **Animal Emojis** = Quick identification of species
- **Pop-up Details** = Date, location, animal type, severity

### Reading the Report
The terminal report shows:
- Total incidents, deaths, and injuries
- Frequency analysis (how often deaths occur)
- Animals most affected
- Top accident hotspots

## 📈 Sample Statistics

The sample data includes:
- **36 total incidents** (2024-2025)
- **24 deaths** | **12 injuries**
- **Average gap between deaths**: ~14 days
- **Most affected species**: Deer (most incidents)
- **Hottest zones**: Highway 69, I-235, Highway 163

## 🔧 Customizing the Data

### Add Your Own Data
Edit `sample_data.csv` with your own data. Format:
```
date,latitude,longitude,animal_type,incident_type,severity,location_description
2024-01-15,41.5868,-93.6250,Deer,Vehicle Accident,Death,Highway 69 near Merle Hay Road
```

### Supported Animal Types
- Deer
- Raccoon
- Opossum
- Coyote
- Squirrel
- Fox
- (Add more as needed)

### Severity Levels
- **Death** - Animal was killed
- **Injury** - Animal was injured

## 📚 Understanding the Output

### waze_map.html
An interactive web map showing:
- All accident locations with color-coded severity
- Zoom and pan controls
- Heat map visualization
- Legend with animal emojis
- Detailed pop-up information on click

### statistics.json
Machine-readable statistics including:
- General statistics
- Frequency analysis
- Animal-by-animal breakdown
- Hotspot information

## 🎓 Learning Outcomes

This project teaches:
- 📊 Data analysis with Pandas
- 🗺️ Geospatial visualization with Folium
- 📈 Statistical analysis
- 🐍 Python programming
- 🌍 Environmental awareness

## 🌍 Real-World Impact

This application can help:
- 🛣️ Identify roads needing wildlife crossing signs
- 🚨 Alert drivers about accident-prone areas
- 🔬 Support wildlife research organizations
- 🛡️ Develop wildlife protection strategies
- 📡 Share data with environmental agencies

## 📝 Research Sources

Data sourced from simulated research organization observations of animal-vehicle accidents in Des Moines, IA (2024-2025). In real-world scenarios, data could come from:
- State wildlife agencies
- Animal rescue organizations
- Road accident databases
- Citizen science initiatives

## 🤝 Contributing

To improve this project:
1. Add more real data
2. Implement additional filters
3. Add time-series analysis
4. Create prediction models
5. Integrate with real data APIs

## 📄 License

This project is open source and available for educational use.

## 🎯 FLL Connection

This project aligns with FLL BioGlow's mission to:
- 🌱 Understand biological systems
- 🔍 Solve real-world problems
- 🌍 Make a positive environmental impact
- 💡 Use technology for good

## 👨‍💻 Author

Created for FLL BioGlow Innovation Project
Des Moines, Iowa

---

**Questions?** Check the comments in `app.py` for code explanations!
