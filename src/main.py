import sys
### CONSTANTES ###

NUM_AVENTUREIROS_FACIL = 20; NUM_AVENTUREIROS_MEDIO = 12; NUM_AVENTUREIROS_DIFICIL = 6
FACIL = 1; MEDIO = 2; DIFICIL = 3

##################

### VAR GLOBAIS ###

max_aventureiros = {FACIL: NUM_AVENTUREIROS_FACIL, MEDIO: NUM_AVENTUREIROS_MEDIO, DIFICIL: NUM_AVENTUREIROS_DIFICIL} # Número de aventureiros por dificuldade

###################

class excecaoNumAventureirosUltrapassado(Exception):
    pass

class excecaoNumAventureirosInsuf(Exception):
    pass

class excecaoDificuldadeInvalida(Exception):
    pass

# ## Classe Monstro
# class Monstro:
#     def __init__(self, vida):
#         self.vida = vida

# ##Subclasses de Monstro
# class Dragao(Monstro):

# class MortoVivo(Monstro):

# class Orc(Monstro):

# #Classe Aventureiro
# class Aventureiro:
#     def __init__(self, ):


# #Subclasses de Aventureiro
# class Druida(Aventureiro):

# class Mago(Aventureiro):

# class Guerreiro(Aventureiro):

def main():
    ### Definições ###

    ##################

    print("\nMenu Principal\n")
    
    dificuldade_escolhida = selecionarDificuldade()
    time_aventureiros = selecionarTimeAventureiros(dificuldade_escolhida)

    print("Agora só continuar!")

def selecionarDificuldade():
    while True:
        try:
            print("Escolha a dificuldade de jogo (Isso definirá a quantidade total de herois que poderá ser utilizada)")
            print("1 - Facil (20 heróis)  2 - Medio (12 heróis)  3 - Dificil (6 heróis)")
            dificuldade = int(input("Digite o valor da dificuldade correspondente: "))
            
            if(dificuldade != 1 and dificuldade != 2 and dificuldade != 3): raise excecaoDificuldadeInvalida
            return dificuldade

        except excecaoDificuldadeInvalida:
            input("ERRO: Dificuldade inválida, escolha entre 1, 2 ou 3! Pressione ENTER para tentar novamente ")
            print()
        except ValueError:
            input("ERRO: Entrada inválida! Pressione ENTER para tentar novamente ")
            print()

def selecionarTimeAventureiros(dificuldade):
    while True:
        try:
            print("\nHora de escolher seu time de aventureiros! O numero maximo de membros da sua equipe é " + str(max_aventureiros[dificuldade]) + "!")

            aventureiros_restantes = max_aventureiros[dificuldade]
            num_aventureiros = {'druida': 0, 'guerreiro': 0, 'mago': 0}
            
            print("Time atual: {} Druidas, {} Guerreiros e {} Magos. (Aventureiros restantes: {})".format(num_aventureiros['druida'], num_aventureiros['guerreiro'], num_aventureiros['mago'], aventureiros_restantes))
            
            num_aventureiros['druida'] =  int(input("Insira o numero de druidas que deseja convocar: "))
            aventureiros_restantes = aventureiros_restantes - num_aventureiros['druida']
            if(aventureiros_restantes < 0): raise excecaoNumAventureirosUltrapassado 

            print("Time atual: {} Druidas, {} Guerreiros e {} Magos. (Aventureiros restantes: {})".format(num_aventureiros['druida'], num_aventureiros['guerreiro'], num_aventureiros['mago'], aventureiros_restantes))
            num_aventureiros['guerreiro'] = int(input("Insira o numero de guerreiros que deseja convocar: "))
            aventureiros_restantes -= num_aventureiros['guerreiro']
            if(aventureiros_restantes < 0): raise excecaoNumAventureirosUltrapassado
            
            print("Time atual: {} Druidas, {} Guerreiros e {} Magos. (Aventureiros restantes: {})".format(num_aventureiros['druida'], num_aventureiros['guerreiro'], num_aventureiros['mago'], aventureiros_restantes))
            num_aventureiros['mago'] =  int(input("Insira o numero de magos que deseja convocar: "))
            aventureiros_restantes -= num_aventureiros['mago']
            if(aventureiros_restantes < 0): raise excecaoNumAventureirosUltrapassado

            if(aventureiros_restantes > 0): raise excecaoNumAventureirosInsuf

            break
        except excecaoNumAventureirosInsuf:
            input("Número de aventureiros insuficiente, pressione ENTER para começar novamente ")
            print()
        except excecaoNumAventureirosUltrapassado:
            input("Número de aventureiros ultrapassou o limite estabelecido pela dificuldade, pressione ENTER para começar novamente ")
            print()
        except ValueError:
            input("Insira um inteiro válido! Pressione ENTER para começar novamente")
            print()

    return num_aventureiros     

main()
