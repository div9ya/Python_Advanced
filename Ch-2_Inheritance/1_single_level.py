class company:

    def __init__(self,company_name):
        self.company_name=company_name

    def info(self):
        print(f"Company Name: {self.company_name}")
        return f"Company Name: {self.company_name}"
        

class employee(company):

    def __init__(self,employee_name,company_name):

        self.employee_name=employee_name
        self.company_name=company_name

    def employee_info(self):
        response=company.info(self)
        print(f"The Employee: {self.employee_name} , {response}")


obj=employee("John Doe","Tech Soutions")
obj.employee_info()

