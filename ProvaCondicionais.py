
limite_velocidade = 80
velocidade = input(int("Qual a sua velocidade? "))

if velocidade > limite_velocidade:

    valor_multa = (velocidade - limite_velocidade) * 20.0

    print(f"Você excedeu o limite de velocidade {limite_velocidade} km/h.")

    print(f"Você foi multado em R${valor_multa:.2f}")

else:
    print("Velocidade dentro do limite permitido.")