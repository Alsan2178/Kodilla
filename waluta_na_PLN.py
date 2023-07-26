import requests
import csv
from flask import Flask, request, render_template


app=Flask(__name__)


response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
rates=data[0]['rates']

with open('plik.csv', 'w', encoding='utf-8') as waluty_csv:
    csvwriter = csv.writer(waluty_csv,delimiter=';')
    csvwriter.writerow(["currency","code","bid","ask"])
    for i in range (0,len(rates)):
        csvwriter.writerow([rates[i].get("currency"), rates[i].get("code"), rates[i].get("bid"), rates[i].get("ask")])

file = open("plik.csv", "r",encoding='utf-8')
data2 = list(csv.reader(file, delimiter=';'))
file.close()


@app.route('/', methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        data = request.form
        currency = data.get('currency')
        quantity = data.get('quantity')
        if currency == "dolar amerykański":
           wynik = float(data2[2][2])*float(quantity)
           return f"Za {quantity} dolarów amerykańskich musisz zapłacić {round(wynik, 2)} ZŁ"
        elif currency == "dolar australijski":
            wynik = float(data2[4][2])*float(quantity)
            return f"Za {quantity} dolarów australijskich musisz zapłacić {round(wynik, 2)} ZŁ"
        elif currency == "dolar kanadyjski":
            wynik = float(data2[6][2])*float(quantity)
            return f"Za {quantity} dolarów kanadyjskich musisz zapłacić {round(wynik, 2)} ZŁ"
        elif currency == "euro":
            wynik = float(data2[8][2])*float(quantity)
            return f"Za {quantity} euro musisz zapłacić {round(wynik, 2)} ZŁ"
        elif currency == "forint (Węgry)":
            wynik = float(data2[10][2])*float(quantity)
            return f"Za {quantity} forintów węgierskich musisz zapłacić {round(wynik, 2)} ZŁ"
        elif currency == "frank szwajcarski":
            wynik = float(data2[12][2])*float(quantity)
            return f"Za {quantity} franków szwajcarskich musisz zapłacić {round(wynik, 2)} ZŁ"
        elif currency == "funt szterling":
            wynik = float(data2[14][2])*float(quantity)
            return f"Za {quantity} funtów szterlingów musisz zapłacić {round(wynik, 2)} ZŁ"
        elif currency == "jen (Japonia)":
            wynik = float(data2[16][2])*float(quantity)
            return f"Za {quantity} jenów japońskich musisz zapłacić {round(wynik, 2)} ZŁ"
        elif currency == "korona czeska":
            wynik = float(data2[18][2])*float(quantity)
            return f"Za {quantity} koron czeskich musisz zapłacić {round(wynik, 2)} ZŁ"
        elif currency == "korona duńska":
            wynik = float(data2[20][2])*float(quantity)
            return f"Za {quantity} koron duńskich musisz zapłacić {round(wynik, 2)} ZŁ"
        elif currency == "korona norweska":
            wynik = float(data2[22][2])*float(quantity)
            return f"Za {quantity} koron norweskich musisz zapłacić {round(wynik, 2)} ZŁ"
        elif currency == "korona szwedzka":
            wynik = float(data2[24][2])*float(quantity)
            return f"Za {quantity} koron szwedzkich musisz zapłacić {round(wynik, 2)} ZŁ"
        elif currency == "SDR (MFW)":
            wynik = float(data2[26][2])*float(quantity)
            return f"Za {quantity} SDR (MFW) musisz zapłacić {round(wynik, 2)} ZŁ"
    return render_template("currency_form.html")


if __name__ == "__main__":
    app.run(debug=True)