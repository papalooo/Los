Lord of SQLInjection 
orge 문제 [7단계]
if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("orge"); 
DB에 있는 pw 를 입력하면 문제가 풀린다.
쿼리문 : select id from prob_orge where id='guest' and pw='{$_GET[pw]}'
id 에 admin 을 넣기 위해 no 에 임의의 값을 넣어 쿼리문의 조건에 만족하지 않게 한다.
쿼리문뒤에 or 문을 써서 pw 의 길이를 알아낸다.
or 은 필터링 되기때문에 || 을 사용해서 pw 가 8자리 인걸 알아냈다.
사이트의 주소와 쿠키 값을 받아와 작성한 자동화 코드로 비밀번호를 알아내서 입력하면 문제가 풀린다.
pw = 7b751aec