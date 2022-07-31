from operator import itemgetter

my_dict_list = [
    {"이름" : "김싸피", "나이" : 26, "정렬대상" : 2},
    {"이름" : "홍길동", "나이" : 30, "정렬대상" : 1},
    {"이름" : "토르", "나이" : 1500, "정렬대상" : 4},
    {"이름" : "울트론", "나이" : 1, "정렬대상" : 3}
]
# sorted( 정렬대상, key = 어떤 값을 기준으로 정렬할지.)

def function1(dict1): #dict1은 딕셔너리다.
    return dict1.get("정렬대상") # 정렬기준으로 삼고싶은 값을 리턴하는 함수를 만들어서

sorted_dict_list = sorted

sorted_dict_list = sorted(my_dict_list, key = function1, reverse=True)
#sorted_dict_list = sorted(my_dict_list, key = lambda dict1: dict1.get("정렬대상"), reverse = True)

