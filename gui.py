import tkinter as tk
from tkinter import filedialog
import numpy as np
from PIL import ImageTk, Image
import cv2
import kara
import random

class App:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        self.window.resizable(False, False)

        self.width = 1920
        self.height = 1080

        self.canvas_width = 960
        self.canvas_height = 540

        self.relative_size = (self.canvas_width / self.width , self.canvas_height / self.height)


        self.canvas1 = tk.Canvas(window, width = self.canvas_width, height = self.canvas_height, background='#%02x%02x%02x' % (0, 0, 0))
        self.canvas1.pack(side=tk.LEFT)
        self.File = ""
        self.img = None
        self.img_displayed = None

        #self.canvas1.configure()
        #self.preview_image = np.zeros((self.canvas_height, self.canvas_width, 3), np.uint8)
        #self.blank_image = np.zeros((self.height, self.width, 3), np.uint8)
        #self.preview_image = cv2.resize(self.blank_image, (100, 50))

        #self.photo = ImageTk.PhotoImage(image=Image.fromarray(self.preview_image))
        #self.canvas1.create_image(0, 0, image=self.photo, anchor=tk.NW)
        #self.canvas1.update()

        self.scaleR = tk.Scale(window, from_=0, to=255, orient=tk.HORIZONTAL, label="Red", command=self.updateRed, width= 10, sliderlength= 15)
        self.scaleR.pack()

        self.scaleG = tk.Scale(window, from_=0, to=255, orient=tk.HORIZONTAL, label="Green", command=self.updateGreen, width= 10, sliderlength= 15)
        self.scaleG.pack()

        self.scaleB = tk.Scale(window, from_=0, to=255, orient=tk.HORIZONTAL, label="Blue", command=self.updateBlue, width= 10, sliderlength= 15)
        self.scaleB.pack()

        self.scaleSize = tk.Scale(window, from_=1, to=0.01, resolution=0.01, orient=tk.HORIZONTAL, label="Size", command=self.updateSize, width= 10, sliderlength= 15)
        self.scaleSize.set(1)
        self.scaleSize.pack()

        self.scalePosX = tk.Scale(window, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL, label="Position x", command=self.updatePositionX, width= 10, sliderlength= 15)
        self.scalePosX.set(0.5)
        self.scalePosX.pack()

        self.scalePosY = tk.Scale(window, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL, label="Position y", command=self.updatePositionY, width= 10, sliderlength= 15)
        self.scalePosY.set(0.5)
        self.scalePosY.pack()

        self.btn_save= tk.Button(window, text="Quick Save", width=15, command=self.quicksave)
        self.btn_save.pack(side=tk.BOTTOM)

        self.btn_browse1= tk.Button(window, text="Browse", width=15, command=self.loadImg)
        self.btn_browse1.pack(side=tk.BOTTOM)

        self.btn_random= tk.Button(window, text="Random Color", width=15, command=self.randomColor)
        self.btn_random.pack(side=tk.BOTTOM)

        self.window.mainloop()

    def updateRed(self, r):
        g = self.scaleG.get()
        b = self.scaleB.get()
        self.canvas1.configure(background = '#%02x%02x%02x' % (int(r), g, b))
        self.canvas1.update()
        #self.preview_image[:,:,0] = v
        #self.photo = ImageTk.PhotoImage(image=Image.fromarray(self.preview_image))
        #self.canvas1.create_image(0, 0, image=self.photo, anchor=tk.NW)

    def updateGreen(self, g):
        r = self.scaleR.get()
        b = self.scaleB.get()
        self.canvas1.configure(background = '#%02x%02x%02x' % (r, int(g), b))
        self.canvas1.update()

    def updateBlue(self, b):
        r = self.scaleR.get()
        g = self.scaleG.get()
        self.canvas1.configure(background = '#%02x%02x%02x' % (r, g, int(b)))
        self.canvas1.update()

    def loadImg(self):
        self.file = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Image files","*.jpg *.png"),("All files","*.*")))
        if self.file != "":
            self.img = cv2.cvtColor(cv2.imread(self.file, cv2.IMREAD_UNCHANGED), cv2.COLOR_BGRA2RGBA)
            self.img_displayed = cv2.resize(self.img, (0,0), fx=self.scaleSize.get() * self.relative_size[0], fy=self.scaleSize.get() * self.relative_size[1])

            centroid_y = int(self.img_displayed.shape[0]/2)
            centroid_x = int(self.img_displayed.shape[1]/2)

            self.photo1 = ImageTk.PhotoImage(image=Image.fromarray(self.img_displayed))
            self.canvas1.create_image(int(self.canvas_width*self.scalePosX.get())-centroid_x, int(self.canvas_height*self.scalePosY.get())-centroid_y, image=self.photo1, anchor=tk.NW)
            self.canvas1.update()

    def updateSize(self, v):
        if self.img is not None:
            self.img_displayed = cv2.resize(self.img, (0,0), fx=float(v) * self.relative_size[0], fy=float(v) * self.relative_size[1])
            centroid_y = int(self.img_displayed.shape[0]/2)
            centroid_x = int(self.img_displayed.shape[1]/2)
            self.photo1 = ImageTk.PhotoImage(image=Image.fromarray(self.img_displayed))
            self.canvas1.create_image(int(self.canvas_width*self.scalePosX.get())-centroid_x, int(self.canvas_height*self.scalePosY.get())-centroid_y, image=self.photo1, anchor=tk.NW)
            self.canvas1.update()

    def updatePositionX(self, x):
        if self.img_displayed is not None:
            centroid_y = int(self.img_displayed.shape[0]/2)
            centroid_x = int(self.img_displayed.shape[1]/2)
            self.photo1 = ImageTk.PhotoImage(image=Image.fromarray(self.img_displayed))
            self.canvas1.create_image(int(self.canvas_width*self.scalePosX.get())-centroid_x, int(self.canvas_height*self.scalePosY.get())-centroid_y, image=self.photo1, anchor=tk.NW)
            self.canvas1.update()

    def updatePositionY(self, y):
        if self.img_displayed is not None:
            centroid_y = int(self.img_displayed.shape[0]/2)
            centroid_x = int(self.img_displayed.shape[1]/2)
            self.photo1 = ImageTk.PhotoImage(image=Image.fromarray(self.img_displayed))
            self.canvas1.create_image(int(self.canvas_width*self.scalePosX.get())-centroid_x, int(self.canvas_height*self.scalePosY.get())-centroid_y, image=self.photo1, anchor=tk.NW)
            self.canvas1.update()

    def quicksave(self):
        if self.img is not None:
            kara.createWallpaper(self.img,(self.width, self.height),(self.scaleR.get(),self.scaleG.get(),self.scaleB.get()),(self.scalePosX.get(),self.scalePosY.get()),self.scaleSize.get())

    def randomColor(self):
        self.scaleR.set(random.randint(0, 256))
        self.scaleG.set(random.randint(0, 256))
        self.scaleB.set(random.randint(0, 256))

App(tk.Tk(), "KaraWallpaper")