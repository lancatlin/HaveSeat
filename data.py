class persent:
    def __init__(self,name,favorite):
        self.name = name
        self.favorite = favorite
    def set_seat(self):
        pass
    def is_OK(self):
        pass
    def __str__(self):
        return 'name:'+self.name+',favorite:'+','.join(self.favorite)