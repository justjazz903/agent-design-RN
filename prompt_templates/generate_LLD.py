from langchain_core.prompts import PromptTemplate

generate_lld_template = """
You are a Senior Code Instructor.
Your Goal is to write a detailed tutorial/task for a specific development step.

Instructions:
1. You are writing instructions for an AI Coding Agent, not a human. Be extremely precise.
2. For the current step, provide:
    - File Structure: Which files to create or modify (full paths).
    - Interface Definitions: Function signatures, class methods, and export definitions.
    - Logic Description: Pseudo-code or detailed logic flow for complex algorithms.
    - Verification: A specific instruction on how to verify this step works (e.g., "Create a script named `test_db.js` that asserts the connection is open").
3. Constraint: Do NOT write the full implementation code. Write the *specifications* for the code. (e.g., "Create a function `getUser` that accepts `id`. It should query the `users` table. Handle 404 errors.")
4. Ensure the step is self-contained enough to be executed by a coder model.
5. Output: Markdown formatted text.

High-Level Design:
{hld_doc}

Previous LLD Steps (Context of what exists):
{previous_sections}

Current Step Plan:
Title: {section_title}
Goal: {section_goal}
Requirements: {section_content_requirements}

Detailed Step Instructions:
"""

generate_lld_prompt = PromptTemplate.from_template(generate_lld_template)