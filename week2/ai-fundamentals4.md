# AI for Automation

## Workflow

Repeatable sequence of steps that takes input, applies decisions and produces output
1. Input
2. Sequence
3. Decisions
4. Output

## Automated Workflow

Predefined process that runs automatically when triggered and carries out a sequence of tasks without manual intervention
1. Trigger
2. Action
3. Condition

### Good candidate for automation

- Something that happens often
- Same steps every time
- Rule-based decisions
- Delays have consequences

### Connecter

Connects workflow platform to another system

## AI-powered Workflow

At least one step is decided by a model rather than a rule written in advance
- Makes workflows probabalistic rather than deterministic
- Can route to human in certain cases for safeguarding (HITL)
- Unstructured input handling (e.g. email bodies, call transcripts)
- Edge case coverage (generalises to cases you cannot anticipate)
- Intent rather than pattern matching (predefined)
- Generation rather than transfer (e.g. draft reply, write summary rather than just moving data between systems)
- Easy modification (can simply edit instruction to add new requirement)

### Good candidate for AI automation

- Input is prose, PDFs, transcripts, images
- Cases cannot be enumerated in advance
- Good enough judgement is better than no judgement
- Low risk in case of mistakes

### Diligence

- Approval (human actively accepts before flow continues)
- Escalation (defined route for cases the flow should not handle)
- Accountability (named human who owns the workflow)
- Verification (e.g. example ouput for the AI to validate against)