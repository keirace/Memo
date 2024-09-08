
############################################################
#  Write code in this file
# Post this file in Canvas
# Cut and paste the whole file in Leetcode and run. All tests must pass
# Note that you should do 4 times in 225, 235,622 and 641
# TA will run this file 4 times in 225, 235,622 and 641
# All tests must pass for 100
########################################################### 

class ListNode:
    #NOTHING CAN BE CHANGED HERE
    def __init__(self, val = 0, next= None):
        self.val = val
        self.next = next
            
############################################################
#  class  Slist
###########################################################   
class Slist():
    def __init__(self):
        #NOTHING CAN BE CHANGED HERE
        self._first = None
        self._last = None
        self._len = 0 
        
    #############################
    # WRITE All public functions BELOW
    # YOU CAN HAVE ANY NUMBER OF PRIVATE FUNCTIONS YOU WANT
    #############################
    def get_len(self):
        return self._len
    
    def get_first_val(self):
        return self._first.val
    
    def get_last_val(self):
        return self._last.val
    
    def append(self, value):
        new_node = ListNode(value, None)
        if self.get_len() == 0:
            self._first = new_node
        else:
            self._last.next = new_node
        self._last = new_node
        self._len += 1

    def prepend(self, value):
        new_node = ListNode(value, self._first)
        if self.get_len() == 0:
            self._last = new_node
        self._first = new_node
        self._len += 1

    def delete_first(self):
        temp = self._first.val
        self._first = self._first.next
        self._len -= 1
        return temp
    
    def delete_last(self):
        temp = self._first
        if temp == self._last:
            self._first = None
            self._last = None
        else:
            while temp.next != self._last:
                temp = temp.next
            temp.next = None
            self._last = temp
        self._len -= 1

############################################################
#  class  MyStack
#225. Implement Stack using Slist

#https://leetcode.com/problems/implement-stack-using-queues
########################################################### 
class MyStack:
    def __init__(self):
        #NOTHING CAN BE CHANGED HERE
        self._s = Slist()

    #############################
    # Stack functions
    #############################
    def push(self, x: int) -> None:
        self._s.prepend(x)

    def pop(self) -> int: # first item
        if self.empty():
            return -1
        return self._s.delete_first()

    def top(self) -> int:
        if self.empty():
            return -1
        return self._s.get_first_val()

    def empty(self) -> bool:
        return self._s.get_len() == 0

############################################################
#  class  MyQueue
#232. Implement Queue using Slist

# https://leetcode.com/problems/implement-queue-using-stacks/
########################################################### 
class MyQueue:
    def __init__(self):
        #NOTHING CAN BE CHANGED HERE
        self._s = Slist()

    #############################
    # Queue functions
    #############################
    def push(self, x: int) -> None:
        self._s.append(x)

    def pop(self) -> int: # first item
        if self.empty():
            return -1
        return self._s.delete_first()

    def peek(self) -> int:
        if self.empty():
            return -1
        return self._s.get_first_val()

    def empty(self) -> bool:
        return self._s.get_len() == 0

############################################################
#  MyCircularQueue
# 622. Design Circular Slist
# https://leetcode.com/problems/design-circular-queue/
########################################################### 

class MyCircularQueue:
    def __init__(self, k: int):
        #NOTHING CAN BE CHANGED HERE
        self._K = k 
        self._s = Slist()

    #############################
    # CircularQueue functions
    #############################
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self._s.append(value)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self._s.delete_first()
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self._s.get_first_val()

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self._s.get_last_val()

    def isEmpty(self) -> bool:
        return self._s.get_len() == 0

    def isFull(self) -> bool:
        return self._K == self._s.get_len()

############################################################
#  MyCircularDeque
#641. Design Circular Deque using Slist
#https://leetcode.com/problems/design-circular-deque

###########################################################  
class MyCircularDeque:
    def __init__(self, k: int):
        #NOTHING CAN BE CHANGED HERE
        self._K = k 
        self._s = Slist()

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self._s.prepend(value)
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self._s.append(value)
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self._s.delete_first()
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self._s.delete_last()
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self._s.get_first_val()

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self._s.get_last_val()

    def isEmpty(self) -> bool:
        return self._s.get_len() == 0

    def isFull(self) -> bool:
        return self._s.get_len() == self._K