#pragma once

#include <iostream>
#include <random>

// Using other namespaces
using namespace std;


class SpeedMeasurement final
{
private:
	mt19937 generator;
	normal_distribution<float> distribution;

public:
	SpeedMeasurement(float speed_mean, float speed_stddev);
	float Measure();
};

