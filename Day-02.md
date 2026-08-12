SYS Module 
---

sys module is used to pass the cmd argumnets
sys.argv[0] is always reservd for the program 
sys.argv[1] is the first argument passed to the argumnet.

List in  Python
---
Index is always moved in the forward direction not in reverse unless the step is set to negative
In case negative indeing the first numnber is smaller than the second number other wise you will recive an empty list (postive step size)
step size can never be zero it is default set to +1 
if the list index is set to -1::-1 which mens start is set and end is empty and step is set to -1 then the list will become reverse


List methods mututate the orginal list, alwyas be careful while perfomaing the list operations as they work on orginal list
list methods are append, pop, insert, remove etc.. 
appned: add the element to the end of the list port.append(5000)
insert: add the element at the desired location in a list port.insert(1, 8080)
pop: remove the element from the end of the list port.pop(<index>)
remove: remove the desired element in a list port.remove(5000)
---

Tubles:
---
Immutable sequence and ordered and defiend (). once created their content cannot be chnaged.
Orderd iteam maintain positions
Immutiable cannot add, removee, change after creation
Useful for fixed recoreds like cooredinated, version numbers. 

host_port = ("127.0.0.0", 3000)
red_gb = (255, 0 , 0)
when creating an empty tuple we need add trailing , simple_tuple = (,)


sets:
---
Unordered, Mutuable, unique iteams only 
iteams of a set must be immutuable sets cannot conatins set of list, set of sets, but we can have set of tuples.
Meambership testing using in. 
add() an iteam to a sets
discard() to remove an iteam
remove() to remove an iteam but rises an error in case of element not found.
---
union operations:  | union() combine all the iteams from two sets
Intersection: intersection() or & find common  itemas between two sets 
Difference: difference() or - Find the items in one set and not in other set


items of a set must be immutable (unchangeable) because sets use an underlying mechanism called a hash table to ensure that all stored elements are unique and can be found almost instantly






