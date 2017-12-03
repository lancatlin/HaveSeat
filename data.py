class person:
    def __init__(self,name,favorite,launcher):
        self.name = name
        self.favorite = favorite
        self.master = launcher
        self.seat = None
    def set_seat(self,seat):
        if seat['free'] and self.seat == None:
            self.seat = seat
            seat['free']=False
            seat['person']=self
            return True
        else:
            return False
    def is_OK(self):
        pass
    def f_amount(self):
        result = 0
        for i in self.master.people:
            if i.seat != None and i.name in self.favorite:
                result += 1
        return result
    def satisfy(self):
        result = 0
        for i in self.master.people:
            if i.seat != None and i.name in self.favorite:
                w,h,iw,ih = self.seat['w'],self.seat['h'],i.seat['w'],i.seat['h']
                if abs(w-iw) <=1 and abs(h-ih) <= 1:
                    result += 1
        return result
    def __str__(self):
        return 'name:'+self.name+',favorite:'+','.join(self.favorite)+' ,seat: '+str(self.seat['w'])+','+str(self.seat['h'])