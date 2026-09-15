# Supply Chain Quest

A local touchscreen quiz for supply-chain open house visitors. The game uses Python and Tkinter only, keeps session state in memory, and is designed for a 480 x 320 Raspberry Pi display.

## Development

Requires Python 3 and Tkinter.

```bash
python3 -m unittest discover -s python_app/tests -v
python3 -m compileall python_app
python3 python_app/app.py
```

Use `Esc` to leave fullscreen mode during maintenance. The app does not use a network connection or store visitor data.

## Raspberry Pi 4

These commands assume Raspberry Pi OS with the desktop and a project checkout at `/home/pi/supply-chain-quest`.

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

The game opens fullscreen. Press `Esc` when a keyboard is connected to leave fullscreen mode, then use `Alt+F4` to close the application.

### Automatic startup

```bash
mkdir -p /home/pi/.config/autostart
cp python_app/deployment/supply-chain-quest.desktop /home/pi/.config/autostart/
sudo reboot
```

The desktop entry launches the game directly with Python. No Node.js, npm, Chromium, web server, or internet connection is required after installation.

For an open-house display, configure the LCD in landscape orientation, disable screen blanking and power saving, and optionally hide the cursor:

```bash
unclutter -idle 3 -root &
```

### Updating

```bash
cd /home/pi/supply-chain-quest
git pull
python3 -m unittest discover -s python_app/tests -v
sudo reboot
```
