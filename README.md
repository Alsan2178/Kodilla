# Kodilla
Funkacja, która sprawdza czy dane słowo jest palindromem.

Wewnątrz fukcji tworzę podział za pomocą wyrażania if, na dwie pętle while, jedna dotyczy wyrażeń o parzystej liczbię liter i druga o nieparzystej.

Pętle sprawdzają czy pokoleji; pierwsza i ostatnia, druga i przedostatnia itd. są takie same, do momentu aż, iteracja znajdzie się na dwóch środkowych literach w przypadku
słow o parzystej liczbie liter, albo na środkowej literze w przypadku o nieprzystej liczbie. Jeżeli któreś porównanie nie jest takie samo funkcja zwraca wyrażenie boolean False,
a gdy przliczy do końca wyrzuca boolean True.
