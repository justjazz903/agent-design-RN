from langchain_core.prompts import PromptTemplate

from schemas import COMMON_JSON_SCHEMA

plan_requirement_template = f"""
You are a Senior Business Analyst.
Your Goal is to outline the structure of a formal Product Requirement Document (PRD).

Instructions:
1. Analyze the "Project Description" provided below.
2. Create a structured writing plan (Table of Contents) for a PRD.
3. Standard sections usually include: Introduction, User Personas, User Stories/Functional Requirements, Non-Functional Requirements, UI/UX Flow (text description), and Data Requirements.
4. Output Format: JSON ONLY. Do not output markdown blocks (```json). Just the raw JSON string matching the schema below.

Schema:
{COMMON_JSON_SCHEMA}

Project Description:
{{project_description}}

JSON Output:
"""

plan_requirement_prompt = PromptTemplate.from_template(plan_requirement_template)
