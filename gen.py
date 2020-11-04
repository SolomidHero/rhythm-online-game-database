import random as rd
import re

songs = [
  "Highscore - Panda Eyes & Teminite",
  "Nanamori-chu*Gorakubu - Yuriyurarararayuruyuri Daijiken",
  "Powerless - Frey's Philosophy",
  "xi - Zauberkugel",
  "Yura Hatsuki - Shadows ~Kage Iro Yousei Ehon~",
  "Hiroyuki Sawano - BLOWIN'",
  "DJ Genki VS Camellia feat. moimoi - YELL!",
  "EMILIA(CV: Rie Takahashi) - Stay Alive",
  "Shinji Orito - shionari",
  "Halozy - S.A.T.O.R.A.R.E",
  "Hanasaka Yui(CV: M.A.O) - Harumachi Clover",
  "Yasuda Rei - Best of my Love",
  "JYOCHO - Taiyou to Kurashite Kita",
  "KOTOKO - One Small Step",
  "Primary - SHUTTER*GIRL-crossfade-",
  "Okui Aki - Calendrier",
  "yuiko - Chiisana Amai Koi",
  "Skytree - Duet",
  "Red Velvet - Red Flavor",
  "This Is America - Childish Gambino",
  "Nice For What - Drake",
  "God's Plan - Drake",
  "Psycho - Post Malone Featuring Ty Dolla $ign",
  "Meant To Be - Bebe Rexha & Florida Georgia Line",
  "The Middle - Zedd, Maren Morris & Grey",
  "Friends - Marshmello & Anne-Marie",
  "Rockstar - Post Malone Featuring 21 Savage",
  "Pray For Me - The Weeknd & Kendrick Lamar",
  "NegaRen - A Bunch Of Samples Played Consecutively",
  "Himeringo - Shinitai-chan",
  "REOL - 404 not found",
  "Camellia - Feelin Sky (Camellia's \"200step\" Self-remix)",
  "S3RL feat Tamika - Tell Me What You Want",
  "yukizakurasou - Natsukage ~Ano Hikoukigumo wo Koeta, Sono Saki e~",
  "Rezonate - The Journey",
  "Marika - knowing",
  "Satou Hitomi - Reitou Container",
  "Aqours - Mirai no Bokura wa Shitteru yo",
  "ZUN - U.N. Owen was her? (Christmas Remix)",
  "monet - Kagami no Sekai ni wa Watashi shika Inai -another version-",
  "Mitsuki Nakae - Ouka Enbu",
  "halyosy - Snowman",
  "TJ PA5CON - Let's Go",
  "Yuki Kajiura - wo ist die Kaese?",
  "Shimotsuki Haruka - FLOWERS",
  "Mami Kawada - Contrail ~Kiseki~",
  "Furimawasare-tai - Heart Purupuru Jiken desu",
  "TO-MAS feat. Chima - FLIP FLAP FLIP FLAP (TV SIZE)",
  "Imperial Circus Dead Decadence - Yomi yori Kikoyu, Koukoku no Tou to Honoo no Shoujo.",
  "Kansou - Nyanpasu Bang Bang",
  "Maaya Sakamoto - Sanagi",
  "aran - Moonbound feat. Yukacco (USAO Remix)",
  "KASAI HARCORES - Cycle Hit",
  "Squarepusher - Dark Steering",
  "Draw the Emotional - Endless cycle of rebirth & We cannot get out of here forever",
  "Yasuda Rei - Mirror",
  "fhana - Hello!My World!!",
  "Shimotsuki Haruka - EXEC_PAJA/.#Orica extracting.",
  "Denkishiki Karen Ongaku Shuudan - Toki Hatsuru Yume",
  "Asaka - Edelweiss",
  "fhana - Songs Compilation",
  "Petit Rabbit's - No Poi!",
  "Savant - Virgin",
  "Oshimizu Nako (CV:Toyosaki Aki) - Diamond",
  "Feint - Fall Away",
  "Streetlight Manifesto - Punk Rock Girl",
  "GET IN THE RING - Rebirth",
  "Yasuda Rei - Kimi no Uta TV ver.",
  "Chima - Hajimari no Shirushi (Anime Size)",
  "shoujo byou - Gareki no Shuuon",
  "KOTOKO - Koi Kou Enishi",
  "Guilty Kiss - Shadow gate to love",
  "Razlom - Darkmist",
  "chano & 40mP - Natsukoi Hanabi",
  "Sasaki Sayaka - Exceed the Destiny (short ver.)",
  "MrWeebl - Narwhals",
  "fourfolium - Yumeiro Compass",
  "VerseQuence - Wilt"
]

mods = ['easy', 'no fail', 'less time', 'hard rock', 'hidden', 'double time', 'hardcore', 'flashlight'];

name = list()
artist = list()
words = list()

