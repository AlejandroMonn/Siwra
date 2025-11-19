Mouse and Keyboard Automation Tool
SIWRA is a (CLI) tool for automating repetitive tasks on your local computer.

🚀 Features
Auto-clicker: Infinite automatic clicking 
Basic Auto-writer: Automatically writes and deletes text
Advanced Auto-writer: Writes random phrases with pause/resume controls and also deltes them
Auto-move mouse: moves the mouse around the screen wothout a pattern
📋 System Requirements
 Windows, macOS, or Linux and at least python 3.11
🔧 Installation (Python Method)
Step 1: Install python
If you have Python installed go with step 2

Step 2: Download SIWRA
Download the complete SIWRA folder to your computer.

Step 3: Install Dependencies
Open your terminal/console in the siwra folder and run:

pip install -r requirements.txt

Step 4: Verify Installation
python siwra_cli.py --help

You should see the help menu with the available commands.

📦 Installation (Standalone Executable)
Download the executable file for your operating system:

Windows: siwra.exe
macOS/Linux: siwra
On macOS/Linux, give it execute permissions:

chmod +x siwra

Run it directly:

# Windows
siwra.exe --help
# macOS/Linux
./siwra --help

Available Commands
1. Auto-clicker
Performs infinite automatic clicks. Press 'S' to stop.

python siwra_cli.py click

Instructions:

The script waits 2 seconds.
Position your mouse where you want to click.
Clicks start automatically.
Press 'S' to stop.
2. Basic Auto-Writer
Repeatedly writes and deletes the letters "ABC".

python siwra_cli.py write

Instructions:

The script waits 2 seconds.
Click in the text field where you want to write.
Writing starts automatically.
Press 'S' to stop.

3. Advanced Auto-Writer
Writes random phrases with pause controls.

python siwra_cli.py write-adv

Instructions:

The script waits 3 seconds.
Click in the text field where you want to write.
Writing starts automatically.
Controls:

P = Pause
R = Resume
S = Exit

4. Auto-Move Mouse
Moves the mouse randomly around the screen.

python siwra_cli.py move

Instructions:

The script waits 2 seconds.
The mouse starts moving randomly.
Press 'S'  or " ALT+SHIFT+S/Q " to stop.

Run as Administrator in windows

Some systems require running as administrator for keyboard/mouse control.
Security

All scripts can be stopped by pressing 'S' or ALT+SHIFT+Q/S
If a script is unresponsive reboot the PC

Project Structure:
siwra/
├── siwra_cli.py # Main CLI
├── Autoclicker.py # Auto-click script
├── autowriter.py # Basic auto-write script
├── advanced_autowriter.py # Advanced auto-write script
├── Automovedormouse.py # Mouse movement script
├── requirements.txt # Python dependencies
└── README.md # This documentation

Dependencies
pyautogui - Mouse and keyboard control
keyboard - Key press detection
pillow - Required by pyautogui for screenshots and 
solving problems

📝 License
This project is open source

Add new automation scripts.
Improve the CLI with more options.
Optimize performance.
Report bugs or suggest improvements.
Version: 1.0.0
Last updated: November 2025
