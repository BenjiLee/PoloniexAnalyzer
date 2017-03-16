import time
from Canvas import Rectangle

from autobahn.twisted.wamp import ApplicationSession
from autobahn.twisted.wamp import ApplicationRunner
from kivy import Config
from kivy.app import App
from kivy.graphics.context_instructions import Color
from kivy.support import install_twisted_reactor
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from twisted.internet import task

from poloniex_apis import public_api

install_twisted_reactor()


class PoloniexComponent(ApplicationSession):
    def onJoin(self, details):
        print("session ready", self.config.extra)
        ui = self.config.extra['ui']
        ui.on_session(self)
        self.subscribe(ui.update_gui, u"ticker")


class TickerApp(App):
    def __init__(self, **kwargs):
        super(TickerApp, self).__init__(**kwargs)

        self.previous1 = 0
        self.difference1 = 0
        self.previous2 = 0
        self.difference2 = 0
        self.previous3 = 0
        self.difference3 = 0
        self.volume = ""

    def build(self):
        self.session = None
        runner = ApplicationRunner(
            url=u"wss://api.poloniex.com:443",
            realm=u"realm1",
            extra=dict(ui=self))
        runner.run(PoloniexComponent, start_reactor=False)

        def update_volume():
            self.volume = public_api.return_chart_data(
                period=1800,
                currency_pair=self.col1_ticker_input.text,
                start=time.time() - 1801,
                end=time.time()
            )
            try:
                self.col1_volume.text = str.format('{0:.1f}', self.volume[0]["volume"])
            except KeyError as e:
                self.col1_volume.text = "Invalid Ticker"

        self.l = task.LoopingCall(update_volume)
        root = self.setup_gui()
        self.l.start(60)
        return root

    def setup_gui(self):
        """
        Setup Kivy UI.
        """
        self._setup_layout()
        return self.layout

    def on_session(self, session):
        self.session = session

    def update_gui(self, *msg, **kwargs):
        for tick in msg:
            if tick == self.col1_ticker_input.text:
                current = msg[1]
                difference = (float(current) - float(self.previous1))
                self.col1_current.text = current.strip("\n")
                self.col1_change.text = self._get_color(difference) + str.format('{0:.8f}', difference)
                if self.previous1 != 0:
                    self.difference1 += difference
                    self.col1_total_change.text = self._get_color(self.difference1) + str.format('{0:.8f}', self.difference1)
                    raw_percent = 100 * ((float(current) / (float(current) - self.difference1)) - 1)
                    formatted_percent = str.format('{0:.3f}%',
                                                   100 * ((float(current) / (float(current) - self.difference1)) - 1))
                    self.col1_percent.text = self._get_color(raw_percent) + formatted_percent
                self.previous1 = current
            elif tick == self.col2_ticker_input.text:
                current = msg[1]
                difference = (float(current) - float(self.previous2))
                self.col2_current.text = current.strip("\n")
                self.col2_change.text = self._get_color(difference) + str.format('{0:.8f}', difference)
                if self.previous2 != 0:
                    self.difference2 += difference
                    self.col2_total_change.text = self._get_color(self.difference1) + str.format('{0:.8f}', self.difference2)
                    raw_percent = 100 * ((float(current) / (float(current) - self.difference2)) - 1)
                    formatted_percent = str.format('{0:.3f}%',
                                                   100 * ((float(current) / (float(current) - self.difference2)) - 1))
                    self.col2_percent.text = self._get_color(raw_percent) + formatted_percent
                self.previous2 = current
            elif tick == self.col3_ticker_input.text:
                current = msg[1]
                difference = (float(current) - float(self.previous3))
                self.col3_current.text = current.strip("\n")
                self.col3_change.text = self._get_color(difference) + str.format('{0:.8f}', difference)
                if self.previous3 != 0:
                    self.difference3 += difference
                    self.col3_total_change.text = self._get_color(self.difference3) + str.format('{0:.8f}', self.difference3)
                    raw_percent = 100 * ((float(current) / (float(current) - self.difference3)) - 1)
                    formatted_percent = str.format('{0:.3f}%',
                                                   100 * ((float(current) / (float(current) - self.difference3)) - 1))
                    self.col3_percent.text = self._get_color(raw_percent) + formatted_percent
                self.previous3 = current

    @staticmethod
    def _get_color(number):
        if number < 0:
            return "[color=ff3333]"
        elif number > 0:
            return "[color=009900]"
        else:
            return "[color=eeeeee]"

    def _setup_layout(self):
        Config.set('graphics', 'width', '420')
        Config.set('graphics', 'height', '350')
        self._setup_col1()
        self._setup_col2()
        self._setup_col3()

        self.layout = BoxLayout(orientation='horizontal')
        self.layout.add_widget(self.col1)
        self.layout.add_widget(self.col2)
        self.layout.add_widget(self.col3)

    def _setup_col1(self):
        self.col1 = BoxLayout(orientation='vertical')

        def col1_on_enter(instance):
            self.difference1 = 0
            self.previous1 = 0
            self.col1_current.text = str(0)
            self.col1_total_change.text = str(0)
            self.col1_percent.text = "0%"
            self.col1_change.text = str(0)
            self.l.reset()

        self.col1_ticker_input = TextInput(text='BTC_DASH', multiline=False)
        self.col1_ticker_input.bind(on_text_validate=col1_on_enter)

        self.col1_current_title = Label(text='Current:')
        self.col1_current = Label(text='...', font_size='18sp')
        self.col1_change_title = Label(text='Last Change:')
        self.col1_change = Label(text='...', markup=True, font_size='18sp')
        self.col1_total_change_title = Label(text='Total Change:')
        self.col1_total_change = Label(text='...', markup=True, font_size='18sp')
        self.col1_percent_title = Label(text='Percent Change:')
        self.col1_percent = Label(text='...', markup=True, font_size='18sp')
        self.col1_volume_title = Label(text='Last 30m Volume:')
        self.col1_volume = Label(text='...', markup=True, font_size='18sp')

        def callback_col1_difference(instance, value):
            self.difference1 = 0
            self.col1_total_change.text = str(0)
            self.col1_percent.text = "0%"

        self.col1_reset_button = Button(text='Reset %', font_size=14)
        self.col1_reset_button.bind(state=callback_col1_difference)

        self.col1.add_widget(self.col1_ticker_input)
        self.col1.add_widget(self.col1_current_title)
        self.col1.add_widget(self.col1_current)
        self.col1.add_widget(self.col1_change_title)
        self.col1.add_widget(self.col1_change)
        self.col1.add_widget(self.col1_total_change_title)
        self.col1.add_widget(self.col1_total_change)
        self.col1.add_widget(self.col1_percent_title)
        self.col1.add_widget(self.col1_percent)
        self.col1.add_widget(self.col1_volume_title)
        self.col1.add_widget(self.col1_volume)
        self.col1.add_widget(self.col1_reset_button)

    def _setup_col2(self):
        self.col2 = BoxLayout(orientation='vertical')

        def col2_on_enter(instance):
            self.difference2 = 0
            self.previous2 = 0
            self.col2_current.text = str(0)
            self.col2_total_change.text = str(0)
            self.col2_percent.text = "0%"
            self.col2_change.text = str(0)
            self.l.reset()

        self.col2_ticker_input = TextInput(text='BTC_ETH', multiline=False)
        self.col2_ticker_input.bind(on_text_validate=col2_on_enter)

        self.col2_current_title = Label(text='Current:')
        self.col2_current = Label(text='...', font_size='18sp')
        self.col2_change_title = Label(text='Last Change:')
        self.col2_change = Label(text='...', markup=True, font_size='18sp')
        self.col2_total_change_title = Label(text='Total Change:')
        self.col2_total_change = Label(text='...', markup=True, font_size='18sp')
        self.col2_percent_title = Label(text='Percent Change:')
        self.col2_percent = Label(text='...', markup=True, font_size='18sp')
        self.col2_volume_title = Label(text='Last 30m Volume:')
        self.col2_volume = Label(text='...', markup=True, font_size='18sp')

        def callback_col2_difference(instance, value):
            self.difference2 = 0
            self.col2_total_change.text = str(0)
            self.col2_percent.text = "0%"

        self.col2_reset_button = Button(text='Reset %', font_size=14)
        self.col2_reset_button.bind(state=callback_col2_difference)

        self.col2.add_widget(self.col2_ticker_input)
        self.col2.add_widget(self.col2_current_title)
        self.col2.add_widget(self.col2_current)
        self.col2.add_widget(self.col2_change_title)
        self.col2.add_widget(self.col2_change)
        self.col2.add_widget(self.col2_total_change_title)
        self.col2.add_widget(self.col2_total_change)
        self.col2.add_widget(self.col2_percent_title)
        self.col2.add_widget(self.col2_percent)
        self.col2.add_widget(self.col2_volume_title)
        self.col2.add_widget(self.col2_volume)
        self.col2.add_widget(self.col2_reset_button)

    def _setup_col3(self):
        self.col3 = BoxLayout(orientation='vertical')

        def col3_on_enter(instance):
            self.difference3 = 0
            self.previous3 = 0
            self.col3_current.text = str(0)
            self.col3_total_change.text = str(0)
            self.col3_percent.text = "0%"
            self.col3_change.text = str(0)
            self.l.reset()

        self.col3_ticker_input = TextInput(text='USDT_BTC', multiline=False)
        self.col3_ticker_input.bind(on_text_validate=col3_on_enter)

        self.col3_current_title = Label(text='Current:')
        self.col3_current = Label(text='...', font_size='18sp')
        self.col3_change_title = Label(text='Last Change:')
        self.col3_change = Label(text='...', markup=True, font_size='18sp')
        self.col3_total_change_title = Label(text='Total Change:')
        self.col3_total_change = Label(text='...', markup=True, font_size='18sp')
        self.col3_percent_title = Label(text='Percent Change:')
        self.col3_percent = Label(text='...', markup=True, font_size='18sp')
        self.col3_volume_title = Label(text='Last 30m Volume:')
        self.col3_volume = Label(text='...', markup=True, font_size='18sp')

        def callback_col3_difference(instance, value):
            self.difference3 = 0
            self.col3_total_change.text = str(0)
            self.col3_percent.text = "0%"

        self.col3_reset_button = Button(text='Reset %', font_size=14)
        self.col3_reset_button.bind(state=callback_col3_difference)

        self.col3.add_widget(self.col3_ticker_input)
        self.col3.add_widget(self.col3_current_title)
        self.col3.add_widget(self.col3_current)
        self.col3.add_widget(self.col3_change_title)
        self.col3.add_widget(self.col3_change)
        self.col3.add_widget(self.col3_total_change_title)
        self.col3.add_widget(self.col3_total_change)
        self.col3.add_widget(self.col3_percent_title)
        self.col3.add_widget(self.col3_percent)
        self.col3.add_widget(self.col3_volume_title)
        self.col3.add_widget(self.col3_volume)
        self.col3.add_widget(self.col3_reset_button)


if __name__ == '__main__':
    TickerApp().run()
