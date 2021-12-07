import streamlit as st
import pickle
import numpy as np
import joblib, os
# import sklearn
import pandas as pd

def prediction_model(model_file):
	return joblib.load(open(os.path.join(model_file),"rb"))

lr_model = pickle.load(open('model.pkl', 'rb'))


def main():
    
    st.title('STRATUP SUCESS PREDICTION')  
    
    label = {
        'Yes': 1,
        'No': 0
    }
    
    top500 = {
        'Yes': 1,
        'No': 0
    }
    col1, col2 = st.columns(2)
    with col1:
        label_ = st.radio('Advesrtisements', options=label.keys())
    with col2:
        age_first_funding_year = st.number_input('First Funding year:')
        
    col3, col4 = st.columns(2)
    with col3:
        age_first_milestone_year = st.number_input('First Milestone year:')
    
    with col4:
        relationships = st.number_input('Company Relationships:')
        
    col5, col6 = st.columns(2)
    with col5:
        milestones = st.number_input('Milestones Achieved:')
    with col6:
        avg_participants = st.number_input('Avg. Participants')
        
    is_top500 = st.radio('in in Top 500?', options=top500.keys())
               
    predict = st.button('Predict')
    
    if predict:
        list_of_columns = ['labels',
                        'age_first_funding_year',
                        'age_first_milestone_year',
                        'relationships',
                        'milestones',
                        'avg_participants',
                        'is_top500',
                        'status']
        input_data = pd.DataFrame(columns=list_of_columns)
        input_data.drop(['status'], axis='columns', inplace=True)
        
        # input_data.at[0, 'labels'] = 
        if label_ == 'Yes':
            input_data.at[0, 'labels'] = 1
        if label_ == 'No':
            input_data.at[0, 'labels'] = 0
        
        input_data.at[0, 'age_first_funding_year'] = age_first_funding_year
        input_data.at[0, 'age_first_milestone_year'] = age_first_milestone_year
        input_data.at[0, 'relationships'] = relationships
        input_data.at[0, 'milestones'] = milestones
        input_data.at[0, 'avg_participants'] = avg_participants
        
        if is_top500 == 'Yes':
            input_data.at[0, 'avg_participants'] = 1
        if is_top500 == 'No':
            input_data.at[0, 'avg_participants'] = 0
            
        input_data.at[0, 'is_top500'] = 1
        
        input_data['labels']=(input_data['labels']-0/(1-0))
        input_data['age_first_funding_year']=(input_data['age_first_funding_year']-0/(1-0))
        input_data['age_first_milestone_year']=(input_data['age_first_milestone_year']-0/(1-0))
        input_data['relationships']=(input_data['relationships']-0/(1-0))
        input_data['milestones']=(input_data['milestones']-0/(1-0))
        input_data['avg_participants']=(input_data['avg_participants']-0/(1-0))
        input_data['is_top500']=(input_data['is_top500']-0/(1-0))
        y_pred =  lr_model.predict(input_data)
        if(y_pred==1):
            st.success('Sucess')
            st.write("kjsdhjfk")
        else:
            st.error('Fail')
            st.write("flhdsfjkaf")
        
    
    
if __name__ == '__main__':
    main()