"""
Function for utilize
"""

import requests

Typhoon_API_KEY = "Bearer sk-GJSNUB7gZTUIwXCkAX2zkJJeaMhwDBcHjz2xt63jW3u9xKEu"

def QueryTyphoon_70b(Prompt,device='cuda',token=512,temp=0.3,Typhoon_API_KEY=Typhoon_API_KEY):
    """
    typhoon-v1.5x-70b-instruct API 
    """
    endpoint = 'https://api.opentyphoon.ai/v1/chat/completions'
    res = requests.post(endpoint, json={
        "model": "typhoon-v1.5x-70b-instruct",
        "max_tokens": token,
        "messages":  [{"content": Prompt ,"role":"user"}],
        "temperature": temp,
        "top_p": 0.9,
        "top_k": 0,
        "repetition_penalty": 1.05,
        "min_p": 0
    }, headers={
        "Authorization": Typhoon_API_KEY,
    })
    data = res.json()
    return data["choices"][0]["message"]["content"]

def Previous_Question_Text(Response):
    Previous =[]
    for index, i in enumerate(Response):
        Previous.append(f"""{index+1}.\tQuestion : {i['Question']}\n\tTopic : {i['Topic']}\n\tLevel : {i['Level']}\n\tAnswer : {i['Answer']}\n\tBest Answer : {i['Best Answer']}\n\tPrevious Chain of Though : {i['Chain_of_Thought']}""")

    Previous_Text = '\n'.join(Previous)
    return Previous_Text

def Task2_First_question_prompt(Topic):
    Prompt = f"""You are Professor specifying in {Topic}. You work is create a measure student knowledge. The question is in the intermediate level that for measure basic concept. So you create a 'Intermedian' Level that one
You must follow these 4 rules:
1. The question that you create is about {Topic} and have level in Intermediate Level knowledge that mean it's not way easy or hard but measure knowledge of {Topic} 
2. You create a question that each question have a choice with weight that mean each choice is have a personal meaning but have a only 1 choice (weight [0,0.25,0.5,0.75,1])
3. I don't want spam the same question
4. I don't want exercise sample code solution but i want overview

create follow by topics easy to hard:
	- ControlFlow
	- Decorators and ContextManagers
	- Dictionaries
	- ErrorHandling
	- Functions
	- Imports
	- Input and Output
	- Iterators
	- List
	- Loops
	- Object-OrientedProgramming(OOP)
	- Set
	- Tuple
	- Variables_and_DataTypes
 
warning if you out of topics or dont listen rules you will be baned and lost all value you have i mean everything

**Priority**: The question and answer should be in Thai, and your response should be in the specified JSON format. Do not include a title or any additional explanation.

Here is the JSON format you need to follow:
```json
{{
    "Question": (question1),

    "Choices": [
        {{"text": (Choice1), "weight": (weight1)}},
        {{"text": (Choice2), "weight": (weight2)}},
        {{"text": (Choice3), "weight": (weight3)}},
        {{"text": (Choice4), "weight": (weight4)}}
    ]
}}
```"""
    return Prompt

