sudo apt-get install openssh-server
pip install -r install_pip.txt
logfilename=$(python3 getname.py)
nohup python3 main.py > logs/$logfilename 2>&1 & 
logfilename=$(python3 getname.py)
nohup python3 utils.py > logs/$logfilename 2>&1 & 