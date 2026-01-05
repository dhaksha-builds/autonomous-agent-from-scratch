# autonomous-agent-from-scratch

# Autonomous Agent Control Loop (From Scratch)

## Overview
This project implements a minimal autonomous agent architecture without using LangChain or agent frameworks.
The agent operates via a closed-loop control system consisting of planning, execution, observation, evaluation,
conditional replanning, and enforced termination.

## Architecture
Planner → Executor → Observer → Evaluator → Decision

## Key Features
- Persistent agent state
- Conditional replanning logic
- Deterministic evaluator policy
- Enforced STOP condition
- Defensive normalization of LLM outputs
- No agent frameworks used

## Why This Matters
Most agent demos loop blindly.
This implementation focuses on control, safety, and decision enforcement.

## Example Run
(put your logs here showing `replan → replan → stop`)

## Limitations
- Single-plan execution (no step-level execution)
- Mocked environment (simulated follower growth)

## Future Work
- Step-wise execution
- Environment-backed metrics
- State serialization
