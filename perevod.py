p=int(input("p="))
Np=int(input(f"N{p}="))
k=int(1)
N10=int(0)
while  Np!=0:
    N10+= (Np %10)*k
    k=k*p
    Np= Np//10
print(f"N10={N10}")