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
        # Get the first fact in the list and see if it's in the knowledge base.
        # If it is, print it out. If not, see if it's a subset of the
        # if statement for a rule. If it is, print out the then statement
        # and the explanation. Then, add the then statement to the list
        # of facts and call the function again.
        # If it's neither, print sorry, I don't know what that game / genre.

        fact = facts.pop(0)
        found = False
        if fact in self.knowledge_base:
            print(f"{fact}: {self.knowledge_base[fact]}")
            found = True
        for rule in self.rules:
            # If the rule's if statement is a subset of the facts,
            # I nnow know something else
            if rule["if"] == fact:
                print("Inferred: " + rule["then"] + " Because: " + rule["explanation"])
                facts.append(rule["then"])
                found = True
        print("----------------------")
        if not found:
            print("Sorry, I don't know what that game / genre.")
        if len(facts) == 0:
            return
        self.infer(facts)


engine = InferenceEngine(knowledge_base, rules)
engine.infer(["Diablo 2", "fighters"])
print("\n")
engine.infer(["Super Star Wars"])
