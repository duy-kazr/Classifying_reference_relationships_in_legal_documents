import re
import pandas as pd
import numpy as np
import tensorflow as tf
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import libs.Extract_entity as extract_entity

from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential, Model, load_model
from keras_self_attention import SeqSelfAttention
import streamlit as st

def tokenization(data, max_length):
    Text_col = data
    tokenizer = Tokenizer(split=' ')
    tokenizer.fit_on_texts(Text_col)
    words_to_index = tokenizer.word_index
    vocab_size = len(words_to_index) + 1

    # chuyển đổi dữ liệu văn bản thành các chuỗi số
    tokenizer_seq = tokenizer.texts_to_sequences(Text_col)

    # Đảm bảo mỗi sequece có cùng độ dài
    # 'post' có nghĩa là thêm padding vào cuối mỗi sequence
    # 'pre' có nghĩa là thêm padding vào đầu mỗi sequence
    tokenizer_pad = pad_sequences(tokenizer_seq, padding='pre', maxlen=max_length)

    return tokenizer_pad, vocab_size, words_to_index

def load_dicchar():
    dic = {}
    char1252 = 'à|á|ả|ã|ạ|ầ|ấ|ẩ|ẫ|ậ|ằ|ắ|ẳ|ẵ|ặ|è|é|ẻ|ẽ|ẹ|ề|ế|ể|ễ|ệ|ì|í|ỉ|ĩ|ị|ò|ó|ỏ|õ|ọ|ồ|ố|ổ|ỗ|ộ|ờ|ớ|ở|ỡ|ợ|ù|ú|ủ|ũ|ụ|ừ|ứ|ử|ữ|ự|ỳ|ý|ỷ|ỹ|ỵ|À|Á|Ả|Ã|Ạ|Ầ|Ấ|Ẩ|Ẫ|Ậ|Ằ|Ắ|Ẳ|Ẵ|Ặ|È|É|Ẻ|Ẽ|Ẹ|Ề|Ế|Ể|Ễ|Ệ|Ì|Í|Ỉ|Ĩ|Ị|Ò|Ó|Ỏ|Õ|Ọ|Ồ|Ố|Ổ|Ỗ|Ộ|Ờ|Ớ|Ở|Ỡ|Ợ|Ù|Ú|Ủ|Ũ|Ụ|Ừ|Ứ|Ử|Ữ|Ự|Ỳ|Ý|Ỷ|Ỹ|Ỵ'.split(
        '|')
    charutf8 = "à|á|ả|ã|ạ|ầ|ấ|ẩ|ẫ|ậ|ằ|ắ|ẳ|ẵ|ặ|è|é|ẻ|ẽ|ẹ|ề|ế|ể|ễ|ệ|ì|í|ỉ|ĩ|ị|ò|ó|ỏ|õ|ọ|ồ|ố|ổ|ỗ|ộ|ờ|ớ|ở|ỡ|ợ|ù|ú|ủ|ũ|ụ|ừ|ứ|ử|ữ|ự|ỳ|ý|ỷ|ỹ|ỵ|À|Á|Ả|Ã|Ạ|Ầ|Ấ|Ẩ|Ẫ|Ậ|Ằ|Ắ|Ẳ|Ẵ|Ặ|È|É|Ẻ|Ẽ|Ẹ|Ề|Ế|Ể|Ễ|Ệ|Ì|Í|Ỉ|Ĩ|Ị|Ò|Ó|Ỏ|Õ|Ọ|Ồ|Ố|Ổ|Ỗ|Ộ|Ờ|Ớ|Ở|Ỡ|Ợ|Ù|Ú|Ủ|Ũ|Ụ|Ừ|Ứ|Ử|Ữ|Ự|Ỳ|Ý|Ỷ|Ỹ|Ỵ".split(
        '|')
    for i in range(len(char1252)):
        dic[char1252[i]] = charutf8[i]
    return dic

# Chuyển đổi mã kí tự 1252 sang UTF-8
def covert_unicode(text):
    dicchar = load_dicchar()
    return re.sub(
        r'à|á|ả|ã|ạ|ầ|ấ|ẩ|ẫ|ậ|ằ|ắ|ẳ|ẵ|ặ|è|é|ẻ|ẽ|ẹ|ề|ế|ể|ễ|ệ|ì|í|ỉ|ĩ|ị|ò|ó|ỏ|õ|ọ|ồ|ố|ổ|ỗ|ộ|ờ|ớ|ở|ỡ|ợ|ù|ú|ủ|ũ|ụ|ừ|ứ|ử|ữ|ự|ỳ|ý|ỷ|ỹ|ỵ|À|Á|Ả|Ã|Ạ|Ầ|Ấ|Ẩ|Ẫ|Ậ|Ằ|Ắ|Ẳ|Ẵ|Ặ|È|É|Ẻ|Ẽ|Ẹ|Ề|Ế|Ể|Ễ|Ệ|Ì|Í|Ỉ|Ĩ|Ị|Ò|Ó|Ỏ|Õ|Ọ|Ồ|Ố|Ổ|Ỗ|Ộ|Ờ|Ớ|Ở|Ỡ|Ợ|Ù|Ú|Ủ|Ũ|Ụ|Ừ|Ứ|Ử|Ữ|Ự|Ỳ|Ý|Ỷ|Ỹ|Ỵ',
        lambda x: dicchar[x.group()], text)

