# Supply Chain Open House Game

## Business Requirements

- Build an interactive educational game for visitors at an open house.
- Run it on a Raspberry Pi connected to a 3.5-inch LCD touchscreen.
- Launch automatically in fullscreen mode when Raspberry Pi OS starts.
- Explain supply-chain management with simple, familiar examples.
- Present one question at a time with exactly two large answer choices.
- Allow one answer, show immediate correct or incorrect feedback, and explain the answer briefly.
- Show progress, score, a positive completion message, and a prominent restart button.
- Return from the completion screen to the welcome screen after a short inactivity period.
- Do not add accounts, administration, leaderboards, data collection, persistence, or online services.

## Technical Requirements

- Implement the supported game as a lightweight Python 3 GUI using Tkinter.
- Keep the application under `python_app`.
- Use Python's standard library wherever possible; do not require Node.js, npm, Chromium, a web server, or third-party Python packages.
- Keep all questions and visual content local so the game runs offline after installation.
- Keep game state in memory and do not record visitor information.
- Target a 480 x 320 landscape display without inaccessible controls or horizontal overflow.
- Use large touch targets, readable text, strong contrast, and symbols plus text for feedback.
- Prevent accidental window resizing and unsuitable desktop interactions where practical.

## Content Requirements

- Include at least 10 questions; the current bank contains 20.
- Each question has a unique ID, prompt, exactly two choices, one valid correct answer, explanation, category, and local visual key.
- Mix word questions, scenarios, roles, transport, warehouse, sustainability, and technology topics.
- Keep the correct answer position varied.

## Raspberry Pi Deployment

- Document Raspberry Pi OS setup and the `python3-tk` package.
- Provide a direct Python startup script and desktop autostart entry.
- Start the game in fullscreen mode without a browser or local web server.
- Document landscape orientation, screen blanking, optional cursor hiding, and maintenance exit.
- Ensure the app recovers cleanly after a restart and needs no network at runtime.

## Testing Requirements

- Test question validation and exactly two choices.
- Test correct and incorrect scoring.
- Test answer locking and repeated taps.
- Test progression, final completion, restart, and inactivity reset behavior.
- Run the complete visitor flow at the 480 x 320 target size.
- Verify offline operation and Raspberry Pi autostart on the target hardware.

## Coding Standards

1. Keep the solution simple and avoid unnecessary dependencies.
2. Prefer clear components, pure game-state logic, and editable question data.
3. Keep user-facing text concise and suitable for general visitors.
4. Keep documentation focused on Python development and Raspberry Pi deployment.
5. Do not use remote assets or services that prevent offline operation.
6. Do not include emojis in the interface, source code, documentation, or commit messages.
