import numpy as np
#z score formula is z =(value -mean)/std

data = np.array([10, 12, 15, 18, 20])
mean = np.mean(data) 
print("Mean:", mean)
std = np.std(data)
print("Standard Deviation:", std)
z_scores = (data - mean)/std
print ("Z-scores:", z_scores)


#3d array for time series sensor data
#shape = samples, time_steps, features
samples =5
time_steps = 10
features = 3
sensor_data = np.random.rand(samples,time_steps, features)
print("\nSensor Data Shape:", sensor_data.shape)
print("Sensor Data:\n", sensor_data)