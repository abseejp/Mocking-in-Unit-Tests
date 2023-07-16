import unittest
from unittest.mock import patch, Mock
import pandas as pd
from utility import get_data_and_return_dataframe

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

