import os
import xmlaccess
import mti_interactive
import time

dic = {}
for filename in os.listdir('./ecgen-radiology'):

    print(filename)
    #get text of the report
    txt = xmlaccess.getText(filename)
    print(txt)

    #get mti tags and store it in the dictionary
    it = time.time()
    tags = mti_interactive.getmtiTags('mbanthia.211cs232@nitk.edu.in','bf04a376-ac80-4451-a072-2e1487fa1a3d',txt)
    ft = time.time()
    print(ft-it)
    print(tags)
    dic[filename] = tags

