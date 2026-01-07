# Reproducibility Structure Case

This project demonstrates a **reproducible Python project structure**.  
The goal is to showcase how to organize source code, tests, and configuration files in a clean and repeatable way.

The repository was created using an **Ubuntu terminal** and then pushed to GitHub.  
Since my main system is **Windows**, I used **WSL (Windows Subsystem for Linux)** to interact with Ubuntu.

---

## Project Structure

```text
your-ghcr-repo/
├─ src/
│  ├─ __init__.py
│  └─ processor.py
├─ test/
│  ├─ test_smoke.py
│  └─ test_processor.py
├─ Makefile
├─ pytest.ini
├─ requirements.txt
└─ README.md
```

## Setup Steps

### 1. Create the directory structure
Create the folders and files as shown above using the Ubuntu terminal.

---

### 2. Implement source code
Edit the following file:

- `src/processor.py`

This file contains the main logic of the project.

---

### 3. Add tests
Create corresponding tests in:

- `test/test_processor.py`

This ensures the functionality in `processor.py` can be automatically validated.

---

### 4. Configure pytest
Edit `pytest.ini`.

This configuration file tells `pytest` to include the `src/` directory in the Python path so that test files can correctly import and test the source code.

---

### 5. Add Makefile commands
Edit the `Makefile` to enable simple command-line execution:

- `make test` → runs the test suite  
- `make clean` → cleans up generated files  

This improves usability and reproducibility across environments.

