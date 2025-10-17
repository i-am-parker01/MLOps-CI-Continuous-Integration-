import streamlit as st

st.title('Power Claculator')
st.write('Enter any number to calculate the square,cube or the fifth power')

# getting the user input
n=st.number_input('Enter a number',value=1,step=1)

# Calculating the results
square=n**2
cube=n**3
fifth_power=n**5

# Displaying results
st.write(f'Square of {n} is: {square}')
st.write(f'Cube of {n} is: {cube}')
st.write(f'fifth_power of {n} is: {fifth_power}')

