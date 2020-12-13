import queue
import sys
import random
### CONSTANTES ###

NUM_AVENTUREIROS_FACIL = 20; NUM_AVENTUREIROS_MEDIO = 12; NUM_AVENTUREIROS_DIFICIL = 6
FACIL = 1; MEDIO = 2; DIFICIL = 3
NUM_MONSTROS_PADRAO = 5

MAGO_NUM_INIMIGOS = 4; MAGO_DANO_TIPO = 'magico'; MAGO_DANO_VALOR = 4
DRUIDA_NUM_INIMIGOS = 3; DRUIDA_DANO_TIPO = 'veneno'; DRUIDA_DANO_VALOR = 5
GUERREIRO_NUM_INIMIGOS = 2; GUERREIRO_DANO_TIPO = 'fisico'; GUERREIRO_DANO_VALOR = 6

DRAGAO_PONTOS_VIDA = 12; DRAGAO_TIPO_RESISTENCIA = 'magico'; DRAGAO_VALOR_RESISTENCIA = 50
MORTO_VIVO_PONTOS_VIDA = 8; MORTO_VIVO_TIPO_RESISTENCIA = 'veneno'; MORTO_VIVO_VALOR_RESISTENCIA = 50
ORC_PONTOS_VIDA = 6; ORC_TIPO_RESISTENCIA = 'fisico'; ORC_VALOR_RESISTENCIA = 50

##################

### VAR GLOBAIS ###

max_aventureiros = {FACIL: NUM_AVENTUREIROS_FACIL, MEDIO: NUM_AVENTUREIROS_MEDIO, DIFICIL: NUM_AVENTUREIROS_DIFICIL} # Número de aventureiros por dificuldade

###################

### EXCEÇÕES ###

class excecaoNumAventureirosUltrapassado(Exception):
    pass

class excecaoNumAventureirosInsuf(Exception):
    pass

class excecaoDificuldadeInvalida(Exception):
    pass

################

### Classes ### 

# Classe Monstro
class Monstro:
   def __init__(self, vida, tipo_resistencia, valor_resistencia):
       self.vida = vida
       self.tipo_resistencia = tipo_resistencia
       self.valor_resistencia = valor_resistencia

# Subclasses de Monstro
class Dragao(Monstro):
    def __init__(self):
        super().__init__(DRAGAO_PONTOS_VIDA, DRAGAO_TIPO_RESISTENCIA, DRAGAO_VALOR_RESISTENCIA)

class MortoVivo(Monstro):
    def __init__(self):
        super().__init__(MORTO_VIVO_PONTOS_VIDA, MORTO_VIVO_TIPO_RESISTENCIA, MORTO_VIVO_VALOR_RESISTENCIA)

class Orc(Monstro):
    def __init__(self):
        super().__init__(ORC_PONTOS_VIDA, ORC_TIPO_RESISTENCIA, ORC_VALOR_RESISTENCIA)


## Classe Aventureiro
class Aventureiro:
    def __init__(self, num_inimigos, tipo_dano, valor_dano):
        self.num_inimigos = num_inimigos
        self.tipo_dano = tipo_dano
        self.valor_dano = valor_dano

#Subclasses de Aventureiro
class Druida(Aventureiro):
    def __init__(self, num_inimigos, tipo_dano, valor_dano):
        super().__init__(DRUIDA_NUM_INIMIGOS, DRUIDA_DANO_TIPO, DRUIDA_DANO_VALOR)

class Mago(Aventureiro):
    def __init__(self, num_inimigos, tipo_dano, valor_dano):
        super().__init__(MAGO_NUM_INIMIGOS, MAGO_DANO_TIPO, MAGO_DANO_VALOR)

class Guerreiro(Aventureiro):
    def __init__(self, num_inimigos, tipo_dano, valor_dano):
        super().__init__(GUERREIRO_NUM_INIMIGOS, GUERREIRO_DANO_TIPO, GUERREIRO_DANO_VALOR)

# Classe andar masmorra
class NivelMasmorra():
    def __init__(self, nivel_atual):
        self.nivel_masmorra = nivel_atual
        self.num_monstros = int(NUM_MONSTROS_PADRAO + (3 * nivel_atual))
        self.fila_monstros = self.preencherFilaMonstros(self.num_monstros)
    
    def preencherFilaMonstros(self, numero_monstros):
        random.seed(numero_monstros)
        fila_monstros = queue.Queue(maxsize = numero_monstros)
        while(fila_monstros.qsize() < numero_monstros):
            num_monstro = random.randrange(1, 4)
            
            if(num_monstro == 1):
                monstro = Dragao()
            elif(num_monstro == 2):
                monstro = Orc()
            else:
                monstro = MortoVivo()
            
            fila_monstros.put(monstro)
        print("Fila com {} monstros criada!".format(fila_monstros.qsize()))
        return fila_monstros


###############

def main():
    ### Definições ###

    ##################

    print("\nMenu Principal\n")
    
    dificuldade_escolhida = selecionarDificuldade()
    time_aventureiros = selecionarTimeAventureiros(dificuldade_escolhida)
    num_aventureiros_restantes = max_aventureiros[dificuldade_escolhida]    
    
    iniciarMasmorra(time_aventureiros, num_aventureiros_restantes)

    
def iniciarMasmorra(time_aventureiros, num_aventureiros_restantes):
    nivel_atual = 1
    while(num_aventureiros_restantes > 0):
        enfrentarNivel(time_aventureiros, num_aventureiros_restantes, nivel_atual)
        nivel_atual += 1

        # PARADA TESTES #
        num_aventureiros_restantes = 0
        #################


def enfrentarNivel(time_aventureiros, num_aventureiros_restantes, nivel_atual):
    nivel = NivelMasmorra(nivel_atual)
    
    

    

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
