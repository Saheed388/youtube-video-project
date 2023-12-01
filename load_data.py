import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://data.sfgov.org/resource/5cei-gny5.json'
    api_headers = {
        "X-App-Token": '',
        "X-App-Secret": ''
    }
    response = requests.get(url, headers=api_headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response and convert it to a DataFrame
        data = response.json()
        df = pd.DataFrame.from_dict(data)
        return df.head(4)
    else:
        # Print an error message if the request was not successful
        print(f"Error: {response.status_code}")
        return None

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

# Example usage:
# data = load_data_from_api()
# test_output(data)