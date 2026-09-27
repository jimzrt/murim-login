<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1184.txt",
      "sha256": "bb8a93337410add719801d76634cb26eb9e9f0628f2df988de3b17f9374f07e6",
      "bytes": 11761
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "108dd7425c4185f154ab6a718d1400ea03d5e37b85c703836029a7b81a4277ea",
      "bytes": 1827
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2372eff4014bbbfe2875ceb74264c004f7f386d353a549f999d2b18a5d322a72",
      "bytes": 248683
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "d5774108c292047a09f3a5e321f84823a84a2d1c71cc770fc0706d07d69f3bf4",
      "bytes": 1230
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "c81f6c68b9c175aa8a55be95f399cf3d4f326306dabbb54a91ff358469150465",
      "bytes": 760
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "061227dcb21013ba5cb0c97eb13ac055b9486d9f19fa839b38ed33c782f407eb",
      "bytes": 670
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "2e096eae48afc4e315b7d44bbc4d3693ab08fd7eecb268a20d81164ca078e316",
      "bytes": 1377
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "0ddc9b2a68dd51ed25782307893882e0823a62ea9e4d7db8b16cd4b789ee7886",
      "bytes": 1701
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "29723f09a36b285eeafd4cd1466b3f8d1cfdb445660e1f699cf0ec3888721648",
      "bytes": 1550
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "adfa90bdd87cab81bdbccc49526e70215950557eb43e4ac6dc4d6d22a5a27176",
      "bytes": 623
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "01b1e80be6e931f6120072d24569b8c8aa7aa9a5578349dbf37c93382a7f9e47",
      "bytes": 974
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "c9f26e8bb6e4b62955577c0083bbc7c7d98b829b33cde48e27d2524107ddd5a8",
      "bytes": 774
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "6667c52c3e290ba4caaca1dbf434ebd8dcf1194b48f8257ae36c0b04d1ccca92",
      "bytes": 980
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "603e3c49f5d38d12148c65f30dba06292ea6e50bd93d8155390005ac0494757a",
      "bytes": 295700
    }
  ],
  "estimated_tokens": 12915
}
-->

