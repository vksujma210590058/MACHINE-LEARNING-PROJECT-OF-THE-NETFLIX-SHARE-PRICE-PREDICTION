import streamlit as st
import pickle
import sklearn
import pandas as pd
st.title("NEXT DAY SHARE PRICE PREDICTION")
st.write("GIVE THE DATA TO TO DAY OUR MODEL WILL PREDICT THE MAXIMUM HIGHEST PRICE FOR THE TOMORROW ")
# to_data_netflix=pd.DataFrame({"Open":[float(input("OPEN PRICE IN DOLLER "))],"High":[float(input("High."))],"Low":[float(input("LOW PRICE OF THE DAY "))],"Close":[float(input("CLOSE PRICE OF THE DAY "))],"Adj Close":[float(input("ADJ CLOSE PRICE "))],"year":[float(input("YEAR "))],
#                               "month":[float(input("MONTH "))],"day":[float(input("DAY "))],"Volume_in_lakh ":[float(input("TOTAL VOLUME AND DIVIDE BY ONEL LAKH THEN WRITE "))]})
#
# print(to_data_netflix)
# #283.250000	290.630005	283.220001	289.619995	2019	11	14	65.290
#
#
# print()
# print("HIGHEST PRICE WOULD BE THIS FOR THE TOMORROW ")
# print("ERROR IS NEAR ABOUT 1%")
# linear_regression.predict(to_data_netflix.values)
Open=st.number_input(label="OPEN PRICE ")
# st.write(Open)
high=st.number_input(label="HIGH PRICE ")
# st.write(high)
low=st.number_input(label="LOW PRICE ")
# st.write(low)
close=st.number_input(label="CLOSE PRICE ")
# st.write(close)
adj_close=st.number_input(label="ADJ_CLOSE PRICE ")
# st.write(adj_close)
year=st.number_input(label="YEAR")
# st.write(year)
month=st.number_input(label="MONTH")
# st.write(month)
day=st.number_input(label="DAY")
# st.write(day)
volume=st.number_input(label="VOLUME OF THE NETFLIX OR SHARES")/100000
# st.write(volume*100000)


to_data_netflix=pd.DataFrame({"Open":[Open],"High":[high],"Low":[low],"Close":[close],"Adj Close":[adj_close],"year":[year],
                              "month":[month],"day":[day],"Volume_in_lakh":[volume]})
st.write(to_data_netflix)
#Open	High	Low	Close	Adj Close	year	month	day	Volume_in_lakh
# predict_value=model(to_data_netflix)
# if st.button:
#     st.write("THIS IS OUR PREDICTED HIGH PRICE FOR THE NEXT PRICE")
#     st.write(predict_value)
#     st.write("Mean_Absolute_Percentage_Error=1.166% ERROR")
with open(r"C:\Users\vksuj\IdeaProjects\NETFLIX_TOMORROW_SHARE_PRICE_PREDICTION\linear_re.pkl",'rb') as file:

    linear_regression=pickle.load(file)

predict_value=linear_regression.predict(to_data_netflix)
button_clicked = st.button("Click Me")
if button_clicked:
    st.write("THIS IS OUR PREDICTED HIGH PRICE FOR THE NEXT PRICE")
    st.write(predict_value)
    st.write("Mean_Absolute_Percentage_Error=1.166% ERROR")


st.write("ok")
# a=linear_regression.predict(to_data_netflix)
# st.write(a)C:\Users\vksuj\IdeaProjects\NETFLIX_TOMORROW_SHARE_PRICE_PREDICTION\linear_re.pkl