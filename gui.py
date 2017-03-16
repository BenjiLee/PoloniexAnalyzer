import time

from kivy.app import App

from kivy.support import install_twisted_reactor
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from poloniex_apis import public_api
from twisted.internet import task

install_twisted_reactor()

from autobahn.twisted.wamp import ApplicationSession
from autobahn.twisted.wamp import ApplicationRunner


class PoloniexComponent(ApplicationSession):
    def onJoin(self, details):
        print("session ready", self.config.extra)
        ui = self.config.extra['ui']
        ui.on_session(self)
        self.subscribe(ui.print_message, u"ticker")


class TickerApp(App):
    def __init__(self, **kwargs):
        super(TickerApp, self).__init__(**kwargs)

        self.previous = 0
        self.difference = 0
        self.ticker = ""
        self.volume = ""

    def build(self):
        self.session = None
        runner = ApplicationRunner(
            url=u"wss://api.poloniex.com:443",
            realm=u"realm1",
            extra=dict(ui=self))
        runner.run(PoloniexComponent, start_reactor=False)

        def update_volume():
            if self.ticker:
                self.volume = public_api.return_chart_data(
                    period=1800,
                    currency_pair=self.ticker,
                    start=time.time()-1801,
                    end=time.time()
                )
                try:
                    self.col1_volume.text = str.format('{0:.1f}', self.volume[0]["volume"])
                except Exception as e:
                    print self.ticker
                    print self.volume
        self.l = task.LoopingCall(update_volume)
        self.l.start(60)

        # setup the Kivy UI
        root = self.setup_gui()
        return root

    def setup_gui(self):
        """
        Setup Kivy UI.
        """
        self._setup_layout()
        return self.layout

    def on_session(self, session):
        self.session = session

    def print_message(self, *msg, **kwargs):
        """
        Called from WAMP app component when message was received in a PubSub event.
        """
        for tick in msg:
            if tick == self.col1_ticker_input.text:
                self._popluate_gui(msg)

    def _popluate_gui(self, msg):
        current = msg[1]
        difference = (float(current) - float(self.previous))
        self.col1_current.text = current.strip("\n")
        self.col1_change.text = self._get_color(difference) + str.format('{0:.8f}', difference)
        if self.previous != 0:
            self.difference += difference
            self.col1_total_change.text = self._get_color(self.difference) + str.format('{0:.8f}', self.difference)
            raw_percent = 100 * ((float(current) / (float(current) - self.difference)) - 1)
            formatted_percent = str.format('{0:.3f}%', 100 * ((float(current) / (float(current) - self.difference)) - 1))
            self.col1_percent.text = self._get_color(raw_percent) + formatted_percent
        self.previous = current

    def _get_color(self, number):
        if number < 0:
            return "[color=ff3333]"
        elif number > 0:
            return "[color=009900]"
        else:
            return "[color=eeeeee]"

    import kivy
    kivy.require('1.9.0')

    from kivy.config import Config
    Config.set('graphics', 'width', '175')
    Config.set('graphics', 'height', '350')

    def _setup_layout(self):
        self._setup_col1()
        self.layout = BoxLayout(orientation='horizontal')
        self.layout.add_widget(self.col1)

    def _setup_col1(self):
        self.col1 = BoxLayout(orientation='vertical')

        def col1_on_enter(instance):
            self.ticker = self.col1_ticker_input.text
            self.difference = 0
            self.previous = 0
            self.col1_current.text = str(0)
            self.col1_total_change.text = str(0)
            self.col1_percent.text = "0%"
            self.col1_change.text = str(0)
        self.col1_ticker_input = TextInput(text='BTC_DASH', multiline=False)
        self.ticker = self.col1_ticker_input.text
        self.col1_ticker_input.bind(on_text_validate=col1_on_enter)

        self.col1_current_title = Label(text='Current:')
        self.col1_current = Label(text='...', font_size='20sp')
        self.col1_change_title = Label(text='Last Change:')
        self.col1_change = Label(text='...', markup=True, font_size='20sp')
        self.col1_total_change_title = Label(text='Total Change:')
        self.col1_total_change = Label(text='...', markup=True, font_size='20sp')
        self.col1_percent_title = Label(text='Percent Change:')
        self.col1_percent = Label(text='...', markup=True, font_size='20sp')
        self.col1_volume_title = Label(text='30-Minute Volume:')
        self.col1_volume = Label(text='...', markup=True, font_size='20sp')

        def callback_col1_difference(instance, value):
            self.difference = 0
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


if __name__ == '__main__':
    TickerApp().run()
