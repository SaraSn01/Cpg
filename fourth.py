def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    typ = figurka["typ"]
    r1, s1 = figurka["pozice"]
    r2, s2 = cilova_pozice
    if not (1 <= r2 <= 8 and 1 <= s2 <= 8):
        return False
    if cilova_pozice in obsazene_pozice:
        return False
    dr = r2 - r1
    ds = s2 - s1

    if typ == "pěšec":
        if dr == 1 and ds == 0:
            return True
        if r1 == 2 and dr == 2 and ds == 0 and (r1 + 1, s1) not in obsazene_pozice:
            return True
        return False
    
    if typ == "jezdec":
        if (abs(dr), abs(ds)) in [(1, 2), (2,1)]:
            return True
        return False
    
    if typ == "věž":
        if r1 == r2:
            step = 1 if ds > 0 else -1
            s = s1 + step
            while s != s2:
                if (r1, s) in obsazene_pozice:
                    return False
                s += step
            return True
        if s1 == s2:
            step = 1 if dr > 0 else -1
            r = r1 + step
            while r != r2:
                if (r, s1) in obsazene_pozice:
                    return False
                r += step
            return True
        return False
    
    if typ == "střelec":
        if abs(dr) == abs(ds):
            step_r = 1 if dr > 0 else -1
            step_s = 1 if ds > 0 else -1
            r = r1 + step_r
            s = s1 + step_s
            while (r, s) != (r2, s2):
                if (r, s) in obsazene_pozice:
                    return False
                r += step_r
                s += step_s
            return True
        return False
    
    if typ == "dáma":
        return je_tah_mozny({"typ":"věž", "pozice":(r1, s1)}, cilova_pozice, obsazene_pozice) or je_tah_mozny({"typ": "střelec", "pozice": (r1, s1)}, cilova_pozice, obsazene_pozice)
    
    if typ == "král":
        return max(abs(dr), abs(ds)) == 1
    return False

if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice)) 
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  
    print(je_tah_mozny(pesec, (5, 2), obsazene_pozice))  
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice)) 
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice)) 
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice)) 
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))