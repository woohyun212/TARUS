# TARUS
Todoist_Auto_Reflect_University_Schedules

The official Todoist Python API library 가 있지만 그건 Sync API 다 
내가 만드는건 REST API를 이용한 것이다.
왜 굳이 REST API를 사용하냐고 묻는다면
Sync API를 읽다가 느낀건데, Sync API는 project의 id 값을 불러올 방법이 없다..!
project id를 알기위해 project id를 알아야 한다.(?)

분명 어딘가엔 있겠지만, 내 영어실력을 탓해야하기에 
내가 직접 
https://developer.todoist.com/rest/v1/#overview
에 있는 모든 기능을 메소드화 하리라 다짐했다.

사실 원래 목표는 대학교 e-캠퍼스에서 강의 일정을 파싱해와서
todoist에 추가하는 것이였는데 일이 좀 커졌다.
그래서 목표를 확고히 잡아가려고한다.

목표
1. todoist REST API 에서 당장 필요한 메소드 구현
 1.1 Task 추가
2. 로그인을 통해 파싱해오기
3. 파싱한 데이터 정리해서 todoist에 추가하기 
