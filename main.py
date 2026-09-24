# 1. Apresentação / Título do programa
print("====================================")
print("       CALCULADORA DE VIAGEM        ")
print("====================================")
print()


def ler_numero(mensagem):
    """Pede um número ao usuário e só aceita valores positivos."""
    while True:
        try:
            valor = float(input(mensagem))
            if valor <= 0:
                print("Digite um valor maior que zero.")
                continue
            return valor
        except ValueError:
            print("Valor inválido. Digite um número, por exemplo 12.5")


def formatar_horas(horas_decimais):
    """Converte horas decimais (ex: 2.5) em texto 2h 30min."""
    horas = int(horas_decimais)
    minutos = int(round((horas_decimais - horas) * 60))
    if minutos == 60:
        horas += 1
        minutos = 0
    return f"{horas}h {minutos:02d}min"


# 2. Entrada de dados
distancia = ler_numero("Distância da viagem (km): ")
litros = ler_numero("Combustível no tanque (litros): ")
consumo = ler_numero("Consumo do carro (km/l): ")
preco = ler_numero("Preço do combustível (R$/litro): ")
velocidade = ler_numero("Velocidade média estimada (km/h): ")
reserva_km = ler_numero("Reserva de segurança desejada (km): ")

ida_e_volta = input("Calcular ida e volta? (s/n): ").strip().lower()
if ida_e_volta == "s":
    distancia_total = distancia * 2
    tipo_viagem = "ida e volta"
else:
    distancia_total = distancia
    tipo_viagem = "somente ida"

# 3. Cálculos avançados
autonomia = litros * consumo
combustivel_necessario = distancia_total / consumo
combustivel_com_reserva = (distancia_total + reserva_km) / consumo
diferenca_litros = litros - combustivel_necessario
custo_viagem = combustivel_necessario * preco
custo_com_reserva = combustivel_com_reserva * preco
custo_por_km = preco / consumo
tempo_horas = distancia_total / velocidade
autonomia_apos_viagem = autonomia - distancia_total
litros_apos_viagem = litros - combustivel_necessario
abastecer_litros = max(0, combustivel_com_reserva - litros)
custo_abastecer = abastecer_litros * preco

# 4. Relatório
print()
print("====================================")
print("           RESULTADO                ")
print("====================================")
print(f"Tipo de viagem: {tipo_viagem}")
print(f"Distância total: {distancia_total:.1f} km")
print(f"Autonomia atual: {autonomia:.1f} km")
print(f"Tempo estimado: {formatar_horas(tempo_horas)}")
print()
print(f"Combustível necessário: {combustivel_necessario:.2f} L")
print(f"Combustível com reserva: {combustivel_com_reserva:.2f} L")
print(f"Custo da viagem: R$ {custo_viagem:.2f}")
print(f"Custo por km: R$ {custo_por_km:.2f}")
print()

# 5. Tomada de decisão
if autonomia >= distancia_total + reserva_km:
    print("Pode viajar com segurança. Há combustível suficiente, incluindo a reserva.")
    print(f"Sobra após a viagem: {litros_apos_viagem:.2f} L ({autonomia_apos_viagem:.1f} km).")
elif autonomia >= distancia_total:
    print("Dá para chegar ao destino, mas a reserva de segurança não está garantida.")
    print(f"Sobra após a viagem: {litros_apos_viagem:.2f} L ({autonomia_apos_viagem:.1f} km).")
    print(f"Para manter a reserva, abasteça mais {abastecer_litros:.2f} L (R$ {custo_abastecer:.2f}).")
else:
    falta_litros = abs(diferenca_litros)
    falta_km = distancia_total - autonomia
    print("Atenção! Você precisa abastecer antes de viajar.")
    print(f"Faltam {falta_litros:.2f} L para completar a viagem ({falta_km:.1f} km).")
    print(f"Para viajar com reserva, abasteça {abastecer_litros:.2f} L (R$ {custo_abastecer:.2f}).")
    print(f"Custo total estimado com reserva: R$ {custo_com_reserva:.2f}.")
