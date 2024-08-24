Solar Data Dashboard
This project is a Streamlit dashboard designed to visualize solar radiation data for different countries with interactive elements for filtering and analysis.

Setup Instructions
Follow these steps to set up and run the dashboard:

Clone the repository:

git clone <repo_url>
cd <repository_name>
Create and activate virtual environment(Optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies
pip install -r requirements.txt

Run the Streamlit app:
streamlit run app/dashboard.py

Features
Country Selection: Choose between Benin, Sierra-Leone, and Togo.

Date Filtering**: Select a start and end date to filter the dataset.

GHI Threshold Filtering: Adjust the GHI (Global Horizontal Irradiance) threshold to refine the data.

Visualizations: View GHI, DNI (Direct Normal Irradiance), and DHI (Diffuse Horizontal Irradiance) trends over time.

Interactive Options: Display additional visualizations, such as temperature vs. GHI scatter plots and bubble charts for GHI vs. temperature.

Usage
Dashboard Interaction:
Use the sidebar to select the country and set filters such as date range and GHI threshold.

The main dashboard will display filtered data and visualizations based on your selections.

Viewing Raw Data:
Toggle the “Show Raw Data” option in the sidebar to view the filtered dataset.
Additional Visualizations:
Enable checkboxes in the sidebar for extra visualizations, such as DNI and DHI trends or temperature vs. GHI scatter plots.
Contribution Guidelines
Contributions are welcome! Please feel free to open an issue or submit a pull request. Ensure that you adhere to the project’s coding standards and that your code passes all tests.

License
This project is licensed under the MIT License. See the LICENSE file for more details.