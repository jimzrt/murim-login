<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0617.txt",
      "sha256": "3b7d530516d744e0e1bc8a492795cbfc7757de7ef4ff9ac727631eda6c47f63f",
      "bytes": 14975
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "3e8a7acdd1a0e301671cf77d6b5b46bfd9bf729754ff0cbf1aacac46573c57c7",
      "bytes": 1477
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "96783d1eada5d051bb3f3faf589b67343b470abeb49606ae7838739780ac3741",
      "bytes": 191592
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "d37e0f585ee8a0a32c0d767583a19cf46cdc7e44671b61a25085b926f2f24fd8",
      "bytes": 553
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "d1b3363c5137cd4852dc92fefcb25c69b31ffe6ca93bdd88674917af05613983",
      "bytes": 1147
    },
    {
      "path": "characters/Jang Sam.md",
      "sha256": "4da57e52f2532e2f448f78c4a14177c006e79429b521c0fa826fc9a68639d0cd",
      "bytes": 408
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "5a54a23c369ff5d356779326a7b2dde3c5443b76d007e7d46f33f34de2cbefcd",
      "bytes": 1775
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "1951bb1ec1307405b390a803835722aee69d28ffe3cf6b601483ada17010b91a",
      "bytes": 622
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "27db5f8233cc019733cd3be40252a1785f91b2736ab1dff9d365d05c6924265e",
      "bytes": 959
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "fa6d0dd3aadf19fb89c0a157ee2ad0dee0850e27bb0cdb168f5d57de500ef389",
      "bytes": 1061
    },
    {
      "path": "characters/Mu Song.md",
      "sha256": "a2d7cd1a6a4d375792248422d5318a32e58e34b0bca86f1ea79f1e63a9f4b659",
      "bytes": 1114
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "e6f6b227a7ba3bfca33afb4317ef01b57aacd5679ddeeddb71a236aeb3d0b13c",
      "bytes": 899
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "6a5f0c236ac53a5fda006118f67eccd8694174a2fb3faa5a1bcf1941626f0638",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "a49716ed7ea55032c455762d71b97c030c3e4d22371af94d3a8c85661ef34b39",
      "bytes": 957
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "91e39e00d4e83fb7eac082fcf5ed3eb92fdec5bea824dec2e25fed9c2c6dbcb6",
      "bytes": 528
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "630eb81ce8d3238c11058f1c750a888d8cf1ef8aeee2234372cc58146cbea3ff",
      "bytes": 193961
    }
  ],
  "estimated_tokens": 14004
}
-->

# Durable State Update — Chapter 617

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 617. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 617. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that
are absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
Before returning JSON, verify every `speaker` and `addressee` value contains at
least one Hangul character; use the Korean source spelling even when the same
person's English name appears in the reading copy. If no valid new pair exists,
return `"address_pairs": []`.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 617,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 617,
    "continuity_sources": [617],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "진태경",
      "addressee": "문경",
      "kinship": "kinship or role relation",
      "normal_address": "established English address",
      "speech_level": "speech level",
      "notes": "brief note"
    }
  ],
  "profile_updates": [
    {
      "path": "characters/Listed Profile.md",
      "current": "- **Role:** exact current full line",
      "replacement": "- **Role:** finished replacement full line"
    }
  ],
  "profile_creations": [
    {
      "filename": "English Name.md",
      "korean": "source name",
      "english": "English Name",
      "aliases": [],
      "role": "stable role",
      "personality": "stable traits",
      "voice": "stable voice",
      "relationships": "stable relationships"
    }
  ]
}

Use empty arrays when no name, address-pair, or profile change is required.
`profile_creations` is only for characters with no existing `characters/` file.
If the person already appears under Listed compact profiles, use `profile_updates`.

## Prior durable context

