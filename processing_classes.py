# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Starter files
# Description: A collection of classes for managing the application
# ChangeLog: (Who, When, What)
# NPlaza,8.15.2024,Created Script
# ------------------------------------------------------------------------------------------------- #

import json
from data_classes import Employee  # Import the Employee class

class FileProcessor:
    """
    A collection of processing layer functions that work with JSON files

    ChangeLog: (Who, When, What)
    NPlaza,8.15.2024,Created Class
    """

    @staticmethod
    def read_employee_data_from_file(file_name: str, employee_data: list, employee_type: Employee) -> list:
        """ This function reads data from a JSON file and loads it into a list of employee objects

        ChangeLog: (Who, When, What)
        NPlaza,8.15.2024,Created Function

        :param file_name: string data with name of file to read from
        :param employee_data: list of employee objects to be filled with file data
        :param employee_type: a reference to the Employee class
        :return: list of employee objects
        """
        try:
            with open(file_name, "r") as file:
                list_of_dictionary_data = json.load(file)  # Load function returns a list of dictionary rows.
                for employee in list_of_dictionary_data:
                    employee_object = employee_type()  # Create an instance of Employee
                    employee_object.first_name = employee["FirstName"]
                    employee_object.last_name = employee["LastName"]
                    employee_object.review_date = employee["ReviewDate"]
                    employee_object.review_rating = employee["ReviewRating"]
                    employee_data.append(employee_object)
        except FileNotFoundError:
            raise FileNotFoundError("The file must exist before running this script!")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("The file contains invalid JSON format.")
        except Exception as e:
            raise Exception(f"There was a non-specific error: {str(e)}")
        return employee_data

    @staticmethod
    def write_employee_data_to_file(file_name: str, employee_data: list) -> None:
        """ This function writes data to a JSON file from a list of employee objects

        ChangeLog: (Who, When, What)
        NPlaza,8.15.2024,Created Function

        :param file_name: string data with the name of the file to write to
        :param employee_data: list of employee objects to be written to the file
        :return: None
        """
        try:
            list_of_dictionary_data: list[dict] = []  # Specify that it's a list of dictionaries
            for employee in employee_data:  # Convert List of employee objects to a list of dictionary rows.
                employee_json: dict = {
                    "FirstName": employee.first_name,
                    "LastName": employee.last_name,
                    "ReviewDate": employee.review_date,
                    "ReviewRating": employee.review_rating
                }
                list_of_dictionary_data.append(employee_json)

            with open(file_name, "w") as file:
                json.dump(list_of_dictionary_data, file, indent=4)  # Adding indent for better readability of the JSON file
        except TypeError:
            raise TypeError("Please check that the data is in a valid JSON format")
        except PermissionError:
            raise PermissionError("Please check the data file's read/write permissions")
        except Exception as e:
            raise Exception(f"There was a non-specific error: {str(e)}")