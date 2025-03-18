# Open close principle

# Open for extension, but closed for modification

# Open close principle uses polymorphism

class Manager:
    billable = 0
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def show_info(self):
        print(f"{self.name} is a Manager.")

class Programmer:
    def __init__(self, name, billable):
        self.name = name
        self.billable = billable

    def show_info(self):
        print(f"{self.name} is a Programmer.")

class Designer:
    def __init__(self, name, billable, tool):
        self.name = name
        self.billable = billable
        self.tool = tool

    def show_info(self):
        print(f"{self.name} is a Designer.")

def show_employee_info(employee_list):
    for e in employee_list:
        e.show_info()

def show_billable_hourse(employee_list):
    billable = 0
    for e in employee_list:
        billable += e.billable

    print(f"Total billable :{billable}")
        
employees = [
    Manager("Vera", "IT"),
    Programmer("Tejas", 50),]

show_employee_info(employees)
show_billable_hourse(employees)