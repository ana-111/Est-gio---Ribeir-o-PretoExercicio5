import time

# Funções para simular os interruptores e lâmpadas
def ligar_interruptor(nome):
    print(f"{nome} ligado")

def desligar_interruptor(nome):
    print(f"{nome} desligado")

def verificar_lampada():
    # Simula a verificação do estado das lâmpadas
    # Retorna um dicionário com o estado das lâmpadas
    return {
        "Lâmpada 1": "acesa",  # O nome da lâmpada corresponde ao interruptor B
        "Lâmpada 2": "quente",  # O nome da lâmpada corresponde ao interruptor A
        "Lâmpada 3": "fria"     # O nome da lâmpada corresponde ao interruptor C
    }

# Função principal para simular a descoberta dos interruptores
def descobrir_interruptores():
    # Passo 1: Simulação
    ligar_interruptor("Interruptor A")
    time.sleep(5)  # Espera para simular o tempo em que a lâmpada esquenta
    desligar_interruptor("Interruptor A")

    ligar_interruptor("Interruptor B")

    # Passo 2: Simulação da verificação
    estado_lampadas = verificar_lampada()

    # Determina qual lâmpada é controlada por qual interruptor
    for lampada, estado in estado_lampadas.items():
        if estado == "acesa":
            interruptor = "Interruptor B"
        elif estado == "quente":
            interruptor = "Interruptor A"
        elif estado == "fria":
            interruptor = "Interruptor C"
        print(f"{lampada} é controlada pelo {interruptor}")

# Executa a função principal
descobrir_interruptores()
