
### Task: Get pull request information on a GitHub repository using python 

import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")   # Make a GET request to fetch pull requests data from the GitHub API

complete_details = response.json()   # Convert the JSON response to a dictionary 

for i in range (len(complete_details)):
    print(complete_details[i]["user"]["login"])



O/p: 
amritansh1502
michaelasp
tico88612
codeafridi
yykkibbb
ianw
gavinkflam
danwinship
lalitc375
ibm-adarsh
amritansh1502
nispriha
itzPranshul
bishal7679
ffromani
stlaz
macsko
Jefftree
KhushAhuja
natasha41575
mm4tt
luxas
tosi3k
serathius
brejman
harshil562
adrianreber
kannon92
everpeace
dhruv7539
