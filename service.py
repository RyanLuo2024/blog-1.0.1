import multiprocessing
import os
runflag = True

def runningmain():
    print("-------running main-------")
    os.system("python main.py")

def runningssh():
    print("-------running ssh-------")
    os.system("python ssh.py")

if __name__ == "__main__":
    print("\033[1mmineblog\033[0m")
    print("v1.1")
    print("-------Press CTRL+C to quit-------")
    main = multiprocessing.Process(target=runningmain)
    ssh = multiprocessing.Process(target=runningssh)
    main.start()
    ssh.start()