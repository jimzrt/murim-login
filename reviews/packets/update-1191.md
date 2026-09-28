<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1191.txt",
      "sha256": "349f35e810231403793bbd1aa218af8184189dfff6f97e0269b854ae9c608515",
      "bytes": 13682
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "d43f3af95ed47fb024f79e805adf6b8ec7a99ec6940d220a78d2a1997a97a60d",
      "bytes": 1880
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0821386659bc3addb778ca5fcefcff90bf100119ece13916b00f44e929e9de3b",
      "bytes": 248927
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "08b5d8bf11fa10414dccade48872845f0d465178b90bc8959bd9d1d9bf56bfeb",
      "bytes": 1230
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "d1b0010e141f34bed2235b006e143be549e71e7ff0f0c543b7784246fdbd5cc7",
      "bytes": 684
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "ee8e9f56f718ae34df042487ef90c8e8eb2bbeaaecb3a1f9702d94d18ad69a5c",
      "bytes": 1393
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "20c4ca5e837dce406581c89d30f20a37e8671e4f6c131a70bdc9bd3dfed08ffd",
      "bytes": 1802
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "1c95dc747bc96ce64dc8818d1718e2d009c4df1aa186c1a11d129c891528f8eb",
      "bytes": 1550
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "23c1839d260fac67a2b4b0df7006dd8b0e7493cd3e4659bdec1e10b8f86fe36b",
      "bytes": 623
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "3346e46b9642f5586df4a36b72f9a317c73dee19589ad15aab65075444e07818",
      "bytes": 974
    },
    {
      "path": "characters/Morgoth.md",
      "sha256": "841912084a5efda5ebac0c1abf42e806d821f87ceab996d26ed854f64e078f1c",
      "bytes": 853
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "27d613139df10edfe20e7e75a2745ea939252247aa4aa212420a0f207100462e",
      "bytes": 774
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "862b1050b892c90e7f358b90c56814642f02130d8baee461ff08d500a54f81ca",
      "bytes": 980
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "6592233b34dcd7f1d0f74935310ed387046c3f86f1869fa5f218139dd6824a3a",
      "bytes": 295903
    }
  ],
  "estimated_tokens": 14606
}
-->