it = 0
for e in songs:
  it += 1
  pair = e.split(" - ")
  name.append(pair[0])
  artist.append(pair[1])
  words.append(re.findall('\w+', e))

# # Tournament plays
# for i in range(12):
#   pl = rd.sample(range(i*400, i * 400 + 400), 70)
#   for p in pl:
#     print(f' ({i + 1}, {p + 1}),', end="")
#   print()

# Tournament maps
for i in range(12):
  pl = rd.sample(range(i * 17, i * 17 + 17), 8)
  for j in range(len(pl)):
    print(f' ({i + 1}, {pl[j]}, {len(pl) - j}),', end="")
  print()

# # Play modes
# file = open('rate_text.txt', 'w')
# for i in range (5678):
#   num = rd.randrange(1, 11);
#   if num == 10:
#     ml = rd.sample(mods, 2);
#     file.write(f'({i + 1}, {ml[0]!r}), ')
#     file.write(f'({i + 1}, {ml[1]!r}),\n')
#   elif num > 7:
#     file.write(f'({i + 1}, {mods[rd.randrange(0, 8)]!r}),\n')

# # Followers
# file = open('rate_text.txt', 'w')
# for i in range(36):
#   num = rd.randrange(1, 36)
#   pl = rd.sample(list(range(36)[:i]) + list(range(36)[i+1:]), num)
#   for e in pl:
#     date = f'\'{rd.randrange(2010, 2017)}-{rd.randrange(1, 13)}-{rd.randrange(1, 29)} {rd.randrange(0, 24)}:{rd.randrange(0, 60)}:{rd.randrange(0, 60)}\''
#     file.write(f'({i + 1}, {e + 1}, {date}),\n')

# # BeatmapRate
# file = open('rate_text.txt', 'w')
# for i in range(78):
#   num = rd.randrange(1, 37)
#   pl = rd.sample(range(1, 37), num)
#   for e in pl:
#     file.write(f'({i + 1}, {e}, {rd.randrange(1, 11)}),\n')

# # Score
# f = open('gen_text.txt', 'w')
# def def_score(diff_id, difficulty, object_count):
#   for i in range(rd.randrange(1, 10)):
#     acc = 100 - rd.randrange(0, 10000) / 300
#     if acc == 100:
#       grade = 'SS'
#     elif acc > 97:
#       grade = 'S'
#     elif acc > 94:
#       grade = 'A'
#     elif acc > 85:
#       grade = 'B'
#     elif acc > 70:
#       grade = 'C'
#     else:
#       grade = 'D'
#     user_id = rd.randrange(1, 36)
#     max_combo = rd.randrange(object_count // 2, object_count)
#     score = int(object_count * acc * 30 + 200 * max_combo)
#     miss = rd.randint(0, int(object_count * (100 - acc) / 100))
#     pp = int(difficulty * max_combo * (acc - 55) / object_count * 2)
#     date = f'\'{rd.randrange(2010, 2017)}-{rd.randrange(1, 13)}-{rd.randrange(1, 30)} {rd.randrange(0, 24)}:{rd.randrange(0, 60)}:{rd.randrange(0, 60)}\','
#     f.write(f'({diff_id}, {user_id}, {grade!r}, {score}, {(format(acc, ".2f"))!r}, {date} {max_combo}, {miss}, {pp}, \'https://mega.nz/...\'),\n')

# # diffs
# for it in range(78):
#   length = rd.randrange(30, 240)
#   BPM = rd.randrange(120, 240)
#   for diff in range(rd.randrange(1, 6)):
#     length = length + rd.randrange(-10, 10)
#     BPM = BPM + rd.randrange(-12, 12)
#     d = 3 + BPM / 120 + rd.randrange (-100, 100) / 100 + length / 200
#     object_count = int(d * length / 2 + rd.randrange(-10, 10));
#     print(f'({it + 1}, {(format(d, ".2f"))!r}, {length}, {BPM}, {object_count}),')
#     for i in range(rd.randrange(4, 7)):
#       def_score(rd.randrange(1, 200), d, object_count)

# # tags
# it = 0
# for tags in words:
#   it += 1
#   for tag in tags:
#     print(f'({(it)!r}, {tag!r})', end=', ')
#   print()

# songs
# for i in range(len(name)):
#   s = f'({name[i]!r}, {artist[i]!r}, \'{rd.randrange(1, 37)!r}\', '
#   s += f'\'{rd.randrange(2010, 2017)}-{rd.randrange(1, 13)}-{rd.randrange(1, 30)} {rd.randrange(0, 24)}:{rd.randrange(0, 60)}:00\','
#   s += f'\'{rd.randrange(2010, 2017)}-{rd.randrange(1, 13)}-{rd.randrange(1, 30)} {rd.randrange(0, 24)}:{rd.randrange(0, 60)}:00\','
#   s += f'\'electronic\', \'instrumental\', \'exact_link\'),'
#   print(s)

