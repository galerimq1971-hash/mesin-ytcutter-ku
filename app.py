import streamlit as st
import os
import subprocess
import sys

# --- FUNGSI INSTALASI PAKSA (JANGAN DIUBAH) ---
def install_requirements():
    try:
        import yt_dlp
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])

# Jalankan instalasi sebelum aplikasi mulai
install_requirements()
import yt_dlp
# ---------------------------------------------

st.set_page_config(page_title="GMQ YT Cutter", page_icon="✂️")
st.title("✂️ Mesin Pemotong Video Cloud")

url = st.text_input("Link YouTube:")
start = st.text_input("Mulai (00:00:10):")
end = st.text_input("Selesai (00:00:20):")
filename = st.text_input("Nama Video:", "video_gmq")

if st.button("🚀 PROSES SEKARANG"):
    if url and start and end:
        output = f"{filename}.mp4"
        st.info("Sabar ya, server lagi memproses...")
        
        ydl_opts = {
            'format': 'best',
            'outtmpl': output,
            'download_ranges': lambda info_dict, ydl: [{'start_time': sum(x * int(t) for x, t in zip([3600, 60, 1], start.split(':'))), 'end_time': sum(x * int(t) for x, t in zip([3600, 60, 1], end.split(':')))}],
            'force_keyframes_at_cuts': True,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            if os.path.exists(output):
                st.success("Berhasil!")
                with open(output, "rb") as f:
                    st.download_button("📥 DOWNLOAD KE HP", f, file_name=output)
            else:
                st.error("Gagal: File tidak tercipta.")
        except Exception as e:
            st.error(f"Sistem Error: {e}")
