# Python - Dictionaries

A **dictionary** is a mutable collection that stores data as **key-value pairs**.

Example:

```python
my_dictionary = {
    "a": 1,
    "b": 2,
    "c": 3
}
```

A dictionary is commonly used in DevOps scripts to store structured data such as:

- Server configuration
- Environment variables
- Application settings
- AWS resource information
- Tags
- Metadata

---

# 1. Create a Dictionary

```python
my_dictionary = {
    "a": 1,
    "b": 2,
    "c": 3
}

print(my_dictionary)
```

Output:

```text
{'a': 1, 'b': 2, 'c': 3}
```

---

# 2. Find the Number of Items

```python
print(len(my_dictionary))
```

Output:

```text
3
```

`len()` returns the number of key-value pairs in the dictionary.

---

# 3. Get Dictionary Keys

```python
print(my_dictionary.keys())
```

Output:

```text
dict_keys(['a', 'b', 'c'])
```

`keys()` returns a view containing all the keys.

---

# 4. Get Dictionary Values

```python
print(my_dictionary.values())
```

Output:

```text
dict_values([1, 2, 3])
```

`values()` returns a view containing all the values.

---

# 5. Get Key-Value Pairs

```python
print(my_dictionary.items())
```

Output:

```text
dict_items([('a', 1), ('b', 2), ('c', 3)])
```

`items()` returns the key-value pairs as tuple-like pairs.

---

# 6. Loop Through a Dictionary

Use `items()` when you need both the key and the value.

```python
for key, value in my_dictionary.items():
    print(key)
    print(value)
```

Output:

```text
a
1
b
2
c
3
```

A more readable version is:

```python
for key, value in my_dictionary.items():
    print(f"{key}: {value}")
```

Output:

```text
a: 1
b: 2
c: 3
```

---

# 7. Check Whether a Key Exists

The `in` operator checks dictionary **keys** by default.

```python
print(f"b is in my dictionary: {'b' in my_dictionary}")
```

Output:

```text
b is in my dictionary: True
```

Another example:

```python
print(f"E is in my dictionary: {'E' in my_dictionary}")
```

Output:

```text
E is in my dictionary: False
```

---

# 8. Check Whether a Value Exists

To check values, use:

```python
in my_dictionary.values()
```

Example:

```python
print(f"1 is in my dictionary values: {1 in my_dictionary.values()}")
```

Output:

```text
1 is in my dictionary values: True
```

### Important

```python
1 in my_dictionary
```

checks the **keys**, not the values.

```python
1 in my_dictionary.values()
```

checks the **values**.

---

# 9. Convert Dictionary Values to a Set

```python
print(set(my_dictionary.values()))
```

This converts the dictionary values into a set.

Example:

```python
my_dictionary = {
    "a": 1,
    "b": 2,
    "c": 3
}

print(set(my_dictionary.values()))
```

Output:

```text
{1, 2, 3}
```

This is useful when you need only unique values.

---

# 10. Access Dictionary Values Using Keys

You can access a value using its key:

```python
print("a :", my_dictionary["a"])
print("b :", my_dictionary["b"])
print("c :", my_dictionary["c"])
```

Output:

```text
a : 1
b : 2
c : 3
```

> **Correction:** Your original code printed `"b :"` for all three values. The labels should match the keys being accessed.

---

# 11. `[]` vs `get()`

## Using `[]`

```python
print(my_dictionary["a"])
```

If the key exists, the value is returned.

If the key does not exist:

```python
print(my_dictionary["g"])
```

Python raises:

```text
KeyError
```

---

## Using `get()`

```python
print(my_dictionary.get("g"))
```

If the key does not exist, `get()` returns:

```text
None
```

You can also provide a default value:

```python
print(my_dictionary.get("g", 0))
```

Output:

```text
0
```

### Best Practice

Use `get()` when the key may not exist and you do not want a `KeyError`.

---

# 12. `setdefault()`

The `setdefault()` method gets the value of a key.

If the key does not exist, it adds the key with the given default value.

Example:

```python
my_dictionary.setdefault("d", 4)

print(my_dictionary)
```

Output:

```text
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

If the key already exists, `setdefault()` does not replace its value.

Example:

```python
my_dictionary.setdefault("a", 100)

print(my_dictionary["a"])
```

Output:

```text
1
```

The existing value `1` remains unchanged.

---

# 13. `pop()`

The `pop()` method removes an item using its key and returns its value.

```python
removed_value = my_dictionary.pop("a")

