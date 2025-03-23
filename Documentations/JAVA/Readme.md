In Java, every function must be inside a class, Let's start by a class Main for now:
```java
public class Main {  
    public static void main(String[] args) {
		System.out.println("Hello and welcome!");
	}
}
```
Like so, this is because Java is an Object-oriented programming language that is structured around classes and objects.
- `main` function is the entry point of any Java application and is mandatory.
# What are Objects
- A reference to a CLASS's object stored in memory.
- Inside that object, we can store variables
```java
public class Student {
    String name;

    // Function (Method)
    public void setName(String newName) {
        name = newName;
    }

    public static void main(String[] args) {
        Student s = new Student();  // No constructor used
        s.setName("Alex");  // Function is manually called
        System.out.println("Student Name: " + s.name);
    }
}
```
***Note:*** Standard practice for object naming is to have lower case letters, and with the same name as the class, while the class starts with an upper case letter `Student student = new Student()`
# Basics
### Access Modifiers
1) `public` 
	Publicly accessible
2) `private` 
	Accessible **only within the class** it is defined in.
3) `default`
	Accessible **only within the same package** (working directory).
4) `protected` 
	Accessible **within the same package**, and **from subclasses** even if they are in **different packages**.
### Functions
##### Printing
Printing Strings has to be inside ***double*** quotation marks.
```java
public class Main {  
    public static void main(String[] args) {
		System.out.println("Hello and welcome!");
		String name = scanner.nextInt(); // Reads only an integer
		tring name = scanner.nextLine(); // Reads the full line until it encounters (\n)
```
##### Inputs
```java
	Scanner scanner = new Scanner(System.in);
```
##### Calling
`<OBJECT>.<FUNCTION>(<INPUT>)`
```java
public class Student {
    String name;

    // Function (Method)
    public void setName(String newName) {
        name = newName;
    }

    public static void main(String[] args) {
        Student student = new Student(); // Created object "student" No constructor used
        student.setName("Alex");  // Function is manually called
        System.out.println("Student Name: " + student.name);
    }
}
```
##### Returning
```java
	int getId(){
		return id;
	}
```
### Variables
##### Defining variables
```java
public class Student {  
    String name01; // Declared 
    
    public void function01 (String newName) {
        name01 = newName; // No need for variable declaration
        String name02 = newName; // needed variable declaration
    }
    
    public void function02(String newName) {
        String name02 = newName; // STILL needed variable declaration
    }
}
```
##### Strings
```java
	String var01 = "Alex";
	System.out.println("Name is " + var01);
```
##### Integers
```java
	int var02 = 23;
	System.out.println("Age is " + var02);
```
- `int` data type has an `Integer.MAX_VALUE` & an `Integer.MIN_VALUE` value. "2147483647 & -2147483648"
- Over flowing of max values goes to negative value, and vice versa
##### Float & doubles
```java
	float var02 = 23.55;
	System.out.println("Score is " + var02);
```
##### Boolean
```java
	boolean var02 = true;
	System.out.println("Answer is " + var02);
```
##### Strings to integers
```java
	newNumber = "10"
	x = Integer.parseInt(newNumber)
```
##### <this.VAR>
When a **local variable (parameter)** has the **same name** as an **instance variable**, the local variable **hides** the instance variable.
- The keyword `this` refers to the **current object’s instance variable**, helping differentiate between the two.
```java
public class Student {
    int id;  // Instance variable

    public Function01 (int id) {
        this.id = id;  // Assign parameter to instance variable
    }
}
```

