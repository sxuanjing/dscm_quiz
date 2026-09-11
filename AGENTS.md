# Supply Chain Open House Game

## Business Requirements

- An MVP of an interactive educational game for visitors at an open house
- The game will run on a Raspberry Pi connected to a 3.5-inch LCD touchscreen
- The game should launch automatically in full-screen kiosk mode when the Raspberry Pi starts
- The game should help visitors understand the meaning, activities, and importance of Supply Chain Management
- Each game session consists of multiple questions
- Every question has exactly 2 answer choices for the visitor to select
- Questions and answers may use words, graphics, icons, illustrations, or a combination of these
- The interaction must be simple enough for first-time visitors to understand without assistance
- Display one question at a time with large, touch-friendly answer buttons
- Provide immediate visual feedback after each answer, showing whether the selected answer is correct
- Include a short and simple explanation after each answer to reinforce learning
- Display the visitor's score and a positive completion message at the end of the game
- Provide a prominent button to restart the game for the next visitor
- Automatically return to the welcome screen after a short period of inactivity on the completion screen
- The priority is an interactive, interesting, colourful, and polished UI/UX designed for open house visitors
- The app should open with a complete set of dummy questions and suitable visual content
- No administration panel, login, leaderboard, data collection, online account, or other additional functionality

## Suggested Learning Content

- What Supply Chain Management means
- How products move from suppliers to customers
- The roles of suppliers, manufacturers, warehouses, transport providers, retailers, and customers
- Basic inventory and warehouse decisions
- Choosing suitable transport options
- Matching products with the correct supply chain activity
- Sustainability in supply chains, such as reducing waste and selecting greener delivery options
- The use of technology, automation, data, and robots in modern supply chains
- Simple real-life examples that are familiar to secondary school students and members of the public

## Game Flow

1. Display a colourful welcome screen with the game title and a large Start Game button
2. Start the game when the visitor touches the button
3. Present one question with exactly 2 large answer choices
4. Allow only one answer to be selected for each question
5. Show immediate correct or incorrect feedback with a short explanation
6. Provide a large Next Question button
7. Repeat until all questions have been completed
8. Display the final score and a positive message
9. Provide a Play Again button that resets the game
10. Return automatically to the welcome screen after inactivity on the final screen

## Technical Details

- Implement the game as a lightweight, client-rendered web app
- Create the application in a subdirectory named `frontend`
- Ensure the interface fits a 3.5-inch Raspberry Pi LCD touchscreen without horizontal scrolling
- Design primarily for a 480 x 320 landscape display while keeping the layout responsive
- Use large touch targets, readable text, clear contrast, and minimal on-screen content
- Support Chromium running in Raspberry Pi kiosk mode
- The game must work locally without an internet connection after installation
- Store all questions, answers, explanations, and local visual assets within the project
- No backend, database, cloud service, persistence, or user management
- Do not record visitors' names, answers, scores, or personal information
- Keep game state in memory and reset it after each completed session
- Use popular, lightweight, actively maintained libraries only when they simplify development
- Avoid heavy dependencies that may reduce performance on the Raspberry Pi
- Include a simple startup script and setup instructions for automatically launching the game after Raspberry Pi startup
- Prevent accidental text selection, browser navigation, zoom gestures, and interactions that are unsuitable for kiosk use where practical

## Content Requirements

- Include at least 10 sample questions for the MVP
- Each question must contain:
  - A unique identifier
  - A question prompt
  - Exactly 2 answer choices
  - The correct answer
  - A short explanation
  - An optional local image or icon reference
- Use concise language suitable for general open house visitors
- Avoid technical jargon unless it is explained clearly
- Ensure the correct answer is not always displayed in the same position
- Use a balanced mix of question styles, including:
  - Word-based questions
  - Image recognition questions
  - Simple scenario questions
  - Match-the-activity questions
  - Sustainability and technology questions
- All visual assets must be appropriate for public and educational use

## UI and Interaction Requirements

- Use a colourful and energetic visual style suitable for an educational open house
- Use a supply chain theme with visual references to trucks, ships, warehouses, products, factories, robots, and customers
- Keep each screen uncluttered and focused on one action
- Make all important controls easy to tap on the 3.5-inch touchscreen
- Recommended minimum touch target size is 48 x 48 pixels, with larger answer buttons preferred
- Use clear visual states for default, pressed, correct, incorrect, and disabled controls
- Do not rely on colour alone to communicate correct or incorrect answers; also use clear symbols and text labels
- Use short, smooth transitions that make the game feel polished without slowing down interaction
- Avoid small links, hover-only interactions, complex menus, scrolling question screens, and keyboard-dependent controls
- Ensure visitors cannot proceed without selecting an answer
- Prevent repeated scoring from multiple taps on the same question

## Color Scheme

