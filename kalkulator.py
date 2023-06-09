import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')

logging.info("""

Podaj jakie chcesz wykonać działanie: 
Dodawanie - wpisz numer 1 
Odejmowanie - wpisz numer 2  
Mnożenie - wpisz numer 3 
Dzielenie - wpisz numer 4 """)
operation=int(input())

first_number=float(input("Podaj pierwszą liczę:"))
second_number=float(input("Podaj drugą liczbę:"))

def calculator(parametr,number,number2):
    result=0
    if parametr==1:
        result=number+number2
        logging.debug("Dodaje {} do {}".format(str(number),str(number2)))
        return result
    elif parametr==2:
        result=number-number2
        logging.debug("Odejmuje {} od {}".format(str(number),str(number2)))
        return result
    elif parametr==3:
        result=number*number2
        logging.debug("Mnożę {} przez {}".format(str(number),str(number2)))
        return result
    elif parametr==4:
        result=number/number2
        logging.debug("Dzielę {} przez {}".format(str(number),str(number2)))
        return result
    else:
        return False

logging.debug("Wynik operacji to: %s" %str(calculator(operation,first_number,second_number)))
