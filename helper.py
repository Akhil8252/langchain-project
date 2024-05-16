from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
import os
import json


with open('config.json') as f:
    config = json.load(f) 
    api_key = config['api_key']
os.environ['OPENAI_API_KEY'] = api_key

#in OenAi there is a variable called temperature. which specifies the creativity .if it is set to zero means it will be very safe but least creative but if it is set to 1,
# then it may give error but will be highly creative
llm = OpenAI(temperature = 0.6)

def generate_restaurant_name_items(cuisine):
    #chain 1 :-restaurant name
    prompt_tempt_name = PromptTemplate(
            input_variables=['cuisine'],
            template = "I want to open a restaurant for {cuisine} food. suggest a fancy name for this")
    name_chain = LLMChain(llm = llm, prompt=prompt_tempt_name, output_key="restaurant_name")

    # chain 2:- generating food items

    prompt_tempt_items = PromptTemplate(
                input_variables=['restaurant_name'],
                template = "suggest some food items for {restaurant_name}. return it as a comma separated file")
    item_chain = LLMChain(llm = llm, prompt=prompt_tempt_items, output_key="menu_items")


    #to get the name of restaurant we should use sequential chain rather simple sequential chain. as simple sequential change only shows the 
    #2nd output not the first output
    chain = SequentialChain(chains=[name_chain,item_chain],
                        input_variables = ['cuisine'],
                        output_variables = ['restaurant_name','menu_items']
    )

    response = chain({'cuisine':cuisine})

    return response


