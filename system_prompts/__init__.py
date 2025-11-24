from os import path

work_dir = "system_prompts"
filenames = [
    "clarify.md",
    "generate_HLD.md",
    "generate_implementation.md",
    "generate_LLD.md",
    "generate_requirement.md",
    "plan_HLD.md",
    "plan_LLD.md",
    "plan_requirement.md",
]

class SystemPrompts:

    def __init__(self):
        for filename in filenames:
            file_path = path.join(work_dir, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                setattr(self, filename.replace(".md", ""), content)


system_prompts = SystemPrompts()
