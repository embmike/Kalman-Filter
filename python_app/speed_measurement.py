import numpy as np

# Simulated speed measurement
class Measurement:
    '''Simulated speed measurement

        position:       the true train position in m
        speed:          the measured train speed in in m/s
        dt:             the sampling rate in s
        const_speed:    the constant train speed without acceleration in m/s
    '''

    def __init__(self, position, speed, dt):
        self.position = position
        self.speed = speed
        self.dt = dt
        self.const_speed = speed


    def rand(self):
        return np.random.randn()


    def measure(self):
        '''Train speed measurement
        '''

        # simulated measurement noise in m
        v = 0 + 10 * self.rand()

        # True position in m
        self.position = self.position + self.speed * self.dt

        # Measured speed inclusive measurement noise in m/s
        self.speed = self.const_speed + v

        Z = []
        Z.append([self.speed])

        return Z