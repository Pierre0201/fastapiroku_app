import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

from ml_model import predict

# App title
st.title("Streamlit very basic demo")

# User-defined model inputs appear on the app' sidebar
x1 = st.sidebar.number_input('Enter input value X1')
x2 = st.sidebar.number_input('Enter input value X2')
x3 = st.sidebar.number_input('Enter input value X3')

# Display model output
st.write(f'Sum of inputs = {x1 + x2 + x3}')
st.write(f'Model prediction Y = {predict([x1, x2, x3])}')


# Use cache decorator to compute some stuff only once
@st.cache
def generate_samples():
    return np.random.normal(0, 1, size=10000)


# Plot a nice figure
samples = generate_samples()

fig = plt.figure()
plt.hist(samples, density=True)
plt.axis("off")
plt.title("A nice figure")
st.pyplot(fig)