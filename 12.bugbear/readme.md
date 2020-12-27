Lord of SQLInjection 
bugbear 문제 [12단계]

  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("bugbear"); 

11번 문제와 유사하지만 필터링 되는 것이 많아졌다.

  if(preg_match('/prob|_|\.|\(\)/i', $_GET[no])) exit("No Hack ~_~"); 
  if(preg_match('/\'/i', $_GET[pw])) exit("HeHe"); 
  if(preg_match('/\'|substr|ascii|=|or|and| |like|0x/i', $_GET[no])) exit("HeHe"); 

substr은 mid로 대체한다
ascii는 hex로 대체한다(ord 또한 or 때문에 필터링)
=은 in으로 대체한다(like 필터링)
or,and 는 ||,&&로 대체한다
공백은 %09(tab)으로 대체한다

0x가 필터링 되면 헥사값이 필터링에 걸리기 때문에 헥사값을 구해서 쿼리문에 넣지않고
쿼리문에서 헥사값을 연산하도록 작성했다.

코드를 실행해서 알아낸 pw 를 쿼리에 넣어준다.

pw = 52dc3991