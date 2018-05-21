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

print('%s, eggs, and %s' % ('spam', 'SPAM!'))
print('{0}, eggs, and {1}'.format('spam','SPAM!'))
print('{}, eggs, and {}'.format('spam', 'SPAM!'))

print('{:,.2f}'.format(296999.2567))
print('%.2f | %+05d' % (3.14159, -42))

print(dir(S))
print(help(S.replace))

msg = """
a
b'''c""d'e
f
"""
print(msg)