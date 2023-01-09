Dictionary=["Oursky","OurSky","OurskyLimited", "OurskyHK", "SkymakersDigitalLTD", "SkymakersDigitalLtd"]

Dictionary2=["Hi","Hello","HelloWorld", "HiWorld", "HelloWorldWideWeb", "HelloWWW"]

def calLen(item: str):
    if len(item) == 1: return 1
    count = 1
    for i in range(1, len(item)):
        if item[i].isupper() and item[i - 1].islower():
            count += 1
    return count

maxSum = 0
index = -1
for i in range(len(Dictionary)):
    tmp = calLen(Dictionary[i])
    if maxSum < tmp:
        maxSum = tmp
        index = i
print("Output=", Dictionary[index])
