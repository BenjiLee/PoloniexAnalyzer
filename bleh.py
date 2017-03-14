import Queue
from multiprocessing import Process

import utils
from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner

q = Queue.Queue()


class PoloniexComponent(ApplicationSession):
    def __init__(self, config=None):
        ApplicationSession.__init__(self, config)
        print("component created")

    def onConnect(self):
        print("transport connected")
        self.join(self.config.realm)

    def onChallenge(self, challenge):
        print("authentication challenge received")

    def onLeave(self, details):
        print("session left")

    def onOpen(self, transport):
        super(PoloniexComponent, self).onOpen(transport)


    @inlineCallbacks
    def onJoin(self, details):
        self.previous = 0

        def ticker_event(*msg, **kwargs):

            for tick in msg:
                print tick
                if tick[u"data"][u"type"] in [u'sell', u'buy']:
                    current = tick[u"data"][u'rate']
                    if current > self.previous:
                        print utils.bcolors.GREEN,
                    elif current < self.previous:
                        print utils.bcolors.RED,
                    else:
                        print utils.bcolors.END_COLOR,
                    print current, ":", str.format('{0:.7f}', (float(current) - float(self.previous)))
                    self.previous = current
                    print utils.bcolors.END_COLOR,
        yield self.subscribe(ticker_event, u'ticker')

    def onDisconnect(self):
        if reactor.running:
            reactor.stop()


class Ticker():
    def __init__(self):
        self._appRunner = ApplicationRunner(
            url=u"wss://api.poloniex.com:443",
            realm=u"realm1",
            extra=dict(ui=self))
        self._appProcess, self._tickThread = None, None

    def start(self):
        """ Start the ticker """
        print("Starting ticker")
        self._appProcess = Process(
                target=self._appRunner.run,
                args=(PoloniexComponent,)
                )
        self._appProcess.daemon = True
        self._appProcess.start()
        print('TICKER: tickPitcher process started')

    def stop(self):
        """ Stop the ticker """
        print("Stopping ticker")
        self._appProcess.terminate()
        print("Joining Process")
        self._appProcess.join()


if __name__ == '__main__':
    ticker = Ticker()
    ticker.start()
    import time
    time.sleep(10000)

