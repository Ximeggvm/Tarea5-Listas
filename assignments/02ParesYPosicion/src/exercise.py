def main():
numeros=[]
veces=int(input())
contador=0

while contador<veces:
    aa=input()
    numeros+=[aa]
    contador=contador+1
for i in range (veces):
    valor=int(numeros[i])%2
    if valor==0:
        print('pos', str(i)+str(','),'valor',(numeros[i]))
        
if __name__=='__main__':
    main()
