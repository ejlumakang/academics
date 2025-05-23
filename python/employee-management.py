class Manager:
    def __init__(self, name, department, post="Manager" ):
        self.name = name
        self.department = department
        self.post = post
        
    def post_details(self):
        if self.department.lower() == "hr":
            bsalary = 30000
        else:
            bsalary = 25000
        hrent = 10000
        transport = 5000
        salary=self.salary(bsalary, hrent, transport)
            
        print(f"The post of {self.name} is {self.post}\nThe salary is {salary}")
            
    def salary(self, bsalary, hrent, transport):    
        salary = bsalary+hrent+transport
        return salary

class Clerk():
    def __init__(self, name, post="Clerk"):
        self.name = name
        self.post = post
        
    def post_details(self):
        bsalary = 10000
        transport = 2000
        salary = self.salary(bsalary, transport)
        print(f"The post of {self.name} is {self.post}\nThe salary is {salary}")
            
    def salary(self, bsalary, transport):    
        salary = bsalary+transport
        return salary

mr = Manager("Juan", "HR")
mr1 = Manager("Maria", "accounting")
ck = Clerk("Pedro")

emp = [mr, mr1, ck]
for x in emp:
    print()
    x.post_details()
            



            
            
            
            
        