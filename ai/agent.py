import os, openai

input_example = "--- a/requirements.txt\
+++ b/requirements.txt\
@@ -1 +1,2 @@\
 GitPython==3.1.44\
+openai==1.90.0\
\ No newline at end of file"

documentation_example = "# requirements\
- openai==1.90\
"

def message(role, data):
    return {
        "role": "user",
        "content": data
    }

def ask(client, documentation=documentation_example, input=input_example):
    try:
        response = client.responses.create(
            model=os.getenv("MODEL") if os.getenv("MODEL") else "o4-mini",
            input=[
                message("developer", "Considering the following input:"),
                message("user", input),
                message("developer", "Update the following section of the documentation for developers (in Markdown):"),
                message("user", documentation),
            ]
        )
        print(response.output_text)
    except openai.AuthenticationError as e:
        print("❌ Auth Error:", e)
    except Exception as e:
        print("⚠️ Other Error:", e)