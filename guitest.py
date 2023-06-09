import tkinter as tk
from tkinter import ttk
from PIL import Image

class ScrollableFrame(tk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

class SongApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Song App")
        self.root.geometry("800x600")

        self.left_frame = tk.Frame(self.root)
        self.left_frame.pack(side="left", fill="both", expand=True)

        self.scrollable_frame = ScrollableFrame(self.root)
        self.scrollable_frame.pack(side="right", fill="both", expand=True)

        self.add_songs()

    def add_songs(self):
        for i in range(10):
            song_frame = tk.Frame(self.scrollable_frame.scrollable_frame, bg="white", padx=10, pady=10)
            song_frame.pack(padx=10, pady=10, fill="x")

            song_label = tk.Label(song_frame, text=f"Song {i+1}", bg="white")
            song_label.pack(side="left")

            play_button = tk.Button(song_frame, text="Play")
            play_button.pack(side="left", padx=5)

            pause_button = tk.Button(song_frame, text="Pause")
            pause_button.pack(side="left", padx=5)

            progress_bar = ttk.Progressbar(song_frame, orient="horizontal", length=200, mode="determinate")
            progress_bar.pack(side="left", padx=5)

root = tk.Tk()
app = SongApp(root)
root.mainloop()
