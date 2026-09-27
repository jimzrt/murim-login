<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1185.txt",
      "sha256": "00393c12c30d3c493ca0bb946366a866ad51d2f150be22417890982b9f494176",
      "bytes": 11229
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "38fb29db60e9e51f30c3b7c605068d08f6b67e25f0cffe8a75e96fd307b8791a",
      "bytes": 1979
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2372eff4014bbbfe2875ceb74264c004f7f386d353a549f999d2b18a5d322a72",
      "bytes": 248683
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "6be5e717b8f605b4aa06d2e8db4fe269e8ddee9c6cc196756f003bcf5e8a0ef9",
      "bytes": 760
    },
    {
      "path": "characters/Hak Eui.md",
      "sha256": "e630878cf1e1f7affa80354f5761a1804b9e4172d95d27594bd1b97eeebeb644",
      "bytes": 554
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "9b28bad050654a1bb5c3d09561205cc83089daad387db8a9efd13e4273d2fc2c",
      "bytes": 1377
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "4d49949381bb711670a04893a15de89d32b2047a4ce9200656d2d09dad67e7bc",
      "bytes": 1701
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "8d686b06846aa54651e4cdfaa031ae1cade4aab8f6a94574c052bdcf464ad111",
      "bytes": 1550
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "20d81fbab44d3ca8a58509e81f939d52284e927cb8567f4d9f8117586c0f7d0f",
      "bytes": 623
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "25d6b4481c61f0b3744bcead06f29f40379677976b6944c8aa01e36a1756de97",
      "bytes": 974
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "f7e888350cf5aaad1d26b6107f10682291ef4eb064f67e9403fc1e835166e879",
      "bytes": 1084
    },
    {
      "path": "characters/Pill Physician.md",
      "sha256": "89c21ff3c26a13f7557dd09581f7793a7c925028058b5f51cde60f59635d6f72",
      "bytes": 555
    },
    {
      "path": "characters/Son of Heaven.md",
      "sha256": "69b4e2550d17aa20c914bd82fbee43cf24b694ba5feeaafd568cbddedd113a5b",
      "bytes": 715
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "6592233b34dcd7f1d0f74935310ed387046c3f86f1869fa5f218139dd6824a3a",
      "bytes": 295903
    }
  ],
  "estimated_tokens": 11288
}
-->

