<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0953.txt",
      "sha256": "afaa4dce20224ccb951752c7b365e765bbb66a13eda130b5a8baad6a5a7113ab",
      "bytes": 14419
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ac6cb84dfab6e5a5f5d4d385035096966abda6fec7760375d0703f9e36d29c55",
      "bytes": 2558
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "24305d1c9dc05d1f447a15c73fed9c251ab1fd23035f65c1d6eee6786b6d41c1",
      "bytes": 234031
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "5a3f5ae686ff9d1738e15884a5f5b129fba4456d07b88c9c1e87657ac30ff657",
      "bytes": 759
    },
    {
      "path": "characters/Hanga.md",
      "sha256": "569f941ca4f16561d78f4e046f9135d5edf42f34f2cb95109f0b407404318e0e",
      "bytes": 568
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "80696f946b0a91a482b4eddeca9a76c4ed609b0f461d837dbc96a64948d8f500",
      "bytes": 853
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "30fd28eb3a955049ec45d65e2e42ee1d9c025468df2b4135a00541c096bf540e",
      "bytes": 1343
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "d7ada8e2fa88cddf412418195d8c4c7e8ca5a16bdb80da5945a3be67d1ed0dc7",
      "bytes": 1449
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "7c97c9abd302462243e3d18fcdce33df0887aba4c03f47028e67bff693df34c3",
      "bytes": 1282
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "3a45721fc963280dc2452a03c2206ecfb18fd01191d9ba7fcc908d5127fb32e9",
      "bytes": 622
    },
    {
      "path": "characters/Li Feng.md",
      "sha256": "4a7acc1cabf2257fa0559ecd3d31fa2acfeef1fa15125a76690fc7760aa5171f",
      "bytes": 888
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "557f88f23c5c70b5e7cb3e7a5464328fca4e180d5a5d17eeefa764325af00fdc",
      "bytes": 267731
    }
  ],
  "estimated_tokens": 12307
}
-->

