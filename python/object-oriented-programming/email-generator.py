class Email:
    company="dlsud.edu.ph"

    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname

    def __str__(self):
        return f"{self.fname[0]}{self.lname}@{Email.company}.com".lower()

def addname():
        fname=input("Enter your first name: ")
        lname=input("Enter your last name: ")
        return Email(fname, lname)

def display(genemail):
    print("===============Generated Email===============")
    for x, range in enumerate(genemail, 1):
        print(f"{x}. {range}")

print("\t\tWelcome to Email Generator App!")
print("=============================================")

genemail=[]
while True:
    name = input("Add name?: ")
    if name.lower()=='yes':
        genemail.append(addname())
    elif name.lower()=='no':
        display(genemail)
        break