"""Minimal Tkinter display test for the Raspberry Pi 7-inch Touch Display."""

import argparse
import tkinter as tk


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480


def main() -> None:
    parser = argparse.ArgumentParser(description="Test the Raspberry Pi 7-inch Touch Display with Tkinter")
    parser.add_argument("--fullscreen", action="store_true", help="Fill the active display")
    args = parser.parse_args()

    root = tk.Tk()
    root.title("Raspberry Pi Touch Display Test")
    root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
    root.resizable(False, False)
    root.configure(bg="#032147")
    root.attributes("-fullscreen", args.fullscreen)
    root.bind("<Escape>", lambda _event: root.destroy())

    message = tk.Label(
        root,
        text="Hello World",
        bg="#032147",
        fg="#ffffff",
        font=("Trebuchet MS", 28, "bold"),
    )
    message.pack(expand=True)

    root.update_idletasks()
    root.deiconify()
    root.lift()
    root.focus_force()
    root.mainloop()


if __name__ == "__main__":
    main()
