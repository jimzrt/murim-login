<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1171.txt",
      "sha256": "a39008cff7fc087a20675bf8c8bddb2f472df578ce7b7531a95b5e0ed4c078ad",
      "bytes": 12601
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "39468789c73014bb2784c2528ee298adfc0cf7e32e51e27f11f47f8b6911e05e",
      "bytes": 1184
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "e5e79ce2dcef0e436ab63d6d7ce4514037a40b7300c4332ed3928f63771f12a9",
      "bytes": 248116
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "3cd49b5d2082a5160b5ee6a3ad141e4caef9975083e1ac78009dff883041cb03",
      "bytes": 760
    },
    {
      "path": "characters/Grand Mage.md",
      "sha256": "bb4beed677c882cd7e73b52e438c999a52ec15b2025e4e610799877807527818",
      "bytes": 545
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "f3bcd41720d12025ae7cd4c42f74301e99ed343f27119903c52e2e2dcf924a5c",
      "bytes": 1515
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "2cf4651b4c2ee25ae38fa4e687e904f2f65cbf4aee682a564c518642d81a48e4",
      "bytes": 623
    },
    {
      "path": "characters/Morgoth.md",
      "sha256": "837f15dbb77c4aa1ae6cee8287a67ac284b16925c8abdaa0fa476d4cd27056ba",
      "bytes": 895
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "97b900dbb29a57db84ee2adbffd58479c504d0863bf1805451d09b1ed9be91d4",
      "bytes": 294489
    }
  ],
  "estimated_tokens": 9672
}
-->

# Durable State Update — Chapter 1171

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
1 and safe_through 1171. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1171. Profile updates may replace only one
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
  "chapter": 1171,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1171,
    "continuity_sources": [1171],
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
    "Humanity won the battle against Morgoth; its surviving forces are wounded but rallying.",
    "Jin’s physical injuries were healed, but severe mental exhaustion remains; his Fire Dragon Armor was destroyed.",
    "Jin created Open Heaven, the third form of the Fire Dragon Divine Spear; Fire Gate Divine Technique and Qi Sense reached the ninth star.",
    "Jin recovered the Skeleton King from Morgoth.",
    "Morgoth is gravely wounded, with his Dragon Heart exposed; a streak of light is now shooting toward it.",
    "Morgoth noticed an object at Jin’s neck surrounded by energy that is neither mana nor magical power, and sensed it as a trace of the one he sought.",
    "Jin is determined to keep going and hopes to survive alongside his allies, regardless of whether he was chosen by God."
  ],
  "continuity_sources": [
    1169,
    1170
  ],
  "open_questions": [
    "Is Jin truly chosen by God, and what does that mean?",
    "What will happen to Morgoth and the Skeleton King?",
    "What is the object at Jin’s neck, and whose trace did Morgoth recognize?"
  ],
  "safe_through": 1170,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 절정     | **Peak**          |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 보상               | **Reward**                     |
