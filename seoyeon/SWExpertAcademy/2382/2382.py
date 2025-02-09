#SWExpert Academy #2382 미생물 격리

T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    microbes = [list(map(int, input().split())) for _ in range(K)]

    answer = 0

    for time in range(M):
        merge = []
        for microbe in range(len(microbes)):

            if microbes[microbe][3] == 1:
                microbes[microbe][0] -= 1
            elif microbes[microbe][3] == 2:
                microbes[microbe][0] += 1
            elif microbes[microbe][3] == 3:
                microbes[microbe][1] -= 1
            elif microbes[microbe][3] == 4:
                microbes[microbe][1] += 1

            if microbes[microbe][0] == 0 or microbes[microbe][0] == N-1 or microbes[microbe][1] == 0 or microbes[microbe][1] == N-1:
                microbes[microbe][2] = microbes[microbe][2] // 2

                if microbes[microbe][3] == 1:
                    microbes[microbe][3] = 2
                elif microbes[microbe][3] == 2:
                    microbes[microbe][3] = 1
                elif microbes[microbe][3] == 3:
                    microbes[microbe][3] = 4
                elif microbes[microbe][3] == 4:
                    microbes[microbe][3] = 3

            location = [microbes[microbe][0], microbes[microbe][1]] 

            if location not in merge:
                merge.append(location)

        for i in merge:  
            microbes_big = 0  
            microbes_num = 0 
            microbes_sum = 0  
            temp_list = []

            for j in range(len(microbes)-1, -1, -1): 

                if [microbes[j][0], microbes[j][1]] == i:  
                    if microbes[j][2] > microbes_big: 
                        microbes_big = microbes[j][2] 
                        microbes_num = j
                    temp_list.append(j)

            dir = microbes[microbes_num][3]

            for k in temp_list:
                pop_micro = microbes.pop(k)
                microbes_sum += pop_micro[2]

            microbes.append([i[0], i[1], microbes_sum, dir])

    for microbe in microbes:
        answer += microbe[2]

    print(f'#{test_case} {answer}')