n, m = map(int, input().split())
dna = [list(input()) for _ in range(n)]

# n, m = 5, 8
# dna = [['T', 'A', 'T', 'G', 'A', 'T', 'A', 'C'], ['T', 'A', 'A', 'G', 'C', 'T', 'A', 'C'], ['A', 'A', 'A', 'G', 'A', 'T', 'C', 'C'], ['T', 'G', 'A', 'G', 'A', 'T', 'A', 'C'], ['T', 'A', 'A', 'G', 'A', 'T', 'G', 'T']]

example = ['A', 'C', 'G', 'T']
sample = ''
ans = 0

for i in range(m):
    a_cnt = 0
    c_cnt = 0
    g_cnt = 0
    t_cnt = 0
    
    for j in range(n):
        if dna[j][i] == example[0]:
            a_cnt += 1
        elif dna[j][i] == example[1]:
            c_cnt += 1
        elif dna[j][i] == example[2]:
            g_cnt += 1
        elif dna[j][i] == example[3]:
            t_cnt += 1
            
    cnt_list = [a_cnt, c_cnt, g_cnt, t_cnt]
    idx = cnt_list.index(max(cnt_list))
    sample += example[idx]


    for k in range(n):
        if dna[k][i] != example[idx]:
            ans += 1
            
            
print(sample)
print(ans)
    
        
