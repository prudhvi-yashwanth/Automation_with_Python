# Python - `for` Loop, `while` Loop, `break`, and `continue`

## 1. `for` Loop

A `for` loop is used to iterate over an **iterable** such as:

- List
- Tuple
- String
- Set
- Dictionary
- `range()`

### Syntax

```python
for var in iterator:
    print(var)
```

The loop takes one item at a time from the iterable and executes the block of code.

---

# 2. Loop Through a List

```python
servers = ["web01", "web02", "DB01"]

for server in servers:
    print("Pinging server:", server)
```

Output:

```text
Pinging server: web01
Pinging server: web02
Pinging server: DB01
```

Here:

```python
server
```

holds one item from the list in each iteration.

```text
servers
   │
   ├── web01 → server = web01
   ├── web02 → server = web02
   └── DB01  → server = DB01
```

> **Correction:** `"Pining"` was corrected to `"Pinging"`.

---

# 3. Using `range()`

The `range()` function generates a sequence of numbers.

Example:

```python
for index in range(10):
    print(f"Server {index}")
```

Output:

```text
Server 0
Server 1
Server 2
Server 3
Server 4
Server 5
Server 6
Server 7
Server 8
Server 9
```

### Important

```python
range(10)
```

generates:

```text
0 1 2 3 4 5 6 7 8 9
```

The ending value `10` is **not included**.

---

# 4. `for` vs `while`

## `for` Loop

A `for` loop is commonly used when:

- You want to iterate over a known collection.
- You want to repeat something over a range.
- The iterable itself determines when the loop ends.

Example:

```python
servers = ["web01", "web02", "DB01"]

for server in servers:
    print(server)
```

The loop stops automatically after all items have been processed.

> **Important:** A `for` loop does not always mean that you know the exact number of iterations in advance. For example, you can loop over a file or generator whose size is not known beforehand.

---

## `while` Loop

A `while` loop repeats the block of code **as long as the condition remains `True`**.

Example:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```text
1
2
3
4
5
```

A `while` loop is useful when the number of iterations depends on a condition and is not known in advance.

### Real-Time Example

```python
while server_is_ready:
    check_status()
```

The loop continues until:

```python
server_is_ready
```

becomes `False`.

---

# 5. `break`

The `break` statement **immediately exits the innermost loop**.

It is useful when you have already found what you need and do not want to continue the loop.

### Example

```python
servers = ["web01", "web02", "DB01", "web03"]

for server in servers:
    if server == "DB01":
        print("Database server found")
        break

    print("Checking:", server)
```

Output:

```text
Checking: web01
Checking: web02
Database server found
```

The loop stops as soon as `DB01` is found.

---

# 6. `continue`

The `continue` statement **skips the current iteration** and moves to the next iteration of the loop.

### Example

```python
servers = ["web01", "DB01", "web02", "DB02"]

for server in servers:
    if server.startswith("DB"):
        continue

    print("Checking web server:", server)
```

Output:

```text
Checking web server: web01
Checking web server: web02
```

When the loop finds a database server, `continue` skips that iteration.

---

# `break` vs `continue`

| Keyword | Purpose |
|---------|---------|
| `break` | Completely exits the loop |
| `continue` | Skips the current iteration and continues with the next one |

### Easy Way to Remember

```text
break
  ↓
STOP THE LOOP

continue
  ↓
SKIP THIS ITERATION
```

---

# 7. Real-Time DevOps Example

Suppose you have a list of servers and want to find the first server that is down.

```python
servers = ["web01", "web02", "DB01", "web03"]

for server in servers:
    print(f"Checking {server}...")

    if server == "DB01":
        print(f"{server} is down")
        break
```

Once the problematic server is found:

```python
break
```

stops further checking.

---

# 8. Another Example Using `continue`

Suppose you want to skip database servers and check only web servers:

```python
servers = ["web01", "DB01", "web02", "DB02"]

for server in servers:
    if server.startswith("DB"):
        continue

    print(f"Checking {server}")
```

Output:

```text
Checking web01
Checking web02
```

---

# Quick Revision

```text
for
→ Iterates over an iterable

range()
→ Generates a sequence of numbers

while
→ Repeats while a condition is True

break
→ Immediately exits the loop

continue
→ Skips the current iteration
```

---

# Interview Answer

> **"A `for` loop is mainly used to iterate over an iterable such as a list, tuple, string, or range. A `while` loop is used when execution should continue as long as a condition is true, especially when the number of iterations is not known in advance. `break` immediately exits the current loop, while `continue` skips the current iteration and moves to the next one."**


