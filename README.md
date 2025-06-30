# OpenAI API Experiment

This project demonstrates how to interact with OpenAI's GPT models using the latest OpenAI Python API. It includes example scripts for getting started and for running a basic conversational flow.

---

## Setup

1. **Clone the Repository**

   ```sh
   git clone <your-repo-url>
   cd openai-api-experiment
   ```

2. **Install Dependencies**

   Make sure you have Python 3.12+ installed. Then run:

   ```sh
   pip install openai python-dotenv ipython
   ```

3. **Set Up Environment Variables**

   Create a `.env` file in your project directory and add your OpenAI API key:

   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Run Example Scripts**

   Use the following command to run any script:

   ```sh
   python basic_flow.py
   ```

---

## File Descriptions

### `basic_flow.py`

- Loads your OpenAI API key from the `.env` file.
- Initializes the OpenAI API client.
- Sends a conversation to the GPT-3.5-turbo model, prompting it to act as a stand-up comic specializing in dad jokes for data scientists.
- Prints the finish reason and the AI-generated joke to the console.
- Demonstrates the new OpenAI Python API usage (`client.chat.completions.create`).

### `getting_started.py`

- (If present) Intended as a minimal example for initializing the OpenAI client and making a simple API call.
- Useful for verifying your environment and API key setup.

---

## Notes

- The `IPython.display` import in `basic_flow.py` is for enhanced output in Jupyter notebooks but is not required for terminal execution.
- You can modify the prompts and messages in the scripts to experiment with different conversations or roles.
- For more information on the new OpenAI Python API, see the [official documentation](https://github.com/openai/openai-python).

---

## Example Output

```
Finish Reason: stop
Why did the statistician bring a ladder to the bar? Because he heard the drinks were on the house!
```
