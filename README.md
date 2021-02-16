# Kalman filter
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
  ![Equations](/images/1_kalman_equations.PNG "Equations") 

+ ### Kalman filter calculation:
  ![Kalman filter calculation](/images/2_kalman_filter_calculation.PNG "Kalman filter calculation") 

## Example
A train travels at a constant speed of 80 km/h. The speed is measured every 100 ms. The speed is filtered and the current position is predicted using a Kalman filter.

+ ### Vectors and matrices:
  ![Vectors and matrices](/images/3_vectors_and_matrices.PNG "Vectors and matrices") 
  
+ ### A priori prediction of the position:
  ![A priori prediction of the position](/images/4_a_priori_prediction.PNG "A priori prediction of the position") 
  
+ ### Speed measurement with noise:
  ![Speed measurement with noise](/images/5_speed_measurement.PNG "Speed measurement with noise") 
  
+ ### Plotted speed and predicted position:
  ![Plotted speed and predicted position](/images/6_plotted_speed_and_posotion.PNG "Plotted speed and predicted position") 
  
+ ### Plotted kalman gain and error covariance:
  ![Plotted kalman gain and error covariance](/images/7_kalman_gain_and_error_covariance.PNG "Plotted kalman gain and error covariance") 


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
