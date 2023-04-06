import os
import random
import tkinter as tk
from tkinter import filedialog
import moviepy.editor as mp

from moviepy.video.io.VideoFileClip import VideoFileClip
import time

import struct
print(struct.calcsize("P") * 8)


class RandomVideoPlayer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Random Video Player")
        self.selected_video_label = tk.Label(self.window, text="")
        self.selected_video_label.grid(row=2, column=0, columnspan=2)

        self.directory_path = tk.StringVar()
        self.file_list = []

        # Create the directory selection label and button
        tk.Label(self.window, text="Select a directory:").grid(row=0, column=0)
        tk.Button(self.window, text="Browse", command=self.browse_directory).grid(row=0, column=1)

        # Create the play button
        tk.Button(self.window, text="Play", command=self.play_random_video).grid(row=1, column=0, columnspan=2)
        
        # Create the pause/play button
        self.play_button = tk.Button(self.window, text="Pause/Play", command=self.play_pause_video)
        self.play_button.grid(row=4, column=0, columnspan=2)

        # Create empty row
        tk.Label(self.window, text="").grid(row=3, column=0)

        self.window.mainloop()

    def play_pause_video(self):
        if not hasattr(self, 'clip'):
            # Choose a random video file from the file list
            video_file = random.choice(self.file_list)

            # Load the video file into a VideoFileClip object without audio
            self.clip = VideoFileClip(video_file, audio=False)
            self.selected_video_label.config(text=f"Selected video: {os.path.basename(video_file)}")
            self.play_button.config(text="Pause")
            self.clip.preview()

        elif self.clip.reader.is_playing():
            self.clip.reader.pause()
            self.play_button.config(text="Play")

        else:
            self.clip.reader.play()
            self.play_button.config(text="Pause")
            while self.clip.reader.is_playing():
                self.window.update()
                time.sleep(0.01)


    def browse_directory(self):
        # Open a dialog box to select a directory
        self.directory_path.set(filedialog.askdirectory())

        # Update the file list with all video files in the directory
        self.file_list = [os.path.join(self.directory_path.get(), file) for file in os.listdir(self.directory_path.get()) if file.endswith((".mp4", ".avi", ".mkv"))]

    

    def play_random_video(self):
        # Choose a random video file from the file list
        video_file = random.choice(self.file_list)

        # Load the video file into a VideoFileClip object without audio
        clip = mp.VideoFileClip(video_file, audio=False)

        self.selected_video_label.config(text=f"Selected video: {os.path.basename(video_file)}")

        # Play the video file
        clip.preview()


if __name__ == "__main__":
    RandomVideoPlayer()