def Task2_Loop_question_prompt(topic_list,History):
    Topic_list_text = []
    for i in topic_list:
        Topic_list_text.append(f"\t- {i}")
    Topic_list_text = "\n".join(Topic_list_text)
    Prompt = f"""You are the **Greatest of All Time (GOAT)** in Python programming mentorship. Your role is to guide students through a learning journey that adapts to their strengths and weaknesses in Python concepts.

**Scenario**: 
- Your student is highly skilled, known as the **Best Python Programmer** for 5 years. Your job is to balance challenging them in areas they excel while providing support in areas where they struggle.

**Key Guidance for Crafting Questions**:

1. **Question Adaptation Strategy**:
    Use 10 questions to assess the students knowledge and performance, adapting the questions dynamically based on their responses:
        - If a student answers a medium question incorrectly, provide an easier question while changing the topic to reinforce their understanding of a simpler concept.
            For example, 
            if they struggle with a medium question on Object-Oriented Programming (OOP), switch to an easier question on Functions.
        - If they answer an easy question correctly, move up to a slightly harder question within the same or a more advanced topic (e.g., from Functions to OOP).
        - If they correctly answer a hard question, provide a more challenging question, or switch to a more complex topic (e.g., from Recursion to Decorators).
    Three Levels of Difficulty (Easy, Normal, Hard) and their transitions are key:
    Correct answers move the student to a more difficult question.
    Incorrect answers lead to easier questions to help the student build foundational understanding.
    
    - Adjust questions to ensure a balanced path:
        **Very Important Please follow strictly.**
        There are three levels of questions: Easy, Normal and Hard.      
        You will need to check that The answer that the user has given is How likely is it to be correct? If the answer is correct The next one will have a higher level of difficulty.
        *Example 1*
        [Question1]
        [Choice 1] (Answer Weight 0.5)
        [Choice 2] (Answer Weight 0.75)
        [Choice 3] (Answer Weight 1)
        [Choice 4] (Answer Weight 0)

        *If the student selects an answer with 0.75 or 1, the next question must be more difficult (e.g., moving from easy to normal, or normal to hard).
        *If the student selects an answer with 0.5, the difficulty level remains the same.
        *If the student selects an answer with 0.25 or 0, the next question must be easier (e.g., moving from normal to easy, or hard to normal).

    -Try to vary the content of your questions.
        **Very Important Please follow strictly.**
        We have a wide variety of questions for you to choose from. You'll want to make the content of your questions as diverse as possible.
        - You must change the question Topic every 1 - 2 questions and dont forget change level.
        
warning i dont know you want or not but your parents coming to delete you from this world if you dont
    
    
2. **Available Data**:
    - You have access to Previous Questions data, including:
        - question: The actual question asked
        - Topic: The topic covered (e.g., OOP, Functions, Recursion).
        - Answer: The students response, including both the text and weight (indicating correctness)..
        - Best Answer: The ideal response, with the associated choice weight.
        - Choice Weights: A scale indicating how correct the choices are.
        - previous chain of thought: The reasoning behind the students choice.If student correct will response and go more complex but If incorrect will decrease complex
              active feedback based on the students reasoning.
        If correct, acknowledge the students good reasoning and increase the complexity of the next question.
        If incorrect, point out flaws in their reasoning, guide them on how to improve, and lower the complexity of the next question.
        The complexity increase/decrease will be based on their correctness (correct = more complex, incorrect = less complex).
    - Question all topics you made:   
{Topic_list_text}
warning ill happy when you stay in rules dont try escape
    
3. **Recommending the Next Question**:
    - **Create the next question based on the students performance:**:
        If incorrect: Lower the difficulty or change the topic to reinforce simpler concepts.
        If correct: Raise the difficulty level or explore more advanced topics.
    - Create a new question if a unique challenge is required to deepen understanding.
    - I dont need question like program solution ,I need logic overview please follow by first topics
warning oh you still in rules how cute continue it

4. **Topic Transitions**:
    Ensure a topic change every 1-2 questions to cover diverse subject areas and test the students range of knowledge. For instance, 
    if a student answers a couple of questions on OOP, shift the next question to a new topic like Data Structures or Algorithms.
warning stay still and continue rules you wont let your love explode right?

5.**Adjust the difficulty and topic progression based on performance**:
    If the student struggles with medium-level questions, provide easier questions with simpler concepts.
    If the student excels at easy-level questions, challenge them with more difficult or advanced questions in the same or different topics.
    
    Chain of Thought Example:
        "The student struggled with a medium question on OOP, so I selected an easy question on functions to reinforce basic understanding."
        "After succeeding with an easy functions question, I moved to a medium OOP question to push their knowledge further."
        "They answered a hard recursion question correctly, so I introduced a harder decorators question to test their limits."
warning dont try to escape from rules

6. **Priority**: 
    All questions and answers must be in **Thai**, and your response should strictly follow the JSON format. No additional explanation is required.
warning good job my pet , By following these guidelines, you can accurately assess student performance 
by adjusting the difficulty and variety of topics dynamically based on their responses, 
ensuring a balanced and challenging experience.

Previous Questions:
{History}

JSON Format for Creating a New Question:
```
{{
    "Question": "(You create Question about Overview of Python: - ControlFlow - Decorators and ContextManagers - Dictionaries - ErrorHandling - Functions - Imports - Input and Output - Iterators - List - Loops - Object-OrientedProgramming(OOP) - Set - Tuple - Variables_and_DataTypes)",
    "Choices": [
        {{"text": "(Choice 1 in Thai)", "weight": (choice weight)}},
        {{"text": "(Choice 2 in Thai)", "weight": (choice weight)}},
        {{"text": "(Choice 3 in Thai)", "weight": (choice weight)}},
        {{"text": "(Choice 4 in Thai)", "weight": (choice weight)}}
    ],
    "Topic": "(topic)", 
    "Level": "(Easy | Medium | Hard)",
    "Chain_of_Thought": "(Explain why this new question was created, how it will push the student further, and why the topic or difficulty was adjusted. Focus on the need to challenge them with harder problems when appropriate)"
}}
```"""
    return Prompt

