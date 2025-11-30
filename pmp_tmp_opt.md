Here are the `langchain_core.prompts.PromptTemplate` definitions for your workflow.

I have organized them by stage. I also defined the `COMMON_JSON_SCHEMA` as a constant to ensure consistency across the planning stages (3, 5, 7) as requested.

```python
from langchain_core.prompts import PromptTemplate

# --- Shared Constants ---

COMMON_JSON_SCHEMA = """
{
  "sections": [
    {
      "section_index": integer,
      "title": "string",
      "goal": "string (brief description of what this section covers)",
      "content_requirements": "string (detailed instructions on what needs to be written in this section)"
    }
  ]
}
"""

# --- 1. Clarify ---

clarify_template = """
You are an Expert Product Manager and Requirements Analyst.
Your Goal is to elicit a complete, unambiguous software requirement set from the user.

Instructions:
1. Analyze the user's raw input and the conversation history.
2. Identify missing critical information (e.g., tech stack preferences, specific features, user roles, edge cases, scale requirements).
3. Ask clarifying questions to fill these gaps.
4. Constraint: Do not assume features. If something is vague, ask.
5. Termination Condition: If you have sufficient information to build a comprehensive Product Requirement Document (PRD), output the exact string `[READY]` at the end of your response. Otherwise, end with your questions.

Current Context:
User's Original Input: {user_input}

Conversation History:
{chat_history}

Your Response:
"""

clarify_prompt = PromptTemplate.from_template(clarify_template)


# --- 2. Merge Clarification ---

merge_clarification_template = """
You are a Technical Writer / Product Owner.
Your Goal is to synthesize a chaotic conversation into a single, pristine source of truth.

Instructions:
1. You will receive an initial raw requirement and a transcript of a Q&A session.
2. Merge these into a single, cohesive "Project Description."
3. Resolve any conflicts (prioritize the latest clarification in the chat history).
4. Discard conversational filler ("Hello," "Sure," "I think").
5. Organize by: Project Overview, Core Features, User Roles, Technical Constraints (if mentioned), and Future Scope.
6. Output: A narrative text document. No JSON, just clear, structured text.

Input Data:
Raw Requirement: {user_input}
Clarification Transcript: {chat_history}

Merged Project Description:
"""

merge_clarification_prompt = PromptTemplate.from_template(merge_clarification_template)


# --- 3. Plan Requirement (PRD) ---

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


# --- 4. Generate Requirement (Iterative) ---

generate_requirement_template = """
You are a Technical Documentation Specialist.
Your Goal is to write one specific section of the PRD based on the plan and context.

Instructions:
1. Write the content for the Current Section Plan ONLY.
2. Ensure the tone is professional, clear, and unambiguous.
3. Do not repeat content from Previous Sections unless necessary for context.
4. Output: Markdown formatted text for this specific section.

Project Context (Full Description):
{project_context}

Previous Sections (Already Written):
{previous_sections}

Current Section Plan:
Title: {section_title}
Goal: {section_goal}
Requirements: {section_content_requirements}

Section Content:
"""

generate_requirement_prompt = PromptTemplate.from_template(generate_requirement_template)


# --- 5. Plan HLD ---

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
{{prd_content}}

JSON Output:
"""

plan_hld_prompt = PromptTemplate.from_template(plan_hld_template)


# --- 6. Generate HLD (Iterative) ---

generate_hld_template = """
You are a Senior Systems Architect.
Your Goal is to write one specific section of the HLD.

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


# --- 7. Plan LLD (Task Book) ---

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
{{prd_content}}

High-Level Design Document:
{{hld_content}}

JSON Output:
"""

plan_lld_prompt = PromptTemplate.from_template(plan_lld_template)


# --- 8. Generate LLD (Iterative Task Book) ---

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
```

### How to use these templates in your Python code

When invoking the chains, you will map your variables to the input keys defined in the templates.

**Example for Step 4 (Generate Requirement):**

```python
# Assuming you have the plan from Step 3 parsed as a Python dict named `plan`
# and you are iterating through `plan['sections']`

current_section = plan['sections'][0] # Example: First section

formatted_prompt = generate_requirement_prompt.format(
    project_context=full_project_description_string,
    previous_sections=string_of_already_generated_markdown,
    section_title=current_section['title'],
    section_goal=current_section['goal'],
    section_content_requirements=current_section['content_requirements']
)

# Pass `formatted_prompt` to your LLM
```