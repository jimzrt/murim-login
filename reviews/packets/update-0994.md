<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0994.txt",
      "sha256": "7310a1c58a13066f23df46776805d229c1856cdc729b37c8344d7f10ddde493a",
      "bytes": 12688
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "04740fc65ba4d2f9bb636dcfbdc9f458c7c59e259020b53c5feb2d9ca0be365d",
      "bytes": 1829
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d13308fe31a2c64daebd8b79b1737ef2a4f6a2f6e86338670363f6d7acf5174f",
      "bytes": 236719
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "958fd9f0b896a9d8459a45dc6ceefcfd863489fea71456ce08f41d6d338fbbf5",
      "bytes": 776
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "7a709db42e99bfe7d3a3188df33d603a08de94200f8e9f838bde2ece10b7a733",
      "bytes": 759
    },
    {
      "path": "characters/Doppelganger.md",
      "sha256": "da60b83ea9aca916e4daaeae7952cfb2995b97f071b514e7066c81a1d57c478c",
      "bytes": 866
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "2ea6564afa04f0c521e549415b6c4a862e9c66b1c455f8017c17a3a8c29ca1b5",
      "bytes": 1374
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "b9b8ac7830733457b77472db59485628e78272200d3164ef4dbb1156ed2ca065",
      "bytes": 1391
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "941cb96487325ca82c0ec05ec9ae9cec94b371dc19913ec4808a5b7f06db900a",
      "bytes": 1613
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "b11a9e1ce9250efb1f8bda200631c5b12e025a1603d362bb764984b1217cef30",
      "bytes": 1178
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "dc837ea526486f78366bcad40bf9c228eae7dc55bb6bef56c0fc871925275618",
      "bytes": 622
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "c7ed6041834f7dfdf85ecd5afa49c37be1a6c7c5e6f99eb8ec7dfd82a3244373",
      "bytes": 778
    },
    {
      "path": "characters/Peng Cheolhu.md",
      "sha256": "7ac3ba23f314216183777870250a5deca7cfdbf595dcf9671ba47dec4b475d49",
      "bytes": 1001
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "bd5753e5df794eedf5b2ea27975a392475eb9bba5427ebd9beecb42050b7771b",
      "bytes": 273611
    }
  ],
  "estimated_tokens": 12197
}
-->

# Durable State Update — Chapter 994

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
1 and safe_through 994. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 994. Profile updates may replace only one
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
  "chapter": 994,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 994,
    "continuity_sources": [994],
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
    "Taekyung has fully opened his Middle Dantian, reached the Supreme Peak realm, completed Bone Transformation, and absorbed the internal energy passed on by the Heavenly Power Demon and Peng Cheolhu.",
    "Taekyung is resolved to repay the dead by continuing to grow and helping bring about the peace they wanted; he now aspires to reach the upper dantian.",
    "A voice once spoke to Taekyung within his consciousness, said “That was a good decision. Just like back then,” and seemed to know him from before; Taekyung cannot identify it or remember its sound.",
    "The System has forced Taekyung to proceed with the Unknown Voice Quest.",
    "Whether any part of the original Jin Taekyung’s consciousness remains in Taekyung is unresolved; Taekyung and Jeok Cheongang intended to discuss the consciousness mystery privately.",
    "The Bow Saint may know part of the truth about the chosen one and remains in Hebei.",
    "Dark Heaven threatens the world; the Eight Heavens Blood Calamity and Peng Cheolhu’s death intensified mobilization against it.",
    "Unprecedented snowfall and rapidly changing heavenly patterns have been occurring around the world.",
    "Cheongpung is in Qinghai with the Slaughter Saint."
  ],
  "continuity_sources": [
    992,
    993
  ],
  "open_questions": [
    "Does any part of the original Jin Taekyung’s consciousness remain inside Taekyung?",
    "Who was the unknown voice, how did it communicate with Taekyung within his consciousness, and what was their earlier encounter?",
    "What is behind the worldwide weather and heavenly-pattern changes?",
    "What are Dark Heaven and the Lord of Heaven planning?",
    "What does the Bow Saint know about the chosen one?"
  ],
  "safe_through": 993,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 천태민    | **Cheon Taemin**  |
