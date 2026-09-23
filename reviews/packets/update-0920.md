<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0920.txt",
      "sha256": "195bc92a4147910d584851f3325c6b06b27e74990723a3cf9a8abc451b9ec4cd",
      "bytes": 15596
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "e492f0fa80a92b05e5ab27b579b5cd0d025f789f6d85327f25cdd9275c53ebc9",
      "bytes": 1362
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "e4f261a256443b1a8267b983fdbd4ae7aa3530803a007681e483b189b757b921",
      "bytes": 231635
    },
    {
      "path": "characters/Baek Yeon.md",
      "sha256": "43536bf77001cc486c9b6b787b0546bbbd23aa4c5495cd90fb1e21be34b40906",
      "bytes": 837
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "0ffde581a211e47992348538e0e54d18682b91192d9fe69caa0c09ee32ed61ab",
      "bytes": 759
    },
    {
      "path": "characters/Eastern Heaven Demon Lord.md",
      "sha256": "8ed1ff367ce0bd67d4a745902852eaf0d4a543351575b5c94db44602b54ff177",
      "bytes": 807
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "8f7d39ea155455e5a6f397ac93b0888a732f0c0b8dd63596ee47d43ce80869b5",
      "bytes": 1244
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "dccf3e04538228613531ad593c949ebf4c657516e12df4cf3623020c4fa14793",
      "bytes": 1429
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "f152ef01470895a5470844294b5fe8c9ecdf5bb01bb17d05fe6379260bc6f86a",
      "bytes": 622
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "b8a409c487c7536a52c951197817b1ef3f9d8b18f3cafa546083e363caf0eb6e",
      "bytes": 850
    },
    {
      "path": "characters/So Gyo.md",
      "sha256": "a645fe17f1bd804f4581c662dd7835a7b5a7d21de5d70477e7655b79c7e38f1b",
      "bytes": 900
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "3eb46d69786f2a320514a4de60ce386a1a455eb20e966e881679b96c100d03e9",
      "bytes": 265121
    }
  ],
  "estimated_tokens": 12880
}
-->

