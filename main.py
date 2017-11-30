from data import persent
class launcher:
    def __init__(self):
        with open('test_data','r') as file:
            w,h = (file.readline().split('=')[1].split('*'))
            print(w,h)
            self.people = []
            for i in file.readlines():
                n,p = i.split(':')[0],i.split(':')[1].split(',')
                self.people.append(persent(n,p))
                print(self.people[-1])
        self.seat = []
        for i in range(int(w)):
            for j in range(int(h)):
                self.seat.append({'w':i,'h':j,'free':False})
        print(self.seat)
    def start(self):
        pass