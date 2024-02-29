from prompt import user_prompt, persona
from openai import OpenAI
import os

API_KEY = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=API_KEY)

# 이전 대화 목록을 저장할 리스트
conversation_history = [{"role": "system", "content": persona}, {"role": "system", "content": user_prompt}]

#GPT 호출 메서드
def ask_to_get(user_input):
    # 사용자 입력을 대화 기록에 추가
    conversation_history.append({'role': 'user', 'content': user_input})

    # GTP 모델 호출
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        top_p=0.2,
        temperature=0.2,
        messages=conversation_history # 이전 대화 기록 포함
    )

    # GPT의 응답을 대화 기록에 추가
    bot_response = response.choices[0].message.content
    conversation_history.append({'role': 'assistant', 'content': bot_response})

    return bot_response