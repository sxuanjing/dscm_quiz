#!/bin/bash
set -e

APP_DIR="/home/pi/supply-chain-quest/frontend"
PORT="4173"

cd "$APP_DIR"
npx serve dist --listen "$PORT" >/tmp/supply-chain-quest-server.log 2>&1 &
SERVER_PID=$!
trap 'kill "$SERVER_PID"' EXIT
sleep 2
chromium-browser --kiosk --noerrdialogs --disable-infobars --disable-session-crashed-bubble "http://localhost:${PORT}"
