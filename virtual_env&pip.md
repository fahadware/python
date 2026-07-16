# Python Virtual Environments & Pip — Complete Reference Guide

A combined study/reference notes file covering **Virtual Environments** and **Pip**, including theory and all commonly used commands. Useful as a quick-reference cheat sheet for any Python / AI-ML project setup.

---

## Part 1: Virtual Environments

### What is a Virtual Environment?

A **virtual environment** is an isolated, self-contained Python installation for a specific project — with its own separate set of installed packages, completely independent from your system's main Python installation and from other projects' environments.

### Why We Need It

If you work on two projects that need **different versions** of the same package (e.g., Project A needs `numpy 1.20`, Project B needs `numpy 1.26`), installing packages **globally** means only one version can exist at a time — installing for one project could break the other. Virtual environments solve this by giving **each project its own private package storage**.

### Real-World Importance (especially AI/ML)

AI/ML libraries (`numpy`, `pandas`, `torch`, `tensorflow`) evolve rapidly with frequent breaking changes. Virtual environments let you:
- Work on multiple projects with conflicting dependency versions, side by side
- Share exact project requirements with teammates
- Deploy with the same package versions used during development

### Key Terms

| Term | Meaning |
|---|---|
| Global/System Python | The one main Python installation on your computer, shared by default |
| Virtual environment | An isolated copy/reference to Python, with its own independent package storage |
| Activating | Switching into a virtual environment so `pip`/`python` commands use it |
| Deactivating | Leaving the virtual environment, returning to the system Python |
| `requirements.txt` | A text file listing a project's exact dependencies (and versions) |

### How It Works Internally

Activating a virtual environment temporarily modifies your terminal's **PATH** (the system's list of "where to look for programs"), so that `python` and `pip` point to the environment's own copies **first**, before the system-wide versions. Deactivating simply removes that priority, restoring normal behavior. Nothing about the system Python is ever touched.

```
BEFORE activation:
PATH -> [System Python location, ...]

AFTER activation:
PATH -> [myenv's Python location, System Python location, ...]
               ^
       Found FIRST — takes priority!
```

### Virtual Environment Commands

| Purpose | Command |
|---|---|
| Create a virtual environment | `python -m venv myenv` |
| Activate (Windows) | `myenv\Scripts\activate` |
| Activate (Mac/Linux) | `source myenv/bin/activate` |
| Deactivate | `deactivate` |
| Check which Python is active (Mac/Linux) | `which python` |
| Check which Python is active (Windows) | `where python` |
| Save current environment's packages to a file | `pip freeze > requirements.txt` |
| Recreate an environment from a requirements file | `pip install -r requirements.txt` |

### Typical AI/ML Project Setup Workflow

```bash
mkdir ml_project
cd ml_project
python -m venv venv
source venv/bin/activate        # or venv\Scripts\activate on Windows
pip install numpy pandas scikit-learn matplotlib
pip freeze > requirements.txt
```

### Common Mistakes

1. Forgetting to activate before installing → packages pollute the global Python instead of the intended isolated environment.
2. Committing the entire virtual environment folder to Git — instead, add it to `.gitignore` and commit only `requirements.txt`.
3. Confusing "creating" (`venv` command, one-time) with "activating" (must be done every new terminal session).
4. Not tracking which environment is currently active — always check the terminal prompt, e.g. `(venv)`.
5. Creating an environment with the wrong Python version — a venv uses whichever Python version was active at creation time.

### Best Practices

- One virtual environment **per project** — never share across unrelated projects.
- Use a conventional folder name like `venv` or `.venv`.
- Always maintain an up-to-date `requirements.txt`.
- Add the environment folder to `.gitignore`.
- Activate the project's environment every time you start working on it.

---

## Part 2: Pip

### What is Pip?

**Pip** ("Pip Installs Packages") is Python's official **package manager** — it downloads, installs, updates, and removes third-party Python packages, primarily from **PyPI** (the Python Package Index).

### Why We Need It

Without pip, you'd have to manually download library source code and handle installation and dependencies yourself. Pip automates all of this with a single command.

### Key Terms

| Term | Meaning |
|---|---|
| PyPI | The online repository hosting almost all public Python packages |
| Package | A distributable bundle of Python code |
| Dependency | A package that another package needs in order to work |
| Version pinning | Specifying an exact version of a package to install, for reproducibility |

### How Pip and Virtual Environments Work Together

Pip **installs** packages; the active virtual environment determines **where** those packages actually get installed (isolated vs. system-wide). They are used together constantly in real practice.

### How It Works Internally

```
pip install numpy
     |
     v
1. Pip contacts PyPI over the internet
2. PyPI returns available versions + download location
3. Pip picks the best matching version (or the one you specified)
4. Pip downloads the package files (often pre-built ".whl" files)
5. Pip checks numpy's own dependencies and installs those too (dependency resolution)
6. Pip copies everything into the CURRENT environment's site-packages/ folder
7. numpy is now import-able in your code
```

### Pip Commands

| Purpose | Command |
|---|---|
| Install a package | `pip install numpy` |
| Install a specific version | `pip install numpy==1.26.0` |
| Install a minimum version or higher | `pip install numpy>=1.20` |
| Install multiple packages at once | `pip install numpy pandas matplotlib` |
| Uninstall a package | `pip uninstall numpy` |
| Upgrade a package | `pip install --upgrade numpy` |
| List installed packages | `pip list` |
| Show details about an installed package | `pip show numpy` |
| Check pip's own version | `pip --version` |
| Install everything from a requirements file | `pip install -r requirements.txt` |
| Save current package list to a file | `pip freeze > requirements.txt` |
| Check for outdated packages | `pip list --outdated` |

### Common Mistakes

1. Forgetting to activate a virtual environment before installing → pollutes the global Python.
2. Using `pip` vs `pip3` inconsistently on some Mac/Linux systems (not usually an issue inside an activated venv).
3. Installing packages one-by-one instead of maintaining `requirements.txt` → inconsistent environments over time.
4. Ignoring version conflicts and force-installing → can silently break compatibility between packages.
5. Typos in package names → "No matching distribution found" errors.

### Best Practices

- Always work inside an activated virtual environment before running `pip install`.
- Regularly update `requirements.txt` via `pip freeze > requirements.txt`.
- Pin exact versions (`package==1.2.3`) for reproducibility in shared/production projects.
- Periodically check `pip list --outdated` before deciding to upgrade.
- Use `pip show package_name` to investigate dependency relationships when debugging conflicts.

---

## Quick Cheat Sheet (Both Topics Combined)

```bash
# 1. Create and enter a project folder
mkdir my_project && cd my_project

# 2. Create a virtual environment
python -m venv venv

# 3. Activate it
source venv/bin/activate       # Mac/Linux
venv\Scripts\activate          # Windows

# 4. Install packages
pip install numpy pandas matplotlib

# 5. Check what's installed
pip list
pip show numpy

# 6. Save exact dependencies
pip freeze > requirements.txt

# 7. Recreate this environment elsewhere
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 8. Leave the environment when done
deactivate
```

---

*Notes compiled as part of an AI/ML-focused Python learning course.*