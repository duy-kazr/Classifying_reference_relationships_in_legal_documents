import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="🏠",
)

st.write("# KLTN_K20_2020-2024! 🏠")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Đây là bài làm khóa luận tốt nghiệp được thực hiện bởi các sinh viên:
    Nguyễn Phạm Ngọc Duy - 20133031  
    Trì Hoài Lộc         - 20133063  
    Project được xây dựng bằng Python và deploy trên Streamlit.
    ### Contact
    - Email: (kazr1582@gmail.com)
    - Github Website: (https://github.com/crytalwing/Classifying_reference_relationships_in_legal_documents)
    - Project: (https://github.com/crytalwing/kltn)
"""
)
