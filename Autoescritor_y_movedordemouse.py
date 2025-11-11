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
    "Escribiendo como si fuera de verdad.",
    "Simulación de tipeo natural en progreso."
]

detener = False

def detener_script():
    global detener
    detener = True
    print("\n⛔ Script detenido por el usuario.")

keyboard.add_hotkey("ctrl+alt+s", detener_script)


def obtener_ventana():
    ventanas = gw.getWindowsWithTitle(NOMBRE_APP)

    if not ventanas:
        print(f"❌ No se encontró una ventana con el nombre: {NOMBRE_APP}")
        sys.exit()

    win = ventanas[0]
    win.activate()
    time.sleep(0.3)
    return win


def escribir_humano(texto):
    """Simula escritura humana variando velocidad y con pausas micro"""
    for letra in texto:
        pyautogui.write(letra)
        time.sleep(random.uniform(0.03, 0.14))  # velocidad humana


def borrar_humano(cantidad):
    """Simula borrar uno por uno como persona"""
    for _ in range(cantidad):
        pyautogui.press("backspace")
        time.sleep(random.uniform(0.02, 0.09))


def mover_mouse_humano(win):
    """Movimiento suave dentro de VS Code"""
    x_dest = random.randint(win.left + 80, win.left + win.width - 80)
    y_dest = random.randint(win.top + 80, win.top + win.height - 80)
    duracion = random.uniform(0.15, 0.55)

    pyautogui.moveTo(x_dest, y_dest, duration=duracion)


def automatizar():
    win = obtener_ventana()

    print(f"✅ Automatizando únicamente en: {win.title}")
    print("⏸ Pausar: P | ▶ Reanudar: R | ❌ Detener: CTRL + ALT + S")

    activo = True

    while not detener:
        win.activate()

        if keyboard.is_pressed("p"):
            activo = False
            print("⏸ Pausado")
            time.sleep(0.5)

        if keyboard.is_pressed("r"):
            activo = True
            print("▶ Reanudado")
            time.sleep(0.5)

        if not activo:
            time.sleep(0.1)
            continue

        frase = random.choice(frases)
        escribir_humano(frase)
        time.sleep(random.uniform(0.4, 1.2))  # como si pensaras luego de escribir
        borrar_humano(len(frase))

        mover_mouse_humano(win)

        time.sleep(random.uniform(0.6, 2.2))  # descanso entre "acciones"

    print("Script finalizado.")
    sys.exit()


if __name__ == "__main__":
    automatizar()
