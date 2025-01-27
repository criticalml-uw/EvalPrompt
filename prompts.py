def make_open_ended(text):
    text = text.split("(A)")
    text = text[0]
    text = text.replace("which of the following", "what")
    text = text.replace("Which of the following", "What")
    return text


def chatgpt(client, model, question):
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
