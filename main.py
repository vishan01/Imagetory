import streamlit as st
import imgtext
import prompt_generator as pg
import story
import text2image as textimg
import storyvoice as sv


def main():
    st.set_page_config(page_title="Imagetory", page_icon="🖥️")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        st.write(bytes_data)

        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        st.write(stringio)

        string_data = stringio.read()
        st.write(string_data)

        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)
