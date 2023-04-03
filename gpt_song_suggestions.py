import os
import openai

openai.api_key = "OPENAI_API_KEY"

musicGenre = input("Enter a genre to get a song recommendation (e.g. pop, rap, etc.): ")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"Suggest a song in the {musicGenre} genre:",
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.6
)

print(response["choices"][0]["text"])
