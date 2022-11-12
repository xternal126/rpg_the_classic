import random as r
import weaponry as w
import armory as a
import location as l
import accesory as ac
import skill as s
def 습득(item):
    print("{}) {} 습득!".format(character_nickname, item['name']))
    character_inventory.append(item)
def weaponinfo(weapon):
    print("이름:{}\n""종류:{}\n""공격력:{}, 내구도:{}, 공격 속도:{}, 효과:{}".format(weapon['name'], weapon['kind'], weapon['dmg'],
                                                                     weapon['dur'],
                                                                     weapon['spd'], weapon['effect']))
def rounding(n):
    n = int(n * 10)
    if n % 10 >= 5:
        return n // 10 + 1
    else:
        return n // 10
global speed, point, exp, goalexp, level
count = 0
s.skills = []
gold = 0
speed = 0
level = 1
point = 0
exp = 0
goalexp = 20
HPotion = 0
MPotion = 0
dungeonkey = 0
dungeonprice = 30
dungeonlevel = 1
loc = l.시작의평원
encountered = 0
playerweapon = w.공기
playerarmor = a.공기
playeraccesory = ac.공기
character_stat = {'근력': 10, '민첩': 10, '체력': 10, '지능': 10}
stat = ['근력', '민첩', '체력', '지능']
character_gear = {'무기:': playerweapon, '방어구:': playerarmor, "장신구:": playeraccesory}
character_inventory = []
print("RPG 더 클래식에 오신 것을 환영합니다.")
character_nickname = input("텍스트 RPG를 시작하기 위해 닉네임을 입력해 주십시오.\n:")
print("{}님, RPG의 세계에 잘 오셨습니다.".format(character_nickname))
character_class = input("{}님의 클래스를 입력해 주십시오.\n클래스:전사/마법사/궁수/성기사/암살자\n클래스 입력:".format(character_nickname))
# 직업 가중치
if character_class == '전사':
    character_stat['근력'] += 3
    character_stat['민첩'] += 0
    character_stat['체력'] += 2
    character_stat['지능'] -= 1
if character_class == '마법사':
    character_stat['근력'] -= 2
    character_stat['민첩'] += 2
    character_stat['체력'] += 0
    character_stat['지능'] += 4
if character_class == '궁수':
    character_stat['근력'] += 1
    character_stat['민첩'] += 2
    character_stat['체력'] += 0
    character_stat['지능'] += 1
if character_class == '성기사':
    character_stat['근력'] += 3
    character_stat['민첩'] += 0
    character_stat['체력'] += 1
    character_stat['지능'] += 2
if character_class == '암살자':
    character_stat['근력'] += 2
    character_stat['민첩'] += 4
    character_stat['체력'] -= 2
    character_stat['지능'] += 0
print("{}님, {}가 되신 것을 축하드립니다.".format(character_nickname, character_class))
습득(w.초짜막대기)
습득(w.조잡한활)
print("커맨드\n"
      "몬스터 사냥:h\n"
      "장비 장착:e\n"
      "캐릭터 정보:c\n"
      "필드 이동:f\n"
      "포인트 분배:p\n"
      "상점:s\n"
      "포션:r\n"
      "던전 입장:d")
fields = []
def unlockfield(lvl):
    global fields
    for i in range(len(l.locationlist)):
        if l.locationlist[i]['lvl'] == lvl and l.locationlist[i] not in fields:
            print(f"{l.locationlist[i]['name']} 대륙이 해금되었습니다! ")
            fields.append(l.locationlist[i])
def update():
    global maxmp
    global maxhp
    global hp
    global atk
    maxhp = character_stat['체력'] * 10 + playerarmor['prot'] + playeraccesory['prot']
    hp = maxhp
    speed = character_stat['민첩'] * 10 + playerweapon['spd']
    speed /= 2
    if playerarmor['effect'] == '신속':
        speed += playerarmor['effectrank'] * 4
    if playeraccesory['effect'] == '신속':
        speed += playeraccesory['effectlevel'] * 4
    if playerarmor['effect'] == '둔화':
        speed -= playerarmor['effectrank'] * 4
    if playerweapon['effect'] == '둔화':
        speed -= playerweapon['effectrank'] * 4
    if playerarmor['effect'] == '불굴':
        maxhp += playerarmor['effectrank'] * 4
    if playeraccesory['effect'] == '불굴':
        maxhp += playeraccesory['effectrank'] * 4
    if playerarmor['effect'] == '마나부스트':
        maxmp += playerarmor['effectrank'] * 4
    if playeraccesory['effect'] == '마나부스트':
        maxmp += playeraccesory['effectrank'] * 4
    atk = character_stat['근력'] + playerweapon['dmg']
    atk = rounding(atk)
    if character_class == '궁수' and playerweapon['kind'] == '활' or '석궁' or '장궁' or '단궁':
        atk += level
        atk = rounding(atk)
    if character_class == '암살자':
        atk += character_stat['민첩'] / 10
        atk = rounding(atk)
    global mana
    maxmp = character_stat['지능'] * 10
    mana = maxmp
