import tkinter as tk
import numpy as np
from PIL import ImageTk, Image

class App:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        self.window.resizable(False, False)

        self.canvas1 = tk.Canvas(window, width = 960, height = 540)
        self.canvas1.pack(side=tk.LEFT)
        self.blank_image = np.zeros((1080, 1920, 3), np.uint8)

        self.photo = ImageTk.PhotoImage(image=Image.fromarray(self.blank_image))
        self.canvas1.create_image(0, 0, image=self.photo, anchor=tk.NW)
        self.canvas1.update_idletasks()

        self.scaleR = tk.Scale(window, from_=0, to=255, orient=tk.HORIZONTAL, label="Red", command=self.updateRed)
        self.scaleR.pack()
        self.scaleG = tk.Scale(window, from_=0, to=255, orient=tk.HORIZONTAL, label="Green", command=self.updateGreen)
        self.scaleG.pack()
        self.scaleB = tk.Scale(window, from_=0, to=255, orient=tk.HORIZONTAL, label="Blue", command=self.updateBlue)
        self.scaleB.pack()


        self.scaleSize = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, label="Size", command=self.updatePosition)
        self.scaleSize.pack()

        self.scalePos = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, label="Position", command=self.updatePosition)
        self.scalePos.pack()



        self.btn_save= tk.Button(window, text="Save", width=15, command=None)
        self.btn_save.pack(side=tk.BOTTOM)

        self.btn_preview = tk.Button(window, text="Preview", width=15, command=None)
        self.btn_preview.pack(side=tk.BOTTOM)

        self.btn_browse1= tk.Button(window, text="Browse", width=15, command=None)
        self.btn_browse1.pack(side=tk.BOTTOM)
        self.window.mainloop()

    def updateRed(self, v):
        print(v)

    def updateGreen(self, v):
        print(v)

    def updateBlue(self, v):
        print(v)

    def updatePosition(self, v):
        print(v)

App(tk.Tk(), "KaraWallpaper")