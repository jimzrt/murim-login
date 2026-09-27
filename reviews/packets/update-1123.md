<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1123.txt",
      "sha256": "fd640e7233d0b1218beb71321ef0f6ce25686dfec4ad45b0bcf9511f18cf9d82",
      "bytes": 15744
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "d04cfaca6e034336482533fab296173244538ebff67388f2a484bbe7da119a2b",
      "bytes": 1575
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "307189767337c5394589bdcaa7f59f3e28cdf1da9d380fecae4d63447025be4b",
      "bytes": 245178
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "22efd7ac1f7574bb25eb92dfe4eaf58c0f119a3a70d7e4cde68b2a166ec468de",
      "bytes": 944
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "8d9f075ace9e72019f31c175a06b11557fad9d169b40d521882487345430c721",
      "bytes": 1230
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "00fd5cffc43d8184e1b90658d74baf79d8af701ece1d763f340ef3a6ae02095e",
      "bytes": 760
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "09ce596ce5f934cc89ede01c93058705f552b5f27d199589241bb483b65ab22b",
      "bytes": 1357
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "d2fd961d911fea9e6206216080b9a367567efa43223993cf4372e463767653ab",
      "bytes": 1513
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "9b644eb29fb72fc0ebc957e4e93bf62664e528b652074003b550dd4fe7be3e5a",
      "bytes": 850
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "c7b5ad003c69b38df994244f3ea3a57cf41b38d6e19ec7087d5aa02ef6240e3b",
      "bytes": 774
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "e7e37c7e9a413bbdd3ee1938d7d33ebcc2f2df32224cd4ccc20068522e048696",
      "bytes": 980
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "fa727e06f38fa0b22cdccc46176be46ed0fd3383a8c574d097c0fd4f924742a3",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "fbe26e0ec5f89ce57df0b052ec3ff3869882eaa7728f4db5939e2d5122fb744c",
      "bytes": 289919
    }
  ],
  "estimated_tokens": 14100
}
-->

