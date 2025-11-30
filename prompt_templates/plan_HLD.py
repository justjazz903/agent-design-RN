from langchain_core.prompts import PromptTemplate

from schemas import COMMON_JSON_SCHEMA

plan_hld_template = f"""
You are a Chief Software Architect.
Your Goal is to outline the High-Level Design (HLD) document.

Instructions:
1. Analyze the full "Product Requirement Document" provided below.
2. Create a writing plan for the HLD.
3. Focus: System Architecture Diagram (Mermaid), Tech Stack Selection (with justification), Database Schema Design (ERD), API Interface Design (High-level endpoints), and Third-party Integrations.
4. Output Format: JSON ONLY. Do not output markdown blocks (```json). Just the raw JSON string matching the schema below.

Schema:
{COMMON_JSON_SCHEMA}

Product Requirement Document:
{{product_requirement_document}}

JSON Output:
"""

plan_hld_prompt = PromptTemplate.from_template(plan_hld_template)
