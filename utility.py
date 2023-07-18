import pandas as pd
import requests
import sqlite3


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



## This function retrieves user data from a SQLite database based on the provided user ID.
def fetch_user_data(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Fetch the user data from the database
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user_data = cursor.fetchone()

    # Close the database connection
    cursor.close()
    conn.close()

    if user_data:
        user = {
            'id': user_data[0],
            'name': user_data[1],
            'email': user_data[2],
            'status': 'active' if user_data[3] else 'inactive'
        }
        return user
    else:
        return "User record not found"
