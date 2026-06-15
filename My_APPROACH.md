Thinking Model

My approach follows a structured engineering loop:

1. Problem Decomposition

Converted the vague specification into explicit functional and non-functional requirements such as alarm scheduling, background execution, CLI responsiveness, and input validation.

2. Constraint Identification

Identified system constraints: CLI-only interface, no external dependencies, and no persistent storage requirement. These constraints directly influenced the decision to use in-memory state and standard library threading.

3. System Design

Designed a modular architecture separating concerns into clock display, alarm management, background monitoring, and CLI orchestration. This ensures maintainability and clear separation of responsibilities.

4. Implementation Strategy

Built the system incrementally: alarm manager first, then clock utility, followed by background alarm service using threading, and finally CLI integration. AI was used as a design assistant to validate concurrency approach and edge cases before implementation.

5. Validation

Performed manual testing for invalid inputs, duplicate alarms, concurrent execution stability, and alarm trigger accuracy. Also verified that CLI interaction remains responsive while background monitoring runs.

link to my video https://drive.google.com/file/d/1Q8Za2Z8Bdcnd_PEBtXH1jBpIlJEE-P7_/view?usp=sharing 