SIWRA - Herramienta de Automatización de Mouse y Teclado
SIWRA es una herramienta CLI (Command Line Interface) para automatizar tareas repetitivas del mouse y teclado en tu computadora local.

🚀 Características
Auto-clicker - Clic automático infinito en la posición del mouse
Auto-escritor básico - Escribe y borra texto automáticamente
Auto-escritor avanzado - Escribe frases aleatorias con controles de pausa/reanudación
Auto-mover mouse - Mueve el mouse aleatoriamente por la pantalla
📋 Requisitos del Sistema
Sistema Operativo: Windows, macOS o Linux
Python: 3.11 o superior
Acceso a interfaz gráfica (no funciona en servidores sin GUI)
🔧 Instalación (Método Python)
Paso 1: Instalar Python
Si no tienes Python instalado:

Windows: Descarga desde python.org
macOS: brew install python o descarga desde python.org
Linux: sudo apt install python3 python3-pip (Ubuntu/Debian)
Paso 2: Descargar SIWRA
Descarga la carpeta siwra completa a tu computadora.

Paso 3: Instalar Dependencias
Abre la terminal/consola en la carpeta siwra y ejecuta:

pip install -r requirements.txt

Paso 4: Verificar Instalación
python siwra_cli.py --help

Deberías ver el menú de ayuda con los comandos disponibles.

📦 Instalación (Ejecutable Standalone)
Si prefieres usar la versión ejecutable sin instalar Python:

Descarga el archivo ejecutable para tu sistema operativo:

Windows: siwra.exe
macOS/Linux: siwra
En macOS/Linux, dale permisos de ejecución:

chmod +x siwra

Ejecuta directamente:

# Windows
siwra.exe --help
# macOS/Linux
./siwra --help

🎮 Uso
Comandos Disponibles
1. Auto-clicker
Realiza clics automáticos infinitos. Presiona 'S' para detener.

python siwra_cli.py click

Instrucciones:

El script espera 2 segundos
Posiciona tu mouse donde quieres hacer clic
Los clics comienzan automáticamente
Presiona 'S' para detener
2. Auto-escritor Básico
Escribe y borra las letras "ABC" repetidamente.

python siwra_cli.py write

Instrucciones:

El script espera 2 segundos
Haz clic en el campo de texto donde quieres escribir
La escritura comienza automáticamente
Presiona 'S' para detener
3. Auto-escritor Avanzado
Escribe frases aleatorias con controles de pausa.

python siwra_cli.py write-adv

Instrucciones:

El script espera 3 segundos
Haz clic en el campo de texto donde quieres escribir
La escritura comienza automáticamente
Controles:

P = Pausar
R = Reanudar
S = Salir
4. Auto-mover Mouse
Mueve el mouse aleatoriamente por toda la pantalla.

python siwra_cli.py move

Instrucciones:

El script espera 2 segundos
El mouse comienza a moverse aleatoriamente
Presiona 'S' para detener
⚠️ Advertencias Importantes
Permisos de Accesibilidad (macOS)

Es posible que necesites dar permisos de accesibilidad a la terminal o al ejecutable
Ve a: Configuración del Sistema > Privacidad y Seguridad > Accesibilidad
Ejecutar como Administrador (Windows)

Algunos sistemas requieren ejecutar como administrador para el control del teclado/mouse
Seguridad

Usa estos scripts de manera responsable
No los uses para automatización no autorizada en aplicaciones o juegos
Detener Scripts

Todos los scripts se pueden detener presionando 'S'
Si un script no responde, puedes cerrar la ventana de terminal
🛠️ Desarrollo
Estructura del Proyecto
siwra/
├── siwra_cli.py              # CLI principal
├── Autoclickeador.py         # Script de auto-click
├── autoescritor.py           # Script de auto-escritura básica
├── autoescritor_avanzado.py  # Script de auto-escritura avanzada
├── Automovedormouse.py       # Script de movimiento de mouse
├── requirements.txt          # Dependencias Python
└── README.md                 # Esta documentación

Dependencias
pyautogui - Control de mouse y teclado
keyboard - Detección de teclas presionadas
pillow - Requerido por pyautogui para capturas de pantalla
🐛 Solución de Problemas
Error: "No module named 'pyautogui'"
Solución:

pip install -r requirements.txt

Error: "Permission denied" (macOS/Linux)
Solución:

chmod +x siwra_cli.py

El script no detecta las teclas en macOS
Solución:

Abre Configuración del Sistema
Ve a Privacidad y Seguridad > Accesibilidad
Agrega Terminal (o tu aplicación de terminal) a la lista de apps permitidas
El auto-clicker no funciona
Verificar:

¿Posicionaste el mouse antes de que inicien los clics?
¿Estás ejecutando con permisos suficientes?
¿Esperaste los 2 segundos iniciales?
📝 Licencia
Este proyecto es de código abierto para uso personal y educativo.

🤝 Contribuciones
Si deseas mejorar SIWRA, puedes:

Agregar nuevos scripts de automatización
Mejorar la CLI con más opciones
Optimizar el rendimiento
Reportar bugs o sugerir mejoras
Versión: 1.0.0
Última actualización: Noviembre 2025
