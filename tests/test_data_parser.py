import os
import pandas as pd
import requests

from Parsing import DataParser


class TestGetData:
    def test_get_data_response_code(self):
        parser = DataParser("QA", number_of_pages=1)
        response = requests.get(parser.url)
        assert response.status_code == requests.codes.ok

    def test_get_data_return_type(self):
        parser = DataParser("QA", number_of_pages=1)
        response = parser.get_data()
        assert isinstance(response, list)

    def test_get_data_return_value(self):
        parser = DataParser("QA", number_of_pages=1)
        response = parser.get_data()[0]
        assert response["items"][0]["name"].startswith("QA")


class TestSaveToCsv:
    def test_save_to_csv_file_exists(self):
        parser = DataParser("QA", number_of_pages=1)
        parser.save_to_csv()
        assert os.path.exists("QA.csv"), "CSV file does not exist"

    def test_save_to_csv_file_not_empty(self):
        parser = DataParser("QA", number_of_pages=1)
        parser.save_to_csv()
        df = pd.read_csv("QA.csv")
        assert not df.empty, "CSV file is empty"
