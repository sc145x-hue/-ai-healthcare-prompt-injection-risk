# Prompt Injection Risk in AI-Assisted Healthcare Referral Workflows

A portfolio-ready starter project for exploring **AI security risk** in a realistic, non-clinical healthcare referral workflow.

## Project summary

This project evaluates how an AI assistant used in a healthcare referral workflow handles benign tasks when the user input contains indirect or direct prompt-injection attempts. The goal is to measure whether the assistant:

1. Completes the legitimate business task.
2. Refuses or ignores injected instructions.
3. Avoids disclosing fake sensitive data or internal instructions.
4. Escalates high-risk cases for human review.

This is a safe, defensive research project. It uses synthetic data only and does not interact with live healthcare systems, real patients, credentials, or production tools.

## Why this project matters

Healthcare referral workflows involve sensitive context, handoffs between organizations, and administrative pressure to move quickly. AI assistants can help with triage and summarization, but they also introduce risk if malicious or malformed input can override system instructions, leak sensitive details, or trigger unsafe workflow actions.

This project aligns with the AI Security track because it studies prompt-injection risk, testing methodology, and practical mitigations for LLM-enabled workflows.

## What is included

```text
ai_healthcare_prompt_injection_portfolio/
├── README.md
├── requirements.txt
├── data/
│   ├── referral_test_cases.csv
│   └── attack_prompt_library.csv
├── docs/
│   ├── research_design.md
│   ├── portfolio_abstract.md
│   ├── literature_review_start.md
│   └── safety_and_ethics.md
├── src/
│   ├── evaluator.py
│   └── run_demo.py
├── results/
│   └── sample_results.csv
└── tests/
    └── test_evaluator.py
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
# .venv\\Scripts\\activate  # Windows
pip install -r requirements.txt
python src/run_demo.py --mode defended
python src/run_demo.py --mode naive
```

The demo uses a toy assistant so the project can run without API keys. To make this application-ready, replace the toy assistant in `src/run_demo.py` with calls to a real model API or a local open-source model, then run the same test cases.

## Suggested GitHub description

> Defensive AI security evaluation of prompt-injection risk in synthetic healthcare referral workflows, with test cases, scoring logic, and mitigation recommendations.

## Next improvements

- Add a real LLM provider adapter.
- Expand the test set from 8 cases to 50–100 cases.
- Add automated scoring with structured JSON outputs.
- Compare baseline, guarded, and human-review workflows.
- Publish a short report with findings, limitations, and recommendations.

