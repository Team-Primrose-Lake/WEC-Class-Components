import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("My streamlit GUI test")


# Button
if st.button("Click Here"):
    st.write("Button Clicked")

# slider
value = st.slider("select a value", 0, 100, 50)
st.write(f"Slider value: {value}")

#Checkbox
checkbox = st.checkbox("Check me!")
if checkbox:
    st.write("Checkbox is checked!")

#graph
x = np.linspace(0,10,100)
y= np.sin(x)
fig, ax = plt.subplots()
ax.plot(x,y)
st.pyplot(fig)
