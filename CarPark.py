# Python version 3.5
# Queue class definition
class Queue:
    def __init__(self):
        self._qList = list()
    def isEmpty(self):
        return len(self._qList)==0
    def __len__(self):
        return len(self._qList)
    def enqueue(self,item):
        self._qList.append(item)
    def dequeue(self):
        assert not self.isEmpty(),"Cannot dequeue from an empty queue"
        return self._qList.pop(0)

# Car class definition
class Car:
    def __init__(self,pltNum):
        self.pltNum = pltNum
        self.counter = 0
        self.next = None

# LinkedList class definition
class LinkedList:

    def __init__(self):
        self.head = None
        self.numCar = 0

    # insertion
    def insertLast(self,pltNum):
        newCar = Car(pltNum)
        newCar.next = None
        if self.head == None:
            self.head = newCar
            return
        lcar = self.head # last car
        while lcar.next != None:
            lcar = lcar.next
        lcar.next = newCar
        self.numCar += 1
        
    # moving to park or departing
    def remFirst(self):
        fcar = self.head # first car
        self.head = fcar.next
        fcar.next = None
        return fcar
        del fcar
        self.numCar -= 1

    # departing
    def remSpecified(self,pltNum):
        self.pltNum = pltNum
        scar = self.head # selected car
        while scar != None:
            pcar = scar # privious car
            scar = scar.next
            if self.head.pltNum == self.pltNum:
                fcar = self.head # first car
                self.head = fcar.next
                fcar.next = None
                return fcar
                del fcar
                self.numCar -= 1
                break
            elif scar.pltNum == self.pltNum:
                pcar.next = scar.next
                scar.next = None
                return scar
                del scar
                self.numCar -= 1
                break

    # check the car, is in waiting list or not
    def checkCar(self,pltNum):
        scar = self.head
        k = False
        while scar!=None:
            if scar.pltNum==pltNum:
                k = True
            scar = scar.next
        return k

# main program
park = Queue()
parkIn = list()
waitingList = LinkedList()
maxSize = 10

# arriving function
def arriving(plateNum,counter):
    
    # when park has a free space
    if checkSpaces():
        newCar = Car(plateNum)
        newCar.counter = counter
        park.enqueue(newCar)
        parkIn.append(plateNum)
        if newCar.counter==0:
            print("There is a free room for a car. ",newCar.pltNum," car is arriving to park.")

    # when park hasn't a free space
    else:
        print("There is no free room in park. %s have to wait." % plateNum)
        waitingList.insertLast(plateNum)


# departing function
def departing(plateNum):
    
    # when car in the park
    if plateNum in parkIn:
        n = 0
        l = park.__len__()
        while n < l:
            n += 1
            x = park.dequeue()
            x.counter += 1
            if x.pltNum==plateNum and n==1:
                parkIn.pop(parkIn.index(plateNum))
                print("\n" , x.pltNum , " car was moved " , x.counter , " times within the garage and now it's departing.\n")
                break
            elif x.pltNum==plateNum:
                parkIn.pop(parkIn.index(plateNum))
                print("\n" , x.pltNum , " car was moved " , x.counter , " times within the garage and now it's departing.\n")
            else:
                arriving(x.pltNum,x.counter)

        # move car to park from waiting list
        if waitingList.numCar != 0:
            y = waitingList.remFirst()
            arriving(y.pltNum,y.counter)

    # when car not in the park
    else:
        
        # when car in the waiting list
        if waitingList.checkCar(plateNum):
            x = waitingList.remSpecified(plateNum)
            print("\n" , x.pltNum , " car was moved " , x.counter , " times within the garage and now it's departing.\n")      

        # when car not in the waiting list
        else:
            print("There is no a vehicle under " , plateNum)

    

# check free spaces in park
def checkSpaces():
    if (park.__len__() < maxSize):
        return True
    else:
        return False


# inputs.txt file should include in same folder that the python program has saved.
#   there should not blank lines between inputs or end of the file
#   input structure must be {'a' or 'd'} {space} {plate number with 4 digits}


# getting inputs and inserting to program
file = open("inputs.txt","r")
while True:
    line = file.readline()
    if(""==line):
        print("\n##### All the inputs have read.")
        break
    k = line.split(" ")
    aORd = k[0]
    plateNum = k[1][:4]
    if aORd=='a':
        arriving(plateNum,0)
    elif aORd=='d':
        departing(plateNum)
    else:
        print("\n your input ", aORd,"  is not identified.\n")
    


