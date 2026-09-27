<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1178.txt",
      "sha256": "cbce34fe8e7822b6fdf23f432b07efa6b42cdd49527e49dc22f93c3cb3a0cc91",
      "bytes": 11632
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "d4d901670292c980dbd6129e2ebbe8550be81b94f32b6039bd3db2697b7841c5",
      "bytes": 1762
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "6bd67da46d2a4fea774ad7ef64f30f16a650b1c6d85bd1a995fc818ad294b01a",
      "bytes": 248538
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "3d3d1e20014c7dc6c006642900170dda7d0abbde3ee60603b89ff3028b2e32b9",
      "bytes": 1230
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "c30079f63bf703c76f353edc7108713a71e6392ca071751fd1877c4f14b5ca80",
      "bytes": 760
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "5fd254985bf65115472507e5dead06d77860d6d96c4be738bd95b37d5ecf2952",
      "bytes": 668
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "92d077ee9b40c32a7989d5d59bc42e67af2964954cc585b3235f7909f843ec26",
      "bytes": 1377
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "05a28995cda7b16df74a39ae3c0dabdb288da12b24247b6c7a4c89982ceea346",
      "bytes": 1701
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "23e42b34e87e8b0e74ccc3f1c28885671a9dcbf8fc5dc3630b702c1cd7825009",
      "bytes": 1550
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "73dc1426d137e59c0e3bd7540974186fbd45f0f2c7e3942208ebc6b901e0ac57",
      "bytes": 623
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "a47225780a805b3f4acfd1cf8c95f345a1098aba0104e4f2b094c86d72875294",
      "bytes": 974
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "0b807e2efa43342e238d59443fcb5f7e08d9b3c4eda68c956e9725bec977f191",
      "bytes": 807
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "1df348f7bbe89043d28753da52bd027dbceabfa4104532e5568759a2c330762c",
      "bytes": 295029
    }
  ],
  "estimated_tokens": 11723
}
-->

# Durable State Update — Chapter 1178

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
1 and safe_through 1178. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1178. Profile updates may replace only one
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
  "chapter": 1178,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1178,
    "continuity_sources": [1178],
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
    "Taekyung has returned to Murim and reunited with Jeok Cheongang in Xinjiang.",
    "Nearly a month passed in Murim during Taekyung’s less-than-week-long absence in the modern world.",
    "Taekyung’s group is crossing the Taklamakan Desert, where the land appears to contain no living things.",
    "The Slaughter Saint now knows about Taekyung’s otherworldly origin; Jeok Cheongang told him during Taekyung’s month-long sleep.",
    "Taekyung identifies the Lord of Heaven as the living Demon King Asmodeus, who caused the Great Cataclysm.",
    "The Lord of Heaven has awakened and regained greater strength; the process is not complete, but the Lord of Heaven says it will be.",
    "The Grand Mage serves the Lord of Heaven and awaits a command; none has been given.",
    "The Main Quest “Rift and Collapse” failed; “The Foreordained Collapse” warns that player choices can cause irreversible consequences.",
    "Cheon Taemin remains unconscious in a secret facility beneath the Pentagon; Jin knows he is the Martial God and a former Player.",
    "An alert reported that Alpha had awakened; what Alpha is and what its awakening means remain unknown."
  ],
  "continuity_sources": [
    1177,
    1176
  ],
  "open_questions": [
    "What command will the Lord of Heaven give the Grand Mage?",
    "What remains to be completed, and what will happen when it is completed?",
    "What is Alpha, and what does its awakening mean?",
    "Why does the land around Taekyung’s group in Xinjiang contain no living things?",
    "Why is Cheon Taemin still alive despite the capsule’s stated permanent binding to its Player until death?"
  ],
  "safe_through": 1177,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 주화란    | **Ju Hwaran**      |
