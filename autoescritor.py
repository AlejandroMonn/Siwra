import pyautogui
import keyboard
import time
import sys

def algoritmo_escritura():
    letras = "AbC"
    print("Iniciando escritura automática..")

    while True:
        try:
            pyautogui.write(letras, interval=0.002)
            time.sleep(0.001)
            pyautogui.press("backspace", presses=len(letras), interval=0.002)
        except:
            print("Algo falló al escribir, pero sigo intentando")
            time.sleep(0.3)

        if keyboard.is_pressed("s"):
            print("\nOk, el usuario pidió detener")
            sys.exit()


def main():
    print("--- Auto Escritor Básico ---")
    print("Haz clic en el lugar donde quieras que escriba")
    print("Presiona S para detener el script")
    time.sleep(2)

    try:
        algoritmo_escritura()
    except Exception as e:
        print("Hubo un error:", e)
    finally:
        print("Script terminado.")


if __name__ == "__main__":
    main()


