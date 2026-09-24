<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0933.txt",
      "sha256": "9e6e972247813daa3296972abeb194cb59a4de501e264d0bd8fd2bef6f37a581",
      "bytes": 13092
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "98268e9525c4826c89074df8df773331420165d70c3a96a951aefc82643f7b1d",
      "bytes": 1461
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0666305ef3a14502bbfe5c72134a55888b76af6f3fad7264eaf0463c809292b0",
      "bytes": 231946
    },
    {
      "path": "characters/Baek Yeon.md",
      "sha256": "c1d1fccfd5164cb10391aa97eff1dc6052c23cddec157ec29e64379ac6a2a166",
      "bytes": 837
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "2d8f3b1ddb22207bc279510657d7163c80e134f3bb72eadf9f225cfa9a81db4e",
      "bytes": 853
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "05f8f8cc22a543d0c4539b323698180174d1ec5e9fb46895c038a53c41af656e",
      "bytes": 628
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "ebba9e8cb239fd6e3d67667f7cf6e8267c8f5caf8b8817d75907ca2e1246e318",
      "bytes": 1343
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "f7d112fcc40172b2bfedbebaff13ca3cf03e60d7865d5826da9b6e8ad447251f",
      "bytes": 622
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "bdb639b94210bffa609ed90c3687698ecf6281cad0b139f1c6153c4f43f105bc",
      "bytes": 699
    },
    {
      "path": "characters/So Gyo.md",
      "sha256": "82ad9f7e6df138da6cbb8a08c3e7d368c09559dd80594c3717ceb87a3b061b62",
      "bytes": 767
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "0e2d532f2af4d7be69c6e65c1cef25321d7cf2235ebf140c6de94d6147d63060",
      "bytes": 266948
    }
  ],
  "estimated_tokens": 10995
}
-->

