import os
import openai

openai.api_key = "create your own key"


def get_category(comment):
  restart_sequence = "\n"
  response = openai.Completion.create(
    engine="text-davinci-002",
    prompt="The following is a feedback given by a costumer:\n\n\"{}\"\n\nThe only possible categories are: [cleanness], [crowded], [delayed], [staff], [sound], [food]\n\nthe feedback would belong to the category:".format(comment),
    temperature=0,
    max_tokens=6,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["\n"]
  )
  return response.choices[0]["text"][2:-1]
