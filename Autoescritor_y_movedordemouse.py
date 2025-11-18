import pyautogui
import keyboard
import pygetwindow as gw
import random
import time
import sys

NOMBRE_APP = "Siwra"

frases = [
    "Solo estoy probando algo.",
    "Esta automatización pareciera humana si o que?",
    "Simulación de tipeo natural en progreso"
]

detener = False


# Hotkey para terminar todo
keyboard.add_hotkey("alt+shift+q", lambda: terminar_script())

def terminar_script():
    global detener
    print("\n eteniendo todo...")
    detener = True


def obtener_ventana():
    # Busco la ventana un poco “a lo bruto”
    ventana = gw.getWindowsWithTitle(NOMBRE_APP)
    if not ventana:
        print("❌ No encontré la ventana, revisa si está abierta o escrita igual")
        sys.exit()

    v = ventana[0]
    try:
        v.activate()
    except:
        print("No pude activar la ventana, pero sigo intentando...")
    time.sleep(0.4)
    return v


def escribir_humano(texto):
    teclas = 0

    for letra in texto:
        keyboard.write(letra)
        teclas += 1
        time.sleep(random.uniform(0.04, 0.18))  # Más lento, estilo humano

    return teclas


def borrar_humano(total):
    for _ in range(total):
        pyautogui.press("backspace")
        time.sleep(random.uniform(0.03, 0.1))


def mover_mouse_humano(ventana):
    try:
        x = random.randint(ventana.left + 60, ventana.left + ventana.width - 60)
        y = random.randint(ventana.top + 60, ventana.top + ventana.height - 60)
    except:
        # por si algo sale mal, mouse a un lugar random cualquiera
        x, y = random.randint(0, 400), random.randint(0, 400)

    pyautogui.moveTo(x, y, duration=random.uniform(0.2, 0.7))


def automatizar():
    vent = obtener_ventana()

    print(f"✅ Trbajando solo en: {vent.title}")
    print(" Pausa con P | Reanuda con R | ❌ Salida con ALT + SHIFT + Q")

    activo = True

    while not detener:
        try:
            vent.activate()
        except:
            pass

        if keyboard.is_pressed("p"):
            activo = False
            print(" pausado...")
            time.sleep(0.5)

        if keyboard.is_pressed("r"):
            activo = True
            print("▶ Ok, seguimos")
            time.sleep(0.5)

        if not activo:
            continue

        frase = random.choice(frases)
        t = escribir_humano(frase)

        time.sleep(random.uniform(0.5, 1.3))
        borrar_humano(t)

        mover_mouse_humano(vent)
        time.sleep(random.uniform(1, 2.7))

    print("Listo, script finalizado")
    sys.exit()


if __name__ == "__main__":
    automatizar()
