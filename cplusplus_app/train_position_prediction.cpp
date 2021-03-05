#include <iostream>
#include "KalmanFilter.h"
#include "SpeedMeasurement.h"

// Using other namespaces
using namespace std;

// Type definitions
typedef vector<float> VectorStdf;

// Function declaration
VectorStdf TimeSteps(const float time_begin, const float dt, const float time_peride);


int main()
{
    // Sampling rate in s
    const float dt {0.1f};

    // Periode of time in s
    const float time_begin {0.0f};
    const float time_peride {10.0f};

    // Time steps
    VectorStdf time_steps = TimeSteps(time_begin, dt, time_peride);

    // Initial state (location and velocity)
    MatrixXf x {2, 1};
    x << 0, 
        20;

    //Initial Uncertainty
    MatrixXf P = MatrixXf::Ones(2, 2);
    P << P * 5;

    //Next State Function
    MatrixXf F {2, 2};
    F << 1, dt,
         0, 1;

    //Measurement Function
    MatrixXf H {1, 2};
    H << 0, 1;

    //Process Uncertainty
    MatrixXf Q {2, 2};
    Q << 1, 0,
         0, 3;

    //Measurement Uncertainty
    MatrixXf R {1, 1};
    R << 45;

    // Identity Matrix
    MatrixXf I {2, 2};
    I << 1, 0,
         0, 1;

    // Iternal matrices
    MatrixXf Z {1, 1};
    MatrixXf y {1, 1};
    MatrixXf S {1, 1};
    MatrixXf K {2, 1};

    // Kalman filter
    KalmanFilter kalman_filter {x, P, F, H, Q, R, I, Z, y, S, K};

    //Speed measurement
    float speed_mean {80.0f};
    float speed_stddev {8.0f};
    SpeedMeasurement measurement {speed_mean, speed_stddev};

    for(float time_step : time_steps)
    {
        float z = measurement.Measure();
        tie(x, P, K) = kalman_filter.Filter(z);

        cout << "z_speed = " << z       << endl;
        cout << "x_speed = " << x(1)    << endl;
        cout << "x_pos   = " << x(0)    << endl;
        cout << "K_pos   = " << K(1, 0) << endl;
        cout << "P_pos   = " << P(1, 1) << endl << endl;
    }

    return 0;
}


// Function definition
VectorStdf TimeSteps(const float time_begin, const float dt, const float time_peride)
{
    VectorStdf time_steps;

    for (float time_step = time_begin; time_step <= time_peride; time_step += dt)
    {
        time_steps.push_back(time_step);
    }

    return time_steps;
}
