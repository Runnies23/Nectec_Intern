from Prompt import *
import json
import os 

Learning_goal = 'python'
Time = '1 month'

# Learning_goal = input("Enter Learning Goal : ")
# Time = input("Enter Time : ")
Topic = "python"
Response = []

Task_1_Required_response = QueryTyphoon_70b(Task_1_Required(Learning_goal,Time))
Task_1_Required_response_Json = json.loads(Task_1_Required_response)
del Task_1_Required_response

if Task_1_Required_response_Json['Decision'] ==  "Not Achievable":
    print(f"""Because {Task_1_Required_response_Json['Reason']}""")
    for index,i in enumerate(Task_1_Required_response_Json['Choice_Path']):
        print(f"{index+1} : {i['PATH']}\n\t- {i['Detail']}")
else:
    print(Task_1_Required_response_Json['Decision'])


topic_list_query = QueryTyphoon_70b(Prompt=topic_list_prompt(Topic),token=2024)
topic_list_json = json.loads(topic_list_query)
topic_list = [i['Topic'] for i in topic_list_json]
Topic_list_text = []
for i in topic_list:
    Topic_list_text.append(f"\t- {i}")
Topic_list_text_ = '\n'.join(Topic_list_text)
print(Topic_list_text_)

Task2_First_question_Query = QueryTyphoon_70b(Task2_First_question_prompt(Topic))
Task2_First_question_Json = json.loads(Task2_First_question_Query)
print(f"Question : {Task2_First_question_Json['Question']}\n")
for index, i in enumerate(Task2_First_question_Json['Choices']):
    print(f"""{index+1}. {i['text']}""")

weight = [i['weight'] for i in Task2_First_question_Json['Choices']]
print(f'\n{weight}')

decision = int(input("Enter Choice : ")) -1 
Response.append({
    "Question" : Task2_First_question_Json['Question'],
    "Topic" : f"Overview of {Topic}",
    "Level" : "Medium",
    "Answer" : (Task2_First_question_Json['Choices'][decision]['weight'], Task2_First_question_Json['Choices'][decision]['text']),
    "Best Answer" : (weight[weight.index(max(weight))], Task2_First_question_Json['Choices'][weight.index(max(weight))]['text']),
    "Chain_of_Thought" : None
})

while len(Response) < 10:
    print(len(Response) + 1)
    Task2_Loop_question_Query = QueryTyphoon_70b(Task2_Loop_question_prompt(topic_list,Previous_Question_Text(Response)))
    Task2_Loop_question_Json = json.loads(Task2_Loop_question_Query)
    print(f"Question : {Task2_Loop_question_Json['Question']}\n")
    for index, i in enumerate(Task2_Loop_question_Json['Choices']):
        print(f"""{index+1}. {i['text']}""")

    #================================================
    weight = [i['weight'] for i in Task2_Loop_question_Json['Choices']]
    print(f'\n{weight}')
    #================================================

    decision = int(input("Enter Choice : ")) -1 
    Response.append({
        "Question" : Task2_Loop_question_Json['Question'],
        "Topic" : f"{Task2_Loop_question_Json['Topic']}",
        "Level" : f"{Task2_Loop_question_Json['Level']}",
        "Answer" : (Task2_Loop_question_Json['Choices'][decision]['weight'], Task2_Loop_question_Json['Choices'][decision]['text']),
        "Best Answer" : (weight[weight.index(max(weight))], Task2_Loop_question_Json['Choices'][weight.index(max(weight))]['text']),
        "Chain_of_Thought" :  Task2_Loop_question_Json['Chain_of_Thought']
    })


Task2_Level_measure_Query = QueryTyphoon_70b(Task2_Measure_prompt(Previous_Question_Text(Response)))
Task2_Level_measure_Json = json.loads(Task2_Level_measure_Query)

Task2_final_each_level_Query = QueryTyphoon_70b(Task2_3_eachtopic(Topic,Topic_list_text_,Task2_Level_measure_Json["Level"],Previous_Question_Text(Response)),token=2048)
Task2_final_each_level_Json = json.loads(Task2_final_each_level_Query)

Task2_final_each_level = []
print(f"Student Level : {Task2_Level_measure_Json['Level']}")
for i in Task2_final_each_level_Json:
    Task2_final_each_level.append(f"- {i['Topic']} : {i['Knowledge_Level']}")

Task2_final_each_level_Text = '\n\t'.join(Task2_final_each_level)
print(Task2_final_each_level_Text)

Task3_Query = QueryTyphoon_70b(Task3_Prompt(Time,Task2_final_each_level_Text,Task2_Level_measure_Json['Level']),token=2048)
Task3_Json = json.loads(Task3_Query)
print(Task3_Json)

print("End the process")