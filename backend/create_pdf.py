from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem, PageBreak

def create_study_guide_pdf(data, filename="study_guide.pdf"):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    content = []
    
    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Title"],
        fontSize=16,
        spaceAfter=12,
    )
    
    heading_style = ParagraphStyle(
        "HeadingStyle",
        parent=styles["Heading2"],
        fontSize=14,
        spaceAfter=8,
    )
    
    body_style = ParagraphStyle(
        "BodyStyle",
        parent=styles["BodyText"],
        fontSize=12,
        spaceAfter=6,
    )
    
    bullet_style = ParagraphStyle(
        "BulletStyle",
        parent=styles["BodyText"],
        fontSize=12,
        leftIndent=20,
        spaceAfter=4,
    )
    
    # Title
    content.append(Paragraph("Study Guide", title_style))
    content.append(Spacer(1, 12))
    
    # Extract study guide content
    for section in data.get("study_guide", []):
        # Main point
        content.append(Paragraph(section["main point"], heading_style))
        
        # Subpoints (bullet points)
        if "subpoints" in section:
            bullet_list = ListFlowable([
                ListItem(Paragraph(f"{point}", bullet_style)) for point in section["subpoints"]
            ], bulletType='bullet')
            content.append(bullet_list)
        
        # Explanation
        if "explanation" in section:
            content.append(Paragraph(section["explanation"], body_style))
        
        content.append(Spacer(1, 12))
    
    # Build PDF
    doc.build(content)
    return filename

def create_quiz_pdf(data, filename="quiz.pdf"):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    content = []
    
    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Title"],
        fontSize=16,
        spaceAfter=12,
    )
    
    question_style = ParagraphStyle(
        "QuestionStyle",
        parent=styles["Heading3"],
        fontSize=12,
        spaceAfter=8,
    )
    
    choice_style = ParagraphStyle(
        "ChoiceStyle",
        parent=styles["BodyText"],
        fontSize=12,
        leftIndent=20,
        spaceAfter=4,
    )
    
    answer_style = ParagraphStyle(
        "AnswerStyle",
        parent=styles["BodyText"],
        fontSize=12,
        textColor='blue',
        spaceAfter=6,
    )
    
    # Title
    content.append(Paragraph("Quiz", title_style))
    content.append(Spacer(1, 12))
    
    # Extract quiz content
    answers = []
    for index, question in enumerate(data.get("quiz", []), start=1):
        question_quiz = question["question"]
        content.append(Paragraph(f"{index}. {question_quiz}", question_style))
        
        # Choices
        if "choices" in question:
            choice_list = ListFlowable([
                ListItem(Paragraph(f"{choice}", choice_style)) for choice in question["choices"]
            ], bulletType='bullet')
            content.append(choice_list)
        
        # Store answers for the answer sheet
        answers_quiz = question["answer"]
        answers.append(Paragraph(f"{index}. {answers_quiz}", answer_style))
        
        content.append(Spacer(1, 12))
    
    # Page break before answer sheet
    content.append(PageBreak())
    content.append(Paragraph("Answer Key", title_style))
    content.append(Spacer(1, 12))
    content.extend(answers)
    
    # Build PDF
    doc.build(content)
    return filename

def create_flashcards_pdf(data, filename="flashcards.pdf"):
    doc = SimpleDocTemplate(filename, pagesize=landscape(letter))
    styles = getSampleStyleSheet()
    content = []
    
    title_style = ParagraphStyle("TitleStyle", parent=styles["Title"], fontSize=16, spaceAfter=12)
    term_style = ParagraphStyle("TermStyle", parent=styles["Heading2"], fontSize=14, spaceAfter=6)
    explanation_style = ParagraphStyle("ExplanationStyle", parent=styles["BodyText"], fontSize=12, spaceAfter=6)
    
    # Title
    content.append(Paragraph("Flashcards", title_style))
    content.append(Spacer(1, 12))
    
    # Create flashcards
    for flashcard in data.get("flashcards", []):
        content.append(Paragraph(flashcard["term/concept"], term_style))
        content.append(Spacer(1, 6))
        content.append(Paragraph(flashcard["explanation"], explanation_style))
        content.append(PageBreak())
    
    # Build PDF
    doc.build(content)
    return filename



