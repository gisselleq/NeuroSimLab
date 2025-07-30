import streamlit as st
import matplotlib.pyplot as plt
from simulate import lif_neuron

st.title("LIF Neuron Simulation")

st.sidebar.header("Simulation Controls")
I = st.sidebar.slider("Input Current (I)", 0.0, 5.0, 1.5, 0.1)
threshold = st.sidebar.slider("Threshold Voltage", 0.0, 5.0, 1.0, 0.1)
leak = st.sidebar.slider("Leakage Rate", 0.0, 0.1, 0.01, 0.001)
duration = st.sidebar.slider("Duration (ms)", 100, 1000, 200, 50)

#simulate the LIF neuron
time, voltage = lif_neuron(I, threshold, leak, duration)

#plot the results
fig, ax = plt.subplots()
ax.plot(time, voltage, label='Membrane Potential')
ax.axhline(y=threshold, color='r', linestyle='--', label='Threshold')
ax.set_xlabel('Time (ms)')
ax.set_ylabel('Membrane Potential (V)')
ax.set_title('LIF Neuron Simulation')
ax.legend()
st.pyplot(fig)
