## EvalPrompt: Analyzing Large Language Models for Self-Diagnosis

To better understand the capability of using Large Language Models (LLMs) for self-diagnosis, we prompted ChatGPT with medical questions from the United States Medical Licensing Exam (USMLE). This repository contains the initial set of USMLE questions, along with the corresponding ChatGPT-4.0 responses which can then be evaluated by humans.

### Getting Started

1. Create a local virtual environment
    ```
    python3 -m venv .venv
    ```
2. Activate the virtual environment
    ```
    source .venv/bin/activate
    ```
3. Install dependencies
    ```
    pip install -r requirements.txt
    ```
4. Create an `.env` file, with the key: `OPENAI_API_KEY`
    ```
    touch .env
    ```
5. When needed, deactivate the local virtual environment
    ```
    deactivate
    ```

### Adding Additional Dependencies

1. Activate the virtual environment
    ```
    source .venv/bin/activate
    ```
2. Install dependencies in the terminal. As an example
    ```
    pip install pandas
    ```
3. Update requirements
    ```
    pip freeze > requirements.txt
    ```
4. Commit `requirements.txt`
