import openai
from config import config

input_example = "--- a/requirements.txt\
+++ b/requirements.txt\
@@ -1 +1,2 @@\
 GitPython==3.1.44\
+openai==1.90.0\
\ No newline at end of file"

documentation_example = {
    "data": "# requirements\n- openai==1.90"}

def message(data, role="user"):
    return {
        "role": role,
        "content": "".join(data)
    }

def ask(client, documentation=documentation_example, input=input_example):
    print(f"Sending the request to OpenAI")
    try:
        response = client.responses.create(
            model=config.MODEL,
            input=[
                message("Considering the following input:", "developer"),
                message(input),
                message("Update the following section of the documentation for developers (in Markdown):", "developer"),
                message(documentation),
            ]
        )
        print("Response received")
        return response.output_text
    except openai.AuthenticationError as e:
        print("❌ Auth Error:", e)
    except Exception as e:
        print("⚠️ Other Error:", e)