```json
{
  "active_continuity": [
    "The Fire Dragon Pavilion expedition has crossed Hubei and reached Sichuan using secret horse-caravan shortcuts and Ju Hwaran's route knowledge.",
    "Ju Hwaran's expertise has substantially accelerated the expedition and exceeded Jin Taekyung's expectations.",
    "Jin Taekyung can carry two horses, while Taishan can carry three.",
    "Song Ilseom's willow-leaf saber was given to him when he was a sword boy for a Third Rate wandering martial artist, and he used it for his first killing at approximately age twelve.",
    "Song Ilseom has expressed concern that Ju Hwaran not be hurt or die needlessly.",
    "Swift ships flying Water Dragon Stronghold flags have arrived through the fog on the Yangtze in Sichuan."
  ],
  "continuity_sources": [
    616
  ],
  "open_questions": [
    "Who is aboard the Water Dragon Stronghold's swift ships, and will they transport the expedition?",
    "Why does Ju Hwaran flee whenever Jin Taekyung sincerely praises her?",
    "Is Song Ilseom's commitment to Ju Hwaran more than paid escort duty?"
  ],
  "safe_through": 616,
  "temporary_decisions": [
    "Use horse caravans for 마방 and Pavilion Master for 화룡각주 and 각주.",
    "Use Young Lady Ju for 주 소저.",
    "Preserve Taishan's clipped, childlike speech.",
    "Render 금분세수 as golden-basin handwashing with a retirement-ritual footnote.",
    "Render 불밥 할아버지 as Fire-Rice Grandpa."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 매종학    | **Mae Jonghak**    |
| 송일     | **Song Il**        |
| 파륜     | **Pa Ryun**        |
| 주화란    | **Ju Hwaran**      |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 해상왕    | **Seafaring King**            | Pa Ryun        |
| 일신     | **One God**         |
| 태원진가   | **Jin Family of Taiyuan**        |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 장강수로맹  | **Yangtze River Channel League** |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 신법     | **movement technique**                           |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 정파     | **orthodox faction**                             |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 제자     | **Disciple**                                 |
| 선배     | **Senior**                                   |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 칭호               | **Title**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소저      | **Young Lady**                                                  |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 무송 | **Mu Song** | Lord of Water Dragon Stronghold and disciple of the Seafaring King. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 인피면구 | **human-skin mask** | Disguise made from peeled human facial skin. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 박도 | **broad-bladed saber** | Rough weapon swung by the bald swordsman. |
| 천기 | **heavenly patterns** | Celestial patterns Hong Dao studies to perceive major changes and omens. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 녹림맹 | **Green Forest Alliance** | Bandit alliance receiving Black Mountain Stronghold’s tribute. |
| 운남 | **Yunnan** | Region from which Jongni Chu comes. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 수룡채 | **Water Dragon Stronghold** | Major river stronghold belonging to the Yangtze River Channel League. |
| 선화아 | **Ship-Fire Boy** | Mu Song's sobriquet; literally a child who lights fires aboard a ship. |
| 채주 | **Stronghold Lord** | Title used for the lord of a water stronghold. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 장강일도 | **Yangtze One Saber** | Hwang Chung's sobriquet. |
| 쾌조선 | **swift ship** | Fast vessel operated by the Yangtze River Channel League. |
| 묘족 | **Miao people** | Ethnic group the Escort Bureau expects to encounter near Yunnan. |
| 새외 | **Outer Lands** | Lands outside the Central Plains and its Murim. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 송일 | 진태경 | hostile Zhongnan Elder to accused outsider | you / Jin Taekyung | hostile and threatening | Song Il questions Taekyung's identity and later threatens him over Gong Ilhyuk's injury. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 수하 | 채주 | subordinate_to_stronghold_lord | Stronghold Lord | deferential | The subordinate calls Mu Song 채주 while reporting the nearby vessel. |
| 진태경 | 무송 | junior_martial_artist_to_senior_martial_artist | Senior | formal-polite | Taekyung uses 선배님 after recognizing Mu Song as a senior martial artist and disciple of the Seafaring King. |
| 무송 | 진태경 | senior_martial_artist_to_junior_martial_artist | Junior | familiar-teasing | Mu Song calls Taekyung 후배 and jokes about his supposed taste for men. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 주화란 | 사마표 | former_fiancés | Young Sect Leader | formal and guarded | Hwaran formally greets her former fiancé. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 진태경 | 매종학 | younger ally to newly installed Alliance Leader | Alliance Leader | formal and deferential | Uses 맹주님 while formally greeting Mae Jonghak as the Alliance Leader. |
| 사마표 | 진태경 | prospective recruit to pavilion master | you | polite, controlled, and candid | Sama Pyo uses 자네 while asking about Taekyung's attitude and admitting his intention to use him. |
| 진태경 | 사마표 | pavilion master to prospective recruit | you / that guy | blunt, informal, and distrustful | Taekyung speaks to and about Sama Pyo with casual forms such as 녀석 and 저놈. |
| 진태경 | 송일섬 | pavilion master to prospective member | Song Ilseom | direct and evaluative | Taekyung directly names Song Ilseom while comparing his qualifications with Hwaran's. |
| 혁무진 | 송일섬 | pavilion_member_to_escort_captain | Great Hero Song | formal and deferential | Mujin addresses Song Ilseom while commenting on his broad experience. |
| 송일섬 | 사마표 | fellow_pavilion_member_to_hostile_fellow_member | you | hostile and casual | Song Ilseom discusses fighting Sama Pyo and answers him while preparing to move away. |
| 사마표 | 송일섬 | fellow_pavilion_member_to_hostile_fellow_member | you | controlled and antagonistic | Sama Pyo responds to Song Ilseom's accusations and proposes moving aside to fight. |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 616
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 616
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and a member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jang Sam.md

# Jang Sam (장삼)

- **Safe through:** Chapter 546
- **Aliases:** Killing Ghost
- **Role:** Jang Sam was a Hubei fisherman who disappeared for a month and reappeared as a grotesque mutant monster known as a Killing Ghost.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** No relationships established.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 615
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license, and he has completed an unnamed cultivation technique designed for even the lowest-rank Hunter to learn without making it easily abusable.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 615
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 616
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, a member of the Fire Dragon Pavilion, and an experienced Nanman escort guide with route knowledge from the Escort King's records.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather and rescued the Guangdong Chen Family’s surviving child, who became Song Ilseom’s grandmother; Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort, and Jin Taekyung is a trusted ally.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 551
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader and has ordered Jin Taekyung's first Fire Dragon Pavilion mission to Nanman.
- **Personality:** Playful, easygoing, and teasing, but capable of handling heavy administrative responsibilities efficiently.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Mu Song.md

# Mu Song (무송)

- **Safe through:** Chapter 510
- **Aliases:** Ship-Fire Boy
- **Role:** Lord of Water Dragon Stronghold, a Peak master and the Seafaring King's second martial Disciple who controls major Yangtze river traffic in Sichuan, belongs to the Yangtze River Channel League's moderate faction, and is an exceptionally skilled ship captain.
- **Personality:** Ambitious, domineering, impatient with interruptions, strongly attached to life on the water, and capable of pragmatic cooperation when circumstances demand it.
- **Voice:** Deep and low in private, shifting to dry authority or boisterous command when addressing subordinates and rivals.
- **Relationships:** Mu Song belongs to the Yangtze River Channel League's moderate faction, regards Hwang Chung, his senior and Uncle Hwang, as family, must weigh whether the League will support the New Murim Alliance while the Seafaring King retains authority over major League decisions, and has been threatened by Mungyeong to keep Mungyeong's identity secret with five subordinates.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 615
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan and willing to redirect blame onto his subordinate.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 616
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 616
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 616
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

## Korean source

```text
＃617화



