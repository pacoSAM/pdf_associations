from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button


def error_popup():
    """popup window for error"""
    content = Button(text='\n\t1:Please You can only select images or pdf files\n\t2:One of your files is corrupt\n\nClick here to continue!!',
                     pos_hint={'down': 1},
                     size_hint=(1, 0.30),
                     background_color=(1.0, 0.0, 0.0, 1.0))
    pt = Popup(title='Something Wrong during process:',
               content=content, size_hint=(None, None), size=(400, 400),)
    content.bind(on_press=pt.dismiss)
    pt.open()


def ok_popup(file_name):
    """popup window for correct size"""
    content = Button(text='%s is creat' % file_name,
                     pos_hint={'down': 1},
                     size_hint=(1, 0.30),
                     background_color=(0.0, 1.0, 0.0, 1.0))
    pt = Popup(title='Convertion Done', content=content,
               size_hint=(None, None), size=(400, 400),)
    content.bind(on_press=pt.dismiss)
    pt.open()
