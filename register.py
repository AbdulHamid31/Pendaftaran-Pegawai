import streamlit as st

st.title("📊 Diagram Alur Penelitian Otomatis")

st.write("Masukkan langkah-langkah alur dengan format seperti ini:")
st.code("""
[Mulai]
   ↓
[Perumusan Masalah]
   ↓
...
[Selesai]
""", language="text")

steps_input = st.text_area("Langkah-langkah alur penelitian:", """
[Mulai]
   ↓
[Perumusan Masalah]
   ↓
[Pengumpulan Dataset Dota 2]
   ↓
[Preprocessing Data]
   ↓
[Ekstraksi Fitur Time-Series & Sosial]
   ↓
[Embedding Graph dengan DeepWalk/LINE]
   ↓
[Clustering dengan K-Means]
   ↓
[Evaluasi & Visualisasi Klaster]
   ↓
[Interpretasi Hasil & Simpulan]
   ↓
[Selesai]
""")

if st.button("Buat Diagram"):
    # Proses parsing
    lines = [line.strip('[]').strip() for line in steps_input.splitlines() if line.strip() and not line.strip().startswith('↓')]
    if len(lines) < 2:
        st.error("Masukkan minimal 2 langkah.")
    else:
        edges = [f'"{lines[i]}" -> "{lines[i+1]}"' for i in range(len(lines)-1)]
        graph_code = "digraph ResearchFlow {\n" \
                      "rankdir=TB;\n" \
                      "node [shape=box, style=rounded, color=blue];\n" + \
                      "\n".join(edges) + "\n}"

        st.subheader("Hasil Diagram Alur:")
        st.graphviz_chart(graph_code)