촤아아악!

물가를 향해 빠르게 접근하는 십여 척의 쾌조선은 맹인이 아닌 이상 누구나 볼 수 있었다.

하물며 경지에 접어든 무림인이라면 말할 것도 없다.

“수룡채(水龍寨)라…….”

경신법을 발휘하여 단숨에 달려온 사마표가 중얼거렸다.

눈을 가늘게 뜬 채 쾌조선의 깃발을 응시하던 그는 이번엔 나를 향해 시선을 옮겼다.

“잠시 기다리라더니, 이것 때문이었나?”

“맞아.”

“사천은 험지(險地)로 가득한 땅이니 장강을 타고 내려간다면 분명 지금보다 더욱 빠르게 이동할 수 있겠지. 하지만 상대가 장강수로맹이라는 것이 마음에 좀 걸리는군.”

사마표가 언뜻 비치는 불신에는 그만한 이유가 있었다.

장강수로맹은 기본적으로 약탈을 업으로 삼는 수적 집단이다.

게다가 맹주인 해상왕(海上王) 파륜은 일신의 무력과는 별개로 상당히 음흉한 인물이라는 평이 세간에선 지배적이었다.

‘무림맹 결성 당시에도 모종의 이유로 참석하지 않았고.’

병환 때문인지, 아니면 거리 때문인지 모른다.

그저 사자를 보내 입맹(入盟)하겠다는 뜻을 전하고 공식 발표한 것이 전부다. 물론 이는 녹림맹 역시 마찬가지였다.

이 두 세력은 정파보다는 사파 쪽에 가까웠고, 사파보다는 자신들만의 강력한 영역을 구축한 약탈자로 보는 것이 옳았다.

“파륜은 속내를 알 수 없는 자라고 들었다. 하남에서도 암암리에 그와 관련된 소문이 돌고 있어.”

“때가 되면 암천에 붙어먹을 인간이다, 뭐 그런 거?”

“들어 본 모양이군.”

“내 귀는 장식이냐? 그리고 기왕 말이 나왔으니 하는 말인데.”

나는 사마표를 바라보며 나직하게 말을 이었다.

“네가 말하는 세간의 평대로라면 장강수로맹이나, 흑룡마문이나 거기서 거기야.”

“……!”

“맞아. 틀려?”

잠깐 침묵하던 사마표가 떫은 표정으로 대꾸했다.

“생각해 보니 맞는 것 같다.”

“맞는 것 같은 게 아니라 맞지, 인마. 자세히 따지고 들어가면 오히려 흑룡마문이 더 안 좋을걸. 쟤들은 그나마 정파 사파 안 가리고 훔치지만, 너희는 빼도 박도 못하고 사파잖아.”

“……충분히 알아들었으니 그만해라. 듣고 있자니 정신이 혼미해지는군.”

사마표의 주위를 대형견처럼 어슬렁거리던 태산이 말을 받았다.

“주군. 태산이도 배고파서 정신이 혼미하다.”

“…….”

아, 보고 있자니 나까지 정신이 혼미해지려고 하네. 나는 지끈거리는 관자놀이를 문지르며 입을 열었다.

“그리고 하나 더. 저 수적들은 믿을 수 있으니까 괜한 걱정하지 마라.”

“믿을 만한 수적이라. 무공을 익히지 않은 무림인과 같은 말이군.”

“말하자면 긴데, 아무튼 나름대로 끈끈한 인연이 있어서 하는 말이야.”

나는 해상왕 파륜이 어떤 사람인지 모른다.

하지만 설령 그를 향한 세간의 평이 사실이라 해도, 선화아(船火兒) 무송에 대한 생각만큼은 달라지진 않을 거다.

적어도 내가 보고 겪은 무송은 신의가 있고 정도를 지키는 인물이었으니까.

꼭 제자가 스승을 닮으라는 법은 없지 않나.

‘사천에 도착해서 연통을 넣자마자 이렇게 달려온 것만으로도 알 수 있지.’

내가 그런 생각을 하는 사이, 어느덧 강가에 도착한 쾌조선에서 십여 명의 사내들이 쏟아져 내렸다.

