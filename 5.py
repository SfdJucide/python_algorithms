"""
https://drive.google.com/file/d/1F75qG34K29tcX7xx0CqapIQP08CDKZV-/view?usp=sharing
"""
start = 32
stop = 41

for i in range(10):
    for j in range(start, stop + 1):
        print(f'{j} - {chr(j):4}', end='  ')
        if j == 127:
            break

    start += 10
    stop += 10
    print()
