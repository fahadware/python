import time
print("Creating Stack..")
time.sleep(1)
stack=[]
print("Appending elements...")
time.sleep(2)
stack.append(10)
stack.append(11)
stack.append(12)
print("Final stack...")
print(stack)
print("Now removing element from stack...")
time.sleep(2)
while len(stack)>0:
  pop_element=[]
  pop_element=stack.pop()
  print(pop_element)
time.sleep(1)
print("Final empty Stack...")
print(stack)

from collections import deque

queue = deque()
queue.append(10)      # enqueue (add to the back)
queue.append(20)
queue.append(30)

first_item = queue.popleft()   # dequeue - removes and returns the FIRST item (10)
print(first_item)  #10

#lets make linkedlist
class Node:
  def __init__(self,value):
    self.value=value
    self.next=None

node1=Node(10)
node2=Node(11)
node1.next=node2
print(node1.value)
print(node1.next.value)

#brwosing history stack:
history=[]

def visit(page):
  history.append(page)
  print("Visited Pages:",page)
def goback():
  if len(history)>1:
    history.pop()
    print("Back to :",history[-1])
  else:
    print("Now history of visiting pages")
visit("home.com")
visit("products.com")
visit("checkout.com")
goback()
goback()