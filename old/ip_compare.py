import pandas as pd
from datetime import datetime
from io import StringIO

ip_data = pd.read_csv("./outputs/ip_to_int.csv")
mal_data = pd.read_csv("./outputs/ip_to_int_maldata.csv")

start_time = datetime.now().strftime("%H:%M:%S.%f")[:-3] 
print(f"start: {start_time}")

def find_country_code(ip_int, df):
    # ip_int가 시작IP_as_int와 끝IP_as_int 사이에 있는지 확인
    mask = (df['시작IP_as_int'] <= ip_int) & (df['끝IP_as_int'] >= ip_int)

    # 조건을 만족하는 행이 있다면 국가 코드 반환, 없다면 None 반환
    if mask.any():
        return df.loc[mask, '국가코드'].values[0]
    else:
        return "Unknown"

def write_country_code():
    for index, row in mal_data.iterrows():
        code = find_country_code(row['Trans_IP_as_int'], ip_data)
        mal_data.loc[index, '국가코드'] = code

    mal_data.to_csv("./outputs/mal_data_step2.csv", encoding='utf-8', index=False)

print(find_country_code(3390500625, ip_data))

write_country_code()

end_time = datetime.now().strftime("%H:%M:%S.%f")[:-3] 
print(f"end: {start_time}")

start_datetime = datetime.strptime(start_time, "%H:%M:%S.%f")
end_datetime = datetime.strptime(end_time, "%H:%M:%S.%f")
time_diff = end_datetime - start_datetime
print(f"시간 차이: {time_diff}")