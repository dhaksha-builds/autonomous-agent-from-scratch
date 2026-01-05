class Observe:
  def __init__(self, llm, question, observe_template):
    self.llm = llm
    self.question = question
    self.observe_template = observe_template
  def run(self, results):
    observation = self.llm(
        prompt=self.observe_template.format(question=self.question,results=results),
        max_tokens=1024,
        temperature=0,
        top_p=0.95,
        repeat_penalty=1.2,
        echo=False
    )

    observation = observation["choices"][0]["text"].strip()
    print(observation)
    return observation
