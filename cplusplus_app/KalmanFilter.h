#pragma once

#include <iostream>
#include <math.h>
#include <tuple>
#include <array>
#include <vector>
#include "eigen/Core" // Eigen Library
#include "eigen/LU"   // Eigen Library

// Using other namespaces
using namespace std;
using namespace Eigen;

// Type definitions
typedef tuple<MatrixXf, MatrixXf, MatrixXf> TupleStdM3f;


class KalmanFilter final
{
private:
    MatrixXf x;
    MatrixXf P;

    MatrixXf F;
    MatrixXf H;
    MatrixXf Q;
    MatrixXf R;
    MatrixXf I;

    MatrixXf Z;
    MatrixXf y;
    MatrixXf S;
    MatrixXf K;

public:
    KalmanFilter(   MatrixXf x_, MatrixXf P_,
                    MatrixXf F_, MatrixXf H_, MatrixXf Q_, MatrixXf R_, MatrixXf I_,
                    MatrixXf Z_, MatrixXf y_, MatrixXf S_, MatrixXf K_);

    TupleStdM3f filter(float z);
};



