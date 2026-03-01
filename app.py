import streamlit as st
import os
import subprocess
import sys

# --- FUNGSI DARURAT (PENGUSIR KUCING) ---
def install_requirements():
    try:
        import yt_dlp
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])

install_requirements()
import yt_dlp
# ---------------------------------------

st.set_page_config(page_title="GMQ YT Cutter", page_icon="✂️")
st.title("✂️ Mesin Pemotong Video Cloud")

link = st.text_input("Link YouTube Utama:")
mulai = st.text_input("Mulai (00:00:10):")
selesai = st.text_input("Selesai (00:00:20):")
judul = st.text_input("Nama File:", "video_gmq")

if st.button("🚀 MULAI POTONG"):
    if link and mulai and selesai:
        output = f"{judul}.mp4"
        st.info("Sedang memproses di Server... Tunggu ya.")
        
        # Perintah langsung ke mesin yt-dlp
        perintah = [
            "yt-dlp",
            "--download-sections", f"*{mulai}-{selesai}",
            "--force-keyframes-at-cuts",
            "-f", "best",
            link,
            "-o", output
        ]
        
        try:
            subprocess.run(perintah, check=True)
            if os.path.exists(output):
                st.success("✅ Berhasil! Klik tombol di bawah:")
                with open(output, "rb") as f:
                    st.download_button("📥 DOWNLOAD KE HP", f, file_name=output)
            else:
                st.error("Gagal: File tidak ditemukan.")
        except Exception as e:
            st.error(f"Error Sistem: {e}")
    else:
        st.warning("Mohon isi semua kolom!")