| 무신     | **Martial God**               | —              |
| 궁성     | **Bow Saint**                 | —              |
| 살성     | **Slaughter Saint**           | —              |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 은인     | **Benefactor**                               |
| 몬스터     | **monster**           |
| 감숙     | **Gansu**              |
| 노부      | **this old man / I**                                            |
| 소저      | **Young Lady**                                                  |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 한서불침 | **Unaffected by Cold and Heat** | Condition attributed to Taekyung after opening both vessels. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 선계 | **realm of immortals** | The other world that Jin travels to and from. |
| 대인 | **Great Sir** | Name used for the mysterious figure in Ningxia. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 청풍 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Cheongpung among the Benefactors when greeting Taekyung's companions. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 혁무진 | 주화란 | Fire Dragon Pavilion member to fellow member | Young Lady Ju | polite and deferential | Mujin addresses Hwaran as 주 소저 while asking her to call a physician. |
| 주화란 | 적천강 | younger ally to legendary martial master | Great Hero Jeok | formal and deferential | Ju Hwaran addresses Jeok as 적 대협 while asking whether he is all right. |
| 신의 | 주화란 | senior physician to younger ally | Young Lady Ju | warm and teasing | The Divine Physician lightly teases Hwaran about being more worried for Jin than he is. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 살성 | 청풍 | senior martial figure to younger companion | you | blunt and familiar | The Slaughter Saint scolds Cheongpung for disappearing without a word. |
| 청풍 | 살성 | younger companion to senior martial figure | old man | polite and familiar | Cheongpung apologizes and explains why he wandered off. |
| 진태경 | 대인 | young martial artist to benefactor | you | casual and blunt | Taekyung asks who Great Sir is, addressing him as 당신. |
| 대인 | 진태경 | older benefactor to young martial artist | you | familiar conversational | Great Sir addresses Taekyung as 자네. |
| 청풍 | 대인 | younger companion addressing an older benefactor | Uncle Great Sir | polite and familiar | Cheongpung repeatedly calls him 대인 아저씨. |
| 대인 | 청풍 | older benefactor addressing a younger companion | you | familiar and teasing | Great Sir addresses Cheongpung as 자네. |
| 궁성 | 살성 | allied martial masters | Slaughter Saint | formal-polite | The Bow Saint directly addresses him as 살성 and uses 당신 while urging him to stay and defend the South Gate. |
| 살성 | 적천강 | familiar peer and fellow martial master | you | familiar and teasing | Uses 자네 while teasing Jeok and reassuring him. |
| 적천강 | 살성 | familiar fellow martial master | you | familiar, insulting-casual | Trades teasing insults with the Slaughter Saint over who is welcome in Taekyung’s carriage. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 1177
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, Sword Saint Mae Jonghak’s grandson and Disciple, a Supreme Peak master known as the Huashan Divine Dragon, creator of Mimi Step, and master of the Azure Dragon Pavilion; he has mastered the Slaughter Saint’s Ghost Illusory Slaughter Step and blended it with his Dark Fragrance Drift.
- **Personality:** Affable, dreamy, and childlike, with innocent curiosity, a deep love of martial arts, and compassion; guided by his grandfather’s righteousness and Taekyung’s chivalry, he meets danger with resolve and trusts Taekyung without wavering.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions; Taekyung is his true martial rival and the person whose way of life he admires, and the Slaughter Saint is his mentor in concealment and Ghost Illusory Slaughter Step.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1177
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 1158
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1144
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and Vice Captain of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is deeply loyal to Taekyung, who trusts him as a close companion and values him as family, and has a warm friendship with fellow Fire Dragon Pavilion member Taishan; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Pavilion members accompanying Taekyung, and his parents own the Hyuk Family Textile Shop, which his younger sibling may inherit.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1177
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and follows his own path rather than pursuing grand causes; though he turned his back on the world, he wants Taekyung to pursue righteousness, practice chivalry, and win people’s hearts, and fiercely protects those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, and shares familiar, teasing camaraderie with the Slaughter Saint; he accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1175
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and eleventh member of the Ten Kings, a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; he serves as Thousand Captain of the Embroidered Uniform Guard, is enfeoffed as Prince Shangshan, and is widely regarded as a new-age savior.
- **Personality:** Hungry, self-aware, and dryly observant, he is pragmatic and fiercely defiant; he protects those he cherishes and meets mounting responsibility with hope and a determination to endure.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother and Jeok Cheongang his Master and trusted confidant; he shares deep loyalty with Hyuk Mujin, whom he values as family, and considers the revived Undead King, formerly the Skeleton King, a friend.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1175
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 1138
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, and filial; remains controlled under pressure but has grown more assertive and openly impatient after the hardships she has endured.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 1175
- **Aliases:** None
- **Role:** Cheon Taemin, the legendary martial artist known as the Martial God and a former Player, is regarded as a pinnacle above the Ten Kings; more than fifty years ago, he defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, Mae Jonghak received several teachings from him, and he left the Bow Saint a letter describing a chosen one; the Tutorial Helper is confirmed to be the Martial God, whom Jin remembers as humanity’s savior.

