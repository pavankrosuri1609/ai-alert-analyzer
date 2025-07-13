from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
print(llm.predict("Summarize this: 5 errors occurred while connecting to MQ server."))

