import pyautogui
import keyboard
import time
import random
import sys

# Lista de frases que el bot escribirá aleatoriamente
frases = [
    "Hola, ¿cómo estás?",
    "Estoy automatizando tareas.",
    "La tecnología nos hace más eficientes.",
    "Automatización completada.",
    "Probando auto-escritor avanzado."
]

def auto_escritor():
    print("Auto-escritor listo.")
    print("P = Pausar  |  R = Reanudar  |  S = Salir")
    time.sleep(2)

    activo = True  # controla pausa/reanudación

    while True:
        if keyboard.is_pressed("s"):
            print("\n⛔ Script terminado.")
            sys.exit()

        if keyboard.is_pressed("p"):
            activo = False
            print("\n⏸ Pausado (presiona R para reanudar)")
            time.sleep(0.5)

        if keyboard.is_pressed("r"):
            activo = True
            print("\n▶ Reanudado")
            time.sleep(0.5)

        if activo:
            frase = random.choice(frases)
            pyautogui.write(frase, interval=0.01)  # velocidad de escritura
            pyautogui.press("enter")  # salto de línea
            time.sleep(0.3)  # tiempo entre envíos (ajustable)


def main():
    """Función principal para ejecutar desde CLI o standalone."""
    print("--- AUTO ESCRITOR AVANZADO ---")
    print("Haz clic en el editor donde se escribirán los mensajes.")
    print("P = Pausar  |  R = Reanudar  |  S = SALIR")
    time.sleep(3)

    try:
        auto_escritor()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Script finalizado.")


if __name__ == "__main__":
    main()
