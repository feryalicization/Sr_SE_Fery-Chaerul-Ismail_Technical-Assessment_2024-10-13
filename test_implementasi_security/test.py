def tingkat_kemahiran_maksimal(N, M, A, B):
    lawan = list(zip(A, B))
    
    lawan.sort()

    tingkat_kemahiran_juned = M

    for kemahiran_lawan, kenaikan_kemahiran in lawan:
        if tingkat_kemahiran_juned >= kemahiran_lawan:
            tingkat_kemahiran_juned += kenaikan_kemahiran
        else:
            break

    return tingkat_kemahiran_juned

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(tingkat_kemahiran_maksimal(N, M, A, B))
