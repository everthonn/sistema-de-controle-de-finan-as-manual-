import pandas as pd
import datetime
import json

with open("gastos-ganho.json", "r", encoding="utf-8") as json_file:
    gastos_ganho = json.load(json_file)

dataDMA = datetime.datetime.now().strftime("%d-%m-%Y")

dataf = pd.DataFrame(gastos_ganho)


def adicionar_gasto():
    print("adicionar uma data diferente da data atual? (s/n)")
    if input().lower() == "s" or "s" in input().lower():
        print("Digite a data no formato dd-mm-aaaa:")
        dia = input("Dia: ")
        mes = input("Mês: ")
        ano = input("Ano: ")
        data = f"{dia}-{mes}-{ano}"
        valor = float(input("Digite o valor do gasto: "))
        categoria = input("Digite a categoria do gasto: ")
        novo_gasto = {"id": (len(gastos_ganho) + 1), "data": data, "categoria": categoria, "valor": -valor}
        gastos_ganho.append(novo_gasto)
        with open("gastos-ganho.json", "w", encoding="utf-8") as json_file:
            json.dump(gastos_ganho, json_file, ensure_ascii=False, indent=4)
        print("Gasto adicionado com sucesso!")
    else :
        valor = float(input("Digite o valor do gasto: "))
        categoria = input("Digite a categoria do gasto: ")
        novo_gasto = {"id": (len(gastos_ganho) + 1), "data": dataDMA, "categoria": categoria, "valor": -valor}
        gastos_ganho.append(novo_gasto)
        with open("gastos-ganho.json", "w", encoding="utf-8") as json_file:
            json.dump(gastos_ganho, json_file, ensure_ascii=False, indent=4)
        print("Gasto adicionado com sucesso!")

def remover_gasto_ganho():
    print("Digite o ID do gasto que deseja remover:")
    id_remover = int(input())
    for gasto in gastos_ganho:
        if gasto["id"] == id_remover:
            gastos_ganho.remove(gasto)
            with open("gastos-ganho.json", "w", encoding="utf-8") as json_file:
                json.dump(gastos_ganho, json_file, ensure_ascii=False, indent=4)
            print(f"Gasto/Ganho com ID {id_remover} removido.")
            return
    print(f"Gasto/Ganho com ID {id_remover} não encontrado.")

def encontrar_gastos_por_categoria():
    categoria_desejada = input("Digite a categoria que deseja buscar: ")
    print(dataf[dataf["categoria"].isin([categoria_desejada])])

def mostrar_todos_gastos():
    print("Todos os gastos registrados:")
    print(dataf)

def mostrar_gastos_por_data():
    dia = input("Digite o dia (dd): ")
    mes = input("Digite o mês (mm): ")
    ano = input("Digite o ano (aaaa): ")
    data_buscar = f"{dia}-{mes}-{ano}"
    print(dataf[dataf["data"].isin([data_buscar])])
    if dataf[dataf["data"].isin([data_buscar])].empty:
        print(f"Nenhum gasto encontrado na data '{data_buscar}'.")

def adicionar_ganho():
    print("adicionar uma data diferente da data atual? (s/n)")
    if input().lower() == "s" or "s" in input().lower():
        print("Digite a data no formato dd-mm-aaaa:")
        dia = input("Dia: ")
        mes = input("Mês: ")
        ano = input("Ano: ")
        data = f"{dia}-{mes}-{ano}"
        valor = float(input("Digite o valor do ganho: "))
        categoria = input("Digite a categoria do ganho: ")
        novo_ganho = {"id": (len(gastos_ganho) + 1), "data": data, "categoria": categoria, "valor": valor}
        gastos_ganho.append(novo_ganho)
        with open("gastos-ganho.json", "w", encoding="utf-8") as json_file:
            json.dump(gastos_ganho, json_file, ensure_ascii=False, indent=4)
        print("Ganho adicionado com sucesso!")
    else :
        valor = float(input("Digite o valor do ganho: "))
        categoria = input("Digite a categoria do ganho: ")
        novo_ganho = {"id": (len(gastos_ganho) + 1), "data": dataDMA, "categoria": categoria, "valor": valor}
        gastos_ganho.append(novo_ganho)
        with open("gastos-ganho.json", "w", encoding="utf-8") as json_file:
            json.dump(gastos_ganho, json_file, ensure_ascii=False, indent=4)
        print("Ganho adicionado com sucesso!")
