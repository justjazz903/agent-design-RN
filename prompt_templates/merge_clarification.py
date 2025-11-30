from langchain_core.prompts import PromptTemplate

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
