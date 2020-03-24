def asti(massiv_strok):
    massiv_chisel = []

    for element in massiv_strok:
        massiv_chisel.append(int(element))

    return massiv_chisel

def zadanie_massiva():
    h_file = open("1.txt", "r")
    buf = h_file.read();
    massiv = buf.split(' ')
    massiv_chisel = asti(massiv)
    return massiv_chisel

def zadanie_chisla():
    chislo = int(input())
    return chislo 

def zadanie_peremennyh():
    massiv = zadanie_massiva()
    chislo = zadanie_chisla()
    return massiv,chislo

def super_summa(x,y):
    s = y in x
    return s

def main():
    a,b = zadanie_peremennyh()
    res = super_summa(a,b)
    print(res)

main()
