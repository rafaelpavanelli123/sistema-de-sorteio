import random

total_sorteios = 0
historico_acertos = []  

def sortear_numeros():
    """Sorteia 6 números únicos entre 1 e 60 e devolve a lista ordenada."""
    numeros = []
    while len(numeros) < 6:
        n = random.randint(1, 60)
        if n not in numeros:
            numeros.append(n)
    numeros.sort()
    return numeros

def fazer_aposta_manual():
    print("\n--- Fazer Aposta ---")
    print("Escolha 6 números entre 1 e 60.")
    aposta = []
    while len(aposta) < 6:
        n = int(input(f"Número {len(aposta)+1} de 6: "))
        if n < 1 or n > 60:
            print(">> Número fora do intervalo (1 a 60). Tente novamente.")
        elif n in aposta:
            print(">> Você já escolheu esse número. Tente outro.")
        else:
            aposta.append(n)
    aposta.sort()
    return aposta

def aposta_surpresinha():
    return sortear_numeros()

def conferir_aposta(aposta, sorteio):
    acertos = []
    for n in aposta:
        if n in sorteio:
            acertos.append(n)
    return acertos

def classificar_premio(qtd_acertos):
    if qtd_acertos == 6:
        return "SENA  ===> VOCÊ É MILIONÁRIO! 🎉"
    elif qtd_acertos == 5:
        return "QUINA ===> Bom prêmio!"
    elif qtd_acertos == 4:
        return "QUADRA ===> Você ganhou um prêmio!"
    else:
        return "Não premiado. Mais sorte na próxima!"

def jogar():
    global total_sorteios

    print("\n--- Nova Aposta ---")
    print("1 - Escolher meus números")
    print("2 - Surpresinha (números aleatórios)")
    escolha = int(input("Opção: "))

    if escolha == 1:
        aposta = fazer_aposta_manual()
    elif escolha == 2:
        aposta = aposta_surpresinha()
        print(f"Sua surpresinha: {aposta}")
    else:
        print("Opção inválida.")
        return

    print("\nSorteando os números da Mega-Sena...")
    sorteio = sortear_numeros()

    print(f"\nNúmeros sorteados: {sorteio}")
    print(f"Sua aposta:        {aposta}")

    acertos = conferir_aposta(aposta, sorteio)
    print(f"\nVocê acertou {len(acertos)} número(s): {acertos}")
    print(f"Resultado: {classificar_premio(len(acertos))}")

    total_sorteios += 1
    historico_acertos.append(len(acertos))

def simular_varias_apostas():
    global total_sorteios

    print("\n--- Simulação de Apostas ---")
    qtd = int(input("Quantas apostas surpresinha você quer simular? "))

    if qtd <= 0:
        print("Quantidade inválida.")
        return

    melhor = 0
    for i in range(qtd):
        aposta = aposta_surpresinha()
        sorteio = sortear_numeros()
        acertos = conferir_aposta(aposta, sorteio)
        historico_acertos.append(len(acertos))
        total_sorteios += 1
        if len(acertos) > melhor:
            melhor = len(acertos)

    print(f"\nSimulação concluída! {qtd} apostas realizadas.")
    print(f"Melhor resultado nessa simulação: {melhor} acerto(s).")

def mostrar_estatisticas():
    print("\n--- Estatísticas ---")
    if total_sorteios == 0:
        print("Nenhum sorteio realizado ainda.")
        return

    print(f"Total de sorteios realizados: {total_sorteios}")

    soma = 0
    for a in historico_acertos:
        soma += a
    media = soma / len(historico_acertos)

    print(f"Média de acertos por aposta: {media:.2f}")
    print(f"Melhor resultado até agora:  {max(historico_acertos)} acerto(s)")

    sena = 0
    quina = 0
    quadra = 0
    for a in historico_acertos:
        if a == 6:
            sena += 1
        elif a == 5:
            quina += 1
        elif a == 4:
            quadra += 1

    print(f"\nPremiações conquistadas:")
    print(f"  Sena:   {sena}")
    print(f"  Quina:  {quina}")
    print(f"  Quadra: {quadra}")


def menu():
    print("\n========================================")
    print("        SISTEMA MEGA-SENA")
    print("========================================")
    print("1 - Fazer uma aposta")
    print("2 - Simular várias apostas (surpresinha)")
    print("3 - Ver estatísticas")
    print("0 - Sair")
    print("========================================")

print("Bem-vindo(a) ao Sistema Mega-Sena!")

opcao = -1
while opcao != 0:
    menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        jogar()
    elif opcao == 2:
        simular_varias_apostas()
    elif opcao == 3:
        mostrar_estatisticas()
    elif opcao == 0:
        print("\nObrigado por jogar! Boa sorte da próxima vez!")
    else:
        print("Opção inválida.")