# Durable State Update — Chapter 1185

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
1 and safe_through 1185. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1185. Profile updates may replace only one
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
  "chapter": 1185,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1185,
    "continuity_sources": [1185],
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
    "The Murim allied forces split into three forces near the Qinghai-Xinjiang border, intending to rendezvous with the Imperial Army near Tianshan.",
    "Taekyung’s group reached the rendezvous, but the Murim Alliance and Imperial Guards missed the agreed deadline.",
    "Taekyung was secretly designated the main attack against Dark Heaven; the Sword Saint, Emperor, and gathered allies agreed to conceal this plan from him.",
    "Taekyung decided to turn back at least half a day to search for his missing companions, but the Slaughter Saint’s medicine and the Bow Saint’s intervention stopped him; he collapsed into Jeok Cheongang’s arms.",
    "The fate of the separated companions and the more than one hundred thousand allied troops is unknown.",
    "Taekyung experiences unexplained chest pain and difficulty sleeping.",
    "The Lord of Heaven has awakened and regained strength, but says the process is incomplete; the Grand Mage awaits a command.",
    "The Main Quest “Rift and Collapse” failed; “The Foreordained Collapse” warns that player choices can cause irreversible consequences.",
    "Cheon Taemin remains unconscious in a secret facility beneath the Pentagon; Jin knows he is the Martial God and a former Player.",
    "An alert reported Alpha’s awakening; what Alpha is and what its awakening means remain unknown."
  ],
  "continuity_sources": [
    1184,
    1183
  ],
  "open_questions": [
    "What happened to the separated companions and allied troops?",
    "Why did the Murim Alliance and Imperial Guards miss the rendezvous?",
    "What caused Taekyung’s chest pain and sleeplessness?",
    "What remains to be completed for the Lord of Heaven, and what command will he give the Grand Mage?",
    "What is Alpha, and what does its awakening mean?"
  ],
  "safe_through": 1184,
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
| 매종학    | **Mae Jonghak**    |
| 주화란    | **Ju Hwaran**      |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 살성     | **Slaughter Saint**           | —              |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 청해     | **Qinghai**            |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 학의 | **Hak Eui** | Kunlun Sect First-Generation Disciple. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 환의 | **Pill Physician** | Title of the current Family Head of the Seongsu Jang Family. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 벽곡단 | **fasting pills** | Food-substitute pills found in the hidden cave where Cheol trained. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천산 | **Tianshan** | Mountain region identified as the Demonic Cult's headquarters. |
| 천산산맥 | **Tianshan Mountains** | Mountain range associated with the Demonic Cult. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 만독지환 | **Myriad-Poison Ring** | Quest title concerning a legendary treasure said to detoxify any poison. |
| 마비 | **Paralyzed** | Status abnormality inflicted by Kraken's Ink. |
| 멸지 | **Land of Ruin** | Name used for the desert region beyond which Dark Heaven’s forces are approaching. |
| 진인 | **Perfected One** | Honorific for the two Kongtong Elders killed at Dunhuang. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 매종학 | 적천강 | long-standing martial rival and friend | Great Hero Jeok | casual and familiar | Mae addresses Jeok as 적 대협 while discussing the Alliance Leader position. |
| 적천강 | 매종학 | long-standing martial rival and friend | you | blunt and familiar | Jeok addresses Mae as 당신 while recalling their meeting at Mount Jiuhua. |
| 진태경 | 매종학 | younger ally to newly installed Alliance Leader | Alliance Leader | formal and deferential | Uses 맹주님 while formally greeting Mae Jonghak as the Alliance Leader. |
| 적천강 | 의원 | interrogator_to_physician | you; quack | blunt and threatening | Jeok shakes the physician and demands an explanation for Jin's seven-day sleep before ordering him to summon the Beast Miao King. |
| 혁무진 | 주화란 | Fire Dragon Pavilion member to fellow member | Young Lady Ju | polite and deferential | Mujin addresses Hwaran as 주 소저 while asking her to call a physician. |
| 주화란 | 적천강 | younger ally to legendary martial master | Great Hero Jeok | formal and deferential | Ju Hwaran addresses Jeok as 적 대협 while asking whether he is all right. |
| 신의 | 주화란 | senior physician to younger ally | Young Lady Ju | warm and teasing | The Divine Physician lightly teases Hwaran about being more worried for Jin than he is. |
| 학의 | 진태경 | Kunlun Sect disciple to renowned martial artist | Great Hero Jin Taekyung | formal and deferential | Uses 진태경 대협 when introducing himself and greeting Taekyung. |
| 살성 | 적천강 | familiar peer and fellow martial master | you | familiar and teasing | Uses 자네 while teasing Jeok and reassuring him. |
| 적천강 | 살성 | familiar fellow martial master | you | familiar, insulting-casual | Trades teasing insults with the Slaughter Saint over who is welcome in Taekyung’s carriage. |
| 살성 | 진태경 | senior allied martial artist to younger companion | you | familiar and blunt | Addresses Taekyung with 너 and 네가 while explaining that he anticipated Taekyung’s response. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1184
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hak Eui.md

# Hak Eui (학의)