| 칭호               | **Title**                      |
| 몬스터     | **monster**           |
| 마법사     | **mage**              |
| 대격변     | **Great Cataclysm**   |
| 화산     | **Huashan**            |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 모르고스 | **Morgoth** | The being who answers the summoning. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 용족 | **dragonkin** | Monster classification including wyverns and drakes. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 슬레이어 | **Slayer** | Cheon Taemin's title after killing the Demon King. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 신력 | **divine strength** | Superhuman strength attributed to Taekyung. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 골골이 | **Bones** | Jin’s familiar nickname for the Skeleton Warlord and its new Skeleton King form. |
| 골골 | **Golgoli** | Jin's nickname for the Skeleton King. |
| 무한 | **Wuhan** | Capital of Hubei Province near Dongting Lake. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 위압 | **Intimidation** | System attribute strengthened by the achievement reward. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 재생 | **Regeneration** | The masked man's rapid recovery from shattered bones and severe wounds. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 언데드 | **undead** | Supernatural beings that are neither dead nor alive. |
| 흑룡공 | **Black Dragon Duke** | Title in Morgoth's System announcement. |
| 드래곤 | **Dragon** | The species to which Morgoth belongs. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 골골 | captor_to_subordinate_undead | Bones | mocking-casual | Jin uses the mocking nickname while treating the Skeleton Warlord like a pet. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 진태경 | 마법사 | rescuer assisting the operation | mage; otherwise you | polite emergency imperative | Taekyung orders the exhausted mage to request rescue under his name. |
| 골골 | 진태경 | subordinate_undead_to_captor_and_master | human | mocking, reluctant, and familiar | Calls Jin 인간 and 간악한 인간 while complaining about being deceived into searching Area A. |
| 존슨 | 진태경 | allied friend and comrade-in-arms | Jin | familiar and conversational | Johnson calls Jin 진 while asking what he was thinking. |
| 대마도사 | 진태경 | adversary_to_adversary | you | polite, teasing | She uses polite phrasing while taunting him and warning him not to overexert himself. |
| 진태경 | 대마도사 | adversary_to_adversary | you bitch | insulting-casual | He curses at her while refusing to give up. |
| 모르고스 | 진태경 | enemy Dragon addressing a human opponent | you | formal, measured | Uses 자네 while addressing Jin. |
| 진태경 | 모르고스 | human opponent addressing an enemy Dragon | son | casual and mocking | Calls Morgoth 아들. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1170
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Grand Mage.md

# Grand Mage (대마도사)

- **Safe through:** Chapter 1169
- **Aliases:** None
- **Role:** Magic Johnson is the United States' Grand Mage and a War Mage, one of the two remaining masters of Magic.
- **Personality:** Strategic and ambitious, with a sharp temper when others squander opportunities or act without consulting her.
- **Voice:** He speaks casually and directly, with colloquial phrasing and occasional profanity.
- **Relationships:** He is Jin Taekyung's friend.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1170
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and eleventh member of the Ten Kings, a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; he serves as Thousand Captain of the Embroidered Uniform Guard, is enfeoffed as Prince Shangshan, and is widely regarded as a new-age savior.
- **Personality:** Hungry, self-aware, and dryly observant, he is pragmatic and fiercely defiant; he protects those he cherishes and meets mounting responsibility with hope and a determination to endure.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother and Jeok Cheongang his Master and trusted confidant; he shares deep loyalty with Hyuk Mujin, whom he values as family, and considers the Skeleton King a friend.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1170
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Morgoth.md

# Morgoth (모르고스)

- **Safe through:** Chapter 1170
- **Aliases:** None
- **Role:** Morgoth is a Dragon and sovereign of a vast palace who collects powerful beings he kills or subdues as Guardians, including seven S-rank Hunters from Earth.
- **Personality:** Composed and intellectually curious, Morgoth spent millennia seeking God and regards powerful beings as sources of amusement, willing to aid a worthy rival when it promises greater future entertainment.
- **Voice:** He speaks in polished, measured phrasing, but can drop his courtesy for blunt, direct admissions when speaking sincerely.
- **Relationships:** Asmodeus summoned Morgoth, though Morgoth says he is not devoted to him; Morgoth returned the Skeleton King to Jin to help him grow stronger and commands seven soul-stolen S-rank Hunters as Guardians.

## Korean source

