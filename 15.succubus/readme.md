Lord of SQLInjection 
succubus 문제 [15단계]

if($result['id']) solve("succubus");
id에 값이 들어가면 문제가 풀린다.

"select id from prob_succubus 
where id = '' and pw = ''"

id 에 \를 넣어서 싱글쿼터를 무력화 해주고 
pw 에 기본적인 우회 방법인 or 1#(%23)을 넣어 
문제를 풀 수 있다.

id = \ pw = or 1%23