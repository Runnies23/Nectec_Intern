import pandas as pd 

Question_bank_df =  pd.read_csv("Question_bank_Python/Concat_Question_Bank_Topic_V2_BIG_Clearning.csv")
df_concept = pd.read_csv('Question_bank_Python/Question_bank_v2.csv')

def Select_topic_and_level(Content,Level,DF=Question_bank_df):
    if Content and Level:
        Easy = [DF['Index'].iloc[i] for i in range(len(DF)) if DF['Level'].iloc[i] == Level and DF['Topic'].iloc[i] == Content]
        return Easy
    
def Question_bank_by_Index(Question_bank_index):
    Question_bank_Text  = []
    for index,i in enumerate(Question_bank_index):
        Question_bank_Text.append(f"Question : {Question_bank_df['Question'].iloc[i]}\nTopic : {Question_bank_df['Topic'].iloc[i]}\nLevel : {Question_bank_df['Level'].iloc[i]}")    

    Question_bank_Texts = '\n'.join(Question_bank_Text)
    return Question_bank_Texts

def Prompt_Func(Question_bank_topics, Previous_Text):
    Prompt = f"""You are the **Greatest of All Time** (GOAT) in Python programming mentorship. Your deep knowledge allows you to create custom-tailored learning paths that can challenge and elevate even the brightest minds. 

Your student is exceptionally talented—holding the title of **Best Python Programmer** for 5 consecutive years. They have a strong grasp of fundamentals and can quickly adapt to new challenges. However, your mission is to push their boundaries and expose any subtle gaps in their understanding.

**Key Guidance for Crafting the Questions**:

1. **Question Adaptation**:
    - You have **10 questions** to assess the student's knowledge. Each question should adapt based on their answers.
    - If the student answers a question **correctly and with ease**, the next question should shift to a **harder topic** or increase in difficulty. For example:
        - If the student handles a question on **Functions** with ease, the next could be on **Decorators and Context Managers** or **OOP**.
        - If they excel in **basic error handling**, challenge them with **advanced debugging scenarios** or **complex exception handling**.
    - Aim to **change the topic** approximately every 2 questions, ensuring the student faces a broad range of topics.

2. **Data at Your Disposal**:
    - You have access to the 'Previous Questions' data, including:
        - 'question': The text of the question.
        - 'Topic': The topic covered.
        - 'Answer': The student's response.
        - 'Best Answer': The ideal answer.
        - 'Choice Weights': Indicates the relative correctness of each choice.
        - 'Previous Chain of Thought': The rationale behind selecting each question.
    - The list of 'Question Bank Topics' includes:
        {Question_bank_topics}

3. **Your Mission: Recommend the Next Question**:
    - You have two modes for selecting the next question:
        - **Mode 1: Query in Question Bank**:
            - Select a question based on topic and difficulty (Easy, Medium, Hard).
            - If a student consistently answers correctly, **escalate to a higher difficulty or advanced topic**.

4. **Be More Sensitive to Their Performance**:
    - If a student answers a question well, **quickly adapt** and provide a harder question—even if it means skipping intermediate steps.
    - Adjust the 'Chain_of_Thought' to reflect why you are making these jumps in difficulty or switching topics. For example:
        - "The student answered a medium question on loops effortlessly, so I chose a hard question on nested loops and recursion."
        - "Their quick understanding of basic OOP concepts suggests readiness for abstract classes and polymorphism."
    - Always include in your reasoning how the current question aims to **uncover deeper insights** into their strengths and potential areas for growth.

5. **Priority**: The question and answer should be in Thai, and your response should strictly follow the JSON format. No additional explanation is required.

Previous Questions:
{Previous_Text}

```
JSON Format for a Question from the Question Bank:
{{
    "Mode": 1,
    "Topic": "(topic)",
    "Level": "Easy" | "Medium" | "Hard",
    "Chain_of_Thought": "(Explain why this question was selected, how it escalates the challenge, and your reasoning for changing the topic or difficulty level. Focus on why an advanced topic was chosen if applicable)"
}}
```"""
    return Prompt