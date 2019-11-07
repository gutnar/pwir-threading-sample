from thread import Thread
from ai import ai


class Vision(Thread):
    def __init__(self):
        Thread.__init__(self)

        # Open video capture
        # self.cap = cv2.VideoCapture()

    def on_message(self, msg):
        print("vision received:", msg)

    def on_tick(self):
        # TODO: read frame and process it
        # frame = self.cap.read()

        # Send processed frame results to AI
        ai.send_message({
            "closest_ball_coordinates": (50, 100)
        })


vision = Vision()
