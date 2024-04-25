import tkinter as tk
from tkinter import messagebox
import time

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")

        self.time_label = tk.Label(root, text="", font=("Helvetica", 48))
        self.time_label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        self.remaining_time = 0
        self.running = False

    def start_timer(self):
        if not self.running:
            self.remaining_time = 60  # 60 seconds countdown
            self.running = True
            self.update_timer()

    def stop_timer(self):
        if self.running:
            self.running = False
            self.stop_button.config(state=tk.DISABLED)

    def update_timer(self):
        if self.running:
            if self.remaining_time <= 0:
                messagebox.showinfo("Countdown Timer", "Time's up!")
                self.running = False
                self.stop_button.config(state=tk.DISABLED)
            else:
                self.time_label.config(text=str(self.remaining_time))
                self.remaining_time -= 1
                self.root.after(1000, self.update_timer)
                self.stop_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    timer = CountdownTimer(root)
    root.mainloop()
