import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s')

first_number=input("Podaj pierwszą liczę:")
second_number=input("Podaj drugą liczbę:")

print(type(first_number))

def calculator(number,number2):
    result=0
    result=number+number2
    return result

pop=calculator(first_number,second_number)

print(pop)
