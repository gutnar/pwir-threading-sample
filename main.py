from ai import ai
from vision import vision
from mainboard import mainboard

# Start all threads
mainboard.start()
vision.start()
ai.start()

# Close all threads
ai.join()
vision.join()
mainboard.join()
