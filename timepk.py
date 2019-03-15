class time:
 def __init__(self):
        self.hr=00
        self.min=00
        self.sec=00
 def  get_time(self,hr,min,sec):
        self.hr=hr
        self.min=min
        self.sec=sec
 def show_time(self):
        print(self.hr)
        print(self.min)
        print(self.sec)
t=time()
t.get_time(12, 21, 10)
t.show_time()