### Constructors
A **constructor** in Java is a special method used to initialize objects. It has the same name as the class and does not have a return type. Constructors are automatically called when an object of a class is created. 
- Similar to a function, but with no return data. "No `void` or `int` before its name"
- Must have the same name as the class
Java provides two types of constructors:
##### 1) Default Constructor
- Created implicitly if no constructor is defined. It initializes object properties with default values.
- It's also the constructor with no inputs.
```java
public class Custom {
    int x = 2;
    public Custom() {  
        System.out.println("Number is " + x);  
    }  
}
// ------
public class Main {
    public static void main(String[] args) {
        Custom obj = new Custom(); // Calls the printed line
    }
}
```
##### 2) Parameterized Constructor
- Allows passing arguments to initialize object properties with custom values.
- If existed, it will function as the default constructor.
```java
public class Custom {  
    int x;  
    public Custom(String newNumber) {  
        x = Integer.parseInt(newNumber);  
        System.out.println("Value of x: " + x);  
    }  
}
// ----
public class Main {  
    public static void main(String[] args) {  
        Custom obj = new Custom("10");  // Calls the printed line with the given argument "10"
    }  
}
```
##### Difference between Constructors & Functions
| Feature           | Constructor                                                              | Function (Method)                                                        |
| ----------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| **Definition**    | Special method used to initialize objects.                               | Block of code that performs a task when called.                          |
| **Name**          | Must have the **same name** as the class.                                | Can have **any name**.                                                   |
| **Return Type**   | **No return type**, not even `void`.                                     | Can return a value (e.g., `int`, `String`, `void`).                      |
| **Invocation**    | Called **automatically** when an object is created.                      | Called **manually** by using its name.                                   |
| **Purpose**       | Initializes object properties.                                           | Performs specific operations or computations.                            |
| **Overloading**   | Can be **overloaded** (multiple constructors with different parameters). | Can also be **overloaded** (multiple methods with different parameters). |
| **Explicit Call** | Cannot be called explicitly like a normal function.                      | Must be called explicitly when needed.                                   |
##### Multiple Constructors
When a class has **multiple constructors**, Java selects the constructor based on the **type and number of arguments** provided when creating an object. This is called **constructor overloading**.
```java
public class Student {
    String name; 
    int age;
    // Constructor 1 - No parameters
    public Student() {
        String name = "Unknown";
        int age = 0;
    }

    // Constructor 2 - One parameter (String)
    public Student(String newName) {
        name = newName;
        age = 0;
    }

    // Constructor 3 - Two parameters (String, int)
    public Student(String newName, int newAge) {
        name = newName;
        age = newAge;
    }

    public static void main(String[] args) {
        Student s1 = new Student();               // Calls Constructor 1
        Student s2 = new Student("Alex");         // Calls Constructor 2
        Student s3 = new Student("Sara", 22);     // Calls Constructor 3

        System.out.println(s1.name + ", " + s1.age);  // Output: Unknown, 0
        System.out.println(s2.name + ", " + s2.age);  // Output: Alex, 0
        System.out.println(s3.name + ", " + s3.age);  // Output: Sara, 22
    }
}
```
# OOP - Dealing with objects & Classes
### Inheritance
Allows a **child class** (subclass) to acquire properties and behaviors from a **parent class** (superclass). This helps in code **reuse**, **extensibility**, and **maintainability**.  A class inherits from another class using the `extends` keyword.
```java
class Parent {
    void show() {
        System.out.println("This is the parent class.");
    }
}
class Child extends Parent {
    void display() {
        System.out.println("This is the child class.");
    }
}

public class Main {
    public static void main(String[] args) {
        Child obj = new Child();
        obj.show();    // Inherited method
        obj.display(); // Own method
    }
}
```
- **Java does NOT support Multiple Inheritance** for one child
- A better approach for this is **Multilevel Inheritance**: A child class inherits from another child class.
- Multiple classes can inherit from the same parent. (**Hierarchical Inheritance**).
### Creating objects from a child class (`super()`)
- Upon creating an object from a class inheriting another class, the ***default constructor*** of the parent is inherited as well
- Thus upon creating an object from the child class the default constructor of the parent is executed first, **then** the default constructor of the child class.
- **Remember:** in case of no constructor, a default constructor is created implicitly with no outputs, showing nothing in the output screen
```java
class Parent {
    // Default constructor of the parent class
    Parent() {
        System.out.println("Parent class constructor");
    }
}
class Child extends Parent {
    // Default constructor of the child class
    Child() {
        System.out.println("Child class constructor");
    }
}

public class Main {
    public static void main(String[] args) {
        // Creating an object from the child class
        Child obj = new Child();
    }
}


// OUTPUT :
// Parent class constructor  
// Child class constructor 
```

- The `super()` keyword in Java is used to **refer to the parent class** (also called the superclass). It is commonly used in **inheritance** to access the **parent class’s methods, variables, or constructors**.
- it is **implicitly called** at the beginning of the child constructor

- If the **parent class** has a **parameterized constructor** **without** a **default constructor**, the **child class constructor** will fail because it implicitly tries to call the **unexisting default constructor** of the parent ❎

