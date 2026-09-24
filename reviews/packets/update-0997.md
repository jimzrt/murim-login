<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0997.txt",
      "sha256": "973da94aa5e1614899ab69adc841582a66dbfa629aa293a2bb9d42b98a035e93",
      "bytes": 13707
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "aa97bf902652c9274099592329b922920d96c61a997bbd394fcfc3bbe997f448",
      "bytes": 969
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d13308fe31a2c64daebd8b79b1737ef2a4f6a2f6e86338670363f6d7acf5174f",
      "bytes": 236719
    },
    {
      "path": "characters/Cheol Mubaek.md",
      "sha256": "cc21dfe4549881168b19cfc6d85df2b5176059ffc548815939704e3161168255",
      "bytes": 924
    },
    {
      "path": "characters/Hak Woo.md",
      "sha256": "e64e8929d10eb718b04c68bc7d4c67a5553c9d6237902bb1c197f21bffd062ad",
      "bytes": 612
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "24eb539031c5bb2be9929af89549c5486e0ad0181340265180b8ada02a1fcbb8",
      "bytes": 1665
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "901c254cc3c6e11b5023f569e414cac4819f71ff0dbddb55a429080582eeecaa",
      "bytes": 1613
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "9ae3d663458cb085b8918366f411bf07569f34adff9946225987136ffdc91632",
      "bytes": 1178
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "3c70e56c15039704ed3ac9494d3b49ea72bbd4df242949be25343e1345c346b2",
      "bytes": 622
    },
    {
      "path": "characters/Lee Seowol.md",
      "sha256": "8da764842ce0f08ef32965bf0e59b86f261806c8a913d3d0dcc0d99d3186ed65",
      "bytes": 1015
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "ae4a906e25e989781ab7ed57408da8c12a295beb9451068591fd500292ca5fea",
      "bytes": 1083
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "4cbd9ee2fb6eefb64d28bbef58f6af87882c9135f7649e7e3419eb623cacdedf",
      "bytes": 778
    },
    {
      "path": "characters/Song Ho.md",
      "sha256": "6fb3cb8887e8192b8f537c2313ef5638413a3e1a70824f007150c985605ebc72",
      "bytes": 767
    },
    {
      "path": "characters/Wipeng.md",
      "sha256": "de84a5db01c64f8362f43d8da346e35fa3dc2888b80165d453be80ea14299395",
      "bytes": 911
    },
    {
      "path": "characters/Zhuge Feng.md",
      "sha256": "f3d3878ef82cf7978041ac19986870ce6ecb9ffa20a4bfa4041a483ce49aae5d",
      "bytes": 649
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "bd5753e5df794eedf5b2ea27975a392475eb9bba5427ebd9beecb42050b7771b",
      "bytes": 273611
    }
  ],
  "estimated_tokens": 13602
}
-->

# Durable State Update — Chapter 997

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
1 and safe_through 997. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 997. Profile updates may replace only one
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
  "chapter": 997,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 997,
    "continuity_sources": [997],
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
    "Taekyung has fully assimilated the Heavenly Power Demon’s and Peng Cheolhu’s energy, reaching four jiazi of internal energy under his control.",
    "The “Desert Mirage” Quest requires Taekyung to head west; the Fire Dragon Pavilion is preparing to depart.",
    "Dark Heaven’s forces are advancing from Xinjiang; Qinghai and the Kunlun Sect are considered likely targets.",
    "Snow has begun falling months earlier than expected.",
    "Sama Pyo burned his father’s order to return immediately and left with the group."
  ],
  "continuity_sources": [
    996
  ],
  "open_questions": [
    "What is the objective behind Dark Heaven’s advance from Xinjiang, and where will its forces strike?",
    "What caused the System malfunction, and is it connected to the Lord of Heaven?",
    "Why did Sama Pyo’s father order him to return immediately?"
  ],
  "safe_through": 996,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 위팽     | **Wipeng**         |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 매종학    | **Mae Jonghak**    |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 무신     | **Martial God**               | —              |
