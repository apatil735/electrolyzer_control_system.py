import time
import simpy

class Electrolyzer:
    def __init__(self, env, capacity, pressure):
        self.env = env
        self.capacity = capacity
        self.pressure = pressure
        self.state = 'idle'
        self.action = env.process(self.run())

    def run(self):
        while True:
            yield self.env.timeout(1)
            if self.state == 'idle':
                if self.pressure < self.capacity:
                    self.state = 'electrolyzing'
                    print(f"Electrolyzer: Starting electrolysis at {self.env.now}")
                else:
                    print(f"Electrolyzer: Pressure is at capacity, cannot start electrolysis at {self.env.now}")
            elif self.state == 'electrolyzing':
                self.pressure += 1
                if self.pressure >= self.capacity:
                    self.state = 'idle'
                    print(f"Electrolyzer: Stopping electrolysis at {self.env.now}")
                else:
                    print(f"Electrolyzer: Electrolyzing at {self.env.now}, pressure: {self.pressure}")

def control_system(env, electrolyzer):
    while True:
        yield env.timeout(5)
        if electrolyzer.state == 'idle':
            if electrolyzer.pressure < electrolyzer.capacity * 0.5:
                electrolyzer.state = 'electrolyzing'
                print(f"Control System: Starting electrolysis at {env.now}")
        elif electrolyzer.state == 'electrolyzing':
            if electrolyzer.pressure >= electrolyzer.capacity * 0.9:
                electrolyzer.state = 'idle'
                print(f"Control System: Stopping electrolysis at {env.now}")

env = simpy.Environment()
electrolyzer = Electrolyzer(env, capacity=100, pressure=0)
control_process = env.process(control_system(env, electrolyzer))
env.run(until=100)
