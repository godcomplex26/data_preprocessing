import pandas as pd

ip_data = pd.read_csv("C:\\Users\\KB\\Desktop\\김홍근프로\\Raw_DATA\\ipv4.csv", encoding='cp949')
mal_data = pd.read_csv("C:\\Users\\KB\\Desktop\\김홍근프로\\Raw_DATA\\step1.csv", encoding='cp949')

def Find_Country(ip='1.1.1.1'):
    sips, dips, countries = [], [], []
    sips = ip_data['시작IP']
    dips = ip_data['끝IP']
    countries = ip_data['국가코드']
    count = []
    ip = list(map(lambda x: int(x), ip.split('.')))

    for sip, dip, country in zip(sips, dips, countries):
        sip = list(map(lambda x: int(x), sip.split('.')))
        dip = list(map(lambda x: int(x), dip.split('.')))

        if sip[0] <= ip[0] <= dip[0]:
            if sip[1] <= ip[1] <= dip[1]:
                if sip[2] <= ip[2] <= dip[2]:
                    return country
    return 'Unknown'

count = 0
for att in mal_data['Trans_IP']:
    coCode = Find_Country(att)
    mal_data.loc[count, 'Co_code'] = coCode
    count += 1

print(mal_data[['IP주소','Trans_IP','Co_code']])

mal_data.to_csv("C:\\Users\\KB\\Desktop\\김홍근프로\\Raw_DATA\\Step2.csv", encoding='cp949')