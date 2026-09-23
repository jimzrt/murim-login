# Character Profile Rules

Do not load this file unless creating or restructuring a profile.

- One chapter-safe profile per major character: `characters/<preferred-name>.md`.
- Heading Korean and `Aliases:` Korean in parentheses join the names ledger.
- Major means recurring, plot-bearing, or voice-sensitive; skip named extras.
- Keep only stable role, personality, voice, relationships, and active continuity.
- Cite source chapters and any wiki page used. The Korean and accepted translation control voice; the wiki is only a cross-check.
- Put useful unrevealed facts in the matching `characters/spoilers/<preferred-name>.md`.
- Update existing fields instead of appending chapter recaps.

Profiles currently include Jin Taekyung and Seong Jinho; create or update profiles only after the relevant chapter is accepted.

## Profile Retrofit

`python tools/profile_retrofit.py inventory` ranks profiles with weak voice
fields by recurrence in chapters that have both Korean source and accepted
translation. Build a bounded, history-spanning proposal for one profile with:

```bash
python tools/profile_retrofit.py propose "Jin Taekyung" --samples 6
```

For a name shared by distinct characters, restrict evidence to the identity's
first known chapter:

```bash
python tools/profile_retrofit.py propose "Jang Sam" --samples 6 --from-chapter 546
```

Review and edit the proposal under `.work/profile-retrofit/` before applying it:

```bash
python tools/profile_retrofit.py apply .work/profile-retrofit/Jin Taekyung.proposal.json
```

Applying checks that the profile and cited source/translation chapters have not
changed. The tool never applies model output automatically.