def banner():
    print "#=========================================================================#"
    print "|_______                               ____             _                 |"
    print "|__   __|                             |  _ \           | |                |"
    print "|  | | ___ _ __ _ __ ___  _   ___  __ | |_) | __ _  ___| | ___   _ _ __   |"
    print "|  | |/ _ \ '__| '_ ` _ \| | | \ \/ / |  _ < / _` |/ __| |/ / | | | '_ \  |"
    print "|  | |  __/ |  | | | | | | |_| |>  <  | |_) | (_| | (__|   <| |_| | |_) | |"
    print "|  |_|\___|_|  |_| |_| |_|\__,_/_/\_\ |____/ \__,_|\___|_|\_\\__,_| .__/  |"
    print "|                                                                 | |     |"
    print "|                                                                 |_|     |"
    print "#=========================================================================#"
    print "Optons :                             "
    print " 1. Backup all Package"
    print " 2. Restore All Package"
    print " 0. Exit"

opt = raw_input("masukan opsinya : ")
if opt == "1":
    os.system("termux-setup-storage") print "creating setup storage..."
    os.system("mkdir -p /sdcard/termux-backup") print "make dir termux backup..."
    os.system("apt update && apt -o APT::Keep-Downloaded-Packages='true' upgrade -y") print "updating & backuping"
    os.system("mv $PREFIX/var/cache/apt/archives/*.deb /sdcard/termux-backup 2>/dev/null")
    print "Backuping Package Finised!"
    banner()
elif opt == "2":
    print "finding termux-backup on sdcard..." os.system("cd /sdcard/termux-backup") 
    print "installing all Package..." os.system("dpkg -i ./*")
    print "Restoring Finished!" os.system("cd $HOME")
else:
    os.system("exit()")
