import streamlit as st
import imgtext
import story
import text2image as textimg
import storyvoice as sv


def c1f():
    uploaded_file = st.file_uploader("Upload an Image")
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        with open(uploaded_file.name, "wb") as file:
            file.write(bytes_data)
        st.image(image=uploaded_file, caption="Uploaded Image",
                 use_column_width=True)

        Description = imgtext.query(uploaded_file.name, st.secrets["hf"])
        Story = story.story(Description, st.secrets["openai"])
        sv.query(Story, st.secrets["hf"])

        with st.expander("Description"):
            st.write(Description)
        with st.expander("Story"):
            st.write(Story)
        st.audio("audio.mp3")


def c2f():
    prompt = st.text_input('Enter The Image Prompt',
                           placeholder="Ex: kittens with cat")
    if prompt != "":
        result = textimg.query(prompt, st.secrets["hf"])
        st.image(result, caption=prompt, use_column_width=True)


def main():
    st.set_page_config(page_title="Imagetory", page_icon="🖥️")
    st.title(":orange[Imagetory]📷: The story of an image")
    st.markdown(
        "A unique way to bring **photographs to life**, delving into the emotions, characters, and environments within them.")
    option = st.selectbox(
        'Select your way',
        ('NONE ❌', 'IMAGE TO STORY ✔️', 'TEXT TO IMAGE ✔️'))

    st.write('You selected:', option)
    if (option == 'IMAGE TO STORY ✔️'):
        c1f()
    if (option == 'TEXT TO IMAGE ✔️'):
        c2f()


if __name__ == '__main__':
    main()
