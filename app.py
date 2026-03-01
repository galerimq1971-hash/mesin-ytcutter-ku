import streamlit as st
import subprocess
import os

st.set_page_config(page_title="YTCutter Cloud", page_icon="✂️")
st.title("✂️ Mesin Pemotong Video (Cloud)")
st.write("Akses 24 Jam Nonstop! Potong video dan langsung simpan ke HP-mu.")

# Kolom Input
link = st.text_input("Masukkan Link YouTube Utama:")
judul = st.text_input("Judul File (Tanpa spasi/tanda baca):", "Hasil_Potongan")
mulai = st.text_input("Waktu Mulai (contoh 02:45):")
selesai = st.text_input("Waktu Selesai (contoh 05:10):")

# Tombol Aksi
if st.button("🚀 MULAI POTONG DI CLOUD"):
    if link and judul and mulai and selesai:
        st.info("⏳ Mesin Cloud sedang bekerja... Mohon tunggu dan jangan tutup halaman ini.")
        
        output_file = f"{judul}.mp4"
        
        # Hapus sisa file lama jika ada yang namanya sama
        if os.path.exists(output_file):
            os.remove(output_file)
        
        # Perintah yt-dlp versi Linux (Cloud) tanpa .exe
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
            # Eksekusi di server
            subprocess.run(perintah, check=True)
            st.success("✅ Alhamdulillah Selesai! Silakan klik tombol di bawah untuk menyimpan ke HP-mu:")
            
            # Memunculkan tombol download ke HP/Laptop pengguna
            with open(output_file, "rb") as file:
                st.download_button(
                    label="📥 DOWNLOAD VIDEO SEKARANG",
                    data=file,
                    file_name=output_file,
                    mime="video/mp4"
                )
        except Exception as e:
            st.error(f"❌ Terjadi kesalahan: {e}")
    else:
        st.warning("⚠️ Harap isi semua kolom terlebih dahulu!")