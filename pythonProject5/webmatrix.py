import streamlit as st
import AddingMatrices as am
import MultiplyingMatrices as ma
import InverseMatrices as im
import TranposeMatrices as tm
import DeterminantofMatrices as dm
import numpy as np
st.markdown(
    """
    <iframe src="https://www.bing.com/ck/a?!&&p=4dd4fd599a0660c2JmltdHM9MTcxMDI4ODAwMCZpZ3VpZD0yNWVkMmE3Zi05OGI2LTY4OTktMThkMi0zYWU3OTlkODY5MDcmaW5zaWQ9NTQ4OA&ptn=3&ver=2&hsh=3&fclid=25ed2a7f-98b6-6899-18d2-3ae799d86907&u=a1L3ZpZGVvcy9yaXZlcnZpZXcvcmVsYXRlZHZpZGVvP3E9Y29jYStjb2xhK3ZpZGVvK2NsaXArdGhhdCtpcytub3QraW4reW91dHViZSZtaWQ9NjlEMjJDRDhFRTRCOTQzQkU0Nzg2OUQyMkNEOEVFNEI5NDNCRTQ3OCZGT1JNPVZJUkU&ntb=1" width="1500" height="200" frameborder="0" scrolling="no"></iframe>
    """,
    unsafe_allow_html=True
)
background_image = "https://3.bp.blogspot.com/-HfZVy28VUJs/WLcaLQnmxfI/AAAAAAAA0xs/Kx416jtMPL0sxU33FBIxOG4H2L8C5bZ3gCLcB/s1600/white-background.jpg"
title_text = "<div style='text-align: center; color: black; font-size: 50px; font-family: 'Arial, sans-serif';'>💡MATRIXGENIUS SOLVER PRO💡</div>"
markdown_str = f"""
    <style>
        .background {{
            background-image: url('{background_image}');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
    </style>

    <div class="background">
        <h1 class="">{title_text}</h1>
    </div>
"""
st.markdown(markdown_str, unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .stApp{
        background-color : #D3D3D3 ;

    }
    </style>
    """,
    unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
        <h1 style="font-size: 28px; font-family: 'Arial, sans-serif'; color: black; text-align: center">
        Enter the size of the matrices:
        </h1>
    """, unsafe_allow_html=True)
with col2:
    row = st.number_input("ROW:", min_value=1, max_value=5, key='row')
with col3:
    column = st.number_input("COLUMN:", min_value=1, max_value=5, key='column')

col4, col5 = st.columns(2)
with col4:
    st.markdown("""
            <h1 style="font-size: 24px; text-align: center; color: black; font-family: 'Arial, sans-serif';">
            Matrix A
            </h1>
        """, unsafe_allow_html=True)
    matrixA = []
    for row_index in range(row):
        columns = st.columns(column)
        row_values = []
        for col_index, col in enumerate(columns):
            with col:
                value = st.text_input("", key=f'Arow{row_index + 1}Acol{col_index + 1}')
                row_values.append(value)
        matrixA.append(row_values)

with col5:
    st.markdown("""
                <h1 style="font-size: 24px; text-align: center; color: black; font-family: 'Arial, sans-serif';">
                Matrix B
                </h1>
            """, unsafe_allow_html=True)
    matrixB = []
    for row_index in range(row):
        columns = st.columns(column)
        row_values = []
        for col_index, col in enumerate(columns):
            with col:
                value = st.text_input("", key=f'Brow{row_index + 1}Bcol{col_index + 1}')
                row_values.append(value)
        matrixB.append(row_values)

selected_option = st.selectbox("Select an option:", ["Add Matrices", "Multiplying Matrices", "Inverse of Matrices","Transpose Matrices", "Determinant of Matrices"])


if selected_option == "Add Matrices":
    calculate = st.button("Click To Add", key='add_button')
    if calculate:
        matrix_Result = am.adding_matrices(matrixA, matrixB)
        col6, col7, col8 = st.columns(3)
        with col7:
            st.markdown("""
                            <h1 style="font-size: 24px; text-align: center; color: black; font-family: 'Arial, sans-serif';">
                            Sum of Matrix A and B
                            </h1>
                        """, unsafe_allow_html=True)
            for row_index in range(row):
                columns = st.columns(column)
                for col_index, col in enumerate(columns):
                    with col:
                        st.text_input("", value=matrix_Result[row_index][col_index],
                                      key=f'Rrow{row_index + 1}Rcol{col_index + 1}')