- **Safe through:** Chapter 1151
- **Aliases:** None
- **Role:** Hak Eui is a First-Generation Disciple of the Kunlun Sect.
- **Personality:** Composed, observant, and assertive; he investigates matters closely and uses his standing to bring consequential findings before the leaders.
- **Voice:** Calm and formal, with measured phrasing and dry, blunt statements of fact.
- **Relationships:** He has met Jin Taekyung and respectfully addresses him as a Great Hero.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1184
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and Vice Captain of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is deeply loyal to Taekyung, who trusts him as a close companion and values him as family, and has a warm friendship with fellow Fire Dragon Pavilion member Taishan; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Pavilion members accompanying Taekyung, and his parents own the Hyuk Family Textile Shop, which his younger sibling may inherit.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1184
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and follows his own path rather than pursuing grand causes; though he turned his back on the world, he wants Taekyung to pursue righteousness, practice chivalry, and win people’s hearts, and fiercely protects those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, and shares familiar, teasing camaraderie with the Slaughter Saint; he accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1184
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and eleventh member of the Ten Kings, a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; he serves as Thousand Captain of the Embroidered Uniform Guard, is enfeoffed as Prince Shangshan, and is widely regarded as a new-age savior.
- **Personality:** Hungry, self-aware, and dryly observant, he is pragmatic and fiercely defiant; he protects those he cherishes and meets mounting responsibility with hope and a determination to endure.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother and Jeok Cheongang his Master and trusted confidant; he shares deep loyalty with Hyuk Mujin, whom he values as family, and considers the revived Undead King, formerly the Skeleton King, a friend.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1184
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 1184
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, and filial; remains controlled under pressure but has grown more assertive and openly impatient after the hardships she has endured.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 1181
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader and has ordered Jin Taekyung's first Fire Dragon Pavilion mission to Nanman.
- **Personality:** Playful and easygoing in ordinary company, yet guided by a principled commitment to chivalry that can outweigh strategic caution.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Pill Physician.md

# Pill Physician (환의)

- **Safe through:** Chapter 1153
- **Aliases:** None
- **Role:** Current Family Head of the Seongsu Jang Family in Shandong, who personally placed and signed the Thousand-Year Snow Ginseng in the casket entrusted to the Yongbong Escort Bureau.
- **Personality:** No personality traits are established.
- **Voice:** No voice traits are established.
- **Relationships:** The Pill Physician heads the Seongsu Jang Family, a prestigious medical family in Shandong.

### Son of Heaven.md

# Son of Heaven (천자)

- **Safe through:** Chapter 1182
- **Aliases:** Emperor, Zhu Di
- **Role:** The Son of Heaven is the Emperor of Great Ming and Zhu Bao’s elder brother; he has ordered a personal expedition to Xinjiang and will not return to the palace until the traitors are rooted out.
- **Personality:** Strategic and imperious, the Son of Heaven has learned to value compassion for his people and will risk himself to protect them.
- **Voice:** Calm and commanding, with dry, understated humor.
- **Relationships:** Zhu Bao is his younger brother and heir; Jin Taekyung gave him the White Illusion Jiangshi Art; he killed Ma Sanbao.

## Korean source

