class MinStack:
    class Node:
        
        def __init__(self, value):
            self.value = value
            self.next = None
            self.prev = None


    def __init__(self):
        self.tail = None
        self.min = float("inf")
        self.mtail = None
        

    def push(self, val: int) -> None:
        node = self.Node(val)
        mnode = self.Node(val)
        # if empty
        if self.tail is None:
            self.tail = node
            self.min = node.value
            self.mtail = mnode
        # if not 
        else:
            curr_tail = self.tail

            # update min
            if self.min >= node.value:
                self.min = node.value
                self.mtail.next = mnode
                mnode.prev = self.mtail
                self.mtail = mnode

            # update tail and add node
            curr_tail.next = node
            node.prev = curr_tail
            self.tail = node
        

    def pop(self) -> None:
        curr_tail = self.tail

        # if last node
        if curr_tail.prev is None:
            self.tail = None
            self.min = float("inf")
            self.mtail = None
        else: # has a previous
            #if min was popped off
            if self.mtail.value == curr_tail.value:
                mtail = self.mtail

                if mtail.prev is not None:
                    mtail.prev.next = None

                self.mtail =mtail.prev
                self.min = self.mtail.value
                mtail.prev = None

            curr_tail.prev.next = None
            self.tail = curr_tail.prev




        

    def top(self) -> int:
        return self.tail.value
        

    def getMin(self) -> int:
        return self.mtail.value
        
