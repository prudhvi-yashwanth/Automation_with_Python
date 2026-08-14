# Python Environment - Quick Reference

This is a quick reference for managing Python versions, virtual environments, and project dependencies.

---

# Daily Commands

| Task | Command |
|------|---------|
| Install a Python version | `pyenv install 3.12.5` |
| Set the local Python version | `cd myproject && pyenv local 3.11.9` |
| Create a virtual environment | `python -m venv .venv` |
| Activate the virtual environment | `source .venv/bin/activate` |
| Install a package | `python -m pip install <package_name>` |
| Save dependencies | `python -m pip freeze > requirements.txt` |
| Install dependencies from a file | `python -m pip install -r requirements.txt` |
| Deactivate the virtual environment | `deactivate` |

> **Note:** `python -m pip` is preferred over just `pip` because it makes sure you are using the `pip` associated with the currently selected Python interpreter.

---

# 1. Install a Python Version

```bash
pyenv install 3.12.5
```

Installs Python `3.12.5` using `pyenv`.

Check the installed versions:

```bash
pyenv versions
```

---

# 2. Set a Local Python Version

Move into your project:

```bash
cd myproject
```

Set the Python version for that project:

```bash
pyenv local 3.11.9
```

This creates a `.python-version` file inside the project directory.

The selected Python version will automatically be used when you work inside that directory.

> **Important:** The Python version used by `pyenv` and the Python version inside a virtual environment are related. Create the virtual environment using the Python version you want the project to use.

---

# 3. Create a Virtual Environment

```bash
python -m venv .venv
```

Creates an isolated Python environment named `.venv`.

Example project structure:

```text
myproject/
├── .venv/
├── app.py
├── requirements.txt
└── .gitignore
```

---

# 4. Activate the Virtual Environment

On Linux or macOS:

```bash
source .venv/bin/activate
```

After activation, your terminal usually shows:

```text
(.venv)
```

This means commands such as `python` and `pip` will use the virtual environment.

Verify:

```bash
python --version
which python
```

---

# 5. Install a Python Package

```bash
python -m pip install <package_name>
```

Example:

```bash
python -m pip install requests
```

Verify the installed package:

```bash
python -m pip show requests
```

---

# 6. Save Project Dependencies

```bash
python -m pip freeze > requirements.txt
```

This writes the installed packages and their versions into:

```text
requirements.txt
```

Example:

```text
requests==2.32.4
urllib3==2.5.0
```

---

# 7. Install Dependencies from `requirements.txt`

On another machine or inside a new virtual environment:

```bash
python -m pip install -r requirements.txt
```

This installs the packages listed in the file.

---

# 8. Deactivate the Virtual Environment

```bash
deactivate
```

This exits the currently active virtual environment.

---

# Best Practices

## 1. Use One Virtual Environment per Project

Create a separate virtual environment for each project.

Example:

```text
Project A → .venv
Project B → .venv
Project C → .venv
```

This prevents dependency conflicts between projects.

---

## 2. Use `.venv` as the Directory Name

A common convention is:

```text
.venv
```

Example:

```bash
python -m venv .venv
```

Many development tools, including VS Code, can automatically detect `.venv`.

---

## 3. Add `.venv` to `.gitignore`

Do not commit the virtual environment to Git.

Add this to `.gitignore`:

```gitignore
.venv/
```

The virtual environment can be recreated using the project's Python version and dependency file.

---

## 4. Pin Dependencies

For simple projects, you can capture the exact installed package versions using:

```bash
python -m pip freeze > requirements.txt
```

This helps reproduce the same environment.

Install them later using:

```bash
python -m pip install -r requirements.txt
```

> **Note:** `pip freeze` captures **all packages installed in the virtual environment**, including transitive dependencies. For larger projects, dependency-management tools such as Poetry or `pip-tools` can provide more controlled dependency management.

---

## 5. Set a Local Python Version

Use:

```bash
pyenv local <version>
```

Example:

```bash
pyenv local 3.12.5
```

This creates:

```text
.python-version
```

inside the project directory.

When you enter the directory, `pyenv` automatically selects that Python version.

This helps the team use a consistent Python version for the project.

---

# Recommended Project Setup

```bash
# Enter the project
cd myproject

# Select the required Python version
pyenv local 3.12.5

# Create the virtual environment
python -m venv .venv

# Activate it
source .venv/bin/activate

# Install dependencies
python -m pip install requests

# Save dependencies
python -m pip freeze > requirements.txt
```

Add the virtual environment to `.gitignore`:

```gitignore
.venv/
```

---

# Complete Workflow

```text
Project
   │
   ▼
Select Python Version
   │
   │ pyenv local 3.12.5
   ▼
Create Virtual Environment
   │
   │ python -m venv .venv
   ▼
Activate Environment
   │
   │ source .venv/bin/activate
   ▼
Install Dependencies
   │
   │ python -m pip install ...
   ▼
Save Dependencies
   │
   │ python -m pip freeze > requirements.txt
   ▼
Commit Application Code
   │
   ├── requirements.txt → Commit
   ├── .python-version  → Commit
   └── .venv/            → Do NOT commit
```

---

# Quick Revision

```text
pyenv
  → Manage Python versions

.python-version
  → Stores the Python version for the project

venv
  → Creates an isolated Python environment

.venv
  → Common name for the virtual environment

requirements.txt
  → Stores project dependencies

.gitignore
  → Prevents .venv from being committed
```

---