# Durable State Update — Chapter 933

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
1 and safe_through 933. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 933. Profile updates may replace only one
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
  "chapter": 933,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 933,
    "continuity_sources": [933],
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
    "The System update is complete; its reward is a very durable pocket watch that appears broken and bears the faint inscription, “A broken clock is right twice a day.” Its significance is unknown.",
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin.",
    "The Emperor has summoned Taekyung, and Taekyung agreed to go.",
    "Hong Jin has been promoted to Eunuch Hong and is responsible for the East Depot; the Cang Gong post remains vacant.",
    "Ma Sanbao escaped and evaded the Imperial Army’s three-day search.",
    "The Eastern Heaven Demon Lord’s final instruction was to find an unspecified object at a particular place."
  ],
  "continuity_sources": [
    931,
    932
  ],
  "open_questions": [
    "What is the Martial God’s identity, and how did he know a chosen one would appear?",
    "How far has Dark Heaven infiltrated the Great Nation, and which officials or commanders are involved?",
    "Where is Ma Sanbao, and what is his current status?",
    "What object and place did the Eastern Heaven Demon Lord refer to, and what significance does the object have?",
    "What is the significance, if any, of the broken pocket watch given as the System update reward?"
  ],
  "safe_through": 932,
  "temporary_decisions": [
    "Taekyung will keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 궁성     | **Bow Saint**                 | —              |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 영약     | **elixir**                                       |                                                       |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 백연 | **Baek Yeon** | Commander of the Embroidered Uniform Guard. |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 소교 | **So Gyo** | The palace attendant leading the group assigned to serve Prince Shangshan. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 태자 | **Crown Prince** | Title of the Emperor's older brother who was reportedly assassinated. |
| 황태자 | **Crown Prince** | The Emperor's older brother in Taekyung's recollection. |
| 선황 | **the late Emperor** | The former Emperor whom Hong Jin served. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 살인멸구 | **Silencing the Witnesses** | Killing witnesses to prevent a secret from being exposed. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 독물 | **venomous beasts** | Venomous creatures associated with the Nanman Beast Palace. |
| 황족 | **Huang tribe** | Nanman tribe involved in a recently settled dispute. |
| 궁인 | **palace attendant** | Former Inner Palace attendant expelled by Baeksang. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 혈혼고 | **Blood Soul Gu** | Rare gu poison found deep in Nanman. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 건청궁 | **Qianqing Palace** | The Emperor's palace, where Baek Yeon meets him. |
| 앵속 | **poppy** | The dried poppy sap Hong Jin describes; Taekyung identifies it as opium. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 홍진 | 진태경 | political_host_to_young_martial_artist | Young Hero Jin; Young Master Jin; Sleeping Dragon of Shanxi | polite, coaxing, and probing | Uses respectful forms while steering Taekyung toward relaying the Escort Bureau proposal and teasing him with the Seongun Escort Bureau. |
| 진태경 | 홍진 | young_martial_artist_to_political_official | Comrade Chairman—no, Deputy Military Commissioner | casual and teasing, then formally corrective | Deliberately jokes with an inappropriate title before correcting himself to Hong Jin's official office. |
| 정호 | 진태경 | Shaolin Discipline Hall Master to patient and Benefactor | Benefactor Jin | formal-polite | Jung Ho repeatedly uses 진 시주 and 시주. |
| 진태경 | 정호 | patient to Shaolin Discipline Hall Master | Monk | polite and familiar | Taekyung addresses Jung Ho as 스님. |
| 진태경 | 정호군 | young martial artist to senior imperial officer | Commander Jeong | casual and teasing, then conciliatory | Jin addresses him by rank while trying to defuse the standoff. |
| 백연 | 정호군 | commander to subordinate | you | direct and commanding | Uses 네 while testing Jeong Hogun’s obedience. |
| 홍진 | 백연 | imperial aide confronting a senior military officer | you | angry and confrontational | Uses 당신 in an indignant outburst. |
| 진태경 | 백연 | young martial artist confronting an imperial military commander | you | casual and insulting | Refers to Baek as 이 양반 while challenging his conduct. |
| 백연 | 천자 | imperial officer addressing the Emperor | Your Majesty | formal, deferential in address but openly defiant in private counsel | Baek uses formal honorifics while sharply confronting the Emperor over their shared undertaking. |
| 천자 | 백연 | Emperor addressing his military commander | Baek Yeon | familiar and authoritative | The Emperor addresses Baek by name and gives him a direct warning. |
| 정호군 | 홍진 | Embroided Uniform Guard officer addressing a senior imperial official | Deputy Military Commissioner | formal and admonishing | Hogun tells Hong Jin to mind his words. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 소교 | 진태경 | palace attendant addressing a martial artist and guest under escort | Young Master Jin | formal and respectful, but firm | Addresses him as 진 공자 while escorting him and warning him not to investigate. |
| 홍진 | 정호군 | Embroided Uniform Guard officers of equal rank | Thousand Captain Jeong | polite and direct | Hong Jin addresses Jeong Hogun by rank and surname. |
| 진태경 | 소교 | palace attendant and martial artist under imperial scrutiny | you | formal-polite, controlled and challenging | Taekyung addresses So Gyo as 당신 while questioning her presence and demanding an explanation. |
| 백연 | 진태경 | imperial commander confronting a young martial artist | Jin Taekyung | measured and familiar, using 자네 | Baek Yeon cautions Taekyung about his words and asks whether he must cause a scene. |
| 소교 | 백연 | political ally addressing a senior military commander | you | informal and direct | So Gyo uses 당신 and speaks without formality; no personal name or title is established. |
| 백연 | 소교 | military commander addressing a powerful political ally | you | formal and deferential | Baek Yeon uses 그대 while questioning So Gyo; she speaks without formality, which he accepts as her due. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |
| 황제 | 소교 | Emperor questioning a political ally | you | quiet and direct | The Emperor questions So Gyo through Sound Transmission about why she is only watching. |
| 소교 | 황제 | political ally answering the Emperor | Your Majesty | calm and direct | So Gyo answers the Emperor through Sound Transmission without wavering. |
| 황제 | 백연 | Emperor to the imperial court’s foremost military commander and trusted comrade | Baek Yeon | Direct and familiar; framed as a request rather than an order | The Emperor asks Baek Yeon to sound the war drum. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |

## Listed compact profiles

### Baek Yeon.md

# Baek Yeon (백연)

- **Safe through:** Chapter 926
- **Aliases:** Blood Envoy
- **Role:** Baek Yeon is the Commander of the Embroidered Uniform Guard, a former martial arts instructor to the Crown Prince, and the Blood Envoy who helped the fourth prince seize the throne and led the purge.
- **Personality:** Politically assured and controlled, he enforces authority with ruthless decisiveness but speaks with striking defiance to the Emperor in private when their shared undertaking is at stake.
- **Voice:** Not established
- **Relationships:** He commands the Embroidered Uniform Guard and serves the Emperor, carrying out the late Emperor’s final command to plan for the future alongside the fourth prince; he treats Taekyung as a dangerous potential obstacle.

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 931
- **Aliases:** None
- **Role:** Hong Jin is Eunuch Hong, a former Deputy Military Commissioner of Shanxi Province and East Depot member who is now responsible for the East Depot and remains a trusted aide to Prince Shangshan.
- **Personality:** Composed, socially deft, and ambitious, Hong Jin became a eunuch to escape poverty and save his family, then used his abilities to pursue a broader life.
- **Voice:** Delicate and deferential with Prince Shangshan, but warm, familiar, and playfully forthright with trusted allies.
- **Relationships:** Hong Jin is devoted to Prince Shangshan and is trusted by the Emperor to take responsibility for the East Depot; he is a longtime friend of Ma Sanbao and a trusted ally of Jin Taekyung.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 932
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he follows imperial orders without hesitation and reads the political consequences of events with care.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Jeong Hogun serves under Baek Yeon’s command in the Embroidered Uniform Guard.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 930
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 930
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 932
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### So Gyo.md

# So Gyo (소교)

- **Safe through:** Chapter 922
- **Aliases:** None
- **Role:** So Gyo is the Bow Saint, a Supreme Peak master and palace attendant assigned to Prince Shangshan, whose two curved swords can join into their original bow form.
- **Personality:** Calm, calculating, and self-possessed; she conceals her strength and identity and can be openly taunting.
- **Voice:** Measured and composed, shifting from deferential formality to casual, pointed taunts and threats.
- **Relationships:** So Gyo recognizes Jin Taekyung as the chosen one spoken of by the Martial God; she says only she and the Emperor know a secret she withheld from Baek Yeon, while her true allegiance remains unknown.

## Korean source

```text
＃933화



나는 정호군을 따라 이동하며 주위를 찬찬히 살폈다.

뭔가 극적인 변화가 있을 거라고 예상했던 것과는 달리, 황궁은 처음 왔을 때와 비교해도 크게 달라진 것이 없었다.

정갈한 복색을 차려입은 궁인들이 종종걸음으로 바쁘게 움직였고, 중무장한 금의위들은 각자의 위치에서 철탑처럼 경계를 취하고 있었다.

다만, 큰 변화가 있다면 그것은 다름 아닌 나 자신이었다.

스윽.

건너편에서 다가오던 한 무리의 궁인들이 깊게 고개를 숙이고 지나갈 때만 하더라도 우연인 줄 알았다.

철컥.

삼엄한 기세로 경계를 서고 있던 금의위들이 갑옷을 두드리며 군례(軍禮)를 취했을 때도, 별다른 이상함을 느끼진 못했다.

그저 금의위 내부에서도 한 끗발 하는 정호군이 동행하고 있으니 당연하다고 생각했을 뿐이었다.

“명색이 천호(千戶)라서 그런가, 방귀깨나 뀌나 봐?”

하지만 장난삼아 던진 그 말에 돌아온 정호군의 목소리는 담담하기 그지없었다.

“보기보다 눈치가 없는 편이군.”

“응?”

“저들이 예를 갖추는 이유는, 내가 있어서가 아니다.”

그 말을 듣고 나서야 문득 깨달았다.

그제야 비로소 보였다.

주위를 스쳐 지나가는 사람들의 시선이, 감사와 존경의 뜻을 담은 그들의 눈빛이 오직 나를 향하고 있다는 것을.

“어…….”

무슨 말을 해야 할까.

순간 할 말을 잃어버린 내가 머뭇거리던 그때, 막힘없이 나아가던 정호군의 발걸음이 우뚝 멈췄다.

아니, 그와 함께 온 모두의 발걸음이 동시에 멈췄다.

저벅.

칼 같은 움직임과 함께 묵직한 쇳소리가 울린다.

십여 장 앞, 건청궁(乾淸宮)이라 쓰여진 현판을 힐끗 바라본 정호군이 나를 향해 시선을 돌렸다.

“언제 다시 볼 수 있을지 모르니, 이 한마디는 지금 해야겠군.”

깊게 눌러쓴 투구 사이로 비치던 그의 날카로운 눈매가, 일순간 초승달처럼 부드럽게 휘었다.

“함께 싸울 수 있어서 영광이었소, 열화신룡 진태경.”

“……!”

나는 크게 뜨인 눈으로 정호군을 바라보았다.

지금껏 황제를 제외한 그 누구에게도 굽혀지지 않았던 그의 허리가, 뻣뻣한 목이 나를 향해 기울어지고 있었다.

정중하기 이를 데 없는 포권지례(抱拳之禮)와 함께.

“다시 만날 그날까지, 부디 무운(武運)을 빌겠소.”

“부디, 무운을!”

차차창!

복명복창하듯 힘차게 외친 수십의 금의위가 검을 뽑아 역수(逆手)로 그러쥔다.

건청궁으로 향하는 방향을 따라 양옆으로 나란히 시립한 그들의 모습에, 나는 참지 못하고 풀썩 웃어 버렸다.

“거, 낯간지럽게 왜들 이러시나.”

하지만 이내 웃음을 그치고, 그들 모두를 향해 나 역시 두 손을 모아 포권지례를 올렸다.

“나중에 또 봅시다. 꼭.”

진심이 담긴 한 마디.

그거면 충분하다.

언제 다시 저들과 만날지는 아무도 모르지만, 남은 이야기는 그때로 미뤄 두기로 했다.

만남과 인연에는 언제나 헤어짐이 있는 법이니까.

저벅. 저벅.

나는 정호군과 금의위가 만들어 준 길을 따라 천천히 걸음을 옮겼다.

높게 솟은 건청궁의 처마 아래, 새로 생긴 흉터로 드디어 얼굴을 구분할 수 있게 된 쌍둥이 무장이 나를 기다리고 있었다.

그리고 마치 아무런 절차도 필요 없다는 듯, 막 계단을 오른 내 앞을 가로막지 않고 조용히 비켜섰다.

그들이 지키고 있던 거대한 철문은, 처음 왔을 때와 달리 활짝 열려 있었다.



* * *



황궁에서도 가장 깊은 곳에 자리 잡은 건청궁.

바로 그 건청궁에서도 가장 안쪽에 위치한 그곳에서, 황제는 나를 기다리고 있었다.

“오, 왔나.”

전과는 달리 부드러운 어투와 반가움이 담긴 목소리.

그리고 웃고 있는 눈매.

하지만 즉위 전부터 무수한 숙청과 비정한 결단으로 철혈(鐵血)이라고까지 불리는 황제의 환대에도, 나는 웃지 않았다.

아니, 정확히는 웃지 못했다.

‘어째서?’

비록 입 밖으로 소리 내어 말하지는 않았지만, 완전히 감추지 못한 당혹스러움이 표정과 눈빛에 묻어 나온 모양이다.

할 말을 찾고 있는 내 모습을 바라보던 황제가 피식 웃으며 한발 먼저 입을 열었다.

“적잖이 당황한 모양이군. 하긴, 명색이 천자라는 이가 이런 꼴을 하고 있으니 그럴 만도 하지.”

황제는 상반신을 휘감고 있는 붕대를 툭툭 건드렸다.

입가에 맺힌 희미한 웃음으로 인해, 움푹 들어간 볼이 더욱더 도드라져 보였다.

“짐이 자네를 위해 조언 하나 해 주자면, 이럴 때는 고개부터 숙이는 게 좋아.”

사흘 전과 비교해도 말도 안 되게 수척해진 황제의 모습에 느낀 당황스러움은 아직 그대로였지만, 나는 애써 담담하게 대꾸했다.

“그럴 만한 이유라도 있습니까?”

“두 가지일세. 첫째로는 표정을 감출 수 있고, 둘째로는 아주 잠시뿐이지만 생각할 시간을 벌 수 있지.”

“그렇군요. 기왕 이렇게 된 김에 저도 한번 해 보죠.”

나는 잠시 고개를 숙인 뒤, 십여 초가 지나기도 전에 슬쩍 들어 올렸다.

“표정이야 이미 들켰으니 어쩔 수 없고, 확실히 생각할 시간이 있으니 좋은 것 같긴 합니다.”

“무슨 생각을 했는지 들어 볼 수 있겠나?”

“폐하께서 어째서 지금 같은 모습이신지 생각해 봤습니다. 그 이유도 함께요.”

“쓸데없는 생각을 했군. 짐은 단지 그날의 전투에서 무리했을 뿐이야.”

황제는 웃으며 손을 내저었지만, 그의 입가에 맺혀 있던 미소는 다음 순간 돌아온 내 대답을 듣는 순간 씻은 듯이 사라졌다.

“그래서, 또다시 앵속(罌粟)을 하신 겁니까?”

“……!”

“알아차리는 게 좀 늦었습니다. 예상치 못한 폐하의 모습에 주위의 냄새까지 신경 쓰지 못했거든요.”

나는 굳어 버린 황제의 얼굴을 바라보며 작게 심호흡했다. 콧속을 통해 스며드는 진하면서도 특이한 향은, 분명 기억 속에 존재하는 그것과 일치했다.

“언제부터…… 알고 있었나.”

어느새 깊게 가라앉은 황제의 목소리에, 나는 건청궁에 처음 발을 디뎠을 때를 떠올렸다.

마침내 대면한 황제에게서 느껴졌던 왠지 모를 익숙한 향과 때마침 간혹 앵속을 피우던 누군가를 통해 진실을 알게 되었던 순간도 함께.

“몰랐습니다. 처음에는.”

“자네가 어찌 알아차렸는지 모를 일이군. 시중에서 쉽게 구할 수도 없거니와, 무림인은 심신(心神)에 해가 되는 것을 멀리한다고 하던데.”

“아시는 바가 맞습니다. 확실히 그런 편이죠. 무림인은.”

나는 담담하게 덧붙였다.

“하지만 환관들은 종종 한다더군요.”

“……홍진이로군.”

한 번 입은 상처의 유통기한은 길다.

그 원인이 심리적인 것이든, 육체적인 것이든 인간의 머리와 몸은 똑똑히 기억한다.

수십여 년이 흐르고 흉터조차 희미해진 뒤에도 과거의 상흔(傷痕)이 욱신거리는데, 하물며 중요 부위를 잘라 낸 환관들은 오죽하겠나.

홍진 역시 예외일 수는 없었다.

그는 부지불식간에 찾아오는 통증을 이겨 낼 수 없을 때면 앵속에 손을 댔고, 그 덕분에 나는 뜻하지 않게 황제에 관한 한 가지 비밀을 알 수 있었다.

“도대체 언제부터, 그리고 무슨 이유로 앵속을 하시는 겁니까.”

“글쎄. 그걸 자네가 알아야 할 이유는 없지.”

뭐라 말하기도 전에, 황제가 씁쓸한 미소를 지으며 자신을 머리를 가리켰다.

“짐이 무슨 말을 한다 해도, 크게 달라지는 것 또한 없을 테고.”

“……설마?”

이미 체념한 듯한 태도. 거기에 더해 의미가 담긴 손짓까지.

눈을 부릅뜬 나를 향해, 황제는 메마른 입술을 달싹였다.

“맞네. 지금 자네가 생각하는 그것이.”

“……!”

“혈혼고(血魂蠱). 그 저주받은 독물이 이미 짐의 골수에까지 미쳤어.”

짐작이 확신으로 뒤바뀐 순간. 나도 모르게 신음과도 같은 외마디 욕설이 입 밖으로 튀어나왔다.

“이런 제기랄.”

“무엄하군. 감히 만백성의 어버이인 짐의 앞에서 그런 상스러운 말을 내뱉다니. 만약 이 자리에 백 지휘사가 있었다면 당장 형옥(刑獄)으로 끌려갔을 걸세.”

다른 누군가가 이런 말을 들었다면 손발을 벌벌 떨며 용서를 빌었겠지만, 나는 짐짓 눈살을 찌푸리고 있는 황제를 바라보며 한숨을 푹 내쉬었다.

“지금 그런 농담이 나옵니까?”

“짐이 농담에 일가견이 있다는 사실을 말해 줬던가?”

“처음 듣습니다. 심지어 소름 끼칠 정도로 재미없어요.”

“그건 자네가 원체 재미없는 사람이라 그런걸세. 짐이 전장을 누비던 시절에는 밤마다 수하들과 함께 술잔을 기울이며 웃고 떠들었었지. 참 재미있는 시절이었어.”

“굳이 중환자한테 이런 말 하고 싶진 않은데, 폐하 혼자만 재밌었을 겁니다.”

“그럴 리가. 짐이 무슨 말을 할 때마다 다들 배꼽을 잡았었는데.”

“……저런.”

그 시절의 수하들이 누구인지는 몰라도 웃어 주느라 고생깨나 했을 것 같다.

물론 이 상황에 그게 뭐가 중요하겠느냐마는.

눈치 없는 사단장, 아니 황제의 모습에 절레절레 고개를 내저은 나는 가장 궁금한 것부터 물었다.

“언제부터입니까?”

“십여 년 전. 정확히는 정변(政變) 직후였지.”

더는 감출 것도 없다는 듯, 황제는 담담하게 말을 이었다.

“믿고 있던 충복이 손을 썼네. 알아차렸을 때는 이미 늦어 있었지.”

“폐하의 측근 중 이 사실을 아는 사람은…….”

“단 두 사람뿐일세. 백연과 소교. 아니, 이제는 궁성이라고 불러야 할지도 모르겠군.”

황제가 나를 바라보며 덧붙였다.

“그리고 바로 오늘 이 자리에서, 알려져서는 안 될 진실을 아는 사람이 하나 더 늘었고.”

그 말에 담긴 의미를 즉각 알아차린 나는 작게 혀를 찼다.

“살인멸구(殺人滅口)라도 하시려고요?”

“만약 시도하면, 순순히 당해 줄 생각은 있나?”

“전혀요. 벽에 똥칠할 때까지 살 겁니다.”

“그런 의미에서는 짐이 훨씬 낫군. 황제씩이나 되어서 그런 추태를 부릴 수는 없지.”

그때였다.

작게 너털웃음을 흘리던 황제가 돌연 잔기침을 내뱉은 것은.

쿨럭.

붉게 물든 황금빛 옷소매. 갑작스러운 토혈(吐血)에 얼굴이 굳은 채 주위를 둘러보는 내 모습에, 황제가 한 박자 앞서 고개를 내저었나.

“괜한 짓 말게.”

“뭐가 괜한 짓입니까.”

“어의(御醫)라도 부를 생각이면, 그만두라는 말일세.”

“…….”

“그들의 의술로 치료할 수 있는 병이었다면 진즉 손을 썼을 거야. 하지만 짐이 어의들에게조차 이 사실을 숨긴 이유가 무엇이었겠나.”

황제는 핏물에 젖은 옷소매를 물끄러미 바라보며 혼잣말처럼 중얼거렸다.

“아바마마와 어마마마. 그리고 세분의 형님과 든든하게 종묘사직을 위해 힘쓰시던 황실의 웃어른들…… 단 한 사람도 예외는 없었어. 모두 죽음을 피할 수 없었지.”

맞다. 그 누구도 혈혼고의 마수(魔手)를 피하지 못했다.

정변 이후 모든 것을 되돌려 놓으려던 그의 시도가 수포로 돌아간 것 역시 그 때문이었다.

선황이, 황후가, 황태자를 비롯한 여러 직계 황족들이 차례대로 죽음을 맞이했고 정변을 일으킨 사황자는 용서받지 못할 폐륜아 이자 찬탈자로 낙인찍혔다.

“더 이상의 미련은 없네. 살기 위해 온갖 영약을 섭취하고, 뼈를 깎아가며 무공을 익혀 혈혼고의 독성(毒性)을 이겨 내야 했지. 그렇게 버텨 온 세월이 무려 십 년이야.”

비로소 깨달았다.

왜 그가, 천하에서 가장 거대한 영토와 수많은 군사를 발 아래 둔 그가 어째서 지금의 경지에 다다를 수 있었는지.

“십 년이 넘는 겨울을 버틴 끝에 바야흐로 봄이 찾아왔으니, 그것으로 되었다.”

지금 이 순간.

황제의 입가에는, 선명한 미소가 맺혀 있었다.
```

## Final English reading copy

```markdown
# Chapter 933

I followed Jeong Hogun, taking a careful look around as we went.

Contrary to what I’d expected, the Imperial Palace hadn’t changed much since my first visit. No dramatic transformation or anything.

Palace attendants in neat uniforms hurried back and forth, while the heavily armed Embroidered Uniform Guards stood watch at their posts like iron towers.

But if there was one big change, it was me.

*Swish.*

When a group of palace attendants coming from the other direction bowed deeply as they passed, I thought it was just a coincidence.

*Clank.*

Even when the Embroidered Uniform Guards, standing watch with a formidable air, struck their armor and saluted, I didn’t think much of it.

I just assumed it was because Jeong Hogun—a man with considerable pull even among the Embroidered Uniform Guards—was accompanying me.

“Guess being a Thousand Captain means you can throw your weight around, huh?”

But Jeong Hogun’s reply to my joking remark was utterly calm.

“You’re less observant than you look.”

“Hm?”

“They aren’t paying their respects because I’m here.”

Only then did it hit me.

Only then did I see it.

The gazes of the people passing around us—their eyes filled with gratitude and respect—were fixed solely on me.

“Uh…”

What was I supposed to say?

I hesitated, at a loss for words, when Jeong Hogun’s steady stride came to an abrupt halt.

No—not just his. Everyone who’d come with him stopped at the same time.

*Clop.*

With a movement as sharp as a blade, they rang with the heavy sound of metal.

A dozen or so jang away, Jeong Hogun glanced at the plaque that read *Qianqing Palace*, then turned to look at me.

“We may not get another chance to see each other, so I should say this now.”

The sharp eyes visible beneath his low-pulled helmet softened in an instant, curving like a crescent moon.

“It was an honor to fight alongside you, Blazing Flame Divine Dragon Jin Taekyung.”

“……!”

I stared at Jeong Hogun, eyes wide.

The back that had never bowed to anyone but the Emperor, the stiff neck—both were inclining toward me.

Along with a most respectful fist-and-palm salute.

“Until we meet again, I wish you good fortune in battle.”

“We wish you good fortune!”

*Ching, ching, ching!*

Dozens of Embroidered Uniform Guards shouted in unison and drew their swords, gripping them in reverse.

They stood in two neat rows on either side of the path leading to Qianqing Palace. I couldn’t help but burst out laughing.

“Come on, you’re making me blush.”

But I stopped laughing almost at once and returned their salute, bringing my hands together.

“See you again sometime. We will.”

A few words, spoken from the heart.

That was enough.

No one knew when we’d meet again, but I decided to leave the rest of the conversation for that day.

Every meeting, every bond, eventually came with a parting.

*Clop. Clop.*

I walked slowly along the path Jeong Hogun and the Embroidered Uniform Guards had made for me.

Beneath the high eaves of Qianqing Palace, the twin armored guards were waiting. A new scar finally let me tell their faces apart.

And as if no formalities were needed, they silently stepped aside instead of blocking my way as I came up the stairs.

The enormous iron gate they guarded stood wide open, unlike the last time I’d visited.



* * *



Qianqing Palace stood in the deepest part of the Imperial Palace.

And in the deepest part of Qianqing Palace, the Emperor was waiting for me.

“Oh, you’re here.”

His tone was gentler than before, his voice warm with welcome.

And his eyes were smiling.

But even with the welcome of an Emperor known as Iron Blood for his countless purges and ruthless decisions, even before his accession to the throne, I didn’t smile.

No—to be precise, I couldn’t.

*Why?*

I hadn’t said it out loud, but apparently I hadn’t managed to hide my bewilderment. It showed in my expression and my eyes.

The Emperor watched me searching for something to say, then gave a quiet laugh and spoke first.

“You seem rather taken aback. I suppose it’s understandable, given that the Son of Heaven looks like this.”

He tapped the bandages wrapped around his upper body.

His cheeks were sunken, made all the more prominent by the faint smile at the corner of his mouth.

“If I may offer you one piece of advice, it’s best to lower your head first at times like this.”

The Emperor looked absurdly gaunt compared to just three days ago. My shock hadn’t eased, but I forced myself to reply calmly.

“Is there a reason for that?”

“Two. First, you can hide your expression. Second, you buy yourself a little time to think.”

“I see. Since we’re here, I’ll give it a try too.”

I lowered my head for a moment, then lifted it again before even ten seconds had passed.

“I’ve already been found out, so there’s no point trying to hide my expression. But I have to admit, it does give me time to think.”

“May I ask what you thought about?”

“I wondered why Your Majesty looks like this. And what the reason might be.”

“You’ve been thinking about something pointless. I simply overexerted myself in that battle.”

The Emperor smiled and waved a hand, but the smile vanished without a trace when he heard my next words.

“So you’ve taken poppy again?”

“……!”

“I was a little slow to notice. Your Majesty’s appearance caught me by surprise, and I didn’t pay attention to the smell around me.”

I took a slow breath as I looked at the Emperor’s face, gone rigid. The heavy, peculiar scent drifting into my nose was unmistakably familiar.

“How long… have you known?”

The Emperor’s voice had sunk low. I thought back to the first time I’d stepped into Qianqing Palace.

I remembered the strangely familiar scent I’d sensed from the Emperor I finally met—and the moment I learned the truth through someone who occasionally smoked poppy.

“I didn’t know at first.”

“I can’t imagine how you figured it out. It’s not something you can easily get on the street, and I’d heard Murim practitioners avoid anything that harms the mind and spirit.”

“You’re right. They generally do.”

I added calmly,

“But I hear eunuchs sometimes use it.”

“……Hong Jin, then.”

A wound, once inflicted, has a long shelf life.

Whether the cause is psychological or physical, the human mind and body remember it clearly.

Even decades later, after the scars have faded, old wounds still ache. How much worse must it be for eunuchs, who’ve had their most private parts cut off?

Hong Jin was no exception.

Whenever the pain struck without warning and he couldn’t bear it, he turned to poppy. That was how I’d accidentally learned one of the Emperor’s secrets.

“How long have you been using it, and why?”

“Well. I don’t see why you need to know.”

Before I could say anything, the Emperor gave a bitter smile and gestured toward his own head.

“And even if I told you, it wouldn’t change much.”

“……No way.”

He seemed to have already given up. And that gesture had meaning, too.

The Emperor moved his dry lips as I stared at him, eyes wide.

“That’s right. What you’re thinking.”

“……!”

“The Blood Soul Gu. That cursed poison has already reached my very marrow.”

The moment my suspicion became certainty, a curse escaped me with a groan.

“Damn it.”

“Impertinent. To say something so vulgar in front of me, the father of all the people. If Commander Baek were here, he’d have you dragged to the prison at once.”

Someone else might have trembled and begged forgiveness, but I only sighed at the Emperor, who was making a show of frowning.

“Is this really the time for jokes?”

“Have I ever told you I’m good at jokes?”

“This is the first I’ve heard of it. And you’re so bad it gives me goose bumps.”

“That’s because you’re a dull fellow. Back when I was campaigning on the battlefield, I’d drink and laugh with my men every night. Those were good times.”

“I hate to say this to a critically ill man, but you were probably the only one having fun.”

“That can’t be. Every time I said something, they’d laugh until they doubled over.”

“……I see.”

I didn’t know who his men had been back then, but they must’ve worked hard to laugh along.

Not that any of that mattered right now.

I shook my head at the tactless commander—or rather, Emperor—and asked what I was most curious about.

“When did it start?”

“More than ten years ago. Just after the coup, to be exact.”

The Emperor continued calmly, as though there was nothing left to hide.

“A trusted loyalist did it. By the time I realized, it was already too late.”

“Who among Your Majesty’s inner circle knows?”

“Only two people. Baek Yeon and So Gyo. Though perhaps I should call her the Bow Saint now.”

The Emperor looked at me and added,

“And here, today, one more person has learned a truth that must never be known.”

I understood what he meant at once and clicked my tongue.

“Are you going to kill me to keep me quiet?”

“If I tried, would you let me?”

“Not a chance. I’m going to live until I’m so old I’m smearing shit on the walls.”

“In that respect, I’m much better off. I can’t disgrace myself like that as Emperor.”

That was when it happened.

The Emperor, who’d been chuckling softly, suddenly gave a small cough.

*Cough.*

His golden sleeve stained red. I looked around, my face hardening at the sudden spitting of blood, but the Emperor shook his head before I could move.

“Don’t bother.”

“Bother with what?”

“If you’re thinking of calling an imperial physician, don’t.”

“……”

“If their medicine could’ve treated this, I would’ve sought their help long ago. Why do you think I hid this even from the imperial physicians?”

The Emperor gazed at his blood-soaked sleeve and murmured as though to himself.

“My father and mother. My three elder brothers. And the senior members of the imperial family who worked so faithfully to protect the ancestral shrines and the state… Not one person was spared. They all died.”

That was right. No one had escaped the Blood Soul Gu’s grasp.

That was why his attempt to set everything right after the coup had come to nothing.

The late Emperor, the Empress, and several direct members of the imperial family, including the Crown Prince, had died one after another. The Fourth Prince who’d started the coup was branded an unfilial son and an unforgivable usurper.

“I have no regrets left. I took every elixir I could to stay alive, and trained in martial arts until my bones ached, trying to overcome the Blood Soul Gu’s poison. I endured like that for ten years.”

At last, I understood.

Why he—the man who held the greatest territory in the world and commanded countless troops—had reached the realm he stood in now.

“After enduring a winter that lasted more than ten years, spring has finally come. That’s enough for me.”

Right now,

a clear smile rested on the Emperor’s lips.
```
