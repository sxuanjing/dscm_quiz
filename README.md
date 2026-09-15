# Supply Chain Quest

Supply Chain Quest is an offline two-choice quiz for visitors at a supply-chain open house. It runs as a lightweight Python Tkinter GUI on a Raspberry Pi 4 connected to a 3.5-inch touchscreen.

The supported application is in [python_app](python_app). It uses Python's standard library and keeps all game state in memory. No web server, Chromium, Node.js, npm, backend, database, network connection, or visitor data collection is required.

## Run locally

Requires Python 3 and Tkinter.

```bash
python3 -m unittest discover -s python_app/tests -v
python3 python_app/app.py
```

Use `Esc` to leave fullscreen mode during maintenance. The game contains 20 questions and selects 10 questions for each session.

## Raspberry Pi 4

On Raspberry Pi OS with the desktop:

```bash
sudo apt update
sudo apt install -y git python3 python3-tk unclutter
cd /home/pi
git clone https://github.com/YOUR-GITHUB-USERNAME/YOUR-REPOSITORY.git supply-chain-quest
cd /home/pi/supply-chain-quest
python3 -m unittest discover -s python_app/tests -v
chmod +x python_app/deployment/start-kiosk.sh
python_app/deployment/start-kiosk.sh
```

Configure the LCD in landscape orientation and check the game at 480 x 320. Press `Esc`, then `Alt+F4`, to exit during maintenance.

Enable automatic startup:

```bash
mkdir -p /home/pi/.config/autostart
cp python_app/deployment/supply-chain-quest.desktop /home/pi/.config/autostart/
sudo reboot
```

The complete deployment guide is in [python_app/README.md](python_app/README.md).
