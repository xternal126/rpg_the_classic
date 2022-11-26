import random as r
import weaponry as w
import armory as a
import accesory as ac


def monsterdict(name, atk, spd, hp, drop, exp, chance, reward):
    global monst
    monst = {'name': name, 'atk': atk, 'spd': spd, 'hp': hp, 'drop': drop, 'exp': exp, 'chance': chance,
             'reward': reward, 'maxhp': hp}


드랍테이블1 = [a.가죽방어구, a.기초로브, a.날렵한늑대, a.헐거운체인메일,
          w.초보자의검, w.단단한목검, w.나무꾼도끼, w.녹슨구리검, w.뾰족한대거, w.나무쌍도끼, w.기초창, w.여행자의지팡이, w.조잡한활, w.도적단궁, w.목제석궁,
          ac.나무반지, ac.돌목걸이]
드랍테이블2 = [a.브론즈아머, a.암살자의옷, a.마법병로브,
          w.브론즈블레이드, w.흑요석해머, w.뼈검, w.화속성지팡이, w.용병의창, w.사냥용장궁, w.단도, w.양날돌도끼, w.속사용단궁,
          ac.구리팔찌, ac.가죽장갑, ac.흑요석반지, ac.가벼운목걸이]
드랍테이블3 = [a.기사의갑옷, a.그림자늑대, a.드래곤갑주, a.소울맨서로브, w.강철검, w.서번트의독이빨, w.용뼈대검, w.아크스태프, w.플레어보우, w.디바인해머,
                ac.강철목걸이, ac.치유의반지, ac.백금팔찌]
드랍테이블4 = [a.아처스피릿, a.불굴의기사의갑주, a.마력의지배자의로브, a.성스러운갑옷, w.아다만티움검, w.그림자용의어금니, w.매직마스터스태프, w.태고의활, w.신이내린망치,
          ac.아다만티움반지, ac.마나석목걸이, ac.금건틀릿]
monsterdict('고블린', r.randint(8, 14), r.randint(85, 110), 50,
            드랍테이블1, r.randint(7, 8),
            20, r.randint(1, 3))
고블린 = monst
monsterdict('늑대', r.randint(7, 12), r.randint(100, 120), 45,
            드랍테이블1, r.randint(6, 7),
            20, r.randint(1, 2))
늑대 = monst
monsterdict('슬라임', r.randint(4, 7), r.randint(60, 110), 30,
            드랍테이블1, r.randint(4, 6),
            15, r.randint(1, 2))
슬라임 = monst
monsterdict('거미', r.randint(5, 9), r.randint(90, 115), 45,
            드랍테이블1, r.randint(6, 7),
            20, r.randint(1, 2))
거미 = monst
monsterdict('흙 골렘', r.randint(12, 16), r.randint(60, 80), 70,
            드랍테이블1, r.randint(8, 10),
            20, r.randint(3, 5))
흙골렘 = monst
I급 = [고블린, 늑대, 슬라임, 거미, 흙골렘]


monsterdict('해골병사', r.randint(17, 21), r.randint(80, 100), 60,
            [w.뼈검], r.randint(12, 15),
            20, r.randint(4, 8))
해골병사 = monst
monsterdict('불의 정령', r.randint(15, 16), r.randint(115, 130), 55,
            [w.화속성지팡이], r.randint(11, 17),
            20, r.randint(3, 9))
불의정령 = monst
monsterdict('홉고블린', r.randint(19, 25), r.randint(90, 110), 80,
            드랍테이블2, r.randint(14, 19),
            20, r.randint(5, 9))
홉고블린 = monst
monsterdict('트롤', r.randint(21, 23), r.randint(80, 95), 90,
            드랍테이블2, r.randint(15, 18),
            25, r.randint(4, 10))
트롤 = monst
monsterdict('하급드래곤', r.randint(18, 23), r.randint(110, 120), 75,
            드랍테이블2, r.randint(16, 19),
            25, r.randint(6, 8))
하급드래곤 = monst

II급 = [해골병사, 불의정령, 홉고블린, 트롤, 하급드래곤]

monsterdict('해골기사', r.randint(24, 31), r.randint(75, 90), 120,
            [w.용뼈대검], r.randint(25, 32),
            30, r.randint(11, 19))
해골기사 = monst
monsterdict('화염드래곤', r.randint(28, 39), r.randint(80, 110), 140,
            드랍테이블3, r.randint(30, 41),
            30, r.randint(17, 23))
화염드래곤 = monst
monsterdict('철의골렘', r.randint(27, 36), r.randint(65, 85), 165,
            드랍테이블3, r.randint(29, 38),
            30, r.randint(16, 18))
철의골렘 = monst
monsterdict('소울트리', r.randint(28, 37), r.randint(80, 130), 140,
            [ac.치유의반지], r.randint(25, 39),
            30, r.randint(14, 19))
소울트리 = monst

III급 = [해골기사, 화염드래곤, 철의골렘, 소울트리]

monsterdict('데몬', r.randint(45, 58), r.randint(100, 130), 180,
            드랍테이블4, r.randint(48, 56),
            30, r.randint(28, 34))
데몬 = monst
monsterdict('흑염룡', r.randint(49, 67), r.randint(120, 165), 210,
            드랍테이블4, r.randint(57, 69),
            30, r.randint(31, 45))
흑염룡 = monst
monsterdict('파이어슬라임', r.randint(36, 45), r.randint(90, 125), 140,
            드랍테이블4, r.randint(29, 38),
            30, r.randint(26, 37))
파이어슬라임 = monst

IV급 = [데몬, 흑염룡, 파이어슬라임]

