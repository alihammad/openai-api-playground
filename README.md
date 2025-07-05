# OpenAI API Experiment

This project demonstrates how to interact with OpenAI's GPT models for text, audio, and image generation using the latest OpenAI Python API. Example scripts are provided for getting started, running a basic conversational flow, transcribing audio, and generating images.

---

## Setup

1. **Clone the Repository**

   ```sh
   git clone https://github.com/alihammad/openai-api-playground.git
   cd openai-api-experiment
   ```

2. **Install Dependencies with UV**

   This project uses the [uv](https://github.com/astral-sh/uv) package manager. All dependencies are defined in the `pyproject.toml` file.

   To sync and install all packages, run:

   ```sh
   uv pip sync
   ```

   If you need to install uv, run:

   ```sh
   pip install uv
   ```

3. **Set Up Environment Variables**

   Create a `.env` file in your project directory and add your OpenAI API key:

   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Run Example Scripts**

   Use the following command to run any script:

   ```sh
   python <script_name>.py
   ```

   Or, open and run the Jupyter notebooks for image and audio examples.

---

## File Descriptions

- **getting_started.py**  
  Minimal example for initializing the OpenAI client and making a simple API call.

- **basic_flow.py**  
  Sends a conversation to GPT and prints a data science dad joke.

- **audio_to_text.py**  
  Converts audio files to text using OpenAI's speech-to-text API.

- **generate_image.ipynb**  
  Generates an image using DALL·E and displays it inline in the notebook.

---

## Notes

- For image generation, ensure your OpenAI account has access to DALL·E. If you encounter a permissions error, your account or organization may need to be verified.
- You can modify the prompts and messages in the scripts to experiment with different conversations, roles, or image descriptions.
- For more information on the new OpenAI Python API, see the [official documentation](https://github.com/openai/openai-python).

---

## Example Output

**Text Generation:**
```
Finish Reason: stop
Why did the statistician bring a ladder to the bar? Because he heard the drinks were on the house!
```

**Image Generation (Jupyter Notebook):**
- The generated image will be displayed inline in the notebook after running the cell.

**Audio to Text:**
```
Transcribed text: "Hello, this is a test of OpenAI's speech-to-text
```