# Durable State Update — Chapter 920

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
1 and safe_through 920. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 920. Profile updates may replace only one
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
  "chapter": 920,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 920,
    "continuity_sources": [920],
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
    "Jin Taekyung killed Gye Yabu of the Salcheonmun; the System warns that the sect will pursue him if it learns of his role.",
    "The Salcheonmun vowed to pursue Mungyeong, the Slaughter Saint, regardless of the cost or delay.",
    "Jeok Cheongang and Jin Taekyung survived the confrontation with the assassins and the Eastern Heaven Demon Lord.",
    "The Eastern Heaven Demon Lord is alive but has lost all four limbs.",
    "The Eastern Heaven Demon Lord's rebellion has powerful military and political supporters beyond the banquet hall.",
    "Thousands of soldiers arrived, but a powerful beam of light struck them; the outcome is unknown."
  ],
  "continuity_sources": [
    919
  ],
  "open_questions": [
    "What enabled Jin Taekyung to return from his seemingly fatal injuries?",
    "Will the Salcheonmun pursue Mungyeong, and will it discover Taekyung killed Gye Yabu?",
    "What happened to the thousands of soldiers struck by the beam of light?",
    "What is So Gyo's identity and allegiance, and why did the Eastern Heaven Demon Lord call her name?",
    "What information does the Eastern Heaven Demon Lord hold about Dark Heaven and the Lord of Heaven?"
  ],
  "safe_through": 919,
  "temporary_decisions": [
    "Keep “Force” for 강기 distinct from “death energy” for 사기."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 궁성     | **Bow Saint**                 | —              |
| 암천     | **Dark Heaven**                  |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 백연 | **Baek Yeon** | Commander of the Embroidered Uniform Guard. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 소교 | **So Gyo** | The palace attendant leading the group assigned to serve Prince Shangshan. |
| 선황 | **the late Emperor** | The former Emperor whom Hong Jin served. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 외궁 | **Outer Palace** | The outer compound of the Nanman Beast Palace. |
| 초일류 | **Supreme First Rate** | Realm attained by each Baekcheon Unit member. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |
| 금위군 | **Imperial Guards** | Imperial force distinct from the Embroidered Uniform Guard. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 백연 | young martial artist confronting an imperial military commander | you | casual and insulting | Refers to Baek as 이 양반 while challenging his conduct. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 소교 | 진태경 | palace attendant addressing a martial artist and guest under escort | Young Master Jin | formal and respectful, but firm | Addresses him as 진 공자 while escorting him and warning him not to investigate. |
| 진태경 | 소교 | palace attendant and martial artist under imperial scrutiny | you | formal-polite, controlled and challenging | Taekyung addresses So Gyo as 당신 while questioning her presence and demanding an explanation. |
| 백연 | 진태경 | imperial commander confronting a young martial artist | Jin Taekyung | measured and familiar, using 자네 | Baek Yeon cautions Taekyung about his words and asks whether he must cause a scene. |
| 소교 | 백연 | political ally addressing a senior military commander | you | informal and direct | So Gyo uses 당신 and speaks without formality; no personal name or title is established. |
| 백연 | 소교 | military commander addressing a powerful political ally | you | formal and deferential | Baek Yeon uses 그대 while questioning So Gyo; she speaks without formality, which he accepts as her due. |
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
| 동천마군 | 진태경 | enemy recognizing the spear wielder | Jin Taekyung | shouted, informal | The Demon Lord cries Taekyung's name after identifying him as the spear's owner. |

## Listed compact profiles

### Baek Yeon.md

# Baek Yeon (백연)

- **Safe through:** Chapter 915
- **Aliases:** Blood Envoy
- **Role:** Baek Yeon is the Commander of the Embroidered Uniform Guard, a former martial arts instructor to the Crown Prince, and the Blood Envoy who helped the fourth prince seize the throne and led the purge.
- **Personality:** Politically assured and controlled, he enforces authority with ruthless decisiveness but speaks with striking defiance to the Emperor in private when their shared undertaking is at stake.
- **Voice:** Not established
- **Relationships:** He commands the Embroidered Uniform Guard and serves the Emperor, carrying out the late Emperor’s final command to plan for the future alongside the fourth prince; he treats Taekyung as a dangerous potential obstacle.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 919
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Eastern Heaven Demon Lord.md

# Eastern Heaven Demon Lord (동천마군)

- **Safe through:** Chapter 919
- **Aliases:** None
- **Role:** The Eastern Heaven Demon Lord is a former Maoshan Sect disciple who commands the dead with a bell and has spent half a century infiltrating the imperial court while building a far-reaching rebellion.
- **Personality:** His hatred of rulers is rooted in the loss of his family to the violence of the age of chaos and the destruction of the Maoshan Sect, where he had found happiness.
- **Voice:** He speaks in measured, almost lyrical phrasing, recounting the past before turning to pointed accusations.
- **Relationships:** Ma Sanbao is his Disciple; he holds the Emperor responsible for Taizu’s actions against the Maoshan Sect.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 919
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts Jin Taekyung, his publicly acknowledged second Disciple and intended heir; warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, remains Peng Cheolhu's rival, and is the target of an attack by the assassin Heaven's Slaughter.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 919
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Ma Sanbao, whom Taekyung killed, has been raised among the Eastern Heaven Demon Lord’s undead, while Jeong Hogun and the Embroidered Uniform Guard have declared themselves allies of the Emperor, and So Gyo’s allegiance remains unknown.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 919
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 919
- **Aliases:** None
- **Role:** Ma Sanbao is the East Depot’s Brush-Holding Eunuch and a Supreme Peak martial artist who secretly led a restoration effort for Prince Shangshan as a disciple of the Eastern Heaven Demon Lord.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks in measured, courteous language and uses calm repetition, feigned agreement, and procedural reminders to steer conversations while keeping sensitive details guarded.
- **Relationships:** Ma Sanbao was a longtime friend and former East Depot cohort of Hong Jin, served the Eastern Heaven Demon Lord, and led a restoration effort for Prince Shangshan.

### So Gyo.md

# So Gyo (소교)

- **Safe through:** Chapter 919
- **Aliases:** None
- **Role:** A palace attendant assigned to Prince Shangshan who is a Supreme Peak master and has a mission to keep Jin Taekyung alive; her identity and allegiance remain unconfirmed.
- **Personality:** Calm, calculating, and self-possessed; she conceals her strength and identity and can be openly taunting.
- **Voice:** Measured and composed, shifting from deferential formality to casual, pointed taunts and threats.
- **Relationships:** She poses as the leader of the palace attendants assigned to Prince Shangshan and is Jin Taekyung’s opponent, yet believes he may be the person she seeks and the person foretold by “that person”; she says only she and the Emperor know a secret she withheld from Baek Yeon, while her true allegiance remains unknown.

## Korean source

```text
＃920화



모든 것이 한순간이었다.

적어도 무너진 외벽의 잔해를 타 넘어, 선봉으로 돌격하던 동창의 고수들은 그렇게 느꼈다.

화아악.

이것은 도대체 무엇일까.

어찌 이토록 빠르고, 파괴적일 수 있는 것일까.

눈앞을 물들이는 휘황한 섬광에 그들은 잠시 넋을 놓았고, 그것이 이승에서 본 마지막 광경이 되었다.

콰아아아앙!

거대한 굉음이 귓가를 후려친다. 항거할 수 없는 힘이 석상처럼 굳어 버린 육신을 휩쓸었다.

콰드득, 푸화아악!

들이닥친 것만큼이나 빠르게 사라진 섬광 속, 자신의 동료들을 따라 돌격하던 동창의 환관은 눈을 깜빡였다.

그리고 마침내 돌아온 시야와 함께 깨달았다.

조금 전의 그 섬광이, 누군가가 쏘아 보낸 강기(罡氣)였다는 것을.

그 무시무시한 기운이 수십여 명의 동료들을 휩쓸고, 자신의 한쪽 팔마저 앗아 갔다는 것을.

“아, 아아. 아아아……!”

턱이 덜덜 떨렸다. 쉴 새 없이 부딪치는 잇새 사이로 넋 나간 듯한 신음이 흘러나왔다.

죽었다. 아니, 도륙당했다.

이제는 더 이상 형체를 알아볼 수 없는 고깃덩어리가 되어 버린, 한때 동료였던 자들의 흔적을 확인한 동공이 이 믿을 수 없는 현실을 뇌로 전달했다.

마치 맹수에게 뜯겨 나간 듯, 처참하게 너덜거리는 어깻죽지로부터 뒤늦게 전해진 통증과 함께.

“크아아악!”

쩍 벌어진 입에서 고통에 찬 비명이 쏟아졌다.

아니, 지금 이 순간 극심한 혼란과 고통에 사로잡힌 것은 비단 그 한 사람뿐만이 아니었다.

“끄윽, 끄으으으.”

“사, 살려 주…….”

“우웁, 쿠에에엑!”

누군가는 잘린 두 다리를 부여잡고 신음하고, 누군가는 죽음의 끝에서 간절히 도움을 구걸했으며, 또 다른 누군가는 눈앞에서 벌어진 참극에 허리를 굽히고 토사물을 게우기도 했다.

두 눈으로 똑똑히 목격한 참혹한 죽음에 대한 두려움에, 아무것도 할 수 없던 무력감에 몸을 떨며.

한 걸음 늦게 현실을 인지한 이들도 상황은 크게 다르지 않았다.

“이, 이게 무슨.”

이미 오래전 동천마군에게 포섭되어 역모에까지 가담한 일부 금위군도, 그들을 이끌고 대연회장까지 들이닥친 동창의 환관들도 순간 할 말을 잃었다.

일격.

단 일격에 오십여 명에 달하는 병력이 죽거나 전투 불능상태에 빠졌다.

주저 없이 선봉에 섰던 만큼, 그들 한 사람 한 사람이 초일류에서 절정의 경지를 오가던 실력자들.

물경 삼천에 달하는 병력을 생각한다면 그리 큰 피해는 아니었으나, 모두의 발걸음이 멈춘 이유는 단 한 번의 공격으로 수십여 명의 절정 고수들을 집어삼킨 저 무시무시한 위력이었다.

아니, 악마와 같은 신위(神威)를 보인 고수의 존재였다.

‘도대체…….’

누구냐.

한 가지 의문이 모두의 뇌리를 관통했다.

대연회장을 휩쓸며 들이닥치던 삼천의 반란군도.

아무리 죽이고 또 죽여도 쓰러지지 않는 망자들과 맞서 싸우고 있던 금의위와 화룡각 대원들도.

심지어는 요령이 파괴됨과 동시에 더더욱 이성을 잃고 날뛰던 망자들도 본능의 경고에 따라 움직임을 멈추었다.

그리고 고개를 돌려 바라보았다.

섬광이 시작되었던 발원지(發源地)를.

그 무수한 시선의 끝에서, 꿈틀거리는 망자들의 사지를 짓밟고 우뚝 서 있는 누군가를.

솨아아.

어디선가 불어온 바람이, 여인의 풍성한 머리카락을 흔들었다.

“소교……!”

삽시간에 주위에 내려앉은 침묵 속, 뒤늦게 울려 퍼진 비명 같은 외침에 여인은, 아니 소교는 고개를 들어 목소리가 들려온 방향을 바라보았다.

정확히는, 그곳에 있는 한 사람을.

진태경.

소리 없이 달싹인 입술과 함께, 그녀의 검푸른 눈동자가 깊게 가라앉았다.



* * *



연단으로 이어진 수백여 개의 계단은 이미 무수한 시체로 뒤덮여 있었다.

일천에 달하던 망자들은 갈가리 찢겨 마침내 죽음을 맞이하거나, 사지가 토막 난 채로 버둥거렸다.

마치 누군가가 이 질긴 목숨을 끊어 주길 바라는 듯이.

서걱.

공간을 가로지르는 한 줄기의 섬광.

하나뿐인 팔로 엉금엉금 계단을 기어 올라오던 망자의 몸뚱어리를 반으로 가른 사내는, 쥐고 있던 검을 늘어트리며 가쁜 호흡을 내뱉었다.

후욱, 훅.

피와 땀에 절어 있는 전신이 들썩거린다.

예술품처럼 정교하고 화려한 황금빛 갑옷과 검은 그 어느 때보다 무겁게 느껴졌다.

아니, 어쩌면 그것은 사내가 지금껏 짊어지고 있던 책임감과 자책의 무게일지도 몰랐다.

그러나…… 후회는 없다.

없어야 했다.

오늘 이 자리에서 재가 되어 스러진 금의위들 역시 죽음을 각오했었으니.

그들이 스스로 받아들인 희생을 동정하는 것은, 죽음 이상의 모독이었으니.

설령, 사내가 하늘 아래 그 누구보다 존귀한 만인지상(萬人之上)의 존재라 하더라도.

“백연.”

사내, 황제는 쇳소리가 섞인 목소리로 입을 열었다.

그리고 선황과 황실을 지키기 위해 누구보다 애썼고 자신이 무너질 때마다 호된 질책으로 일으켜 세워 주었던, 그렇기에 신하보다는 동료였던 황실 제일의 무관에게 명령이 아닌 부탁을 건넸다.

“북을, 전고(戰鼓)를 울리게.”

“……!”

백연의 눈동자가 파르르 떨렸다.

그 어느 때보다 지치고 피로에 젖어 있는 황제의 모습을 눈에 담은 그는, 깊게 고개를 숙인 뒤 이 연회의 시작을 알렸던 커다란 북을 향해 일장(一掌)을 뻗었다.

두웅!

웅혼한 공력이 실린 북소리가 끝없이 뻗어 나갔다.

오늘날을 위해 긴 세월을 기다려야 했던 무장의 마음을 담아. 황제의 뜻을 담아.

한 번.

또다시 한번.

그것은 대연회장의 모두가 들을 수 있을 만큼 거대한 울림이었다. 아니, 대연회장을 넘어 황도 전체를 휩쓸 듯한 파도였다.

두우우웅!

세 번째 북소리가 울려 퍼졌을 때도 물경 삼천에 달하는 반란군들은 어찌할 바를 몰라 머뭇거렸다.

이 모든 일련의 상황들이 너무나도 자연스럽게 흘러갔으니까.

갑작스럽게 선봉을 휩쓴 소교의 막강한 무력에, 뭐라 설명할 수 없을 만큼 웅장하게 울려 퍼지는 북소리에 순간 자신들도 모르게 압도되었으니까.

심지어는 이 역모의 시작이자 중심인, 누구보다 앞장서서 그들을 이끌어야 할 동천마군조차 진태경과 적천강의 발치에 참혹한 몰골로 쓰러져 있었으니까.

‘무엇이냐. 도대체 무슨 일이 벌어지고 있는 것이냐.’

동천마군이 사로잡혔다. 마삼보는 어디에도 보이지 않는다.

이미 황실과 대국을 배반하여 암천의 휘하에 들어간 금위군과 동창의 수뇌부는 당황했다. 혼란스러운 눈빛으로 서로를 바라보았다.

외궁을 손에 넣었을 때만 해도 모든 것이 끝났다고 생각했다.

또 다른 아군이 황도를 휩쓴 틈을 타, 황궁으로 통하는 모든 문을 철저하게 봉쇄하고 남아 있던 수비 병력을 격파할 때만 해도 새로운 하늘이 열리리라 확신했다.

하지만 기쁜 마음으로 마주한 현실은, 진즉 승기를 잡았어야 했을 전황(戰況)은 달랐다.

처음 대연회장에 들이닥칠 때만 하더라도 힘차게 흩날렸던 깃발은, 이제 그들의 마음처럼 불안하게 흔들리고 있었다.

그리고 바로 그 순간.

둥. 두웅.

다시 한번 울려 퍼진 북소리가 그들의 귓가에 닿았다.

본능처럼 전신을 솜털을 바짝 곤두세우고, 등골을 서늘하게 엄습해 왔다.

앞서 들려온 것보다 크지도, 그렇다고 웅혼한 깊은 울림이 느껴지는 것도 아닌 네 번째 북소리.

그러나 그것이 그 어느 때보다 반란군의 가슴을 덜컥 내려앉게 만든 이유는 단 하나였다.

등 뒤.

저 멀리 보이는 백연이 아닌, 자신들의 등 뒤 어디에선가 들려온 북소리.

그것에 그치지 않고, 곧이어 사방으로 퍼져가는 그 울림.

두둥. 두두둥.

너른 들판을 휩쓰는 불길처럼 번져가는 그 무수한 북소리는 어딘가에 부딪혀 되돌아온 메아리도, 환청도 아니었다.

이 길고 참혹했던 연회의 끝을 알리는 신호였고, 마침내 덫에 걸린 먹잇감을 포위하는 사냥꾼들의 발걸음이었다.

드드득.

언제부터였을까.

저토록 많은 군세가 도대체 어디에, 무슨 이유로 지금껏 나서지 않고 숨어 있던 것일까.

‘함정!’

한 줄기 벼락이 정수리를 관통하는 듯한 충격과 동시에, 반란군들은 빠르게 가까워지는 거대한 진동을 느낄 수 있었다.

동시에 보았다.

마침내 사방에서 높이 솟아오른 수백여 개의 깃발을.

펄럭이는 깃발을 따라 살아 있는 것처럼 꿈틀거리는, 황금빛 수실로 수놓아진 한 마리의 용을.

“……!”

“……!”

보이지 않는 경악과 기쁨. 그리고 절망감이 대연회장 전체를 휩쓸었다.

누군가는 가슴이 터질 듯한 고양감에 사로잡혔고, 또 다른 누군가는 피가 나오도록 이를 악물었다.

삼천의 반란군은 후자(後者)였다.

수천. 혹은 수만.

정확한 적들의 숫자는 그 누구도 짐작할 수 없었으나 한 가지는 확실했다.

지금 이 순간에도 시시각각 포위망을 좁혀 오는 적들의 기세가 자신들을 압도하리라는 것.

반란군들은 엄습해 오는 살기를 느꼈다.

출렁이는 피 웅덩이에 비친 자신들의 얼굴을 보며, 곧 들이닥칠 불길한 미래를 떠올렸다.

그러나 동시에, 사면초가나 다름없는 이 절망적인 상황을 타개할 수 있는 유일한 방법을 떠올렸다.

모든 것의 중심이며, 시작이자 끝.

이 광활한 천하에서 가장 드높은 봉우리에 위치한 지존.

“황제를…….”

누군가의 입술 사이로 흘러나온 희미한 목소리는, 이내 살고자 하는 욕망으로 비롯된 거대한 외침이 되어 터져 나왔다.

“황제를 사로잡아라!”

성즉군왕 패즉역적(成卽君王敗卽逆賊)이라.

이미 절벽 끝에 몰린 그들에게 더 이상의 선택지는 없었다.

머리를 잃은 몸뚱어리는 움직이지 못하는 법.

황제를 비롯한 그 일가를 생포하여 이 반란을 성공시키는 것만이, 그들 앞에 놓인 유일한 활로(活路)였다.

“황제와 그 일가를 생포하는 자, 열후(列侯)가 되어 자손 대대로 부귀영화를 누리리라!”

그 순간.

드드드득!

수천의 인마(人馬)는 파도가 되어 나아갔다.

드높은 계단 위에서 노쇠한 얼굴로 자신들을 굽어보는 황제를 향해.

동시에 그 앞에 우뚝 선 한 여인에 대한 두려움을, 악에 받힌 함성으로 애써 지워 내며.

“으아아아아!”

“돌격하라! 멈추지 마라!”

비명과도 같은 그 고함이, 무수한 발걸음과 거센 말발굽 소리가 깊은 밤을 깨웠다. 사방이 장막처럼 드리워진 짙은 어둠을 뚫고 퍼져나갔다.

멀리, 더 멀리.

크고 또렷하게.

그러나 필사적으로 달려 나가는 그들의 움직임과 함성은 너무나도 느리고, 멀게만 느껴졌다.

적어도 지금 이 순간 서로를 마주한 어느 청년과 여인에게는 그랬다.

그가 그녀를, 그녀는 그를 바라보았다.

두 사람 사이에 놓인 백여 장의 거리는 지금 이 순간 아무런 의미도 없었다.

그들은 이미 알고 있었다.

자신들이 서로를 바라보고 있음을. 허공에서 부딪친 이 시선이 누구의 것인지를.

하지만 상대의 진정한 정체를 깨달은 것은, 오직 소교뿐이었다.

‘그래, 너였구나.’

뜻 모를 한 마디를 삼킨 소교는 말없이 발아래 펼쳐진 전장을 바라보았다.

거대했다. 동시에 참혹했다.

종횡으로 수백여 장에 이르는 대연회장은 핏물로 잠겨 있었다. 주인 잃은 병장기가, 팔다리가 굴러다녔고 부릅뜬 눈동자에서는 생명의 빛을 찾아볼 수 없었다.

잠시나마 울려 퍼진 풍악이 사라진 빈자리를 채운 것은 오직 죽음뿐이었고, 그 위에 새로운 죽음을 덧칠하기 위해 밀려드는 이들 또한 있었다.

솨아아아.

적들이 내지르는 거대한 고함 속, 어디선가 불어온 차가운 바람에 섬단 같은 머리카락이 풍성하게 부풀어 오른다.

바람을 타고 콧속 깊숙이 스며드는 혈향(血香)은 사방에 고여있는 선홍빛 핏물처럼 진했다.

세월에 잠겨 있던 과거의 편린을 그녀의 머릿속에서 끄집어낼 만큼.

잊고 싶었으나 잊을 수 없었던, 그 참혹했던 기억을 되살릴 만큼.

아마도 그런 이유일 것이다.

오랫동안 찾아 헤매었던 해답이자 열쇠를 찾아냈음에도, 조금의 기쁨조차 들지 않는 것은.

이 길고도 참혹했던 연회를 끝낼 때가 왔다는 확신이 든 것은.

스륵.

고요함 속에서 움직인 소교의 양손이, 핏물로 말라붙은 손아귀에 감겨있던 두 개의 곡도(曲刀)가 하늘과 땅을 향해 겨누어진다. 이내 서로를 향해 맞물린다.

스르릉, 철컥.

어느 장인의 수 없는 담금질과 두드림으로 완성된 강철이 서늘한 소리를 토해 냄과 동시에, 보이지 않는 홈과 그 안에 심어진 쇠붙이가 두 개의 병장기를 연결했다.

마치 처음부터 한 몸이었던 것처럼.

곡도가 아닌 다른 무엇이었던 것처럼.

우우우웅.

긴 세월 만에 본래의 모습을 되찾은 그것이 주인의 손안에서 몸을 떨었다. 깊숙이 스며드는 익숙한 기운과 공명(共鳴)하며, 빛을 닮은 눈물을 흘렸다.

지이잉.

파르르 떨리는 공기.

보는 이로 하여금 곡도를 떠올리게 만들었던, 비스듬히 꺾여나간 양 끝자락 사이로 새하얀 섬광이 이어진다.

오랜 과거의 모습 그대로.

누군가에게는 천벌이었고, 누군가에게는 구원이었던 그 시절의 위용을 간직한 채로.

“그래, 오랜만이구나.”

소교는 다정한 목소리와 함께 애병을 들어 올렸다.

그리고 수천, 수만 번도 넘게 그러했듯이 끝과 끝을 이은 섬광을 그러쥐고, 힘주어 당겼다.

스아아아.

허공에서 그려지듯 나타난, 섬광에 걸린 휘황한 빛줄기.

동시에 그 믿을 수 없는 광경이 멀리서 모든 것을 지켜보던 한 사람의 옛 기억을 일깨웠다. 먼지로 뒤덮인 과거에서 누군가의 모습을 일으켜 세웠다.

그 누구보다 거대한 활로, 벼락과도 같은 강기를 쏟아내며 전장을 지배했던 어느 노파를.

“궁성(弓星)……!”

바로 그 순간.

슈화아아아악!

소교, 아니 궁성의 손끝을 떠나 쏘아진 빛줄기가 대연회장을 가로질렀다.
```

## Final English reading copy

```markdown
# Chapter 920

It all happened in an instant.

At least, that was how it felt to the East Depot masters charging at the vanguard, scrambling over the rubble of the collapsed outer wall.

*Fwoosh.*

What in the world was this?

How could anything be so fast—and so destructive?

The dazzling flash washed over their vision, leaving them stunned for a moment. It was the last thing they ever saw.

*KABOOM!*

A tremendous roar battered their ears. An irresistible force swept over their bodies, frozen like stone statues.

*Crack! Fwoosh!*

The flash vanished as quickly as it had come. One of the East Depot eunuchs charging alongside his comrades blinked.

Then, as his vision finally cleared, he understood.

That flash had been Force someone had sent flying.

That terrifying energy had swept away dozens of his comrades—and taken one of his arms, too.

“A-ah. Ahh. Aaaaaah…”

His jaw trembled. A dazed moan slipped between his teeth as they clattered without pause.

They were dead. No—they’d been butchered.

His pupils, fixed on what remained of his former comrades, sent the impossible sight to his brain: chunks of meat so mangled he could no longer tell what they had been.

Only then did pain reach him from his shoulder, horribly shredded as though a beast had torn into it.

“GRAAAAH!”

A scream of agony poured from his gaping mouth.

But he wasn’t the only one consumed by shock and pain in that moment.

“Ugh… Uuugh.”

“P-please, save…”

“Ugh—bleurgh!”

Some groaned as they clutched their severed legs. Some pleaded desperately for help on the brink of death. Others bent over and vomited at the carnage before their eyes.

They trembled, terrified by the gruesome deaths they’d witnessed with their own eyes, helpless to do anything.

Those who realized what had happened a moment later were little better off.

“W-what is this…?”

Some of the Imperial Guards, long since recruited by the Eastern Heaven Demon Lord and drawn into the rebellion, and the East Depot eunuchs who had led them into the grand banquet hall were struck speechless.

One strike.

A single strike had killed or incapacitated more than fifty soldiers.

They had charged at the vanguard without hesitation, and every one of them was a formidable fighter, ranging from Supreme First Rate to Peak.

Compared to the full force of some three thousand, it wasn’t a major loss. But everyone had stopped because that one attack had swallowed dozens of Peak masters in its terrifying power.

No—it was because of the master whose might seemed almost demonic.

*Who…?*

Who was it?

The question pierced everyone’s mind.

The three thousand rebels who had surged into the grand banquet hall.

The Embroidered Uniform Guard and Fire Dragon Pavilion members fighting the dead who kept rising no matter how many times they were killed.

Even the dead, who had lost what little reason they had left when the bell was destroyed, stopped moving at some instinctive warning.

Then they turned their heads.

Toward the source of the flash.

At the end of countless gazes stood someone, trampling the twitching limbs of the dead.

*Whoosh.*

A breeze from somewhere stirred the woman’s thick hair.

“So Gyo…!”

In the silence that had fallen over the hall, a cry like a scream rang out belatedly. The woman—no, So Gyo—lifted her head and looked toward the voice.

More precisely, at the person standing there.

Jin Taekyung.

Her lips moved silently, and her dark blue eyes sank deep.

* * *

Hundreds of steps leading up to the dais were already buried beneath countless bodies.

The thousand or so dead had been torn to shreds and finally died—or lay there writhing with their limbs severed.

As if hoping someone would put an end to their tenacious lives.

*Slice.*

A streak of light cut through the air.

The man who had split in two the body of a dead man crawling up the steps on a single arm lowered his sword and let out a ragged breath.

*Huff. Huff.*

His entire body, soaked in blood and sweat, heaved.

His golden armor and sword, exquisitely ornate as works of art, felt heavier than ever.

No—perhaps what weighed on him was the responsibility and guilt he had carried all this time.

And yet… he had no regrets.

He couldn’t afford to.

The Embroidered Uniform Guard who had fallen to ash here today had also been prepared to die.

To pity them for a sacrifice they had accepted of their own accord would be an insult greater than death.

Even if the man was the most exalted person beneath the heavens, the one above all others.

“Baek Yeon.”

The man—the Emperor—spoke, his voice rough with a metallic rasp.

Then he addressed the foremost military commander of the imperial court, who had done more than anyone to protect the late Emperor and the imperial family, and who had repeatedly lifted him back to his feet with harsh reprimands whenever he faltered. The Emperor gave him a request, not an order—as he would to a comrade rather than a subject.

“Sound the drum. The war drum.”

“……!”

Baek Yeon’s eyes trembled.

Taking in the Emperor’s exhaustion, his fatigue more visible than ever, he bowed deeply and extended a palm toward the great drum that had announced the start of the banquet.

*Boom!*

The drumbeat, charged with his profound internal energy, rang out without end.

It carried the heart of a warrior who had waited a long time for this day. It carried the Emperor’s will.

Once.

Then again.

The sound was immense enough for everyone in the grand banquet hall to hear. No—it rolled like a wave that would sweep through the entire imperial capital and beyond.

*Booooom!*

Even when the third drumbeat rang out, the three thousand rebels didn’t know what to do. They hesitated.

Everything had unfolded so naturally.

So Gyo’s overwhelming display of martial power had abruptly swept through the vanguard, and the drumbeat resounded with a grandeur they couldn’t explain. For a moment, they had been overwhelmed before they even knew it.

Even the Eastern Heaven Demon Lord—the instigator and center of the rebellion, who should have been leading them from the front—lay in a horrific state at Jin Taekyung and Jeok Cheongang’s feet.

*What is this? What in the world is happening?*

The Eastern Heaven Demon Lord had been captured. Ma Sanbao was nowhere to be seen.

The Imperial Guards and East Depot leadership who had already betrayed the imperial court and the Great Nation to join Dark Heaven were thrown into confusion. They looked at one another, their eyes bewildered.

When they took the Outer Palace, they had thought it was all over.

Even when they had seized every gate leading into the imperial palace and defeated the remaining defenders, taking advantage of another allied force sweeping through the capital, they had been certain a new age was about to begin.

But the reality they’d met with such joy—and the battle that should already have been theirs—had turned out differently.

The flags that had flown so proudly when they first stormed into the grand banquet hall now fluttered as uneasily as their hearts.

And at that very moment—

*Boom. Boom.*

The drumbeat rang out once again, reaching their ears.

Instinctively, every hair on their bodies stood on end. A chill ran down their spines.

The fourth drumbeat was no louder than the ones before it, nor did it have a deeper, more resonant ring.

But there was only one reason it made the rebels’ hearts sink more than ever.

Behind them.

The sound came not from Baek Yeon, visible in the distance, but from somewhere behind them.

And then it spread in every direction.

*Boom. Boom-boom.*

Countless drumbeats spread like flames sweeping across a wide plain. They weren’t echoes bouncing back from somewhere, nor were they hearing things.

They were the signal that this long and gruesome banquet was coming to an end—the footsteps of hunters closing in on prey at last caught in a trap.

*Rumble.*

How long had this been going on?

Where had such a vast army been hiding all this time, and why hadn’t it made a move until now?

*A trap!*

A shock struck them as if lightning had pierced their skulls. At the same time, the rebels felt the colossal tremors rapidly drawing closer.

Then they saw it.

Hundreds of flags rising high around them at last.

Following the fluttering flags, a dragon embroidered in golden thread writhed as though alive.

“……!”

“……!”

Unseen shock, joy, and despair swept across the grand banquet hall.

Some were seized by an elation so intense their hearts felt ready to burst. Others clenched their teeth until they tasted blood.

The three thousand rebels were the latter.

Thousands. Or tens of thousands.

No one could guess the exact number of their enemies, but one thing was certain.

Even now, the force of the enemy closing in around them would overwhelm them.

The rebels felt the killing intent bearing down on them.

Looking at their faces reflected in the rippling pools of blood, they imagined the ominous future about to descend.

But at the same time, they thought of the only way to break through this hopeless situation, surrounded on all sides.

The center and beginning and end of everything.

The ruler at the highest peak in this vast realm beneath the heavens.

“The Emperor…”

The faint voice that slipped from someone’s lips soon erupted into a massive shout, born of the desire to survive.

“Capture the Emperor!”

The victor is king; the loser, a rebel.

With their backs already against the cliff, they had no other choice.

A body without a head could not move.

Capturing the Emperor and his family to make the rebellion succeed was the only way forward.

“Whoever captures the Emperor and his family will become a marquis and enjoy wealth and glory for generations to come!”

At that moment—

*Rumble!*

Thousands of men and horses surged forward like a wave.

Toward the Emperor, who looked down at them from the high steps with his aged face.

And at the same time, trying to drown their fear of the woman standing tall in front of him with angry shouts.

“GRAAAAAH!”

“Charge! Don’t stop!”

Their cries, like screams, and the countless footsteps and thundering hooves woke the deep night. They rang out through the thick darkness hanging over everything like a curtain.

Far away. Farther still.

Loud and clear.

But their desperate advance and shouts seemed unbearably slow and distant.

At least, to the young man and woman facing each other at that moment.

He looked at her. She looked at him.

The more than three hundred yards between them meant nothing now.

They already knew.

They knew they were looking at each other. They knew whose gaze they had met in midair.

But only So Gyo had realized the other person’s true identity.

*So it was you.*

Swallowing a cryptic murmur, So Gyo silently looked down at the battlefield spread out beneath her.

It was vast. And it was horrific.

The grand banquet hall, stretching nearly a thousand yards in both length and breadth, was submerged in blood. Abandoned weapons and severed limbs lay scattered across the ground. The wide-open eyes of the dead held no trace of life.

Only death had filled the silence left behind when the music briefly fell quiet, and now more people were surging in to paint another layer of death over it.

*Whoosh.*

Amid the enemies’ thunderous shouts, a cold wind blew from somewhere, billowing her silky hair into a lush cloud.

The smell of blood, carried by the wind and seeping deep into her nose, was as thick as the crimson pools of blood collected all around her.

Thick enough to dredge up fragments of a past submerged by time.

Thick enough to revive the horrific memories she’d wanted to forget but never could.

Perhaps that was why she felt not even the slightest joy, despite having found the answer and key she had searched for so long.

Perhaps that was why she felt certain the time had come to end this long and gruesome banquet.

*Shhk.*

In the silence, So Gyo moved both hands. The two curved swords, clutched in hands caked with dried blood, pointed toward the sky and the earth. Then they turned to face each other.

*Shrring. Clack.*

The steel, forged through countless rounds of quenching and hammering by some master artisan, gave off a cold ring. An invisible groove and the metal set inside it joined the two weapons together.

As if they had been one from the beginning.

As if they had never been curved swords at all.

*Wooooong.*

After countless years, it had regained its original form. It trembled in its owner’s hands, resonating with the familiar energy seeping deep into it, and shed tears that resembled light.

*Zing.*

The air quivered.

Between the two ends, bent at an angle and shaped to call a curved sword to mind, a pure-white flash connected them.

Just as it had looked in the distant past.

Still bearing the splendor of an age when it had been divine punishment to some, salvation to others.

“Hello again, old friend.”

In a tender voice, So Gyo lifted her beloved weapon.

And, as she had done tens of thousands of times before, she gripped the flash joining its ends and pulled hard.

*Fwoosh.*

A brilliant shaft of light appeared as though traced in midair, set against the shining bowstring.

The unbelievable sight stirred the old memories of someone watching from afar. It raised someone’s figure from a past buried in dust.

A crone who had ruled the battlefield with a bow larger than any other, unleashing Force like lightning.

“The Bow Saint…!”

At that very moment—

*SHWAAAAAK!*

The beam of light left So Gyo’s—or rather, the Bow Saint’s—fingertips and streaked across the grand banquet hall.
```
