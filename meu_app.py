import streamlit as st

st.set_page_config(page_title="Trabalho de Física")

with st.container():
    st.subheader('A Chegada da cor e do som')
    st.title('Vamos ver como que era o resultado de tantos estudos com essas câmeras')
    st.write('Aqui está os nossos diretórios: [Vídeo](https://www.youtube.com/watch?v=vfZZ_VTmVEU); [Câmera](https://webinsider.com.br/2019/01/03/o-glorioso-technicolor-de-tres-peliculas/)')

with st.container():
    st.write('---')
    
    st.subheader('Aqui está a filmagem colorida:')

    video_file = open("20251021_114321.mp4", "rb")
    video_bytes = video_file.read()
    st.video(video_bytes)

with st.container():
    st.write('---')

    st.subheader('Aqui está como era o funcionamento da câmera:')
   
    st.image("Camera.jpg", caption="Câmera Technicolor funcionamento")