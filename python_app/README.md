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

The recommended lightweight setup is Raspberry Pi OS Lite with the LCD driver, Xorg, and a project checkout at `/home/pi/supply-chain-quest`. Tkinter cannot run from a headless SSH session by itself; the service below creates the X display during boot. Raspberry Pi OS with Desktop also works, but use only one startup method.

```bash
sudo apt update
sudo apt install -y git python3 python3-tk xserver-xorg-core xinit x11-xserver-utils unclutter
cd /home/pi
git clone https://github.com/YOUR-GITHUB-USERNAME/YOUR-REPOSITORY.git supply-chain-quest
cd /home/pi/supply-chain-quest
python3 -m unittest discover -s python_app/tests -v
chmod +x python_app/deployment/start-kiosk.sh
python_app/deployment/start-kiosk.sh
```

The LCD driver must already be installed and configured as the active X display. If an HDMI monitor is connected, X may appear there instead of the LCD. For the first test, disconnect the HDMI monitor and confirm that the LCD driver is configured for `480x320` landscape orientation. Do not set a fake `DISPLAY` value: Tkinter needs a real X display server.

The game opens fullscreen. Press `Esc` when a keyboard is connected to leave fullscreen mode, then use `Alt+F4` to close the application.

### Automatic startup

For Raspberry Pi OS Lite or a kiosk without the full desktop, install the provided systemd service:

```bash
sudo cp python_app/deployment/supply-chain-quest.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable supply-chain-quest.service
sudo systemctl start supply-chain-quest.service
sudo systemctl status supply-chain-quest.service
```

View startup errors with:

```bash
journalctl -u supply-chain-quest.service -b --no-pager
```

The service uses `startx` on `tty1`, then starts the fullscreen Tkinter app. Do not enable this service and the desktop autostart entry at the same time.

For Raspberry Pi OS with Desktop, use the desktop autostart entry instead:

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
