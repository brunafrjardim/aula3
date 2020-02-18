#Ex 3
import random as rd
quantidade_lista=int(input('Digite o número de itens que a lista deve ter: '))
lista=[]
linha=1
if quantidade_lista<=0:
    print('O número de itens da lista não pode ser igual ou menor que 0')
else:
    while linha<= quantidade_lista:
        lista.append(rd.randrange(0,100))
        linha+=1
    print('Essa é a lista',lista)
    print('Maior número: ',max(lista))
    print('Menor número: ',min(lista))

