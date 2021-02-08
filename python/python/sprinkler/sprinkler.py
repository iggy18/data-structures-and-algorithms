# Problem domain: Estimate water usage for a sprinkler system.The sprinkler system is made of an inlet and a number of connected sprinkler heads that spray water. Each single spinkler head has a T connection that can be connected to 0, 1, or 2 other sprinklers.Each sprinkler head is configured for a certain amount of output, each potentially different, in millileters per minute

'''
algo:
create empty array for node values
create helper function that takes in systems root
add roots value to array
recurse to the left line
recurse to the right line
return the sum of the values in the array
'''


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





















































