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

    def info(self):
        response=company.info(self)
        print(f"The Employee: {self.employee_name} , {response}")

class contractor(company):

    def __init__(self,contractor_name,company_name):

        self.contractor_name=contractor_name
        self.company_name=company_name

    def info(self):
        response=company.info(self)
        print(f"The Contractor: {self.contractor_name} , {response}")


# if same name then look for closest member 

obj=employee("John Doe","Tech Soutions")
obj.info()

obj2=contractor("Jane Smith","Tech Solutions")
obj2.info()