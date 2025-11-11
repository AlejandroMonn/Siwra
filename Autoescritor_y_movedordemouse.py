import pyautogui
import keyboard
import random
import time
import sys

frases = [
    "Hola, esto es una prueba.",
    "Automatización combinada: teclado + mouse.",
    "Mensaje de prueba."
]

escribir_interval = 0.003
entre_frases = 0.25
mouse_move_duration = 0.06
mouse_wait = 0.03


def combinado():
    print("Iniciando automatización (mouse + teclado).")
    print("P = Pausar | R = Reanudar | S = Salir")
    time.sleep(2)

    activo = True
    screen_w, screen_h = pyautogui.size()

    try:
        while True:

            if keyboard.is_pressed("s"):
                print("\n⛔ Script detenido por el usuario.")
                break

            if keyboard.is_pressed("p") and activo:
                activo = False
                print("\n⏸ PAUSADO. Presiona R para reanudar.")
                time.sleep(0.4)

            if keyboard.is_pressed("r") and not activo:
                activo = True
                print("\n▶ REANUDADO.")
                time.sleep(0.4)

            if not activo:
                time.sleep(0.1)
                continue

            # Movimiento del mouse
            x = random.randint(0, screen_w - 1)
            y = random.randint(0, screen_h - 1)
            pyautogui.moveTo(x, y, duration=mouse_move_duration)
            time.sleep(mouse_wait)

            # Escribir frase
            frase = random.choice(frases)
            pyautogui.write(frase, interval=escribir_interval)

            # ✅ Selecciona el texto y lo borra SIN afectar otras líneas
            with pyautogui.hold("shift"):
                for _ in range(len(frase)):
                    pyautogui.press("left")

            pyautogui.press("delete")

            time.sleep(entre_frases)

    except pyautogui.FailSafeException:
        print("\n⚠ FailSafe activado (mouse esquina superior izquierda).")
    except Exception as e:
        print(f"\nError inesperado: {e}")
    finally:
        print("Script finalizado.")
        sys.exit(0)


if __name__ == "__main__":
    combinado()


