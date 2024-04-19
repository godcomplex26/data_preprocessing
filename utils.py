from datetime import datetime
import chardet

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        print(f"start: {start_time}")
        
        result = func(*args, **kwargs)
        
        end_time = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        print(f"end: {end_time}")
        
        start_datetime = datetime.strptime(start_time, "%H:%M:%S.%f")
        end_datetime = datetime.strptime(end_time, "%H:%M:%S.%f")
        time_diff = end_datetime - start_datetime
        print(f"걸린 시간: {time_diff}")
        
        return result
    return wrapper


def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        result = chardet.detect(file.read())
        encoding = result['encoding']
        # confidence = result['confidence']
        # print(f"Detected encoding: {encoding} (Confidence: {confidence})")
        return encoding
    

if __name__=="__main__":
    print(detect_encoding('./Raw_DATA/2018_mal_data.csv'))