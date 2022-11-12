import monster as m

def locationdict(name, monster, level, num):
    global location
    location = {'name':name, 'monster':monster, 'lvl':level, 'battle':num}

locationdict("시작의평원", m.I급, 1, 3)
시작의평원 = location
locationdict("모험의황야", m.II급, 6, 5)
모험의황야 = location
locationdict("마수의대지", m.III급, 12, 6)
마수의대지 = location
locationdict("지옥산", m.IV급, 18, 8)
지옥산= location
locationlist = [시작의평원, 모험의황야, 마수의대지, 지옥산]