import pyautogui
import keyboard
import random
import time
import sys

def mover_mouse():
    print("Iniciando el movimiento automático del mouse...")
    print("Recuerda que puedes presionar S para detener todo")
    time.sleep(2)

    pantalla = pyautogui.size()
    ancho = pantalla[0]
    alto = pantalla[1]

    while True:
        # Genero coordenadas aleatorias
        x = random.randint(0, ancho - 1)
        y = random.randint(0, alto - 1)

        try:
            pyautogui.moveTo(x, y, duration=0.12)
        except:
            print("Hubo un pequeño error moviendo el mouse, pero sigo.¡..")
            time.sleep(0.2)

        # Revisión manual
        if keyboard.is_pressed("s"):
            print("\nOk, detuviste el scrip")
            sys.exit()


def main():
    print("--- Movimiento Automático basico ---")
    print("El mouse se moverá por toda la pantalla aleatoriamente")
    print("Presiona S en cualquier momento para frenar")
    time.sleep(2)

    try:
        mover_mouse()
    except Exception as err:
        print("\nError inesperado:", err)
    finally:
        print("Script terminado")


if __name__ == "__main__":
    main()
