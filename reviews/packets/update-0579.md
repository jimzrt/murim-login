<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0579.txt",
      "sha256": "edaf49357a237811ce6f3ef5041e9c5051ac3280ef455e824b4a920d96ff45f8",
      "bytes": 13247
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "a00f160f44b242154ebc55a00e4005a5796704cf744e577f77ca81dcbc481999",
      "bytes": 2356
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "979337dec45c6d24df237cb0ad58355d3ce4d797870bdd238aec038545cf3071",
      "bytes": 182422
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "5d6e42c855db8fd129fe6aec16696a219997ad3b0c7900e692fab169dbf06d21",
      "bytes": 730
    },
    {
      "path": "characters/Cheonwoo.md",
      "sha256": "e634fb24f01dd4ff7f54dab47b4ad53970891fdddce96ab8fb4b952645311110",
      "bytes": 590
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "f3da79b1b55b8e95cff343f37682839249833a19b108f557059df43c5b79ccf1",
      "bytes": 553
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "ffe1cef41928c0c80d8dbc87cb22ca931290c00cf3c4047fccbce6cb6dd2f129",
      "bytes": 976
    },
    {
      "path": "characters/Hwa-jong.md",
      "sha256": "461502eaf0c4e29482dbbb45d9bbadd19c94eefdbfab571c5c201f2099745ab6",
      "bytes": 562
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "2ed7c75fe2c91b8145f08a700b847b188bd4167123eb8baa0b4efd102149ba31",
      "bytes": 2280
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "08906ce878047a7ce02abea1d4820ea1b99a826760aba0e816863c2cf6bd6c04",
      "bytes": 622
    },
    {
      "path": "characters/Kim Hwajong.md",
      "sha256": "51b2ce74d43c9c03ca9151b26b446dfeaaabec0719f631f24611c0511cf02d34",
      "bytes": 482
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "d10308b5bd25c2bf694f36daee7f16a175fbfe1e48779eddf2c965f0c53eb2c0",
      "bytes": 1384
    },
    {
      "path": "characters/Song Cheonwoo.md",
      "sha256": "1dddfc0b75bd540914f8ad12ed7c50ee8a5bacbdffa7068eee8983872780ce5a",
      "bytes": 1076
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "0d9e52a8fbb10d41d8dfe5f9e0cd490a3b6ed8d0639b0f8e65c707d37ceea01d",
      "bytes": 956
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4a5eddc3bae4d911d482b6b8d8dab4f2ad1d27d864cb7faeeb0aea4afb791a80",
      "bytes": 179227
    }
  ],
  "estimated_tokens": 12026
}
-->

