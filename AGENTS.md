# Supply Chain Open House Game

## Current Phase

Validate the official Raspberry Pi 7-inch Touch Display path with a minimal Tkinter Hello World screen before rebuilding the quiz.

## Hardware Requirements

- Raspberry Pi 4.
- Official Raspberry Pi 7-inch Touch Display (DSI, capacitive).
- 800 x 480 landscape display.

## Phase 1: Display Bring-Up

- Use Python 3 and Tkinter only for the first test.
- Run `hello_world.py` manually through a real X display on the local Raspberry Pi console.
- Disconnect HDMI while testing so X output cannot be mistaken for touch display output.
- Confirm the touch display shows `Hello World` at 800 x 480.
- Confirm touchscreen input or a local mouse can interact with the window.
- Do not add the quiz or automatic service until the manual display test passes.
- Do not use a fake `$DISPLAY`; Tkinter requires a real X display server.

## Phase 2: Quiz Requirements

- Build an offline educational supply-chain quiz.
- Show one question at a time with exactly two large answer choices.
- Allow only one answer per question and show immediate correct/incorrect feedback.
- Include a short explanation, progress, score, completion message, restart button, and inactivity reset.
- Keep all questions and visuals local; do not add accounts, persistence, networking, or data collection.
- Keep state in memory and use Python's standard library wherever possible.

## Phase 3: Kiosk Deployment

- Use Raspberry Pi OS with Desktop.
- Start the GUI directly without Node.js, npm, Chromium, or a web server.
- Add systemd startup only after manual X/Tkinter touch display testing passes.
- Document display orientation, touch calibration, maintenance exit, and service logs.
- Keep the startup path compatible with `/home/pi/supply-chain-quest` and user `pi` unless deployment documentation is updated together.

## Testing

- Compile every Python module.
- Test pure game state transitions without a display.
- Test the complete visitor flow at 800 x 480.
- Test repeated taps, scoring, progression, completion, restart, and timeout reset.
- Test the Hello World screen on the physical touch display before kiosk automation.
- Test offline operation and automatic startup after reboot.

## Coding Standards

1. Keep the implementation simple and focused on the open-house visitor flow.
2. Prefer pure, testable game logic separated from Tkinter rendering.
3. Use large touch targets, strong contrast, and text plus symbols for feedback.
4. Keep user-facing copy short and suitable for general visitors.
5. Do not add remote assets, network services, persistence, or unnecessary dependencies.
6. Do not include emojis in the interface, source code, or documentation.
