import re
import random
class Burn:
    Ln = [ ]
    La = [ ]
    Lp = [ ]
    Li = [ ]
    def __init__(self, name, age, percent):
        self.name = name
        self.age = age
        self.percent = percent

    def addpatient(self, name, age, percent):
        
        Ln.append(self.name)
        La.append(self.age)
        Lp.append(self.percent)

        print("Num 이름   나이 범위")
        for i in len(Ln):
            if Lp[i] < 20:
                print("{num}   {n} {a}   {p} %%").format(num = i+1, n = Ln[i], a = La[i], p = Lp[i])
            else:
                print("{num}   {n} {a}   {p} %% 중환자").format(num = i+1, n = Ln[i], a = La[i], p = Lp[i])


    def phone(phonenumber):
        PN = phonenumber
        print(re.sub(r'(?P<1>[0-9]+)[-]([0-9]+)[-](?P<2>[0-9]+)','(?P=1)-****-(?P=2)',PN))


    if name.percent >= 20:        
        class Severe(Burn):
            def assign():
                
                x = random.randint(1,100)
                print("{n} 환자에게 {r_n}번 병상을 배정해 주세요.").format(n = Ln[i], r_n = x)
     
