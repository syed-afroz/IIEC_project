import os
syed_system = input("Enter Name Of The Application:")
if("run" or "open" or "execute" in syed_system) and ("word" or "msword" or "winword" in syed_system):
    os.system("start winword")

elif("run" or "open" or "execute" in syed_system) and ("excel" or "msexcel" in syed_system):
    os.system("start excel")

elif("run" or "open" or "execute" in syed_system) and ("powerpoint" or "mspowerpoint" or "powerpnt" in syed_system):
    os.system("powerpnt")

elif("run" or "open" or "execute" in syed_system) and ("access" or "msaccess" in syed_system):
    os.system("msaccess")

elif("run" or "open" or "execute" in syed_system) and ("mspublisher" or "publisher" or "mspub" in syed_system):
    os.system("mspub")

elif("run" or "open" or "execute" in syed_system) and ("onenote" or "msonenote" in syed_system):
    os.system("onenote")

elif("run" or "open" or "execute" in syed_system) and ("outlook" or "msoutlook" in syed_system):
    os.system("outlook")
    
else:
    print("sorry couldn't find the file")
