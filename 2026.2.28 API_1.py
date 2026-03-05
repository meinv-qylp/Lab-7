import requests
import os


API_KEY = os.getenv('HOLIDAY_API_KEY')


COUNTRY = input("Select country(for example: RU US CN AM ....) :")
YEAR = input("Enter year(free: last year) :")


URL = f"https://holidayapi.com/v1/holidays"


canshu = {
    "key": API_KEY,
    "country": COUNTRY,
    "year": YEAR
}


def output():
    global i,h
    print(f"{i}. {h['name']}")
    print(f"Date :{h['date']}")
    print(f"Weekday :{h['weekday']['date']['name']}")
    if h['public'] == True:
        print(f"Type :Public")
    else:
        print(f"Type :not public")    
    print(f"Country :{h['country']}")
    print(f"Observed :{h['observed']}")


try:
    response = requests.get(url, params=canshu)  #  ！最核心的请求网址，以及上传参数的代码 ！
    data = response.json()
    #  response.status_code == 200 用来判断API是否请求成功，200 是HTTP请求成功的状态码 
    if response.status_code == 200:
        if data.get('holidays'):
            print(f"there were {len(data['holidays'])} holidays in {COUNTRY} in {YEAR}")
            # print(data['holidays'])    # 查看输出格式
            A = input("View all holidays(Y/N):")
            if A== "Y":
                for i, h in enumerate(data['holidays'], 1):
                    output()  
            else:
                for i, h in enumerate(data['holidays'], 1):
                    output()
                    if i >3:
                        break
                print(".\n.\n.\n.")

        else:
            print("No holidays found...")        
    else:
        print(f"API request failed, failed to obrain data")


except Exception as reason:
    print(f"Program error: {reason}")

