string = list(input())


def delete_string(s):
    moves = 0
    s = list(s)

    while s:
        found = False
       
        for end in range(len(s) - 1, 0, -1):
            if s[0] == s[end]:
               
                del s[0:end+1]
                moves += 1
                found = True
                break
        if not found:
            
            del s[0]
            moves += 1

    return moves

print(delete_string(string))
