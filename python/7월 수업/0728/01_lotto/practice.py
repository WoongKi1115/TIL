import json


    














file1 = open(f'data/lotto_{1024}.json')
open1 = json.load(file1)


draw_number = 1024



print('============================================================================')
print(f'               제 {draw_number}회 로또')
print('============================================================================')
print('추첨일 :','/'.join((open1.get('drwNoDate')).split('-')),'(토)')
print('============================================================================')



date =tuple((open1.get('drwNoDate')).split('-'))














