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




def bursting_neuron(I=1.5, threshold=1.0, leak=0.01, duration=200, dt=1, burst_interval=50):
    time = np.arange(0, duration, dt)
    voltage = np.zeros_like(time, dtype=float)
    v = 0.0
    for i in range(1, len(time)):
        #switch between on and off current every burst_interval ms
        I_burst = I if (i // burst_interval) % 2 == 0 else 0
        dv = -leak * v + I_burst
        v += dv * dt
        if v >= threshold:
            voltage[i] = 1.0
            v = 0.0
        else:
            voltage[i] = v
    return time, voltage

def silent_neuron(I = 0.2, threshold = 1.0, leak = 0.01, duration = 200, dt = 1):
    return lif_neuron(I, threshold, leak, duration, dt)  # silent neuron behaves like a LIF neuron with low input current
