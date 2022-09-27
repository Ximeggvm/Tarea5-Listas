def main():
    #escribe tu código abajo de esta línea
a=0
repetidor=0
lista=[]
repeticiones=[]
contador=0
veces=int(input())

while contador<veces:
    aa=input()
    lista+=[aa]
    contador=contador+1

for i in lista:
    if i in repeticiones:
        lista.pop(a)
    else:
        repeticiones.append(i)
        a=a+1
        
print(lista)


if __name__=='__main__':
    main()
