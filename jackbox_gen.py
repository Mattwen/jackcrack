alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

keywords = []
text_file = open("jackbox.txt", "w")
for alpha1 in alphabets:
    for alpha2 in alphabets:
        for alpha3 in alphabets:
            for alpha4 in alphabets:
                
                text_file.write(('http://blobcast.jackboxgames.com/room/' + alpha1+alpha2+alpha3+alpha4).upper() + '?userId=c700d781-5468-47c9-93c0-f71aec39d0c8')
                text_file.write('\n')
                
                
                

