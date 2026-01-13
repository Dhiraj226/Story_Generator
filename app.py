from main import generate_story_from_images
from PIL import Image 
import streamlit as st 
from main import narrate_story

st.title('AI Story Generator From Images')
st.markdown('upload 1 to 10 images, choose style and let AI generate and narrate story for you ')

with st.sidebar:
    st.header('Controls')

    uploaded_files=st.file_uploader(
        "Upload your images",
        type=['png','jpg','jpeg'],
        accept_multiple_files=True
    )

    story_style=st.selectbox(
        'Select Story Type',
        ('Comedy','Thriller','Sci-Fi','Mystery','Adventures','Morale','Fairy tale')
        )


    generate_button=st.button('Generate and Narrate Story',type='primary')
    
if generate_button:
    if not uploaded_files:
        st.warning('Select atleast one image')
    
    elif len(uploaded_files) > 10:
        st.warning('You can provide Maximum 10 Images')

    else:
        with st.spinner('AI is generating and narrating Story for you, Please Wait'):
            try:
                pil_images=[Image.open(uploaded_file) for uploaded_file in uploaded_files] 
                st.subheader('Your Visuals')
                image_columns=st.columns(len(pil_images))

                for i,image in enumerate(pil_images):
                    with image_columns[i]:
                        st.image(image,use_container_width=True)

                generate_story=generate_story_from_images(pil_images,story_style)

                if "Error" in generate_story or 'Falied' in generate_story or 'API key' in generate_story:
                    st.error(generate_story)

                else:
                    st.subheader(f'Your {story_style} story')
                    st.success(generate_story)

                st.subheader("Listen to your Story:")
                audio_file= narrate_story(generate_story)
                if audio_file:
                    st.audio(audio_file,format="audio/mp3")

                      
            except Exception as e:
                st.error(f'Appication error occured {e}')


