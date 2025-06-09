from transformers import pipeline
chatbot = pipeline('text-generation',model='gpt-2')
print("Chatbot LLM simples. Digite 'sair' para encerrar")

while True: 
  entrada = input("Você: ")
  if entrada.lower() = 'sair':
     break

resposta = chatbot(entrada, max_length=50,num_return_sequences=1)
[0]['generated-text']
print("Bot: ",resposta[len(entrada):].strip())
