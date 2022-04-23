import streamlit as st
from PIL import Image
from wav2vec2_inference import *
import os

st.set_page_config(
    page_title="Automatic Speech Recognition",
    page_icon="🗣",
    layout="centered",
    initial_sidebar_state="auto",
)

upload_path = "uploads/"
download_path = "downloads/"

@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def asr_inference_wav2vec2(uploaded_file):
    asr = Wave2Vec2Inference("facebook/wav2vec2-base-960h")
    text = asr.file_to_text(uploaded_file)
    return text

@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def save_text(text, downloaded_txt_file):
    with open(downloaded_txt_file, 'w') as outtxt:
        outtxt.write(text)
    print(downloaded_txt_file)

@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def download_success():
    st.balloons()
    st.success('✅ Download Successful !!')

main_image = Image.open('static/main_banner.png')

st.image(main_image,use_column_width='auto')
st.title("🗣 Automatic Speech Recognition 🔉")
st.info('✨ Supports WAV Format only for audio files.')

uploaded_file = st.file_uploader("Upload audio file", type=["wav"])
if (uploaded_file is not None) and (uploaded_file.name.split(".")[-1] == "wav"):
    with open(os.path.join(upload_path,uploaded_file.name),"wb") as f:
        f.write((uploaded_file).getbuffer())
    with st.spinner(f"Converting speech to text... 💫"):
        text = asr_inference_wav2vec2(upload_path + uploaded_file.name)
        print(text)
        downloaded_txt_file = os.path.abspath(os.path.join(download_path,str("processed_"+uploaded_file.name.split(".")[0] + ".txt")))
        save_text(text, downloaded_txt_file)
        with open(downloaded_txt_file, "rb") as file:
            if st.download_button(
                                    label="Download ASR Output 🗣",
                                    data=file,
                                    file_name=str("ASR_output_"+uploaded_file.name.split(".")[0]+ ".txt"),
                                    mime='text/plain'
                                 ):
                download_success()
else:
    st.warning("Please upload your WAV file. Any other audio format is currently not supported")

st.markdown("<br><hr><center>Made with ❤️ by <a href='mailto:ralhanprateek@gmail.com?subject=ASR WebApp!&body=Please specify the issue you are facing with the app.'><strong>Prateek Ralhan</strong></a></center><hr>", unsafe_allow_html=True)
