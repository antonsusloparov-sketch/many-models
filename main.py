#!/usr/bin/env python3

from __future__ import annotations
from yandex_cloud_ml_sdk import YCloudML
import os
from dotenv import load_dotenv
from gigachat import GigaChat
from gigachat.models import Chat, Messages, MessagesRole
import my_math
import inspect as ins

load_dotenv()

ya_sdk = YCloudML(
    folder_id=os.getenv('YaGPT_FOLDER_ID'),
    auth=os.getenv('YaGPT_API_KEY'),
)
yagpt = ya_sdk.models.completions("yandexgpt").configure(temperature=0.5)

giga = GigaChat(
    credentials=os.getenv('GIGACHAT_CREDENTIALS'),
    verify_ssl_certs=False
)


def test_writer_agent(sources, model_id):
    s_name = ins.getmodule(sources).__name__
    sys_prompt = (f'Напиши тест для Python-функций из модуля {s_name}: {ins.getsource(sources)}, '
                'используя unittests. Оставь только код модуля с тестами. Пояснения не нужны.')
    if model_id == 1:
        # GigaChat
        chat = Chat(
                messages=[
                    Messages(
                        role=MessagesRole.SYSTEM,
                        content=(sys_prompt)
                    )
                ]
            )
        i = 1
        while i:
            response = giga.chat(chat)
            answer = response.choices[0].message.content
            print('------------ GigaChat: ----------------')
            print(answer)
            print("----------- конец ответа --------------")
            question = input("Введите уточнения (0 для выбора модели): ")
            if question == "0":
                break
            chat.messages.append(
                Messages(
                    role=MessagesRole.USER,
                    content=question
                )
            )
    elif model_id == 2:
        # YandexGPT
        messages = [
            {
                "role": "system",
                "text": sys_prompt,
            },
        ]
        i = 1
        while i:
            result = yagpt.run(messages)
            answer = result.alternatives[0].text
            print('----------- Yandex GPT: ---------------')
            print(answer)
            print("----------- конец ответа --------------")
            question = input("Введите уточнения (0 для выбора модели): ")
            if question == "0":
                break
            messages.append(
                    {
                        "role": "system",
                        "text": question,
                    }
                )

j = 1
while j:
    print((f'Выберите модель:\n'
           '1 - GigaChat\n'
           '2 - Yandex GPT\n'
           '0 - выход из программы'
           ))
    choice = input("Ваш выбор: ")
    if choice == "0":
        break
    elif choice in ("1", "2"):
        test_writer_agent(my_math, int(choice))
    else:
        pass