# Durable State Update — Chapter 579

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 579. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 579. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 579,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 579,
    "continuity_sources": [579],
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
    "Song Cheonwoo says Cheon Taemin suddenly collapsed more than twenty years ago and has remained unconscious, but no one knows why.",
    "Song Cheonwoo and Lee Jungryong concealed Taemin's condition, waited two years, conducted experiments, and purged aides who knew the truth.",
    "Song survived by negotiating the European regional director position and saving his family.",
    "Hwa-jong was not told about Taemin's condition and remains loyal to Choi Minwoo.",
    "Song claims Taemin is still alive, but his location is unknown and Area A is only suspected.",
    "Choi Minwoo will verify the facts before seeking payment for Song's crimes.",
    "Song describes his disclosure as atonement for wrongs against Taemin and Choi.",
    "Busan's Kraken has been eliminated, but more than one thousand Mermen remain across Haeundae and Gwangalli while the Peace Guild and other forces contain the disaster.",
    "Song Cheonwoo warned Choi Minwoo that Go Jun is preparing a trap related to Choi's maternal grandfather.",
    "Go Jun is holding Song Cheonwoo's children as leverage, forcing Song to attack Choi despite their temporary alignment against Go Jun.",
    "Song Cheonwoo used the Yeti's Necklace to bring hundreds of yetis into the confrontation; Kim Hwajong diverted them while Choi fought Song.",
    "Choi Minwoo's Hero's Soul and awakened resolve allow him to fight Song Cheonwoo, but the outcome of Choi's final strike is unresolved."
  ],
  "continuity_sources": [
    578
  ],
  "open_questions": [
    "What caused Cheon Taemin's collapse, and what happened during his more than twenty years of unconsciousness?",
    "Is Cheon Taemin actually being kept in Area A of Ares Guild headquarters?",
    "What trap is Go Jun preparing, and can Song Cheonwoo's warning be trusted?",
    "Who empowered and released the Kraken, and did that person engineer the Monster Wave?",
    "Did Choi Minwoo's final strike kill or incapacitate Song Cheonwoo?"
  ],
  "safe_through": 578,
  "temporary_decisions": [
    "Use Yeti's Winter Range for 예티의 겨울 산맥.",
    "Use Stone King for 스톤 킹 and Skeleton King for 스켈레톤 킹.",
    "Use Area A for A구역.",
    "Use Hwa-jong for 화종.",
    "Use Hero's Soul for 영웅의 혼 and Yeti's Necklace for 예티의 목걸이."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 김화종    | **Kim Hwajong**   |
| 최민우    | **Choi Minwoo**   |
| 천태민    | **Cheon Taemin**  |
| 이정룡    | **Lee Jungryong** |
| 상태               | **Status**                     |
| 길드      | **Guild**             |
| 대격변     | **Great Cataclysm**   |
| 천우 | **Cheonwoo** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 화종 | **Hwa-jong** | Butler Kim's personal name. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 송천우 | **Song Cheonwoo** | Ares Guild Director, former third-ranked Korean Hunter, and longtime European regional branch director. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 도련님 | **Young Master** | Address used for Team Leader Choi by Butler Kim. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 예티 | **yeti** | Monster species in the Gate's name and raid dialogue. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 김화종 | 진태경 | senior_Hunter_to_younger_Hunter | Mr. Jin | formal-polite | Hwajong addresses Taekyung as 진태경 씨 while proposing an exchange of stories. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 이정룡 | 고준 | Master to Disciple | Go Jun | familiar and testing | Lee switches from Seok's office title to his personal name while considering whether he can defeat Taekyung. |
| 고준 | 이정룡 | Disciple to Master | Master | deferential | Go Jun responds to Lee's personal-name address as 스승님. |
| 이정룡 | 천태민 | younger_to_older_brother_by_choice | older brother | reverent and familiar; internal | Lee Jungryong uses 형님 in unspoken thoughts and regards Cheon Taemin as an older brother despite having no blood relation. |
| 석고준 | 최민우 | Ares security leader to rival Guild Master | Team Leader Choi Minwoo | formal but barbed | Uses 평화 길드 최민우 팀장님 while belittling Choi and blaming the Peace Guild for Taekyung's apparent death. |
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 최민우 | 진태경 | trusted allied team leader to younger allied Hunter | Mr. Jin | formal-polite and concerned | Choi warns Jin about the danger of the operation and affirms his deep trust. |
| 진태경 | 최민우 | younger allied Hunter to allied team leader | Team Leader Choi | polite, familiar, and teasing | Jin jokes with Choi while acknowledging and dismissing his concern. |
| 고준 | 진태경 | Ares Guild combatant confronting the killer of his Master | you | hostile and informal | Go Jun uses 너 while demanding Jin confess to Lee Jungryong's death and threatening retaliation. |
| 진태경 | 고준 | dominant adversary confronting Lee Jungryong's Disciple | you | contemptuous and informal | Jin uses 너 and 놈 while overpowering Go Jun and ordering him to end the conflict with Lee Jungryong. |
| 송천우 | 석고준 | adversary; captor of Song's children | you | shocked and confrontational | Song reacts directly to Go Jun's admission that he took the children. |
| 화종 | 최민우 | butler_to_Young_Master | Young Master | formal and deferential | Butler Kim consistently addresses Choi Minwoo with the established deferential title. |
| 송천우 | 화종 | former_allies | Hwa-jong | familiar and informal | Song uses Hwa-jong's personal name, prompting Hwa-jong to reject the familiarity. |
| 화종 | 송천우 | former_allies_now_hostile | you | formal and cold | Hwa-jong challenges Song's right to expect Choi's trust and rejects their former intimacy. |
| 송천우 | 최민우 | older_former_ally_to_younger_former_ally | Minwoo | familiar and informal | Song addresses Choi by his given name while discussing the meeting place and surveillance. |
| 최민우 | 화종 | Young Master to butler | Butler Kim | formal and respectful | Choi refers to Hwa-jong as 김 집사님 while discussing the concealed truth. |
| 최민우 | 송천우 | temporary ally to rival | Regional Director | formal and cutting | Choi uses 지사장님 while condemning Song's survival and concealment. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 578
- **Aliases:** Slayer
- **Role:** Cheon Taemin is Ares Guild Master and the world's greatest Hunter, known as the Slayer for killing the Demon King and creating the first Mana Cultivation Method during the Great Cataclysm, and he is believed to remain alive after more than twenty years of unconsciousness, with Area A only suspected as his location.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Cheonwoo.md

# Cheonwoo (천우)

- **Safe through:** Chapter 578
- **Aliases:** None
- **Role:** One of the five current Five Gates of Shanxi scions and a First Rate martial artist present at Honghwa Inn.
- **Personality:** Pampered and contemptuous toward Cheongpung's group as part of the five scions' collective mockery.
- **Voice:** Mocking in the group's exchange; no distinct individual speech is established.
- **Relationships:** Associates with Seongryong, Myeonghwa, Sohye, and Jintae as a group of current Five Gates scions.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 578
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 578
- **Aliases:** Team Leader Seok
- **Role:** Go Jun is Ares Guild's Vice Guild Master, Lee Jungryong's disciple and former Head of Security, and the de facto successor to Lee's Ares legacy who passed the S-rank Hunter qualification assessment with a very high score but lacks Lee's legitimacy.
- **Personality:** Disciplined and controlled under ordinary pressure, fiercely loyal to Lee Jungryong, but consumed by humiliation and rage when Ares Guild's authority is challenged.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Disciple and direct protégé of Lee Jungryong, Go Jun inherited Lee's Ares Guild legacy after his death, regards Jin Taekyung and Choi Minwoo as enemies seeking to take it away, and has seized Song Cheonwoo's children as leverage while calling it protection.

### Hwa-jong.md

# Hwa-jong (화종)

- **Safe through:** Chapter 578
- **Aliases:** Butler Kim
- **Role:** Hwa-jong is Choi Minwoo's loyal butler and personal escort.
- **Personality:** Loyal, vigilant, and uncompromising toward perceived threats to Choi Minwoo.
- **Voice:** Formal and deferential toward Choi Minwoo, cold and openly hostile toward Song Cheonwoo.
- **Relationships:** Hwa-jong serves Choi Minwoo and was formerly close to Song Cheonwoo, but their relationship ended over loyalty and ambition.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 578
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, can command coordinated raids against powerful monsters, serves as one of the two pavilion masters of the Alliance Leader's direct Fire Dragon Pavilion, leads its first mission to Nanman, and is the Peace Guild's wealthy patron in the modern world.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 578
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Kim Hwajong.md

# Kim Hwajong (김화종)

- **Safe through:** Chapter 578
- **Aliases:** Butler Kim
- **Role:** Kim Hwajong is a Level 80 mage known as Butler Kim and Choi Minwoo's loyal butler and personal escort.
- **Personality:** Gentle and composed
- **Voice:** Gentle and measured
- **Relationships:** Former instructor of Im Chunsoo, who remains terrified of and obedient to him; addresses Im Chunsoo familiarly as Chunsoo

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 578
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regarded Cheon Taemin as an older brother despite no blood relation and long held him in respect and fear; secretly supported the orphanage where Lee Dongseok grew up and was regarded by Dongseok as a father; operated as Ares Guild's senior authority beneath its Guild Master; concealed Taemin's condition with Song Cheonwoo and participated in purging aides who knew the truth.

### Song Cheonwoo.md

# Song Cheonwoo (송천우)

- **Safe through:** Chapter 578
- **Aliases:** Director Song
- **Role:** Ares Guild Director and former A-rank Hunter who reached third place among Korean rankers, briefly headed the Hunter training center, and led Ares Guild's European regional branch for twenty years; he now leads an internal faction capable of threatening Go Jun.
- **Personality:** Highly ambitious, honor-obsessed, politically calculating, and determined to use his final opportunity to reclaim influence before retirement.
- **Voice:** Not established.
- **Relationships:** Song Cheonwoo followed Cheon Taemin since before Team Leader Choi was born, was Lee Jungryong's former friend and rival, helped conceal Taemin's condition and purge aides who knew the truth, negotiated the European regional director position to save himself and his family, is aligned with Choi against Go Jun, has had his children seized by Go Jun as leverage, and has told Choi that Taemin is probably alive but may be in Area A.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 578
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Cheon Taemin's only living blood relative, a formidable aura-wielding swordsman who wields Hero's Soul, and is positioning himself to take control of the Ares Guild after Lee Jungryong's death.
- **Personality:** Strategic, candid, controlled, and possessive of the power and influence he intends to inherit.
- **Voice:** Dry, formal, and direct, with calm candor and carefully chosen metaphors.
- **Relationships:** Choi Minwoo is Cheon Taemin's maternal grandson and only living blood relative, was kept out of public knowledge by Lee Jungryong, is closely integrated with Jin Taekyung's family, seeks to acquire the Ares Guild intact, and now knows that Song Cheonwoo and Lee concealed Taemin's collapse and purged aides while he investigates Taemin's fate.

## Korean source

```text
＃579화



서걱!

한 줄기 섬광이 가슴을 가로지른 순간, 송천우는 눈앞이 아득해지는 것을 느꼈다.

‘뜨겁다.’

그건 벼락이었다.

혼란하고 위태롭던 대격변의 한 줄을 장식했던 옛 영웅조차 막을 수 없었던 벼락.

송천우는 떨리는 눈빛으로 손에 들린 검을 바라보았다.

불과 몇 초 전만 하더라도 형형한 오라를 뿜어내던 그의 검은, 더욱 파괴적이고 예리한 무언가에 의해 반으로 잘려져 있었다.

철컹.

손아귀에서 미끄러진 검이 땅바닥을 나뒹군다. 한 박자 늦게 찾아온 고통이 송천우의 전신을 엄습했다.

“쿨럭.”

투두둑. 입가에서 쏟아진 검붉은 핏물이 눈 위를 적셨다. 옷과 갑옷이 비스듬히 갈라지고, 구릿빛의 상반신이 드러났다.

그리고 탄탄한 근육과 피부 위를 가로지른 미세한 선이 붉게 달아오른 순간.

촤아아악!

엄청난 양의 핏물이 폭포수처럼 터져 나왔다.

왼쪽 가슴으로부터 오른쪽 골반에 이르기까지. 벼락이 훑고 지나간 상흔(傷痕)은 극심했고 두 번 다시 아물지 않을 것이다.

송천우는 힘이 풀리는 것을 느끼며 뒷걸음질 쳤다.

사박.

힘없는 발걸음이 피에 젖은 눈을 밟았다.

한 걸음. 두 걸음. 세 걸음. 그리고…….

푸스슥.

쌓여 있던 눈이 떨어지는 소리에, 송천우는 간신히 신형을 바로잡았다.

어느덧 그의 등 뒤에는 크레바스라 불리는 거대한 균열이 아가리를 쩍 벌린 채 기다리고 있었다.

더 이상 물러설 곳도, 나아갈 곳도 없다.

‘빌어먹을 일이로군.’

송천우는 가슴이 공허해지는 것을 느꼈다.

어쩌면 그것은 지금 이 순간조차도 자신의 몸에서 빠져나가는 생기(生氣) 때문일지도 모른다.

문득 고개를 든 그의 시야에, 천천히 걸어오는 한 사람의 모습이 들어왔다.

‘최민우.’

언제나 존경과 두려움의 대상이었던 ‘그분’의 유일한 핏줄. 송천우는 벼락을 마주하기 직전 들었던 나직한 목소리를 떠올렸다.



‘내 몸 안에 흐르는 피가, 누구의 것인지 잊었습니까.’



지금 이 순간, 노인의 눈동자에 비친 것은 이 자리에 없는 또 다른 누군가였다.

이제는 과거의 기억으로만 남게 된 한 사람.

그저 옆에서 지켜보는 것만으로도 존경과 두려움을 느낄 수밖에 없던 존재.

송천우는 오랫동안 잊고 있던 사실을 깨달았다. 저 청년의 몸속에는, 천태민의 피가 흐르고 있다는 것을.

“……형님?”

송천우는 숨을 헐떡이며 중얼거렸다.

온통 붉게 물든 시야 속, 찬란한 빛을 내뿜고 있는 검을 든 청년의 모습은 그의 외조부와 닮아 있었다.

깊게 가라앉은 눈빛이 왜 변심했느냐 묻는 듯했다.

“오지 마. 오지 마라!”

송천우는 간신히 쥐어짠 외침과 함께 검을 휘둘렀다. 아니, 휘둘렀다고 생각했다.

그러나 앞서 검을 떨어트린 그의 손은 텅 비어 있었고, 허공만을 휘젓던 손은 마침내 다가온 누군가의 단단한 손아귀에 가로막혔다.

후우웅, 턱.

송천우의 손목을 움켜쥔 최민우는 손아귀에 힘을 가했다. 으득, 뼈가 어긋나는 소리와 함께 비명이 터져 나왔다.

“크아아아악!”

털썩. 고통을 견디지 못하고 무릎을 꿇은 송천우를, 최민우는 가라앉은 눈빛으로 응시했다.

지금 그의 눈에 비친 것은 송천우가 아니라 나이 든 노인이었다.

츠츠츠츠.

[영웅의 혼]에 서린 광휘가 서서히 사그라들었다. 이 싸움의 승부는 이미 결정되었다.

쓰러진 패자를 향해, 우뚝 선 승자는 나직한 목소리로 이 치열한 싸움의 결과를 알려 주었다.

“그만하십시오, 끝났습니다.”

“……!”

고통으로 몸부림치던 송천우의 신형이 우뚝 굳었다.

자신이 패배하다니. 말도 안 되는 소리다. 그건 있을 수도 없고 있어서도 안 되는 일이었다.

하지만 비로소 깨닫게 된 현실은 그렇지 않았다.

파르르 떨리던 시선이 위를 향했다. 조금 전까지만 해도 벌어진 혈투가 무색할 만큼, 침착한 표정을 짓고 있는 최민우를 바라본 송천우가 중얼거렸다.

“네가, 네가 어떻게?”

“글쎄요.”

최민우는 자신의 몸 안에 흐르는 막강한 기운을 느꼈다.

불과 몇 달 전까지만 하더라도 알아차릴 수 없던 그것은 외조부가 그에게 남긴 유일한 선물이었고, 진태경은 그 포장지를 뜯어 주인에게 돌려주었다.

선물을 유용하게 활용하는 방법과 함께.

“그건 아마도…… 내가 당신보다 강했기 때문일 겁니다.”

뿐만이 아니다. 최민우는 스스로를 믿었고, 올곧은 마음으로 행했다.

그리고 자격을 갖춘 주인에게, 어느 영웅의 혼이 서린 검은 더욱 큰 힘을 선물했다.

최민우는 힘 있는 눈빛으로 송천우를 내려다보았다.

“나는 승리했고, 당신은 졌습니다. 우리에게 남은 사실은 그뿐입니다.”

“……!”

잘게 떨리던 노인의 시선이 차츰 가라앉았다. 피에 젖은 입술 사이로 갈라진 목소리가 흘러나왔다.

“그래, 네 말대로다. 이런 결과는 예상치 못했지만.”

“그 부분만큼은 저와 같군요. 저 역시 정말 이런 상황이 오리라고는 생각지 못했으니까요.”

분노. 적개심. 밑바닥까지 추락한 인간을 향한 미약한 동정.

송천우를 향한 최민우의 감정은 다양했으나, 그중에서도 가장 앞선 것은 의문이었다.

도대체 왜. 무슨 이유로 송천우가 이런 짓을 벌였는지에 대한 의문. 그리고 앞서 그에게 들은 이야기에 대한 불신.

“왜 이런 짓을 벌였습니까. 우리가 힘을 합쳤다면, 석고준을 몰아내고 아레스 길드를 장악하는 건 그리 어려운 일이 아니었을 겁니다.”

최민우의 물음에, 송천우가 공허한 목소리로 대답했다.

“안다. 나 역시 그렇게 생각했다.”

“그렇다면 어째서?”

“어쩔 수 없었다. 거절할 수 없는 제안이었어.”

그리고 송천우에게 거절할 수 없는 제안을 건넨 사람의 이름을, 최민우는 이미 알고 있었다.

“석고준. 모든 것이 그자의 명령이었습니까? 나와의 연합부터 지금까지, 모두 다?”

“쿨럭. 명령?”

다시 한번 핏물을 쏟아 낸 송천우가 힘없이 웃었다. 그건 석고준을 향한 명백한 조소(嘲笑)였다.

“이정룡이라면 모를까. 그놈은 힘센 철부지에 불과하다. 내가 비록 비열하고 한심한 늙은이라고 해도, 그런 어린놈의 명령에 굴복할 정도는 아니야. 너와의 연합은 순전히 내 의지였다.”

“그렇다면.”

“말하지 않았느냐. 거절할 수 없는 제안이었다고.”

금방이라도 꺼질 듯한 송천우의 눈동자를 들여다보던 최민우는 문득 깨달았다.

눈앞의 노인에게 남은 것이 무엇인지. 거절할 수 없는 제안에 무엇이 들어가 있는지.

“가족이군요.”

작게 고개를 끄덕인 송천우가 입을 열었다.

“이정룡과의 싸움에서 진 후에야 알았다. 가장 소중한 것을 잊고 있었다는 사실을.”

치열했던 삶이었다.

대격변 이전에는 가장으로서 밤낮없이 생계를 책임져야 했고, 대격변 중에는 전장을 떠날 수 없었으며, 대격변 이후에는 권력의 중심에 다가서기 위해 또 다른 싸움을 시작했으니까.

그리고 이정룡과의 정쟁(政爭)에서 패하며 다시금 기억해 낸 가족의 소중함은, 이정룡의 죽음과 함께 깨어난 야심으로 잊혀졌다.

“자리를 비운 것이 화근이었다. 늙은이가 뒤늦게 욕심을 부린 대가겠지.”

“아마도 그 생각이 맞을 겁니다.”

송천우의 한탄에 대답하는 최민우의 목소리는 냉정했다. 그의 말을 듣고 있자니 마지막 남아 있던 동정심마저 사라지는 기분이었다.

“당신과 이정룡 때문에, 난 하나뿐인 가족을 잃어야 했습니다.”

차가운 말투에는 불길이 담겨 있었다.

두 어른의 야심에 의해, 야심이라는 단어의 뜻조차도 모르던 어린아이는 고아와 같은 신세가 됐다.

부모의 죽음을 제대로 인지하기도 전에 사라진 외조부를 원망하며 지금껏 살아 와야 했다.

“……미안하구나. 내 잘못이다.”

“그럼 당장 태워 죽여도 할 말이 없겠군. 그렇지 않나?”

허공에서 불쑥 들려온 목소리는 최민우가 아닌 다른 사람의 것이었다.

사박. 예티의 푸른 피를 전신에 뒤집어쓴 김화종이 지면에 발을 내디뎠다.

노 집사의 눈동자에는 손에 들린 불의 채찍과 같은 화염이 서려 있었다.

“화종이. 자네였나.”

“아가리 닥쳐라. 이 개새끼야. 네놈 때문에 도련님께서 얼마나-”

당장이라도 채찍을 휘두르려는 김화종을 만류한 것은 최민우였다.

가벼운 눈짓에 입을 꾹 다문 노복이 물러나자, 최민우의 시선이 송천우를 향했다.

“그럼 외할아버님에 관한 이야기도 모두 거짓입니까?”

“차라리 거짓이었다면 좋겠구나. 하지만 전부 사실이다. 이미 너무 멀리 와 버렸어.”

대답의 의미를 알아듣지 못해 미간을 찌푸리는 김화종과 달리, 최민우는 내심 안도와 실망이 뒤섞인 한숨을 내쉬었다.

외조부가 살아 있다는 사실은 기쁜 일이지만, 이십 년이 넘도록 의식을 잃은 상태라는 것이 마음에 걸렸다.

하지만 그것은 나중의 일. 지금 당장은 송천우의 처분이 우선이었다.

- 도련님.

자신을 향한 대견함과 송천우에 대한 분노, 그리고 일말의 기대감이 섞여 있는 김화종의 메시지 마법에 최민우는 고개를 저었다.

그가 무슨 말을 할지는 이미 알고 있었다.

- 김 집사님. 그건 안 됩니다.

- 안 된다니. 그게 무슨 말씀이십니까.

- 포션을 주십시오. 우선 죽지 않을 만큼만 치료해야겠습니다.

- 하지만……!

뭔가 외치려던 김화종은 침착한 최민우의 시선에 애써 마음을 억눌렀다.

그도 알고 있었다. 송천우는 살아 있는 것만으로도 결정적인 증인이자 증거라는 것을.

다만 부정하고 싶을 뿐이었다.

“김 집사님.”

“빌어먹을. 알겠습니다.”

중급 포션을 건네주며 욕설을 내뱉는 김화종의 모습에 최민우가 눈을 동그랗게 떴다.

“지금 제 앞에서 욕하신 겁니까?”

“예, 했습니다. 왜요?”

“이야기는 얼핏 들었지만, 제가 기억하는 모습과는 너무 다른데요.”

“이게 접니다. 도련님 어릴 때만 해도 보고 배울까 싶어서 행동 조심, 입조심 했던 거죠.”

“계속 조심하시지 왜…….”

“도련님도 이제 곧 서른입니다. 기왕 이렇게 된 거, 보고 배우려면 배우십시오. 아니면 마시고.”

어릴 적부터 곁을 지키던 그 사람이 맞나.

불퉁한 노 집사의 말투에 피식 웃은 최민우가 한 마디를 건넸다.

“김 집사님.”

“왜요. 그리고 웃지 마십시오. 어른한테 그러는 거 아닙니다.”

“감사합니다. 제 유일한 가족이 되어 주셔서.”

“……!”

“항상 이 말씀을 드리고 싶었습니다.”

진심이 담긴 한마디에 우뚝 굳은 노 집사와 눈을 마주칠 자신이 없어, 최민우는 말없이 돌아섰다.

내딛는 걸음 끝에는 눈밭에 파묻힌 채 죽음을 기다리는 한 노인이 그를 기다리고 있었다.

달칵.

마개를 따자 청아하면서도 은은한 향기가 비릿한 피 냄새를 몰아낸다.

송천우는 금방이라도 꺼질 듯한 눈동자로 다가오는 최민우를 바라보았다.

“나를…… 살릴 셈이냐?”

“살고 싶습니까?”

“그, 그건…….”

갈등하는 송천우의 모습에 최민우는 극심한 혐오를 느꼈다.

“마음 같아서는 당신을 죽이고 싶습니다. 백 번, 천 번도 더.”

“하, 하지만 가족들이…….”

“분명 방법이 있을 겁니다. 우선 이곳을 나간 후에 처리해야겠지만.”

“…….”

“선택하십시오.”

망설이던 송천우가 체념 어린 표정으로 고개를 끄덕였다.

냉정한 눈빛으로 그를 바라본 최민우가 천천히 포션을 기울였다.

치이익.

우윳빛 액체가 닿기 무섭게 조금씩 아무는 상처.

그것은 아주 미약한 회복이었지만, 누군가에게는 마지막 힘을 발휘할 수 있는 동앗줄과도 같았다.

파팍!

어디서 그런 힘이 솟았을까.

사방으로 튀는 눈더미 사이, 초인적인 힘으로 몸을 날린 송천우의 신형이 거대한 균열의 틈으로 미끄러졌다.
```

## Final English reading copy

```markdown
# Chapter 579

*Slice!*

The instant a streak of light cut across his chest, Song Cheonwoo felt his vision go dim.

*It’s hot.*

It was lightning.

The kind of lightning even a hero of old—one who had left his mark on the chaotic, perilous Great Cataclysm—had been unable to stop.

With trembling eyes, Song Cheonwoo stared at the sword in his hand.

Only a few seconds ago, it had been radiating a brilliant aura. Now it had been cut in half by something even more destructive and razor-sharp.

*Clang.*

The sword slipped from his grip and rolled across the ground. A beat later, pain swept through his entire body.

“Cough.”

*Drip, drip.*

Dark red blood spilled from the corner of his mouth and stained the snow. His clothes and armor split diagonally, exposing his bronze-colored upper body.

Then, the instant a fine line across his firm muscles and skin glowed red—

*SHWAAA!*

An enormous amount of blood burst forth like a waterfall.

From his left chest to his right hip. The scar left behind by the lightning that had swept across him was horrific, and it would never heal.

Feeling the strength leave his body, Song Cheonwoo staggered backward.

*Crunch.*

His powerless foot stepped onto snow soaked in blood.

One step. Two steps. Three steps. And then…

*Fsssh.*

At the sound of the piled-up snow sliding away, Song Cheonwoo barely managed to steady himself.

By then, a massive fissure known as a crevasse had opened its jaws behind him, waiting.

There was nowhere left to retreat—and nowhere left to advance.

*What a fucking mess.*

Song Cheonwoo felt his chest grow hollow.

Perhaps it was because the vitality was still draining from his body at that very moment.

He suddenly raised his head, and a figure slowly walking toward him entered his view.

*Choi Minwoo.*

The only blood relative of *that person*, who had always been an object of respect and fear.

Song Cheonwoo recalled the quiet voice he had heard just before facing the lightning.

*“Have you forgotten whose blood flows through my body?”*

At this moment, what was reflected in the old man’s eyes was someone else who was not here.

A person who had now become nothing more than a memory of the past.

A being who inspired respect and fear in anyone who merely watched him from nearby.

Song Cheonwoo realized something he had forgotten for a long time.

Cheon Taemin’s blood flowed through that young man’s body.

“...Hyung?”

Song Cheonwoo muttered the word between ragged breaths.

Through his vision dyed entirely red, the young man holding a sword that radiated brilliant light resembled his maternal grandfather.

The deep, solemn look in his eyes seemed to ask why Song Cheonwoo had changed sides.

“Don’t come any closer. Don’t!”

With a shout he barely managed to force out, Song Cheonwoo swung his sword. Or rather, he thought he had swung it.

But the hand that had dropped the sword moments earlier was empty. The hand flailing through empty air was finally stopped by the firm grip of someone who had reached him.

*Whooom. Crack.*

Choi Minwoo seized Song Cheonwoo’s wrist and tightened his grip.

With a sickening sound as the bones shifted out of place, a scream burst forth.

“GRAAAAAH!”

*Thud.*

Song Cheonwoo dropped to his knees, unable to withstand the pain. Choi Minwoo stared down at him with sunken eyes.

What he saw now was not Song Cheonwoo, but an old man.

*Zzt, zzt, zzt.*

The radiance contained within *Hero’s Soul* gradually faded.

The winner of this fight had already been decided.

Facing the fallen loser, the victor stood tall and quietly announced the result of their fierce battle.

“Stop. It’s over.”

“...!”

Song Cheonwoo’s body, writhing in pain, suddenly went rigid.

He had lost.

It was impossible. It could not happen, and it should not have happened.

But the reality he had finally come to understand was different.

His trembling gaze rose. He looked at Choi Minwoo, whose expression was calm enough to make the bloody battle from moments ago seem unreal, and muttered,

“How? How did you...?”

“I wonder.”

Choi Minwoo felt the immense energy flowing through his body.

Only a few months ago, he had been unable to sense it. It was the only gift his maternal grandfather had left him—and Jin Taekyung had torn open the wrapping and returned it to its rightful owner.

Along with how to make good use of the gift.

“Perhaps... it’s because I was stronger than you.”

That was not all. Choi Minwoo had believed in himself and acted with an upright heart.

And to a qualified owner, a sword containing the soul of a hero had granted even greater strength.

Choi Minwoo looked down at Song Cheonwoo with powerful eyes.

“I won, and you lost. That is all that remains between us.”

“...!”

The old man’s trembling gaze gradually settled. A cracked voice escaped between his bloodstained lips.

“Yes. You’re right. I didn’t expect this result, though.”

“We agree on that much. I never thought a situation like this would come either.”

Anger. Hostility. A faint trace of pity for a man who had fallen to the very bottom.

Choi Minwoo felt many things toward Song Cheonwoo, but the strongest of them all was a question.

Why? For what reason had Song Cheonwoo done this?

And he still distrusted the story Song Cheonwoo had told him earlier.

“Why did you do this? If we had joined forces, driving Go Jun out and taking control of Ares Guild would not have been difficult.”

Song Cheonwoo answered Choi Minwoo’s question in an empty voice.

“I know. I thought the same.”

“Then why?”

“I had no choice. It was an offer I couldn’t refuse.”

Choi Minwoo already knew the name of the person who had made Song Cheonwoo that offer.

“Go Jun. Was everything his order? From forming an alliance with me to what happened just now?”

“Cough. An order?”

Song Cheonwoo spat out blood once more and let out a weak laugh.

It was unmistakable mockery directed at Go Jun.

“If it were Lee Jungryong, perhaps. But that bastard is nothing more than a powerful, immature brat. I may be a despicable and pathetic old man, but I haven’t fallen so low that I would submit to the orders of some young punk. My alliance with you was entirely my own decision.”

“Then—”

“Didn’t I tell you? It was an offer I couldn’t refuse.”

As he looked into Song Cheonwoo’s eyes, which seemed ready to go out at any moment, Choi Minwoo suddenly understood.

What the old man still had left.

What that impossible-to-refuse offer contained.

“Your family.”

Song Cheonwoo gave a small nod before speaking.

“I only realized it after losing to Lee Jungryong. I had forgotten what mattered most.”

It had been a fierce life.

Before the Great Cataclysm, he had been forced to support his household day and night. During the Great Cataclysm, he had been unable to leave the battlefield. After the Great Cataclysm, he had begun another battle to approach the center of power.

And after losing his political struggle against Lee Jungryong, he had remembered the value of his family once more—only to forget it again when ambition awoke alongside Lee Jungryong’s death.

“My absence was the root of all this. I suppose this is the price an old man paid for reaching too greedily after ambition too late in life.”

“You’re probably right.”

Choi Minwoo’s voice as he answered Song Cheonwoo’s lament was cold. Listening to him made even the last remnants of pity disappear.

“Because of you and Lee Jungryong, I had to lose the only family I had.”

His cold voice held a flame.

Because of the ambitions of two adults, a child who did not even understand the meaning of ambition had been left in the position of an orphan.

Before he could properly comprehend his parents’ deaths, he had been forced to live on while resenting the maternal grandfather who had disappeared.

“...I’m sorry. It was my fault.”

“Then I suppose you wouldn’t have any objections if I burned you to death right now. Would you?”

The voice that suddenly rang out through the empty air did not belong to Choi Minwoo.

*Crunch.*

Kim Hwajong stepped onto the ground, covered from head to toe in blue yeti blood.

Flames like the fire whip in his hand burned in the old butler’s eyes.

“Hwa-jong. It was you.”

“Shut your fucking mouth, you piece of shit. Because of you, how much the Young Master—”

Choi Minwoo was the one who stopped Kim Hwajong from swinging his whip immediately.

At a slight glance from Choi Minwoo, the old servant clamped his mouth shut and stepped back. Choi Minwoo turned his gaze toward Song Cheonwoo.

“Then is everything you told me about my maternal grandfather a lie as well?”

“I wish it were a lie. But it is all true. I’ve already come too far.”

Unlike Kim Hwajong, who furrowed his brow because he could not understand the meaning of the answer, Choi Minwoo let out a sigh filled with both relief and disappointment.

The fact that his maternal grandfather was alive was good news, but the thought that he had been unconscious for more than twenty years troubled him.

But that was for later.

For now, Song Cheonwoo’s fate came first.

*—Young Master.*

At the message spell from Kim Hwajong, carrying pride in Choi Minwoo, fury toward Song Cheonwoo, and a trace of hope, Choi Minwoo shook his head.

He already knew what the old butler was going to say.

*—Butler Kim. That isn’t possible.*

*—What do you mean, it isn’t possible?*

*—Give me a potion. We need to treat him enough to keep him alive, at least for now.*

*—But...!*

Kim Hwajong had been about to shout something, but he forcibly restrained himself beneath Choi Minwoo’s calm gaze.

He knew too.

Song Cheonwoo was a decisive witness and a crucial piece of evidence simply by remaining alive.

He merely wanted to deny it.

“Butler Kim.”

“Damn it. All right.”

Choi Minwoo’s eyes widened when Kim Hwajong cursed as he handed over a mid-grade potion.

“Did you just swear in front of me?”

“Yes, I did. Why?”

“I heard bits and pieces about it, but this is completely different from how I remember you.”

“This is who I am. When you were young, I watched my behavior and my language in case you learned from me.”

“Why not keep doing that...?”

“You’re almost thirty now. Since things have come to this, learn from me if you want to learn. Otherwise, drink this.”

*Is he really the same person who stayed by my side since I was young?*

At the old butler’s gruff tone, Choi Minwoo let out a quiet laugh and said,

“Butler Kim.”

“What? And don’t laugh. You shouldn’t laugh at an adult like that.”

“Thank you. For becoming my only family.”

“...!”

“I’ve always wanted to say that.”

Unable to meet the old butler’s eyes after speaking those sincere words, Choi Minwoo turned away without another word.

At the end of the path before him, an old man lay buried in the snow, waiting for death.

*Click.*

When he opened the stopper, a clear yet subtle fragrance drove away the sharp smell of blood.

Song Cheonwoo looked at Choi Minwoo approaching him with eyes that seemed ready to go out at any moment.

“Are you... planning to save me?”

“Do you want to live?”

“I... I...”

As Song Cheonwoo hesitated, Choi Minwoo felt an intense disgust.

“If I had my way, I would kill you a hundred times, a thousand times over.”

“B-but my family...”

“There must be a way. But we’ll have to deal with that after we get out of here.”

“...”

“Choose.”

Song Cheonwoo hesitated, then nodded with an expression of resignation.

Choi Minwoo looked down at him coldly and slowly tilted the potion.

*Hiss.*

The wounds began to close little by little the instant the milky liquid touched them.

It was an extremely weak recovery, but to someone, it was a lifeline that could give them enough strength for one final effort.

*Crack!*

Where had he found such strength?

Amid the snow exploding in every direction, Song Cheonwoo launched himself with superhuman force and slipped into the enormous crevasse.
```
