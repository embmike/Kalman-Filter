import numpy as np
from numpy.linalg import multi_dot as mm
from numpy import add as ma
from numpy import subtract as ms
from numpy.linalg import inv as miv
from numpy import identity as mid


class Kalman(object):
    ''' Kalman filter

        State-transition equation:  xp = F * x + w
        Measurement equation:       z  = H * xp + v

        x  : State vector
        z  : Measurement vector
        w  : Process noise
        v  : Measurement noice
        F  : State space matrix
        H  : Measurement matrix
        Q  : Covariance of the process noise
        R  : Covariance of the measurement noise
        P  : Error covariance matrix
        K  : Kalman gain matrix
        xp : Predicted state vector
        Pp : Predicted error covariance matrix
        x0 : Initial state vector
        P0 : Initial error covariance matrix

    '''


    def __init__(self, x0, P0, F, H, Q, R):

        self.x = x0
        self.P = P0
        self.F = F
        self.H = H
        self.Q = Q
        self.R = R

        self.P_list = []
        self.K_list = []


    def filter(self, z):

        # Prediction
        # xp = F * x
        self.xp = mm([self.F, self.x])

        # Pp = F * P * F' + Q
        self.Pp = ma(mm([self.F, self.P, self.F.transpose()]), self.Q)

        # Update prediction
        # S = H * Pp * H' + R
        self.S = ma(mm([self.H, self.Pp, self.H.transpose()]), self.R)

        # K = Pp * H' * S^-1
        self.K = mm([self.Pp, self.H.transpose(), miv(self.S)])
        self.K_list.append(self.K[1][0])

        # y = z - H * xp
        self.y = ms(z, mm([self.H, self.xp]))

        # x = xp + K * y
        self.x = ma(self.xp, mm([self.K, self.y]))

        # P = (I - K * H) * Pp'
        I = mid(self.K.shape[0])
        self.P = mm([ms(I, mm([self.K, self.H])), self.Pp.transpose()])
        self.P_list.append(self.P[1][1])

        return self.x.tolist()