| 궁성     | **Bow Saint**                 | —              |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 무림맹    | **Murim Alliance**               |
| 하북팽가   | **Hebei Peng Family**            |
| 제갈세가   | **Zhuge Clan**                   |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 중원     | **Central Plains**                               |                                                       |
| 가주     | **Family Head**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 본가      | **our family / this family**                                    |
| 공자      | **Young Master**                                                |
| 학우 | **Hak Woo** | Kunlun Sect top young prodigy known as the Kunlun Cloud Dragon; Taekyung addresses him as Hak. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 송호 | **Song Ho** | Elderly martial artist known as the Thousand-Faced Fox. |
| 제갈풍 | **Zhuge Feng** | Current Family Head of the Zhuge Clan. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 평화 | **Peace Guild** | Guild name. |
| 나비 | **Nabi** | Name used for the black kitten Familiar. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 천면호리 | **Thousand-Faced Fox** | Epithet of Song Ho. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 은영각주 | **Chief of the Hidden Shadow Pavilion** | Office formerly held by Song Ho. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 와룡객 | **Crouching Dragon Guest** | Epithet of Zhuge Feng. |
| 제갈 | **Zhuge** | Surname used for Sir Zhuge. |
| 모용세가 | **Murong Family** | One of the Five Great Families, based in Liaoning. |
| 천하제일검 | **Number One Sword Under Heaven** | Mae Jonghak's title. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 만족 | **Man people** | An ethnic group mentioned by the Poison Flower Pavilion owner. |
| 심해 | **deep sea** | Unexplored ocean depths where the ancient monster awakens. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 소월 | 철무백 | niece_to_paternal_uncle | Uncle Cheol | familiar-polite | Lee Seowol asks Cheol Mubaek to suppress his heat because she cannot breathe. |
| 철무백 | 소월 | paternal_uncle_to_niece | Seowol | affectionate-familiar | Cheol Mubaek speaks gently to Seowol and says protecting her is his duty. |
| 진태경 | 철무백 | junior_to_respected_Peak_master | Sir | apologetic-polite | Taekyung first calls Cheol Grandpa, then corrects himself to the respectful 대협. |
| 이소월 | 진태경 | rescued_sect_leader_to_benefactor | Benefactor | deferential | Lee Seowol repeatedly addresses Taekyung as 은공 after acknowledging that he and Jin Mukyung saved the Mount Heng Sword Sect. |
| 진무경 | 이소월 | junior_to_sect_leader | Sect Leader | formal-polite | Uses 문주 while greeting Lee Seowol. |
| 철무백 | 진무경 | senior_martial_peer_to_younger_martial_artist | Heaven Shaking Sword | affectionate-teasing | Uses 우리 진천검 while warmly inviting Mukyung to return. |
| 철무백 | 진태경 | senior_martial_peer_to_benefactor | you | casual-teasing | Uses 자네 while teasing Taekyung about his greeting and injuries. |
| 진위경 | 위팽 | lord_to_personal_guard | you | formal-but-familiar | Uses 자네 while assigning Wipeng the banner-preparation task. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 위팽 | 진무경 | Jin Family retainer to Second Young Master | Second Young Master | deferential and blunt | Uses 이공자 while directing Mukyung to wash before the guest's arrival. |
| 위팽 | 진태경 | retainer_to_third_young_master | Third Young Master | formal-polite and admonishing | Uses 삼공자 while warning Taekyung to return by noon and behave respectfully toward Jang Taebo. |
| 진위경 | 이소월 | host_to_new_sect_leader | Young Lady | formal-polite | Jin Wikyung addresses Lee Seowol as 소저 before accepting her oath. |
| 이소월 | 진위경 | new_sect_leader_to_lesser_family_head | Lesser Family Head | formal-deferential | Lee Seowol refers to Jin Wikyung as 소가주님 when describing his summons. |
| 철무백 | 진위경 | sect_elder_to_lesser_family_head | Lesser Family Head | formal-deferential | Cheol Mubaek formally greets Jin Wikyung as the Lesser Family Head of the Jin Family of Taiyuan. |
| 진태경 | 이소월 | young_martial_artist_to_allied_sect_leader | Young Lady Lee | formal-polite | Taekyung uses 이 소저 while greeting Seowol at the banquet. |
| 송호 | 청년 | elderly_martial_artist_to_younger_martial_artist | Young Hero | formal-polite | Song Ho calls out to the young man as 소협 at the chapter's end. |
| 송호 | 진태경 | senior_martial_artist_to_junior_martial_artist | you | familiar-polite | Uses 자네 while recognizing Taekyung and discussing his preliminary performance. |
| 매종학 | 송호 | savior_to_survivor | you | casual-familiar | Mae uses 자네 while speaking to Song Ho after his identity is recognized. |
| 송호 | 매종학 | rescued_survivor_to_savior | Great Hero; you | formal-deferential and familiar | Song Ho credits Mae with saving his life and addresses him as 대협. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 제갈풍 | 진태경 | senior strategist_to_younger_martial_artist | you | calm and familiar | Uses 자네 while inviting Taekyung to continue questioning the Hubei incident. |
| 가솔 | 진태경 | Zhuge Clan retainer to Great Hero | Great Hero Jin | polite and pleading | Uses 진 대협 while urging Taekyung to stop provoking Ju Wongong. |
| 제갈풍 | 진위경 | Zhuge Clan Family Head to Jin Family Lesser Family Head | Lesser Family Head | formal and conciliatory | Uses 소가주 while trying to secure Jin Wikyung's support during the settlement. |
| 진위경 | 제갈풍 | Jin Family Lesser Family Head to Zhuge Clan Family Head | Sir Zhuge | formal with deliberate comic deference | Uses 제갈 대협 while theatrically scolding Taekyung to force Zhuge Feng to concede. |
| 진태경 | 제갈풍 | younger martial artist to senior clan head | Sir Zhuge | blunt and challenging | Uses 제갈 대협 while disputing Zhuge Feng's attempted ten-percent claim. |
| 천면호리 | 매종학 | intelligence_chief_to_alliance_leader | Alliance Leader | formal and deferential | Requests that Mae move elsewhere with the others before he reports further. |
| 진태경 | 학우 | former_rival_to_Kunlun_young_prodigy | Hak | mocking and threatening | Taekyung uses Sound Transmission to intimidate Hak Woo into leaving. |
| 학우 | 진태경 | Kunlun_young_prodigy_to_famous_senior | Fellow Daoist Jin | formal and defensive | Hak Woo addresses Taekyung as 진 도우 while denying that he is busy. |
| 진태경 | 매종학 | younger ally to newly installed Alliance Leader | Alliance Leader | formal and deferential | Uses 맹주님 while formally greeting Mae Jonghak as the Alliance Leader. |
| 매종학 | 천면호리 | Alliance Leader to Hidden Shadow Pavilion Chief | Chief of the Hidden Shadow Pavilion | casual-but-commanding | Asks Song Ho's view of Taekyung's suspected target. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |

## Listed compact profiles

### Cheol Mubaek.md

# Cheol Mubaek (철무백)