| 무신     | **Martial God**               | —              |
| 궁성     | **Bow Saint**                 | —              |
| 벽력도왕   | **Thunderbolt Saber King**    | Peng Cheolhu   |
| 삼성     | **Three Saints**    |
| 십왕     | **Ten Kings**       |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 시스템              | **System**                     |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 로그인              | **Login**                      |
| 로그아웃             | **Logout**                     |
| 길드      | **Guild**             |
| 산서     | **Shanxi**             |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 도플갱어 | **Doppelganger** | The Prophet’s revealed species. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 평화 | **Peace Guild** | Guild name. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 신력 | **divine strength** | Superhuman strength attributed to Taekyung. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 격체전공 | **Transmitting Internal Energy Across the Body** | Technique for transferring internal energy between bodies. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |
| 무한 | **Wuhan** | Capital of Hubei Province near Dongting Lake. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 호법 | **stand guard** | Mungyeong offers to protect Jeok during cultivation. |
| 은잠술 | **concealment technique** | Technique used by Hidden Shadow Pavilion agents to hide their presence. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 진위경 | 적천강 | host_to_legendary_guest | Great Hero Jeok | formal-deferential | Introduces himself and pays respects to Jeok Cheongang as the Fire King. |
| 적천강 | 진위경 | elder_to_younger_family_head | you | gruff and teasing | Uses 자네 while mistaking Wikyung for Taekyung’s father and questioning his age. |
| 적천강 | 벽력도왕 | rival_martial_master_to_rival_martial_master | Virility Saber King | insulting and taunting | Jeok coins 정력도왕 as a taunting replacement for the established title. |
| 벽력도왕 | 적천강 | rival_martial_master_to_rival_martial_master | Jeok Cheongang | boisterous and hostile-teasing | The Thunderbolt Saber King calls Jeok by name before their argument escalates. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 벽력도왕 | 진태경 | elder martial master to younger rival | you | boisterous and confrontational | Peng addresses Taekyung as 네놈 while discussing Peng Dojin. |
| 진태경 | 도플갱어 | enemy | you; the Doppelganger | blunt and informal | Jin directly challenges the Doppelganger and demands to know what it wants. |
| 도플갱어 | 진태경 | enemy | you | measured and informal | Replies to Jin’s taunt without using a name or title. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 진태경 | 벽력도왕 | younger martial artist to senior martial master | Great Hero Peng | formal and deferential | Taekyung offers a respectful salute and addresses Peng as 팽 대협. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 827
- **Aliases:** Slayer; Sky (the American epithet used for him)
- **Role:** Ares Guild Master and humanity's greatest Hunter, the Slayer who defeated the Demon King and created the first Mana Cultivation Method during the Great Cataclysm; after more than twenty years in seclusion, he remains unconscious in a secret area within Area A.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 993
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Doppelganger.md

# Doppelganger (도플갱어)

- **Safe through:** Chapter 843
- **Aliases:** The Final Abyss
- **Role:** The last surviving member of its species, the Doppelganger was a Demon Realm being capable of regenerating in new bodies and was erased by Jin Taekyung.
- **Personality:** Arrogant and manipulative, it treats others as tools and is willing to sacrifice its followers to escape, but becomes desperate when its own survival is threatened.
- **Voice:** It speaks with theatrical, grandiose confidence, taunting opponents in polished, self-important phrasing.
- **Relationships:** It claims to have served Demon King Asmodeus as its master and acted on his order, regarded Michael Silbert as a subordinate and disposable tool, and selected Yahya Muhammad Ahmad Bedouin to teach him magical power.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 991
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 993
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 992
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Peng Cheolhu regarded Taekyung as a worthy successor, inheriting all that Peng had to pass on; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 992
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm and politically capable, Jin Wikyung takes responsibility for his people and prioritizes their lives; he uses calculated leverage to keep dangerous allies in line and commits firmly to his principles, even when doing so means remaining in a losing battle.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Jin Wikyung is Taekyung’s eldest brother and future Family Head, protects and mentors him, and commands the Jin Family’s forces; Jin Mukyung is his younger brother, and he considers the Jin Family indebted to the Dongting Fisherman and the other fallen defenders of Shanxi.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 992
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 992
- **Aliases:** None
- **Role:** An unidentified legendary martial artist regarded as a pinnacle above the Ten Kings; more than fifty years ago, he defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, Mae Jonghak received several teachings from him, and he left the Bow Saint a letter describing a chosen one; the Bow Saint says he chose her, while his identity, whereabouts, and possible connection to Cheon Taemin remain unknown.

