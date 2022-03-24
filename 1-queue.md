# Introduction

#### Queues are something we are all fimilar with. We Join a queue whenever we get in line and, then there's other people that get in line behind. When we talk about queues in Python programming and even with other langauges adding items in a queue is called **Enqueue** and when we remove items from the queue we call that **Dequeue**. Something to remember is that we **Enqueue** from the back and we **Dequeue** from the Front. We use *FIFO*, First In First Out method with queues. A queue operation uses *BigO (1)*
![Alternate Text to Display](pictures/1.png)
![Alternate Text to Display](pictures/2.png)
![Alternate Text to Display](pictures/3.png)
![Alternate Text to Display](pictures/4.png)



### **Here is an example of using Enqueue:**

#### *Remember that to enqueue uses Big0(1)*

```python
 class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        

my_queue = Queue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)

my_queue.print_queue()
```


## **Here is an example using Dequeue**

``` python
    class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp

 
my_queue = Queue(1)
my_queue.enqueue(2)

# (2) Items - Returns 2 Node
print(my_queue.dequeue())
# (1) Item -  Returns 1 Node
print(my_queue.dequeue())
# (0) Items - Returns None
print(my_queue.dequeue())
```



## Problem to Solve: **Cash Withdrawal at the ATM**

#### They are alot of wanting to withdraw some cash from the ATM at Mountain America Credit Union but this must be done in an orderly manner. These people must be in a single file and give each other time to go to the ATM machine that way they won't be a confusion and people will be served quickly and, they can be able to go and do other things. 

#### Using the following code place these people in a *Queue* and then once everyone has withdrawn their cash the *Queue* should be empty.
##  *Martin, Taona, Seth, Vivian, Takudzwa, Dexter, Pearl* 


```python
 class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp
    
        

my_queue = Queue()


my_queue.print_queue()
```

### Please click this link after you have completed the problem on your own [Solution](solution.py)