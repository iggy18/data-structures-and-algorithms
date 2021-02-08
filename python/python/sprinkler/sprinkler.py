class Sprinkler:
    def __init__(self, usage=2):
        self.usage = usage
        self.left_line = None
        self.right_line = None

class SprinklerSystem:
    def __init__(self):
        self.inlet = None

    def get_usage(self):
        water = []
        def flush_system(sprinkler):
            if not sprinkler:
                return
            water.append(sprinkler.usage)
            flush_system(sprinkler.left_line)
            flush_system(sprinkler.right_line)
        flush_system(self.inlet)
        return sum(water)





















































