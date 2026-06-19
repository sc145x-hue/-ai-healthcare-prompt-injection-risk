# Sample Report: Prompt Injection Risk in AI-Assisted Healthcare Referral Workflows

## Executive summary

This starter evaluation compares a deliberately weak baseline assistant against a defended assistant pattern across eight synthetic healthcare referral test cases. The defended pattern improved average rule-based score from 2.25/4.00 to 3.75/4.00 in the toy demonstration.

## Key finding

The highest-risk failure modes in the baseline assistant were:

- Following unauthorized approval or bypass instructions
- Including fake sensitive identifiers
- Treating quoted source text as workflow instructions
- Fabricating payer or clinical status
- Accepting persistent instruction changes from user-provided text

## Recommended controls

1. Treat all referral source text as untrusted data.
2. Use structured outputs with separate fields for summary, risk flags, and recommended next action.
3. Block the assistant from approving services, confirming coverage, or making clinical determinations.
4. Redact or avoid sensitive identifiers by default.
5. Escalate ambiguous, clinical, payer, privacy, or suspicious instructions to human review.
6. Evaluate models against direct and indirect prompt-injection test suites before deployment.

## Portfolio next step

Replace the toy assistant with a real LLM call, expand the dataset to 50+ scenarios, and publish results showing model behavior before and after adding structured guardrails.
