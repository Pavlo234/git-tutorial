from collections import deque
du = deque([1,2,3,4,5])
du.pop()
print(du)


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.end = None
    
    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.end = new_node
            return 
        self.end.next = new_node
        self.end = new_node
        # courend_node  = self.head
        # while courend_node.next:
        #     courend_node = courend_node.next
        # courend_node.next = new_node
    
    def print_list(self):
        courend_node = self.head
        while courend_node:
            print(courend_node.data,end=', '  if courend_node.next else '\n')
            courend_node = courend_node.next
po = LinkedList()
po.append(False)
po.append('wewew')
po.prepend(100000)
po.append({212,12,121,2133,1})

po.print_list()



class Queue:
    def __init__(self) -> None:
        self._list = list()

    def push(self, elem):
        self._list.append(elem)

    def pop(self):
        if len(self._list) == 0:
            pass
        else:
            self._list.pop(0)
            # elem = self._list[-1]
            # self._list.remove(elem)
    
    def show(self):
        if len(self._list) == 0:
            pass
        return self._list

    def isempty(self):
        return len(self._list) == 0 

l = Queue()
print(l.isempty())
l.push('pavlo')
l.push('pavlo')
l.push('pavlo')
l.push(123)
l.push('pavlo')
l.push(4343)
l.push(456)
l.pop()
l.pop()

print(l.show())

print(l.isempty())



