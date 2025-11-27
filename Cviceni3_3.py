
from Cviceni3_1 import levensteinova_vzdalenost
from Cviceni3_2 import jaccardova_vzdalenost_mnozin


def deduplikace_dotazu(dotazy):
    """
    tato funkce spocita jaccardovu vzdalenost a levensteinovu vzadelnost a vyradi z seznamu dotazy, polozky, ktere budou mit
    jaccardovu vzdalenost mensi nez 0.5 a levensteinovu vzdalenost <= 1
    """
    i = 0
    while i < len(dotazy):
        j = i + 1
        while j < len(dotazy):
            lev = levensteinova_vzdalenost(dotazy[i]["dotaz"], dotazy[j]["dotaz"])
            jac = jaccardova_vzdalenost_mnozin(dotazy[i]["serp"], dotazy[j]["serp"])
            if lev <= 1 or jac < 0.5:
                dotazy.pop(j)
            else:
                j += 1 
        i += 1
    return dotazy

    



if __name__ == "__main__":

    dotaz1 = {
        "dotaz": "seznam",
        "serp": ["https://www.seznam.cz", "https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz", "https://www.google.com"]
    }
    dotaz2 = {
        "dotaz": "seznamka",
        "serp": ["https://www.seznam.cz", "https://www.google.com", "https://www.novinky.cz", "https://www.idnes.cz", "https://www.zpravy.cz", "https://www.tn.cz"]
    }
    dotaz3 = {
        "dotaz": "sesnam",
        "serp": ["https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz"]
    }
    dotaz4 = {
        "dotaz": "google",
        "serp": ["https://www.google.com", "https://maps.google.com", "https://www.gmail.com"]
    }
    print(eduplikace_dotazu([dotaz1, dotaz2, dotaz3, dotaz4]))