```java
class Parent {
    Parent(String name) {
        System.out.println("Hello, " + name);
    }
}
class Child extends Parent {
    Child() {
        super();  // Sending a call to parent default constructor (ERROR)
        System.out.println("Child class constructor");
    }
}

public class Main {
    public static void main(String[] args) {
        Child obj = new Child();
    }
}


//  ERROR (CAN'T FIND PARENT DEFAULT CONSTRUCTOR)
```

- Adding a default constructor will call it and ignore the desired existing one.
```java
class Parent {
    Parent() {
        System.out.println("Default Parent constructor");
    }

    Parent(String name) {
        System.out.println("Hello, " + name);
    }
}
class Child extends Parent {
    Child() {
        super();  // Sending a call to parent default constructor (Ignoring the desired one)
        System.out.println("Child class constructor");
    }
}

public class Main {
    public static void main(String[] args) {
        Child obj = new Child();
    }
}


// OUTPUT :
// Default Parent constructor 
// Child class constructor  
```

- Simply editing the `super()` keyword to call the **desired constructor** would fix the issue ✅
```java
class Parent {
	// No default constructor, no change if it existed (ignored as we called a specific constructor)
    Parent(String name) {
        System.out.println("Hello, " + name);
    }
}
class Child extends Parent {
    Child() {
        super("Alex");  // Explicitly call the desired parent constructor
        System.out.println("Child class constructor");
    }
}

public class Main {
    public static void main(String[] args) {
        Child obj = new Child();
    }
}


// OUTPUT :
// Hello, Alex  
// Child class constructor  
```

***Example For better understanding;***
```java
class Parent {
	Parent() {
        System.out.println("Default Parent constructor");
    }
    Parent(String name) {
        System.out.println("Hello, " + name);
    }
    Parent(String age, int x) {
        System.out.println("AGE is " + x);
    }
}
class Child extends Parent {
    Child() {
        super("Alex");  // Explicitly call the desired parent constructor
        System.out.println("Child class constructor");
    }
    Child(int z) {
   // $ super();   // Created implicitly
	    System.out.println("Number is " + z);
    }
}

public class Main {
    public static void main(String[] args) {
        Child obj = new Child(5);
    }
}

// OUTPUT :
// Default Parent constructor
// Number is 5
```
- In the previous example, the parameterized constructor of the class `Child` was called; as it had a superclass, the constructor of the superclass called in `super` was initiated first.
- No mentioning of `super` in the called `Child` Constructor resulted in implicitly creating a default `super();` calling the default instructor
- If the hashed line (Marked with $)  was replaced with `super(<STRING>);` then the output would be:
```
Hello, $STRING
Number is 5
```
- If the hashed line (Marked with $)  was replaced with `super(<STRING>, <INTEGER>);` then the output would be
```
AGE is $INTEGER
Number is 5
```

### Overwriting an inherited function
When a **child class** has a method with the **same name and parameters** as a method in the **parent class**, the **child method overrides** the **parent method**.
- Can be used to **provide a specific implementation** in the child class.
- The **access modifier** of the **overriding method** cannot be **more restrictive** than the **parent method**.
- The **`@Override` annotation** is optional but recommended to **indicate the intention**.
```java
class Parent {
    void show() {
        System.out.println("Parent method");
    }
}
class Child extends Parent {
    @Override
    void show() {
        System.out.println("Child method");
    }
}

public class Main {
    public static void main(String[] args) {
        Child obj = new Child();
        obj.show();  // Calls the overridden method in the child class
    }
}

// OUTPUT :
// Child method
```
- If both methods are required, we can use `super().<METHOD_NAME>;` to call the parent method.
```java
class Parent {
    void show() {
        System.out.println("Parent method");
    }
}

class Child extends Parent {
    @Override
    void show() {
        super.show();  // Calls the parent method
        System.out.println("Child method");
    }
}

public class Main {
    public static void main(String[] args) {
        Child obj = new Child();
        obj.show();
    }
}

// OUTPUT :
// Parent method
// Child method
```
### Final Classes (Prohibiting Inheritance)
A **final class** is a class that **cannot be extended (inherited)** by any other class.
```java
final class DBConnection {
    void connect() {
        System.out.println("Connecting to DB");
    }
}

// If we tried creating a child class from this class like so, Code exits with an error (Cannot inherit from final class)

// class extends CustomConnection {}  
```
### Final Methods (Prohibiting Overwriting) 
A **final method** is a method that **cannot be overridden** by any **subclass**.
```java
class DBConnection {
    final void connect() {
        System.out.println("Connecting to DB");
    }
}

class CustomConnection extends DBConnection {
//     If we tried overwriting the method like so, Code exits with an error (cannot overwrite a final method)
//     void connect() {
//         System.out.println("Trying to override the connection");
//     }
}
```