촤아악!

장강에서 도가 튼 수적답게 거친 기세와 움직임에 강물이 사방으로 튄다.

헐렁한 장삼 사이로 구릿빛 근육을 드러낸 그들은 나는 듯한 걸음으로 달려와 포권을 취했다.

“진 대협!”

“연통을 받고 부리나케 온 길입니다.”

이들은 수룡채 내에서도 조장급 이상인 무송의 수족들이다.

지난번 사천에 왔을 때 하루에도 몇 번씩이나 보던 얼굴들이었지만, 정작 가장 익숙한 얼굴은 어디에서도 찾아볼 수 없었다.

“다들 아는 얼굴들이구만. 그런데 무송 선배가 안 보이네?”

내 물음에 부채주가 즉각 대답했다.

“그, 말씀드리기 죄송합니다만 이틀 전 총단(總團)으로 떠나셨습니다요.”

“총단이라면…… 장강수로맹의?”

“예, 맹주님의 명이라 조금도 지체하면 안 되는지라.”

“그래요?”

장강수로맹 내에서 해상왕의 명령은 절대적. 그의 직계 제자인 선화아 무송이 소집에 불응할 수는 없는 일이다.

나는 약간의 아쉬움과 고마움이 담긴 눈빛으로 수적들을 바라봤다.

“그래도 이 와중에 용케 바로 와 주셨네. 무송 선배도 자리에 안 계신데.”

화들짝 놀란 부채주가 손을 내저었다.

“어이구. 그런 말씀 마십시오. 채주께서도 선견지명이 있으신지, 진 대협에 관해 아주 신신당부를 하고 가셨습니다요.”

“나에 관해서?”

“예. 사람이 신세를 졌으면 꼭 갚아야 한다고. 작고하신 장강일도(長江一刀) 황 대협에 관한 일도 있고 하니, 혹시 태원진가나 진 대협께서 도움이 필요하시다면 손 닿는 데까지 힘쓰라고 하셨습죠.”

“오. 역시 무송 선배가 신의를 알아. 아주 협객이야, 협객.”

봤지, 인마.

내가 흐뭇하게 웃으며 사마표에게 눈짓하던 그때. 옆에 있던 덩치 큰 수적 하나가 어리둥절한 표정으로 부채주에게 속삭였다.

“저기, 부채주님.”

“응?”

“안 도와주면 지랄할 거 뻔하니까, 괜히 멀쩡한 쾌조선 부숴 먹지 말고 원하는 거 다해 주라는 말도 하시지 않았습니까요?”

“앗. 아아. 장필 네 이놈!”

“…….”

“…….”

순간 내려앉은 침묵.

수적들은 둘째치고 자랑스러운 우리 화룡각 대원들의 시선이 따갑기 그지없다.

삽시간에 고요해진 사방에서 주화란이 들릴 듯 말 듯 한 목소리로 작게 중얼거렸다.

“도대체 무슨 짓을 하고 다니셨길래 수적들까지…….”

폐부를 쑤시고 들어온 한 마디. 나는 가슴이 먹먹해지는 것을 느끼며 끝없이 펼쳐진 장강을 바라보았다.

뭐라 변명이라도 하고 싶은데, 이것저것 땡깡 부리고 콜택시처럼 이용한 건 사실이라 뭐라 할 말이 없다.

“어떻게 보면 사파보다 더 하군.”

기어코 종지부를 찍는 사마표의 독백을 애써 무시하며, 나는 슬픈 눈동자로 부채주를 바라보았다.

“출발이나 합시다.”

“예, 옙.”

“그리고 부채주는 이따가 나 좀 따라와요. 저 장필이라는 친구도 같이.”

“…….”

잠시 공포에 찬 눈빛으로 나를 바라보던 부채주가 먹먹한 음성으로 외쳤다.

“닻을. 닻을 올려라!”

목소리에 울음기가 섞여 있다고 느낀 건 분명 기분 탓이다.



* * *



쏴아아아!

뱃머리가 신속하고도 힘차게 강물을 가른다.

어느덧 봄에 접어든 바람은 순풍(順風)이었고, 다년간의 약탈로 숙련된 수적들의 노질은 범접할 수 없는 경지에 다다라 있었다.

물론 이들이 무송에 의해 교화된, 제법 착한 수적이라 해도, 특유의 본능은 여전했다.

“남동쪽에 선박 다섯 척 출현!”

“오, 부채주님. 상당한 규모의 상선(商船)입니다!”

“상선? 그럼 털어야지!”

이 와중에 털긴 뭘 털어. 이 미친놈들아.

나를 비롯한 모두가 어이없는 눈빛으로 그 상황을 지켜볼 때, 부채주가 와락 얼굴을 구겼다.

“이 얼빠진 놈들! 귀한 객들이 계시는데 이게 무슨 짓들이냐! 네놈들은 기본적인 예의도 없단 말이더냐!”

“죄, 죄송합니다.”

수적 주제에 하는 말만 들어 보면 판관 포청천이 따로 없다.

준엄하게 수하들을 꾸짖은 부채주가 우리에게 다가와 정중히 고개를 숙였다.

“못난 모습을 보여서 죄송합니다요.”

“껄걸. 뭐 이런 것 가지고.”

