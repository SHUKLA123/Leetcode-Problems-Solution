# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

# If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

N = 2
trust = [[1,2],[2,3]]
def findJudge(trust, N):
    if N == 1:
        return 1
    count = [0 for i in range(N+1)]
    for i,j in trust:
        count[i] -= 1
        count[j] += 1
    for k in range(len(count)):
        if count[k] == N-1:
            return k
    return -1
print(findJudge(trust,N))