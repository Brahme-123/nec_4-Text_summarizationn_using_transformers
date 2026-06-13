# 🚀 Next-Gen AI Text & Document Summarizer

A professional, lightweight Desktop GUI application built using Python and Tkinter that allows users to instantly summarize long English articles, paragraphs, or uploaded documents (`.txt` and `.pdf` files) into executive key highlights using an advanced internal frequency-scoring algorithm.

---

## ✨ Key Features
* **Dual Input System:** Paste raw text directly into the window or upload document files.
* **Smart File Parser:** Seamlessly reads and processes both `.txt` and `.pdf` documents.
* **Deterministic AI Engine:** Highly optimized word-frequency algorithm that guarantees summary output without crashing or lagging.
* **Premium Modern UI:** Built with a dark-mode theme utilizing high-contrast, professional visual hierarchy.

---

## 📸 Application Preview (Output Screenshot)

Here is the live execution preview of the summarizer engine:

![Application Output Screenshot](./text_summarization.png)

> **Note:** Replace `output_screenshot.png` with the actual path/name of your saved image inside your repository.

---

## 🛠️ Tech Stack & Requirements
* **Language:** Python 3.10+
* **GUI Framework:** Tkinter (Built-in)
* **PDF Processing:** PyPDF2

### Installation

1. Clone or download this project repository to your local system.
2. Open your terminal or PowerShell inside the project folder and install the required PDF library:
   ```bash
   pip install PyPDF2

2. How to Run Locally
Execute the main application controller script using this command:

Bash
python summarizer.py
📤 How to Push this Project to GitHub
If you want to host this project on your GitHub repository, open your terminal inside the project folder (C:\Users\lenovo\Desktop\text summarization) and execute these commands in order:

Step 1: Initialize Git Repository
Bash
git init
Step 2: Stage All Project Files
This adds your code, README file, and screenshots to the staging area:

Bash
git add .
Step 3: Commit the Files
Bash
git commit -m "Initial commit - Fully functional Text Summarizer UI"
Step 4: Rename the Default Branch
Bash
git branch -M main
Step 5: Link Local Folder to GitHub
(Create a new repository on GitHub web, copy its URL link, and paste it below)

Bash
git remote add origin [https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME.git)
Step 6: Push Code to GitHub Live
Bash
git push -u origin main
📖 How to Use the App
Method 1 (File Upload): Click the "📁 Select PDF / TXT File" button on the left panel, choose any English document, and the summary will display instantly at the bottom section.

Method 2 (Raw Text Paste): Copy any long paragraph or essay, paste it inside the dark input field on the right panel, and click "⚡ SUMMARIZE PASTED TEXT" to generate bullet-point highlights.