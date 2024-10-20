import pandas as pd
import json
import os
import random
import requests
from Question_bank_Prompt import * 
from Prompt import * 

Learning_goal = input()
Time = input()
Topic = "python"
Response = []

df_concept = pd.read_csv('Question_bank_Python/Question_bank_v2.csv')
Question_bank_df =  pd.read_csv("Question_bank_Python/Concat_Question_Bank_Topic_V2_BIG_Clearning.csv")

Question_bank_topic = Question_bank_df['Topic'].unique()
Question_bank_topic = ['\t- ' + i for i in Question_bank_topic]
Question_bank_topics = '\n'.join(Question_bank_topic)

Response = []
Index_list = df_concept['Index']
Index_rand = random.choice(Index_list)
rows = df_concept.iloc[Index_rand]
print(f"Question : {rows['Question']}\n")
value = json.loads(rows['Choice'].replace("'",'"'))
weight = [i['weight'] for i in value]
for index, i in enumerate(value):
    print(f"{index+1}. {i['text']}")
print(weight)
decision = int(input()) -1 
Response.append({
    "Question" : rows['Question'],
    "Topic" : "Overview of Python",
    "Level" : "Medium",
    "Answer" : (weight[decision], value[decision]['text']),
    "Best Answer" : (weight[weight.index(max(weight))], value[weight.index(max(weight))]['text']),
    "Chain_of_Thought" : None
})

while len(Response) < 10:
    print(len(Response)+1)
    Query = QueryTyphoon_70b(Prompt_Func(Question_bank_topics,Previous_Question_Text(Response)),token=2048)
    response = json.loads(Query)
    print(response['Topic'],response['Level'])
    if response['Mode'] == 1:
        if response['Topic'] == 'Overview of Python':
            Index = Select_topic_and_level(response['Topic'],response['Level'],DF=df_concept)
            Random_Choice_Index = random.choice(Index)
            rows = df_concept.iloc[Random_Choice_Index]
        else:
            Index = Select_topic_and_level(response['Topic'],response['Level'])
            Random_Choice_Index = random.choice(Index)
            rows = Question_bank_df.iloc[Random_Choice_Index]
        print(f"Question : {rows['Question']}\n")
        value = json.loads(rows['Choice'].replace("'",'"'))
        weight = [i['weight'] for i in value]
        for index, i in enumerate(value):
            print(f"{index+1}. {i['text']}")
        print(weight)
        decision = int(input()) -1 
        Response.append({
            "Question" : rows['Question'],
            "Topic" : rows['Topic'],
            "Level" : rows['Level'],
            "Answer" : (weight[decision], value[decision]['text']),
            "Best Answer" : (weight[weight.index(max(weight))], value[weight.index(max(weight))]['text']),
            "Chain_of_Thought" : response['Chain_of_Thought']
        })
        # print(Response)

    if response['Mode'] == 2: 
        print(2)

Task2_Level_measure_Query = QueryTyphoon_70b(Task2_Measure_prompt(Previous_Question_Text(Response)))
Task2_Level_measure_Json = json.loads(Task2_Level_measure_Query)
Task2_final_each_level_Query = QueryTyphoon_70b(Task2_3_eachtopic(Topic,Question_bank_topics,Task2_Level_measure_Json["Level"],Previous_Question_Text(Response)),token=2048)
Task2_final_each_level_Json = json.loads(Task2_final_each_level_Query)
Task2_final_each_level_Json
Task2_final_each_level = []
print(f"Student Level : {Task2_Level_measure_Json['Level']}")
for i in Task2_final_each_level_Json:
    Task2_final_each_level.append(f"- {i['Topic']} : {i['Knowledge_Level']}")
Task2_final_each_level_Text = '\n\t'.join(Task2_final_each_level)
print(Task2_final_each_level_Text)
Task3_Query = QueryTyphoon_70b(Task3_Prompt(Time,Task2_final_each_level_Text,Task2_Level_measure_Json['Level']),token=2048)
Task3_Json = json.loads(Task3_Query)
print(Task3_Json)