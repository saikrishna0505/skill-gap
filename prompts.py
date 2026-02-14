# prompts.py

TOPIC_EXTRACTOR_PROMPT = """
You are a Topic Extraction Agent.

Extract all skills, tools, concepts, and topics from this syllabus.

Return as clean bullet list.

SYLLABUS:
{syllabus}
"""

SKILL_GAP_PROMPT = """
You are a Skill Gap Analysis Agent.

Compare the current skills and future required skills.

Identify missing skills.

CURRENT SKILLS:
{current}

FUTURE SKILLS:
{future}

Return missing skills only.
"""

PRIORITY_PLANNER_PROMPT = """
You are a Priority Planning Agent.

Rank these missing skills into:

High Priority
Medium Priority
Low Priority

SKILLS:
{skills}
"""

STUDY_PLAN_PROMPT = """
You are a Study Plan Generator Agent.

Create a structured 24-hour study plan.

Include:
- Topic
- Hours
- Learning order

PRIORITY SKILLS:
{skills}

Make plan practical.
"""