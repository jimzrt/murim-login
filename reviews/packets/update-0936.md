<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0936.txt",
      "sha256": "c75ecaa592b473a5ba30eb4fb01c29ebca686796e08dca7ede644defc9eef25c",
      "bytes": 13772
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "0691ce5125ee3692d40087b5e7d5fa1e304b96fbd88b52dc1eacf950cba58402",
      "bytes": 2107
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b51f7a56cfa82ca1164fe5c2453945cbf42f0adc0ae050d159295fd4e544b433",
      "bytes": 232009
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "fa7979f615c295b0a76086b9664b79b391207ece4166f2aa400fd98ea2ebe062",
      "bytes": 759
    },
    {
      "path": "characters/Eastern Heaven Demon Lord.md",
      "sha256": "53457f9d612e29832de85cba1463cdfae57b13ed9e154b3220cdf5f8ba9b2a7f",
      "bytes": 838
    },
    {
      "path": "characters/Hanga.md",
      "sha256": "fe149801204239d7e83215fd88e696bdb8bbca76b4557664271fa5a0f11fdb7e",
      "bytes": 568
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "e07d8e2a9bf0515ba716db87345c19ad6df031280734063755a5630bcfe177f2",
      "bytes": 853
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "b1e07a2e7c3b5836ad28564d1aed578f811d551230fa5ce8fc30ac90a46868d4",
      "bytes": 1445
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "3f8916acf900af2b0068a8a1137ba7b91c6c6e4882c5e7b3eb645bb01393cfb1",
      "bytes": 1244
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "3b2290f905317fdb8492f28576c21d65f513b3be91b35da1f2be58427379ff0c",
      "bytes": 1343
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "ad93d023b3277eb7403a6a06b2d2b0f8d5b9cce1e4737ee8e9250b6274761b40",
      "bytes": 622
    },
    {
      "path": "characters/Pill Physician.md",
      "sha256": "7e492bea1a790d954c490ed46c1927bc74b55c643a1b85aa4dc3c0826339ae2d",
      "bytes": 554
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "93b042d352e737c4c8b235d213b4e624a3a64b8e8ad11c8c32c739bc0e7ed1b9",
      "bytes": 1042
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "0e2d532f2af4d7be69c6e65c1cef25321d7cf2235ebf140c6de94d6147d63060",
      "bytes": 266948
    }
  ],
  "estimated_tokens": 12950
}
-->

