#Author: Musa Nyathi

import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class CalcWindow(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        Window.size = (300,500)

        numb = [7,8,9,"+",4,5,6,"-",1,2,3,"*",".",0,"(",")","/"]
        self.numbers = self.ids.numbers

        numbc = ["C", "CA"]
        self.numbers = self.ids.numbers

        for num in numb:
            btn = Button(text=str(num),font_size = "30px", background_color = (1.0,2.0,3.0,0.6))
            btn.bind(on_release=self.cancel_numbs)
            self.numbers.add_widget(btn)

        for num in numbc:
            btn = Button(text=str(num),font_size = "30px", background_color = (1.0,0.0,0.0,1.0))
            btn.bind(on_release=self.cancel_numbs)
            self.numbers.add_widget(btn)

        eq = Button(text="=", font_size = "30px", background_color =(1.0,0.0,0.0,1.0))
        eq.bind(on_release = self.eval_numb)
        self.numbers.add_widget(eq)

    def cancel_numbs(self,instance):
        inputt = self.ids.inputt
        inputt.text += instance.text

        if instance.text == "CA":
            inputt.text = ""

        elif instance.text == "C":
            inputt.text = inputt.text[:-2]

    def eval_numb(self,text):
        inputt = self.ids.inputt
        exp  =inputt.text
        eva = eval(exp)
        inputt.text = str(eva)

class CalcApp(App):
    def build(self):
        return CalcWindow()

if __name__=="__main__":
    CalcApp().run()
