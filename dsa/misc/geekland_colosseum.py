

def compare(x):
    return (x[0], x[1])

def compare2(x):
    return (x[1], x[0])

def colosseum(N, A): 
    new_A = []
    x = len(A)
    for i in range(len(A)):
        new_A.append([A[i], i+1]) # [strength, roll_no]
    strength_sorted = sorted(new_A, key=compare)
    # if N % 2 == 0:
    half = int(N/2)
    for j in range(half):
        strength_sorted.pop(0)
    for j in range(half):
        strength_sorted.pop(-1)
    
    op = sorted(strength_sorted, key=compare2)
    print(op)
    l = []
    s1=s2=0
    for i in op:
        l.append(i[0])
    for i in range(half):
        s1 = s1+l[i]
    for i in range(half):
        s2 = s2+l[half+i]
    print(l)
    print(s1, s2)
    print(s1-s2)

def solve(N, A):
    x = len(A)
    grp1 = []
    grp2 = []
    half = int(x/2)
    half_n = int(N/2)
    for i in range(half):
        grp1.append(A[i])
        grp2.append(A[half+i])
    print(grp1, grp2)
    grp1.sort()
    grp2.sort(reverse=True)
    grp1 = grp1[half_n:]
    grp2 = grp2[half_n:]
    print(sum(grp1) - sum(grp2))







N = 1
A = [1, 2, 3]
solve(N, A)