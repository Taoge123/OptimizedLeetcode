import string

def solution(riddle):
    riddle = list(riddle)

    def generate_letter(used):
        for c in string.ascii_letters:
            if c in used:
                continue
            return c

    for i in range(len(riddle)):
        if riddle[i] == '?':
            riddle[i] = generate_letter(set(riddle[i-1:i] + riddle[i+1:i+2]))
    return ''.join(riddle)

print(solution('ab?ac?'))


