# Final Touches — Murim Login

## Goal

Prepare one mastered chapter for readers. This pass adds footnotes, repairs formatting, and fixes duplicate or missing sentences. It is not a fluency rewrite.

Keep the mastered prose. Change a sentence only to attach a footnote, repair System / thought / speech / chat formatting, restore a source sentence the English dropped, or remove an English sentence the Korean does not support.

## Duplicates and omissions

Compare the English with the Korean source.

- Restore source facts, events, dialogue, and sentences the English dropped, in the same place in the scene.
- Remove English sentences that have no support in the Korean.
- Keep repetition the Korean itself repeats: comedy, panic, emphasis, echoed dialogue, and short beats such as `……`.
- Do not treat a short refrain or a deliberate echo as a duplicate.

## Footnotes

Use Markdown footnotes (`[^1]`, `[^2]`, …). Number them in reading order, starting at 1 for this chapter. Put every definition in one block at the end of the file. Move existing definitions there and keep their facts.

This pass overrides the usual “footnote once” rule. Footnote every occurrence in this chapter, even when an earlier sentence or an earlier chapter already explained it. A repeated note may be shorter, but it must still contain the conversion or the explanation.

Write notes in factual English. No spoilers and no jokes added by the note. Romanize words. A note may include the original character when it is explaining that character. Keep Hangul jamo already used as chat reactions, such as ㅋㅋ and ㄷㄷ.

Skip a conversion footnote only when that same occurrence already states both metric and imperial.

### Won

Footnote every mention of Korean won, including round figures and vague amounts (“hundreds of millions of won”). Use only the project rates in the packet. Show dollars, then euros, as approximate figures. Round large amounts to about two significant figures and say “about.” For a vague amount, give the approximate range those words cover.

Do not convert traditional money (nyang, taels, cash) or Chinese yuan with the won rate. Explain those with a cultural or historical note instead.

### Units

Footnote every Korean or Chinese traditional unit with both metric and imperial, using this table:

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

Footnote every Korean, Chinese, or other Asian cultural reference a general English reader might not fully understand: institutions, food, customs, holidays, history, myth, religion, slang, wordplay, memes, and jokes. Explain the reference in one or two sentences. Do this even when the English already carries part of the meaning, and even when the joke still works in English.

## Formatting

Enforce these four patterns. Repair anything that drifts.

- **System.** Each real game System panel is one Markdown blockquote headed exactly `> **System**`. Keep the panel’s lines inside that blockquote. Start a new panel only when prose intervenes. Do not wrap System text in square brackets or label a manual, sign, or ordinary quotation as System.
- **Speech.** Spoken dialogue uses curly double quotes (`“` `”`). Not straight quotes, not italics.
- **Thoughts.** Direct thoughts are italics with no quotation marks.
- **Chat and comments.** Public comment threads and private chat logs shown as threads are one unheaded blockquote. Each message line begins with `└`, as in `> └ message`. Do not add a `**Chat**` heading. Ordinary spoken dialogue stays in curly quotes.

Leave narration as narration. Scene breaks stay `* * *`, with the same count as the source.

## Output contract

Return only the complete English Markdown chapter. The first nonblank line must be `# Chapter N`. No status line and no model preamble. Do not add Hangul syllables. Chat jamo and a character cited in a note may stay.
