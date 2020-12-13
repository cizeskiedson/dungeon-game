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

class excecaoAcaoInvalida(Exception):
    pass

################

### Classes ### 

# Classe Monstro
class Monstro:
    def __init__(self, vida, tipo_resistencia, valor_resistencia):
        self.vida = vida
        self.tipo_resistencia = tipo_resistencia
        self.valor_resistencia = valor_resistencia
    
    def tomarDano(self, tipo_dano, valor_dano):
        if(self.tipo_resistencia == tipo_dano): # resiste ao dano 
            self.vida -= ((self.valor_resistencia / 100) * valor_dano)
        else:
            self.vida -= valor_dano
        if(self.vida < 0):
            self.vida = 0

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


# Classe Aventureiro
class Aventureiro:
    def __init__(self, num_inimigos, tipo_dano, valor_dano):
        self.num_inimigos = num_inimigos
        self.tipo_dano = tipo_dano
        self.valor_dano = valor_dano

# Subclasses de Aventureiro
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
        fila_monstros = []
        while(len(fila_monstros) < numero_monstros):
            num_monstro = random.randrange(1, 4)
            
            if(num_monstro == 1):
                monstro = Dragao()
            elif(num_monstro == 2):
                monstro = Orc()
            else:
                monstro = MortoVivo()
            
            fila_monstros.append(monstro)
        print("Fila com {} monstros criada!".format(len(fila_monstros)))
        return fila_monstros

    def removeMortos(self):
        for i in range(len(self.fila_monstros)):
            if(self.fila_monstros[i].vida <= 0):
                print("Monstro {} morto, HP = {}".format(self.fila_monstros[i].__class__.__name__, self.fila_monstros[i].vida))
                self.fila_monstros.pop(i)        
                return 1
        return -1

    def mostrarFilaMonstros(self):
        print("########################## FILA DE MONSTROS ##########################")
        for i in range(len(self.fila_monstros) - 1, -1, -1):
            print("Pos: {}  \tTipo: {}\t\tVida: {}  \tResist: {}".format(i + 1, self.fila_monstros[i].__class__.__name__, self.fila_monstros[i].vida, self.fila_monstros[i].tipo_resistencia))
        print("######################################################################")

###############

def main():
    print("\nMenu Principal\n")
    
    dificuldade_escolhida = selecionarDificuldade()
    time_aventureiros = selecionarTimeAventureiros(dificuldade_escolhida)
    num_aventureiros_restantes = max_aventureiros[dificuldade_escolhida]    
    iniciarMasmorra(time_aventureiros, num_aventureiros_restantes)
    sys.exit()
    
def iniciarMasmorra(time_aventureiros, num_aventureiros_restantes):
    nivel_atual = 1
    while(num_aventureiros_restantes > 0):
        input("\nINICIANDO NÍVEL {} DA MASMORRA! Pressione ENTER para continuar!\n".format(nivel_atual))
        num_aventureiros_restantes = enfrentarNivel(time_aventureiros, num_aventureiros_restantes, nivel_atual)
        if(num_aventureiros_restantes <= 0):
            break
        input("\nFIM DO NÍVEL {} DA MASMORRA! PARABÉNS! Pressione ENTER para continuar".format(nivel_atual))
        nivel_atual += 1
    if(nivel_atual == 1):
        print("FIM DE JOGO! Infelizmente você não conseguiu vencer nenhum nível da masmorra! Mais sorte na próxima!")
    else:
        print("FIM DE JOGO! Parabéns, você conseguiu chegar até o nível {} da masmorra!".format(nivel_atual))

