#Ex 5 
try:
    raio_circulo=float(input('Digite o valor do raio: '))
    pi=float(3.1416)
    area = float((raio_circulo**2)*pi)
    comprimento = float((raio_circulo*pi)*2)
    print('Area :',round(area,2))
    print('Comprimento: ',round(comprimento,2))

except:
    print('Inserir um valor numérico')


 


