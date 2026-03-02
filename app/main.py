# external imports
import threading
from time import sleep
# internal imports
from src.actors.points.circular_point import CircularPoint
from src.actors.points.eight_point import EightPoint
from src.actors.radar import Radar


if __name__ == '__main__':
    # Constants
    AREA=200

    # Create points
    points = [
        CircularPoint(75, 75, 10),
        CircularPoint(150, 150, 20),
        EightPoint(100, 125),
    ]

    # Create radar
    radar = Radar(
        name="radar0",
        position=(AREA/2, AREA/2),
        detection_range=(AREA/2)*0.6,
        orientation=0,
        points=points,
    )

    # Start radar and point threads
    radar.start()

    for point in points:
        point.start()

    # Wait 10 seconds of execution
    sleep(10)

    # Stop all threads
    radar.stop()
    radar.join()

    for point in points:
        point.stop()
        point.join()

    exit(0)
