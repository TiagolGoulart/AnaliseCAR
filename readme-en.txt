Rural Property Analysis using CAR
This Python script performs an analysis of rural properties using data from the Rural Environmental Registry (CAR). It reads shapefiles, processes the information, and generates an interactive map with overlay layers and a land use chart.

Prerequisites
Python 3.x
Python Libraries:
geopandas
pandas
matplotlib
folium
Pillow
base64
To install the required libraries, you can use the following command:

bash
Copy code
pip install geopandas pandas matplotlib folium Pillow base64
Data
The data used in this script is available on the SICAR website and can be downloaded according to the preferred state for analysis:

SICAR - Downloads (https://www.car.gov.br/publico/estados/downloads)

Usage Instructions
Download and extract the SICAR data for the desired state.
Organize the shapefiles into the appropriate folders, following the structure expected by the script.
Run the script and enter the CAR code in the indicated format when prompted.
Script Structure
Reading shapefiles.
Filtering data based on the provided CAR code.
Creating an interactive map using Folium.
Adding layers to the map with different colors and transparencies.
Generating a land use chart and adding it to the map.
Saving the map as an HTML file.
Example Execution
bash
Copy code
python analiseCAR.py
When prompted, enter the CAR code in the format UF-XXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.