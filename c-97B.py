intro = input("Introduce yourself: ")
charcount = 0
wordcount = 1
for i in intro:
    charcount += 1
    if i == " ":
        wordcount += 1 

print(charcount)
print(wordcount)

about = input("Tell us something about your location: ")
print("{}. {}".format(intro, about))