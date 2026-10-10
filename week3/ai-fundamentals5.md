# Agentic AI

## AI Evolution

- Manual (human)
- Assistance (human runs workflow, AI drafts, human accepts or rejects)
- Collaboration (flow runs itself and AI decides one defined step)
- Delegation (human sets a goal and model chooses steps, order, tools)

## AI Agent

System that can pursue a goal, decide what to do, take actions using tools and adapt
- Agency to make decisions on our behalf in pursuit of goal
- Humans can stay involved by
    - Approving the proposed plan
    - Gating actions (e.g. actively approve or reject proposed action)
    - Stopping (interrupt, redirect or cap)

### Agent Capabilites

- Maintains goal across multiple steps
- Has access to tools
- Decides sequence itself
- Self checks against result and retries when wrong

Agents are built on top of LLMs and extend their capabilities with:
- Instructions (goal and task definition)
- Tools (e.g. APIs, files, databases, code, applications)
    - Agent decides when to use tools based on goal
    - Stop and ask to give permission
- Memory (relevant information and past interactions)
- Agent logic (rules, strategies and decision framework)
    - Orient (read request)
    - Plan (generate sequence)
    - Act (use tools to change something)
    - Check (test result against goal and retry if needed)
    - Report (tell you what it did)

## Coding Agent

Specialised AI agent
- Codebase environment
- Developer tools
- Can run what its own output so the environment itself tells it whether it worked
- Changes are revertible because of VCS
- Wider blast radius since a terminal has full control of machine so needs tighter guardrails

### Vibe Coding

Build software by expressing outcome in natural language and AI handles implementation
- Lowers barrier to prototyping
- Human cannot understand and verify what the code is doing

## Responsibility

Agents have the ability to act without human approval so mistakes can have real-world consequences

Blast radius of access
1. Read
2. Create
3. Modify
4. Execute

### Access

Agents should only have the access required for its mission
- Scope (what it can access)
- Action (what it can do with that access)
- Duration (how long it will have access for)

### Reversibility

Agents should have less autonomy the harder it is to undo actions
- Easy to reverse = draft, analysis, local file, proposed change
- Harder to reverse = external communications, deleted record, code merged to production, published content, financial transaction

### Safe Use
- Sandbox (experiment safely) 
- Test (validate before it matters)
- Production (stronger controls, narrower permissions)