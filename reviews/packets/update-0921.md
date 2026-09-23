<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0921.txt",
      "sha256": "942573c220a6257c0f8b5772dbb7b5693f2ceba221e499d0aebb2941a4c2c30f",
      "bytes": 12835
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "9161b7498d84a85dd836f4d47bfb5502f837e50d12b7b47705ba78027956175a",
      "bytes": 1328
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "e4f261a256443b1a8267b983fdbd4ae7aa3530803a007681e483b189b757b921",
      "bytes": 231635
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "e80ce421bab023d56ee5f0b335fbb94bce29ebe1b7344e45bf0497f6707d93c7",
      "bytes": 759
    },
    {
      "path": "characters/Eastern Heaven Demon Lord.md",
      "sha256": "be190360534680a5711c6a5882a735ae10b13b83343fea4ec7301655b997c254",
      "bytes": 807
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "670dc83c399eb7500ea111b07d8b848d4b7bb8bcad6a8cd3f753a2f1905e6ed8",
      "bytes": 1244
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "5f3ee64daf262d6805d3a81972bdc467bd71893881184844d511b367dd58df61",
      "bytes": 1429
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "16c79ae73840b5cce5dc77665a56177c7aafb01ed6e50a26c4a133f139d49feb",
      "bytes": 622
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "e93180fede4dae9ac0e0acefd1ff9a73a672f31e775af13e328e867e1ac17f69",
      "bytes": 752
    },
    {
      "path": "characters/So Gyo.md",
      "sha256": "01d3287fa7a5065f9956f2c3ec6f8e652d518057ee721790fd3c3ee6d2eeaedd",
      "bytes": 754
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "21fe7ebbf3c46e6a6c651cab2cf39578c984d9cc64cf538e5662e8d6ad657b81",
      "bytes": 265353
    }
  ],
  "estimated_tokens": 10651
}
-->

