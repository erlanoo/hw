class Company:
        def __init__(self, company_bank, company_name):
                self.company_bank = company_bank
                self.company_name = company_name

class Person(Company):
        def __init__(self, company_bank, company_name, first_name, last_name, salary):
                super().__init__(company_bank, company_name)
                self.first_name = first_name
                self.last_name = last_name
                self.salary = salary
        def person_info(self):
                print(f"""  
                First_name : {self.first_name} 
                Last_name : {self.last_name}  
                Salary : {self.salary}$
                """)
        def get_salary(self):
                if self.company_bank < self.salary:
                        print("У банка недостаточно средств!")
                else:
                        b = self.company_bank - self.salary
                        print(f'Остаток средств компании {b}')



Alex = Person(30000, "Walmart", "Alex", "Smith", 29500)
John = Person(30000, "Walmart", "John", "Tailor", 29000)

Alex.get_salary()
John.get_salary()
Alex.person_info()
John.person_info()