def text_preprocessing(document):
    # Chuyển đổi mã kí tự 1252 sang UTF-8
    document['Text'] = document['Text'].apply(covert_unicode)
    # Đưa về dạng chữ thường
    document['Text'] = str(document['Text']).lower()
    # xóa các ký tự không cần thiết
    document['Text'] = document['Text'].apply(lambda x: re.sub(r'[^\w\s]', '', str(x)))
    document = document['Text'].apply(lambda y: re.sub(r'[^\s\wáàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệóòỏõọôốồổỗộơớờởỡợíìỉĩịúùủũụưứừửữựýỳỷỹỵđ_]',' ',str(y)))
    return document


def entity_Extraction(A, sentence):
    key_dict = {
        'Hiến_pháp': 'HP',
        'Bộ_luật': 'BL',
        'Luật': 'LT',
        'Pháp_lệnh': 'PL',
        'Lệnh': 'LH',
        'Quyết_định': 'QĐ',
        'Nghị_định': 'NĐ',
        'Nghị_quyết': 'NQ',
        'Nghị_quyết liên_tịch': 'NQLT',
        'Thông_tư': 'TT',
        'Thông_tư liên_tịch': 'TTLT',
        'Chỉ_thị': 'CT',
    }

    specialCharset = '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'

    def check_entity(child_line): 
        pattern = re.compile(r'((?:(?!ngày|tháng|năm|số)\w+[ _,]+)+)?(_số|số)?\s?(\d+?[\w]+(?:(?:/|-)+(?:\d|\w)+)+)?\s?((?:năm |tháng |ngày |)(?:\d{4}|\d{1,2}))?((?: năm | tháng |[-]|[/])(?:\d{4}|\d{1,2}))?((?: năm |[-]|[/])\d{4})?')
        matches = pattern.findall(child_line)
        

        entity = []
        for match in matches:
            match = [en for en in match if en]
            if match:
                entity.append(match)

        if entity:
            entity = ' '.join(entity[0]).replace('  ', ' ').replace(' -', '-').replace(' /', '/')
            filter_entity = ['quy định','được sửa_đổi , bổ_sung','bị thay_thế','dẫn_chiếu','căn_cứ','được hướng_dẫn','hết hiệu_lực','hiến_pháp','bộ_luật','luật','pháp_lệnh','lệnh','quyết_định','nghị_định','nghị_quyết','nghị_quyết liên_tịch','thông_tư','thông_tư liên_tịch','chỉ_thị']
            for word in filter_entity:
                if word in entity:
                    entity = entity.split(word)[0]
                    break
            entity = entity.strip()

            return entity

        return False

    def extracting_entity(line, key):
        entity_list = []
        # Hiến pháp được xử lý riêng vì đây là trường hợp đặc biệt
        if key == 'Hiến_pháp':
            pattern = rf'({key}) '+ r'(nước Cộng_hoà xã_hội chủ_nghĩa Việt_nam)?\s?(\d+|năm \d+)?'
            matches = re.findall(pattern, line)
            for match in matches:
                match = [m for m in match if m]
                if match and len(match) > 1:
                    Entity = ' '.join(match).strip()
                    entity_list.append(Entity)
        else:
            # tách các đối tượng trên 1 dòng thành các phần tử theo loại văn bản
            list_child_line = line.split(key)
            if len(list_child_line) > 1:
                for i_child_line in range(1, len(list_child_line)): 
                    Entity = ''
                    child_line = list_child_line[i_child_line]
                    child_line = child_line.strip()

                    if child_line:
                        first_child_line = child_line.split()[0]
                        # Lọc các xong có chứa ký tự không liên quan
                        if not (any(True for wrong in ['này', 'khác', 'có'] if wrong == first_child_line) or 
                            (list_child_line[i_child_line - 1].split() and list_child_line[i_child_line - 1].split()[-1] in key_dict.keys()) or
                            first_child_line in specialCharset or
                            (first_child_line == 'liên_tịch' and key in ['Nghị_định', 'Thông_tư'])):
                        
                            # Tìm đối tượng được nhắc tới
                            entity = check_entity(child_line)
                            if not entity:
                                continue
                            key_plus = key + ' '
                            if entity[0] == '_':
                                key_plus = key
                            Entity = key_plus + entity
                            entity_list.append(Entity)

                            
        return entity_list

    list_B = {
        'Thực thể tham chiếu': [],
        'Nội dung trước thực thể được tham chiếu': [],
        'Thực thể được tham chiếu': [],
        'Nội dung sau thực thể được tham chiếu': []
    }

    list_entity = []
    for key in key_dict.keys():
        if key in sentence:
            entity = extracting_entity(sentence, key)
            if entity:
                list_entity.extend(entity)

    list_entity = list(set(list_entity))

    for B in list_entity:
        if B in A:
            continue
        pattern_i = r'([\w+\s_^;.<()>:]+)?' + rf'{B}' + r'([\w+\s_^;.<()>:]+)?'
        match_i = re.findall(pattern_i, sentence)
    
        for match in match_i:
            list_B['Thực thể tham chiếu'].append(A)
            list_B['Nội dung trước thực thể được tham chiếu'].append(match[0])
            list_B['Thực thể được tham chiếu'].append(B)
            list_B['Nội dung sau thực thể được tham chiếu'].append(match[1])

    # Kiểm tra xem list_B có chứa dữ liệu không trước khi tạo DataFrame
    if any(len(values) > 0 for values in list_B.values()):
        df = pd.DataFrame(list_B)
        return df
    else:
        return pd.DataFrame()
    

