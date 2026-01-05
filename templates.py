plan_template = """[INST]
You are provided with the task of coming up with a plan for a question.

Think internally, but DO NOT show your reasoning.

Output ONLY a numbered list of 5–6 steps.
Each step must be on its own line.
Do not add any explanation or commentary.

If there are any modifications or fine tuning required then it will be available as feedback in the observation.

observation:{observation}
question:{question}
[/INST]
"""

observe_template = """[INST]
You are supposed to provide an observation report in one short sentence based on the progress seen in the result in comparison to the question. You should comment on how successful or unsuccessful or neutral the results of the plan has turned out to be based on the time taken
question:{question}
results:{results}
[/INST]
"""

evaluate_template = """[INST]
You are a strict decision function.

Rules:
- If follower_growth == 0 AND week >= 3 → output "stop"
- If follower_growth > 0 → output "execute"
- If follower_growth == 0 AND week < 3 → output "replan"

Output ONLY ONE WORD:
execute, replan, or stop

observation: {observation}
week: {week}
follower_growth: {follower_growth}
[/INST]
"""