print(removed_value)
print(my_dictionary)
```

Output:

```text
1
{'b': 2, 'c': 3, 'd': 4}
```

If the key does not exist:

```python
my_dictionary.pop("x")
```

Python raises:

```text
KeyError
```

You can provide a default value:

```python
my_dictionary.pop("x", None)
```

This avoids the error.

---

# 14. `popitem()`

`popitem()` removes and returns the **last inserted key-value pair**.

Example:

```python
print(my_dictionary.popitem())
print(my_dictionary)
```

If the dictionary is:

```python
{
    "b": 2,
    "c": 3,
    "d": 4
}
```

the result will be similar to:

```text
('d', 4)
```

and the dictionary becomes:

```python
{
    "b": 2,
    "c": 3
}
```

> **Important:** In modern Python, dictionaries preserve insertion order, so `popitem()` removes the last inserted item.

---

# 15. Merging Dictionaries

Suppose we have default tags:

```python
default_tags = {
    "Environment": "Production",
    "Owner": "Finance",
    "CostCenter": 1000
}
```

and custom tags:

```python
custom_tags = {
    "CostCenter": 1234
}
```

---

## Using `|`

Python 3.9+ supports dictionary merging using `|`.

```python
merged_tags = default_tags | custom_tags

print(merged_tags)
```

Output:

```text
{
    'Environment': 'Production',
    'Owner': 'Finance',
    'CostCenter': 1234
}
```

The value from `custom_tags` replaces the value from `default_tags` when the same key exists.

```text
default_tags:
CostCenter = 1000

custom_tags:
CostCenter = 1234

Result:
CostCenter = 1234
```

> **Important:** `|` creates a **new dictionary**. The original dictionaries are not changed.

---

# 16. `update()`

The `update()` method adds the key-value pairs from another dictionary to the current dictionary.

```python
default_tags.update(custom_tags)

print(default_tags)
```

Result:

```text
{
    'Environment': 'Production',
    'Owner': 'Finance',
    'CostCenter': 1234
}
```

Unlike `|`, `update()` **modifies the original dictionary**.

---

# `|` vs `update()`

| Operation | Creates New Dictionary? | Changes Original? |
|-----------|---------------------------|--------------------|
| `dict1 | dict2` | Yes | No |
| `dict1.update(dict2)` | No | Yes |

---

# 17. `dict.fromkeys()`

`dict.fromkeys()` creates a new dictionary using the provided keys and assigns the same default value to each key.

Example:

```python
new_dictionary = dict.fromkeys(
    ["one", "two", "one"],
    0
)

print(new_dictionary)
```

Output:

```text
{'one': 0, 'two': 0}
```

The duplicate key `"one"` appears only once because dictionary keys must be unique.

---

# 18. `clear()`

The `clear()` method removes all key-value pairs from the dictionary.

```python
new_dictionary.clear()

print(new_dictionary)
```

Output:

```text
{}
```

---

# 19. Add a New Key After Clearing

A dictionary can still be used after `clear()`.

```python
new_dictionary["danger"] = 100

print(new_dictionary)
```

Output:

```text
{'danger': 100}
```

---

# Dictionary Key Rules

Dictionary keys must be **hashable**.

Common valid key types include:

```python
str
int
float
tuple
```

Example:

```python
my_dictionary = {
    "name": "Prudhvi",
    1: "one",
    (10, 20): "location"
}
```

Mutable objects such as lists cannot be dictionary keys:

```python
my_dictionary = {
    [1, 2]: "value"
}
```

This raises:

```text
TypeError: unhashable type: 'list'
```

---

# Important DevOps Example

Dictionaries are very useful for storing configuration.

```python
server = {
    "name": "web01",
    "environment": "production",
    "ip": "10.0.0.10",
    "port": 8080,
    "monitoring": True
}
```

Access values:

```python
print(server["name"])
print(server["ip"])
print(server["port"])
```

Output:

```text
web01
10.0.0.10
8080
```

---

# Example: AWS Resource Tags

Dictionaries are commonly used to represent AWS or Azure resource tags.

```python
tags = {
    "Environment": "Production",
    "Owner": "Finance",
    "CostCenter": "1234"
}
```

You can then loop through the tags:

```python
for key, value in tags.items():
    print(f"{key}: {value}")
```

---

# Important Note About Updating Data

When you modify a dictionary using methods such as:

```python
update()
pop()
popitem()
clear()
setdefault()
```

the original dictionary can be changed.

For example:

```python
default_tags = {
    "Environment": "Production",
    "Owner": "Finance"
}

default_tags.update({
    "Owner": "DevOps"
})

print(default_tags)
```

The original data is now changed:

```text
{'Environment': 'Production', 'Owner': 'DevOps'}
```

For data that should remain unchanged, create a copy first.

---

# Create a Copy Before Updating

```python
default_tags = {
    "Environment": "Production",
    "Owner": "Finance"
}

custom_tags = default_tags.copy()

custom_tags.update({
    "Owner": "DevOps"
})

print("Original:", default_tags)
print("Updated :", custom_tags)
```

Output:

```text
Original: {'Environment': 'Production', 'Owner': 'Finance'}
Updated : {'Environment': 'Production', 'Owner': 'DevOps'}
```

This keeps the original dictionary unchanged.

> **Best Practice:** When the original data is important, create a copy before performing updates or destructive operations.

---

# Dictionary Methods Quick Reference

| Method / Operation | Purpose |
|--------------------|---------|
| `keys()` | Get all keys |
| `values()` | Get all values |
| `items()` | Get all key-value pairs |
| `get()` | Safely get a value |
| `setdefault()` | Get a value or add a default |
| `update()` | Add/update multiple key-value pairs |
| `pop()` | Remove a specific key |
| `popitem()` | Remove the last inserted item |
| `clear()` | Remove everything |
| `copy()` | Create a shallow copy |
| `dict.fromkeys()` | Create a dictionary from keys |
| `|` | Merge dictionaries into a new dictionary |

---

# Quick Revision

```text
Dictionary
→ Stores key-value pairs
→ Keys must be unique
→ Mutable
→ Preserves insertion order

