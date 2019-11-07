from thread import Thread
from mainboard import mainboard


class AI(Thread):
    def __init__(self):
        Thread.__init__(self)
    
    def on_message(self, msg):
        print("ai received:", msg)

    def on_tick(self):
        print("process ai")
        mainboard.send_message("go left")


ai = AI()