```text
＃1071화



그건 마치 보석과도 같았다.

세상에 존재하는 그 어떤 예술품보다도, 아니 그 모든 것을 합치더라도 따라올 수 없는 아름다움과 신비를 갖춘 보석.

그러나 불길하리만치 어두운 빛을 사방에 흩뿌리고 있는 그것은 단순한 광물 따위가 아니었다.

드래곤 하트(Dragon Heart).

명칭 그대로, 드래곤이라 불리는 위대한 종족의 심장이자 힘의 원천.

그리고 지금 이 순간, 하늘과 땅이 구분된 이래 가장 지혜롭고 강력했던 드래곤 로드(Dragon Lord)이자 그 어떤 드래곤보다 깊게 타락한 누군가는 자신의 기나긴 삶이 끝났음을 깨닫고 있었다.

온몸으로, 영혼으로.

또한, 천둥처럼 귓가에 울려 퍼지는 소리로.

쩌저적.

매끈한 표면 위로 거미줄처럼 번져가는 실금.

오직 주인의 강인한 의지와 마지막 남은 힘으로 가까스로 형태를 유지하고 있던 드래곤 하트의 균열을 막을 수 있는 것은 이제 아무것도 없었다.

그저, 이미 예정되어 있던 파괴를 앞당기는 한 줄기의 섬광만이 있을 뿐.

콰직!

부서지고, 갈라진다.

창날을 타고 흐르던 노을빛이, 그 누구의 손길조차 허락한 적 없던 용의 심장이.

우우우웅.

핏물 대신 울컥 쏟아지는 어둠.

주위를 둘러싼 대기가, 세상이 곧 벌어질 일을 깨달은 것처럼 부르르 몸을 떨었다.

하지만 생명이 꺼져 가는 그 순간조차도, 자신의 심장에 창날을 박아 넣은 신룡(神龍)을 향한 마룡(魔龍)의 시선만큼은 조금도 흔들리지 않았다.

- 네게 주어진 온 힘을 다해 싸워라. 끝없이 넘어서고, 발버둥 쳐라.

혼잣말처럼 흘러나온 음성에 담긴 감정은 후회도, 분노나 저주도 아니었다.

그것은 듣는 이조차 이해할 수 없었던 격려인 동시에 짙은 아쉬움이었다.

앞으로 일어날 놀라운 유희를 경험하지 못한다는 사실로부터 비롯된 아쉬움.

- ……내가 있는 곳에서도 보일 수 있도록.

그 순간.

고오오옹.

일대의 모든 것이 움직임을 멈췄다.

바람도, 공기도.

실로 아득했던 삶의 마지막 숨결을 내뱉은 용의 거대한 몸뚱어리도.

그리고.

콰아아아아!

드래곤 하트가, 그 안에 고여 있던 수천 년의 시간과 무한에 가까운 마력이 온 사방으로 흘러넘쳤다.



* * *



어둠과 눈부심이란 결코 공존할 수 없는 단어다.

하지만 적어도 그 순간만큼은, 전장의 모두가 확실하게 보고 느낄 수 있었다.

기둥이 되어 솟구치는 눈부신 어둠과 온 세상을 뒤흔들며 터져 나오는 거대한 힘을.

그리고 그것을 가장 먼저, 또한 누구보다 가까이에서 겪은 것은 당연하게도 진태경이었다.

화아아악-

삽시간에 시야를 뒤덮은 칠흑빛 어둠을 직면한 그때부터, 더 이상의 생각은 필요 없었다.

진태경은 오직 본능에 따라 움직였다.

용의 심장에 박혀 있던 창날을 뽑는 동시에, 가까스로 되찾은 스켈레톤 킹의 머리를 품속 깊이 감싸 안으며 태아처럼 몸을 웅크렸다.

바로 다음 순간, 찰나의 정적을 찢으며 들이닥친 마력의 파도를 느끼면서.

구구구구궁!

귓가를 먹먹하게 물들이는 굉음과 함께 세상이 뒤집혔다.

하늘과 땅이 수없이 회전하며 눈앞을 어지럽히고, 무중력 상태와 같은 부유감(浮游感)이 전신을 지배했다.

하지만 진태경이 그토록 극심한 혼란 속에서도 정신을 잃지 않을 수 있었던 것은, 그 자신의 강인한 정신력과 굉음으로도 덮지 못한 맑은 종소리 덕분이었다.

띠링. 띠링. 띠링.



- [Lv195. ‘흑룡공’ 모르고스]를 처치했습니다!

- 위대한 업적, [용살자(龍殺者)]를 달성하셨습니다!

- 업적 달성 보상이 지급됩니다!

- 막대한 경험치를 획득했습니다!

- 당신의 [위압]이 크게 증가합니다!

- 칭호, [드래곤 슬레이어]를 획득하셨습니다!

- [용족]과의 전투 시 모든 능력이 상당량 증가합니다. 만약 언젠가 당신이 또 다른 [드래곤]과 조우하게 된다면, 해당 개체의 성향에 따라 당신을 대하는 태도가 엇갈릴 것입니다.

- 레벨 업!

- 레벨 업!

- 레벨 업!

- 레벨 업!

- 모든 부상과 상태 이상이 회복됩니다!



시스템 알림.

또 한 번의 위기를 넘겼다는 가장 확실한 증거.

아마도 그 때문이었을 것이다. 진태경이 지금껏 온 힘을 다해 부여잡고 있던 의식의 끈을 놓으려 한 것은.

‘쉬고 싶다.’

오직 그 생각만이 전부였다.

뒤에 벌어질 일은 아무래도 좋았다.

정작 몸뚱어리는 지금 이 순간에도 포탄처럼 저 멀리 튕겨 나가고 있긴 하지만, 그게 대관절 무슨 상관이란 말인가.

이미 모르고스는 확실한 죽음을 맞이했고, 그 많던 몬스터 군단 역시 송두리째 와해되어 사냥감으로 전락한 상황.

설령 이대로 어딘가에 처박혀 뼈가 몇 군데 부러지더라도 괜찮다.

아니, 어쩌면 고통조차 느낄 수 없을 것이다.

지금 눈을 감는다면, 그 즉시 신체적 통증쯤은 가볍게 무시할 정도의 깊은 수면 상태에 빠질 테니까.

그러니 모든 것이 마무리된 지금, 그의 휴식을 가로막을 요소는 아무것도 없었다.

‘그래, 아무것도.’

적어도 진태경은 그렇게 확신했다.

끔찍하게도 무겁게 느껴지는 눈꺼풀을 내려놓기 직전, 귓가를 통해 전해지는 누군가의 목소리를 듣기 전까지는.

- 제기랄, 끔찍하군.

처음에는 착각이라고 생각했다.

혹은 맹렬한 바람 소리가 만들어낸 환청이라든지.

하지만 둘 다 아니었다.

그는 아직 잠들지 않았고, 곧이어 이어지는 목소리는 이 모든 것이 현실이라는 사실을 증명하듯 선명했다.

- 하필이면 땀 냄새 진동하는 사내놈 품에서 깨어나다니.

퉁명스러운, 그래서 더 반가운 그 음성에 진태경은 온 힘을 다해 눈꺼풀을 들어 올렸다.

그리고 어느새 자신의 품 안에서 깨어난 목소리의 주인을 멍하니 바라보다가, 문득 입을 열었다.

“너 냄새 못 맡잖아. 언데드라서.”

- ……이 개자식아.

잠깐의 침묵 뒤에 튀어나온 외마디 욕설.

그러나 그 안에는 숨길 수 없는 웃음기가 섞여 있었고, 새하얀 해골의 미간을 타고 이어진 황금빛 기운은 횃불처럼 타올랐다.

온 사방에 흘러넘치는 용의 마력을 장작 삼아, 그 어느 때보다도 맹렬하게.

솨아아아악!

일순간, 바람을 타고 퍼져나가던 짙은 어둠이 진태경을 향해 쏘아졌다.

아니, 정확히는 그의 품 안에 있는 존재가 그것들을 빨아들였다.

마치 소나기가 생명을 깨우고, 태양이 힘을 불어넣으며, 토양을 밑거름 삼아 성장하듯이.

스아아아.

어둠이 스며들수록 선명해지는 황금빛 기운.

그리고 그 상반된 두 줄기의 색 너머로 점차 커져 가는 그림자.

그건 누구도 본 적 없는 경이로운 광경이었다.

재생, 부활.

어쩌면, 새로운 탄생(誕生)이라 불러도 좋을.

그러나 주위의 모든 어둠을 집어삼키며 성장한 그것은 결코 불길한 존재가 아니었다.

설령 또 다른 누군가는 그를 손가락질하며 욕하더라도, 진태경에게는 아니었다.

그는 저 찬란한 황금빛 왕관만큼이나 밝게 빛나는 존재였으니까.

스륵.

진태경은 눈을 깜빡였다.

어지럽게 뒤집히던 시야도, 칼날처럼 휘몰아치던 바람도 이제는 느껴지지 않았다.

그저 꿈처럼 몽롱한 의식 너머로 조심스럽게 자신을 땅에 눕히는 누군가의 익숙한 손길과 그의 머리 위에 떠오른 한 줄의 글귀만이 흐릿하게 망막을 비추고 있을 뿐.



[Lv180. ‘망자의 군주’ 언데드 킹]



짧은 이별 끝에 다시 만난 친구는 조금 달라져 있었고, 그 모습에 진태경은 헛웃음을 흘렸다.

함께 힘을 합쳐 아크 리치를 쓰러트린 과거의 그 날을 떠올리며.

“많이 컸네, 우리 골골이.”

아직도 기억 속에 선명히 남아 있는 그 말을 들은 스켈레톤, 아니 언데드 킹이 천연덕스럽게 대꾸했다.

“뭐, 키야 원래 이 몸이 조금 더 컸지.”

“지랄.”

“어허, 천박하긴.”

다음 순간, 두 친구는 약속이라도 한 것처럼 소리 내어 웃었다.

잠시 헤어져 있는 동안 각자에게 벌어진 모든 일을 그들은 정확히 알지 못했지만, 한 가지는 확실했다.

그들은 서로를 믿었고, 소중한 것을 지키기 위해 싸웠다는 것.

“인간.”

“왜.”

“고생했다.”

이제는 정말 한계에 다다른 것일까. 메아리처럼 멀게만 느껴지는 친구의 음성에, 진태경이 희미한 목소리로 답했다.

“……그래, 너도.”

“편히 쉬어라.”

아마 여느 때와 같은 진태경이었다면 누가 죽기라도 하냐며 볼멘소리를 했겠지만, 지금의 그에게 허락된 시간은 여기까지였다.

쉬어라.

그 짧지만 유혹적인 제안은 모르고스의 마법보다도 강력했고, 바닥난 정신력은 이미 주인의 의지를 거스를 만반의 준비를 끝마친 뒤였으니.

툭.

기울어지는 고개와 함께 굳게 닫힌 눈꺼풀. 말이 끝나기가 무섭게 기절하듯 깊은 잠에 빠진 친구의 모습을, 언데드 킹은 물끄러미 응시했다.

차마 덧붙이지 못한 한 마디를 혼잣말처럼 뇌까리며.

“……편히 쉬기에는 너무나도 짧은 휴식이 되겠지만.”

만약 진태경의 정신력이 조금만 더 버텨 주었더라면, 이 말에 담긴 정확한 뜻을 이해했을 것이다.

아니, 구태여 자신을 통해 듣지 않더라도 스스로 깨달았을 것이 분명했다.

그가 아는 진태경은 그 고약한 성미만큼이나 놀라운 힘과 직감을 지닌 사람이니까.

하지만 어느샌가 가까워진 거구의 대마도사 역시, 특별함으로 치자면 현존하는 모든 인류를 통틀어도 손에 꼽히는 존재임은 분명했다.

“도대체. 도대체 어째서.”

혼란에 가득 찬 목소리와 흔들리는 동공.

만신창이가 된 몸을 이끌고 다가온 매직 존슨은 무언가에 홀린 듯 주위를 둘러보았다.

재회의 반가움과 승리의 기쁨 따위는 이미 뇌리에서 지워진 지 오래.

처음에는 진태경의 안위를 확인하기 위해 왔던 그였으나, 사방에서 전해지는 불길한 힘의 맥동은 그 모든 것을 잊게 만들었다.

우우우웅.

매직 존슨은 이를 악물었다.

드높은 경지에 오른 마법사이기에 더욱 선명하게 느낄 수 있는, 한없이 어둡고 늪처럼 끈적한 기운.

마력(魔力).

그것도 대격변이 절정에 달했던 수십여 년의 과거가 떠오를만큼 지극히 순수하고 밀도 높은 마력이 온 사방을 물들이고 있었다.

“……드래곤 하트.”

원인을 알아차린 인류 최후의 대마도사는 자신도 모르게 몸을 떨었다.

앞서 언데드 킹이 흡수한 방대한 마력조차 새 발의 피로 만들어 버릴 정도의, 그야말로 무한에 가까운 마력의 원천.

하지만 바로 지금 불현듯 매직 존슨의 뇌리에 떠오른 생각은, 용의 심장이 끊임없이 뿜어내는 마력보다도 어둡고 불길했다.

“설마?”

“그래.”

애써 담담하게, 그럼에도 목소리에 담긴 두려움을 감추지 못한 언데드 킹이 부풀어 오르는 어둠을 바라보며 덧붙였다.

“시작됐다. 아니, 정확히는 완성되었다고 해야겠군.”

그의 말이 옳았다.

그것은 이 거대한 퍼즐의 마지막 한 조각이자 열쇠였다.

가장 위대하고 강력했던 드래곤의 죽음으로 완성된, 또 다른 재앙의 시작.

삐빅.

오직 선택받은 자만이 들을 수 있는, 그러나 지금만큼은 어디에도 닿지 못할 서늘한 기계음이 울려 퍼진 그 순간.

구구구궁!

세상을 뒤흔드는 거대한 울림과 함께, 하늘과 땅을 잇던 마력의 기둥이 폭발했다.

마치 모든 준비를 끝마친 활화산처럼.
```

