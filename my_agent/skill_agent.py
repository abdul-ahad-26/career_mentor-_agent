from agents import Agent
from tools.skill_road_map import get_career_roadmap
from my_agent.job_agent import job_agent
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX



skill_agent = Agent(
    name = "SkillAgent",
instructions = f"""{RECOMMENDED_PROMPT_PREFIX}
You help users plan their skill journey for a specific career field.

Steps:
* Verify the career choice from the user (if not already provided).
* Use the tool `get_career_roadmap()` to generate a beginner-to-advanced roadmap.
* Present the skill roadmap clearly in bullet or numbered format.
* Then ask if the user wants to explore job roles in this field. If yes, hand off to JobAgent.

Tone:
* Motivational, encouraging, and helpful.
""",
tools=[get_career_roadmap],
handoffs=[job_agent]
)