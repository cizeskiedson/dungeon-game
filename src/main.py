import sys
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
def verifica_max(valor, max):
    if(valor > max):
        print("Quantidade de membros na equipe extrapolou o maximo permitido! Repense, e tente novamente.\n")
        sys.exit()

def main():
    ##definir a quantidade maxima de aventureiros
    # por equipe
    facil = 1;
    medio = 2;
    dificil = 3;
    max_aventureiros = {facil: 20, medio: 12, dificil: 6}
    ##escolher quantos aventureiros de cada tipo 
    # o jogador quer ter
    print("Menu Principal\n")

    print("Escolha o modo de jogo, digitando o valor correspondente:\n")
    print("1 - Facil\n")
    print("2 - Medio\n")
    print("3 - Dificil\n")
    dificuldade = int(input("Digite o valor da dificuldade escolhida:\n"))

    print("Hora de escolher seu time de aventureiros!\n")
    print("O numero maximo de membros da sua equipe eh " + str(max_aventureiros[dificuldade]))
    num_aventureiros = {'druida': 0, 'guerreiro': 0, 'mago': 0}
    num_aventureiros['druida'] = int(input("Quantos druidas voce deseja convocar?\n"))
    num_aventureiros['guerreiro'] = int(input("Quantos guerreiros voce deseja convocar?\n"))
    num_aventureiros['mago'] = int(input("Quantos magos voce deseja convocar?\n"))
    qnt_escolhidos = num_aventureiros['druida'] + num_aventureiros['guerreiro'] + num_aventureiros['mago']
    verifica_max(qnt_escolhidos, max_aventureiros[dificuldade])

    
main()
