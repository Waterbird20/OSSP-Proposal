# 튜터링 수강신청 사이트

###### 웹페이지 기반 오픈소스 프로젝트로, 현재 존재하는 학교 수강신청 방식과 유사하게 작동하는 튜터링 신청 웹사이트이다.
------------
### [Website Screenshot]
![오소실_수강신청사이트](https://user-images.githubusercontent.com/90546366/205305341-5cbdc302-1db5-4ce4-abc0-fd286b7e45ed.png)

------------
### [Youtube Link]
https://www.youtube.com/watch?v=etFQuUTkYFo&t=4s

------------
### [Instruction of Website]
총 4 개의 html 파일, 1개의 css 파일, 그리고 3개의 javascript 파일을 통해 해당 웹사이트를 구현하였다.

#### 각각의 창에 대한 설명은 다음과 같다.
1. index.html (초기 창)
> 초기 창에서는 로그인 기능을 구현하였다. 로그인을 시도하려는 학생의 학번과 비밀번호를 입력 받는다.
> 서버에 등록된 ID, PW와 대조하여 일치하면 'Success', 틀리면 'Wrong ID password', 그리고 입력하지 않았다면 'Please Enter your ID and Password'를 띄운다.
2. application.html (수강신청 창)
> 초기 창에서 로그인을 성공했다면, 수강신청 창으로 넘어가게 된다. 좌측 상단에는 로그인한 사람의 인적사항이 나타난다.
> 그리고 그 아래에는 로그아웃 버튼과 튜터링매뉴얼다운로드 버튼이 존재한다.
> 로그아웃 버튼을 통해서 초기 창인 index.html로 넘어갈 수 있고, 튜터링매뉴얼다운로드 버튼을 통해서 해당 매뉴얼을 다운로드 받을 수 있다.
> 중상단에는 공지사항, 수강신청, 그리고 전공수업조회가 가능한 radio 탭이 존재한다.
>   > 가. 공지사항 탭에서는 튜터링 소개 및 신청 방법 등을 소개한다.  
>   > 나. 수강신청 탭에서는 현재 개설된 멘토링 분반을 나타낸다. 개설된 과목을 select box에서 보여주고, 학수번호와 분반 입력을 통해 과목 검색도 가능하다.
>   > 다. 전공수업조회 탭에서는 해당 전공의 학부 강의 전부가 조회 가능하다. 해당 강의 중 튜터링 분반이 개설된 과목의 경우 '가능'을, 개설되지 않은 과목의 경우 '불가'라고 나타난다.
> 그리고 하단에는 내가 신청한 튜터링 분반을 나열해준다.
> 학수번호-분반, 교과목명, 교강사, 튜터, 수강인원, 그리고 수업시간을 알려준다.
3. modal.html (튜터링 분반 정보 창)
> 수강신청 창에서 수강신청 탭을 보면, 개설된 튜터링 과목 리스트 좌측에 더보기 란이 존재한다.
> 이 더보기 란의 (+) 버튼을 누르게 되면, 모달창 형태로 튜터링 분반의 정보를 표시해준다.
> 멘티들은 이 정보를 직관적으로 볼 수 있고, 이를 통해 해당 분반을 신청할지 말지를 결정할 수 있게된다.
4. tutorLecture.html (튜터링과목등록)
> application.html 창에서 튜터링과목등록 버튼을 누르게 되면 튜터링과목등록을 할 수 있는 창으로 넘어가게 된다.
> 창에서도 확인할 수 있듯, 입력해야하는 정보들은 다음과 같다.
>   > * 취득 성적(A+, A)  
>   > * 신청 과목 정보  
>   > * 튜터링 계획  
>   > * 지원 동기  
>   > * 그룹 지원 여부  
>   > * 가능한 시간
> 
> 모든 내용이 작성 완료된 후, 하단의 과목등록 버튼을 클릭하여 튜터링 분반 개설을 완료한다. 완료된 경우, '등록이 완료되었습니다'를 띄운다.


우수 프로젝트 시상 프로그램에 지원합니다.
