# Local execution workflow

Use ChatGPT/GitHub for planning and specs, and Pi + local Qwen 9B for execution.

## Rule

Run exactly one spec per fresh Pi session.

Recommended cycle:

1. git pull
2. start pi from the project root
3. ask Pi to read and execute exactly one spec
4. require the spec verification command to pass
5. exit Pi
6. start a fresh Pi session for the next spec

Do not batch multiple specs into one long session. On this workstation, accumulated context above ~20k tokens makes local prefill unnecessarily slow.

## Safety

- no sudo unless explicitly approved
- no package installation unless explicitly approved
- work only inside the current project
- keep tests/verification green before advancing
