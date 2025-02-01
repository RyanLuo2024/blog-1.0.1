import time,random
uid = time.strftime("%Y%m%d%H%M%S")
uid += str(random.randint(0,10))
uid += str(random.randint(0,10))
print(uid+".log")