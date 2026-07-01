import datetime

hoje = datetime.datetime.now()
ano = int(input("Que ano voce nasceu?"))
print(hoje.year, ano, hoje.year-ano)
