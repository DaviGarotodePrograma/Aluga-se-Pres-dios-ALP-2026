x = float(input("Digite o primeiro número!: "))
y = float(input("Digite o segundo número!: "))
def calculadora(x, y, op):
    if op == "+":
        return f"O resultado é: {x+y}" 
    if op == "-":
        return f"O resultado é: {x-y}" 
    if op == "*":
        return f"O resultado é: {x*y}" 
    if op == "/":
        return f"O resultado é: {x/y}" 
op = input("Digite o operador da conta!: ")
print(calculadora(x, y, op))
