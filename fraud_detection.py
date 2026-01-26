import streamlit as st
import pandas as pd
import joblib

model = joblib.load("fraud_detection_model.pkl")

st.title("Credit Card Fraud Detection")

st.markdown("Please input the transaction details below:")

st.divider()

transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT","DEPOSIT"])
amount = st.number_input("Transaction Amount", min_value=0.0, value = 1000.0)
oldbalanceOrg = st.number_input("Old Balance of Origin Account(Sender)", min_value=0.0, value = 10000.0)
newbalanceOrig = st.number_input("New Balance of Origin Account(Sender)", min_value=0.0, value = 9000.0)
oldbalanceDest = st.number_input("Old Balance of Destination Account(Receiver)", min_value=0.0, value = 5000.0)
newbalanceDest = st.number_input("New Balance of Destination Account(Receiver)", min_value=0.0, value = 0.0)

if st.button("Predict Fraudulence"):
    input_data = pd.DataFrame([{
        "type" : transaction_type,
        "amount" : amount,
        "oldbalanceOrg" : oldbalanceOrg,
        "newbalanceOrig" : newbalanceOrig,
        "oldbalanceDest" : oldbalanceDest,
        "newbalanceDest" : newbalanceDest
    }])

    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction Result: '{int(prediction)}' ")

    if prediction == 0:
        st.success("The transaction is Legitimate.")
    else:
        st.error("The transaction is Fraudulent.")

st.divider()