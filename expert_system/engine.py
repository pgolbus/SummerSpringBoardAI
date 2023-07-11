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
]

class InferenceEngine:
    def __init__(self, knowledge_base, rules):
        self.knowledge_base = knowledge_base
        self.rules = rules

    def infer(self, facts):
        # Get the first fact in the list
        fact = facts.pop(0)

        #see if it's a fact in the knowledge base.
        found = False
        if fact in self.knowledge_base:
            # If it is, print it out
            print(f"{fact}: {self.knowledge_base[fact]}")
            found = True

        # see if it's a rule's if statement.
        for rule in self.rules:
            if rule["if"] == fact:
                found = True
                #if it is, print out the then statement and the explanation
                print("Inferred: " + rule["then"] + " Because: " + rule["explanation"])

                #add the then statement to the list of facts
                facts.append(rule["then"])
        print("\n----------------------\n")

        # If it's neither, print sorry, I don't know what that game / genre.
        if not found:
            print("Sorry, I don't know what that game / genre.")

        # if there are still facts left, call the function again
        if len(facts) > 0:
            self.infer(facts)

        # if there are no more facts, we're done
        return

if __name__ == "__main__":
    engine = InferenceEngine(knowledge_base, rules)
    engine.infer(["Diablo 2", "fighters"])
    print("\n")
    engine.infer(["Super Star Wars"])
