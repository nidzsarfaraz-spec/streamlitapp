import streamlit as st
import pandas as pd
#import plotly.express as px


st.title("Cric info app")

def load_data(file_path):
    df=pd.read_csv(file_path)
    return df

data_path="./newcricinfo.csv"

df=load_data(data_path)

#st.dataframe(df)


country_match=df.groupby("country")["Matches"].sum().sort_values().reset_index()

fig_country=px.pie(
    country_match,
    names="country",
    values="Matches",
    title="Country wise Matches"
)

st.sidebar.header("filters")

country=st.sidebar.multiselect("select country",options=df["country"].unique(),default=df["country"].unique())
#duration=st.sidebar.slider("Select Duration",)
filtered_df=df[
    (df["country"].isin(country))
]


st.dataframe(filtered_df)
 
total_runs=filtered_df["Runs"].sum()
total_matches=filtered_df["Matches"].sum()
total_hundreds=filtered_df["100"].sum()
total_sixes=filtered_df["6s"].sum()
total_players=filtered_df["Players"].nunique()


col1,col2,col3,col4,col5 =st.columns(5)

with col1:
    st.metric(label="Total Runs",value=total_runs)

with col2:
    st.metric(label="Matches", value=total_matches)

with col3:
    st.metric(label="Total Hundreds",value=total_hundreds)

with col4:
    st.metric(label="Total Sixes",value=total_sixes)

with col5:
    st.metric(label="Total Players",value=total_players)


#st.plotly_chart(fig_country)


#country_runs=df.groupby("country")["Runs"].sum().sort_values().reset_index().head(10)

#fig_country=px.bar(
    #country_runs,
    #x="country",
    #y="Runs",
    #title="country wise Runs"
#)

#st.plotly_chart(fig_country)
