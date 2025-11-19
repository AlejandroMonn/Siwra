Herramienta de automatización de ratón y teclado

SIWRA es una herramienta de línea de comandos (CLI) para automatizar tareas repetitivas en tu ordenador.

Autoclic: Clic automático infinito
Autoescritura básica: Escribe y borra texto automáticamente
Autoescritura avanzada: Escribe frases aleatorias con controles de pausa/reanudación y también las borra
Movimiento automático del ratón: Mueve el ratón por la pantalla sin un patrón predefinido
Compatible con Windows, macOS o Linux y Python 3.11 o superior
Instalación (si deseas instalarlo con Python)
Paso 1: Instala Python
Si ya tienes Python instalado, continúa con el paso 2
Paso 2: Descarga SIWRA
Descarga la carpeta completa de SIWRA a tu ordenador. Paso 3: Instalar dependencias
Abre tu terminal/consola en la carpeta siwra y ejecuta:
pip install -r requirements.txt
Paso 4: Verificar la instalación
python siwra_cli.py --help
Deberías ver el menú de ayuda con los comandos disponibles.
Instalación (Ejecutable independiente)
Descarga el archivo ejecutable para tu sistema operativo:
Windows: siwra.exe macOS/Linux: siwra (dale permisos de ejecución: chmod +x siwra)
Comandos disponibles
1. Autoclic
Realiza clics automáticos infinitos. Pulsa 'S' para detener.
python siwra_cli.py click
Instrucciones:
El script espera 2 segundos.
Coloca el ratón donde quieras hacer clic.
Los clics comienzan automáticamente.
Pulsa 'S' para detener.
2. Autoescritor básico
Escribe y borra repetidamente las letras "ABC".
python siwra_cli.py write
Instrucciones:
El script espera 2 segundos.
Haga clic en el campo de texto donde desea escribir.
La escritura comienza automáticamente.
Presione 'S' para detener.
3. Autoescritura avanzada
Escribe frases aleatorias con controles de pausa.
python siwra_cli.py write-adv
Instrucciones:
El script espera 3 segundos.
Haga clic en el campo de texto donde desea escribir.
La escritura comienza automáticamente.
Controles:
P = Pausa
R = Reanudar
S = Salir
4. Movimiento automático del ratón
Mueve el ratón aleatoriamente por la pantalla.
python siwra_cli.py move
Instrucciones:
El script espera 2 segundos.
El ratón comienza a moverse aleatoriamente.
Presione 'S' o "ALT+SHIFT+S/Q" para detener.
Ejecutar como administrador en Windows. Algunos sistemas requieren privilegios de administrador para controlar el teclado y el ratón.
Seguridad
Todos los scripts se pueden detener pulsando «S» o ALT+MAYÚS+Q/S. Si un script no responde, reinicie el PC.
Estructura del proyecto:
siwra/siwra_cli.py # Interfaz de línea de comandos principal
Autoclicker.py # Script de clic automático
autowriter.py # Script básico de escritura automática
advanced_autowriter.py # Script avanzado de escritura automática
Automovedormouse.py # Script de movimiento del ratón
requirements.txt # Dependencias de Python necesarias (dependencias: pyautogui, keyboard y pillow)
README.md # Este documento

Licencia
Este proyecto es de código abierto.

Versión: 1.0.0
Última actualización: noviembre de 2025