# Python - List, Set, and Dictionary Comprehensions

## What is Comprehension?

A **comprehension** is a shorter and cleaner way to create a new collection from an existing iterable.

The common types are:

- List Comprehension
- Set Comprehension
- Dictionary Comprehension

Comprehensions are useful when the logic is simple and easy to understand.

---

# 1. List Comprehension

### Basic Syntax

```python
[expression for item in iterable]
```

Example:

```python
numbers = [1, 2, 3, 4]
doubled_numbers = [num * 2 for num in numbers]

print(doubled_numbers)
```

Output:

```text
[2, 4, 6, 8]
```

---

# 2. Traditional `for` Loop vs List Comprehension

## Traditional Approach

```python
old_items = [1, 2, 3, 4]

doubled_items = []

for item in old_items:
    doubled_items.append(item * 2)

print(doubled_items)
```

Output:

```text
[2, 4, 6, 8]
```

## Using List Comprehension

```python
old_items = [1, 2, 3, 4]

doubled_items = [item * 2 for item in old_items]

print(doubled_items)
```

Output:

```text
[2, 4, 6, 8]
```

The comprehension does the same work in one line.

---

# 3. How List Comprehension Works

Consider:

```python
[item * 2 for item in old_items]
```

Read it as:

> For every `item` in `old_items`, multiply the item by `2` and put the result into a new list.

Flow:

```text
old_items
    │
    ▼
Take one item
    │
    ▼
item * 2
    │
    ▼
Add result to new list
    │
    ▼
Repeat for all items
```

---

# 4. Filtering with List Comprehension

You can add a condition to filter the values.

### Syntax

```python
[expression for item in iterable if condition]
```

Example:

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [
    num for num in numbers
    if num % 2 == 0
]

print(even_numbers)
```

Output:

```text
[2, 4, 6]
```

The condition:

```python
num % 2 == 0
```

checks whether the number is even.

---

# 5. List Comprehension Execution Order

For:

```python
[num for num in numbers if num % 2 == 0]
```

the basic flow is:

```text
for num in numbers
       │
       ▼
Check if condition is true
       │
       ├── False → Skip item
       │
       └── True
            │
            ▼
          Add num
```

This is different from a ternary expression, where the `if/else` decides the value to produce.

---

# 6. Set Comprehension

A **set comprehension** creates a set instead of a list.

### Syntax

```python
{expression for item in iterable}
```

Example:

```python
numbers = [1, 2, 2, 3, 4]

unique_squares = {num * num for num in numbers}

print(unique_squares)
```

Output contains unique squared values:

```text
{1, 4, 9, 16}
```

The duplicate input value `2` produces the same square `4`, and the set keeps only one `4`.

> **Important:** Sets are unordered, so do not depend on the displayed order of the result.

---

# 7. Dictionary Comprehension

A **dictionary comprehension** creates a dictionary using a key-value expression.

### Syntax

```python
{key: value for item in iterable}
```

Example:

```python
servers = ["web", "backend"]

server_ips = {
    server: f"192.168.1.{i}"
    for i, server in enumerate(servers)
}

print(server_ips)
```

Output:

```text
{
    'web': '192.168.1.0',
    'backend': '192.168.1.1'
}
```

> **Correction:** The original code used `enumurate`. The correct function name is `enumerate()`.

---

# 8. `enumerate()`

The `enumerate()` function gives both:

- Index
- Value

Example:

```python
servers = ["web", "backend"]

for i, server in enumerate(servers):
    print(i, server)
```

Output:

```text
0 web
1 backend
```

---

# 9. Start `enumerate()` from a Custom Index

By default, the index starts from `0`.

You can change the starting number:

```python
servers = ["web", "backend"]

for i, server in enumerate(servers, start=10):
    print(i, server)
```

Output:

```text
10 web
11 backend
```

### Syntax

```python
enumerate(iterable, start=0)
```

Example:

```python
enumerate(servers, start=10)
```

starts counting from `10`.

> **Correction:** `enumerate()` is a function that accepts the iterable and an optional `start` value. The default is `0`.

---

# 10. Ternary Operator

Python provides a conditional expression, commonly called the **ternary operator**.

### Syntax

```python
value_if_true if condition else value_if_false
```

Example:

```python
result = "PASS" if num >= 8 else "FAIL"
```

Meaning:

```text
If num >= 8
    → PASS
Otherwise
    → FAIL
