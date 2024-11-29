import random

valor_aleatorio = random.randint(1, 10)
acertou = False

# Você sabe o que o código/jogo faz. O cliente/Jogador não, então sempre bom deixar claro nessas situações
print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número secreto entre 1 e 10.")

# Em loops simples, o uso de while not é mais comum e deixa o código mais limpo/legível
while not acertou:
    # O try/except é uma boa prática para capturar exceções (como letras ao invés de números) 
    # e evitar que o programa quebre
    try:
        chute = int(input('Digite um valor de 1 a 10: '))
        
        if chute > valor_aleatorio:
            print('Chutou Alto')
        elif chute < valor_aleatorio:
            print('Chutou Baixo')
        else:
            acertou = True
            # Isso que usei é uma FString, uma boa e dinâmica formatação de strings
            print(f'Parabéns, você acertou! O número secreto era {valor_aleatorio}.')
    except ValueError:
        # Captura inputs que não são números inteiros
        print("Entrada inválida! Por favor, digite um número inteiro entre 1 e 10.")