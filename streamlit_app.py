import streamlit as st
import numpy as np

st.title("Eigenvalues Calculator")

# Create a 3x3 matrix input form
a1, b1, c1, a2, b2, c2, a3, b3, c3 = st.beta_columns(3)
with a1:
    a11 = st.number_input(label='', key='a11')
with b1:
    a12 = st.number_input(label='', key='a12')
with c1:
    a13 = st.number_input(label='', key='a13')
with a2:
    a21 = st.number_input(label='', key='a21')
with b2:
    a22 = st.number_input(label='', key='a22')
with c2:
    a23 = st.number_input(label='', key='a23')
with a3:
    a31 = st.number_input(label='', key='a31')
with b3:
    a32 = st.number_input(label='', key='a32')
with c3:
    a33 = st.number_input(label='', key='a33')

# Arrange values in a 3x3 matrix
A = np.array([[a11, a12, a13], [a21, a22, a23], [a31, a32, a33]])

# Calculate eigenvalues
eigenvalues = np.linalg.eigvals(A)

# Print the eigenvalues
st.write("The eigenvalues of the matrix are:", eigenvalues)
