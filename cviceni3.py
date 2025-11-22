

def levensteinova_vzdalenost(dotaz1, dotaz2):
    """
    Levensteinova vzdalenost říka, jak jsou 2 řetězce rozdílné, pokud jsou stejné je Levensteinova vzdalenost 0,
    pro řetězce "čas" a "čaj" je Levensteinova vzdalenost 1 (liší se v 1 písmenu)
    """

    levenstein = 0 
    i = 0
    min_len = min(len(dotaz1), len(dotaz2))
    while i < min_len:
        if dotaz1[i] != dotaz2[i]:
            levenstein += 1
        i += 1
        levenstein += abs(len(dotaz1) - len(dotaz2))
        return levenstein

if __name__ == "__main__":

    query1 = "seznam"
    query2 = "seznamka"
    query3 = "sesnam"
    query4 = "seznam"

    print(levensteinova_vzdalenost(query1, query2))
    print(levensteinova_vzdalenost(query2, query3))
    print(levensteinova_vzdalenost(query1, query3))

    print(levensteinova_vzdalenost(query1, query4))

    

