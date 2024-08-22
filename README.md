# Introduction

This project focuses on the comprehensive analysis of datasets from three distinct regions: Benin, Sierra Leone, and Togo. The primary objective is to ensure the datasets are clean, well-structured, and ready for in-depth analysis by addressing any missing values and anomalies.

# Importing Libraries

To begin, we utilize essential libraries for data manipulation, visualization, and analysis:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
from scipy.stats import zscore
```
# Loading the datasets

We load the datasets into our environment using pandas:

```python
benin_df = pd.read_csv("../data/benin-malanville.csv")
sierraleone_df = pd.read_csv("../data/sierraleone-bumbuna.csv")
togo_df = pd.read_csv("../data/togo-dapaong_qc.csv")
```

# Inspecting the Data
To gain insights into the structure and content of each dataset, we examine the first five rows:

```python
benin_df.head()
sierraleone_df.head()
togo_df.head()
```

# Checking Dataset Shapes
Understanding the dimensions of each dataset helps us grasp the scale of our data:

```python
benin_df.shape
sierraleone_df.shape
togo_df.shape
```
# Handling Missing Values
We identify missing values using the isnull().sum() method:

```python
togo_nulls = togo_df.isnull().sum() 
benin_nulls = benin_df.isnull().sum()
sierraleone_nulls = sierraleone_df.isnull().sum()

nulls_df = pd.concat([togo_nulls, benin_nulls, sierraleone_nulls], axis=1)
nulls_df.columns = ["Togo", "Benin", "Sierra Leone"]
nulls_df
```

# Dropping Unnecessary Columns
We remove the "Comments" column from all three datasets, as it contains missing values in every row:

```python
togo_df = togo_df.drop(columns="Comments", axis=1)
benin_df = benin_df.drop(columns="Comments", axis=1)
sierraleone_df = sierraleone_df.drop(columns="Comments", axis=1)
```

# Confirming No Missing Values
After removing the "Comments" column, we confirm that no missing values remain in any of the columns across the three datasets:

```python
togo_df.isnull().sum()
benin_df.isnull().sum()
sierraleone_df.isnull().sum()

