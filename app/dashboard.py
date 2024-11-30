import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load data
benin_df = pd.read_csv("./data/benin-malanville.csv")
sierraleone_df = pd.read_csv("./data/sierraleone-bumbuna.csv")
togo_df = pd.read_csv("./data/togo-dapaong_qc.csv")

st.sidebar.header("Country Selection")
country = st.sidebar.selectbox("Select a Country", ["Benin", "Sierra-Leone", "Togo"])

if country == "Benin":
    df = benin_df
    # Removing Comments column from the dataset
    df = df.drop(columns = "Comments", axis = 1)
    # Handling negative values in the dataset
    df['GHI'] = df['GHI'].apply(lambda x : 0 if x < 0 else x)
    df['DNI'] = df['DNI'].apply(lambda x : 0 if x < 0 else x)
    df['DHI'] = df['DHI'].apply(lambda x : 0 if x < 0 else x)

elif country == "Togo":
    df = togo_df
    # Removing Comments column from the dataset
    df = df.drop(columns = "Comments", axis = 1)
    # Handling negative values in the dataset
    df['GHI'] = df['GHI'].apply(lambda x : 0 if x < 0 else x)
    df['DNI'] = df['DNI'].apply(lambda x : 0 if x < 0 else x)
    df['DHI'] = df['DHI'].apply(lambda x : 0 if x < 0 else x)

elif country == "Sierra-Leone":
    df = sierraleone_df
    # Removing Comments column from the dataset
    df = df.drop(columns = "Comments", axis = 1)
    # Handling negative values in the dataset
    df['GHI'] = df['GHI'].apply(lambda x : 0 if x < 0 else x)
    df['DNI'] = df['DNI'].apply(lambda x : 0 if x < 0 else x)
    df['DHI'] = df['DHI'].apply(lambda x : 0 if x < 0 else x)

df['Timestamp'] = pd.to_datetime(df['Timestamp'])

st.sidebar.header('Filters')

start_date = st.sidebar.date_input("Start Date", value = df["Timestamp"].min())
end_date = st.sidebar.date_input("End Date", value = df['Timestamp'].max())
ghi_threshold = st.sidebar.slider("GHI Threshold", min_value = 0, max_value = 1000, value = 500)

# Filter data based on user inputs
filtered_df = df[(df['Timestamp'] >= pd.to_datetime(start_date)) &
                (df['Timestamp'] <= pd.to_datetime(end_date)) &
                (df["GHI"] >= ghi_threshold)]

# Main Title
st.title(f"Solar Data Dashboard - {country}")
st.write("Visualizing key insights from solar radiation data")

# GHI Over Time
st.markdown("### GHI over Time")
fig, ax = plt.subplots(figsize = (10, 6))
sns.lineplot(data = filtered_df, x = "Timestamp", y = "GHI", label = "GHI", ax = ax)
ax.set_title("GHI over Time")
ax.set_ylabel("GHI")
st.pyplot(fig)

# DHI and DHI Over Time
st.markdown('### DNI and DHI over Time')
fig, ax = plt.subplots(figsize = (10, 6))
sns.lineplot(data = filtered_df, x = "Timestamp", y = "DNI", label = "DNI", ax = ax)
sns.lineplot(data = filtered_df, x = "Timestamp", y = "DHI", label = "DHI", ax = ax)
ax.set_title("DNI and DHI over Time")
ax.set_xlabel("Timestamp")
ax.set_ylabel("Irradiance")
st.pyplot(fig)

# Additional Visualization Options
st.sidebar.header("Additional Visualization")
show_dni = st.sidebar.checkbox("Show DNI")
show_dhi = st.sidebar.checkbox("Show DHI")
show_temp = st.sidebar.checkbox("Show Temprature vs GHI Scatter Plot")
show_bubble_chart = st.sidebar.checkbox("Show Buble chart: GHI vs Tamb with Normalized RH")
if show_dni:
    st.markdown("### DNI over Time")
    fig, ax = plt.subplots(figsize = (10, 6))
    sns.lineplot(data = filtered_df, x = "Timestamp", y = "DNI", color = "orange")
    ax.set_title("DNI over Time")
    ax.set_xlabel("Timestamp")
    ax.set_ylabel("DNI")
    st.pyplot(fig)

if show_dhi:
    st.markdown("### DHI over Time")
    fig, ax = plt.subplots(figsize = (10, 6))
    sns.lineplot(data = filtered_df, x = "Timestamp", y = "DHI", ax = ax, color = "green")
    ax.set_title("DHI over time")
    ax.set_xlabel("Timestamp")
    ax.set_ylabel("DHI")
    st.pyplot(fig)

if show_temp:
    st.markdown("### Temprature vs FHI Scatter Plot")
    fig, ax = plt.subplots(figsize = (10, 6))
    sns.scatterplot(data = filtered_df, x = "GHI", y = "Tamb", ax = ax, hue = "WS", size = "RH", sizes = (20, 200), alpha = 0.7, palette = "coolwarm", edgecolor = "black")
    ax.set_title("Temprature vs GHI with wind speed and Relative Humidity")
    ax.set_xlabel("GHI")
    ax.set_ylabel("Temprature (Tamb)")
    st.pyplot(fig)

if st.sidebar.checkbox("Show Raw Data"):
    st.markdown("### Raw Datat")
    st.write(filtered_df)

if show_bubble_chart:
    st.markdown('### Bubble Chart: GHI vs Tamb with Bubble Size Representing Normalized RH')

    # Normalize the RH column for bubble size
    df['RH_normalized'] = (df['RH'] - df['RH'].min()) / (df['RH'].max() - df['RH'].min())
    bubble_size = df['RH_normalized'] * 100

    # Creating the bubble chart
    fig, ax = plt.subplots(figsize=(12, 8))
    scatter = ax.scatter(df['GHI'], df['Tamb'], s=bubble_size, c=df['WS'], alpha=0.6, cmap='plasma', 
                         edgecolors='w', linewidth=0.5)
    ax.set_xlabel('GHI')
    ax.set_ylabel('Tamb')
    ax.set_title('GHI vs Tamb with Bubble Size Representing Normalized RH')
    plt.colorbar(scatter, label='WS')
    plt.grid(True)
    
    # Display the chart in Streamlit
    st.pyplot(fig)