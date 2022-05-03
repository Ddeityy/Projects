#Track a purple blob and output the center of the contour as x, y for After Effects tracking.

import tkinter as tk
from tkinter import ttk
import os
import glob
import numpy as np
import cv2 as cv
from tkinterdnd2 import DND_FILES, TkinterDnD

#HSV colors
lower = np.array([130, 150, 20])
higher = np.array([150, 255, 255])

frames = open(r"PurpleTracker\frames.txt", "w")
path = r"C:\Users\ddeit\Desktop\pythonProject\PurpleTracker\frames"


def process_frames():
    frames.write("txt = [];\n")
    txt['text']='0/0'
    process_box['text'] = "Processing..."
    counter = 0
    for f in range(1283):
        img = cv.imread(os.path.join(path, f'frame{f}.jpg'))
        image = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        mask = cv.inRange(image, lower, higher)
        conts, hier = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        root.update_idletasks()
        txt['text']=f'{counter}/{int(1283)}'
        counter+=1
        cv.waitKey()
        if len(conts) != 0:
            for cont in conts:
                M = cv.moments(cont)           
                if M['m00'] != 0:
                    cx = int(M['m10']/M['m00'])
                    cy = int(M['m01']/M['m00'])
                    if int(cv.contourArea(cont)) > 200:
                        frames.write(f"txt[{counter}] = [{cx}, {cy}];\n")
                    else:
                        frames.write(f"txt[{counter}] = [3000, 3000]; area <200\n")
        else:
            frames.write(f"txt[{counter}] = [3000, 3000]; len = 0\n")
            
    txt['text'] = 'Done'
    process_box['text'] = "Drop the file here"
    for f in path:
        os.remove(f)
   
def process_video(event):
    video = cv.VideoCapture(event.data)
    global frame_total
    frame_total = int(video.get(cv.CAP_PROP_FRAME_COUNT))
    process_box['text'] = "Extracting..."
    success, image = video.read()
    counter = -1
    while success:
        counter += 1
        print(f"frame {counter} extracted")
        cv.imwrite(os.path.join(path, f'frame{counter}.jpg'), image)     # save frame as JPEG file      
        success,image = video.read()
        root.update_idletasks()
        txt['text']=f'{counter}/{int(frame_total-2)}'
        cv.waitKey()
        
    process_frames()
         
#GUI
root = TkinterDnD.Tk()
root.title("Purple Tracker")
root.geometry("300x200")
root.resizable(0, 0)
root.columnconfigure(0, weight=1)

process_box = tk.Label(
    root,
    text="Drop the file here",
    height=9,
    width=20,
    bg="grey"
)
process_box.pack()
process_box.drop_target_register(DND_FILES)
process_box.dnd_bind("<<Drop>>", process_video)
process_box.grid(column=0, row=0, sticky='', padx=5, pady=5)
        
txt = tk.Label(
    root,
    text = '0/0',
    bg = '#345',
    fg = '#fff'

)
txt.grid(column=0, row=1, sticky=tk.S, padx=0, pady=0)

process_frames()

root.mainloop()



