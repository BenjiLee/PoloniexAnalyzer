"""
All kivy setup things.
"""
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

from kivy.config import Config
Config.set('graphics','resizable',0)
from kivy.core.window import Window
Window.size = (400, 400)


def setup_layout(self):
    _setup_column1(self)
    _setup_column2(self)
    _setup_column3(self)

    self.layout = BoxLayout(orientation='horizontal')
    self.layout.add_widget(self.column1)
    self.layout.add_widget(self.column2)
    self.layout.add_widget(self.column3)


def _setup_column3(self):
    self.column3 = BoxLayout(orientation='vertical')

    def column3_on_enter(instance):
        print('User pressed enter in', instance)
    self.column3_ticker_input = TextInput(text='Enter Ticker Code', multiline=False)
    self.column3_ticker_input.bind(on_text_validate=column3_on_enter)

    self.column3_ticker = Label(text='connecting...\n')
    self.column3_difference = Label(text='...\n')
    def callback_column3_difference(instance, value):
        self.column3_difference.text = str(self.difference)
    self.column3_reset_button = Button(text='Reset %', font_size=14)
    self.column3_reset_button.bind(state=callback_column3_difference)

    self.column3.add_widget(self.column3_ticker_input)
    self.column3.add_widget(self.column3_ticker)
    self.column3.add_widget(self.column3_difference)
    self.column3.add_widget(self.column3_reset_button)


def _setup_column2(self):
    self.column2 = BoxLayout(orientation='vertical')

    def column2_on_enter(instance):
        print('User pressed enter in', instance)
    self.column2_ticker_input = TextInput(text='Enter Ticker Code', multiline=False)
    self.column2_ticker_input.bind(on_text_validate=column2_on_enter)

    self.column2_ticker = Label(text='connecting...\n')
    self.column2_difference = Label(text='...\n')

    def callback_column2_difference(instance, value):
        self.column2_difference.text = str(self.difference)
    self.column2_reset_button = Button(text='Reset %', font_size=14)
    self.column2_reset_button.bind(state=callback_column2_difference)

    self.column2.add_widget(self.column2_ticker_input)
    self.column2.add_widget(self.column2_ticker)
    self.column2.add_widget(self.column2_difference)
    self.column2.add_widget(self.column2_reset_button)


def _setup_column1(self):
    self.column1 = BoxLayout(orientation='vertical')

    def column1_on_enter(instance):
        print('User pressed enter in', instance)
    self.column1_ticker_input = TextInput(text='Enter Ticker Code', multiline=False)
    self.column1_ticker_input.bind(on_text_validate=column1_on_enter)

    self.column1_ticker = Label(text='connecting...\n')
    self.column1_difference = Label(text='...\n')

    def callback_column1_difference(instance, value):
        self.column1_difference.text = str(self.difference)
    self.column1_reset_button = Button(text='Reset %', font_size=14)
    self.column1_reset_button.bind(state=callback_column1_difference)

    self.column1.add_widget(self.column1_ticker_input)
    self.column1.add_widget(self.column1_ticker)
    self.column1.add_widget(self.column1_difference)
    self.column1.add_widget(self.column1_reset_button)
