import json


def max_revenue(movies):
    pass 
    # 여기에 코드를 작성합니다.  
    a = []
    revenue = []
    for i in range(len(movies)):
        a.append(movies[i]['id'])
        b = open(f'data/movies/{a[i]}.json', encoding='UTF8')
        b1 = json.load(b)
        revenue.append(b1['revenue'])
    x = sorted(revenue, reverse=True)
    for j in range(len(a)):
        if revenue[j]  == x[0]:
            movie_name = movies_list[j]['title']
            return movie_name

    
        

     
    
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
