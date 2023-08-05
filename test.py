import unittest
from unittest.mock import patch, Mock
import pandas as pd
from utility import get_data_and_return_dataframe, fetch_user_data, convert_to_upper

class TestGetDataAndReturnDataframe(unittest.TestCase):
    @patch('utility.requests.get')
    def test_get_data_and_return_dataframe_success(self, mock_get):
        # Configure the mock response for a successful request
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"userid": 1, "id": 1, "title": "Title 1", "body": "Body 1"},
            {"userid": 2, "id": 2, "title": "Title 2", "body": "Body 2"}
        ]
        mock_get.return_value = mock_response

        # Call the function being tested
        result = get_data_and_return_dataframe('https://example.com/api/data')

        # Verify that the result is a DataFrame
        self.assertIsInstance(result, pd.DataFrame)

        # Verify that the DataFrame contains the expected columns
        expected_columns = ['userid', 'id', 'title', 'body']
        self.assertListEqual(list(result.columns), expected_columns)

        # could add other test assertions


    @patch('utility.requests.get')
    def test_get_data_and_return_dataframe_failure(self, mock_get):
        # Configure the mock response for a failed request
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        # Call the function being tested
        result = get_data_and_return_dataframe('https://example.com/api/data')
        expected_output = "Request failed with a status code other than 200"

        # Verify that we get the expected response when status code is not 200
        self.assertEqual(result, expected_output)

        # could add other test assertions


class TestFetchUserData(unittest.TestCase):
    @patch('utility.sqlite3.connect')
    def test_fetch_user_data_success(self, mock_connect):
        # Configure the mock cursor
        mock_cursor = mock_connect.return_value.cursor.return_value
        mock_cursor.fetchone.return_value = (1, 'Abraham Musa', 'abmusa@example.com', 1)

        # Call the function being tested
        result = fetch_user_data(1)

        # Verify the expected user data
        expected_user = {
            'id': 1,
            'name': 'Abraham Musa',
            'email': 'abmusa@example.com',
            'status': 'active'
        }
        self.assertEqual(result, expected_user)

        # Check if the database connection and cursor were called correctly
        mock_connect.assert_called_once()
        mock_cursor.execute.assert_called_once_with('SELECT * FROM users WHERE id = ?', (1,))
        mock_cursor.close.assert_called_once()
        mock_connect.return_value.close.assert_called_once()



    @patch('utility.sqlite3.connect')
    def test_fetch_user_data_not_found(self, mock_connect):
        # Configure the mock cursor
        mock_cursor = mock_connect.return_value.cursor.return_value
        mock_cursor.fetchone.return_value = None

        # Call the function being tested
        result = fetch_user_data(1)

        # Verify that None is returned when user data is not found
        self.assertEqual(result, 'User record not found')

        # Check if the database connection and cursor were called correctly
        mock_connect.assert_called_once()
        mock_cursor.execute.assert_called_once_with('SELECT * FROM users WHERE id = ?', (1,))
        mock_cursor.close.assert_called_once()
        mock_connect.return_value.close.assert_called_once()



class TestUtilityFunction(unittest.TestCase):
    @patch('utility.mocked_function')
    def test_convert_to_upper(self, mock_external_function):
        # Configure the mock external function
        mock_external_function.return_value = "Mocked result"

        # Call the function being tested
        result = convert_to_upper()

        # Verify the expected result
        expected_result = "MOCKED RESULT"
        self.assertEqual(result, expected_result)

        # Check if the external function was called
        mock_external_function.assert_called_once()