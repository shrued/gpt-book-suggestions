import os
import openai

openai.api_key = "OPENAI_API_KEY"

genreDataObj = {}
genreDataObj["whichTV"] = input("Enter a TV type (e.g. movie or tv show): ")
genreDataObj["genre"] = input("Enter a genre (e.g. sci-fi, romance, etc.): ")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"Suggest a {genreDataObj['whichTV']} in the {genreDataObj['genre']} genre:",
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.6
)

print(response["choices"][0]["text"])
