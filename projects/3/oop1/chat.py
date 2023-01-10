import openai

openai.Completion.create(
  engine="davinci",
  prompt="Tell me story about students.",
  api_key="",
)
