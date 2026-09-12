# utils/prompts.py

SUMMARY_PROMPT = """
You are an expert AI productivity assistant. 
Provide a structured executive summary of the following document.
Highlight key takeaways, background, and important facts.
"""

TASK_EXTRACTION_PROMPT = """
Extract all actionable tasks, action items, assigned persons, and deadlines from the following text.
Format the output as a Markdown table with columns: [Task, Assignee, Priority, Deadline].
"""

REPORT_PROMPT = """
Generate a comprehensive professional report based on the provided text.
Include Executive Summary, Key Findings, Risks/Challenges, and Next Steps.
"""