# Durable State Update — Chapter 936

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
1 and safe_through 936. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 936. Profile updates may replace only one
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
  "chapter": 936,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 936,
    "continuity_sources": [936],
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
    "The Emperor was poisoned with Blood Soul Gu after the coup; it has reached his marrow, and he has endured its effects for more than ten years.",
    "The Divine Physician examined the Emperor three days before chapter 934 and said the condition was too advanced for him to treat at present.",
    "The Emperor has prepared for his death by transferring his loyal retainers and power base to Zhu Bao, but avoids meeting his younger brother to spare him the grief of an impending farewell.",
    "Taekyung promised the Emperor he would save him; the Emperor feels hopeful despite believing survival is probably impossible.",
    "Taekyung told Jeok Cheongang about the Emperor’s Blood Soul Gu poisoning, breaking his promise to keep the matter secret.",
    "The System update reward is a very durable pocket watch that appears broken and bears the faint inscription, “A broken clock is right twice a day”; its significance is unknown.",
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin.",
    "Hong Jin is Eunuch Hong, responsible for the East Depot; the Cang Gong post remains vacant.",
    "Ma Sanbao escaped and evaded the Imperial Army’s three-day search.",
    "The Eastern Heaven Demon Lord’s final instruction was to find an unspecified object at a particular place."
  ],
  "continuity_sources": [
    935
  ],
  "open_questions": [
    "What is the Martial God’s identity, and how did he know a chosen one would appear?",
    "How far has Dark Heaven infiltrated the Great Nation, and which officials or commanders are involved?",
    "Where is Ma Sanbao, and what is his current status?",
    "What object and place did the Eastern Heaven Demon Lord refer to, and what significance does the object have?",
    "What is the significance, if any, of the broken pocket watch given as the System update reward?"
  ],
  "safe_through": 935,
  "temporary_decisions": [
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 살성     | **Slaughter Saint**           | —              |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 영약     | **elixir**                                       |                                                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 노부      | **this old man / I**                                            |
| 공자      | **Young Master**                                                |
| 소저      | **Young Lady**                                                  |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 항아 | **Hanga** | Local village boy who lives near Jang Taebo. |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 환의 | **Pill Physician** | Title of the current Family Head of the Seongsu Jang Family. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 평화 | **Peace Guild** | Guild name. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 중독 | **Poisoned** | System status abnormality caused by the poisons. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 무형지독 | **Formless Ultimate Poison** | Unidentified poison discovered inside Jeok Cheongang's body. |
| 만독지환 | **Myriad-Poison Ring** | Quest title concerning a legendary treasure said to detoxify any poison. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 독물 | **venomous beasts** | Venomous creatures associated with the Nanman Beast Palace. |
| 심해 | **deep sea** | Unexplored ocean depths where the ancient monster awakens. |
| 진상 | **Jinsang** | Koizumi's punning address to Jin, retained for the Korean wordplay. |
| 혈혼고 | **Blood Soul Gu** | Rare gu poison found deep in Nanman. |
| 건청궁 | **Qianqing Palace** | The Emperor's palace, where Baek Yeon meets him. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 홍진 | 진태경 | political_host_to_young_martial_artist | Young Hero Jin; Young Master Jin; Sleeping Dragon of Shanxi | polite, coaxing, and probing | Uses respectful forms while steering Taekyung toward relaying the Escort Bureau proposal and teasing him with the Seongun Escort Bureau. |
| 진태경 | 홍진 | young_martial_artist_to_political_official | Comrade Chairman—no, Deputy Military Commissioner | casual and teasing, then formally corrective | Deliberately jokes with an inappropriate title before correcting himself to Hong Jin's official office. |
| 진태경 | 항아 | visiting_adult_to_local_child | little one | friendly and coaxing | Questions Hanga and offers food in exchange for information. |
| 혁무진 | 항아 | visiting_adult_to_local_child | little one | coaxing and encouraging | Questions Hanga with an artificially kind smile and offers two food bundles. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 적천강 | 의원 | interrogator_to_physician | you; quack | blunt and threatening | Jeok shakes the physician and demands an explanation for Jin's seven-day sleep before ordering him to summon the Beast Miao King. |
| 홍진 | 혁무진 | imperial aide addressing a martial artist accompanying the prince | Martial artist Hyuk | polite and conversational | Uses 혁 무인 when asking whether Mujin knows of an exception. |
| 진태경 | 상산왕 | protector addressing a young prince | His Highness | respectful royal address | Taekyung refers to the prince as 상산왕 전하 when ordering Mujin to bring him. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 상산왕 | 황제 | younger brother addressing the Emperor | Your Majesty | deferential royal address | Shangshan addresses the Emperor as 폐하 while pleading for Taekyung. |
| 혁무진 | 홍진 | martial artist addressing a senior official and political ally | Comrade Hong | casual and coaxing | Hyuk Mujin addresses Hong Jin as 홍 동지님 while trying to calm him and de-escalate the confrontation. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |
| 적천강 | 동천마군 | enemies | you | blunt and informal | Jeok Cheongang addresses the Eastern Heaven Demon Lord with hostile familiarity. |
| 동천마군 | 적천강 | enemies | you | informal | The Eastern Heaven Demon Lord speaks to Jeok Cheongang during their duel. |
| 황제 | 동천마군 | former ruler addressing a former subject, now an enemy | you | measured and formal | The Emperor asks why the Demon Lord betrayed his father, the late Emperor. |
| 동천마군 | 황제 | former subject addressing the Emperor, now an enemy | you; you bastards | hostile and contemptuous | He denies ever being loyal to the imperial family and accuses the rulers of betrayal. |
| 진태경 | 동천마군 | young martial artist confronting an enemy | ugly-ass big bro | casual, profane, and taunting | Jin calls out to the Demon Lord after returning to the hall. |
| 동천마군 | 진태경 | enemy recognizing the spear wielder | Jin Taekyung | shouted, informal | The Demon Lord cries Taekyung's name after identifying him as the spear's owner. |
| 상산왕 | 동천마군 | young imperial prince addressing the enemy who killed his parents and brothers and suffered at the hands of his grandfather | you | formal-polite | He apologizes for his grandfather’s actions using 당신 and deferential speech. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 935
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Eastern Heaven Demon Lord.md

# Eastern Heaven Demon Lord (동천마군)

- **Safe through:** Chapter 931
- **Aliases:** Wei Zhong
- **Role:** The Eastern Heaven Demon Lord was Wei Zhong, the East Depot’s Seal-Holding Eunuch and a former Maoshan Sect disciple who commanded the dead with a bell; Jin Taekyung killed him with blue-white flames.
- **Personality:** His hatred grew from losing his family and sect, but recognizing his own lonely childhood in Zhu Bao ultimately moved him to relinquish his vengeance and choose a less harmful final act.
- **Voice:** He speaks in measured, almost lyrical phrasing, recounting the past before turning to pointed accusations.
- **Relationships:** Ma Sanbao is his Disciple; he holds the Emperor responsible for Taizu’s actions against the Maoshan Sect.

### Hanga.md

# Hanga (항아)

- **Safe through:** Chapter 895
- **Aliases:** None
- **Role:** Local village girl, Jang-pal’s daughter, who lives near Jang Taebo and regularly visits him.
- **Personality:** Curious, energetic, observant, and already attentive to the value of information and food.
- **Voice:** Childlike, direct, and inquisitive, with an occasional surprisingly worldly remark.
- **Relationships:** Calls Jang Taebo Grandpa; Jang Taebo is his elderly neighbor and only conversational companion.

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 933
- **Aliases:** None
- **Role:** Hong Jin is Eunuch Hong, a former Deputy Military Commissioner of Shanxi Province and East Depot member who is now responsible for the East Depot and remains a trusted aide to Prince Shangshan.
- **Personality:** Composed, socially deft, and ambitious, Hong Jin became a eunuch to escape poverty and save his family, then used his abilities to pursue a broader life.
- **Voice:** Delicate and deferential with Prince Shangshan, but warm, familiar, and playfully forthright with trusted allies.
- **Relationships:** Hong Jin is devoted to Prince Shangshan and is trusted by the Emperor to take responsibility for the East Depot; he is a longtime friend of Ma Sanbao and a trusted ally of Jin Taekyung.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 932
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; he regards Taekyung as the person who has repeatedly saved him and now believes he may be able to save Taekyung in turn. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 935
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts Jin Taekyung, his publicly acknowledged second Disciple and intended heir; warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, remains Peng Cheolhu's rival, and is the target of an attack by the assassin Heaven's Slaughter.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 935
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 935
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Pill Physician.md

# Pill Physician (환의)

- **Safe through:** Chapter 877
- **Aliases:** None
- **Role:** Current Family Head of the Seongsu Jang Family in Shandong, who personally placed and signed the Thousand-Year Snow Ginseng in the casket entrusted to the Yongbong Escort Bureau.
- **Personality:** No personality traits are established.
- **Voice:** No voice traits are established.
- **Relationships:** The Pill Physician heads the Seongsu Jang Family, a prestigious medical family in Shandong.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 934
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is the Emperor’s thirteen-year-old younger brother, an exceptionally skilled young swordsman, and the newly appointed Crown Prince.
- **Personality:** Earnest and compassionate, he takes responsibility for others’ suffering and dreams of a peaceful age founded on justice, care for the people, wise counsel, and accountability, even when doing so demands personal sacrifice.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Zhu Bao is the Emperor’s younger brother and Crown Prince, and Hong Jin has been his steadfast caretaker since childhood. He admires Jin Taekyung and calls him a friend; his compassion for the Eastern Heaven Demon Lord reflects the different path made possible by those who supported him.

## Korean source

```text
＃936화



황제가 혈혼고에 중독되었다는, 실로 중차대한 소식을 접한 적천강의 감상평은 짧고 굵었다.

“아프겠군.”

“……?”

“왜, 노부의 말이 틀렸느냐?”

“그 뭐, 틀린 말은 아니긴 한데 단순히 아픈 정도가 아니잖아요.”

누가 들으면 혈혼고가 아니라 감기인 줄 알겠네.

황당해하는 내 모습에 적천강이 어깨를 으쓱해 보였다.

“이거나 그거나. 결국에는 아파서 죽을 지경까지 왔다는 것 아니냐. 저 쓸데없이 입 무거운 돌팔이 놈도 못 고칠 만큼.”

적천강의 갑작스러운 지목에, 앞서 내가 이야기하는 내내 떨떠름한 표정을 짓고 있던 신의가 입을 열었다.

“당신께서 직접 말씀하시기 전까지는 누구에게도 알리지 말라 하기에 환자의 뜻을 따랐을 뿐입니다. 그리고 제가 왜 돌팔이입니까?”

“의원이라는 자가 병을 못 고치면 돌팔이지. 오늘부로 신의라는 이름표도 떼라.”

“붙인 적도 없습니다. 애초에 제 것도 아니었고요.”

“기왕 말 나온 김에 하나만 묻자. 만약에…….”

“무슨 생각이신지는 알겠습니다만, 설령 스승님이 오시더라도 달라지는 것은 없을 겁니다.”

그렇지 않아도 나 역시 묻고 싶었던 부분이었지만, 한 박자 먼저 흘러나온 신의의 대답은 침착하고 단호했다.

“혈혼고는…… 지금까지 알려진 여러 극독과도 궤를 달리합니다. 오직 숙주를 죽이기 위해 만들어진 독물(毒物)이 아닐까 생각될 정도로 말입니다.”

적천강이 침음을 흘렸다.

“말인즉슨, 해약(解藥)이 없다?”

“본래 독과 약은 한 뿌리나 다름없으니, 치료법은 반드시 있을 겁니다. 다만 문제는 시간이지요.”

맞다. 황제는 지금 이 순간에도 죽어 가고 있다.

사흘 전, 대연회장에서의 전투가 끝난 직후 그가 유난히도 지치고 피로해 보였던 것은 결코 착각이 아니었다.

“제가 살펴본 바로는 이미 기력이 한계에 다다랐습니다. 앞으로 두어 달은 더 버틸 수 있을지조차 장담할 수 없는 상황이지요.”

신의가 이렇게까지 말한다는 건, 이미 영약이나 공력으로도 독기를 막을 수 없을 지경까지 왔다는 뜻이다.

마치 계속해서 물을 부어도 채워지지 않은 구멍 난 항아리처럼, 황제의 생기(生氣)는 빠르게 사라지고 있었다.

‘이대로면 얼마 안 가서 죽고 말겠지. 황제가 급사하면 대국이 뒤엎어질 테고.’

개인적인 감정을 떠나, 황제는 죽어서는 안 되는 인물이다.

온갖 오욕(汚辱)을 뒤집어쓰고도 별다른 잡음 없이 십 년이 넘는 세월 동안 대국을 통치해 온 그다.

더군다나 동천마군이 이끄는 강력한 반대 세력이 있음에도 황위를 지켰다는 것은, 그가 얼마나 뛰어난 능력을 지닌 군주인지 증명하는 부분이었다.

‘반드시 살려야 한다. 앞으로의 일을 위해서라도.’

이미 황궁 밖은 숯불 위 가마솥처럼 끓어오르고 있다고 했다.

내가 깨어나기 이틀 전, 다시 한번 대규모 숙청을 거행한 황제가 황도 곳곳에 수백 장이 넘는 방을 붙였기 때문이었다.

옥새(玉璽)의 날인이 선명히 찍힌 그 커다란 종이에는, 지금까지의 모든 진상이 낱낱이 적혀 있었다.

이른바 암천(暗天)이라 불리는, 극악무도한 역적들을 토벌하겠다는 황제의 일갈도 함께.

‘이제 곧 전쟁이 시작된다.’

아니, 이미 시작되었다.

황제의 의지는 분명했고 암천을 향한 백성들의 분노는 들불처럼 타오르고 있었다.

그들에게 있어 암천이란 삶의 터전과 자신들의 생명을 위협하는 외적(外敵)에 지나지 않는다. 그 누구도 전쟁을 원하지 않지만, 평화를 지키기 위해서는 맞서 싸워야 했다.

그리고 이 전쟁에는, 모두를 이끌 지도자가 필요하다.

냉정하며 빈틈없고, 때로는 과감한 결단을 밀어붙일 수 있는 위엄을 지닌 강력한 지도자가.

거기에 더해 여러 전장을 전전했던 경험까지 있다면, 그야말로 더할 나위 없다.

“진 공자께서는 어찌하실 생각입니까.”

무거운 표정으로 입을 연 신의를 향해, 나는 담담하게 대답했다.

“그야 어떻게든 살려 내야죠.”

“하지만 그 방법이라는 것이 없지 않습니까. 앞서 말씀드렸다시피 시간이 충분치 않습니다.”

“괜찮습니다. 아마도 제가 시도하려는 방법은 그리 오랜 시간이 필요하진 않을 거라서.”

“이렇게까지 말씀하신다는 건…… 뭔가 제가 모르는 묘책이 있으신 모양이군요.”

“맞아요. 있습니다. 기가 막힌 묘책이.”

자신감 넘치는 태도로 대답하는 내 모습에, 말없이 오가는 대화를 듣고 있던 적천강이 문득 눈을 크게 떴다.

“잠깐. 네놈이 말하는 묘책이라는 게 혹시.”

“지금 생각하시는 그게 맞습니다.”

“이런, 깜빡하고 있었군. 그래, 그 귀물(貴物)이라면 이야기가 다르지.”

뒤늦게 한 물건의 존재를 떠올린 적천강이 이마를 탁, 치자 그제야 신의도 놀란 듯이 눈을 깜빡였다.

“설마, 만독지환(萬毒指環)을 염두에 두고 계신 겁니까?”

“예. 당연한 거 아닙니까?”

“허어.”

낮게 탄식하는 신의의 모습에, 나는 피식 웃으며 말을 이었다.

“제아무리 혈혼고라고 해도 만독지환이면 충분한 가능성이. 아니, 확실히 치료할 수 있습니다.”

잠시나마 적천강의 위협했던 무형지독마저 어렵지 않게 흡수했던 만독지환이다.

당시 살성과 함께 적천강을 치료했던 신의는 누구보다 그 사실을 잘 알고 있는 사람이었기에, 그가 지금까지도 만독지환을 떠올리지 못했다는 것이 나로서는 희한할 정도였다.

“아무래도 상황이 상황이다 보니 많이 정신이 없으셨나 보네. 이해합니다. 그럴 수 있어요.”

“그, 진 공자.”

“괜찮다니까요. 다만 아시다시피 상산왕. 아니지, 황태제에게 잠시 맡겨 두었으니 곧바로 찾아오겠습니다. 잠깐이면 되니까 그때까지 치료 준비나 해 두시면 될 것 같네요.”

“진 공자?”

“아이고, 사람이 살다 보면 깜빡하고 그럴 수도 있죠. 뭘 또 자꾸 그렇게까지 말씀을 하세요. 전 이만 갑니다.”

나는 사람 좋은 미소와 함께 돌아섰다.

아니, 정확히는 돌아서려고 했다.

어느샌가 신의의 손에 들려 있는 무언가를 보기 전까지는.

“……?”

잠깐만. 저거 뭐야.

매우 익숙한 형태의 반지를 말없이 바라보던 나는, 짧은 침묵을 깨트리며 입을 열었다.

“참 이상하네요. 내가 아는 뭔가랑 많이 닮았네.”

신의가 짜게 식은 눈빛으로 대답했다.

“닮을 수밖에 없을 겁니다.”

“역시 대륙이라 그런지 모조품 하나는 끝내주네. 어디서 사셨어요?”

“산 거 아닙니다.”

“아, 선물로 받으셨구나.”

“선물도 아닙니다. 잠시 빌렸습니다.”

“누구한테?”

“황태제 전하께 대강의 사정을 말씀드리고 받아왔습니다. 중요한 일에 필요하여 진 공자를 대신해 왔다고 하니, 자세히 묻지 않고 내주시더군요.”

눈앞이 아찔하다.

호흡을 가다듬은 나는 어렵사리 입을 열었다.

“그, 중요한 일이라는 게 혹시…….”

“뭐겠습니까. 오늘 건청궁에만 두 번 들렀습니다.”

“폐하께 그런 말은 못 들었는데…….”

“굳이 그런 말까지 할 필요가 있었겠습니까.”

“그럼 결과는……?”

“앞서 말씀드린 그대로입니다.”

또다시 침묵이 내려앉았다.

전보다도 훨씬 무겁고, 숨 막히는 침묵이.

그리고 그 누구도 섣불리 입을 열지 않는 가운데, 적천강의 나지막한 한 마디가 울려 퍼졌다.

“기가 막히다 못해, 코까지 막힌 묘책이었군.”

“…….”

“…….”

그러게.

이제 어쩌냐.



* * *



퀘스트



[닥터 최태경]



당신은 병마로 고통받는 황제에게 치료를 약속하여 매우 깊은 인상을 남겼습니다.

그러나 죽음을 앞둔 이에게는, 섣부른 희망보다 잔인한 것은 없습니다.

남아일언중천금. 약속을 지키십시오.

황제의 머릿속에 자리 잡은 혈혼고를 제거하여, 오랜 세월 그를 괴롭혀 왔던 고통에서 해방시키십시오.

만약 황제를 치료하지 못한다면…….



등급 : 초절정

제한 : 진태경

임무 : 성공적인 치료 (미완료)

보상 : ???

실패 : ???





말없이 허공을 바라보던 나는 조용히 홀로그램 창을 껐다.

머릿속에는 이미 한 가지 생각만 가득했다.

‘조졌네.’

진짜 조졌다.

설마하니 만독지환까지 안 먹힐 줄 누가 알았겠나.

현실을 받아들이지 못한 내 다그침에도 신의에게서 돌아오는 대답은 한결같았다.



‘실패했습니다.’

‘아, 될 것 같았는데?’

‘아닙니다. 실패했습니다.’

‘그러니까, 될 것 같았는데 한 끗 차이로?’

‘그게 아니라 완전히 실패했습니다. 그냥 안 먹힙니다. 오히려 만독지환의 기운을 느낀 혈혼고가 위기를 느끼고 더욱 몸부림치더군요. 지금도 그때만 생각하면 식은땀이 흐릅니다.’

‘거짓말. 이런 질 나쁜 장난이나 치고. 이 개구쟁이.’

‘……진 공자. 잠시 저쪽에서 이야기 나누시겠습니까?’



신의의 소매 속에서 뭔가가 반짝하길래 봤더니, 코끼리 발바닥도 뚫을 것 같은 대침(大針)이더라.

나도 모르게 간담이 서늘해져서 도망치듯이 처소로 돌아왔던 것이 불과 일각 전이었다.

‘이런 제기랄.’

내가 무슨 배짱으로 황제에게 무사 퇴원을 약속했겠나.

다 만독지환이라는 사기템을 믿고 했던 말이다. 무형지독도 어렵지 않게 해결했는데, 그깟 벌레 한 마리 못 잡아 죽일까 싶어서.

그런데.

“망했다.”

그래, 망했다.

심지어 망해도 보통 망한 게 아니다.

단순히 퀘스트를 떠나서 황제의 죽음은 막아야 하는데, 만독지환이라는 마지막 희망마저 사라지자 눈앞이 샛노랬다.

“도대체…… 이걸 어떡해야 하지?”

이제는 익숙해진 천장을 바라보며 망연자실하게 중얼거린 그때, 이제는 당연하다는 듯이 방 한구석을 차지하고 있던 혁무진이 다가와 어깨를 토닥였다.

“괜찮습니다, 조장님. 다 괜찮아요.”

“무진아.”

“예.”

“너, 뭐 알고 씨부리는 거야?”

“알죠.”

자신 있게 고개를 끄덕인 혁무진이 말을 이었다.

“주 소저께 차이신 거 아닙니까?”

“…….”

“허허. 아닌가 보네요, 제가 주제넘었습니다. 죄송합니다.”

사과하는 속도만큼은 초절정 고수 그 자체다.

광속으로 허리를 굽혀 인사한 녀석은 아직도 미련이 뚝뚝 묻어 나오는 눈으로 내 목에 걸린 회중시계를 바라보며 입을 열었다.

“그나저나, 도대체 무슨 일이길래 그러세요?”

“무진아. 말을 할 때는 눈을 봐야지. 시계를 보지 말고.”

“빛이 워낙 영롱해서 저도 모르게 그만.”

뒤통수 한 대 쥐어박고 싶은 마음이 간절하지만, 지금은 그럴 만한 기운도 없다.

한숨을 푹 내쉰 나는 대략적인 상황을 설명했다. 이야기의 주인공이 황제라는 것이 드러나지 않도록 조심해가며.

“그러니까, 중병에 걸린 누군가한테 다른 누군가가 치료를 약속했다 이거네요.”

“그래.”

“그런데 한바탕 호언장담을 해놓고, 아무런 대책이나 방법도 없는 거고요.”

한 마디, 한 마디가 뼈아프다.

타격감에 몸을 움찔거리던 나는 조심스럽게 한 마디를 보탰다.

“맞긴 한데, 정확히는 있었다가 없어졌다고 봐야지.”

“그래 봤자 결국은 치료할 방법이 없다는 거 아닙니까?”

“그렇지.”

“음. 알겠습니다. 감 잡았어요.”

고개를 끄덕인 혁무진이 준엄한 목소리로 선언했다.

“거, 아주 씹새끼네요.”

“……!”

“조장님께서도 그렇게 생각하지 않으십니까? 이제 겨우 맘 잡고 죽음을 받아들이는 사람한테 그따위로 희망을 주면 어떡해요. 뭐 하나 확실한 것도 없으면서. 어떻게 되먹은 새낀지는 몰라도…….”

그 순간, 파르르 떨고 있는 내 모습을 본 혁무진이 확연히 줄어든 목소리로 말을 이었다.

“참으로 잘생기고, 위엄이 넘치며, 언제나 다른 이에게 희망을 심어 주는 올바른 청년이라고 생각합니다.”

“…….”

“…….”

“……다했냐?”

“……더 할까요?”

“……아니.”

더 비참해지니까 그만해, 이 새끼야.

슬픈 눈빛으로 들리지 않는 한 마디를 건넨 내가 차마 혁무진을 마주 보지 못하고 고개를 떨군 그 순간.

타다닥.

빠르게 다가오는 인기척과 함께, 문이 열리며 익숙한 얼굴이 나타났다.

“중요한 일이라길래 최대한 빠르게 처리했…… 어머, 분위기 왜 이래요?”

홍진이었다.
```

## Final English reading copy

```markdown
# Chapter 936

Jeok Cheongang’s reaction to the truly grave news that the Emperor had been poisoned with Blood Soul Gu was short and to the point.

“That must hurt.”

“……?”

“What? Am I wrong?”

“Well, no, but it’s not just a matter of being in pain.”

Anyone listening would think the Emperor had a cold instead of Blood Soul Gu.

At my baffled expression, Jeok Cheongang shrugged.

“Same difference. He’s in so much pain he’s on the verge of dying, isn’t he? Bad enough that even that tight-lipped quack can’t cure him.”

At Jeok Cheongang’s sudden jab, the Divine Physician—who’d worn a troubled expression the whole time I’d been talking—spoke up.

“I was told not to tell anyone until you spoke of it yourself, so I simply respected the patient’s wishes. And why am I a quack?”

“If a physician can’t cure an illness, he’s a quack. Take that Divine Physician name tag off today.”

“I never put one on. It wasn’t mine to begin with.”

“Since we’re on the subject, let me ask you something. What if……”

“I know what you’re thinking, but even if my Master came, it wouldn’t change anything.”

It was something I’d wanted to ask, too. But the Divine Physician’s answer came a beat ahead of me, calm and firm.

“Blood Soul Gu…… is in a class of its own, unlike any of the many deadly poisons known to us. It’s almost as if it was created for the sole purpose of killing its host.”

Jeok Cheongang let out a low groan.

“So you’re saying there’s no antidote?”

“Poison and medicine are two sides of the same coin, so there must be a way to treat it. The problem is time.”

He was right. The Emperor was dying even now.

The fact that he’d looked especially exhausted and drained after the battle in the grand banquet hall three days ago hadn’t been my imagination.

“From what I’ve seen, his vitality is already at its limit. I can’t even guarantee he’ll last another couple of months.”

For the Divine Physician to say that much meant the poison had advanced beyond anything even elixirs or internal energy could hold back.

Like a jar full of holes that wouldn’t fill no matter how much water you poured into it, the Emperor’s life force was draining away fast.

*At this rate, he’ll die before long. If the Emperor dies suddenly, the Great Nation will be thrown into chaos.*

Personal feelings aside, the Emperor couldn’t die.

He’d borne every kind of humiliation and ruled the Great Nation for over ten years without any serious disturbance.

And the fact that he’d held on to the throne despite facing a powerful opposition led by the Eastern Heaven Demon Lord proved what an exceptional ruler he was.

*I have to save him. If only for what’s coming.*

I’d heard the Imperial Capital was already simmering like a cauldron over hot coals.

Two days before I woke up, the Emperor had carried out another large-scale purge, then posted hundreds of proclamations across the capital.

Those huge sheets of paper, stamped clearly with the Imperial Seal, laid out the whole truth in detail.

They also carried the Emperor’s declaration that he would crush the vile traitors known as Dark Heaven.

*The war is about to begin.*

No—it had already begun.

The Emperor’s resolve was clear, and the people’s anger toward Dark Heaven was spreading like wildfire.

To them, Dark Heaven was nothing more than a foreign enemy threatening their homes and their lives. No one wanted war, but they had to fight to protect the peace.

And this war needed a leader to guide them all.

A powerful leader—cool-headed and meticulous, with the authority to make bold decisions when the time came.

Someone with experience on many battlefields would be ideal.

“What do you intend to do, Young Master Jin?”

I answered the Divine Physician, who’d spoken with a grave expression, as calmly as I could.

“We have to save him somehow.”

“But there is no way to do that. As I said, we don’t have enough time.”

“That’s all right. The method I’m going to try probably won’t take long.”

“The fact that you speak so confidently…… suggests you have some plan I don’t know about.”

“Right. I do. A brilliant plan.”

At my confident reply, Jeok Cheongang, who’d been listening to our conversation in silence, suddenly widened his eyes.

“Wait. The plan you’re talking about wouldn’t happen to be……”

“You’re thinking of the right thing.”

“I’d forgotten all about it. Yes, that precious treasure changes everything.”

Jeok Cheongang tapped his forehead. Only then did the Divine Physician blink in apparent surprise.

“Don’t tell me you have the Myriad-Poison Ring in mind?”

“Of course. What else?”

“Huh……”

At the Divine Physician’s low sigh, I gave a short laugh and continued.

“Even against Blood Soul Gu, the Myriad-Poison Ring gives us a good chance. No—it can definitely cure him.”

The Myriad-Poison Ring had effortlessly absorbed even the Formless Ultimate Poison, which had once threatened Jeok Cheongang.

The Divine Physician had treated Jeok Cheongang alongside the Slaughter Saint back then. He knew better than anyone what the ring could do, so I found it strange that he hadn’t thought of it until now.

“I guess you’ve had a lot on your mind, given the circumstances. I understand. It happens.”

“Y-Young Master Jin.”

“It’s fine. As you know, I left it with Prince Shangshan—or rather, the Crown Prince. I’ll go get it right away. It’ll only take a moment, so you can start preparing the treatment in the meantime.”

“Young Master Jin?”

“Oh, come on. Anyone can forget something now and then. Why are you making such a big deal of it? I’ll be off, then.”

I turned with a friendly smile.

Or, more precisely, I was about to turn—until I noticed the object in the Divine Physician’s hand.

“……?”

Wait a second. What’s that?

I stared at the very familiar-looking ring in silence, then broke it.

“That’s strange. It looks a lot like something I know.”

The Divine Physician replied with a flat stare.

“It would have to. It is the same thing.”

“I guess they make great knockoffs on this continent. Where’d you buy it?”

“I didn’t buy it.”

“Oh, someone gave it to you as a gift?”

“It wasn’t a gift, either. I borrowed it for a while.”

“From whom?”

“I told His Highness the Crown Prince the general situation and borrowed it from him. I said I’d come on your behalf because it was needed for something important. He handed it over without asking for details.”

My vision swam.

I drew a breath and managed to speak.

“Th-this important matter wouldn’t happen to be……”

“What else could it be? I’ve been to Qianqing Palace twice today.”

“I didn’t hear anything about that from His Majesty……”

“Was there any need to tell you?”

“Then the result was……?”

“Just as I told you earlier.”

Silence fell once again.

Heavier and more suffocating than before.

No one dared to speak out of turn. Then Jeok Cheongang’s low voice rang out.

“Quite a plan. It was so brilliant it plugged up your nose, too.”

“……”

“……”

Yeah.

What now?


* * *


> **System**
> 
> **Quest**
> 
> **Dr. Choi Taekyung**
> 
> You made a profound impression on the Emperor, who suffers from illness, by promising to treat him.
> 
> But for someone standing at death’s door, nothing is crueler than giving them hope too soon.
> 
> A man’s word is worth a thousand gold. Keep your promise.
> 
> Remove the Blood Soul Gu lodged in the Emperor’s head and free him from the pain that has tormented him for so many years.
> 
> If you fail to treat the Emperor……
> 
> **Grade:** Supreme Peak
> 
> **Restriction:** Jin Taekyung
> 
> **Mission:** Successful treatment (Incomplete)
> 
> **Reward:** ???
> 
> **Failure:** ???

I stared at the air in silence, then quietly closed the holographic window.

There was only one thought filling my head.

*I’m screwed.*

Really screwed.

Who could’ve guessed even the Myriad-Poison Ring wouldn’t work?

No matter how much I pressed him, unwilling to accept reality, the Divine Physician gave me the same answer every time.

*“It failed.”*

*“Huh? But it looked like it was going to work.”*

*“No. It failed.”*

*“So it almost worked, but missed by a hair?”*

*“That’s not what I mean. It failed completely. It just doesn’t work. In fact, the Blood Soul Gu sensed the Myriad-Poison Ring’s energy, felt threatened, and started thrashing around even more. I still break into a cold sweat whenever I think about it.”*

*“Liar. Playing such a nasty prank on me. You little rascal.”*

*“……Young Master Jin. Would you care to speak with me over there for a moment?”*


I’d noticed something glinting inside the Divine Physician’s sleeve. It turned out to be a huge needle that looked like it could pierce an elephant’s foot.

A chill ran down my spine, and I fled back to my quarters. That had been barely fifteen minutes ago.

*Damn it.*

What nerve had I had to promise the Emperor he’d make a full recovery?

I’d said it because I trusted the Myriad-Poison Ring, that overpowered item. It had dealt with the Formless Ultimate Poison without any trouble. Surely it could kill one lousy bug.

And yet.

“I’m screwed.”

Yeah. Screwed.

And not just a little.

Forget the quest—the Emperor’s death had to be prevented. But with my last hope, the Myriad-Poison Ring, gone, my vision had gone yellow.

“What the hell…… am I supposed to do now?”

I stared blankly at the ceiling I’d grown accustomed to, muttering to myself. Then Hyuk Mujin—who seemed to have claimed one corner of the room as his own—came over and patted my shoulder, as if this were only natural.

“It’s all right, Captain. Everything’s all right.”

“Mujin.”

“Yes?”

“Do you even know what the hell you’re talking about?”

“I do.”

Hyuk Mujin nodded confidently and continued.

“You got dumped by Young Lady Zhu, didn’t you?”

“……”

“Ah. Guess not. I’m sorry for overstepping.”

At least when it came to apologizing, he was a Supreme Peak master.

The guy bowed at the speed of light. Then he looked wistfully at the pocket watch hanging from my neck and asked,

“But seriously, what happened?”

“Mujin. When you’re talking to someone, you should look them in the eye. Not at their watch.”

“It was so radiant, I couldn’t help myself.”

I desperately wanted to whack him on the back of the head, but I didn’t have the energy for it right now.

I let out a long sigh and explained the situation in broad strokes, taking care not to reveal that the Emperor was the person at the center of the story.

“So someone with a serious illness had another person promise to treat them.”

“Yeah.”

“But after making all those grand claims, that person had no plan or method at all.”

Every word hit hard.

I flinched from the blow and cautiously added,

“That’s right, but it’s more accurate to say there was a plan and then it disappeared.”

“Either way, that still means there’s no way to treat them, right?”

“Right.”

“Hmm. Got it. I see what’s going on.”

Hyuk Mujin nodded and announced in a stern voice,

“What a total piece of shit.”

“……!”

“Don’t you think so too, Captain? How could someone give a person who’d finally made peace with death that kind of hope? When they haven’t got a single thing figured out. Whoever the hell that bastard is……”

Seeing me tremble, Hyuk Mujin continued in a much quieter voice.

“I think he’s a very handsome and dignified young man who always gives others hope and does the right thing.”

“……”

“……”

“……You done?”

“……Want me to keep going?”

“……No.”

Don’t make me feel any worse, you bastard.

I gave him a silent word with sad eyes, then lowered my head, unable to look Hyuk Mujin in the face.

Tap-tap-tap.

Fast approaching footsteps came with an opening door, and a familiar face appeared.

“I heard it was important, so I took care of it as quickly as I could…… Oh my, why’s the mood so grim?”

It was Hong Jin.
```
