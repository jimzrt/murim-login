# Final Touches — Murim Login

## Goal

Prepare one mastered chapter for readers. This pass adds footnotes, repairs formatting, and fixes duplicate or missing sentences. It is not a fluency rewrite.

Keep the mastered prose. Change a sentence only to attach a footnote, repair System / thought / speech / chat formatting, restore a source sentence the English dropped, remove an English sentence the Korean does not support, or fix a character's name or pronoun as described below.

## Names and pronouns

The packet lists the profiled characters named in this chapter with their gender, and any required name corrections.

- Use the glossary or character-card English for every name. Apply each required name correction everywhere it occurs.
- Do not add “Young Hero” to a name, and do not restore it where the English uses the name alone. `소협` is rendered by context (`RULES.md` → Address).
- Korean usually omits pronouns. When a card gives `female` or `male` and the English uses the other pronoun for that character, fix the pronoun. Leave pronouns alone for a character whose gender is `unknown`.

## Duplicates and omissions

Compare the English with the Korean source.

- Restore source facts, events, dialogue, and sentences the English dropped, in the same place in the scene.
- Remove English sentences that have no support in the Korean.
- Keep a bold label that names a quoted document, manual, warning, or sign, such as `> **Warning**`. Keep it when this chapter recalls or reprints a notice that was labeled earlier, even if the Korean reprint shows only the body.
- Keep repetition the Korean itself repeats: comedy, panic, emphasis, echoed dialogue, and short beats such as `……`.
- Do not treat a short refrain or a deliberate echo as a duplicate.

## Footnotes

Use Markdown footnotes (`[^1]`, `[^2]`, …). Number them in order of first appearance, starting at 1 for this chapter. Put every definition in one block at the end of the file.

Within this chapter, write one definition for a term, unit, amount, or reference. Every later occurrence of that same thing reuses the same marker. `goshiwon` five times is one note, and so is `hyung`. A different amount or a different term gets its own note. Another chapter may carry its own note for the same term.

Write notes in factual English. No spoilers and no jokes added by the note. Romanize words. A note may include the original character when it is explaining that character. Keep Hangul jamo already used as chat reactions, such as ㅋㅋ and ㄷㄷ.

Never write a footnote whose job is to identify or describe a story character, creature, pet, group, place, item, or plot event. The story introduces its own cast; a note must not say who someone is, what they did, or what a name refers to inside the story. This holds even when the glossary or a character card explains the name: those are reference for you, not footnote material.

When a story name coincides with a real person, brand, or work (Magic Johnson, Mimi), the name is the story's. Do not footnote the real one unless the Korean source itself makes that reference.

Add a note only when an English reader would otherwise miss the meaning or the conversion. Skip it when the sentence already says what the reference means. A translated proverb whose warning is plain, a joke the next line completes, a place name used as a place, and a fictional law the dialogue already describes do not get notes.

Skip a conversion footnote when the prose already states both metric and imperial for that quantity.

### Won

Footnote Korean won, including round figures and vague amounts (“hundreds of millions of won”), when the prose does not already give the conversion. Use only the project rates in the packet. Show dollars, then euros, as approximate figures. Round large amounts to about two significant figures and say “about.” For a vague amount, give the approximate range those words cover. One note per distinct amount; reuse it for every later mention of that same amount.

Do not convert traditional money (nyang, taels, cash) or Chinese yuan with the won rate. Explain those with a cultural or historical note only when the English does not already carry the meaning.

### Units

Footnote a Korean or Chinese traditional unit, or a metric quantity, once in the chapter, with both metric and imperial, using this table:

| Unit | Use | Metric | Imperial |
| --- | --- | --- | --- |
| pyeong (평) | area | 3.31 m² | 35.6 ft² |
| geun (근) | Korean weight | 600 g | 1.32 lb |
| ja / cheok (자) | length | 30.3 cm | 11.9 in |
| chi (치) | length | 3.03 cm | 1.19 in |
| don (돈) | weight | 3.75 g | 0.132 oz |
| gwan (관) | weight | 3.75 kg | 8.27 lb |
| ri (리), Korea | distance | 393 m | 0.244 mi |
| li (里), China | distance | 500 m | 0.311 mi |
| jin (斤), modern Chinese | weight | 500 g | 1.10 lb |
| liang (两), modern Chinese | weight | 50 g | 1.76 oz |

Choose Korean ri or Chinese li from the setting. Say which one the note uses.

Also footnote metric quantities already in the English (kilometers, meters, centimeters, kilograms, grams, liters, square meters, degrees Celsius) with the imperial equivalent. Use unit words or abbreviations (`ft`, `in`, `mi`, `lb`, `oz`, `gal`). Do not use `"` or `'` as unit marks.

### Cultural references

Footnote a Korean, Chinese, or other Asian word, custom, institution, food, joke, or allusion when the English does not already carry it: `goshiwon`, `hyung`, `doenjang`, `jeonse`. Explain it in one or two sentences. One note per term in the chapter, reused by every later occurrence.

Leave it unnoted when the English is already clear. Do not explain a proverb the translation has already stated, a pun the scene completes, or ordinary vocabulary.

Do not footnote standing series vocabulary. Never add a note whose job is to define any of these, including ordinary variants and compounds:

- Murim
- qi, including demonic qi, innate qi, and qi deviation
- dantian, including the Upper, Middle, and Lower Dantian
- internal energy
- mana

A note about something else may mention these words. Do not attach a marker to them.

## Formatting

Enforce these four patterns. Repair System, speech, thought, and chat formatting when it drifts. Leave every other blockquote heading as it stands.

- **System.** Each real game System panel is one Markdown blockquote headed exactly `> **System**`. Keep the panel’s lines inside that blockquote. Start a new panel only when prose intervenes. Keep every `> **System**` panel from the mastered chapter, including a notice the narrator only hears. Do not turn a panel into italics, a sound effect, or narration. Do not repeat a panel. A notice the mastered chapter already shows more than once stays repeated that many times, and no more. Do not wrap System text in square brackets or label a manual, sign, or ordinary quotation as System. A manual or remembered notice keeps its own label, such as `> **Warning**` or `> **Product User Manual**`. That label is not a System panel, and it is not drift.
- **Speech.** Spoken dialogue uses curly double quotes (`“` `”`). Not straight quotes, not italics.
- **Thoughts.** Direct thoughts are italics with no quotation marks. Keep a mastered thought in italics. Do not turn it into spoken dialogue.
- **Chat and comments.** Public comment threads and private chat logs shown as threads are one blockquote. Each message line begins with `└`, as in `> └ **Name:** message`. Keep a thread title that is not itself a message, such as `> **Peace Guild**`, on its own line above the messages. Do not add a `**Chat**` heading. A status line that is only a name or level, such as `> **Lv. 22 Hyuk Mujin**`, is not a chat message. Leave that line unchanged, including the bold. Ordinary spoken dialogue stays in curly quotes.
- **Headings.** The only Markdown heading is `# Chapter N`. Do not add `##` or `###`. A diary title or similar label stays a bold line, `**Training Day 1**`, even when the mastered copy used a smaller heading.

Leave narration as narration. Scene breaks stay `* * *`, with the same count as the source.

## Output contract

Return only the complete English Markdown chapter. The first nonblank line must be `# Chapter N`. No status line and no model preamble. Do not add Hangul syllables. Chat jamo and a character cited in a note may stay.
