import os

tarefas = []
program = bool(True)

def limpar_terminal():
    sistema = os.name
    if sistema == 'nt':  
        os.system('cls')
    else:  
        os.system('clear')

def divisor():
    return print("............................................")

def imprimirLista(tarefas):
    iteracao = 0
    divisor()
    print('Lista de tarefas:')
    if len(tarefas) == 0:
        print("- Não há tarefas")
    else:
        for valor in tarefas:
            print(f'{iteracao} - {valor} ')
            iteracao += 1
    divisor()

def adicionarTarefa(tarefas):
    tarefa = input(str('Digite a tarefa que você deseja adicionar: - '))
    tarefas.append(f'{tarefa} (pendente)')

def removerTarefa(tarefas):
    if len(tarefas) == 0:
        return print("Não há tarefas para remover")
    else:
        numeroRemover = int(input("Digite o número da tarefa que você deseja remover: "))
        if numeroRemover > len(tarefas) - 1:
            return "Escolha um número válido para remoção"
        else: 
            del tarefas[numeroRemover]

def marcarConcluidas(tarefas):
    posicao = int(input("Qual tarefa você deseja marcar como concluída? "))
    string_atual = tarefas[posicao]
    if "(pendente)" in string_atual and "(concluída)" not in string_atual:
        string_modificada = string_atual.replace("(pendente)", "(concluída)")
        tarefas[posicao] = string_modificada
    else:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print('A tarefa já está marcada como concluída')
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

def marcarPendentes(tarefas):
    posicao = int(input("Qual tarefa você deseja marcar como pendente? "))
    string_atual = tarefas[posicao]
    if "(concluída)" in string_atual and "(pendente)" not in string_atual:
        string_modificada = string_atual.replace("(concluída)", "(pendente)")
        tarefas[posicao] = string_modificada
    else:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print('A tarefa já está marcada como pendente')
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

def imprimirOpcoes():
    return print("""1 - Adicionar tarefa
2 - Remover tarefar
3 - Marcar como concluída
4 - Marcar como pendente""")



while program == True:
    log = ""
    limpar_terminal()
    imprimirLista(tarefas)
    imprimirOpcoes()
    escolha = int(input("- "))
    match escolha:
        case 1:
            adicionarTarefa(tarefas)
        case 2:
            removerTarefa(tarefas)
        case 3:
            marcarConcluidas(tarefas)
        case 4:
            marcarPendentes(tarefas)


