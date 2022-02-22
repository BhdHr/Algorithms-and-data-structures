class Node:
    def __init__(self, data = None, next = None ):
        self.data = data
        self.next = next


class linkedList:
    def __init__(self):
        self.head = None

    def createHEAD(self,data):
        node = Node(data, self.head)
        self.head = node

    def createNEXT(self, data):
        if self.head is None:
            self.head = Node(data, None)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data,None)
   
    def deleteNode(self, key):
        temp = self.head 
        if (temp is not None): 
            if (temp.data == key): 
                self.head = temp.next
                temp = None
                return
        while(temp is not None): 
            if temp.data == key: 
                break
            prev = temp 
            temp = temp.next
        if(temp == None): 
            return
        prev.next = temp.next
        temp = None

    def reverseNode(self):
        prev = None
        temp = self.head
        while temp is not None:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        self.head = prev
    
    def deleteTail(self):
        if(self.head != None):
            if(self.head.next == None):
                self.head = None
            else:
                temp = self.head
                while(temp.next.next != None):
                    temp = temp.next
        lastNode = temp.next
        lastForPrint = lastNode
        temp.next = None
        lastNode = None
        print(lastForPrint.data)

    def deleteHead(self):
        if self.head !=None:
            temp = self.head
            self.head = self.head.next
            temp = None
        
    def searchNode(self, key):
        temp = self.head

        if temp.data == key:
            print("We have found necessary item %s "%format(temp.data))
        else:
            print( 'Element not found')
        temp = temp.next

    def toArray(self):
        arr = []
        temp = self.head
        while temp!=None:
            arr.append(temp.data)
            temp = temp.next

        print(arr)
        return
    
    def fromArray(self, data):
        for i in range(0,len(data),1):
            self.createNEXT(data[i])
        return

    def printingList(self):
        temp = self.head
        linkedListStr = ''
        if temp is  None:
            print('List is empty')
        while temp:
            linkedListStr += '['+str(temp.data)+'] ' + '-->'
            temp = temp.next
        print(linkedListStr)

if __name__ == '__main__':

    list1 = linkedList()
    
    list1.createHEAD('one') #add to begining 
    list1.createNEXT(2) # add to end 
    list1.createNEXT(78.9)
    list1.createNEXT(12)
    
    
    list1.fromArray(data =[99, 88, 98]) #add from array
    list1.printingList() # print as string

    list1.toArray() #convert to array

    list1.deleteTail() #delete the last element
    list1.printingList()

    list1.deleteHead() #delete first element
    list1.printingList()

    list1.searchNode('2') #find Node with value