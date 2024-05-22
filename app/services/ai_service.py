import openai

openai.api_key = 'sk-proj-Z8pp38lMYDv3kmHkCrS5T3BlbkFJ8Dk3RhDvrRqS1ffyAU51'

def generate_latex(user_data):
    prompt = f"Generate LaTeX code for a resume with the following details: {user_data}"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=1000
    )
    return response.choices[0].text.strip()
