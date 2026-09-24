<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0941.txt",
      "sha256": "fccdad721d6ab7b870ea942164da0b8318401ecbb67554043d7a3e44ac2989d8",
      "bytes": 13274
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "f341ad2838f2f29a2512fe9eabed965af555b4e6f58c064c126bb8b16a132f64",
      "bytes": 2742
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b7362053c664e6f24cbb4f8d83aadc2742edb1834ab199c54febc7d524200e9b",
      "bytes": 232730
    },
    {
      "path": "characters/Baek Yeon.md",
      "sha256": "2091f2e4efb69e9693b64076abea1f572f067b2ef05fe71a447854844a0ab341",
      "bytes": 950
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "a25d7e32e31d4697c3d57e4a20701a066fddc45cc54d3299c786ab2049b3fc63",
      "bytes": 759
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "5094be032c2be4ddfda069d0770f75534582b1d77d77613d46e0bb436ee0b9d7",
      "bytes": 853
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "51dd0086f90d0e28086f008678c0ac99d63bc6450b2b16dcc9cb6a7825c0c1c6",
      "bytes": 699
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "c1dcb2fc0fcdfd998cf01a9ee1e97718ac4b7f1419718318dbcec4f80c9cc627",
      "bytes": 1343
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "eb80ee537d8239f0ea50a59421b860f7ed45e38a1b5e9b1df22c4b955a77ed5b",
      "bytes": 622
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "5df2e68d4f6a8ffa831b089645fc57ab98c320ab9d696f779a98ac6d2d3da416",
      "bytes": 699
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "4ee3b6543b8632569121cbfe4a568ad965221b0b9c1b73ab8cd6468d20573f97",
      "bytes": 1042
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "0e2d532f2af4d7be69c6e65c1cef25321d7cf2235ebf140c6de94d6147d63060",
      "bytes": 266948
    }
  ],
  "estimated_tokens": 11914
}
-->

