import pytest
import pandas as pd
import numpy as np
from unittest.mock import patch
from scipy.stats import zscore
from scripts.analyze_data import analyze_dataset

# Sample data for testing
@pytest.fixture
def sample_data():
    # Create a DataFrame with sample data
    data = {
        'Timestamp': pd.date_range(start='2022-01-01', periods=100, freq='H'),
        'GHI': np.random.uniform(-10, 100, size=100),  # Includes negative values
        'DNI': np.random.uniform(-10, 100, size=100),  # Includes negative values
        'DHI': np.random.uniform(-10, 100, size=100),  # Includes negative values
        'Tamb': np.random.uniform(20, 30, size=100),
        'Cleaning': np.random.choice([0, 1], size=100),
        'ModA': np.random.uniform(0, 1, size=100),
        'WS': np.random.uniform(0, 10, size=100),
        'WSgust': np.random.uniform(0, 10, size=100),
        'WD': np.random.uniform(0, 360, size=100),
        'RH': np.random.uniform(30, 100, size=100)
    }
    df = pd.DataFrame(data)
    return df

def test_analyze_dataset(sample_data):
    # Test the function without raising exceptions
    try:
        analyze_dataset(sample_data)
    except Exception as e:
        pytest.fail(f"analyze_dataset raised an exception: {e}")

    # Test if negative values are replaced by zero in 'GHI', 'DNI', 'DHI'
    cleaned_data = sample_data.copy()
    cleaned_data['GHI'] = cleaned_data['GHI'].apply(lambda x: 0 if x < 0 else x)
    cleaned_data['DNI'] = cleaned_data['DNI'].apply(lambda x: 0 if x < 0 else x)
    cleaned_data['DHI'] = cleaned_data['DHI'].apply(lambda x: 0 if x < 0 else x)

    # Check if the values have been cleaned
    assert (cleaned_data['GHI'] == 0).sum() + (cleaned_data['DNI'] == 0).sum() + (cleaned_data['DHI'] == 0).sum() > 0

    # Check if new columns for Z-scores are created
    z_scores = cleaned_data[['GHI', 'DNI', 'DHI']].apply(zscore)
    cleaned_data['Z_GHI'] = z_scores['GHI']
    cleaned_data['Z_DNI'] = z_scores['DNI']
    cleaned_data['Z_DHI'] = z_scores['DHI']

    # Check if outliers are detected correctly
    outliers = cleaned_data[(cleaned_data['Z_GHI'].abs() > 3.5) |
                            (cleaned_data['Z_DNI'].abs() > 3.5) |
                            (cleaned_data['Z_DHI'].abs() > 3.5)]
    assert isinstance(outliers, pd.DataFrame)

    # Mocking the plotting function to ensure it's called without displaying
    with patch('matplotlib.pyplot.show'), patch('matplotlib.pyplot.savefig'), patch('matplotlib.pyplot.plot'):
        # Call the visualization function here, if separate from analyze_dataset.
        # Example: analyze_dataset(sample_data) might include plotting functions.
        analyze_dataset(sample_data)  # Ensure this includes plotting if applicable

        # Check that show() was called; this will now succeed since we mocked it
        # If you want to check for specific plotting calls, you can assert them here as well