import streamlit as st
import pickle
import pandas as pd
def recommend(book):
    book_index = Bookre[Bookre["title"] == book].index[0]
    distance = similarity[book_index]
    book_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_books=[]
    for i in book_list:
        recommended_books.append(Bookre.iloc[i[0]].title)
    return recommended_books
book_dict=pickle.load(open("book.pkl","rb"))
Bookre=pd.DataFrame(book_dict)
similarity=pickle.load(open("similarity.pkl","rb"))

st.title("Book Recommender System")
selected_movie_name=st.selectbox(
    "Please check with following movies",
    Bookre['title'].values
)

if st.button("Recommend"):
    recom=recommend(selected_movie_name)
    for i in recom:
        st.write(i)