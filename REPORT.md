# The project REPORT is where students will document key learnings, challenges, and reflections on their experience using CoPilot for software development. 

# First Impressions - Initial Take on the Project Assignment
## In this section, students will provide their initial thoughts on the project assignment, including their understanding of the requirements, any assumptions they made, points that need clarification, and their overall approach to tackling the project.
## Initial Thoughts
## Assumptions Made
## Points Needing Clarification

# Key Learnings
## Here, students will summarize the most important things they learned while working on the project. This could include computer science related concepts, technical skills, insights about using CoPilot effectively, and any new concepts or tools they encountered
## Computer Science Concepts and Technical Skills
## Insights about Using CoPilot Effectively
## New Concepts or Tools Encountered

# Report on CoPilot Prompting Experience
## Student may pull examples from the JOURNAL.md to illustrate their experience, including specific interactions that were particularly helpful or challenging.
### Types of prompts that worked well
### Types of prompts that did not work well or failed

# Limitations, Hallucinations and Failures
## In this section, students will document any instances where CoPilot provided incorrect or misleading information (hallucinations) or where it failed to provide a useful response. They will analyze why these issues occurred and how they impacted their work on the project.
## For example: Fabricated APIs, Deprecated functions, Subtle logical errors, Confident but wrong explanations, Over-engineered solutions, Under-engineered solutions, overcomplicated code, oversimplified code, etc.
## Examples of Hallucinations or Failures or Misleading Information or Confident but Wrong Explanations, or Over-engineered or Under-engineered Solutions
## Analysis of Why These Issues Occurred
## Impact on the Project

# AI Trust
## When did I trust the AI?
## When did I stop trusting it?
## What signals or situations or patterns indicated low reliability?

# What I Learned
## What did you learn about software development?
## What did you learn about using AI tools?
## When should you trust AI? When should you double-check it?

# Reflection
## Did AI make you faster? Why or why not?
## Did you feel in control of the code?
## Would you use AI the same way next time? What would you change?



# First Impressions - Initial Take on the Project Assignment

## Initial Thoughts
When I first saw this project I thought it would be straightforward - just a simple word guessing game. But once I started thinking about the states and variables needed, I realized there were more edge cases than I expected.

## Assumptions Made
I assumed I could build it in one or two functions. I ended up needing 8 separate functions to keep the logic and UI properly separated.

## Points Needing Clarification
I wasn't sure at first whether replay had to be supported without restarting the program, or whether the masked word needed spaces between letters.

# Key Learnings

## Computer Science Concepts and Technical Skills
I learned how to use type hints properly in Python, write pure functions with no side effects, and use list comprehensions. I also learned how to separate game logic from display functions.

## Insights about Using CoPilot Effectively
Asking Copilot to review my code was much more useful than asking it to write everything. It caught bugs I missed, like multi-character guesses passing validation.

## New Concepts or Tools Encountered
I used pytest for the first time to write and run unit tests.

# Report on CoPilot Prompting Experience

### Types of prompts that worked well
Asking Copilot to review specific functions worked really well. It gave detailed feedback ordered by severity with exact line references.

### Types of prompts that did not work well or failed
When I asked for help writing tests, Copilot kept asking me Socratic questions instead of just helping. It was useful for learning but slow when under time pressure.

# Limitations, Hallucinations and Failures

## Examples of Hallucinations or Failures
Copilot didn't hallucinate in this project, but it did initially miss that the recursion in play_game() could cause a stack overflow after many replays.

## Analysis of Why These Issues Occurred
It focused on correctness of logic but not on long-term runtime behavior.

## Impact on the Project
Minor - it was caught during the review phase and fixed quickly.

# AI Trust

## When did I trust the AI?
When it reviewed my code and found real bugs like missing input validation.

## When did I stop trusting it?
When it was being overly cautious and asking too many questions instead of just helping implement.

## What signals indicated low reliability?
When Copilot gave vague answers or kept redirecting instead of being direct.

# What I Learned

## What did you learn about software development?
Breaking a program into small pure functions makes it much easier to test and debug.

## What did you learn about using AI tools?
AI is most useful as a reviewer and collaborator, not as a code generator you blindly accept.

## When should you trust AI? When should you double-check it?
Trust it for syntax and patterns. Always double-check logic, edge cases, and anything correctness-critical.

# Reflection

## Did AI make you faster? Why or why not?
Yes for reviewing and catching bugs. No when it kept asking questions instead of helping directly.

## Did you feel in control of the code?
Yes - because I wrote the core functions myself and used Copilot mainly for review and cleanup.

## Would you use AI the same way next time? What would you change?
I would use Agent Mode more directly and be more specific in my prompts to avoid the Socratic back-and-forth.
