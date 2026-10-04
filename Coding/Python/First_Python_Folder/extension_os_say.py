import os

def say(word, /):
    word = word.lower()
    if word == "chargoggagoggmanchauggagoggchaubunagungamaugg":
        os.system('say "char gogg a gogg man chau ggag ogg chau boona gung a maugg"')
    if word == "supercalifragilisticexpialidocious":
        os.system('say "super cali frajil estic expi ali doush ious"')
    if word == "pneumonoultramicroscopicsilicovolcanoconiosis":
        os.system('say "new mono ultra microscopic silico volcano coneio sis"')
    if word == "canaliculodacryocystorhinostomy":
        os.system('say "can a lick you low dack ree oh sis tor hein ostomy"')
    if word == "taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronokupokaiwhenuakitanatahu":
        os.system('say "taw mata waka taung ee hanga ko au a o tamat ea turi pu kaka piki manga horono kupokai when new a kit a nata hu"')
    if word == "llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch":
        os.system('say "llan fair pool gwin gill gogery chwern drobwl lanty silio gogogoh"')
    else:
        os.system(f'say "{word}"')