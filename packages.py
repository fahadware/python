print("Package")

#A package is a collection of related modules organized together
#  inside a folder. If a module is a single toolbox, a package is an entire cabinet of
#  toolboxes, grouped logically and accessed through a shared folder structure

# my_package/  <-folder
#     __init__.py          <- this will tell pyhton marks this folder as a package
#     module_one.py
#     module_two.py
#     sub_package/
#         __init__.py  #contain code that will run one module is imported...
#         module_three.py

#for example....
#create simple pacage sturcture
#/my_package
   #__init__.py
   #basic_op.py
   #adv_op.py

#basic_op.py
def add(a,b):
    return a+b
#adv_op.py
def power(base,exp):
    return base**exp

# Importing from a package:
#these are just examples to understandd..
from my_package import basic_op
print(basic_ops.add(5, 3))
from my_package import adv_op

# Or import a specific function directly:
from my_package.adv_op import power
print(power(2, 3))

#sub packages nested
# my_project/  ---Folder 1
#     __init__.py
#       data/      --folder 2
#       __init__.py
#       loader.py
#         models/   --folder 3
#       __init__.py
#        neuralner.py
# for import call this
#  from my_project.data import loader
# from my_project.models import neural_net