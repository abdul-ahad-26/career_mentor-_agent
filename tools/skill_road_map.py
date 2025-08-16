from agents import function_tool
from typing import Dict, Any
# Tool: Skill Roadmap Generator
@function_tool
def get_career_roadmap(field: str) -> Dict[str, Any]:
    roadmaps = {
        "Data Analyst": {
            "Overview": "Use mathematical and statistical techniques to interpret data and help businesses make informed decisions.",
            "Core Skills": ["Statistics", "Data Visualization", "SQL", "Excel"],
            "Intermediate": ["Python for Data Analysis", "Machine Learning Basics", "Business Intelligence Tools"],
            "Suggested Projects": ["Sales data analysis report", "Interactive dashboard using Power BI"]
        },
        "Actuary": {
            "Overview": "Assess financial risks using math, statistics, and financial theory.",
            "Core Skills": ["Probability", "Statistics", "Excel", "Financial Mathematics"],
            "Intermediate": ["Risk Modeling", "Insurance Mathematics", "Predictive Analytics"],
            "Suggested Projects": ["Life insurance risk model", "Financial risk simulation"]
        },
        "Mathematics Teacher": {
            "Overview": "Inspire the next generation by teaching math concepts in schools.",
            "Core Skills": ["Mathematical Knowledge", "Lesson Planning", "Classroom Management"],
            "Intermediate": ["Educational Technology", "Assessment Design", "Curriculum Development"],
            "Suggested Projects": ["Interactive math lesson plan", "Math games for high school students"]
        }
    }

    return roadmaps.get(field, {
        "Overview": f"A roadmap for {field} (auto-generated).",
        "Core Skills": ["Foundational skill 1", "Foundational skill 2"],
        "Intermediate": ["Intermediate skill A", "Intermediate skill B"],
        "Suggested Projects": ["Project A", "Project B"]
    })
