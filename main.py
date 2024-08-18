# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08
# Description: Main application file
# ChangeLog: (Who, When, What)
# NPlaza,8.14.2024,Created Script
# ------------------------------------------------------------------------------------------------- #
import presentation_classes as pres
import processing_classes as proc
import data_classes as dc  # Importing the Employee class

# Data -------------------------------------------- #
FILE_NAME: str = 'EmployeeRatings.json'

MENU: str = '''
---- Employee Ratings ------------------------------
  Select from the following menu:
    1. Show current employee rating data.
    2. Enter new employee rating data.
    3. Save data to a file.
    4. Exit the program.
--------------------------------------------------
'''

employees: list = []  # a table of employee data
menu_choice = ''

# Beginning of the main body of this script
try:
    employees = proc.FileProcessor.read_employee_data_from_file(file_name=FILE_NAME,
                                                                employee_data=employees,
                                                                employee_type=dc.Employee) # Now correctly referencing the Employee class
except FileNotFoundError:
    print(f"File {FILE_NAME} not found. Starting with an empty employee list.")
except Exception as e:
    pres.IO.output_error_messages(e)

# Repeat the follow tasks
while True:
    pres.IO.output_menu(menu=MENU)

    menu_choice = pres.IO.input_menu_choice()

    if menu_choice == "1":  # Display current data
        try:
            pres.IO.output_employee_data(employee_data=employees)
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    elif menu_choice == "2":  # Get new data (and display the change)
        try:
            employees = pres.IO.input_employee_data(employee_data=employees,
                                                    employee_type=dc.Employee)  # Correct reference to Employee class
            pres.IO.output_employee_data(employee_data=employees)
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    elif menu_choice == "3":  # Save data in a file
        try:
            proc.FileProcessor.write_employee_data_to_file(file_name=FILE_NAME, employee_data=employees)
            print(f"Data was saved to the {FILE_NAME} file.")
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    elif menu_choice == "4":  # End the program
        break  # out of the while loop

print("Program Ended")
