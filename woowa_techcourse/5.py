def solution(penter, pexit, pescape, data):
    data_len = len(data) // len(penter)
    packet_len = len(penter)

    answer = penter
    for i in range(data_len):
        head = i * packet_len
        tail = head + packet_len

        chunk = data[head:tail]

        if chunk in (penter, pexit, pescape):
            answer += pescape
        answer += chunk

    answer += pexit
    return answer


r = solution("1100", "0010", "1001", "1101100100101111001111000000")
a = "110011011001100110010010111100111001110000000010"
print(r == a)
r = solution("10", "11", "00", "00011011")
a = '100000010010001111'
print(r == a)
