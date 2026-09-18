# Supply Chain Quest

An offline two-choice supply-chain quiz for the official Raspberry Pi 7-inch Touch Display. The project uses Python and Tkinter without a web server, Node.js, Chromium, or third-party runtime packages.

## Phase 1: Test the Touch Display

Install Python and Tkinter on the development computer or Raspberry Pi, then run:

```bash
python3 hello_world.py
```

On the Raspberry Pi, disconnect HDMI, start X on the local Pi console, and run:

```bash
startx /usr/bin/python3 /home/pi/supply-chain-quest/hello_world.py -- --fullscreen
```

The touch display should show `Hello World` at 800 x 480. Press `Esc` to close the test. Do not configure the quiz or systemd service until this test works on the display.

## Phase 2: Build the game

The quiz implementation will live in [python_app](python_app), with pure game logic tests and a direct Raspberry Pi kiosk launcher. The full deployment guide is in [python_app/README.md](python_app/README.md).