if __name__ == "__main__":
    # Example dictionary
    study_guide_data = {
        'study_guide': [
            {'main point': 'Memorial Lectures for Robert Sobukwe', 'subpoints': ["Hosted by African People's Convention", "Focus on Sobukwe's legacy", 'Series started in February'], 'explanation': "The African People's Convention (APC) held a series of memorial lectures honoring Robert Mangaliso Sobukwe, a prominent anti-apartheid figure and founder of the Pan-Africanist Congress (PAC). These lectures aimed to reflect on Sobukwe's contributions to fighting segregation and educating younger generations about his impact. The series, which commenced in February, the month marking Sobukwe's death in 1978, took place in various regions including Limpopo."},
            {'main point': 'Key Themes Discussed', 'subpoints': ["Importance of Sobukwe's legacy", 'Lack of audio/visual materials', 'Call for unity among African nations'], 'explanation': "Key themes during the lectures included the significance of preserving Sobukwe's legacy through recorded materials, as there are currently no known audio or video recordings of him. This highlights a desire within the APC to amplify Sobukwe's messages and ideologies, especially regarding unity and Africanism. Discussions also centered on contemporary issues affecting Africa, emphasizing the need for collaborative efforts among African nations to address security and peace challenges."},
            {'main point': 'Political Context and Challenges', 'subpoints': ['Critique of current political strategies', 'Focus on bilateral discussions', "Contemporary relevance of Sobukwe's ideas"], 'explanation': "The APC president addressed current political strategies, criticizing how some entities allegedly tarnished the country's name. Sobukwe's legacy was invoked to advocate for a more principled approach to governance and national issues. His ideals are viewed as a guiding force for contemporary leaders, particularly concerning the importance of unity within Africa to facilitate solutions for ongoing conflicts and ethnic tensions."}
        ]
    }

    quiz_data = {'quiz': [{'question': 'Robert Mangaliso Sobukwe broke away from the ANC to form the Pan-Africanist Congress in 1959.', 'choices': ['True', 'False'], 'answer': 'True'}, {'question': 'Sobukwe died in 1978.', 'choices': ['True', 'False'], 'answer': 'True'}, {'question': "The African People's Convention (APC) carries the political ownership of Sobukwe's narrative.", 'choices': ['True', 'False'], 'answer': 'False'}, {'question': 'The key theme explored in the lectures was the lack of audio or video recordings of Robert Sobukwe.', 'choices': ['True', 'False'], 'answer': 'True'}, {'question': 'The APC began the series of lectures in January.', 'choices': ['True', 'False'], 'answer': 'False'}, {'question': 'Robert Mangaliso Sobukwe is tied to the legacy of fighting segregation policies against black people.', 'choices': ['True', 'False'], 'answer': 'True'}, {'question': 'The memorial lectures took place across various provinces in South Africa.', 'choices': ['True', 'False'], 'answer': 'True'}, {'question': 'The APC believes that the wealth of the country should be controlled by foreign investors.', 'choices': ['True', 'False'], 'answer': 'False'}, {'question': 'Security crises in the DRC and ethnic battles were mentioned as current issues during the discussions.', 'choices': ['True', 'False'], 'answer': 'True'}, {'question': 'The president of APC mentioned that Sobukwe would have supported the current strategies seen in the country.', 'choices': ['True', 'False'], 'answer': 'False'}, {'question': "The African People's Convention has been conducting these lectures since February.", 'choices': ['a) 2020', 'b) 2021', 'c) 2022', 'd) 2023'], 'answer': 'c'}, {'question': 'The memorial lecture for Sobukwe took place in Mandiwana Village.', 'choices': ['a) Mpumalanga', 'b) Limpopo', 'c) Cape Town', 'd) Johannesburg'], 'answer': 'b'}, {'question': 'Sobukwe was a figure associated with the anti-apartheid movement.', 'choices': ['a) True', 'b) False'], 'answer': 'a'}, {'question': "The APC is advocating for more access to Sobukwe's voice and image through recordings.", 'choices': ['a) True', 'b) False'], 'answer': 'a'}, {'question': 'Robert Sobukwe passed away on February 27th.', 'choices': ['a) 1976', 'b) 1978', 'c) 1980', 'd) 1982'], 'answer': 'b'}, {'question': "The lectures started to honor Sobukwe's contributions to African unity and pan-Africanism.", 'choices': ['a) True', 'b) False'], 'answer': 'a'}, {'question': 'Key issues discussed included peace and bilateral discussions in Africa.', 'choices': ['a) True', 'b) False'], 'answer': 'a'}]} 

    flashcards_data = {'flashcards': [{'term/concept': 'Robert Mangaliso Sobukwe', 'explanation': 'A prominent Pan-Africanist who broke away from the ANC to form the Pan-African Congress in 1959, and played a significant role in fighting segregation and advocating for black South Africans.'}, {'term/concept': "African People's Convention (APC)", 'explanation': "A political party that honors Sobukwe's legacy and conducted memorial lectures on his contributions to the anti-apartheid struggle, emphasizing the importance of his ideals for contemporary society."}, {'term/concept': 'Memorial Lectures', 'explanation': "A series of discussions conducted by the APC throughout South Africa to reflect on Sobukwe's life and impact, specifically in February, which is declared as Sobukwe's month."}, {'term/concept': 'Ideological Ownership', 'explanation': 'Both the APC and the PAC lay claim to the political and ideological legacy of Sobukwe, each wanting to establish a narrative around his contributions and principles.'}, {'term/concept': 'Challenges Facing South Africa', 'explanation': 'During the memorial lectures, it was noted that Sobukwe would not tolerate current political antics, and there was a call for South Africans to unite in addressing ongoing challenges.'}, {'term/concept': 'Voice of Sobukwe', 'explanation': "The APC's desire to find audio or video recordings of Sobukwe speaking to ensure his voice and thoughts on contemporary issues are preserved."}, {'term/concept': 'Pan-Africanism', 'explanation': 'A movement promoting unity and solidarity among African states, which Sobukwe strongly advocated for, especially in light of current geopolitical tensions on the continent.'}, {'term/concept': 'Contemporary African Issues', 'explanation': 'Discussions during the memorial reflected on modern crises faced by African nations, emphasizing the need for peaceful regional dialogue and bilateral solutions.'}, {'term/concept': "Sobukwe's Ideals", 'explanation': "The APC aims to propagate Sobukwe's vision for a united Africa centered on Africanism, particularly regarding economic control and the welfare of black Africans."}, {'term/concept': "February as Sobukwe's Month", 'explanation': 'The APC dedicates February to commemorate the life and legacy of Robert Sobukwe, marking the anniversary of his death, to inspire current and future generations.'}]}