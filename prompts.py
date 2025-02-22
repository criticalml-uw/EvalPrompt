def make_open_ended(text: str) -> str:
    """
    Converts a multiple-choice question to an open-ended one.

    Args:
        text (str): The initial multiple-choice question.

    Returns:
        str: The transformed open-ended question.
    """
    text = text.split("(A)")
    text = text[0]
    text = text.replace("which of the following", "what")
    text = text.replace("Which of the following", "What")
    return text


def chatgpt(client, model: str, question: str) -> str:
    """
    Prompts an OpenAI model with a question, attaining the model's response.

    Args:
        client: The OpenAI client.
        model (str): The name of the model to be used.
        question (str): The open-ended question.

    Returns:
        str: The model's response to the question.
    """
    question = f"Including an explanation, answer the following question: {question}"
    completion = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": question}],
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    ans = completion.choices[0].message.content.strip()
    ans = " ".join(ans.splitlines())
    return ans