# Durable State Update — Chapter 1184

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
1 and safe_through 1184. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1184. Profile updates may replace only one
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
  "chapter": 1184,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1184,
    "continuity_sources": [1184],
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
    "The Murim allied forces split into three forces at the Qinghai-Xinjiang border, planning to rendezvous with the Imperial Army near Tianshan.",
    "Taekyung's group reached the planned rendezvous near Tianshan, but the Murim Alliance and Imperial Guards missed the agreed deadline.",
    "Jeok Cheongang's group will advance into Tianshan without waiting; Taekyung is to be the main attack.",
    "Taekyung and Hyuk Mujin are concerned for their separated companions and expect them to arrive.",
    "Taekyung experiences unexplained chest pain and difficulty sleeping.",
    "The Son of Heaven's army is fighting monsters in a basin; the outcome is unknown.",
    "The Lord of Heaven has awakened and regained strength, but says the process is incomplete; the Grand Mage awaits a command.",
    "The Main Quest “Rift and Collapse” failed; “The Foreordained Collapse” warns that player choices can cause irreversible consequences.",
    "Cheon Taemin remains unconscious in a secret facility beneath the Pentagon; Jin knows he is the Martial God and a former Player.",
    "An alert reported Alpha's awakening; what Alpha is and what its awakening means remain unknown."
  ],
  "continuity_sources": [
    1183,
    1182
  ],
  "open_questions": [
    "Why did the Murim Alliance and Imperial Guards miss the rendezvous?",
    "What does it mean for Taekyung to be the main attack, and why was the plan concealed from him?",
    "What caused Taekyung's chest pain and sleeplessness?",
    "What command will the Lord of Heaven give the Grand Mage, and what remains to be completed?",
    "What is Alpha, and what does its awakening mean?"
  ],
  "safe_through": 1183,
  "temporary_decisions": [
    "Render 대인 as Great Sir, following the established glossary."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 궁성     | **Bow Saint**                 | —              |
| 살성     | **Slaughter Saint**           | —              |
| 암천     | **Dark Heaven**                  |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 노부      | **this old man / I**                                            |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 벽곡단 | **fasting pills** | Food-substitute pills found in the hidden cave where Cheol trained. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 와이번 | **Wyvern** | High-tier dragonkin monster. |
| 중독 | **Poisoned** | System status abnormality caused by the poisons. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 만독지환 | **Myriad-Poison Ring** | Quest title concerning a legendary treasure said to detoxify any poison. |
| 대적자 | **the Adversary** | Ancient human enemy remembered by the Arch Lich. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 신강 | **Xinjiang** | Region beyond Qinghai described as the domain of the Demonic Path. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
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
| 송일 | 진태경 | hostile Zhongnan Elder to accused outsider | you / Jin Taekyung | hostile and threatening | Song Il questions Taekyung's identity and later threatens him over Gong Ilhyuk's injury. |
| 송일 | 청풍 | hostile Zhongnan Elder to younger martial artist | Sword Saint's heir / you | hostile and threatening | Song Il identifies Cheongpung as the Sword Saint's heir and demands that he face the consequences of injuring Gong Ilhyuk. |
| 송일 | 적천강 | former rescued junior to former rescuer | Great Hero Jeok | formal, fearful, and defensive | Uses 적 대협 while insisting that Jeok has no business interfering in the dispute. |
| 적천강 | 송일 | former rescuer to former rescued junior | Zhongnan brat; you; insolent bastard | blunt, mocking, and humiliating | Jeok recalls Song's youthful arrogance and addresses him with contempt while publicly disciplining him. |
| 궁기방 | 진태경 | rival_finalists | you bastard | insulting-casual | Gung Gibang answers Taekyung's collective insult with a profane threat. |
| 진태경 | 궁기방 | rival_finalists | you three idiots | insulting-casual | Taekyung addresses Gung Gibang as part of the trio and threatens them before a duel. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 궁기방 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Gung Gibang among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 청풍 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Cheongpung among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 송일섬 | 궁기방 | senior_martial_artist_to_Beggars_Sect_successor | Successor Beggar | blunt and irritated | Uses 후개 while objecting to Gung Gibang’s spitting and insults. |
| 궁기방 | 송일섬 | Beggars_Sect_successor_to_young_escort_captain | Young Hero Song | casual and admiring | Uses 송 소협 while praising the famous Soul-Chasing Guest and comparing their looks. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |
| 적천강 | 궁기방 | overwhelming_elder_to_younger_martial_artist | you | blunt and threatening | Jeok Cheongang rebukes Gung Gibang for speaking informally and orders him to lie down. |
| 진태경 | 송일섬 | pavilion master to prospective member | Song Ilseom | direct and evaluative | Taekyung directly names Song Ilseom while comparing his qualifications with Hwaran's. |
| 혁무진 | 송일섬 | pavilion_member_to_escort_captain | Great Hero Song | formal and deferential | Mujin addresses Song Ilseom while commenting on his broad experience. |
| 혁무진 | 주화란 | Fire Dragon Pavilion member to fellow member | Young Lady Ju | polite and deferential | Mujin addresses Hwaran as 주 소저 while asking her to call a physician. |
| 주화란 | 적천강 | younger ally to legendary martial master | Great Hero Jeok | formal and deferential | Ju Hwaran addresses Jeok as 적 대협 while asking whether he is all right. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 신의 | 주화란 | senior physician to younger ally | Young Lady Ju | warm and teasing | The Divine Physician lightly teases Hwaran about being more worried for Jin than he is. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 황제 | 신의 | Emperor addressing a physician | Divine Physician | direct and familiar | The Emperor asks whether the Divine Physician left something behind. |
| 신의 | 황제 | physician addressing his patient and sovereign | Your Majesty | formal and deferential | The Divine Physician addresses the Emperor as 폐하 while explaining the treatment. |
| 살성 | 청풍 | senior martial figure to younger companion | you | blunt and familiar | The Slaughter Saint scolds Cheongpung for disappearing without a word. |
| 청풍 | 살성 | younger companion to senior martial figure | old man | polite and familiar | Cheongpung apologizes and explains why he wandered off. |
| 송일섬 | 혁무진 | Older fellow Pavilion member and martial senior | you | casual and informal | Song insists that his age and martial experience entitle him to speak casually to Mujin. |
| 궁성 | 살성 | allied martial masters | Slaughter Saint | formal-polite | The Bow Saint directly addresses him as 살성 and uses 당신 while urging him to stay and defend the South Gate. |
| 살성 | 적천강 | familiar peer and fellow martial master | you | familiar and teasing | Uses 자네 while teasing Jeok and reassuring him. |
| 적천강 | 살성 | familiar fellow martial master | you | familiar, insulting-casual | Trades teasing insults with the Slaughter Saint over who is welcome in Taekyung’s carriage. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 1180
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, Sword Saint Mae Jonghak’s grandson and Disciple, a Supreme Peak master known as the Huashan Divine Dragon, creator of Mimi Step, and master of the Azure Dragon Pavilion; he has mastered the Slaughter Saint’s Ghost Illusory Slaughter Step and blended it with his Dark Fragrance Drift.
- **Personality:** Affable, dreamy, and childlike, with innocent curiosity, a deep love of martial arts, and compassion; guided by his grandfather’s righteousness and Taekyung’s chivalry, he meets danger with resolve and trusts Taekyung without wavering.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions; Taekyung is his true martial rival and the person whose way of life he admires, and the Slaughter Saint is his mentor in concealment and Ghost Illusory Slaughter Step.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1183
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 1135
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered, but grieves deeply for fellow Beggars’ Sect disciples and defends those who risk their lives for others.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun, and shares a blunt, teasing friendship with Taekyung.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1183
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and Vice Captain of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is deeply loyal to Taekyung, who trusts him as a close companion and values him as family, and has a warm friendship with fellow Fire Dragon Pavilion member Taishan; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Pavilion members accompanying Taekyung, and his parents own the Hyuk Family Textile Shop, which his younger sibling may inherit.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1183
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and follows his own path rather than pursuing grand causes; though he turned his back on the world, he wants Taekyung to pursue righteousness, practice chivalry, and win people’s hearts, and fiercely protects those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, and shares familiar, teasing camaraderie with the Slaughter Saint; he accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1183
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and eleventh member of the Ten Kings, a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; he serves as Thousand Captain of the Embroidered Uniform Guard, is enfeoffed as Prince Shangshan, and is widely regarded as a new-age savior.
- **Personality:** Hungry, self-aware, and dryly observant, he is pragmatic and fiercely defiant; he protects those he cherishes and meets mounting responsibility with hope and a determination to endure.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother and Jeok Cheongang his Master and trusted confidant; he shares deep loyalty with Hyuk Mujin, whom he values as family, and considers the revived Undead King, formerly the Skeleton King, a friend.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1183
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 1178
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, and filial; remains controlled under pressure but has grown more assertive and openly impatient after the hardships she has endured.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 1138
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect, known as the Roaring Fury Swordsman and one of Sect Leader Gong Iljung’s two Senior Brothers.
- **Personality:** Arrogant and domineering, but capable of remorse over choices that harmed his sect and those he failed to protect.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 1138
- **Aliases:** Escort Captain Song
- **Role:** Song Ilseom is a Level 110 escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Direct and rough, with dry, matter-of-fact teasing among allies and forceful urgency in command.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

## Korean source

```text
＃1184화



“우리가…… 아니, 네가 주공(主攻)이다.”

“……!”

적천강의 나직한 음성이 귓가를 파고든 순간, 진태경의 신형이 덜컥 굳었다.

동시에 그의 머릿속을 뿌옇게 물들이고 있던 안개가 비로소 걷히기 시작했다.

그러나 그의 바람과는 반대로, 그렇게 안개 밖 너머로 드러나기 시작한 현실의 풍경은 그리 희망차지도 아름답지도 않았다.

“그게, 그게 무슨 뜻입니까.”

본래 질문의 본질은 의문이며, 그것이 추구하는 목적은 의문을 해소할 명쾌한 해답이다.

하지만 적천강은 알고 있었다.

지금 진태경이 던진 저 질문에는 의문 대신 부정만이 가득하다는 것을.

자신의 입을 통해 이 믿고 싶지 않은 현실을 부정하고자 한다는 사실을.

“이미 알고 있지 않느냐. 노부가 무슨 말을 하는 것인지.”

늙은 스승은 깊게 가라앉은 눈빛으로 제자를 바라보았다.

그리고 천천히, 힘을 실어 말을 이었다.

“전부 우리를, 너를 위한 것이었다.”

“……그렇다는 건 설마.”

“신강은 암천(暗天)의 영역이다. 아니, 비단 이 땅뿐만이 아니었지. 지금껏 놈들의 눈과 귀는 천하 어디에나 숨어 있었고, 우리는 모든 가능성을 생각해야 했다.”

뭉쳐진 것은 단단하고, 흩어진 것은 무르다.

그럼에도 그들이 십만이 넘는 강대한 군세를 굳이 세 갈래로 나눈 것은, 단지 보급이나 진군 속도와 같은 현실적인 문제 때문만은 아니었다.

“만일의 상황을 대비하여 끝까지 숨겨야만 했다. 마지막 비수 하나만큼은.”

그 비수의 이름은 진태경이다.

세상에서 제일 날카롭지도, 가장 귀한 것도 아니지만 암천을 상대로는 그 무엇보다 치명적인 무기.

아니 어쩌면, 하늘이 선택한 천주(天主)의 유일한 대적자.

“그렇기에 모두가 동의했다. 검성도, 황제도. 그리고…….”

적천강이 고요해진 좌중을 바라보며 덧붙였다.

“우리도.”

진태경은 그제야 불현듯 깨달았다.

이 자리에 모여 있는 일행 중 그 누구도 지금의 이 상황에 이의를 제기하지 않았다는 사실을.

살성과 궁성. 주화란과 송일섬. 청풍, 궁기방, 심지어는 혁무진까지.

그들은 어두운 얼굴로 말없이 진태경을 바라보거나, 혹은 차마 시선을 마주하지 못한 채 고개를 떨구고 있었다.

“저를 속였군요. 처음부터.”

“미안하구나.”

적천강은 사과했다. 만약 그를 조금이라도 아는 누군가가 보았다면 눈과 귀를 의심했을 만큼 진심 어린 태도로.

하지만 진태경에게는 사과 한마디로 끝낼 수 있는 일이 아니었다.

십만.

무려 십만이 넘는 생명이 아직 저 창밖 어둠 너머에 있다.

그리고 이제는 생사(生死)를 알 수 없는 그들 중에는, 시간보다 깊은 정을 나눈 사람들이 있었다.

등을 맡길 수 있는 전우, 기꺼이 목숨을 내놓을 수 있는 벗, 비록 피는 섞이지 않았으나 이제는 진정 가족과도 같은 형제까지.

“돌아가겠습니다.”

억눌린 음성과 함께 진태경은 자리에서 일어났다.

생각지도 못한 이야기를 들은 충격 때문인지 속이 울렁거리고 현기증이 일었지만, 그는 이를 악물었다.

지금이라도 돌아가 그들을 구해야만 했다. 찾아야 했다.

……그 시신들만이라도.

하지만 그가 미처 발걸음을 떼기도 전, 재차 들려온 적천강의 목소리가 진태경의 앞을 가로막았다.

정확히는, 얼어붙어 있던 그의 마음을 후려쳤다.

“우리에게 그럴 수 있는 시간이 남아 있었더냐.”

“……!”

“약속했던 시일은 지났고, 더는 망설일 수 없다. 여기서 조금이라도 더 지체한다면 뒷일은 더욱 걷잡을 수 없게 되겠지.”

그것은 단순한 말이 아닌 현실이었다.

그 누구보다 진태경 자신이 잘 알고 있는, 냉혹하기 그지없는 현실.

거대한 둑이 허물어지듯 이미 모든 것은 붕괴하고 있다.

현대도, 무림도.

퀘스트를 깨기 전까지 두 세상을 연결하는 다리는 이어지지 않을 것이며, 이미 한참이나 뒤집혀 버린 시간의 흐름은 무엇으로도 되돌릴 수 없다.

아니, 한 가지 방법만이 남아 있다.

눈을 감고, 입을 다문 채 그저 앞으로 나아가는 것.

그리고 이 여정의 끝에서 기다리고 있을 모든 재앙의 근원, 천주를 쓰러트리는 것.

하지만…….

‘설령 그렇게 모든 일을 성공적으로 마무리 짓는다 해도, 나는 죽을 때까지 후회하겠지.’

새로운 인류의 구원자로 칭송받고, 막대한 부와 명예를 움켜쥐더라도 그 사실은 달라지지 않을 것이다.

세상 모든 것을 손에 넣을 수 있겠지만, 그것들은 모래알처럼 손가락 사이로 빠져나갈 것이 분명했다.

진태경은 이미 많은 것을 이루어낸 현재까지도 종종 악몽을 꾸곤 하니까.

지금이라면 일격에 죽일 수도 있는 블랙 와이번의 포효에 몸을 떨고, 동료들의 비명이 끝없이 울려 퍼지던 그 어두컴컴한 동굴을 헤매곤 하니까.

그렇기에 진태경은 결정했다.

“죄송합니다.”

그는 마음을 굳혔다.

하루, 혹은 반나절의 거리만이라도 되돌아가 보기로.

설령 그 반나절로 인해 모든 것이 어그러진다면, 그저 빌어먹을 운명으로 받아들일 생각이었다.

가장 가까웠던 몇 사람조차 구하지 못한다면, 그것이야말로 신이라 불리는 존재가 벌이는 미친 장난질에 불과할 테니까.

그리고 이와 같은 제자의 모습에, 적천강은 씁쓸한 어조로 뇌까렸다.

“그래, 결국 이렇게 되었구나.”

“아시잖아요. 제가 어떤 놈인지.”

“알지. 그러니 네 녀석을 제자로 삼았던 것이고.”

스승에게서 느껴지는 진심에, 진태경이 희미하게 웃었다.

“금방 돌아오겠습니다.”

“미안하게 되었다.”

진태경은 고개를 저었다.

스승에게 말해 주고 싶었다.

이건 그 누구의 잘못도 아니라고. 단지 선택의 문제였을 뿐이니, 사과할 필요 없다고.

하지만 어째서인지 그 말은 입술 밖으로 새어 나가지 못했고, 이미 한 번 내디딘 걸음은 두 번째로 이어지지 못했다.

‘뭐지?’

자연스럽게 떠오른 의문과 함께, 진태경은 가쁜 호흡을 내뱉었다.

어느샌가 심장이 미친 듯이 뛰고 있었다.

눈가는 횃불로 지지는 것처럼 뜨겁게 달아오르고, 시야는 한낮의 사막보다 더한 아지랑이로 물들었다.

그리고 온통 휘어지고 출렁이는 그 세상 속에서, 생각지도 못한 누군가의 목소리가 메아리처럼 울려 퍼졌다.

“흥분할 필요 없다. 금세 편안해질 테니.”

담담한 어조와 착잡한 눈빛.

비록 극심한 혼란에 빠진 상황이었으나, 목소리의 주인을 알아보는 것은 그리 어려운 일이 아니었다.

“도대체…… 왜?”

간신히 쥐어 짜낸 그 물음에, 살성은 조금 전 진태경이 했던 말을 고스란히 되돌려주었다.

“알고 있었으니까. 네가 어떤 녀석인지.”

“……!”

“혹여 나중에라도 혁가 놈은 탓하지 말거라. 저놈도 상관을 닮아 어찌나 고집이 쇠심줄 같던지, 설득만 한 세월이 걸렸다.”

살성의 어깨 너머로 고개를 푹 숙이고 있는 혁무진을 보자, 진태경은 그제야 모든 상황을 이해할 수 있었다.

구태여 찾아와 복용을 확인했던 녀석의 묘한 태도도, 살성이 만들었다는 특제 벽곡단의 정체도.

‘독?’

하지만 어딘지 모르게 이상했다.

만약 독에 중독되었다면 즉시 시스템 경고가 울렸을 테고, 손가락에 끼워져있는 만독지환(萬毒指環)의 해독 효과가 발동되었을 테니까.

그리고 이러한 진태경의 의문은 매우 합당한 것이었다.

다만, 신의(神醫)라는 또 다른 이름을 지닌 상대 역시 그 사실을 너무나도 잘 알고 있다는 것이 문제였을 뿐.

“독과 약은 본래 한 몸이라, 아주 미세한 차이로 그 경계가 나뉘는 법이지.”

바로 그 ‘아주 미세한 차이’로 독에 가까운 약을 만들어낸 장본인은 작게 한숨을 내쉬며 덧붙였다.

“이렇게까지 하기는 싫었다. 진심으로.”

진태경이 갈라진 목소리로 대꾸했다.

“이해합니다.”

“그렇게 말해 주니 다행이군.”

“그러니, 저도 이해해 주셨으면 합니다.”

“그게 무슨-”

이상함을 느낀 살성이 반문하려던 그 순간.

후웅!

묵직한 파공성과 함께, 진태경이 내뻗은 일권(一拳)이 그의 눈앞으로 성큼 들이닥쳤다.

퍼어엉!

벼락처럼 허공을 후려친 주먹을 따라 압축된 공기가 폭발하고, 휘몰아친 바람이 바닥에 쌓여 있던 먼지들을 일으켜 세웠다.

가까스로 신형을 뒤집어 공격을 피해 낸 살성이 눈을 부릅떴다.

‘분명 몸도 제대로 가누지 못할 텐데, 어떻게?’

사실상 중독된 것이나 다름없는 상태라는 것이 믿어지지 않을 정도의 힘과 속도.

하지만 앞서 살성이 했던 것과는 달리, 진태경은 상대의 의문을 해결해 줄 생각 따윈 없었다.

정확히는 그럴 만한 여유가 없었다.

당황한 살성을 뒤로한 채, 자욱하게 솟아오른 먼지구름을 뚫고 창가로 쇄도하는 그의 신형을 또 다른 누군가가 가로막았으니까.

쉬이이잉!

번뜩이는 두 줄기의 섬광.

그 끝에는 무쇠로 이루어진 바위도 단숨에 쪼개버릴 힘과 기세가 실려 있었으나, 진태경은 한 치의 망설임도 없이 상반신을 틀었다.

마치 그 모든 걸 예측한 것처럼.

스아악.

소름 끼칠 만큼 낮은 소음과 함께 스쳐 지나가는 칼날.

그리고 동시에 이루어진, 출수(出手).

콰앙!

쌍장(雙掌)과 쌍도(雙刀)가 부딪혔다. 

포탄이 터지는 듯한 굉음과 함께, 부르르 떨리는 곡도의 도신 위로 침잠하게 가라앉은 궁성의 눈동자가 비쳤다.

“그만두거라.”

진태경은 대답 대신 이를 악물었다.

으득.

어금니를 통해 전해지는 통증이 꺼져 가던 정신을 다시금 일깨운다. 아직 잠들지 않은 육신에 불을 지핀다.

드드득.

도신과 맞닿은 손바닥이 나아갔다.

동시에 두꺼운 장포로도 그 윤곽을 가릴 수 없는, 완벽하면서도 거대한 근육이 꿈틀거리자 궁성의 몸이 애병과 함께 서서히 밀려나기 시작했다.

실로 태곳적 거인과도 같은 힘. 그리고 꺼지지 않는 의지력.

하지만 딱 거기까지였다.

그의 마음이, 육신이 버틸 수 있었던 것은.

“미안하구나. 진정으로.”

등 뒤에서 들려온 적천강의 젖은 음성을 듣는 순간, 진태경은 몸 안에서 용암처럼 들끓어 오르던 모든 힘이 차갑게 식는 것을 느꼈다.

동시에 시야만큼이나 흐려진 얼굴들이, 그들과 함께했던 기억이 하나둘씩 떠올라 눈 앞을 가렸다.

그 어떤 안개와 먼지구름보다도 자욱하고, 희뿌옇게.

툭, 투둑.

어디서 떨어졌는지 모를 빗물이 바닥을 적셨고, 늙은 스승은 마침내 허물어지는 제자의 신형을 받아 들었다.
```

## Final English reading copy

```markdown
# Chapter 1184

“We… No. You’re the main attack.”

“……!”

The moment Jeok Cheongang’s quiet voice pierced his ears, Jin Taekyung’s body went rigid.

At the same time, the fog clouding his mind finally began to lift.

But contrary to his hopes, the reality emerging beyond that fog was neither hopeful nor beautiful.

“What… what do you mean?”

A question was meant to express uncertainty, to seek a clear answer that would resolve it.

But Jeok Cheongang knew.

There was no uncertainty in the question Jin Taekyung had just asked. Only denial.

He was trying to use his own words to deny a reality he didn’t want to believe.

“You already know what this old man means.”

The old master looked at his Disciple with a grave expression.

Then he slowly continued, putting weight behind each word.

“Everything was for us. For you.”

“……You mean—”

“Xinjiang is Dark Heaven’s domain. No, it wasn’t only this land. Their eyes and ears have been hidden everywhere under Heaven. We had to consider every possibility.”

Things gathered together are strong; things scattered apart are weak.

Even so, they hadn’t divided their mighty army of more than a hundred thousand into three forces solely for practical reasons like supplies or marching speed.

“We had to keep it hidden until the very end, in case of the worst. We had to save one last dagger.”

That dagger was Jin Taekyung.

Not the sharpest in the world, nor the most precious—but against Dark Heaven, a weapon more lethal than any other.

No. Perhaps the Lord of Heaven’s only Adversary, chosen by Heaven itself.

“That’s why everyone agreed. The Sword Saint, the Emperor. And…”

Jeok Cheongang looked around at the silent group and added,

“We did, too.”

Only then did Jin Taekyung suddenly realize that not one person gathered here had objected to what was happening.

The Slaughter Saint and the Bow Saint. Ju Hwaran and Song Ilseom. Cheongpung, Gung Gibang, even Hyuk Mujin.

They either looked at Jin Taekyung in silence, faces dark, or lowered their heads, unable to meet his eyes.

“You deceived me. From the very beginning.”

“I’m sorry.”

Jeok Cheongang apologized with such sincerity that anyone who knew him even a little would have doubted their own eyes and ears.

But an apology wasn’t enough to make this right.

A hundred thousand.

More than a hundred thousand lives were still out there, beyond the darkness outside the window.

Among them were people whose bonds with him ran deeper than time itself—people whose fate was now unknown.

Comrades he could trust with his back. Friends he’d gladly lay down his life for. Brothers who weren’t related by blood, but had become true family all the same.

“I’m going back.”

With a strained voice, Jin Taekyung rose from his seat.

Shock from the unexpected revelation churned his stomach and made his head spin, but he gritted his teeth.

He had to go back now and save them. Find them.

……Even if all he could find were their bodies.

But before he could take a step, Jeok Cheongang’s voice stopped him again.

Or rather, it struck his frozen heart.

“Did we have time to do that?”

“……!”

“The agreed date has passed. We can’t hesitate any longer. If we delay even a little more, what comes after will be even more impossible to control.”

It wasn’t just something he’d said. It was reality.

A merciless reality Jin Taekyung understood better than anyone.

Everything was already collapsing, like a massive dam giving way.

The modern world. Murim.

Until the Quest was cleared, the bridge between the two worlds wouldn’t be connected. And the flow of time, already thrown far out of alignment, couldn’t be turned back.

No. There was only one way left.

Close his eyes, keep his mouth shut, and move forward.

Then, at the end of this journey, defeat the source of every disaster waiting there: the Lord of Heaven.

But…

*Even if I bring everything to a successful end, I’ll regret this for the rest of my life.*

That wouldn’t change even if he were hailed as the savior of a new humanity and seized immense wealth and fame.

He might gain everything in the world, but it would all slip through his fingers like sand.

Even now, after achieving so much, Jin Taekyung still sometimes had nightmares.

He still trembled at the roar of the Black Wyvern, which he could now kill with a single strike. He still wandered through that dark cave, where the screams of his companions had echoed without end.

And so, Jin Taekyung made his decision.

“I’m sorry.”

He steeled himself.

He would go back, even if only half a day or a day’s distance.

Even if that half day threw everything into disarray, he would accept it as a damnable twist of fate.

If he couldn’t save even the few people closest to him, then it would be nothing but the insane game of a being called a god.

Watching his Disciple, Jeok Cheongang muttered in a bitter voice,

“So, in the end, this is how it happens.”

“You know what I’m like.”

“I do. That’s why I took you as my Disciple.”

Feeling the sincerity in his master’s voice, Jin Taekyung smiled faintly.

“I’ll be back soon.”

“I’m sorry.”

Jin Taekyung shook his head.

He wanted to tell his master that none of this was anyone’s fault. It was simply a matter of choice; there was no need to apologize.

But for some reason, the words wouldn’t pass his lips. And the step he’d already taken wasn’t followed by another.

*What’s going on?*

The question came naturally, and Jin Taekyung breathed hard.

At some point, his heart had started pounding like mad.

His eyes burned as if torches were being pressed against them, and his vision shimmered with heat haze more intense than in the midday desert.

Then, in that world, warped and rippling all around him, an unexpected voice echoed like a distant call.

“No need to get worked up. You’ll feel peaceful soon.”

A calm tone. A troubled look.

Though he was in the middle of overwhelming confusion, it wasn’t hard to recognize the speaker.

“Why…?”

In answer to the question he’d barely managed to force out, the Slaughter Saint returned the very words Jin Taekyung had spoken a moment ago.

“Because I knew what kind of person you are.”

“……!”

“And don’t blame that Hyuk brat later. He was just as stubborn as his superior. It took me ages just to convince him.”

When Jin Taekyung saw Hyuk Mujin with his head bowed over the Slaughter Saint’s shoulder, he finally understood what was going on.

The strange way Mujin had insisted on checking that he’d taken the pill. The special fasting pills the Slaughter Saint had made.

*Poison?*

But something didn’t feel right.

If he’d been poisoned, the System would have warned him immediately, and the detoxification effect of the Myriad-Poison Ring on his finger would have activated.

His suspicion was entirely reasonable.

The problem was that his opponent, who was also known as the Divine Physician, knew that all too well.

“Poison and medicine are one and the same. It takes a very fine line to separate them.”

The man who’d used that “very fine line” to make a medicine almost indistinguishable from poison sighed softly and added,

“I didn’t want to go this far. I truly didn’t.”

Jin Taekyung answered in a hoarse voice.

“I understand.”

“I’m glad you can say that.”

“Then I hope you’ll understand me, too.”

“What do you—”

The Slaughter Saint was about to ask what he meant when—

*Whoom!*

With a heavy rush of air, Jin Taekyung’s fist came hurtling toward his face.

*Boom!*

The compressed air exploded as his fist struck through the space like lightning. The resulting gust whipped up the dust that had settled on the floor.

The Slaughter Saint twisted around just in time to evade the attack, his eyes wide.

*He can barely keep his body steady. How could he—?*

The strength and speed were hard to believe from someone practically in a poisoned state.

But unlike the Slaughter Saint, Jin Taekyung had no intention of answering his question.

To be exact, he didn’t have the time.

Another figure blocked his way as he rushed toward the window, cutting through the thick cloud of dust behind the startled Slaughter Saint.

*Shing!*

Two streaks of light flashed.

At their tips lay enough force and momentum to cleave through a boulder of solid iron in a single stroke, but Jin Taekyung twisted his upper body without a moment’s hesitation.

As if he’d predicted it all.

*Shhk.*

A blade passed by with a sound low enough to raise goose bumps.

And in the same instant, he struck back.

*Crash!*

Both his palms slammed into her twin sabers.

With a boom like an exploding cannonball, the Bow Saint’s sunken eyes appeared reflected on the trembling blade of her curved saber.

“Stop.”

Jin Taekyung answered by gritting his teeth.

*Crk.*

The pain in his jaw jolted his fading consciousness awake. It set fire to a body that had yet to fall asleep.

*Grind.*

His palm pushed against the blade.

At the same time, the Bow Saint began to slide backward with her treasured weapon as Jin Taekyung’s perfect, massive muscles flexed—too large to hide even beneath his thick robe.

It was a strength worthy of an ancient giant. A will that refused to die.

But that was as far as he could go.

As far as his heart and body could endure.

“I’m sorry. Truly.”

The moment Jeok Cheongang’s tearful voice came from behind him, Jin Taekyung felt every bit of the strength boiling inside him like lava turn cold.

At the same time, faces blurred like his vision, and memories of the time they’d spent together rose one after another, clouding his eyes.

Thicker and whiter than any fog or cloud of dust.

*Drip. Drip.*

Rainwater fell from somewhere, wetting the floor, and the old master finally caught his Disciple as his body collapsed.
```
