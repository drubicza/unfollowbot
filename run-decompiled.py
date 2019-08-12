import aux_funcs, sys, json, time, random, os
from LevPasha.InstagramAPI import InstagramAPI
followers = []
followings = []
min_delay = 5
max_delay = 10
MAXIMO = 100
G0 = '\x1b[0;32m'
G1 = '\x1b[1;32m'
C0 = '\x1b[0;36m'
C1 = '\x1b[1;36m'
P0 = '\x1b[0;35m'
P1 = '\x1b[1;35m'
W0 = '\x1b[0;37m'
W1 = '\x1b[1;37m'
B0 = '\x1b[0;34m'
B1 = '\x1b[1;34m'
R0 = '\x1b[0;31m'
R1 = '\x1b[1;31m'

def logo():
    os.system('clear')
    print('\n\n%s\n   ________,  \n  /_  ___   \\  %s+ %sINSTAGRAM UNFOLLOW BOT%s\n /%s@%s \\/%s@%s  \\   \\ %s- %shttps://instagram.com/soekamti97%s\n \\__/\\___/   / %s- %shttps://facebook.com/dafuq.co.id%s\n  \\_%s\\/%s______/  %s- %shttps://youtube.com/NjankSoekamti\n' % (G1, R1, C1, G1, R1, G1, R1, G1, R1, P0, G1, R1, P0, G1, W0, G1, R1, P0))


def bye():
    print('\n%s  Thanks for using this tool and keep support me :)' % C0)
    time.sleep(0.9)
    print(u'  %s\u25a3 %sAuthor        %s:   %sNjank Soekamti ' % (R1, W0, C0, W0))
    print(u'  %s\u25a3 %sContributor   %s:   %skiller.Bytes[%s0%s] ' % (R1, W0, C0, W0, R0, W0))
    time.sleep(0.5)
    exit(' ')


try:
    logo()
    print('%s  Please login using your Instagram account first' % C0)
    time.sleep(0.8)
    uname = input(u'%s  \u2022 %susername : ' % (G1, W0))
    passwd = input(u'%s  \u2022 %spassword : ' % (G1, W0))
    api = InstagramAPI(uname, passwd)
except KeyboardInterrupt:
    bye()

def super_unfollow():
    print('\n  %sStart unfollow not follow back. Please wait ...' % C0)
    count = 0
    for i in followings:
        if i not in followers:
            count += 1
            time.sleep(float(random.uniform(min_delay * 10, max_delay * 10) / 10))
            user_id = aux_funcs.get_id(i)
            print('  %s%s%s) %sUnfollowing %s> %s%s' % (W0, str(count), R0, W0, R0, W0, i))
            api.unfollow(user_id)


def unfollowall():
    print('\n  %sStart unfollowing all user. Please wait ...' % C0)
    count = 0
    for i in followings:
        count += 1
        time.sleep(float(random.uniform(min_delay * 10, max_delay * 10) / 10))
        user_id = aux_funcs.get_id(i)
        print('  %s%s%s) %sUnfollowing %s> %s%s' % (W0, str(count), R0, W0, R0, W0, i))
        api.unfollow(user_id)


def main():
    try:
        api.login()
        print('\n  %sLogin success. select this menu below' % C0)
        print('  %s{%s1%s} %sunfollow not follback' % (R0, W0, R0, W0))
        print('  %s{%s2%s} %sunfollow all user' % (R0, W0, R0, W0))
        option = input('  %s>%s>%s> %s' % (R0, W0, R0, W0))
        for i in api.getTotalSelfFollowers():
            followers.append(i.get('username'))

        for i in api.getTotalSelfFollowings():
            followings.append(i.get('username'))

        if option == '1':
            super_unfollow()
        elif option == '2':
            unfollowall()
        else:
            bye()
    except KeyboardInterrupt:
        bye()


if __name__ == '__main__':
    main()
