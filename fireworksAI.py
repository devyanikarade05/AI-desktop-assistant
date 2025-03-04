import fireworks.client

fireworks.client.api_key = "fw_3ZG2noJG4uBep3ZU7pQZh7pG"

model_name = "accounts/fireworks/models/mixtral-8x7b-instruct"

chat_history = []

def firework_chat(prompt):
    chat_history.append({"role": "user", "content": prompt})

    response = fireworks.client.ChatCompletion.create(
            model=model_name,
            messages=chat_history,
            max_tokens=50    # 1 word = 1.5 token
        )

    bot_reply = response.choices[0].message.content
    chat_history.append({"role": "assistant", "content": bot_reply})

    return bot_reply


