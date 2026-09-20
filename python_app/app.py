"""Tkinter touchscreen interface for Supply Chain Quest."""

from __future__ import annotations

import argparse
import tkinter as tk
from tkinter import font as tkfont

try:
    from .game import QUESTIONS_PER_GAME, GameState, answer, answer_is_correct, current_question, next_question, reset_game, start_game
except ImportError:
    from game import QUESTIONS_PER_GAME, GameState, answer, answer_is_correct, current_question, next_question, reset_game, start_game


COLORS = {
    "blue": "#209dd7",
    "blue_dark": "#0877a8",
    "orange": "#f0783c",
    "teal": "#16a6a0",
    "purple": "#753991",
    "purple_dark": "#52256a",
    "yellow": "#ecad0a",
    "navy": "#032147",
    "green": "#22a06b",
    "green_dark": "#16784e",
    "red": "#d64545",
    "red_dark": "#af3030",
    "background": "#f5f8fc",
    "white": "#ffffff",
    "muted": "#6f7782",
    "border": "#d9e5eb",
}

CATEGORY_COLORS = {
    "flow": (COLORS["blue"], "#e3f5fb"),
    "roles": (COLORS["purple"], "#f0e8f3"),
    "warehouse": (COLORS["yellow"], "#fff5d8"),
    "transport": ("#e66b2f", "#fff0e8"),
    "sustainability": (COLORS["green"], "#e9f8f1"),
    "technology": ("#3567b7", "#eaf0fc"),
}

VISUAL_SYMBOLS = {
    "AIR": "AIR",
    "BARCODE": "SCAN",
    "CHECK": "OK",
    "COUNT": "STOCK",
    "DATA": "DATA",
    "FINAL": "LAST",
    "FIX": "FIX",
    "FLOW": "FLOW",
    "GREEN": "ECO",
    "MAKE": "MAKE",
    "MOVE": "MOVE",
    "PLAN": "PLAN",
    "REUSE": "REUSE",
    "ROBOT": "BOT",
    "SAFE": "SAFE",
    "SCAN": "SCAN",
    "SHIP": "SHIP",
    "SHOP": "SHOP",
    "STORE": "STORE",
    "SUPPLY": "SUPPLY",
    "TRUCK": "TRUCK",
    "USE": "USE",
}


