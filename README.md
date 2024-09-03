# Solar Radiation Data Analysis

This project focuses on analyzing solar radiation data across different regions, specifically Benin, Sierra Leone, and Togo. The analysis includes data visualization and statistical analysis to understand various factors like Global Horizontal Irradiance (GHI), Direct Normal Irradiance (DNI), Diffuse Horizontal Irradiance (DHI), and ambient temperature (Tamb).

## Project Overview

The core of the project involves the use of a Python function, `analyze_dataset`, to automate the visualization and analysis of solar radiation data. This function is used to process and analyze data, generating insights and visualizations to support understanding and decision-making regarding solar radiation in the specified regions.

## Installation

### Creating a Virtual Environment

#### Using Conda

If you prefer Conda as your package manager:

1. Open your terminal or command prompt.

2. Navigate to your project directory.

3. Run the following command to create a new Conda environment:

    ```bash
    conda create --name your_env_name python=3.12.5
    ```
    - Replace `your_env_name` with the desired name for your environment (e.g., `solar_analysis`) and `3.12.5` with your preferred Python version.

4. Activate the environment:

    ```bash
    conda activate your_env_name
    ```

#### Using Virtualenv

If you prefer using `venv`, Python's built-in virtual environment module:

1. Open your terminal or command prompt.

2. Navigate to your project directory.

3. Run the following command to create a new virtual environment:

    ```bash
    python -m venv your_env_name
    ```
    - Replace `your_env_name` with the desired name for your environment.

4. Activate the environment:

    - On Windows:
        ```bash
        .\your_env_name\Scripts\activate
        ```

    - On macOS/Linux:
        ```bash
        source your_env_name/bin/activate
        ```

### Installing Dependencies with pip

Once your virtual environment is created and activated, you can install packages and run your Python scripts within this isolated environment. Install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

### Installing Dependencies with Conda

Alternatively, you can use Conda to install the project dependencies. Note that you will need to install each package individually. To do this, first ensure that you have activated your Conda environment, then use the following commands to install each required package:

```bash
conda install -c conda-forge package-name
```

### Clone this package
- To install the network_analysis package, follow these steps:

- Clone the repository:

```bash
git clone https://github.com/your-username/Solar_radiation_analysis.git
```
- Navigate to the project directory:

```bash
cd Solar_radiation_analysis
Install the required dependencies:
```

```bash
pip install -r requirements.txt
```

## Usage Instructions

Once the dependencies are installed, you can run the analysis notebooks by launching Jupyter Notebook or JupyterLab:

```bash
jupyter notebook
```

## Contributions
Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to create a pull request or open an issue.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

### Contact
For any questions or additional information please contact Endekalu.simon.haile@gmail.com
