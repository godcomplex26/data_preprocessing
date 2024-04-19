import pandas as pd
from datetime import datetime
from utils import measure_time

def find_country_code(ip_int, df):
    # ip_int가 시작IP_as_int와 끝IP_as_int 사이에 있는지 확인
    mask = (df['시작IP_as_int'] <= ip_int) & (df['끝IP_as_int'] >= ip_int)

    # 조건을 만족하는 행이 있다면 국가 코드 반환, 없다면 None 반환
    if mask.any():
        return df.loc[mask, '국가코드'].values[0]
    else:
        return "Unknown"

@measure_time
def set_country_code(file, file_ipv4, column='Trans_IP_as_int', output='./outputs/step3_country_code.csv'):
    data = pd.read_csv(file)
    ipv4 = pd.read_csv(file_ipv4)
    for index, row in data.iterrows():
        code = find_country_code(row[column], ipv4)
        data.loc[index, '국가코드'] = code
    data.to_csv(output, encoding='utf-8', index=False)

if __name__=="__main__":
    file = "./outputs/step2_ip_to_int.csv"
    file_ipv4 = "./outputs/step2-2_ipv4.csv"
    set_country_code(file, file_ipv4)