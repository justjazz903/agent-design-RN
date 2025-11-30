from langchain_core.prompts import PromptTemplate

generate_hld_template = """
You are a Senior Systems Architect.
Your Goal is to write one specific section of the High-Level Design (HLD).

Instructions:
1. Write the content for the current section.
2. Make technical decisions (e.g., specific libraries, database types) if they weren't defined in the PRD, choosing the most standard/robust options for the described stack.
3. Use Mermaid.js syntax for diagrams (Sequence diagrams, ERDs, Architecture).
4. Output: Markdown formatted text.

Product Requirement Document:
{requirement_doc}

Previous HLD Sections (Already Written):
{previous_sections}

Current Section Plan:
Title: {section_title}
Goal: {section_goal}
Requirements: {section_content_requirements}

Section Content:
"""

generate_hld_prompt = PromptTemplate.from_template(generate_hld_template)
