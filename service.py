import os
import sys
try:
    command = sys.argv[1]
    if (command=="start"):
        os.system("sh run.sh")
    if (command=="stop"):
        os.system("sh stop.sh")
    if (command=="restart"):
        os.system("sh stop.sh")
        os.system("sh run.sh")
    else:
        print("Error: not command:",command)
        print("""python3 service.py <command>
command:
    start -> start the web
    stop -> stop  the web
    restart ->restart the web""")
except:
    print("Error: please input command!")
    print("""python3 service.py <command>
command:
    start -> start the web
    stop -> stop  the web
    restart ->restart the web""")