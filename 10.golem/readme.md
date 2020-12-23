Lord of SQLInjection 
golem 문제 [10단계]
 if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("golem"); 
DB에 있는 pw 값을 알아내서 입력하면 문제가 풀린다.
우선 pw의 길이를 알아내기 위해 쿼리문에 or id = "admin" and length(pw) = ? 형태의 구문을 집어넣어 길이를 구하도록 한다. 하지만 등호(=)와 or, and가 필터링 되기 때문에 등호(=)는 like 으로 or, and 는 ||,&& 으로 바꿔서 구문을 입력해준다. 그렇게해서 pw 가 8자리 라는 것을 알아낼 수 있다.
pw=2%27||id%20like%20"admin"%20%26%26%20length(pw)%20like%208%23
