import streamlit as st

st.set_page_config(
    page_title="Ashish Kumar Tripathi - CV",
    page_icon="📄",
    layout="wide"
)

# Left Column
left, right = st.columns([1,3])

with left:
    st.title("Ashish Kumar Tripathi")
    st.caption("B.Tech Student — AI & ML")

    st.markdown("### Personal Info")
    st.write("📞 +91 7905736061")
    st.write("📧 ashishtripathi67991@gmail.com")
    st.write("📍 Raebareli, Uttar Pradesh")

    st.markdown("**LinkedIn:** _Coming soon_")
    st.markdown("**GitHub:** _Coming soon_")
    st.markdown("**Figma:** _Coming soon_")

    st.markdown("### Languages")
    st.progress(95)
    st.text("Hindi — Native")

    st.progress(65)
    st.text("English — Beginner–Intermediate")

    st.markdown("### Core Strengths")
    st.write("- Adaptive")
    st.write("- Curious")
    st.write("- Fast Learner")


with right:
    st.header("Profile Summary")
    st.write("""
Dedicated undergraduate specializing in **Artificial Intelligence and Machine Learning**
with strong foundations in **Python, JavaScript, HTML and CSS**.
Experienced in content writing, documentation formatting and English–Hindi translation.
Known for adaptability, curiosity, and rapid learning.
Actively building projects to strengthen applied programming skills.
""")

    st.header("Education")

    st.subheader("2029 - Lovely Professional University")
    st.write("B.Tech – Computer Science (AI & ML) — Semester 1")

    st.subheader("2024 - Class XII – Intermediate")
    st.write("Lucknow Public School, Raebareli")

    st.subheader("2022 - Class X – High School")
    st.write("Lucknow Public School, Raebareli")

    st.header("Technical Skills")
    st.write("""
- **Programming:** Python, JavaScript  
- **Web:** HTML, CSS  
- **Data Tools:** Excel, Google Sheets, Data Entry  
- **Writing:** Articles, Product Descriptions, Translation
""")

    st.header("Projects")

    st.subheader("2025 — Python Calculator")
    st.write("CLI calculator performing arithmetic operations using conditional logic.")

    st.subheader("2025 — Student Result Management System")
    st.write("""
Python-based program to record marks, compute totals,
calculate percentage and assign grades using flow control and formatted outputs.
""")

    st.header("Career Objective")
    st.write("""
To establish a strong professional footprint in the field of
**Artificial Intelligence and Machine Learning**
through continuous academic excellence and practical software development.
""")