## Korean source

```text
＃1178화



세상에 완전한 비밀이란 없다.

낮말은 새가 듣고, 밤말은 쥐가 들으며, 그 모든 소리는 결국 사람의 입으로부터 흘러나온다.

“하늘에 맹세코, 노부는 진짜 딱 한 놈한테만 얘기했느니라.”

갓 태어난 아이가 첫울음을 터트리듯, 내 비밀을 처음으로 발설한 주범의 선언에 바로 그 ‘딱 한 놈’이 입술을 핥았다.

“그게 그러니까, 약간의 사실 확인 정도만 해 볼 생각이었다. 저 정신 나간 늙은이가 하는 말을 도통 믿을 수가 있어야지.”

나는 가라앉은 어조로 반문했다.

“그래서요?”

“어쩔 수 없이, 네 녀석에 대해 가장 잘 알 것 같은 놈을 따로 붙잡고 물어봤지.”

자연스럽게 옮겨진 시선에, 마차 구석에 처박혀서 눈치만 살피던 혁무진이 우물쭈물 대답했다.

“정확히는 야밤에 곤히 잠들어 있는 저를 납치해서 사막에 파묻으셨죠. 목만 빼놓고.”

“그건 맞다. 그런데 예상 밖으로 입이 무겁더군. 혹시 네게 해가 될 수 있으니 곧 죽어도 말 못 하겠다고 버티던데.”

살성의 증언에 힘이라도 얻었는지, 혁무진이 한껏 움츠러들어 있던 어깨를 쭉 폈다.

“들으셨죠? 제가 이 정도로 신의 있는 놈입니다.”

“그래서 어쩔 수 없이 내가 들은 이야기를 대강 말해 주었더니, 곧장 그다음 날에 웬 엉뚱한 놈이 찾아와서 묻더군.”

참으로 시기적절하게도, 그 순간 ‘웬 엉뚱한 놈’이 불쑥 얼굴을 들이밀었다.

“은인, 은인. 정말 선계(仙界)에서 온 거죠? 정말 사실인 거죠? 와! 저 선계에서 온 사람 처음 봐요!”

“그래, 딱 저렇게.”

피곤한 눈빛으로 청풍을 노려본 살성이 덧붙였다.

“여하튼, 나도 딱 한 놈한테만 말했다.”

혁무진이 당당하게 폈던 어깨를 다시 움츠리며 중얼거렸다.

“저돈데요.”

그래, 그러셨겠지.

하지만 내가 만약 혁무진이었다면, ‘도저히 다른 사람과 공유 하지 않고서는 못 배길 굉장한 비밀’을 청풍에게 털어놓진 않았을 거다.

이유? 간단하다.

그야 당연히, 청풍이니까.

“은인, 저도요. 저도 주 소저한테만 말했어요!”

나도 모르는 사이에 결백 입증 대회라도 열린 건지, 매우 열광적인 태도로 외치는 청풍의 모습에 적천강이 고개를 끄덕였다.

“틀린 말은 아니다. 다만 딱 저 정도 크기의 목소리로, 대부분이 모여 있던 식사 자리에서 말한 게 문제였지.”

“…….”

어지럽네, 진짜.

고개를 절레절레 내젓던 나는 문득 누군가와 눈이 마주쳤다.

다른 이들과 다르게 아까부터 아무런 반응 없이 침묵만 지키고 있던 한 사람, 바로 주화란이었다.

“아, 주 소저.”

어색한 미소와 함께 인사를 건넸지만, 돌아오는 대답은 없었다.

그저 물끄러미 바라보는 시선만이 얇은 바늘처럼 얼굴을 콕콕 찌를 뿐.

아니, 지금 나를 향한 시선은 그녀의 것뿐만이 아니다.

어느샌가 내려앉은 정적 속, 마차 안의 모두가 나를 바라보고 있다.

음. 모르겠다.

분명 아무 말이라도 해야 할 것 같은데, 도대체 무슨 말을 어떻게 해야 하는지.

‘아무 일 없는 것처럼 굴어야 하나? 아니면 미리 알려 주지 않은 것에 대한 사과를…….’

머릿속이 실타래처럼 엉켜 가던 그 순간이었다.

굳게 닫혀 있던 붉은 입술이 열린 것은.

“아니죠?”

“네? 갑자기 그게 무슨.”

“사실 사람이 아니라 신선(神仙)이라든지, 뭐 그런 거요.”

“……신선?”

멍하니 눈만 껌뻑거리던 나는, 이내 상황을 이해하고 실소했다.

“신선은 무슨. 주 소저는 제가 그렇게 대단한 놈으로 보여요?”

“웃지 말고요.”

“……아, 죄송합니다. 저도 모르게 그만. 그런데 진짜 아니에요.”

“정말이죠?”

“그럼요. 제가 사람이 아니면 뭐겠어요. 어쩌다 보니 오해가 겹쳐서 선계(仙界)로 불리는 것뿐이지, 제 고향도 이곳과 똑같이 그냥 사람 사는 곳이에요.”

“그래요?”

“네.”

사실 똑같은 세상이라고 하기에는 매우 큰 어폐가 있다.

기술 발전 차이야 둘째치더라도, 최소한 이 동네는 집 앞 사거리 객잔 가는 길에 몬스터 마주칠 일은 없을 테니까.

하지만 나는 굳이 부연 설명을 하지 않았고, 주화란도 굳이 그 부분에 대해 깊게 파고들 생각이 없어 보였다.

대신 그녀는 또 한 번 생각지도 못한 질문을 던졌다.

“그럼 실제 나이는요?”

“……아니, 갑자기?”

“그냥 궁금해서요. 혼백(魂魄)만 오고 갈 뿐이지, 이곳과는 다르다면서요.”

나는 얼떨떨한 목소리로 대답했다.

“어, 음. 스물여덟 정도?”

“정도?”

“아니, 맞아요. 몇 번 오가다 보니 시간 개념이 좀 망가져서 잠깐 헷갈렸…….”

나도 모르게 주절주절 변명을 늘어놓으려던 찰나, 주화란이 칼 같은 음성으로 말을 잘랐다.

“아직 이립(而立)도 안 된 거네요.”

“그렇죠.”

“우화등선으로 오백 년쯤 살아온 신선이나 선인도 아니시고.”

“……사람이라니까요, 사람.”

우화등선은 무슨.

등신 소리는 꽤 들어 봤다. 하연이한테.

그리고 정말 내가 오백 년 묵은 신선이었다면 지금쯤 이 팔두 마차를 끌고 있는 게 말이 아니라 천주였겠지.

‘진짜 그랬으면 바랄 게 없겠네.’

달콤하면서도 슬픈 생각에 잠겨 있던 그때, 주화란이 모든 재판을 끝마친 판사처럼 선언했다.

“됐어요, 그럼.”

“네?”

“괜찮아요. 사람이고, 스물여덟 정도면.”

퍽 희한한 판결문이었다.

아무런 사건 경위도. 형량도 없는.

하지만 그것으로 됐다.

뭔진 모르겠지만, 된 거다.

‘아니, 솔직히 알 것 같긴 한데.’

왠지 모르게 가슴 한구석이 뻐근하다. 심장에 가까운 쪽이다.

그러나 동시에 다른 한쪽 가슴은 무거워졌다.

지금 같은 상황에 이런 감정이 들어도 되나, 이래도 되는 걸까 하는 마음에.

아마도 그래서였을 것이다.

주위 사람들의 시선이 더해져 더욱 묘해진 공기 속, 꿋꿋하게 나를 바라보는 그 시선을 쉽게 마주할 수 없었던 이유도.

다음 순간 괜히 화제를 돌린 이유도.

“그나저나, 다른 사람들은 언제쯤 다 돌아옵니까?”

“으, 응?”

“이 자리에 없는 사람들이요.”

나와 주화란을 번갈아 바라보고 있던 적천강이 헛기침을 내뱉었다.

“커흠. 갑자기 그건 왜 묻느냐?”

“보고 싶기도 하고, 이렇게 된 마당에 다 모아 놓고 제 입으로 직접 할 이야기도 있어서요.”

“뭐, 그야 각자 수색하는 범위 차가 있다 보니 곧 다들 돌아오겠지. 한데 굳이 그럴 필요까지는 없다. 아직 네 녀석에 관해 아무것도 모르는 녀석도 있으니.”

“예? 하지만 아까 전에는 분명히 청풍 저 인간이…….”

“그래, 저 경망스러운 주둥이로 다 들리게 말했지. ‘대부분이 모인’ 식사 자리에서.”

“아.”

나는 짧게 탄성을 내뱉었다.

그리고 동시에, 아직 내 비밀에 대해 듣지 못했을 가장 유력한 사람을 그리 어렵지 않게 떠올릴 수 있었다.

“대인(大人)이군요.”

감숙 땅에서 처음 인연을 맺어 이곳까지 함께하게 된 초절정 고수.

봉두난발의 행색만큼이나 의문에 쌓인, 심지어는 그 자신조차 스스로의 정체가 누구인지 모르는 괴인.

“하루에도 몇 번씩 정신이 오락가락하는 놈이 대인은 무슨.”

콧방귀를 뀐 적천강이 말을 이었다.

“때마침 자리에 있었다면 어쩔 수 없었겠으나, 그렇다고 한들 구태여 그런 이야기를 해 주는 것도 영 석연찮아서 노부가 입단속을 시켰다. 그간 제법 도움이 되긴 했으나 비밀은 비밀이고, 정체도 잘 모르니.”

“음.”

“네 녀석이 무슨 생각을 하는지 다 짐작하고 있느니라. 노부의 판단을 억지로 관철시킬 마음도 없고. 그러니 그 대인인지 하는 놈에 관해서는 네가 원하는 대로 하거라. 다만…….”

문득 말꼬리를 흐린 적천강이 덥수룩한 수염을 긁적였다.

“노부는 그놈보다 다른 쪽이 신경 쓰이는구나.”

“다른 쪽이라면.”

“지금 이 자리에 있는 녀석들이야 이제는 얼추 이해하고 받아들였지만, 세상일이 그리 쉽고 간단하게 풀리는 것이겠느냐. 특히 늙은이들은 새로운 것을 이해하기 어려운 법이지.”

앞서 대인을 떠올렸듯이, 나는 아직 이 자리에 없는 또 다른  한 사람을 기억 해냈다.

‘궁성(弓星).’

나는 마음속 뇌까림과 함께 창밖을 바라 보았다.

캄캄한 밤하늘을 스쳐 지나가는 구름 탓인지, 오늘따라 별빛은 유난히도 흐렸다.



* * *



사막의 밤은 냉혹하다.

낮에는 온 세상을 태워 버릴 듯한 열기를 내뿜다가도, 해가 떨어지고 어둠이 찾아오면 얼음장 같은 냉기가 대지를 뒤덮는다.

그러나 뼛속까지 스며드는 그 추위 속에서도, 모래 언덕 위에 홀로 드리워진 가냘픈 그림자는 조금도 흔들림이 없었다.

그림자의 주인은 이미 오래전 한서불침(寒暑不侵)의 경지를 넘어선 고수이니 당연한 일이었지만, 단지 그렇기 때문만은 아니었다.

“선계, 선계라.”

그녀, 궁성은 깊게 가라앉은 눈빛으로 어둠에 잠긴 사막을 바라보았다.

끝없이 펼쳐진 저 광활한 모래의 바다는, 마치 그녀의 마음을 닮아 있는 듯했다.

아무리 걸어도 끝이 보이지 않을 것만 같고, 그 안에는 힘겨운 고난과 꺼끌거리는 모래 알갱이만 가득한.

“그거였군요. 당신께서 숨기고 계셨던 비밀이.”

궁성은 나지막한 음성으로 중얼거렸다.

깊은 밤의 사막은 훌륭한 청자(聽者)였다. 

아무것도 되묻지 않고, 어디서 흘러왔는지 모를 바람만을 묵묵히 흘려보낸다.

하지만 좋은 대화상대는 아니었다.

아니, 설령 사막이 사람의 말을 할 수 있게 되더라도 그 사실은 달라지지 않을 것이다.

궁성이 대화를 원하는 상대는 따로 있었으니.

“……무신(武神)이여.”

투명한 피부와 달리, 강철처럼 단단하고 못 박힌 손가락이 품 안을 더듬었다.

무신이 오직 그녀에게 남긴, 그렇기에 그 누구에게도 말하지 못할 비밀이 담긴 낡은 서신이 옷자락 너머로 붙잡혔다.

“당신께서 원하는 바가 이것입니까?”

궁성으로서는 도무지 이해할 수 없었다.

이 서신을 남긴 이가 무신이었기에 그저 믿고 따랐을 뿐, 그 안에 담긴 내용을 쉬이 납득할 수 없었던 것은 처음부터 지금까지 변한 적이 없었다.

불과 며칠 전, 진태경에 관한 비밀을 듣고 난 후에는 더더욱 그랬다.

“진정으로…… 이것이 맞습니까?”

그 순간.

스륵.

등 뒤에서 울려퍼진 미세한 소음이, 궁성의 귓가에 닿았다.
```

