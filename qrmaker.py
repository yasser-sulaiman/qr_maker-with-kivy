import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import qrcode as qr


class Layout(GridLayout):
    # runs on initialization
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 2  # used for our grid

        self.add_widget(Label(text='Link:'))  # widget #1, top left
        self.link = TextInput(text='', multiline=True)  # defining self.ip...
        self.add_widget(self.link) # widget #2, top right

        self.add_widget(Label(text='Name of QR:'))
        self.name = TextInput(text='', multiline=False)
        self.add_widget(self.name)


        # add our button.
        self.save_button = Button(text="Save")
        self.save_button.bind(on_press=self.save_func)
        self.add_widget(Label())  # just take up the spot.
        self.add_widget(self.save_button)

    def save_func(self, instance):
        image = qr.make(self.link.text)
        image_name = self.name.text + '.png'
        image.save('qrs/'+ image_name,'PNG')
        self.link.text=''
        self.name.text=''

class QrMaker(App):
    def build(self):
        return Layout()

if __name__ =="__main__":
    QrMaker().run()
