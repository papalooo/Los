Lord of SQLInjection 
darkknight 문제 [11단계]
if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("darkknight"); 
DB에 있는 pw 값을 알아내서 입력하면 문제가 풀린다.
싱글쿼터('),substr,ascii,등호(=) 가 필터링 되어있기 때문에 쿼리문에 or id like  char(0x61, 0x64, 0x6d, 0x69, 0x6e) and length(pw) in (?) 형태의 구문을 집어넣어 길이를 구하도록 한다. 해서 pw 가 8자리 라는 것을 알아낼 수 있다.
그 다음은 자동화 코드를 작성해 pw 의 값을 알아내야 한다.
ascii 와 substr 이 필터링 되기 때문에 ascii 대신 같은 기능읋 하는 ord, substr 대신 mid 를 사용했다.
등호도 필터링 되기 때문에 pw 을 알아낼 땐 in 을 사용해 주었다.
"1 or id like char(0x61, 0x64, 0x6d, 0x69, 0x6e) and ord(mid(pw,{},1)) in ({})".format(pw_value,ascii)
의 형태로 쿼리문을 작성해준다.
코드를 실행해서 알아낸 pw 를 쿼리에 넣어준다.
?pw = 0b70ea1f