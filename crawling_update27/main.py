import json
import crawlKoreaData_All as crawl1
import crawlKoreaData_Gyeonggi as crawl2
import crawlKoreaData_Seoul as crawl3
import LED_Display as LMD
import threading
from datetime import date, timedelta
from matrix import *

today = date.today()
a = str(today)



def LED_init():
    thread=threading.Thread(target=LMD.main, args=())
    thread.setDaemon(True)
    thread.start()
    return

crawl1.run()
crawl2.run()
crawl3.run()

def draw_matrix(array):
    for x in range(16):
        for y in range(32):
            if array[x][y] == 1:
                LMD.set_pixel(x,y,4)
            elif array[x][y] == 0:
                LMD.set_pixel(x,y,0)
            else:
                continue
        print()

array_screen = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

number_array = [
    [[0,1,1,1,0],
     [1,0,0,0,1],
     [1,0,0,0,1],
     [1,0,0,0,1],
     [0,1,1,1,0]], #0
    [[0,0,1,0,0],
     [0,0,1,0,0],
     [0,0,1,0,0],
     [0,0,1,0,0],
     [0,0,1,0,0]], #1
    [[1,1,1,1,1],
     [0,0,0,0,1],
     [1,1,1,1,1],
     [1,0,0,0,0],
     [1,1,1,1,1]], #2
    [[1,1,1,1,1],
     [0,0,0,0,1],
     [1,1,1,1,1],
     [0,0,0,0,1],
     [1,1,1,1,1]], #3
    [[1,0,0,1,0],
     [1,0,0,1,0],
     [1,1,1,1,1],
     [0,0,0,1,0],
     [0,0,0,1,0]], #4
    [[1,1,1,1,1],
     [1,0,0,0,0],
     [1,1,1,1,1],
     [0,0,0,0,1],
     [1,1,1,1,1]], #5
    [[1,1,1,1,1],
     [1,0,0,0,0],
     [1,1,1,1,1],
     [1,0,0,0,1],
     [1,1,1,1,1]], #6
    [[1,1,1,1,1],
     [0,0,0,0,1],
     [0,0,0,1,0],
     [0,0,1,0,0],
     [0,0,1,0,0]], #7
    [[1,1,1,1,1],
     [1,0,0,0,1],
     [1,1,1,1,1],
     [1,0,0,0,1],
     [1,1,1,1,1]], #8
    [[1,1,1,1,1],
     [1,0,0,0,1],
     [1,1,1,1,1],
     [0,0,0,0,1],
     [0,0,0,0,1]], #9
]

covid_array = [
    [[0, 1, 1, 1, 1],
     [1, 0, 0, 0, 0],
     [1, 0, 0, 0, 0],
     [1, 0, 0, 0, 0],
     [0, 1, 1, 1, 1]], # C
    [[0, 1, 1, 1, 0],
     [1, 0, 0, 0, 1],
     [1, 0, 0, 0, 1],
     [1, 0, 0, 0, 1],
     [0, 1, 1, 1, 0]], # O
    [[1, 0, 0, 0, 1],
     [1, 0, 0, 0, 1],
     [0, 1, 0, 1, 0],
     [0, 0, 1, 0, 0],
     [0, 0, 1, 0, 0]], # V
    [[0, 1, 1, 1, 0],
     [0, 0, 1, 0, 0],
     [0, 0, 1, 0, 0],
     [0, 0, 1, 0, 0],
     [0, 1, 1, 1, 0]], # I
    [[1, 1, 1, 0, 0],
     [1, 0, 0, 1, 0],
     [1, 0, 0, 1, 0],
     [1, 0, 0, 1, 0],
     [1, 1, 1, 0, 0]] # D
]

LED_init()
draw_matrix(array_screen); print()

# 지역별 확진자 수 검색 함수 (LED구현)
def search_count(js_file,search_region,array):
    with open (js_file,"r",encoding="utf-8") as f:
        json_data = json.load(f)
        for i in range(0,len(json_data)-1):
            if (json_data[i]['지역이름']) == search_region:
                print(json_data[i]['확진자수'])
                list =[int(i) for i in str(json_data[i]['확진자수'])]
                for j in range(0,len(list)):
                    for x in range(5):
                        for y in range(0+5*j,5+5*j):
                            array[x][y] = number_array[list[j]][x][y-5*j]

def main_UI(array):
    for j in range(0,5):
        for x in range(2,7):
            for y in range(1+5*j,6+5*j):
                array[x][y] = covid_array[j][x-2][y-5*j-1]

def all_count(js_file,array):
    with open (js_file,"r",encoding="utf-8") as f:
        json_data = json.load(f)
        list = [int(i) for i in str(json_data[0]['확진자수'])]
        for j in range(0,len(list)):
            for x in range(10,15):
                for y in range(1+5*j,6+5*j):
                    array[x][y] = number_array[list[j]][x-10][y-5*j-1]

# 지역별 전날대비 확진자 수 증감 검색 함수
def count_change(js_file,search_region):
    with open (js_file,"r",encoding="utf-8") as f:
        json_data = json.load(f)
        for i in range(0,len(json_data)-1):
            if (json_data[i]['지역이름']) == search_region:
                return json_data[i]['전날비교']

menu = 1
while(menu):
    print("*****Menu*****")
    print("1.All")
    print("2.Seoul")
    print("3.Gyeonggi")
    print("4.Exit")
    print("**************")
    main_menu = 0
    if main_menu == 0:
        main_UI(array_screen)
        file = 'koreaData_All' + '_' + a + '.js'
        all_count(file, array_screen)
        draw_matrix(array_screen);print()

    menu_choice = int(input("Select menu: "))

    # while > 뒤로가기 입력전까지 menu 반복시행
    while menu_choice == 1:  # 전국 확진자 수 검색
        js_file = 'koreaData_All'+ '_'+ a +'.js'
        search_region = input("지역을 입력하세요 (ex:서울): ")
        for x in range(16):
            for y in range(32):
                array_screen[x][y] = 0
        draw_matrix(array_screen);print()
        search_count(js_file,search_region,array_screen)
        draw_matrix(array_screen);print()
        if search_region == '0': # 0을 입력하면 메뉴로 복귀
            main_menu = 0
            break


    while menu_choice == 2: # 서울 세부지역 확진자 수 검색
        js_file = 'koreaData_Seoul_' + a + '.js'
        search_region = input("지역을 입력하세요 (ex:종로구): ")
        for x in range(16):
            for y in range(32):
                array_screen[x][y] = 0
        draw_matrix(array_screen);print()
        search_count(js_file,search_region,array_screen)
        draw_matrix(array_screen);print()
        if search_region == '0': # 0을 입력하면 메뉴로 복귀
            break

    while menu_choice == 3: # 경기 세부지역 확진자 수 검색
        js_file = 'koreaData_Gyeonggi'+ a + '.js'
        search_region = input("지역을 입력하세요 (ex:수원): ")
        for x in range(16):
            for y in range(32):
                array_screen[x][y] = 0
        draw_matrix(array_screen);print()
        search_count(js_file,search_region,array_screen)
        draw_matrix(array_screen);print()
        #print(str(count_change(js_file,search_region)),"명 증가")
        if search_region == '0': # 0을 입력하면 메뉴로 복귀
            break

    if menu_choice == 4: # 메뉴 종료
        menu = 0


