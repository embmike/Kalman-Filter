# Kalman-Filter
This sample application uses a Kalman filter to predict a position based on speed measurement.

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
  
