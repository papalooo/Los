Lord of SQLInjection 
orc 문제 [4단계]
if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("orc"); 
DB에 있는 id가 admin 인 
쿼리문 : select id from prob_orge where id='guest' and pw='{$_GET[pw]}'
id 에 admin 을 넣기 위해 no 에 임의의 값을 넣어 쿼리문의 조건에 만족하지 않게 한다.
no 에 1을 넣었을 때 Hello guest 라고 출력된다.
guest 의 no 은 1인것같으니 1외에 다른 값을 넣으면
Hello guest가 출력되지않는다
쿼리문에 or id = [값] 의 형태로 admin 을 넣어줘야한다
하지만 따옴표가 필터링 되니 url 인코딩 상에서 따옴표인 %27을 사용해서 입력을 해봤다.
하지만 %27도 필터링 되었다. 
다음 방법으로 admin 을 hex 값으로 변환해서 입력해보았다. (https://www.online-toolz.com/langs/ko/tool-ko-text-hex-convertor.html)
admin 의 hex 값은 0x61646d696e 이다
이를 이용해 or id = 0x61646d696e 를 쿼리문에 추가하면
문제가 해결된다