- Supply Chain Blue: `#209dd7` - primary buttons, key sections, progress indicators
- Innovation Purple: `#753991` - important actions, completion screen, secondary highlights
- Accent Yellow: `#ecad0a` - highlights, progress, decorative details
- Dark Navy: `#032147` - main headings and high-contrast text
- Success Green: `#22a06b` - correct answer feedback
- Error Red: `#d64545` - incorrect answer feedback
- Light Background: `#f5f8fc` - main background
- White: `#ffffff` - cards, answer panels, and readable content areas
- Gray Text: `#6f7782` - supporting text and labels

## Accessibility and Usability

- Use readable font sizes appropriate for a small screen
- Maintain strong colour contrast between text and backgrounds
- Provide text or symbols in addition to colour-based feedback
- Use plain language and short instructions
- Ensure all interactions work by touch without requiring a mouse or keyboard
- Keep important content within the visible display area
- Make the restart flow obvious so the next visitor can begin independently
- Include a visible progress indicator such as `Question 3 of 10`
- Keep animations brief and respect reduced-motion settings where available

## Raspberry Pi Deployment

- Provide clear setup instructions for Raspberry Pi OS
- Provide commands to install project dependencies and create the production build
- Provide a reliable command to run the app locally
- Configure Chromium to open the local game URL in full-screen kiosk mode
- Include an autostart configuration so the game launches after the Raspberry Pi desktop starts
- Hide the mouse cursor after a short period of inactivity if a cursor is visible
- Disable screen blanking and sleep during the open house where practical
- Ensure the app can recover cleanly after the Raspberry Pi is restarted
- Document how staff can exit kiosk mode for maintenance
- Do not require internet access during normal operation

## Strategy

1. Write a phased implementation plan with measurable success criteria for each phase
2. Scaffold the project inside `frontend`, including `.gitignore`, a minimal README, and test configuration
3. Build the responsive welcome screen and establish the visual design system
4. Implement the question data structure and populate it with at least 10 sample Supply Chain Management questions
5. Implement the complete game flow, scoring, feedback, progress, restart, and inactivity reset
6. Optimise the interface for a 480 x 320 touchscreen and confirm that no essential screen requires horizontal scrolling
7. Add local visual assets and confirm that the game works fully offline
8. Add unit tests for scoring, question progression, answer locking, restart behaviour, and inactivity reset
9. Carry out integration and end-to-end testing with Playwright or a similar tool, using a 480 x 320 viewport and touch input where supported
10. Test the production build on the target Raspberry Pi and LCD touchscreen, fixing display, touch, performance, and kiosk-mode defects
11. Configure automatic startup and verify that the game launches successfully after a full Raspberry Pi reboot
12. Only complete the project when the MVP is finished, tested, running in kiosk mode, and ready for open house visitors

## Success Criteria

- The Raspberry Pi launches the game automatically after startup
- The game displays correctly on the 3.5-inch LCD touchscreen in landscape orientation
- Visitors can complete the entire game using touch only
- Every question offers exactly 2 answer choices
- Correct and incorrect feedback is clear and immediate
- The visitor's score is calculated correctly
- The game can be restarted easily for the next visitor
- The completion screen resets automatically after inactivity
- The game works without internet access
- No visitor data is stored
- All automated unit and end-to-end tests pass
- The interface is colourful, professional, responsive, and suitable for an open house environment
- There are no unnecessary features beyond the stated MVP scope

## Testing Requirements

- Unit test question progression and end-of-game behaviour
- Unit test correct and incorrect scoring
- Unit test that each question accepts only one answer
- Unit test Play Again and full state reset
- Unit test inactivity reset on the completion screen
- Validate that every question has exactly 2 answers and one valid correct answer
- Run end-to-end tests for the complete visitor journey
- Run end-to-end tests at a 480 x 320 viewport
- Test repeated fast taps to prevent duplicate scoring or skipped questions
- Test refreshing and restarting the local app
- Test the production build without an internet connection
- Test automatic launch after a Raspberry Pi reboot
- Test actual touch input, readability, button sizing, and screen fit on the target LCD

## Coding Standards

1. Use current stable versions of libraries and idiomatic approaches at the time of implementation
2. Keep the solution simple and never over-engineer
3. Do not add functionality that is not included in the business requirements
4. Prefer clear components, straightforward state management, and easily editable question data
5. Use semantic HTML and accessible interaction patterns
6. Keep all user-facing text concise and suitable for the target audience
7. Keep the README minimal but include installation, local development, testing, production build, Raspberry Pi deployment, kiosk startup, and maintenance exit instructions
8. Use consistent formatting, linting, and meaningful file names
9. Do not use remote assets or services that would prevent offline operation
10. Do not include emojis in the interface, source code, documentation, or commit messages
