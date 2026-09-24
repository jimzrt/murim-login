<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0952.txt",
      "sha256": "e8337132e57a6d55b375af401336277692201d05dc47a9e7ce950b6b0927f704",
      "bytes": 12909
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b83af320a763dee3187dd9c67e937ae7b351beee460ef4972e84081916228756",
      "bytes": 2820
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "24305d1c9dc05d1f447a15c73fed9c251ab1fd23035f65c1d6eee6786b6d41c1",
      "bytes": 234031
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "831d36ae338d9763d65155ad066f7fcb225932c1844daf68acf37f01a734dec6",
      "bytes": 1325
    },
    {
      "path": "characters/Chinggen.md",
      "sha256": "ccc8a23e49a3b2cd3eb3fc1b9a4eabcf8e59afa5fcbf37e8e1fdc9146e9b0c3c",
      "bytes": 598
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "05159d9e749de0e824b32b7bc71b58dd1a8d7d4956b5a598b478d65ee7717d54",
      "bytes": 759
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "876b4a89c1bd9d04fbe2a5c04074c236be5e19f8fdcbedbebd8dea06d0dc98b3",
      "bytes": 667
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "3c3929f4f488029e3e8b0b5364a7e7b38ecd7bf94023128c5792f8b9de66bd4c",
      "bytes": 1497
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "f61af9c1ac6ea3e6e230d1b8a351d6da0994371477a94863ca018b869f94f579",
      "bytes": 1449
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "7607c3a047f59ee5f56be8675ec962c77466a175ed94fd08baac779ebbfa4a77",
      "bytes": 1282
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "9119b3427e209d4298d63393c8cfa62c18ee383c385510f25fb1cbb5e2adce4c",
      "bytes": 622
    },
    {
      "path": "characters/Li Feng.md",
      "sha256": "97c5c9d3715266a6bc2bf6adf52c3f57d4676f7530306d60c5bee88630145dbc",
      "bytes": 888
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "557f88f23c5c70b5e7cb3e7a5464328fca4e180d5a5d17eeefa764325af00fdc",
      "bytes": 267731
    }
  ],
  "estimated_tokens": 12688
}
-->

