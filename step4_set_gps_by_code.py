import pandas as pd
from datetime import datetime
from utils import measure_time, detect_encoding

def find_gps_info(code, gps_data :pd.DataFrame):
    # gps_data["국가코드"][code]
    try:
        longitude = gps_data.loc[gps_data["국가코드"] == code, "Longitude"].values[0]
        latitude = gps_data.loc[gps_data["국가코드"] == code, "Latitude"].values[0]
        return (longitude, latitude)
    except:
        return (0,0)


@measure_time
def set_gps_data(file, column='국가코드', column_lo="Longitude", column_la="Latitude", output='./outputs/step4_set_gps.csv'):
    data = pd.read_csv(file, encoding=detect_encoding(file))
    gps_data = pd.read_csv("./Raw_DATA/gps.csv", encoding=detect_encoding("./Raw_DATA/gps.csv"))
    for index, row in data.iterrows():
        gps = find_gps_info(row[column], gps_data)
        data.loc[index, column_lo] = gps[0]
        data.loc[index, column_la] = gps[1]
    data.to_csv(output, encoding='utf-8', index=False)
        

# @measure_time
# def set_country_code(file, file_ipv4, column='Trans_IP_as_int', output='./outputs/step3_country_code.csv'):
#     data = pd.read_csv(file)
#     ipv4 = pd.read_csv(file_ipv4)
#     for index, row in data.iterrows():
#         code = find_country_code(row[column], ipv4)
#         data.loc[index, '국가코드'] = code
#     data.to_csv(output, encoding='utf-8', index=False)

if __name__=="__main__":
    # file = "./outputs/step2_ip_to_int.csv"
    # file_ipv4 = "./outputs/step2-2_ipv4.csv"
    # set_country_code(file, file_ipv4)
    file = "./Raw_DATA/Goemetry.csv"
    gps_data = pd.read_csv(file, encoding=detect_encoding(file))
    print(find_gps_info("GH", gps_data))
    
    file = "./outputs/step3_country_code.csv"
    set_gps_data(file)