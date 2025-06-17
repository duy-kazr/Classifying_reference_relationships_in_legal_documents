# **Website tóm tắt văn bản báo chí và luật pháp**
## 1. Project Description
Với sự phức tạp của hệ thống tài liệu trong lĩnh vực pháp luật, nhằm thuận tiện cho việc trích xuất các Nghị định/ Hiến pháp/ Thông tư ... và phân loại quan hệ dẫn chiếu giữa chúng với văn bản hiện hành, chúng tôi quyết định xây dựng một ứng dụng hỗ trợ cho việc trích xuất đối tượng tham chiếu và phân loại quan hệ dẫn chiếu.

Website có một số chức năng hữu ích như sau:
1. Trích xuất các đối tượng trong văn bản pháp luật.
2. Phân loại quan hệ dẫn chiếu giữa văn bản và các đối tượng tham chiếu bên trong.

Chúng tôi đã sử dụng [Streamlit](https://streamlit.io/) framework để xây dựng lên website này.
## 2. Khởi chạy ứng dụng
Để khởi chạy ứng dụng, đầu tiên ta mở cửa sổ command prompt ngay trong thư mục và sau đó chạy lệnh
```
streamlit run Home_page.py
```


## 3. Sử dụng ứng dụng website
Đầu tiên, ta cần phân biệt được rằng đâu là đối tượng tham chiếu đâu là đối tượng được tham chiếu.
```Đối tượng tham chiếu``` ở đây chính là ```title``` của văn bản pháp luật đầu vào và ```Đối tượng được tham chiếu``` là những văn bản pháp luật khác được đề cập bên trong văn bản này.

Để sử dụng trang web, đơn giản chỉ cần nhập ```title``` của văn bản pháp luật đầu vào vào ô ```Đối tượng tham chiếu```, sau đó copy nội dung của văn bản đó vào ô ```Đoạn văn chứa đối tượng được tham chiếu``` sau đó nhấn vào button ```Classify``` để thực thi.


## 4. Data
Bộ dữ liệu luật pháp Việt Nam được lấy từ:
1. [Cơ sở dữ liệu Quốc gia về văn bản pháp luật](https://vbpl.vn/pages/portal.aspx)
2. [Thư viện Pháp luật](https://thuvienphapluat.vn/)
   
## 5. Người thực hiện
1. Nguyễn Phạm Ngọc Duy
2. Trì Hoài Lộc
### Người hướng dẫn
ThS. Trần Trọng Bình
