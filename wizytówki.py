from faker import Faker
fake = Faker()

Type_of_contact=input("""Podaj jakiego typu mają być wygenerowane wizytówki:
                        BaseContact - Wprowadź liczę 1
                        BusinessContact - Wprowadź liczbę 2
                        """)

Number_of_Contacts=input("Podaj ilość wizytówek jaka ma zostać wygenerowa: ")

class BaseContact :
    def __init__(self,name,phone_number,e_mail):
        self.name=name
        self.phone_number=phone_number
        self.e_mail=e_mail
        #Variable
        self.label_lenght=len(name)
        
                            
    def __str__(self):
        return f'{self.name} {self.phone_number} {self.e_mail} '
    def contact(self):
        return (f'Wybieram numer prywatny {self.phone_number} i dzwonię do {self.name}')


    
class BusinessContact(BaseContact):
    def __init__(self,company,job,business_phone,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.company=company
        self.job=job
        self.business_phone=business_phone
    def __str__(self):
        return f'{self.name} {self.phone_number} {self.e_mail} {self.company} {self.job} {self.business_phone}'
    
    def contact(self):
        return (f'Wybieram numer służbowy {self.business_phone} i dzwonię do {self.name} z firmy {self.company}')

def create_contacts(a,b):
    if a == 1:
        for i in range (b):
            i=BaseContact(name=fake.name(),phone_number=fake.phone_number(),e_mail=fake.email())
            print(i.contact())
            print(f'Długość imienia i nazwiska (ze spacją) wynosi: {i.label_lenght}')
    elif a == 2:
        for i in range(b):
            i=BusinessContact(name=fake.name(),phone_number=fake.phone_number(),e_mail=fake.email(),company=fake.company(),job=fake.job(),business_phone=fake.phone_number())
            print(i.contact())
            print(f'Długość imienia i nazwiska (ze spacją) wynosi: {i.label_lenght}')
    else:
        print("Nie ma takiego numeru :(")
        
create_contacts(int(Type_of_contact),int(Number_of_Contacts))
