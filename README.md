THIS REPO CONTAINS ALL THE PROJECTS FROM 28th May to 4th June.
#28th May:-
# PDF AI Analyzer

A simple Streamlit application that reads a PDF file from your device and sends its contents to a free AI API for summarization and analysis.

## Features

* Load a PDF directly from a local file path
* Extract text using `pypdf`
* Send extracted text to an AI model using OpenRouter
* Display AI-generated summaries in a Streamlit web app

---

## Installation

Install the required packages:

```bash
pip install streamlit pypdf requests
```

---

## Setup

Get a free API key from OpenRouter:

https://openrouter.ai/

Then add your API key inside the code:

```python
API_KEY = "your_api_key_here"
```

---

## Configure PDF Path

Specify the PDF you want to analyze:

```python
PDF_PATH = r"/path/to/your/file.pdf"
```

Example:

### Windows

```python
PDF_PATH = r"C:\Users\John\Downloads\paper.pdf"
```

### Mac/Linux

```python
PDF_PATH = "/Users/john/Downloads/paper.pdf"
```

---

## Running the App

Run the Streamlit app from the terminal:

```bash
streamlit run testinga.py
```

After launching, Streamlit will open in your browser automatically.

---

## Notes

* Free AI endpoints may occasionally be unavailable.
* Large PDFs are truncated before being sent to the API to avoid token limits.
* Streamlit apps should be run from a `.py` file, not from a Jupyter notebook.

---

## Tech Stack

* Python
* Streamlit
* pypdf
* OpenRouter API
