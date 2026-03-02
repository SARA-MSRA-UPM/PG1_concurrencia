# external imports
import threading
from time import sleep
# internal imports
from src.actors.points.circular_point import CircularPoint
from src.actors.points.eight_point import EightPoint
from src.actors.points.point import Point
from src.actors.radar import Radar
from src.actors.lector import Lector
from src.actors.monitor import Monitor


if __name__ == '__main__':
    # Constants
    AREA=200

    # Initialize monitor
    detections_monitor = Monitor()

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
        monitor=detections_monitor
    )

    # Start radar and point threads
    radar.start()

    for point in points:
        point.start()

    # Create and start lector
    detections_lector = Lector(monitor=radar.monitor)
    detections_lector.start()

    # Wait 10 seconds of execution
    sleep(10)

    # Stop all threads
    detections_lector.stop()
    detections_lector.join()

    radar.stop()
    radar.join()

    for point in points:
        point.stop()
        point.join()

    exit(0)
