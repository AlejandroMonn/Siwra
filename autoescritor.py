import pyautogui
import keyboard
import time
import sys

def algoritmo_escritura():
    letras = "ABC"

    while True:
        # Escribir las letras sin saturar el driver
        pyautogui.write(letras, interval=0.001)

        # Borrar las letras correctamente
        pyautogui.press("backspace", presses=len(letras), interval=0.001)

        # Detener con S
        if keyboard.is_pressed("s"):
            print("\nScript detenido por el usuario.")
            sys.exit()

if __name__ == "__main__":
    print("--- Auto Escritor Sin Saturación ---")
    print("Haz clic en el editor donde se escribirán las letras.")
    print("Presiona 'S' en cualquier momento para detener.")
    time.sleep(2)

    try:
        algoritmo_escritura()
    except Exception as e:
        print(f"\nOcurrió un error: {e}")
    finally:
        print("Script finalizado.")
