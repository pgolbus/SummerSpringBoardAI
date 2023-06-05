knowledge_base = {
    "Diablo 2": "Who doesn't love Diablo?",
    "Street Fighter 2": "You have excellent taste.",
}

rules = [
    {
        "if": "fighters",
        "then": "Street Fighter 2",
        "explanation": "If you're into fighters, you have to check out the original."
        },
    {
        "if": "Street Fighter 2",
        "then": "fighters",
        "explanation": "Careful. I'm here to cause an infinite loop. Why will I cause an inifinite loop?)"
    },
]

class InferenceEngine:
    def __init__(self, knowledge_base, rules):
        self.knowledge_base = knowledge_base
        self.rules = rules

    def infer(self, facts):
        fact = facts.pop(0)
        if fact in self.knowledge_base:
            print(f"{fact}: {self.knowledge_base[fact]}")
        for rule in self.rules:
            # If the rule's if statement is a subset of the facts,
            # I know know something else
        print("----------------------")

engine = InferenceEngine(knowledge_base, rules)
engine.infer(["Diablo 2", "fighters"])
print("\n")
engine.infer(["Super Star Wars"])
