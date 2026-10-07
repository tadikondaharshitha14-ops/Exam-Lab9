**Stack and Queue using Type Hints and Dataclasses**

**1. Objective**

To develop a reusable Python package that implements Stack and Queue using Type Hints, Generics, and Dataclasses.

**2. Input**

The program accepts:

* Customer request details
  
* Elements for Stack
  
* Elements for Queue
  
* Stack operations: `push()`, `pop()`, `peek()`
  
* Queue operations: `enqueue()`, `dequeue()`, `front()`

**3. Output**

The program displays:

* Front element of Queue
  
* Dequeued element from Queue
  
* Top element of Stack
  
* Popped element from Stack
  
* Empty Stack/Queue message when applicable

**4. Algorithm**

 Start.
   
 Create a `Request` dataclass to store customer details.
   
 Create a generic Stack class using Type Hints

 Use `push()` to add elements to the Stack.

 Use `pop()` to remove elements from the Stack.
 
 Use `peek()` to view the top element.

 Create a generic Queue class using Type Hints.
 
 Use `enqueue()` to add elements to the Queue.
 
 Use `dequeue()` to remove elements from the Queue.
 
 Use `front()` to view the first element.
 
 Handle empty Stack and Queue conditions.
 
 Display the results.
 
 Stop.

**5. Time and Space Complexity**

**Time Complexity**

Stack:

* Push = O(1)
  
* Pop = O(1)
  
* Peek = O(1)

Queue:

* Enqueue = O(1)
  
* Dequeue = O(n)
  
* Front = O(1)

**Space Complexity**

* Stack = O(n)
* Queue = O(n)
* Overall = O(n)