- **Safe through:** Chapter 981
- **Aliases:** Tiger of Mount Heng
- **Role:** Cheol Mubaek is the ninth-generation successor of the Shura Annihilating Fist and the Peak master known as the Tiger of Mount Heng, now out of seclusion and active in the rebuilding of the Mount Heng Sword Sect.
- **Personality:** Fierce, short-tempered, intimidating, and fiercely protective; becomes gentle and attentive toward Seowol
- **Voice:** Roaring and confrontational when rebuking the Mount Heng senior figures; gentle and affectionate when speaking to Seowol
- **Relationships:** He was a close friend and peer of Lee Cheonbaek, a paternal uncle and protector of Lee Seowol, and a Benefactor to Jin Taekyung, Jin Mukyung, and Hyuk Mujin; he died buying Mukyung time against the Demon Bird and left him the Shura Annihilating Fist manual.

### Hak Woo.md

# Hak Woo (학우)

- **Safe through:** Chapter 532
- **Aliases:** Kunlun Cloud Dragon
- **Role:** Hak Woo is the Kunlun Sect's greatest young prodigy and is known as the Kunlun Cloud Dragon.
- **Personality:** He is wary, easily intimidated by threats to his hair, and eager to avoid unnecessary confrontation.
- **Voice:** He speaks politely and defensively, frequently using Daoist invocations.
- **Relationships:** Jin Taekyung is his former rival and can pressure him into leaving, while Ju Hwaran is an acquaintance he addresses formally.

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 985
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Jin Mukyung is the second son of the Jin Family of Taiyuan, a Supreme Peak swordsman known as the Heaven Shaking Sword, and Commander of the Heaven Shaking Squad.
- **Personality:** Reserved and disciplined, Jin Mukyung is devoted to swordsmanship and guided by a strong sense of chivalry and responsibility; losses deepen his self-reproach and resolve to grow strong enough to protect others.
- **Voice:** Quiet and resonant, clipped and blunt, with dry sarcasm in familiar exchanges.
- **Relationships:** Jin Wikyung is his older brother and the Lesser Family Head who formed the Heaven Shaking Squad in his honor; Jin Taekyung is his younger brother, who shares his own grief and encourages him to keep trying; Cheol Mubaek died protecting Mukyung and left him the Shura Annihilating Fist manual; their father—the Jin Family Head—once apologized to Mukyung for his mother’s death in childbirth.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 996
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Peng Cheolhu regarded Taekyung as a worthy successor, inheriting all that Peng had to pass on; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 996
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm and politically capable, Jin Wikyung takes responsibility for his people and prioritizes their lives; he uses calculated leverage to keep dangerous allies in line and commits firmly to his principles, even when doing so means remaining in a losing battle.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Jin Wikyung is Taekyung’s eldest brother and future Family Head, protects and mentors him, and commands the Jin Family’s forces; Jin Mukyung is his younger brother, and he considers the Jin Family indebted to the Dongting Fisherman and the other fallen defenders of Shanxi.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 996
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Seowol.md

# Lee Seowol (이소월)

- **Safe through:** Chapter 985
- **Aliases:** None
- **Role:** Lee Seowol is the eighteen-year-old Sect Leader of the reconstructed and rapidly growing Mount Heng Sword Sect, a vassal of the Jin Family of Taiyuan who still awaits Taekyung’s answer to her marriage proposal.
- **Personality:** Cold, commanding, and composed; capable of stopping a fierce confrontation with a calm request
- **Voice:** Clear and cool, gentle with Cheol Mubaek but frost-cold and firm when asserting her authority
- **Relationships:** Daughter of the deceased Lee Cheonbaek and niece of the deceased Cheol Mubaek, who entrusted her with the Shura Annihilating Fist manual; younger sister of the deceased Lee Seogeun and Lee Seogwang; has proposed marriage to Jin Taekyung in exchange for the Blood Wolf Sword Technique, Blood Wolf Footwork, and Shura Annihilating Fist; asked Taekyung to address her as Young Lady rather than Sect Leader.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 989
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader and has ordered Jin Taekyung's first Fire Dragon Pavilion mission to Nanman.
- **Personality:** Playful and easygoing in ordinary company, yet guided by a principled commitment to chivalry that can outweigh strategic caution.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 994
- **Aliases:** None
- **Role:** An unidentified legendary martial artist regarded as a pinnacle above the Ten Kings; more than fifty years ago, he defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, Mae Jonghak received several teachings from him, and he left the Bow Saint a letter describing a chosen one; the Bow Saint says he chose her, while his identity, whereabouts, and possible connection to Cheon Taemin remain unknown.

### Song Ho.md

# Song Ho (송호)

- **Safe through:** Chapter 989
- **Aliases:** Thousand-Faced Fox
- **Role:** Elderly Peak master known as the Thousand-Faced Fox, a martial artist with a prosthetic leg, and current Chief of the Hidden Shadow Pavilion, overseeing a vetted intelligence network that includes highly trained assassins.
- **Personality:** Outwardly genial and relaxed, but observant, forceful, and intimidating when pursuing information.
- **Voice:** Lightly genial and conversational, turning quietly coercive during interrogation.
- **Relationships:** He serves under Mae Jonghak's New Murim Alliance, commands the Hidden Shadow Pavilion, and recognizes Jin Taekyung as Jeok Cheongang's Disciple.

### Wipeng.md

# Wipeng (위팽)

