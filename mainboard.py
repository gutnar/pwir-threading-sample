from thread import Thread


class Mainboard(Thread):
    def __init__(self):
        Thread.__init__(self)

        # Open serial port
        # self.serial = pyserial.open or something

        # Last command from AI, initially no command
        self.last_command = None
    
    def on_message(self, msg):
        print("mainboard received:", msg)
        self.last_command = msg

    def on_tick(self):
        # Do nothing when no command has been received
        if self.last_command == None:
            return

        # Send command over serial
        # self.serial.send(self.last_command) or something
        print("mainboard tick:", self.last_command)


mainboard = Mainboard()
