#Ex 1
import datetime as date

def dias(data_inicial,data_final):
    idade =(data_inicial-data_final)/365.25
    return idade

data_inicial=date.date.today()
dia=int(input('Insira seu dia de nascimento: '))
mes=int(input('Insira seu mês de nascimento: '))
ano=int(input('Insira seu ano de nascimento: '))
data_final=date.date(ano,mes,dia)

resultado=dias(data_inicial,data_final)
print('Sua idade é: ',resultado,'anos')





