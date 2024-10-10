import os
from dotenv import load_dotenv

# 載入 .env 文件中的環境變量  這一行是為了讀取環境變量  再測試
load_dotenv()

# 讀取 test_key 環境變量
test_key = os.getenv('test_key')
print(f"測試環境變量: {test_key}")

def 西元轉民國(西元年):
    return 西元年 - 1911

def 民國轉西元(民國年):
    return 民國年 + 1911

while True:
    選擇 = input("請選擇轉換類型 (1: 西元轉民國, 2: 民國轉西元, q: 退出): ")
    
    if 選擇 == 'q':
        print("感謝使用，再見！")
        break
    
    if 選擇 not in ['1', '2']:
        print("無效的選擇，請重新輸入。")
        continue
    
    年份 = input("請輸入年份: ")
    
    try:
        年份 = int(年份)
    except ValueError:
        print("請輸入有效的數字。")
        continue
    
    if 選擇 == '1':
        if 年份 < 1912:
            print("西元年份必須大於或等於1912。")
        else:
            結果 = 西元轉民國(年份)
            print(f"西元 {年份} 年相當於民國 {結果} 年。")
    else:
        結果 = 民國轉西元(年份)
        print(f"民國 {年份} 年相當於西元 {結果} 年。")
