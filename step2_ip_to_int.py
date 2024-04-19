import pandas as pd
from utils import detect_encoding, measure_time

def ip_to_int(ip):
    # IP 주소를 '.'으로 분할하여 리스트로 변환
    octets = ip.split('.')
    # 각 옥텟을 정수로 변환하고 시프트 연산을 통해 합산
    ip_int = (int(octets[0]) << 24) + (int(octets[1]) << 16) + (int(octets[2]) << 8) + int(octets[3])
    return ip_int

@measure_time
def dataset_ip_to_int(file, col_name, new_col_name, output="./outputs/step2_ip_to_int.csv"):
    encoding = detect_encoding(file)
    data = pd.read_csv(file, encoding=encoding)
    for index, row in data.iterrows():
        ip = row[col_name]
        int_ip = ip_to_int(ip)
        data.loc[index, new_col_name] = int_ip
    data.to_csv(output, encoding='utf-8', index=False)
    
if __name__=="__main__":
    file = "./outputs/step1_start_to_ip.csv"
    column = "Trans_IP"
    new_column = "Trans_IP_as_int"
    output="./outputs/step2_ip_to_int.csv"
    dataset_ip_to_int(file, column, new_column, output)
    
    # file_ipv4 = "./Raw_DATA/ipv4.csv"
    # column_ipv4 = "시작IP"
    # new_col_ipv4 = "시작IP_as_int"
    # output_ipv4 = "./outputs/step2-1_ipv4.csv"
    # dataset_ip_to_int(file_ipv4, column_ipv4, new_col_ipv4, output_ipv4)
    
    # file_ipv4_2 = output_ipv4
    # column_ipv4_2 = "끝IP"
    # new_col_ipv4_2 = "끝IP_as_int"
    # output_ipv4_2 = "./outputs/step2-2_ipv4.csv"
    # dataset_ip_to_int(file_ipv4_2, column_ipv4_2, new_col_ipv4_2, output_ipv4_2)