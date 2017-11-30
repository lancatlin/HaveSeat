from data import persent
class launcher:
    def __init__(self):
        with open('test_data','r') as file:
            self.w_h = (file.readline().split('=')[1].split('*'))
            print(self.w_h)
            self.people = []
            for i in file.readlines():
                n,p = i.split(':')[0],i.split(':')[1].split(',')
                self.people.append(persent(n,p))
        print(self.people)
    def start(self):
        pass