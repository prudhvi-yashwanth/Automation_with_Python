# Python - Lists, Tuples, and Sets

## 1. Lists

A **list** is an ordered and mutable collection of items.

Example:

```python
ports = [80, 443, 8080, 5000]
```

Lists are useful when:

- Order matters.
- Items may need to be changed.
- Items may need to be added or removed.

---

# List Indexing and Slicing

Python list indexing starts from:

```text
0
```

Example:

```python
ports = [80, 443, 8080, 5000]

print(ports[0])   # 80
print(ports[1])   # 443
print(ports[-1])  # 5000
```

A positive index moves from the beginning:

```text
 0     1     2     3
 ↓     ↓     ↓     ↓
80    443   8080  5000
```

A negative index moves from the end:

```text
 -4    -3    -2    -1
  ↓     ↓     ↓     ↓
80    443   8080  5000
```

---

# List Slicing

The basic slicing syntax is:

```python
list[start:end:step]
```

Where:

- `start` → Starting index
- `end` → Stopping index (not included)
- `step` → Number of positions to move

The default step is:

```python
+1
```

---

## Positive Step

With a positive step, Python normally moves from left to right.

Example:

```python
ports = [80, 443, 8080, 5000]

print(ports[0:3])
```

Output:

```text
[80, 443, 8080]
```

---

## Negative Step

A negative step moves from right to left.

Example:

```python
ports = [80, 443, 8080, 5000]

print(ports[::-1])
```

Output:

```text
[5000, 8080, 443, 80]
```

The following:

```python
ports[::-1]
```

means:

```text
start → not specified
end   → not specified
step  → -1
```

Therefore, Python traverses the complete list backwards.

---

## Important Slicing Rule

For a positive step:

```python
list[start:end:positive_step]
```

the start position should normally come before the end position.

Example:

```python
ports = [80, 443, 8080, 5000]

print(ports[3:1:1])
```

Output:

```text
[]
```

Because Python tries to move forward from index `3` towards index `1`, which is not possible with a positive step.

For a negative step, the direction is reversed.

Example:

```python
ports = [80, 443, 8080, 5000]

print(ports[3:1:-1])
```

Output:

```text
[5000, 8080]
```

---

## Step Size Cannot Be Zero

The step value cannot be `0`.

This is invalid:

```python
ports[::0]
```

It raises:

```text
ValueError: slice step cannot be zero
```

The default step is:

```python
+1
```

---

# List Methods

Most list methods **modify the original list**.

This is important because the operation does not create a separate copy of the list.

Example:

```python
ports = [80, 443]

ports.append(5000)

print(ports)
```

Output:

```text
[80, 443, 5000]
```

The original `ports` list has changed.

---

# `append()`

Adds an item to the **end** of the list.

```python
ports = [80, 443]

ports.append(5000)

print(ports)
```

Output:

```text
[80, 443, 5000]
```

---

# `insert()`

Adds an item at a specific position.

```python
ports = [80, 443, 5000]

ports.insert(1, 8080)

print(ports)
```

Output:

```text
[80, 8080, 443, 5000]
```

Syntax:

```python
list.insert(index, value)
```

---

# `pop()`

Removes and **returns** an item from the list.

Without an index, `pop()` removes the last item:

```python
ports = [80, 443, 8080, 5000]

removed = ports.pop()

print(removed)
print(ports)
```

Output:

```text
5000
[80, 443, 8080]
```

You can also provide an index:

```python
removed = ports.pop(1)
```

This removes the item at index `1`.

> **Important:** `pop()` uses an **index**, not a value.

---

# `remove()`

Removes the first matching value from the list.

```python
ports = [80, 443, 5000]

ports.remove(5000)

print(ports)
```

Output:

```text
[80, 443]
```

> **Important:** `remove()` uses the **value**, not the index.

If the value does not exist:

```python
ports.remove(8080)
```

Python raises:

```text
ValueError
```

---

# List Methods Quick Reference

