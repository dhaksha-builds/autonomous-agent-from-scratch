state = AgentState()

planner = Planner(mistral,plan_template)
executor = Execute()
observe = Observe(mistral, ig_question, observe_template)
evaluator = Evaluate(mistral, evaluate_template)
plan = None
observation = ''
iters = 0

while iters<20:

  if plan == None or state.decision == 'replan':
    plan = planner.run(
        ig_question,
        state.observation
    )



  results = executor.run(state, plan)

  state.observation = observe.run(results)

  state.decision = evaluator.run(
      state.observation,
      state.week, 
      state.follower_growth
      )

  if state.decision == 'stop':
    break

  
  iters += 1
