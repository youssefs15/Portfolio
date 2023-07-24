import requests
page1 = "https://assess.joincyberdiscovery.com/challenge-files/clock-pt1?verify=zgIk5vQ4Cj45Y9c8s9je0Q%3D%3D"
page1_content = requests.get(page1)
page1text = page1_content.text

page2 = "https://assess.joincyberdiscovery.com/challenge-files/clock-pt2?verify=zgIk5vQ4Cj45Y9c8s9je0Q%3D%3D"
page2_content = requests.get(page2)
page2text = page2_content.text

page3 = "https://assess.joincyberdiscovery.com/challenge-files/clock-pt3?verify=zgIk5vQ4Cj45Y9c8s9je0Q%3D%3D"
page3_content = requests.get(page3)
page3text = page3_content.text

page4 = "https://assess.joincyberdiscovery.com/challenge-files/clock-pt4?verify=zgIk5vQ4Cj45Y9c8s9je0Q%3D%3D"
page4_content = requests.get(page4)
page4text = page4_content.text

page5 = "https://assess.joincyberdiscovery.com/challenge-files/clock-pt5?verify=zgIk5vQ4Cj45Y9c8s9je0Q%3D%3D"
page5_content = requests.get(page5)
page5text = page5_content.text

code = (page1text + page2text + page3text + page4text + page5text)
page6 = "https://assess.joincyberdiscovery.com/challenge-files/get-flag?verify=zgIk5vQ4Cj45Y9c8s9je0Q%3D%3D&string="+code
page6_content = requests.get(page6)
page6text = page6_content.text

print page6text
