import pandas as pd
from datetime import datetime
from utils import measure_time, detect_encoding, parse_datetime

@measure_time
def change_datetime(file="./outputs/step4_set_gps.csv", column_year='생성년도', column_month="생성월", column_date="생성일", column_time="생성시분초",
                    output='./outputs/step5_datetime.csv'):
    data = pd.read_csv(file, encoding=detect_encoding(file))
    datetime_columns = ['생성년도', '생성월', '생성일', '생성시분초']
    selected_columns = ['Trans_IP', 'Trans_IP_as_int', '국가코드', 'Latitude', 'Longitude']
    datetime_data = data[datetime_columns]
    new_data = data[selected_columns]
    for index, row in datetime_data.iterrows():
        new_data.loc[index, '생성일시'] = parse_datetime(row.tolist())
    new_data.to_csv(output, encoding='utf-8')
    
if __name__=="__main__":
    change_datetime()