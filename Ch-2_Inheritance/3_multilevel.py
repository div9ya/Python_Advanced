class company:

    def __init__(self,company_name):
        self.company_name=company_name

    def info(self):
        print(f"Company Name: {self.company_name}")
        return f"Company Name: {self.company_name}"
    

class manager(company):

    def __init__(self,manager_name,company_name):

        self.manager_name=manager_name
        self.company_name=company_name

    def info(self):
        response=company.info(self)
        print(f"The Manager: {self.manager_name} , {response}")
        return f"The Manager: {self.manager_name} , {response}"

class employee(manager):

    def __init__(self,employee_name,manager_name,company_name):

        self.employee_name=employee_name
        self.manager_name=manager_name
        self.company_name=company_name

    def info(self):
        response=manager.info(self)
        print(f"The Employee: {self.employee_name} , {response}")        


obj=employee("John Doe","Jane Smith","Tech Soutions")
obj.info()