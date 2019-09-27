class callDetail:
    def __init__(self,phnofrom,phnoto,time,typecall):
        self.phnofrom=phnofrom
        self.phnoto=phnoto
        self.time=time
        self.typecall=typecall
class Util:
    def __init__(self):
        self.temp=None
    def parse_cust(self,temp):
        self.temp=[]
        for i in temp:
            f,t,d,ty=map(str,i.split(","))
            self.temp.append(callDetail(f,t,d,ty))
call='1234,3456,23,STD'
call1='6423,8532,34,Local'
call2='43351,825245,60,ISD'
list_of_call=[call,call1,call2]
ob=Util()
ob.parse_cust(list_of_call)
