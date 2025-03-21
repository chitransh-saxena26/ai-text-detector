
# AI Text Detector

A web-based AI text detection tool that identifies AI-generated text using Hugging Face's Transformers.


## Features

- Detects AI-generated text using RoBERTa-large OpenAI Detector
- Simple Flask backend for API requests
- User-friendly frontend for easy text input and results display
- Cross platform


## Tech Stack

**Backend:** Flask, Transformers(HuggingFace)

**Frontend:** HTML, CSS, JavaScript

## Installation

Clone the repository:

```bash
    git clone https://github.com/chitransh-saxena26/ai-text-detector.git  

    cd ai-text-detector  

```
    
Install dependencies:

```
    pip install -r requirements.txt
```
## Usage

Run the flask 
```python

    python app.py

```
connect the flask with the website using JavaScript
```javascript

    const response = await fetch("http://127.0.0.1:5000/analyze", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: text })
    });
```



## Deployment

The flask backend is still not deployed due to the model being too large. And most hosting website offers limited space for free package.
