import multiprocessing
import os
from includes.colour import colour
runflag = True
os.system("clear")
print("""\033[1
    #       #     ### ##   # ###  #     ####### ######
   # #     # #     #  # #  # #  # #     #     # #
  #   #   #   #    #  #  # # #### #     #     # #   ###
 #     # #     #   #  #   ## #  # #     #     # #    #
#       #      #  ### #    # ###  ##### ####### ######
\033[0m
{0}v1.1@20250201build01{1}
""".format(colour.GREEN,colour.NONE))
def runningmain():
    print("[MAIN_SERVICE_MASSAGE] service.py -> _log line:16 [INFO] :  running main")
    os.system("./.venv/bin/python main.py")

if __name__ == "__main__":
    print("-------Press CTRL+C to quit-------\n\n\n")
    try:
        main = multiprocessing.Process(target=runningmain)
        main.start()
    except KeyboardInterrupt:
        print("[MAIN_SERVICE_MASSAGE] service.py -> _log line:25 [INFO] :  stop main")
    