```

---

# 11. Ternary Expression Inside a List Comprehension

Example:

```python
numbers = [5, 8, 10, 6, 9]

categories = [
    "PASS" if num >= 8 else "FAIL"
    for num in numbers
]

print(categories)
```

Output:

```text
['FAIL', 'PASS', 'PASS', 'FAIL', 'PASS']
```

Here:

```python
"PASS" if num >= 8 else "FAIL"
```

decides **what value should be added to the new list**.

---

# 12. Ternary Expression with Filtering

You can combine:

- `if/else` to decide the output value
- A final `if` to filter which items are included

Example:

```python
numbers = [5, 8, 10, 6, 9]

categories = [
    "PASS" if num >= 8 else "FAIL"
    for num in numbers
    if num % 2 == 0
]

print(categories)
```

Output:

```text
['PASS', 'PASS', 'FAIL']
```

---

# 13. Understand the Execution Order

This syntax can be confusing:

```python
[
    "PASS" if num >= 8 else "FAIL"
    for num in numbers
    if num % 2 == 0
]
```

The easiest way to understand it is as a normal loop:

```python
categories = []

for num in numbers:
    if num % 2 == 0:
        if num >= 8:
            categories.append("PASS")
        else:
            categories.append("FAIL")
```

So the **filtering condition**:

```python
if num % 2 == 0
```

determines whether the item is included.

Only for included items do we evaluate:

```python
"PASS" if num >= 8 else "FAIL"
```

Therefore, the final filtering `if` is conceptually applied before adding the result.

---

# 14. Important Difference

Compare these two:

### Filter

```python
[num for num in numbers if num % 2 == 0]
```

This decides:

> **Should this item be included?**

---

### Ternary Expression

```python
["PASS" if num >= 8 else "FAIL" for num in numbers]
```

This decides:

> **What value should be added for this item?**

---

# 15. Combined Example

```python
numbers = [5, 8, 10, 6, 9]

result = [
    "PASS" if num >= 8 else "FAIL"
    for num in numbers
    if num % 2 == 0
]

print(result)
```

Step-by-step:

```text
numbers = [5, 8, 10, 6, 9]

5  → odd  → skip
8  → even → 8 >= 8 → PASS
10 → even → 10 >= 8 → PASS
6  → even → 6 >= 8 → FAIL
9  → odd  → skip
```

Final result:

```text
['PASS', 'PASS', 'FAIL']
```

---

# 16. Common Mistakes

## Incorrect Variable Name

```python
doubled_iteams_with_compression
```

The correct spelling is:

```python
doubled_items_with_comprehension
```

---

## Incorrect `enumerate` Spelling

Incorrect:

```python
enumurate(servers)
```

Correct:

```python
enumerate(servers)
```

---

## Incorrect List Comprehension Variable

Incorrect:

```python
[item * 2 for item in old_list]
```

when the variable is actually named `old_items`.

Correct:

```python
[item * 2 for item in old_items]
```

The variable names inside the comprehension must match the data being used.

---

# Comprehension Quick Reference

## List

```python
[expression for item in iterable]
```

## List with Filter

```python
[expression for item in iterable if condition]
```

## Set

```python
{expression for item in iterable}
```

## Dictionary

```python
{key: value for item in iterable}
```

## Ternary Expression

```python
value_if_true if condition else value_if_false
```

## `enumerate()`

```python
for index, value in enumerate(items):
    ...
```

Custom starting index:

```python
for index, value in enumerate(items, start=10):
    ...
```

---

# DevOps Examples

Comprehensions are useful when working with:

- Server lists
- IP addresses
- AWS resources
- Kubernetes Pods
- Environment variables
- Configuration data
- Log processing

Example:

```python
servers = ["web01", "web02", "db01"]

web_servers = [
    server for server in servers
    if server.startswith("web")
]

print(web_servers)
```

Output:

```text
['web01', 'web02']
```

---

# Best Practice

Use comprehensions when the logic is **simple and readable**.

Good:

```python
even_numbers = [n for n in numbers if n % 2 == 0]
```

Avoid making a comprehension too complicated. If the logic becomes difficult to understand, use a normal `for` loop instead.

---

# Quick Revision

```text
List comprehension
→ Create a new list in a compact way

Set comprehension
→ Create a set with unique values

Dictionary comprehension
→ Create a dictionary

if condition
→ Filter which items are included

if/else
→ Decide what value is produced

enumerate()
→ Get index + value

enumerate(..., start=10)
→ Start index from 10

Ternary expression
→ value_if_true if condition else value_if_false
```

