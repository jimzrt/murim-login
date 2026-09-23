<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0915.txt",
      "sha256": "cbd011752ed68c2ab4622397eb523bfd3b8cf43ff7c8f7bfc812c8df79e597e0",
      "bytes": 13183
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "3725bc3081d6b209fdd2a5bffdd69be36577bf02d50800fa0f890431370468e1",
      "bytes": 1554
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "66855c040f4342a0b241cbbead8026d866de6b64af95427c21f76fe8c96ddd55",
      "bytes": 231435
    },
    {
      "path": "characters/Baek Yeon.md",
      "sha256": "4efdb36dafe54d9b026b5ab5b117f8cd1e61d8990dd7dfbce3e44083d6e6a109",
      "bytes": 837
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "379abce5f311d04d77615709e48c2f6cdc47349171eca79aa0e5b0fee606a0b6",
      "bytes": 759
    },
    {
      "path": "characters/Eastern Heaven Demon Lord.md",
      "sha256": "ace3be08fb2cc08f73a0b23fb42b9fc84889c21297d568785b70f1f92e53c8ad",
      "bytes": 731
    },
    {
      "path": "characters/Hwangso.md",
      "sha256": "3ea7ffafaff7e6ce0436d5c4d2f3f6266dd614e1feb6fa65c6db5a31071939ef",
      "bytes": 698
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "394975e0f0262261462cc25d678b0fc3740dea3448c8b5974993c6c730b72dce",
      "bytes": 1270
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "a91eced8abeb30cb1cb199e74c8e21a0a6725529239a0100306b347a4473d666",
      "bytes": 628
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "bd7e92f0fcef82e3f0bf1daae36c6a8d63fa57a70fd19bfa8481df19acd0eb78",
      "bytes": 1429
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "e18c7ee560ba241370446aaec13219ca084c53e692a24cc3ff1516b74db8e67f",
      "bytes": 622
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "1638683e95efbb9765394f7bfe067e25e20ecd1d06eee9d9ce474453e71d647d",
      "bytes": 699
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "4637725a14defe9252ef63a97ed6d3c413ad81e4f7b959b165b9baa1b6100caa",
      "bytes": 850
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "29cf583444f876891ad615e844577b5e2d4b1c783fbea0806f856e4390233855",
      "bytes": 998
    },
    {
      "path": "characters/So Gyo.md",
      "sha256": "218f31f96e2b07506047f777b8d7a965d713bd43e7cbafa67d554cb92e98bdd7",
      "bytes": 900
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "5dc14c33fe63f22c0a67a72bf57e7b23528ab2f8e6a624f4cf9bc5d8d10d226a",
      "bytes": 715
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "b4a0942083a80ea856a35d2e08827d4c15d441c985e29b1b8111b320877066df",
      "bytes": 888
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "321ba4a5c5fa5e418756499eee03dcf5f1245e9c9d95088e44d14e86ccef84c4",
      "bytes": 264440
    }
  ],
  "estimated_tokens": 14391
}
-->

