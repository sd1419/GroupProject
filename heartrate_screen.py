
# importing all necessary modules
# MDApp, MDLabel Screen, MDTextField
# and MDRectangleFlatButton
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton
import time
import random


# creating Demo Class(base class)
class Demo(MDApp):

    def build(self):
        screen = Screen()

        start_time = time.time()
        HR_list = []

        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time
            if elapsed_time >= 50:
                break
        HR = random.randint(50, 120)
        HR_list.append(HR)

        with open("HR_database.txt", "a") as file:
            file.write("Time: " + str(current_time) + "  HR: " + str(HR) + "\n")

        color = (0, 1, 0, 1) if all(x <= 100 for x in HR_list[-5:]) else (1, 0, 0, 1)
        btn2.background_color = color
        time.sleep(5)

        # defining label with all the parameters
        l = MDLabel(text="Panic Attack Detection", halign='center',
                    theme_text_color="Custom",
                    text_color=(0.5, 0, 0.5, 1),
                    font_style='Caption')

        # defining Button1 with all the parameters
        btn1 = MDRectangleFlatButton(text="display current heart rate values", pos_hint={
                                    'center_x': 0.5, 'center_y': 0.8},
                                    on_release=self.btnfunc1)
                                    
        btn2 = MDRectangleFlatButton(text="Risk", pos_hint={
                                    'center_x': 0.5, 'center_y': 0.6},
                                    on_release=self.btnfunc2) 
         
        # defining Button2 with all the parameters
        btn3 = MDRectangleFlatButton(text="Call carer", pos_hint={
                                    'center_x': 0.5, 'center_y': 0.3},
                                    on_release=self.btnfunc3)
        # adding widgets to screen
        screen.add_widget(btn1)
        screen.add_widget(btn2)
        screen.add_widget(btn3)
        screen.add_widget(l)
        # returning the screen
        return screen


    # defining a btnfun() for the button to
    # call when clicked on it
    def btnfunc1(self, obj):
        print("button1 is pressed!!")
    def btnfunc2(self, obj):
        print("button2 is pressed!!")
    def btnfunc3(self, obj):
        print("button3 is pressed!!")
    
if __name__ == "__main__":
    Demo().run()