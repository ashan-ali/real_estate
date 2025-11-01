import pandas as pd
import streamlit as st
from PIL import Image
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

men = st.sidebar.selectbox("Menu ",  options = ('Home', 'Data', 'Prediction', 'Accuracy'))
if men == 'Home':
    st.title("HOUSE PRICE PREDICTION")
    im = Image.open("house.jpg")
    im1 = im.resize((600, 300))
    st.image(im1)
    st.title("-" * 45)
    st.markdown("\t\t\t\tAshan Ali")
    st.markdown("\t\t\t\tPGT - CS/IP/AI")
    st.markdown("\t\t\t\tNew St. Stephen's Public School, Agra")
    st.title("-" * 45)
elif men == 'Data':
    st.title("House sample data set ")
    if st.button("!!CLICK!!"):
        st.dataframe(data1)
        st.image("check.gif")

elif men ==  'Accuracy':
    st.title("Model Accuracy")
    st.title("-" * 45)
    if st.button("Check"):
        st.title(f"Accuracy is ==>{round(ac, 2)}%")
        st.image("line.jpg")
        
elif men == 'Prediction':
    st.title("Making House Price Prediction")
    st.image("processing.gif")
    st.title("-" *45)
    age = st.number_input("Enter the age of house :=>")
    dst =st.slider("Select distance to the nearest MRT station", min_value = 22.0, max_value=7000.0, value= 50.0)
    con =st.slider("Select number of convenience stores", min_value = 0, max_value=10, value= 5)
    #aprice=st.slider("Select house price of unit area", min_value = 10.0, max_value=120.0 , value= 15.0)

    pr = model.predict([[age, dst, con]])
    
    if st.button("Now Predict House price"):
        st.write(f"House price of unit area is ===> {round(pr[0][0],2)}")
    
    
    



























