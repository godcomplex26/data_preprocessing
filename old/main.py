import pandas as pd
import random as rand
from datetime import datetime

def ip_to_int(ip):
    # IP 주소를 '.'으로 분할하여 리스트로 변환
    octets = ip.split('.')

    # 각 옥텟을 정수로 변환하고 시프트 연산을 통해 합산
    ip_int = (int(octets[0]) << 24) + (int(octets[1]) << 16) + (int(octets[2]) << 8) + int(octets[3])

    return ip_int

start_time = datetime.now().strftime("%H:%M:%S.%f")[:-3] 
print(f"start: {start_time}")

ip_data = pd.read_csv("./Raw_Data/ipv4.csv", encoding='cp949')
mal_data = pd.read_csv("./outputs/Step1.csv")

# print(ip_data.head(10))

def ipv4():
    for index, row in ip_data.iterrows():
        start_ip = row["시작IP"]
        end_ip = row["끝IP"]
        ip_data.loc[index, '시작IP_as_int'] = int(ip_to_int(start_ip))
        ip_data.loc[index, '끝IP_as_int'] = int(ip_to_int(end_ip))

    ip_data.to_csv("./outputs/ip_to_int.csv", encoding='utf-8')

def mal_ip():
    for index, row in mal_data.iterrows():
        ip = row["Trans_IP"]
        mal_data.loc[index, 'Trans_IP_as_int'] = int(ip_to_int(ip))

    mal_data.to_csv("./outputs/ip_to_int_maldata.csv", encoding='utf-8')

# ipv4()
mal_ip()
end_time = datetime.now().strftime("%H:%M:%S.%f")[:-3] 
print(f"end: {start_time}")

start_datetime = datetime.strptime(start_time, "%H:%M:%S.%f")
end_datetime = datetime.strptime(end_time, "%H:%M:%S.%f")
time_diff = end_datetime - start_datetime
print(f"시간 차이: {time_diff}")