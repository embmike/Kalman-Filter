import numpy as np
from matplotlib import pyplot as plt
from kalman_filter import Kalman
from speed_measurement import Measurement


if __name__ == '__main__':

    # Sampling rate in s
    dt = 0.1

    # Periode of time
    time_peride = np.arange(0., 10.1, 0.1).tolist()

    # Process matrix
    F = np.array( [[1, dt], [0, 1]] )

    # Measurement matrix
    H = np.array( [[0, 1]] )

    # Process noise
    Q = np.array( [[1, 0], [0, 3]] )

    # Measurement noise
    R = np.array( [[10]] )

    # Initial states x0=0m und v=20m/s
    x0 = np.array( [[0, 20]] ).transpose()

    # Initial error covariance matrix
    P0 = np.array(5 * np.eye(2))

    # Initialize kalman Filter
    kalman = Kalman(x0, P0, F, H, Q, R)

    # initialize measurement
    measure = Measurement(0, 80, dt)

    # Temporary state values and measurement values
    measured_speeds = []
    positions = []
    speeds = []

    # Perform measurement for the time period
    for index, k in enumerate(time_peride):

        Z = measure.measure() # train speed measurement
        X = kalman.filter(Z)  # train position prediction

        measured_speeds.append( Z[0][0] )
        positions.append( X[0][0] )
        speeds.append( X[1][0] )


    # Plot results
    plt.plot(time_peride, measured_speeds, color='gray', linestyle=':')
    plt.plot(time_peride, speeds)
    plt.xlabel('Measurement samples [sample/s]')
    plt.ylabel('Train speed [m/s]')
    plt.legend(['Measurement speed', 'Filtered speed'])
    plt.title('Train speed by kalman filter')
    plt.show()

    plt.plot(time_peride, positions)
    plt.xlabel('Measurement samples [sample/s]')
    plt.ylabel('Train postion [m]')
    plt.title('Train position estimated by kalman filter')
    plt.show()

    plt.plot(time_peride, kalman.P_list)
    plt.xlabel('Measurement samples [sample/s]')
    plt.ylabel('Error covariance P [(m/s)^2]')
    plt.title('Error covariance of the kalman filter')
    plt.show()

    plt.plot(time_peride, kalman.K_list)
    plt.xlabel('Measurement samples [sample/s]')
    plt.ylabel('Kalman gain K')
    plt.title('Kalman gain of the kalman filter')
    plt.show()