Continuously run python tools/run_next_mastering.py, one chapter at a time.

After each successful run, immediately run it again for the next chapter.

If a run fails, gets stuck, or needs a fix, do not lose track of the main task. Diagnose the problem, fix it, retry the same chapter until it succeeds, then continue with the next chapter.

If there is no meaningful progress for about 10 minutes, stop the stuck run and retry.

Never change the configured models, providers, model roles, or reasoning settings.

If OpenAI/Codex quota is exhausted, check the actual quota/reset time, wait until quota is available again, then resume the same chapter and continue the loop.

Keep doing this indefinitely unless there are no more chapters or the problem cannot be safely resolved.