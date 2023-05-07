
from langchain import OpenAI, ConversationChain, LLMChain, PromptTemplate
from langchain.chains.conversation.memory import ConversationalBufferWindowMemory
from langchain.prompts import PromptTemplate
from langchain.evaluation.qa import QAEvalChain
from langchain.evaluation.qa import *
from langchain.utilities import GoogleSearchAPIWrapper
import os

os.environ["GOOGLE_API_KEY"] = ""
os.environ['OPENAI_API_KEY'] = ''
hasQuit = bool(0)

examples = [
    {
        "query": "What did the president say about Ketanji Brown Jackson",
        "answer": "He praised her legal ability and said he nominated her for the supreme court."
    },
    {
        "query": "What did the president say about Michael Jackson",
        "answer": "Nothing"
    }
]

llm = OpenAI(temperature = 0.9)
example_gen_chain = QAGenerateChain.from_llm(llm=llm)
#new_examples = example_gen_chain.apply_and_parse(input_list=examples)

#examples += new_examples

template = """Assistant is a large language model trained by OpenAI.
{history}
Human: {human_input}
Assistant:"""

predictions = QAEvalChain.apply(self=predictions,input_list=examples)
llm = OpenAI(temperature=0)
eval_chain = QAEvalChain.from_llm(llm)

global gpt3_chain; gpt3_chain = LLMChain(llm=OpenAI(temperature = 0), 
       prompt=prompt,
       verbose=False,
       memory = ConversationalBufferWindowMemory(k=3)
)

def main():
    human_input = input("User: ")
    output = gpt3_chain.predict(human_input=human_input)
    print("LLM: "+output)
    print(gpt3_chain.generate(input_list=human_input))

while True:
    if not hasQuit:
        main()
    else:
        quit()

