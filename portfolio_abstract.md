# Portfolio Abstract

**Project title:** Prompt Injection Risk in AI-Assisted Healthcare Referral Workflows

This project evaluates prompt-injection risk in a synthetic healthcare referral workflow where an AI assistant summarizes referrals, drafts provider follow-up notes, classifies administrative urgency, and creates CRM-style notes. The test set includes direct prompt injection, indirect prompt injection inside quoted referral text, sensitive-data requests, authority spoofing, fabrication pressure, and clinical overreach scenarios.

The project is designed as a defensive AI security evaluation. It uses synthetic data only and does not connect to live healthcare systems. The core research question is whether an AI assistant can resist injected instructions while preserving legitimate task completion in a regulated, high-trust workflow.

The initial implementation includes a test-case library, a scoring harness, a toy baseline assistant, a defended assistant, and a sample report structure. Future work will compare multiple real language models, expand the dataset, and evaluate mitigations such as structured outputs, human-review routing, and strict separation of trusted instructions from untrusted referral content.
