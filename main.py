import os, sys
os.system("cls")
adata = os.getenv("APPDATA")
cwd = os.path.dirname(sys.argv[0])
path = input(f'Path to logfile (The latest log is "{adata}\\.minecraft\\logs\\latest.log"): ')
path = path.strip('"')
os.system("cls")
print("Processing... please wait")
with open(path,"r") as f:
    lines = f.read().splitlines()
with open("blacklisted.txt","r") as f:
    blacklisted = f.read().splitlines()
goodlines = []
for line in lines:
    chat = True
    if "[CHAT]" in line:
        chat = True
        ls = line.split("[CHAT]")
        line = ls[1]
        line = line[1:]
    else:
        for word in blacklisted:
            if word in line:
                chat = False
                break
        if line.startswith(" "):
            chat = False
    if chat ==True:
        ### COLORS
        line = line.replace("§6","\033[38;2;255;170;0m")
        line = line.replace("§c","\033[38;2;255;85;85m")
        line = line.replace("§4","\033[38;2;170;0;0m")
        line = line.replace("§e","\033[38;2;255;255;85m")
        line = line.replace("§2","\033[38;2;0;149;73m")
        line = line.replace("§a","\033[38;2;85;255;85m")
        line = line.replace("§b","\033[38;2;85;255;255m")
        line = line.replace("§3","\033[38;2;0;170;170m")
        line = line.replace("§1","\033[38;2;0;0;170m")
        line = line.replace("§9","\033[38;2;85;85;255m")
        line = line.replace("§d","\033[38;2;255;85;255m")
        line = line.replace("§5","\033[38;2;170;0;170m")
        line = line.replace("§f","\033[38;2;255;255;255m")
        line = line.replace("§7","\033[38;2;170;170;170m")
        line = line.replace("§8","\033[38;2;85;85;85m")
        line = line.replace("§0","\033[38;2;0;0;0m")
        ### STYLE
        line = line.replace("§l","\033[1m")
        line = line.replace("§n","\033[4m")
        line = line.replace("§o","\033[3m")
        line = line.replace("§m","\033[9m")
        line = line.replace("§k","\033[8m")
        line = line.replace("§r","\033[0m")
        goodlines.append(line)
os.system("cls")
for line in goodlines:
    print(line)
while True:
    pass