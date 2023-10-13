from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext, set_global_service_context

service_context = ServiceContext.from_defaults(llm="local")
set_global_service_context(service_context)

documents = SimpleDirectoryReader(input_files=["./data/sample.txt"]).load_data()
index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()
prompt = input("Enter prompt: ")
response = query_engine.query(prompt)

print(response)
