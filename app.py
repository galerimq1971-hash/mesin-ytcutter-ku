import streamlit as st
import subprocess
import os

st.set_page_config(page_title="YTCutter Cloud", page_icon="✂️")
st.title("✂️ Mesin Pemotong Video (Cloud)")
st.write("Akses 24 Jam Nonstop dari HP-mu!")

# Kolom Input
link = st.text_input("Masukkan Link YouTube Utama:")
judul = st.text_input("Judul File (Tanpa spasi):", "Hasil_Potongan")
mulai = st.text_input("Waktu Mulai (contoh 00:00:10):")
selesai = st.text_input("Waktu Selesai (contoh 00:00:20):")

if st.button("🚀 MULAI POTONG DI CLOUD"):
    if link and judul and mulai and selesai:
        st.info("⏳ Sedang memproses... Tunggu sampai tombol download muncul.")
        output_file = f"{judul}.mp4"
        
        # Perintah sakti langsung ke mesin yt-dlp
        perintah = [
            "yt-dlp",
            "--download-sections", f"*{mulai}-{selesai}",
            "--force-keyframes-at-cuts",
            "-f", "bestvideo[vcodec^=avc][height<=1080]+bestaudio[ext=m4a]/bestvideo[ext=mp4]+bestaudio[ext=m4a]/best",
            "--merge-output-format", "mp4",
            link,
            "-o", output_file
        ]
        
        try:
            subprocess.run(perintah, check=True)
            if os.path.exists(output_file):
                st.success("✅ Selesai! Klik tombol di bawah:")
                with open(output_file, "rb") as file:
                    st.download_button(
                        label="📥 DOWNLOAD VIDEO KE HP",
                        data=file,
                        file_name=output_file,
                        mime="video/mp4"
                    )
            else:
                st.error("❌ File tidak ditemukan setelah diproses.")
        except Exception as e:
            st.error(f"❌ Terjadi kesalahan: {e}")
    else:
        st.warning("⚠️ Isi semua kolom dulu!")