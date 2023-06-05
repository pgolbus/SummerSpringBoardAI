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

    def infer(self, facts, seen, found=False):
        if len(facts) == 0:
            if not found:
                print("Sorry, I don't know what that game / genre.")
            return
        fact = facts.pop(0)
        if fact in self.knowledge_base:
            print(f"{fact}: {self.knowledge_base[fact]}")
            found = True
        for rule in self.rules:
            if rule["if"] not in seen:
                if rule["if"] == fact:
                    print("Inferred: " + rule["then"] + " Because: " + rule["explanation"])
                    facts.append(rule["then"])
                    seen.append(rule["then"])
                    found = True
        print("----------------------")
        self.infer(facts, seen, found)

engine = InferenceEngine(knowledge_base, rules)
engine.infer(["Diablo 2", "fighters"], [])
print("\n")
engine.infer(["Super Star Wars"], [])
