from step1_star_to_ip import random_ip
from step2_ip_to_int import dataset_ip_to_int
from step3_set_country_code import set_country_code
from step4_set_gps_by_code import set_gps_data
from step5_datetime import change_datetime
from utils import measure_time

step1 = {
    "file": "./Raw_Data/KIS_KIS00000000000000006_20201110000000.csv",
    "column": "IP주소"
    }

step2 = {
    "file": "./outputs/step1_start_to_ip.csv",
    "column": "Trans_IP",
    "new_column": "Trans_IP_as_int",
    "output": "./outputs/step2_ip_to_int.csv"
}

step2_1 = {
    "file": "./Raw_DATA/ipv4.csv",
    "column":"시작IP",
    "new_column": "시작IP_as_int",
    "output": "./outputs/step2-1_ipv4.csv"
}

step2_2 = {
    "file": "./outputs/step2-1_ipv4.csv",
    "column": "끝IP",
    "new_column": "끝IP_as_int",
    "output": "./outputs/step2-2_ipv4.csv"
}

step3 = {
    "file": "./outputs/step2_ip_to_int.csv",
    "file_ipv4": "./outputs/step2-2_ipv4.csv"
}

step4 = {
    "file": "./outputs/step3_country_code.csv"
}

step5 = {
    "file": "./outputs/step4_set_gps.csv"
}

@measure_time
def run_all():
    random_ip(step1["file"], step1["column"])
    dataset_ip_to_int(step2["file"], step2["column"], step2["new_column"], step2["output"])
    dataset_ip_to_int(step2_1["file"], step2_1["column"], step2_1["new_column"], step2_1["output"])
    dataset_ip_to_int(step2_2["file"], step2_2["column"], step2_2["new_column"], step2_2["output"])
    set_country_code(step3["file"], step3["file_ipv4"])
    set_gps_data(step4["file"])
    change_datetime(step5["file"])

if __name__=="__main__":
    change_datetime(step5["file"])
    # run_all()