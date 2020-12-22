Lord of SQLInjection 
orc 문제 [4단계]

if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("orc"); 

db에 id가 admin인 행의 pw 를 알아내야한다.
'or length(pw) = ? # 의 형태로 pw 의 길이를 알아내고

자동화 코드를 작성하여 비밀번호를 알아낼 수 있다.
숫자와 문자를 모두 비교하기위해 substr 로 알아낸 비밀번호를 ascii 코드 값으로 바꿔준후 비교하여
pw를 한자리씩 찾아낸다.