나는 사람 좋게 웃으며 말을 이었다.

“이해합니다. 뭐 본업이 그쪽이니까 충분히 그럴 수 있지.”

“이해해 주신다니 감사합니다. 대신 금방 털고 다시 출발하겠습니다.”

“응?”

“길어 봤자 반 시진이면 충분합니다요. 적당히 쓱싹하고 보내면…….”

“엎드려.”

약간의 해프닝이 있긴 했지만, 몇 번 부채주가 엎드려 뻗친 이후에는 그마저도 사라졌다.

그리고 이런 와중에도 쾌조선은 순풍을 받아 계속해서 나아가고 있었다.

하루, 이틀. 사흘…….

빠르게 흐르는 시간 속에서, 선상에 머무르게 된 화룡각 대원들은 각자의 할 일에 집중했다.

쉬쉭! 후우웅!

사마표와 송일섬은 첫날 이후 아무런 충돌 없이 자신만의 무공 수련에 몰두했고.

“태산이. 회 좋아한다. 그런데 물고기가 안 잡힌다. 한 마리만 줘라.”

“이 양반 이거 양심이 없네. 고생고생해서 기껏 몇 마리 잡아 놨더니 그걸 달래? 조장님, 이 인간이 자꾸 성가시게 구는데 좀 떼어 주시면 안 됩니까?”

“지금까지 잡은 물고기 다 내놔. 당연하겠지만 회까지 떠서.”

“태산이. 감탄했다. 각주는 천재인가?”

“…….”

혁무진과 태산은 대부분 뱃머리에서 낚시하며 시간을 보냈다.

물론 허탕을 치는 날이 허다했고, 혁무진은 그마저도 다른 사람에게 뺏기곤 했지만 별다른 불평은 하지 않았다.

그리고 나는 녀석이 그러는 이유가 체념했기 때문이 아니라는 걸 알고 있었다.

낚시하는 것조차 물고기를 잡기 위함이 아니었으니까.

‘그래서 아무 말도 하지 않는 거고.’

혁무진이 낚시를 하는 것은 그렇게라도 마음을 비우기 위해서였다.

녀석은 눈앞에서 찌가 흔들려도 굳이 낚싯대를 잡아채지 않았고, 밤마다 선실에 틀어박혀 무공을 수련하거나 운기조식에 몰두했다.

그렇게 하루하루, 시시각각 운남(雲南)에 가까워질수록 사람들은 각자의 방식으로 혹시 모를 전투에 대비하고 있었고, 그건 나 역시 마찬가지였다.

‘퀘스트 창 오픈.’

띠링.



퀘스트



[남만행(南蠻行)]



무림 맹주 매종학이 화룡각에 첫 번째 임무를 부여했습니다.

이제 당신은 남만으로 향하여 혹시 모를 상황에 능동적으로 대처해야 합니다.

당신과 화룡각의 앞길에 무엇이 있을지는 알 수 없는 상황.

늘 주위를 경계하고, 유연한 사고방식으로 행동하십시오.



등급 : 절정

제한 : 진태경 및 화룡각 인원

임무 : 남만 진입 (미완료)

보상 : 연계 퀘스트

 ???

실패 : 칭호, [남만을 못 가] 획득

 명성 및 신뢰도 대폭 하락





무림에서의 시간으로는 약 보름 전. 현대까지 합친다면 한 달도 전에 받았던 퀘스트다.

내가 놓친 부분이 있나 퀘스트 창을 찬찬히 다시 살펴보던 그때, 불어오는 바람 사이로 희미한 꽃향기가 섞여들었다.

“왜 그렇게 유심히 허공을 보고 계세요?”

주화란이다.

홀로그램 창을 닫은 나는, 진중한 표정으로 별이 총총히 박힌 밤하늘을 응시했다.

“천기(天氣)를 읽고 있었습니다.”

“아하. 정말요?”

“네, 정말로.”

“대단하시네요.”

피식 웃은 주화란이 물었다.

“그래서, 하늘이 뭐라 알려 주던가요?”

“오늘 날씨 좋다는데요.”

“그래요?”

“네. 주 소저, 저기 북두칠성 보이시죠?”

내 손가락을 따라 하늘을 올려다본 주화란이 눈을 깜빡였다.

“어. 음.”

“왜요?”

“각주님. 죄송하지만 저건 북두칠성이 아니에요.”

“……그럴 리가 없는데, 그사이에 모양이 바뀌었나?”

“네?”

이게 말이야, 방구야.

뱉어 놓고도 아차 싶었다. 순간 당황해서 턱만 긁적이는 내 모습에 주화란이 소리 내어 웃었다.

“재미있는 방법으로 천기를 읽으시네요.”

“솔직히 말하자면, 사실 천기 같은 거 잘 모릅니다. 그냥 닥치는 대로 상황 봐 가면서 하는 거지.”

“알아요. 그래도 더 듣고는 싶어지네요. 때마침 개인적으로 한 가지 궁금한 게 있는데, 여쭤봐도 되나요?”

입맛을 다신 내가 대답했다.

“이미 말씀드렸지만, 저는 천기 같은 거 볼 줄 모르는데요.”

“저도 이미 말씀드렸지만, 알아요. 그리고 이건 하늘이 아니라 각주님께 여쭤보고 싶은 거예요.”

