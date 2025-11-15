import pyautogui
import keyboard
import time
import sys

def auto_click():
    print("Auto-click activo. Posiciona el mouse donde quieras que haga clic.")
    print("Presiona 'S' para detener el script.")
    time.sleep(2)  

    while True:
        pyautogui.click()  
        time.sleep(0.01)   

        if keyboard.is_pressed("s"):
            print("\nAuto-click detenido por el usuario.")
            sys.exit()


def main():
    """Función principal para ejecutar desde CLI o standalone."""
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


if __name__ == "__main__":
    main()

