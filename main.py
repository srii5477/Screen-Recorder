import pyautogui
import numpy as np
import cv2
import keyboard
import typer
from rich import print as rprint
import os

app = typer.Typer()

@app.command("Start")
def func():
    rprint("[blink cyan bold] Welcome to ScreenRec 1.0 [/blink cyan bold] [red bold] Press y to get started or q to quit [/red bold]")
    cmd = input("Enter y to get started: ")
    if cmd == 'q':
        rprint("[magenta bold] Thank you for trying out ScreenRec! [/magenta bold]")
    elif cmd == 'y':
        # create a video writer object
        resolution = (1920, 1080)

        # specify how to compress & encode the video
        code = cv2.VideoWriter_fourcc(*"XVID")

        # name the output 
        name = "ScreenRec.avi"

        # specify frame rate, will experiment with it to obtain the best result
        fps = 60

        obj = cv2.VideoWriter(name, code, fps, resolution)


        while True:
            # take a ss
            ss = pyautogui.screenshot()
        
            # convert the screenshot to a numpy array
            frame = np.array(ss)
        
            # default opencv capture is in bgr color scheme (inverted)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # write it to the output file
            
            obj.write(frame)
            
            if keyboard.is_pressed('q'):
                rprint("[magenta bold] Your recording has been saved. Thanks for using ScreenRec! [/magenta bold]")
                break 

        # discard video writer object and close windows   
        cv2.destroyAllWindows

        obj.release()
        
app()

    
    

