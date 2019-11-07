from thread import Thread


class Mainboard(Thread):
    def __init__(self):
        Thread.__init__(self)
    
    def on_message(self, msg):
        print("mainboard received:", msg)

    def on_tick(self):
        print("process mainboard")


mainboard = Mainboard()
