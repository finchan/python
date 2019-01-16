try:
    data = open("missing.txt")
    print(data.readline(), end='')
except IOError as err:
    print('File error: ' + str(err))
finally:
    if 'data' in locals():
        data.close()

try:
    with open('its.txt', 'w') as data:
        print("It's...", file=data)
except IOError as err:
    print('File error: ' + str(err))