import os

# Removes demos not in killstreaks.txt

demo_dir = r"D:\merged_partition_content\Steam\steamapps\common\Team Fortress 2\tf\demos"

os.chdir(demo_dir)
demo_list = os.listdir(demo_dir)

with open(r"C:\Users\ddeit\Desktop\KillStreaks.txt", 'r') as f:
    myNames = [line.strip() for line in f]

for f in demo_list:
    if f not in myNames: 
        fname = f.rstrip()
        os.remove(fname)
    
    


