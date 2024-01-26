"ABCDEFCD"
# Action, State

LENGTH = 8 - 1 # indexing purposes

def rotate(letter):
    if letter == 'F':
        return 'A'
    return chr(ord(letter)+1)

def applyAction(state,index):
    state = list(state)
    if state[index] == 'A':
        if index > 0:
            state[index+1] = rotate(state[index+1])
        if index < LENGTH:
            state[index-1] = rotate(state[index-1])
    elif state[index] == 'B' and 0 < index < LENGTH:
        state[index+1] = state[index-1]
    elif state[index] == 'C':
        state[8-index] = rotate(state[8-index])
    elif state[index] == 'D':
        if index < 4:
            for i in range(index):
                state[i] = rotate(state[i])
        else:
            for i in range(index+1,LENGTH+1):
                state[i] = rotate(state[i])
    elif state[index] == 'E':
        if index <= LENGTH / 2:
            state[0] = rotate(state[0])
            if index != 0:
                state[index * 2] = rotate(state[index * 2])
        else:
            state[LENGTH] = rotate(state[LENGTH])
            state[2 * LENGTH - index] = rotate(state[2 * LENGTH - index])
    elif state[index] == 'F':
        rotate_index = (index + 9) // 2 if index % 2 != 0 else index // 2
        state[rotate_index] = rotate(state[rotate_index])
        
    return ''.join(state)

state = "ABCDEFCD"
index = 5
print(applyAction(state,index))