**Role:** Lead Developer / Engineering Manager.
**Goal:** Create a linear, dependency-sorted "Task Book" for a solo developer.

**Context:**
You are planning a guide for a solo developer who will build this from scratch. They cannot build the API before the Database is ready. They cannot build the UI before the API is ready.

**Instructions:**
1.  Analyze the High-Level Design (HLD) and Product Requirement Document (PRD).
2.  Break the project down into granular implementation tasks (Sections).
3.  **Topological Sort Constraint:** You MUST order the sections by dependency.
    *   *Order:* Environment Setup -> Shared Utils/Config -> Database Models/Migrations -> Repositories/DAOs -> Core Business Logic/Services -> API Controllers/Routes -> Frontend Setup -> Frontend Components -> Frontend Pages -> Integration.
4.  Each section represents a "Development Step" that results in testable code.
5.  **Output Format:**
    ```json
    {
      "sections": [
        {
          "id": integer,
          "title": "string",
          "goal": "string (brief description of what this section covers)",
          "content": "string (detailed instructions on what needs to be written in this section)"
        }
      ]
    }
    ```