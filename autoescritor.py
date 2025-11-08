import keyboard
import time
import sys

def algoritmo_escritura():
    letras = "ABC"

    while True:
        # Escribe rápido
        for letra in letras:
            keyboard.write(letra)
            time.sleep(0.01)  # puedes bajar a 0.001 para más velocidad

        # Borra rápido
        for _ in range(len(letras)):
            keyboard.press_and_release("backspace")
            time.sleep(0.01)

        # Si presionas "S", termina todo
        if keyboard.is_pressed("s"):
            print("\nScript detenido por el usuario.")
            sys.exit()


if __name__ == "__main__":
    print("--- Auto Escritor Loop Infinito ---")
    print("Haz clic en el editor donde se escribirán las letras.")
    print("Presiona 'S' en cualquier momento para detener el script.")
    time.sleep(2)

    try:
        algoritmo_escritura()
    except Exception as e:
        print(f"\nOcurrió un error: {e}")
    finally:
        print("Script finalizado.")