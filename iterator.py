#An iterator is an object that lets you traverse
#  through a collection one item at a time, remembering exactly 
# where it left off. Every single for loop you've written 
# so far has been secretly powered by iterators
 #this topic finally reveals that machinery explicitly.
#example
item=[1,2,3,4]
num_iteraotr=iter(item)
print(next(num_iteraotr))
print(next(num_iteraotr))
print(next(num_iteraotr))
print(next(num_iteraotr))

word = "Fahad"
word_iterator = iter(word)
while True:
    try:
        num=next(word_iterator)
        print(num)
    except StopIteration as s:  #after end word iteration will be stop
        print(s)
        break

 #Checking if something is iterable vs. is an iterator
numbers = [1, 2, 3]
print(hasattr(numbers, "__iter__"))    # True - it's iterable
print(hasattr(numbers, "__next__"))    # False - it's NOT itself an iterator

num_iterator = iter(numbers)
print(hasattr(num_iterator, "__next__"))  # True - now it IS an iterator
