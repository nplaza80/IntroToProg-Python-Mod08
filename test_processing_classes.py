# ------------------------------------------------------------------------------- #
# Title: Test Processing Classes Module
# Description: A collection of tests for the processing classes module
# ChangeLog: (Who, When, What)
# NPlaza,08.18.2024,Created Script
# ------------------------------------------------------------------------------- #
import unittest
import tempfile
import json
import data_classes as data
from processing_classes import FileProcessor

class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w+')
        self.temp_file_name = self.temp_file.name
        self.employee_data = []

    def tearDown(self):
        # Clean up and delete the temporary file
        self.temp_file.close()

    def test_read_employee_data_from_file(self):
        # Create some sample data and write it to the temporary file
        sample_data = [
            {"FirstName": "John", "LastName": "Doe", "ReviewDate": "2023-01-01", "ReviewRating": 3},
            {"FirstName": "Alice", "LastName": "Smith", "ReviewDate": "2023-02-01", "ReviewRating": 4},
        ]
        with open(self.temp_file_name, "w") as file:
            json.dump(sample_data, file)

        # Call the read_employee_data_from_file method and check if it returns the expected data
        FileProcessor.read_employee_data_from_file(self.temp_file_name, self.employee_data, data.Employee)

        # Assert that the employee_data list contains the expected employee objects
        self.assertEqual(len(self.employee_data), len(sample_data))
        self.assertEqual(self.employee_data[0].first_name, "John")
        self.assertEqual(self.employee_data[1].review_rating, 4)

    def test_write_employee_data_to_file(self):
        # Create some sample employee objects
        employee1 = data.Employee("John", "Doe", "2023-01-01", 3)
        employee2 = data.Employee("Alice", "Smith", "2023-02-01", 4)
        self.employee_data = [employee1, employee2]

        # Call the write_employee_data_to_file method to write data to the temporary file
        FileProcessor.write_employee_data_to_file(self.temp_file_name, self.employee_data)

        # Read the file and check its contents
        with open(self.temp_file_name, "r") as file:
            file_data = json.load(file)

        # Assert that the file contains the expected data
        self.assertEqual(len(file_data), len(self.employee_data))
        self.assertEqual(file_data[0]["FirstName"], "John")
        self.assertEqual(file_data[1]["ReviewRating"], 4)

if __name__ == '__main__':
    unittest.main()