import streamlit as st

st.set_page_config(
    page_title="Main Page",
    page_icon="🏠",
)

st.title(":blue[WEBSITE PHÂN LOẠI QUAN HỆ DẪN CHIẾU TRONG VĂN BẢN PHÁP QUY]")

st.markdown(
    """

    - *Đây là Project tốt nghiệp của sinh viên Trường Đại học Sư phạm Kỹ thuật TP.HCM*

    - ***GVHD***: *ThS.Trần Trọng Bình*

"""
)

st.sidebar.success("Select a demo above.")

duy, loc = st.columns(2)

duy.markdown(
    """
    ## Thông tin sinh viên:

    - **Họ và tên**: *Nguyễn Phạm Ngọc Duy* \n

    - **MSSV**: *20133031*  \n

    - **Github**: [KaZR](https://github.com/crytalwing)
"""
)

loc.markdown(
    """
    ## Thông tin sinh viên:

    - **Họ và tên**: *Trì Hoài Lộc* \n

    - **MSSV**: *20133063*  \n

    - **Github**: [HoaiLocTri](https://github.com/HoaiLocTri)
"""
)

st.markdown(
    """

    ### ***Note:***
    - *Hiện tại website chỉ có chức năng phân loại dựa trên đoạn văn được đưa vào.*
    
    - *Website sẽ được cập nhật thêm chức năng phân loại dựa trên file văn bản trong tương lai.*
"""
)