# Durable State Update — Chapter 915

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 915. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 915. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
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
  "chapter": 915,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 915,
    "continuity_sources": [915],
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
    "The Eastern Heaven Demon Lord survived Taizu's destruction of the Maoshan Sect and blames the rulers and the world for the loss of his family and sect.",
    "The Eastern Heaven Demon Lord used Cang Gong's identity to rise to power within the Great Nation.",
    "The Eastern Heaven Demon Lord's bell raises the dead as powerful, agile corpses that do not fear injury or death.",
    "Ma Sanbao is among the risen dead following the Eastern Heaven Demon Lord.",
    "The Eastern Heaven Demon Lord has raised more than a thousand dead Imperial Guards and is advancing on the Emperor.",
    "Baek Yeon and So Gyo are defending the Emperor against the risen dead.",
    "So Gyo has revealed power comparable to Jeok Cheongang's and stopped the Eastern Heaven Demon Lord; her identity remains unknown.",
    "Jeok Cheongang and Jin Taekyung have returned to confront the Eastern Heaven Demon Lord.",
    "Jeok Cheongang still suffers unexplained cold pain."
  ],
  "continuity_sources": [
    914
  ],
  "open_questions": [
    "What caused Jeok Cheongang’s unexplained cold pain?",
    "What is So Gyo's identity and allegiance?",
    "Can Jeok Cheongang and Jin Taekyung stop the Eastern Heaven Demon Lord and protect the Emperor?",
    "What will happen to the Emperor and Prince Shangshan as the battle continues?"
  ],
  "safe_through": 914,
  "temporary_decisions": [
    "Keep “undead” as Jin Taekyung’s general term distinct from “jiangshi,” Jeok Cheongang’s Maoshan-related term."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 열화문    | **Fire Gate Clan**               |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 극양                        | **Extreme Yang**      |
| 상태               | **Status**                     |
| 명성               | **Fame**                       |
| 헌터      | **Hunter**            |
| 노부      | **this old man / I**                                            |
| 백연 | **Baek Yeon** | Commander of the Embroidered Uniform Guard. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 황소 | **Hwangso** | First-generation disciple of the Gongdao Sect and a reluctant search-party member. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 소교 | **So Gyo** | The palace attendant leading the group assigned to serve Prince Shangshan. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 강시 | **jiangshi** | Reanimated corpse from folklore; Childeuk and Hong mistakenly identify Taekyung as one. |
| 명장 | **Master Artisan** | Master craftsman capable of handling Ten-Thousand-Year Cold Iron |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 무한 | **Wuhan** | Capital of Hubei Province near Dongting Lake. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 서천 | **Western Heaven** | Short form used by the Lord of Heaven for the Western Heaven Demon Lord. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 황도십이궁 | **Twelve Palaces of the Zodiac** | Collective title for twelve Supreme Peak masters representing the imperial court. |
| 금우궁 | **Golden Ox Palace** | Palace title held by the Imperial Guard commander. |
| 금위군 | **Imperial Guards** | Imperial force distinct from the Embroidered Uniform Guard. |
| 언데드 | **undead** | Supernatural beings that are neither dead nor alive. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 서천마군 | 진태경 | hostile_opponents | you | calm and taunting | Uses 자네 while questioning Taekyung and offering to take him alive. |
| 진태경 | 서천마군 | hostile_opponents | Western Heaven Demon Lord | casual and defiant | Identifies the Demon Lord by title and answers his surrender demand with sarcasm. |
| 서천마군 | 신의 | hostile_invader_to_physician | Divine Physician | calm and mocking | Uses 신의 and 그대 while taunting the physician and dismissing his objections. |
| 신의 | 서천마군 | physician_to_invading_fiend | fiend | defiant and formal | Calls the Western Heaven Demon Lord an 악귀 and orders him to leave. |
| 서천마군 | 적천강 | hostile_invader_to_unconscious_patient | you | calm and predatory | Says someone wants to see Jeok Cheongang and attempts to move him with Seizing an Object Through Empty Space. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 서천마군 | hostile_opponents | you bastard | blunt and threatening | Jeok addresses the Western Heaven Demon Lord with 네놈 while defending Taekyung and ordering him not to touch his Disciple. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 사령관 | captor to captive undead commander | you | casual, mocking, and dismissive | Taekyung addresses the Skeleton Warlord informally while rejecting its pleas to turn back. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 적천강 | 남천마후 | legendary_martial_master_to_hostile_demon_empress | you bitch | blunt and threatening | Threatens to punish her and Lord of Heaven. |
| 남천마후 | 적천강 | hostile_demon_empress_to_legendary_martial_master | Fire King Jeok / you | flattering and mocking | Addresses Jeok Cheongang as the Fire King while praising Lord of Heaven. |
| 정호 | 진태경 | Shaolin Discipline Hall Master to patient and Benefactor | Benefactor Jin | formal-polite | Jung Ho repeatedly uses 진 시주 and 시주. |
| 진태경 | 정호 | patient to Shaolin Discipline Hall Master | Monk | polite and familiar | Taekyung addresses Jung Ho as 스님. |
| 적천강 | 의원 | interrogator_to_physician | you; quack | blunt and threatening | Jeok shakes the physician and demands an explanation for Jin's seven-day sleep before ordering him to summon the Beast Miao King. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 진태경 | 정호군 | young martial artist to senior imperial officer | Commander Jeong | casual and teasing, then conciliatory | Jin addresses him by rank while trying to defuse the standoff. |
| 백연 | 정호군 | commander to subordinate | you | direct and commanding | Uses 네 while testing Jeong Hogun’s obedience. |
| 진태경 | 백연 | young martial artist confronting an imperial military commander | you | casual and insulting | Refers to Baek as 이 양반 while challenging his conduct. |
| 진태경 | 상산왕 | protector addressing a young prince | His Highness | respectful royal address | Taekyung refers to the prince as 상산왕 전하 when ordering Mujin to bring him. |
| 정호군 | 상산왕 | imperial guard officer escorting the prince | His Highness | formal and deferential | Hogun formally reports that he has come to escort the prince. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 상산왕 | 황제 | younger brother addressing the Emperor | Your Majesty | deferential royal address | Shangshan addresses the Emperor as 폐하 while pleading for Taekyung. |
| 소교 | 진태경 | palace attendant addressing a martial artist and guest under escort | Young Master Jin | formal and respectful, but firm | Addresses him as 진 공자 while escorting him and warning him not to investigate. |
| 진태경 | 소교 | palace attendant and martial artist under imperial scrutiny | you | formal-polite, controlled and challenging | Taekyung addresses So Gyo as 당신 while questioning her presence and demanding an explanation. |
| 백연 | 진태경 | imperial commander confronting a young martial artist | Jin Taekyung | measured and familiar, using 자네 | Baek Yeon cautions Taekyung about his words and asks whether he must cause a scene. |
| 소교 | 백연 | political ally addressing a senior military commander | you | informal and direct | So Gyo uses 당신 and speaks without formality; no personal name or title is established. |
| 백연 | 소교 | military commander addressing a powerful political ally | you | formal and deferential | Baek Yeon uses 그대 while questioning So Gyo; she speaks without formality, which he accepts as her due. |
| 마삼보 | 정호군 | East Depot de facto leader to Embroidered Uniform Guard Thousand Captain | Commander Jeong | courteous and controlled | Ma Sanbao addresses him as 정 천호 while asserting procedural limits and drawing him into a conversation. |
| 정호군 | 마삼보 | Embroidered Uniform Guard Thousand Captain to East Depot official | Eunuch Ma | formal and guarded | Jeong Hogun addresses him as 마 태감 and shows wariness despite his restrained replies. |
| 마삼보 | 진태경 | political ally recruiting a young martial artist | you; my friend | courteous and familiar | Ma uses 자네 and 이보게 while explaining his choice of Jin and inviting him to join the restoration army. |
| 진태경 | 마삼보 | young martial artist addressing the East Depot’s Brush-Holding Eunuch and prospective ally | you; Brush-Holding Eunuch | polite and direct | Jin asks Ma why he withheld information and presses him for a clear answer; he refers to him as 태감. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |
| 황제 | 소교 | Emperor questioning a political ally | you | quiet and direct | The Emperor questions So Gyo through Sound Transmission about why she is only watching. |
| 소교 | 황제 | political ally answering the Emperor | Your Majesty | calm and direct | So Gyo answers the Emperor through Sound Transmission without wavering. |
| 적천강 | 동천마군 | enemies | you | blunt and informal | Jeok Cheongang addresses the Eastern Heaven Demon Lord with hostile familiarity. |
| 동천마군 | 적천강 | enemies | you | informal | The Eastern Heaven Demon Lord speaks to Jeok Cheongang during their duel. |
| 마삼보 | 동천마군 | disciple_to_master | Master | deferential | Ma Sanbao addresses the Eastern Heaven Demon Lord as 스승님 when rejoining him. |
| 황제 | 동천마군 | former ruler addressing a former subject, now an enemy | you | measured and formal | The Emperor asks why the Demon Lord betrayed his father, the late Emperor. |
| 동천마군 | 황제 | former subject addressing the Emperor, now an enemy | you; you bastards | hostile and contemptuous | He denies ever being loyal to the imperial family and accuses the rulers of betrayal. |
| 동천마군 | 소교 | enemies | you; you woman | hostile and demanding | He demands that So Gyo reveal her identity. |
| 소교 | 동천마군 | enemies | you | casual, taunting, and threatening | She warns him to stop and taunts him about whether suicide would still kill him. |
| 진태경 | 동천마군 | young martial artist confronting an enemy | ugly-ass big bro | casual, profane, and taunting | Jin calls out to the Demon Lord after returning to the hall. |

## Listed compact profiles

### Baek Yeon.md

# Baek Yeon (백연)

- **Safe through:** Chapter 914
- **Aliases:** Blood Envoy
- **Role:** Baek Yeon is the Commander of the Embroidered Uniform Guard, a former martial arts instructor to the Crown Prince, and the Blood Envoy who helped the fourth prince seize the throne and led the purge.
- **Personality:** Politically assured and controlled, he enforces authority with ruthless decisiveness but speaks with striking defiance to the Emperor in private when their shared undertaking is at stake.
- **Voice:** Not established
- **Relationships:** He commands the Embroidered Uniform Guard and serves the Emperor, carrying out the late Emperor’s final command to plan for the future alongside the fourth prince; he treats Taekyung as a dangerous potential obstacle.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 914
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Eastern Heaven Demon Lord.md

# Eastern Heaven Demon Lord (동천마군)

- **Safe through:** Chapter 914
- **Aliases:** None
- **Role:** The Eastern Heaven Demon Lord is a being no longer human, a former Maoshan Sect disciple who commands the dead with a bell.
- **Personality:** His hatred of rulers is rooted in the loss of his family to the violence of the age of chaos and the destruction of the Maoshan Sect, where he had found happiness.
- **Voice:** He speaks in measured, almost lyrical phrasing, recounting the past before turning to pointed accusations.
- **Relationships:** Ma Sanbao is his Disciple; he holds the Emperor responsible for Taizu’s actions against the Maoshan Sect.

### Hwangso.md

# Hwangso (황소)

- **Safe through:** Chapter 908
- **Aliases:** None
- **Role:** First-generation disciple of the Gongdao Sect in Sichuan, deployed with roughly thirty second- and third-generation disciples to search for the surviving Third Fiend.
- **Personality:** Privileged, impatient, pleasure-seeking, inattentive, and dismissive of the danger surrounding the mission.
- **Voice:** Complaining and casual, with irreverent sarcasm toward his Senior Brother and the search.
- **Relationships:** His Senior Brother supervises him, and his prosperous merchant father forced him into the Murim to establish family connections.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 914
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts Jin Taekyung, his publicly acknowledged Disciple and intended heir, regards him as the light of his later years, and will stand by him whatever path he chooses; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 913
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he follows imperial orders without hesitation and reads the political consequences of events with care.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Jeong Hogun serves under Baek Yeon’s command in the Embroidered Uniform Guard.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 914
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Ma Sanbao, whom Taekyung killed, has been raised among the Eastern Heaven Demon Lord’s undead, while Jeong Hogun and the Embroidered Uniform Guard have declared themselves allies of the Emperor, and So Gyo’s allegiance remains unknown.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 914
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 913
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 914
- **Aliases:** None
- **Role:** Ma Sanbao is the East Depot’s Brush-Holding Eunuch and a Supreme Peak martial artist who secretly led a restoration effort for Prince Shangshan as a disciple of the Eastern Heaven Demon Lord.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks in measured, courteous language and uses calm repetition, feigned agreement, and procedural reminders to steer conversations while keeping sensitive details guarded.
- **Relationships:** Ma Sanbao was a longtime friend and former East Depot cohort of Hong Jin, served the Eastern Heaven Demon Lord, and led a restoration effort for Prince Shangshan.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 914
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is the Emperor’s twelve-year-old youngest younger brother, an exceptionally skilled young swordsman, and the heir publicly designated by the Emperor.
- **Personality:** Earnest and compassionate, he takes responsibility for his loyal subjects’ hardship, admires Jin Taekyung, seeks candid counsel, and shows composure beyond his years in the face of death and political danger.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s youngest younger brother; the late Emperor entrusted Hong Jin with his care. Zhu Bao admires Jin Taekyung, seeks to emulate him, and calls him a friend; the Emperor says he will take care of Zhu Bao.

### So Gyo.md

# So Gyo (소교)

- **Safe through:** Chapter 914
- **Aliases:** None
- **Role:** A palace attendant assigned to Prince Shangshan who is a Supreme Peak master and has a mission to keep Jin Taekyung alive; her identity and allegiance remain unconfirmed.
- **Personality:** Calm, calculating, and self-possessed; she conceals her strength and identity and can be openly taunting.
- **Voice:** Measured and composed, shifting from deferential formality to casual, pointed taunts and threats.
- **Relationships:** She poses as the leader of the palace attendants assigned to Prince Shangshan and is Jin Taekyung’s opponent, yet believes he may be the person she seeks and the person foretold by “that person”; she says only she and the Emperor know a secret she withheld from Baek Yeon, while her true allegiance remains unknown.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 904
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress was Honglan, the creator of the rift behind the Inner Palace, and was killed after the rift closed.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 904
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃915화



“빨리 왔군. 생각했던 것보다도 훨씬.”

짧은 침묵 끝에 흘러나온 첫 마디와 함께, 동천마군은 깊게 가라앉은 눈빛으로 말을 이었다.

“그래서 더 일찍 죽게 되겠지만.”

차가운 회색빛 눈동자가 나와 적천강을 번갈아 응시한다.

정확히는 우리의 전신 곳곳에 아로새겨진 크고 작은 상처들을.

‘빌어먹을. 눈치 하나는 더럽게 빨라요.’

억지로 끌어올렸던 입꼬리가 느슨해진다. 나는 몸 곳곳에서 전해지는 통증을 애써 무시하며 자세를 낮추었다.

강시. 혹은 언데드.

도무지 무엇으로 정의 내려야 할지조차 모를 그것들을 몇 마리나 쓰러트렸는지 모르겠다.

그저 끝없이 밀려드는 괴물들을 상대로 싸우고, 또 싸웠을 뿐이다.

손에 잡히는 거라면 뭐든 휘둘렀고, 그조차도 없으면 주먹과 발길질로 터트리고 부쉈다.

상대가 평범한 인간이었다면 이토록 고생하지는 않았을 것이다.

그러나 놈들은 아니었다.

일격만으로도 즉사시켰을 공격을 최소 서너 번은 쏟아부어야 했고, 그렇게 해야 비로소 전투 불능 상태에 빠트릴 수 있었다.

‘차라리 공력이라도 충분했다면 훨씬 수월했겠지만…….’

이미 나도, 적천강도 지속된 전투로 상당한 공력을 소모한 상태.

열화문의 비전 심법으로 축적할 수 있는 극양(極陽)의 열양지기는 망자들이 지닌 사기(死氣)와 서로 상극이지만, 무한정 끌어 쓸 수는 없는 법이었다.

더군다나, 아직 동천마군이라는 강적이 남아 있다면 더더욱.

“꽤나 지친 것 같은데, 차라리 지금이라도 돌아가는 건 어떻겠느냐.”

동천마군이 우리의 어깨너머를 힐끗 바라보며 덧붙였다.

“남아 있는 자들이 모조리 죽기 전에.”

꾸욱.

정곡을 찌르는 한 마디에, 나도 모르게 창을 쥐고 있는 손아귀에 힘이 들어간다.

그 말이 사실이었으니까.

동천마군의 판단이 그만큼 정확했으니까.

나와 적천강이 포위망의 일각을 허물어트리고 왔을 뿐 등 뒤에는 아직 적지 않은 숫자의 괴물들이 남아 있었고, 정호군이 이끄는 금의위와 화룡각 대원들은 온 힘을 다해 분투 중이었다.

적들에 비하면 절반에도 턱없이 못 미치는 머릿수.

게다가 그 적들의 정체는 지치지도, 쉽사리 죽지도 않는 진짜배기 괴물들.

하지만 그럼에도 저들을 두고 올 수밖에 없었던 이유는, 이것만이 유일한 정답이라고 판단했기 때문이었다.

‘동천마군을 제거하지 않는 이상, 이 전투는 끝나지 않는다.’

이미 두 번에 걸쳐 시체를 일으켜 세운 동천마군이다. 그 두 번이 세 번, 네 번이 되지 않으리라는 법은 없다.

그리고 지금 같은 상황이 반복된다면…….

‘죽겠지. 모두.’

시간이 흐를수록 아군은 죽어 가고, 적들은 증식한다.

언제 도착할지 모를, 아니 황제가 준비해 뒀는지조차 모르는 지원군이 합류한다고 해도 마찬가지다.

‘하지만 우두머리를 제거한다면 다르지.’

무림인이기 이전에 헌터로서 살아왔던 나는 알고 있다.

언데드 군단을 무너트리는 가장 빠르고 효율적인 방법은, 그들을 죽음에서 일으켜 세운 리치(Lich)를 제거하는 것뿐이라는 사실을.

다만 문제는 시간이었다.

늦어도 일각(一刻).

그 안에 어떻게든 놈을 쓰러트려야 한다. 일각을 넘게 되면 나와 적천강이 빠진 빈자리는 아군의 시체로 가득 채워질 것이다.

소교와 백연이 책임지고 있는 또 다른 전선이 허물어져도 결과는 마찬가지다.

지금 유지되고 있는 이 양면전선(兩面前線)의 균형이 기울어지기 전에 동천마군을 쓰러트리는 것만이, 이 상황을 타개할 수 있는 유일한 해법이었다.

하지만…….

‘할 수 있을까. 그것도 그 짧은 시간 안에?’

나는 불현듯 떠오른 의문을 쉽게 떨쳐내지 못했다.

모르겠다. 이 선택이 옳은 것인지.

어쩌면 상산왕과 화룡각 대원들만이라도 구해서 이 빌어먹을 황궁을 탈출하는 것이, 그렇게라도 살아남는 것이 최선은 아닐까 하는 의문이 송곳처럼 마음 한구석을 찔렀다.

그어어어!

카카캉. 커헉!

애써 외면하고 있던 등 뒤의 괴성이, 사람들의 비명과 날붙이가 부딪치는 충돌음이 귓가로 선명하게 전해진다. 끊임없이 머릿속을 헤집었다.

‘제기랄.’

흘러나오려는 욕설을 삼키며 창 자루를 터질 듯이 움켜쥔 그 순간.

- 할 수 있다.

“……!”

- 믿거라.

내 생각을 훤히 들여다본 듯한 적천강의 전음(傳音)에, 나는 흔들리던 마음이 놀라울 만큼 평온하게 가라앉는 것을 느꼈다.

맞다.

할 수 있다. 아니, 해내야 한다.

노야라면, 적천강과 함께라면 가능하다.

나 혼자가 아니라 ‘우리’이기에 그렇다.

설령 그 상대가 무려 셋이나 되는 초절정 고수라고 해도.

그들 한 사람, 한 사람이 이미 인간을 아득히 벗어난 괴물들이라 해도.

나는 싸워야 한다.

놈들을 쓰러트려야 한다.

- 지금!

귓가를 파고드는 힘 있는 한 마디와 함께, 나와 적천강은 동시에 발걸음을 떼었다.

팟.

찰나의 순간 속에 지워지는 공간에서, 우리는 이미 오래전부터 약속했던 것처럼 일장(一掌)을 뻗었다.

화륵, 콰아아아!

맹렬한 화염이, 공기를 살라 먹었다.



* * *



콰아아앙!

끔찍하리만치 뜨겁고, 위협적이다.

삼파전(三巴戰)이 되어 버린 전투의 흐름 속에서, 불길을 피해 신형을 날린 동천마군은 문득 떠올렸다.

지금의 이 상황이, 세 발 달린 솥과 다름없다는 생각을.

‘한쪽 다리라도 꺾이면, 솥 전체의 균형이 허물어진다.’

물론 전체적인 전황은 동천마군에게 유리했다.

가장 주의해야 할 소교는 백연과 함께 물경 일천이 훌쩍 넘어가는 괴물들을 상대하느라 발이 묶여 있었고, 정호군이 이끄는 금의위와 화룡각 대원들은 버티는 것이 고작이었으니까.

그러나 한 개의 다리라도 사라지면 허물어지는 세 발 솥에도 가장 중요한 다리는 있었다.

바로 동천마군 자신이다.

‘그걸 위해, 이토록 무리하면서까지 포위망을 뚫은 거겠지.’

콰앙!

빗나간 일격에 이어, 이격(二擊)도 어렵지 않게 피해 낸 동천마군은 자신을 향해 달려드는 두 사람을 침착하게 바라보았다.

저들은 순식간에 핵심을 파악했다.

이미 한 번 죽은 적들이, 동료들이 되살아나는 이 혼란스러운 상황 속에서 약점을 간파해 냈다.

그렇다면 그건 스승과 제자 중 누구의 판단이었을까.

적천강?

아니면 진태경?

‘전자라면 과연 화왕이다 싶겠지만, 만약 후자라면…… 왜 그분께서 그토록 원하시는지 알겠군.’

나이를 믿을 수 없을 만큼 강대한 무위. 거기에 더해 어떤 상황에서도 흔들리지 않는 침착성과 전투의 핵심을 꿰뚫는 과감한 판단력까지.

물경 백만에 달하는 대국의 군부에도 맹장(猛將)은 많다.

하지만 명장(名將)은 드물다.

그리고 진태경은 그 두 가지를 모두 갖췄다. 고작 약관이 갓 넘은 나이에.

‘혹, 저 아이로 떠난 자들의 빈자리를 채울 심산이신가.’

지난 몇 달 사이 서천마군이, 남천마후가 죽었다.

비록 아직 동천마군 자신을 비롯한 여러 강자가 남아 있다고는 해도, 떠난 이들의 공백으로 비어 버린 전력은 어떤 방식으로든 채워야 한다.

자신의 복수를 위해서라도.

남아 있는 대업을 위해서라도.

그리고 그런 의미에서, 지금 이 순간 동천마군의 눈에 비친 진태경은 그들의 공백을 메우고도 남을 훌륭한 재목이었다.

물론 그 스승은 결코 살려 두어선 안 되겠지만.

딸랑.

물 흐르듯 회피하는 움직임과 함께 울려 퍼지는 방울 소리.

그와 동시에 금위군 총사령관이자, 황도십이궁에 속한 초절정 고수인 금우궁(金牛宮)이 즉각 반응했다.

후웅!

어지간한 장정보다도 커다란 대검(大劍)이 공간을 가른다.

물러나는 동천마군을 향해 끊임없이 짓쳐 들던 적천강이 불길 같은 외침을 토해 냈다.

“네놈 따위가 감히!”

그 순간.

화륵, 꽈아앙!

생전의 위력보다도 강력해진 대검의 강기가, 멸염신권(滅炎神拳)의 열기와 만났다.

아니, 휩쓸렸다.

쩌적, 콰아아아!

무언가 갈라지는 듯한, 미세한 소음.

그것은 끔찍하리만치 강력한 힘을 이겨 내지 못한 강기가, 대검이 파괴되는 소리였고 맹렬하게 일어난 화염은 수십여 개로 나뉜 파편을 녹이는 동시에 튕겨 냈다.

감히 화왕이라는 이름에 맞선 대검의 주인을 향해.

파파파팟! 푸푹!

마치 섬광처럼 살과 뼈를 부수며 틀어박힌 십여 개의 핏줄기.

그 충격에 금우궁의 육신이 흔들리고, 체내에 남아 있던 핏물이 분수처럼 뿜어져 나왔다.

푸화악!

천하의 그 어떤 의원이 보더라도 즉사를 확신했을 부상.

그러나 금우궁은, 인간을 벗어난 괴물이 되어 버린 그에게는 저주와도 같은 끈질긴 생명력과, 몇 번을 죽더라도 반드시 이뤄 내야 할 사명이 있었다.

- 화왕을 죽여라.

앞서 텅 비어 버린 의식 속에 선명히 틀어박힌 주인의 명령이.

방울 소리로 각인된 그의 유일한 사명이 비틀거리던 망자의 육신에 힘을 불어넣는다. 이미 잊어버린 통증 따위는 조금도 신경 쓰지 않고 달려들게 만든다.

바로 지금처럼.

그아아아!

새하얗게 드러난 흰자위와 듣는 이로 하여금 공포를 느끼게 하는 괴성.

한때 금우궁이라 불리던 금위군의 우두머리는, 생전의 명성을 증명하는 부서진 황금빛 갑옷을 번뜩이며 쏘아졌다.

후웅!

바람이 뭉개진다. 공간이 지워진다.

앞을 가로막은 화염에, 끔찍한 열기에 갑옷과 살갗이 녹아 하나가 되어도 그는 멈추지 않았다.

금우궁이라는 그 이명처럼, 성난 황소가 되어 그저 온 힘을 다해 돌진할 뿐이었다.

오직 한 사람.

화왕이라 불리는 거인(巨人)을 향해.

그리고 자신을 방패막이로 삼아 그 거인을 쓰러트리려 하는 주인의 명령을 완수하기 위해.

츠츠츠!

이제는 대검이라고 부를 수 없는, 고작 한 뼘밖에 남지 않은 검신 위로 솟구치는 강기.

하지만 지금 이 순간 적천강의 지닌 날 선 감각에는, 사각(斜角)에서 들이닥치는 또 다른 공격이 느껴지고 있었다.

“……!”

동천마군. 바로 그였다.

교활한 것만큼이나 고강한 무위를 지닌 그가, 스스로를 살아 있는 괴물로 만들면서까지 사문의 원한을 갚으려 하는 복수귀(復讐鬼)가 신형을 틀어 섬광처럼 들이닥치고 있었다.

멸염신권의 화염에도 아랑곳하지 않는 또 다른 괴물과 함께.

‘제기랄.’

느려진 세상 속, 일순간 적천강의 눈동자 위로 갈등이 스쳤다.

불과 일장도 되지 않는 거리.

이미 물러서기에는 늦었다.

회피?

물론 성공한다면 최선이다. 그러나 만약 실패한다면, 그로 인해 여기서 더 치명적인 부상을 입게 된다면…….

‘죽는다. 틀림없이.’

그리고 적천강이 걱정하는 것은 자신의 목숨이 아니었다.

얼마 떨어지지 않은 곳에서 싸우고 있는 한 사람.

이미 지칠 대로 지쳐 있음에도 마삼보를 상대로 몰아붙이고 있는, 자랑스럽기 그지없는 자신의 제자였다.

‘노부가 이대로 쓰러지면, 모든 것이 끝장이다.’

그렇기에 코앞까지 들이닥친 그 공격을 피할 수 없었다.

맞서 싸울 수밖에 없었다.

회복하지 못할 부상을 입는다 하더라도, 설령 숨이 끊긴다 해도 이 격돌에서 이겨야 했다.

저 괴물들에게 두 번 다시 극복하지 못할 확실한 죽음을 내려 주어야 했다.

‘그래, 그래야만…….’

저 아이가 산다.

화륵.

느리게 흐르는 시간 속에서, 한 줄기 불꽃이 아름답게 피어오른 그 순간.

‘죽여 주마. 죽을 때까지.’

화왕 적천강은 그 어느 때보다 강맹한 화염과 함께 두 팔을 떨쳤다.

꽈아아앙!

거대한 굉음이, 시야를 물들이는 섬광이 멈췄던 시간이 되돌렸다. 그 뒤흔들리는 시간 속에서 한 줄기의 검광(劍光)과 익숙한 외침이 뒤섞였다.

“노야!”

푹!

뜨거운 핏물이 떨어졌다.
```

## Final English reading copy

```markdown
# Chapter 915

“You got here fast. Much faster than I expected.”

After a brief silence, the Eastern Heaven Demon Lord continued, his gaze sunk deep.

“Which means you’ll die all the sooner.”

His cold, gray eyes moved between Jeok Cheongang and me.

More precisely, they lingered on the large and small wounds etched across our bodies.

*Damn. He’s sharp as hell.*

The smile I’d forced onto my face slackened. I ignored the pain coming from every part of my body and lowered my stance.

Jiangshi. Or undead.

I’d lost count of how many of those things I’d taken down. I couldn’t even decide what to call them.

All I’d done was fight the monsters pouring in without end, then fight some more.

I swung anything I could get my hands on. When there was nothing left to swing, I smashed them apart with my fists and feet.

If they’d been ordinary humans, it wouldn’t have been this hard.

But they weren’t.

I had to hit them at least three or four times with attacks that should’ve killed them in one blow just to render them unable to fight.

*It would’ve been a lot easier if I’d had enough internal energy…*

Jeok Cheongang and I had both spent a considerable amount of internal energy in the fight.

The Extreme Yang Scorching Yang Qi accumulated through the Fire Gate Clan’s secret cultivation technique was the polar opposite of the death energy the dead possessed. But we couldn’t draw on it without limit.

Especially with a powerful enemy like the Eastern Heaven Demon Lord still ahead of us.

“You both look exhausted. Why don’t you turn back now, while you still can?”

The Eastern Heaven Demon Lord glanced over our shoulders.

“Before everyone left behind is dead.”

*Clench.*

His words hit a little too close to home, and my hand tightened around the spear before I realized it.

Because he was right.

His judgment was that accurate.

Jeok Cheongang and I had broken through one section of the encirclement to reach him, but plenty of monsters remained behind us. The Embroidered Uniform Guard led by Jeong Hogun and the Fire Dragon Pavilion members were fighting with everything they had.

Their numbers fell far short of even half the enemy’s.

And the enemy were genuine monsters—things that didn’t tire and wouldn’t die easily.

But we’d had no choice but to leave them behind. We’d decided this was the only right answer.

*This battle won’t end unless we take out the Eastern Heaven Demon Lord.*

He’d raised the dead twice already. There was no guarantee it wouldn’t become three times, or four.

And if the same thing happened again…

*We’d die. Every last one of us.*

As time passed, our allies died while the enemy multiplied.

It wouldn’t matter even if reinforcements arrived—assuming they ever did, and assuming the Emperor had prepared any at all.

*But if we take out their leader, things will change.*

Before I was a Murim martial artist, I’d lived as a Hunter. I knew that the fastest, most efficient way to bring down an undead army was to eliminate the Lich who’d raised them from the dead.

The problem was time.

Fifteen minutes at most.

We had to take him down somehow within that time. If it went longer, the gap left by Jeok Cheongang and me would be filled with the bodies of our allies.

The result would be the same if the other front, where So Gyo and Baek Yeon were holding the line, collapsed.

The only way to turn this situation around was to defeat the Eastern Heaven Demon Lord before the balance of the two fronts tipped.

But…

*Can we do it? In that short a time?*

The doubt that suddenly surfaced refused to leave.

I didn’t know if this was the right choice.

Maybe saving Prince Shangshan and the Fire Dragon Pavilion members and escaping this damn imperial palace was the best we could do. Maybe surviving, even if that was all we managed, was the right answer. The question stabbed at a corner of my heart like an awl.

*GRAAAH!*

*Clang! Cough!*

The roars I’d been trying to ignore behind me, the screams of people and the clash of blades, rang sharply in my ears. They kept tearing through my thoughts.

*Damn it.*

I swallowed the curse rising to my lips and gripped the spear shaft until it felt ready to burst.

—You can do it.

“……!”

—Trust me.

At Jeok Cheongang’s Sound Transmission, as if he could see straight through my thoughts, my wavering heart settled into a surprising calm.

That’s right.

I can do this. No—I have to.

If it’s the Old Master, if I’m with Jeok Cheongang, it’s possible.

Because I’m not alone. It’s *us*.

Even if we’re facing three Supreme Peak masters.

Even if every one of them is a monster who’s already left humanity far behind.

I have to fight.

I have to take them down.

—Now!

At the forceful words that pierced my ear, Jeok Cheongang and I stepped forward at the same time.

*Whoosh.*

As space vanished in an instant, we thrust out our palms as if we’d planned it long ago.

*Fwoosh! KABOOM!*

A raging blaze devoured the air.

* * *

*BOOM!*

It was unbearably hot. And terrifying.

As the fight became a three-way battle, the Eastern Heaven Demon Lord leaped clear of the flames and suddenly thought of a three-legged cauldron.

*If even one leg gives way, the whole cauldron loses its balance.*

The overall battle was certainly in his favor.

So Gyo, the one he had to be most wary of, was tied down fighting the well over a thousand monsters alongside Baek Yeon. The best the Embroidered Uniform Guard led by Jeong Hogun and the Fire Dragon Pavilion members could do was hold on.

But even a three-legged cauldron, which would topple if a single leg disappeared, had one leg more important than the others.

That leg was the Eastern Heaven Demon Lord himself.

*That’s why they broke through the encirclement at such a cost.*

*Boom!*

After easily dodging the first missed attack and then the second, the Eastern Heaven Demon Lord calmly watched the two men charging at him.

They’d grasped the heart of the matter in an instant.

Amid the chaos of fallen enemies and comrades alike rising again, they’d seen through his weakness.

So which of the two had made the call—the Master or the Disciple?

Jeok Cheongang?

Or Jin Taekyung?

*If it was the former, I’d expect nothing less of the Fire King. But if it was the latter… I understand why that person wants him so badly.*

Powerful enough to defy his age. On top of that, a composure that never wavered, and the bold judgment to see through the heart of a battle in any situation.

Even the armies of the Great Nation, numbering a million, had many fierce generals.

But truly great commanders were rare.

And Jin Taekyung had both qualities. At barely past twenty.

*Could that person intend for this boy to fill the vacancies left by those who have departed?*

Over the past few months, the Western Heaven Demon Lord had died, and so had the Southern Heaven Demon Empress.

Though many powerful figures remained, including the Eastern Heaven Demon Lord himself, the forces lost with those who had departed had to be replenished somehow.

For his revenge.

For the great undertaking that remained.

And in that sense, Jin Taekyung looked to the Eastern Heaven Demon Lord like a fine prospect—one who could more than fill the gap they’d left behind.

His Master, of course, could never be allowed to live.

*Jingle.*

As the Eastern Heaven Demon Lord moved with fluid evasions, a bell rang out.

At the same moment, Golden Ox Palace—the commander-in-chief of the Imperial Guards and a Supreme Peak master of the Twelve Palaces of the Zodiac—reacted at once.

*Whoosh!*

A greatsword, larger than most grown men, cut through the air.

Jeok Cheongang had been relentlessly pressing the retreating Eastern Heaven Demon Lord. Now he let out a shout like a burst of flame.

“How dare a bastard like you!”

In that moment—

*Fwoosh! KABOOM!*

The Force of the greatsword, stronger than it had been in life, met the heat of the Flame-Extinguishing Divine Fist.

No—it was swept away by it.

*Crack. KABOOM!*

A faint sound, like something splitting apart.

The Force, unable to withstand the terrifying power, shattered along with the greatsword. The blazing flames melted the dozens of fragments and sent them flying back.

Straight toward the wielder of the greatsword, who had dared to challenge the name of the Fire King.

*Papat! Thud!*

More than ten blood-streaked shards shot into him like flashes of light, shattering flesh and bone as they lodged inside.

The impact shook Golden Ox Palace’s body, and the blood still left inside him gushed out like a fountain.

*Splaaat!*

Any physician in the land would have looked at the wound and been certain he was dead on the spot.

But Golden Ox Palace had become a monster, and with that came a cursed tenacity—a life that refused to end. He also had a mission that had to be completed, no matter how many times he died.

—Kill the Fire King.

His master’s command, driven deep into the empty consciousness that had opened before him. His sole mission, engraved in the sound of the bell, poured strength into the swaying corpse. It sent him charging forward without a care for the pain he’d already forgotten.

Just as he was now.

*GRAAAH!*

With his whites showing and a roar that made anyone who heard it feel fear, the commander of the Imperial Guards, once called Golden Ox Palace, shot forward. His broken golden armor gleamed, proof of the fame he’d earned in life.

*Whoosh!*

The wind buckled. Space vanished.

Even as the armor and flesh of his body melted together in the heat and flames blocking his path, he didn’t stop.

Like an enraged bull, true to the name Golden Ox Palace, he charged with all his might.

At one person alone.

The giant known as the Fire King.

And to carry out the order of his master, who meant to use him as a shield to bring that giant down.

*Tssss!*

Force surged over what could no longer be called a greatsword, with barely a handspan of blade left.

But in that moment, Jeok Cheongang’s keen senses detected another attack closing in from an angle.

“……!”

The Eastern Heaven Demon Lord. It was him.

A man as powerful as he was cunning, a vengeful spirit willing to turn himself into a living monster to avenge his sect’s grudge, twisted his body and shot toward Jeok Cheongang like a flash of light.

Alongside another monster, one who paid no heed to the flames of the Flame-Extinguishing Divine Fist.

*Damn it.*

In the slowed world, a flicker of conflict crossed Jeok Cheongang’s eyes.

They were less than one *jang* away.

It was too late to retreat.

Dodge?

Of course, that would be best if he could manage it. But if he failed, and ended up with an even more serious injury…

*I’ll die. No question.*

And Jeok Cheongang wasn’t worried about his own life.

It was the one fighting not far away.

His proud Disciple was exhausted to the limit, yet still driving Ma Sanbao back.

*If this old man falls here, it’s all over.*

That was why he couldn’t avoid the attack bearing down on him.

He had no choice but to fight back.

Even if he suffered an injury he’d never recover from, even if his life ended, he had to win this clash.

He had to give those monsters a certain death they would never overcome again.

*Yes. That’s the only way…*

The boy would live.

*Fwoosh.*

In the slow-moving time, a single flame blossomed beautifully.

*I’ll kill you. I’ll kill you until you die.*

The Fire King Jeok Cheongang swung both arms, unleashing flames more fierce than ever before.

*KABOOM!*

The deafening boom and the flash that filled his vision returned time to motion. Within that shuddering moment, a streak of swordlight mingled with a familiar cry.

“Old Master!”

*Thud!*

Hot blood fell.
```