# Durable State Update — Chapter 952

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
1 and safe_through 952. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 952. Profile updates may replace only one
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
  "chapter": 952,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 952,
    "continuity_sources": [952],
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
    "War with Dark Heaven is imminent. The Jin Family of Taiyuan and Shanxi forces are preparing a stand at Eight Spring Gorge against an estimated thirty to forty thousand advancing enemies.",
    "The Hebei Peng Family, Murong Family, Huashan, and Zhongnan Sect are each sending two thousand reinforcements to Shanxi; two thousand martial artists have departed the Murim Alliance headquarters for the north.",
    "The improved Temporary Strength Pill may be spreading through Murim and may create a dangerous drive for strength; its effects and distribution network remain unknown.",
    "Jang Sam abruptly rose from Level 40 to Level 60, attacked Taekyung while apparently irrational, and is unconscious; his silk pouch from an unknown traveler in Hubei may have contained a modified Temporary Strength Pill.",
    "The Bow Saint wondered whether Pung Yang might have been the chosen one; the Martial God’s identity and connection to the chosen one and the Bow Saint remain unknown.",
    "The Eastern Heaven Demon Lord’s hidden iron chest contained old bamboo slips, recent papers, and a small silk pouch of unknown significance.",
    "The real Chinggen was killed in the attack on the khans’ gathering; an impostor wearing his face has manipulated Temur into gathering tribespeople.",
    "Jamukha has joined the steppe army with more than twenty thousand tribespeople and a thousand Keshik; the army expects to cross the Shanxi border in about a day, before the Fire King and Taekyung arrive."
  ],
  "continuity_sources": [
    950,
    951
  ],
  "open_questions": [
    "What will happen in the Shanxi campaign, and what role will Dark Heaven play in the fighting?",
    "Who gave Jang Sam the silk pouch, and what are the modified pill’s effects and side effects?",
    "How widely has the improved Temporary Strength Pill spread, and who is distributing it?",
    "What is the Martial God’s identity, and what is his connection to the chosen one and the Bow Saint?",
    "What do the Eastern Heaven Demon Lord’s papers and silk pouch contain, and what is their significance?"
  ],
  "safe_through": 951,
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
| 청풍     | **Cheongpung**     |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 화산파    | **Huashan**                      |
| 천무학관   | **Heaven's Gate Temple**         |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 신법     | **movement technique**                           |                                                       |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 대주     | **Squad Leader** / **Commander**             |
| 제자     | **Disciple**                                 |
| 생도     | **cadet**                                    |
| 상태               | **Status**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 화산     | **Huashan**            |
| 본가      | **our family / this family**                                    |
| 공자      | **Young Master**                                                |
| 칭겐 | **Chinggen** | Northern Gaoyuan chieftain commanding one hundred tribespeople; restrains Temur. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 이풍 | **Li Feng** | Shanxi Province's Assistant Military Commissioner; former Huashan lay disciple |
| 정양 | **Jeongyang** | Shanxi location |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 강남 | **Gangnam** | Formerly valuable Seoul-area real estate. |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 벽곡단 | **fasting pills** | Food-substitute pills found in the hidden cave where Cheol trained. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 구주 | **Nine Provinces** | Traditional geographic expression used in a threat. |
| 도지휘첨사 | **Assistant Military Commissioner** | Military office held by the unnamed official responsible for training soldiers. |
| 산서성부 | **Shanxi Provincial Office** | Government office where the City Lord resides west of Taiyuan. |
| 구주팔황 | **Nine Provinces and Eight Wastes** | Literary geographic phrase appearing in a wuxia novel title. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 사해오호 | **Four Seas and Five Lakes** | Traditional geographic phrase used with the Nine Provinces and Eight Wastes. |
| 수련동 | **training hall** | Building located roughly two hundred jang from the training ground. |
| 성라대연 | **Star-Array Grand Banquet** | Major martial gathering held in Henan every two or three years. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 화주 | **strong liquor** | Liquor stored and consumed by the dark-path swordsmen. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 탈진 | **Exhaustion** | System status effect caused by exhausting all internal energy while severely injured. |
| 한나절 | **half a day** | Elapsed duration in Jeok's first time-loss episode. |
| 황하 | **Yellow River** | River along which civilization began. |
| 중양절 | **Double Ninth Festival** | Festival used as the expected date for the invasion of the Central Plains. |
| 자무카 | **Jamukha** | Khan of the western grasslands and the steppe army’s practical leader. |
| 케식 | **Keshik** | Elite warriors serving the Golden Clan. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 이풍 | 진태경 | senior_official_to_respected_young_martial_artist | Young Hero Jin | formal and respectful | Addresses Taekyung as 진 소협 after praising his reputation. |
| 이풍 | 청풍 | Huashan lay disciple to martial uncle | Young Hero; Martial Uncle Cheongpung | formal and reverent | Li Feng initially addresses Cheongpung as 소협 while testing his knowledge, then recognizes him as 사숙 after witnessing his Huashan sword technique. |
| 청풍 | 이풍 | Martial Uncle to Martial Nephew | Martial Nephew Li Feng | exuberant and deferential | Cheongpung adopts the address to obtain royal-guard armor and weapons. |
| 진태경 | 이풍 | junior_to_respected_official_and_martial_ally | Great Hero Li | polite and respectful | Agrees with Li Feng's proposal that Zhu Bao visit the Jin Family's banquet. |
| 청풍 | 진무경 | young_martial_artist_to_renowned_senior_martial_artist | Young Hero Jin Mukyung | deferential and excited | Cheongpung calls him 진천검 진무경 소협 and later 진 소협 while seeking his duel. |
| 진무경 | 청풍 | senior_martial_artist_to_newly_met_young_martial_artist | Young Hero | deferential and expectant | Mukyung addresses Cheongpung as 소협 while asking whether Great Hero Mae descended from Huashan. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진위경 | 막내 | older brother to younger brother | my youngest | intimate and informal | Jin Wikyung uses 막내야 affectionately for Jin Taekyung. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 가솔 | 진태경 | Zhuge Clan retainer to Great Hero | Great Hero Jin | polite and pleading | Uses 진 대협 while urging Taekyung to stop provoking Ju Wongong. |
| 진위경 | 청풍 | Jin Family Lesser Family Head to young martial companion | Young Hero Cheongpung | formal-polite | Uses 청 소협 while summoning Cheongpung to the Alliance Leader's Hall. |
| 칭겐 | 자무카 | fellow_khan_to_elder_khan | Khan Jamukha | formal-respectful | The impostor wearing Chinggen’s face addresses Jamukha with deference. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 946
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak martial master known as the Huashan Divine Dragon, the creator of the snake-inspired Mimi Step footwork technique, and the master of the Azure Dragon Pavilion within the Alliance Leader's Two Dragons Pavilion.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi, now a large horned snake, to him, and Cheongpung is accompanying Mungyeong while learning his martial arts through observation to become stronger and adapt to this world.

### Chinggen.md

# Chinggen (칭겐)