- **Safe through:** Chapter 970
- **Aliases:** Ghost Sword; God of Drinking
- **Role:** Jin Wikyung’s personal guard and Commander of the Jin Dragon Squad; one of the Jin Family’s three Peak masters
- **Personality:** Loyal, observant, teasing, capable, and resigned to Jin Wikyung’s impulsive behavior. Respects the dead and urges others to live on their behalf.
- **Voice:** Weary and knowing, with dry humor when addressing Jin Wikyung or Jin Taekyung. Uses Sound Transmission when appropriate.
- **Relationships:** Trusted guard and retainer of Jin Wikyung; a reliable senior ally of Jin Taekyung and a longtime sword mentor to Jin Mukyung, whom he taught as a boy. He remains alert to threats connected with Dark Heaven, and the Human Butcher has claimed him as a personal target.

### Zhuge Feng.md

# Zhuge Feng (제갈풍)

- **Safe through:** Chapter 505
- **Aliases:** Crouching Dragon Guest
- **Role:** Zhuge Feng is the current Family Head of the Zhuge Clan and father of its Lesser Family Head, Zhuge Gyun.
- **Personality:** Analytical, disarmingly casual, eccentric, and inventive; he treats comfort and time as principles while delivering grave intelligence with unsettling directness.
- **Voice:** Clear, calm, polished, and conversational, with understated humor and pointed questioning.
- **Relationships:** Zhuge Gyun is his son, and Zhuge Gonghu was his grandfather.

## Korean source