### Abstract Methods & Abstract Classes
An **abstract method** is a method that **does not have a body** (no implementation) and is meant to be **overridden** in **subclasses**.
- The **class containing an abstract method** must also be declared as **abstract**
- You **cannot create objects** from an **abstract class**. 
- **Subclasses** that **inherit** an abstract class **must implement** all **abstract methods**, or they will also be considered **abstract**.
```java
abstract class Class {
    abstract void fun01();  // Abstract method with no body or curled brackets
    void fun02() {  
    System.out.println("Text");  // normal method
	}
}
```

### Static
The keyword `static` members are shared among all objects of that class, and its purpose is to make members belong to the class itself.
#### Static Variables
- Shared among all instances of the class.
- Only one copy in the memory exists regardless of how many objects are created.
- All objects **share the same static variable**.
- Accessed using the **class name** rather than an object.

```java
class Counter {
    static int count = 0;  // Variable not reset for each object
    Counter() {
        count++;
        System.out.println("Count: " + count);
    }
}
public class Main {
    public static void main(String[] args) {
        new Counter();                     // Count: 1
        new Counter();                     // Count: 2
        new Counter();                     // Count: 3
        Counter counter4 = new Counter();  // Count: 4
        Counter counter5 = new Counter();  // Count: 5
        Counter counter6 = new Counter();  // Count: 6
    }
}


// Output: 
// Count: 1
// Count: 2
// Count: 3
// Count: 4
// Count: 5
// Count: 6
```
***Note:*** Variables are **static final** by default
#### Static Methods
- Can be called **without creating an instance** of the class.
- Commonly used for **utility or helper methods**.
- Accessed using the **class name** rather than an object.
- Static methods **can't be overwritten**.
- They can **NOT be inherited**.
```java
class Math {
    static int add(int a, int b) {
        return a + b;
    }
}

public class Main {  
    public static void main(String[] args) {  
        System.out.println("Sum: " +Math.add(5, 3));   // No object creation needed  
    }  
}


// Output: 
// Sum: 8
```

### Interface Classes 
An **interface Class** contains **abstract methods** (methods without a body) and **constants**.
- An interface **cannot contain method implementations** (only **method signatures**).
- You **cannot create objects** from an **interface class**. 
- Methods in an interface are **public and abstract** by default (no need for specifying).
- Fields in an interface are **public**, **static**, and **final** by default.
- A **class implements an interface** using the **`implements`** keyword, and **it must override all interface class methods**.
- When a class overrides an interface method, it has to be declared `public`
- A class can **implement multiple interfaces**.
```java
interface Printable {
    void print();     // Methods are public abstract by default
}
interface Showable {
    void show();      // Methods are public abstract by default
    int MAX_READERS = 10;  // Fields are public static final by default
}

class Document implements Printable, Showable {
    public void print() {
        System.out.println("Printing the document...");
    }
    public void show() {
        System.out.println("Showing the document...");
    }
}

public class Main {
    public static void main(String[] args) {
        Document doc = new Document();
        doc.print();
        doc.show();
        System.out.println("Max Connections: " + Showable.MAX_READERS);  // Output: 10
        
//     If we tried overwriting the field like so, Code exits with an error (cannot assign a value to final variable)
//     Config.MAX_READERS = 20;
    }
}

// Output: 
// Printing the document...
// Showing the document...
// Max Connections: 10
```
***Notes:*** 
Interface Classes have methods that are public abstract by default (no specifications), however, it may have static functions for **utility** or **helper methods** that are related to the interface itself, not to any instance of a class that implements it.
- We can change the default `public abstract` methods to be `default` to act as regular methods, with the ability to be inherited or overwritten, and to have implementation.
#### Using Interfaces with Multiple Implementations (Interface referencing when creating an object)
In case of creating objects for multiple classes implementing the same interface, we can refer to the name of the interface name:
`java <InterfaceName> <objectName> = new <ClassName>();`
- This is useful when multiple classes implement the **same interface**.
- By referencing the object as an **interface type**, we gain flexibility in swapping out implementations without changing the code structure.
- When creating an object, the object have access to methods and variables from the member which created it (Class or interface)
```java
interface AnimalSounds {  
    void sound();  
}  
  
class Dog implements AnimalSounds {  
    public void sound() {  
        System.out.println("Bark");  
    }  
    public void name() {  
        System.out.println("Dog");  
    }  
}  
class Cat implements AnimalSounds {  
    public void sound() {  
        System.out.println("Meow");  
    }  
    public void name() {  
        System.out.println("Cat");  
    }  
}

public class Main {  
    public static void main(String[] args) {  
        Dog dogObj = new Dog();  
        AnimalSounds catObj = new Cat();  
  
        dogObj.sound();  
        dogObj.name();  // Objects call methods in the class  
  
        catObj.sound();  // Objects call methods in the interface on
    }  
}

// Output: 
// Bark
// Dog
// Meow
```

