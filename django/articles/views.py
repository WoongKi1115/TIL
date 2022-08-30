from django.shortcuts import render
import random
# Create your views here.
def index(request):
	# request : 사용자의 요청 정보가 담겨있다. 
	# render은 장고 안의 함수. 사용자에게 보여줄 화면 html 파일 이름.
	return render(request, "index.html")

def greeting(request):
	# 화면에 필요한 데이터들
	foods = ["사과", "바나나", "코코넛"]
	info = {"name" : "나웅기"}
	# 각 데이터들을 다시 context라는 콘 딕셔너리로 묶은 다음
	context = {
		"foods" : foods,
		"info" : info
	}
	return render(request, "greeting.html", context)

def dinner(request):
	foods = ['족발', '햄버거', '치킨', '초밥']
	pick = random.choice(foods)
	long_str = 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Fugit delectus mollitia reiciendis perferendis laboriosam, autem praesentium quidem quisquam ipsam voluptas provident nam magni, aspernatur possimus exercitationem nostrum ad eveniet animi, consequuntur quae. Asperiores quod nisi, omnis hic non, magni itaque esse laboriosam veritatis officia ex velit ipsum similique reiciendis delectus!'
	number = 11
	context = {
		'pick' : pick,
		'foods' : foods,
		'long_str' : long_str,
		'number' : number
	}
	return render(request, 'dinner.html', context)

def throw(request):
	return render(request, 'throw.html')

def catch(request):
	print(request)
	print(type(request))
	print(request.GET)
	print(request.GET.get("messsage"))

	message = request.GET.get("message")
	context = {"message":message}
	return render(request, 'catch.html', context)

def hello(request,name):
	context = {
		'name' : name,
	}
	return render(request, 'hello.html', context)