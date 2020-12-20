import os
import requests
from bs4 import BeautifulSoup
import subprocess as sp

# Path for your favourite code editor
programName = "C://XYZ\Programs\Microsoft VS Code\Code.exe"

# Supported Sites
codeforces = "https://codeforces.com/"
atcoder = "https://atcoder.jp/"

# Codeforces function
def codeforces_func():
    # Random Stuffs
    soup = BeautifulSoup(r.content, 'lxml')
    all_div = soup.findAll("div",{"class" : "title"})
    all_pre = soup.find_all("pre")

    if all_div and all_pre:
        pass
    else:
        print("Not a valid URL")
        exit(1)

    def listToString(s):
        str1 = ""
        for ele in s:
            str1 += ele
        return str1

    title = list(all_div[0].text)
    title = list(filter(lambda x: x != '.', title))
    for idx, item in enumerate(title):
        if(not item.isalpha()):
            title[idx] = "_"
    # Random Stuffs ends

    # language
    lang = "cpp"

    name = listToString(title)+"."+lang
    # print(name)

    # creating the file
    if not os.path.exists(name):
        f = open(name,'w')
        f.write("// "+URL+"\n\n")
        f.write("")
        f.close()
        print(name + " Created")
        sp.Popen([programName, name])
    else:
        print("File already exists")

# Atcoder function
def atcoder_func():
    # Random Stuffs
    soup = BeautifulSoup(r.content, 'lxml')
    all_span = soup.find_all("span",{"class":"h2"})
    title = []

    if all_span:
        pass
    else:
        print("Not a valid URL")
        exit(1)

    def listToString(s):
        str1 = ""
        for ele in s:
            str1 += ele
        return str1

    for x in all_span:
        title = list(x.text)
        title = list(filter(lambda x: x != '\n', title))
        title = list(filter(lambda x: x != '\t', title))
        title = list(filter(lambda x: x != '-', title))
        title = listToString(title)
        title = " ".join(title.split())
        title = "_".join(title.split())
        if title.endswith('Editorial'):
            title = title[:-(len('Editorial'))]
    # Random Stuffs ends

    # language
    lang = "cpp"

    name = listToString(title)+"."+lang
    # print(name)

    # creating the file
    if not os.path.exists(name):
        f = open(name,'w')
        f.write("// "+URL+"\n\n")
        f.write("")
        f.close()
        print(name + " Created")
        sp.Popen([programName, name])
    else:
        print("File already exists")


URL = input("Enter URL : ")

if(codeforces in URL):
    r = requests.get(URL)
    codeforces_func()
elif(atcoder in URL):
    r = requests.get(URL)
    atcoder_func()
else:
    print("Not a valid URL")
    exit(1)

# NOOB OP