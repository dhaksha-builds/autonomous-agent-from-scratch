class Evaluate:
    def __init__(self, llm, evaluate_template):
        self.llm = llm
        self.evaluate_template = evaluate_template

    def run(self, observation, week, follower_growth):
        prompt = self.evaluate_template.format(
            observation=observation,
            week=week,
            follower_growth=follower_growth
        )

        response = self.llm(
            prompt=prompt,
            max_tokens=10,
            temperature=0.1,
            top_p=1,
            repeat_penalty=1.2,
            echo=False
        )

        raw_text = response["choices"][0]["text"]

        decision = (
            raw_text
            .strip()
            .lower()
            .replace(".", "")
            .replace("\n", "")
            .replace("\r", "")
        )


        if decision not in {"execute", "replan", "stop"}:
            print("Invalid decision, defaulting to replan")
            decision = "replan"

        return decision
