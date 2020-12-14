Lord of SQLInjection 
cobolt 문제 [2단계]
if($result['id']== 'admin') solve("cobolt")
id 의 값으로 admin이 들어가게 되면 문제가 풀린다
쿼리문 : select id from prob_cobolt where id='{$_GET[id]}' and pw=md5('{$_GET[pw]}')";
pw 는 해시되기 때문에 풀 수 없다.
id 에 admin 을 넣고 나머지를 주석으로 바꿔주면된다.
인코드 표를 참고하여 '(%27) 와 #(%23) 을 값에 포함했다.
id=admin%27%23 을 넣어주면 id 에 admin 이 넣어지고
뒷 부분은 주석이 되고 문제가 풀린다.