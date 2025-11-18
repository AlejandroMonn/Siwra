import pyautogui
import keyboard
import time
import sys

def auto_click():
    print("Iniciando el auto click... espera un momento")
    time.sleep(1.5)

    print("Ubica el mouse donde quieres que haga clic")
    print("Para detener todo presiona la tecla S")
    time.sleep(2)

    # Bucle principal del autoclick
    while True:
        try:
            pyautogui.click()
            # Sleep un poquito para no saturar tanto (se podría hacer mejor)
            time.sleep(0.02)
        except:
            print("Hubo un problema al intentar hacer clic")
            break

        # Revisión manual y poco eficiente de la tecla
        if keyboard.is_pressed("s"):
            print(" presionaste S, deteniendo...")
            time.sleep(0.5)
            sys.exit()


def main():
    print("==== AUTO CLICKEADOR BÁSICO ====")
    print("Este programa hará clics automáticos")
    print("Presiona S cuando quieras salir\n")
    time.sleep(1)

    try:
        auto_click()
    except Exception as error:
        print("Algo salio mal:", error)
        print("intentando cerrar el programa...")
    finally:
        print("El script termino")


if __name__ == "__main__":
    main()



