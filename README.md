# Text2Tree Converter

A beautiful and efficient tool to convert indented plain text into visual Unicode tree diagrams.

## ✨ Features
- **Interactive Desktop App**: Modern UI with real-time conversion and dark mode.
- **CLI Interface**: Perfect for piping input from other tools.
- **Standalone Executable**: Easy to package and share without requiring Python.
- **Micro-animations**: Smooth, responsive design.

---

## 🚀 Installation

1. **Clone or Download** this repository.
2. **Install Python 3.8+** if not already installed.
3. **Install Dependencies**:
   Open your terminal in the project folder and run:
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Usage

### 1. Run as Desktop Application
Simply run the main application script:
```bash
python app.py
```
This will open a native window where you can type or paste your text.

### 2. Run in CLI (Command Line)
You can pipe text into the CLI tool:
```bash
# On Windows (PowerShell/CMD):
type test_input.txt | python cli.py

# On Linux/macOS:
cat test_input.txt | python cli.py
```
Options:
- `-s` or `--spaces`: Change indentation size (default is 2).
  Example: `type input.txt | python cli.py --spaces 4`

---

## 📦 How to Build the .exe
If you want to create a standalone executable for Windows:

1. Run the build script:
   ```bash
   python build_app.py
   ```
2. Wait for the process to finish.
3. Your application will be in the **`dist`** folder as **`Text2Tree.exe`**.

---

## 📝 Input Format
The tool expects text where hierarchy is defined by indentation (spaces or tabs).

**Example Input:**
```text
Root
  Category A
    Item 1
    Item 2
  Category B
    Subitem
```

**Output Example:**
```text
Root
├── Category A
│   ├── Item 1
│   └── Item 2
└── Category B
    └── Subitem
```

---

## 🛠️ Tech Stack
- **Backend**: FastAPI, Uvicorn
- **Logic**: Python
- **GUI**: PyWebView
- **Packaging**: PyInstaller
- **Frontend**: HTML5, CSS3 (Glassmorphism), Vanilla JavaScript
