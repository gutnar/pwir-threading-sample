from thread import Thread


class Vision(Thread):
    def __init__(self):
        Thread.__init__(self)
    
    def on_message(self, msg):
        print("vision received:", msg)

    def on_tick(self):
        # TODO: read frame and process it
        print("procession vision")


vision = Vision()
