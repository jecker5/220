from sales_person import SalesPerson


class SalesForce:

    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        self.sales_people = []
        infile = open(file_name, "r")
        for line in infile:
            self.sales_people.append(line)
            self.sales_people = [x[:-1] for x in self.sales_people]

    def quota_report(self, quota):
        quota_list = []
        if SalesPerson.met_quota:
            quota_list.append(SalesPerson.__str__)
        return quota_list

    def top_seller(self):
        seller_list = []
        acc = 0
        for i in self.sales_people:
            if i.total_sales() > acc:
                acc = i.total_sales()
                seller_list = [i]
            elif i.total_sales() == acc:
                seller_list.append(i)
        return seller_list

    def individual_sales(self, employee_id):
        name = SalesPerson.get_name(employee_id)
        return name

    def get_sale_frequencies(self):
        data = {}
        for person in self.sales_people:
            for sale in person.get_sales():
                if sale in data:
                    data[sale] += 1
                else:
                    data[sale] = 1
            return data


