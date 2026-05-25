class company:

    def __init__(self,company_name):
        self.company_name=company_name

    def info(self):
        print(f"Company Name: {self.company_name}")
        return f"Company Name: {self.company_name}"
        
class client_company:

    def __init__(self,client_company_name):

        self.client_company_name=client_company_name

    def info(self):
        print(f"The Client Company: {self.client_company_name} ")
        return f"The Client Company: {self.client_company_name} "
    
class employee(company,client_company):

    def __init__(self,employee_name,client_company_name,company_name):

        self.employee_name=employee_name
        self.client_company_name=client_company_name
        self.company_name=company_name

    def info(self):
        response1=company.info(self)
        response2=client_company.info(self)
        print(f"The Employee: {self.employee_name} , {response1} , {response2}")


obj=employee("John Doe","Client Company","Tech Soutions")  
obj.info()      