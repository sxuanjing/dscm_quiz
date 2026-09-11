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

## Raspberry Pi

Build the app with `npm run build`, install a lightweight static server such as `serve`, and run `deployment/start-kiosk.sh` after copying the project to the Pi. The script serves the bundled `dist` directory locally and opens Chromium in kiosk mode:

```bash
chromium-browser --kiosk --noerrdialogs --disable-infobars http://localhost:4173
```

Copy `deployment/supply-chain-quest.desktop` to `~/.config/autostart/` and update the project path in the desktop entry if needed. Disable screen blanking for the event session using Raspberry Pi OS display power settings. Staff can exit kiosk mode with `Alt+F4` when a keyboard is connected.

The game has no network dependency at runtime. The local server is only used to serve bundled files to Chromium; questions and visual styling are included in the production build.
