# Solar Radiation Data Analysis

This project focuses on analyzing solar radiation data across different regions, specifically Benin, Sierra Leone, and Togo. The analysis includes data visualization and statistical analysis to understand various factors like Global Horizontal Irradiance (GHI), Direct Normal Irradiance (DNI), Diffuse Horizontal Irradiance (DHI), and ambient temperature (Tamb).

## Project Overview

The core of the project involves the use of a Python function, `analyze_dataset`, to automate the visualization and analysis of solar radiation data. This function is used across three Jupyter notebooks—Benin, Sierra Leone, and Togo—to generate insightful visualizations and detect anomalies in the data.

## Files and Structure

- **Jupyter Notebooks**: Each notebook contains initial data processing steps such as importing the dataset, exploring basic statistics using `head()` and `describe()`, and performing necessary data cleaning (e.g., dropping irrelevant columns). After these steps, the `analyze_dataset` function is called to create detailed visualizations.

- **analyze_dataset.py**: This script contains the `analyze_dataset` function, which is the backbone of the project. It handles time series analysis, histogram plots, heatmap, correlation analysis, scatter plots, bubble charts and anomaly detection.

## Libraries Used

- **Pandas**: For data manipulation and analysis.
- **Matplotlib**: For creating static, animated, and interactive visualizations.
- **Seaborn**: For statistical data visualization.
- **SciPy**: For scientific and technical computing, specifically the `zscore` function from `scipy.stats`.

## Usage Instructions

To run the analysis:

1. **Load the Dataset**: Import the dataset in any of the Jupyter notebooks.
2. **Preprocess the Data**: Use functions like `head()` and `describe()` to explore the data and clean it as needed.
3. **Run the Analysis**: Call the `analyze_dataset` function to generate visualizations and perform the analysis.

## Key Visualizations

- **Monthly, Daily, and Hourly Patterns**: Line graphs showing trends in GHI, DNI, DHI, and Tamb.
- **Impact of Cleaning on Sensors**: Line graphs comparing sensor readings with and without cleaning applied.
- **Correlation Analysis**: Heatmaps to explore correlations between variables.
- **Scatter Matrices**: Pair plots to examine relationships between wind conditions and solar irradiance.
- **Bubble Charts**: Visualizations representing relationships between GHI, Tamb, and WS with bubble sizes denoting Relative Humidity (RH).

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
