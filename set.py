with open('test_data', 'w') as file:
    string = 'wh=5*6\n'
    for i in range(1,30):
        string += '%s:%s\n' % (str(i), ','.join([str(x) for x in range(i+1,i+5)]))
    print(string)
    file.write(string)
