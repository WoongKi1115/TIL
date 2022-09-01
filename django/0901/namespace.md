No reversematch error => url의 태그가 문제. 이 부분만 체크하면 됨.

두번 째 문제. url을 바꾸어도 화면이 바뀌지 않음.
이 문제는 장고의 특성 때문.
app/templates 이후로 찾기 때문에 이름을 바꾸어도 index라는 이름이 articles와 pages 두개가 있기 때문에 그중 setting의 app에서 위에 있는 articles의 index만을 보여줌.
이를 해결하기 위해 index 위에 폴더를 만들어줌
articles의 templates폴더 안에 articles 폴더를 만들어서 그 안에 html파일들을 넣어줌 
pages에도 마찬가지로 진행.

이후 view.py에서 원래의 경로로 실행하게 되면 
장고는 app/templates까지만 보기 때문에 오류가 뜨게 됨.
때문에 view.py에서도 articles/throw.html의 형태로 바꾸어줘야함.

articles/templates/index
articles/templates/articles/index 의 구조로 바뀡어있음

이는 단일 앱으로 이루어진 경우에는 고려할 필요 없음.
하지만 여러개의 앱으로 이루어져 있다면 이름이 겹칠 가능성이 높기 때문에
위의 사항을 생각해야함.