# Durable State Update — Chapter 941

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
1 and safe_through 941. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 941. Profile updates may replace only one
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
  "chapter": 941,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 941,
    "continuity_sources": [941],
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
    "The Emperor was poisoned with Blood Soul Gu after the coup; it has reached his marrow, and the Divine Physician says his vitality is at its limit and cannot guarantee he will survive another couple of months.",
    "Taekyung’s System quest requires him to remove the Blood Soul Gu from the Emperor’s head and successfully treat him; its reward and failure consequence are unknown.",
    "The Emperor prepared for his death by transferring loyal retainers and his power base to Zhu Bao, and avoids meeting his younger brother to spare him the grief of an impending farewell.",
    "The Emperor has publicly exposed Dark Heaven and declared his intent to crush it; war against Dark Heaven has begun.",
    "The Emperor has ordered Baek Yeon to announce that he will personally lead the campaign against Dark Heaven, despite his failing health.",
    "The imperial court is mobilizing troops and warships after Taekyung warned that Dark Heaven’s main force may invade Shanxi Province before the Double Ninth Festival.",
    "Ma Sanbao escaped and evaded the Imperial Army’s three-day search.",
    "Taekyung found and opened the Eastern Heaven Demon Lord’s hidden iron chest; it contains old bamboo slips, recent papers, and a small silk pouch of unknown significance.",
    "The System update reward is a durable pocket watch that appears broken and bears the faint inscription “A broken clock is right twice a day.”",
    "The Bow Saint says the Martial God chose her; she tested Taekyung in the banquet-hall battle to confirm he was the chosen one and assess his power and character.",
    "The Bow Saint remembers the dead and counts casualties after every battle; she says 1,319 orthodox fighters died at Mount Small Hua and 2,562 allies died in the banquet hall.",
    "Jeok Cheongang considers Taekyung his one and only Disciple and is furious that the Bow Saint put him in danger."
  ],
  "continuity_sources": [
    939,
    940
  ],
  "open_questions": [
    "What is the Martial God’s identity, and what is the full nature of his connection to the chosen one and the Bow Saint?",
    "How far has Dark Heaven infiltrated the Great Nation, and which officials or commanders are involved?",
    "Where is Ma Sanbao, and what is his current status?",
    "Who sent the Shanxi Annihilation Plan missive, and will Dark Heaven’s invasion proceed as described?",
    "What do the papers, bamboo slips, and silk pouch from the Eastern Heaven Demon Lord’s chest contain, and what is their significance?"
  ],
  "safe_through": 940,
  "temporary_decisions": [
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 암천     | **Dark Heaven**                  |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 은인     | **Benefactor**                               |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 백연 | **Baek Yeon** | Commander of the Embroidered Uniform Guard. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 정양 | **Jeongyang** | Shanxi location |
| 혼주 | **Honju** | Shanxi location |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 양천 | **Yangcheon** | Shanxi-area location near which a small martial arts academy operates. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 북문 | **North Gate** | The gate where Jin Taekyung and Yohi arrive. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 홍진 | 주표 | servant and political aide to prince | His Highness | formal-deferential | Uses the elongated royal call 전하 while summoning Zhu Bao. |
| 진태경 | 주표 | visitor to prince | His Highness, Prince Shangshan | formal-deferential | Addresses Zhu Bao as 상산왕 전하 after kneeling to meet his gaze. |
| 주표 | 진태경 | prince to visiting young hero | Jin Taekyung | formal and inquisitive | Uses the formal second-person address before asking Taekyung's name and requesting an autograph. |
| 홍진 | 진태경 | political_host_to_young_martial_artist | Young Hero Jin; Young Master Jin; Sleeping Dragon of Shanxi | polite, coaxing, and probing | Uses respectful forms while steering Taekyung toward relaying the Escort Bureau proposal and teasing him with the Seongun Escort Bureau. |
| 진태경 | 홍진 | young_martial_artist_to_political_official | Comrade Chairman—no, Deputy Military Commissioner | casual and teasing, then formally corrective | Deliberately jokes with an inappropriate title before correcting himself to Hong Jin's official office. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 정호 | 진태경 | Shaolin Discipline Hall Master to patient and Benefactor | Benefactor Jin | formal-polite | Jung Ho repeatedly uses 진 시주 and 시주. |
| 진태경 | 정호 | patient to Shaolin Discipline Hall Master | Monk | polite and familiar | Taekyung addresses Jung Ho as 스님. |
| 주표 | 홍진 | prince to loyal subject | you | formal and reassuring | Zhu Bao refers to Hong Jin as 그대 while apologizing for the hardship he has endured. |
| 진태경 | 정호군 | young martial artist to senior imperial officer | Commander Jeong | casual and teasing, then conciliatory | Jin addresses him by rank while trying to defuse the standoff. |
| 주표 | 백연 | prince addressing an imperial military officer | Commander Baek Yeon | formal and authoritative | Addresses Baek Yeon by name and office while insisting that he answer. |
| 백연 | 주표 | imperial officer addressing a prince | Your Highness | formal and deferential | Uses 전하 when apologizing to and answering Prince Shangshan. |
| 백연 | 정호군 | commander to subordinate | you | direct and commanding | Uses 네 while testing Jeong Hogun’s obedience. |
| 홍진 | 백연 | imperial aide confronting a senior military officer | you | angry and confrontational | Uses 당신 in an indignant outburst. |
| 진태경 | 백연 | young martial artist confronting an imperial military commander | you | casual and insulting | Refers to Baek as 이 양반 while challenging his conduct. |
| 백연 | 천자 | imperial officer addressing the Emperor | Your Majesty | formal, deferential in address but openly defiant in private counsel | Baek uses formal honorifics while sharply confronting the Emperor over their shared undertaking. |
| 천자 | 백연 | Emperor addressing his military commander | Baek Yeon | familiar and authoritative | The Emperor addresses Baek by name and gives him a direct warning. |
| 진태경 | 상산왕 | protector addressing a young prince | His Highness | respectful royal address | Taekyung refers to the prince as 상산왕 전하 when ordering Mujin to bring him. |
| 정호군 | 상산왕 | imperial guard officer escorting the prince | His Highness | formal and deferential | Hogun formally reports that he has come to escort the prince. |
| 정호군 | 홍진 | Embroided Uniform Guard officer addressing a senior imperial official | Deputy Military Commissioner | formal and admonishing | Hogun tells Hong Jin to mind his words. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 상산왕 | 황제 | younger brother addressing the Emperor | Your Majesty | deferential royal address | Shangshan addresses the Emperor as 폐하 while pleading for Taekyung. |
| 홍진 | 정호군 | Embroided Uniform Guard officers of equal rank | Thousand Captain Jeong | polite and direct | Hong Jin addresses Jeong Hogun by rank and surname. |
| 백연 | 진태경 | imperial commander confronting a young martial artist | Jin Taekyung | measured and familiar, using 자네 | Baek Yeon cautions Taekyung about his words and asks whether he must cause a scene. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |
| 황제 | 백연 | Emperor to the imperial court’s foremost military commander and trusted comrade | Baek Yeon | Direct and familiar; framed as a request rather than an order | The Emperor asks Baek Yeon to sound the war drum. |
| 황제 | 주표 | older brother addressing his younger brother and newly appointed Crown Prince | Bao’er | intimate and authoritative | The Emperor uses a warm childhood-style name before commanding Zhu Bao to accept the succession. |
| 주표 | 황제 | younger brother and Crown Prince addressing the Emperor | Your Majesty | formal and deferential | Zhu Bao formally accepts the Emperor’s command. |

## Listed compact profiles

### Baek Yeon.md

# Baek Yeon (백연)

- **Safe through:** Chapter 940
- **Aliases:** Blood Envoy
- **Role:** Baek Yeon is the Commander of the Embroidered Uniform Guard, a martial arts instructor to the Emperor, and the Blood Envoy who helped the fourth prince seize the throne and led the purge.
- **Personality:** Politically assured and controlled, Baek Yeon prioritizes the Great Nation and its people over Murim’s interests, and is willing to dismantle Murim if it becomes a threat to them.
- **Voice:** Baek Yeon speaks with measured formality in public, but with the Emperor he shifts easily into familiar teasing and earnest, eloquent praise.
- **Relationships:** Baek Yeon is the Emperor’s trusted confidant and former martial arts instructor, and he is entrusted with protecting Zhu Bao; he commands the Embroidered Uniform Guard and treats Taekyung as a dangerous potential obstacle.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 940
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 939
- **Aliases:** None
- **Role:** Hong Jin is Eunuch Hong, a former Deputy Military Commissioner of Shanxi Province and East Depot member who is now responsible for the East Depot and remains a trusted aide to Prince Shangshan.
- **Personality:** Composed, socially deft, and ambitious, Hong Jin became a eunuch to escape poverty and save his family, then used his abilities to pursue a broader life.
- **Voice:** Delicate and deferential with Prince Shangshan, but warm, familiar, and playfully forthright with trusted allies.
- **Relationships:** Hong Jin is devoted to Prince Shangshan and is trusted by the Emperor to take responsibility for the East Depot; he is a longtime friend of Ma Sanbao and a trusted ally of Jin Taekyung.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 933
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he follows imperial orders without hesitation and reads the political consequences of events with care.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Jeong Hogun serves under Baek Yeon’s command in the Embroidered Uniform Guard and honors Jin Taekyung as a comrade-in-arms after their shared battle.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 940
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 940
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 933
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 936
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is the Emperor’s thirteen-year-old younger brother, an exceptionally skilled young swordsman, and the newly appointed Crown Prince.
- **Personality:** Earnest and compassionate, he takes responsibility for others’ suffering and dreams of a peaceful age founded on justice, care for the people, wise counsel, and accountability, even when doing so demands personal sacrifice.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Zhu Bao is the Emperor’s younger brother and Crown Prince, and Hong Jin has been his steadfast caretaker since childhood. He admires Jin Taekyung and calls him a friend; his compassion for the Eastern Heaven Demon Lord reflects the different path made possible by those who supported him.

## Korean source

```text
＃941화



끝없이 펼쳐진 성벽과 북쪽의 출입을 통제하는 거대한 철문.

그리고 용이 아로새겨진 황실의 깃발을 높이 곧추세운 채 좌우로 시립한 일천의 금의위와 여러 조정 대신들의 선두에, 한 사람이 있었다.

“그래, 인사도 없이 이대로 떠날 속셈이었나?”

갑작스러운 황제의 등장에 나는 당황했고, 곧이어 웃고 있는 그를 따라 희미한 미소를 머금었다.

“오셨습니까.”

“짐이 귀중한 시간을 뺏는 건 아니겠지?”

“귀중한 시간이지만, 아주 잠시뿐이라면 귀중한 만남에 쓰겠습니다. 때마침 직접 전해 드려야 할 것도 있었고요.”

내 말의 의미를 파악하지 못해 잠시 고개를 갸웃거린 황제가 입맛을 다셨다.

“마치 짐이 기다릴 거라는 걸 알고 있었다는 듯한 어투인데.”

“솔직히 그것까진 예상 못 했습니다만, 이렇게라도 뵙게 되니 참 반갑네요.”

“그런 입 발린 소리는 집어넣게. 자네한테는 안 어울려.”

짐짓 눈살을 찌푸린 황제가 자신의 어깨너머를 턱짓하며 덧붙였다.

“평소처럼 솔직하게 대답하지 그러나. 실은 짐이 아니라 저들이 반가운 것이라고.”

맞다.

황도의 북문(北門) 앞에서 나를 기다리고 있던 것은 황제뿐만이 아니었다.

‘저건.’

시야에 들어오는 익숙한 얼굴들.

어쩌다 보니 황실에서 가장 먼저, 그리고 자주 본 얼굴이 된 금의위 천호 정호군은 시작에 불과하다.

지금 이 순간 황제와 더불어 가장 바쁘게 움직여야 할 백연과 홍진은 물론, 지난 며칠간 보지 못했던 한 사람의 모습도 보였다.

‘상산왕, 아니 황태제(皇太弟).’

마음 한구석이 따뜻해진다. 한때 목숨이 경각에 달했던 저 아이가 지금은 하나뿐인 가족과 함께 하고 있다는 사실에.

이곳을 떠나기 전, 마지막 인사를 건넬 수 있다는 사실에.

금방이라도 눈물이 쏟아질 듯한 얼굴로 말안장에 앉아 이쪽을 바라보는 주표에게 살짝 웃어 보인 나는, 황제를 향해 시선을 돌렸다.

“앞서 하신 말씀대로, 정말 솔직하게 대답해도 됩니까?”

“아니, 됐네. 생각이 바뀌었어.”

“저도 생각이 바뀌었습니다. 확실히 폐하보다는 저 사람들이 더 반갑네요.”

“이자가 감히……!”

억눌린 음성과 동시에 삽시간에 가라앉는 공기.

그러나 순간 굳은 표정으로 나를 노려보던 황제는, 언제 그랬냐는 듯 꾹 참고 있던 웃음을 터트렸다.

“언제나 신기하군. 아니, 희한할 정도야. 어찌 만백성의 어버이이자 지존에게 이리 오만무례하게 굴 수 있는가?”

“이미 말씀드렸다시피, 저는 한낱 무뢰배에 불과한지라 호패도 없고 부모님도 따로 계십니다.”

거침없는 대답에 곳곳에서 헛숨 삼키는 소리가 새어 나온다.

대부분의 사람들, 특히 이 자리에 왜 왔는지 모를 조정 대신들은 이게 맞나 하는 표정으로 서로를 바라보고 있었다.

물론 황제는 여전히 웃고 있을 따름이었지만.

“확실히 알겠네. 자네는 짐의 신하도, 대국의 백성도 아니라는 것을.”

황제는 내 대답을 기다리지 않고 말을 이었다.

“다만 정(正)과 의(義). 그리고 협(俠)에 따라 생각하고 행하니, 가히 일세의 영웅이며 만인의 경애를 받아 마땅할 터.”

다그닥. 다그닥.

천천히 말을 몰아 코앞까지 다가온 황제는 나를 물끄러미 바라보다, 불현듯 자신의 어깨로 손을 가져갔다.

스륵. 툭.

단단히 매어져 있던 끈이 풀어진다. 한 치의 망설임도 없이 스스로 망토를 끌러 내게 내민 황제가 흐릿하게 웃었다.

“뭐 하나. 받지 않고.”

“……!”

“……!”

보이지 않는 파장이 모두를 휩쓸었다.

특히 풍이라도 맞은 것처럼 파르르 떨고 있는 조정 대신들은, 금방이라도 살아 움직일 듯한 황금빛 용이 수놓아진 망토에 경악을 금치 못했다.

“폐, 폐하!”

“그, 그것은!”

사방에서 빗발치는 외침.

그러나 그 다급한 목소리들은, 황제의 짤막한 한마디와 함께 바람에 파묻혀 사라졌다.

“그만.”

주위를 무겁게 짓누르는 침묵 속, 나를 향해 시선을 돌린 황제가 입을 열었다.

“어서 받게. 별것 아닌 짐의 선물일세.”

재촉하듯 말하는 황제와 그런 그의 손에 들린 망토를 번갈아 바라보던 나는 그저 눈만 깜빡였다.

이 망토가 단순한 하사품이 아니라는 것쯤은, 사람들의 격렬한 반응이 없었더라도 충분히 알고 있었으니까.

“이건…… 충분히 별거 같은데요.”

결코 평범한 망토가 아니다.

황제가 직접 착용했던 것부터가 도저히 평범한 물건일 수 없지만, 그전에 가장 중요한 것은 따로 있었다.

용.

망토에 황금빛 수실로 수놓아진, 한 마리의 용.

그것이 곧 천자와 황실의 권위를 상징하는 문장이라는 것은, 세 살배기 어린아이도 아는 사실이었다.

“이미 알고 있는 모양이군. 이것이 어떤 의미인지.”

나는 기가 차서 대답했다.

“아니, 모를 수가 있습니까?”

“안다니 다행일세. 그럼 짐의 손이 떨어지기 전에, 더더욱 이 귀중한 선물을 받고 싶어질 테니.”

“잠시, 잠시만요.”

이 갑작스러운 상황에 당황한 나는 머뭇거렸지만, 황제의 태도는 단호했다.

“부디 거절하지 말게. 그랬다간 아주 후회할 만한 일이 벌어질 거야.”

“예?”

멍하니 반문하는 내게, 황제가 짐짓 준엄한 어조로 말을 이었다.

“자네가 이것조차 거부한다면, 짐은 아주 섭섭해질 걸세.”

“그게 무슨.”

“어떤 상황이 벌어질지는 아무도 모르지. 하지만 안심하게. 고작 이런 일로 설마 황실의 은인이 불편하게 만들겠나?”

“……조금도 안심이 되지 않는 건, 그저 제 기분 탓입니까?”

“정확하군. 맞네, 자네 기분 탓이야.”

나와 황제는 한동안 아무런 말 없이 서로를 바라보았다.

그리고 약속이라도 한 것처럼, 동시에 실소를 흘렸다.

비록 내가 그를, 그를 내가 알게 된 시간은 짧았으나 우리 두 사람은 이미 알고 있었다.

어쩌면. 아주 조금은…….

‘서로를 닮아 있다는 것을.’

나는 소중한 것을 지키기 위해 싸웠다. 그 역시 다른 누군가를 위해 희생했다.

거리낌 없이 자신의 목숨을 판 돈으로 내던졌고, 그 선택을 후회하진 않는다.

서 있는 장소와 보이는 풍경만이 다를 뿐. 내가 그렇듯이 황제 역시 한 명의 인간이었다.

도움에 감사할 줄 알고, 농담을 좋아하며, 죽음을 두려워하는.

그저 자신의 위치에서 최선을 다해 싸운 한 사람.

스륵.

나는 손을 뻗어 황제가 내민 망토를 받아 어깨에 둘렀다. 그리고 공손히 포권 지례를 취했다.

“귀한 선물, 감사히 받겠습니다.”

“잘 어울리는군. 하지만 한 가지가 부족해.”

망토를 두른 내 모습을 흡족하게 바라보던 황제가, 갑옷 사이에서 번쩍이는 은패(銀牌)를 꺼내어 내밀었다.

다음 순간 두 귀를 의심케 만드는 한 마디와 함께.

“천자의 이름으로 명하니. 태원진가의 진태경을 상산후(上山侯)에 봉한다!”

공력이 실린 목소리가 깊은 밤을 깨웠다.

끝없이 퍼져 나가는 그 외침에, 감히 다가오지 못하고 멀찍이 떨어져서 황제의 행차를 구경만 하던 백성들이 금의위들의 손에 들린 횃불을 향해 모여들었다.

계속해서 울려 퍼지는 황제의 준엄한 외침을 들으며.

“산서성의 태원(太原)을 포함한 혼주, 양천, 정양, 진중, 태곡, 교성 등 십여 개 현을 봉토로 내리며, 식읍(食邑) 일만 호와 금은 십만 냥. 그에 더하여…….”

스릉.

돌연 허리춤에서 솟구친 섬광. 황실의 보검을 뽑아 든 황제가 안광을 번뜩이며 외쳤다.

“금일 이 시간부로 금의위 천호(千戶)의 직위를 내리니, 속히 일천의 금의위를 이끌고 황명에 따라 천하의 질서를 어지럽히는 외적(外賊)을 토벌하라!”

“……!”

“……!”

숨이 막힌다. 가슴이 두방망이질 쳤다.

쿵. 쿵. 쿵!

심장이 뛰는 소리가 아니다.

좌우로 시립한 일천의 금의위가 힘차게 발을 구르고 있었다. 각자의 병장기를 부딪치고, 갑옷을 두드렸다.

황제를 위하여.

아니, 나를 위하여.

‘아.’

나는 차오르려는 신음을 삼켰다.

이제야 깨달았다.

황제가 일천이나 되는 금의위를 거느리고 이곳에서 나를 기다렸던 목적은, 단지 호위뿐만이 아니었다는 것을.

저들은 황제의 명을 따라 결성된 토벌군이었다.

동시에 나를 위해 준비한 지원군이었다.

암천에 맞서 산서성을, 태원진가를 지켜 낼 방패이자 검.

와아아아아!

띠링. 띠링 띠링.

귓가가 먹먹했다.

쉴 새 없이 울려 퍼지는 종소리로. 그리고 모두가 내지르는 함성과 환호로.

그리고 그 중심에서, 황제는 나를 바라보며 웃고 있었다.

“성공하면 군왕이요(成卽君王). 실패하면 역적이라(敗卽逆賊).”

혁명을 꾀한 것은 둘이나, 살아남은 것은 하나다.

역적들을 뿌리 뽑고 모든 것을 되돌려 놓은 황제는, 떠나는 이들을 위한 논공행상(論功行賞)을 잊지 않았다.

“이렇듯 모든 일에는 그만한 대가가 따르기 마련인 법. 어떤가, 짐이 준비한 선물이?”

무슨 말이 더 필요할까.

나는 참았던 숨을 토해 내며 대답했다.

“끝내줍니다.”

“열후(列侯)의 반열에 올랐으니 마땅히 짐의 신하여야 할 것이나, 아무래도 상관없다.”

툭.

황제의 손이 내 어깨에 닿았다. 몸 안의 불씨가 서서히 꺼져 가고 있음에도, 손끝을 타고 전해지는 온기가 느껴졌다.

“지금껏 해 왔던 것처럼, 그렇게 행하라.”

시선은 늘 올바름(正)을 바라보고, 뜻과 행동은 의협(義俠)에 따르라.

흐르는 물처럼 이어지는 목소리와 함께, 황제가 나직이 덧붙였다.

“짐의 백성도, 신하도 아닌…… 단지 이 천하(天下)를 밝게 빛내는 한 사람이 되어 주게.”

깊게 가라앉은 그 한마디는, 마치 마지막 유언처럼 귓가를 울렸다.



* * *



만남과 이별은 떼놓을 수 없는 단어다.

만남이 있다면 이별이 있고, 이별 뒤에는 또 다른 만남이 기다리고 있다.

하지만 그럼에도 불구하고 이별의 순간은 늘 씁쓸하고 아쉽다.

특히나, 크게 의지했던 누군가를 떠나보내는 어린아이에게는 더더욱.

툭. 투둑.

말안장을 적시는 물기.

황제는 소리 없이 울고 있는 막내아우의 얼굴을 바라보는 대신, 떠나간 이들의 빈자리를 바라보며 담담하게 입을 열었다.

“그리도 슬프더냐.”

“아닙, 아닙니다.”

주표는 황급히 소매로 눈가를 닦았다.

어린아이는 울어도 되지만, 황태제는 다르다.

대국의 후계자로서 전란과 맞서야 하는 주표는, 결코 울어서는 안 되는 사람이 되었다.

“조금도, 슬프지 않습니다.”

“그거 참 희한하구나.”

“예?”

“짐은 아쉽기만 하거늘, 지학(志學)도 되지 않은 너는 어찌 슬프지 않을 수 있는지.”

순간 놀라서 고개를 든 주표의 눈동자에, 웃고 있는 황제의 모습이 고스란히 담겼다.

“표아야.”

대답도 잊은 채 자신을 멍하니 바라보는 주표를 향해, 황제는 부드럽게 말을 이었다.

“벌써부터 애써 삼킬 필요는 없다.”

“……!”

“인내는 쓰고 열매는 달다고 하나, 그렇게 쌓인 인내는 언젠가 독이 되는 법이니.”

“혀, 형님. 아니 폐하.”

“울고 싶을 때, 마음껏 울거라.”

툭.

어색한 손길로 주표의 머리를 쓰다듬은 황제는 말고삐를 돌려 돌아섰다.

누군가에게 들었던 한마디와 함께.

“짐도, 너도. 결국 사람이니라.”

이내 등 뒤에서 흘러나오는 울음소리를 들으며, 황제는 생각했다.

주표만큼은, 막내아우만큼은 자신과 같은 전철을 밟지 않기를.

‘짐은…… 너무나도 뒤늦게 깨달았지.’

그리고 황제의 입가에 흐릿하게 웃음이 맺힌 그 순간. 서서히 닫혀 가는 거대한 철문 너머로 한 마리의 준마가 달려왔다.

‘잠깐. 저자는.’

이해할 수 없는 상황 속, 황제는 되돌아온 한 사람을 보며 물었다.

“놓고 간 것이라도 있는가? 신의(神醫).”

“예.”

신의가 웃으며 말을 이었다.

“환자를 두고 왔습니다.”
```

## Final English reading copy

```markdown
# Chapter 941

An endless stretch of city wall, and a massive iron gate controlling passage to the north.

At the head of a thousand Embroidered Uniform Guards and several court ministers standing in formation on either side, the imperial banners bearing embroidered dragons held high, stood one man.

“So, were you planning to leave just like this without saying goodbye?”

The Emperor’s sudden appearance caught me off guard. Then, following his smile, I let a faint one settle on my own face.

“Your Majesty.”

“I hope I’m not taking up your precious time.”

“My time is precious, but if it’s only for a little while, I’ll spend it on a precious meeting. As it happens, there was something I needed to tell you in person, too.”

The Emperor tilted his head, not quite grasping what I meant, then smacked his lips.

“You speak as if you knew I’d be waiting.”

“Honestly, I didn’t expect that much. But I’m glad I get to see you, even like this.”

“Enough of that empty flattery. It doesn’t suit you.”

The Emperor feigned a frown, then jerked his chin over his shoulder.

“Why not answer honestly, like you usually do? In truth, it isn’t me you’re glad to see. It’s them.”

He was right.

The Emperor wasn’t the only one waiting for me in front of the North Gate of the imperial capital.

*That’s…*

Familiar faces came into view.

The Thousand Captain of the Embroidered Uniform Guard, Jeong Hogun—the first face I’d seen at the imperial court, and the one I’d seen most often since—was only the beginning.

Baek Yeon and Hong Jin, who should have been busier than anyone else right now, were there, too. And I spotted someone I hadn’t seen in the past few days.

*Prince Shangshan. No—the Crown Prince.*

Warmth spread through a corner of my heart. That boy, whose life had once hung by a thread, was now beside his only family.

And I’d get to say goodbye before I left.

I gave Zhu Bao, who sat astride his horse and looked ready to burst into tears, a faint smile. Then I turned back to the Emperor.

“May I answer honestly, as you said?”

“No, never mind. I’ve changed my mind.”

“I’ve changed mine, too. You’re right—I’m happier to see them than I am to see Your Majesty.”

“How dare you…!”

His suppressed voice was accompanied by an air that instantly turned cold.

But the Emperor, who had glared at me with a rigid expression for just a moment, suddenly burst into the laughter he’d been holding back.

“You never cease to amaze me. No—your behavior is downright bizarre. How can you be so arrogant and rude to the father of all the people and the supreme ruler?”

“As I’ve already told you, I’m nothing more than a mere rogue. I don’t even have an identity plaque, and I have parents of my own.”

At my unhesitating reply, gasps escaped from here and there.

Most of the people—especially the court ministers who had no idea why they were even here—looked at one another as if to ask whether this was really happening.

The Emperor, of course, was still smiling.

“I understand now. You are neither my subject nor a citizen of the Great Nation.”

Without waiting for my reply, the Emperor continued.

“But you think and act according to justice, righteousness, and chivalry. You are truly a hero of your age, worthy of the admiration of all.”

Clip-clop. Clip-clop.

The Emperor rode slowly toward me until he was right in front of me. He gazed at me for a moment, then suddenly raised a hand to his shoulder.

*Slip. Thump.*

The tightly tied cord came loose. Without the slightest hesitation, the Emperor removed his own cloak and held it out to me, smiling faintly.

“What are you waiting for? Take it.”

“……!”

“……!”

An unseen shockwave swept through everyone.

The court ministers were trembling as if they’d been struck by a stroke. They could hardly believe their eyes as they stared at the cloak embroidered with a golden dragon that looked ready to spring to life.

“Y-Your Majesty!”

“T-That is…!”

Shouts came from every direction.

But their desperate voices were swallowed by the wind at the Emperor’s curt command.

“Enough.”

In the heavy silence pressing down on those around us, the Emperor turned his gaze to me and spoke.

“Take it. It’s only a small gift from me.”

I looked from the Emperor, who was urging me on, to the cloak in his hand. All I could do was blink.

Even without everyone’s vehement reaction, I knew this wasn’t some simple gift.

“This is… pretty far from ‘only a small gift.’”

It was no ordinary cloak.

The fact that the Emperor himself had worn it already made it impossible for it to be an ordinary thing. But there was something even more important.

A dragon.

A dragon embroidered on the cloak in golden thread.

Even a three-year-old knew that this was the emblem of the Son of Heaven and the authority of the imperial house.

“You seem to know what it means.”

I could only stare at him in disbelief.

“How could I not?”

“Good. Then you’ll be all the more eager to accept this precious gift before my hand falls off.”

“Wait, wait a moment.”

Taken aback by this sudden turn of events, I hesitated, but the Emperor was firm.

“Please don’t refuse. If you do, something will happen that you’ll deeply regret.”

“What?”

I stared at him blankly. The Emperor continued in a deliberately stern voice.

“If you refuse even this, I’ll be very hurt.”

“What does that—”

“No one can say what might happen. But rest assured. Surely I wouldn’t make the imperial house’s Benefactor uncomfortable over something so trivial?”

“Is it just me, or does that not make me feel reassured at all?”

“Exactly. That’s all in your head.”

The Emperor and I stared at each other in silence for a while.

Then, as if we’d agreed to it, we both let out a dry chuckle.

Though we hadn’t known each other long, we already understood.

Maybe, just a little…

*That we were alike.*

I had fought to protect what was precious to me. He, too, had made sacrifices for someone else.

He’d wagered his life without hesitation, and he didn’t regret that choice.

The only difference was where we stood and what we saw. Just like me, the Emperor was only human.

Someone who knew how to be grateful for help, who liked jokes, who feared death.

Just one person who had fought as best he could from the place he stood.

*Swish.*

I reached out, took the cloak the Emperor offered, and draped it over my shoulders. Then I respectfully clasped my hands in a salute.

“I gratefully accept this precious gift.”

“It suits you. But there’s one thing missing.”

The Emperor looked at me in my cloak with satisfaction, then took a gleaming silver plaque from between the plates of his armor and held it out.

The next moment, he said something that made me doubt my own ears.

“By the Son of Heaven’s authority, I appoint Jin Taekyung of the Jin Family of Taiyuan Marquis of Shangshan!”

His voice, strengthened with internal energy, shattered the deep night.

His cry rang out without end. Commoners who had watched the Emperor’s procession from a distance, not daring to approach, began gathering around the torches held by the Embroidered Uniform Guards.

As the Emperor’s solemn declaration continued to echo—

“I grant you as your fief more than ten counties, including Taiyuan in Shanxi Province, Honju, Yangcheon, Jeongyang, Jinzhong, Taigu, and Jiaocheng, along with ten thousand households for your stipend and a hundred thousand taels of gold and silver. In addition…”

*Shing.*

A flash of light suddenly leapt from his waist. The Emperor drew the imperial sword, his eyes gleaming as he shouted,

“From this moment, I also appoint you Thousand Captain of the Embroidered Uniform Guard. Lead a thousand guards and, in accordance with the imperial command, swiftly put down the foreign bandits who disturb the order of the realm!”

“……!”

“……!”

I could hardly breathe. My heart pounded.

*Thump. Thump. Thump!*

It wasn’t the sound of my heart.

The thousand Embroidered Uniform Guards standing in formation on either side stamped their feet with all their might. They clashed their weapons together and struck their armor.

For the Emperor.

No—for me.

*Ah.*

I swallowed the groan rising in my throat.

Only now did I understand.

The Emperor hadn’t brought a thousand Embroidered Uniform Guards here to wait for me just as an escort.

They were an army assembled by imperial command to punish the enemy.

And at the same time, they were reinforcements prepared for me.

A shield and a sword to defend Shanxi Province and the Jin Family of Taiyuan against Dark Heaven.

“Waaaah!”

*Ding. Ding-ding.*

My ears rang.

From the incessant chime of bells. From the shouts and cheers erupting all around me.

And there, at the center of it all, the Emperor smiled at me.

“Success makes you a king; failure makes you a traitor.”

Two men had plotted a revolution, but only one had survived.

Having uprooted the traitors and restored everything, the Emperor hadn’t forgotten to reward those who had helped him.

“Everything comes at a price. So, what do you think of the gift I prepared?”

What more could I say?

I let out the breath I’d been holding and answered,

“It’s incredible.”

“As a marquis, you should rightfully be my subject, but I don’t care about that.”

*Tap.*

The Emperor’s hand came to rest on my shoulder. His life force was slowly fading, and yet I could feel the warmth that reached me through his fingertips.

“Go on as you have until now.”

Keep your eyes on what is right. Let your intentions and actions follow righteousness and chivalry.

Along with his voice, flowing like water, the Emperor added quietly,

“Be not my subject, nor my citizen… Just be one person who shines brightly in this world.”

His words, low and heavy, rang in my ears like a final testament.

* * *

Meeting and parting are inseparable.

Where there’s a meeting, there’s a parting; and after a parting, another meeting awaits.

Even so, the moment of parting is always bitter and full of regret.

Especially for a child saying goodbye to someone he had relied on so deeply.

*Tap. Drip.*

Moisture fell onto the saddle.

Rather than look at his youngest brother’s silently weeping face, the Emperor gazed at the empty places left by those who had departed and spoke calmly.

“Are you really that sad?”

“N-no, I’m not.”

Zhu Bao hurriedly wiped his eyes with his sleeve.

A child was allowed to cry, but the Crown Prince was different.

As heir to the Great Nation, Zhu Bao would have to face the coming war. He had become someone who must never cry.

“I’m not sad at all.”

“That’s very strange.”

“Pardon?”

“I’m nothing but regretful, yet how can you, who haven’t even reached the age of fifteen, not be sad?”

Zhu Bao looked up in surprise. The Emperor’s smiling face was reflected clearly in his eyes.

“Bao’er.”

The Emperor spoke gently to Zhu Bao, who was staring at him blankly, having forgotten to answer.

“You don’t have to force yourself to swallow your feelings already.”

“……!”

“People say endurance is bitter and its fruit sweet, but endurance piled up like that will one day turn to poison.”

“Hyung… I mean, Your Majesty.”

“When you want to cry, cry as much as you like.”

*Tap.*

With an awkward hand, the Emperor stroked Zhu Bao’s head. Then he turned his horse around and rode away.

Along with a few words he’d once heard from someone.

“You and I are both, in the end, only human.”

As he heard the sobs rising behind him, the Emperor thought to himself:

He hoped Zhu Bao—his youngest brother—wouldn’t follow the same path he had.

*I… realized far too late.*

And just then, as a faint smile touched the Emperor’s lips, a magnificent horse came galloping through the enormous iron gate, which was slowly closing behind him.

*Wait. That man…*

Amid a situation he couldn’t understand, the Emperor saw the man who had returned and asked,

“Did you leave something behind, Divine Physician?”

“Yes.”

The Divine Physician smiled and continued,

“I left a patient behind.”
```