# Durable State Update — Chapter 953

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
1 and safe_through 953. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 953. Profile updates may replace only one
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
  "chapter": 953,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 953,
    "continuity_sources": [953],
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
    "The Emperor was poisoned with Blood Soul Gu, which reached his marrow; the Divine Physician said his vitality was at its limit and could not guarantee survival for another couple of months.",
    "The Divine Physician says the Emperor’s only path to survival requires him to die once; the method remains unexplained.",
    "Taekyung’s System Quest requires him to remove the Blood Soul Gu from the Emperor’s head and successfully treat him; its reward and failure consequence remain unknown.",
    "War with Dark Heaven is imminent. The Jin Family of Taiyuan and Shanxi forces are preparing a stand at Eight Spring Gorge against an estimated thirty to forty thousand advancing enemies; reinforcements are on their way.",
    "Jin Wikyung appointed Jin Mukyung Commander of the Heaven Shaking Squad and ordered him to lead two hundred men against enemy troops detouring around Jeongyang.",
    "A thousand-man steppe vanguard, including one hundred Keshik, was annihilated before the main army advanced; Jamukha killed its sole survivor.",
    "The improved Temporary Strength Pill may be spreading through Murim; its effects and distribution network remain unknown. Jang Sam abruptly rose from Level 40 to Level 60, attacked Taekyung while apparently irrational, and is unconscious.",
    "The Bow Saint wondered whether Pung Yang might have been the chosen one; the Martial God’s identity and connection to the chosen one and the Bow Saint remain unknown.",
    "The Eastern Heaven Demon Lord’s hidden iron chest contained old bamboo slips, recent papers, and a small silk pouch of unknown significance.",
    "The real Chinggen was killed in the attack on the khans’ gathering; an impostor wearing his face has manipulated Temur and now accompanies Jamukha."
  ],
  "continuity_sources": [
    951,
    952
  ],
  "open_questions": [
    "What will happen in the Shanxi campaign, and what role will Dark Heaven play in the fighting?",
    "Who gave Jang Sam the silk pouch, and what are the modified pill’s effects and side effects; how widely has the improved pill spread and who is distributing it?",
    "What is the Martial God’s identity, and what is his connection to the chosen one and the Bow Saint?",
    "What do the Eastern Heaven Demon Lord’s papers and silk pouch contain, and what is their significance?"
  ],
  "safe_through": 952,
  "temporary_decisions": [
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 진룡대    | **Jin Dragon Squad**             |
| 무인     | **martial artist**                               | Default term                                          |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 대주     | **Squad Leader** / **Commander**             |
| 제자     | **Disciple**                                 |
| 상태               | **Status**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 팔천협    | **Eight Spring Gorge** |
| 정마대전   | **Great Faction War**         |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 항아 | **Hanga** | Local village boy who lives near Jang Taebo. |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 이풍 | **Li Feng** | Shanxi Province's Assistant Military Commissioner; former Huashan lay disciple |
| 정양 | **Jeongyang** | Shanxi location |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 도지휘첨사 | **Assistant Military Commissioner** | Military office held by the unnamed official responsible for training soldiers. |
| 산서성부 | **Shanxi Provincial Office** | Government office where the City Lord resides west of Taiyuan. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 철전 | **iron coins** | Lower-value coin currency used to compare the payment's value. |
| 홍가 | **Hong** | Unnamed middle-aged Jin Family martial artist who identifies himself by surname. |
| 홍가촌 | **Hong Family Village** | Clan village said to be three hundred li from Jang Family Village. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 진룡 | **Jin Dragon** | The two characters embroidered on the Jin Dragon Squad's uniforms. |
| 한나절 | **half a day** | Elapsed duration in Jeok's first time-loss episode. |
| 장성 | **Great Wall** | Wall used in the discussion of the Outer Lands. |
| 소평 | **So Pyeong** | Alliance office worker assigned to prepare a report. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 이풍 | 진태경 | senior_official_to_respected_young_martial_artist | Young Hero Jin | formal and respectful | Addresses Taekyung as 진 소협 after praising his reputation. |
| 홍진 | 주표 | servant and political aide to prince | His Highness | formal-deferential | Uses the elongated royal call 전하 while summoning Zhu Bao. |
| 진태경 | 주표 | visitor to prince | His Highness, Prince Shangshan | formal-deferential | Addresses Zhu Bao as 상산왕 전하 after kneeling to meet his gaze. |
| 주표 | 진태경 | prince to visiting young hero | Jin Taekyung | formal and inquisitive | Uses the formal second-person address before asking Taekyung's name and requesting an autograph. |
| 홍진 | 진태경 | political_host_to_young_martial_artist | Young Hero Jin; Young Master Jin; Sleeping Dragon of Shanxi | polite, coaxing, and probing | Uses respectful forms while steering Taekyung toward relaying the Escort Bureau proposal and teasing him with the Seongun Escort Bureau. |
| 진태경 | 홍진 | young_martial_artist_to_political_official | Comrade Chairman—no, Deputy Military Commissioner | casual and teasing, then formally corrective | Deliberately jokes with an inappropriate title before correcting himself to Hong Jin's official office. |
| 진태경 | 이풍 | junior_to_respected_official_and_martial_ally | Great Hero Li | polite and respectful | Agrees with Li Feng's proposal that Zhu Bao visit the Jin Family's banquet. |
| 이풍 | 주표 | official_to_prince | Your Highness | formal-deferential | Suggests that Zhu Bao visit the Jin Family's grand banquet in fifteen days. |
| 진위경 | 홍진 | political_host_to_deputy_military_commissioner | Comrade Hong | formal-polite and playful | Jin Wikyung adopts Hong Jin's requested casual address, 홍 동지. |
| 홍진 | 진위경 | deputy_military_commissioner_to_lesser_family_head | Lesser Family Head Jin | formal and teasing | Hong Jin addresses Jin Wikyung as 진 소가주님 while flattering and joking with him. |
| 진태경 | 항아 | visiting_adult_to_local_child | little one | friendly and coaxing | Questions Hanga and offers food in exchange for information. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 주표 | 홍진 | prince to loyal subject | you | formal and reassuring | Zhu Bao refers to Hong Jin as 그대 while apologizing for the hardship he has endured. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 952
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hanga.md

# Hanga (항아)

- **Safe through:** Chapter 950
- **Aliases:** None
- **Role:** Local village girl, Jang-pal’s daughter, who lives near Jang Taebo and regularly visits him.
- **Personality:** Curious, energetic, observant, and already attentive to the value of information and food.
- **Voice:** Childlike, direct, and inquisitive, with an occasional surprisingly worldly remark.
- **Relationships:** Calls Jang Taebo Grandpa; Jang Taebo is his elderly neighbor and only conversational companion.

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 941
- **Aliases:** None
- **Role:** Hong Jin is Eunuch Hong, a former Deputy Military Commissioner of Shanxi Province and East Depot member who is now responsible for the East Depot and remains a trusted aide to Prince Shangshan.
- **Personality:** Composed, socially deft, and ambitious, Hong Jin became a eunuch to escape poverty and save his family, then used his abilities to pursue a broader life.
- **Voice:** Delicate and deferential with Prince Shangshan, but warm, familiar, and playfully forthright with trusted allies.
- **Relationships:** Hong Jin is devoted to Prince Shangshan and is trusted by the Emperor to take responsibility for the East Depot; he is a longtime friend of Ma Sanbao and a trusted ally of Jin Taekyung.

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 952
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Jin Mukyung is the second son of the Jin Family of Taiyuan, a Peak-level swordsman known as the Heaven Shaking Sword, and Commander of the Heaven Shaking Squad.
- **Personality:** Reserved and disciplined, Jin Mukyung is devoted to swordsmanship and seeks strength in service of his family.
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Jin Wikyung is his older brother and the Lesser Family Head who formed the Heaven Shaking Squad in his honor; Jin Taekyung is his younger brother, and Mukyung cherishes his promise to reunite with him.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 952
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor has appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 952
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm and politically capable, Jin Wikyung takes responsibility for his people and prioritizes their lives, but carries self-blame for past losses and can falter under the weight of a decision before resolving to act.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Jin Wikyung is Taekyung's eldest brother and future Family Head who protects and mentors him, commands Wipeng and the Jin Family's forces, has worked with Jeok Cheongang, maintains a political connection with Hongcheon, Prince Shangshan's hidden loyal retainer, and wants Taekyung to tell him his untold stories when the current crisis is over; Jin Mukyung is his younger brother and a potential successor alongside Taekyung.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 952
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Li Feng.md

# Li Feng (이풍)

- **Safe through:** Chapter 952
- **Aliases:** None
- **Role:** Assistant Military Commissioner of Shanxi Province; former Huashan lay disciple who left the sect nearly ten years ago
- **Personality:** Resolute, proud, blunt, and hostile toward political and martial rivals
- **Voice:** Formal and restrained in official settings; dry and cutting with opponents
- **Relationships:** Former lay disciple of Huashan; visited the hidden residence of his Grandmaster Mae Jonghak and saw ten-year-old Cheongpung there; recognizes Cheongpung as his Martial Uncle; direct subordinate and political rival of Hong Jin, the Deputy Military Commissioner; agrees to act as Hong Jin's intermediary with Huashan and send a messenger pigeon to his Master; bears a humiliating martial grievance involving Gong Ilhyuk

## Korean source

```text
＃953화



수십, 수백 명이 얽혀 싸우면 전투다.

하지만 그 단위가 수천, 수만으로 변한다면 그것은 더 이상 전투라고 부를 수 없다.

그건 전쟁이다.

서로가 온 힘을 다해 부딪치는, 각자의 모든 것을 건 전쟁.

그리고 진위경은 단 한 번의 도박으로 가진 것을 모두 잃을 생각 따위는 추호도 없었다.

“진천대주 진무경. 소가주께 보고드립니다.”

담담한 목소리와는 달리 핏물에 흠뻑 젖은 전신.

정오에 떠나 자정 무렵이 되어서야 되돌아온 진무경의 모습은, 그야말로 혈귀(血鬼)나 다름없었다.

진천검이라는 별호에서 비롯된 그의 수하들 역시도.

그러나 그들의 당당한 걸음걸이와 형형한 안광은, 태원진가가 거둔 첫 번째 승리의 증거였다.

“지엄하신 명령에 따라, 적의 예봉을 꺾고 돌아왔나이다.”

진무경은 천천히 말을 이었다.

이백여 명의 진천대 중 죽은 이가 스물셋, 크고 작은 부상을 입은 이가 서른일곱.

태원진가가 진룡대와 더불어 가장 심혈을 기울여 키워 낸 정예 무력대에서 단 한 번의 전투로 육십 명의 사상자가 나왔다는 소식에 몇몇 수뇌부의 낯빛이 무거워졌으나, 뒤이어 흘러나온 보고는 찰나의 슬픔마저 깨끗이 씻어냈다.

일천.

무려 다섯 배에 달하는 적의 선봉대를 궤멸시켰다.

심지어 그중에는, 적들의 정예 병력 일백 역시 포함되어 있었다.

“와아아아아!”

숨죽여 상황을 듣고 있던 이들이 일제히 함성을 내질렀다.

적들을 상대로 거둔 첫 번째 승리.

그것도 부정할 여지조차 없는 대승(大勝).

하지만 뜨겁게 달아오르는 공기 속, 진위경은 기뻐하는 와중에도 평정심을 잃지 않았다.

‘이건 단지 시작에 불과하다.’

그는 알고 있었다.

전쟁은 하나의 모래성을 쌓는 것과 같다. 여러 번 계속해서 모래를 퍼 올려 쌓아야 완성된다.

또한 그렇게 정성 들여 쌓아 올린 모래성 역시, 강한 발길질 한 번에 무너질 수 있었다.

‘하지만…… 발길질에도 무너지지 않을 만큼 공고히 쌓는다면 이야기는 달라진다.’

다행히 태원진가의 준비는 촉박했던 시간이 무색할 만큼 철저했다.

아마도 지금쯤 장성을 넘어 산서성 북부를 지나고 있을 초원의 군세는 당혹감을 느끼고 있을 것이다.

최정예가 포함되어 있던 선봉대의 전멸 소식에 한 번.

그리고 정말 ‘텅 비어 버린’ 북부의 상황에 또다시 한번.

‘네놈들이 북부에서 취할 수 있는 것은, 아무것도 없을 것이다.’

북부에서 빠져나간 것은 사람뿐만이 아니다.

진위경은 모든 병력과 양민들을 북부에서 후퇴시키는 한편, 곧 추수 시기에 이르는 논밭을 모조리 불태웠다.

이른바 초토화 작전.

당연히 물경 수만을 아우르는 대군을 상대로 펼치기에는 더할 나위 없는 묘수였으나, 진위경은 이 결정을 내리기 전 수십 번이나 고민했다.

산서성 도지휘첨사 이풍과 수백여 명의 사람들이 먼저 그를 찾아오기 전까지는.



‘비축되어 있는 군량만 수만 석입니다. 저들의 식량 문제는 충분히 감당할 수 있습니다.’



주표와 홍진의 부재로 현 산서성부의 실질적 최고위 인사라 할 수 있는 이풍은 적극적인 협조를 약속했고.



‘까짓거, 싹 다 불태우십쇼.’



하루아침에 고향 땅을 떠나야 했던 북부의 양민들. 아니 촌장들은 이미 분노로 눈이 반쯤 뒤집힌 상태였다.



‘염병할 새끼들. 허구헌날 쳐들어와서 지랄병을 떨더니 이제는 우리 논밭까지 털어먹으려고 들어?’

‘이미 우리 마을 사람들도 동의했습니다. 오랑캐 놈들 주둥이로 쌀 한 톨이라도 들어갔다간 내가 찢겨 죽을 판입니다.’

‘차라리 소나 돼지한테 쌀밥을 처먹이고 말지, 내 눈에 흙이 들어가도 그 꼴은 못 보겠소!’

‘시바 거. 반대하는 놈 있으면 지금 나와. 누군지는 몰라도 입 벙긋했다간 오랑캐 새끼로 간주하고 머리털을 싹 밀어서 변발을 틀어 줄라니까.’

‘거기 송 씨! 왜 아무 말도 안 해? 논밭에 꿀 발라 놨어?’



그리고 한마디도 하지 않은 채 침묵을 하고 있던 송 씨 촌장은, 단 한 마디로 모두의 박수갈채를 받았다.



‘불만 지르지 말고, 우물에 독을 탑시다.’

‘……!’

‘개울가에 똥오줌도 한 번씩 갈기고 떠나면 더 좋고.’

‘또, 똥오줌은 왜?’

‘물이 더러워지잖소. 똥오줌 섞인 물을 시원하게 들이키고 나면 그놈들 몸뚱어리가 멀쩡하겠소?’

‘허어어, 어떻게 그런 묘책을……!’

‘내가 한 번 먹어 봤어. 한 됫박 마셨다가 뒈지는 줄 알았소.’



똥물 섭취라는 특이 이력을 보유한 농사꾼 송 씨는 일약 영웅으로 등극했고, 사람들은 우물에 독초를 쑤셔 박고 개울가에 똥오줌을 갈기며 왜 그가 장원 급제자 출신이 아닌지 의문을 품었다.

착한 오랑캐는 죽은 오랑캐뿐이라는, 누군가가 들었다면 깜짝 놀랐을 이야기를 하면서.

‘이곳까지 오는 길이, 결코 순탄치는 않을 것이다.’

진위경은 서늘한 미소를 머금었다.

산서성은 부정할 수 없는 변방이다.

곡물 생산량은 상당하지만 중원만큼 발달하지도, 그만큼 강한 전력을 지닌 것도 아니다.

하지만 그렇기에, 위기 앞에서 더욱 강하게 뭉칠 수 있다.

오랫동안 지속된 마적단과 유목민들의 약탈은 산서인들에게 강한 심지를 심어주었고, 현재에 이르러서는 그 심지에 불이 붙었다.

‘반드시 지켜 낸다.’

진위경은 이미 굳게 다짐했다.

잠과 휴식을 없애고 모든 것에 전념했다. 발 빠른 수하들을 풀어 북부의 상황을 살피고, 소규모 별동대를 꾸려 혹시 모를 병력의 분산을 파악했다.

정양을 제외한 모든 우회로에 온갖 함정과 철질려(鐵蒺藜)를 설치한 것도, 직접 명령한 작업의 진행도를 살피는 것도 그 일환이었다.

“토성(土城)의 진행 상황은 어찌 되어 가고 있습니까?”

“보강 작업까지 생각한다면, 늦어도 한나절 안에는 완성될 것입니다.”

팔천협(八天峽).

과거 정마대전부터 지금까지, 무수한 생명을 집어삼킨 항아리 모양의 협곡 끝자락에는 지금껏 없었던 다섯 개의 성루(城樓)가 우뚝 서 있었다.

진흙과 나무, 그리고 돌을 섞어 만든 그것의 높이는 삼 장에 달했고, 각각 이백여 명의 사람을 수용할 수 있을 만큼 평평한 면적을 지니고 있었다.

정확히는, 이백의 궁수를.

“협곡 위를 점령한 것만으로는 아직 부족합니다. 승리를 위해서는 반드시 필요한 일이니, 부디 토성이 무너지지 않도록 최대한 힘써 주십시오.”

“물론입죠.”

진위경의 당부에, 늙은 목수가 구수한 어투로 대답했다.

짧은 대화를 나누는 두 사람의 주위에는 지금 이 순간에도 수많은 사람들이 각자 맡은 임무에 따라 움직이고 있었다.

그들의 면면은 다양했다.

소속된 문파 명이 새겨진 무복(武服)을 걸친 무림인들은 쉼 없이 병장기와 여러 무거운 자재를 실어 나르고, 관복 차림의 관군들은 여러 장수의 명령에 따라 일사불란하게 움직인다.

그러나 진위경의 시선은, 소속을 알아볼 수 없을 만큼 제각각 다른 차림새로 작업에 매진하는 또 다른 이들을 향하고 있었다.

“셋 하면 당겨!”

“하나, 두울!”

“흐아아압!”

흙먼지를 뒤집어쓴 채, 연신 구슬땀을 흘리며 고된 노동을 이어 가는 사내들.

“이 화살들은 어디에 놓죠?”

“기름, 기름은 여기로 가져와요!”

전투에 필요한 여러 물건들을 옮기고, 간단한 요깃거리를 준비하는 여인들.

무려 수천여 명에 이르는 양민들을 바라보는 진위경은 가슴 한구석이 먹먹해지는 것을 느꼈다.

‘최대한 멀리 피신하라 했거늘.’

몇 번이나 진심을 다해 경고했다. 그리고 설득했다.

이건 단순히 무림인들 간의 분쟁이 아니라고.

수많은 목숨을 앗아 갈 참혹한 전쟁이며, 힘없는 그대들이 가장 큰 피해를 입을 것이라고.

하지만 이미 마음을 정한 이들은 끝끝내 떠나지 않았다.

곧 피바람이 휘몰아칠 전장으로 나와서까지 그들을 돕고 있었다.

눈앞의 늙은 목수처럼.

“우리 소가주님께서 고민이 많으신가 봅니다그려.”

진태경을 곁눈질하던 늙은 목수가 허허 웃었다.

몇 해 전 칠순을 넘겼다는 그가 소리 내어 웃자 절반밖에 남지 않은 이빨들 사이로 바람 소리가 새어 나왔다.

“신경 쓰실 것 없습니다요. 이 늙은이도 그렇고, 저 사람들도 나름대로 각오하고 온 것이니.”

“아무리 그래도…… 어찌 걱정이 안 되겠습니까.”

“어이고, 부디 말씀 낮추십시오. 제가 살날이 얼마 남지 않은 늙은이라지만, 소가주님께 존대를 받을 정도로 염치 없진 않습니다.”

늙은 목수가 황급히 손을 내저었다. 진위경을 바라보는 그의 회백색 눈동자에는 따뜻한 온기가 서려 있었다.

“말 못 하는 짐승도 은혜를 입으면 언젠가는 반드시 보답하는 법입니다. 하물며 사람이라면 어찌 이런 상황을 외면할 수 있겠습니까요.”

“그게 무슨…….”

“이 늙은이가 한창 펄펄 날아다닐 때, 나라에 망조가 들었는지 마교인지 마구니인지 하는 잡것들이 사방을 들쑤시더니, 곧장 흉년(凶年)이 몇 해나 이어졌지요.”

오래전의 이야기다.

진위경이 세상에 태어나기도 전에 있었던.

하지만 늙은 목수는 똑똑히 기억하고 있었다. 가죽을 삶아 먹고, 나무껍질을 벗겨 씹던 그 시절을.

모두가 굶주렸기에 누군가의 도움을 바랄 수도 없었고, 도울 수도 없었던 시기.

만약 뙤약볕이 내리쬐던 어느 날, 마을을 찾아온 한 무리의 사내들이 아니었다면 그와 가족들은 얼마 지나지 않아 굶어 죽고 말았을 것이다.



‘여기가 홍가촌인가?’

‘마, 맞습니다만. 어쩐 일로…….’

‘후우. 다행히 제대로 찾았군.’



알곡 하나 나지 않는 논밭을 일구어서 무엇 한단 말인가.

이미 황폐한 땅을 버리고 산속으로 들어가 화전민이 된 지 오래.

그렇기에 처음에는 도적인 줄 알았다.

혹은 철전 하나, 알곡 한 움큼 없는 그들의 마지막 고혈을 쥐어짜기 위해 높으신 분이 보낸 장정들인 줄 알았다.

그렇지 않고서야 이 깊은 산속까지 찾아올 이유가 없으니까.

그러나 그들은 허리춤에 찬 검을 뽑는 대신, 제각각 짊어지고 있던 것을 내려놓았다.

그건 커다란 자루였다.

언제 마지막으로 보았는지 기억조차 흐릿한, 곡식과 고기가 한가득 담겨 있던 수십여 개의 자루들.



‘이, 이게 도대체…….’

‘줄 서게. 차례대로 나눠 줄 테니.’



꿈을 꾸는 것 같았다.

사내들의 말에 따라 마을 사람 모두가 함께 줄을 설 때도, 며칠 동안 힘없이 쓰러져 있던 아내와 아이들이 배가 터지도록 먹는 것을 지켜볼 때도.

그리고 그 믿을 수 없는 광경을 멍하니 바라보다 따뜻한 고깃국물을 한 모금 삼켰을 때, 비로소 이 모든 것이 현실이라는 것을 깨달았다.

그래서 그는 울었다.

아니, 모두가 울었다.

그들은 소리 내어 울면서도 입안에 든 것을 씹고 삼켰다.

살고 싶어서. 살아 있다는 것을 확인하고 싶어서.

“아마 그날의 도움이 없었더라면, 이 늙은이와 식구들은 그곳에서 굶어 죽었을 겁니다요.”

늙은 목수가 물기 어린 눈으로 진위경을 바라보았다. 과거와 달리 그의 입가에는 환한 미소가 맺혀 있었다.

“한데 그 고마우신 분들이 일언반구도 없이 떠나시려 하지 뭡니까. 해서 그중 한 분의 다리를 붙잡고 매달렸습니다.”

까막눈이라 의복에 적힌 글자도 몰랐다.

그래서 도대체 어디서 오셨냐고. 존함 석 자만 알려 달라고 악착같이 매달렸다.

그리고 한창의 실랑이 끝에, 원했던 대답을 들을 수 있었다.

“그때부터였습니다. 태원진가를 위해서라면, 언젠가 이 하잘것없는 목숨을 바치겠노라 다짐했던 것이.”

“……!”

“이 늙은이뿐만이 아닙니다. 이들 모두가 태원진가의 크고 작은 도움을 받았습니다.”

은혜를 입은 자들 중 더러는 떠났고, 더러는 남았다.

그리고 남은 자들은 목숨을 바칠 각오가 되어 있었다.

자신의 아버지가, 어머니가, 자신들이 살아온 이 땅을 지키기 위해.

지쳐 쓰러져 죽음을 기다리던 어느 날 도움의 손길을 내민 태원진가를 위해.

그것이 태원진가가, 흥망성쇠를 반복하며 삼백 년이라는 긴 시간 동안 이어진 명가(名家)가 지닌 진정한 힘이었다.

‘아.’

진위경은 가슴 한구석이 욱신거리는 것을 느꼈다.

어쩌면 태원진가를, 산서성을 가장 과소평가했던 것은 자신이었을지 모른다는 생각과 함께.

그리고 진위경이 붉어진 눈가를 감추기 위해 고개를 돌린 그때였다.

두두두두!

먼 거리임에도 똑똑히 들을 수 있는, 맹렬한 말발굽 소리.

무언가에 쫓기듯 협곡을 가로지르는 한 마리의 준마에 매달려 있는 것은, 눈을 부릅뜬 채 죽어 있는 태원진가의 무인이었다.

“……!”

“……!”

삽시간에 얼어붙은 공기 속, 진위경이 피를 토하듯 부르짖었다.

“전원, 전투 준비!”

놈들이 왔다.
```

## Final English reading copy

```markdown
# Chapter 953

When dozens or hundreds of people fought tangled together, it was a battle.

But when the numbers grew to thousands, tens of thousands, it could no longer be called a battle.

It was war.

A war in which both sides clashed with all their might, each staking everything they had.

And Jin Wikyung had not the slightest intention of gambling everything he had on a single throw.

“Commander of the Heaven Shaking Squad, Jin Mukyung. I report to the Lesser Family Head.”

His voice was calm, but his whole body was soaked in blood.

Jin Mukyung had left at noon and returned only around midnight. He looked like nothing so much as a blood demon.

So did his men, whose squad took its name from his epithet, the Heaven Shaking Sword.

But their proud strides and blazing eyes were proof of the Jin Family of Taiyuan’s first victory.

“Under your strict orders, I broke the enemy’s vanguard and returned.”

Jin Mukyung continued, unhurried.

Of the slightly more than two hundred men in the Heaven Shaking Squad, twenty-three had died and thirty-seven had suffered injuries, both serious and minor.

At the news that a single battle had left sixty casualties among the elite fighting force the Jin Family of Taiyuan had devoted itself to cultivating alongside the Jin Dragon Squad, several of the senior leaders grew somber. But the report that followed washed away even that brief sadness.

A thousand.

They had annihilated the enemy vanguard, five times their number.

And that included a hundred of the enemy’s elite troops.

“Waaaah!”

The people who had been listening in tense silence all let out a cheer at once.

Their first victory against the enemy.

And not just a victory, but an overwhelming one beyond any dispute.

Yet even as the air grew hot with excitement, Jin Wikyung kept his composure amid the celebrations.

*This is only the beginning.*

He knew it.

War was like building a sandcastle. You had to keep scooping up sand and piling it on, again and again, before it was complete.

And even a sandcastle painstakingly built that way could collapse from a single hard kick.

*But if we build it solidly enough that it won’t collapse even when kicked, that changes things.*

Fortunately, the Jin Family of Taiyuan’s preparations had been thorough enough to make the limited time they’d had seem irrelevant.

By now, the grassland army—likely crossing the Great Wall and passing through northern Shanxi Province—must have been bewildered.

First, by the news that its vanguard, which included its finest troops, had been wiped out.

Then again, by the situation in the north, which had truly been left *empty*.

*You won’t find a thing to take in the north.*

It wasn’t only the people who had left the north.

Jin Wikyung had pulled all the troops and commoners back from the north. He had also ordered every field—on the verge of harvest—to be burned.

A scorched-earth strategy.

Naturally, it was an excellent tactic against a huge army numbering in the tens of thousands. But Jin Wikyung had agonized over the decision dozens of times before making it.

That was, until Assistant Military Commissioner Li Feng of Shanxi Province and several hundred people came to him first.

*“We have several tens of thousands of seok of provisions in reserve. We can more than handle their food supply.”*

Li Feng, who could be considered the most senior official actually present at the Shanxi Provincial Office in the absence of Zhu Bao and Hong Jin, promised his full cooperation.

*“Just burn the whole damn lot.”*

The northern villagers, forced to leave their homes overnight—or rather, the village headmen—were already half blind with rage.

*“Those damn bastards. They’ve been storming in and raising hell all the time, and now they’ve come to take our fields, too?”*

*“Everyone in our village has already agreed. If even one grain of rice gets into those barbarian bastards’ mouths, I’ll be torn to pieces.”*

*“I’d sooner feed rice to pigs and cows. I wouldn’t stand for that even after I’m dead!”*

*“Shit. If anyone objects, step forward now. I don’t know who you are, but if you so much as open your mouth, I’ll call you a barbarian and shave your head clean so I can give you a queue!”*

*“Hey, you, Mr. Song! Why aren’t you saying anything? You got honey on those fields?”*

And the village headman, Mr. Song, who had stayed silent without saying a word, earned a round of applause from everyone with just one suggestion.

*“Don’t just set fires. Let’s poison the wells.”*

*“……!”*

*“It’d be even better if we took a dump and pissed in the stream before we left.”*

*“Why the piss and shit, too?”*

*“It’ll dirty the water. You think those bastards will be fine after gulping down water mixed with shit and piss?”*

*“Good heavens! How could anyone come up with such a brilliant plan…!”*

*“I tried it once. Drank nearly half a gallon of the stuff. Thought I was going to die.”*

Mr. Song, a farmer with the unusual distinction of having drunk sewage, became a hero overnight. As people shoved poisonous weeds into the wells and shat and pissed by the streams, they wondered why he hadn’t placed first in the civil service exams.

All while saying that the only good barbarian was a dead one—words that would have shocked someone if they’d heard them.

*The road here won’t be easy.*

Jin Wikyung wore a cold smile.

Shanxi Province was undeniably a frontier.

It produced plenty of grain, but it was neither as developed as the Central Plains nor as powerful.

But for that very reason, when crisis came, its people could come together all the more strongly.

The long years of raids by mounted bandits and nomads had instilled a fierce resolve in the people of Shanxi. Now that resolve had caught fire.

*We will protect it. No matter what.*

Jin Wikyung had already made up his mind.

He had given up sleep and rest, devoting himself to everything at hand. He sent swift-footed subordinates to survey the situation in the north and organized small detachments to watch for any unexpected division of enemy forces.

He had personally ordered traps and iron caltrops set along every detour except Jeongyang, and checked on the progress of the work himself. All of it was part of the same effort.

“How is the earthen fort coming along?”

“Taking the reinforcement work into account, it should be finished within half a day at the latest.”

Eight Spring Gorge.

At the end of this vase-shaped gorge, which had swallowed countless lives from the Great Faction War to the present, five new towers now rose where none had stood before.

Made from a mixture of mud, wood, and stone, each stood three *jang* high and had a flat area large enough to accommodate a little over two hundred people.

Two hundred archers, to be exact.

“Taking the heights above the gorge isn’t enough. These forts are essential to our victory. Please do everything you can to make sure they don’t collapse.”

“Of course, sir.”

The old carpenter answered in a folksy drawl.

Even as the two exchanged a few brief words, countless people around them went about their assigned tasks.

They were a diverse lot.

Martial artists in uniforms embroidered with the names of their sects tirelessly hauled weapons and heavy materials. Government troops in official uniforms moved in orderly formation at the commands of their officers.

But Jin Wikyung’s gaze was fixed on another group, each dressed so differently that their affiliations were impossible to make out, all hard at work.

“On three, pull!”

“One, two!”

“Hyaah!”

The men, covered in dust, labored on, sweat streaming off them.

“Where should we put these arrows?”

“Oil! Bring the oil over here!”

The women carried supplies needed for battle and prepared simple meals.

As Jin Wikyung looked at the several thousand commoners, he felt a tightness in his chest.

*I told them to flee as far away as they could.*

He had warned them in all sincerity, over and over. He had tried to persuade them.

This wasn’t just a dispute among martial artists.

It was a brutal war that would claim countless lives, and they—the powerless—would suffer the most.

But the people who had already made up their minds had refused to leave to the very end.

They had come here to help, even onto a battlefield about to be swept by a storm of bloodshed.

Like the old carpenter standing before him.

“Looks like our Lesser Family Head has a lot on his mind.”

The old carpenter, who had been glancing sideways at Jin Taekyung, chuckled.

He said he had turned seventy several years ago. As he laughed out loud, air whistled through the gaps between the few teeth he had left.

“Don’t you worry about it. This old man and all those folks out there came prepared.”

“But still… how could I not worry?”

“Goodness, please don’t speak so formally to me. I may be an old man with little time left, but I’m not shameless enough to expect the Lesser Family Head to address me with honorifics.”

The old carpenter hurriedly waved his hands. Warmth shone in his pale gray eyes as he looked at Jin Wikyung.

“Even a beast that can’t speak repays a kindness someday. How could a person turn away from a situation like this?”

“What do you mean by that…?”

“When I was young and in my prime, the country must have been nearing its end. The Demonic Cult, or demons, or whatever those wretches were, stirred up trouble all over the place, and then years of bad harvests followed.”

It had happened a long time ago.

Before Jin Wikyung was even born.

But the old carpenter remembered it clearly. The days when they boiled and ate leather, and stripped bark from trees to chew.

Everyone was starving, so there was no one to turn to for help—and no one who could help.

If a group of men hadn’t come to their village one scorching day, he and his family would have starved to death before long.

*“Is this Hong Family Village?”*

*“Y-yes, it is. What brings you here…?”*

*“Phew. Thank goodness we found the right place.”*

What was the point of tilling fields that yielded not a single grain?

They had abandoned the already barren land long ago, gone into the mountains, and become slash-and-burn farmers.

So at first, they’d thought the newcomers were bandits.

Or strongmen sent by some powerful official to squeeze the last bit of blood from them, when they didn’t have a single iron coin or handful of grain left.

Otherwise, there would have been no reason to come all the way into these deep mountains.

But instead of drawing the swords at their waists, the men set down the loads they had been carrying.

They were huge sacks.

Dozens of them, filled to the brim with grain and meat—the kind of sight they could barely remember ever seeing.

*“W-what in the world is this…?”*

*“Get in line. We’ll hand it out one by one.”*

It felt like a dream.

When every villager lined up together at the men’s direction, and when he watched his wife and children—who had been lying weak and helpless for days—eat until their bellies nearly burst.

And then, when he had stared blankly at that unbelievable sight and swallowed a mouthful of warm meat broth, only then did he realize it was all real.

So he cried.

No—everyone cried.

They wept aloud even as they chewed and swallowed what was in their mouths.

Because they wanted to live. Because they wanted to make sure they were alive.

“If we hadn’t received help that day, this old man and my family would have starved to death right there.”

The old carpenter looked at Jin Wikyung with tear-bright eyes. Unlike back then, a radiant smile now rested on his lips.

“But those kind people were about to leave without saying a word. So I grabbed one of them by the leg and clung on.”

He couldn’t read, not even the characters written on their clothes.

So he’d clung on stubbornly, asking where they were from and begging them to tell him their three-character names.

After a long struggle, he finally heard the answer he wanted.

“From that day on, I vowed that if the Jin Family of Taiyuan ever needed it, I would give this worthless life of mine.”

“……!”

“And it’s not just me. Every one of these people has received help from the Jin Family of Taiyuan, in one way or another.”

Some of those who had received their kindness left. Others stayed.

And those who stayed were ready to lay down their lives.

To protect the land where their fathers and mothers—and they themselves—had lived.

To repay the Jin Family of Taiyuan, who had reached out to help them on the day they had lain exhausted, waiting to die.

That was the Jin Family of Taiyuan’s true strength: the strength of a distinguished family that had endured for three hundred years through the rise and fall of fortune.

*Ah.*

Jin Wikyung felt an ache deep in his chest.

He wondered if he himself had been the one to underestimate the Jin Family of Taiyuan—and Shanxi Province—most of all.

And just as Jin Wikyung turned away to hide his reddened eyes—

*Thududududu!*

A fierce pounding of hooves, clear even from a great distance.

A single fine horse raced across the gorge as if fleeing something. Hanging from its back was a martial artist of the Jin Family of Taiyuan, dead with his eyes wide open.

“……!”

“……!”

The air froze in an instant. Jin Wikyung shouted as if spitting blood.

“Everyone, prepare for battle!”

They were here.
```
