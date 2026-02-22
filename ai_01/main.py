from openai import OpenAI
from dotenv import load_dotenv
import os
#from agents import Agent, Runner
#import asyncio

load_dotenv()
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")


client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# fact_check_instructors = """
# Context:
# You are fact checker who verfies the accuracy of the statements.

# Instructions:
# When given a statement, carefully analyze its factual accuracy using your knowledge.

# Input:
# You will receive a statement that requires fact checking.

# Output:
# Respond with:
# 1. A verfict prefix: either "✅True" or ❌"False".
# 2. A brief, one sentence explanation justifying your conclusion
# """

fact_checker_message = [
    {
        "role": "system",
        "content": "You are fact checker who verfies the accuracy of the statements.",
        "instruction": "When given a statement, carefully analyze its factual accuracy using your knowledge.",
        "input": "You will receive a statement that requires fact checking.",
        "ouput": "A verfict prefix: either ✅True or ❌False."
    },
    {
        "role": "user",
        "content": "Is tendons tissue which connect muscel to bone"
    }
    ]

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=fact_checker_message
)
# response = client.chat.completions.create(
#     model = "gemini-2.5-flash",
#     messages=fact_check_instructors
# )

print(response.choices[0].message)

# fact_checker_agent = Agent(
#     name = "Fast Checker",
#     instructions = fact_check_instructors,
#     model = "gemini-2.5-flash"
# )


# print(f'Agnet {fact_checker_agent.name} Created Successfully')
# statement = "Is tendons tissue which connect muscel to bone"

# async def main():
#     response = await Runner.run(
#         starting_agent = fact_checker_agent,
#         input = statement
#     )

#     print(response)

# if __name__ == "__main__":
#     asyncio.run(main())