```

# Descriptive Statistics for Togo Dataset
We then explore the Togo dataset by generating descriptive statistics:

```python
togo_df.describe()
```
# Identifying Negative Values in Togo Dataset

We check for any negative values in the GHI, DNI, and DHI columns:

```python
print(togo_df[(togo_df['DHI'] < 0)])
print(togo_df[(togo_df['DNI'] < 0)])
print(togo_df[(togo_df['GHI'] < 0)])
```

# Outlier Detection Using Z-scores
We use Z-scores to detect outliers in the GHI, DNI, and DHI columns:

```python
z_scores = togo_df[['GHI', 'DNI', 'DHI']].apply(zscore)
outliers = z_scores[(z_scores > 3.5) | (z_scores < -3.5)]
out_sum = outliers.count().sum()
print(out_sum)
```

# Time Series Analysis for Togo Dataset
We plot the time series analysis for GHI, DNI, DHI, and Tamb:

```python
togo_df['Timestamp'] = pd.to_datetime(togo_df['Timestamp'])
togo_df['Year'] = togo_df['Timestamp'].dt.year
togo_df['Month'] = togo_df['Timestamp'].dt.month
togo_df['Day'] = togo_df['Timestamp'].dt.day
togo_df['Hour'] = togo_df['Timestamp'].dt.hour
```

# Plot the time series analysis 
```python
plt.figure(figsize=(14, 6))
plt.plot(togo_df['Timestamp'], togo_df['GHI'], label="GHI")
plt.plot(togo_df['Timestamp'], togo_df['DNI'], label="DNI")
plt.plot(togo_df['Timestamp'], togo_df['DHI'], label="DHI")
plt.plot(togo_df['Timestamp'], togo_df['Tamb'], label="Tamb")
plt.xlabel("Date")
plt.ylabel("Irradiance")
plt.title("GHI, DNI, DHI, Tamb over time")
plt.legend()
plt.show()
```

# Impact of Cleaning on ModA and ModB in Togo Dataset
We assess the impact of data cleaning on sensor readings:

```python
cleaning_applied = togo_df[togo_df['Cleaning'] == 1]
cleaning_not_applied = togo_df[togo_df['Cleaning'] == 0]
plt.figure(figsize=(14, 6))
plt.plot(cleaning_applied['Timestamp'], cleaning_applied['ModA'], label='ModA (Cleaning applied)', color="blue")
plt.plot(cleaning_not_applied['Timestamp'], cleaning_not_applied['ModA'], label='ModA (Cleaning not applied)', color="cyan", linestyle='--')
plt.xlabel('Timestamp')
plt.ylabel('Sensor reading')
plt.title('Impact of cleaning on sensor reading (ModA and ModB) over time')
plt.legend()
plt.grid(True)
plt.show()
```

# Correlation Analysis for Togo Dataset

We generate a heatmap to visualize the correlation between variables in the Togo dataset:

```python
togo_df_corr = togo_df.drop(columns=['Timestamp','Year', 'Month', 'Day', 'Hour'])
plt.figure(figsize=(14, 6))
sns.heatmap(togo_df_corr.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation heatmap")
plt.show()
```

# Scatter Matrix for Wind Conditions and Solar Irradiance
We explore relationships between wind conditions and solar irradiance using scatter matrices:

```python
data = togo_df[['WS', 'WSgust', 'WD', 'GHI', 'DNI', 'DHI']]
sns.pairplot(data)
plt.suptitle("Scatter matrix of Wind Conditions and Solar Irradiance", y=1.02)
plt.show()
```
# Wind Analysis Using Polar Plot
We analyze wind speed and direction using a polar plot:

```python
plt.figure(figsize=(14, 6))
plt.polar(togo_df['WD'], togo_df['WS'])
plt.title("Wind speed and Direction")
plt.show()
```

# Temperature Analysis Using Scatter Plot
We explore the relationship between relative humidity and temperature:

```python
sns.scatterplot(x=togo_df['RH'], y=togo_df['Tamb'])
plt.title("Relative humidity vs Temperature")
plt.show()
```

# Creating Histograms for GHI, DNI, DHI, WS, and Temperature
We create histograms to visualize the distribution of these variables:

```python
columns = ['GHI', 'DNI', 'WS', 'Tamb']
data = togo_df[columns]
plt.figure(figsize=(15, 10))
for i, column in enumerate(data, 1):
    plt.subplot(2, 3, i)
    plt.hist(data[column], bins=30, edgecolor="black", alpha=0.7)
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel("Frequency")

plt.tight_layout()
plt.show()
```

# Identifying Outliers Using Z-scores
We identify outliers in the GHI, DNI, and DHI columns using Z-scores:

```python
z_scores = zscore(togo_df[['GHI', 'DNI', 'DHI']])
togo_df['Z_GHI'] = z_scores[:, 0]
togo_df['Z_DNI'] = z_scores[:, 1]
togo_df['Z_DHI'] = z_scores[:, 2]
outliers = togo_df[(togo_df['Z_GHI'].abs() > 3.5) |
                   (togo_df['Z_DNI'].abs() > 3.5) |
                   (togo_df['Z_DHI'].abs() > 3.5)]
print(outliers.count().sum())
```

# Creating Bubble Charts
We visualize the relationship between GHI, Tamb, RH, and WS using a bubble chart:

```python
plt.scatter(togo_df['GHI'], togo_df['Tamb'], s=togo_df['RH']*10, c=togo_df['WS'], alpha=0.5, cmap='viridis')
plt.xlabel('GHI')
plt.ylabel('Tamb')
plt.title('GHI vs Tamb with Bubble Size Representing RH')
plt.colorbar(label='WS')
plt.show()
```

# Dataset Shape and Handling
Each dataset has a shape of (525,600, 19), indicating a substantial volume of data that requires thorough analysis. Initially, I attempted to concatenate the three datasets, but the resulting dataset was too large to handle efficiently, so we opted to analyze each dataset individually.