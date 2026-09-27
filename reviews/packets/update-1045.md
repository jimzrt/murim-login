<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1045.txt",
      "sha256": "3d7aac41afb4317d74fee3e6f71e73cd51070b28db4d8a5bb29b0ca2f7216249",
      "bytes": 13373
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "c73bcd3fec8881085068197c0cfb69992886dc3f71a05c75437a09d1235e6e62",
      "bytes": 2316
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "91edff1ea0e7f2d1bdf20f77998a86f250b89f1bc3f043cd106289bea1e118b4",
      "bytes": 240895
    },
    {
      "path": "characters/Blood-Sword Demon Lord.md",
      "sha256": "7904e1644dca9cdea2fd7d5ac536baf99036e6c83dad09ba92691b93437f935f",
      "bytes": 914
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "7abdfe5b182458b21c1673ed8b6e9c5aa5e56e28d305460f08c1a295b12a3fae",
      "bytes": 760
    },
    {
      "path": "characters/Grand Mage.md",
      "sha256": "2a338a4046454b358b76eb4664ebe65aa2c44fa49a66f1046eb1f74008b0cdf9",
      "bytes": 549
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "388dc5cb719a565b81ed426b066a5cfd16cd5c83338f233df4d3872525eab926",
      "bytes": 1502
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "5b9053549777d776dccf6ff0c8037d9a5be9efff52ada7c1728803a4be00fb1e",
      "bytes": 1823
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "f49496e0b4236d2b63f903acd14777aa37ad56e7b8c143acb8d872d8faea6035",
      "bytes": 623
    },
    {
      "path": "characters/Sima Gong.md",
      "sha256": "04f7147f5fd104ffda1b9a0463f26ef52443f323a6fd177bbee63735b3d95a5c",
      "bytes": 778
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "e352fbeddc440de548677bd122eec9e46a97219f0018ab1bff7c9cc1089c0938",
      "bytes": 280765
    }
  ],
  "estimated_tokens": 11621
}
-->

