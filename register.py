import streamlit as st
import cv2
import numpy as np
from utils import get_embedding, save_knowledge_base, load_knowledge_base

st.set_page_config(page_title="Pendaftaran Wajah Pegawai", layout="centered")
st.title("📝 Daftarkan Wajah Pegawai Baru")

name = st.text_input("Masukkan Nama Pegawai")
img_file = st.camera_input("Ambil Foto Wajah Pegawai")

if img_file is not None and name:
    bytes_data = img_file.getvalue()
    image = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    st.image(image, channels="BGR", caption="📷 Foto yang diambil")

    embedding = get_embedding(image)
    if embedding is not None:
        kb = load_knowledge_base()
        kb.append({
            "user": name,
            "embedding": embedding,
            "threshold": 0.6
        })
        save_knowledge_base(kb)
        st.success(f"✅ Pegawai '{name}' berhasil didaftarkan!")
    else:
        st.warning("⚠️ Wajah tidak terdeteksi. Silakan coba ulangi dengan posisi wajah yang jelas.")
