# 1. Apresentação / Título do programa
print("====================================")
print("       CALCULADORA DE VIAGEM        ")
print("====================================")
print() # Essa linha vazia serve apenas para dar um espaço visual
# 2. Entrada de dados
distancia = float(input("Distância da viagem (km): "))
litros = float(input("Combustível no tanque (litros): "))
consumo = float(input("Consumo do carro (km/l): "))
# 3. Cálculo
autonomia = litros * consumo
print("\nSua autonomia atual é de:", autonomia, "km")
# 4. Tomada de decisão
if autonomia >= distancia:
    print("Pode viajar! Você tem combustível suficiente.")
else:
    print("Atenção! Você precisa abastecer antes de viajar.")