## Final English reading copy

```markdown
# Chapter 1171

It was like a jewel.

A jewel possessed of a beauty and mystery beyond any work of art in the world—or even all of them combined.

But the thing casting an ominously dark glow in every direction was no mere mineral.

Dragon Heart.

Just as its name said, it was the heart and source of power of the mighty race known as Dragons.

And now, in this moment, someone who had once been the wisest and most powerful Dragon Lord since the division of heaven and earth—and had fallen deeper into corruption than any other Dragon—was realizing that his long life had come to an end.

With his whole body. With his soul.

And with a sound ringing in his ears like thunder.

*Crack.*

Hairline fractures spread across its smooth surface like a spiderweb.

Nothing could stop the cracks in the Dragon Heart, which had barely held its shape through the master’s iron will and the last of his strength.

There was only a streak of light, bringing forward the destruction that had already been ordained.

*Crunch!*

It shattered. Split apart.

The sunset glow that had flowed along the spearhead—and the Dragon’s heart, which had never allowed anyone to touch it.

*Rumble.*

Darkness surged out in place of blood.

The surrounding air trembled, as if the world had realized what was about to happen.

But even in the moment his life was fading, the Demon Dragon’s gaze never wavered from the Divine Dragon who had driven a spearhead into his heart.

“Fight with all the strength you’ve been given. Keep surpassing yourself. Keep struggling.”

The voice that slipped out as if in soliloquy held neither regret, anger, nor a curse.

It was encouragement the listener couldn’t understand, tinged with deep disappointment.

He would miss the astonishing amusement that lay ahead.

“…So I can see it, wherever I am.”

At that moment—

*Rumble.*

Everything in the area stopped moving.

The wind. The air.

Even the Dragon’s enormous body, which had just breathed out its last after a life beyond imagining.

And then—

*Whooooom!*

The Dragon Heart spilled the millennia of time and nearly infinite magical power stored within it in every direction.

* * *

Darkness and brilliance should never coexist.

But for that moment at least, everyone on the battlefield saw and felt it clearly:

A pillar of dazzling darkness surging skyward, and an enormous power erupting as it shook the whole world.

And the first to experience it—and the one closest to it—was, naturally, Jin Taekyung.

*Whoosh—*

From the moment he faced the pitch-black darkness that covered his vision in an instant, he didn’t need to think anymore.

Jin Taekyung moved on instinct alone.

As he pulled his spearhead from the Dragon’s heart, he cradled the Skeleton King’s head—recovered at last—deep in his arms and curled up like a fetus.

Then he felt the wave of magical power crash over him, tearing through the brief silence.

*Rumble, rumble!*

A deafening roar filled his ears, and the world turned upside down.

The sky and earth spun around and around, making his vision reel, while a feeling of weightlessness took hold of his entire body.

But Jin Taekyung managed to stay conscious through the chaos thanks to his own iron will—and the clear sound of bells that even the roar couldn’t drown out.

*Ding. Ding. Ding.*

> **System**
>
> You have defeated Lv. 195 “Black Dragon Duke” Morgoth!
>
> You have achieved the great feat Dragon Killer!
>
> Achievement Reward has been granted!
>
> You have gained a tremendous amount of EXP!
>
> Your Intimidation has increased significantly!
>
> You have acquired the Title Dragon Slayer!
>
> All abilities are greatly increased when fighting dragonkin. If you ever encounter another Dragon, how it treats you will depend on its disposition.
>
> Level Up!
>
> Level Up!
>
> Level Up!
>
> Level Up!
>
> All injuries and status effects have been healed!

System notifications.

The clearest proof that he had survived yet another crisis.

Maybe that was why Jin Taekyung was about to let go of the thread of consciousness he’d been holding onto with all his might.

*I want to rest.*

That was all he could think about.

He didn’t care what happened next.

His body was still flying off into the distance like a cannonball, but what did that matter?

Morgoth had certainly met his death, and the countless monster armies had been utterly shattered and reduced to prey.

Even if he crashed into something and broke a few bones, he’d be fine.

No—he might not even feel pain.

If he closed his eyes now, he would fall straight into a deep sleep that could easily drown out any physical pain.

With everything over, there was nothing to keep him from resting.

*Right. Nothing.*

At least, that was what Jin Taekyung was sure of.

Until he heard someone’s voice in his ear, just before he let his terribly heavy eyelids fall shut.

“Damn it. This is awful.”

At first, he thought he’d imagined it.

Or that the howling wind had made him hallucinate.

But neither was true.

He wasn’t asleep yet, and the voice that followed was so clear it proved all of this was real.

“To wake up in the arms of some guy reeking of sweat. Just my luck.”

The gruff voice was all the more welcome for it. Jin Taekyung forced his eyes open with every ounce of strength he had.

He stared blankly at the owner of the voice, who had somehow awakened in his arms, then suddenly opened his mouth.

“You can’t smell anything. You’re undead.”

“…You bastard.”

A brief silence, then a single curse.

But an unmistakable laugh crept into the words, and golden energy running across the brow of the pure-white skull burned like a torch.

Feeding on the Dragon’s magical power spilling in every direction, it blazed more fiercely than ever.

*Whoosh!*

In an instant, the thick darkness that had spread on the wind shot toward Jin Taekyung.

No—to be precise, the being in his arms was sucking it in.

As if rain awakened life, the sun gave it strength, and the earth nourished its growth.

*Fwoosh.*

The more darkness seeped in, the clearer the golden energy became.

And beyond those two contrasting streams of color, a shadow steadily grew.

It was a wondrous sight unlike anything anyone had ever seen.

Regeneration. Resurrection.

Perhaps even a new birth.

But the thing that grew by devouring all the darkness around it was no ominous presence.

Even if someone else might point at him and curse him, Jin Taekyung would never see him that way.

He shone as brightly as that radiant golden crown.

*Rustle.*

Jin Taekyung blinked.

The dizzying world had stopped spinning, and the wind that had whipped past like blades was gone.

Through his dreamlike, hazy consciousness, he could make out only the familiar touch of someone carefully laying him on the ground, and a single line of text hovering above that person’s head.

[Lv. 180 “Lord of the Dead” Undead King]

The friend he’d met again after a brief farewell had changed a little. Jin Taekyung let out a hollow laugh at the sight.

He thought of that day long ago, when the two of them had joined forces to defeat the Arch Lich.

“You’ve grown a lot, Bones.”

The Skeleton—or rather, the Undead King—replied as casually as ever to words that still stood clear in his memory.

“Well, I was always a little taller.”

“Bullshit.”

“Now, now. How vulgar.”

The next moment, the two friends laughed aloud as if they’d planned it.

They didn’t know exactly what had happened to each other while they were apart, but one thing was certain.

They trusted each other, and they’d fought to protect what they held dear.

“Human.”

“What?”

“You’ve been through a lot.”

Maybe he really had reached his limit. Jin Taekyung answered in a faint voice, the sound of his friend’s words seeming to echo from far away.

“…Yeah. You too.”

“Rest easy.”

If Jin Taekyung had been his usual self, he would have grumbled, “What, is someone dying?” But this was as far as he could go.

Rest easy.

That short, tempting offer was more powerful than Morgoth’s magic, and his exhausted mind was already poised to defy his will.

*Thump.*

His head drooped, and his eyelids shut tight. The Undead King watched as his friend sank into a deep sleep, as if he’d passed out the instant the words were spoken.

Then he murmured, as if to himself, the words he hadn’t quite been able to add.

“…It’ll be far too short a rest for you to rest easy.”

If Jin Taekyung’s will had held out just a little longer, he would have understood exactly what those words meant.

No—he surely would have figured it out on his own, even without hearing it from him.

The Jin Taekyung he knew had power and instincts as remarkable as his foul temper.

But the gigantic Grand Mage who had drawn near without anyone noticing was also, beyond a doubt, one of the most remarkable beings among all of humanity.

“Why? Why on earth?”

His voice was full of confusion, and his eyes wavered.

Magic Johnson, dragging his battered body along, looked around as if under a spell.

The joy of reunion and the thrill of victory had long since vanished from his mind.

He’d first come to check on Jin Taekyung, but the ominous pulse of power coming from every direction made him forget all of that.

*Rumble.*

Magic Johnson gritted his teeth.

A mage who had reached such a high realm could sense it all the more clearly: a boundlessly dark, swamp-thick energy.

Magical power.

So pure and dense that it called to mind the decades-old past, when the Great Cataclysm had reached its height, it was staining everything around them.

“…Dragon Heart.”

The last Grand Mage of humanity trembled before he knew it, having realized the cause.

A source of magical power so nearly infinite that it made even the vast power the Undead King had absorbed seem like a drop in the bucket.

But the thought that had suddenly occurred to Magic Johnson was darker and more ominous than the magical power the Dragon Heart continued to pour out.

“Surely…?”

“Yes.”

The Undead King tried to sound calm, but couldn’t hide the fear in his voice as he gazed at the swelling darkness and added,

“It’s begun. No—more precisely, it’s been completed.”

He was right.

It was the final piece and the key to this enormous puzzle.

The beginning of another catastrophe, completed by the death of the greatest and most powerful Dragon.

*Beep.*

At that instant, a cold mechanical tone rang out—one that only the chosen could hear, yet now reached no one.

*Rumble, rumble!*

With a tremendous roar that shook the world, the pillar of magical power connecting heaven and earth exploded.

Like an active volcano that had finished making all its preparations.
```
