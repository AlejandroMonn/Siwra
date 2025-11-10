import pyautogui
import keyboard
import random
import time
import sys

# --- Configurables ---
frases = [
    "Hola, esto es una prueba.",
    "Automatización combinada: teclado + mouse.",
    "Otra frase para enviar.",
    "Mensaje de prueba."
]
escribir_interval = 0.005    # intervalo entre caracteres al escribir
entre_frases = 0.3           # tiempo entre frases
mouse_move_duration = 0.08   # duración del movimiento del mouse a cada punto
mouse_wait = 0.05            # espera entre movimientos
# -----------------------

def combinado():
    print("Iniciando automatización combinada (teclado + mouse).")
    print("P = Pausar | R = Reanudar | S = Salir")
    print("Nota: mover el mouse a la esquina superior izquierda también aborta (PyAutoGUI failsafe).")
    time.sleep(2)  # tiempo para colocar el foco donde quieras

    activo = True  # controla pausa/reanudar

    screen_w, screen_h = pyautogui.size()

    try:
        while True:
            # Chequeos de control (no bloqueantes)
            if keyboard.is_pressed("s"):
                print("\n⛔ Script detenido por el usuario (S).")
                break

            if keyboard.is_pressed("p"):
                if activo:
                    activo = False
                    print("\n⏸ Pausado. Presiona R para reanudar.")
                    time.sleep(0.4)  # evitar múltiples detecciones rápidas

            if keyboard.is_pressed("r"):
                if not activo:
                    activo = True
                    print("\n▶ Reanudado.")
                    time.sleep(0.4)

            # Si está pausado, esperar en ciclo corto
            if not activo:
                time.sleep(0.15)
                continue

            # --- Acción 1: mover el mouse a una posición aleatoria ---
            x = random.randint(0, screen_w - 1)
            y = random.randint(0, screen_h - 1)
            pyautogui.moveTo(x, y, duration=mouse_move_duration)
            time.sleep(mouse_wait)  # pequeña espera entre movimientos

            # --- Acción 2: escribir una frase aleatoria ---
            frase = random.choice(frases)
            pyautogui.write(frase, interval=escribir_interval)
            pyautogui.press("enter")
            time.sleep(entre_frases)

            # PyAutoGUI failsafe: si mueves a esquina superior izquierda, lanza excepción y sale
    except pyautogui.FailSafeException:
        print("\n⚠️ Failsafe activado (mouse en esquina superior izquierda). Terminando.")
    except KeyboardInterrupt:
        print("\nInterrupción por teclado (Ctrl+C).")
    except Exception as e:
        print(f"\nOcurrió un error: {e}")
    finally:
        print("Script finalizado.")
        sys.exit(0)


if __name__ == "__main__":
    combinado()
