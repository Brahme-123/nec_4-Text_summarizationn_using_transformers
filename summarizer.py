import os
import re
import collections
import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2

def read_file(file_path):
    """Safely reads PDF or TXT files using robust encoding handling"""
    if not os.path.exists(file_path):
        return None
    ext = os.path.splitext(file_path)[1].lower()
    try:
        if ext == '.txt':
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    return f.read()
            except UnicodeDecodeError:
                with open(file_path, 'r', encoding='latin-1') as f:
                    return f.read()
        elif ext == '.pdf':
            text = ""
            with open(file_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
            return text
    except Exception as e:
        print(f"Read Error: {e}")
        return None
    return None

def simple_summarizer(text, num_sentences=2):
    """Guaranteed to return summarized sentences without any failing logic"""
    if not text or not text.strip():
        return "Please enter or upload some text to summarize!"
        
    # Clean spaces
    clean_text = re.sub(r'\s+', ' ', text).strip()
    
    # Split into sentences safely
    sentences = [s.strip() for s in re.split(r'[.!?]\s*', clean_text) if len(s.strip()) > 0]
    
    if not sentences:
        return [clean_text]
    if len(sentences) <= num_sentences:
        return sentences
        
    # Word frequency logic
    words = re.findall(r'\b\w+\b', clean_text.lower())
    stop_words = {'the', 'is', 'at', 'which', 'on', 'and', 'a', 'an', 'to', 'in', 'of', 'for', 'it', 'that', 'this', 'with', 'as', 'by', 'are', 'was', 'were', 'be', 'or', 'from'}
    
    freq = collections.Counter([w for w in words if w not in stop_words and len(w) > 2])
    
    if not freq:
        return sentences[:num_sentences]
        
    # Score sentences based on word frequency
    scores = {}
    for sent in sentences:
        for word in re.findall(r'\b\w+\b', sent.lower()):
            if word in freq:
                scores[sent] = scores.get(sent, 0) + freq[word]
                
    # Sort and pick top sentences
    ranked_sentences = sorted(scores, key=scores.get, reverse=True)
    summary = ranked_sentences[:num_sentences]
    
    # Keep original order
    summary.sort(key=lambda x: sentences.index(x))
    return summary

def display_output(result):
    """Helper to refresh and show output safely"""
    output_entry.config(state="normal")
    output_entry.delete("1.0", tk.END)
    
    if isinstance(result, list):
        formatted_text = ""
        for i, line in enumerate(result, 1):
            formatted_text += f"🔥 Key Point {i}: {line}.\n\n"
        output_entry.insert("1.0", formatted_text)
    else:
        output_entry.insert("1.0", result)
        
    output_entry.config(state="disabled")

def process_text():
    """Handles manual pasted text"""
    input_text = text_entry.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Warning", "Please paste some English text first!")
        return
    result = simple_summarizer(input_text)
    display_output(result)

def process_file_upload():
    """Handles PDF/TXT file upload option"""
    file_path = filedialog.askopenfilename(filetypes=[("Documents", "*.txt *.pdf")])
    if file_path:
        file_text = read_file(file_path)
        if file_text and file_text.strip():
            result = simple_summarizer(file_text)
            display_output(result)
        else:
            messagebox.showerror("Error", "Could not read any valid text from this file.")

# --- UI SETUP ---
app = tk.Tk()
app.title("Text & Document Summarizer Pro")
# FIXED: Bad geometry lines completely removed
app.geometry("980x700")
app.configure(bg="#1e293b")

# Main Title
title = tk.Label(app, text="🚀 NEXT-GEN AI SUMMARIZER", font=("Segoe UI", 16, "bold"), bg="#1e293b", fg="#38bdf8")
title.pack(pady=15)

# Workspace Grid Frame
workspace = tk.Frame(app, bg="#1e293b")
workspace.pack(fill="both", expand=True, padx=20, pady=5)

# LEFT PANEL: File Upload Option
left_panel = tk.Frame(workspace, width=320, bg="#0f172a", highlightbackground="#334155", highlightthickness=1)
left_panel.pack(side="left", fill="both", padx=(0, 10), pady=5)
left_panel.pack_propagate(False)

left_title = tk.Label(left_panel, text="OPTION 1: UPLOAD FILE", font=("Segoe UI", 11, "bold"), bg="#0f172a", fg="#38bdf8")
left_title.pack(pady=20)

upload_btn = tk.Button(left_panel, text="📁 Select PDF / TXT File", font=("Segoe UI", 11, "bold"), bg="#0284c7", fg="white", activebackground="#0369a1", activeforeground="white", bd=0, height=2, cursor="hand2", command=process_file_upload)
upload_btn.pack(pady=40, padx=20, fill="x")

# RIGHT PANEL: Paste Text Option
right_panel = tk.Frame(workspace, bg="#0f172a", highlightbackground="#334155", highlightthickness=1)
right_panel.pack(side="right", fill="both", expand=True, padx=(10, 0), pady=5)

right_title = tk.Label(right_panel, text="OPTION 2: PASTE RAW TEXT", font=("Segoe UI", 11, "bold"), bg="#0f172a", fg="#38bdf8")
right_title.pack(pady=10)

text_entry = tk.Text(right_panel, font=("Segoe UI", 11), bg="#1e293b", fg="white", insertbackground="white", height=10, wrap="word", padx=10, pady=10)
text_entry.pack(fill="both", expand=True, padx=15, pady=5)

summarize_btn = tk.Button(right_panel, text="⚡ SUMMARIZE PASTED TEXT", font=("Segoe UI", 11, "bold"), bg="#10b981", fg="white", activebackground="#059669", activeforeground="white", bd=0, height=2, cursor="hand2", command=process_text)
summarize_btn.pack(pady=10, padx=15, fill="x")

# BOTTOM PANEL: Output Highlights Box
bottom_panel = tk.Frame(app, height=220, bg="#0f172a", highlightbackground="#334155", highlightthickness=1)
bottom_panel.pack(fill="x", padx=20, pady=15)
bottom_panel.pack_propagate(False)

output_title = tk.Label(bottom_panel, text="📋 AI GENERATED EXECUTIVE HIGHLIGHTS (OUTPUT)", font=("Segoe UI", 11, "bold"), bg="#0f172a", fg="#34d399")
output_title.pack(anchor="w", padx=20, pady=(10, 5))

output_entry = tk.Text(bottom_panel, font=("Segoe UI", 11, "bold"), bg="#1e293b", fg="#34d399", height=6, wrap="word", padx=10, pady=10, state="disabled")
output_entry.pack(fill="both", expand=True, padx=15, pady=(0, 15))

app.mainloop()