| Method | Purpose | Example |
|--------|---------|---------|
| `append()` | Adds an item to the end | `ports.append(5000)` |
| `insert()` | Adds an item at a specific index | `ports.insert(1, 8080)` |
| `pop()` | Removes and returns an item by index | `ports.pop()` |
| `remove()` | Removes the first matching value | `ports.remove(5000)` |

> **Important:** These methods modify the original list.

---

# 2. Tuples

A **tuple** is an:

- Ordered
- Immutable
- Sequence

Tuples are generally written using parentheses:

```python
host_port = ("127.0.0.1", 3000)
```

---

## Ordered

Tuple elements maintain their position.

```python
host_port = ("127.0.0.1", 3000)

print(host_port[0])
print(host_port[1])
```

Output:

```text
127.0.0.1
3000
```

---

## Immutable

Once a tuple is created, its elements cannot be changed.

```python
host_port = ("127.0.0.1", 3000)

host_port[1] = 8080
```

This raises:

```text
TypeError
```

Therefore, you cannot directly:

- Add items
- Remove items
- Change existing items

---

# Tuple Use Cases

Tuples are useful when the data should remain fixed.

Examples:

```python
host_port = ("127.0.0.1", 3000)
```

```python
rgb = (255, 0, 0)
```

```python
version = (3, 12, 5)
```

They are useful for fixed records where the values should not change.

---

# Empty Tuple

An empty tuple is created using:

```python
empty_tuple = ()
```

> **Correction:** `simple_tuple = (,)` is not valid Python syntax.

---

# Single-Item Tuple

A tuple with one item requires a **trailing comma**:

```python
simple_tuple = (100,)
```

Without the comma:

```python
simple_tuple = (100)
```

Python treats it as an integer, not a tuple.

Check:

```python
type((100,))
```

Output:

```text
<class 'tuple'>
```

---

# 3. Sets

A **set** is a collection that:

- Contains unique items
- Is mutable
- Does not support positional indexing
- Is unordered in the sense that you should not rely on element order

Example:

```python
ports = {80, 443, 8080}
```

---

# Unique Items

A set automatically removes duplicate values.

```python
ports = {80, 443, 443, 8080, 80}

print(ports)
```

The duplicates are removed.

The result contains only:

```text
80
443
8080
```

> **Important:** Do not rely on the displayed order of a set.

---

# Set Items Must Be Hashable

Set elements must be **hashable**.

Immutable built-in types such as:

- `int`
- `str`
- `float`
- `tuple` (when all of its elements are hashable)

can be set elements.

Mutable types such as:

- `list`
- `dict`
- `set`

cannot be directly stored as set elements.

---

## Valid Example

```python
servers = {
    ("web01", 80),
    ("web02", 443)
}
```

Tuples can be used because they are hashable when all their elements are hashable.

---

## Invalid Example

```python
servers = {
    ["web01", 80]
}
```

This raises:

```text
TypeError: unhashable type: 'list'
```

---

## Set of Sets

This is also invalid:

```python
my_set = {{1, 2}, {3, 4}}
```

because a set is mutable and therefore unhashable.

If you need nested set-like data, use `frozenset`:

```python
my_set = {
    frozenset({1, 2}),
    frozenset({3, 4})
}
```

---

# Membership Testing

Sets are very useful for checking whether an item exists.

Use:

```python
in
```

Example:

```python
ports = {80, 443, 8080}

if 443 in ports:
    print("Port 443 exists")
```

Output:

```text
Port 443 exists
```

Set membership testing is generally very efficient.

---

# `add()`

Adds an item to a set.

```python
ports = {80, 443}

ports.add(8080)

print(ports)
```

The set now contains:

```text
80
443
8080
```

---

# `discard()`

Removes an item from a set.

```python
ports = {80, 443, 8080}

ports.discard(443)
```

If the item does not exist, `discard()` does **not** raise an error.

```python
ports.discard(9999)
```

No error occurs.

---

# `remove()`

Also removes an item from a set.

```python
ports = {80, 443, 8080}

ports.remove(443)
```

