# Part C: Comparison Document

## 1. 🛠 Assembly Reflections

- What did you notice about registers and instructions?
  - Assembly is a low level language. Registers like eax ebx ecx store the data temporarily.
  - Instructions are very specific and limited and each register does a small and specific task so it takes multiple steps to perform a simple task.
  - There's no automatic management of memory and you have to be careful or you would not be able to identify even the minor mistakes.
- How is coding in Assembly different from Python?
  - Assembly is like telling the computer instructions step by step while python simplifies small tasks by using variables, loops, functions and libraries.
  - Assembly focuses more on micromanagement while python focuses more on problem solving.

## 2. Python Reflections

- Why is Python easier/faster for building the same project?
  - It is a high level language that allows us to code using fewer lines.
  - There is no worry of memory, registers or jumping to addresses manually.
  - Built-in data types and libraries makes simple tasks easier.
  - Debugging is simpler. We can use tools like print() and IDE's to trace errors.
- Which features of Python help abstraction (variables, functions, loops)?
  - **Variables:* We can name things like counter, total and user_input.*
  - **Functions:* It is used to group related code into reusable blocks.*
  - **Loops:* For and while loops allow us to repeat and process lists and actions.*
## 3. Comparison Table


| Feature          | Assembly Example   | Python Example   | Notes                                                                                                                                            |
|------------------|--------------------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Variable Storage | Register (EAX)     | x=5              | In Assembly, variables are stored in CPU registers or memory locations. In Python, they are abstracted as objects stored in memory automatically.|
| Printing Output  | INT 21h            | print()          | In Assembly, printing requires calling system interrupts. Python provides a simple built-in function.                                            |
| Arithmetic       | ADD AX, BX         | x+y              | Assembly works with registers directly. Python abstracts arithmetic into simple operations on variables.                                         |
