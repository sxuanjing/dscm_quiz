# Supply Chain Quest

# Supply Chain Quest

An offline touchscreen quiz for supply chain open house visitors. The app is designed for a 480 x 320 Raspberry Pi display and keeps all session state in memory.

## Development

```bash
npm install
npm run dev
```

## Checks

```bash
npm run typecheck
npm run lint
npm test
npm run build
```

## Raspberry Pi 4 Deployment

These steps assume Raspberry Pi OS 64-bit with the Raspberry Pi desktop, a working internet connection during installation, and a GitHub repository containing this project. Internet is only needed to install software and clone/build the project. The finished game itself runs from local files.

### 1. Prepare the Pi

Connect the 3.5-inch LCD, keyboard, and network. Open a terminal and update Raspberry Pi OS:

```bash
sudo apt update
sudo apt full-upgrade -y
sudo reboot
```

After the reboot, open a terminal again and install Git, Node.js, Chromium, and display utilities:

```bash
sudo apt update
sudo apt install -y git nodejs npm chromium unclutter
node --version
npm --version
```

If the display is rotated or does not use landscape orientation, set the display rotation in Raspberry Pi Configuration, then reboot before continuing.

### 2. Clone the project from GitHub

Replace the placeholder URL with the HTTPS or SSH URL of your GitHub repository:

```bash
cd /home/pi
git clone https://github.com/YOUR-GITHUB-USERNAME/YOUR-REPOSITORY.git supply-chain-quest
cd /home/pi/supply-chain-quest/frontend
```

For a private repository, use SSH instead and make sure the Pi has an SSH key registered with GitHub:

```bash
git clone git@github.com:YOUR-GITHUB-USERNAME/YOUR-REPOSITORY.git supply-chain-quest
```

Confirm that the frontend files are present:

```bash
ls
```

You should see `package.json`, `src`, `deployment`, and `index.html`.

### 3. Install dependencies and build

From `/home/pi/supply-chain-quest/frontend`, install dependencies and create the production build:

```bash
npm install
npm run typecheck
npm run build
```

Install the small local web server used by the kiosk launcher:

```bash
sudo npm install --global serve
```

Test the production build before enabling kiosk mode:

```bash
serve dist --listen 4173
```

Open Chromium manually and visit `http://localhost:4173`. Check the welcome screen, start a game, answer questions, confirm the score, and press `Ctrl+C` in the terminal to stop the test server.

### 4. Test the kiosk launcher

Make the launcher executable and run it:

```bash
cd /home/pi/supply-chain-quest/frontend
chmod +x deployment/start-kiosk.sh
deployment/start-kiosk.sh
```

Chromium should open full-screen and display the game. Exit kiosk mode with `Alt+F4` when a keyboard is connected. If the launcher fails, inspect the server log:

```bash
cat /tmp/supply-chain-quest-server.log
```

### 5. Enable automatic startup

Create the Raspberry Pi desktop autostart folder and copy the provided entry:

```bash
mkdir -p /home/pi/.config/autostart
cp /home/pi/supply-chain-quest/frontend/deployment/supply-chain-quest.desktop /home/pi/.config/autostart/
```

Ensure the launcher is executable:

```bash
chmod +x /home/pi/supply-chain-quest/frontend/deployment/start-kiosk.sh
```

Reboot and verify that Chromium opens the game automatically:

```bash
sudo reboot
```

### 6. Configure the open-house display

Disable screen blanking and power saving in Raspberry Pi OS display settings. If a mouse cursor is visible, add this command to the desktop session startup or run it before the kiosk launcher:

```bash
unclutter -idle 3 -root &
```

Keep the Pi connected to its power supply and use landscape orientation. Test the game at the physical display resolution, ideally 480 x 320.

### 7. Update the game from GitHub

When a new version is pushed to GitHub, exit Chromium, then run:

```bash
cd /home/pi/supply-chain-quest
git pull
cd frontend
npm install
npm run build
sudo reboot
```

If dependencies have not changed, `npm install` can be skipped. Rebuilding is required after source changes.

### 8. Maintenance and troubleshooting

- Exit Chromium with `Alt+F4` and use a terminal for maintenance.
- Check the launcher with `bash -x deployment/start-kiosk.sh`.
- Check the local server log with `cat /tmp/supply-chain-quest-server.log`.
- Check that the server exists with `command -v serve`.
- Check that Chromium exists with `command -v chromium || command -v chromium-browser`.
- Restart the Pi with `sudo reboot` after correcting startup or display settings.

The game has no network dependency at runtime. The local server only serves the bundled `dist` directory; questions, icons, and visual styling are included in the production build.
