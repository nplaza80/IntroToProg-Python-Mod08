# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Starter files
# Description: A collection of classes for managing the application
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# ------------------------------------------------------------------------------------------------- #

import unittest
from data_classes import Person, Employee


class TestPerson(unittest.TestCase):

    def test_person_init(self):  # Tests the constructor
        person = Person("John", "Doe")
        self.assertEqual(person.first_name, "John")
        self.assertEqual(person.last_name, "Doe")

    def test_person_invalid_name(self):  # Test the first and last name validations
        with self.assertRaises(ValueError):
            person = Person("123", "Doe")
        with self.assertRaises(ValueError):
            person = Person("John", "123")

    def test_person_str(self):  # Tests the __str__() magic method
        person = Person("John", "Doe")
        self.assertEqual(str(person), "John,Doe")


class TestEmployee(unittest.TestCase):  # Corrected class name

    def test_employee_init(self):  # Tests the constructor
        employee = Employee("Alice", "Smith", "1900-01-01", 3)
        self.assertEqual(employee.first_name, "Alice")
        self.assertEqual(employee.last_name, "Smith")
        self.assertEqual(employee.review_date, "1900-01-01")
        self.assertEqual(employee.review_rating, 3)

    def test_employee_invalid_data(self):  # Corrected test method name
        with self.assertRaises(ValueError):
            employee = Employee("Bob", "Johnson", "invalid_review_date", "Invalid review_rating")

    def test_employee_str(self):  # Corrected test method name
        employee = Employee("Eve", "Brown", "1900-01-01", 3)  # Tests the __str__() magic method
        self.assertEqual(str(employee), "Eve,Brown,1900-01-01,3")  # Adjusted to the expected string format


if __name__ == '__main__':
    unittest.main()