# Durable State Update — Chapter 1191

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
1 and safe_through 1191. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1191. Profile updates may replace only one
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
  "chapter": 1191,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1191,
    "continuity_sources": [1191],
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
    "Jeok Cheongang and Jin Taekyung cleared the mutated Gate Forest of Death-I in the Tianshan Mountains; the Black Ghosts and monsters there were defeated.",
    "Taekyung leveled up and recovered from status ailments and fatigue after clearing the Gate.",
    "The last Black Ghost said that “that person” was waiting for Taekyung; the figure’s identity and purpose remain unknown.",
    "Jeok regards the Black Ghost’s remains as an empty shell of a boy who had once been someone’s joy and reason for living, and now feels able to let him go.",
    "The other separated companions’ status remains unknown.",
    "The Lord of Heaven has awakened and regained strength, but says the process is incomplete; the Grand Mage awaits a command.",
    "Cheon Taemin remains unconscious in a secret facility beneath the Pentagon; Jin knows he is the Martial God and a former Player.",
    "An alert reported Alpha’s awakening; what Alpha is and what its awakening means remain unknown.",
    "Taekyung has experienced unexplained chest pain and difficulty sleeping; the Slaughter Saint also wondered whether he used his full strength while affected by the fasting pill."
  ],
  "continuity_sources": [
    1190,
    1189
  ],
  "open_questions": [
    "Who is “that person” waiting for Taekyung, and what do they want?",
    "What has happened to the separated companions?",
    "What is causing Taekyung’s chest pain and sleeplessness, and did he use his full strength against the fasting pill’s effects?",
    "What remains to be completed for the Lord of Heaven, and what command will he give the Grand Mage?",
    "What is Alpha, and what does its awakening mean?"
  ],
  "safe_through": 1190,
  "temporary_decisions": [
    "Render 진인사대천명 as “Do all that man can, then await Heaven’s will.”"
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
| 궁성     | **Bow Saint**                 | —              |
| 살성     | **Slaughter Saint**           | —              |
| 태원진가   | **Jin Family of Taiyuan**        |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 제자     | **Disciple**                                 |
| 은인     | **Benefactor**                               |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 보상               | **Reward**                     |
| 칭호               | **Title**                      |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 태원     | **Taiyuan**            |
| 본좌      | **I / this lord** only when deliberately grandiose              |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 소저      | **Young Lady**                                                  |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 모르고스 | **Morgoth** | The being who answers the summoning. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 후개 | **Successor Beggar** | Title of the Beggars' Sect successor competing in the preliminaries. |
| 천산 | **Tianshan** | Mountain region identified as the Demonic Cult's headquarters. |
| 천산산맥 | **Tianshan Mountains** | Mountain range associated with the Demonic Cult. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 무아지경 | **Trance** | State Taekyung briefly enters during the energy digestion. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 탈진 | **Exhaustion** | System status effect caused by exhausting all internal energy while severely injured. |
| 암초 | **reef** | Reefs blocking the narrow water route. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 모스크바 | **Moscow** | Russian city used in Taekyung's modern-world comparison. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 마계 | **Demon Realm** | Realm associated with the S-rank monsters and Leviathan. |
| 멸지 | **Land of Ruin** | Name used for the desert region beyond which Dark Heaven’s forces are approaching. |
| 무아 | **No-self** | The brief self-forgetting state the disciple mistakes for a breakthrough. |
| 흑귀 | **Black Ghost** | The Blood-Sword Demon Lord’s name for the Death Knights. |
| 대인 | **Great Sir** | Name used for the mysterious figure in Ningxia. |
| 흑룡공 | **Black Dragon Duke** | Title in Morgoth's System announcement. |
| 드래곤 | **Dragon** | The species to which Morgoth belongs. |
| 심안 | **Mind’s Eye** | Ability that activates under specific conditions and causes extreme fatigue. |

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
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |
| 적천강 | 궁기방 | overwhelming_elder_to_younger_martial_artist | you | blunt and threatening | Jeok Cheongang rebukes Gung Gibang for speaking informally and orders him to lie down. |
| 진태경 | 송일섬 | pavilion master to prospective member | Song Ilseom | direct and evaluative | Taekyung directly names Song Ilseom while comparing his qualifications with Hwaran's. |
| 혁무진 | 송일섬 | pavilion_member_to_escort_captain | Great Hero Song | formal and deferential | Mujin addresses Song Ilseom while commenting on his broad experience. |
| 적천강 | 의원 | interrogator_to_physician | you; quack | blunt and threatening | Jeok shakes the physician and demands an explanation for Jin's seven-day sleep before ordering him to summon the Beast Miao King. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 혁무진 | 주화란 | Fire Dragon Pavilion member to fellow member | Young Lady Ju | polite and deferential | Mujin addresses Hwaran as 주 소저 while asking her to call a physician. |
| 주화란 | 적천강 | younger ally to legendary martial master | Great Hero Jeok | formal and deferential | Ju Hwaran addresses Jeok as 적 대협 while asking whether he is all right. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 살성 | 청풍 | senior martial figure to younger companion | you | blunt and familiar | The Slaughter Saint scolds Cheongpung for disappearing without a word. |
| 청풍 | 살성 | younger companion to senior martial figure | old man | polite and familiar | Cheongpung apologizes and explains why he wandered off. |
| 송일섬 | 혁무진 | Older fellow Pavilion member and martial senior | you | casual and informal | Song insists that his age and martial experience entitle him to speak casually to Mujin. |
| 진태경 | 대인 | young martial artist to benefactor | you | casual and blunt | Taekyung asks who Great Sir is, addressing him as 당신. |
| 대인 | 진태경 | older benefactor to young martial artist | you | familiar conversational | Great Sir addresses Taekyung as 자네. |
| 청풍 | 대인 | younger companion addressing an older benefactor | Uncle Great Sir | polite and familiar | Cheongpung repeatedly calls him 대인 아저씨. |
| 대인 | 청풍 | older benefactor addressing a younger companion | you | familiar and teasing | Great Sir addresses Cheongpung as 자네. |
| 궁성 | 살성 | allied martial masters | Slaughter Saint | formal-polite | The Bow Saint directly addresses him as 살성 and uses 당신 while urging him to stay and defend the South Gate. |
| 살성 | 적천강 | familiar peer and fellow martial master | you | familiar and teasing | Uses 자네 while teasing Jeok and reassuring him. |
| 적천강 | 살성 | familiar fellow martial master | you | familiar, insulting-casual | Trades teasing insults with the Slaughter Saint over who is welcome in Taekyung’s carriage. |
| 모르고스 | 진태경 | enemy Dragon addressing a human opponent | you | formal, measured | Uses 자네 while addressing Jin. |
| 진태경 | 모르고스 | human opponent addressing an enemy Dragon | son | casual and mocking | Calls Morgoth 아들. |
| 궁성 | 대인 | Acquaintances traveling together; Bow Saint is wary of the mysterious Great Sir. | you | polite, controlled | Bow Saint questions him formally and apologizes after mistaking him for an enemy. |
| 대인 | 궁성 | Acquaintances traveling together; Great Sir calls Bow Saint “Young Lady” and “heroine.” | Young Lady; heroine | polite conversational, familiar and teasing | He alternates respectful titles with candid personal questions. |
| 살성 | 진태경 | senior allied martial artist to younger companion | you | familiar and blunt | Addresses Taekyung with 너 and 네가 while explaining that he anticipated Taekyung’s response. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 1184
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, Sword Saint Mae Jonghak’s grandson and Disciple, a Supreme Peak master known as the Huashan Divine Dragon, creator of Mimi Step, and master of the Azure Dragon Pavilion; he has mastered the Slaughter Saint’s Ghost Illusory Slaughter Step and blended it with his Dark Fragrance Drift.
- **Personality:** Affable, dreamy, and childlike, with innocent curiosity, a deep love of martial arts, and compassion; guided by his grandfather’s righteousness and Taekyung’s chivalry, he meets danger with resolve and trusts Taekyung without wavering.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions; Taekyung is his true martial rival and the person whose way of life he admires, and the Slaughter Saint is his mentor in concealment and Ghost Illusory Slaughter Step.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 1187
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered, but grieves deeply for fellow Beggars’ Sect disciples and defends those who risk their lives for others.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun, and shares blunt, teasing friendships with Taekyung and Hyuk Mujin.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1187
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and Vice Captain of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is deeply loyal to Taekyung, who trusts him as a close companion and values him as family, and has warm friendships with fellow Fire Dragon Pavilion members Taishan and Gung Gibang; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Pavilion members accompanying Taekyung, and his parents own the Hyuk Family Textile Shop, which his younger sibling may inherit.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1190
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and follows his own path rather than pursuing grand causes; though he turned his back on the world, he wants Taekyung to pursue righteousness, practice chivalry, and win people’s hearts, and fiercely protects those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, and shares familiar, teasing camaraderie with the Slaughter Saint; he accepted Jangcheon as a Disciple before he became Jopil, later cast him out, and regards their failings toward each other as a debt to settle in another life; he was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1190
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and eleventh member of the Ten Kings, a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; he serves as Thousand Captain of the Embroidered Uniform Guard, is enfeoffed as Prince Shangshan, and is widely regarded as a new-age savior.
- **Personality:** Hungry, self-aware, and dryly observant, he is pragmatic and fiercely defiant; he protects those he cherishes and meets mounting responsibility with hope and a determination to endure.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother and Jeok Cheongang his Master and trusted confidant; he shares deep loyalty with Hyuk Mujin, whom he values as family, and considers the revived Undead King, formerly the Skeleton King, a friend.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1190
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 1187
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, and filial; remains controlled under pressure but has grown more assertive and openly impatient after the hardships she has endured.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Morgoth.md

# Morgoth (모르고스)

- **Safe through:** Chapter 1176
- **Aliases:** None
- **Role:** Morgoth was a Dragon Lord and sovereign of a vast palace, slain by Jin Taekyung when Jin pierced his Dragon Heart.
- **Personality:** Composed and intellectually curious, Morgoth spent millennia seeking God and regards powerful beings as sources of amusement, willing to aid a worthy rival when it promises greater future entertainment.
- **Voice:** He speaks in polished, measured phrasing, but can drop his courtesy for blunt, direct admissions when speaking sincerely.
- **Relationships:** Asmodeus summoned Morgoth, though Morgoth says he is not devoted to him; Morgoth returned the Skeleton King to Jin to help him grow stronger and commands seven soul-stolen S-rank Hunters as Guardians.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 1187
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect, known as the Roaring Fury Swordsman and one of Sect Leader Gong Iljung’s two Senior Brothers.
- **Personality:** Arrogant and domineering, but capable of remorse over choices that harmed his sect and those he failed to protect.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 1187
- **Aliases:** Escort Captain Song
- **Role:** Song Ilseom is a Level 110 escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Direct and rough, with dry, matter-of-fact teasing among allies and forceful urgency in command.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

## Korean source

```text
＃1191화



현실과 게이트를 잇는 유일한 길. 

마력장(魔力場)을 통과할 때의 감각은 베테랑 헌터인 나에게 있어 더없이 익숙하지만, 그럼에도 종종 몸서리칠 수밖에 없을 만큼 불쾌하다.

바로 지금처럼.

솨아아악.

소용돌이에 휩쓸린다면 이런 느낌일까.

마력 특유의 차갑고 끈적한 감각이 전신을 감싸고, 이내 저 너머의 어딘가로 토해 낸다.

그리고 새로운 공간에서 눈을 뜬 순간, 나는 지금껏 모르고 있던 한 가지 사실을 깨달았다.

‘다르다.’

빼곡하게 하늘을 뒤덮은 나뭇가지와 가파른 언덕.

사방을 메우고 있던 시체의 산과 핏물의 강도 더는 보이지 않는다.

하지만 뒤바뀐 것은 주위를 둘러싼 풍경만이 아니었다.

마력.

게이트를 빠져나옴과 동시에 깨끗이 떨어져 나갔어야 할 그 오물과도 같은 기운이, 아직도 몸뚱어리에 들러붙어 있다.

아니, 이 공간 전체에.

“이건…….”

신음처럼 흘러나온 무거운 목소리.

잠시 말을 잇지 못하는 내 모습에, 마력장의 불쾌한 감각에 진저리 치고 있던 적천강이 즉각 반응했다.

“왜 그러느냐?”

평소였다면 별거 아니라며 너스레를 떨었을 거다.

그러나 눈을 뜬 그 순간부터 오감을 통해 전해지는 짙은 기시감은 불과 몇 주도 채 지나지 않은 과거의 기억을 떠올리게 만들었고, 적천강은 이미 나에 관한 대부분의 진실을 알고 있다.

“이런 곳을 와 본 적이 있거든요. 그것도 아주 최근에.”

“아, 혹시?”

“예. 이번에 말씀드렸던 그 사건이요.”

문명을 집어삼키던 거대한 버섯구름. 생명의 흔적을 찾아볼 수 없던 대도시.

그리고 검게 죽은 대지 위, 새로이 우뚝 선 암흑의 성에서 나를 기다리고 있던 한 존재.

‘모르고스.’

맞다.

이곳은 흑룡공 모르고스가 모스크바의 폐허 위에 세운 드래곤 레어와 매우 흡사한 기운을 풍기고 있었다.

마계(魔界)라 불러도 이상하지 않은 정도의 기운을.

‘아니, 그 이상이야.’

적천강의 말에 의하면 내가 의식을 잃었던 시간은 하루 남짓.

이 정도로 순도 높은 마력은 드래곤 레어 가까이에 접근한 후에야 느꼈을 정도인데, 이미 주위에는 그때와 버금가는 힘이 들끓어 오르고 있었다.

‘이런 거였나. 시스템이 말한 제한구역의 의미가.’

이제야 알겠다.

온갖 허황된 소문들이 떠도는 곳이 무림이라지만, 이 지랄 같은 산맥에 관한 이야기만큼은 오히려 한없이 축소되었다는 것을.

오늘에서야 직접 보고 느낀 천산산맥은 말 그대로 금지(禁地)이자 멸지(滅地)였다.

주인에게 허락받지 않은 불청객은 들어가서도 안 되고, 나올 수도 없는.

그리고 이 끝없이 펼쳐진 어둠의 산맥은 좀처럼 자신이 온몸으로 가리고 있는 비밀을 드러낼 생각이 없어 보였다.

산맥의 주인은 물론, 나와 적천강을 제외한 또 다른 불청객들까지도.

“다른 사람들이 안 보이는군요.”

“괴이두(怪異竇)인지 뭔지 하는 것에 당했을 때부터 짐작은 했다만, 역시로군.”

침음성을 흘린 적천강이 주위에 흐르는 안개를 노려보았지만, 그런다고 사라진 사람들이 갑작스럽게 나타나진 않았다.

백 장 밖의 개미도 선명하게 파악할 정도의 안력(眼力)을 지닌 초인이라 할지라도, 사람의 눈으로 현실과 게이트 사이에 놓인 아공간을 꿰뚫어 볼 수는 없으니.

‘……그래, 그건 불가능하겠지.’

문득 뇌리를 스친 한 가지 생각과 함께, 마음속으로 덧붙였다.

‘사람의 눈으로는.’

지금 떠오른 이 방법이 성공할지는 확신할 수는 없다.

사실 냉정하게 확률만 따져보자면, 괜히 기력만 소모하는 자충수가 될 가능성이 더욱 크다.

하지만 눈앞에 놓인 길이 하나뿐이라면, 그리고 이미 그 길을 한번 지나간 적이 있다면 앞에 어떤 거대한 장애물이 가로막고 있더라도 부수며 나아가야 하지 않겠나.

우우우웅.

부르르 떨리기 시작한 공기 속, 나는 심호흡과 동시에 창날을 들어 올렸다.

하품이 나올 만큼 천천히, 몸 안에 웅크린 기운을 전신으로 퍼트리며.

아무런 예고 없이 벌인 이 행동에 적천강이 반응하는 것이 느껴졌으나 그것도 잠시뿐, 이내 온 사방이 고요해졌다.

정확히는, 최고조에 이른 집중력이 필요 없는 잡음을 포함한 모든 것을 지워냈다.

오직 단 하나의 목적을 위해서.

보이지 않는 장막 뒤에 숨겨진, 또 다른 공간들을 찾기 위해서.

그리고.

키이이이잉.

천둥과도 같은 이명(耳鳴)과 함께 불현듯 찾아온 끔찍한 두통이 눈앞을 새하얗게 물들인 그 순간.

띠링.

어디선가 희미하게 울려 퍼지는 맑은 종소리를 들으며, 나는 이 무모한 시도가 끝내 성공했음을 깨달았다.

인고 끝에 찾아온, 이 찰나의 틈새를 놓쳐선 안 된다는 사실도.

투둑, 툭.

안구의 실핏줄이 가닥가닥 터져나간 탓일까. 아니면 인지하지도 못한 새에 입술 사이로 흘러나오는 핏물 때문일까.

시야가 온통 붉다. 통증이 가슴과 뇌를 찌른다.

그러나 상관없었다.

이미 보았으니까. 읽었으니까.

‘벤다.’

참았던 숨을 내뱉으며, 나는 하늘 높이 솟아오른 창날을 내리그었다.

또 다른 눈, 심안(心眼)이 알려준 한 줄기의 길을 따라서.

스아아아악-

눈부신 섬광이 세상을, 보이지 않는 장막을 갈랐다.



* * *



- 상태 이상, [무아지경]이 해제되었습니다.



가장 먼저 진태경의 눈앞에 떠오른 한 줄의 메시지.

그것이 바로 신호탄이었다.

시스템 알림의 파도가 몰려오고 있음을 알리는 신호탄.

띠링. 삐빅.



- 특수 능력, [심안]의 발동 조건이 충족됨에 따라 해당 능력이 발동됩니다!

- [심안]에 대한 깨달음이 한층 깊어졌습니다.

- 항상 유의하십시오. 해당 능력은 사용자의 심신에 심각한 피해를 유발하며, 최악의 경우 죽음에 이를 수도 있습니다!

- 상태 이상, [탈진]이 적용되었습니다!

- 상태 이상, [극심한 피로]이 적용되었습니다!

- 상태 이상, [내상]이…….



.

.

.

진태경은 숨을 헐떡였다.

가슴이 답답하다.

차오르는 욕지기와 함께, 방향 감각을 상실한 몸뚱어리가 이리저리 흔들린다.

아지랑이처럼 일그러진 시야 너머로 불쑥 다가온 적천강이 부축과 함께 무어라 외쳤으나, 이미 망가진 감각은 그의 말과 손길을 제대로 받아들이지 못했다.

아주 잠시.

겹겹이 울려 퍼지는 종소리와 동시에 밀려온, 두 번째 파도가 그를 덮치기 전까지는.

띠링. 띠링. 띠링.



-변이 게이트, [죽음의 숲-Ⅱ]를 파괴했습니다!

-변이 게이트, [죽음의 숲-Ⅲ]를 파괴했습니다!

.

.



- 변이 게이트, [죽음의 숲-Ⅵ]를 파괴했습니다!

- 매우 희귀한 업적, [두드려라, 열릴 것이다]를 달성했습니다!

- 매우 희귀한 업적을 달성한 보상으로 막대한 경험치를 획득했습니다!

- 칭호, [문을 여는 자]를 획득했습니다!

- 레벨 업!

- 레벨 업의 효과로 모든 부상과 피로가 회복되었습니다!



하이 리스크 하이 리턴.

위험성이 큰 시도였던 만큼 그 대가는 충분했다.

흑귀를 몇 마리나 쓰러트려야 얻을 수 있는 경험치를 일거에 획득한 데다, 가장 중요한 목적을 달성했으니.

“도대체……!”

경악하는 스승의 모습에, 제자는 피에 젖은 입꼬리를 말아 올리며 웃었다.

“보시는 대로죠.”

그 말처럼, 일대를 둘러싼 변화는 이미 육안으로 확인할 수 있을 만큼 뚜렷했다.

그그그극.

아무것도 없이 텅 비어있던 허공이 일그러진다. 

흡사 억지로 무언가를 토해내는 괴물의 얼굴처럼.

그리고 이내.

솨아아악.

보이지 않던 여러 개의 틈새가 차례대로 아가리를 벌렸다.

그 안을 가득 채우고 있던 어둠을 울컥, 쏟아내며 감춰두었던 무언가를 함께 토해 냈다.

정확히는.

“으아아아! 이 거지만도 못한 개새끼들아!”

“오너라! 본좌는 대 태원진가가 자랑하는 최고의 협객 혁무……!”

자아비판을 서슴지 않는 한 명의 거지와, 소속 가문을 향한 불타는 애사심과 자기객관화를 엿 바꿔 먹은 어느 무인을.

“…….”

“…….”

“…….”

“…….”

숨 막히는 침묵 속, 대 태원진가가 자랑하는 최고의 협객이 무겁게 입술을 뗐다.

“속지 마라, 거지. 이건 모두 놈들의 사술이다.”

개새끼들보다 조금 나은 거지가 대꾸했다.

“내가 병신이냐? 이런 거에 속게. 이따위 수작은 진즉 꿰뚫고 있었다.”

“후후, 역시 개방의 후개답군.”

“너도 제법이군. 단번에 간파할 줄이야.”

그리고 아득한 눈빛으로 이 모든 광경을 지켜본 스승과 제자는 동시에 비슷한 생각을 떠올렸다.

‘저놈들, 다시 집어넣을 수는 없나?’

‘그냥 다시 집어넣을까.’

하지만 안타깝게도 그런 일은 벌어지지 않았다.

진지하게 방법을 고민해 보기도 전에 두 번째 균열이 열렸으니까.

솨아아.

힘없이 흩어지는 어둠 너머, 쇄도하듯이 모습을 드러낸 한 사내는 인상만큼이나 냉정한 눈빛으로 주위를 둘러보더니 이내 진태경을 향해 물었다.

“사술인가?”

“이 새끼도 지랄이네.”

숨도 쉬지 않고 돌아온 대답에 사내, 송일섬이 핏물이 뚝뚝 떨어지는 칼날을 늘어트렸다.

“진짜군.”

“살아 있어서 다행이네. 그나저나 주 소저는?”

“곧 나올 거다. 혹시 함정일 수도 있으니 내가 앞장섰거든.”

송일섬이 잠시 고민하더니 덧붙였다.

“고용주의 안전이 최우선이니까.”

“그건 안 물어 봤…… 아, 주 소저!”

“은인! 진 대협! 진 공자!”

앞의 세 사람과 달리, 뒤이어 모습을 드러낸 주화란은 한 치의 의심도 없이 진태경을 향해 달려갔다.

정확히는, 그러려고 했다.

만약 그 순간, 세 번째와 네 번째 균열이 동시에 열리지 않았다면.

“우와! 이렇게 기분 더러운 감각은 처음 느껴봐요!”

말과는 전혀 다른 산뜻한 목소리로 등장한 청풍에 이어, 마력과 한 몸이라도 되는 양 유령처럼 나타난 그림자는 즉각 행동으로 말을 대신했다.

슈확, 카아앙!

소리마저 앞질러 공간을 가로지른 섬광.

가공할 속도로 쏘아진 비수를 단숨에 튕겨낸 진태경이 어깨를 으쓱했다.

“그냥 말로 하시지, 뭘 또 이렇게까지.”

“항상 주위의 모든 것에 의심을 품어야 한다는 건 살수와 의원의 몇 안 되는 공통점이지. 의심할수록 실수가 줄어드니까.”

“그래서, 의심은 풀리셨습니까?”

“적어도 지금 보고 있는 현실에 대한 의심은 풀린 것 같군.”

살성이 이채 띤 눈빛으로 진태경을 바라보았다.

“정작 나 자신에 대한 의심은 깊어졌지만. 도대체 어떻게 벌써 깨어난 거지?”

“네놈이 돌팔이라서.”

“그냥 뭐, 보통이죠. 천무지체에 이 정도 무공이면 다들 할 수 있는 거잖아요.”

“…….”

조롱과 거만으로 가득 찬 두 사승의 대답에 살성이 두 눈을 질끈 감은 그때, 마지막 다섯 번째 균열에서 한 사람이 모습을 드러냈다.

다른 이들과 달리 서두르지도, 은밀하지도 않은 발걸음과 피 한 방울 묻어 있지 않은 의복과 피부.

하지만 그녀, 궁성의 눈빛만큼은 평소와 달랐다.

격랑.

아주 잠시뿐이었으나, 몇몇 사람은 똑똑히 보았다.

언제나 흔들림 없었던 맑은 눈동자에 남아있는 격렬한 감정의 잔재를.

암초에 부딪힌 파도가 새하얀 포말(泡沫)을 숨길 수 없듯이, 그것은 밤하늘처럼 새카만 그녀의 눈 어딘가에 흔적을 남겼다.

그리고 누군가가 이 상황에 명확한 의구심을 품기도 전에, 어느 거지와 협객이 낮은 목소리로 주고받는 대화가 모두의 귓가를 파고들었다.

“뭐야, 진짠가?”

“어허, 아니라니까. 후개 아니랄까 봐 뭔 거지발싸개 같은 소리를 하고 있어.”

“아니, 아무리 봐도 진짜 같은데?”

“그러니까, 진짜 사술이라고.”

“하, 씨. 그런가?”

미간을 찌푸린 궁기방을 향해, 혁무진이 마지막 결정타를 날렸다.

“하지만 대저 사술이란 정도(正道)를 벗어나 힘을 얻는 대신 완전할 수는 없는 법. 봐라, 머릿수가 하나 부족하잖아. 아마 다른 사람들은 다 따라 해도 그 양반은 흉내 낼 엄두도 안 났나 보지.”

“……!”

“……!”

그 순간, 두 사람의 대화를 듣고 있던 사람들은 까맣게 잊고 있던 한 가지 사실을 깨달았다.

마지막 균열이 닫힌 지금까지도, 대인(大人)이 보이지 않는다는 것을.
```

## Final English reading copy

```markdown
# Chapter 1191

The only path connecting reality and a Gate.

The sensation of passing through a magical field was more than familiar to a veteran Hunter like me. Even so, it was often unpleasant enough to make me shudder.

Like right now.

*Whoooosh.*

Was this what it felt like to be swept into a whirlpool?

The cold, sticky sensation unique to magical power wrapped around my entire body, then spat me out somewhere beyond.

The moment I opened my eyes in the new space, I realized something I’d never known before.

*It’s different.*

Branches packed so tightly they covered the sky. Steep hills.

The mountains of corpses and rivers of blood that had filled every direction were gone.

But it wasn’t only the surrounding scenery that had changed.

Magical power.

That filthy energy should have fallen cleanly away the moment I left the Gate, but it was still clinging to my body.

No—it filled this entire space.

“This is…”

The heavy words slipped out like a groan.

Jeok Cheongang, who had been shuddering at the magical field’s repulsive sensation, reacted at once when I fell silent.

“What is it?”

Normally, I’d have laughed it off and said it was nothing.

But the intense sense of déjà vu pressing in on all five senses since the moment I opened my eyes brought back memories from less than a few weeks ago. And Jeok Cheongang already knew most of the truth about me.

“I’ve been somewhere like this before. Very recently, in fact.”

“Ah. Could it be…?”

“Yes. The incident I told you about.”

A gigantic mushroom cloud swallowing civilization. A metropolis with no trace of life.

And one being waiting for me in a dark castle newly raised above the blackened earth.

*Morgoth.*

That was right.

This place carried an energy remarkably like the Dragon Lair the Black Dragon Duke Morgoth had built atop the ruins of Moscow.

An energy intense enough that you could call it the Demon Realm.

*No. It’s even worse.*

According to Jeok Cheongang, I’d been unconscious for about a day.

I’d only felt magical power this pure after approaching a Dragon Lair, but already, energy nearly as powerful was churning all around us.

*So this is what the System meant by a restricted area.*

Now I understood.

All kinds of absurd rumors floated around Murim, but the stories about this damn mountain range had been watered down to an almost ridiculous degree.

Only now, after seeing and feeling the Tianshan Mountains for myself, did I understand that they were a forbidden land in the truest sense—a Land of Ruin.

Uninvited guests who hadn’t received permission from its master shouldn’t enter—and couldn’t leave.

And this endless range of dark mountains showed no sign of revealing what it hid within its vast bulk.

That included the mountains’ master—and the other uninvited guests besides Jeok Cheongang and me.

“I don’t see the others.”

“I suspected as much when we were caught by that strange thing, whatever it was called. Seems I was right.”

Jeok Cheongang narrowed his eyes at the mist drifting around us, but that didn’t make the missing people suddenly appear.

Even a superhuman with the eyesight to clearly make out an ant a hundred yards away couldn’t peer through the space between reality and a Gate with human eyes.

*…Right. That would be impossible.*

A thought suddenly crossed my mind, and I added silently,

*With human eyes.*

I couldn’t be sure this idea would work.

Frankly, if I looked at the odds coldly, I was more likely to waste my energy and make things worse.

But when there’s only one path ahead—and you’ve already traveled it once—then no matter how huge an obstacle stands in the way, you have to smash through it and keep going.

*Bzzzzzz.*

The air began to tremble. As I took a deep breath, I raised my spear.

Slowly enough to make someone yawn, I spread the energy coiled within me through my whole body.

Jeok Cheongang reacted to this sudden move, but only for a moment. Then the entire area fell silent.

More precisely, my concentration reached its peak and erased everything, even the irrelevant noise.

For one purpose alone.

To find the other spaces hidden behind the invisible veil.

And then—

*Keeeeeng.*

A thunderous ringing filled my ears. At the same moment, a terrible headache struck and whitened my vision.

*Ding.*

As I heard a clear chime ringing faintly somewhere, I realized my reckless attempt had finally succeeded.

I also knew I couldn’t let this fleeting gap slip away after all that effort.

*Plip. Plip.*

Was it because the tiny blood vessels in my eyes had burst one by one? Or because blood had begun to seep between my lips without my even noticing?

My vision was red all over. Pain pierced my chest and brain.

But it didn’t matter.

I’d already seen it. Read it.

*Cut.*

I let out the breath I’d been holding and brought the spearhead, raised high above me, slashing down.

Following the single path my other eye—the Mind’s Eye—had shown me.

*Shhhhaaa—*

A blinding flash split the world—and the invisible veil.

* * *

> **System**
> - Status effect **Trance** has ended.

The first line of text to appear before Jin Taekyung’s eyes.

It was the starting flare.

A flare announcing that a wave of System notifications was coming.

*Ding. Beep.*

> **System**
> - Special ability **Mind’s Eye** has been activated because its activation conditions have been met!
> - Your insight into **Mind’s Eye** has deepened.
> - Always exercise caution. This ability can cause severe harm to the user’s mind and body, and in the worst case, can lead to death!
> - Status effect **Exhaustion** has been applied!
> - Status effect **Extreme Fatigue** has been applied!
> - Status effect **Internal Injury** has…

Jin Taekyung gasped for breath.

His chest felt tight. Nausea rose as his disoriented body swayed from side to side.

Through vision warped like a heat haze, he saw Jeok Cheongang rush up and catch him, shouting something. His battered senses could barely register the man’s words or touch.

For a moment.

Then a second wave swept over him, accompanied by a cascade of chimes.

*Ding. Ding. Ding.*

> **System**
> - Mutated Gate **Forest of Death-II** destroyed!
> - Mutated Gate **Forest of Death-III** destroyed!
> - …
> - Mutated Gate **Forest of Death-VI** destroyed!
> - You have achieved the very rare achievement **Knock, and It Shall Be Opened**!
> - You have gained a tremendous amount of EXP as a reward for achieving a very rare achievement!
> - You have acquired the Title **Door Opener**!
> - Level up!
> - All injuries and fatigue have been recovered as a result of leveling up!

High risk, high reward.

It had been a dangerous move, but the payoff was worth it.

He’d gained all at once the EXP it would take to defeat several Black Ghosts—and, more importantly, achieved his main goal.

“What on earth…!”

At his Master’s stunned expression, the Disciple curled his bloodied lips into a smile.

“Just like you see.”

The changes around us were already plain enough to see with the naked eye.

*Grrrrk.*

The empty air warped.

Like the face of a monster being forced to spit something out.

And then—

*Whoooosh.*

Several invisible gaps opened their maws one after another.

They belched out the darkness that had filled them, along with something they’d hidden away.

More precisely—

“Arrrgh! You sons of bitches—you’re worse than beggars!”

“Come forth! I am Hyuk Mu—best hero the great Jin Family of Taiyuan has to offer!”

One beggar who didn’t hesitate to criticize himself, and one martial artist whose fierce loyalty to his family was matched only by his willingness to trade self-awareness for a piece of candy.

“……”

“……”

“……”

“……”

In the suffocating silence, the great Jin Family of Taiyuan’s best hero finally spoke.

“Don’t be fooled, beggar. This is all their dark arts.”

The beggar, who was just a little better than a son of a bitch, shot back.

“Do I look like an idiot who’d fall for this? I saw through this crap ages ago.”

“Heh. Just what I’d expect from the Beggars’ Sect’s Successor Beggar.”

“You’re not bad yourself. You figured it out right away.”

As the two traded words, Master and Disciple watched the whole thing with distant eyes and had nearly the same thought.

*Can’t we put those guys back?*

*Should we just put them back in?*

Unfortunately, it didn’t happen.

Before they could seriously consider how, a second rift opened.

*Whoooosh.*

Beyond the darkness fading away, a man appeared in a rush. His eyes were as cold as his expression as he surveyed the area, then asked Jin Taekyung,

“Is this dark arts?”

“This asshole’s at it too.”

At the answer that came without a pause, the man—Song Ilseom—lowered the blade dripping with blood.

“It’s really you.”

“Glad you’re alive. By the way, where’s Young Lady Ju?”

“She’ll be out soon. It might’ve been a trap, so I went first.”

Song Ilseom hesitated for a moment, then added,

“The employer’s safety comes first.”

“I didn’t ask— Ah, Young Lady Ju!”

“Benefactor! Great Hero Jin! Young Master Jin!”

Unlike the three before her, Ju Hwaran ran toward Jin Taekyung without the slightest hesitation.

More precisely, she would have—

If the third and fourth rifts hadn’t opened at the same time.

“Wow! I’ve never felt anything this gross before!”

Cheongpung appeared with a voice that sounded nothing like his words. A shadow appeared right after him, as though it were one with the magical power, and let its actions speak for it.

*Shwack—CLANG!*

A flash raced through the space, outstripping even sound.

Jin Taekyung knocked aside the dagger, which had shot toward him with terrifying speed, and shrugged.

“You could’ve just said something. Did you really have to go that far?”

“One of the few things assassins and physicians have in common is that we must be suspicious of everything around us. The more suspicious we are, the fewer mistakes we make.”

“So, are you satisfied now?”

“I think I’m less suspicious of the reality I’m seeing, at least.”

The Slaughter Saint looked at Jin Taekyung with a curious glint in his eyes.

“I’m more suspicious of myself now, though. How did you wake up already?”

“Because you’re a quack.”

“Well, I’m just normal. Anyone can do this with the Heavenly Martial Physique and martial arts like mine.”

“……”

At the two Master and Disciple’s mocking, arrogant replies, the Slaughter Saint squeezed his eyes shut. Just then, a person appeared from the fifth and final rift.

Unlike the others, she didn’t hurry or move stealthily. Her clothes and skin were untouched by a single drop of blood.

But Bow Saint’s eyes were different from usual.

A tempest.

It lasted only a moment, but a few people saw it clearly: the traces of intense emotion left in those clear, normally unshakable eyes.

Just as a wave that crashes against a reef can’t hide its white foam, that emotion left its mark somewhere in her eyes, black as the night sky.

Before anyone could form a clear suspicion about what they’d just seen, the low-voiced conversation between a beggar and a hero reached everyone’s ears.

“What, so it’s real?”

“I told you it isn’t. Don’t go saying beggar-rag nonsense just because you’re the Successor Beggar.”

“No, it looks real to me, no matter how I look at it.”

“I said it’s real dark arts.”

“Ha, shit. Is that so?”

Hyuk Mujin delivered the final blow to Gung Gibang, who was frowning.

“But dark arts can never be perfect. You gain power by abandoning the proper path. Look—we’re one person short. They must have managed to imitate everyone else, but not dared to try imitating that man.”

“……!”

“……!”

The people listening to the two suddenly realized something they’d completely forgotten.

Even now, after the final rift had closed, the Great Sir was nowhere to be seen.
```
