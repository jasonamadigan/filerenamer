import os
import re
from titlecase import titlecase
import itertools

##def addzero:
##    files = os.listdir(os.getcwd())
##
##    old_pattern = 'Extreme Open Guard-3-'
##    repl_pattern = 'Extreme Open Guard-3-0'
##
##    for file in files:
##        new_name = re.sub(old_pattern, repl_pattern, file)
##        os.rename(file, new_name)

def fixcase(text):
    return titlecase(text)


#Format Should be n-nn-Title.m4v


#Get a list of names of all the files in the directory
#Save the numbers from the file name
#Associate number to title
#Rename the file based on this format 'n-nn-Title.m4v'

all_files = os.listdir(os.getcwd())

valid_files = []

for line in all_files:
    if re.search('(Extreme Open Guard-)(5-\d\d)\.m4v',line):
        #print line
        valid_files.append(line)


with open('Drills.txt','r') as f:
    #title_list = f.readlines()
    title_list = []
    for line in f:
        title_list.append(titlecase(line))
    #print(title_list)


for files,title in itertools.izip(valid_files, title_list):
    pattern = re.compile('(Extreme Open Guard-)(5-\d\d)\.m4v')
    mo = pattern.match(files)
    prefix = mo.group(2)

    new_name = prefix + "-" + title.strip() +".m4v"
    #print "Old name:" + files
    print "new name:" + new_name
    #print os.getcwd()+'\\'+files
    os.rename(files, new_name)
    