# Data Structures
### Map
- Stores **key-value pairs**
- Keys are **unique**
- Has 3 types of implementations, **HashMap**, **TreeMap**, or **LinkedHashMap**.
#### HashMap
- **No guaranteed order** of keys.
- Allows one **null key** and multiple **null values**.
- **Not synchronized** (not thread-safe).
```java
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        Map<String, Integer> hashMap = new HashMap<>();
        hashMap.put("Apple", 1);
        hashMap.put("Banana", 2);

        System.out.println("HashMap: " + hashMap);
    }
}
```
#### LinkedHashMap
- Maintains **insertion order** or **access order**.
- **Slower than HashMap** but maintains **insertion order** (Important for caching).
```java
import java.util.LinkedHashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        Map<String, Integer> linkedHashMap = new LinkedHashMap<>();
        linkedHashMap.put("First", 10);
        linkedHashMap.put("Second", 20);


        System.out.println("LinkedHashMap: " + linkedHashMap);
    }
}
```
#### TreeMap
- Maintains **natural ordering** or **custom comparator** ordering.
- **Slower than HashMap** but **sorted** (Natural or custom sorting).
```java
import java.util.TreeMap;
import java.util.Comparator;

public class Main {
    public static void main(String[] args) {
        TreeMap<String, Integer> map = new TreeMap<>();
        map.put("Banana", 3);
        map.put("Apple", 5);
        map.put("Cherry", 2);
        
        System.out.println("TreeMap: " + map); //  (Comparator.reverseOrder()) is an example of custom sorting
    }
}

// // The Output will be sorted
// OUTPUT:
// TreeMap: {Apple=5, Banana=3, Cherry=2}
```
#### ConcurrentHashMap
- Does **not allow null keys or values**.
```java
import java.util.concurrent.ConcurrentHashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        Map<String, Integer> concurrentMap = new ConcurrentHashMap<>();
        concurrentMap.put("User1", 100);
        concurrentMap.put("User2", 200);


        // Printing the map contents
        for (String key : concurrentMap.keySet()) {
            System.out.println("Key: " + key + ", Value: " + concurrentMap.get(key));
        }
    }
}

```
#### IdentityHashMap
- Suitable for scenarios where **reference equality** is needed.
- Same keys with different values are treated as different because of reference comparison
```java
import java.util.IdentityHashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        Map<String, Integer> identityMap = new IdentityHashMap<>();
        identityMap.put(new String("A"), 1);
        identityMap.put(new String("A"), 2);


        // Printing the map to show both keys exist
        System.out.println("Map size: " + identityMap.size());
        for (String key : identityMap.keySet()) {
            System.out.println("Key: " + key + ", Value: " + identityMap.get(key));
        }
    }
}
// Both keys are treated as different because of reference comparison
```

