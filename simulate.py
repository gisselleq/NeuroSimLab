import numpy as np

def lif_neuron(I = 1.5, threshold = 1.0, leak = 0.01, duration = 200, dt = 1):
    time = np.arange(0, duration, dt)   
    voltage = np.zeros_like(time, dtype=float)
    v = 0.0
    
    for i in range(1, len(time)):
        dv = -leak * v + I
        v += dv * dt
        if v >= threshold:
            voltage[i] = 1.0  # spike
            v = 0.0 # resets after the spike
        else:
            voltage[i] = v
    
    return time, voltage

