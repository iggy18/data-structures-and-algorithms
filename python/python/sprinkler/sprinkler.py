class Sprinkler:
    def __init__(self, usage=2):
        self.usage = usage
        self.left_line = None
        self.right_line = None

class SprinklerSystem:
    def __init__(self):
        self.inlet = None

    def get_usage(self, sprinkler_system):
        if not self.sprinkler_system:
            return 0
        usage = 0
        def flush_system(sprinkler):
            if not sprinkler:
                return
            usage += sprinkler.usage
            flush_system(sprinkler.left_line)
            flush_system(sprinkler.right_line)
        return usage





















































