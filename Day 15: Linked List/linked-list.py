

    def insert(self,head,data): 
    #Complete this method
        if head is None:
            head = Node(data)
            self.tail = head
        else:
            node = Node(data)
            self.tail.next = node
            self.tail = node
        return head
        
