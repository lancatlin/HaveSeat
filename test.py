from main import launcher
up = 0
up_draw = ''
for i in range(100000):
    main = launcher()
    main.start()
    result = 0
    for i in main.people:
        result += i.satisfy()
    if result > up:
        up = result
        up_draw = main.output()
print(up_draw)
print(up)