“그렇다면 상관없습니다. 제가 대답할 수 있는 부분이라면 뭐든.”

타닥.

사뿐하게 뱃머리로 뛰어오른 주화란이 시커먼 강물을 바라보며 입을 열었다.

“앞으로 어떻게 될까요? 우리.”

남만이 코앞까지 다가오니 주화란도 불안한 것이 틀림없었다.

어떻게 하면 그녀를 안심시켜 줄 수 있을까. 잠시 생각하던 나는 입을 열었다.

“모르겠습니다. 암천이 일을 꾸미고 있을 가능성이 농후하지만, 다행히 아무 일도 없을 수도 있죠.”

남만은 새외(塞外)로 분류될 만큼 외진 곳.

게다가 남만의 패자라 할 수 있는 남만야수궁과 묘족을 비롯한 여러 이민족이 거주하고 있는 광활한 땅이기도 했다.

만약 내가 느낀 불길한 짐작이 모두 사실이었고 암천이 남만에서 뭔가를 꾸미고 있다면, 숱한 위험이 나와 화룡각을 기다리고 있을 터였다.

하지만…….

“아무 일 없을 겁니다. 어떤 일이 생기더라도 무사히 집으로 돌아갈 수 있을 거예요. 이것 하나만큼은 약속드립니다.”

주화란은 대답하지 않았다. 그 대신 알 수 없는 눈빛으로 나를 잠시, 아니 아주 오랫동안 바라보았다.

“주 소저?”

“……음. 그렇군요.”

침묵 끝에 흘러나온 짧은 음성.

희미한 웃음을 입가에 머금은 주화란이 작게 고개를 흔들었다.

인피면구로도 감추지 못한 윤기 나는 머리카락이 강물처럼 출렁인다.

“믿을게요, 각주님을.”

“……?”

석연치 않은 기분이다. 혹시 내 대답이 잘못되었나, 잠시 스스로 생각에 잠겨 있던 그때.

횃불을 든 부채주가 나타나 상기된 얼굴로 입을 열었다.

“진 대협. 도착했습니다.”

“……!”
```

## Final English reading copy

```markdown
# Chapter 617

*Splash!*

A dozen or so swift ships rapidly approaching the riverside were visible to anyone who wasn’t blind.

For a martial artist who had reached a realm stage, it went without saying.

“Water Dragon Stronghold…”

Sama Pyo had used his movement technique to rush over in an instant. He muttered while narrowing his eyes at the flags on the swift ships, then shifted his gaze toward me.

“You told me to wait a moment. Was this why?”

“Yep.”

“Sichuan is a land filled with treacherous terrain, so if we travel down the Yangtze, we can certainly move faster than we are now. Still, I’m somewhat concerned that our counterparts are the Yangtze River Channel League.”

There was a good reason for the distrust faintly visible in Sama Pyo’s expression.

The Yangtze River Channel League was, at its core, a group of water bandits whose livelihood was plunder.

Moreover, the prevailing opinion was that the Seafaring King, Pa Ryun, was a deeply sinister man, quite apart from his personal martial prowess.

*He didn’t attend the formation of the Murim Alliance, either, for some reason.*

I didn’t know whether it was because of illness or the distance.

All he had done was send an envoy to convey his intention to join the Alliance and make an official announcement. Of course, the same was true of the Green Forest Alliance.

These two forces were closer to the unorthodox faction than the orthodox faction. More accurately, they were plunderers who had established powerful domains of their own.

“I hear Pa Ryun is a man whose true intentions are impossible to read. Rumors about him have even been circulating quietly in Henan.”

“You mean the kind of man who’ll sell out to Dark Heaven when the time comes?”

“Sounds like you’ve heard them.”

“Are my ears just decoration? And since we’re on the subject…”

I looked at Sama Pyo and continued in a low voice.

“If the public opinion you mentioned is accurate, then the Yangtze River Channel League and the Black Dragon Demon Gate are two of a kind.”

“……”

“Am I wrong?”

After a brief silence, Sama Pyo replied with a bitter expression.

“Now that I think about it, it seems you’re right.”

“Not ‘it seems.’ I’m right, you bastard. If you look closely, the Black Dragon Demon Gate is actually worse. At least those guys rob people without discriminating between the orthodox and unorthodox factions. You people are unambiguously unorthodox.”

“……I understand perfectly well. Stop now. Listening to you is making me dizzy.”

Taishan, who had been circling Sama Pyo like a large dog, joined the conversation.

“Lord. Taishan hungry too. Head dizzy.”

“……”

*Watching this is making my head dizzy, too.*

I rubbed my throbbing temple and opened my mouth.

“And one more thing. You don’t need to worry. Those water bandits can be trusted.”

“Trustworthy water bandits. That sounds like a martial artist who hasn’t learned martial arts.”

“It’s a long story. Anyway, we have a pretty strong bond.”

I didn’t know what kind of person the Seafaring King Pa Ryun was.

But even if the public opinion about him was true, my opinion of Ship-Fire Boy Mu Song wouldn’t change.

At least the Mu Song I had seen and known was trustworthy and held to his principles.

It wasn’t as though a Disciple was required to resemble his master.