```text
＃1185화



“좋군, 아무 이상 없어.”

진태경의 상태를 확인한 살성의 첫마디에, 적천강이 무거운 얼굴로 입을 열었다.

“확실한가?”

“장담하지.”

“세 시진 전쯤에 들었던 이야기와 같군.”

“믿음을 좀 가져 보지 그러나. 약효가 조금 늦게 퍼진 것뿐이야.”

“좀처럼 믿음이 가질 않는군. 어느 돌팔이의 어설픈 장담 때문에 일이 틀어질 뻔 했어서.”

일순간, 허공에서 두 사람의 시선이 마주쳤다.

팽팽하게 조여드는 공기 속, 짧은 침묵 끝에 적천강이 작게 한숨을 내쉬었다.

“말이 과했군. 사과하지.”

“아니, 사과할 필요까지는 없네. 어떤 마음인지 충분히 이해하니까.”

살성은 진심으로 개의치 않았다.

반평생을 살수로 살았으나, 또 다른 반평생은 의원으로 살아온 그다.

지금껏 헤아릴 수조차 없을 만큼 무수한 환자를 돌보며 터득한 것은 의술뿐만이 아니었다.

마음.

병든 이의 마음과, 그 모습을 가장 가까운 곳에서 지켜보며 고통을 공유하는 이들의 마음을 느끼게 되었다.

그렇기에 자신이 지금 마주하고 있는 이가 화왕이라 불리는 위대한 무인이 아닌, 적천강이라는 한 명의 인간이자 환자의 가족이라는 사실을 누구보다 잘 알고 있었다.

‘더군다나 의원으로서 충분한 믿음을 주지 못한 내 잘못도 있으니.’

살성은 마음속 뇌까림과 함께, 이미 의식을 잃은 진태경의 얼굴을 가만히 내려다보았다.

그리고 동시에 떠올렸다.

조금 전, 진태경이 보여 준 그 무시무시한 힘과 속도를.

‘분명 모든 게 완벽했다. 미리 만들어 두었던 약의 배합도, 약효가 발휘될 만한 시간도.’

진태경이 섭취한 벽곡단은 만독지환의 존재를 염두에 둔 살성이 심혈을 기울여 만들어 낸 역작이었다.

처음에는 그저 평범한 벽곡단에 불과하지만, 세 시진이 넘는 시간에 걸쳐 느릿하게 약효가 퍼지기 시작한다면 이야기는 달라진다.

팔다리는 마비되고 정신과 기감은 흐려지며, 공력이 흩어지는 산공(散功)의 효과까지 더해지니 그 어떤 초절정 고수라고 해도 쉽사리 버틸 수 없으리라 확신했다.

심지어는 약을 제조한 살성 그 자신조차도 모르고 당한다면 곤경에 처할 것이라 생각될 만큼.

‘그런데 이 녀석은 어찌 이렇게.’

문득 진태경을 향한 살성의 눈빛이 깊어졌다.

단순히 기분 탓일까, 조금 전 들이닥쳤던 그 맹렬한 권풍(拳風)이 스쳐 지나간 등줄기가 찌르르 울리는 듯했다.

과연 그것이 진정 전력을 다한 일격이었을까, 하는 희미한 의문도 함께.

“……어쩌면.”

무심코 입술 사이로 흘러나온 음성.

뒤이어 돌아온 적천강의 의혹 어린 시선에, 곧장 자신의 실수를 깨달은 살성이 고개를 내저었다.

“아무것도 아닐세. 잠시 생각할 것이 있어서.”

“혹시…….”

“안심하게. 누차 말하지만 자네 제자에게는 아무런 문제도 없으니까. 아주 길어야 이틀 후면 정신을 차릴걸세.”

살성은 주화란과 혁무진의 부축으로 옮겨지는 진태경을 바라보며 덧붙였다.

“그리고 녀석이 깨어났을 때쯤에는, 우리도 저 어딘가에 있겠지.”

그 말에 적천강의 시선이 창밖을 향했다.

별조차 자취를 감춘 세상 너머, 어둠으로도 완전히 지울 수 없는 거대한 천산산맥은 흡사 신화 속 괴물처럼 우뚝 서 있었다.

천 년 전에도 그러했고, 천 년 후에도 그러할 것처럼.

하지만 저 천산 어딘가에 웅크리고 있을 천주(天主)야말로 진정한 괴물이요, 심연이라 불릴 만한 존재였다.

그를 쓰러트리기 위해 천하의 명운을 걸어야 할 만큼.

“도저히 모르겠군. 이것이 진정 옳은 선택이었는지.”

혼잣말처럼 흘러나온 적천강의 의문에, 살성이 대답했다.

“자네도 알고 있지 않나. 이것은 최선도, 차선도 아니라는 것을. 단지 가까스로 최악을 면한 차악(次惡)일 뿐이고, 지금의 우리에게 주어진 유일한 선택지이기도 하지.”

맞다. 최선을 논하기에는 너무 멀리 와 버렸다.

황군과 무림맹. 그 어느 쪽도 약속된 시일에 도착하지 못한 이상, 그들 앞에 놓인 길은 하나뿐이었다.

그리고 이는, 이미 청해 땅을 떠나기 전부터 염두에 두었던 여러 가능성 중 하나이기도 했다.

‘만약 정해진 날짜까지 아무도 도착하지 않는다면, 만에 하나 그렇게 된다면…….’

적천강은 불현듯 떠올렸다.

어스름한 새벽, 극비리에 이루어진 만남에서 나지막한 음성으로 속삭이던 검성 매종학의 모습을.



‘그곳을 떠나 천산으로 가시오. 단 한 치의 망설임도 없이.’

‘떠나라니, 진심인가?’

‘천하에서 가장 강한 무인들이, 가장 지혜로운 지자(智者)들이 세운 계획에 따랐는데도 일이 어긋났다면 더 이상 무슨 말이 필요하겠소. 이미 천자께서도 동의한 바요.’

‘하지만.’

‘이건 희생이 아니라, 단지 모두를 위한 선택일 뿐이오. 그 어떤 불상사가 있더라도 최악은 면할 수 있겠지. 우리에게는 아직 남아 있는 한 수가 있을 테니.’



진인사대천명(盡人事待天命).

사람의 일을 다했으니, 하늘의 명을 기다린다.

모두가 마음속에 새긴 그 여섯 글자를 소리내어 읊던 매종학은, 분명 웃고 있었다.

‘그럼, 다음에는 천산에서 뵙지요.’

날이 밝자, 그들은 그렇게 헤어졌다.

무림맹은 서쪽으로. 황군은 동쪽으로. 그리고 그들 모두의 희망을 실은 한 대의 마차는 사막으로.

혹시 모를 간자(間者)에 대비하여 이 모든 과정은 매우 은밀히 실행되었다.

진태경 일행의 부재를 모두가 알아차릴 즈음, 매종학은 그들이 진작 황군에 합류하여 이동 중이라는 사실을 알렸고 그것은 황군 측 역시 다르지 않았다.

그들은 온 힘을 다해 진격하는 한편 끊임없이 역정보를 흘렸다.

어디에 숨어 있을지 모를 암천의 이목이 사막으로 향하지 않도록.

만에 하나 최악의 상황이 닥치더라도, 자신들이 미끼가 될 수 있도록.

그리고 우려했던 바는 현실로 드러났다.

‘도대체 무슨 일이 벌어진 것인가.’

혀끝에만 맴도는 그 의문을, 적천강은 애써 삼켜 냈다.

아니, 이는 비단 그 한 사람에게만 해당되는 것이 아니었다.

아군에게 변고가 벌어진 것은 이미 이 자리의 모두가 아는 기정사실. 하지만 그 누구도 그 생각을 소리내어 말하지 않았다.

지금 그들에게 필요한 것은 꺼지지 않는 용기와 희망이지, 늪처럼 깊고 끈적거리는 불안감이 아니었으니까.

‘끝까지 포기하지 않는 수밖에.’

계획은 아직 실패하지 않았다.

비록 일이 틀어지긴 했으나 자신들은 흔들림 없이 천산으로 나아갈 것이고, 뒤늦게 도착한 아군 역시 그들의 뒤를 쫓아 합류할 것이다.

어디까지나 미약한 희망에 불과하더라도, 지금은 그렇게 믿는 것만이 최선이었다.

“출발한다. 더 늦기 전에.”

적천강의 무거운 음성이 울려 퍼진 그 순간.

훅.

위태롭게 휘청이며 공간을 밝히고 있던 촛불이, 마침내 사그라졌다.



* * *



한 번 결정이 내려지자, 사람들은 일사불란하게 움직였다.

진태경만 모르고 있었을 뿐, 나머지 일행은 이미 모든 가능성과 현실을 염두에 두고 있었기에 그들의 행동에는 조금의 망설임도 없었다.

그런 의미에서 이 버려진 소도시에서 머물렀던 지난 이틀의 시간은 실로 귀중했다.

그간 쌓여 있던 피로를 회복하는 것은 물론, 지나친 강행군으로 인하여 더 이상 움직일 수 없게 된 말들을 새로운 식량으로 삼을 수 있었으니까.

“피는 뽑아서 따로 호리병에 보관하고, 살은 육포로 만들어 놓거라. 이제부터는 산세가 험하여 마차를 쓸 수도 없고, 이대로 풀어 준다 한들 굶어 죽고 말 터이니.”

“그, 정말 이렇게까지 해야 합니까?”

“왜, 정이라도 들었느냐?”

“아니라면 거짓말이죠. 아무리 축생이어도 함께한 시간이 있는데. 이놈들 눈 좀 보십시오. 벌써 눈물 고여 있는 거 안 보이십니까? 꼭 사람 말을 알아듣는 것 같다니까요?”

“알겠다. 그럼 혁가 네놈은 내일부터 굶는 것으로…….”

“다시 생각해 보니까 침이 고이네요.”

“…….”

“지들이 뭘 어쩌겠습니까. 축생으로 태어난 게 죄지.”

지금까지 최선을 다해 준 여덟 마리의 한혈보마에게는 참으로 미안한 일이었지만, 그건 도덕적인 부분을 제외한다면 매우 합리적인 결정이었다.

자정이 막 지난 깊은 밤, 마침내 천산에 첫 발자국을 내디딘 그 순간부터 그들 모두는 직감하게 되었으니까.

‘이곳은 도대체…….’

달랐다.

공기의 무게, 바람의 흐름. 그 모든 것이.

마치 분리된 또 하나의 세상처럼 뒤바뀐 분위기에, 사람들은 불현듯 등줄기를 타고 솟구치는 한기(寒氣)를 느꼈다.

마치, 빠져나올 수 없는 미로와도 같은 감옥에 갇힌 듯한 착각도 함께.

‘실로 지독한 기운이다.’

적천강은 찌르르 울리는 오감(五感)을 느끼며 생각했다.

온갖 시체와 독으로 가득 찬 웅덩이를 마주한다 하더라도 이 정도는 아닐 것이라고.

아니, 어쩌면 한편으로는 이것이 당연한 일일지도 몰랐다.

바로 이 천산이야말로, 지난 천년 간 마(魔)라는 독을 품고 있던 멸지였으니.

그러나 동시에, 반드시 넘어서야 할 마지막 언덕이기도 했다.

이미 휴식도 취했고, 식량도 충분히 확보해 두었다.

저 가시밭 같은 풀숲 어딘가에 도사리고 있을 위험만 주의한다면, 머지않아 목적지에 다다를 수 있을 터였다.

‘우리가 이곳까지 아무런 방해도 없이 무사히 도착할 수 있었다는 것은, 적어도 아직까지는 놈들의 이목에 걸려들지 않았다는 증거.’

적천강은 마음속 뇌까림과 함께 캄캄한 숲을 응시했다.

비록 흘러가는 상황은 좋지 않았으나, 저 사실만으로도 아직 희망은 충분하다.

그리고 혈육처럼 아끼는 제자를 등에 업은 늙은 스승은, 부러질지언정 결코 꺾이지 않을 것이다.

저벅.

적천강의 힘주어 첫걸음을 내디뎠다. 

어디선가 불어온 강한 바람에, 사방을 빽빽하게 매운 잿빛 나뭇가지가 이 허락받지 않은 불청객들을 향해 손을 흔들었다.
```

