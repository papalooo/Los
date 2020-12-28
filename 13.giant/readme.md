Lord of SQLInjection 
giant 문제 [13단계]

if($result[1234]) solve("giant"); 
쿼리문 : select 1234 fromprob_giant where 1
[$query = "select 1234 from{$_GET[shit]}prob_giant where 1"; ]

shit에 값을 알맞게 넣어 쿼리문이 실행돼 1234의 값이 
result 에 들어가게 되면 문제가 풀린다.

shit 의 위치를 보면 공백을 넣어 쿼리문이 잘 작동되게
해주어야한다.

  if(strlen($_GET[shit])>1) exit("No Hack ~_~"); 
  if(preg_match('/ |\n|\r|\t/i', $_GET[shit])) exit("HeHe"); 

shit의 길이가 1보다 커선 안되고 공백을 표현할 수 있는
식들도 필터링 되었다.

내가 알고있는 공백 필터링 우회 방법들을 써보니
%0a, %09, \r, 주석, +, 등등 모두 필터링 되고
%0b는 필터링에 걸리지 않아 문제를 풀 수 있었다.

shit = %0b