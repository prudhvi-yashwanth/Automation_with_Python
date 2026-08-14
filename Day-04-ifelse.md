# Python - Conditions, Truthy/Falsy Values, and Guard Clauses

## 1. Using `if` with the `in` Operator

The `in` operator checks whether a value exists inside another object.

Example:

```python
server_status = "running"

if "r" in server_status:
    print("Server is active")
```

Output:

```text
Server is active
```

Here:

```python
"r" in server_status
```

checks whether the character `"r"` exists in:

```text
running
```

Since it exists, the condition is `True`.

---

# 2. Truthy and Falsy Values

Python treats some values as **Truthy** and some as **Falsy** when they are used directly in a condition.

## Common Falsy Values

These values evaluate to `False`:

```python
False
None
0
0.0
""
[]
{}
()
```

Examples:

```python
bool("")
# False

bool([])
# False

bool(0)
# False

bool(None)
# False
```

---

## Common Truthy Values

Most non-empty and non-zero values are truthy.

Examples:

```python
True
1
10
3.14
"hello"
[1, 2, 3]
{"name": "Web01"}
(1, 2)
```

Example:

```python
bool("hello")
# True

bool([1, 2, 3])
# True

bool(10)
# True
```

> **Important:** `[""]` and `(" ")` are **truthy** because the list and tuple themselves are not empty. The presence of an empty string inside them does not make the container falsy.

---

# 3. Using `not`

The `not` operator reverses the truth value of an expression.

```text
True  → False
False → True
```

Example:

```python
server_status = "running"

if not server_status:
    print("Server status is empty")
```

Since:

```python
bool("running")
```

is `True`:

```python
not True
```

becomes:

```python
False
```

Therefore, the `print()` statement does not execute.

---

## Example with an Empty Value

```python
server_status = ""

if not server_status:
    print("Server status is not set")
```

Output:

```text
Server status is not set
```

Because:

```python
bool("")
# False
```

and:

```python
not False
# True
```

---

# 4. `if`, `elif`, and `else`

Python uses `if`, `elif`, and `else` to make decisions.

### Syntax

```python
if condition:
    # Runs if condition is True

elif another_condition:
    # Runs if the first condition is False
    # and this condition is True

else:
    # Runs if all previous conditions are False
```

Example:

```python
server_status = "stopped"

if server_status == "running":
    print("Server is running")

elif server_status == "stopped":
    print("Server is stopped")

else:
    print("Unknown server status")
```

Output:

```text
Server is stopped
```

### Execution Flow

```text
if condition
     │
     ├── True  → Execute if block
     │
     └── False
            │
            ▼
       elif condition
            │
            ├── True  → Execute elif block
            │
            └── False
                   │
                   ▼
                 else
```

> **Correction:** `elif` must always have a condition. This is invalid:
>
> ```python
> elif:
> ```
>
> Use:
>
> ```python
> elif condition:
> ```

---

# 5. Guard Clauses

A **Guard Clause** is a condition placed at the beginning of a function to validate input or handle invalid cases before executing the main logic.

Guard clauses help to:

- Validate input
- Prevent invalid operations
- Handle missing data
- Reduce deeply nested `if` statements
- Make code easier to read

A common pattern is:

```text
Validate input
     │
     ├── Invalid → Stop / Return
     │
     └── Valid
          │
          ▼
      Main Logic
```

---

# 6. Example: Guard Clauses

```python
def process_data(data):
    if not data:
        print("No data provided")
        return

    if not isinstance(data, list):
        print("Error: Data must be a list")
        return

    print(f"Processing {len(data)} items...")
    print(data)
```

---

# 7. `isinstance()`

The `isinstance()` function checks whether a value belongs to a particular data type.

Syntax:

```python
isinstance(value, type)
```

Example:

```python
isinstance([1, 2, 3], list)
```

Output:

```python
True
```

Another example:

```python
isinstance("hello", list)
```

Output:

```python
False
```

---

# 8. Run the Guard Clause Example

```python
process_data(None)
```

Output:

```text
No data provided
```

Because:

```python
bool(None)
```

is `False`.

---

## Empty List

```python
process_data([])
```

Output:

```text
No data provided
```

Because an empty list is falsy:

```python
bool([])
# False
```

---

## Valid List

```python
process_data([1, 2, 3])
```

Output:

```text
Processing 3 items...
[1, 2, 3]
```

---

# 9. Correct Error Handling

The original example had:

```python
elif not isinstance(data, list):
    print(f"Error: {len(data)} Required data type List")
```

This has a technical problem.

If `data` is not a list, it may not support `len()`. For example:

```python
data = 10
len(data)
```

raises:

```text
TypeError
```

The safer version is:

```python
elif not isinstance(data, list):
    print("Error: Data must be a list")
    return
```

---

# 10. Better Guard Clause Pattern

A clean DevOps-style function can look like this:

```python
def process_data(data):
    if data is None:
        print("Error: No data provided")
        return

    if not isinstance(data, list):
        print("Error: Data must be a list")
        return

    if not data:
        print("Error: List is empty")
        return

    print(f"Processing {len(data)} items...")
    print(data)
```

This separates the checks clearly:

```text
Is data provided?
      │
      ├── No → Stop
      │
      ▼
Is it a list?
      │
      ├── No → Stop
      │
      ▼
Is the list empty?
      │
      ├── Yes → Stop
      │
      ▼
Process the data
```

---

# DevOps Use Case

Guard clauses are very useful in automation scripts.

For example, before deploying an application, you can validate:

```python
def deploy(environment, image):
    if not environment:
        print("Error: Environment is not provided")
        return

    if not image:
        print("Error: Docker image is not provided")
        return

    if environment not in ["dev", "staging", "prod"]:
        print("Error: Invalid environment")
        return

    print(f"Deploying {image} to {environment}")
```

This prevents the deployment logic from running with invalid inputs.

---

# Quick Revision

```text
if
→ Executes code when a condition is True

elif
→ Checks another condition if the previous condition is False

else
→ Executes when all previous conditions are False

in
→ Checks whether an item exists inside a collection

not
→ Reverses a truth value

Truthy
→ Usually non-empty and non-zero values

Falsy
→ None, False, 0, 0.0, "", [], {}, ()

isinstance()
→ Checks the data type of a value

Guard Clause
→ Validates input early and stops invalid execution
```

---

# Interview Example

A simple interview explanation:

> **"In Python, I use `if`, `elif`, and `else` to make decisions. Python also has truthy and falsy values, so values like empty strings, empty lists, zero, and `None` are treated as false. The `not` operator reverses the result. In DevOps automation, I commonly use guard clauses inside functions to validate inputs before performing the main operation. For example, before processing deployment data, I can check whether the data is provided, whether it is the expected type, and whether it is empty. If any validation fails, I return early instead of continuing with invalid data."**
