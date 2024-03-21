import heapq

def solution(operations):
    heap = []
    
    for i in operations:
        cmd, num = i.split() 

        if cmd == 'I':  #I이면 heap에 push
            heapq.heappush(heap, int(num))
        elif heap and cmd == 'D' and num == '-1':  #heap이 비어있지 않고 "D -1" 이면 최솟값 제거
            heapq.heappop(heap)
        elif heap and cmd == 'D' and num == '1':   #heap이 비어있지 않고 "D 1" 이면 최댓값 제거
            heap.remove(max(heap))
            
            
    if not heap:
        return [0,0]
    else:
        return [max(heap), min(heap)]