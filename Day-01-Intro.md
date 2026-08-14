````markdown id="pyday101"
# Python for DevOps - Day 1

## Why Type Conversion is Important

In DevOps, almost everything coming from:

- Shell commands
- Log files
- APIs
- Configuration files

is received as **text (string)**, even if it looks like a number.

For example:

```text
CPU: 42%
Memory: 85%
Disk Free: 15GB
```

Although `42`, `85`, and `15` look like numbers, Python treats them as **strings** until you explicitly convert them.

When writing automation scripts, you often need to:

- Compare values
- Perform calculations
- Check thresholds
- Generate alerts

To do this, you must first convert the string into an integer (`int`) or decimal (`float`).

---

# Common Beginner Errors

The two most common errors while working with type conversion are:

## 1. TypeError

Example:

```python
age = "25"
print(age + 5)
```

Output:

```text
TypeError: can only concatenate str (not "int") to str
```

### Reason

Python cannot perform mathematical operations between a **string** and an **integer**.

### Correct Way

```python
age = "25"
print(int(age) + 5)
```

Output:

```text
30
```

---

## 2. ValueError

Example:

```python
cpu = "42%"
print(int(cpu))
```

Output:

```text
ValueError: invalid literal for int()
```

### Reason

The `%` symbol is not a number, so Python cannot convert `"42%"` into an integer.

### Correct Way

Remove unwanted characters before converting.

```python
cpu = "42%"
cpu = cpu.replace("%", "")

print(int(cpu))
```

Output:

```text
42
```

---

# DevOps Example

Suppose a monitoring script returns:

```text
Disk free: 15GB
```

Your requirement is:

- If free disk space is less than **20 GB**, display a warning.

---

## Python Code

```python
disk_raw = "Disk free: 15GB"
threshold_gb = "20"

disk_usage = int(
    disk_raw.split(":")[1]
            .strip()
            .replace("GB", "")
)

threshold_data = int(threshold_gb)

if disk_usage < threshold_data:
    print("LOW DISK SPACE")
```

---

# Line-by-Line Breakdown

## Step 1

```python
disk_raw = "Disk free: 15GB"
```

Creates a string variable containing the disk usage information.

Value:

```text
"Disk free: 15GB"
```

---

## Step 2

```python
threshold_gb = "20"
```

Stores the minimum safe disk space as a string.

Value:

```text
"20"
```

---

## Step 3

```python
disk_raw.split(":")
```

Splits the string at the colon (`:`).

Output:

```python
["Disk free", " 15GB"]
```

---

## Step 4

```python
disk_raw.split(":")[1]
```

Selects the second item from the list.

Output:

```text
" 15GB"
```

---

## Step 5

```python
.strip()
```

Removes leading and trailing spaces.

Output:

```text
"15GB"
```

---

## Step 6

```python
.replace("GB", "")
```

Removes the `"GB"` text.

Output:

```text
"15"
```

---

## Step 7

```python
int(...)
```

Converts the string `"15"` into an integer.

Output:

```python
15
```

---

## Step 8

```python
threshold_data = int(threshold_gb)
```

Converts the threshold value from a string to an integer.

Before:

```python
"20"
```

After:

```python
20
```

---

## Step 9

```python
if disk_usage < threshold_data:
```

Compares the two integer values.

```python
15 < 20
```

Result:

```python
True
```

---

## Step 10

```python
print("LOW DISK SPACE")
```

Since the condition is `True`, Python prints:

```text
LOW DISK SPACE
```

---

# Execution Flow

```text
Disk free: 15GB
        │
        ▼
Split using ":"
        │
        ▼
" 15GB"
        │
        ▼
Remove spaces
        │
        ▼
"15GB"
        │
        ▼
Remove "GB"
        │
        ▼
"15"
        │
        ▼
Convert to Integer
        │
        ▼
15
        │
        ▼
Compare with 20
        │
        ▼
15 < 20
        │
        ▼
Print:
LOW DISK SPACE
```

---

# Interview Tips

- Data from shell commands, APIs, and log files is usually received as a **string**.
- Always convert numeric strings using `int()` or `float()` before performing calculations.
- If the string contains extra characters such as `%`, `GB`, or `MB`, remove them using methods like `.replace()` or `.strip()` before converting.
- `TypeError` occurs when mixing incompatible data types.
- `ValueError` occurs when trying to convert an invalid string into a number.

---

# Summary

Today you learned:

- Why type conversion is important in DevOps automation.
- The difference between strings and integers.
- How to use `int()` for type conversion.
- Common errors: `TypeError` and `ValueError`.
- How to clean strings using `.split()`, `.strip()`, and `.replace()`.
- A real-world example of checking disk space using Python.

---

# End of Day 1
````