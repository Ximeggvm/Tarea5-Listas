def main():
    #escribe tu código abajo de esta línea
valor=1
numeros=[]
pares=0
impares=0
while valor==1:
    n=input()
    if n=='*':
        veces=len(numeros)
        valor=0
        for i in range (veces):
            valor=int(numeros[i])%2
            if valor==0:
                pares=pares+1
            if valor==1:
                impares=impares+1
        print('Pares='+str(pares))
        print('Impares='+str(impares))
        
    numeros +=[n]
    

if __name__=='__main__':
    main()
