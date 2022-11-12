def accedict(name, kind, Prot, effect, effectrank):
    global acce
    acce = {'name': name, 'kind': kind, 'prot': Prot, 'effect': effect, 'effectrank':effectrank}

accedict('없음', '-', 0, '-', 0)
공기 = acce
accedict('나무반지', '반지', 1, '-', 0)
나무반지 = acce
accedict('돌목걸이', '목걸이', 2, '-', 0)
돌목걸이 = acce

I티어 = [나무반지, 돌목걸이]

accedict('구리팔찌', '팔찌', 3, '-', 0)
구리팔찌 = acce
accedict('가죽장갑', '장갑', 2, '-', 0)
가죽장갑 = acce
accedict('흑요석반지', '반지', 2, '불굴', 2)
흑요석반지 = acce
accedict('가벼운목걸이', '목걸이', 1, '신속', 1)
가벼운목걸이 = acce

II티어 = [구리팔찌, 가죽장갑, 흑요석반지, 가벼운목걸이]

accedict('강철목걸이', '목걸이', 5, '-', 0)
강철목걸이 = acce
accedict('치유의반지', '반지', 3, '재생', 2)
치유의반지 = acce
accedict('백금팔찌', '팔찌', 2, '불굴', 3)
백금팔찌 = acce

III티어 = [강철목걸이, 치유의반지, 백금팔찌]

accedict('아다만티움반지', '반지', 7, '불굴', 4)
아다만티움반지 = acce
accedict('마나석목걸이', '목걸이', 5, '마나부스트', 3)
마나석목걸이 = acce
accedict('금건틀릿', '장갑', 9, '재생', 4)
금건틀릿 = acce

IV티어 = [아다만티움반지, 마나석목걸이, 금건틀릿]

straccesory = ["나무반지", "돌목걸이", "구리팔찌", "가죽장갑", "흑요석반지", "가벼운목걸이", "강철목걸이", "치유의반지", "백금팔찌",
               "아다만티움반지", "마나석목걸이", "금건틀릿"]