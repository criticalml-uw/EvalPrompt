# EvalPrompt: Analyzing Large Language Models for Self-Diagnosis

To better understand the capability of using Large Language Models (LLMs) for self-diagnosis, we prompted ChatGPT-4.0 with medical questions from the United States Medical Licensing Exam (USMLE). This repository contains the initial set of USMLE questions, along with the corresponding ChatGPT-4.0 responses which can then be evaluated by humans.


## Contents of Repository

This repository contains 3 major files across 2 experiments. Experiment 1 assesses the correctness and clarity of ChatGPT-4.0 and Experiment 2 re-prompts ChatGPT-4.0 through sentence dropout by using the correctly answered questions from the first experiment.
1. `generate_responses.ipynb`: The notebook used to generate LLM responses for a specific experiment.
2. `output.xlsx`: The final ChatGPT-4.0 responses.
3. `questions.xlsx`: The initial USMLE questions.

To directly use the results of this repository, please download the `output.xlsx` Excel files from Experiments 1 and 2. Please refer to [Data File Contents](#data-file-contents) for details on the contents of the data files.

If you would like to replicate the experiment and reproduce the results, please follow [Replicate the Experiment](#replicate-the-experiment) to begin setting up your local environment.


## Data File Contents

Experiment 1 contains a single ChatGPT-4.0 response for each question, while Experiment 2 contains multiple answers for each question through sentence dropout.

### Experiment 1

| Column Name      | Description                                                                                   |
|------------------|-----------------------------------------------------------------------------------------------|
| `usmle_1_q_num`  | An ID referring to each Step 1 question. Any numbers missing are questions that were dropped. |
| `usmle_1_q`      | The full multiple-choice textual question from the USMLE Step 1 test.                         |
| `correct_answer` | The correct answer to the multiple-choice question.                                           |
| `usmle_1_a`      | ChatGPT's answer to the open-ended version of the question.                                   |

### Experiment 2

| Column Name        | Description                                                                                     |
|--------------------|-------------------------------------------------------------------------------------------------|
| `usmle_1_q_num`    | An ID referring to each Step 1 question. Any numbers missing are questions that were dropped.   |
| `usmle_1_q`        | The full multiple-choice textual question from the USMLE Step 1 test.                           |
| `correct_answer`   | The correct answer to the multiple-choice question.                                             |
| `non_expert_match` | The assessor categorization from all nonexperts, where C = correct, PC = partially correct, I = incorrect, and A = ambiguous. For example, `CCC` represents 3 assessors each categorizing ChatGPT-4.0's response to the particular question as correct. |
| `expert_match`     | The assessor categorization from all experts. This is similar to the `non_expert_match` column. |
| `usmle_1_a_*`      | Multiple columns each with the same prefix, representing one ChatGPT-4.0 response for each sentence. For example, `usmle_1_a_0` represents ChatGPT-4.0's answer to the open-ended question with the first sentence being dropped. |


## Replicate the Experiment

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
4. Attain your API key from OpenAI. You may refer to this [guide](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key) to locate your OpenAI key.
5. Create an `.env` file, with the key: `OPENAI_API_KEY`
    ```
    touch .env
    ```
6. Open the `generate_responses.ipynb` in the `experiment_1` folder, and run each cell of code.
7. Have humans evaluate the `output.xlsx` file from Experiment 1 to determine which questions the LLM answered correctly and clearly.
8. Update the `non_expert_match` and `expert_match` columns from the `questions.xlsx` file from Experiment 2 with the results from the previous step.
9. Open the `generate_responses.ipynb` in the `experiment_2` folder, and run each cell of code.
10. Have humans evaluate the `output.xlsx` file from Experiment 2 to evaluate the robustness of the LLM by determining which questions the LLM continued to answer correctly.
