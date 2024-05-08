from langchain.llms import VLLM
import time


llm = VLLM(model="facebook/opt-125m",
           trust_remote_code=True,  
           max_new_tokens=50,
           temperature=0.6
)


start_time = time.time()
output = llm("Who is president of US?")
end_time = time.time()
latency = end_time - start_time
print(f"Latency: {latency} seconds")
print("Generated text:", output)