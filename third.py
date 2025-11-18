import math

def je_prvocislo(cislo):
    cislo = int(cislo)
    if cislo <= 1:
        return False
    for i in range(2, cislo):
        if cislo % i == 0:
                return False
    return True
       

def vrat_prvocisla(maximum):
    maximum=int(maximum)
    return [i for i in range (2, maximum + 1) if je_prvocislo(i)] 

        
          
if __name__ == "__main__":
    cislo = input("Zadej maximum:")
    print(je_prvocislo(cislo))
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)