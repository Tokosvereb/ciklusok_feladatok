def elsofeladat(szam1):
    i = 1
    while i < szam1:
        if i == (szam1-1):
            print(i)
        else:
            print(i,end=',')   
        i+=1

def masodikfeladat(szam2):
    i = 1
    osszeg = 0
    while i <= szam2:
        if szam2 % i == 0:
            print(i) 
            osszeg += i
        i+=1
    print(osszeg)

def harmadikfeladat(szam3, szam4):
    while szam3 <= szam4:
        print(szam3, end=" ")
        szam3 += 2

def negyedikfeladat()

    