SIWRA - Mouse and Keyboard Automation Tool
SIWRA is a command-line interface (CLI) tool for automating repetitive mouse and keyboard tasks on your local computer.

🚀 Features
Auto-clicker - Infinite automatic clicking at the mouse position
Basic Auto-writer - Automatically writes and deletes text
Advanced Auto-writer - Writes random phrases with pause/resume controls
Auto-move mouse - Randomly moves the mouse around the screen
📋 System Requirements
Operating System: Windows, macOS, or Linux
Python: 3.11 or higher
Access to a graphical interface (does not work on servers without a GUI)
🔧 Installation (Python Method)
Step 1: Install Python
If you don't have Python installed:

Windows: Download from python.org
macOS: `brew install python` or download from python.org
Linux: `sudo apt install python3` or `python3-pip` (Ubuntu/Debian)
Step 2: Download SIWRA
Download the complete SIWRA folder to your computer.

Step 3: Install Dependencies
Open your terminal/console in the siwra folder and run:

pip install -r requirements.txt

Step 4: Verify Installation
python siwra_cli.py --help

You should see the help menu with the available commands.

📦 Installation (Standalone Executable)
If you prefer to use the executable version without installing Python:

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

🎮 Usage
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
Press 'S' to stop.
⚠️ Important Warnings
Accessibility Permissions (macOS)

You may need to grant accessibility permissions to the terminal or the executable.
Go to: System Settings > Privacy & Security > Accessibility
Run as Administrator (Windows)

Some systems require running as administrator for keyboard/mouse control.
Security

Use these scripts responsibly.
Do not use them for unauthorized automation in applications or games.
Stopping Scripts

All scripts can be stopped by pressing 'S'.
If a script is unresponsive, you can close the terminal window.
🛠️ Development
Project Structure
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
pillow - Required by pyautogui for screenshots
🐛 Troubleshooting
Error: "No module named 'pyautogui'"
Solution:

pip install -r requirements.txt

Error: "Permission denied" (macOS/Linux)
Solution:

chmod +x siwra_cli.py

The script isn't detecting the keys on macOS.
Solution:

Open System Settings.
Go to Privacy & Security > Accessibility.
Add Terminal (or your terminal application) to the list of allowed apps.
The auto-clicker isn't working.
Check:

Did you position the mouse before the clicks started?

Are you running with sufficient permissions?

Did you wait the initial 2 seconds?

📝 License
This project is open source for personal and educational use.

🤝 Contributions
If you want to improve SIWRA, you can:

Add new automation scripts.
Improve the CLI with more options.
Optimize performance.
Report bugs or suggest improvements.
Version: 1.0.0
Last updated: November 2025