However, if the item does not exist, `remove()` raises a:

```text
KeyError
```

### Difference

| Method | Item Exists | Item Does Not Exist |
|--------|-------------|---------------------|
| `discard()` | Removes item | No error |
| `remove()` | Removes item | Raises `KeyError` |

---

# Set Operations

Suppose:

```python
devops = {"Docker", "Kubernetes", "Terraform"}
cloud = {"AWS", "Azure", "Terraform"}
```

---

# Union

Union combines all unique items from both sets.

Using `|`:

```python
devops | cloud
```

Or:

```python
devops.union(cloud)
```

Result:

```text
{
    "Docker",
    "Kubernetes",
    "Terraform",
    "AWS",
    "Azure"
}
```

---

# Intersection

Intersection finds items common to both sets.

Using:

```python
devops & cloud
```

Or:

```python
devops.intersection(cloud)
```

Result:

```text
{"Terraform"}
```

---

# Difference

Difference finds items that exist in one set but not the other.

Using:

```python
devops - cloud
```

Or:

```python
devops.difference(cloud)
```

Result:

```text
{"Docker", "Kubernetes"}
```

The operation:

```python
cloud - devops
```

would return:

```text
{"AWS", "Azure"}
```

---

# Set Operations Quick Reference

| Operation | Operator | Method | Meaning |
|-----------|----------|--------|---------|
| Union | `\|` | `union()` | All unique items from both sets |
| Intersection | `&` | `intersection()` | Common items |
| Difference | `-` | `difference()` | Items in one set but not the other |

---

# Why Must Set Items Be Immutable?

Python sets use a **hash table** internally.

A hash table allows Python to perform membership checks efficiently.

For this to work correctly, an element's hash value must remain stable while it is stored in the set.

Mutable objects such as lists can change their contents, so they are not hashable and cannot be used as set elements.

This is why:

```python
{1, 2, 3}
```

is valid, while:

```python
{[1, 2, 3]}
```

is invalid.

---

# List vs Tuple vs Set

| Feature | List | Tuple | Set |
|---------|------|-------|-----|
| Ordered | Yes | Yes | No guaranteed order |
| Mutable | Yes | No | Yes |
| Allows duplicates | Yes | Yes | No |
| Indexing | Yes | Yes | No |
| Slicing | Yes | Yes | No |
| Main use | Changeable collection | Fixed collection | Unique items / membership |
| Example | `[1, 2, 3]` | `(1, 2, 3)` | `{1, 2, 3}` |

---

# DevOps Examples

## List

Useful when order matters and values can change:

```python
servers = ["web01", "web02", "web03"]
servers.append("web04")
```

---

## Tuple

Useful for fixed information:

```python
host_port = ("10.0.0.10", 8080)
```

---

## Set

Useful when you want unique values:

```python
used_ports = {80, 443, 8080, 443}
```

Duplicate `443` is automatically removed.

---

# Quick Revision

```text
List
→ Ordered
→ Mutable
→ Allows duplicates
→ Supports indexing and slicing

Tuple
→ Ordered
→ Immutable
→ Allows duplicates
→ Supports indexing and slicing

Set
→ Unique items
→ Mutable
→ No guaranteed order
→ No indexing
→ Very useful for membership testing
```

---

# Important Points to Remember

1. List indexes normally move forward with a positive step and backward with a negative step.
2. `list[start:end:step]` uses `+1` as the default step.
3. A slice step cannot be `0`.
4. `[::-1]` reverses a sequence.
5. Methods such as `append()`, `insert()`, `pop()`, and `remove()` modify the original list.
6. Tuples are ordered and immutable.
7. An empty tuple is `()`.
8. A single-item tuple needs a trailing comma: `(10,)`.
9. Sets contain unique hashable items.
10. `discard()` does not raise an error when an item is missing, while `remove()` raises `KeyError`.
11. Set operations include union, intersection, and difference.
12. Lists cannot be stored directly inside sets because lists are mutable and unhashable.