def turnup():
    global turns
    turns += 1
    for i in range(len(s.skills)):
        if s.skills[i]['cool'] != 0:
            s.skills[i]['cool'] -= 1
    if playerarmor['effect'] == '재생':
        hp += playerarmor['effectrank'] * 3
    if playeraccesory['effect'] == '재생':
        hp += playeraccesory['effectrank'] * 3
    if playerweapon['effect'] == '재생':
        hp += playerweapon['effectrank'] * 3
    if playerweapon['effect'] == '출혈' or '화염' or '독':
        encountered['hp'] -= playerweapon['effectrank'] * 2
def lvup():
    global level, point, goalexp, exp
    update()
    level += 1
    print("레벨 업!")
    print("레벨:{}".format(level))
    s.unlockskill(eval("s." + str(character_class)), level)
    point += 4
    exp -= goalexp
    goalexp += 2
    goalexp *= 1.2
    goalexp = rounding(goalexp)
    unlockfield(level)
def monsterdefeat():
    global gold, encountered, character_inventory, exp
    print("{}을(를) 쓰러트렸다!".format(encountered['name']))
    gold += encountered['reward']
    exp += encountered['exp']
    print("경험치:{}/{}".format(exp, goalexp))
    if r.randint(1, 100) <= encountered['chance']:
        습득(r.choice(encountered['drop']))
    if exp >= goalexp:
        lvup()
    encountered['hp'] = encountered['maxhp']
