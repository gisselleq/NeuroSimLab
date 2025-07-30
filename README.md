# NeuroSimLab

**NeuroSim Lab** is an interactive neuron simulator that visualizes the behavior of a Leaky Integrate and Fire (LIF) neuron model in real time. Built with Python and Streamlit, this project allows users to explore how different neuron parameters affect membrane potential over time. 

## Features
- Interactive sliders to adjust neuron properties:
  - Input current (I)
  - Membrane threshold
  - Leak rate
  - Duration
- Real-time plot of voltage over time
- Clean, responsive UI built with Streamlit
- Tool for beginners in computational neuroscience

## Tech Stack
- **Python**
- **Streamlit** 
- **matplotlib / NumPy**
  
## How to Run
1. Clone the repo:

   ```bash
   git clone https://github.com/gisselleq/NeuroSimLab.git
   cd NeuroSimLab

2. Install the dependencies
  - pip isntall -r requirements.txt

3. Launch the application
  - steamlit run main.py
