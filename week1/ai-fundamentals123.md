# Demystifying AI

## Artificial Intelligence

Simulation of human intelligence
- Traditional AI = designed for a specific task (e.g. facial recognition)
- Modern AI = generalist and adaptable (e.g. chatbots)
- Machine learning = subset of AI where model learns rules from data rather than being programmed using
    - Decision trees to learn rules
    - Neural networks to learn patterns
    - Statistical models to learn relationships
- Deep learning = subset of machine learning that uses multi-layered neural networks
- Generative AI = deep learning that produces something new (e.g. text, code, images)

## Neural Networks

Simulation of neural networks in brain
- Composed of interlinked nodes arranged into layers that process information
    - CNN = Convolutional Neural Network (image classification and computer vision)
    - FNN = Feed-Forward Neural Network (structured data processing without memory)
    - RNN = Recurrent Neural Network (sequential data processing with memory)
- Networks learn by adjusting strength of connection between nodes

## Model

Neural network trained on data to perform task
- Learning = model training
    - Supervised learning uses data that includes known answers or labels
    - Unsupervised learning uses data without being given the correct answers
    - Reinforcement learning incentivises model to think correctly using rewards
- Inference = model uses learning data to infer expected result using new data
- Training dataset = augmented
- Validation (testing) dataset = normal

# Understanding Modern AI

## LLM

Large Language Model
- Specialised neural network trained on vast textual datasets to generate text
- LMM = Large Multimodal Model (most LLMs are now multimodal but still referred to as LLMs)
- LLMs do not retrieve facts but infer the most likely answer

## Architecture

1. Text input (user writes prompt)
2. Tokenisation (prompt split into small pieces of text)
3. Embedding (each token becomes numerical vector representation)
4. Transformer (many layers compare tokens against context)
    - Comprehends what user wants and puts forward most likely tokens
    - Attention (keywords)
    - Context mixing (how words link together)
    - Feed forward (writes prompt as per interpretation)
    - Repeat layers (sends to next transformer)
5. Output (model predicts most likely reply)
    - Takes final token vectors from transformer and calculates probabilities
    - Tokens that best fit context have higher probabilities
    - Model selects most probable token using probability distribution
    - Repeats until response is generated

## Inference Parameters

- Models should be non-deterministic (i.e. identical prompts generate different answers)
- Temperature = randomness
    - Low temperature = responses are more deterministic (academic writing, fact-finding)
    - High temperature = responses are more unpredictable (creative writing, conversation)
- Top-K sampling = keeps the K most likely tokens
- Nucleus sampling = adds most likely tokens until cumulative probability reaches threshold
- Presence penalties = prevents model from fixating on already-used tokens
    - Low presence penalty = responses are more repetitive and focused
    - High presence penalty = responses are more varied and original

## Limitations

- Hallucinations = false claims or facts
- LLMs are prone to error due to reliance on probability
- LLMs can take on demographic biases found in training data and tend to disproportionately reflect Western perspectives
- Training data should be vast and varied
- Entity disambiguation = LLM cannot distinguish between two entities of the same name
- Model collapse theory = LLM repeatedly training on LLM data

## Context Window

- Smaller context windows reduce ability to handle long conversations and large documents
- Larger context windows allow more information to be considered but may lead to recency bias or overlooked details
- RAG = Retrieval-Augmented Generation
    1. Search for relevant information
    2. Add retrieved information to context window
    3. Answer using both general knowledge and retrieved context

# Effective AI Use

AI is trained to be helpful and cooperative which can lead to:
- Sycophancy (prioritise user agreement over independent reasoning)
- Overconfidence (AI prefers to make a confident choice and risk being wrong rather than admit it doesn't know due to reinforcement learning)
    - RLCR = Reinforcement Learning with Calibration Rewards (confidence vs correctness determines rewards)
- Recency bias (important context from earlier in the conversation receives less attention)

## Prompt Engineering

Designing, structuring and refining instructions given to AI to generate more useful responses

### Framework

1. Persona (define role, expertise or perspective)
2. Task (clearly state outcome, deliverable or action)
3. Context (provide relevant background, documents, data and examples)
4. Constraints (set rules and requirements)
5. Evaluate output and iterate if needed

### Context Engineering

Designing and managing the information given to AI so that it has the right context for the task
- More context is not always better (prioritise relevent, current and trustworthy information)
- Do not include PII or IP due to AI's context capture for training

## Responsibility

### Environmental Impact

Servers in AI data centres generate heat and their cooling systems use water and energy
- Use prompt engineering to avoid unnecessary repeated generations
- Use the simplest tool for the need
- Reuse and refine existing outputs rather than starting over
- Avoid generating unnecessary multimodal outputs

### Human-In-The-Loop (HITL)

Human oversight is essential because AI can make mistakes
- Review AI outputs and validate accuracy, appropriateness and safety before taking action
- Approve important decisions and only use AI to assist with decision-making process

### Model Selection

Use the lowest model for the need, balancing:
- Task complexity
- Required accuracy
- Risk level
- Cost and resource use
- Context window size

## AI Fluency Framework

1. Delegation (What should be delegated to AI vs. what should be done by humans)
2. Description (prompt engineering)
3. Discernment (assess usefulness of AI output)
4. Diligence (take responsibility for AI use)