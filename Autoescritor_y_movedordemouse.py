import pyautogui
import keyboard
import pygetwindow as gw
import random
import time
import sys

NOMBRE_APP = "Visual Studio Code"

frases = [
    "Solo estoy probando algo.",
    "Esta automatización parece humana.",
    "Simulación de tipeo natural en progreso."
]

detener = False

# ✅ Nuevo método para finalizar: ALT + SHIFT + Q (no interfiere con ninguna letra)
keyboard.add_hotkey("alt+shift+q", lambda: terminar_script())


def terminar_script():
    global detener
    detener = True
    print("\n⛔ Script detenido por el usuario.")


def obtener_ventana():
    win_list = gw.getWindowsWithTitle(NOMBRE_APP)
    if not win_list:
        print(f"❌ No se encontró la ventana: {NOMBRE_APP}")
        sys.exit()

    win = win_list[0]
    win.activate()
    time.sleep(0.3)
    return win


def escribir_humano(texto):
    """Escribe y devuelve cuántas teclas reales fueron enviadas sin perder letras."""
    total_teclas = 0

    for letra in texto:
        keyboard.write(letra)  # ✅ PROTEGE LA Ñ, Ó, Á, É, Í...
        total_teclas += 1
        time.sleep(random.uniform(0.035, 0.16))

    return total_teclas


def borrar_humano(teclas):
    """Borra la cantidad exacta de teclas enviadas."""
    for _ in range(teclas):
        pyautogui.press("backspace")
        time.sleep(random.uniform(0.02, 0.09))


def mover_mouse_humano(win):
    x = random.randint(win.left + 80, win.left + win.width - 80)
    y = random.randint(win.top + 80, win.top + win.height - 80)
    pyautogui.moveTo(x, y, duration=random.uniform(0.15, 0.6))


def automatizar():
    win = obtener_ventana()

    print(f"✅ Automatizando solo en: {win.title}")
    print("⏸ Pausar: P | ▶ Reanudar: R | ❌ Finalizar: ALT + SHIFT + Q")

    activo = True

    while not detener:
        win.activate()

        if keyboard.is_pressed("p"):
            activo = False
            print("⏸ Pausado")
            time.sleep(0.4)

        if keyboard.is_pressed("r"):
            activo = True
            print("▶ Reanudado")
            time.sleep(0.4)

        if not activo:
            continue

        frase = random.choice(frases)
        teclas_enviadas = escribir_humano(frase)

        time.sleep(random.uniform(0.4, 1.2))
        borrar_humano(teclas_enviadas)

        mover_mouse_humano(win)
        time.sleep(random.uniform(0.8, 2.5))

    print("Script finalizado.")
    sys.exit()


if __name__ == "__main__":
    automatizar()
