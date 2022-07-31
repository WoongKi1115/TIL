import requests
from pprint import pprint


def recommendation(title):
    pass 
    # 여기에 코드를 작성합니다.  
    try:  
        URL = 'https://api.themoviedb.org/3/search/movie?language=en-US&page=1&include_adult=false'
        
        params = {'language' : 'ko',
        'region' : 'KR',
        'api_key' : '250864cefa8edb436b78f5f5b8803df1',
        'query' : title
        }
        response = requests.get(URL, params=params).json()
        movie_id = response['results'][0]['id']
        URL1 = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key=250864cefa8edb436b78f5f5b8803df1&language=en-US&page=1'
        
        response1 = requests.get(URL1, params=params).json()
        a = []
        for i in range(len(response1['results'])):
            a.append(response1['results'][i]['title'])
        return a
    except:
        return None    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
