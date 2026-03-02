# external imports
from threading import Condition
# internal imports


class Monitor:
     
    def __init__(self):
        self.lock = Condition()
        self.data: list = []

    def update(self, radar, point):
        with self.lock:
            self.data.append((radar, point))
            self.lock.notify_all()
    
    def get_first(self):
        with self.lock:
            while not self.data:
                self.lock.wait()
            data = self.data.pop(0)
            return data

    def get_data(self):
        with self.lock:
            while not self.data:
                self.lock.wait()
            data = self.data.copy()
            self.data.clear()
            return data