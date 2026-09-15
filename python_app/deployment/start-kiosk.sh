#!/bin/sh
set -eu

APP_DIR="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"

if ! command -v python3 >/dev/null 2>&1; then
    echo "python3 was not found. Install it with: sudo apt install -y python3 python3-tk" >&2
    exit 1
fi

if ! python3 -c 'import tkinter' >/dev/null 2>&1; then
    echo "Tkinter was not found. Install it with: sudo apt install -y python3-tk" >&2
    exit 1
fi

if [ -z "${DISPLAY:-}" ]; then
    echo "No graphical display is available (DISPLAY is not set)." >&2
    echo "Use Raspberry Pi OS with Desktop and start this from its graphical session." >&2
    echo "A headless SSH terminal cannot run the Tkinter touchscreen GUI." >&2
    exit 1
fi

exec python3 "$APP_DIR/app.py" --fullscreen
