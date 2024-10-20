# PlanPy : Find A Python Learning Path
This is a project internship about Adptive Learning in 1 month.

**Our Goal**
1. Understand "What is Adaptive Learning?"
2. Do a research
3. Brainstrom for creating project
4. Everyone can explain and responsible a project

## What is Adaptive Learning?
Each learner has different abilities, so learning activities should be adaptable to their individual skill levels. This requires adjusting the content, format, and feedback according to each user's performance.

## About PlanPy project
This adaptive learning project utilizes the Typhoon-V1.5x-70B-Instruct LLM API to support individuals who want to learn Python programming in a way that suits their personal style and schedule. By simply inputting the Python topics you're interested in and specifying the amount of time you have available, the system will generate a customized learning path tailored to your needs.

**What sets this project apart** is that while you can find countless Python courses online, it’s often difficult to know where to begin based on your current knowledge level, and even harder to plan your learning within your limited time. PlanPy solves this problem by creating a personalized learning experience that adapts dynamically to your abilities and time constraints. Additionally, Typhoon LLM's support for the Thai language and its user-friendly interface make it accessible to a broader audience, further enhancing the learning experience. The API also ensures detailed feedback and progress tracking, empowering users to improve continuously based on real-time performance analytics.

### Why have to use Typhoon-V1.5x-70B-Instruct API? ###
The primary reason for using the Typhoon-V1.5x-70B-Instruct API is its robust support for the Thai language, built upon the Qwen1.5 model and developed by Thai experts. This model outperforms GPT-4 on the ThaiExam (average), showcasing its superior ability to understand and generate Thai content. It is also user-friendly and free to access. The model’s versatility allows it to handle various tasks, such as generating responses for chatbots, following complex instructions, and creating content based on specific prompts. These capabilities make it an excellent choice for diverse applications, particularly those requiring advanced Thai language processing.

Try Typhoon API [here](https://huggingface.co/scb10x/typhoon-v1.5-72b-instruct)
Huggingface Model [here](https://huggingface.co/scb10x/typhoon-v1.5-72b-instruct)

## Opportunity ##
1. Our team plans to develop a platform that caters to every individual's desire to learn various topics, providing a comprehensive and personalized educational experience.
2. We aim to create a user-friendly environment, utilizing platforms like Discord bots and APIs to enhance accessibility and interaction.
3. Question Bank will integrate a diverse question bank that allows the LLM to generate more effective quizzes. This feature will provide users with engaging assessments to test their knowledge, reinforce learning, and identify areas for improvement.

**Our focus on optimizing the system**
  * Addressing Hallucination
  * Enhancing Accuracy

## Source ##
Here is our [Presentation](https://www.canva.com/design/DAGT_p843FA/Y6y_e4gWoSdm6mL9IcT3OQ/edit?utm_content=DAGT_p843FA&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

## Get Start ##

### Environment
First, you have to pip install the necessary library.
```
!pip pandas requests
```
or you can create requirements.txt and copy my requirements.txt in your file.
Then run this command in terminal or command prompt.
```
!pip install -r requirements.txt
```

### Experiment
- **Overall.py && Overall.ipynb** | Large Language Model Create real time Quetion 
- **Question_bank.py && Question_bank.ipynb** | Use Query Question in Question Bank database


## Member ##
Mr.Tanawat Wongwad

Mr.Nattapong  Pakdeeviboon

Miss Thitaree Lumsan

From Nawaminthrachinuthit Satriwitthaya Phutthamonthon School

## Final ##
*We extend our gratitude to Mr. Chatchawal Sangkeettrakarn, our supervisor and a researcher from the National Electronics and Computer Technology Center, for his valuable suggestions and for inviting us to participate in the internship. Throughout the one-month period, we gained a wealth of experience.*
