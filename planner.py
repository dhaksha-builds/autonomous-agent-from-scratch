class Planner:
  def __init__(self, llm, plan_template):
    self.llm = llm
    self.plan_template = plan_template

  def run(self, question, observation):
    plan = self.llm(
        prompt=self.plan_template.format(question=question, observation=observation),
        max_tokens=4096,
        temperature=0,
        top_p=0.95,
        repeat_penalty=1.2,
        echo=False
    )
    output = plan["choices"][0]["text"].strip()
    print(output)
    return output
