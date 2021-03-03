#include "SpeedMeasurement.h"


SpeedMeasurement::SpeedMeasurement(float speed_mean, float speed_stddev)
{
	random_device rd {};
	generator = mt19937 {rd()};
	distribution = normal_distribution<float> {speed_mean, speed_stddev};
}


float SpeedMeasurement::Measure()
{
	return distribution(generator);
}