### Set
- No Duplicate Elements
- No Indexing
- No ordering (Except for (e.g., `LinkedHashSet` and `TreeSet`)
```java
Set<String> names = new HashSet<>();
names.add("Alice");
names.add("Bob");
names.add("Alice");  // Duplicate, will be ignored
System.out.println(names);  // Output: [Alice, Bob]

```
### Fixed Array
- Has a **predefined size** that cannot change after initialization.
- Stores elements in **contiguous memory locations**.
```java
public class Main {
    public static void main(String[] args) {
        int[] numbers = new int[5];  // Creates an array of size 5

        // Initializing array elements
        numbers[0] = 10;
        numbers[1] = 20;
        numbers[2] = 30;
        numbers[3] = 40;
        numbers[4] = 50;
        // You cannot directly add elements to an array after initialization.

        // Printing array elements
        for (int i = 0; i < numbers.length; i++) {
            System.out.println("Element at index " + i + ": " + numbers[i]);
        }
    }
}
```
#### Dynamic Array
- Similar to a fixed array but can **grow or shrink in size** during runtime.
```java
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
	// list.add(index, element);
        list.add(10); // added to the end of the list
        list.add(2,20); // added to third item of index 2 of the list (shift the existing element to the right)

        System.out.println("List elements: " + list);  // Output: [10, 20]
    }
}
```
#### Queue
- A queue is a **First In, First Out (FIFO)** data structure.
- Operations include **enqueue** (add) and **dequeue** (remove).
- Efficient operations at both ends.
```java
import java.util.Queue;  
import java.util.LinkedList;  
  
public class Main {  
    public static void main(String[] args) {  
        Queue<String> queue = new LinkedList<>();  
        queue.add("Alice");  
        queue.add("Bob");  
  
        String first = queue.remove();  // Removes and returns "Alice"  
        System.out.println("First element removed: " + first);  // Alice  
        System.out.println("Queue after removal: " + queue);    // [Bob]  
    }
```
### Stack
- A stack is a **Last In, First Out (LIFO)** data structure.
- Elements are **pushed** onto the top and **popped** from the top.
- Useful for **function call management**, **undo mechanisms**, and **expression evaluation**.
- **Operations:**
	- **Push:** Add an element to the top of the stack.
	- **Pop:** Remove and return the element at the top.
	- **Peek/Top:** View the top element without removing it.
	- **IsEmpty:** Check if the stack is empty.
	- **Size:** Get the number of elements in the stack.
```java
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();
        stack.push(5);
        stack.push(10);
        int top = stack.pop();  // Removes and returns 10

        System.out.println("Top element removed: " + top);  // 10
        System.out.println("Current stack: " + stack);      // [5]
    }
}
```
Another example:
```java
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Stack<String> stack = new Stack<>();

        // Push elements onto the stack
        stack.push("Apple");
        stack.push("Banana");
        stack.push("Cherry");

        // Peek at the top element
        System.out.println("Top element: " + stack.peek());  // Cherry

        // Pop an element from the stack
        System.out.println("Popped: " + stack.pop());  // Cherry

        // Check the size after popping
        System.out.println("Size after pop: " + stack.size());  // 2

        // Check if the stack is empty
        System.out.println("Is empty: " + stack.isEmpty());  // false

        // Print remaining elements
        System.out.println("Stack: " + stack);  // [Apple, Banana]
    }
}

// OUTPUT:
// Top element: Cherry
// Popped: Cherry
// Size after pop: 2
// Is empty: false
// Stack: [Apple, Banana]
```
#### Deque (Double-Ended Queue)
- Supports insertion and Deletion from Both Ends
- Supports Both Stack and Queue Operations
- No Capacity Restrictions
- **Flexible Operations** and better performance (Can function as a **queue** or **stack**.)
- Has two types:
	- **Input-Restricted Deque**: Insertion is allowed at one end only, but deletion can occur from both ends. 
	- **Output-Restricted Deque**: Deletion is allowed at one end only, but insertion can occur from both ends.
```java
import java.util.Deque;
import java.util.ArrayDeque;

public class Main {
    public static void main(String[] args) {
        Deque<String> deque = new ArrayDeque<>();

        // Adding elements to the front and rear
        deque.addFirst("Alice");
        deque.addLast("Bob");
        deque.addFirst("Eve");

        // Printing the deque
        System.out.println("Deque: " + deque);  // [Eve, Alice, Bob]

        // Accessing elements
        System.out.println("First: " + deque.getFirst());  // Eve
        System.out.println("Last: " + deque.getLast());    // Bob

        // Removing elements from both ends
        deque.removeFirst();  // Removes "Eve"
        deque.removeLast();   // Removes "Bob"
        
        System.out.println("Deque after removal: " + deque);  // [Alice]

        // Stack operation
        deque.push("Charlie");
        deque.push("David");
        System.out.println("Stack mode: " + deque);  // [David, Charlie, Alice]

        // Queue operation
        deque.addLast("Eve");
        System.out.println("Queue mode: " + deque);  // [David, Charlie, Alice, Eve]

        // Popping elements (like stack)
        System.out.println("Popped: " + deque.pop());  // David
        System.out.println("After pop: " + deque);     // [Charlie, Alice, Eve]
    }
}
```
***Note:*** `Stack` is considered **legacy** in Java. The recommended approach is to use `Deque` when you need stack-like behavior.
#### Linked Lists
- A linked list is a **sequential data structure** where each element, known as a **node**, points to the next node.
- Nodes contain **data** and a **reference to the next node**.
- No contiguous memory allocation, unlike arrays.
- Suitable for **dynamic data management** and **frequent insertions/deletions**.
```java
class Node {
    int data;      // Holds the value of the node
    Node next;     // Reference to the next node in the linked list

    // Constructor to initialize the node with data
    Node(int data) {
        this.data = data;
        this.next = null;  // By default, the next node is null
    }
}
```

### Hierarchy of Collection Framework
The following shows an overview of Java collection, from which we can see the different interfaces and classes 
- We can't instantiate an interface.
- When Creating an object we can only instantiate an instance from a class.
- If an interface is required, we can instantiate a class implementing the instance.
![Pasted image 20250322125147](https://github.com/user-attachments/assets/128045f5-03b9-4748-ac61-02dd5b98f8fd)
# Design Patterns
### Singleton Pattern
- Ensures that only one instance of the class is created.
- The class has a `private` constructor and `private static` object
- **Static Instance Variable:** Holds the single instance of the class.
```java
public class Class01 {   
    private String name;  
    public void setName(String name) {  
        this.name = name;  
    }  
    public String getName() {  
        return name;  
    }  

	// static object
    private static Class01 obj;  
    private Class01() {  }
    public static Class01 createObject(){  
        if (obj == null) {  
            obj = new Class01();  
            return obj;  
        }  
        return obj;  
    }
}
```

- The previous class has a private default constructor, thus preventing the creation of any objects.
- The static method `createObject` is used to create objects without creating an instance of the class.
- Last object created from the method will overwrite the static object `obj`.
```java
public class Main {  
    public static void main(String[] args) {  
        Class01 obj1 = Class01.createObject();  
        obj1.setName("A");  
        System.out.println(obj1.getName());  
        
	 // Overwriting the object
        Class01 obj2 = Class01.createObject();  
        obj2.setName("B");  
	 // Testing the two objects
        System.out.println(obj1.getName());  
        System.out.println(obj2.getName());  
  
    }  
}

// OUTPUT:
// AA
// BB
// BB
```

### IOC (Inversion of control)
- A design principle used to reduce tight coupling between components.
- The controller does not create instances of dependent services directly. Instead, the controller receives the service through an external source (like a constructor).
- To simplify, if we have multiple implementations for an interface, we can create a new class to control the usage of the implementing classes.
```java
public interface Interface01 {
    void performAction();
}
// --------------------------
public class Class01Service implements Interface01 {
    @Override
    public void performAction() {
        System.out.println("Performing action in Class01Service");
    }
}

public class Class02Service implements Interface01 {
    @Override
    public void performAction() {
        System.out.println("Performing action in Class02Service");
    }
}

public class Class03Service implements Interface01 {
    @Override
    public void performAction() {
        System.out.println("Performing action in Class03Service");
    }
}

// --------------------------
public class MyController {
    private Interface01 interface01;

	// Instead of tightly coupling the controller to a specific service class, we make it flexible by accepting any implementation of MyService. 
    public MyController(Interface01 interface01) {      // ---> Parameterized Constructor
        this.interface01 = interface01;
    }

    public void execute() {
        interface01.performAction();
    }
}
// --------------------------

public class Main {
    public static void main(String[] args) {
       
		// Create the controller and pass the desired service
        MyController controller = new MyController(new Class01Service());
        controller.execute();


        // Change the service without modifying the controller
        controller = new MyController(new Class02Service());
        controller.execute();

        controller = new MyController(new Class03Service());
        controller.execute();
    }
}


// OUTPUT
// Performing action in Class01Service
// Performing action in Class02Service
// Performing action in Class03Service
```

