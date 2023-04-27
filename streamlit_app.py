import streamlit as st
import numpy as np

st.title("TOPSIS MCDM Method")

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

# Create a weights input form
weights = st.beta_container()
with weights:
    st.write("Enter the weights for each criterion below:")
    w1, w2, w3 = st.beta_columns(3)
    w = np.array([w1.number_input(label='', key='w1'),
                  w2.number_input(label='', key='w2'),
                  w3.number_input(label='', key='w3')])

# Create alternative and criterion name input forms
names = st.beta_container()
with names:
    st.write("Enter the names for each alternative and criterion below:")
    a1, a2, a3 = st.beta_columns(3)
    alt_names = [a1.text_input("Alternative 1 name:", "A1"),
                 a2.text_input("Alternative 2 name:", "A2"),
                 a3.text_input("Alternative 3 name:", "A3")]
    c1, c2, c3 = st.beta_columns(3)
    crit_names = [c1.text_input("Criterion 1 name:", "C1"),
                  c2.text_input("Criterion 2 name:", "C2"),
                  c3.text_input("Criterion 3 name:", "C3")]

# Arrange values in a 3x3 matrix
A = np.array([[a, b, c], [d, e, f], [g, h, i]])

# TOPSIS MCDM Method
norm = np.sqrt(np.sum(A * A, axis=0))
A_normalized = A / norm
A_weighted = A_normalized * w
ideal_best = np.max(A_weighted, axis=0)
ideal_worst = np.min(A_weighted, axis=0)
S_best = np.sqrt(np.sum((A_weighted - ideal_best) ** 2, axis=1))
S_worst = np.sqrt(np.sum((A_weighted - ideal_worst) ** 2, axis=1))
C = S_worst / (S_worst + S_best)

# Print the results
st.write("The normalized matrix is:", A_normalized)
st.write("The weighted matrix is:", A_weighted)
st.write("The ideal best values are:", ideal_best)
st.write("The ideal worst values are:", ideal_worst)
st.write("The S_best values are:", S_best)
st.write("The S_worst values are:", S_worst)

result = []
for i, alt in enumerate(alt_names):
    result.append((alt, C[i]))
result = sorted(result, key=lambda x: x[1], reverse=True)

ranking = []
for i in range(len(alt_names)):
    ranking.append((result[i][0], [x[0] for x in result].index(result[i][0]) + 1))

st.write("The final ranking is:")
for alt, rank in ranking:
    st.write(f"{alt}: {rank:.0f}")