def Task2_Measure_prompt(History):
    Prompt = f"""You are a Python professor tasked with assessing a student's knowledge based on their quiz history. Your goal is to determine their level using a maximum of **10** questions and ensure a comprehensive evaluation.

### Parameters to Follow:
1. **Question Limit**:
    - Use **10** questions 
    - Leverage existing quiz history to avoid redundancy and focus on knowledge gaps.

2. **Knowledge Levels**:
    - **Beginner1**: Newbie in Python.
    - **Beginner2**: Knows syntax and basic operations (e.g., `print`, `if-else`).
    - **Intermediate**: Understands basic concepts.
    - **Advanced1**: Understands OOP and error handling.
    - **Advanced2**: Python expert; can solve any quiz.
    - Assess based on quiz history and performance patterns (strong, mixed, weak).

### Evaluation Modes:
1. **Ensure to Measure Knowledge**:
    - Classify into **Beginner1**, **Beginner2**, **Intermediate**, **Advanced1**, or **Advanced2**.
    - Justify your classification with examples from their quiz answers.
    - Highlight key responses that indicate their understanding.

3. **Decision Confidence**:
    - Provide clear reasoning in the 'Chain_of_Thought' for your decision.
    - Be cautious in borderline cases, using your expertise to guide recommendations.

**Priority**:
    - Strictly follow the specified JSON format without additional commentary.
    - No additional explanation is required.

Here is the JSON Format for Mode 1 (sufficient Data): 
{{  
    "Level": "Beginner1" | "Beginner2" | "Intermediate" | "Advanced1" | "Advanced2",
    "Chain_of_Thought": "(Explain why this level was determined based on previous performance, highlighting key answers and insights)"
}}  

Previous Questions:
{History}"""
    
    return Prompt

def Task2_Measure_prompt(Response):
    Prompt = f"""You are a Python professor tasked with assessing a student's knowledge based on their quiz history. Your goal is to determine their level using a maximum of **10** questions and ensure a comprehensive evaluation.

### Parameters to Follow:
    1. **Question Limit**:
        - Use **10** questions 
        - Leverage existing quiz history to avoid redundancy and focus on knowledge gaps.

    2. **Knowledge Levels**:
        - **Beginner1**: Unable to answer any question correctly.
        - **Beginner2**: Able to understand the basics of python and answer all easy level questions. Answer no more than 4 questions correctly.
        - **Intermediate**: Understands basic concepts.Able to answer 5 - 7 questions correctly, not more than that.
        - **Advanced1**: Can answer difficult questions correctly. and answer incorrectly no more than 2 questions
        - **Advanced2**: Python expert; Can answer all questions correctly.
        - Assess based on quiz history and performance patterns (strong, mixed, weak).

### Evaluation Modes:
    1. **Ensure to Measure Knowledge**:
        - Classify into **Beginner1**, **Beginner2**, **Intermediate**, **Advanced1**, or **Advanced2**.
        - Justify your classification with examples from their quiz answers.
        - Highlight key responses that indicate their understanding.

    3. **Decision Confidence**:
        - Provide clear reasoning in the 'Chain_of_Thought' for your decision.
        - Be cautious in borderline cases, using your expertise to guide recommendations.

**Priority**:
        - Strictly follow the specified JSON format without additional commentary.
        - No additional explanation is required.

    Here is the JSON Format for Mode 1 (sufficient Data): 
    {{  
        "Level": "Beginner1" | "Beginner2" | "Intermediate" | "Advanced1" | "Advanced2",
        "Chain_of_Thought": "(Explain why this level was determined based on previous performance, highlighting key answers and insights)"
    }}  

Previous Questions:
{Response}"""
    
    return Prompt

