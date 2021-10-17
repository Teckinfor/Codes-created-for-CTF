input = {8:0, 7:0, 6:0, 5:0, 4:0, 3:0, 2:0, 1:0, 0:0}
out = {8:0, 7:0, 6:0, 5:0, 4:0, 3:0, 2:0, 1:0, 0:0}
string = 'a_cdefaijkltmnopwzstueabez01200067890ABCDEFGHIJKnooodtdvw000eta?T!VW00Y!ETA?*-+/{}[]=&%£"!()abcdefghijklmnopqrsABCDEFGHIJKLNMuuuvwxipsilonnnnnnz%%/9876543210|!"£$ohdear!%&/(((()*;:_AAAABSIDEOWabcdefghijklmnopqrstuvwxyz012345678?8?8?8?9!!!!!EGIN.CERTIFICATEa_cdefaijkltmnopwzstueabez01200067890ABCDEFGHIJKnooodtdvw000eta?T!VW00Y!ETA?*-+/{}[]=&%£"!()abcdefghijklmnopqrsABCDEFGHIJKLNMuuuvwxipsilonnnnnnz%%/9876543210|!"£$ohdear!%&/(((()*;:_AAAABSIDEOWabcdefghijklmnopqrstuvwxyz012345678?8?8?8?9!!!!!EGIN.CERTIFICATE'
j = 0
while j < 10 :

    i = 0
    while i < 9 :
        input[i] = out[i]
        i = i + 1
    
    #module ADD
    test = input[3] + input[4] + input[2]
    if test == 3 :
        A = 1
        C = 1
    elif test == 2 :
        A = 0
        C = 1
    elif test == 1:
        A = 1
        C = 0
    elif test == 0:
        A = 0
        C = 0

    #Out2
    if input[6] == C :
        out[2] = 0
    else :
        out[2] = 1

    #Out0
    if input[8] == out[2] :
        out[0] = 0
    else :
        out[0] = 1

    #Out1

    out[1] = input[5]

    #Out3
    out[3] = A

    #Out4
    if input[0] == 1 or A == 1 or input[5] == 0 :
        out[4] = 1
    else :
        out[4] = 0

    #Out5
    out[5] = input[0]

    #Out6
    if input[5] == input[0] :
        out[6] = 0
    else :
        out[6] = 1

    #Out7
    if input[7] == 1 and input[1] == 1 :
        out[7] = 1
    else :
        out[7] = 0

    #Out8
    if input[8] == out[6] :
        out[8] = 0
    else :
        out[8] = 1
    

    #Check Char
    addr = ""
    for value in out.values():
        addr = addr + str(value)
    decimal = int(addr, 2)
    #print(addr, ":", decimal, ":", hex(decimal), ":", string[decimal])
    print(string[decimal], end="")
    j = j + 1

#Good flag {FLG:weeGo0dY0u}
