import pandas as pd
import random as rand
from datetime import datetime

start_time = datetime.now().strftime("%H:%M:%S.%f")[:-3] 
print(f"start: {start_time}")

ip_data = pd.read_csv("./Raw_Data/ipv4.csv", encoding='cp949')
mal_data = pd.read_csv("./Raw_Data/2018_mal_data.csv")

l1 = []
l2 = []
for index, row in mal_data.iterrows():
    data = row["IP주소"]
    if '*' in data:
        trans_ip = data.replace('*', str(rand.randrange(0,256)))
        mal_data.loc[index, 'Trans_IP'] = trans_ip

    # r = row['data'].split('*')
    # l1.append(r[0])
    # l2.append(r[1])
mal_data.to_csv("./outputs/Step1.csv", encoding='utf-8')

# def Find_Country(ip='1.1.1.1'):
#     sips, dips, countries = [], [], []
#     sips = ip_data['시작IP']
#     dips = ip_data['끝IP']
#     countries = ip_data['국가코드']
#     count = []
#     ip = list(map(lambda x: int(x), ip.split('.')))

#     for sip, dip, country in zip(sips, dips, countries):
#         sip = list(map(lambda x: int(x), sip.split('.')))
#         dip = list(map(lambda x: int(x), dip.split('.')))

#         if sip[0] <= ip[0] <= dip[0]:
#             if sip[1] <= ip[1] <= dip[1]:
#                 if sip[2] <= ip[2] <= dip[2]:
#                     return country
#     return 'Unknown'


# count = 0

# for row in mal_data.loc[:, 'IP주소']:
#     trans_ip = row.replace('*', str(rand.randrange(0,256)))
#     mal_data.loc[count, 'Trans_IP'] = trans_ip
#     count += 1
# print(mal_data.head(10))

# mal_data.to_csv("./outputs/Step1.csv", encoding='cp949')
end_time = datetime.now().strftime("%H:%M:%S.%f")[:-3] 
print(f"end: {start_time}")