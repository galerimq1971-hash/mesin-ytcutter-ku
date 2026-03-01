import streamlit as st
import subprocess
import os

st.title("✂️ Mesin Potong Video")
url = st.text_input("Link YouTube:")
start = st.text_input("Mulai (00:00:10):")
end = st.text_input("Selesai (00:00:20):")

if st.button("POTONG"):
    out = "hasil.mp4"
    cmd = ["yt-dlp", "-f", "best", "--download-sections", f"*{start}-{end}", url, "-o", out]
    subprocess.run(cmd)
    if os.path.exists(out):
        with open(out, "rb") as f:
            st.download_button("DOWNLOAD", f, file_name=out)
