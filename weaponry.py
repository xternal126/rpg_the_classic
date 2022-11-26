def weapondict(name,  kind, dmg, dur, spd, effect, effectrank):
    global weapon
    weapon = {'name':name, 'kind':kind, 'dmg':dmg, 'dur':dur, 'spd':spd, 'effect':effect, 'effectrank':effectrank, 'maxdur':dur}
def rankedupweapondict(name, dmg, dur, spd, effect, effect2, kind):
    global weapon
    weapon = {'name':name, 'kind:':kind, 'dmg':dmg, 'dur':dur, 'spd':spd, 'effect':effect, 'effect2':effect2}

weapondict('주먹', '-', 2, 100000000, 100, '-', 0)
공기 = weapon
weapondict('초짜막대기', '스태프', 5, 30, 100, '-', 0)
초짜막대기 = weapon
weapondict('초보자의검', '검', 10, 40, 100, '-', 0)
초보자의검 = weapon
weapondict('단단한목검', '검', 12, 80, 70, '-', 0)
단단한목검 = weapon
weapondict('나무꾼도끼', '도끼', 16, 50, 85, '-', 0)
나무꾼도끼 = weapon
weapondict('녹슨구리검', '검', 14, 30, 110, '-', 0)
녹슨구리검 = weapon
weapondict('뾰족한대거', '단검', 8, 35, 130, '-', 0)
뾰족한대거 = weapon
weapondict('나무쌍도끼', '도끼', 11, 40, 115, '-', 0)
나무쌍도끼= weapon
weapondict('기초창', '창', 15, 65, 80, '-', 0)
기초창 = weapon
weapondict('여행자의지팡이', '스태프', 13, 80, 80, '-', 0)
여행자의지팡이 = weapon
weapondict('조잡한활', '활', 5, 30, 100, '-', 0)
조잡한활 = weapon
weapondict('도적단궁', '단궁', 9, 60, 120, '-', 0)
도적단궁 = weapon
weapondict('목제석궁', '석궁', 16, 70, 80, '-', 0)
목제석궁 = weapon

I티어 = [초보자의검, 단단한목검, 나무꾼도끼, 녹슨구리검, 뾰족한대거, 나무쌍도끼, 기초창, 여행자의지팡이, 조잡한활, 도적단궁, 목제석궁]

weapondict('브론즈블레이드', '검', 17, 70, 100, '-', 0)
브론즈블레이드 = weapon
weapondict('흑요석해머', '망치', 23, 75, 65, '-', 0)
흑요석해머 = weapon
weapondict('뼈검', '검', 15, 85, 90, '-', 0)
뼈검 = weapon
weapondict('화속성지팡이', '스태프', 15, 80, 80, '마력증가', 1)
화속성지팡이 = weapon
weapondict('용병의창', '창', 19, 100, 100, '-', 0)
용병의창 = weapon
weapondict('사냥용장궁', '장궁', 16, 100, 110, '-', 0)
사냥용장궁 = weapon
weapondict('단도', '단검', 12, 70, 120, '출혈', 1)
단도 = weapon
weapondict('양날돌도끼', '도끼', 18, 70, 70, '-', 0)
양날돌도끼 = weapon
weapondict('속사용단궁', '단궁', 13, 80, 110, '-', 0)
속사용단궁 = weapon

II티어 = [브론즈블레이드, 흑요석해머, 뼈검, 화속성지팡이, 용병의창, 사냥용장궁, 단도, 양날돌도끼, 속사용단궁]

weapondict('강철검', '검', 22, 110, 100, '-', 0)
강철검 = weapon
weapondict('서번트의 독이빨', '단검', 16, 85, 130, '독', 2)
서번트의독이빨 = weapon
weapondict('용뼈대검', '대검', 29, 100, 60, '둔화', 2)
용뼈대검 = weapon
weapondict('아크스태프', '스태프', 19, 90, 80, '마력증가', 3)
아크스태프 = weapon
weapondict('플레어보우', '장궁', 20, 95, 90, '화염', 2)
플레어보우 = weapon
weapondict('디바인해머', '망치', 26, 100, 110, '치유', 2)
디바인해머 = weapon

III티어 = [강철검, 서번트의독이빨, 용뼈대검, 아크스태프, 플레어보우, 디바인해머]

weapondict('아다만티움검', '검', 41, 160, 100, '-', 0)
아다만티움검 = weapon
weapondict('그림자 용의 어금니', '단검', 34, 135, 150, '독', 3)
그림자용의어금니 = weapon
weapondict('매직마스터 스태프', '스태프', 38, 95, 95, '마력증가', 4)
매직마스터스태프 = weapon
weapondict('태고의활', '장궁', 39, 140, 110, '-', 0)
태고의활 = weapon
weapondict('신이내린망치', '망치', 48, 150, 75, '재생', 4)
신이내린망치 = weapon

IV티어 = [아다만티움검, 그림자용의어금니, 매직마스터스태프, 태고의활, 신이내린망치]

strweapon = ["초짜막대기", "초보자의검", "단단한목검", "나무꾼도끼", "녹슨구리검", "뾰족한대거", "나무쌍도끼", "기초창", "여행자의지팡이", "조잡한활", "도적단궁",
      "목제석궁", "브론즈블레이드", "흑요석해머", "뼈검", "화속성지팡이", "용병의창", "사냥용장궁", "단도", "양날돌도끼", "속사용단궁", "강철검", "서번트의독", "용뼈대검",
             "아크스태프", "플레어보우", "디바인해머", "아다만티움검", "그림자용의어금니", "매직마스터스태프", "태고의활", "신이내린망치"]
