You are an expert in creating system instructions for large language models that maximizing models' performance and capabilities.



I created a workflow for a large language model to generate software design documents:
1. **clarify**: ueser provides raw requirement descriptions and the model clarifies the requirement with user until the model decides it has all the necessary information to proceed. During the clarify process, I will record the conversation between user and the model.
2. **merge_clarification**: The user's raw requirement descriptions and clarification conversation will be passed into a model and the model will merge and summarize them into a concrete requirement description. The clarify and merge_clarification process might repeat multiple times so that I can make sure every aspect is considered.
3. **plan_requirement**: the requirement description from step 2 will be passed into a model and the model will generate structured output (JSON) that represents a writing plan for the formal requirement document. The plan is a list of sections.
4. **generate_requirement**: the requirement plan from previous step will be parsed. A model will write the formal requirement document one section a time iteratively. For example: a model will first write section one in one prompt, then the section one will also be passed in as context for the model to write section two in the next promopt.
5. **plan_HLD**: it is the same logic with plan_requirement only with model's input be the formal requirement document from previous step. HLD stands for High-Level Design.
6. **generate_HLD**: it is the same logic with generate_requirement only with model's input be the plan generated from previous step.
7. **plan_LLD**: LLD stands for Low-Level Design. Same logic as before.
8. **generate_LLD**: Same logic as before

The work flow ends with a detailed LLD document, this document should be a task book for the whole development and test process. Almost like a tutorial with specific and detailed goals at each step. But the LLD will not do the actual coding, it should only guide coding. Later I will use another model to process each step from the LLD and do the coding step by step to make sure the model can perform on small task with good performance. I, as a solo developer, will be the only human using this LLD doc to complete the whole project. I want to be able to follow the generated LLD document directly, generate and test code at each stage. From start to the end, so each section should be in the right order (topological sort), modules with no dependencies first, modules with dependencies later. For planning stage that needs structured output (3, 5, 7), use the same schema.

Now help me construct system instructions for each stage in the workflow.