def enfrentarNivel(time_aventureiros, num_aventureiros_restantes, nivel_atual):
    nivel = NivelMasmorra(nivel_atual)
    while(len(nivel.fila_monstros) > 0) and (num_aventureiros_restantes > 0):
        while True:
            try:
                nivel.mostrarFilaMonstros()
                print("Time atual: {} Druidas, {} Magos e {} Guerreiros".format(time_aventureiros['druida'], time_aventureiros['mago'], time_aventureiros['guerreiro']))
                print("1 - Atacar usando um DRUIDA ({} de dano {} nos {} primeiros inimigos)".format(DRUIDA_DANO_VALOR, DRUIDA_DANO_TIPO, DRUIDA_NUM_INIMIGOS))    
                print("2 - Atacar usando um MAGO ({} de dano {} nos {} primeiros inimigos)".format(MAGO_DANO_VALOR, MAGO_DANO_TIPO, MAGO_NUM_INIMIGOS))
                print("3 - Atacar usando um GUERREIRO ({} de dano {} nos {} primeiros inimigos)".format(GUERREIRO_DANO_VALOR, GUERREIRO_DANO_TIPO, GUERREIRO_NUM_INIMIGOS))           
                acao_num = int(input("ESCOLHA SUA AÇÃO: "))
                if(acao_num != 1 and acao_num != 2 and acao_num != 3): raise excecaoAcaoInvalida # Ação escolhida invalida
                if(acao_num == 1):  # Tenta atacar com um DRUIDA
                    if(time_aventureiros['druida'] <= 0): raise excecaoNumAventureirosInsuf # Num de druidas insuficiente
                    Atacar('druida', nivel.fila_monstros) 
                    time_aventureiros['druida'] -= 1 # Remove o druida que atacou do grupo de aventureiros

                elif(acao_num == 2): # Tenta atacar com um MAGO
                    if(time_aventureiros['mago'] <= 0): raise excecaoNumAventureirosInsuf # Num de magos insuficiente
                    Atacar('mago', nivel.fila_monstros) 
                    time_aventureiros['mago'] -= 1 # Remove o mago que atacou do grupo de aventureiros
                
                elif(acao_num == 3): # Tenta atagar com um GUERREIRO
                    if(time_aventureiros['guerreiro'] <= 0): raise excecaoNumAventureirosInsuf # Num de guerreiros insuficiente
                    Atacar('guerreiro', nivel.fila_monstros)
                    time_aventureiros['guerreiro'] -= 1 # Remove o guerreiro que atacou do grupo de aventureiros
                
                num_aventureiros_restantes -= 1

                while True:                         # Remove os inimigos mortos da lista de inimigos
                    if(nivel.removeMortos() == -1):
                        break
                print()
                break

            except excecaoAcaoInvalida:
                input("Ação inválida, selecione uma ação válida. Pressione ENTER para tentar novamente")
                print()
            except excecaoNumAventureirosInsuf:
                input("Numero de aventureiros desse tipo insuficiente para realizar ação. Pressione ENTER para tentar novamente")
                print()  
            except ValueError:
                input("Ação inválida, selecione uma ação válida. Pressione ENTER para tentar novamente")
                print()
    return num_aventureiros_restantes      

def Atacar(classe_aventureiro, fila_monstros):
    if(classe_aventureiro == 'druida'):
        for i in range(DRUIDA_NUM_INIMIGOS):
            if(len(fila_monstros) > i):
                fila_monstros[i].tomarDano(DRUIDA_DANO_TIPO, DRUIDA_DANO_VALOR)
    elif(classe_aventureiro == 'mago'):
        for i in range(MAGO_NUM_INIMIGOS):
            if(len(fila_monstros) > i):
                fila_monstros[i].tomarDano(MAGO_DANO_TIPO, MAGO_DANO_VALOR)
    elif(classe_aventureiro == 'guerreiro'):
        for i in range(GUERREIRO_NUM_INIMIGOS):
            if(len(fila_monstros) > i):
                fila_monstros[i].tomarDano(GUERREIRO_DANO_TIPO, GUERREIRO_DANO_VALOR)

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
            
            print("Time atual: {} Druidas, {} Magos e {} Guerreiros. (Aventureiros restantes: {})".format(num_aventureiros['druida'], num_aventureiros['mago'], num_aventureiros['guerreiro'], aventureiros_restantes))
            num_aventureiros['druida'] =  int(input("Insira o numero de druidas que deseja convocar: "))
            aventureiros_restantes = aventureiros_restantes - num_aventureiros['druida']
            if(aventureiros_restantes < 0): raise excecaoNumAventureirosUltrapassado 

            print("Time atual: {} Druidas, {} Guerreiros e {} Magos. (Aventureiros restantes: {})".format(num_aventureiros['druida'], num_aventureiros['guerreiro'], num_aventureiros['mago'], aventureiros_restantes))
            num_aventureiros['mago'] =  int(input("Insira o numero de magos que deseja convocar: "))
            aventureiros_restantes -= num_aventureiros['mago']
            if(aventureiros_restantes < 0): raise excecaoNumAventureirosUltrapassado


            print("Time atual: {} Druidas, {} Guerreiros e {} Magos. (Aventureiros restantes: {})".format(num_aventureiros['druida'], num_aventureiros['guerreiro'], num_aventureiros['mago'], aventureiros_restantes))
            num_aventureiros['guerreiro'] = int(input("Insira o numero de guerreiros que deseja convocar: "))
            aventureiros_restantes -= num_aventureiros['guerreiro']
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
