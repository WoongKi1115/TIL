import json
from pprint import pprint


def movie_info(movie, genres):
    a = {
        'genre_ids' : movie.get('genre_ids'),
        'id' : movie.get('id'),
        'title' : movie.get('title'),
        'poster_path' : movie.get('poster_path'),
        'vote_average' : movie.get('vote_average'),
        'overview' : movie.get('overview')
        

    }
    a['genre_name'] = a.pop('genre_ids')
   
    new_one = []
    for i in a['genre_name']:
        for j in range(len(genres)):
            if i == genres[j]['id']:
                new_one.append(genres[j]['name'])
    a['genre_name'] = new_one
    return a




    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))