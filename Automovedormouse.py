import pyautogui
import keyboard
import random
import time
import sys

def mover_mouse():
    print("Movimiento automático iniciado.")
    print("Presiona 'S' para detener el script.")
    time.sleep(2)  
    width, height = pyautogui.size()  

    while True:
        
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)

        pyautogui.moveTo(x, y, duration=0.1)  
        
        if keyboard.is_pressed("s"):
            print("\nMovimiento detenido por el usuario.")
            sys.exit()


def main():
    """Función principal para ejecutar desde CLI o standalone."""
    print("--- Mouse Mover Infinito ---")
    print("El mouse se moverá por toda la pantalla.")
    print("Presiona 'S' en cualquier momento para detener.")
    time.sleep(2)

    try:
        mover_mouse()
    except Exception as e:
        print(f"\nOcurrió un error: {e}")
    finally:
        print("Script finalizado.")


if __name__ == "__main__":
    main()

