import streamlit as st
import numpy as np
import pandas as pd 
import joblib 
import matplotlib.pyplot as plt
import plotly.express as px 
import seaborn as sns
import os 

# Reading the Data:
df = pd.read_csv("C:/guvi/project3/youtube.csv")

st.markdown(
    """
    <style>
    div.row-widget.stRadio > div{
        flex-direction:column;
    }
    /* Target the text labels next to the radio buttons */
    div.stRadio label p {
        font-size: 20px !important;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)
 
col11,col12 = st.columns([8,2])
with col11:
    st.markdown(
        "<h1 style='text-align: center; color: " \
        "black;'>Predict Youtube Ad_revenue 💰</h1>", 
        unsafe_allow_html=True)
with col12:
    st.image("C:/guvi/project3/logo.png", width = 200)

with st.sidebar:
    options = ['Model_prediction', 'Data insights','Data']
    option = st.radio("Pages :", options, width = 500)




if option == 'Model_prediction':

    st.markdown(
        '<p style="font-size:30px; color:red;">Numerical Input</p>',
        unsafe_allow_html=True
    )
    
    Views = st.number_input("Enter Views ")
    Likes = st.number_input("Enter Likes ") 
    Comments = st.number_input("Enter comments")
    Watch_Time_Minutes = st.number_input("Enter Watch_Time_Minutes")
    Video_Length_Minutes = st.number_input("Enter Video_Length_Minutes")
    Subscribers = st.number_input("Enter Subscribers")
    
    st.markdown(
        '<p style="font-size:30px; color:red;">Categorical Input</p>',
        unsafe_allow_html=True
    ) 
    category = {'TV' : 3, 'Tablet' :2, 'Mobile' :1, 'Desktop' : 0}
    device = {'Entertainment' : 1, 'Gaming' : 2, 'Education' : 0, 'Music' : 4, 'Tech' : 5, 'Lifestyle' :3}
    country = {'India' : 3, 'Canada' : 1, 'United Kingtom' : 4, 'United States' : 5, 'Germany' : 2, 'Australia' : 0}
    Category = st.selectbox("Enter Category", category.keys())
    Device = st.selectbox("Enter Device", device.keys())
    Country = st.selectbox("Enter Country", country.keys()) 
    Year = st.selectbox("Select the year",[2024, 2025])
    Month = st.selectbox("Select the month", [2, 3, 4, 5, 6, 7, 8, 9, 10, 12])
    
    
    try:
        Engagement_Rate = round((Likes + Comments)/Views, 2) 
    except ZeroDivisionError:
        Engagement_Rate = 0

   
    input_features = {
        "Views" : [Views],
        "Likes" : [Likes],
        "Comments" : [Comments],
        "Watch_Time_Minutes" : [Watch_Time_Minutes],
        "Video_Length_Minutes" : [Video_Length_Minutes],
        "Subscribers" : [Subscribers],
        "Category" : [category[Category]], 
        "Device" : [device[Device]],
        "Country" : [country[Country]],
        "Year" : [Year],
        "Month" : [Month], 
        "Engagement_Rate" : [Engagement_Rate]
         } 
    
     
    filename = 'C:/guvi/project3/finalized_model.joblib'
    Best_model = joblib.load(filename) 
    
    if st.button("predict"): 
        df = pd.DataFrame(input_features)
        st.write("\nUser Input :\n")
        st.write(df)
        
        try:
            result = Best_model.predict(df)[0]
            result = max(0,result)
            st.write(f"Predicted Ad_revenue is  :  {result:.2f} Usd") 
            if result == 0:
                st.info("This video may not generate revenue")

        except Exception as e:
            st.error(f"predicted Error :{str(e)}")

        finally:
            if result is not None:
                st.info(" Model is Sucessfully Predicted!")
    

 

elif option == 'Data insights':
    st.write("\n\n")
    st.markdown(
        '<p style="font-size:30px; color:red;">Trend Ananlysis for Watch_Time_Minutes Vs Ad_Revenue_Usd </p>',
        unsafe_allow_html=True 
        )
    plt.Figure(figsize = (5, 3))
    fig = px.scatter(df, x = 'Watch_Time_Minutes', y = 'Ad_Revenue_Usd',color = 'Year') 
    st.plotly_chart(fig, use_container_width=True) 
    col1, col2 = st.columns([1,1])
    
    # Data Distribution plot:
    fig1 = px.histogram(df, x = 'Ad_Revenue_Usd', nbins = 20, title = "Data Distribution")

    # pie plot: 
    fig2 = px.pie(df, values = 'Ad_Revenue_Usd', names = 'Country', title= "Ad_Revenue_Usd vs Country")
    fig2.update_layout(uniformtext_minsize = 12, uniformtext_mode = 'hide') 

    with col1 :
        st.markdown(
        '<p style="font-size:30px; color:red;">Data Distribution of Target Variable </p>',
        unsafe_allow_html=True 
        ) 
        st.plotly_chart(fig1, use_container_width=True)

    with col2 :
        st.markdown(
        '<p style="font-size:30px; color:red;">Ad_Revenue_Usd vs Country </p>',
        unsafe_allow_html=True 
        )
        st.plotly_chart(fig2, use_container_width=True) 

    # bar plot:
    st.markdown(
        '<p style="font-size:30px; color:red;">Ad_Revenue_Usd Based on Year And Month </p>',
        unsafe_allow_html=True 
        )
    year_group = df.groupby(['Year', 'Month'])['Ad_Revenue_Usd'].sum()
    year_group = year_group.reset_index()
    fig3 = px.bar(year_group, x = 'Year', y = 'Ad_Revenue_Usd', color = 'Month', 
                  hover_name = 'Month', color_discrete_sequence = px.colors.sequential.Aggrnyl)
    st.plotly_chart(fig3, use_container_width=True) 

    # which video id got highest views:

    st.markdown(
        '<p style="font-size:30px; color:red;">Toppest Ad_Revenue Video_id </p>',
        unsafe_allow_html=True 
        )
    
    df_grp = df.groupby('Video_Id')[['Views','Subscribers', 'Likes', 'Ad_Revenue_Usd', 'Engagement_Rate']].sum() 
    df_grp = df_grp.reset_index()
    df_grp = df_grp.sort_values(by = 'Engagement_Rate', ascending = False)
    st.dataframe(df_grp.head()) 

    # which video id got lowest Ad_revenue:

    st.markdown(
        '<p style="font-size:30px; color:red;">Lowest Ad_Revenue Video_id </p>',
        unsafe_allow_html=True 
        )
    
    df_grp = df.groupby('Video_Id')[['Views','Subscribers', 'Likes', 'Ad_Revenue_Usd', 'Engagement_Rate']].sum() 
    df_grp = df_grp.reset_index()
    df_grp = df_grp.sort_values(by = 'Engagement_Rate', ascending = False)
    st.dataframe(df_grp.tail()) 

elif option == 'Data':
    st.write("\n\n")
    df = pd.read_csv("C:/guvi/project3/youtubevm/Scripts/youtube_data.csv") 

    st.markdown(
        '<p style="font-size:30px; color:red;">YouTube Monetization Modeler Data :</p>',
        unsafe_allow_html=True
    )
    st.write("\n\n")
    st.dataframe(df)