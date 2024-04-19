import pandas as pd
import random as rand
from utils import detect_encoding, measure_time

# ip_data = pd.read_csv("./Raw_Data/ipv4.csv", encoding='cp949')
# mal_data = pd.read_csv("./Raw_Data/2018_mal_data.csv")

# for index, row in mal_data.iterrows():
#     data = row["IP주소"]
#     if '*' in data:
#         trans_ip = data.replace('*', str(rand.randrange(0,256)))
#         mal_data.loc[index, 'Trans_IP'] = trans_ip

# mal_data.to_csv("./outputs/Step1.csv", encoding='utf-8')

@measure_time
def random_ip(file, col_name, new_col_name="Trans_IP", output="./outputs/step1_start_to_ip.csv"):
    encoding = detect_encoding(file)
    data = pd.read_csv(file, encoding=encoding)
    for index, row in data.iterrows():
        if '*' in row[col_name]:
            trans_ip = row[col_name].replace('*', str(rand.randrange(0,256)))
            data.loc[index, new_col_name] = trans_ip
    data.to_csv(output, encoding='utf-8', index=False)
    
if __name__=="__main__":
    file = "./Raw_Data/2018_mal_data.csv"
    column = "IP주소"
    random_ip(file, column)