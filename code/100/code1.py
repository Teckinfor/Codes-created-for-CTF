def checkchar(instruction):

    with open("maze.txt") as maze :
        
        maze_lst = []
        for line in maze :
            maze_lst.append(line[0:-1])


    count = 0
    while count < len(maze_lst) :
        if instruction["bloc1"] in maze_lst[count] :
            break
        else : 
            count += 1

    if instruction["bloc1"] in maze_lst[count] :
        i = 0
        while i < len(maze_lst[count]):
            if maze_lst[count][i] == instruction["bloc1"][0]:
                if maze_lst[count][i+1] == instruction["bloc1"][1]:
                    if maze_lst[count][i+2] == instruction["bloc1"][2]:
                        break
            i += 1
            
    print(maze_lst[count + instruction["lineFromTop"]][i + instruction["letter"]], end="")





instruction = {"bloc1":"", "lineFromTop":0, "letter":0, "lineFromBottom":0, "bloc2":""}
line_count = 0
first = True
test = True

with open("map.txt") as map :

    for line in map :

        if line_count == 0:
            if first :
                first = False
            else :
                checkchar(instruction)
        elif line_count == 1 :
            instruction["bloc1"] = line[0:-1]
        elif line_count == 2 :
            instruction["lineFromTop"] = int(line[0:-1])
        elif line_count == 3 :
            instruction["letter"] = int(line[0:-1])
        elif line_count == 4 :
            instruction["lineFromBottom"] = int(line[0:-1])
        elif line_count == 5 :
            instruction["bloc2"] = line[0:-1]
            line_count = 0
            test = False

        if test:
            line_count += 1
        else : 
            test = True
