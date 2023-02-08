from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import random

class MyApp(App):
    def build(self):
        self.HR_list = []
        self.start_time = 0
        self.start_time = self.start_time + 1

        layout = BoxLayout(orientation='vertical')
        label = Label(text='Panic Attack Detection', font_size='30sp')
        layout.add_widget(label)
        button1 = Button(text='Newest HR', size_hint=(0.2, 0.1))
        button1.bind(on_press=self.display_newest_hr)
        layout.add_widget(button1)
        button2 = Button(text='Risk', size_hint=(0.2, 0.1))
        button2.bind(on_press=self.display_risk)
        layout.add_widget(button2)
        button3 = Button(text='Call Carer', size_hint=(0.2, 0.1))
        button3.bind(on_press=self.call_carer)
        layout.add_widget(button3)

        return layout

    def update_hr_list(self):
        current_time = self.start_time
        if current_time >= 50:
            return
        HR = random.randint(50, 120)
        self.HR_list.append(HR)
    
    def display_newest_hr(self, instance):
        newest_hr = self.HR_list[-1] if self.HR_list else "No HR data available"
        print(f"Newest HR value: {newest_hr}")

    def display_risk(self, instance):
        if not self.HR_list:
            print("No HR data available")
        else:
            avg_hr = sum(self.HR_list[-5:]) / 5
            risk = "Low" if avg_hr <= 100 else "High"
            print(f"Risk level: {risk}")
        
    def call_carer(self, instance):
        print("Calling carer...")

if __name__ == '__main__':
    MyApp().run() 
