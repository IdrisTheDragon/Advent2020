door = 14788856
card = 19316454

# card = 5764801
# door = 17807724

startingValue = 1
divisor = 20201227

doorSubjectNum = 7
cardSubjectNum = 7

def transform(value,subjectNumber,divisor):
    value = value * subjectNumber
    value = value % divisor
    return value

def figureLoopSize(startingValue,subjectNum,divisor,target):
    loopSize = 0
    value = startingValue
    while value != target:
        value = transform(value,subjectNum,divisor)
        loopSize = loopSize + 1
    return loopSize,value

cardLoopSize, cardPublicKey = figureLoopSize(startingValue,cardSubjectNum,divisor,card)
doorLoopSize, doorPublicKey = figureLoopSize(startingValue,cardSubjectNum,divisor,door)

print(cardLoopSize,cardPublicKey)
print(doorLoopSize,doorPublicKey)

value = startingValue
for i in range(0,doorLoopSize):
    value = transform(value,cardPublicKey,divisor)
print(value)