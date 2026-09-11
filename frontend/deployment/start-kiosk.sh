#!/bin/bash
set -e

APP_DIR="/home/pi/supply-chain-quest/frontend"
PORT="4173"
CHROMIUM="$(command -v chromium || command -v chromium-browser || true)"

if [ -z "$CHROMIUM" ]; then
	echo "Chromium was not found. Install it with: sudo apt install -y chromium"
	exit 1
fi

cd "$APP_DIR"
serve dist --listen "$PORT" >/tmp/supply-chain-quest-server.log 2>&1 &
SERVER_PID=$!
trap 'kill "$SERVER_PID"' EXIT
sleep 2
"$CHROMIUM" --kiosk --noerrdialogs --disable-infobars --disable-session-crashed-bubble "http://localhost:${PORT}"
