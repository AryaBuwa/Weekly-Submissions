from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Define careers and their required skills
careers = {
    "Software Developer": "Python, Java, C++, problem-solving, debugging, algorithms",
    "Web Developer": "HTML, CSS, JavaScript, React, Node.js, version control (Git)",
    "Data Analyst": "SQL, Python, Excel, data visualization (Tableau, Power BI), statistics",
    "Machine Learning Engineer": "Python, TensorFlow, PyTorch, data preprocessing, model training",
    "DevOps Engineer": "Docker, Kubernetes, CI/CD, Jenkins, cloud platforms (AWS, Azure)",
    "Cybersecurity Analyst": "Network security, penetration testing, cryptography, firewall management",
    "Cloud Architect": "Cloud platforms (AWS, Azure), system architecture, Kubernetes, containerization",
    "AI Researcher": "Machine learning, neural networks, deep learning, research papers, advanced algorithms",
    "Blockchain Developer": "Solidity, Ethereum, blockchain technology, smart contracts, cryptography",
    "Game Developer": "C++, Unity, Unreal Engine, game design, physics simulations",
    "Mechanical Engineer": "CAD, solid mechanics, thermodynamics, material science",
    "Electrical Engineer": "Circuit design, electrical systems, programming (Python, C++), MATLAB",
    "Civil Engineer": "Structural analysis, CAD, project management, material science",
    "Robotics Engineer": "Mechanical design, Python/C++, automation, AI, sensor integration",
    "Environmental Engineer": "Environmental regulations, water treatment, waste management, sustainability",
    "Chemical Engineer": "Thermodynamics, process design, chemical reaction engineering, MATLAB",
    "Aerospace Engineer": "Aerodynamics, propulsion systems, CAD, system modeling",
    "Industrial Engineer": "Lean manufacturing, process optimization, supply chain management, operations research",
    "Biomedical Engineer": "Medical device design, biology, biomechanics, signal processing",
    "Nanotechnologist": "Nanomaterials, molecular biology, quantum mechanics, material science",
    "Product Manager": "Market research, Agile methodology, project management, product strategy",
    "Marketing Manager": "SEO, content marketing, social media, Google Analytics, branding",
    "Operations Manager": "Supply chain management, logistics, project planning, team management",
    "Sales Manager": "Lead generation, CRM tools, sales strategies, negotiation",
    "HR Manager": "Recruitment, employee engagement, performance management, labor laws",
    "Financial Analyst": "Financial modeling, Excel, data analysis, risk management",
    "Investment Banker": "Financial analysis, Excel, market research, corporate finance",
    "Business Analyst": "Data analysis, SQL, business modeling, process improvement",
    "Management Consultant": "Strategy, business analysis, data-driven insights, market research",
    "UX/UI Designer": "Adobe XD, wireframing, user research, design principles",
    "Digital Marketer": "SEO, content creation, analytics, social media, branding",
    "Operations Research Analyst": "Optimization models, statistics, MATLAB, decision analysis",
    "Content Writer": "Research, SEO, writing, editing, content management",
    "Copywriter": "Persuasive writing, creativity, storytelling, content marketing",
    "Journalist": "Writing, investigative research, editing, public relations",
    "Editor": "Proofreading, grammar, writing, content management",
    "Photographer": "Photography techniques, editing, studio management, creative direction",
    "Videographer": "Cinematography, editing, storytelling, video production",
    "SEO Specialist": "Keyword research, content strategy, Google Analytics, on-page SEO",
    "Brand Manager": "Brand strategy, market research, marketing, communication skills",
    "Public Relations Specialist": "Communication, media relations, press releases, crisis management",
    "Event Planner": "Event coordination, logistics, vendor management, budgeting",
    "Recruiter": "Sourcing, interviewing, negotiation, candidate relationship management",
    "Training and Development Manager": "Employee training, coaching, program development",
    "Customer Support Representative": "Problem-solving, communication skills, empathy, customer service software",
    "Social Media Manager": "Social media platforms, content creation, analytics, audience engagement",
    "Legal Advisor": "Corporate law, contract negotiation, legal writing, compliance",
    "Paralegal": "Legal research, document preparation, legal proceedings",
    "Medical Doctor": "Diagnosis, patient care, medical procedures, surgery",
    "Nurse": "Patient care, medical knowledge, empathy, attention to detail",
    "Pharmacist": "Pharmacology, drug prescriptions, healthcare laws, patient interaction",
    "Psychologist": "Counseling, therapy, mental health, psychological assessments",
    "Physiotherapist": "Physical rehabilitation, body mechanics, injury recovery, patient care",
    "Dentist": "Oral health, dental procedures, patient care, anatomy",
    "Veterinarian": "Animal care, medicine, surgery, diagnosis",
    "Biologist": "Research, lab techniques, biology, fieldwork",
    "Chemist": "Lab work, chemical analysis, material science, research",
    "Physicist": "Research, theoretical physics, lab experiments, mathematical modeling",
    "Geologist": "Fieldwork, research, geology, earth science",
    "Meteorologist": "Climate science, forecasting, data analysis, environmental monitoring",
    "Astronomer": "Astrophysics, research, space science, data analysis",
    "Marine Biologist": "Oceanography, marine ecosystems, field research, data analysis",
    "Ecologist": "Environmental science, ecosystems, research, biodiversity",
    "Anthropologist": "Research, cultural studies, data collection, fieldwork",
    "Sociologist": "Social research, data analysis, sociology theory, surveys",
    "Historian": "Research, data analysis, historical knowledge, writing",
    "Archivist": "Collection management, preservation, archival research, documentation",
    "Librarian": "Library science, cataloging, information management, research",
    "Tour Guide": "Customer service, history knowledge, communication skills, local knowledge",
    "Translator": "Language fluency, translation tools, writing skills, cultural knowledge",
    "Interpreter": "Language fluency, translation skills, listening skills, cultural knowledge",
    "Artist": "Art techniques, creativity, visual communication, design software",
    "Musician": "Music theory, instrument skills, composition, performance",
    "Actor": "Performing arts, stage presence, voice training, acting techniques",
    "Fashion Designer": "Fashion design, creativity, pattern making, CAD",
    "Interior Designer": "Design principles, CAD, space planning, creativity",
    "Chef": "Cooking techniques, kitchen management, creativity, nutrition",
    "Baker": "Baking techniques, recipe development, food safety, creativity",
    "Bartender": "Mixology, customer service, drink recipes, bar management",
    "Waiter/Waitress": "Customer service, food knowledge, multitasking, communication",
    "Fitness Trainer": "Exercise techniques, nutrition, client assessment, coaching",
    "Yoga Instructor": "Yoga techniques, mindfulness, anatomy, teaching skills"
}


# Listing career names and their skillsets
career_names = list(careers.keys())
career_skills = list(careers.values())

# Initialize the TF-IDF Vectorizer and fit it on the career skills
vectorizer = TfidfVectorizer()
career_vectors = vectorizer.fit_transform(career_skills)

def recommend_career(user_input):
    """Recommends the best career based on user skills input"""
    user_vector = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vector, career_vectors)

    # Find the career with the highest similarity score
    top_match_index = similarity.argmax()
    recommended_career = career_names[top_match_index]
    match_score = similarity[0][top_match_index]

    return recommended_career, match_score

# Getting User Input
user_skills = input("Enter your skills (comma separated): ")

# Getting recommendation
recommended_career, match_score = recommend_career(user_skills)

# Printing the result
print(f"Recommended Career: {recommended_career}")
print(f"Match Score: {match_score:.2f}")
