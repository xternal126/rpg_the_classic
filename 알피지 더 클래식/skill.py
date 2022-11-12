def skilldict(name, clas, mana, kind, power, lv, maxcool):
    global skil
    skil = {'name': name, 'class': clas, 'mana': mana, 'kind': kind, 'power': power, 'level': lv, 'cool': 0,
            'maxcool': maxcool}


# 종류:공격, 치유
skilldict('강타', '전사', 15, '공격', 40, 3, 1)
강타 = skil
skilldict('파이어볼', '마법사', 25, '공격', 30, 2, 1)
파이어볼 = skil
skilldict('역장베기', '마법사', 50, '공격', 60, 3, 2)
역장베기 = skil
skilldict('기초힐', '성기사', 25, '치유', 25, 2, 2)
기초힐 = skil
skilldict('급소찌르기', '암살자', 35, '공격', 60, 3, 1)
급소찌르기 = skil
skilldict('차지샷', '궁수', 40, '공격', 90, 3, 3)
차지샷 = skil
skilldict('지면타격', '전사', 45, '공격', 75, 6, 3)
지면타격 = skil
skilldict('라이트닝볼트', '마법사', 200, '공격', 200, 9, 7)
라이트닝볼트 = skil
skilldict('라이프스틸', '암살자', 40, '치유', 50, 4, 2)
라이프스틸 = skil
skilldict('성스러운타격', '성기사', 45, '공격', 70, 4, 3)
성스러운타격 = skil
skilldict('회심의일격', '암살자', 70, '공격', 130, 6, 7)
회심의일격 = skil
skilldict('피어셔', '궁수', 60, '공격', 120, 5, 4)
피어셔 = skil
skilldict('마력치유', '마법사', 60, '치유', 50, 8, 4)
마력치유 = skil
skilldict('광폭의돌진', '전사', 90, '공격', 130, 7, 6)
광폭의돌진 = skil
skilldict('상급치유', '성기사', 60, '치유', 75, 7, 4)
상급치유 = skil
skilldict('장전중휴식', '궁수', 40, '치유', 35, 5, 3)
장전중휴식 = skil
skilldict('파멸의울림', '전사', 120, '공격', 170, 9, 7)
파멸의울림 = skil
skilldict('디바인스톰', '성기사', 140, '공격', 190, 9, 7)
디바인스톰 = skil
skilldict('스토밍블레이드', '암살자', 130, '공격', 170, 9, 7)
스토밍블레이드 = skil
skilldict('에로우레인', '궁수', 140, '공격', 170, 9, 7)
에로우레인 = skil
마법사 = [파이어볼, 역장베기, 라이트닝볼트, 마력치유]
전사 = [강타, 지면타격, 광폭의돌진, 파멸의울림]
성기사 = [기초힐, 성스러운타격, 상급치유, 디바인스톰]
암살자 = [급소찌르기, 라이프스틸, 회심의일격, 스토밍블레이드]
궁수 = [차지샷, 피어셔, 장전중휴식, 에로우레인]
global learned
def unlockskill(clas, level):
    global skills
    lis = clas
    for i in range(len(lis)):
        if lis[i]['level'] == level and lis[i] not in skills:
            print("{} 습득!".format(lis[i]['name']))
            skills.append(lis[i])

global cast
cast = {}

global stskills
stskills = []

global skills
def defineskill():
    for i in range(len(skills)):
        print("-{}(쿨타임:{}턴)".format(skills[i]['name'], skills[i]['cool']))
        stskills.append(skills[i]['name'])
    while True:
        cast = input(">>>:")
        if cast in stskills:
            return eval(cast)
        else:
            print("해당 스킬을 습득하지 못하셨거나 존재하지 않는 스킬입니다. 다시 입력해 주십시오.")