*I can tell from the fact that they came rushing over the moment we sent word after reaching Sichuan.*

While I was thinking that, the swift ships reached the riverbank, and a dozen or so men poured off them.

*Splash!*

The river water sprayed in every direction at their rough momentum and movements, befitting water bandits who had made their bones on the Yangtze.

Their bronze-colored muscles showed through their loose robes as they ran toward us with flying steps and clasped their hands in salute.

“Great Hero Jin!”

“We came running as soon as we received your message.”

These were Mu Song’s trusted hands within the Water Dragon Stronghold, all at least squad-captain level.

I had seen their faces several times a day the last time I came to Sichuan, but the face I was most familiar with was nowhere to be found.

“All familiar faces. But I don’t see Senior Mu Song.”

The Deputy Stronghold Lord immediately answered my question.

“I’m sorry to say this, but he left for the League’s headquarters two days ago.”

“The headquarters… You mean the headquarters of the Yangtze River Channel League?”

“Yes, sir. It was on the League Leader’s orders, so he couldn’t delay even a moment.”

“I see.”

Within the Yangtze River Channel League, the Seafaring King’s orders were absolute. His direct Disciple, Ship-Fire Boy Mu Song, had no choice but to answer a summons.

I looked at the water bandits with a mixture of regret and gratitude.

“Even so, you managed to come right away. And Senior Mu Song isn’t even here.”

The Deputy Stronghold Lord was startled and waved his hands.

“Oh, please don’t say that. The Stronghold Lord must have had the foresight to anticipate this. Before he left, he gave us very specific instructions regarding Great Hero Jin.”

“Regarding me?”

“Yes. He said that if a person had received help, they absolutely had to repay it. There’s also the matter concerning the late Yangtze One Saber, Great Hero Hwang. So if the Jin Family of Taiyuan or Great Hero Jin ever needed help, he told us to do everything within our power.”

“Oh. Senior Mu Song truly understands honor. He’s a real hero.”

*See that, you bastard?*

I smiled with satisfaction and glanced at Sama Pyo.

Just then, one of the larger water bandits standing nearby whispered to the Deputy Stronghold Lord with a bewildered expression.

“Deputy Stronghold Lord.”

“Yes?”

“Didn’t the Stronghold Lord also say that since Great Hero Jin was obviously going to raise hell if we didn’t help, we should just give him whatever he wanted instead of letting him wreck perfectly good swift ships?”

“Ah. Right. Jang Pil, you little—!”

“……”

“……”

Silence descended in an instant.

Never mind the water bandits. The gazes of the proud members of our Fire Dragon Pavilion were painfully sharp.

As the entire area fell silent, Ju Hwaran muttered in a voice so quiet it was almost inaudible.

“What on earth have you been doing to make even water bandits…”

Her words had struck deep. I felt my chest grow heavy as I looked out over the endless Yangtze.

I wanted to offer some kind of excuse, but it was true that I had thrown tantrums here and there and used them like a taxi. I had nothing to say.

“In some ways, you’re worse than the unorthodox faction.”

I did my best to ignore Sama Pyo’s final remark and looked at the Deputy Stronghold Lord with mournful eyes.

“Let’s just set off.”

“Yes, sir.”

“And Deputy Stronghold Lord, come with me later. Bring that Jang Pil fellow, too.”

“……”

The Deputy Stronghold Lord stared at me in terror for a moment before shouting in a choked voice,

“Raise the anchor! Raise the anchor!”

I must have imagined the tearful note in his voice.

* * *

*Whoosh!*

The bow of the ship swiftly and powerfully cut through the river water.

Spring had arrived, and the wind was blowing in our favor. The water bandits’ rowing, honed through years of plunder, had reached a level no one else could match.

Of course, even though these were fairly decent water bandits who had been reformed by Mu Song, their innate instincts remained.

“Five ships spotted to the southeast!”

“Oh, Deputy Stronghold Lord. They’re sizable merchant ships!”

“Merchant ships? Then let’s rob them!”

*What the hell are you robbing them for in the middle of this, you lunatics?*

As everyone, myself included, watched the situation with dumbfounded expressions, the Deputy Stronghold Lord’s face twisted.

“You idiots! We have honored guests aboard! What do you think you’re doing? Do you people have no basic manners?”

“S-sorry.”

For a water bandit, he sounded exactly like Judge Bao.[^1]

After sternly rebuking his subordinates, the Deputy Stronghold Lord approached us and bowed politely.

“We’re sorry for showing you such an unbecoming side of ourselves.”

“Heh heh. It’s nothing.”

I smiled amiably and continued.

“I understand. This is your line of work, after all. I can see how it happened.”

“Thank you for understanding. In that case, we’ll rob them quickly and set off again.”

“Huh?”

“It’ll take half a shichen at most. We’ll do a quick job and send them on their way…”

“Get down.”

There had been a slight incident, but after I made the Deputy Stronghold Lord drop and hold the push-up position a few times, even that impulse disappeared.

The swift ship continued onward with the wind at its back.

One day, two days. Three days…

As time passed quickly, the Fire Dragon Pavilion members, who were now confined to the ship, focused on their respective tasks.

*Swish! Whoosh!*

