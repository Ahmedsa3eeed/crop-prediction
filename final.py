import streamlit as st
import pandas as pd
import joblib
Inputs = joblib.load("Inputs.pkl")
model = joblib.load("model.pkl")

def prediction(Nitrogen,phosphorus,potassium,temperature,humidity,ph,rainfall):
    test_df=pd.DataFrame(columns=Inputs)
    test_df.at[0,'Nitrogen']=Nitrogen
    test_df.at[0,'phosphorus']=phosphorus
    test_df.at[0,'potassium']=potassium
    test_df.at[0,'temperature']=temperature
    test_df.at[0,'humidity']=humidity
    test_df.at[0,'ph']=ph
    test_df.at[0,'rainfall']=rainfall
    result=model.predict(test_df)[0]
    return result

def main():
    st.title('crop recommendation')
    Nitrogen=float(st.number_input('insert a number for nitrogen'))
    phosphorus=float(st.number_input('insert a number for phosphorus'))
    potassium=float(st.number_input('insert a number for potassium'))
    temperature=float(st.number_input('insert a number for temperature'))
    humidity=float(st.number_input('insert a number for humidity'))
    ph=float(st.number_input('insert a number for ph'))
    rainfall=float(st.number_input('insert a number for rainfall'))

    if st.button("predict"):
        result=prediction(Nitrogen,phosphorus,potassium,temperature,humidity,ph,rainfall)
        st.text(f'The crop will be {result}')


if __name__ == '__main__':
    main()
    