def main(input_A,input_B):

    PATH_MODEL = 'models/model_tvpl_250_250lstmunits_128_20_0.2_0.1_1121956.82.h5'
    max_length = 250

    with tf.keras.utils.custom_object_scope({'SeqSelfAttention': SeqSelfAttention}):
        # Load mô hình
        loaded_model = load_model(PATH_MODEL)
    
    # Xử lý những trường hợp lí tự dính nhau
    extraction = extract_entity.tvpl_function()
    A_processing = extraction.data_processing(input_A)
    B_processing = extraction.data_processing(input_B)

    X = entity_Extraction(A_processing, B_processing)

    if not X.empty:

        X['Text'] = X.apply(lambda d: f"{d['Thực thể tham chiếu']} {d['Nội dung trước thực thể được tham chiếu']} {d['Thực thể được tham chiếu']} {d['Nội dung sau thực thể được tham chiếu']}".strip(), axis=1)
        X['Text'] = text_preprocessing(X)

        data_tokenizer_pad_new, vocab_size_new, words_to_index_new = tokenization(X['Text'], max_length)

        label = ['BTT', 'CC', 'DC', 'DSD', 'DHD', 'HHL', 'None']

        # Dự đoán trên dữ liệu mới (X_new)
        predictions = loaded_model.predict(data_tokenizer_pad_new)


        # Mã hóa label
        label_encode = LabelEncoder()
        label_encode = label_encode.fit(label)
        y_pred_original = label_encode.inverse_transform(np.argmax(predictions, axis=1))

        y_pred_original_lst = []

        for i in y_pred_original:
            if i == 'BTT':
                y_pred_original_text = 'Bị thay thế'
            elif i == 'DC':
                y_pred_original_text = 'Dẫn chiếu'
            elif i == 'DHD':
                y_pred_original_text = 'Được hướng dẫn'
            elif i == 'DSD':
                y_pred_original_text = 'Được sửa đổi hoặc bổ sung'
            elif i == 'CC':
                y_pred_original_text = 'Căn cứ'
            elif i == 'HHL':
                y_pred_original_text = 'Hết hiệu lực'
            else:
                y_pred_original_text = 'Không có quan hệ với thực thể tham chiếu'
            
            y_pred_original_lst.append(y_pred_original_text)

        st.markdown(f"<hr><br> <u>Văn bản:</u> <h4>{A_processing}</h4> <br>", unsafe_allow_html=True)

        output = pd.DataFrame({'Quan hệ': y_pred_original_lst, 'Thực thể được tham chiếu': X['Thực thể được tham chiếu']})

        output['Thực thể được tham chiếu'] = output['Thực thể được tham chiếu'].astype(str).str.pad(width=155, side='right')
        
        st.dataframe(output, width=700, height=400)
    else:
        st.write("Không tìm thấy đối tượng trong đoạn văn")


if __name__ == "__main__":

    

    st.write("# Phân loại quan hệ dẫn chiếu")

    tabs_font_css = """
    <style>
    div[class*="stTextArea"] label {
        font-size: 30px;
        color: red;
    }

    div[class*="stTextInput"] label {
        font-size: 30px;
        color: cyan;
    }
    </style>
    """

    st.write(tabs_font_css, unsafe_allow_html=True)
    
    input_A = st.text_input("Nhập đối tượng tham chiếu", "")
    input_B = st.text_area("Nhập đoạn văn chứa đối tượng được tham chiếu", "")

    if st.button('Classify'):
        main(input_A, input_B)
