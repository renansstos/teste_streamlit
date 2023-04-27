import streamlit as st
import numpy as np

st.title("Eigenvalues Calculator")

# Create input fields for the four values
a = st.number_input("Enter the first value:")
b = st.number_input("Enter the second value:")
c = st.number_input("Enter the third value:")
d = st.number_input("Enter the fourth value:")

# Arrange values in a 2x2 matrix
A = np.array([[a, b], [c, d]])

# Calculate eigenvalues
eigenvalues = np.linalg.eigvals(A)

# Print the eigenvalues
st.write("The eigenvalues of the matrix are:", eigenvalues)
