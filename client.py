from text_generation import Client

endpoint_url = "my_endpoint_url"

client = Client(endpoint_url)
text = client.generate("Why is the sky blue?").generated_text
print(text)

# Token Streaming
text = ""
for response in client.generate_stream("Why is the sky blue?"):
    if not response.token.special:
        text += response.token.text

print(text)
