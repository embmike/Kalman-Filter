#include "KalmanFilter.h"


KalmanFilter::KalmanFilter( MatrixXf x_, MatrixXf P_, 
                            MatrixXf F_, MatrixXf H_, MatrixXf Q_, MatrixXf R_, MatrixXf I_,
                            MatrixXf Z_, MatrixXf y_, MatrixXf S_, MatrixXf K_)
    : x{x_}, P{P_}, F{F_}, H{H_}, Q{Q_}, R{R_}, I{I_}, Z{Z_}, y{y_}, S{S_}, K{K_}
{}

TupleStdM3f KalmanFilter::Filter(float z)
{
    // Measurement
    Z << z;
    y << Z - (H * x);
    S << H * P * H.transpose() + R;
    K << P * H.transpose() * S.inverse();
    x << x + (K * y);
    P << (I - (K * H)) * P;

    // Prediction
    x << (F * x);
    P << F * P * F.transpose() + Q;

    return make_tuple(x, P, K);
}
