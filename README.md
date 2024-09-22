# NYC Taxi Dataset Analysis and Modeling

## Introduction

This repository contains the final project for the Data Science Course. Our project is based on the [NYC Taxi Trip Duration](https://www.kaggle.com/competitions/nyc-taxi-trip-duration) dataset from a Kaggle competition. The objective of this project is to analyze the NYC taxi dataset, explore various external factors like weather and events, and build machine learning models to predict the trip duration.

The project is organized into multiple Jupyter notebooks, each focusing on different aspects of data exploration, feature engineering, and model building.

## Repository Structure

```
.
├── notebooks/
│   ├── events.ipynb
│   ├── model_training_osrm.ipynb
│   ├── nyc.ipynb
│   ├── osrm.ipynb
│   └── weather.ipynb
└── README.md
```

## Notebooks

### `nyc.ipynb`
- **Description**: This notebook provides an in-depth exploratory data analysis (EDA) of the NYC Taxi dataset. It visualizes trip distributions, pickup and drop-off locations, and examines patterns based on time, location, and other factors.

### `osrm.ipynb`
- **Description**: This notebook explains how to use OSRM to calculate routes and generate features like shortest path distance and travel time. These features are then used in the model training notebook.

### `weather.ipynb`
- **Description**: This notebook integrates weather data with the taxi trip dataset to analyze the impact of weather conditions on trip duration. It covers data collection, cleaning, and feature generation for weather-related variables.

### `events.ipynb`
- **Description**: This notebook explores various sport events happening in NYC and analyzes their potential impact on taxi trip durations. It includes data collection, cleaning, and visualization of events data.

### `model_training_osrm.ipynb`
- **Description**: This notebook focuses on training machine learning models using features generated from NYC Dataset, OSRM (Open Source Routing Machine) data and Weather data. It involves model training, and evaluation of different models.


## Datasets

### NYC Taxi Trip Duration Dataset
The main dataset used in this project is the NYC Taxi Trip Duration dataset.

### Additional Datasets
1. **OSRM Routing Data**:
   - Includes routing information such as the shortest path distance, travel time, and number of intersections for each taxi trip. These features help improve the accuracy of trip duration predictions.

2. **Weather Data**:
   - Contains historical weather information, including temperature, precipitation, and wind speed, for the NYC area. This data is used to evaluate the impact of weather conditions on taxi trip durations.

3. **NYC Sport Events Data**:
   - Events data that been collected from various known sport websites.
   - 

## Getting Started

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/idonahum/NYC_Taxi.git
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Download datasets

   All data is available in the following [Google Drive folder](https://drive.google.com/drive/folders/1NSbIqcCX6a-f4gJ-qSkHYFTwX9wlMKo8?usp=sharing).

   Use the provided `download_datasets.py` script to download the data directly into the repository's base folder or download manually and place the files `datasets` folder in the repository root folder.
   
   ```bash
   python download_datasets.py
   ```

4. **Run the notebooks:**
   Once the data is downloaded, you can run the notebooks in the `notebooks/` directory to explore the analysis and models.

## Contact
For any queries or suggestions, feel free to reach out to us:

- Ido: [nahum92@gmail.com](mailto:nahum92@gmail.com)
- Itzick: [itzick.mamistvalov@gmail.com](mailto:itzick.mamistvalov@gmail.com)
- Kobi: [kobiaflalo87@gmail.com](mailto:kobiaflalo87@gmail.com)
