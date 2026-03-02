# external imports
from threading import Thread, Event
from time import sleep
# internal imports
from src.actors.monitor import Monitor


class Lector(Thread):
    
    def __init__(self, monitor: Monitor):
        super().__init__()
        self._stop_event = Event()
        self.monitor = monitor
        
    def run(self):
        while not self._stop_event.is_set():
            print(f"Número de detecciones: {len(self.monitor.get_data())}")
            sleep(2)
            
    def stop(self):
        self._stop_event.set()