### Peng Cheolhu.md

# Peng Cheolhu (벽력도왕)

- **Safe through:** Chapter 993
- **Aliases:** Thunderbolt Saber King
- **Role:** Peng Cheolhu was the Thunderbolt Saber King, a Ten Kings master and Great Hero of the Hebei Peng Family who died as his accumulated internal energy and remaining life force melted into the flames of Taekyung’s advancement.
- **Personality:** Boisterous and teasing with old friends, yet calm and accepting in the face of death; willing to give everything he has left to protect the world.
- **Voice:** Loud, blunt, confrontational, and prone to disguising embarrassment or retreat as serious martial instruction.
- **Relationships:** He was Jeok Cheongang’s long-standing rival and friend, Hong Dao’s close friend, protective toward Hong Dao’s Disciple Unnamed, father of Peng Cheolyeong, and longtime friend and former youthful rival of Murong Baek; Jeok and Peng parted reconciled as brothers in all but blood.

## Korean source

```text
＃994화



시스템은 종종, 아니 어쩌면 꽤 자주 정확한 의미를 알 수 없는 단서를 퀘스트라는 이름으로 불쑥 내밀고는 한다.

바로 지금처럼.



퀘스트



[알 수 없는 목소리]



어느 날부터인가, 당신은 정체를 알 수 없는 누군가의 목소리를 인지하게 되었습니다.

이와 같은 일은 이번이 처음일 수도, 아닐 수도 있지만 한 가지는 확실합니다.

그리 머지않은 미래에, 당신은 목소리의 주인과 마주할 수 있을 것입니다.

그 만남의 순간이 부디 불행하지 않기를.



등급 : 無

제한 : 진태경

임무 : 계속해서 생존 (진행 중)

보상 : ???

실패 : ???





반투명한 홀로그램 창을 보자마자 든 생각은 한 가지뿐이었다.

‘또 지랄이네.’

거, 좀 명확하게 알려 주면 블루 스크린이라도 뜨나.

처음부터 끝까지 안개에 가려진 것처럼 모호한 설명들.

물론 이러한 퀘스트를 받은 것이 이번이 처음은 아니지만, 그것과는 별개로 도무지 익숙해질 수 없는 일이다.

하지만 동시에.

‘반드시 거쳐야 하는 과정이기도 하지.’

지금까지의 경험을 통해 알고 있듯이, 시스템은 답안지가 아니다.

나아가는 방향과 이 너머에 무엇이 있는지 정보를 알려 주는 표지판에 가깝다.

내 선택에 따라 표지판에 그려진 화살표의 형태가 변화하기도 하고, 때로는 지금처럼 해석해야 할 때도 있다.

그렇기에 나는 홀로그램 창 속의 글자를 읽고 또 읽었다.

스무고개와도 같은 저 글들에 숨겨진 의미를 파악하기 위해서.

그리고 그런 의미에서, 퀘스트 설명란에 적힌 마지막 두 문장은 내 눈길을 끌기에 충분했다.

‘그 알 수 없는 목소리의 주인과 만날 수 있다고? 그것도 머지않은 미래에?’

머지않은, 이라.

시간이 상대적인 것임을 생각한다면 매우 모호한 표현이다.

코흘리개 어린아이에게 있어 일 년이라는 시간은 길고도 아득하지만, 백발이 성성한 노인에게는 찰나와 다름없을 테니까.

그렇기에 나로서는 시스템이 말하는 저 ‘머지않은’ 미래가 어느 정도의 시간을 말하는지는 짐작하기 어려웠다.

며칠. 몇 달. 혹은…… 아니다. 아무리 양심이 없어도 몇 년이나 되는 시간을 저렇게 뭉뚱그려 놓지는 않았겠지.

‘당장 며칠은 너무 빠르고, 년 단위는 너무 길 테니 결국은 몇 달 안에 벌어질 일이라고 이해하는 게 합리적인데.’

그렇다면 불행 운운하는 마지막 문장은 뭘까.

그리고 이처럼 수수께끼와 같은 퀘스트의 원인이나 다름없는, 그 알 수 없는 목소리의 주인은 도대체 누구일까.

‘나와 벽력도왕, 심지어 노야의 이목마저 속이고 가까이 접근할 수 있는 사람. 나만의 심상(心想)에 개입할 수 있을 정도의 누군가.’

격체전공(隔體傳功)이 이루어지는 상황에서 나와 벽력도왕은 기운을 건네주고 받는 것만으로도 벅찼지만, 적천강은 달랐다.

그는 이 위험하기 짝이 없는 대법을 위해 호법을 섰고, 그런 만큼 온 힘을 다해 감각을 곤두세우고 있었다.

그런데 그런 그의, 이제는 십왕(十王)을 넘어 세 명의 별들과 어깨를 나란히 하는 초절정 고수의 이목을 피해서 내게 목소리를 전한다는 건 불가능하다.

아니, 엄밀히 말하자면 완전히 불가능한 건 아닐 것이다.

‘전무후무한 수준의 은잠술을 익힌 고금제일의 살수거나, 노야보다 최소 두 수 이상 앞서는 고수라면.’

그리고 내가 아는 한, 이 최소한의 조건을 충족시킬 수 있는 인물은 천하에서 단 두 명뿐이다.

그중 전자에 해당하는 이는 고금제일의 살수임은 분명하나 이런 짓을 벌일 만한 이유도, 성공 가능성도 확신할 수 없다.

하지만 또 다른 한 명은 다르다.

온 세상의 경이(驚異), 그 자체.

홀로 이 광활한 천하를 굽어보는 하늘이자, 인간의 몸으로 신이라 불리게 된 존재.

“……무신(武神)?”

나도 모르게 입술을 비집고 흘러나온 그 두 글자에, 순간 등골이 찌르르 울렸다.

무신. 바로 그 무신이라니.

‘그럴 리가 없어.’

무신이 자취를 감춘 지 무려 반세기다.

그는 처음 세상에 나타났을 때와 같이 홀연히 떠났고, 이제는 천하의 그 누구도 무신의 행방을 알지 못한다.

아니, 이제는 생사의 여부조차 확신할 수 없다.

이는 무신이 남긴 서신을 통해 나를 찾아낸 궁성조차도 마찬가지.

그런데 이렇게 갑작스럽게 자신의 존재를 드러낸다?

‘말도 안 돼.’

하지만 현실적으로 오늘과 같은 일이 가능한 것은 무신뿐이다.

내가 아는 한, 오직 그만이 이른바 삼성(三星)이라 불리는 초인들을 넘어선 압도적인 존재니까.

그리고 어쩌면 나는, 천하의 그 누구보다 무신이라는 존재에 감춰진 진실을 알고 있는 유일한 사람일지도 몰랐다.

‘만약 내 짐작이 사실이라면…….’

불현듯 스쳐 지나가는 어떤 생각에, 가슴이 거세게 뛰었다.

황궁에서 처음으로 나누었던 궁성과의 깊은 대화.

이후 정신없이 흘러가는 시간 속, 마음 한구석에서만 홀로 만지작거릴 수밖에 없었던 한 사람의 이름이 내 뇌리를 가득 채웠다.

‘천태민.’

아득한 공간 너머에 존재하는 또 한 명의 절대자.

천마(天魔)에 맞서 평화를 되찾은 무신이 그러했듯, 마왕 아스모데우스라는 악마로부터 인류를 구원한 영웅.

아레스 길드의 비밀구역에서 마법과 과학이 결합된 생명 유지 장치를 단 채, 깊은 잠에 빠진 듯 의식을 잃은 그의 모습이 아직도 눈앞에 선했다.

그 위로 흐릿하게 겹쳐지는, 한 여인의 목소리 역시도.



‘선택받은 자를 위해 남기신 전언(傳言)이 있다.’

‘전언이라니, 그게 무슨.’

‘신력(神力). 선택받은 자가 지닌 그 신력과 강철과도 같은 의지로 위기를 헤쳐나가라 하셨지. 바로…….’



그날, 나를 응시하는 궁성의 눈빛은 깊게 가라앉아 있었다.

뒤이어 메아리처럼 아득하게 귓가를 울렸던 그 음성도.



‘바로, 당신께서 그러하셨듯이.’



그 순간에 느꼈던 충격을, 지금도 또렷하게 기억한다.

아니, 분명 죽을 때까지 잊지 못할 것이다.

흘러가는 시간 속에서 어렴풋이 생각하면서도 이내 실소와 함께 고개를 저었던, 생각지도 못한 퍼즐이 끼워 맞춰진 순간이었으니까.

신력.

선택받은 자만이 지닌 괴이한 힘.

지금의 내게, 그리고 과거의 무신에게 깃들었던 이능(異能).

만약 무신이 궁성에게 남긴 전언이 내가 생각하는 그것이 맞다면, 이는 곧 단 한 가지 사실만을 의미했다.

‘시스템 사용자. 플레이어(Player).’

아마도 그것이 바로 무신의 진정한 정체일 것이다.

어느 날 홀연히 나타나 도탄에 빠진 천하를 구한 뒤 사라진, 전에도 없었고 과거에도 나타나지 않을 불세출의 대영웅에게 숨겨진 진실.

그러나 만약 이 가설이 사실이라면…….

‘천태민과 무신은, 결코 동일 인물이 될 수 없다.’

캡슐 사용 설명서에 따르면 시스템은 오직 단 한 사람에게만 허락되는 힘.

거기에까지 생각이 미친 순간, 나는 불현듯 찾아온 두통을 느꼈다.

각각 다른 세상에 존재하는 두 영웅.

그들이 보인 행적은 놀라울 만큼 서로를 닮아있었고, 두 사람에 대해 알아 갈수록 나 역시 어렴풋이 떠올리곤 했다.

어쩌면 천태민이, 혹은 무신이 나와 같은 능력을 지녔을지도 모른다고. 그 두 사람이 동일 인물일지도 모른다고.

하지만 이제는 모르겠다.

무신과 천태민 사이에 어떠한 연관성이 있는지.

하나가 아닌 전혀 다른 개인으로서 존재한다면, 그들이 무슨 진실을 감추고 있는 것인지.

다만 지금 이 순간에도 바늘처럼 뇌리를 쑤시는 이 두통을, 의혹을 조금이라도 해결할 방법만큼은 확실히 알고 있었다.

‘돌아간다. 바로 지금.’

그래.

답은 한 곳에서만 찾을 수 있는 것이 아니다.

현대와 무림.

도무지 설명할 수 없는 힘으로 이어진 두 세계에서, 나는 이 의문에 대한 명확한 답을 찾아내야 한다.

그리고 지금이야말로 더할 나위 없는 적기(適期)다.

산서성의 위기에 관한 중요 퀘스트도 완료했고, 그로 인해 막혀있던 로그아웃 기능 역시 자유로워졌으니까.

‘한 달. 혹은 두달. 그 정도면 충분하겠지.’

천태민에 관해서도 자세히 알아보려는 목적 뿐만이 아니다.

당장 로그인 직전 벌어졌던 도플갱어 사건의 후폭풍도 처리해야 한다.

더군다나 놈이 소멸하기 전 남겼던 의미심장한 말들은 또 다른 후환(後患)을 암시하고 있어, 무림에서 숨 가쁜 시간을 보내는 와중에도 목에 걸린 생선 가시처럼 마음을 불편하게 만들고 있던 차였다.

‘돌아가면 알 수 있겠지. 도플갱어가 왜 그런 말을 남긴 것인지. 무엇을 위해 그렇게까지 했는지.’

결정이 내려졌으니 망설임도 없다. 나는 침상에 곧게 누워 이불을 목까지 끌어올렸다.

설령 현대에서 두어 달을 보낸다 하더라도 무림에서는 기껏해야 세 시진 남짓한 짧은 시간.

창밖 저 멀리에서부터 빠르게 가까워지는 인기척이 누구의 것인지는 모르지만, 침소에 도착한 그가 마주할 수 있는 것은 이미 현대로 떠난, 아니 깊이 잠들어 있는 내 모습일 것이다.

‘로그아웃.’

그리고 천천히 눈을 감으며 익숙한 명령어를 읊은 다음 순간, 나는 깨달았다.

이 세상에는, 예상대로 흘러가지 않는 일도 있다는 것을.

삐비비빅!



- [로그아웃]이 실패했습니다!

- [시스템]이 당신의 [로그아웃] 명령어를 거부합니다!

- Error! Error!

- 시스템 오류로 인하여, 일시적으로 [로그아웃] 기능이 비활성화됩니다!

- 알 수 없는 오류! [임시 점검]이 시작됩니다!



……뭐라고?

순간, 나도 모르게 감겼던 눈이 부릅떠졌다.

그러나 귓가를 파고든 시스템 음성도, 허공에 떠오른 수십여 개의 에러 메시지도 변하지 않았고 나는 극심한 혼란에 사로잡혔다.

‘로그아웃 거부라니, 도대체 어째서?’

지금까지 단 한 번도 존재하지 않았던 일이다.

아니, 있었긴 했지만 그건 중요한 퀘스트를 진행 중이었을 때뿐이었고 그마저도 이런 방식은 아니었다.

‘시스템 오류? 임시 점검?’

업데이트라면 모를까. 그런 건 듣도 보도 못했다.

언제나 절대적이었던 시스템에 오류라니, 말도 되지 않는 일 아닌가.

“이게 무슨……!”

본능처럼 입술을 비집고 흘러나오는 신음. 입술을 질끈 깨문 나는 마음속으로 쉼 없이 소리쳤다.

‘로그아웃! 로그아웃!’

그러나 변하는 건 없었다.

아무것도.

연달아 이어진 명령어와 함께 우수수 쏟아져 나온 홀로그램 창에는 시스템 오류라는 글자만 선명했고, 이 믿을 수 없는 현실 앞에서 내가 할 수 있는 건 그저 멍하니 상황을 받아들이는 것뿐이었다.

아니, 굳이 꼽자면 할 수 있는 것이 하나 더 있었다.

어느새 문 앞까지 가까워진 인기척의 주인이 침소로 들어오기 전, 한발 앞서 그가 불청객임을 인지시켜 주는 것.

“들어오지 마. 나 지금…… 빌어먹을. 아무튼 바쁘니까.”

볼 것도 없이 혁무진이라고 생각했고, 녀석이 아니라면 화룡각 대원 중 한 사람일 거라 생각했다.

하지만 그런 내 예상은 조금 전 로그아웃을 시도했을 때처럼 보기 좋게 빗나갔다.

달칵.

“한 핏줄이라 그런지, 이런 것까지 통하는구나.”

다음 순간 망설임 없이 문을 열고 들어온 불청객. 아니 진위경의 표정은 무겁게 가라앉아 있었다.

그를 바라보는 내 등골이 서늘해질 만큼.
```

