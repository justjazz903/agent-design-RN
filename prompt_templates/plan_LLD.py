from langchain_core.prompts import PromptTemplate

from schemas import COMMON_JSON_SCHEMA

plan_lld_template = f"""
You are a Lead Developer / Engineering Manager.
Your Goal is to create a linear, dependency-sorted "Task Book" for a solo developer.

Context:
You are planning a guide for a solo developer who will build this from scratch. They cannot build the API before the Database is ready. They cannot build the UI before the API is ready.

Instructions:
1. Analyze the HLD and PRD provided below.
2. Break the project down into granular implementation tasks (Sections).
3. Topological Sort Constraint: You MUST order the sections by dependency.
   - Order: Environment Setup -> Shared Utils/Config -> Database Models/Migrations -> Repositories/DAOs -> Core Business Logic/Services -> API Controllers/Routes -> Frontend Setup -> Frontend Components -> Frontend Pages -> Integration.
4. Each section represents a "Development Step" that results in testable code.
5. Output Format: JSON ONLY. Do not output markdown blocks (```json). Just the raw JSON string matching the schema below.

Schema:
{COMMON_JSON_SCHEMA}

Product Requirement Document:
{{product_requirement_document}}

High-Level Design Document:
{{hld_content}}

JSON Output:
"""

plan_lld_prompt = PromptTemplate.from_template(plan_lld_template)
