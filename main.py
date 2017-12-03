from data import person
import random
class launcher:
    def __init__(self):
        with open('test_data','r') as file:
            self.w,self.h = (file.readline().split('=')[1].split('*'))
            self.w = int(self.w)
            self.h = int(self.h)
            print(self.w,self.h)
            self.people = []
            for i in file.read().split('\n'):
                n,p = i.split(':')[0],i.split(':')[1].split(',')
                self.people.append(person(n,p,self))
        self.people_num = len(self.people)
        self.seat = []
        for i in range(int(self.w)):
            for j in range(int(self.h)):
                self.seat.append({'w':i,'h':j,'free':True,'person':None})
        print(self.seat)
    def start(self):
        while self.people_num > 0:
            p = self.people[random.randint(0,len(self.people)-1)]
            s = self.seat[random.randint(0,len(self.seat)-1)]
            if p.set_seat(s):
                self.people_num -= 1
                print(p)
        self.output()
    def search_seat(self,w,h):
        for i in self.seat:
            if i['w'] == w and i['h'] == h:
                return i
    def output(self):
        result = ''
        for i in range(self.w):
            for j in range(self.h):
                s = self.search_seat(i,j)
                if s['free']:
                    result += '| | '
                else:
                    result+='|'+s['person'].name+'| '
            result+='\n'
        print(result)