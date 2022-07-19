def solution(n, k):
    word = ""
    while n:
        word = str(n % k) + word
        n = n // k
    word = word.split("0")

    print(word)
    count = 0
    for w in word:
        sosu = True
        if len(w) == 0:
            continue
        if int(w) < 2:
            continue

        for i in range(2, int(int(w) ** 0.5) + 1):
            if int(w) % i == 0:
                sosu = False
                break

        if sosu:
            count += 1

    return count


print(solution(110011, 10))