update()
unlockfield(1)
while True:
    act = input("(도움말:n)>>>:")
    if act == 'h':
        for i in range(loc['battle']):
            print("\n"
                  "\n"
                  "==============================================")
            encountered = r.choice(loc['monster'])
            print("{}은(는) {}을(를) 맞닥뜨렸다!!".format(character_nickname, encountered['name']))
            turns = 0
            while encountered['hp'] >= 0 or hp >= 0:
                if hp <= 0:
                    print("{}은 눈앞이 깜깜해졌다.......".format(character_nickname))
                    hp = maxhp
                    if level != 1:
                        print("레벨이 낮아집니다!")
                        level -= 1
                        if point >= 4:
                            point -= 4
                        else:
                            character_stat['근력'] -= 1
                            character_stat['민첩'] -= 1
                            character_stat['지능'] -= 1
                            character_stat['체력'] -= 1
                        update()
                    encountered[hp] = encountered['maxhp']
                    break
                print("공격:a 회피:d 후퇴:r 스킬:s")
                print("현재 HP:{}".format(hp))
                print("현재 MP:{}".format(mana))
                print("몬스터 HP:{}".format(encountered['hp']))
                fight = input(">>>:")
                # 공격
                if fight == 'a':
                    if speed >= encountered['spd']:
                        print("{}은(는) {}을 공격했다!!".format(character_nickname, encountered['name']))
                        encountered['hp'] -= atk
                        playerweapon['dur'] -= 1
                        if playerweapon['dur'] == 0:
                            print(f"{playerweapon['name']}이 부러졌다!")
                            playerweapon = w.공기
                        if encountered['hp'] <= 0:
                            monsterdefeat()
                            break
                        print("{}은(는) {}을 공격했다!!".format(encountered['name'], character_nickname))
                        hp -= encountered['atk']
                        playerarmor['dur'] -= 1
                        if playerarmor['dur'] == 0:
                            print(f"{playerarmor['name']}이 망가졌다!")
                            playerarmor = a.공기
                        turnup()
                    if speed < encountered['spd']:
                        print("{}은(는) {}을 공격했다!!".format(encountered['name'], character_nickname))
                        hp -= encountered['atk']
                        playerarmor['dur'] -= 1
                        if playerarmor['dur'] == 0:
                            print(f"{playerarmor['name']}이 망가졌다!")
                            playerarmor = a.공기
                        print("{}은(는) {}을 공격했다!!".format(character_nickname, encountered['name']))
                        encountered['hp'] -= atk
                        playerweapon['dur'] -= 1
                        if playerweapon['dur'] == 0:
                            print(f"{playerweapon['name']}이 부러졌다!")
                            playerweapon = w.공기
                        turnup()
                        if encountered['hp'] <= 0:
                            monsterdefeat()
                            break
                # 회피
                if fight == 'd':
                    print("{}은(는) 회피 준비를 하고 있다.....".format(character_nickname))
                    if speed > encountered['spd']:
                        if r.randint(1, 10) <= 7:
                            print("{}은(는) {}의 공격을 피했다!".format(character_nickname, encountered['name']))
                            print("{}은(는) 놀라 자기 자신을 때렸다!".format(encountered['name']))
                            encountered['hp'] -= encountered['atk']
                            turnup()
                            if encountered['hp'] <= 0:
                                monsterdefeat()
                                break
                        else:
                            print("{}은(는) 공격을 회피하지 못했다!".format(character_nickname))
                            hp -= encountered['atk']
                            playerarmor['dur'] -= 1
                            if playerarmor['dur'] == 0:
                                print(f"{playerarmor['name']}이 망가졌다!")
                                playerarmor = a.공기
                            turnup()
                    if speed <= encountered['spd']:
                        if r.randint(1, 10) <= 3:
                            print("{}은(는) {}의 공격을 피했다!".format(character_nickname, encountered['name']))
                            print("{}은(는) 놀라 자기 자신을 때렸다!".format(encountered['name']))
                            encountered['hp'] -= encountered['atk']
                            turnup()
                            if encountered['hp'] <= 0:
                                monsterdefeat()
                                break
                        else:
                            print("{}은(는) 공격을 회피하지 못했다!".format(character_nickname))
                            hp -= encountered['atk']
                            playerarmor['dur'] -= 1
                            if playerarmor['dur'] == 0:
                                print(f"{playerarmor['name']}이 망가졌다!")
                                playerarmor = a.공기
                            turnup()

                # 후퇴
                if fight == 'r':
                    print("후퇴하였다!")
                    break
                # 스킬
                if fight == 's':
                    if len(s.skills) > 0:
                        print("무슨 스킬을 사용하시겠습니까?")
                        spell = s.defineskill()
                        if spell['mana'] <= mana and spell['cool'] == 0:
                            if spell['kind'] == '공격':
                                print("{} 시전!".format(spell['name']))
                                spell['cool'] = spell['maxcool']
                                if speed >= encountered['spd']:
                                    print("{}은(는) {}을 공격했다!!".format(character_nickname, encountered['name']))
                                    encountered['hp'] -= spell['power'] + character_stat['지능'] - 5
                                    if playerweapon['effect'] == '마력증가':
                                        encountered['hp'] -= playerweapon['effectrank'] * 3
                                    encountered['hp'] = rounding(encountered['hp'])
                                    mana -= spell['mana']
                                    if encountered['hp'] <= 0:
                                        monsterdefeat()
                                        break
                                    print("{}은(는) {}을 공격했다!!".format(encountered['name'], character_nickname))
                                    hp -= encountered['atk']
                                    playerarmor['dur'] -= 1
                                    if playerarmor['dur'] == 0:
                                        print(f"{playerarmor['name']}이 망가졌다!")
                                        playerarmor = a.공기
                                    turnup()
                                    spell['cool'] += 1
                                if speed < encountered['spd']:
                                    print("{}은(는) {}을 공격했다!!".format(encountered['name'], character_nickname))
                                    hp -= encountered['atk']
                                    playerarmor['dur'] -= 1
                                    if playerarmor['dur'] == 0:
                                        print(f"{playerarmor['name']}이 망가졌다!")
                                        playerarmor = a.공기
                                    print("{}은(는) {}을 공격했다!!".format(character_nickname, encountered['name']))
                                    encountered['hp'] -= spell['power'] + character_stat['지능'] - 5
                                    if playerweapon['effect'] == '마력증가':
                                        encountered['hp'] -= playerweapon['effectrank'] * 3
                                    encountered['hp'] = rounding(encountered['hp'])
                                    mana -= spell['mana']
                                    turnup()
                                    spell['cool'] += 1
                                    if encountered['hp'] <= 0:
                                        monsterdefeat()
                                        break
                            elif spell['kind'] == '치유':
                                print("{} 시전!".format(spell['name']))
                                spell['cool'] = spell['maxcool']
                                print("{}은(는) 자신을 치유했다!".format(character_nickname))
                                hp += spell['power'] + character_stat['지능'] - 5
                                if playerweapon['effect'] == '마력증가':
                                    hp += playerweapon['effectrank'] * 3
                                rounding(hp)
                                mana -= spell['mana']
                                turnup()
                                spell['cool'] += 1
                                if r.randint(1, 10) >= 5:
                                    print("{}은(는) {}을 공격했다!!".format(encountered['name'], character_nickname))
                                    hp -= encountered['atk']
                                    playerarmor['dur'] -= 1
                                    if playerarmor['dur'] == 0:
                                        print(f"{playerarmor['name']}이 망가졌다!")
                                        playerarmor = a.공기
                        else:
                            print("스킬의 쿨타임이 남았거나 해당 스킬에 필요한 마나가 없습니다!")
                    else:
                        print("습득한 스킬이 없습니다.")

        if hp < maxhp:
            print("체력이 소량 회복됩니다.")
            hp += character_stat['체력']
    if act == 'e':
        print(
            f"무기: 이름:{playerweapon['name']}, 종류:{playerweapon['kind']}, 내구도:{playerweapon['dur']}/{playerweapon['maxdur']}, "
            f"공격력:{playerweapon['dmg']}, 공격 속도(기본 100):{playerweapon['spd']}, 이펙트:{playerweapon['effect']}.lv.{playerweapon['effectrank']}")
        print(
            f"방어구: 이름:{playerarmor['name']}, 종류:{playerarmor['kind']}, 내구도:{playerarmor['dur']}/{playerarmor['maxdur']}, "
            f"방어력:{playerarmor['prot']}, 이펙트:{playerarmor['effect']}.lv.{playerarmor['effectrank']}")
        print(f"엑세서리: 이름:{playeraccesory['name']}, 종류:{playeraccesory['kind']}, 방어력:{playeraccesory['prot']},"
              f" 이펙트:{playeraccesory['effect']}.lv.{playeraccesory['effectrank']}")
        print("인벤토리:")
        invenstring = ""
        count = 0
        for i in range(len(character_inventory)):
            invenstring = invenstring + character_inventory[i]['name'] + ", "
            count += 1
            if count == 3:
                invenstring = invenstring + "\n"
                count = 0
        print(invenstring)
        equip = input("무슨 아이템을 착용하시겠습니까?")
        if equip in w.strweapon:
            equiped = eval(f"w.{equip}")
            if playerweapon != w.공기:
                character_inventory.append(playerweapon)
            playerweapon = equiped
            print(
                f"무기: 이름:{playerweapon['name']}, 종류:{playerweapon['kind']}, 내구도:{playerweapon['dur']}/{playerweapon['maxdur']}, "
                f"공격력:{playerweapon['dmg']}, 공격 속도(기본 100):{playerweapon['spd']}, 이펙트:{playerweapon['effect']}.lv.{playerweapon['effectrank']}")
            atk = character_stat['근력'] + playerweapon['dmg']
            atk = rounding(atk)
            if character_class == '궁수' and playerweapon['kind'] == '활' or '석궁' or '장궁' or '단궁':
                atk += level
                atk = rounding(atk)
            if character_class == '암살자':
                atk += character_stat['민첩'] / 10
                atk = rounding(atk)
            if playerweapon['effect'] == '둔화':
                speed -= playerweapon['effectrank'] * 4
            print(f"{equiped['name']}를(을) 장비합니다.")
            character_inventory.remove(playerweapon)
        elif equip in a.strarmor:
            equiped = eval(f"a.{equip}")
            if playerarmor != a.공기:
                character_inventory.append(playerarmor)
            playerarmor = equiped
            print(
                f"방어구: 이름:{playerarmor['name']}, 종류:{playerarmor['kind']}, 내구도:{playerarmor['dur']}/{playerarmor['maxdur']}, "
                f"방어력:{playerarmor['prot']}, 이펙트:{playerarmor['effect']}.lv.{playerarmor['effectrank']}")
            maxhp = character_stat['체력'] * 10 + playerarmor['prot'] + playeraccesory['prot']
            if playerarmor['effect'] == '신속':
                speed += playerarmor['effectrank'] * 4
            if playerarmor['effect'] == '둔화':
                speed -= playerarmor['effectrank'] * 4
            if playerarmor['effect'] == '불굴':
                maxhp += playerarmor['effectrank'] * 4
            if playerarmor['effect'] == '마나부스트':
                maxmp += playerarmor['effectrank'] * 4
                print(f"{equiped['name']}를(을) 장비합니다.")
                character_inventory.remove(playerarmor)
        elif equip in ac.straccesory:
            equiped = eval(f"ac.{equip}")
            if playeraccesory != ac.공기:
                character_inventory.append(playeraccesory)
            playeraccesory = equiped
            print(f"엑세서리: 이름:{playeraccesory['name']}, 종류:{playeraccesory['kind']}, 방어력:{playeraccesory['prot']},"
                  f" 이펙트:{playeraccesory['effect']}.lv.{playeraccesory['effectrank']}")
            maxhp = character_stat['체력'] * 10 + playerarmor['prot'] + playeraccesory['prot']
            if playeraccesory['effect'] == '신속':
                speed += playeraccesory['effectlevel'] * 4
            if playeraccesory['effect'] == '불굴':
                maxhp += playeraccesory['effectrank'] * 4
            if playeraccesory['effect'] == '마나부스트':
                maxmp += playeraccesory['effectrank'] * 4
            print(f"{equiped['name']}를(을) 장비합니다.")
            character_inventory.remove(playeraccesory)
        else:
            print("해당 아이템을 가지고 있지 않거나 장비가 아닌 아이템입니다.")
    if act == 'p':
        print(
            f"스탯: 근력:{character_stat['근력']}, 민첩:{character_stat['민첩']}, 체력:{character_stat['체력']}, 지능:{character_stat['지능']}")
        print(f"분배 가능 포인트:{point}")
        statchoice = input("무슨 스탯에 분배하시겠습니까?:")
        if statchoice not in stat:
            print("해당 스탯은 없는 스탯입니다.")
        elif statchoice in stat:
            pointuse = int(input("얼마만큼 분배하시겠습니까?:"))
            if pointuse > point:
                print("포인트가 부족합니다.")
            elif pointuse <= point:
                point -= pointuse
                character_stat[statchoice] += pointuse
                print(f"{statchoice}에 {pointuse}만큼 분배하였습니다.[{statchoice}:{character_stat[statchoice]}]")
                maxhp = character_stat['체력'] * 10 + playerarmor['prot'] + playeraccesory['prot']
                speed = character_stat['민첩'] * 10 + playerweapon['spd']
                atk = character_stat['근력'] + playerweapon['dmg']
                maxmp = character_stat['지능'] * 10
    if act == 'f':
        for i in range(len(fields)):
            print(fields[i]['name'])
        move = input("어느 대륙으로 이동하시겠습니까?:")
        if eval("l." + move) in fields:
            print(f"{move}로 이동합니다.")
            loc = eval("l." + move)
        else:
            print("해당 대륙이 없거나 아직 해금하지 못했습니다.")
    if act == 's':
        print(f"현재 가지신 금액:{gold}gp")
        print("구매:\n"
              "\n"
              "(1)힐링 포션(50hp를 회복합니다.):25gp\n"
              "(2)마나 포션(50mp를 회복합니다.):25gp\n"
              f"(3)던전의 열쇠(던전에 입장할 수 있는 열쇠입니다.):{dungeonprice}gp")
        buy = input("무엇을 구매하시겠습니까?(상품 번호를 입력하세요):")
        if buy == "1":
            if gold >= 25:
                num = int(input("몇 개를 구매하시겠습니까?:"))
                if 25 * num <= gold:
                    print(f"힐링 포션을 {num}개 구매하셨습니다.")
                    print("r 커맨드로 마실 수 있습니다.")
                    HPotion += num
                    gold -= 25 * num
                else:
                    print("골드가 부족합니다.")
            else:
                print("골드가 부족합니다.")
        if buy == "2":
            if gold >= 25:
                num = int(input("몇 개를 구매하시겠습니까?:"))
                if 25 * num <= gold:
                    print(f"마나 포션을 {num}개 구매하셨습니다.")
                    print("r 커맨드로 마실 수 있습니다.")
                    MPotion += num
                    gold -= 25 * num
                else:
                    print("골드가 부족합니다.")
            else:
                print("골드가 부족합니다.")
        if buy == "3":
            if dungeonkey == 0:
                if gold >= dungeonprice:
                    dungeonkey = True
                    print("던전 열쇠를 구매하셨습니다.\n"
                          "d 커맨드를 사용해 입장할 수 있습니다.")
                    gold -= dungeonprice
                else:
                    print("골드가 필요합니다.")
            else:
                print("이미 열쇠를 가지고 있습니다.")
    if act == 'r':
        print("무슨 포션을 마시겠습니까?")
        print(f"힐링 포션:{HPotion}개(h)\n"
              f"마나 포션:{MPotion}개(m)")
        drink = input(":")
        if drink == 'h':
            if HPotion > 0:
                print("힐링 포션을 마셨습니다.")
                HPotion -= 1
                hp += 50
                if hp > maxhp:
                    hp = maxhp
            else:
                print("해당 포션이 없습니다.")
        if drink == 'm':
            if MPotion > 0:
                print("마나 포션을 마셨습니다.")
                MPotion -= 1
                mana += 50
                if mana > maxmp:
                    mana = maxmp
            else:
                print("해당 포션이 없습니다.")
        if drink != 'h' and drink != 'm':
            print("존재하지 않는 포션입니다.")
    if act == 'c':
        print(f"[이름:{character_nickname}]\n"
              f"[레벨:{level}]\n"
              f"[직업:{character_class}]\n"
              f"[HP:{hp}/{maxhp}]\n"
              f"[MP:{mana}/{maxmp}]\n"
              f"\n"
              f"스탯:\n"
              f"근력:{character_stat['근력']} 민첩:{character_stat['민첩']} 체력:{character_stat['체력']} 지능:{character_stat['지능']}\n"
              f"장비:\n"
              f"무기: 이름:{playerweapon['name']}, 종류:{playerweapon['kind']}, 내구도:{playerweapon['dur']}/{playerweapon['maxdur']}, "
              f"공격력:{playerweapon['dmg']}, 공격 속도(기본 100):{playerweapon['spd']}, 이펙트:{playerweapon['effect']}.lv.{playerweapon['effectrank']}\n"
              f"방어구: 이름:{playerarmor['name']}, 종류:{playerarmor['kind']}, 내구도:{playerarmor['dur']}/{playerarmor['maxdur']}, "
              f"방어력:{playerarmor['prot']}, 이펙트:{playerarmor['effect']}.lv.{playerarmor['effectrank']}\n"
              f"엑세서리: 이름:{playeraccesory['name']}, 종류:{playeraccesory['kind']}, 방어력:{playeraccesory['prot']},"
              f" 이펙트:{playeraccesory['effect']}.lv.{playeraccesory['effectrank']}")
    if act == 'n':
        print("커맨드\n"
              "몬스터 사냥:h\n"
              "장비 장착:e\n"
              "캐릭터 정보:c\n"
              "필드 이동:f\n"
              "포인트 분배:p\n"
              "상점:s\n"
              "포션:r\n"
              "던전 입장:d")
    if act == 'd':
        if dungeonkey:
            chance = 3
            print(f"던전에 입장하시겠습니까?\n"
                  f"던전에 입장하시면 던전 레벨만큼 강한 몬스터를 만나게 되며,\n"
                  f"경험치와 골드를 얻을 수도 있으나-\n"
                  f"던전 레벨이 늘어날수록 강해지는 몬스터에게 당할 수도 있습니다.\n"
                  f"던전은 미지의 아공간으로 안에선 포션 사용이 불가해지고 무기/방어구 내구도와 스킬 쿨타임이 적용되지 않습니다.\n"
                  f"던전 레벨:lv.{dungeonlevel}\n"
                  f"도전하시겠습니까?(y/n):")
            go = input(":")
            if go == 'y':
                print("던전에 입장합니다!")
                for i in range(5):
                    if chance == 0:
                        break
                        dungeonkey = False
                    if r.randint(1, 2) == 1:
                        print("던전 파수꾼이 몰려나온다!")
                        for i in range(r.randint(dungeonlevel, dungeonlevel+3)):
                            if chance == 0:
                                break
                            던전파수꾼 = {"name": "던전의 파수꾼", "dmg": 15 * dungeonlevel + r.randint(1, 10),
                                     'spd': 15 * dungeonlevel + r.randint(1, 10),
                                     'hp': 50 * dungeonlevel, 'exp': 5 * dungeonlevel}
                            while 던전파수꾼['hp'] >= 0 or hp >= 0:
                                print("\n"
                                      "\n"
                                      "==============================================")
                                if hp <= 0:
                                    print("쓰러졌다...")
                                    if chance >= 1:
                                        chance -= 1
                                        print(f"기회:{chance}")
                                        update()
                                    if chance == 0:
                                        print("모든 기회가 소진되었다...")
                                        break
                                print("공격:a 회피:d 스킬:s")
                                print(f"HP:{hp}/{maxhp}")
                                print(f"MP:{mana}/{maxmp}")
                                act = input(">>>:")
                                if act == 'a':
                                    print("공격!")
                                    if 던전파수꾼['spd'] > speed:
                                        print("공격당했다!")
                                        hp -= 던전파수꾼['dmg']
                                        print(f"HP:{hp}/{maxhp}")
                                        print("공격했다!")
                                        던전파수꾼['hp'] -= atk
                                        print(f"몬스터 HP:{던전파수꾼['hp']}")
                                        if 던전파수꾼['hp'] <= 0:
                                            print("쓰러트렸다!")
                                            exp += 던전파수꾼['exp']
                                            던전파수꾼['hp'] = 50 * dungeonlevel
                                            if exp >= goalexp:
                                                update()
                                                level += 1
                                                print("레벨 업!")
                                                print("레벨:{}".format(level))
                                                s.unlockskill(eval("s." + str(character_class)), level)
                                                point += 4
                                                exp -= goalexp
                                                goalexp += 2
                                                goalexp *= 1.2
                                                goalexp = rounding(goalexp)
                                            break
                                    if 던전파수꾼['spd'] <= speed:
                                        print("공격했다!")
                                        던전파수꾼['hp'] -= atk
                                        print(f"몬스터 HP:{던전파수꾼['hp']}")
                                        if 던전파수꾼['hp'] <= 0:
                                            print("쓰러트렸다!")
                                            exp += 던전파수꾼['exp']
                                            던전파수꾼['hp'] = 50 * dungeonlevel
                                            if exp >= goalexp:
                                                update()
                                                level += 1
                                                print("레벨 업!")
                                                print("레벨:{}".format(level))
                                                s.unlockskill(eval("s." + str(character_class)), level)
                                                point += 4
                                                exp -= goalexp
                                                goalexp += 2
                                                goalexp *= 1.2
                                                goalexp = rounding(goalexp)
                                            break
                                        print("공격당했다!")
                                        hp -= 던전파수꾼['dmg']
                                        print(f"HP:{hp}/{maxhp}")
                                if act == 'd':
                                    print("회피!")
                                    if 던전파수꾼['spd'] > speed:
                                        if r.randint(1, 10) < 3:
                                            print("회피 성공!")
                                            print("파수꾼은 자신을 때렸다!")
                                            던전파수꾼['hp'] -= 던전파수꾼['dmg']
                                            print(f"몬스터 HP:{던전파수꾼['hp']}")
                                            if 던전파수꾼['hp'] <= 0:
                                                print("쓰러트렸다!")
                                                exp += 던전파수꾼['exp']
                                                던전파수꾼['hp'] = 50 * dungeonlevel
                                                if exp >= goalexp:
                                                    update()
                                                    level += 1
                                                    print("레벨 업!")
                                                    print("레벨:{}".format(level))
                                                    s.unlockskill(eval("s." + str(character_class)), level)
                                                    point += 4
                                                    exp -= goalexp
                                                    goalexp += 2
                                                    goalexp *= 1.2
                                                    goalexp = rounding(goalexp)
                                                break
                                        else:
                                            print("회피 실패!")
                                            print("공격당했다!")
                                            hp -= 던전파수꾼['dmg']
                                            print(f"HP:{hp}/{maxhp}")
                                    if 던전파수꾼['spd'] <= speed:
                                        if r.randint(1, 10) < 7:
                                            print("회피 성공!")
                                            print("파수꾼은 자신을 때렸다!")
                                            던전파수꾼['hp'] -= 던전파수꾼['dmg']
                                            print(f"몬스터 HP:{던전파수꾼['hp']}")
                                            if 던전파수꾼['hp'] <= 0:
                                                print("쓰러트렸다!")
                                                exp += 던전파수꾼['exp']
                                                던전파수꾼['hp'] = 50 * dungeonlevel
                                                if exp >= goalexp:
                                                    update()
                                                    level += 1
                                                    print("레벨 업!")
                                                    print("레벨:{}".format(level))
                                                    s.unlockskill(eval("s." + str(character_class)), level)
                                                    point += 4
                                                    exp -= goalexp
                                                    goalexp += 2
                                                    goalexp *= 1.2
                                                    goalexp = rounding(goalexp)
                                                break
                                        else:
                                            print("회피 실패!")
                                            print("공격당했다!")
                                            hp -= 던전파수꾼['dmg']
                                            print(f"HP:{hp}/{maxhp}")
                                if act == 's':
                                    if len(s.skills) > 0:
                                        print("스킬 선택")
                                        spell = s.defineskill()
                                        if spell['mana'] <= mana and spell['cool'] == 0:
                                            if spell['kind'] == '공격':
                                                print("{} 시전!".format(spell['name']))
                                                mana -= spell['mana']
                                                던전파수꾼['hp'] -= spell['power'] + character_stat['지능'] - 5
                                                print(f"몬스터 HP:{던전파수꾼['hp']}")
                                                print(f"MP:{mana}/{maxmp}")
                                                if 던전파수꾼['spd'] > speed:
                                                    print("공격당했다!")
                                                    hp -= 던전파수꾼['dmg']
                                                    print(f"HP:{hp}/{maxhp}")
                                                    print("공격했다!")
                                                    if 던전파수꾼['hp'] <= 0:
                                                        print("쓰러트렸다!")
                                                        exp += 던전파수꾼['exp']
                                                        던전파수꾼['hp'] = 50 * dungeonlevel
                                                        if exp >= goalexp:
                                                            update()
                                                            level += 1
                                                            print("레벨 업!")
                                                            print("레벨:{}".format(level))
                                                            s.unlockskill(eval("s." + str(character_class)), level)
                                                            point += 4
                                                            exp -= goalexp
                                                            goalexp += 2
                                                            goalexp *= 1.2
                                                            goalexp = rounding(goalexp)
                                                        break

                                                if 던전파수꾼['spd'] <= speed:
                                                    print("공격했다!")
                                                    던전파수꾼['hp'] -= spell['power'] + character_stat['지능'] - 5
                                                    print(f"몬스터 HP:{던전파수꾼['hp']}")
                                                    print(f"MP:{mana}/{maxmp}")
                                                    if 던전파수꾼['hp'] <= 0:
                                                        print("쓰러트렸다!")
                                                        exp += 던전파수꾼['exp']
                                                        던전파수꾼['hp'] = 50 * dungeonlevel
                                                        if exp >= goalexp:
                                                            update()
                                                            level += 1
                                                            print("레벨 업!")
                                                            print("레벨:{}".format(level))
                                                            s.unlockskill(eval("s." + str(character_class)), level)
                                                            point += 4
                                                            exp -= goalexp
                                                            goalexp += 2
                                                            goalexp *= 1.2
                                                            goalexp = rounding(goalexp)
                                                        break
                                                    print("공격당했다!")
                                                    hp -= 던전파수꾼['dmg']
                                                    print(f"HP:{hp}/{maxhp}")
                                            if spell['kind'] == '치유':
                                                print("{} 시전!".format(spell['name']))
                                                mana -= spell['mana']
                                                print(f"MP:{mana}/{maxmp}")
                                                print("치유!")
                                                hp += spell['power'] + character_stat['지능'] - 5
                                                if hp > maxhp:
                                                    hp = maxhp
                                                print(f"HP:{hp}/{maxhp}")
                                                if r.randint(1, 10) <= 5:
                                                    print("공격당했다!")
                                                    hp -= 던전파수꾼['dmg']
                                                    print(f"HP:{hp}/{maxhp}")
                    if r.randint(1, 2) == 2:
                        print("!!!")
                        print("골드가 들어있는 상자를 발견했다!")
                        print(f"{r.randint(dungeonlevel*10, dungeonlevel * 30) * dungeonlevel}골드를 얻었다!")
                if chance > 0:
                    print("던전을 무사히 공략했다!")
                    print("던전 레벨이 올라갑니다!")
                    dungeonlevel += 1
                    print(f"던전레벨:{dungeonlevel}")
                    dungeonprice += 30
            if go == 'n':
                print(f"{character_nickname}은 열쇠를 집어넣었다.")
