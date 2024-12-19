import pyautogui
import keyboard
import random
import time

"""
    autoclick fácil de usar e com randomização.
"""

# criado por: DogeDaVala

def random_number():
    """
    Gera um número aleatório para o click.
    Evita detecção por sistemas anti-ban.

    Retorna:
        Um número float aleatório entre 0.1 e 0.5.
    """
    return random.uniform(0.1, 0.5)

def macro():
    """
    Cria o macro de clique.
    """
    paused = False    
    while True:
        if keyboard.is_pressed("F2"):
            paused = not paused
            print("Pausado" if paused else "Despausado")
            time.sleep(0.2)  # Aguarda um tempo para evitar múltiplos pressionamentos rápidos.
            
        if not paused:
            # Gera um novo número aleatório a cada iteração.
            random_delay = random_number()
            pyautogui.press("space")
            time.sleep(random_delay)
            print(f"Executando o programa... Tempo de delay: {random_delay:.2f} segundos.")
        
        else:
            time.sleep(0.1)  # Aguarda um pouco quando pausado.

macro()  # Chama a função macro sem passar argumentos
