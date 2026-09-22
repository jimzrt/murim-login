/loop

Master the next available chapter using the repository's mastering workflow.

In the current iteration, run:

```bash
python tools/run_next_mastering.py
```

Wait for the command to finish before doing anything else.

If it succeeds, do not summarize, pause, or ask for input. Immediately continue with the next chapter.

If it fails, gets stuck, times out, or needs a fix, remain on the same chapter. Inspect the actual command output and repository artifacts, diagnose the root cause, make the smallest safe fix, and rerun the same chapter. Do not advance until that chapter succeeds.

If there is no meaningful progress for about 10 minutes, stop only the stuck child process, preserve the repository state, and retry the same chapter.

Never change configured models, providers, model roles, timeouts, or reasoning settings.

If OpenAI/Codex quota is exhausted, inspect the actual quota and reset time, wait until quota is available, then retry the same chapter.

Use the existing repository workflow and locks. Do not use parallel agents, TODO items, planning steps, or a separate implementation path for this campaign.

Stop only when `python tools/run_next_mastering.py` explicitly reports that no chapters remain, or when a genuinely unsafe and unresolvable blocker is proven. A tool interruption, repeated-command guard, timeout, session boundary, malformed model response, or transient provider error is not completion; recover and continue.