keys()
→ Get keys

values()
→ Get values

items()
→ Get key-value pairs

get()
→ Safely access a key

setdefault()
→ Add a key only if it does not already exist

pop()
→ Remove a specific key

popitem()
→ Remove the last inserted key-value pair

update()
→ Modify the original dictionary

|
→ Merge dictionaries and create a new dictionary

clear()
→ Remove all items

copy()
→ Create a copy
```

# Python - Nested Dictionaries

A dictionary can contain another dictionary as a value. This is called a **nested dictionary**.

Nested dictionaries are very useful in DevOps because cloud resources often have structured information such as:

- Server ID
- IP address
- State
- Tags
- Region
- Instance type

---

# Example: Server Information

```python
server_info = {
    "id": "Web01",
    "ip_address": "10.0.30.148",
    "state": "running",
    "tags": {
        "environment": "production",
        "owner": "engineering"
    }
}
```

> **Correction:** A comma was missing after `"environment": "production"` in the original code.

The structure is:

```text
server_info
│
├── id
├── ip_address
├── state
└── tags
    ├── environment
    └── owner
```

---

# 1. Access a Top-Level Value

```python
print("Server ID:", server_info.get("id"))
```

Output:

```text
Server ID: Web01
```

> **Correction:** The original code used `"Server state"` while accessing the `"id"` key. The label should match the value being accessed.

---

# 2. Access a Value from a Nested Dictionary

The `tags` key contains another dictionary.

We can access the nested value using:

```python
print(
    "Server environment:",
    server_info.get("tags").get("environment")
)
```

Output:

```text
Server environment: production
```

The access flow is:

```text
server_info
     │
     ▼
   tags
     │
     ▼
environment
     │
     ▼
production
```

---

# 3. Using `get()` with a Default Value

Suppose we want to get the instance type.

The key does not currently exist:

```python
server_info.get("instance_type", "t2.micro")
```

Since `"instance_type"` is not present, Python returns:

```text
t2.micro
```

Example:

```python
print(
    "Instance type:",
    server_info.get("instance_type", "t2.micro")
)
```

Output:

```text
Instance type: t2.micro
```

> **Correction:** The original code used `"instace_type"` and `"t2micro"`. The correct key is `"instance_type"` and a common AWS instance type format is `"t2.micro"`.

---

# 4. Update a Dictionary Value

We can change the server state using:

```python
server_info["state"] = "stopped"
```

Before:

```text
state = running
```

After:

```text
state = stopped
```

Check the value:

```python
print(server_info["state"])
```

Output:

```text
stopped
```

---

# 5. Add a New Value to a Nested Dictionary

We can add a new tag inside the `tags` dictionary:

```python
server_info["tags"]["region"] = "eu-central-1"
```

The `tags` dictionary now contains:

```python
{
    "environment": "production",
    "owner": "engineering",
    "region": "eu-central-1"
}
```

---

# Complete Example

```python
server_info = {
    "id": "Web01",
    "ip_address": "10.0.30.148",
    "state": "running",
    "tags": {
        "environment": "production",
        "owner": "engineering"
    }
}

print("Server ID:", server_info.get("id"))

print(
    "Server environment:",
    server_info.get("tags", {}).get("environment")
)

print(
    "Instance type:",
    server_info.get("instance_type", "t2.micro")
)

server_info["state"] = "stopped"

server_info["tags"]["region"] = "eu-central-1"

print(server_info)
```

---

# Why Use `get("tags", {})`?

Instead of:

```python
server_info.get("tags").get("environment")
```

it is safer to use:

```python
server_info.get("tags", {}).get("environment")
```

If `"tags"` does not exist, Python uses an empty dictionary:

```python
{}
```

This prevents an error such as:

```text
AttributeError: 'NoneType' object has no attribute 'get'
```

---

# DevOps Use Case

Nested dictionaries are common when working with:

- AWS API responses
- Azure API responses
- Kubernetes configuration
- JSON files
- REST APIs
- Infrastructure metadata

For example, an API response may look like:

```json
{
  "id": "Web01",
  "state": "running",
  "tags": {
    "environment": "production",
    "owner": "engineering"
  }
}
```

Python dictionaries are very useful for reading and modifying this type of structured data.

---

# Quick Revision

```text
server_info["state"]
    → Access a top-level value

server_info["tags"]["environment"]
    → Access a nested value

dict.get("key")
    → Get a value safely

dict.get("key", "default")
    → Return a default value if the key is missing

server_info["state"] = "stopped"
    → Update an existing value

server_info["tags"]["region"] = "eu-central-1"
    → Add a new value to a nested dictionary
```