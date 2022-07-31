import json


def dec_movies(movies):
    pass 
    # 여기에 코드를 작성합니다. 
    a=[]
    rd=[]
    answer = []
    for i in range(len(movies)):
        a.append(movies[i]['id'])
        b = open(f'data/movies/{a[i]}.json', encoding='UTF8')
        b1 = json.load(b)
        rd.append(b1['release_date'][5:7])
    
    for j in range(len(rd)):
        if rd[j] == '12':
            answer.append(movies_list[j]['title'])
    return answer
             
    
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))