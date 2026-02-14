# agents.py

import os
from openai import OpenAI
from dotenv import load_dotenv
from prompts import (
    TOPIC_EXTRACTOR_PROMPT,
    SKILL_GAP_PROMPT,
    PRIORITY_PLANNER_PROMPT,
    STUDY_PLAN_PROMPT
)

load_dotenv()

client = OpenAI(api_key=os.getenv("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"))


class AcademicAgentSystem:

    def __init__(self):
        self.model = "gpt-4o-mini"


    def call_llm(self, prompt):
        response = client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        return response.choices[0].message.content


    # Agent 1: Extract Topics
    def extract_topics(self, syllabus):

        prompt = TOPIC_EXTRACTOR_PROMPT.format(
            syllabus=syllabus
        )

        return self.call_llm(prompt)


    # Agent 2: Find Skill Gap
    def find_skill_gap(self, current_topics, future_topics):

        prompt = SKILL_GAP_PROMPT.format(
            current=current_topics,
            future=future_topics
        )

        return self.call_llm(prompt)


    # Agent 3: Plan Priority
    def plan_priority(self, missing_skills):

        prompt = PRIORITY_PLANNER_PROMPT.format(
            skills=missing_skills
        )

        return self.call_llm(prompt)


    # Agent 4: Generate Study Plan
    def generate_study_plan(self, priority_skills):

        prompt = STUDY_PLAN_PROMPT.format(
            skills=priority_skills
        )

        return self.call_llm(prompt)


    # Full Pipeline
    def run_full_analysis(self, current_syllabus, future_syllabus):

        current_topics = self.extract_topics(current_syllabus)

        future_topics = self.extract_topics(future_syllabus)

        missing_skills = self.find_skill_gap(
            current_topics,
            future_topics
        )

        priority = self.plan_priority(missing_skills)

        study_plan = self.generate_study_plan(priority)

        return {
            "current_topics": current_topics,
            "future_topics": future_topics,
            "missing_skills": missing_skills,
            "priority": priority,
            "study_plan": study_plan
        }