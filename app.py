import streamlit as st
import subprocess
import os

# JUDUL APLIKASI
st.set_page_config(page_title="GMQ YT Cutter", page_icon="✂️")
st.title("✂️ Mesin Pemotong Video (Cloud)")
st.write("Akses dari HP - Server Madrasatul Qur'an")

# INPUT DARI USER
link = st.text_input("Masukkan Link YouTube:")
judul = st.text_input("Judul Hasil Video (Tanpa Spasi):", "hasil_potongan")
mulai = st.text_input("Waktu Mulai (Contoh: 00:00:10):")
selesai = st.text_input("Waktu Selesai (Contoh: 00:00:20):")

if st.button("🚀 MULAI POTONG VIDEO"):
    if link and judul and mulai and selesai:
        output_file = f"{judul}.mp4"
        st.info("⏳ Sedang memproses... Server sedang memotong video untukmu.")
        
        # PERINTAH SAKTI (Memanggil yt-dlp sebagai aplikasi, bukan modul python)
        perintah = [
            "yt-dlp",
            "--download-sections", f"*{mulai}-{selesai}",
            "--force-keyframes-at-cuts",
            "-f", "best",
            link,
            "-o", output_file
        ]
        
        try:
            # Jalankan proses pemotongan
            subprocess.run(perintah, check=True)
            
            if os.path.exists(output_file):
                st.success("✅ SELESAI!")
                with open(output_file, "rb") as file:
                    st.download_button(
                        label="📥 DOWNLOAD KE HP SEKARANG",
                        data=file,
                        file_name=output_file,
                        mime="video/mp4"
                    )
            else:
                st.error("❌ Gagal: File tidak ditemukan di server.")
        except Exception as e:
            st.error(f"❌ Terjadi kesalahan: {e}")
    else:
        st.warning("⚠️ Mohon isi semua kolom di atas!")
