import json
from pprint import pprint

def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    movie_list = []
    for i in movies:
        a = {
            'genre_ids' : i.get('genre_ids'),
            'id' : i.get('id'),
            'title' : i.get('title'),
            'poster_path' : i.get('poster_path'),
            'vote_average' : i.get('vote_average'),
            'overview' : i.get('overview')
            

        }
        a['genre_name'] = a.pop('genre_ids')
    
        new_one = []
        for i in a['genre_name']:
            for j in range(len(genres)):
                if i == genres[j]['id']:
                    new_one.append(genres[j]['name'])
        a['genre_name'] = new_one
        movie_list.append(a)
        
    return movie_list

        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))