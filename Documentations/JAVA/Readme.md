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
### Data Types
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
##### Creating objects from a child class (`super()`)
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
"Hello, " + $STRING
Number is 5
```
- If the hashed line (Marked with $)  was replaced with `super(<STRING>, <INTEGER>);` then the output would be
```
"AGE is < <INTEGER> > 
Number is 5
```

