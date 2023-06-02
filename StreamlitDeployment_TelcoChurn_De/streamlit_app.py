import streamlit as st
import pickle
import pandas as pd

st.sidebar.title('Churn Probability of a Single Customer')


html_temp = """
<div style="background-color:tomato;padding:1.5px">
<h2 style="color:white;text-align:center;">Churn Prediction ML App (Demo) </h2>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)

model= pickle.load(open('smote_rf_model_2', 'rb'))
features = pickle.load(open('model_features.pkl', 'rb'))
df_deploy = pickle.load(open('df_deploy.pkl', 'rb'))

def single_customer(tenure, OnlineSecurity, Contract, TotalCharges, InternetService, TechSupport, MonthlyCharges):
    my_dict = {"tenure" :tenure, 
        "OnlineSecurity":OnlineSecurity, 
        "Contract": Contract, 
        "TotalCharges": TotalCharges , 
        "InternetService": InternetService, 
        "TechSupport": TechSupport, 
        "MonthlyCharges":MonthlyCharges}
    df = pd.DataFrame.from_dict([my_dict], orient='columns')
    X = pd.get_dummies(df).reindex(columns=features, fill_value=0)  
    prediction = int(round(model.predict_proba(X)[0][1], 2)*100)
    return prediction

def random_customer():
    df_sample=df_deploy.sample(customer)
    df_2 = pd.get_dummies(df_sample).reindex(columns=features, fill_value=0)
    prediction = model.predict_proba(df_2)
    df_sample["Churn Probability"]=prediction[:,1]
    df_sample.drop("Churn", axis=1, inplace=True)
    df_sample["Churn Probability"]=df_sample["Churn Probability"].apply(lambda x:round(x,2))
    df_sample.rename(columns={"OnlineSecurity": "Onl.Sec", "InternetService": "Service","TechSupport": "Tech.Supp", "MonthlyCharges": "Monthly Charges","TotalCharges": "Total Charges" }, inplace=True)
    return st.table(df_sample)


def top_customers():
    df_sample=df_deploy.copy()
    df_2 = pd.get_dummies(df_sample).reindex(columns=features, fill_value=0)
    prediction = model.predict_proba(df_2)
    df_sample["Churn Probability"]=prediction[:,1]
    df_sample.drop("Churn", axis=1, inplace=True)
    df_sample["Churn Probability"]=df_sample["Churn Probability"].apply(lambda x:round(x,2))
    df_sample.rename(columns={"OnlineSecurity": "Onl.Sec", "InternetService": "Service","TechSupport": "Tech.Supp", "MonthlyCharges": "Monthly Charges","TotalCharges": "Total Charges" }, inplace=True)
    df_sample=df_sample.sort_values(by="Churn Probability", ascending=False).head(customer)
    return st.table(df_sample)
    
def top_loyal_customers():
    df_sample=df_deploy.copy()
    df_2 = pd.get_dummies(df_sample).reindex(columns=features, fill_value=0)
    prediction = model.predict_proba(df_2)
    df_sample["Churn Probability"]=prediction[:,1]
    df_sample.drop("Churn", axis=1, inplace=True)
    df_sample["Churn Probability"]=df_sample["Churn Probability"].apply(lambda x:round(x,2))
    df_sample.rename(columns={"OnlineSecurity": "Onl.Sec", "InternetService": "Service","TechSupport": "Tech.Supp", "MonthlyCharges": "Monthly Charges","TotalCharges": "Total Charges" }, inplace=True)
    df_sample=df_sample.sort_values(by="Churn Probability", ascending=True).head(customer)
    return st.table(df_sample)    
   
  
tenure=st.sidebar.slider("Number of months the customer has stayed with the company (tenure)", 1, 72, step=1) 
MonthlyCharges=st.sidebar.slider("The amount charged to the customer monthly", 0,100, step=5) 
TotalCharges=st.sidebar.slider("The total amount charged to the customer", 0,5000, step=10) 
Contract=st.sidebar.selectbox("The contract term of the customer", ('Month-to-month', 'One year', 'Two year')) 
OnlineSecurity=st.sidebar.selectbox("Whether the customer has online security or not", ('No', 'Yes', 'No internet service')) 
InternetService=st.sidebar.selectbox("Customer’s internet service provider", ('DSL', 'Fiber optic', 'No')) 
TechSupport=st.sidebar.selectbox("Whether the customer has tech support or not", ('No', 'Yes', 'No internet service'))

if st.sidebar.button("Submit"):
    result=single_customer(tenure, OnlineSecurity, Contract, TotalCharges, InternetService, TechSupport, MonthlyCharges)
    st.sidebar.success("The churn probability of selected customer is % {}".format(result))
    
    
    
if st.checkbox("Churn Probability of Randomly Selected Customers"):
    st.subheader("How many customers to be selected randomly?")
    customer=st.selectbox("Please select the number of customers", (1,10,50,100,500,1000))
    if st.button("Analyze"):
        st.success("The Churn Probability of randomly selected {} Customers".format(customer)) 
        random_customer()
        
if st.checkbox("Top Customers to Churn"):
    st.subheader("How many customers to be selected?")
    customer=st.selectbox("Please select the number of top customers to churn", (1, 100, 1000, 5000))
    if st.button("Show"):
        st.success("Top {} Customers to Churn".format(customer)) 
        top_customers()

if st.checkbox("Top Loyal Customers"):
    st.subheader("How many customers to be selected?")
    customer=st.selectbox("Please select the number of top loyal customers", (1, 100, 1000, 5000))
    if st.button("Show Loyal Customers"):
        st.success("Top {} Loyal Customers".format(customer)) 
        top_loyal_customers()


st.markdown(
    f'''
        <style>
            .sidebar .sidebar-content {{
                width: 350px;
            }}
        </style>
    ''',
    unsafe_allow_html=True
)
