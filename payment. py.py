class Employee:

  def _init_(self, employee_id, name):
    self.employee_id = employee_id
    self.name = name

  def calculate_payroll(self):
    raise NotImplementedError("Employee subclass must implement calculate_payroll()")


class SalaryEmployee(Employee):

  def _init_(self, employee_id, name, weekly_salary):
    super()._init_(employee_id, name)
    self.weekly_salary = weekly_salary

  def calculate_payroll(self):
    return self.weekly_salary


class HourlyEmployee(Employee):

  def _init_(self, employee_id, name, hours_worked, hourly_rate):
    super()._init_(employee_id, name)
    self.hours_worked = hours_worked
    self.hourly_rate = hourly_rate

  def calculate_payroll(self):
    return self.hours_worked * self.hourly_rate


class CommissionEmployee(SalaryEmployee):

  def _init_(self, employee_id, name, weekly_salary, commission):
    super()._init_(employee_id, name, weekly_salary)
    self.commission = commission

  def calculate_payroll(self):
    return super().calculate_payroll() + self.commission


# Example usage
# Salary employee
salary_emp = SalaryEmployee(1, "marion nyongesa", 11000)
print(f"{salary_emp.name}'s weekly payroll: ${salary_emp.calculate_payroll():.2f}")

# Hourly employee
hourly_emp = HourlyEmployee(2, "jacky Kwamboka", 100, 20)
print(f"{hourly_emp.name}'s weekly payroll: ${hourly_emp.calculate_payroll():.2f}")

# Commission employee
commission_emp = CommissionEmployee(3, "Jude Mayor", 500, 600)
print(f"{commission_emp.name}'s weekly payroll: ${commission_emp.calculate_payroll():.2f}")