elif selected_option == "Multiplying Matrices":
    calculate = st.button("Click To Multiply", key='multiply_button')
    if calculate:
        try:
            matrix_Result = ma.multiplying_matrices(matrixA, matrixB)
            col6, col7, col8 = st.columns(3)
            with col7:
                st.markdown("""
                                            <h1 style="font-size: 24px; text-align: center; color: black; font-family: 'Arial, sans-serif';">
                                            Product of Matrix A and B
                                            </h1>
                                        """, unsafe_allow_html=True)
                for row_index in range(row):
                    columns = st.columns(column)
                    for col_index, col in enumerate(columns):
                        with col:
                            st.text_input("", value=matrix_Result[row_index][col_index],
                                          key=f'Rrow{row_index + 1}Rcol{col_index + 1}')
        except ValueError as e:
            st.error(str(e))
elif selected_option == "Inverse of Matrices":
    calculate = st.button("Click To Inverse", key='inverse_button')
    if calculate:
        inv_matA, inv_matB = im.inverse_matrices(matrixA, matrixB)
        if inv_matA is not None and inv_matB is not None:
            col6, col7 = st.columns(2)
            with col6:
                st.markdown("""
                                            <h1 style="font-size: 24px; text-align: center; color: black; font-family: 'Arial, sans-serif';">
                                            Inverse of Matrix A
                                            </h1>
                                        """, unsafe_allow_html=True)
                for row_index in range(len(inv_matA)):
                    for col_index in range(len(inv_matA[row_index])):
                        st.text_input("", value=str(inv_matA[row_index][col_index]),
                                      key=f'A_{row_index + 1}Acol{col_index + 1}')
            with col7:
                st.markdown("""
                                                            <h1 style="font-size: 24px; text-align: center; color: black; font-family: 'Arial, sans-serif';">
                                                            Inverse of Matrix B
                                                            </h1>
                                                        """, unsafe_allow_html=True)
                for row_index in range(len(inv_matB)):
                    for col_index in range(len(inv_matB[row_index])):
                        st.text_input("", value=str(inv_matB[row_index][col_index]),
                                      key=f'B_{row_index + 1}Bcol{col_index + 1}')
        else:
            st.error("Error: Singular matrix. Cannot invert the matrices.")
elif selected_option == "Transpose Matrices":
    calculate = st.button("Click To Transpose", key='transpose_button')
    if calculate:
        try:
            matrix_Result = tm.transpose_matrices(matrixA, matrixB)
            col8, col9, col10, = st.columns(3)
            with col9:
                st.markdown("""
                                                                            <h1 style="font-size: 24px; text-align: center; color: black; font-family: 'Arial, sans-serif';">
                                                                            Transpose of Matrix A
                                                                            </h1>
                                                                        """, unsafe_allow_html=True)
                for row_index in range(row):
                    columns = st.columns(column)
                    for col_index, col in enumerate(columns):
                        with col:
                            st.text_input("", value=matrix_Result[row_index][col_index],
                                          key=f'Rrow{row_index + 1}Rcol{col_index + 1}')
        except IndexError as e:
            st.error(str(e))
elif selected_option == "Determinant of Matrices":
    calculate = st.button("Click To Determine", key='determinant_button')
    if calculate:
        try:
            det_matA, det_matB = dm.determinant_matrices(matrixA, matrixB)
            col6, col7 = st.columns(2)
            with col6:
                st.markdown("""
                                                            <h1 style="font-size: 24px; text-align: center; color: black; font-family: 'Arial, sans-serif';">
                                                           Determinant of Matrix A
                                                            </h1>
                                                        """, unsafe_allow_html=True)
                st.text_input("", value=str(det_matA))
            with col7:
                st.markdown("""
                                                                           <h1 style="font-size: 24px; text-align: center; color: black; font-family: 'Arial, sans-serif';">
                                                                          Determinant of Matrix B
                                                                           </h1>
                                                                       """, unsafe_allow_html=True)
                st.text_input("", value=str(det_matB))
        except np.linalg.LinAlgError as e:
            st.error(str(e))