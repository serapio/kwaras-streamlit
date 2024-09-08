import streamlit as st

import s3fs

s3 = s3fs.S3FileSystem()

files = s3.ls("kwaras-raramuri")

st.text("\n".join([item.split('/')[1] for item in files[:5]]))

wav = s3.open(files[0]).read()

st.audio(wav)

st.title("Language template")

language = st.selectbox("Language", ("Generic", "Raramuri", "Mixtec", "Kumiai", "Gitonga"))

# st.title("Config for overall export process")

# init_dir = st.selectbox("Working file directory", ("Corpus",))
# out_dir = st.text_input("auto")

# exp_fields = st.multiselect("Tiers to include", ("Phonetic", "Spanish", "English", "Note"))

# init_eafs = st.text_input("Directory of input EAFs", "corpus_data")

# st.title("Config for HTML export")

# init_meta = st.text_input("WAV session metadata (optional)", "metadata.csv")

# init_wav = st.text_input("WAV input directory", "wav")

# init_www = st.text_input("Web files output directory", "www")

# nav_bar_html = """<div align="right">
#                 <a href="index.html">Corpus</a>
#                 - <a href="dict.xhtml">Dictionary</a>
#                 </div>"""
# nav_bar = st.text_area("HTML div for navigation", nav_bar_html)
# page_title = st.text_input("HTML page title", "Kwaras Corpus")


