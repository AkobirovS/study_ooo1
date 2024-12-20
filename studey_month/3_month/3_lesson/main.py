# # # import openai
# # #
# # # Key = "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"
# # #
# # # openai.api_key = Key
# # #
# # # def generate_response(text):
# # #     response = openai.Completion.create(
# # #         prompt=text,
# # #         engine="text-davinci-003",
# # #         max_tokens=100,
# # #         temperature=0.8,
# # #         n=1,
# # #         # stop=["Hello World", "See you soon"],
# # #         stop=None,
# # #         timeout=15
# # #     )
# # #
# # #     if response and response.choices:
# # #         return response.choices[0].text.strip()
# # #     else:
# # #         # return "gpt can't found answer ! -_- !"
# # #         return None
# # #
# # # # ask = str(input("add the you qustion !!! :: "))
# # #
# # # answer = generate_response("привет как твой дела какая погода сегодня в самарканде ")
# # #
# # # print(answer)
# #
# #
# # import openai
# #
# # Key = "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"
# #
# # openai.api_key = Key
# #
# # def generate_response(text):
# #     response = openai.ChatCompletion.create(
# #         model="gpt-3.5-turbo",  # или "gpt-4" если у вас есть доступ
# #         messages=[{"role": "user", "content": text}],
# #         max_tokens=100,
# #         temperature=0.8,
# #         n=1,
# #         stop=None,
# #         timeout=15
# #     )
# #
# #     if response and response.choices:
# #         return response.choices[0].message["content"].strip()
# #     else:
# #         return None
# #
# # answer = generate_response("привет, как твои дела? какая погода сегодня в Самарканде?")
# # print(answer)
#
#
# import openai
#
#
# Key = "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"
#
# openai.api_key = Key
#
# def generate_response(text):
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[{"role": "user", "content": text}],
#             max_tokens=50,
#             temperature=0.7,
#             n=1,
#             stop=None,
#             timeout=15
#         )
#
#         if response and response.choices:
#             return response.choices[0].message["content"].strip()
#         else:
#             return "Ответ не получен."
#     except openai.error.RateLimitError:
#         return "Ошибка: превышен лимит запросов. Проверьте ваш план и квоты на платформе OpenAI."
#
#
# answer = generate_response("Привет, как твои дела?")
# print(answer)