# Durable State Update — Chapter 921

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
1 and safe_through 921. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 921. Profile updates may replace only one
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
  "chapter": 921,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 921,
    "continuity_sources": [921],
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
    "So Gyo is the Bow Saint; her two curved swords can join into the bow’s original form.",
    "So Gyo recognizes Jin Taekyung as the long-sought answer and key she had been searching for; her allegiance remains unknown.",
    "A large imperial force has surrounded the rebels, who are charging the Emperor and his family to capture them.",
    "The Eastern Heaven Demon Lord is captured at Jin Taekyung and Jeok Cheongang’s feet; Ma Sanbao is missing.",
    "The Salcheonmun vowed to pursue Mungyeong, the Slaughter Saint, regardless of cost or delay.",
    "The Salcheonmun may pursue Jin Taekyung if it learns he killed Gye Yabu."
  ],
  "continuity_sources": [
    919,
    920
  ],
  "open_questions": [
    "What enabled Jin Taekyung to return from his seemingly fatal injuries?",
    "What is the outcome of the battle between the surrounded rebels and the imperial forces?",
    "Where is Ma Sanbao, and what is his current status?",
    "What information does the Eastern Heaven Demon Lord hold about Dark Heaven and the Lord of Heaven?",
    "Will the Salcheonmun pursue Mungyeong or discover that Jin Taekyung killed Gye Yabu?"
  ],
  "safe_through": 920,
  "temporary_decisions": [
    "Keep “Force” for 강기 distinct from “death energy” for 사기."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 무신     | **Martial God**               | —              |
| 궁성     | **Bow Saint**                 | —              |
| 암천     | **Dark Heaven**                  |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 노부      | **this old man / I**                                            |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 소교 | **So Gyo** | The palace attendant leading the group assigned to serve Prince Shangshan. |
| 평화 | **Peace Guild** | Guild name. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 사백 | **Senior Martial Uncle** | Zhongnan Sect title used for a senior of the speaker’s Master’s generation. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 지풍 | **Finger Qi** | Invisible qi attack fired by the Western Heaven Demon Lord. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 기장 | strangers | Captain | casual and commanding | Taekyung directly asks the captain for permission to open the aircraft door before cutting it open. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 소교 | 진태경 | palace attendant addressing a martial artist and guest under escort | Young Master Jin | formal and respectful, but firm | Addresses him as 진 공자 while escorting him and warning him not to investigate. |
| 진태경 | 소교 | palace attendant and martial artist under imperial scrutiny | you | formal-polite, controlled and challenging | Taekyung addresses So Gyo as 당신 while questioning her presence and demanding an explanation. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |
| 황제 | 소교 | Emperor questioning a political ally | you | quiet and direct | The Emperor questions So Gyo through Sound Transmission about why she is only watching. |
| 소교 | 황제 | political ally answering the Emperor | Your Majesty | calm and direct | So Gyo answers the Emperor through Sound Transmission without wavering. |
| 적천강 | 동천마군 | enemies | you | blunt and informal | Jeok Cheongang addresses the Eastern Heaven Demon Lord with hostile familiarity. |
| 동천마군 | 적천강 | enemies | you | informal | The Eastern Heaven Demon Lord speaks to Jeok Cheongang during their duel. |
| 황제 | 동천마군 | former ruler addressing a former subject, now an enemy | you | measured and formal | The Emperor asks why the Demon Lord betrayed his father, the late Emperor. |
| 동천마군 | 황제 | former subject addressing the Emperor, now an enemy | you; you bastards | hostile and contemptuous | He denies ever being loyal to the imperial family and accuses the rulers of betrayal. |
| 동천마군 | 소교 | enemies | you; you woman | hostile and demanding | He demands that So Gyo reveal her identity. |
| 소교 | 동천마군 | enemies | you | casual, taunting, and threatening | She warns him to stop and taunts him about whether suicide would still kill him. |
| 진태경 | 동천마군 | young martial artist confronting an enemy | ugly-ass big bro | casual, profane, and taunting | Jin calls out to the Demon Lord after returning to the hall. |
| 동천마군 | 진태경 | enemy recognizing the spear wielder | Jin Taekyung | shouted, informal | The Demon Lord cries Taekyung's name after identifying him as the spear's owner. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 920
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Eastern Heaven Demon Lord.md

# Eastern Heaven Demon Lord (동천마군)

- **Safe through:** Chapter 920
- **Aliases:** None
- **Role:** The Eastern Heaven Demon Lord is a former Maoshan Sect disciple who commands the dead with a bell and has spent half a century infiltrating the imperial court while building a far-reaching rebellion.
- **Personality:** His hatred of rulers is rooted in the loss of his family to the violence of the age of chaos and the destruction of the Maoshan Sect, where he had found happiness.
- **Voice:** He speaks in measured, almost lyrical phrasing, recounting the past before turning to pointed accusations.
- **Relationships:** Ma Sanbao is his Disciple; he holds the Emperor responsible for Taizu’s actions against the Maoshan Sect.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 920
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts Jin Taekyung, his publicly acknowledged second Disciple and intended heir; warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, remains Peng Cheolhu's rival, and is the target of an attack by the assassin Heaven's Slaughter.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 920
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Ma Sanbao, whom Taekyung killed, has been raised among the Eastern Heaven Demon Lord’s undead, while Jeong Hogun and the Embroidered Uniform Guard have declared themselves allies of the Emperor, and So Gyo’s allegiance remains unknown.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 920
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 917
- **Aliases:** None
- **Role:** An unidentified legendary martial artist regarded as a pinnacle above the Ten Kings; more than fifty years ago, he defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, appearing first as a white-bearded elder and later as a young boy; Mae Jonghak received several teachings from him, while his identity, whereabouts, and possible connection to Cheon Taemin remain unknown.

### So Gyo.md

# So Gyo (소교)

- **Safe through:** Chapter 920
- **Aliases:** None
- **Role:** So Gyo is the Bow Saint, a Supreme Peak master and palace attendant assigned to Prince Shangshan, whose two curved swords can join into their original bow form.
- **Personality:** Calm, calculating, and self-possessed; she conceals her strength and identity and can be openly taunting.
- **Voice:** Measured and composed, shifting from deferential formality to casual, pointed taunts and threats.
- **Relationships:** So Gyo recognizes Jin Taekyung as the long-sought answer and key; she says only she and the Emperor know a secret she withheld from Baek Yeon, while her true allegiance remains unknown.

## Korean source

```text
＃921화



슈확!

공간을 가로질러 쇄도하는 빛줄기를 마주한 순간, 한 덩어리가 되어 돌격하던 삼천의 반란군들은 본능적으로 깨달았다.

그들이 유일한 활로(活路)라고 생각했던 그곳에, 피할 수 없는 죽음이 기다리고 있었다는 것을.

“피하……!”

콰아아아앙!

비명과도 같은 누군가의 외침이 굉음에 파묻힌다. 목이 사라진 시체가, 사지가 뜯겨 나간 인마(人馬)가 폭발과 함께 솟아오른 먼지구름 사이에서 피 분수를 뿜어냈다.

“크아아악!”

“사, 산개(散開)! 즉시 산개하여 돌격하라!”

“멈추지 마라! 멈추면 죽음뿐이다!”

무수한 비명들 사이로 들려오는 다급한 명령.

극심한 혼란과 두려움에 사로잡혀 있던 반란군들은, 아직 건재한 수뇌부의 지휘에 덜덜 떨리는 두 다리에 억지로 힘을 불어넣었다.

맞다.

이곳에서 멈추면 모든 것이 끝장이다.

미쳐 날뛰는 호랑이의 등에 올라탄 이상, 그들의 운명은 이미 정해져 있었다.

“으아아아아!”

“돌격! 돌겨어어억!”

핏발 선 눈동자와 백지장처럼 새하얗게 물든 얼굴로, 살아남은 반란군은 발악하듯 함성을 내지르며 나아갔다.

지금 이 순간에도 어디선가 날아들 것 같은 강기(罡氣)의 화살이 자신만은 피해 가길 간절히 바라며.

운 나쁘게 선두에 선 이들의 몸뚱어리를 방패막이 삼아.

‘제발, 제발!’

그리고 악문 잇새 사이로 끊임없이 맴도는 간절한 부탁과 함께 재차 돌격을 이어 가는 그들의 앞을, 어느샌가 들이닥친 휘황한 빛줄기가 가로막았다.

아니, 휩쓸었다.

콰앙! 콰드드득!

지축이 뒤흔들린다. 솟아오른 먼지구름이 핏물을 머금어 붉게 물들었다.

그러나 그 참혹한 광경을 응시하는 누군가의 시선은, 계속해서 활시위를 당기는 그 손길은 무서우리만치 침착했다.

‘사백 보.’

지이이잉.

거대한 활이 부르르 몸을 떨었다. 주인의 공력을 머금어 찬란하게 빛나는 시위와 화살은 그 어떤 궁사(弓師)도 흉내 내지 못할 속도와 위력을 발산했다.

바로 지금처럼.

퉁, 슈확!

다시 한번 휘몰아치는 광풍(光風)과 함께, 이미 예정된 죽음과 비명이 적들을 덮쳤다. 강기로 이루어진 화살이 한 번 쏘아질 때마다 수십의 목숨이 바람 앞의 촛불처럼 사그라졌다.

‘삼백 보.’

다시.

‘이백 보.’

또 다시.

콰과과과광!

가까워질수록 시체가 쌓였다. 이미 몇 차례에 걸쳐 뒤바뀐 선두의 반란군들은 이제 광인처럼 울부짖으며 달려오고 있었다.

그들에게 주어진 유일한 활로인 동시에, 사지(死地)를 향해.

이 커다란 장기판의 말이 되어 끊임없이 나아가고, 그렇게 생애 마지막이 될 휘황한 빛과 마주했다.

콰드드득!

사백 보의 거리가 절반으로 좁혀지기까지 몇이나 죽은 것일까.

또 남은 이백 보의 거리를 지우기 위해서 몇이나 더 죽어야 하는 것일까.

불현듯 머릿속에 떠오른 의문에 대한 답은 그 누구도 해 줄 수 없었다.

빠져나가는 생명을 느끼며 쓰러지는 이들도, 그런 동료를 뒤로하고 계속해서 나아가야 하는 이들도.

그리고 수하들을 앞세운 채, 쉼 없이 돌격을 부르짖는 수뇌부들도.

“얼마 남지 않았다! 황제를 사로잡는 자, 열후에 봉……!”

퍼엉!

강렬한 파공성과 동시에 뚝 끊인 외침.

찰나의 순간, 안장 위에서 쏘아지듯 튕겨 나간 지휘관의 몸뚱어리가 피 웅덩이에 처박혔다.

철퍽.

“으헉!”

“표, 표기장군(驃騎將軍)께서……!”

뒷말은 들려오지 않았으나, 핏물에 잠긴 채 미동조차 없는 표기장군을 보며 죽음을 떠올리지 않는 이들은 없었다.

볼 것도 없는 절명(絶命).

적지 않은 세월 동안 강력한 병권을 쥐고 있던 군부의 실력자는 그렇게 죽었다.

너무나도 갑작스럽고 비참하게, 동시에 하나의 의문을 남긴 채.

‘어떻게?’

주위에 있던 수뇌부들은 순간 당혹스러움을 느꼈다.

도무지 화살이라고는 믿을 수 없는, 무시무시한 위력을 지닌 빛줄기는 조금 전 어디에서도 찾아볼 수 없었으니까.

‘그렇다면 누가…….’

그리고 보이지 않는 적을 찾기 위해 고개를 돌린 그때, 누군가의 나직한 목소리가 그들의 귓가를 파고들었다.

“노부가 궁금한 것이 하나 있는데, 이런 염병할 판을 벌인 놈들을 뭐라 불러야 하느냐?”

또 다른 누군가가 대답했다.

“뭐라 부르긴요. 완전히 개새끼죠.”

“그럼 이 상황에서도 뒤로 빠져 있는 놈들은?”

“음. 씹새끼?”

“두 가지 경우에 모두 해당한다면?”

“사자성어로 개씹새끼라고 합니다.”

“개씹새끼, 개씹새끼들이라. 그거 아주 혀끝에 착 감기는구나.”

앞도, 뒤도, 양옆도 아니다.

석상처럼 굳어 버린 수뇌부들은 천천히 고개를 들었다.

그리고 자신들의 머리 위, 허공을 밟으며 우뚝 서 있는 두 사람을 볼 수 있었다.

동시에 불길한 직감을 떠올렸다.

어쩌면 지금 눈 앞에 펼쳐진 이 광경이, 저들의 목소리가 생애 마지막으로 보고 듣는 것이 되리라는 사실을.

“자, 잠깐. 지금이라도 우리를 돕는다면 당신들이 원하는…….”

쉭.

바람이 불었고, 그뿐이었다.

분명 그뿐이어야 했다.

그런데 왜, 어째서 정신이 흐릿해지는 걸까.

분명 자신들의 머리 위에 서 있던 것은 두 명이었는데, 그중 하나는 어디로 사라진 것일까.

“이런 개…… 같은.”

누군가의 입술 사이로 쥐어 짜낸 음성이 흘러나온 그 순간.

서걱.

몸속 깊숙한 곳에서, 뒤늦게 깨어난 죽음이 기지개를 켰다.

이미 보이지도 않은 속도로 스쳐 지나간 창날의 흔적을, 희미한 붉은 실선으로 드러냈다.

스륵, 푸화아아악!

몽글몽글하게 맺힌 핏물이 폭발하듯 터져 나온다. 주인의 의지를 배반한 목이, 팔과 다리가, 뼈와 살이 분리되고 미끄러진다.

허물어지는 시신들을 등 뒤, 피 한 방울 묻지 않은 창을 든 청년의 머리 위로 쏟아졌다.

투두두둑!

어두컴컴한 하늘 속 쏟아져 내리는 붉은 비를 맞고 있던 청년, 아니 진태경은 한참 늦은 대답을 건넸다.

“돕긴 뭘 도와. 너희 같은 놈들은 그냥 뒈지는 게 돕는 거야. 이 개씹새끼들아.”

“……!”

“……!”

이 참혹하면서도 믿을 수 없는 광경을 눈앞에서 지켜본 이들은 경악을 금치 못하는 동시에 모든 것이 끝났음을 깨닫고 절망했다.

하나같이 화려한 복장을 한 그들은 이미 대(代)를 이을 만큼 암천과 동천마군에게 충성을 맹세한 거물들이었고, 두 번 다시 돌아올 수 없는 강을 건넌 이들이었으니까.

‘끝났다. 완전히.’

수백의 호위에 둘러싸여 있음에도 담담한 얼굴로 창날을 늘어트린 진태경과 여전히 허공에 우뚝 선 적천강을 보며, 그들은 비로소 불길한 직감이 현실이 되었음을 깨달았다.

이 거대한 역모도, 자신들이 오랜 세월 누려 왔던 부귀영화도 이제 끝장이다.

그나마 유일한 위안이 있다면, 모진 고문으로 끔찍하게 고통받다가 거열형(車裂刑)에 사지가 찢겨 나가는 대신 저 강호의 무뢰배에게 빠른 죽음을 선사받을 수 있다는 것 정도였다.

아니, 그러리라 생각했다.

바로 그 순간, 적천강의 한 마디가 들려오기 전까지는.

“가장 윗대가리로 보이는 놈들은 살려 둬라. 금광(金光)인지 폐광(廢鑛)인지는 모르겠지만, 캐면 뭐가 나올지 모르니 곡괭이질 정도는 해 봐야지.”

“……!”

“……!”

눈동자에 깃든 경악과 체념이 공포로 물들기까지 걸린 시간은 찰나에 불과했고, 그 짧은 순간의 끝에는 진태경으로부터 비롯된 열 줄기의 파공성이 그들을 기다리고 있었다.

쉬쉬쉬쉭!

만에 하나를 대비하여 품에 간직하고 있던 독단(毒團)을 꺼낼 시간도, 허리춤의 단도로 목을 그을 여유도 주어지지 않았다.

투두둑!

느껴진다.

순식간에 공간을 가로지른 지풍(指風)에 뻣뻣해지는 전신이. 정신과 몸을 짓누르는 깊은 절망 속에서 천천히 기울어지는 세상이.

스륵, 쿵!

물 먹은 통나무처럼 쓰러지는 그들의 두 눈동자에, 어느새 사방에서 휘날리는 황금빛 깃발이 틀어박혔다.

마치 살아 있는 것처럼 꿈틀거리는 용의 위로, 어두운 하늘을 덧칠하며 쏟아지는 무수한 화살촉도 함께.

솨아아아아아.

일천의 연노병(連弩兵)이 퍼붓는 강철의 소나기가, 남아 있던 반란군들의 머리 위를 뒤덮었다.

푸푸푸푸푹!

피로 물들었던 연회의 끝을 알리는 파육음이, 고통에 찬 비명이 쉬지 않고 울려 퍼지는 힘찬 북소리와 뒤섞였다.

핏물처럼 진하고, 끈적하게.

둥. 둥. 두웅.



* * *



일각(一刻).

그것이 물경 삼천에 달하던 반란군이 모두 궤멸하기까지 걸린 시간이었다.

무수한 화살비와 함께 대연회장에 진입한 황실 군대의 기세는 이 길고도 참혹했던 연회의 마침표를 찍기에 충분했다.

“역도들은 들어라!”

“역도들은 들어라!”

“지금 즉시 무장을 해제하고 투항하라!”

“지금 즉시 무장을 해제하고 투항하라!”

강력한 공력을 머금은 외침이 연달아 울려 퍼진다.

마치 한 사람이 외치는 것처럼 똑 닮은 목소리와 어조로 투항을 권유하는 쌍둥이 무장의 모습에, 살아남은 반란군들은 마지막 희망마저 잃어버린 듯했다.

툭, 투둑.

철컹.

피로 얼룩진 갑옷의 이음새를 풀고, 금이 가고 부러진 병장기를 내던지듯 내려놓는다.

누가 먼저 시작했는지 모를 투항의 물결은 이내 파도가 되어 대연회장을 휩쓸었다.

“항복, 항복하겠소.”

“제발 목숨만은…….”

혼이 빠져나간 듯한 눈과 표정.

사라진 한쪽 팔을 부여잡고 목숨을 애걸하는 자도, 더 이상 뒷걸음질 칠 수 없는 낭떠러지 끝에서 돌이킬 수 없는 선택을 하는 자도 있었다.

푹.

“커……헉!”

억눌린 단말마와 함께 앞으로 기울어지는 몸뚱어리.

이내 힘없이 허물어지는 이름 모를 반란군의 얼굴에는 모든 것이 끝났다는 절망과, 이 지옥에서 탈출하며 얻은 일말의 평화가 깃들어 있었다.

“끝이로군.”

혼잣말 같은 적천강의 희미한 목소리에, 나는 애써 담담하게 고개를 끄덕였다.

그래, 끝났다.

보이는 곳에서, 혹은 보이지 않는 곳에서 수많은 목숨을 집어삼킨 이 거대한 전투가 드디어 막을 내렸다.

그러나 아직 모든 것이 끝난 것은 아니었다.

죽은 자들은 돌아올 수 없는 먼 곳으로 떠났으나, 죽지도 살지도 않는 괴물은 여전히 이곳에 남아 있었으니까.

더불어 살아 있는 자들에 대한 정리 역시 남아 있었으니까.

철벅.

누군가의 발걸음이 피 웅덩이를 밟는다.

가볍고 사뿐한 걸음과는 어울리지 않는 끈적한 핏물을 보보(步步)마다 아로새기며 다가오는 그녀를, 나는 차갑게 가라앉은 눈빛으로 응시했다.

소교(小嬌).

아니, 궁성(弓星).

모든 것이 베일에 싸여 있던 여자.

첫 만남에는 황제의 충복을 연기했고, 두 번째 만남에는 암천의 가면을 뒤집어썼으며, 세 번째 만남에서야 비로소 자신을 드러낸 여자.

그녀가 나를 향해 다가오고 있었다.

소교라는 이름에 어울리는 고양이 같은 발걸음으로, 조금 일찍 자신의 정체를 밝혔더라면 죽지 않았어도 되었을, 지면에 널브러진 무수한 시신을 가로지르며.

스아아아.

칼날과도 같은 기운이 전신에서 솟아오른다. 몇 걸음 앞에서 멈춰선 궁성이 말없이 나를 바라보다, 불현듯 입을 열었다.

“그래, 너였구나.”

무슨 말일까.

그 말에 담긴 의미를 파악하지 못한 내가 머뭇거리던 그때, 나직한 목소리가 귓가를 울렸다.

- 무신(武神)이 말했던, 선택받은 자가.

……뭐?
```

## Final English reading copy

```markdown
# Chapter 921

*Fwoosh!*

The moment they saw the streak of light hurtling across the open space, the three thousand rebels charging as one instinctively understood.

The only path they had thought could save them was where unavoidable death awaited.

“Dodge—!”

*KABOOOM!*

Someone’s scream was swallowed by the deafening roar. Amid the dust cloud that billowed up with the explosion, headless corpses and men and horses torn limb from limb shot into the air, spraying fountains of blood.

“GRAAAH!”

“S-spread out! Spread out at once and keep charging!”

“Don’t stop! Stop, and you’re dead!”

Urgent commands rang out over countless screams.

Overcome by fear and confusion, the rebels forced strength into their trembling legs at the direction of the command still coming from their surviving leaders.

That was right.

If they stopped here, it was all over.

The moment they climbed onto the back of a rampaging tiger, their fate had been sealed.

“AAAAAAH!”

“Charge! Chaaaarge!”

With bloodshot eyes and faces gone white as paper, the surviving rebels screamed in desperation and pressed forward.

Praying that the Force arrows that seemed liable to come flying from anywhere, at any moment, would spare them.

Using the unlucky men at the front as shields.

*Please, please!*

And as they continued their charge, an earnest plea circling endlessly between clenched teeth, a dazzling streak of light suddenly swept across their path.

No—it swept them away.

*BOOM! CRUNCH!*

The earth shook. The cloud of dust rising into the air turned red as it soaked up blood.

Yet the gaze of the person watching that horrific scene—and the hand that kept drawing the bowstring—remained terrifyingly calm.

*Four hundred paces.*

*Ziiing.*

The great bow shuddered. The string and arrow, glowing brilliantly with their owner’s internal energy, unleashed a speed and force no other archer could imitate.

Just as they did now.

*Thrum. Fwoosh!*

With another howling gale of light, the death already in store—and the screams that came with it—swept over the enemy. Every time an arrow made of Force flew, dozens of lives went out like candles in the wind.

*Three hundred paces.*

Again.

*Two hundred paces.*

Again.

*KABOOM! KABOOM!*

The closer they came, the higher the pile of corpses grew. The rebels at the front had changed several times over by now, and the men charging forward were howling like madmen.

The only path left to them—and the road to their graves.

They pressed on, pawns on a vast game board, until they faced the brilliant light that would be the last thing they ever saw.

*Crunch!*

How many had died by the time the four hundred paces between them had been cut in half?

And how many more would die before they covered the remaining two hundred?

No one could answer the question that suddenly crossed their minds.

Not those collapsing as they felt the life draining out of them. Not those who had to leave their fallen comrades behind and keep going.

Not even the leaders, who kept shouting for the charge while sending their own men ahead of them.

“We’re almost there! Whoever captures the Emperor will be made a marquis and—!”

*Poom!*

The cry cut off at the same time as a sharp crack through the air.

In the blink of an eye, the commander’s body shot off his saddle and slammed into a pool of blood.

*Splash.*

“Ugh!”

“G-General of the Swift Cavalry!”

No one heard the rest of what he said, but looking at the General of the Swift Cavalry lying motionless in the blood, no one could help thinking of death.

There was no question. He was dead.

The powerful military commander, who had held control over the army for many years, died just like that.

So suddenly and miserably, leaving behind one question.

*How?*

The leaders nearby were momentarily bewildered.

That terrifying streak of light, too powerful to seem like an arrow, had been nowhere to be seen a moment ago.

*Then who…?*

Just as they turned their heads to look for the unseen enemy, a low voice slipped into their ears.

“There’s something this old man’s curious about. What do you call the bastards who started this goddamn mess?”

Someone else answered.

“What else? They’re fucking assholes.”

“Then what about the ones hanging back even now?”

“Hmm. Shitheads?”

“And if they’re both?”

“In four-character idiom? Fucking dog-shitheads.”

“Fucking dog-shitheads, is it? That does roll right off the tongue.”

Not in front. Not behind. Not to either side.

The leaders, frozen like statues, slowly raised their heads.

And there they were—two people standing tall in midair above them.

At the same time, an ominous feeling came over them.

Maybe what they were seeing and hearing now would be the last thing in their lives.

“W-wait. If you help us now, we can give you whatever you want…”

*Whoosh.*

A breeze blew. That was all.

It should have been all.

Then why was their consciousness growing hazy?

There had been two people standing over them. Where had one of them gone?

“Y-you fucking…”

A voice squeezed out between someone’s lips.

*Shhk.*

Deep inside their bodies, death awoke late and stretched.

The faint red lines left by a spearhead that had flashed past too fast to see appeared across them.

*Slip. Fwoooosh!*

Blood, welling in soft beads, burst out like an explosion. Heads, arms, legs, bone, and flesh—defying their owners’ will—came apart and slid away.

The young man with the spear, not a drop of blood on it, stood beneath the falling bodies as they collapsed behind him.

*Thud-thud-thud!*

The young man, drenched by the red rain pouring from the dark sky, was Jin Taekyung.

He finally gave them his answer.

“Help you? The best help you bastards can offer is to just fucking die. You fucking dog-shitheads.”

“……!”

“……!”

Those who had witnessed the horrific, unbelievable sight before their eyes were struck with shock—and despair, as they realized it was all over.

Every one of them wore splendid clothes. They were powerful figures whose families had pledged loyalty to Dark Heaven and the Eastern Heaven Demon Lord for generations. They had crossed a river they could never return from.

*It’s over. Completely.*

Surrounded by hundreds of guards, Jin Taekyung stood with a calm expression, his spearhead hanging low. Jeok Cheongang still stood tall in the air.

Only then did they understand that their ominous premonition had come true.

This grand rebellion—and the wealth and glory they had enjoyed for so many years—was finished.

Their only consolation was that instead of suffering through brutal torture before being torn limb from limb by carts, they might be granted a quick death by that martial-world ruffian.

Or so they thought.

Until Jeok Cheongang spoke.

“Leave the ones who look like the top dogs alive. I don’t know if they’re a gold mine or a spent mine, but who knows what we’ll find if we dig? We should at least try a few swings of the pickaxe.”

“……!”

“……!”

It took no more than an instant for the shock and resignation in their eyes to turn into fear. At the end of that brief moment, ten sharp cracks through the air were waiting for them, unleashed by Jin Taekyung.

*Fwish-fwish-fwish!*

They weren’t given time to take out the poison pills they had kept hidden, just in case—or even a moment to draw the daggers at their waists and slash their own throats.

*Thud-thud-thud!*

They felt it.

Finger Qi racing through the air in an instant, stiffening their entire bodies. The world slowly tilting as deep despair weighed down on their minds and bodies.

*Slip. Thump!*

They fell like waterlogged logs. In their eyes, golden flags were already fluttering all around them.

Above the writhing dragons, countless arrowheads rained down, painting over the dark sky.

*Shhhhhhh.*

A steel rain poured from a thousand repeating-crossbow soldiers, covering the remaining rebels.

*Thud-thud-thud!*

The sounds of flesh being pierced announced the end of the blood-soaked banquet. Screams of pain joined them, mingling with the powerful, unceasing beat of drums.

Rich and sticky as blood.

*Boom. Boom. Booooom.*



* * *



Fifteen minutes.

That was how long it took for all three thousand rebels to be wiped out.

Along with a rain of arrows, the Imperial Army swept into the grand banquet hall with enough force to put an end to this long, horrific feast.

“Rebels, listen!”

“Rebels, listen!”

“Disarm and surrender at once!”

“Disarm and surrender at once!”

A powerful voice charged with internal energy rang out over and over.

The twin military officers, urging them to surrender with identical voices and intonations, as though one person were speaking, seemed to extinguish the surviving rebels’ last hope.

*Clunk. Clunk.*

*Clang.*

They loosened the joints of their bloodstained armor and dropped their cracked and broken weapons as if throwing them away.

No one knew who had begun the wave of surrender, but it soon swelled into a tide that swept through the grand banquet hall.

“I surrender. I’ll surrender.”

“Please, just spare my life…”

Eyes and faces that looked as if their souls had left them.

Some clutched their missing arm and begged for their lives. Others made an irreversible choice at the edge of a cliff, unable to take another step back.

*Stab.*

“Kh… Urgh!”

A body pitched forward with a muffled death rattle.

The nameless rebel crumpled without strength. Despair that everything was over mingled in his face with the faint peace he had found in escaping this hell.

“It’s over.”

At the faint words Jeok Cheongang murmured as if to himself, I forced myself to nod calmly.

Yeah. It was over.

This great battle, which had swallowed countless lives in plain sight and out of it, had finally come to an end.

But not everything was over.

The dead had gone somewhere far away, never to return. But the monster who was neither dead nor alive still remained here.

And there was still the matter of dealing with the living.

*Squish.*

Someone’s footsteps sank into a pool of blood.

Each light, graceful step left a sticky imprint in the blood—an unpleasant contrast to her delicate gait. I watched her approach, my gaze cold and steady.

So Gyo.

No—the Bow Saint.

The woman whose every detail had been shrouded in mystery.

At our first meeting, she had pretended to be the Emperor’s loyal servant. At our second, she had put on the mask of Dark Heaven. Only at our third meeting had she finally revealed herself.

She was coming toward me.

With the catlike steps that suited her name, So Gyo, she crossed the ground scattered with countless corpses—people who wouldn’t have had to die if she had revealed her identity a little sooner.

*Fwoooosh.*

Blade-sharp qi rose from every part of my body. The Bow Saint stopped a few steps away and looked at me in silence, then suddenly spoke.

“So it was you.”

What did she mean?

I hesitated, unable to understand the meaning behind her words. A low voice sounded in my ear.

*—The one the Martial God spoke of. The chosen one.*

…What?
```