- **Safe through:** Chapter 951
- **Aliases:** None
- **Role:** The real Chinggen was a Khan of the eastern grasslands and Temur’s brother, but he was killed in the attack on their gathering; an impostor now wears his face.
- **Personality:** Prudent, restrained, and attentive to the danger posed by the gathering's other powers
- **Voice:** Measured, familiar, and cautioning
- **Relationships:** Temur was Chinggen’s brother and fellow Khan; an impostor wearing Chinggen’s face now manipulates Temur.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 951
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 947
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 927
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Jin Mukyung is the second son of the Jin Family of Taiyuan, a twenty-three-year-old cadet at Heaven’s Gate Temple, and a young Peak-level genius swordsman who has remained secluded in the training hall for more than a year after losing to Cheongpung and refuses to emerge until he achieves a great accomplishment.
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away; three years earlier, he flatly refused seven-year-old Zhu Bao’s request for an autograph

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 951
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor has appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 949
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm and politically capable, Jin Wikyung takes responsibility for his people and prioritizes their lives, but carries self-blame for past losses and can falter under the weight of a decision before resolving to act.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Jin Wikyung is Taekyung's eldest brother and future Family Head who protects and mentors him, commands Wipeng and the Jin Family's forces, has worked with Jeok Cheongang, maintains a political connection with Hongcheon, Prince Shangshan's hidden loyal retainer, and wants Taekyung to tell him his untold stories when the current crisis is over; Jin Mukyung is his younger brother and a potential successor alongside Taekyung.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 951
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Li Feng.md

# Li Feng (이풍)

- **Safe through:** Chapter 876
- **Aliases:** None
- **Role:** Assistant Military Commissioner of Shanxi Province; former Huashan lay disciple who left the sect nearly ten years ago
- **Personality:** Resolute, proud, blunt, and hostile toward political and martial rivals
- **Voice:** Formal and restrained in official settings; dry and cutting with opponents
- **Relationships:** Former lay disciple of Huashan; visited the hidden residence of his Grandmaster Mae Jonghak and saw ten-year-old Cheongpung there; recognizes Cheongpung as his Martial Uncle; direct subordinate and political rival of Hong Jin, the Deputy Military Commissioner; agrees to act as Hong Jin's intermediary with Huashan and send a messenger pigeon to his Master; bears a humiliating martial grievance involving Gong Ilhyuk

## Korean source

