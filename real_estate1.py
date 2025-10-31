import pandas as pd
import streamlit as st
import time
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, accuracy_score
#---------------------------------------------------------------------------------------------
data = pd.read_csv ("real_estate.csv")
#print(data)
data1 = data.head(10)
x = data.iloc[ : , 1 : -1]
y = data.loc[ : , ['house price of unit area']]

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2, random_state = 3)

model = LinearRegression()

model.fit(x_train, y_train)

t= model.predict(x_test)

ac = r2_score(y_test, t)
#-----------------------------------------------------------------------------------------------

men = st.sidebar.selectbox("What is your favorite colour ",  options = ('Home', 'Data', 'Prediction', 'Accuracy'))
if men == 'Home':
    st.title("*******HOUSE PRICE PREDICTION**********")
    st.image("house.jpg")
    st.title("-" * 45)
elif men == 'Data':
    st.write("Sample Data for House")
    if st.button("!!CLICK!!"):
        st.dataframe(data1)

elif men ==  'Accuracy':
    st.header("Making Prediction")
    st.subheader("Checking of Model Accuracy")
    if st.button("Check"):
        st.text(f"Accuracy is ==>{ac}")
elif men == 'Prediction':
    st.image("prediction.jpg")
    st.header("Select the field for making prediction")
    age = st.number_input("Enter the age of house :=>")
    dst =st.slider("Select distance to the nearest MRT station", min_value = 22.0, max_value=7000.0, value= 50.0)
    con =st.slider("Select number of convenience stores", min_value = 0, max_value=10, value= 5)
    #aprice=st.slider("Select house price of unit area", min_value = 10.0, max_value=120.0 , value= 15.0)

    pr = model.predict([[age, dst, con]])
    if st.button("Now Predict House price"):
        st.write(f"House price is ===> {pr[0]}")
    
    
    





