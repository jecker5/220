"""
Name: Joseph Decker
hw11.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


class SalesPerson:

    def __init__(self, employee_id, name):
        self.sales = []
        self.employee_id = employee_id
        self.name = name

    def get_id(self):
        return int(self.employee_id)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        sales = 0
        for i in self.sales:
            sales = sales + i
        return sales

    def get_sales(self):
        return list(self.sales)

    def met_quota(self, quota):
        if self.total_sales() >= quota:
            return True
        else:
            return False

    def compare_to(self, other):
        if other.total_sales > self.total_sales():
            return -1
        else:
            pass
        if other.total_sales < self.total_sales():
            return 1
        else:
            pass
        if other.total_sales == self.total_sales():
            return 0

    def __str__(self):
        return str(self.employee_id + "-" + self.name + ":" + self.total_sales())