```text
＃997화



일각(一刻).

차 한 잔조차 제대로 음미하지 못하는 짧은 시간이지만, 나를 비롯한 화룡각 대원들이 모든 준비를 끝마치기에는 충분했다.

다른 이들이 생각지도 못한 배웅을 준비하기에도.

후우웅. 화륵.

무수한 횃불이 흔들렸다.

일찍 찾아온 어둠도, 어느덧 거세게 휘몰아치기 시작한 눈보라도 그 거대한 불길을 꺼트릴 수는 없었다.

사박.

새하얗게 뒤덮인 땅 위로 새겨지는 발자국.

저마다 한 손에 횃불을 든 채 철탑처럼 서 있는 수백여 명의 사람들을 뒤로한 채, 홀로 걸음을 내디딘 진위경이 문득 입을 열었다.

“마침내 돌아온 탕아(蕩兒)가, 또 다시 떠나는구나.”

죄인을 심판하듯 준엄한 목소리였으나, 탕아라는 표현에 낮은 웃음소리가 곳곳에서 흘러나왔다.

이제는 태원진가뿐 아니라 산서성의 모두가, 아니 천하가 알기 때문이다.

진태경이라는 이름은 더 이상 가문의 수치도, 방탕한 망나니도 아니다.

지금으로부터 일 년 하고도 수개월 전, 대장로를 비롯한 배신자들을 쓰러트리고 평화를 되찾은 그 날부터 나는 저들의 자긍심이자 상징이었다.

“두 번 다시 너를 떠나보내고 싶지 않았거늘.”

씁쓸한 음성으로 뇌까리는 진위경을 향해, 나는 어깨를 으쓱해 보였다.

“어쩌겠습니까. 팔자려니 해야죠.”

“무림맹에서 온 것은 정보일 뿐이지, 명령이 아니다. 지금이라도 생각을 바꾼다면 본가에 남아 모두와 함께 움직일 수 있다.”

“그거 괜찮네요. 하지만 먼저 가서 기다리고 있겠습니다. 늦는 건 딱 질색이라서.”

내 완곡한 거절에 진위경이 작게 신음했다.

태원진가의 가주나 다름없는 그는 쉽사리 움직일 수 없다. 가문의 식솔들은 물론 수많은 산서 무림인들. 거기에 더해 굴복시킨 유목민들까지 통제하며 움직여야 한다.

모용세가의 화근을 뿌리 뽑은 뒤, 아직 귀환하지 못한 궁성과 금의위 역시 크게 다르지 않았다.

대군(大軍)과 소규모 별동대.

이중 무엇이 늦고 빠를지는 자명했다. 그리고 결코 짧지 않은 그 시간차가 머나먼 어딘가에 존재하는 나비의 날갯짓이 되어 많은 것을 뒤바꿀지도 모른다.

물론 그 사실을 알고 있다 하더라도, 혈육을 향한 걱정은 별개의 문제였지만.

“위험할 것이다. 그 어느 때보다도.”

우려로 가득한 진위경의 표정에 문득, 지금까지의 여정이 빠르게 눈앞을 스쳤다.

위험이라.

그래, 당연히 그렇겠지.

하지만…….

“항상 마찬가지였습니다. 지금껏 단 한 번의 예외도 없었고, 앞으로도 그럴 겁니다.”

돌이켜 보면 위험하지 않았던 적이 없었다.

힘들지 않은 순간 또한 없었다.

처음에 눈을 떴을 때는 올챙이였고, 살아남기 위해 발버둥 치다 보니 개구리가 되었다.

그렇게 온 힘을 다해 뛰고 또 뛰어 우물을 벗어나자, 그곳에는 비교도 되지 않게 넓고 험난한 우물 밖의 세상이 나를 기다리고 있었다.

그리고 발길을 가로막은 그 수많은 갈림길에서, 나는 늘 선택했다.

“제가 택한 길입니다. 언제쯤 멈출 수 있을지는 모르겠지만…… 달려봐야죠. 끝까지.”

담담하기 그지없는 내 대답에, 잠시 침묵하던 진위경이 불현듯 실소를 터트렸다.

“다 컸구나. 어느새 몰라볼 수도 없을 만큼 훌쩍 커 버렸어.”

하북팽가의 핏줄이 아닐까 의심될 정도로 압도적인 체구를 자랑하는 진위경을 바라보며, 나도 마주 웃어 보였다.

“아직 형님만큼은 아니죠.”

“형님이라, 형님. 그 호칭이 오늘따라 퍽 듣기 좋구나. 네가 나를 그렇게 부른 것이 너무나도 오랜만이라 그런 것인지도 모르겠다.”

이는 비단 내가 긴 시간을 밖에서 떠돌았기 때문만이 아니다. 그저 낯선 세상에서 만난 새로운 가족을 진심으로 받아들일 시간이, 조금 더 필요했을 뿐이다.

설령 이 몸뚱어리의 진정한 주인이 내가 아니라고 해도.

‘그래. 진짜 주인은, 태원진가의 삼공자는 따로 있지.’

문득 떠오른 생각에 마음이 무거워졌지만, 다음 순간 진위경의 옆에 나타난 익숙한 얼굴에 그런 생각은 씻은 듯이 사라졌다.

“오, 이게 누구야. 우리 집 둘째 아냐?”

짐짓 눈을 크게 뜬 내 모습에, 진무경이 고개를 절레절레 내저었다.

“또 시작이로군.”

“뭐가? 내가 틀린 말 했나? 둘째 맞잖아.”

“뒤에 형님을 붙이지 않은 건 쏙 빼놓고 말하는군.”

“원한다면 붙여 줄게. 나 이기면.”

“……이런 양심 없는 놈.”

“왜, 자신 없어?”

어이없다는 듯이 나를 노려보던 진무경이 피식 웃었다.

“그럴 리가. 기다려라. 금방 따라잡아 줄 테니.”

“자신감은 좋지만, 쉽지 않을 거라는 사실만 알아 둬.”

“이미 알고 있다. 대신 네 녀석도 이거 하나만 명심해라.”

“뭘?”

“내가 따라잡을 때까지, 절대 다른 놈한테 쓰러지지 말 것.”

“……!”

순간 말문이 막혔다. 말없이 눈만 깜빡거리는 내 모습에 괜한 말을 했다고 느꼈는지, 잠시 머뭇거리던 진무경이 돌연 주먹을 뻗었다.

툭.

아주 느릿하면서도 힘이 실린 주먹이 가슴에 닿았다.

사방에서 눈보라가 휘몰아치고 있었음에도, 진무경의 주먹이 잠시 닿았다가 떨어진 그 자리에는 온기가 번져 오고 있었다.

“먼저 가 있어라. 이번만큼은 늦지 않을 거다. 반드시.”

평소와는 다른 모습을 보였다는 부끄러움 때문인지. 아니면 울컥 솟구치는 어떠한 감정 때문인지는 모르겠다.

다만 진무경은 그 한마디를 끝으로 돌아섰고, 그의 걸음이 향하는 방향에는 또 다른 익숙한 얼굴들이 나를 기다리고 있었다.

극심한 부상을 입고도 나를 배웅하러 나와 준 위팽.

가장 든든한 후견인이자 또 한 사람의 아버지나 다름없던 의숙, 항산호 철무백의 죽음을 뒤로한 채 애써 미소 짓고 있는 이소월.

몰락해 가던 태원진가가 지금의 천하 오대세가로 거듭나기까지 진위경을 도와 변함없는 충성을 바쳐 온 태원진가의 중진들.

한때 나와 함께 생사를 넘나들었던 정찰대의 조원들도 있었고, 태원진가를 떠나 있는 동안 훌쩍 커 버린 어린 남매의 모습도 보였으며, 이름보다 얼굴이 익숙한 수많은 가솔들 역시 있었다.

그리고 그들 모두가 나를 바라보고 있었다.

한 사람, 한 사람의 눈을 마주칠 때마다 환하게 미소짓고, 조용히 고개를 끄덕이고, 당장이라도 가슴이 터질 것처럼 벅찬 표정으로 발을 굴렀다.

힘차고 굳세게. 누가 먼저라 할 것도 없이 어느덧 새하얗게 뒤덮인 땅을 두드리고, 각자의 병기를 벼락처럼 뽑아 들었다.

차차차차창!

흔들리는 수백여 개의 횃불 사이, 머리 위로 쏟아지는 눈보라와는 비교도 되지 않는 눈부신 강철의 파도가 사방을 밝혔다. 들불과도 같은 기세가 일어나 공기를 뜨겁게 달구었다.

쿵. 쿵. 쿠웅!

힘찬 발구름에 지면이 흔들린다. 어느덧 그에 맞춰 차분하게 가라앉던 심장이 요동치기 시작한 그때, 나직한 목소리가 귓가를 파고들었다.

“보이느냐?”

나는 대답하지 않았다.

아니, 대답하지 못했다.

파르르 떨려 오는 가슴 한구석을 안은 채, 그저 메아리처럼 울려 퍼지는 진위경의 목소리를 듣고만 있었다.

“너는, 우리의 자긍심이다.”

“……!”

“가거라. 네가 택한 그 길로.”

거침없고 맹렬하게 나아가거라.

거센 눈보라에 파묻힌 뒷말을 들으며, 나는 마침내 멈춰 있던 발걸음을 옮겼다.

사박.

수없이 교차된 강철의 지붕 아래, 새하얀 눈밭 위로 새로운 발자국들이 아로새겨지기 시작했다.



* * *



때아닌 눈보라는 비단 산서성에만 국한된 것이 아니었다.

약속된 손님이 들어온 후에도 오랫동안 침묵을 지키던 청년은, 창밖에서 거칠게 흩날리는 눈발을 바라보다 불쑥 입을 열었다.

“예전에, 아주 오래전에 누군가가 내게 그런 말을 했었지.”

투박한 탁자 너머, 한 시진 동안 이어진 침묵 속에서도 흐트러짐 없는 자세로 앉아 있던 손님이 말을 받았다.

“벌써부터 궁금해지는군요. 그가 누구인지.”

모르는 이가 보았다면 참으로 괴상한 광경처럼 느껴졌을 것이다.

방의 주인인 청년과 달리, 손님은 어림잡아 팔순은 되었을 것 같은 노인이었으니까.

그러나 희끗한 백발 너머로 보이는 흉터는 그가 비밀스러운 삶을 살았음을 나타내는 증거였고, 그것은 맞은편의 청년 역시 마찬가지였다.

“자네도 아는 사람일세. 원한다면 미리 알려 주지.”

당연하다는 듯 흘러나오는 하대.

그리고 그런 검성(劍星) 매종학의 제안을, 천면호리 송호는 가볍게 거절했다.

“듣고 나서 맞춰 보지요. 저는 답을 듣는 것보다, 스스로 알아내는 것을 좋아합니다.”

“보통은 전자를 택하지 않나?”

“명색이 은영각주인데, 이 정도는 해야 하지 않겠습니까.”

“그 또한 맞는 말이군.”

“하여, 그 누군가가 맹주께 무슨 말을 했습니까?”

여전히 창밖에 시선을 고정한 채, 매종학이 대답했다.

“지키라고 했지. 내가 서 있던 그 자리를, 마음에 품은 뜻을, 그리고 천하를.”

“……!”

“언젠가 당신께서 사라진다 해도, 변함없이 이곳에 남아 있으라 했었네. 물론 당시로서는 지나가듯이 건넨 말이었기에 나 역시 깊게 생각하지 않았지. 이게 전부일세.”

천면호리는 잠시 참았던 숨을 내쉬었다.

“누구인지 알 것 같군요.”

“그런가?”

“예. 공교롭게도 저 역시 비슷한 말을 들었던 것 같습니다.”

“그분이 알았다면 기뻐하셨겠군. 자네는 그 말을 허투루 듣지 않고 은영각의 정보망을 유지해 왔으니.”

천면호리는 말없이 고개를 끄덕였다.

틀림없이 그랬을 것이다. 어쩌면 손뼉까지 치며 웃음을 터트렸을지도 모른다.

그의 뇌리에 남아 있는 무신(武神)의 모습은, 세상 모든 근심을 떠안은 것 같으면서도 때로는 어린아이처럼 순수한 면모를 지니고 있었으니까.

“한 가지. 묻고 싶은 것이 있네.”

“말씀하십시오. 맹주(盟主).”

천면호리는 자신도 모르게 긴장했다.

무신을 대신하여 중원 무림의 새로운 상징이 된 눈앞의 천하제일검이, 가장 결정적인 시기에 흔들리지 않을까 우려되었기에.

그러나 다음 순간 들려온 매종학의 한 마디는, 그런 천면호리의 우려를 단숨에 허물어트렸다.

“만약 이 전쟁이 끝나면, 자네는 어찌할 생각인가?”

“예?”

“아니, 그냥. 갑자기 걱정되어서 말일세. 하는 일에 비해 봉급도 얼마 못 받아 가는데 지금이라도 올려 줄까 하고. 두 배 정도 올리면 어떤가.”

“……!”

“음. 아니면 세 배? 그쯤 되면 노후는 걱정 안 해도 될 텐데.”

석상처럼 굳은 채, 멍하니 매종학을 바라보던 천면호리는 불현듯 너털웃음을 터트렸다.

그리고 이내 웃음을 거둬들이며 대답했다.

“제 노후는 걱정하지 마십시오. 필요하면 언제든 뒤로 빼돌릴 테니.”

“오. 역시 자네는 다 계획이 있군.”

“이를 말이겠습니까.”

“하지만 이 대화는 자네와 나만의 비밀로 하세. 저 문밖의 친구들이 알게 되면 눈총을 받을지도 모르니. 안 그런가?”

매종학은 대답을 기다리지 않고 자리에서 일어났다.

공기를 타고 뻗어 나간 기의 바람이 굳게 닫혀 있던 문을 열어젖히자, 그곳에는 거대한 탁자에 둘러앉은 수십여 명의 인물들이 있었다.

“미리 말씀드리는데, 저는 양만 적당하다면 은영각주께서 무슨 짓을 하시든 눈감을 용의가 있습니다.”

가장 먼저 입을 연 중년인의 장난스러운 한 마디에, 매종학이 만족스럽게 고개를 끄덕였다.

“역시 똑똑하군. 때에 맞는 말을 할 줄 알아.”

“별말씀을.”

“그래, 맡은 일은 무사히 완수했나. 제갈 가주.”

중년인, 와룡객(臥龍客) 제갈풍이 넝마가 된 학우선을 흔들었다.

“보이십니까?”

“아주 잘.”

“제 고생의 흔적입니다. 아주 죽는 줄 알았지요.”

“그렇다는 건…….”

“제갈세가는 맡은 바 모든 임무를 완수했습니다.”

곳곳에서 탄성이 흘러나왔다. 제갈풍이 어떤 임무를 맡았는지, 또한 그 임무가 얼마나 중요한 것인지 이 자리의 모두가 알고 있었다.

그리고 그것이 의미하는 바는 하나였다.

모든 준비의 끝. 새로운 국면의 전환.

“그럼, 이제부터 모두가 바빠지겠군.”

총력전(總力戰)의 서막이 올랐다.
```

