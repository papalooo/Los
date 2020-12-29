Lord of SQLInjection 
giant 문제 [14단계]

if($result['id'] == 'admin') solve("assassin"); 
result 에 id 가 admin 인 값이 들어가면 된다.

우선 자동화 코드를 통해 pw 에 무차별 대입을 한 결과 
guest 의 pw 에 0,1,2,9,d,e,f 가 포함돼있는 걸 
알 수 있었다.

admin 에도 동일한 문자가 들어가 있을거라 생각하고 
앞에서 부터 한자리씩 키워드들을 대입하는 자동화 코드를 작성하여 실행하면 
admin 의 pw 가 __2E_D__ 의 형태로 이루어져 있다는 것을
알 수 있다. 이를 pw 의 값으로 넣어주면 문제를 풀 수 있다.  