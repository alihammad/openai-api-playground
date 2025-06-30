# OpenAI API Experiment

This project is a standard Python script setup for testing the ChatGPT API.

## Features
- Uses [UV](https://github.com/astral-sh/uv) as the package manager
- Supports environment variables via `.env` file
- Ready for OpenAI/ChatGPT API integration

## Setup

1. **Install UV** (if not already installed):
   ```bash
   pip install uv
   ```
2. **Install dependencies:**
   ```bash
   uv pip install -r requirements.txt
   ```
3. **Create a `.env` file** in the project root with your OpenAI API key:
   ```env
   OPENAI_API_KEY=your-api-key-here
   ```
4. **Run the script:**
   ```bash
   uv python main.py
   ```

## Notes
- Make sure to keep your `.env` file secure and never commit it to version control.
