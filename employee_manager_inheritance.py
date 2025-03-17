class Employee():
    def __init__(self, name, title, rate_per_hour=None):
        self.name = name
        self.title = title
        self.rate_per_hour = rate_per_hour

    def get_name(self):
        return self.name

    def get_title(self):
        return self.title

    def pay_per_year(self):
        pay = 52 * 8 * 5 * self.rate_per_hour
        return pay
    

class Manager(Employee):
    def __init__(self, name, title, salary, report_list = None):
        super().__init__(name, title)
        self.salary = float(salary)
        if not report_list:
            self.report_list = []
        self.report_list = report_list

    def get_reports(self):
        return self.report_list
    
    def pay_per_year(self, give_bonus=False):
        pay = self.salary
        if give_bonus:
            pay = pay + (0.1 * self.salary)

        return pay

print(dir(Manager))