## Final English reading copy

```markdown
# Chapter 1178

There are no secrets in the world that can stay secret forever.

Birds hear what’s said by day, rats hear what’s said by night, and in the end, every word slips from someone’s lips.

“I swear to Heaven, this old man told exactly one person.”

At the declaration of the one who’d first let my secret slip—as if a newborn were crying for the first time—the “one person” in question licked his lips.

“So, I was just planning to check a few facts. It’s not like I could believe a word that crazy old man said.”

I asked in a subdued voice, “And then?”

“I had no choice. I grabbed the person who seemed to know you best and asked him.”

At the Slaughter Saint’s casually shifted gaze, Hyuk Mujin, who’d been huddled in a corner of the carriage, warily watching the others, stammered out an answer.

“To be precise, you kidnapped me in the dead of night while I was sound asleep and buried me in the desert. With only my head sticking out.”

“That’s right. But he turned out to be surprisingly tight-lipped. He insisted he’d rather die than tell me anything that might put you in danger.”

Perhaps buoyed by the Slaughter Saint’s testimony, Hyuk Mujin straightened his hunched shoulders.

“You heard him, right? I’m that loyal.”

“So, I had no choice but to tell him a rough version of what I’d heard. Then the very next day, some random weirdo came asking about you.”

As if perfectly timed, that “random weirdo” suddenly stuck his face into the conversation.

“Benefactor! Benefactor! You really came from the realm of immortals? It’s true? Wow! I’ve never met anyone from the realm of immortals before!”

“Yeah. Just like that.”

The Slaughter Saint glared at Cheongpung with tired eyes, then added, “Anyway, I told exactly one person, too.”

Hyuk Mujin drew in his shoulders again and muttered, “Me too.”

Yeah. I figured.

But if I were Hyuk Mujin, I wouldn’t have spilled a “stupendous secret I couldn’t possibly keep to myself” to Cheongpung.

Why? Simple.

Because it was Cheongpung.

“Benefactor, me too! I only told Young Lady Ju!”

Maybe an innocence-proving contest had started without my noticing. Cheongpung shouted with tremendous enthusiasm, and Jeok Cheongang nodded.

“He’s not wrong. The problem was that he said it at just about that volume, at a meal where most of us were gathered.”

“…”

This was giving me a headache.

I shook my head, then happened to meet someone’s eyes.

Unlike everyone else, she’d been silent the whole time, without a reaction. Ju Hwaran.

“Ah, Young Lady Ju.”

I greeted her with an awkward smile, but she didn’t answer.

She only stared at me, her gaze pricking my face like a thin needle.

No, she wasn’t the only one looking at me.

A hush had fallen over the carriage, and everyone was watching me.

Well. I didn’t know.

I felt like I should say something, but what was I supposed to say? And how?

*Should I act like nothing happened? Or apologize for not telling them sooner…?*

My thoughts began tangling like a ball of yarn.

Then her tightly closed red lips parted.

“You’re not, are you?”

“Huh? What do you mean, all of a sudden?”

“I mean, you’re not actually an immortal or something instead of a human, are you?”

“An immortal?”

I blinked at her blankly. Then, once I understood, I let out a quiet laugh.

“What do you mean, an immortal? Do I look that impressive to you?”

“Don’t laugh.”

“…Oh. Sorry. I didn’t mean to. But really, I’m not.”

“Are you sure?”

“Of course. What else would I be if not human? Somehow, a misunderstanding piled on top of another, and I got called someone from the realm of immortals. But my hometown is just another place where people live, same as here.”

“Is that so?”

“Yeah.”

Calling them the same world would be a huge stretch.

Even setting aside the difference in technological development, you wouldn’t run into a monster on your way to the inn at the intersection by your house in this part of the world.

But I didn’t bother explaining that, and Ju Hwaran didn’t seem inclined to press the point.

Instead, she asked another question I hadn’t expected.

“Then how old are you really?”

“…Wait, what?”

“I’m just curious. You said only your soul goes back and forth, and that the other world is different from this one.”

I answered, sounding a little bewildered.

“Uh, well. Around twenty-eight?”

“Around?”

“No, I mean, that’s right. After going back and forth a few times, I got a little confused about time for a second…”

I’d started rambling out excuses without meaning to when Ju Hwaran cut me off in a voice as sharp as a blade.

“So you haven’t even turned thirty yet.”

“That’s right.”

“And you’re not an immortal or a celestial who’s lived for five hundred years since ascending to immortality.”

“…I told you, I’m human.”

Ascending to immortality? Please.

I’d been called an idiot plenty of times. By Hayeon.

And if I really were a five-hundred-year-old immortal, the one pulling this eight-horse carriage would be Cheonju, not a horse.

*Wouldn’t that be nice?*

I was lost in a thought both sweet and sad when Ju Hwaran delivered her verdict like a judge who’d finished hearing the case.

“That settles it, then.”

“Huh?”

“It’s fine. You’re human, and you’re around twenty-eight.”

It was a strange verdict.

No explanation of what the case was about. No sentence.

But that was enough.

I didn’t know what it was, but it was settled.

*No, actually, I think I do know.*

For some reason, my chest felt tight. Somewhere close to my heart.

At the same time, another part of my chest grew heavy.

I wondered if it was okay to feel this way right now. If I had any right to.

Maybe that was why I couldn’t meet her gaze easily as she kept looking steadily at me through the strange atmosphere, made even stranger by everyone else’s eyes on us.

And why, the next moment, I changed the subject for no good reason.

“Anyway, when will everyone else be back?”

“Hm? What?”

“The people who aren’t here.”

Jeok Cheongang, who’d been looking back and forth between Ju Hwaran and me, cleared his throat.

“Ahem. Why are you asking that all of a sudden?”

“I missed them. And now that it’s come to this, there’s something I want to tell everyone myself.”

“Well, they’re searching different areas, so they’ll all be back before long. But there’s no need to gather them for that. Some of them still don’t know anything about you.”

“What? But earlier, that human Cheongpung clearly—”

“Yeah, he said it all loud enough for everyone to hear. At a meal where *most* of us were gathered.”

“Oh.”

I let out a short gasp.

At the same time, it wasn’t hard to think of the person most likely not to have heard my secret yet.

“Great Sir.”

The Supreme Peak master who’d first crossed paths with us in Gansu and accompanied us all the way here.

A mysterious eccentric, as puzzling as his wild, unkempt hair—even he didn’t know who he was.

“What Great Sir? The guy can lose his mind several times a day.”

Jeok Cheongang snorted, then continued.

“He happened to be there, we couldn’t have helped it. But it still didn’t sit right with this old man to tell him that sort of thing, so I told everyone to keep quiet. He’s been useful enough, but a secret is a secret, and we don’t even know who he is.”

“Right.”

“I can guess what you’re thinking. I’m not about to force my decision on you. So do as you like about that fellow you call Great Sir. But…”

Jeok Cheongang trailed off and scratched his bushy beard.

“There’s someone else I’m more concerned about than him.”

“Someone else?”

“The people here have more or less understood and accepted it by now. But the world doesn’t work out so easily. Especially for old folks—it’s hard for them to understand something new.”

Just as I’d thought of Great Sir, I remembered another person who wasn’t here.

*Bow Saint.*

I muttered the words to myself and looked out the window.

Perhaps because of the clouds drifting across the pitch-black night sky, the stars looked especially dim tonight.

* * *

Desert nights were merciless.

By day, the heat seemed ready to burn the whole world. But once the sun set and darkness arrived, an icy chill blanketed the land.

Even through the cold that seeped into her bones, though, the faint shadow standing alone atop a sand dune didn’t waver in the slightest.

It was only natural. The master who cast the shadow had long since surpassed the realm of Unaffected by Cold and Heat.

But that wasn’t the only reason.

“The realm of immortals… The realm of immortals.”

Bow Saint gazed into the dark desert, her eyes clouded with thought.

The boundless sea of sand stretched endlessly before her, as if it resembled her heart.

As though no matter how far she walked, she’d never see its end—and as though it contained nothing but hardship and gritty grains of sand.

“So that was the secret you were hiding.”

Bow Saint murmured in a low voice.

The desert at night was an excellent listener.

It never asked anything in return. It simply let the wind pass in silence, the wind no one knew where it had come from.

But it wasn’t good company.

No, even if the desert could speak, that wouldn’t change.

The person Bow Saint wanted to talk to was someone else.

“…Martial God.”

Her fingers, as hard as steel and marked with calluses despite her translucent skin, searched inside her robe.

The old letter the Martial God had left only for her—and which, for that reason, she couldn’t tell anyone about—was caught between the folds of her clothes.

“Is this what you want?”

Bow Saint couldn’t understand.

She had believed and followed what the letter said only because the Martial God had left it. From the beginning until now, she had never been able to make sense of its contents.

And after hearing Jin Taekyung’s secret just a few days ago, she found it even harder to understand.

“Is this truly… right?”

At that moment—

*Rustle.*

A faint sound from behind reached Bow Saint’s ears.
```