class SupplyChainQuestApp:
    def __init__(self, root: tk.Tk, fullscreen: bool = False) -> None:
        self.root = root
        self.state = GameState()
        self.reset_job: str | None = None
        self.fullscreen = fullscreen
        self.root.title("Supply Chain Quest")
        self.root.geometry("800x480")
        self.root.minsize(800, 480)
        self.root.configure(bg=COLORS["background"])
        self.root.protocol("WM_DELETE_WINDOW", self.root.destroy)
        self.root.bind("<Escape>", self.exit_fullscreen)
        self.root.bind("<F11>", self.toggle_fullscreen)
        self.root.attributes("-fullscreen", fullscreen)
        self.root.deiconify()
        self.root.lift()
        self.root.focus_force()
        self.root.after(500, lambda: self.root.attributes("-topmost", False))
        self.root.attributes("-topmost", True)
        self.render()

    def exit_fullscreen(self, _event: tk.Event | None = None) -> None:
        self.root.attributes("-fullscreen", False)

    def toggle_fullscreen(self, _event: tk.Event | None = None) -> None:
        self.fullscreen = not bool(self.root.attributes("-fullscreen"))
        self.root.attributes("-fullscreen", self.fullscreen)

    def clear(self) -> None:
        for child in self.root.winfo_children():
            child.destroy()

    def render(self) -> None:
        if self.reset_job is not None:
            self.root.after_cancel(self.reset_job)
            self.reset_job = None
        self.clear()
        if self.state.phase == "welcome":
            self.render_welcome()
        elif self.state.phase == "complete":
            self.render_complete()
            self.reset_job = self.root.after(15000, self.reset)
        else:
            self.render_question()

    def base_frame(self, background: str = COLORS["background"]) -> tk.Frame:
        frame = tk.Frame(self.root, bg=background)
        frame.pack(fill="both", expand=True, padx=16, pady=10)
        return frame

    def label(self, parent: tk.Misc, text: str, size: int, color: str = "navy", bold: bool = False, **kwargs: object) -> tk.Label:
        weight = "bold" if bold else "normal"
        kwargs.setdefault("bg", parent.cget("bg"))
        kwargs.setdefault("fg", COLORS.get(color, color))
        kwargs.setdefault("font", ("Trebuchet MS", size, weight))
        return tk.Label(parent, text=text, **kwargs)

    def button(self, parent: tk.Misc, text: str, command: object, background: str, foreground: str = "white", **kwargs: object) -> tk.Button:
        button_options = {
            "bg": background,
            "fg": foreground,
            "activebackground": background,
            "activeforeground": foreground,
            "relief": "flat",
            "bd": 0,
            "highlightthickness": 0,
            "cursor": "hand2",
            "font": ("Trebuchet MS", 13, "bold"),
            "padx": 16,
            "pady": 9,
        }
        button_options.update(kwargs)
        return tk.Button(parent, text=text, command=command, **button_options)

    def render_welcome(self) -> None:
        frame = self.base_frame("#f5f8fc")
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        hero = tk.Canvas(frame, width=760, height=130, bg="#f5f8fc", highlightthickness=0)
        hero.grid(row=0, column=0, sticky="ew", pady=(0, 4))
        self.draw_welcome_art(hero)
        content = tk.Frame(frame, bg="#f5f8fc")
        content.grid(row=1, column=0, sticky="nsew")
        content.columnconfigure(0, weight=1)
        self.label(content, "OPEN HOUSE GAME", 8, "purple", True).grid(row=0, column=0, sticky="w", pady=(2, 2))
        title = self.label(content, "Supply Chain\nQuest", 26, "navy", True, justify="left")
        title.grid(row=1, column=0, sticky="w")
        self.label(content, "Move it. Make it. Deliver it.", 12, "muted").grid(row=2, column=0, sticky="w", pady=(5, 8))
        self.button(content, "PLAY   ->", self.start, COLORS["blue"], width=16).grid(row=3, column=0, sticky="w")
        self.label(content, "10 questions  |  Tap to start", 8, "muted").grid(row=4, column=0, sticky="w", pady=(6, 0))

    def draw_welcome_art(self, canvas: tk.Canvas) -> None:
        canvas.create_oval(650, 8, 730, 88, fill="#ffe08a", outline="")
        canvas.create_line(20, 106, 730, 106, fill="#b9d7df", width=5)
        canvas.create_line(20, 106, 730, 106, fill=COLORS["white"], width=2, dash=(12, 10))
        canvas.create_rectangle(70, 60, 138, 105, fill=COLORS["orange"], outline=COLORS["orange"])
        canvas.create_rectangle(82, 48, 126, 60, fill="#ffbd55", outline="#ffbd55")
        canvas.create_rectangle(88, 70, 105, 86, fill="#fff4c2", outline="")
        canvas.create_rectangle(110, 70, 127, 86, fill="#fff4c2", outline="")
        canvas.create_oval(78, 94, 96, 112, fill=COLORS["navy"], outline="")
        canvas.create_oval(116, 94, 134, 112, fill=COLORS["navy"], outline="")
        canvas.create_line(160, 78, 570, 78, fill=COLORS["blue"], width=4, arrow=tk.LAST)
        canvas.create_oval(250, 59, 289, 98, fill=COLORS["green"], outline="")
        canvas.create_rectangle(265, 67, 274, 91, fill=COLORS["white"], outline="")
        canvas.create_rectangle(260, 74, 279, 83, fill=COLORS["white"], outline="")
        canvas.create_rectangle(440, 48, 500, 98, fill=COLORS["purple"], outline=COLORS["purple"])
        canvas.create_rectangle(450, 38, 490, 48, fill="#a66ac0", outline="#a66ac0")
        canvas.create_rectangle(451, 60, 467, 76, fill="#f8d86c", outline="")
        canvas.create_rectangle(473, 60, 489, 76, fill="#f8d86c", outline="")
        canvas.create_text(610, 104, text="PLAN  •  MOVE  •  DELIVER", fill=COLORS["purple"], font=("Trebuchet MS", 10, "bold"))

    def render_complete(self) -> None:
        frame = self.base_frame("#f4eefa")
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        self.label(frame, "DONE!", 10, "purple", True).grid(row=0, column=0, pady=(10, 0))
        content = tk.Frame(frame, bg="#f4eefa")
        content.grid(row=1, column=0, sticky="nsew")
        content.columnconfigure(0, weight=1)
        content.rowconfigure(0, weight=1)
        score = tk.Canvas(content, width=140, height=140, bg="#f4eefa", highlightthickness=0)
        score.grid(row=0, column=0, pady=(0, 2))
        score.create_oval(10, 10, 130, 130, fill=COLORS["white"], outline=COLORS["yellow"], width=7)
        score.create_text(70, 60, text=str(self.state.score), fill=COLORS["navy"], font=("Trebuchet MS", 30, "bold"))
        score.create_text(70, 98, text=f"of {QUESTIONS_PER_GAME}", fill=COLORS["muted"], font=("Trebuchet MS", 9))
        self.label(content, "Nice work!", 27, "purple", True).grid(row=1, column=0)
        self.label(content, "You kept it moving.", 12, "muted").grid(row=2, column=0, pady=(4, 10))
        self.button(content, "PLAY AGAIN   ->", self.reset, COLORS["purple"], width=18).grid(row=3, column=0)
        self.label(content, "Resetting soon", 9, "muted").grid(row=4, column=0, pady=(7, 0))
        celebration = tk.Canvas(frame, width=300, height=34, bg="#f4eefa", highlightthickness=0)
        celebration.grid(row=2, column=0, pady=(2, 0))
        self.draw_celebration(celebration)

    def draw_celebration(self, canvas: tk.Canvas) -> None:
        for x, color in ((35, COLORS["blue"]), (85, COLORS["orange"]), (135, COLORS["green"]), (185, COLORS["yellow"]), (235, COLORS["purple"])):
            canvas.create_line(x, 28, x + 8, 8, fill=color, width=3)
            canvas.create_oval(x + 4, 4, x + 12, 12, fill=color, outline="")

    def render_question(self) -> None:
        question = current_question(self.state)
        category_color, category_soft = CATEGORY_COLORS[question.category]
        frame = self.base_frame(COLORS["background"])
        frame.columnconfigure(0, weight=1)
        header = tk.Frame(frame, bg=COLORS["background"])
        header.grid(row=0, column=0, sticky="ew")
        header.columnconfigure(0, weight=1)
        self.label(header, f"QUESTION {self.state.question_index + 1}/{QUESTIONS_PER_GAME}", 9, "purple", True).grid(row=0, column=0, sticky="w")
        self.label(header, f"{self.state.score}  points", 12, "navy", True).grid(row=1, column=0, sticky="w")
        self.label(header, f"SC  {self.state.score}", 12, "purple", True, bg=COLORS["white"], padx=8, pady=3).grid(row=0, column=1, rowspan=2, sticky="e")
        progress = tk.Canvas(frame, height=6, bg="#d9e5eb", highlightthickness=0)
        progress.grid(row=1, column=0, sticky="ew", pady=(6, 8))
        progress.bind("<Configure>", lambda event: self.draw_progress(event, progress, category_color))
        panel = tk.Frame(frame, bg=COLORS["white"], padx=12, pady=9, highlightbackground="#e2eaf0", highlightthickness=1)
        panel.grid(row=2, column=0, sticky="nsew")
        panel.columnconfigure(0, weight=1)
        self.draw_visual(panel, question.visual, category_color, category_soft)
        self.label(panel, question.category.upper(), 8, category_color, True).grid(row=1, column=0, sticky="w", pady=(4, 2))
        self.label(panel, question.prompt, 18, "navy", True, justify="left", wraplength=700).grid(row=2, column=0, sticky="w", pady=(0, 7))
        choices = tk.Frame(panel, bg=COLORS["white"])
        choices.grid(row=3, column=0, sticky="ew")
        choices.columnconfigure(0, weight=1)
        choices.columnconfigure(1, weight=1)
        for index, choice in enumerate(question.choices):
            self.render_choice(choices, question, choice.id, choice.label, index, category_color)
        if self.state.phase == "feedback":
            self.render_feedback(panel, question)

    def draw_progress(self, event: tk.Event, canvas: tk.Canvas, color: str) -> None:
        canvas.delete("all")
        width = max(1, int(event.width * (self.state.question_index + 1) / QUESTIONS_PER_GAME))
        canvas.create_rectangle(0, 0, width, event.height, fill=color, outline=color)

    def draw_visual(self, parent: tk.Frame, visual: str, color: str, soft: str) -> None:
        tile = tk.Canvas(parent, width=120, height=64, bg=soft, highlightthickness=0)
        tile.grid(row=0, column=0, sticky="w")
        tile.create_rectangle(2, 2, 118, 62, outline=color, width=2)
        if visual in {"FLOW", "SUPPLY", "USE", "MOVE", "FINAL"}:
            tile.create_oval(12, 22, 38, 48, fill=COLORS["blue"], outline="")
            tile.create_line(42, 35, 78, 35, fill=color, width=4, arrow=tk.LAST)
            tile.create_rectangle(84, 20, 108, 50, fill=COLORS["orange"], outline="")
            tile.create_line(89, 28, 103, 28, fill="#fff4c2", width=3)
            tile.create_line(89, 36, 103, 36, fill="#fff4c2", width=3)
        elif visual in {"STORE", "MAKE", "SAFE", "COUNT", "CHECK"}:
            tile.create_polygon(18, 29, 42, 12, 66, 29, fill=COLORS["purple"], outline="")
            tile.create_rectangle(25, 29, 59, 51, fill=COLORS["orange"], outline="")
            tile.create_rectangle(37, 35, 47, 51, fill="#fff4c2", outline="")
            tile.create_rectangle(76, 24, 103, 51, fill=COLORS["yellow"], outline="")
            tile.create_line(82, 32, 97, 32, fill=COLORS["navy"], width=2)
            tile.create_line(82, 40, 97, 40, fill=COLORS["navy"], width=2)
        elif visual in {"SHIP", "TRUCK", "AIR"}:
            tile.create_rectangle(17, 27, 78, 47, fill=COLORS["blue"], outline="")
            tile.create_polygon(78, 27, 97, 27, 108, 47, 78, 47, fill=COLORS["orange"], outline="")
            tile.create_rectangle(84, 31, 96, 39, fill="#dff7ff", outline="")
            tile.create_oval(28, 41, 44, 57, fill=COLORS["navy"], outline="")
            tile.create_oval(77, 41, 93, 57, fill=COLORS["navy"], outline="")
        elif visual in {"GREEN", "REUSE", "FIX"}:
            tile.create_line(59, 52, 59, 24, fill=COLORS["green_dark"], width=4)
            tile.create_oval(33, 17, 62, 40, fill=COLORS["green"], outline="")
            tile.create_oval(58, 17, 88, 40, fill=COLORS["teal"], outline="")
            tile.create_rectangle(91, 28, 106, 47, fill=COLORS["yellow"], outline="")
            tile.create_line(94, 34, 103, 34, fill=COLORS["navy"], width=2)
            tile.create_line(94, 40, 103, 40, fill=COLORS["navy"], width=2)
        else:
            tile.create_rectangle(18, 17, 48, 51, fill=COLORS["purple"], outline="")
            for x in (24, 30, 36, 42):
                tile.create_line(x, 22, x, 46, fill=COLORS["white"], width=2)
            tile.create_oval(73, 18, 103, 48, fill=COLORS["blue"], outline="")
            tile.create_rectangle(82, 45, 94, 53, fill=COLORS["blue"], outline="")

    def render_choice(self, parent: tk.Frame, question: object, choice_id: str, text: str, index: int, category_color: str) -> None:
        is_feedback = self.state.phase == "feedback"
        selected = self.state.selected_choice_id == choice_id
        correct = getattr(question, "correct_choice_id") == choice_id
        if not is_feedback:
            background, foreground, border = COLORS["white"], COLORS["navy"], COLORS["border"]
            status = ""
        elif correct:
            background, foreground, border, status = "#e9f8f1", COLORS["green_dark"], COLORS["green"], "OK"
        elif selected:
            background, foreground, border, status = "#fff0f0", COLORS["red_dark"], COLORS["red"], "X"
        else:
            background, foreground, border, status = "#f7f8f9", COLORS["muted"], COLORS["border"], ""
        choice = tk.Button(
            parent,
            text=f"{chr(65 + index)}   {text} {status}",
            command=lambda: self.choose(choice_id),
            state=tk.DISABLED if is_feedback else tk.NORMAL,
            bg=background,
            fg=foreground,
            activebackground=background,
            activeforeground=foreground,
            disabledforeground=foreground,
            relief="solid",
            bd=1,
            highlightthickness=0,
            anchor="w",
            justify="left",
            font=("Trebuchet MS", 10, "bold"),
            padx=8,
            pady=7,
            cursor="hand2",
        )
        choice.grid(row=0, column=index, sticky="ew", padx=(0 if index == 0 else 4, 4 if index == 0 else 0))
        choice.configure(highlightbackground=border)

    def render_feedback(self, parent: tk.Frame, question: object) -> None:
        correct = answer_is_correct(self.state)
        color = COLORS["green_dark"] if correct else COLORS["red_dark"]
        background = "#e9f8f1" if correct else "#fff0f0"
        feedback = tk.Frame(parent, bg=background, padx=7, pady=5)
        feedback.grid(row=4, column=0, sticky="ew", pady=(7, 0))
        feedback.columnconfigure(0, weight=1)
        headline = "YES!" if correct else "TRY AGAIN"
        self.label(feedback, headline, 13, color, True, bg=background).grid(row=0, column=0, sticky="w")
        self.label(feedback, question.explanation, 8, "navy", bg=background, wraplength=550, justify="left").grid(row=1, column=0, sticky="w")
        next_label = "SCORE   ->" if self.state.question_index == QUESTIONS_PER_GAME - 1 else "NEXT   ->"
        self.button(feedback, next_label, self.next, COLORS["purple"], width=10, font=("Trebuchet MS", 9, "bold"), padx=6, pady=4).grid(row=0, column=1, rowspan=2, padx=(7, 0))

    def start(self) -> None:
        self.state = start_game()
        self.render()

    def choose(self, choice_id: str) -> None:
        self.state = answer(self.state, choice_id)
        self.render()

    def next(self) -> None:
        self.state = next_question(self.state)
        self.render()

    def reset(self) -> None:
        self.state = reset_game()
        self.render()


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Supply Chain Quest")
    parser.add_argument("--fullscreen", action="store_true", help="Start in fullscreen kiosk mode")
    args = parser.parse_args()
    root = tk.Tk()
    SupplyChainQuestApp(root, fullscreen=args.fullscreen)
    root.mainloop()


if __name__ == "__main__":
    main()
