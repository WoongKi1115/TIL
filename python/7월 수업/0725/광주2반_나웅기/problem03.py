#get_user_id 함수에 딕셔너리 형태로 신규 생성을 목표하는 정보가 전달인자로 주어짐.
#딕셔너리에서 문자열로.


def get_user_id(user_data):   #user_data로 신규 생성된 정보들이 들어옴.(dictionary형태.)
    return str(user_data['id'])  #정보들 중에서 id 값만 문자열로 출력.


