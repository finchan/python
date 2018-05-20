S = 'Spam'
print(len(S));
print(S[0])
print(S[-1])
print(S[len(S)-1])
print(S[1:3])

print(S[1:])
print(S[0:3])
print(S[:3])
print(S[:-1])
print(S[:])

print(S+'xyz')
print(S*8)

S = 'shrubbery'
L = list(S)
print(L)
L[1] = 'c'
print(''.join(L))

B = bytearray(b'spam')
B.extend(b'eggs')
print(B)
bytearray(b'spameggs')
print(B.decode())

S= 'Spam'
print(S.find('pa'));
print(S.replace('pa', 'XYZ'))

line = 'aaa,bbb,cccc,dd'
print(line.split(','))
S='spam'
print(S.upper())
print(S.isalpha())
line = 'aaa,bbb,ccccc,dd\n'
print(line.rstrip())
print(line.rstrip().split(','))