```text
＃952화



중양절(重陽節)은 대륙 최대의 명절 중 하나다.

제비가 따뜻한 강남을 향해 떠나고, 뱀과 개구리는 겨울잠을 준비하기 위해 땅속으로 들어가는 시기.

이 무렵 사람들은 산에 올라 국화주를 마시고 시를 읊으며 산수를 즐기고는 했다.

이는 하루 벌어 하루 먹고 사는 무지렁이 백성도, 세상 부러울 것 없는 고관대작(高官大爵)도, 풍진 강호에 몸담은 무림인도 예외는 아니었다.

“기억나느냐?”

어느 순간 등 뒤에서 불현듯 울려 퍼진 목소리.

그러나 샛노랗게 피어난 국화밭을 말없이 바라보던 청년은 조금도 당황하지 않았다.

지금 들려온 목소리의 주인이 누구인지, 그는 이미 한참 전부터 알고 있었기 때문이었다.

“무엇이 말입니까?”

여전히 국화에 시선을 고정한 채 되묻는 청년, 진무경의 옆으로 익숙한 인기척이 다가와 섰다.

“오 년 전, 우리 삼 형제가 뒷산에 올라 함께 중양절을 지냈던 것 말이다. 참 즐거웠었지.”

“……십 년 전, 중양절 말씀이십니까?”

석연치 않은 아우의 대답에 진위경이 섭섭한 표정을 지었다.

“이런, 이제는 기억조차 안 나는 게냐?”

“기억은 나는데, 제 기억과는 상당한 차이가 있는 것 같아 여쭤본 겁니다.”

“차이?”

“태경이, 그 천둥벌거숭이 같은 놈이 술에 잔뜩 취해 행패를 부렸잖습니까. 그래서인지 딱히 즐겁진 않았습니다.”

진위경이 고개를 갸웃거렸다.

“그랬느냐? 검집으로 두들겨 팰 때는 꽤 즐거워 보이던데.”

“안 웃었습니다. 단지 혈육을 올바른 길로 이끌기 위한 훈육이었을 뿐입니다.”

“그런 것치고는 입꼬리가 귀에 걸려 있던데.”

정곡을 찌르는 진위경의 한 마디에 진무경은 잠시 침묵했다.

생각해 보니 그랬던 것 같기도 하다.

사고뭉치 막내, 막내라면 그저 어화둥둥 껌뻑 죽는 형님.

이런 갑갑하기 그지없는 상황에서 명분이 생기니 어찌 웃지 않을 수 있었겠나.

물론, 이미 오래전의 일이다.

머릿속 기억의 작은 한 조각으로만 남아 있는.

“막내는 하늘이 무너진 것처럼 엉엉 울었고, 너는 음식에는 손도 대지 않은 채 수련을 시작했지. 사람들과 떨어져 숲속에서 해가 질 때까지 검을 휘두르던 네 모습이 아직도 눈에 선해.”

“그건 기억에 없지만, 분명 그랬겠지요.”

진무경은 담담하게 대꾸했다.

그에게 있어 수련은 너무나도 당연한 일이었다. 어린 시절부터 검을 들었고, 언제나 때와 장소를 가리지 않고 수련에 매진해 왔다.

태원진가의 삼형제가 마지막으로 함께 중양절을 보냈던 오 년 전, 약관 어림의 진무경은 이미 절정의 경지에 오른 고수였다.

“네가 본가를 떠나던 날은 지금도 똑똑히 기억나는구나.”

“아.”

진무경이 문득 입맛을 다셨다.

전날 밤 한바탕 울기라도 했는지, 퉁퉁 부어오른 얼굴로 배웅을 나왔던 형의 모습이 떠올라서.



‘꼭…… 꼭 가야겠느냐?’

‘예. 꼭 가야겠습니다.’

‘이 형님이 이렇게 부탁한다고 해도?’

‘택도 없습니다.’

‘아니, 그까짓 천무학관(天武學館)이 뭐길래 혈육까지 버리고 만리타향까지 떠난단 말이냐!’

‘형님이 말씀하신 그까짓 천무학관에 가려면, 명문대파의 제자들도 몇 년씩 줄을 서야 합니다.’

‘알겠다. 네 뜻이 정 그러하다면 이 형님이 직접 하남까지 바래다주마.’

‘……진심이십니까.’

‘내 관주(館主)님을 직접 찾아뵙고 드릴 말씀이 있다.’

‘아니, 도대체 무슨 말씀을 하시려고.’

‘반드시 알고 계셔야 할 중요한 주의사항만 전달할 것이다. 네가 싫어하는 몇 가지 음식들이랑 생활 습관…… 무경아, 어디 가느냐 무경아!’



튀었다. 젖 먹던 힘까지 쥐어짜서.

그토록 온 힘을 다해 경신법을 발휘한 건 정말 태어나서 처음이었다.

진무경은 천무학관에서 더욱 강해지고 싶었을 뿐, 최단기 퇴학생도라는 업적을 달성할 생각은 추호도 없었다.

“이 형님은 아직도 기억하고 있다. 터지는 울음을 감추기 위해 소매로 눈가로 가린 채 떠나던 네 뒷모습을.”

“…….”

진무경은 조용히 입을 다물었다.

때때로 어떠한 종류의 진실은 드러나지 않았을 때가 더 아름답다.

가령 먼지를 막기 위해 소매로 눈가를 가렸다든지, 극성을 부리는 형님을 피해 도망쳤다든지 하는 것 역시 마찬가지다.

그리고 순간, 자신도 모르게 실소가 터졌다.

“갑자기 왜 웃느냐?”

“아닙니다. 그냥…….”

겨우 웃음을 그친 진무경이 고개를 돌렸다.

지금으로부터 약 이 년 전, 기약 없는 폐관 수련을 위해 또다시 떠나는 자신을 걱정 가득한 눈빛으로 바라보던 한 사람의 얼굴이 시야에 담겼다.

그때 그 순간처럼.

“반가워서 웃었습니다. 변하지 않은 형님의 모습이.”

“무경이 너…….”

“다행입니다. 모든 것이 그대로라서.”

캄캄한 어둠 속에서 이 년 남짓한 시간을 보냈다.

쓰고 떫은 벽곡단(辟穀丹)으로 허기를 채웠고, 동굴 깊숙한 곳에 위치한 수련동에 고인 이슬과 빗물로 목을 축였다.

그리고 탈진할 때까지 검을 휘두르다 차가운 지면에 널브러질 때마다 문득 떠올리곤 했다.

이곳은 어디인지. 나는 누구인지.

언젠가 이 어둠을 벗어난다면, 무엇이 나를 기다리고 있을지.

“한편으로는 두렵기도 했습니다. 제가 알던 세상이, 사람들이 너무나도 달라져 있을까 봐.”

그 짐작은 반은 틀렸고, 반은 맞았다.

주위를 둘러싼 모든 것이 변했지만, 그가 알던 사람들은 그대로였다.

지금은 어디에 있는지 모를 사고뭉치 막내 녀석도, 분명 그럴 것이다.

“녀석이 가문을 떠나던 날, 저를 찾아와 그런 말을 하더군요.”

수천 번. 아니 수만 번을 곱씹었던 대화다.

평소와는 달리 담담하기 그지없던 진태경의 목소리는 지금 이 순간에도 그의 귓가에 맴돌고 있었다.

“나중에 보자, 라고.”

그것은 그저 단순한 인사가 아니었다.

성라대연(星羅大宴).

구주팔황과 사해오호를 수놓은 무수한 별들의 연회에서 만나, 청풍과 함께 겨뤄 보자는 도발이자 도전장이기도 했다.

한 배에서 태어난 형제로서. 한 사람의 무인으로서.

그리고 아우가 떠난 빈자리를 우두커니 지켜보던 진무경은 미처 건네지 못한 대답을 홀로 뇌까렸댔다.

‘그래, 나중에 보자. 반드시.’

하지만 그 약속은 지켜지지 못했다.

시간의 흐름조차 느껴지지 않는 그곳에서 진무경은 쉼 없이 검을 휘둘렀다. 칠흑 같은 어둠 속 너머를 베고, 찌르고, 찢어발겼다.

새로운 것에 눈을 뜰 때마다 또 다른 벽이 앞을 가로막았다.

넘어야 했다. 부숴야 했다.

지키지 못한 약속을 가슴 한구석에 품고 진무경은 계속해서 정진했다.

어둠 속에서 흐릿한 빛을 발견할 때까지.

그 빛이 태양처럼 선명해질 때까지.

그리고 마침내 세상으로 나왔다.

이 년간 그를 휘감았던 어둠을 뒤로한 채, 또 다른 어둠으로 가득 찬 세상으로.

“형님.”

진무경은 나직한 부름과 함께 자신의 혈육을 똑바로 응시했다.

빛이 담긴 두 눈동자로.

보는 이로 하여금 거짓을 말할 수 없는 올곧은 눈빛으로.

“이제 말해 주십시오. 제가 해야 할 일을.”

“……!”

“아니, 명령하십시오. 태원진가의 소가주로서.”

순간, 진위경의 눈동자가 파르르 떨렸다.

“알고…… 있었느냐.”

진무경이 조용히 고개를 끄덕였다.

지금의 태원진가는, 그리고 행방이 묘연한 가주를 대신해 그들 모두를 이끄는 진위경은 산서 무림의 맹주(盟主).

이미 산서성은 전시(戰時) 상태다.

화산파의 속가이자 산서성 도지휘첨사인 이풍은 산서성부의 모든 전력을 동원하여 북부의 백성들을 대피시켰고, 오천 남짓의 무림인들은 중부에 집결했다.

그야말로 일각이 아쉬운 상황.

이런 와중에 진위경이 자신을 찾은 것은, 단지 이 년 만에 세상 밖으로 나온 아우와 해후를 나누고 싶었던 마음뿐만은 아니었으리라.

“형님이 저를 잘 알고 있듯이, 소제(小弟) 역시 마찬가지입니다.”

“……위험한 임무가 될 것이다.”

“상관없습니다.”

진무경은 담담하게 말을 이었다.

“제가 무공을 익힌 것은 그저 검이 좋아서였으나, 강해지고자 한 것은 가문을 위해서였으니.”

몰락한 무가(武家)를 일으켜 세우는 것은 강한 힘뿐이다.

지금껏 진무경이 휘두르는 검신에 실려있던 것은 무(武), 그 자체를 향한 열망뿐만이 아니었다.

“태원진가의 이공자 진무경. 성심을 다해 소가주의 명을 받들겠습니다.”

흔들림 없는 목소리와 함께 포권을 취하는 아우의 모습에, 진위경은 지그시 눈을 감았다.

그리고 짧은 망설임 끝에 눈을 떴을 때, 그는 어느덧 산서 무림의 맹주이자 태원진가의 소가주가 되어 있었다.

“지금부터 너는 태원진가의 이공자도, 소가주의 아우도 아니다.”

참았던 숨과 함께 토해진 한 마디.

진위경은 침착한 눈빛으로 자신의 아우를, 아니 가솔을 바라보며 말을 이었다.

“진천대주(振天隊主) 진무경에게 명한다.”

진천검(振天劍) 진무경.

지금으로부터 약 오 년 전. 약관의 나이에 절정의 경지에 오른 변방의 후기지수는 새로운 별호를 얻었고, 그의 하나뿐인 형은 아우의 별호를 딴 무력대를 만들었다.

언젠가 자신의 아우가 이 자리에 돌아오길 바라는 마음에서.

진천이라는 두 글자에 담긴 뜻처럼, 언젠가 그 이름이 천하를 넘어 하늘에까지 떨쳐 울리길 소망하며.

“북부를 침탈한 적들의 선봉대가 일부 병력을 분산, 정양(定壤)을 피하여 우회하고 있다. 진천대 이백으로 놈들의 예봉(銳鋒)을 꺾어라.”

진무경이 웃으며 대답했다.

“존명(尊命).”



* * *



다음 날.

아무런 저항 없이 북부에 발을 디딘 초원의 대군세를 기다리고 있던 것은, 국화 대신 산자락을 뒤덮은 검붉은 핏물과 공포에 질린 선봉대의 생존자였다.

“카, 칸이시여.”

사시나무처럼 벌벌 떨고 있는 그를 물끄러미 바라보던 자무카는 직감했다.

본대보다 한나절 앞서 산서성을 침범한 일천의 선봉대가, 모조리 전멸당했다는 것을.

그리고 유일하게 살아남은 눈앞의 얼간이가 가져온 것은, 침략자를 향한 강력한 경고라는 것을.

“노, 놈이 이것을 칸께 전해 드리라고…….”

스륵, 툭.

파르르 떨리는 손끝으로 붙잡고 있던 천 자락이 미끄러진다.

핏물에 흠뻑 젖은 그것 사이로 굴러떨어진 케식 백인장의 목을 말없이 응시하던 자무카가 입을 열었다.

“이것이 전부냐.”

“전언(傳言)을, 전언을 남겼습니다.”

변발이 풀어 헤쳐진 생존자가 공포에 질린 얼굴로 말을 이었다.

“오 년 후에도, 우리 형제는 함께 산에 올라 중양절을 보낼…….”

“개소리군.”

서걱.

한 치의 망설임도 없는 손속.

살과 뼈가 분리된 머리가 국화밭에 굴러떨어진다.

이제는 더 이상 본래의 색을 찾아볼 수 없는 붉은 꽃밭을 바라보던 자무카의 모습에, 칭겐이 입맛을 다셨다.

“끝까지 들어 보지 그러셨습니까. 놈이 누구인지도 모르는데.”

“그것이 중요한가?”

중요한 건 일천의 선봉대가 궤멸했다는 것이다.

아니, 단 한 번의 전투로 그 선봉대에 포함되어 있던 일백의 케식이 죽었다는 것만이 중요했다.

“어차피…… 곧 만나게 되겠지.”

자무카가 깊게 가라앉은 목소리로 남쪽을 응시했다.

지금 이 순간, 그의 뇌리에는 문득 어떠한 생각이 스쳐 지나가고 있었다.

압도적이면서도 일방적이어야 할 이 전쟁이, 생각만큼 쉽지 않을 것이라는 생각이.
```

