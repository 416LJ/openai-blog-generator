
import dotenv
import openai
dotenv.dotenv_values()
config = dotenv.dotenv_values(".env")

# config["NAME of API KEY"] to use keys from .env files
openai.api_key = config["OPENAI_KEY"]
keep_blogging = True

def generate_blog(paragraph_topic):
  response = openai.completions.create(
    model = 'gpt-3.5-turbo-instruct',
    prompt = 'Write a paragraph about the following topic. ' + paragraph_topic,
    max_tokens = 400,
    temperature = 0.3
  )

  retrieve_blog = response.choices[0].text
  return retrieve_blog

print(generate_blog(input("What topic would you like to blog about today? ")))

while keep_blogging == True:
    print("\n")
    ans = input('Would you like to continue blogging? Y for yes, anything else for no. ')
    print("\n")
    if ans == "Y":
       print(generate_blog(input("What topic would you like to blog about? ")))
       print("\n")
    else:
       print("Thanks for using the blogger ai.")
       print("\n")
       keep_blogging = False


