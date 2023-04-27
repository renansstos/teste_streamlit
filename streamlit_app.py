import streamlit as st
import numpy as np

st.title("Eigenvalues Calculator")

# Create a 3x3 matrix input form
matrix = st.beta_container()
with matrix:
    st.write("Enter the values for the 3x3 matrix below:")
    a11, a12, a13 = st.beta_columns(3)
    a21, a22, a23 = st.beta_columns(3)
    a31, a32, a33 = st.beta_columns(3)
    a = a11.number_input(label='', key='a')
    b = a12.number_input(label='', key='b')
    c = a13.number_input(label='', key='c')
    d = a21.number_input(label='', key='d')
    e = a22.number_input(label='', key='e')
    f = a23.number_input(label='', key='f')
    g = a31.number_input(label='', key='g')
    h = a32.number_input(label='', key='h')
    i = a33.number_input(label='', key='i')

# Arrange values in a 3x3 matrix
A = np.array([[a, b, c], [d, e, f], [g, h, i]])

# Calculate eigenvalues
eigenvalues = np.linalg.eigvals(A)

# Print the eigenvalues
st.write("The eigenvalues of the matrix are:", eigenvalues)
