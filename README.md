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
   <img width="1128" height="613" alt="image" src="https://github.com/user-attachments/assets/0c961147-a6e8-4eee-896e-6bba30fdc4b0" />
  ==> open terminal on the project folder
3. **Install Python 3.8+** if not already installed.
4. **Install Dependencies**:
   Open your terminal in the project folder and run:
   ```bash
   pip install -r requirements.txt
   ```
<img width="1621" height="252" alt="image" src="https://github.com/user-attachments/assets/94175270-82b2-44dc-b481-d5441865ba93" />

---

## 💻 Usage

### 1. Run as Desktop Application
Simply run the main application script:
```bash
python app.py

```
<img width="1296" height="134" alt="image" src="https://github.com/user-attachments/assets/90888175-fe88-463d-9f72-a2cc329ff99a" />
This will open a native window where you can type or paste your text.
<img width="2559" height="1516" alt="image" src="https://github.com/user-attachments/assets/cedf47ba-796b-4a5a-8b5b-a047d7bc1f83" />

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
   <img width="1497" height="351" alt="image" src="https://github.com/user-attachments/assets/da2f3917-012f-4f70-855c-28a7f32ea471" />

2. Wait for the process to finish.
3. Your application will be in the **`dist`** folder as **`Text2Tree.exe`**.
   <img width="1413" height="568" alt="image" src="https://github.com/user-attachments/assets/31216761-b8ec-4917-b6c1-0526bdb685ac" />
<img width="1094" height="133" alt="image" src="https://github.com/user-attachments/assets/c2f6b761-3635-405b-af6c-5ac9540e6755" />

==> now you can run this app by this .exe file without many complex bash scripting.Just click on Text2Tree.exe and enjoy
<img width="1399" height="515" alt="image" src="https://github.com/user-attachments/assets/5eb75c27-50bd-46f4-a421-21103f08b9fc" />
==> you can move the .exe file to your Desktop for convinient access
---

## 📝 Input Format
The tool expects text where hierarchy is defined by indentation (spaces or tabs).
<img width="2559" height="1364" alt="image" src="https://github.com/user-attachments/assets/9b5b8596-c5b2-4d4e-86bf-c01104497bc3" />



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

