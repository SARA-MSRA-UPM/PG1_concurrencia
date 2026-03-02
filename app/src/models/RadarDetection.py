# external imports
# internal imports


class RadarDetection:
    def __init__(
            self,
            radar_name: str,
            distance: float,
            facing: float,
        ):
        self.radar_name = radar_name
        self.distance = distance
        self.facing = facing

    def __repr__(self):
        return ("RadarDetection("
            f"radar_name={self.radar_name}, "
            f"distance={self.distance}, "
            f"facing={self.facing}"
            ")")
