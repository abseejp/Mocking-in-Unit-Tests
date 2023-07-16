import pandas as pd
import requests


## This function provides a way to fetch data from a URL and return it as a DataFrame, with an added check to handle the case where the request is not successful.
def get_data_and_return_dataframe(url):
    # Make the GET request
    response = requests.get(url)

    # Check the status code to ensure the request was successful
    if response.status_code == 200:
        # Convert the response JSON to a DataFrame
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        return ("Request failed with a status code other than 200")