## Final English reading copy

```markdown
# Chapter 997

Fifteen minutes.

It was too short a time to properly savor even a cup of tea, but plenty for the Fire Dragon Pavilion members, myself included, to finish all our preparations.

And to prepare a send-off no one else had expected.

Whoooosh. Fwoosh.

Countless torches swayed.

Neither the darkness that had fallen early nor the snowstorm now whipping fiercely through the air could put out those enormous flames.

Crunch.

Footprints marked the snow-covered ground.

Leaving behind hundreds of people standing like iron towers, each holding a torch in one hand, Jin Wikyung stepped forward alone. Then he suddenly spoke.

“The prodigal son finally came home, only to leave again.”

His voice was stern, as if passing judgment on a criminal, but the word *prodigal* drew quiet laughter from here and there.

By now, everyone in the Jin Family of Taiyuan knew it. Not just them, but all of Shanxi Province—or rather, the whole world.

The name Jin Taekyung was no longer a stain on his family or a dissolute rogue.

Ever since that day, more than a year ago, when I defeated the traitors—including the Head Elder—and restored peace, I had become their pride and their symbol.

“I never wanted to see you off again.”

I shrugged at Jin Wikyung, who muttered the words with a bitter expression.

“What can I do? Guess it’s fate.”

“What came from the Murim Alliance was information, not an order. If you change your mind, even now, you can stay with the family and move out with everyone.”

“That sounds nice. But I’ll go ahead and wait for you. I hate being late.”

Jin Wikyung let out a small groan at my polite refusal.

He was practically the Family Head of the Jin Family of Taiyuan, so he couldn’t just move at a moment’s notice. He had to lead not only the family members, but countless martial artists from Shanxi—and the nomads they had subdued, too.

It was much the same for the Bow Saint and the Embroidered Uniform Guard, who still hadn’t returned after rooting out the Murong Family’s threat.

A massive army and a small advance unit.

It was obvious which would be slower and which would be faster. And that considerable gap in timing might become the flap of a butterfly’s wings somewhere far away and change a great many things.

Of course, even knowing that didn’t make worrying about family any easier.

“It will be dangerous. More than ever before.”

At the sight of Jin Wikyung’s worried expression, the journey I’d taken so far suddenly flashed through my mind.

Dangerous, huh?

Yeah, of course it would be.

But…

“It’s always been the same. There hasn’t been a single exception, and there won’t be one from here on out.”

Looking back, there had never been a time when I wasn’t in danger.

There had never been a moment that wasn’t hard, either.

When I first opened my eyes, I was a tadpole. I struggled to survive, and became a frog.

Then I threw myself into one leap after another until I escaped the well. Beyond it, a world immeasurably wider and more treacherous than the well had been waiting for me.

And at every fork in the road that blocked my way, I had always made a choice.

“It’s the road I chose. I don’t know when I’ll be able to stop, but… I have to run. All the way to the end.”

Jin Wikyung was silent for a moment at my utterly matter-of-fact answer. Then he suddenly let out a rueful laugh.

“You’ve grown up. Before I knew it, you’d grown so much I hardly recognized you.”

Looking at Jin Wikyung, whose imposing build was enough to make me wonder if he had Hebei Peng blood, I smiled back.

“I’m still not as big as you, hyung.”

“Hyung. That sounds especially good today. Maybe because it’s been so long since you called me that.”

It wasn’t just because I’d spent so long wandering outside. I’d simply needed a little more time to truly accept the new family I’d found in this unfamiliar world.

Even if the body’s true owner wasn’t me.

*Right. The real owner—the Jin Family’s Third Young Master—is someone else.*

The thought weighed on me, but the familiar face that appeared beside Jin Wikyung a moment later washed it away.

“Oh, would you look at that. Isn’t that our family’s second son?”

At my exaggeratedly wide-eyed expression, Jin Mukyung shook his head.

“Here we go again.”

“What? Did I say anything wrong? You are the second son.”

“You conveniently left out the ‘hyung’ that’s supposed to come after it.”

“I’ll add it if you want. Beat me first.”

“…You shameless bastard.”

“What, you don’t think you can?”

Jin Mukyung stared at me in disbelief, then let out a quiet laugh.

“Of course I can. Just wait. I’ll catch up soon.”

“Confidence is good, but just know it won’t be easy.”

“I know. But you’d better remember one thing, too.”

“What?”

“Until I catch up, don’t let anyone else take you down. Ever.”

“……!”

For a moment, I couldn’t speak. Seeing me just blink in silence, Jin Mukyung seemed to realize he’d said something embarrassing. After hesitating briefly, he suddenly thrust out his fist.

Tap.

It was a slow, forceful punch. His fist touched my chest.

Even with the snowstorm raging all around us, warmth spread from the spot where Jin Mukyung’s fist had touched before pulling away.

“Go ahead. This time, I won’t be late. I promise.”

Maybe he was embarrassed to show a side of himself he normally didn’t. Or maybe some emotion had surged up in him.

Whatever the reason, Jin Mukyung turned away after those words. In the direction he headed, more familiar faces were waiting for me.

Wipeng, who had come to see me off despite his grievous injuries.

Lee Seowol, forcing a smile despite the death of her uncle, Cheol Mubaek—the Tiger of Mount Heng—who had been her staunchest guardian and almost another father to her.

The Jin Family of Taiyuan’s senior members, who had served Jin Wikyung with unwavering loyalty and helped him raise the once-declining family into one of the Five Great Families.

The scouts who had once crossed life and death alongside me. The young brother and sister who had grown so much while I was away from the Jin Family of Taiyuan. And countless family retainers whose faces were more familiar than their names.

Every one of them was looking at me.

As I met each person’s eyes, they smiled brightly, nodded quietly, and stamped their feet with such overwhelming emotion that their hearts seemed ready to burst.

Hard and strong. Without anyone having to lead, they stamped the ground, now blanketed in white, and drew their weapons like lightning.

Clang-clang-clang-clang!

Between the hundreds of swaying torches, a dazzling wave of steel lit up the surroundings—nothing like the snowstorm pouring down overhead. A wildfire-like aura rose, heating the air.

Thud. Thud. Thoom!

The ground shook beneath their vigorous footfalls. My heart, which had gradually settled into a steady rhythm to match them, began to pound. Just then, Jin Wikyung’s quiet voice slipped into my ear.

“Do you see it?”

I didn’t answer.

No—I couldn’t.

I could only listen to Jin Wikyung’s voice echoing around me, my chest trembling deep inside.

“You are our pride.”

“……!”

“Go. Down the road you chose.”

Go forward without hesitation, with all your might.

Hearing the rest of his words swallowed by the fierce snowstorm, I finally moved my feet.

Crunch.

Beneath a roof of steel, crisscrossed countless times, new footprints began to mark the white snow.

* * *

The untimely snowstorm wasn’t confined to Shanxi Province.

The young man had remained silent for a long time, even after his expected guest arrived. Watching the snow whip past the window, he suddenly spoke.

“Long ago—very long ago—someone said something like that to me.”

Across the rough table, the guest sat with perfect composure despite a full shichen—about two hours—of silence. He answered,

“You’ve made me curious already. Who was he?”

To anyone who didn’t know them, it would have seemed like a strange sight.

Unlike the young man who owned the room, his guest was an old man who looked to be about eighty.

But the scars visible beneath his graying white hair testified to a life shrouded in secrecy. The young man sitting opposite him was no different.

“You know him, too. I can tell you now, if you want.”

He spoke to the older man as an elder would to a junior, as though it were the most natural thing in the world.

The Thousand-Faced Fox, Song Ho, lightly declined the Sword Saint Mae Jonghak’s offer.

“I’ll try to guess after I hear it. I prefer figuring things out for myself to being given the answer.”

“Wouldn’t most people choose the former?”

“As Chief of the Hidden Shadow Pavilion, shouldn’t I at least be able to do this much?”

“That’s a fair point.”

“So, what did that someone say to the Alliance Leader?”

Still gazing out the window, Mae Jonghak answered.

“He told me to protect it. The place where I stood, the convictions I held in my heart, and the world.”

“……!”

“He told me to remain here, unchanged, even if one day he disappeared. Of course, at the time, it was just something he said in passing, so I didn’t think much of it. That’s all.”

The Thousand-Faced Fox let out a breath he’d been holding.

“I think I know who it was.”

“You do?”

“Yes. As it happens, I believe I heard something similar myself.”

“If he knew, he’d be pleased. You didn’t take his words lightly. You’ve kept the Hidden Shadow Pavilion’s intelligence network going all this time.”

The Thousand-Faced Fox nodded without a word.

He certainly would have been pleased. Maybe he would even have clapped his hands and burst out laughing.

In Song Ho’s memories, the Martial God seemed to carry every worry in the world, yet at times he could be as innocent as a child.

“There’s something I’d like to ask you.”

“Go ahead, Alliance Leader.”

The Thousand-Faced Fox tensed without meaning to.

He worried that the Number One Sword Under Heaven, the man now the new symbol of the Central Plains Murim in the Martial God’s place, might waver at the most crucial moment.

But Mae Jonghak’s next words immediately swept those fears away.

“When this war is over, what are you going to do?”

“Pardon?”

“No, it’s nothing. I just suddenly started worrying. For all the work you do, you hardly get paid. Should I give you a raise now? How about doubling your salary?”

“……!”

“Hmm. Or tripling it? Then you wouldn’t have to worry about retirement.”

The Thousand-Faced Fox stared blankly at Mae Jonghak, frozen like a statue. Then he suddenly burst into a hearty laugh.

When he’d finished laughing, he answered,

“Don’t worry about my retirement. If I need to, I can always siphon some money off to the side.”

“Oh. So you already have a plan.”

“Of course.”

“But let’s keep this conversation between the two of us. If our friends outside that door find out, they might give us a hard time. Right?”

Mae Jonghak stood without waiting for an answer.

A current of qi flowed through the air and swung open the firmly shut door. Beyond it sat dozens of people around a massive table.

“I’ll say this up front: as long as the amount is reasonable, I’m willing to turn a blind eye to whatever the Chief of the Hidden Shadow Pavilion does.”

At the first playful remark from a middle-aged man, Mae Jonghak nodded with satisfaction.

“Clever, as always. You know what to say at the right time.”

“Not at all.”

“Now then, did you complete your mission safely, Family Head Zhuge?”

The middle-aged man, Zhuge Feng, the Crouching Dragon Guest, waved his tattered feather fan.

“Can you see it?”

“Quite clearly.”

“These are the marks of my suffering. I thought I was going to die.”

“Which means…”

“The Zhuge Clan has completed every task assigned to it.”

Exclamations rose from all around the room. Everyone present knew what mission Zhuge Feng had been given, and how important it was.

And it meant one thing.

All preparations were complete. A new phase was beginning.

“Well, then. Everyone’s going to be busy from here on out.”

The opening act of an all-out war had begun.
```
