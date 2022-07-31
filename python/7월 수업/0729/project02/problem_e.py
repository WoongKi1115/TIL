import requests
from pprint import pprint


def credits(title):
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
        URL1 = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=250864cefa8edb436b78f5f5b8803df1&language=en-US'
            
        response1 = requests.get(URL1, params=params).json()
        print(response1)
        cast_directing = {}
        a = []
        for j in range(len((response1)['cast'])):
            if response1['cast'][j]['cast_id'] < 10:
                a.append(response1['cast'][j]['name'])
        b = []
        for i in range(len((response1)['cast'])):
            if response1['crew'][i]['known_for_department'] == 'Directing':
                b.append(response1['crew'][i]['name'])
        
        cast_directing['cast'] = a
        cast_directing['crew'] = b
        return cast_directing
    except:
        return None
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
