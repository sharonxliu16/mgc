import pprint

# dict of all members in mgc who are active and not associate (those that must attend events)
# key : value is email : [full name, org]
masterDict = {
    "zvh5237" : ["Zubaria Humayun", "aKDPhi"],
    "lgm5254" :	["Lauryn Massengill", "aKDPhi"],
    "xbl5246" :	["Lesley Li", "aKDPhi"],
    "vvt5174" :	["Vivian Trinh", "aKDPhi"],
    "lpc5512" :	["Ling Chen", "aKDPhi"],
    "abb6483" :	["Ash Bangching", "aKDPhi"],
    "sbk6105" :	["Bali Kang", "aKDPhi"],
    "jmn6017" :	["Janel Nguyen", "aKDPhi"],
    "hjn5127" :	["Holly Nguyen", "aKDPhi"],
    "nby5087" :	["Narin Yang", "aKDPhi"],
    "gzn5093" :	["Giang Nguyen", "aKDPhi"],
    "szl5263" :	["Sharon Liu", "aKDPhi"],
    "hfs5387" :	["Evelyn Su", "aKDPhi"],
    "emm6477" :	["Emily Miller", "aKDPhi"],
    "cjw6385" :	["Nikki Wu", "aKDPhi"],
    "bjc6146" :	["Bridhi Choudhary", "aKDPhi"],
    "lqe5119" :	["Liyah Ebuen", "aKDPhi"],
    "kvk5855" :	["Kaitlyn Kong", "aKDPhi"],
    "yqw5695" :	["Tiffany	Wang", "aKDPhi"],
    "xbc5128" :	["Xiao Chen", "aKDPhi"],
    "cmc7590" :	["Catherine Chan", "aKDPhi"],
    "ayl5152" :	["Anna LeTendre", "aKDPhi"],
    "ykl5537" :	["Jess Lin", "aKDPhi"],
    "rpv5157" :	["Dianne Valera", "aKDPhi"],
    "mqg5770" :	["Marcus Gonzalez", "LSU"],
    "jqf5517" :	["Jackson Fung", "LSU"],
    "dmc6928" :	["Desiree Cotto", "LTA"],
    "ebs5765" :	["Emily Sanchez", "LTA"],
    "jaf6366" :	["Jayden Foxx", "LTA"],
    "kdm5691" :	["Kayla Marrero", "LTA"],
    "lal5736" :	["Larra Lopez", "LTA"],
    "nzm5539" :	["Nicole Meneses", "MSU"],
    "img5138" :	["Isabel Galan", "MSU"],
    "dvn5263" :	["Derrick Nguyen", "PDPsi"],
    "jzh6435" :	["Joey Hong", "PDPsi"],
    "ari5119" :	["Aryan Ingale", "PDPsi"],
    "kyb5431" :	["Kyle Berlin", "PDPsi"],
    "skk6074" :	["Steven Ky", "PDPsi"],
    "bja5528" :	["Tommy Asbury", "PDPsi"],
    "aks7349" :	["Avish Shakwala", "PDPsi"],
    "pbk5215" :	["Pei-Hsuan Kao", "PDPsi"],
    "jcv5242" :	["Jared Vinluan", "PDPsi"],
    "aek5621" :	["Alp Karalar", "PDPsi"],
    "spk5859" :	["Nathan Kim", "PDPsi"],
    "ald6001" :	["Alexander Du", "PDPsi"],
    "jkf5556" :	["James Fong", "PDPsi"],
    "nfr5224" :	["Nicolas Recinos-Baltodano", "SLB"],
    "egm5344" :	["Edwin Martinez-Alvarez", "SLB"],
    "tdk5224" :	["Thomas Krizek", "SLB"],
    "amc9000" :	["Max Carrillo", "SLB"],
    "ima5272" :	["Isaac Arbelaez", "SLB"],
    "mmg6320" :	["Michael Garza", "SLB"],
    "asn5254" :	["Aditya Nemani", "SLB"],
    "rml5780" :	["Rafael Lara Matos", "SLB"],
    "afj5257" :	["Agha Jahangir", "SLB"],
    "ycc5028" :	["Yuritza Cespedes", "SLG"],
    "ecm5675" :	["Emily Maldonado", "SLG"],
    "skm6491" :	["Salma Morales", "SLG"],
    "mab7841" :	["Makaela Brown", "SLG"],
    "efw5249" :	["Elonie Ward", "SLG"],
    "akl5903" :	["Ashley Lebron", "SLG"],
    "mfm6522" :	["Mariela Martinez", "SLG"],
    "yas5067" :	["Yanira Santillan", "SLG"],
    "aic5650" :	["Alycia Colon", "SLG"],
    "abg5876" :	["Attiliah Garcia", "SLG"],
    "axt5688" :	["Anna Ting", "SOPi"],
    "lfh5411" :	["Lauren Hirschmann", "SOPi"],
    "ckc5857" :	["Claire Chen", "SOPi"],
    "acl5758" :	["Alice Liu", "SOPi"],
    "ayc5652" :	["Amber Chen", "SOPi"],
    "emc6360" :	["Emily Choe", "SOPi"],
    "lkf5255" :	["Lisa Fujii", "SOPi"],
    "mks6746" :	["Miyuko Suzukawa", "SOPi"],
    "mjs8798" :	["Mihika Srivastava", "SOPi"],
    "hdl5108" :	["Helaina Le", "SOPi"],
    "amk7527" :	["Alicia Kim", "SOPi"],
    "ryc5291" :	["Rachel Chang", "SOPi"],
    "smk6862" :	["Sophie Kuo", "SOPi"]
}

# dict to be returned (original is copy of masterDict, because those that are excused and present will be removed from returnDict)
returnDict = masterDict 

#when entering in the list of emails, make sure it is in one line and there is a space between each entry
excused = input("Enter the list of emails who submitted an excuse form: ")
present = input("Enter the list of emails who submitted the attendance form: ")

# turns the input of excused into a list and removes @psu.edu
excusedList = excused.split()
for  i in range(len(excusedList)):
    if "@psu.edu" in excusedList[i]:
        temp = excusedList[i].replace("@psu.edu", "")
        excusedList[i] = temp

# turns the input of those that who filled out attendance form into a list and removes @psu.edu
presentList = present.split()
for  i in range(len(presentList)):
    if "@psu.edu" in presentList[i]:
        temp = presentList[i].replace("@psu.edu", "")
        presentList[i] = temp

# iterates through excusedList and removes the corresponding key from returnDict
for i in excusedList:
    if i in returnDict:
        del returnDict[i]

# iterates through presentList and removes the corresponding key from returnDict
for i in presentList:
    if i in returnDict:
        del returnDict[i]

# now, returnDict should have only those that did not fill out an excuse form AND were not present at the event
# these are also the people who will be fined. 
# However, it is best to manually check this list and cross check on the sheets by Ctrl+F for each name in returnDict to the excuse form and attendance form just to double check

print("Here is a list of those that have unexcused absences and were not present: \n")

# pprint just prints the dictionary where each key : value is in a new line
pprint.pprint(returnDict)