# Durable State Update — Chapter 1123

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
1 and safe_through 1123. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1123. Profile updates may replace only one
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
  "chapter": 1123,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1123,
    "continuity_sources": [1123],
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
    "The East Gate has fallen; the Inner City is under siege.",
    "About five thousand exhausted defenders face tens of thousands of fanatics at the Inner City.",
    "Civilians have joined the battle to protect the defenders, carrying crude bamboo spears and rusty axes.",
    "Jin Taekyung is critically wounded; the Slaughter Saint’s warning suggests he may be dying, though he briefly wakes.",
    "Jeok Cheongang, the Slaughter Saint, the Bow Saint, and Cheongpung are fighting at the Inner City.",
    "An unidentified, immensely powerful man or monster is approaching the defenders.",
    "The Blood Lord is present on the battlefield and reacts with laughter to the approaching figure and civilians.",
    "Hyuk Mujin was struck in the chest and collapsed; his condition remains unknown.",
    "The black-robed figure confronted Cheongheoja at the East Gate; the outcome remains unknown.",
    "The Slaughter Saint and Bow Saint fought the Grand Mage and Black Ghost during the retreat; Black Ghost’s status remains unknown."
  ],
  "continuity_sources": [
    1121,
    1122
  ],
  "open_questions": [
    "Will Jin Taekyung survive his injuries?",
    "Who is the powerful figure approaching the defenders?",
    "Will Hyuk Mujin survive his chest wound?",
    "What happened to Cheongheoja and the black-robed figure at the East Gate?",
    "What happened to Black Ghost?"
  ],
  "safe_through": 1122,
  "temporary_decisions": [
    "Render 부각주 as “Vice Captain” when Taishan addresses Hyuk Mujin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 송일     | **Song Il**        |
| 궁성     | **Bow Saint**                 | —              |
| 살성     | **Slaughter Saint**           | —              |
| 삼성     | **Three Saints**    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 용봉표국   | **Yongbong Escort Bureau**       |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 낭인     | **wandering martial artist**                     |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 기루     | **pleasure house**                               |                                                       |
| 수문조장   | **Captain of the Gatekeepers**               |
| 표국     | **Escort Bureau**                            |
| 제자     | **Disciple**                                 |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 태원     | **Taiyuan**            |
| 감숙     | **Gansu**              |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 소저      | **Young Lady**                                                  |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 회광반조 | **final rally** | Terminal burst of apparent vitality before death. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 광염 | **light-flames** | Violet manifestation surrounding Cheongpung when he uses the Zaha Divine Technique. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 유엽도 | **willow-leaf saber** | Saber wielded by Song Ilseom. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 우모침 | **ox-hair needle** | Extremely fine Tang Clan hidden weapon. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 무한 | **Wuhan** | Capital of Hubei Province near Dongting Lake. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 화원 | **Fire Courtyard** | Courtyard associated with Jin Taekyung and Ju Hwaran's final walk before leaving Sichuan. |
| 상산후 | **Marquis of Shangshan** | Title bestowed on Jin Taekyung by the Emperor. |
| 흑귀 | **Black Ghost** | The Blood-Sword Demon Lord’s name for the Death Knights. |
| 적도 | **Red Blade** | Named blade that shatters in Taekyung’s flames. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 송일 | 청풍 | hostile Zhongnan Elder to younger martial artist | Sword Saint's heir / you | hostile and threatening | Song Il identifies Cheongpung as the Sword Saint's heir and demands that he face the consequences of injuring Gong Ilhyuk. |
| 송일 | 적천강 | former rescued junior to former rescuer | Great Hero Jeok | formal, fearful, and defensive | Uses 적 대협 while insisting that Jeok has no business interfering in the dispute. |
| 적천강 | 송일 | former rescuer to former rescued junior | Zhongnan brat; you; insolent bastard | blunt, mocking, and humiliating | Jeok recalls Song's youthful arrogance and addresses him with contempt while publicly disciplining him. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 혈주 | 청풍 | hostile_opponent_to_newly_revealed_identity | Huashan's Invincible Divine Sword; Sword Saint's Disciple or grandson | mocking and taunting | Recognizes Cheongpung's public identity and needles him with his Sword Saint lineage while dismissing the added threat. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 혁무진 | 송일섬 | pavilion_member_to_escort_captain | Great Hero Song | formal and deferential | Mujin addresses Song Ilseom while commenting on his broad experience. |
| 송일섬 | 사마표 | fellow_pavilion_member_to_hostile_fellow_member | you | hostile and casual | Song Ilseom discusses fighting Sama Pyo and answers him while preparing to move away. |
| 사마표 | 송일섬 | fellow_pavilion_member_to_hostile_fellow_member | you | controlled and antagonistic | Sama Pyo responds to Song Ilseom's accusations and proposes moving aside to fight. |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 사마표 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | formal but sardonic | Sama Pyo addresses Jin as 각주 while questioning his account of the incident. |
| 태산 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | clipped, childlike, and informal | Taishan directly asks Jin whether his Lord Sama Pyo is safe. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 살성 | 청풍 | senior martial figure to younger companion | you | blunt and familiar | The Slaughter Saint scolds Cheongpung for disappearing without a word. |
| 청풍 | 살성 | younger companion to senior martial figure | old man | polite and familiar | Cheongpung apologizes and explains why he wandered off. |
| 송일섬 | 혁무진 | Older fellow Pavilion member and martial senior | you | casual and informal | Song insists that his age and martial experience entitle him to speak casually to Mujin. |
| 궁성 | 살성 | allied martial masters | Slaughter Saint | formal-polite | The Bow Saint directly addresses him as 살성 and uses 당신 while urging him to stay and defend the South Gate. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1122
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure and formidable combatant who commands weapons telekinetically and absorbs blood to restore vitality; after killing the Grand Mage, he claims command of the Dark Heaven army.
- **Personality:** Cunning and controlling, he plans around opponents’ strengths and trusts his overwhelming power; his newly unrestrained madness leads him to defy the Lord of Heaven’s will and seize command for himself.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He has served the Lord of Heaven but now openly defies his will; he is fixated on killing Jin Taekyung, killed the Grand Mage, and recognizes Cheongpung from his connection to Sword Saint Mae Jonghak.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 1122
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, Sword Saint Mae Jonghak’s grandson and Disciple, a Supreme Peak master known as the Huashan Divine Dragon, creator of Mimi Step, and master of the Azure Dragon Pavilion; he has mastered the Slaughter Saint’s Ghost Illusory Slaughter Step and blended it with his Dark Fragrance Drift.
- **Personality:** Affable, dreamy, and childlike, with innocent curiosity, a deep love of martial arts, and compassion; guided by his grandfather’s righteousness and Taekyung’s chivalry, he meets danger with resolve and trusts Taekyung without wavering.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions; Taekyung is his true martial rival and the person whose way of life he admires, and the Slaughter Saint is his mentor in concealment and Ghost Illusory Slaughter Step.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1122
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1120
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and Vice Captain of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, whom he deeply admires, and has developed a warm friendship with fellow Fire Dragon Pavilion member Taishan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1122
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and freely follows his own path rather than pursuing grand causes; he cares about protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1120
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader and heir of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Courteous and calculating, he chooses what he believes is right over expedience and accepts responsibility for his choices, even when they expose him to blame.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo is Sima Gong’s son and chosen heir, commands Taishan, and is Jin Taekyung’s friend; he deliberately let Namho suspect his father’s actions to protect their companions, was Ju Hwaran’s former fiancé, and is hostile toward Song Ilseom.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 1120
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect, known as the Roaring Fury Swordsman and one of Sect Leader Gong Iljung’s two Senior Brothers.
- **Personality:** Arrogant and domineering, but capable of remorse over choices that harmed his sect and those he failed to protect.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 1120
- **Aliases:** Escort Captain Song
- **Role:** Song Ilseom is a Level 110 escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Direct and rough, with dry, matter-of-fact teasing among allies and forceful urgency in command.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1120
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃1123화



“네 녀석……!”

격동으로 파르르 떨리는 익숙한 목소리를 들으며, 나는 참았던 숨을 토해 냈다.

천천히 눈을 깜빡이고, 입안에 고여 있는 핏물을 삼켰다.

난생처음 느껴 보는, 이상한 기분이었다.

영원히 빠져나올 수 없는 꿈속에 갇힌 것처럼 몽롱하기도 하고, 한편으로는 주위의 모든 것이 선명하게 전해지기도 했다.

그리고 내가 태어나 처음으로 맞닥트린 이 낯선 감각의 정체에 대하여, 시스템은 늘 그렇듯 확실한 대답을 내놓았다.

더없이 친절하면서도 잔인한, 특유의 방식으로.

삐빅.



- 상태 이상, [회광반조]가 부여됩니다.



회광반조(回光返照).

해가 지기 직전 강하게 비쳐 오는 햇살처럼, 어두워지는 삶의 끝자락에서 타오르는 최후의 불꽃.

‘이런 느낌이었나.’

문득 떠올렸다.

지금껏 이 두 손으로 직접 쓰러트린, 혹은 간절히 붙잡았음에도 떠나보낼 수밖에 없었던 이들의 마지막 모습을.

그런 그들에게서 엿보았던 무수한 감정들을.

이제야 비로소, 그 모든 것들을 이해할 수 있을 것 같았다.

서서히 드리워지는 죽음을 기다렸던 그들과 달리, 나는 죽음을 향해 달려갈 수밖에 없는 놈이라는 사실도 함께.

띠링.



- [회광반조]는 신의 자비이자 인간의 의지이며, 지나온 삶을 반추할 수 있는 촛불입니다. 비록 타오르는 시간은 짧을지언정, 그 찰나의 빛은 죽음마저 잊을 만큼 밝을 것입니다.



이번만큼은 차갑고 거친 경고음이 아니다.

더없이 익숙한 맑은 종소리가 귓가를 울리고, 끝없이 어둠 속으로 곤두박질치던 몸과 마음을 일깨운다.

시스템이 말했던 것처럼, 죽음마저 잊게 만드는 환한 빛으로.



- 상태 이상, [회광반조]의 지속 시간 동안 당신이 느끼는 모든 고통이 급감합니다.



시시각각 조여 오는 고통과 죽음에 신음하던 육신의 떨림이 멎고.



- [기감]이 일시적으로 대폭 상승합니다.



식어 가던 정신의 잿더미에서 불씨가 타올랐으며.

화아아악.

불현듯 등줄기를 파고든 따스한 열기와 함께, 부풀어 오른 불씨는 화염이 되었다.



- [열양지기]가 당신의 지친 육신을 보듬고, 일부 내상을 치유합니다.



두 개의 불길은 공존할 수 없다.

언젠가는 부딪히고, 공멸한다.

그러나 하나의 뿌리에서 비롯되었다면, 그것은 본래 한 몸이나 다름없다.

그 자신부터가 심각한 내상을 입었음에도, 망설임 없이 내게 기운을 나누어 준 누군가처럼.

“무엇하느냐.”

백지장처럼 새하얗게 질린 안색. 전신 곳곳에 아로새겨진 크고 작은 상처들과 잘게 떨리는 신형.

하지만 그는, 적천강은 나를 향해 웃고 있었다.

당신의 제자가 잠시나마 기운을 차렸다는 기쁨과 그 사실이 무엇을 의미하는지에 대한 슬픔을 애써 억누르며.

“어서 가자. 함께.”

그 순간.

띠링.



- 돌발 퀘스트, [바람 앞의 촛불, 혹은 불꽃]이 생성되었습니다!

- 죽음이 당신을 기다립니다. 해당 퀘스트를 거부할 수 없습니다!



제한 시간 : 9분 59초



멈춰 있던 시간이 흐름과 동시에, 나는 백염(白炎)을 힘주어 잡고 걸음을 내디뎠다.

아직 끝나지 않은 악몽 속으로.

아니, 악몽보다 더한 이 현실을 향해.

‘뒤바꾼다. 반드시.’

혼자만의 싸움이었다면 이미 포기했을지도 모른다.

시체 더미에 지친 몸을 기댄 채, 지나간 시간을 되새기며 서서히 드리워지는 죽음을 기다렸을 수도 있다.

하지만.

슈확!

지금의 나는, 혼자가 아니다.

콰아아앙!

적들을 집어삼키는 눈부신 광염(光焰).

불그스름하게 달아오른 대지와 공간을 일그러트리는 아지랑이 속, 불의 거인이 포효한다.

그와 동시에 살성이, 궁성이, 청풍과 최후의 결사대가.

더불어 헤아릴 수도 없이 수많은 백성이 그 뒤를 따라 파도처럼 나아갔다.

더 이상 악에 받친 함성이 아닌, 생각지도 못한 누군가의 이름을 부르짖으며.

“돌격! 돌격하라! 상산후(上山侯)를 지켜라!”

“……!”

거대한 외침이 전장을 뒤흔들며 귓가에 닿은 그 순간, 벼락과도 같은 한 줄기의 전율이 등줄기 타고 솟구쳤다.

지킨다고 했다.

다른 누구도 아닌 나를.

한 줌의 공력이나 제대로 된 무기조차 없는, 낫과 곡괭이를 손에 쥔 저들이.

내 사람들조차 제대로 지켜 내지 못한 나를 위해, 자신들의 목숨을 걸고 싸우고 있었다.

‘그래, 끝내 지키지 못했지. 너희를.’

불현듯 눈앞을 스치는, 이제는 두 번 다시 볼 수 없게 되어 버린 그리운 얼굴들을 떠올리며 나는 광신도들을 향해 쏘아졌다.

쐐애액!

발끝. 허리. 어깨. 팔과 손목.

무수한 반복과 실전을 거쳐 본능처럼 각인된 움직임을 따라, 거세게 휘몰아치던 비바람이 갈라진다.

서걱!

서늘하게 공간을 가로지른 한 줄기의 절삭음.

그와 동시에 부릅떠진 십여 쌍의 눈동자.

도저히 믿을 수 없다는 듯, 불신 어린 시선으로 나를 바라보던 광신도들이 갈라진 목젖을 움켜잡은 채 허물어진다.

흐릿한 열기가 실린 백염(白炎)의 창날은 평소와는 비교도 할 수 없을 만큼 느리고 약했으나, 그 방향 끝에 기다리고 있는 적들은 어째서인지 제대로 반응하지 못했다.

그리고 그것은, 죽은 동료의 빈자리를 채우며 밀려드는 또 다른 적들 역시 마찬가지였다.

푸푹! 우드득!

나는 막아서는 모든 것을 찌르고, 뽑고, 비틀었다.

시야는 여전히 몽롱했으나, 감각은 그 어느 때보다 선명하다.

자욱하게 맺혀 가는 피 안개 속에서 하나둘씩 스쳐 지나가는 얼굴과 목소리들 역시도.

‘합류하지. 추가 수당만 넉넉히 준다면.’

사나운 눈매와 늘 품에 안고 있던 한 자루의 유엽도.

하지만 겉보기와 달리, 내게 있어 송일섬은 언제나 든든한 전우이자 좋은 사람이었다.

매번 임무의 위험함과 추가 수당에 대해 투덜대면서도, 송일섬은 언제나 가장 위험한 곳에서 싸웠다.

누군가를 지키기 위해 평생토록 걸어왔던 길을 떠난 그는, 마지막 순간까지 그 맹세를 지켰을 것이다.

‘분명 그랬겠지. 내가 아는 그 녀석이라면.’

눈으로 보이는 것만이 전부가 아니다.

남들에게는 거칠고 투박하게만 보였을 어느 낭인이 그랬고, 예상치 못하게 인연을 맺게 된 두 사파인 또한 마찬가지였다.

‘많이 늦은 건가?’

오늘과 같은 혈전이 벌어졌던 감숙성에서의 그날, 아비의 최후를 지키고 되돌아온 사마표의 물음에 나는 망설임 없이 대답했었다.

아니라고. 때맞춰 와 주었다고.

한 줌의 거짓조차 담겨 있지 않은, 그대로의 진심이었다.

설령 여러 고민 끝에 방향을 잃고 멀리 돌아가더라도, 사마표는 끝끝내 올바른 길로 되돌아올 그런 사람이었으니까.

아니.

‘그런 친구였으니까.’

마음 깊은 곳 어딘가로 하염없이 흘러내리는 뇌까림과 함께, 나는 홀린 듯이 움직였다.

쉬쉭!

송일섬처럼 사방에서 날아드는 날붙이를 피해 피 웅덩이를 구르고.

서걱!

사마표처럼 가장 잔혹하고 확실한 수법으로 적들의 숨통을 끊었으며.

콰드드득!

이 자리에 없는 또 다른 누군가처럼, 실로 태산(太山)과 같은 압도적인 기세로 막아서는 것들을 모조리 휩쓸었다.

‘태산이, 각주 믿는다! 세상에서 주군 다음으로 좋다!’

나는 나아갔다.

비산하는 비명과 핏물 사이로 환청처럼 울려 퍼지는 목소리들을 들으며.

짚단처럼 허물어지는 적들의 모습 위로, 차례차례 덧씌워지는 얼굴들을 그려 내며.

‘잠깐, 걸으실래요?’

안개처럼 피어올라, 바람처럼 스쳐 간다.

깊은 어둠에 잠긴 용봉표국의 화원과 그날따라 유난히도 밝고 크던 보름달이.

‘진 대협.’

취기의 힘을 빌려 춤추듯 사뿐하던 걸음걸이와 활기찬 목소리가.

‘나…… 잘할 수 있을까요?’

그 모든 것으로도 숨길 수 없었던 젖은 눈가도.

‘정말, 잘할 수 있을까요?’

생생하게 기억난다.

그 모든 것이.

오늘따라 달이 밝다며 괜한 호들갑을 떨고, 예상치 못했던 물음에 침묵하던 때에도.

그리고 눈물이 그렁그렁 매달린 눈을 바라보며 입을 연 그 순간조차도.

‘잘하지 못해도, 힘내지 않아도 괜찮습니다.’

그날 밤, 나는 달을 보고 있지 않았다.

‘그거면 되지 않을까요. 주 소저.’

보름달보다 밝고, 초승달처럼 휘어지던 그 눈매를 멍하니 바라보고 있었다.

바로 지금 이 순간 눈앞으로 들이닥치는 저 칠흑색 강기처럼, 오늘과 같은 날이 찾아오리라고는 생각지도 못한 채.

후우우우웅!

“피해!”

언제 여기까지 왔을까.

적진을 깊숙이 파고든 내 등 뒤로 적천강의 다급한 외침이 울려 퍼지고, 무시무시한 파공성이 소리를 집어삼켰다.

하지만 나는 동요하지 않았다.

정확히는, 그 정도의 이성마저 남아 있지 않았다.

그저 희뿌연 시야마저 어둡고 탁하게 물들이는, 그렇기에 더욱더 살아 있는 것처럼 느껴지지 않는 두 개의 기운을 직시할 뿐이었다.

눈이 아닌 감각으로.

아니, 마음으로.

그와 동시에, 느려진 시간의 틈새 속에서 창을 내뻗었다.

슈확!

흐릿한 화염을 머금은 백염의 창날이 바람을 가른다.

공간을 꿰뚫고, 그 너머의 어둠을, 일점(一點)을 관통한다.

화아아악!

“……!”

“……!”

흔적도 없이 모든 것을 집어삼킬 것만 같던 두 줄기의 강기가 힘없이 흩어지는 광경에, 사방의 공기가 찌르르 울리는 것이 느껴졌다.

파괴? 격돌?

틀렸다.

조금 전의 그것을 정의할 수 있는 유일한 단어는, 분쇄(分碎)다.

장본인인 나조차도 이해하지 못할 만큼 불가사의한.

또한 앞서 내게 강기를 쏘아 보낸 망자(亡子)들마저 분노시킬 정도로 완벽한 분쇄.

- 진. 태. 경!

마지막까지 살아남은 두 기의 흑귀(黑鬼)가 동시에 부르짖으며 쏘아진다.

십여 장의 허공을 단숨에 뛰어넘은 유령마가 머리 위로 그림자를 드리우고, 번뜩이는 핏빛 안광과 함께 더욱 거대해진 강기가 내리그어졌다.

콰아아아아!

이미 터져나간 고막조차 뒤흔들 정도로 거센 파공음.

그러나 놈들이 들이닥친 방향 끝에 있는 것은, 나 하나만이 아니었다.

콰앙! 구구구궁!

찰나의 순간, 허공에서 뒤얽힌 네 줄기의 섬광이 부풀어 오른다.

압축된 공기가 폭발하고 그 엄청난 힘을 이겨 내지 못한 대지가 뒤집힌다.

그리고 그 중심에, 나를 구하기 위해 달려든 두 명의 초인(超人)이 있었다.

푸푹! 콰드득!

살성의 소도와 우모침이, 궁성이 굳게 말아쥔 두 자루의 곡도가 벼락과도 같은 속도로 흑귀들을 찌르고 베어 갈랐다.

하지만 새하얗게 질린 얼굴로 이를 악문 채 얼마 남지 않은 힘을 쥐어 짜내는 그들과는 달리, 흑귀들은 결코 쓰러지지 않았다.

아니, 치명상은 물론 잘려 나간 팔다리마저 회복하며 수십 번의 죽음을 딛고 다시 일어났다.

우우우웅.

부르르 떨리는 공기.

겹겹이 중첩된 무수한 마법이 흑귀들의 회복력을 북돋고, 더욱더 강하고 빠른 힘과 속도를 부여하고 있었다.

누구보다 가장 치열하게 싸웠기에, 가장 깊은 한계에 다다라 있던 삼성(三星)의 두 사람을 상대할 수 있을 만큼.

“가거라, 어서!”

살성이 다급한 외침이 귓가를 파고들고, 지치고 낮게 가라앉은 궁성의 시선이 뺨에 닿았다. 마치 스스로 선택받은 자임을 증명해 보라는 듯이.

혹은, 네가 죽을 자리는 여기가 아니라는 듯이.

‘그래, 이곳에서 쓰러질 수는 없어.’

나는 그들을 뒤로한 채 비틀거리는 걸음을 옮겼다.

앞장서서 길을 여는 적천강과 청풍의 뒤를 따라, 꿈처럼 몽롱한 시야 너머로 비치는 적들을 쓰러트리고 또 쓰러트리며 생각했다.

이제는 결코 이루어질 수 없게 된 한 사람과의 약속을.

어느덧 이 세상에서 가장 큰 기억으로 자리매김하게 된 누군가에게, 차마 도망치라고 말하지 못했던 그때의 나 자신을.



‘대 태원진가의 수문조장 혁무진입니다. 신원과 방문 목적을 밝혀 주십…… 뭐? 기루?’

‘삼공자, 내 비록 말단 조장이지만 한마디만 합시다.’



첫 만남은 질긴 악연이었으나.



‘정찰조라니. 삼공자가 나를 왜…….’

‘명령에 따르겠소. 조장, 아니 조장님.’



얼마 지나지 않아 녀석과 나는 부드럽게 이어졌고.



‘어허, 조장님. 제가 있는데 뭐가 그리 걱정이십니까!’

‘조장님의 심장! 오른팔! 바로 이 혁무진을 믿으십시오!’

‘……아무리 그래도 새끼발가락은 너무한 거 아닙니까?’



이내 끈끈해졌다.

어느 순간 쉽게 떨어질 수조차 없게 될 만큼.

눈에 보이지 않으면 아쉽고, 떼어내면 걱정되는.

가장 믿는 친구이자 수하.

그랬던 녀석이, 혁무진이 죽었다.

결국 어디에서, 누구에게 죽었는지조차 보지 못했다.

‘설령 천운으로 살아남았더라도, 이제는 두 번 다시 만날 수 없겠지.’

녀석과의 마지막 약속은 영원히 이루어질 수 없을 것이다.

그 전에 내가 죽고 말 테니.

내가 지키고자 했던, 혹은 지금쯤 어딘가에서 나를 애타게 기다리고 있을 이들을 뒤로한 채 되돌아올 수 없는 먼 길로 떠나야 할 테니.

‘하지만……!’

이를 악물고, 참았던 숨을 토해 낸다.

창을 휘두르고, 꺼져 가는 불씨를 쉼 없이 되살렸다.

보보(步步)마다 쌓여 가는 시체와 솟구치는 핏물들을 짓밟으며, 나를 지키는 이들과 함께 한 몸이 되어 나아갔다.

산 자와 죽은 자.

그들 모두를 위한 마지막이자 유일한 길을 향해.

몽롱한 시야 속에서도 선명하게 전해져 오는, 누군가의 핏빛 안광을 향해.

콰드드드득!

본능처럼 내리그은 창날을 따라 조각나는 광신도들의 살과 뼈.

거세게 휘몰아치는 그 짙은 피바람 너머에, 피와 광기에 사무친 한 마리의 괴물이 있었다.

“도망쳐도 모자랄 판에 이리 제 발로 찾아와 주다니. 뭐라 감사의 인사를 해야 할지 모르겠군.”

마침내 다시 마주하게 된 혈주(血主)가, 나를 향해 활짝 웃었다.

정확히는 이미 지칠 대로 지친 적천강과 청풍, 그리고 그들의 중심에 선 나를 향해.

“자, 이제 죽을 시간이다.”

글쎄.

어쩌면 정말 그럴 수도 있겠지.

그러나.

삐빅.



제한 시간 : 5분 00초



아직은 아니다.
```

## Final English reading copy

```markdown
# Chapter 1123

“You…!”

Hearing that familiar voice tremble with agitation, I let out the breath I’d been holding.

I slowly blinked and swallowed the blood pooled in my mouth.

It was a strange feeling, unlike anything I’d ever experienced.

I felt hazy, as if I were trapped in a dream I could never escape. And yet, at the same time, everything around me came through with perfect clarity.

As for what this unfamiliar sensation was—the first I’d ever experienced—the System gave me a clear answer, as it always did.

In its uniquely kind and cruel way.

*Beep.*

> **System**
>
> **Status Effect:** Final Rally has been applied.

Final rally.

Like the sunlight that blazes just before the sun sets, the last flame burning at the edge of a life fading into darkness.

*So this is what it feels like.*

The thought came to me suddenly.

I remembered the final moments of all those people I’d personally brought down with these two hands—or desperately tried to hold on to, only to watch them leave anyway.

All the countless emotions I’d glimpsed in them.

At last, I felt like I could understand it all.

And I understood something else, too: unlike them, who’d waited for death as it slowly drew near, I was the kind of fool who had no choice but to run straight toward it.

*Ding.*

> **System**
>
> Final Rally is an act of divine mercy, a testament to human will, and a candle by which you may reflect on the life you have lived. Though its flame burns only briefly, that instant of light will shine so brightly that even death may be forgotten.

This time, it wasn’t the cold, harsh warning tone.

A clear chime, so familiar it rang in my ears, roused my body and mind from their endless plunge into darkness.

The radiant light the System had promised—a light bright enough to make me forget even death.

> **System**
>
> All pain you feel is greatly reduced for the duration of Final Rally.

The trembling of my body, groaning under the pain and death closing in by the second, came to a halt.

> **System**
>
> **Qi Sense** temporarily increases by a great amount.

A spark caught in the ashes of my cooling mind.

Fwoosh.

A sudden warmth pierced my back. The spark swelled into a flame.

> **System**
>
> Scorching Yang Qi cradles your exhausted body and heals some of your Internal Injuries.

Two flames could not coexist.

Someday they would clash and destroy each other.

But if they sprang from the same root, then they were originally one and the same.

Just like the person who, despite suffering severe Internal Injuries of his own, had given me his energy without hesitation.

“What are you waiting for?”

His face was as pale as paper. Great and small wounds were etched across his body, and his frame trembled.

But he—Jeok Cheongang—was smiling at me.

Trying to suppress the joy that his Disciple had recovered a little strength, along with the sorrow of what that meant.

“Come on. Let’s go. Together.”

At that moment—

*Ding.*

> **System**
>
> A sudden Quest, A Candle in the Wind, or a Flame, has been generated!
>
> Death awaits you. You cannot refuse this Quest!
>
> **Time Limit:** 9 minutes, 59 seconds

As time, which had stood still, began to flow again, I gripped White Flame tightly and took a step forward.

Into the nightmare that wasn’t over yet.

No—toward a reality worse than any nightmare.

*I’ll change it. I have to.*

If this had been a fight I had to face alone, I might have given up already.

I might have leaned my exhausted body against a pile of corpses, looked back on the time I’d left behind, and waited for death to slowly descend.

But—

SHWICK!

I wasn’t alone anymore.

KWA-BOOOOM!

Dazzling light-flames swallowed the enemies whole.

Amid the reddish, overheated earth and the shimmering haze that warped the air, a giant of fire roared.

At the same time, the Slaughter Saint, the Bow Saint, Cheongpung, and the last of the devoted defenders—

And countless civilians beyond counting, surging behind them like a wave.

Their cries were no longer angry shouts. They were shouting the name of someone none of us had expected.

“Charge! Charge! Protect the Marquis of Shangshan!”

“……!”

The great shout shook the battlefield and reached my ears. A streak of lightning shot up my spine.

They said they would protect me.

Me, of all people.

Those people, who didn’t have a scrap of internal energy or a proper weapon, who held sickles and pickaxes in their hands.

They were risking their lives for me—the man who hadn’t even managed to protect his own people.

*Right. In the end, I couldn’t protect you.*

As the beloved faces I would never see again flashed through my mind, I shot toward the fanatics.

SHWIIK!

The toes of my feet. My waist. My shoulder. My arms and wrists.

Following movements etched into instinct through countless repetitions and real battles, I split the raging wind and rain.

Slice!

A single, cool cutting sound swept through the air.

At the same time, more than ten pairs of eyes flew wide open.

The fanatics stared at me in disbelief, clutching their severed throats as they crumpled to the ground.

White Flame’s spearhead, trailing a faint heat, was slower and weaker than it had ever been. But for some reason, the enemies waiting in its path couldn’t react in time.

And neither could the next wave, surging in to fill the gaps left by their dead comrades.

Stab! Crack!

I stabbed through everything in my way, pulled my spear free, and twisted it.

My vision was still hazy, but my senses were sharper than ever.

So were the faces and voices that flickered past, one by one, through the thickening mist of blood.

*“I’ll join you. Just make sure the danger pay is generous.”*

A pair of fierce eyes, and the willow-leaf saber he always carried in his arms.

But despite his appearance, Song Ilseom had always been a reliable comrade and a good person to me.

He complained every time about how dangerous the missions were and how much extra pay he deserved, but Song Ilseom always fought in the most dangerous places.

He’d left behind the path he’d walked his whole life in order to protect someone. I was sure he’d kept that vow until his final moments.

*He must have. If it was the guy I knew.*

There was more to a person than what you saw.

That was true of a wandering martial artist others might have seen as nothing but rough and uncouth. It was true, too, of the two unorthodox faction members I’d unexpectedly formed ties with.

*Am I too late?*

That day in Gansu, when a battle like this one had raged, Sama Pyo had returned from staying with his father through his final moments and asked me that question.

I’d answered without hesitation.

No. You came right on time.

Every word had been the truth. Not a trace of a lie in it.

Even if he lost his way after agonizing over his choices and took a long detour, Sama Pyo was the sort of person who would find his way back to the right path in the end.

No.

*He was that kind of friend.*

With those words muttering endlessly somewhere deep inside me, I moved as if entranced.

SHWICK!

Like Song Ilseom, I rolled through a pool of blood to evade blades flying at me from every direction.

Slice!

Like Sama Pyo, I cut off my enemies’ breath with the cruelest, surest methods.

KRRRUNCH!

Like someone else who wasn’t here, I swept through everything in my way with an overwhelming aura as immense as Taishan.

*Taishan believes in Pavilion Master! Likes him second best in the world, after Lord!*

I pressed forward.

Listening to voices that rang like hallucinations amid flying screams and blood.

Seeing familiar faces laid over the enemies collapsing like bundles of straw.

*“Would you like to take a walk?”*

They rose like mist and passed like the wind.

The Fire Courtyard of the Yongbong Escort Bureau, shrouded in deep darkness, and the full moon, unusually bright and large that night.

*“Great Hero Jin.”*

The light, lively voice and the graceful, dancing steps, as if buoyed by drink.

*“Do you think…I can do it?”*

And the tearful eyes she couldn’t hide, no matter what she did.

*“Can I really do it?”*

I remembered it all, vividly.

Every bit of it.

Even when I made a pointless fuss about how bright the moon was that night, then fell silent at her unexpected question.

Even the moment I looked into her eyes, brimming with tears, and opened my mouth.

*“It’s all right if you can’t do it well. You don’t have to force yourself.”*

That night, I hadn’t been looking at the moon.

*“Wouldn’t that be enough, Young Lady Ju?”*

I’d been staring blankly at the eyes that shone brighter than the full moon and curved like a crescent moon.

Never imagining that a day like today would come, like the pitch-black Force rushing toward me right now.

WHOOOOOSH!

“Get out of the way!”

When had I gotten this far?

Jeok Cheongang’s urgent shout rang out behind me, deep in enemy lines, and a terrible whooshing sound swallowed the noise around us.

But I didn’t flinch.

More precisely, I didn’t have enough reason left to do so.

I simply stared at the two streams of energy that darkened even my hazy vision—so murky that they seemed less alive than anything else.

Not with my eyes, but with my senses.

No—with my heart.

And at the same time, in the gap between moments slowed to a crawl, I thrust out my spear.

SHWICK!

White Flame’s spearhead, wreathed in a faint blaze, cut through the air.

It pierced space, the darkness beyond it, and a single point.

Fwoosh!

“……!”

“……!”

The two streams of Force, which had seemed ready to swallow everything without a trace, scattered helplessly. I felt the air tremble all around me.

Destruction? A clash?

No.

The only word that could describe what had just happened was shattering.

Something so mysterious that even I, who had caused it, couldn’t understand.

So perfectly shattered that it enraged even the dead who had just fired Force at me.

—JIN. TAE. KYUNG!

The two Black Ghosts still standing cried out in unison and charged.

A ghostly horse leaped across the dozen or so jang of open air in an instant, casting its shadow over me. With its blood-red eyes flashing, the now-enlarged Force came crashing down.

KWA-BOOOOOOM!

The blast was so violent it shook my eardrums, already burst.

But I wasn’t the only one waiting where they were headed.

KWAANG! RUMBLE!

In the blink of an eye, four streaks of light collided in midair and swelled.

The compressed air exploded, and the earth overturned, unable to withstand the tremendous force.

At the heart of it were two superhumans who’d rushed to save me.

Stab! Crack!

The Slaughter Saint’s short knife and ox-hair needles, and the two curved swords clenched in the Bow Saint’s hands, stabbed and sliced through the Black Ghosts at lightning speed.

But unlike the Black Ghosts, the two Saints gritted their teeth, faces ashen, forcing out what little strength they had left.

The Black Ghosts refused to fall.

No. They recovered from not just mortal wounds, but even severed limbs, rising again after dying dozens of times.

Wooooong.

The air trembled.

Countless overlapping spells bolstered the Black Ghosts’ ability to heal, giving them even greater strength and speed.

Enough to face two of the Three Saints, who had fought more fiercely than anyone and were now pushed to their absolute limits.

“Go! Hurry!”

The Slaughter Saint’s urgent shout pierced my ears. The Bow Saint’s tired, lowered gaze touched my cheek, as if telling me to prove I was the one who’d been chosen.

Or that this wasn’t where I was meant to die.

*Right. I can’t fall here.*

I staggered forward, leaving them behind.

Following Jeok Cheongang and Cheongpung as they led the way, I cut down the enemies that appeared beyond my dreamlike, hazy vision, again and again, as I thought about a promise with someone that could never be kept now.

About the me who hadn’t been able to tell someone who’d become the greatest memory in the world to run away.

*“I’m Hyuk Mujin, Captain of the Gatekeepers of the great Jin Family of Taiyuan. State your identity and purpose for visiting… What? A pleasure house?”*

*“Third Young Master, I may be a low-ranking Captain, but let me say one thing.”*

Our first meeting had been a stubborn feud.

*“A scouting squad? Why me, Third Young Master…?”*

*“I’ll follow your orders. Captain—no, Captain, sir.”*

Before long, the two of us had fallen into step together.

*“Now, now, Captain. What’s there to worry about when you’ve got me?”*

*“Your heart! Your right arm! Trust Hyuk Mujin!”*

*“……Even so, isn’t your little toe a bit much?”*

And then we’d become inseparable.

So close that, at some point, we couldn’t even bear to be apart.

When I couldn’t see him, I missed him. When he was away, I worried about him.

My most trusted friend and subordinate.

That guy—Hyuk Mujin—had died.

In the end, I hadn’t even seen where or who had killed him.

*Even if he somehow survived by some miracle, I’ll never see him again.*

The last promise I’d made to him would never be fulfilled.

Because I would die first.

Because I’d have to leave behind the people I’d wanted to protect—or the people waiting somewhere for me, desperate for my return—and set off down a long road from which there was no coming back.

*But…!*

I gritted my teeth and let out the breath I’d been holding.

I swung my spear, tirelessly rekindling the dying flame.

Trampling the corpses piling up with each step and the blood spurting into the air, I moved as one with the people protecting me.

Toward the last and only path left to the living and the dead.

Toward the blood-red eyes I could sense with perfect clarity, even through my hazy vision.

KRRRUNCH!

The fanatics’ flesh and bones broke apart beneath the spearhead I brought down on instinct.

Beyond the fierce storm of blood, a monster steeped in blood and madness stood waiting.

“You should’ve been running for your life, and instead you’ve come right to me. I don’t know how to thank you.”

The Blood Lord, at last standing before me again, smiled broadly.

Or rather, at Jeok Cheongang and Cheongpung, already exhausted beyond measure, and me standing between them.

“Well, it’s time for you to die.”

Maybe he was right.

But—

*Beep.*

> **System**
>
> **Time Limit:** 5 minutes, 00 seconds

Not yet.
```
