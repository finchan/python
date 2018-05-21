L = [123, 'spam', 1.23]
print(len(L))
print(L[0])
print(L[:-1])
print(L + [4,5,6])
print(L*2)
print(L)

L.append('NI')
print(L)
L.pop(2)
print(L)

M = ['bb', 'aa', 'cc']
M.sort()
print(M)
M.reverse()
print(M)

M = [[1,2,3],
     [4,5,6],
     [7,8,9]]
print(M)
print(M[1])
print(M[1][2])
col2 = [row[1] for row in M]
print(col2)
col3 = [row[1]+1 for row in M]
print(col3)
col4 = [row[1] for row in M if row[1] %2 ==0]
print(col4)
col5 = [row for row in M]
print(col5)
col6 = [M[i][i] for i in [0,1,2]]
print(col6)
doubles = [c*2 for c in 'spam']
print(doubles)

print(list(range(4)))
print(list(range(-6,7,2)))
print([[x**2, x**3] for x in range(4)])

G = (sum(row) for row in M)
print(next(G))
print(next(G))
print(next(G))