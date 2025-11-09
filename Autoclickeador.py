import pyautogui
import keyboard
import time
import sys

def auto_click():
    print("Auto-click activo. Posiciona el mouse donde quieras que haga clic.")
    print("Presiona 'S' para detener el script.")
    time.sleep(2)  # tiempo para que muevas el mouse al sitio deseado

    while True:
        pyautogui.click()  # clic izquierdo
        time.sleep(0.01)   # velocidad del clic (reduce a 0.001 si quieres súper rápido)

        if keyboard.is_pressed("s"):
            print("\nAuto-click detenido por el usuario.")
            sys.exit()


if __name__ == "__main__":
    print("--- Auto Clicker Loop Infinito ---")
    print("Haz clic en la ventana donde quieras usar el click.")
    print("Presiona 'S' en cualquier momento para detener.")
    time.sleep(2)

    try:
        auto_click()
    except Exception as e:
        print(f"\nOcurrió un error: {e}")
    finally:
        print("Script finalizado.")
