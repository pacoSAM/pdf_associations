# import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from helper_pdf import *
from helper_popup_window import *
from creat_repo import *

import os


class MyPdfWidget(BoxLayout):

    def __init__(self, **kwargs):
        super(MyPdfWidget, self).__init__(**kwargs)
        self.filename = ""
        self.popwindow = ""

    def open(self, path, filename):
        """Combin in One file button"""
        self.filename = filename
        if len(self.filename) > 0:
            if check_format(self.filename) == False:
                error_popup()
            else:
                content = TextInput(
                    pos_hint={'down': 1},
                    size_hint=(1, 0.30),
                    multiline=False,
                )
                self.popwindow = Popup(title='Named your file',
                                       content=content,
                                       size_hint=(None, None),
                                       size=(400, 400),)
                content.bind(on_text_validate=self.MainPopup_combine)
                self.popwindow.open()

    def image_to_pdf(self, path, filename):
        nfile_in_repo = len(os.listdir(os.getcwd()))
        self.filename = filename
        if len(self.filename) > 0:
            if check_format(self.filename) == False:
                error_popup()
            else:
                for file in self.filename:
                    convert_image_to_pdf(file, "pdf")
                ok_popup("file")

                if len(os.listdir(os.getcwd())) > nfile_in_repo:
                    ok_popup("your file ")

    def MainPopup_combine(self, instance):
        """Text input and main for combinaison"""
        outfilename = os.path.splitext(instance.text)[0] + ".pdf"
        combine_in_one_pdf(self.filename, outfilename)
        self.popwindow.dismiss()
        ok_popup(outfilename)

    def selected(self, filename):
        pass


class MyPdfApp(App):

    def build(self):
        self.title = 'PDF COMBINE'
        self.icon = 'PDF.png'
        return MyPdfWidget()

if __name__ == '__main__':
    chek_existdir("PDF_COMBINE")
    # os.chdir(os.getcwd() + "/PDF_COMBINE")
    MyPdfApp().run()
