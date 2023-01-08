"""
Detected time complexity:
O(N + M)
"""


def solution(s, p, q):
    prefix = []
    dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    factor = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    consist = ['A', 'C', 'G', 'T']
    for char in s:
        dic[char] += 1
        prefix.append([dic['A'], dic['C'], dic['G'], dic['T']])
    ans = []
    for i in range(len(p)):
        pi, qi = p[i], q[i]
        if pi == qi:
            ans.append(factor[s[pi]])
        else:
            if pi == 0:
                pi_prefix = [0, 0, 0, 0]
            else:
                pi_prefix = prefix[pi-1]
            qi_prefix = prefix[qi]
            for j in range(4):
                d = qi_prefix[j] - pi_prefix[j]
                if d > 0:
                    ans.append(factor[consist[j]])
                    break
    return ans
