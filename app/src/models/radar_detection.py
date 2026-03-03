# external imports
# internal imports


class RadarDetection:
    def __init__(
            self,
            radar,
            distance: float,
            facing: float,
        ):
        self.radar = radar
        self.distance = distance
        self.facing = facing

    def __repr__(self):
        return ("RadarDetection("
            f"radar={self.radar.name}, "
            f"distance={self.distance}, "
            f"facing={self.facing}"
            ")")
