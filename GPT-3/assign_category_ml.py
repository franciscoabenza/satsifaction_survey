import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

restart_sequence = "\n"

response = openai.Completion.create(
  engine="text-davinci-002",
  prompt="The following is a feedback given by a costumer:\n\n\"the woman was very rood to me and not helpful at all\"\n\nThe possible categories are: [cleanness], [crowded], [design flaw], [staff], [sound]\n\nthe feedback would belong to the category: [staff]\n",
  temperature=0,
  max_tokens=6,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=["\n"]
)