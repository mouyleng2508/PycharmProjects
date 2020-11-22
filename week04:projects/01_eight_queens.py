from itertools import permutations
def eight_queens(N):
    sol = 0
    cols = range(N)
    for combo in permutations(cols):
        if N == len(set(combo[i]+i for i in cols)) == len(set(combo[i]-i for i in cols)):
            sol += 1
            print('Solution '+str(sol)+': '+str(combo)+'\n')
            print("\n".join(' 0 ' * i + ' 1 ' + ' 0 ' * (N-i-1) for i in combo) + "\n\n")

eight_queens(8)