# Durable State Update — Chapter 1045

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
1 and safe_through 1045. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1045. Profile updates may replace only one
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
  "chapter": 1045,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1045,
    "continuity_sources": [1045],
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
    "The Blood-Sword Demon Lord serves the Lord of Heaven and commands the invading army.",
    "Jeok Cheongang is injured but holding off the Blood-Sword Demon Lord while Jin Taekyung targets the mages.",
    "Fire Dragon Armor is severely damaged, stored in Inventory, and unavailable until its automatic repair completes in three days.",
    "Repeatedly dispelling the white-robed mages’ varied Magic causes energy backlash that incapacitates them; nineteen have fallen, and their veiled leader, the Grand Mage, remains.",
    "The Grand Mage’s Hell Fire is a vast sphere capable of killing thousands; Jin’s incomplete One Annihilation failed to break all the Grand Mage’s barriers, leaving him alive but severely exhausted, with an empty dantian and damaged acupoints.",
    "Jin’s White Flame spear throw bends part of the Hell Fire sphere’s course and opens a rift in its flames, but does not stop it; other fighters’ attacks have an unknown result.",
    "The Wind-and-Cloud Sword Lord is badly wounded and refused to retreat; his two Senior Brothers urged him to withdraw after securing a way out.",
    "The two Black Ghosts facing the Wind-and-Cloud Sword Lord were disrupted by a shock wave; the chapter confirms that he defeated them.",
    "Hyuk Sopyung is leading Zhongnan’s surviving disciples.",
    "Song Il and Hwangbo Eom accepted Sima Gong’s transaction to pursue revenge against the Fire Gate Clan and protect Zhongnan; they regret it and face the approaching Hell Fire sphere, with their fate unknown."
  ],
  "continuity_sources": [
    1043,
    1044
  ],
  "open_questions": [
    "What are the identity and purpose of the Lord of Heaven?",
    "Did Dark Heaven cause the Great Faction War?",
    "Who are the white-robed mages, and what is their purpose?",
    "How were the former Demonic Cult fiends made into Black Ghosts?",
    "What happens to the Hell Fire sphere, Jin Taekyung, Song Il, and Hwangbo Eom?"
  ],
  "safe_through": 1044,
  "temporary_decisions": [
    "Render 대마도사 as Grand Mage.",
    "Use Fire Ball, Stone Wall, and Magic Arrow for the named spells.",
    "Render 헬 파이어 as Hell Fire; use hellfire for descriptive 겁화.",
    "Render 쇄월검진 as Moon-Shattering Sword Formation."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 사마공    | **Sima Gong**      |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 궁성     | **Bow Saint**                 | —              |
| 열화문    | **Fire Gate Clan**               |
| 암천     | **Dark Heaven**                  |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 사파     | **unorthodox faction**                           |                                                       |
| 제자     | **Disciple**                                 |
| 화신귀무   | **Dance of the Fire God and Demon** |
| 귀가      | **your family**                                                 |
| 도사      | **Daoist**                                                      |
| 혈검마군 | **Blood-Sword Demon Lord** | Antagonist commanding the army advancing on the Great Snow Mountain. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 선천지기 | **innate qi** | Vital energy said to be damaged by the pill's aftereffects. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 광염 | **light-flames** | Violet manifestation surrounding Cheongpung when he uses the Zaha Divine Technique. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 이형환위 | **Shifting Form and Position** | Supreme Peak movement or evasion technique used by Jeok Cheongang. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 염화일로 | **Flamefire Path** | Fire Gate Clan signature movement technique; Jeok Cheongang has reached its ninth stage. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 창룡후 | **azure dragon's roar** | Battle cry released by Tang Jinhu. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 창룡 | **Azure Dragon** | Divine dragon form invoked in Hyeongong's blessing. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 흑야왕 | **Black Night King** | Epithet of Sima Gong, Sama Pyo's father and the Sect Leader who built the modern Black Dragon Demon Gate. |
| 도산검림 | **a mountain of sabers and a forest of swords** | Idiom describing the lethal life of martial artists. |
| 검마 | **Sword Demon** | A Demonic Cult swordsman whose final technique is compared with One Annihilation. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 대술사 | **Grand Mage** | Title of the veiled woman leading the white-robed mages. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 사마공 | 적천강 | unorthodox sect leader to senior martial master | Senior | formal and deferential | Greets Jeok Cheongang as 노선배. |
| 적천강 | 사마공 | senior martial master to longtime martial acquaintance | you | blunt and familiar | Uses direct, contemptuous language while teasing Sima Gong. |
| 진태경 | 사마공 | allied young martial artist to unorthodox sect leader | Great Hero Sima | polite and deferential | Addresses him as 사마 대협. |
| 사마공 | 진태경 | unorthodox sect leader to celebrated young martial artist | you | polite and familiar | Uses 자네 while speaking to Taekyung. |
| 혈검마군 | 적천강 | former opposing martial masters | Senior Jeok | respectful and familiar | Addresses Jeok as 선배 while teasing him. |
| 적천강 | 혈검마군 | former opposing martial masters | you; you bastard | blunt and hostile | Uses 너 and 네놈 while confronting him. |
| 혈검마군 | 진태경 | enemy addressing a younger martial artist | you | familiar and measured | Uses 자네 while praising and assessing Taekyung. |
| 진태경 | 혈검마군 | young martial artist confronting an enemy | you | casual and challenging | Questions when the Blood-Sword Demon Lord and the Lord of Heaven appeared. |
| 대마도사 | 진태경 | adversary_to_adversary | you | polite, teasing | She uses polite phrasing while taunting him and warning him not to overexert himself. |
| 진태경 | 대마도사 | adversary_to_adversary | you bitch | insulting-casual | He curses at her while refusing to give up. |

## Listed compact profiles

### Blood-Sword Demon Lord.md

# Blood-Sword Demon Lord (혈검마군)

- **Safe through:** Chapter 1041
- **Aliases:** None
- **Role:** The Blood-Sword Demon Lord is a formidable martial master who commands the force advancing on the Great Snow Mountain and now serves the Lord of Heaven.
- **Personality:** Devoted to his master and proud of his abilities, he is deeply wounded by perceived distrust and resolves to prove his worth.
- **Voice:** Casually familiar and self-amused, addressing Jeok Cheongang respectfully as Senior while trading blunt insults; his easy laughter can turn to a low, cold intensity.
- **Relationships:** He serves the Lord of Heaven with deep devotion but believes his master does not fully trust him; he has been ordered not to kill Jin Taekyung, admires Jeok Cheongang, and once shared the Demonic Cult with the fiends who became Black Ghosts.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1044
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Grand Mage.md

# Grand Mage (대마도사)

- **Safe through:** Chapter 1043
- **Aliases:** None
- **Role:** The Grand Mage leads the white-robed mages and is a formidable mage who has reached the edge of truth.
- **Personality:** She remains composed while taunting Jin and appears pleased and excited to meet him.
- **Voice:** Calm and politely phrased, with teasing remarks and a hint of excitement.
- **Relationships:** She commands the white-robed mages and is an adversary of Jin Taekyung.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1044
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1044
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him and feels no fear when Taekyung is with him; Taekyung trusts Sama Pyo and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1044
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Sima Gong.md

# Sima Gong (사마공)

- **Safe through:** Chapter 1044
- **Aliases:** Black Night King
- **Role:** Sima Gong is the Sect Leader who built the Black Dragon Demon Gate into a major unorthodox power and the father of its Young Sect Leader, Sama Pyo.
- **Personality:** Sly and calculating yet outwardly gentle; he calmly accepts sacrificing the rear population as the cost of a strategy he believes offers the best odds of victory.
- **Voice:** Polished and persuasive, with smooth rhetorical turns and a composed, gently teasing manner.
- **Relationships:** Sama Pyo is his youngest son among seven older brothers and nine older sisters; he is personally familiar with Jeok Cheongang, who openly dislikes him.

## Korean source

```text
＃1045화



종류와 용도에 상관없이, 마법의 위력을 한계까지 끌어올릴 수 있는 조건은 크게 두 가지로 나뉜다.

첫 번째. 시전자의 강대한 마나.

두 번째. 그 마나를 가장 효율적으로 결집하고 방출할 수 있는 마법진(魔法陳).

그렇기에 대마도사, 혹은 대술사라 불리는 그녀의 마법은 더할 나위 없이 완벽할 수밖에 없었다.

수없이 두드리고 식힌 끝에 명검이 탄생하듯, 마법 또한 충분한 시간과 공을 들일수록 그 위력을 극대화할 수 있는 법.

언덕 밑이 피로 물드는 동안 이미 완성되어 있던 마법진의 발동은 그 누구도 막을 수 없었고, 저 거대한 화염의 구가 어느 정도의 위력을 지녔는지 짐작하고 있는 이는 진태경 한 사람뿐만이 아니었다.

화아아아악!

세상이 느려진다.

빛이, 불길이 서서히 번져 간다.

아직 지면에 닿기까지는 이 장의 거리가 남아 있었음에도, 불덩어리로부터 흘러나오는 열기는 끔찍하리만치 강했다.

그리고 온 사방의 바람과 습기를 집어삼킨 화염의 그늘이 전장의 일부를 뒤덮으며 드리워지는 광경을, 화왕(火王) 적천강은 아연한 시선으로 바라보았다.

‘이것이…… 마법(魔法).’

사술(邪術)이라는 두 글자는 지금 이 순간 그의 뇌리에서 지워진 지 오래였다.

그래, 이건 그야말로 마법이다.

인간이 아닌 마귀가 부리는 술법. 이보다 더 적절한 표현은 존재하지 않는다는 것을 적천강은 알고 있었다.

더불어 지금 이 순간, 저 강력한 힘의 폭발을 막을 수 있는 사람은 이제 자신뿐이라는 사실 역시도.

퍼엉!

발끝에서 터져 나온 화염과 함께 섬광과도 같은 속도로 쏘아지는 신형.

그러나 염화일로(炎火一路)를 펼치며 불덩어리를 향해 나아가던 적천강은, 이내 등 뒤에서 울려 퍼진 섬뜩한 파공성에 황급히 고개를 숙여야만 했다.

쉬이이잉! 서걱!

불현듯 뜨거워지는 뒤통수.

마치 솜씨 좋은 백정이 고기를 저미듯, 머리카락과 일부 살가죽을 얇게 베어 낸 검붉은 강기가 적천강의 머리를 스쳐 지나가 허공을 갈랐다.

“어딜 그리 급하게 가시나.”

회피를 위해 발끝이 흔들린 찰나의 순간, 어느덧 이형환위(移形換位)를 뛰어넘는 속도로 앞을 가로막은 인간 백정의 모습에 적천강은 입술을 깨물었다.

“혈검마군(血劍魔君), 네놈이 감히……!”

“감히? 그 꼴이 되고서도 아직도 감이 안 잡힌 모양이군.”

혈검마군은 웃으며 손에 쥔 검을 흔들었다.

치열한 격전 끝에 피투성이가 된 적천강과 달리, 몇 군데에 미비한 부상만을 입은 그는 이제 완전히 확신하고 있었다.

명백한 힘의 차이를.

자신의 우위를.

“당신은 막지 못해. 아무것도.”

슈확!

일순간 아지랑이처럼 흐릿해진 검신이 바람을 찢으며 달려들었다.

쾅, 쾅, 콰아아앙!

실로 상상을 초월하는 속도와 파괴력.

거대하게 솟아오른 강기가 사방을 후려치고 터트린다.

숨을 몰아쉬는 것조차 잊은 채, 자신을 향해 퍼부어지는 공격들을 아슬아슬하게 피해 내던 적천강의 눈빛이 깊게 가라앉았다.

‘아무것도 막지 못한다, 라. 그래, 분명 그렇겠지.’

단지 불같은 성정만을 지녔더라면, 화왕이라는 별호는 이미 이 세상에서 지워졌을지도 모른다.

그러나 적천강은 무림이라는 도산검림 속에서 지금껏 끈질기게 살아남았고, 지금 같은 생사의 기로 앞에서도 냉정하게 현실을 직시하고 있었다.

자신의 앞을 가로막은 혈검마군을 지나, 아직 지면에 닿지 않은 저 끔찍한 재앙을 막을 수 있는 단 하나의 길 역시도.

‘화신귀무(火神鬼舞).’

그래, 남은 선택지는 오직 그뿐이었다.

죽음을 각오하고 펼치는 불귀신의 마지막 춤사위.

열화문의 시작이자 끝. 가장 격렬한 불길이자 마지막 잿가루.

이 세상에 영원히 타오르는 불길은 없다. 춤이 끝나면 열기는 사그라지고 육신은 타들어 간다.

강한 불씨를 품은 자일수록 그 위력은 배가 되고, 거세진 불길을 감당하기 위해서는 더욱 많은 생명력을 장작으로 던져 넣어야 하는 법.

‘이번이 마지막이 되겠군.’

화왕 적천강은 본능적으로 직감했다.

이제부터 시작될 춤사위가 자신에게는 세 번째이자 마지막이 되리라는 것을.

그 어느 때보다 강력한 열양지기를 품게 된 이 육신이 이번만큼은 견디지 못하리라는 것을.

그러나 후회는 없었다.

비록 이 육신이 잿더미가 되어 흩날리더라도, 그가 남긴 불씨는 그곳에 남아 있을 테니까.

화왕 적천강의 불길이 사그라지더라도, 열화신룡 진태경이라는 불씨는 세상 어딘가에서 더욱 크게 타오를 테니까.

그러니…….

‘그것으로, 되었다.’

마음속으로 작게 뇌까린 적천강은 신형을 비틀었다. 사방을 빼곡하게 뒤덮은 강기의 그물을 피해 내며 자신에게 지닌 모든 기운을 끌어올렸다.

유구한 세월 동안 쌓아 올린 수 갑자의 열양지기.

그리고 무림인들에게 있어서는 금단의 영역이나 다름없는, 몸속 깊숙한 곳에 잠든 선천지기(先天眞氣)를 마침내 일깨웠다.

아니, 정확히는 일깨우려 했다.

바로 그 순간, 어디선가 날아든 거대한 묵빛 강기가 혈검마군을 막아서기 전까지는.

후웅, 콰아아앙!

힘과 힘, 강기와 강기의 격돌.

굉음과 함께 주변의 대기가 요동친다.

자욱하게 피어오르려는 먼지구름을 단숨에 갈라 내며 모습을 드러낸 혈검마군이 불청객의 정체를 확인하고 눈살을 찌푸렸다.

“……네놈이 어찌.”

“가시오, 화왕.”

굳게 닫혀 있던 입술 사이로 문득 흘러나온 메마른 음성.

불청객. 아니, 흑야왕(黑夜王) 사마공은 혈검마군에게 시선을 고정한 채 등 뒤의 적천강을 향해 담담하게 덧붙였다.

“내 마음이 바뀌기 전에.”

“……!”

이 생각지도 못한 등장에 적천강의 눈이 크게 뜨였다.

배신자라고 생각했던 사마공이다.

아니, 확신이라고 해도 무방했다.

그렇기에 당장 묻고 싶은 것도, 하고 싶은 말도 있었다.

하지만 적천강에게 주어진 시간은 터무니없이 짧았고, 그는 그 모든 것을 뒤로한 채 다시 지면을 박찼다.

외마디 전음(傳音)을 흘리듯 남겨 둔 채로.

- 살아남거라. 이 더러운 사파 잡놈아.

돌아오는 대답은 없었다.

그저 염화일로를 따라 거칠게 전신을 휩쓰는 바람과 그 바람 사이를 떨어 울리는 무시무시한 굉음과 고함이 있을 뿐이었다.

“네깟 놈이 감히-!”

콰아아앙!

사방의 대기가 요동쳤고, 단지 그뿐이었다.

등 뒤에서 날아든 혈검마군의 강기를 사마공이 가까스로 가로막았음을 깨달은 적천강은 이를 악문 채 더욱 속도를 높였다.

촌각.

사마공이 지금의 혈검마군을 상대로 버틸 수 있는 것은 고작해야 촌각이다.

어쩌면 단 수십 합 만에 목숨을 잃을지도 모른다.

그러나…….

‘그것으로 충분하다.’

손가락 한 마디의 길이로 생사가 오가고, 찰나를 쪼개고 쪼갠 순간의 격차로 운명이 뒤바뀐다.

그것이 무림이고, 초인들의 세계니까.

콰드득.

온 힘을 다해 내뻗은 발끝을 따라 지면이 주저앉는다. 세상이 느려지고, 새하얀 불길이 솟구쳤다.

꽈앙!

빛보다 빠르게 움직이는 화염은 없다.

그러나 지금 이 순간, 단숨에 수십여 장을 가로지른 적천강에게 주어진 한계란 없었다.

다만 그를 구속하는 유일한 사슬이 있다면, 그것은 바로 시간뿐이었다.

‘빌어먹을!’

적천강은 당장이라도 입술을 비집고 터져 나오려는 신음을 삼켰다.

그 어느 때보다 빠른 속도로 폭발하듯 쏘아지는 그의 신형이 향하는 그 끝에는 거대한 화염의 구가 있었다.

이제는 불과 일 장도 남지 않은 허공에서 모두의 머리 위를 뒤덮어 내리고 있는, 끔찍할 정도로 강렬한 화염이.

‘더, 조금만 더……!’

하지만 그의 간절한 바람과 달리, 현실은 잔인하리만치 순리를 따라 움직이고 있었다.

화아아악.

뜨겁다.

이십여 장이나 떨어진 거리임에도 불구하고 숨이 막혀 온다.

지면과 맞닿기 전, 마침내 크게 부풀어 오르는 화염을 보며 적천강은 문득 생각했다.

자신에게 단 몇 초의 시간만 더 주어졌더라면.

저것과의 거리가 십여 장이라도 더 가까웠더라면.

그리고…….

적천강 자신이나 진태경이 아닌, 재앙을 막을 수 있는 또 다른 누군가가 이 자리에 있었다면.

‘제기랄.’

적천강은 이를 악물었다. 마지막 힘을 쥐어 짜내어 신형을 내뻗었다.

안다.

이 거대한 폭발을 막기에는 이미 늦어 버렸다는 것을.

하지만 그럼에도 나아가야 했다.

비록 정(正), 사(邪), 마(魔) 어디에도 속하지 않았으나, 이것이 자신이 택한 길이었으니까.

이렇게라도 하지 않는다면, 천둥벌거숭이 같은 제자 놈의 얼굴을 제대로 마주할 수 없을 것 같았으니까.

“오너라-!”

사방을 떨어 울리는 창룡후(蒼龍吼)를 터트리며, 화왕 적천강은 이십여 장 밖의 재앙을 향해 온 힘을 다한 일권을 내질렀다.

그리고 다음 순간, 똑똑히 보았다.

동시에 들었다.

쉬이이이잉!

멸염신권(滅炎神拳)으로 말미암은 백색의 광염이 폭발하듯 쏘아진 그때, 그보다 앞서 어두운 하늘을 환하게 밝히며 공간을 가로지르는 휘황한 빛줄기를.

거대하게 부풀어 오른 화염의 구를 파고드는, 그 눈부신 벼락들을.

고오오옹.

마치 멈춰 버린 듯한 세상 속, 빛과 화염이 뒤섞인 아득한 섬광이 이내 모두의 시야를 새하얗게 물들였다.



* * *



하늘이, 땅이 갈라졌다.

모두가 알고 있던 세상 대신, 빛으로 이루어진 신세계가 열렸다.

적어도 그 순간만큼은, 비단 진태경만이 아니라 전장의 모두가 그렇게 느꼈을 것이다.

‘이건 설마…….’

화아아.

진태경이 마지막 순간 보았던, 믿을 수 없는 광경을 온전히 떠올리기도 전.

그는 아득하게 물들었던 시야가 서서히 되돌아오는 것을 느꼈다.

그리고 모두가 눈 앞을 가렸던 새하얀 섬광이 사라진 빈자리를 채운 것은, 뒤늦게 찾아온 엄청난 굉음과 전장 곳곳에서 솟구쳐 오르는 불길이었다.

콰앙! 콰아아앙!

쿠구구구궁!

하늘 위의 태양이 비가 되어 쏟아진다면 이런 광경일까.

크고 작은 수백 개의 불덩어리가 반경 일백여 장을 뒤덮으며 떨어져 내리고 있었다.

나약하기 그지없는 인간의 살과 뼈를 짓뭉개고, 지면을 녹이고, 핏물과 뒤섞인 눈을 증발시켰다.

헬파이어라는 뜻 그대로, 죽음의 불꽃처럼.

그러나 그 죽음은, 전장의 모두에게 평등한 것이 아니었다.

“아.”

불현듯 입술 사이를 비집고 흘러나온 신음은 진태경의 것이 아니었다.

대마도사, 혹은 대술사라 불리는 그녀는 언덕 아래에 펼쳐진 불지옥을 말없이 바라보았다.

정확히는, 비명조차 내지르지 못한 채 숯덩이가 되어 쓰러져 가는 암천의 교도들을.

‘어째서?’

같은 아군이 끔찍한 죽음을 맞이하고 있다는 것에 대한 슬픔 따위는 없었다.

그저 순수한 의문만이 있었을 뿐.

적들의 한복판에서 폭발했어야 할 불덩어리가 어찌하여 조각조각 난 채 아군들을 휩쓸고 있는지.

어림잡아도 수천에 달하는 사상자 중, 왜 적들의 숫자는 일백도 되어 보이지 않는지.

그녀의 머릿속에는 오직 그에 대한 의문만이 가득했고, 마지막 순간 적천강만을 주시하고 있던 대마도사와는 달리 모든 것을 시야에 담고 있던 또 다른 누군가는 이미 그 의문에 대한 답을 알고 있었다.

“더럽게 늦게 왔네.”

“뭐?”

등 뒤에서 불현듯 울려 퍼진 목소리에, 무심코 고개를 돌린 대마도사는 볼 수 있었다.

힘없이, 그러나 선명하게 웃고 있는 진태경을.

그녀의 어깨너머, 저 멀리 어딘가를 응시하고 있는 그의 눈동자에 어렴풋이 비친 황금빛 무언가를.

“빌어먹을 할망구.”

“……!”

그 순간. 무언가 깨달은 대마도사는 황급히 돌아섰다.

그리고 동시에 자신이 품었던 의문에 대한 답을 두 눈으로 똑똑히 보았다.

쉬이이잉!

앞서 불덩어리를 찢어발긴 빛줄기, 아니 강기의 화살을.

“궁성(弓星)……!”
```

## Final English reading copy

```markdown
# Chapter 1045

Regardless of its type or purpose, there were two main conditions for bringing a spell’s power to its limit.

First: the caster’s immense mana.

Second: a magic circle capable of gathering and releasing that mana with the greatest efficiency.

That was why the magic wielded by the woman known as the Grand Magecould only be utterly perfect.

Just as a masterwork sword was born after countless rounds of hammering and quenching, magic, too, could reach its greatest power when enough time and effort were devoted to it.

While the hillside below was turning red with blood, the spell circle that had already been completed began to activate. No one could stop it. And Jin Taekyung wasn’t the only one who had some idea of the power contained in that enormous sphere of flame.

Fwoooooosh!

The world slowed.

Light and flame spread, slowly.

The fireball was still two *jang* from the ground, but the heat pouring from it was already horrifyingly intense.

The shadow of the flames, having swallowed the wind and moisture all around, stretched over part of the battlefield. Fire King Jeok Cheongang watched it descend with stunned eyes.

*So this is… Magic.*

The words *dark arts* had long since vanished from his mind.

Yes. This was Magic.

A spell wielded not by a human, but by a demon. Jeok Cheongang knew there could be no more fitting description.

He also knew that, at this very moment, he was the only one left who could stop that powerful explosion.

Boom!

Flames burst from his toes as he shot forward at the speed of a flash.

But as Jeok Cheongang charged toward the fireball with the Flamefire Path, a chilling whistle rang out behind him. He had to duck in a hurry.

Shwoooosh! Slice!

The back of his head suddenly grew hot.

Like a skilled butcher slicing meat, a streak of dark-red Force skimmed past Jeok Cheongang’s head, slicing off a thin layer of hair and skin before cutting through the air.

“Where are you in such a hurry to go?”

His toes shifted for the briefest instant as he dodged. By then, the butcher of a man had appeared in front of him at a speed beyond Shifting Form and Position. Jeok Cheongang bit his lip.

“Blood-Sword Demon Lord, how dare you…!”

“How dare I? After ending up in that state, you still don’t get it?”

The Blood-Sword Demon Lord smiled and gave the sword in his hand a shake.

Unlike Jeok Cheongang, who was covered in blood after their fierce battle, he’d suffered only a few minor wounds. Now he was utterly certain.

Of their obvious difference in strength.

Of his own advantage.

“You can’t stop it. Nothing.”

Shwaaak!

His sword turned hazy like a heat shimmer and rushed in, tearing through the wind.

Bang! Bang! KWA-BOOOOM!

Its speed and destructive power defied imagination.

Force surged up like a giant wave, striking and shattering everything around them.

Jeok Cheongang barely dodged the attacks raining down on him, not even taking time to catch his breath. His eyes grew still.

*I can’t stop anything, huh? Yes, I suppose that’s true.*

If he’d possessed nothing but a fiery temper, his title of Fire King might already have been erased from the world.

But Jeok Cheongang had survived this long amid the mountain of sabers and forest of swords that was the Murim, and even at a moment like this, with life and death hanging in the balance, he faced reality with a cool head.

There was only one way past the Blood-Sword Demon Lord blocking his path—and one way to stop the terrible calamity that had yet to reach the ground.

*Dance of the Fire God and Demon.*

Yes. That was his only choice.

The final dance of a fire demon, performed with death already accepted.

The beginning and end of the Fire Gate Clan. The fiercest blaze—and the final ashes.

There was no flame in this world that burned forever. When the dance ended, the heat would fade and his body would burn to ash.

The more powerful the spark within, the greater its blaze. And to endure that growing fire, one had to throw ever more of one’s life into it as kindling.

*This will be the last time.*

Fire King Jeok Cheongang knew it by instinct.

The dance about to begin would be his third—and his last.

This body, holding more Scorching Yang Qi than ever before, wouldn’t survive it this time.

But he had no regrets.

Even if his body turned to ash and scattered, the spark he left behind would remain.

Even if Fire King Jeok Cheongang’s flames died out, the spark called Jin Taekyung, the Blazing Flame Divine Dragon, would burn brighter somewhere in the world.

So…

*That’s enough.*

Jeok Cheongang murmured to himself and twisted his body. He evaded the dense net of Force covering every direction and drew up every last bit of energy he possessed.

The Scorching Yang Qi he’d accumulated over countless years—several *jiazi*’ worth.

And at last, he awoke the innate qi sleeping deep inside his body, a forbidden realm for martial artists.

No—more precisely, he tried to awaken it.

At that very moment, a massive jet-black Force came flying from somewhere and blocked the Blood-Sword Demon Lord.

Whooom—KWA-BOOOOM!

Power clashed with power, Force with Force.

A thunderous crash sent the air around them into turmoil.

The Blood-Sword Demon Lord emerged, parting the cloud of dust that was about to rise in an instant. He recognized the intruder and frowned.

“…Why are you here?”

“Go, Fire King.”

The dry words slipped between his firmly closed lips.

The intruder—no, Black Night King Sima Gong—kept his eyes fixed on the Blood-Sword Demon Lord as he calmly added, addressing Jeok Cheongang behind him,

“Before I change my mind.”

“……!”

Jeok Cheongang’s eyes widened at this unexpected appearance.

Sima Gong—the man he’d thought was a traitor.

No, he’d been certain of it.

There was so much he wanted to ask him, so much he wanted to say.

But Jeok Cheongang had almost no time. He put all of it aside and sprang forward again, leaving only a short Sound Transmission behind.

*Stay alive, you filthy unorthodox bastard.*

There was no answer.

Only the wind that tore across his whole body as he followed the Flamefire Path, and the terrifying crashes and shouts that rang out through it.

“How dare a bastard like you—!”

KWA-BOOOOM!

The air around them shook. That was all.

Jeok Cheongang realized that Sima Gong had barely blocked the Blood-Sword Demon Lord’s Force from behind him. Gritting his teeth, he pushed himself to go faster.

A few moments.

That was all Sima Gong could hold out against the Blood-Sword Demon Lord as he was now.

He might lose his life in only a few dozen exchanges.

But…

*That’s enough.*

A single finger’s breadth could decide life and death, and a gap of a split second—divided and divided again—could change one’s fate.

That was the Murim. The world of superhumans.

Crack!

The ground sank beneath Jeok Cheongang’s toes as he pushed off with all his strength. The world slowed, and pure-white flames surged up.

BANG!

No flame could move faster than light.

But in that instant, Jeok Cheongang crossed dozens of *jang* in a single bound. Nothing could hold him back.

If one chain bound him, it was time alone.

*Damn it!*

Jeok Cheongang swallowed the groan threatening to break from his lips.

His body shot forward in an explosion of speed, heading straight for the enormous sphere of flame.

It was less than one *jang* away from the ground now, a terrible blaze spreading over everyone’s heads.

*Just a little farther…!*

But no matter how desperately he wished otherwise, reality followed its cruel course.

Fwoooooosh.

Hot.

Even from more than twenty *jang* away, it was hard to breathe.

Watching the flames swell at last before they touched the ground, Jeok Cheongang suddenly thought:

If only he’d had a few more seconds.

If only he’d been a dozen *jang* closer to it.

And…

If only someone other than Jeok Cheongang or Jin Taekyung were here—someone who could stop the calamity.

*Damn it.*

Jeok Cheongang clenched his teeth and forced himself forward with his last strength.

He knew.

It was already too late to stop this enormous explosion.

But he still had to move.

He belonged to neither the righteous path, the unorthodox factions, nor the Demonic Path—but this was the path he’d chosen.

If he didn’t at least try, he felt he’d never be able to look that reckless brat of a Disciple in the face again.

“Come on!”

Jeok Cheongang unleashed the azure dragon’s roar, shaking the air in every direction, and threw a punch with all his might at the calamity twenty *jang* away.

Then, in the next instant, he saw it clearly.

And heard it, too.

Shwoooooosh!

Just as the white light-flames of the Flame-Extinguishing Divine Fist shot out in an explosion, a dazzling streak of light shone across the dark sky ahead of it, cutting through space.

Those brilliant bolts plunged into the enormous, swelling sphere of flame.

Gooooooong.

In a world that seemed frozen, a distant flash of light and fire blended together, turning everyone’s vision white.

* * *

The sky and the earth split apart.

Instead of the world everyone knew, a new world made of light opened up.

At least in that moment, everyone on the battlefield—not just Jin Taekyung—must have felt that way.

*Could this be…?*

Fwoosh.

Before Jin Taekyung could fully recall the unbelievable sight he’d seen at the last moment, he felt his vision, which had been washed in blinding light, slowly return.

The blinding white flash that had obscured everyone’s vision faded. What filled the space it left behind was a tremendous roar that came belatedly, and flames surging up across the battlefield.

BANG! KWA-BOOOOM!

KOOOOROOM!

Would this be what it looked like if the sun in the sky rained down?

Hundreds of fireballs, great and small, fell over a radius of more than a hundred *jang*.

They crushed frail human flesh and bone, melted the ground, and evaporated snow mixed with blood.

Just as its name suggested, Hell Fire—like the flames of death.

But death did not treat everyone on the battlefield equally.

“Ah.”

The groan that suddenly slipped between someone’s lips didn’t belong to Jin Taekyung.

The Grand Mage silently gazed at the hellscape spread out below the hill.

More precisely, she was watching the Dark Heaven cultists collapse into charred lumps, unable even to scream.

*Why?*

She felt no sorrow at the sight of her allies meeting such a horrible death.

Only pure confusion.

Why had the fireball that should have exploded in the midst of the enemy’s forces broken into pieces and swept through her own allies instead?

Among the roughly thousands of casualties, why did the enemy number fewer than a hundred?

Her mind was filled with nothing but questions. The Grand Mage had watched only Jeok Cheongang at the last moment, but someone else, who’d taken everything in, already knew the answer.

“You’re damn late.”

“What?”

At the voice that suddenly rang out behind her, the Grand Mage turned without thinking—and saw Jin Taekyung smiling, weakly but unmistakably.

Over her shoulder, in his eyes fixed on some distant place, she caught the faint reflection of something golden.

“Damn old hag.”

“……!”

At that instant, the Grand Mage understood something and spun around in a hurry.

At the same time, she saw the answer to her question with her own eyes.

Shwoooosh!

The streak of light that had torn the fireball apart—the Force arrows.

“Bow Saint…!”
```
