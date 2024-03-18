with open('nfa.txt', 'r') as og:
    lines = og.readlines()
    statelist = lines[0].split(',')
    statelist[-1] = statelist[-1].replace('\n', '')
    dic = {}
    jump = {}
    for i in range(len(statelist)):
        jump[statelist[i]] = []
        dic[statelist[i]] = {}
        for k in lines[1].replace('\n', '').split(','):
            dic[statelist[i]][k] = []
    for i in range(4, len(lines)):
        temp = lines[i].split(',')
        temp[-1] = temp[-1].replace('\n', '')
        if temp[1] == '@':
            jump[temp[0]].append(temp[2])
        else:
            dic[temp[0]][temp[1]].append(temp[2])
    start = lines[2].replace('\n', '')
    final = lines[3].split(',')
    final[-1] = final[-1].replace('\n', '')
with open("input.txt", 'r') as input:
    answer = []
    line = input.readlines()
    for i in range(len(line)):
        moving = [start]
        new = []
        if line[i] != '@\n':
            for k in range(len(line[i].replace('\n', ''))):
                extra = 0
                while len(moving) > extra:
                    if jump[moving[extra]] != []:
                        for value in jump[moving[extra]]:
                            if value not in moving:
                                moving.append(value)
                    extra += 1
                for extra in range(len(moving)):
                    if dic[moving[extra]][line[i][k]] != []:
                        if dic[moving[extra]][line[i][k]] not in new:
                            for value in dic[moving[extra]][line[i][k]]:
                                if value not in new:
                                    new.append(value)
                moving = new
                extra = 0
                while len(moving) > extra:
                    if jump[moving[extra]] != []:
                        for value in jump[moving[extra]]:
                            if value not in moving:
                                moving.append(value)
                    extra += 1
                new = []
        correct = False
        for done in range(len(moving)):
            if moving[done] in final:
                correct = True
        if correct == True:
            answer.append('accept\n')
        else:
            answer.append('reject\n')
with open('output.txt', 'w') as output:
    output.writelines(answer)

    


#region
# lol = "testing 123"
# f = open("Rohan.txt", 'w')
# f.write(lol)
# f.close
# OR YOU CAN DO IT WITH OPEN
# endregion
#region
    # dictstatelist = {}
    # for i in range(len(statelist)):
    #     if statelist[i] in final:
    #         dictstatelist[statelist[i]] = 1
    #     else:
    #         dictstatelist[statelist[i]] = 0
    # moving = {}
    # start = lines[2].replace('\n', '')
    # for i in range(4, len(lines)):
    #     temp = lines[i].split(',')
    #     temp[-1] = temp[-1].replace('\n', '')
    #     moving[temp[0]+temp[1]] = temp[2]
    #endregion


