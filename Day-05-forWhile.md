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