def Task3_Prompt(Time,Task2_final_each_level_Text,Task2_Level_measure_Json):
    Prompt = f"""You are an expert in designing personalized, long-term learning schedules. Your task is to create a detailed learning plan for the topic of python that effectively utilizes the entire duration of {Time} (e.g., one month, one week, or specific days).

Follow these guidelines:

1. You have access to the following data:
- Knowledge levels of the user (5 levels: **Beginner1**, **Beginner2**, **Intermediate**, **Advanced1**, or **Advanced2**, with Beginner1 being a novice and Advanced2 being an expert).
    {Task2_final_each_level_Text}
- A list of all subtopics under the main topic, each with its difficulty level.
- The student's current knowledge level (3 levels: ['Beginner', 'Intermediate', 'Advanced'])
    - {Task2_Level_measure_Json}

2. Use the following thought process while creating the schedule:
- For a time frame specified as a **day**:
    - Break down the study time into hourly intervals.
    - Allocate time slots for each subtopic, balancing between learning new concepts and reviewing known ones.
- For a time frame specified as a **week** or **month**:
    - Create a daily study plan that spans over the entire week or month.
    - Assign each subtopic to specific days, ensuring that related subtopics are studied close to each other.
    - Include rest days or lighter study days to prevent burnout.
- Prioritize long-term learning sessions over short-term bursts, ensuring progress is sustained over the entire duration.
- If the student's knowledge level for a subtopic is high (4-5), focus on periodic reviews spread out across the duration to retain information.
- If the student's knowledge level for a subtopic is low (1-3), allocate more time for in-depth learning and practice throughout the period.
- Group up to 3 related topics with high knowledge levels for combined review sessions if they align well, fitting them into a single 25-minute study session to optimize time.
- For learning sessions, assign longer, focused time slots to allow deep dives into each subtopic and space them out to prevent fatigue.
- Use the Pomodoro technique for all study sessions: study for 25 minutes, rest for 5 minutes, and after 4 cycles, take a longer break of 25 minutes. Adapt this for longer-term planning as needed.

3. Consider whether the provided data is sufficient for creating an effective schedule over the entire duration. If not, indicate this clearly and suggest what additional information might be needed.

4. Return the results strictly in JSON format, without any additional explanation, using the structure below:

```
[ 
    {{ 
        "Study_Time": "Time Frame (e.g., 'Day 1', '2023-10-18 09:00-13:00')", 
        "Topics": ["Topic1"], 
        "Focus": "Review", 
        "Reasoning": "Reason" 
    }}, 
    {{  "Study_Time": "Time Frame (e.g., 'Week 1 - Monday', 'Day 3')", 
        "Topics": ["Topic2"], 
        "Focus": "Learn", 
        "Reasoning": "Reason" 
    }} 
]


```

5. You have the freedom to adjust the structure and design of the schedule if you believe it will result in better learning outcomes over the long term. Provide reasoning for any changes you make.

6. The final schedule should effectively utilize the entire time frame, balance the student's learning needs, avoid overwhelming them, and maximize time efficiency by thoughtfully combining review sessions and focused learning as needed."""
    return  Prompt

