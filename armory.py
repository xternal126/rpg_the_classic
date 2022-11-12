def armordict(name, kind, Prot, dur, effect, effectrank):
    global armor
    armor = {'name':name, 'kind':kind, 'prot':Prot, 'dur':dur,'effect':effect, 'effectrank':effectrank,'maxdur':dur}
def rankedupweapondict(name, dmg, dur, spd, effect, effect2, kind):
    global weapon
    weapon = {'이름':name, '종류':kind, '피해량':dmg, '내구도':dur, '공격 속도':spd, '효과1':effect, '효과2':effect2}

armordict('없음', '-', 0, 1000000, '-', 0)
공기 = armor
armordict('가죽방어구', '갑옷', 15, 100, '-', 0)
가죽방어구 = armor
armordict('기초로브', '로브', 10, 70, '마나부스트', 1)
기초로브 = armor
armordict('날렵한늑대', '활동복', 14, 80, '신속', 1)
날렵한늑대 = armor
armordict('헐거운체인메일', '갑옷', 16, 70, '-', 0)
헐거운체인메일 = armor


I티어 = [가죽방어구, 기초로브, 날렵한늑대, 헐거운체인메일]

armordict('브론즈아머', '갑옷', 25, 110, '-', 0)
브론즈아머 = armor
armordict('암살자의옷', '활동복', 20, 70, '신속', 2)
암살자의옷 = armor
armordict('마법병로브', '로브', 18, 75, '마력증가', 2)
마법병로브 = armor

II티어 = [브론즈아머, 암살자의옷, 마법병로브]


armordict('기사의갑옷', '갑옷', 40, 130, '둔화', 2)
기사의갑옷 = armor
armordict('그림자늑대', '활동복', 28, 80, '신속', 3)
그림자늑대 = armor
armordict('드래곤갑주', '갑옷', 35, 110, '불굴', 2)
드래곤갑주 = armor
armordict('소울맨서로브', '로브', 23, 85, '마나부스트', 3)
소울맨서로브 = armor

III티어 = [기사의갑옷, 그림자늑대, 드래곤갑주, 소울맨서로브]

armordict('아처스피릿', '활동복', 48, 140, '신속', 4)
아처스피릿 = armor
armordict('불굴의 기사의 갑주', '갑옷', 54, 160, '불굴', 4)
불굴기사갑주 = armor
armordict('마력의 지배자의 로브', '로브', 45, 120, '마나부스트', 5)
마력의지배자의로브 = armor
armordict('성스러운 갑옷', '갑옷', 49, 130, '재생', 4)
성스러운갑옷 = armor

IV티어 = [아처스피릿, 불굴기사갑주, 마력의지배자의로브, 성스러운갑옷]



strarmor = ["가죽방어구", "기초로브", "날렵한늑대", "헐거운체인메일", "브론즈아머", "암살자의옷", "마법병로브", "기사의갑옷", "그림자늑대", "드래곤갑주", "소울맨서로브",
            "아처스피릿", "불굴기사갑주", "마력의지배자의로브", "성스러운갑옷"]



