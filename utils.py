# utils.py

def format_output(result):

    output = f"""

CURRENT TOPICS:
{result['current_topics']}

FUTURE TOPICS:
{result['future_topics']}

MISSING SKILLS:
{result['missing_skills']}

PRIORITY PLAN:
{result['priority']}

24-HOUR STUDY PLAN:
{result['study_plan']}

"""

    return output