## Final English reading copy

```markdown
# Chapter 994

The System often—no, maybe pretty frequently—sprang cryptic clues on me in the form of Quests, their meaning impossible to pin down.

Just like now.



> **System**
> **Quest**
>
> **Unknown Voice**
>
> At some point, you became aware of the voice of someone whose identity you cannot determine.
>
> This may or may not be the first time this has happened, but one thing is certain.
>
> In the not-too-distant future, you may come face-to-face with the owner of that voice.
>
> May that moment of meeting not be an unhappy one.
>
> **Grade:** None
>
> **Restriction:** Jin Taekyung
>
> **Objective:** Continue to survive (In progress)
>
> **Reward:** ???
>
> **Failure:** ???



The moment I saw the translucent holographic window, only one thought came to mind.

*Here we fucking go again.*

What, would the screen go blue if it gave me a straight answer?

Vague explanations from beginning to end, as if they were shrouded in fog.

Of course, this wasn’t the first time I’d received a Quest like this. That didn’t make it any less impossible to get used to.

But at the same time—

*This is a process I have to go through.*

As I knew from experience, the System wasn’t an answer sheet.

It was more like a signpost, pointing me in a direction and telling me what lay beyond.

Depending on my choices, the arrows on the sign might change. Sometimes, like now, I had to interpret them myself.

So I read the words in the holographic window again and again.

Trying to figure out the meaning hidden in those twenty-questions-style clues.

And in that regard, the last two sentences in the Quest description were more than enough to catch my eye.

*I might meet the owner of that unknown voice? And in the not-too-distant future?*

Not too distant, huh.

Time was relative, so that was a pretty vague way to put it.

A year could feel like an eternity to a little kid with a runny nose, but to a white-haired old man, it might be no more than a fleeting moment.

So I had no way of guessing how much time the System meant by “not too distant.”

A few days. A few months. Or… No. Even the System couldn’t be so shameless as to call it “not too distant” if it meant years.

*Days would be too soon, and years would be too long. It makes sense to take it as something that’ll happen within a few months.*

Then what was that last line about it not being an unhappy moment?

And who on earth was the owner of that unknown voice—the very person who’d brought about this riddle of a Quest?

*Someone who could approach me without being noticed by me, the Thunderbolt Saber King, or even the Old Master. Someone who could intrude into my private inner world.*

When Transmitting Internal Energy Across the Body was taking place, the Thunderbolt Saber King and I were too busy giving and receiving energy to do much else. But Jeok Cheongang was different.

He’d stood guard for this dangerous technique, and he’d been straining every sense he had.

It should’ve been impossible to evade his notice and speak to me—especially when he was a Supreme Peak master who now stood shoulder to shoulder with the Three Saints, beyond even the Ten Kings.

Well, strictly speaking, it wasn’t completely impossible.

*If they were the greatest assassin of all time, with a concealment technique without precedent, or a master at least two moves ahead of the Old Master…*

And as far as I knew, only two people in the world could meet even those minimum requirements.

The first was undoubtedly the greatest assassin of all time, but I couldn’t think of a reason they’d do something like this—or be sure they could pull it off.

But the other one was different.

A wonder of the entire world.

The sky itself, looking down over this vast land alone. A being who, though born human, had come to be called a god.

“……The Martial God?”

The two syllables slipped from my lips before I realized it. A shiver ran down my spine.

The Martial God. The Martial God himself?

*That can’t be right.*

It had been half a century since the Martial God disappeared.

He’d vanished as suddenly as he’d appeared in the world, and no one under heaven knew where he was now.

No one could even say for sure whether he was alive or dead.

Not even the Bow Saint, who’d found me through the letter the Martial God had left behind.

And now he’d suddenly reveal his presence like this?

*No way.*

But realistically, the only person who could’ve done something like this was the Martial God.

As far as I knew, he alone was an overwhelming presence beyond the superhumans known as the Three Saints.

And perhaps I was the only person under heaven who knew more than anyone else about the truth hidden behind the Martial God.

*If my guess is right…*

A thought flashed through my mind, and my heart began to pound.

The first deep conversation I’d had with the Bow Saint at the Imperial Palace.

Amid the hectic days that followed, the name of someone I could only turn over in the back of my mind filled my thoughts.

*Cheon Taemin.*

Another absolute being who existed beyond a distant space.

Just as the Martial God had opposed the Heavenly Demon and restored peace, he was a hero who’d saved humanity from the demon known as the Demon King Asmodeus.

I could still see him clearly: unconscious, seemingly deep asleep, hooked up to a life-support system combining Magic and science in the Ares Guild’s restricted area.

And over that image, the voice of a woman faintly overlapped.



*“He left a message for the chosen one.”*

*“A message? What does that mean?”*

*“Divine strength. He said the chosen one should overcome the crisis with that divine strength and a Will like steel. Just as…”*



That day, the Bow Saint’s eyes had been fixed on me, deep and solemn.

And then, that voice had echoed faintly in my ears like a distant refrain.



*“Just as you did.”*



I still remembered the shock I’d felt in that moment.

No—I’d never forget it, even on my deathbed.

A piece of a puzzle I’d never imagined suddenly falling into place, after I’d turned it over vaguely in my mind and then laughed it off.

Divine strength.

A strange power possessed only by the chosen one.

The supernatural ability that belonged to me now—and to the Martial God in the past.

If the message the Martial God had left the Bow Saint was what I thought it was, that could mean only one thing.

*System user. Player.*

That was probably the Martial God’s true identity.

The truth hidden behind an unparalleled hero the likes of whom had never been seen before, and would never be seen again: a man who’d appeared out of nowhere, saved a world in turmoil, then disappeared.

But if that theory was true…

*Cheon Taemin and the Martial God can’t possibly be the same person.*

According to the capsule’s user manual, the System was a power granted to only one person.

The moment I reached that thought, a headache came over me.

Two heroes from separate worlds.

Their actions were astonishingly alike, and the more I learned about them, the more I found myself wondering whether Cheon Taemin or the Martial God might have had the same ability as me.

Whether the two of them might be the same person.

But now I didn’t know anymore.

What connection, if any, existed between the Martial God and Cheon Taemin.

If they were two entirely different people, not one and the same, what truth were they hiding?

I did know one thing: there was a way to resolve even a little of this doubt, this headache that was still stabbing my mind like a needle.

*I’m going back. Right now.*

That’s right.

There wasn’t just one place to find the answer.

In the modern world and Murim—in two worlds connected by a power I couldn’t begin to explain—I had to find a clear answer to this question.

And right now was the perfect time.

I’d completed the important Quest concerning the crisis in Shanxi Province, and the Logout function that had been blocked because of it was free again.

*One month. Maybe two. That should be enough.*

And it wasn’t just to learn more about Cheon Taemin.

I also had to deal with the fallout from the Doppelganger incident, which had happened right before I last Logged In.

On top of that, the ominous words it left behind before it vanished hinted at more trouble to come. Even with all the frantic activity in Murim, they’d been bothering me like a fish bone stuck in my throat.

*I’ll find out when I get back. Why the Doppelganger said those things. What it was willing to go that far for.*

Now that I’d made up my mind, there was no hesitation. I lay straight on the bed and pulled the covers up to my neck.

Even if I spent a couple of months in the modern world, only about three shichen would pass in Murim.

I didn’t know whose presence was hurrying toward me from somewhere in the distance beyond the window, but by the time they reached my room, all they’d find would be me already gone to the modern world—or, well, fast asleep.

*Logout.*

I slowly closed my eyes and recited the familiar command. The next moment, I realized something.

Some things in this world didn’t go the way you expected.

Bip-bip-bip!



> **System**
> Logout failed!
>
> The System has rejected your Logout command!
>
> Error! Error!
>
> Due to a System error, the Logout function has been temporarily disabled!
>
> Unknown error! Temporary Maintenance has begun!



……What?

My eyes flew open, even though I hadn’t meant to open them.

But neither the System’s voice that had pierced my ears nor the dozens of error messages floating in the air changed. I was thrown into utter confusion.

*Logout rejected? Why on earth?*

This had never happened before.

No—it had happened before, but only when I was in the middle of an important Quest, and even then it hadn’t happened like this.

*System error? Temporary maintenance?*

An update, sure. But I’d never heard of anything like that.

An error in the System, which had always been absolute? How could that be possible?

“What the…!”

A groan slipped from my lips on instinct. I bit down hard and shouted over and over in my mind.

*Logout! Logout!*

But nothing changed.

Nothing at all.

The holographic windows that poured out with every command showed only the words “System error.” Faced with this unbelievable reality, all I could do was stare blankly and take it in.

Actually, if I had to name one more thing I could do, it was let the person whose presence had drawn close to the door know that he was an unwelcome guest before he entered my room.

“Don’t come in. I’m… damn it. Anyway, I’m busy.”

Without even looking, I assumed it was Hyuk Mujin. If it wasn’t him, I figured it had to be one of the Fire Dragon Pavilion members.

But my guess was just as spectacularly wrong as I’d been when I tried to Logout.

Click.

“Must be because we’re brothers. Even on this, we’re of one mind.”

The next moment, the unwelcome guest opened the door without hesitation. No—it was Jin Wikyung, his expression heavy and grave.

The sight of him sent a chill down my spine.
```