## Final English reading copy

```markdown
# Chapter 952

The Double Ninth Festival was one of the continent’s biggest holidays.

It was the time of year when the swallows left for the warmer south, and snakes and frogs burrowed underground to prepare for hibernation.

Around this time, people would climb mountains, drink chrysanthemum wine, recite poetry, and enjoy the scenery.

That was true of everyone, from commoners who lived from one day’s wages to the next, to high-ranking officials who wanted for nothing, to martial artists who had made their home in the turbulent martial world.

“Do you remember?”

A voice suddenly rang out behind him.

But the young man, silently gazing at the field of bright yellow chrysanthemums, wasn’t startled at all.

He had known for some time who the voice belonged to.

“Remember what?”

The young man, Jin Mukyung, asked without taking his eyes off the flowers. A familiar presence approached and came to stand beside him.

“Five years ago, when the three of us brothers climbed the hill behind the house and spent the Double Ninth Festival together. We had a wonderful time.”

“…You mean the Double Ninth Festival ten years ago?”

At his younger brother’s doubtful response, Jin Wikyung looked hurt.

“Goodness. You don’t even remember anymore?”

“I remember. I only ask because it seems quite different from what I remember.”

“Different?”

“Taekyung, that reckless fool, got completely drunk and caused a scene. It wasn’t exactly a pleasant time.”

Jin Wikyung tilted his head.

“Is that so? You looked like you were having a pretty good time when you were beating him with your scabbard.”

“I wasn’t smiling. I was simply disciplining my own flesh and blood to guide him onto the right path.”

“For someone who wasn’t smiling, the corners of your mouth were practically up to your ears.”

Jin Mukyung fell silent for a moment at Jin Wikyung’s spot-on remark.

Come to think of it, perhaps he had been smiling.

A troublemaking youngest brother, and an older brother who doted on him to no end.

How could he not smile when, in this unbearably frustrating situation, he’d been given an excuse?

Of course, that had all happened long ago.

It remained only as a tiny fragment of memory in his mind.

“The youngest bawled like the sky had fallen, and you didn’t touch your food. You just started training. You went off into the woods, away from everyone, and swung your sword until sunset. I can still picture you as clearly as if it were yesterday.”

“I don’t remember that, but I’m sure it happened.”

Jin Mukyung replied calmly.

Training was as natural to him as breathing. He had held a sword since childhood, and had always devoted himself to training, wherever and whenever he could.

Five years ago, the last time the three brothers of the Jin Family of Taiyuan had celebrated the Double Ninth Festival together, Jin Mukyung had already reached the Peak realm, though he was barely twenty.

“I still remember the day you left home.”

“Ah.”

Jin Mukyung smacked his lips.

He remembered his brother coming to see him off with a swollen face, as if he’d spent the previous night crying.

*“Do you… do you really have to go?”*

*“Yes. I really do.”*

*“Even if your older brother begs you like this?”*

*“Not a chance.”*

*“What’s so special about that Heaven’s Gate Temple that you’d abandon your own family and go all the way to a foreign land?”*

*“Even disciples of the great sects wait years to get into that Heaven’s Gate Temple you call so unimportant.”*

*“All right. If that’s really what you want, I’ll personally escort you to Henan.”*

*“…You’re serious?”*

*“There’s something I need to tell the Hall Master in person.”*

*“What on earth do you need to tell him?”*

*“Just a few important precautions he absolutely needs to know. Some foods you hate, your habits… Mukyung! Where are you going, Mukyung!”*

He ran. With every last bit of strength he could muster.

It was the first time in his life he had ever used his movement technique with such effort.

Jin Mukyung had only wanted to grow stronger at Heaven’s Gate Temple. He’d never had the slightest intention of earning the distinction of being its shortest-lived expelled cadet.

“I still remember your back as you left, covering your eyes with your sleeve to hide your sobs.”

“……”

Jin Mukyung quietly closed his mouth.

Some truths were more beautiful left unrevealed.

Like covering your eyes with your sleeve to keep out the dust, or running away to escape your overzealous older brother.

And then, before he knew it, a quiet laugh escaped him.

“Why did you suddenly laugh?”

“It’s nothing. Just…”

Jin Mukyung finally managed to stop laughing and turned his head.

The face of someone who had watched him with deep concern, about two years ago, when he left once again to enter seclusion for training with no end date in sight.

Just as it had been then.

“I laughed because I’m glad to see you. You haven’t changed at all, older brother.”

“Mukyung, you…”

“I’m glad everything is still the same.”

He had spent a little over two years in pitch-black darkness.

He’d staved off his hunger with bitter, astringent fasting pills, and quenched his thirst with dew and rainwater that collected in the training hall deep inside the cave.

And whenever he swung his sword until he collapsed from exhaustion, sprawled on the cold ground, a thought would come to him.

Where was this place? Who was he?

If he ever escaped this darkness, what would be waiting for him?

“Part of me was afraid, too. Afraid that the world I knew, the people I knew, would have changed beyond recognition.”

That guess had been half wrong and half right.

Everything around him had changed, but the people he knew were just as they’d always been.

Even the troublemaking youngest brother, whose whereabouts were unknown now, would surely be the same.

“The day that brat left home, he came to find me and said something.”

It was a conversation he had turned over in his mind thousands of times. No—tens of thousands.

Jin Taekyung’s voice, so very calm for once, still echoed in his ears at that very moment.

*“See you later.”*

It had been more than a simple farewell.

At the Star-Array Grand Banquet, among the countless stars gathered from the Nine Provinces and Eight Wastes and the Four Seas and Five Lakes, Taekyung had challenged him to meet and test their skills together with Cheongpung.

As brothers born of the same mother. As martial artists.

And Jin Mukyung, standing motionless as he watched the empty place his younger brother had left behind, had murmured the answer he hadn’t managed to give him.

*Yeah. See you later. I promise.*

But that promise had never been kept.

In that place, where he could not even feel time passing, Jin Mukyung swung his sword without rest. He slashed, stabbed, and tore through what lay beyond the pitch-black darkness.

Whenever he opened his eyes to something new, another wall rose before him.

He had to climb it. He had to break it.

With the unkept promise tucked away in a corner of his heart, Jin Mukyung continued to press forward.

Until he found a faint light in the darkness.

Until that light grew as clear as the sun.

And at last, he returned to the world.

Leaving behind the darkness that had enveloped him for two years, only to emerge into a world filled with another kind of darkness.

“Older brother.”

Jin Mukyung called softly and looked his own flesh and blood straight in the eyes.

His eyes held a light.

They were honest eyes that made it impossible for anyone looking into them to lie.

“Tell me what I have to do now.”

“……!”

“No. Give me an order. As the Lesser Family Head of the Jin Family of Taiyuan.”

For a moment, Jin Wikyung’s eyes trembled.

“You knew…?”

Jin Mukyung gave a quiet nod.

The Jin Family of Taiyuan now stood at the head of Shanxi Murim, and Jin Wikyung, who led them all in place of the missing Family Head, was its Alliance Leader.

Shanxi Province was already in a state of war.

Li Feng, a lay disciple of Huashan and Shanxi Province’s Assistant Military Commissioner, had mobilized all the forces of the Shanxi Provincial Office to evacuate the people in the north. Around five thousand martial artists had gathered in the central region.

Every moment mattered.

Jin Wikyung must have sought him out for more than the simple wish to reunite with the younger brother who had returned to the world after two years.

“Just as you know me well, older brother, I know you just as well.”

“This will be a dangerous mission.”

“I don’t mind.”

Jin Mukyung continued in an even tone.

“I learned martial arts because I loved the sword, but I sought strength for the sake of our family.”

Only great strength could restore a fallen martial family.

The sword Jin Mukyung had wielded all this time had carried more than just his passion for martial arts themselves.

“Jin Mukyung, Second Young Master of the Jin Family of Taiyuan. I will devote myself to carrying out the Lesser Family Head’s orders.”

At the sight of his younger brother cupping his hands in a salute and speaking without the slightest hesitation, Jin Wikyung slowly closed his eyes.

Then, after a brief hesitation, he opened them again. By then, he was no longer just an older brother. He was the Alliance Leader of Shanxi Murim and the Lesser Family Head of the Jin Family of Taiyuan.

“From this moment on, you are neither the Second Young Master of the Jin Family of Taiyuan nor the Lesser Family Head’s younger brother.”

He let out a breath he’d been holding, then spoke.

Jin Wikyung looked at his younger brother—or rather, his retainer—with a calm gaze and continued.

“I command Jin Mukyung, Commander of the Heaven Shaking Squad.”

Jin Mukyung, the Heaven Shaking Sword.

About five years ago, a young prodigy from the frontier had reached the Peak realm at barely twenty and earned a new epithet. His only older brother had named a fighting force after it.

In the hope that his younger brother would return to this place one day.

And with the wish that, just like the two characters in Heaven Shaking, his name would one day resound beyond the world and reach the heavens.

“The enemy vanguard that invaded the north has split off some of its troops and is taking a detour to avoid Jeongyang. Take two hundred men from the Heaven Shaking Squad and blunt their vanguard.”

Jin Mukyung smiled as he answered.

“As you command.”

* * *

The next day.

The vast steppe army, which had entered the north without meeting any resistance, was met not by chrysanthemums, but by dark-red blood covering the mountain slopes and a terrified survivor of its vanguard.

“K-Khan…”

Jamukha stared silently at the man trembling like a leaf.

He knew instinctively: the thousand-man vanguard that had invaded Shanxi Province half a day ahead of the main force had been completely wiped out.

And what the only surviving fool before him had brought was a stark warning to the invaders.

“H-he told me to deliver this to you, Khan…”

*Slide. Thump.*

The cloth slipped from the man’s trembling fingertips.

Jamukha silently watched the head of a Keshik centurion roll out from among the blood-soaked fabric, then spoke.

“Is that all?”

“He left a message. A message…”

The survivor, his queue come loose and his face contorted with fear, continued.

“He said, ‘Even five years from now, my brothers and I will climb the mountain together and celebrate the Double Ninth—’”

“Bullshit.”

*Shhk.*

A hand without the slightest hesitation.

His severed head rolled into the chrysanthemum field.

As Jamukha gazed at the field of flowers whose original color was no longer visible, Chinggen clicked his tongue.

“Why not hear him out? You don’t even know who he was.”

“Does that matter?”

What mattered was that a thousand men in the vanguard had been annihilated.

No—what mattered was that a hundred Keshik among them had died in a single battle.

“Either way… we’ll meet soon enough.”

Jamukha’s voice sank low as he stared south.

At that moment, a thought suddenly crossed his mind.

This war, which was supposed to be overwhelmingly one-sided, might not be as easy as he had imagined.
```
