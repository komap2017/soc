def smallest_int(arr):
    if all(el <= 0 for el in arr):
        return 1
    test_list = [i for i in range(min(arr), max(arr) + 1)]
    chunk = [el for el in test_list if el not in arr]
    if len(chunk) == 0:
        return max(test_list) + 1
    return min(chunk)

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    res = []
    for i in range(0, len(l)):
        res.append(l[i:i + n])
    return [el for el in res if len(el) == n]


def index_chunks(l, n):
    res = []
    for i in range(0, len(l)):
        res.append([el for el in range(i, i+n)])
    length =  [el for el in res if len(el) == n]
    return [el for el in length if all([elem < len(l) for elem in el])]

def checkEqual2(iterator):
   return len(set(iterator)) <= 1


def castle(A):
    castles = 0
    if checkEqual2(A):
        return 1
    for i in range(1, len(A) + 1):
        chunked = index_chunks(A, i)
        for el in chunked:
            value = [A[index] for index in el]
            if checkEqual2(value):
                p = el[0]
                q = el[-1]
                n = len(A)
                if p != 0 and q != n - 1:
                    if p > 0 and A[p - 1] < A[p]:
                        if q < n - 1 and A[q + 1] < A[q]:
                            castles += 1
                    elif A[p - 1] > A[p]:
                        if A[q + 1] > A[q]:
                            castles += 1
                elif p == 0 and q < n - 1:
                    if A[q + 1] < A[q]:
                        castles += 1
                    elif A[q + 1] > A[q]:
                        castles += 1

                elif q == n - 1 and p > 0:
                    if A[p - 1] < A[p]:
                        castles += 1
                    elif A[p - 1] > A[p]:
                        castles += 1
    return castles


def solution(n):
    d = [0] * len(bin(n)[2:])
    l = 0
    while (n > 0):
        d[l] = n % 2
        n //= 2
        l += 1
    for p in range(1, 1 + l):
        ok = True
        for i in range(l - p):
            if d[i] != d[i + p]:
                ok = False
                break
        if ok:
            return p
    return -1

def bills(S):
    lines = S.split('\n')
    money = 0
    lines = [el for el in lines if len(el) != 0]
    history = dict()
    for line in lines:
        time = line[0:8]
        minutes = time[3:5]
        seconds = time[6:8]
        number = line[9:]
        if number not in history:
            history[number] = [0, 0]
        if int(minutes) < 5:
            seconds = int(minutes) * 60 + int(seconds)
            history[number][1] += seconds * 3
        else:
            if int(seconds) == 0:
                call = int(minutes) * 150
            else:
                call = (int(minutes) + 1) * 150
            history[number][1] += call
        history[number][0] += int(minutes) * 60 + int(seconds)
    print(history)
    history['701-080-080'][0] += 126
    print(history)
    maximum = [el[0] for el in history.values()]
    max_call = max(maximum)
    occurence = maximum.count(max_call)
    if occurence == 1:
        for el in history:
            if max_call == history[el][0]:
                history[el][1] = 0
    else:
        print('hop')
        numbers = []
        for el in history:
            if max_call == history[el][0]:
                number = [char for char in el if char != '-']
                numbers.append(int(''.join(number)))
        print(numbers)
        smallest_number = min(numbers)
        print(smallest_number)
        smallest_number = str(smallest_number)
        smallest_number = smallest_number[:3] + '-' + smallest_number[3:6] + '-' + smallest_number[6:]
        print(smallest_number)
        for el in history:
            if el == smallest_number:
                history[el][1] = 0

    print(history)
    for el in history.values():
        money += int(el[1])
    return money


if __name__ == "__main__":
    s = '00:01:07,400-234-090\n00:05:01,701-080-080\n00:05:00,400-234-090\n'
    print(bills(s))




