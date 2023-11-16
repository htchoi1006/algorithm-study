from collections import deque


n, m = map(int, input().split())
space = [int(input()) for _ in range(n)]
# space2 = [2, 3, 5]

car = [int(input()) for _ in range(m)]
# car2 = [200, 100, 300, 800]


queue = [False] * n
car_dict = {}
tmp = deque()


for i in range(m*2):
    inout = int(input())
    
    if inout > 0: #차가 들어왔을 때
        for j in range(n):
            if queue[j] == False:  #비어있는 주차공간 찾기
                queue[j] = True
                car_dict[inout-1] = j
#                 print(queue)
#                 print(car_dict)
                break
            elif j == n-1 and queue[j] == True:
                tmp.append(inout-1)
#                 print(queue)
#                 print(car_dict)


    elif inout < 0: #차가 나갈 때
        if len(tmp) == 0: #기다리는 차 없는 경우
            queue[car_dict[-1 * inout-1]] = False 
#             print(queue)
#             print(car_dict)
        else: #기다리는 차 있는 경우
            queue[car_dict[-1 * inout-1]] = False
            queue[car_dict[-1 * inout-1]] = True
            waited_car = tmp.popleft()
            car_dict[waited_car] = car_dict[-1 * inout-1]
#             print(queue)
#             print(car_dict)
            

income = 0

for key, value in car_dict.items():
#     print(key, value)
    income += car[key] * space[value]
    
print(income)

        