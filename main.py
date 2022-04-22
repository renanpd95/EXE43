import os

name = input("Qual o nome do funcionario: ")
sal = float(input("Qual o salario do funcionario: R$"))
os.system('clear')
imp = 0.73 * sal

print("Nome: ",name)
print("Salario liquido sem imposto: R$",sal)
print("Salario liquido com imposto: R$",imp)