## Final English reading copy

```markdown
# Chapter 1185

“Good. There’s nothing wrong.”

At the Slaughter Saint’s first words after examining Jin Taekyung, Jeok Cheongang spoke with a grim expression.

“Are you sure?”

“I guarantee it.”

“That’s what you told me about three shichen ago.”

“Why not try having a little faith? The medicine just took a bit longer to spread through his system.”

“It’s hard to trust you. Things nearly went wrong because of some quack’s careless guarantee.”

For an instant, their eyes met in midair.

The tension tightened. After a brief silence, Jeok Cheongang let out a quiet sigh.

“I went too far. I apologize.”

“No, there’s no need to apologize. I understand how you feel.”

The Slaughter Saint truly didn’t mind.

He had spent half his life as an assassin and the other half as a physician.

Tending to more patients than he could count had taught him more than medicine.

It had taught him about the heart.

He had learned to feel the hearts of the sick, and of those who suffered alongside them, watching from closer than anyone else.

That was why he knew better than anyone that the man before him wasn’t the great martial artist known as the Fire King. He was Jeok Cheongang—a man, and the family of a patient.

*Besides, I’m at fault for not giving him enough reason to trust me as a physician.*

With that thought, the Slaughter Saint quietly studied Jin Taekyung’s face. He had already lost consciousness.

And at the same time, he remembered the terrifying strength and speed Taekyung had displayed moments ago.

*Everything had been perfect. The medicine I’d prepared in advance, even the time it would take for the effects to kick in.*

The fasting pill Taekyung had taken was the Slaughter Saint’s masterpiece, painstakingly crafted with the Myriad-Poison Ring in mind.

At first, it was no different from an ordinary fasting pill. But after more than three shichen, its effects would slowly begin to spread, and everything changed.

His limbs would be paralyzed, his mind and Qi Sense would grow hazy, and the medicine would even disperse his internal energy. The Slaughter Saint had been certain that no Supreme Peak master could easily endure all that.

He had even thought that if he himself were caught unaware after taking a dose, he would be in trouble.

*So how did this brat…?*

The Slaughter Saint’s gaze deepened as he looked at Taekyung.

Was it just his imagination? His back still seemed to tingle where the fierce wind from Taekyung’s fist had swept past moments ago.

A faint doubt crept in, too. Had that really been Taekyung’s full strength?

“……Maybe.”

The words slipped from his lips before he realized it.

When Jeok Cheongang turned to him with a questioning look, the Slaughter Saint immediately realized his mistake and shook his head.

“It’s nothing. Something just crossed my mind.”

“Could it be…?”

“Rest easy. I’ve told you more than once: there’s nothing wrong with your Disciple. At the latest, he’ll come around in two days.”

The Slaughter Saint watched as Ju Hwaran and Hyuk Mujin helped carry Jin Taekyung away, then added,

“And by the time he wakes up, we’ll be somewhere out there.”

At that, Jeok Cheongang turned toward the window.

Beyond the world where even the stars had disappeared, the immense Tianshan Mountains stood tall, impossible to erase completely with darkness, like monsters from myth.

As if they had stood there a thousand years ago and would still stand a thousand years from now.

But the Lord of Heaven, crouched somewhere in those mountains, was the true monster—a being worthy of being called an abyss.

They would have to wager the fate of the world to defeat him.

“I can’t tell if this was truly the right choice.”

At Jeok Cheongang’s question, spoken almost to himself, the Slaughter Saint replied,

“You know as well as I do. This isn’t the best choice, or even the second-best. It’s only the lesser evil that barely lets us avoid the worst—and the only choice left to us now.”

He was right. They had come too far to talk about the best choice.

With neither the Imperial Army nor the Murim Alliance arriving by the agreed date, there was only one path ahead of them.

And it was one of several possibilities they had considered even before leaving Qinghai.

*If no one arrives by the appointed date—if, by some chance, that happens…*

Jeok Cheongang suddenly remembered the Sword Saint, Mae Jonghak, whispering in a low voice during their secret meeting at dawn.

*“Leave this place and go to Tianshan. Without a moment’s hesitation.”*

*“Leave? Are you serious?”*

*“If things went wrong despite following a plan devised by the strongest martial artists and wisest strategists under Heaven, what more is there to say? The Son of Heaven has already agreed.”*

*“But—”*

*“This isn’t a sacrifice. It’s simply a choice made for everyone’s sake. No matter what calamity befalls us, we can still avoid the worst. We should have one move left.”*

Do all that man can, then await Heaven’s will.

Having done all they could, they would wait for Heaven’s decree.

Mae Jonghak had spoken aloud the six characters everyone had engraved in their hearts. He had clearly been smiling.

*“Then I’ll see you in Tianshan.”*

When morning came, they parted.

The Murim Alliance headed west. The Imperial Army headed east. And a single carriage, carrying the hope of them all, went into the desert.

To guard against any possible spies, the entire operation was carried out in utmost secrecy.

By the time everyone realized Jin Taekyung’s group was missing, Mae Jonghak announced that they had already joined the Imperial Army and were on the move. The Imperial Army did the same.

They pressed forward with all their might, constantly feeding the enemy false information.

They had to keep Dark Heaven’s eyes and ears—who knew where they might be hidden—from turning toward the desert.

So that, if the worst came to pass, they could serve as bait.

And their fears had become reality.

*What in the world happened?*

Jeok Cheongang forced down the question that lingered on the tip of his tongue.

And it wasn’t only his question. Everyone there knew something had happened to their allies. But no one said it aloud.

What they needed now was courage and hope that wouldn’t die—not anxiety, deep and sticky as a swamp.

*We have no choice but to keep going.*

The plan had not failed yet.

Though things had gone wrong, they would continue toward Tianshan without wavering, and their allies, once they arrived, would follow and join them.

It was only a faint hope, but for now, believing it was the best they could do.

“We leave. Before it gets any later.”

At the sound of Jeok Cheongang’s heavy voice—

*Fwoosh.*

The candle, flickering precariously and lighting the room, finally went out.

* * *

Once the decision was made, everyone moved in perfect order.

Only Jin Taekyung had been kept in the dark. The rest of the group had already considered every possibility and accepted the reality before them, so not one of them hesitated.

In that sense, the two days they had spent in this abandoned small town had been invaluable.

They had recovered from their accumulated fatigue. And the horses, worn out by their relentless forced march and no longer able to travel, could now become fresh provisions.

“Drain their blood and store it in gourds. Make jerky from the meat. The terrain will be too rough for a carriage from here on, and if we set them free, they’ll starve to death anyway.”

“D-do we really have to go this far?”

“What, have you grown attached?”

“I’d be lying if I said I hadn’t. They may be beasts, but we’ve been together for a while. Look at their eyes. Can’t you see they’re already filling with tears? It’s almost like they understand what we’re saying.”

“Fine. Then you can go hungry starting tomorrow, Hyuk.”

“Now that I think about it, my mouth’s watering.”

“……”

“What can they do about it? It’s their fault for being born beasts.”

It was a miserable fate for the eight sweat-blood horses that had done their best for them until now. But apart from the moral question, it was a perfectly reasonable decision.

Just after midnight, the moment they set foot in Tianshan for the first time, they all sensed it.

*What is this place…?*

It was different.

The weight of the air. The way the wind moved. Everything.

The atmosphere had changed, as though this were another world cut off from their own, and a chill suddenly ran up everyone’s spine.

They even felt as if they had been trapped in a prison shaped like a maze with no way out.

*What a vicious aura.*

Jeok Cheongang thought as his senses prickled.

Even a pool filled with corpses and poison wouldn’t feel this bad.

No—perhaps this was only natural.

This very Tianshan was the Land of Ruin, which had harbored the poison called demonic evil for the past thousand years.

And yet, it was also the final hill they had to cross.

They had rested, and they had secured plenty of food.

If they stayed alert for dangers lurking somewhere in the thorny undergrowth, they would soon reach their destination.

*The fact that we made it this far without a single interruption proves that, at least for now, we haven’t drawn their attention.*

With that thought, Jeok Cheongang gazed into the dark forest.

The situation might be going badly, but that alone was reason enough to hope.

And the old master, with his beloved Disciple on his back, would break before he bent.

*Step.*

Jeok Cheongang took his first step, putting his weight behind it.

A strong wind blew from somewhere. The dense gray branches all around them swayed, waving at the uninvited guests who had come without permission.
```
