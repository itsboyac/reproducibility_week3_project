# Reproducibility Structure Case
This project is to showcase the structure of project reproducibility, here we create a repository in Ubuntu with directory structure shown as it is. 

## Steps
This repository was created using Ubuntu terminal, then pushed to GitHub. Before starting, note that I used Windows system, so I have downloaded WSL to interact with Linux Ubuntu.

1. Create folders in such structure: 

your-ghcr-repo
├─ src
|  ├─ __init__.py
|  └─ processor.py
├─ test
|  ├─ test_smoke.py
|  └─ test_processor.py
├─ Makefile
├─ pytest.ini
├─ requirements.txt
└─ README.md

2. Edit src/processor.py file, and add a test (test/test_processor.py)
3. Edit pytest.ini, this file is used to tell the test_processor.py file that look in src folder so you can find the file to test on. 
4. Edit Makefile, so when you type <make test> or <make clean> in Linux terminal, it'll execute the test and cleanup
5. requiremnts.txt file is to document the package a user need to run this program. 
>>>>>>> c943629 (Initial commit: basic processor and tests)