Sama Pyo and Song Ilseom devoted themselves to their own martial arts training after the first day without a single clash between them.

“Taishan likes sashimi. But no fish caught. Give Taishan one.”

“This guy has no shame. I went through all that trouble to catch a few fish, and now he wants them? Captain, this fellow keeps pestering me. Can you get him away from me?”

“Hand over all the fish you’ve caught so far. Obviously, slice them into sashimi, too.”

“Taishan impressed. Is Pavilion Master a genius?”

“……”

Hyuk Mujin and Taishan spent most of their time fishing at the bow.

Of course, there were plenty of days when they caught nothing, and even when Hyuk Mujin did catch something, someone else would often take it away from him. Still, he didn’t complain much.

And I knew the reason wasn’t that he had given up.

Fishing itself wasn’t even about catching fish.

*That’s why he doesn’t say anything.*

Hyuk Mujin was fishing so he could empty his mind, even if only in that way.

Even when the bobber trembled right in front of him, he didn’t bother yanking on the fishing rod. Every night, he locked himself in the cabin to practice martial arts or devote himself to circulating his qi.

As each day passed and we drew closer to Yunnan, everyone prepared for a possible battle in their own way.

I was no different.

*Open the Quest window.*

*Ding.*

> **System**
>
> **Quest**
>
> **Journey to Nanman**
>
> Murim Alliance Leader Mae Jonghak has assigned the Fire Dragon Pavilion its first mission.
>
> You must now head to Nanman and actively respond to any situation that may arise.
>
> There is no way to know what lies ahead for you and the Fire Dragon Pavilion.
>
> Always remain vigilant and act with a flexible mindset.
>
> **Grade:** Peak
>
> **Restriction:** Jin Taekyung and Fire Dragon Pavilion members
>
> **Mission:** Enter Nanman (Incomplete)
>
> **Reward:** Chain Quest
>
> ???
>
> **Failure:** Obtain Title: Can’t Go to Nanman
>
> Fame and trust greatly reduced

In terms of time spent in Murim, I had received this Quest about half a month ago.

Counting the time in the modern world, it had been more than a month.

I was carefully examining the Quest window again to see if I had missed anything when a faint floral scent mingled with the breeze.

“Why are you staring so intently at empty space?”

It was Ju Hwaran.

I closed the holographic window and gazed seriously at the night sky, thick with stars.

“I was reading the heavenly patterns.”

“Oh. Really?”

“Yes. Really.”

“That’s impressive.”

Ju Hwaran let out a quiet laugh and asked,

“So what did the heavens tell you?”

“They said the weather would be nice today.”

“Really?”

“Yes. Young Lady Ju, you see the Big Dipper over there?”

Ju Hwaran looked up at the sky along my pointing finger and blinked.

“Oh. Um.”

“What is it?”

“Pavilion Master, I’m sorry, but that isn’t the Big Dipper.”

“……That can’t be right. Did its shape change in the meantime?”

“What?”

*What kind of nonsense was that?*

The words were already out before I realized how ridiculous they sounded. When I scratched my chin in embarrassment, Ju Hwaran burst out laughing.

“You read the heavenly patterns in an interesting way.”

“To be honest, I don’t know much about heavenly patterns. I just deal with things as they come and act according to the situation.”

“I know. Still, it makes me want to hear more. As it happens, there’s something I’ve been curious about personally. May I ask you about it?”

I smacked my lips before answering.

“I already told you, but I don’t know how to read the heavenly patterns.”

“I already told you that I know. And this isn’t something I want to ask the heavens about. I want to ask you.”

“If that’s the case, then there’s no problem. I’ll answer anything I can.”

*Tap.*

Ju Hwaran lightly jumped onto the bow and looked out at the pitch-black river before opening her mouth.

“What do you think will happen from here on? To us?”

With Nanman so close, Ju Hwaran was undoubtedly anxious.

*How can I reassure her?*

After thinking for a moment, I opened my mouth.

“I don’t know. There’s a strong possibility that Dark Heaven is plotting something, but it’s also possible that nothing will happen.”

Nanman was a remote region, so far away that it was classified as the Outer Lands.

It was also a vast territory home to the Nanman Beast Palace, the dominant power in Nanman, as well as numerous ethnic groups, including the Miao people.

If my ominous suspicion was entirely correct and Dark Heaven was plotting something in Nanman, countless dangers would be waiting for me and the Fire Dragon Pavilion.

But…

“Nothing will happen. Whatever happens, we’ll be able to return home safely. I promise you that much.”

Ju Hwaran didn’t answer.

Instead, she looked at me with an unreadable expression for a moment—or rather, for a very long time.

“Young Lady Ju?”

“……I see.”

A short voice finally emerged from the silence.

With a faint smile on her lips, Ju Hwaran gently shook her head.

Her glossy hair, which even the human-skin mask couldn’t conceal, rippled like the river.

“I’ll trust you, Pavilion Master.”

“……?”

Something felt off.

I was wondering whether I had given the wrong answer when the Deputy Stronghold Lord appeared with a torch, his face flushed with excitement.

“Great Hero Jin. We’ve arrived.”

“……!”

[^1]: Judge Bao, or Bao Qingtian, is a legendary incorruptible magistrate celebrated in Chinese folklore and popular fiction.
```
