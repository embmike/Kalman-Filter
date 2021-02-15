# Kalman-Filter
This sample application uses a Kalman filter to predicts the train position based on speed measurement.


## Kalman filter algorithm
The [Kalman filter](https://en.wikipedia.org/wiki/Kalman_filter) equations are simplified for the application.       

+ ### Vectors and matrices:
  F : the state-transition model   
  H : the measurement model    
  Q : the covariance of the process noise   
  R : the covariance of the measurement noise   
  x0: the initial state   
  P0: the initial error covariance   

+ ### Equations:
  <img src="/images/kalman_filter_equations.JPG" width="60%" height="60%">

+ ### Kalman filter calculation:
  <img src="/images/kalman_filter_calculation.JPG" width="75%" height="75%">

## Example
A train travels at a constant speed of 80 km/h. The speed is measured every 100 ms. The speed is filtered and the current position is predicted using a Kalman filter.

+ ### Vectors and matrices:
  <img src="/images/process_model.JPG" width="13%" height="13%">
  
+ ### A priori prediction of the position:
  <img src="/images/process_calculation.JPG" width="45%" height="45%">
  
+ ### Speed measurement with noise:
  <img src="/images/measurement_calculation.JPG" width="65%" height="65%">
  
+ ### Plotted speed and predicted position:
  <img src="/images/train_speed_and_position.PNG" width="100%" height="100%">
  
+ ### Plotted kalman gain and error covariance:
  <img src="/images/kalman_gain_and error_covariance.PNG" width="100%" height="100%">


## Important files
- **train_position_prediction.py** : Calculates the train position and plots the results
- **speed_measurement.py** : Simulates the speed measurement
- **kalman_filter.py** : Predicts the position.


## Installation and usage
Clone the repository
```sh
$ cd <your workspace folder>
$ git clone https://github.com/embmike/Kalman-Filter.git
```

You can use the code for example on your computer with [Anaconda](https://www.anaconda.com/) or via cloud computing with [Google Colaboratory](https://colab.research.google.com/)


## Licence
This project is licensed under the terms of the [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