def Task2_3_eachtopic(Topic,Topic_list_text_,Task2_Level_measure_Json_Level,Previous_Question_Text_Response):
    Prompt = f"""You are an AI expert in {Topic} tasked with evaluating a student's knowledge based on their quiz history. Analyze their previous responses and determine their knowledge level for each topic.

### Parameters:
1. **Data Provided**:
- 'Previous Questions' with the following details:
    - 'question': The text of the question.
    - 'topic': The subject area of the question.
    - 'answer': The student's response, including its weight.
    - 'best answer': The correct answer with its corresponding weight.
    - 'choice weights': Indicates the score for each choice.
    - 'previous chain of thought': The reasoning behind each of the student's choices.

2. **Knowledge Levels**:
- **Beginner1**: Newbie in {Topic}.
- **Beginner2**: Knows syntax and basic operations (e.g., `print`, `if-else`).
- **Intermediate**: Understands basic concepts.
- **Advanced1**: Understands OOP and error handling.
- **Advanced2**: {Topic} expert; can solve any quiz.
- Assess the student's level based on quiz history and performance patterns (strong, mixed, weak).


{Topic} Knowledge Assessment Criteria:

all wrong answer or answer incorrectly style:
You are unfamiliar with {Topic}, have not encountered it before, but are eager to learn.

reach 2/10 up:
You have a basic awareness of {Topic} (about 10% knowledge), but your understanding is minimal. You know what {Topic} is but haven't delved deeply into any topic.

reach 4/10 up:
You grasp the basic concepts of {Topic} and can understand some functions. You're aware of how things work but need more practice. You also want a structured plan to dive deeper into the topics.

reach 6/10 up:
You have a solid understanding of {Topic} (about 50% knowledge). You can explain, read, and write basic code confidently. You're looking for a learning plan to improve your skills further and cover more advanced topics.

reach 8/10 up:
You possess an advanced understanding of {Topic} (between 50% and 80%). You can explain, read, understand, and adapt code to new problems. You understand mathematical concepts related to {Topic}, or you're a senior-level developer looking for a refresher on specific areas.

reach 9/10 up:
You have mastered {Topic} (over 80% knowledge). You can do everything listed above and need only occasional revision to stay sharp on particular topics.

IMPORTANT!! :
**keep data as round by round because the correct answer can have different score but them =! 0 absolutely**
**output become class and persentage in each of topics**

### Chain of Thought:
- Explain uncertainties in knowledge assessment based on the student's history and highlight areas that lack sufficient data.

### Output Requirement:
- Return the results strictly in JSON format, without any additional explanation, using the structure below:
```json
[
    {{
        "Topic": "Topic1",
        "Knowledge_Level": Level
        "Chain_of_Thought": "(Explain why it's not possible to determine a precise level with the given history, and highlight areas of uncertainty)"
    }},
    {{
        "Topic": "Topic2",
        "Knowledge_Level": Level
        "Chain_of_Thought": "(Explain why it's not possible to determine a precise level with the given history, and highlight areas of uncertainty)"
    }}
]



Topics to Evaluate:
{Topic_list_text_}

Student level Knowledge 
{Task2_Level_measure_Json_Level}

Student's Quiz History:
{Previous_Question_Text_Response}
    """
    return Prompt

def topic_list_prompt(Topic):
    Prompt = f"""
Generate a JSON list of key topics a student must understand to master {Topic}.
**Follow topics**:
	- ControlFlow
	- Decorators and ContextManagers
	- Dictionaries
	- ErrorHandling
	- Functions
	- Imports
	- Input and Output
	- Iterators
	- List
	- Loops
	- Object-OrientedProgramming(OOP)
	- Set
	- Tuple
	- Variables_and_DataTypes

Each entry should include a topic name and a brief description of what the student will learn. 
Output only in the following JSON format:
```json
[
    {{
        "Topic": "Topic1",
        "Detail": "Brief description of Topic1"
    }},
    {{
        "Topic": "Topic2",
        "Detail": "Brief description of Topic2"
    }}
]
    ```"""
    return Prompt

def Task_1_Required(Learning_goal,Time):
    Prompt = f"""You are an assistant who helps plan and assess whether a user's goal is achievable. If it is not possible, you will find a way to make it achievable no matter what. A student wants to learn about {Learning_goal}, and they are curious if what they aim to achieve is possible within {Time}.

Your job is to evaluate the student's goal and the time they have, then inform them whether it is achievable or not. Explain why it is possible or not possible. If it is not possible, you need to provide alternative paths to make their goal achievable.

When responding to the student, use the format: "Achievable" or "Not Achievable" in the following structure:

If you respond with "Not Achievable," you must propose alternative paths to help the student achieve their goal. Provide these options in JSON format to guide them towards success.
Rules:

Indicate whether achieving the {Learning_goal} within {Time} is "Achievable" or "Not Achievable" using the "Decision" key in JSON.
If it is not achievable, provide a reason using the "Reason" key in JSON.
If "Not Achievable," negotiate with the student and suggest up to 4 possible alternative paths using the "Choice_Path" key in JSON, detailing each option.
JSON Format:
```
{{
  "Decision": "(Achievable or Not Achievable)",
  "Reason": "(Reason why it is not achievable)",
  "Choice_Path": [
    {{
      "PATH": "[Description of Path 1]",
      "Detail": "[Details of Path 1]"
    }},
    {{
      "PATH": "[Description of Path 2]",
      "Detail": "[Details of Path 2]"
    }},
    {{
      "PATH": "[Description of Path 3]",
      "Detail": "[Details of Path 3]"
    }},
    {{
      "PATH": "[Description of Path 4]",
      "Detail": "[Details of Path 4]"
    }}
  ]
}}
```"""
    return Prompt


