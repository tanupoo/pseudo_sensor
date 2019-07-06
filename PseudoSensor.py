import random

class PseudoSensor():
    """
    init_val:
    max_val:
    min_val:
    max_delta: maximum number of value that is incremented or decremented.
    max_steps: maximum times that the value is incremented or decremented.
    init_sign: direction to up or down.
    """
    def __init__(self, init_val=20, max_val=40, min_val=10,
                 max_delta=3, max_steps=10, init_sign=1):
        self.max_delta = max_delta
        self.max_steps = max_steps
        if init_val > max_val:
            raise ValueError("init_val is bigger than max_val. {} > {}"
                             .format(init_val, max_val))
        if init_val < min_val:
            raise ValueError("init_val is smaller than min_val. {} < {}"
                             .format(init_val, min_val))
        self.max_val = max_val
        self.min_val = min_val
        self.val = init_val
        if init_sign not in [1, -1]:
            raise ValueError("init_sign is not 1 or -1.")
        else:
            self.sign = init_sign
        #
        self.init_state()

    def init_state(self):
        self.sign = random.choice([1, -1])
        self.delta = self.sign * random.randint(1, 1 + self.max_delta)
        self.steps = random.randint(1, 1 + self.max_steps)

    def next(self):
        self.steps -= 1
        if self.steps < 0:
            self.init_state()
        while True:
            v = self.val + self.delta
            if v >= self.min_val and v <= self.max_val:
                self.val = v
                break
            self.init_state()
        return self.val

    def __next__(self):
        return self.next()

if __name__ == "__main__":
    import time
    from datetime import datetime, timedelta
    s = PseudoSensor(init_val=24, max_val=40, min_val=22, max_delta=1,
                     max_steps=1, init_sign=1)
    ts = datetime.now()
    t = 0
    while True:
        print((ts+timedelta(seconds=t)).isoformat(), s.next())
        t += 1
        time.sleep(1)

