# Installing Python on macOS (Step-by-Step)

## Step 1: Open Terminal

- Open **Terminal** from Spotlight or Applications.

---

## Step 2: Check Existing Python Version

```bash
python3 --version
```

---

## Step 3: Install Homebrew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
---

## Step 4: Add Homebrew to PATH

```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

---

## Step 5: Install Python Using Homebrew

```bash
brew install python
```

---

## Step 6: Verify Python Installation

```bash
brew upgrade python
```

---

## Step 7: Check Installed Python Files

```bash
ls /opt/homebrew/bin/python3*
```

---

## Step 8: Update PATH to Use Homebrew Python

```bash
echo 'export PATH="/opt/homebrew/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

## Step 9: Verify Active Python Version

```bash
which python3
python3 --version
```

---

## Step 10: Confirm Python Executable Path

```bash
python3 -c "import sys; print(sys.executable)"
```

![alt text](image.png)