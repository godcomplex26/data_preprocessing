from step1_star_to_ip import random_ip
from step2_ip_to_int import dataset_ip_to_int
from step3_set_country_code import set_country_code


if __name__=="__main__":
    file = "./Raw_Data/2018_mal_data.csv"
    column = "IP주소"
    random_ip(file, column)
    
    file = "./outputs/step1_start_to_ip.csv"
    column = "Trans_IP"
    new_column = "Trans_IP_as_int"
    output="./outputs/step2_ip_to_int.csv"
    dataset_ip_to_int(file, column, new_column, output)
    
    file_ipv4 = "./Raw_DATA/ipv4.csv"
    column_ipv4 = "시작IP"
    new_col_ipv4 = "시작IP_as_int"
    output_ipv4 = "./outputs/step2-1_ipv4.csv"
    dataset_ip_to_int(file_ipv4, column_ipv4, new_col_ipv4, output_ipv4)
    
    file_ipv4_2 = output_ipv4
    column_ipv4_2 = "끝IP"
    new_col_ipv4_2 = "끝IP_as_int"
    output_ipv4_2 = "./outputs/step2-2_ipv4.csv"
    dataset_ip_to_int(file_ipv4_2, column_ipv4_2, new_col_ipv4_2, output_ipv4_2)
    
    file = "./outputs/step2_ip_to_int.csv"
    file_ipv4 = "./outputs/step2-2_ipv4.csv"
    set_country_code(file, file_ipv4)