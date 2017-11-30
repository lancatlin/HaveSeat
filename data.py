class person:
    def __init__(self,name,favorite):
        self.name = name
        self.favorite = favorite
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
    def __str__(self):
        return 'name:'+self.name+',favorite:'+','.join(self.favorite)+'seat: '+str(self.seat['w'])+','+str(self.seat['h'])