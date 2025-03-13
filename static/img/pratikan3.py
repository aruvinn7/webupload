EMPLOYEE_DATA_LIST = []  
list_division = ['it', 'hr', 'finance', 'marketing']
list_position = ['staff', 'senior', 'manager']
list_data = {
    'name': ['andi', 'budi', 'citra', 'dewi', 'eka', 'fajar', 'gita', 'hendra', 'indah', 'joko'],
    'position': ['staff', 'senior', 'manager', 'staff', 'senior', 'manager', 'staff', 'senior', 'manager', 'staff'],
    'division': ['it', 'finance', 'marketing', 'hr', 'it', 'finance', 'marketing', 'hr', 'it', 'finance'],
    'years_of_service': [2, 7, 10, 1, 4, 6, 3, 5, 8, 2],
    'working_days': [21, 24, 17, 19, 20, 25, 26, 28, 25, 23],
}

users = {
    'admin': 'admin123',  
    'user': 'user123'    
}     

# Login

    # max_attempts = 3 
    # attempts = 0 

    # while attempts < max_attempts: 
    #     username = input("Enter username: ").strip() 
    #     password = input("Enter password: ").strip() 
        
    #     if username in users or users[username] == password: 
    #         print("Login successful!")
    #         return True
    #     else :
    #         attempts += 1 
    #         print(f"Invalid username or password. {max_attempts - attempts} attempts remaining.")
    # return False


# Validate Input

    # while True:
    #     try:
    #         if input_type == 'str':
    #             value = input(prompt).strip().lower()
    #             if not value:
    #                 raise ValueError("Input cannot be empty!")
    #             if valid_values and value not in valid_values:
    #                 raise ValueError(f"Input must be one of: {', '.join(valid_values)}")
    #             return value
            
    #         elif input_type == 'int':
    #             value = int(input(prompt))
    #             if min_value is not None and value < min_value:
    #                 raise ValueError(f"Input cannot be less than {min_value}")
    #             if max_value is not None and value > max_value:
    #                 raise ValueError(f"Input cannot be more than {max_value}")
    #             return value
            
    #     except ValueError as e:
    #         if str(e).startswith("Input"):
    #             print(f"Error: {str(e)}")
    #         else:
    #             print("Error: Input must be a valid number!")

## Input Employee Data

    # global list_division, list_position

    # employee_data = {}
    # employee_data['name']= validate_input("Enter employee name: ", 'str')
    # employee_data['position']= validate_input(
    #     "Enter position (staff/senior/manager): ",
    #     'str',
    #     valid_values=list_position
    # )
    # employee_data['division']= validate_input(
    #     "Enter division (it/hr/finance/marketing): ",
    #     'str',
    #     valid_values=list_division
    # )
    # employee_data["years_of_service"]= validate_input(
    #     "Enter years of service: ",
    #     'int',
    #     min_value=0,
    #     max_value=50
    # )
    # employee_data["working_days"]= validate_input(
    #     "Enter working days: ",
    #     'int',
    #     min_value=0,
    #     max_value=30
    # )
    # return employee_data

# Calculate Base Salary

    # if position == 'staff':
    #     return 4000000
    # elif position == 'senior':
    #     return 6000000
    # else:  # manager
    #     return 10000000

## Calculate Service Bonus

    # if years_of_service >= 5:
    #     if position == 'manager':
    #         return base_salary * 0.2
    #     elif position == 'senior':
    #         return base_salary * 0.15
    #     else:
    #         return base_salary * 0.1
    # else:
    #     return base_salary * 0.05

## Calculate Division Allowance

    # if division == 'it':
    #     return base_salary * 0.15
    # elif division == 'finance':
    #     return base_salary * 0.1
    # else:
    #     return base_salary * 0.08

## Calculate Deduction

    # if working_days < 20:
    #     if years_of_service < 2:
    #         return base_salary * 0.1
    #     else:
    #         return base_salary * 0.05
    # return 0

## Calculate Salary

## Calculate Salary Stats

## Main Program

    # for i in range(len(EMPLOYEE_DATA_LIST)):
    #     result = calculate_salary(EMPLOYEE_DATA_LIST[i])
    #     EMPLOYEE_DATA_LIST[i].update(result)

    # budget = validate_input("Enter this month's budget: ", 'int', min_value=0)
    # DIVISION_BUDGET = {
    #     'it': budget * 0.3, 
    #     'hr': budget * 0.15,
    #     'finance': budget * 0.10,
    #     'marketing': budget * 0.45, 
    # }

    # print("\nAverage salary by position:")
    # position_salary = {}
    # for employee in EMPLOYEE_DATA_LIST:
    #     position = employee['position']
    #     if position not in position_salary:
    #         position_salary[position] = []
    #     position_salary[position].append(employee['total_salary'])
    
    # for position, salary_list in position_salary.items():
    #     average = sum(salary_list) / len(salary_list)
    #     print(f"{position}: {average:,.0f}")
    
    # print("\nAverage salary by division:")
    # division_salary = {}
    # for employee in EMPLOYEE_DATA_LIST:
    #     division = employee['division']
    #     if division not in division_salary:
    #         division_salary[division] = []
    #     division_salary[division].append(employee['total_salary'])
    
    # for division, salary_list in division_salary.items():
    #     average = sum(salary_list) / len(salary_list)
    #     print(f"{division}: {average:,.0f}")

    # highest_salary, lowest_salary = calculate_salary_stats(EMPLOYEE_DATA_LIST)
    # print("\n=== Salary Statistics ===")
    # if highest_salary and lowest_salary:
    #     print(f"Highest Salary: {highest_salary['total_salary']:,.0f} - {highest_salary['name']} ({highest_salary['position']}, {highest_salary['division']})")
    #     print(f"Lowest Salary: {lowest_salary['total_salary']:,.0f} - {lowest_salary['name']} ({lowest_salary['position']}, {lowest_salary['division']})")

    # print("\n| No  | Name           | Position        | Division       | Years of Service | Working Days | Total Salary  |")
    # print("=" * 110)
    # for idx, employee in enumerate(EMPLOYEE_DATA_LIST, start=1):
    #     print(f"| {idx:<3} | {employee['name']:<15} | {employee['position']:<15} | {employee['division']:<15} | "
    #           f"{employee['years_of_service']:<16} | {employee['working_days']:<12} | {employee['total_salary']:12,.0f} |")

