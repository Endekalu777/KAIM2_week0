import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

def analyze_dataset(df, z_threshold = 3.5):

    # Change the time stamp to dateformat
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df['Year'] = df['Timestamp'].dt.year
    df['Month'] = df['Timestamp'].dt.month
    df['Day'] = df['Timestamp'].dt.day
    df['Hour'] = df['Timestamp'].dt.hour

   # Re assign the value of GHI vales for negative values and replace the the values with 0
    df['GHI'] = df['GHI'].apply(lambda x : 0 if x < 0 else x)
    df['DNI'] = df['DNI'].apply(lambda x : 0 if x < 0 else x)
    df['DHI'] = df['DHI'].apply(lambda x : 0 if x < 0 else x)	

    # Time series analysis using line graphs
    df.set_index('Timestamp', inplace=True)

    # Resample data by month to observe monthly patterns
    monthly_data = df.resample('M').mean()
    # Resample data by day to observe daily trends
    daily_data = df.resample('D').mean()

    # Resample data by hour to observe hourly trends
    hourly_data = df.resample('h').mean()

    # Monthly Patterns
    plt.figure(figsize=(14, 8))
    plt.plot(monthly_data.index, monthly_data['GHI'], label='GHI')
    plt.plot(monthly_data.index, monthly_data['DNI'], label='DNI')
    plt.plot(monthly_data.index, monthly_data['DHI'], label='DHI')
    plt.plot(monthly_data.index, monthly_data['Tamb'], label='Tamb')
    plt.xlabel('Month')
    plt.ylabel('Value')
    plt.title('Monthly Patterns of GHI, DNI, DHI, and Tamb')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Daily trends
    plt.figure(figsize=(14, 8))
    plt.plot(daily_data.index, daily_data['GHI'], label='GHI')
    plt.plot(daily_data.index, daily_data['DNI'], label='DNI')
    plt.plot(daily_data.index, daily_data['DHI'], label='DHI')
    plt.plot(daily_data.index, daily_data['Tamb'], label='Tamb')
    plt.xlabel('Day')
    plt.ylabel('Value')
    plt.title('Daily Trends of GHI, DNI, DHI, and Tamb')
    plt.legend()
    plt.grid(True)
    plt.show()
    
     # Hourly trends
    plt.figure(figsize=(14, 8))
    plt.plot(hourly_data.index, hourly_data['GHI'], label='GHI')
    plt.plot(hourly_data.index, hourly_data['DNI'], label='DNI')
    plt.plot(hourly_data.index, hourly_data['DHI'], label='DHI')
    plt.plot(hourly_data.index, hourly_data['Tamb'], label='Tamb')
    plt.xlabel('Hour')
    plt.ylabel('Value')
    plt.title('Hourly Trends of GHI, DNI, DHI, and Tamb')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Reset the index as we will use the Timestamp column for plotting
    df.reset_index(inplace=True)

    # Impact of cleaning on ModA and ModB in TOGO dataset
    cleaning_applied = df[df['Cleaning'] == 1]
    cleaning_not_applied = df[df['Cleaning'] == 0]
    
    # Plot the impact of cleaning on ModA overtime
    plt.figure(figsize = (14, 6))
    plt.plot(cleaning_applied['Timestamp'], cleaning_applied['ModA'], label = 'ModA (Cleaning applied)', color ="blue")
    plt.plot(cleaning_not_applied['Timestamp'], cleaning_not_applied['ModA'], label = 'ModA (Cleaning not applied)', color = "cyan", linestyle = '--')
    plt.xlabel('Timestamp')
    plt.ylabel('Sensor reading')
    plt.title('Impact of cleaning on sensor reading ModA over time')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot the impact of cleaning on ModB overtime
    plt.figure(figsize = (14, 6))
    plt.plot(cleaning_applied['Timestamp'], cleaning_applied['ModB'], label = 'ModB (Cleaning applied)', color ="blue")
    plt.plot(cleaning_not_applied['Timestamp'], cleaning_not_applied['ModB'], label = 'ModB (Cleaning not applied)', color = "cyan", linestyle = '--')
    plt.xlabel('Timestamp')
    plt.ylabel('Sensor reading')
    plt.title('Impact of cleaning on sensor reading ModB over time')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Correlation analysis for TOGO dataset
    df_corr = df.drop(columns = ['Timestamp', 'Year', 'Month', 'Day', 'Hour'])
    plt.figure(figsize = (14, 6))
    sns.heatmap(df_corr.corr(), annot = True, cmap = 'coolwarm')
    plt.title("Correlation heatmap")
    plt.show()

    # Relationships using scatter matrices
    data = df[['WS', 'WSgust', 'WD', 'GHI', 'DNI', 'DHI']]
    sns.pairplot(data)
    plt.suptitle("Scatter matrix of Wind Conditions and Solar Irradiance", y = 1.02)
    plt.show()
    
    # Wind analysis using polar plot
    plt.figure(figsize = (14, 6))
    plt.polar(df['WD'], df['WS'])
    plt.title("Wind speed and Direction")
    plt.show()

    # Temprature Analysis using scatter plot
    sns.scatterplot(x = df['RH'], y = df['Tamb'])
    plt.title("Relative humidity vs Temprature")
    plt.show()

    #Creating histograms
    columns_name = ['GHI', 'DNI', 'WS', 'Tamb']
    data = df[columns_name]
    plt.figure(figsize = (15, 10))
    for i, column in enumerate(data, 1):
        plt.subplot(2, 3, i)
        plt.hist(data[column], bins = 30, edgecolor = "black", alpha = 0.7)
        plt.title(f'Histogram of {column}')
        plt.xlabel(column)
        plt.ylabel("frequency")

    plt.tight_layout()
    plt.show()

    # Calculating Z-score to identify to flag datapoints
    z_scores = df[['GHI', 'DNI', 'DHI']].apply(zscore)

    # Add Z-scores to DataFrame
    df['Z_GHI'] = z_scores['GHI']
    df['Z_DNI'] = z_scores['DNI']
    df['Z_DHI'] = z_scores['DHI']
    
    # Identify outliers
    outliers = df[(df['Z_GHI'].abs() > z_threshold) |
                  (df['Z_DNI'].abs() > z_threshold) |
                  (df['Z_DHI'].abs() > z_threshold)]
    print("Number of outliers detected: ",outliers.count().sum())

    # Bubble Charts
    df['RH_normalized'] = (df['RH'] - df['RH'].min()) / (df['RH'].max() - df['RH'].min())
    bubble_size = df['RH_normalized'] * 100  

    # Create bubble chart with adjusted parameters
    plt.figure(figsize=(12, 8))
    plt.scatter(df['GHI'], df['Tamb'], s=bubble_size, c=df['WS'], alpha=0.6, cmap='plasma', edgecolors='w', linewidth=0.5)
    plt.xlabel('GHI')
    plt.ylabel('Tamb')
    plt.title('GHI vs Tamb with Bubble Size Representing Normalized RH')
    plt.colorbar(label='WS')
    plt.grid(True)
    plt.show()
