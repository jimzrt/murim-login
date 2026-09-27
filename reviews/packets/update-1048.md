<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1048.txt",
      "sha256": "ce8929d6b2285d02155719b839254af3e70c8edc9ba6bee960461955e8734e17",
      "bytes": 13997
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "3d3bf977433e7ea50888276288d074503348a7a4522c74c3c4d345caee44ada1",
      "bytes": 1363
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "91edff1ea0e7f2d1bdf20f77998a86f250b89f1bc3f043cd106289bea1e118b4",
      "bytes": 240895
    },
    {
      "path": "characters/Blood-Sword Demon Lord.md",
      "sha256": "eee56bfdc962a7e28ad317567ac9ec8eb3d0ac6f6857f5d9d7dec91b160ab642",
      "bytes": 914
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "b29b8942ace372cb9f9b55f45862a5fa341721752a87994b6f08f7c0420ae19b",
      "bytes": 760
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "677d0c26cc1d9903ef9e1a6c5a6b4820726594dc763a7bfea8e214be09912070",
      "bytes": 1502
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "cb517104d392e902fc0a65366834f4e02a6c95969fdb9875425aa004783a67a3",
      "bytes": 1823
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "f6b3b09ac3983521d90cb7038af8a137ff6fc659a2430050c6841ee247a3c080",
      "bytes": 623
    },
    {
      "path": "characters/Sima Gong.md",
      "sha256": "770416e08ad074fe6a2f219de17469e4d78841eca6e9c13186601467cd2de383",
      "bytes": 800
    },
    {
      "path": "characters/So Gyo.md",
      "sha256": "5a6b9089903420f89c8fa26332a732ed084ced177d19fdf7f59e4089103d1062",
      "bytes": 767
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "81ee523228fb993aef67595779687d208f01c57a82b8976ea2248f2a9e916acd",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "83b9caf390abb6921a6ae6d2eea1b967287d0cf54b9b7ff267e98d2daef7e89b",
      "bytes": 281706
    }
  ],
  "estimated_tokens": 12344
}
-->

# Durable State Update — Chapter 1048

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
1 and safe_through 1048. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1048. Profile updates may replace only one
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
  "chapter": 1048,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1048,
    "continuity_sources": [1048],
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
    "The Blood-Sword Demon Lord’s forces have been checked by the Embroidered Uniform Guard and the surviving Coalition Army; the Bow Saint and Jeok Cheongang are now confronting him.",
    "The Grand Mage has not reappeared since the enormous fireball attack.",
    "Sima Gong broke his bargain with Dark Heaven, aided Jeok Cheongang, and is gravely wounded and missing an arm; his fate remains unresolved.",
    "Sima Gong hopes the Black Dragon Demon Gate will survive and grow stronger under his absent heir."
  ],
  "continuity_sources": [
    1046,
    1047
  ],
  "open_questions": [
    "What are the identity and purpose of the Lord of Heaven?",
    "Did Dark Heaven cause the Great Faction War?",
    "Who are the white-robed mages, and what is their purpose?",
    "How were the former Demonic Cult fiends made into Black Ghosts?",
    "Will Sima Gong survive, and what will become of the battle?"
  ],
  "safe_through": 1047,
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

| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 사마공    | **Sima Gong**      |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 궁성     | **Bow Saint**                 | —              |
| 무인     | **martial artist**                               | Default term                                          |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 노부      | **this old man / I**                                            |
| 혈검마군 | **Blood-Sword Demon Lord** | Antagonist commanding the army advancing on the Great Snow Mountain. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 소교 | **So Gyo** | The palace attendant leading the group assigned to serve Prince Shangshan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 시산혈해 | **sea of corpses and blood** | Description of the preceding months of bloodshed. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 장성 | **Great Wall** | Wall used in the discussion of the Outer Lands. |
| 흑야왕 | **Black Night King** | Epithet of Sima Gong, Sama Pyo's father and the Sect Leader who built the modern Black Dragon Demon Gate. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 검마 | **Sword Demon** | A Demonic Cult swordsman whose final technique is compared with One Annihilation. |
| 대설산 | **Great Snow Mountain** | Mountain where Baeksang's wartime account reaches its next episode. |
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
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 미미 | rescuer to companion snake | Mimi or Mimi-chan | informal, pleading | Taekyung calls to Mimi while asking the snake to carry him and the survivors. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 소교 | 진태경 | palace attendant addressing a martial artist and guest under escort | Young Master Jin | formal and respectful, but firm | Addresses him as 진 공자 while escorting him and warning him not to investigate. |
| 진태경 | 소교 | palace attendant and martial artist under imperial scrutiny | you | formal-polite, controlled and challenging | Taekyung addresses So Gyo as 당신 while questioning her presence and demanding an explanation. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
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
| 혈검마군 | 사마공 | former bargaining allies turned enemies | you; you traitor | blunt and hostile | Uses direct, contemptuous forms while accusing Sima Gong of betraying him. |
| 사마공 | 혈검마군 | former bargaining allies turned enemies | you; you Demonic Cult bastard | calm and contemptuous | Uses 당신 before ending with the insult 마교 잡놈아. |

## Listed compact profiles

### Blood-Sword Demon Lord.md

# Blood-Sword Demon Lord (혈검마군)

- **Safe through:** Chapter 1047
- **Aliases:** None
- **Role:** The Blood-Sword Demon Lord is a formidable martial master who commands the force advancing on the Great Snow Mountain and now serves the Lord of Heaven.
- **Personality:** Devoted to his master and proud of his abilities, he is deeply wounded by perceived distrust and resolves to prove his worth.
- **Voice:** Casually familiar and self-amused, addressing Jeok Cheongang respectfully as Senior while trading blunt insults; his easy laughter can turn to a low, cold intensity.
- **Relationships:** He serves the Lord of Heaven with deep devotion but believes his master does not fully trust him; he has been ordered not to kill Jin Taekyung, admires Jeok Cheongang, and once shared the Demonic Cult with the fiends who became Black Ghosts.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1047
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1047
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1046
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him and feels no fear when Taekyung is with him; Taekyung trusts Sama Pyo and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1046
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Sima Gong.md

# Sima Gong (사마공)

- **Safe through:** Chapter 1047
- **Aliases:** Black Night King
- **Role:** Sima Gong is the Sect Leader who built the Black Dragon Demon Gate into a major unorthodox power and the father of its Young Sect Leader, Sama Pyo.
- **Personality:** Sly and calculating yet capable of risking himself for a moment of conscience, he values his heir’s future and repaying a debt to Jeok Cheongang.
- **Voice:** Polished and persuasive, with smooth rhetorical turns and a composed, gently teasing manner.
- **Relationships:** Sama Pyo is his youngest son among seven older brothers and nine older sisters; he aided Jeok Cheongang despite their history, and hopes his heir will carry on the Black Dragon Demon Gate.

### So Gyo.md

# So Gyo (소교)

- **Safe through:** Chapter 935
- **Aliases:** None
- **Role:** So Gyo is the Bow Saint, a Supreme Peak master and palace attendant assigned to Prince Shangshan, whose two curved swords can join into their original bow form.
- **Personality:** Calm, calculating, and self-possessed; she conceals her strength and identity and can be openly taunting.
- **Voice:** Measured and composed, shifting from deferential formality to casual, pointed taunts and threats.
- **Relationships:** So Gyo recognizes Jin Taekyung as the chosen one spoken of by the Martial God; she says only she and the Emperor know a secret she withheld from Baek Yeon, while her true allegiance remains unknown.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1046
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃1048화



혈검마군은 흔들리는 시선으로 자신의 시야에 들어온 두 남녀를 바라보았다.

그것은 일세를 풍미한 대마두인 그조차도 몇 번 느껴 보지 못했던, 실로 기묘한 감각이었다.

먹구름으로 뒤덮인 하늘 아래, 수많은 적과 아군이 뒤얽히며 처절한 전투를 이어 가고 있음에도 오직 그 두 사람만이 시야를 가득 채운 듯했으니.

화왕(火王). 그리고 궁성(弓星)이라는 별호에 담긴 의미와 무게감은 그만큼 대단한 것이었다.

살아있는 두 전설이 한자리에 나타났다는 점에서 더더욱.

‘빈틈이…… 보이지 않는다.’

혈검마군은 자신도 모르게 숨을 삼켰다.

백 명도, 천 명도 아니다. 눈앞의 적은 고작 두 사람일 뿐이다.

한데 그것만으로도 일만이 넘는 대군에 의해 물샐틈없이 포위당한 듯한 기분이 들었다.

아니, 그 이상의 압박감이 있었다.

저벅.

순간, 세 개의 발자국 소리가 겹쳐진다.

좌우에서 천천히 걸음을 옮겨 거리를 좁히는 적천강과 궁성의 모습에, 본능적으로 뒷걸음질 친 혈검마군이 뒤늦게 자신의 행동을 인지하고 얼굴을 붉혔다.

밀렸다.

기세에서, 기백에서.

그리고 화왕 적천강은 그 사실을 조용히 눈감아 줄 정도로 점잖은 상대가 아니었다.

“왜, 조금 전까지는 모두 상대해 주겠다더니. 그새 마음이 바뀌기라도 한 것이냐?”

“……이 빌어먹을 노괴가.”

“오늘따라 제법 듣기 좋군. 어디 더 해 보거라.”

“뭐?”

“새파란 애새끼가 벌써 귓구멍이 막혔나. 더 지껄여 보라고 했느니라.”

적천강이 씩 웃으며 말을 이었다.

이미 겉보기에도 적잖은 부상을 입은 상태였으나, 그의 목소리와 낯빛에는 여전히 강렬한 열기가 서려 있었다.

“생각해 보니 지금껏 노부에게 그딴 식으로 말한 놈들은 전부 다 뒈졌거든. 하나도 빠짐없이.”

“……!”

혈검마군의 눈가가 파르르 떨렸다.

명백한 도발, 하지만 이와 같은 적천강의 언행이 단순한 허장성세 따위가 아니라는 것쯤은 그 역시 피부로 체감하고 있었다.

지금의 자신이 제아무리 본래의 한계를 훌쩍 뛰어넘었다 한들, 화왕과 궁성을 동시에 상대하며 우위를 점하는 모습은 쉽사리 상상할 수 없었으니까.

슈확!

그리고 바로 그 순간 공간을 가른 빛줄기는, 그것에 담긴 휘황함과는 달리 혈검마군의 마음속 불안감을 한층 더 짙게 덧칠하기에 충분했다.

드드득, 콰앙!

예고 없이 날아든 강기의 화살.

즉각적인 반응으로 그 무시무시한 빛줄기를 쳐낸 혈검마군이 충돌의 여파로 부르르 떨리는 검자루를 고쳐 잡았을 때, 먼지구름을 뚫고 나아가는 유려한 신형이 있었다.

스륵.

무게가 느껴지지 않을 정도의 가벼운 발걸음.

숨 쉴 틈 없이 천하의 절반을 가로지른 강행군을 증명하듯, 뿌연 먼지로 뒤덮인 옷자락이 흩날린다.

그러나 그 위로 드러난 여인의 얼굴은 잡티 하나 없이 투명했고, 먼지구름 너머의 적을 주시하는 눈동자는 시릴 만큼 빛났다.

‘전방으로부터 삼 장. 좌측으로 세 치.’

소교(小嬌), 아니 궁성이라는 별호를 가진 위대한 무인은 신형을 내뻗음과 동시에 자신의 애병을 쥐었다.

그와 동시에 섬광처럼 움직인 새하얀 손가락을 따라 맺히는 세 줄기의 강기.

파파팟!

먼지구름이 갈라진다. 벼락보다도 더한 위력이 실린 강기의 화살들이 모든 것을 가르며 나아간다.

그와 동시에, 육안으로 확인하기도 전에 그 너머에서 들끓는 힘의 파동을 느낀 혈검마군이 온 힘을 다해 검을 흩뿌렸다.

후우우웅!

태산조차 베어 버릴 듯한 횡격(橫擊).

검신을 휘감으며 거대하게 부풀어 오른 검붉은 강기가, 인간의 한계를 아득히 벗어난 속도와 힘으로 강기의 화살들을 휩쓸었다.

콰아아아앙!

사방의 공기가 터져 나갔다. 빛줄기를 단숨에 집어삼킨 강기가 그대로 전방을 향해 쏘아졌다.

구구구궁!

지축을 울리는 것으로도 모자라 말 그대로 초토화시킨 일격.

그러나 그 핏빛 섬광이 그린 파괴적인 궤적에, 혈검마군이 찾는 적들의 모습은 어디에도 보이지 않았다.

그저 보이지 않는 사각(斜角)에서 들이닥친, 서로 다른 두 줄기의 파공성만이 있을 뿐.

화륵, 스아악!

느려진 세상 속, 혈검마군은 눈을 부릅떴다.

하나는 더할 나위 없이 맹렬했고, 또 다른 하나는 소름이 끼칠 만큼 은밀했다.

파공성만 들어도 알 수 있을 정도로 상반된 기운이었으나, 혈검마군은 그것들의 공통점을 누구보다 잘 알고 있었다.

‘단 일격이라도 허용한다면, 그것으로 끝이다.’

이 광활한 천하를 통째로 들어 뒤집어도 지금의 공격을 받아낼 수 있는 무인이 몇이나 될까.

화왕과 궁성.

궁성과 화왕.

저들은 단지 낡고 케케묵은 과거가 아니었다.

과거에는 각자의 전설을 써 내려갔고, 현재까지도 그 전설을 이어 가고 있으며, 머나먼 후대에는 숱한 호사가(好事家)들이 그들의 행보를 노래하며 칭송할 것이다.

그렇게 전설은, 거인은 영원히 기억된다.

그리고 어쩌면, 오늘 이 자리에서 그 전설의 한 구절이 새롭게 쓰일지도 몰랐다.

두 명의 위대한 무인이, 혈검마군이라 불리던 흉적을 피와 눈으로 뒤덮인 대설산의 광야에서 쓰러트렸노라고.

하지만…….

‘그런 일은 결코 벌어지지 않을 것이다.’

혈검마군은 이를 악물었다. 서서히 되돌아오는 시간의 흐름 속에서, 자신이 지닌 모든 힘과 감각을 극한으로 끌어올리며 신형을 비틀었다.

아마도, 그의 일생을 통틀어 두 번 다시 재현해 낼 수 없으리라 생각될 정도의 기민한 움직임으로.

서걱!

불현듯 일어난 뜨거운 통증이 혈검마군의 팔과 목줄기를 따라 일었다.

궁성.

활의 형태를 하고 있던 애병을 분리, 두 자루의 곡도(曲刀)로 해체한 그녀는 어느새 혈검마군을 스쳐 지나간 후였다.

은밀하게, 그러나 벼락처럼 휘두른 두 줄기의 섬광으로 혈검마군의 목덜미 일부와 왼팔의 어깻죽지를 뜯어내며.

그러나 단숨에 목숨을 취하고도 남았어야 할 그 공격의 성과는 미미했고, 혈검마군은 그로 인한 통증이 온전히 뇌리로 전해지기도 전에 측면에서 들이닥치는 끔찍한 열기를 느꼈다.

화륵, 퍼어엉!

‘흡……!’

거의 동시였다.

적천강이 내지른 멸염신권(滅炎神拳)이 혈검마군의 옆구리를 맹렬하게 스쳐 지나간 것도.

그 찰나의 스침만으로도 한 움큼이나 되는 살이 녹아 버린 것도.

그리고 이 참을 수 없는 격통에, 혈검마군이 자신도 모르게 헛숨을 삼키며 신형을 멈춘 것도.

하지만 단지 그뿐이었다.

지금 이 순간, 혈검마군은 자신이 살아남았다는 사실에 마음속 깊이 환호하고 있었다.

비록 궁성에 의해 한쪽 팔을 잃고, 적천강의 일권에 실린 열기가 옆구리의 일부를 녹이는 것으로도 모자라 내장까지 미쳤음에도 불구하고.

‘충분하다.’

믿는 구석이 있는 혈검마군에게 있어, 이 정도의 부상은 감내할 만한 부분이었다.

화왕과 궁성의 합공에도 쓰러지지 않았다는 사실이, 이미 절호의 기회를 놓친 그들과 달리 아직 한 수가 남아 있다는 사실이 무엇보다 중요했다.

‘죽인다. 반드시!’

회심의 일격은 늘 빈틈을 만드는 법.

혈검마군은 엄습해 오는 격통을 억누르며, 크게 뜨인 눈으로 자신을 바라보고 있는 적천강을 향해 검을 내리그었다.

아니, 정확히는 내리그으려 했다.

어쩌면 조금 전의 혈검마군만큼, 혹은 그 이상이라 할 수 있는 필사적인 의지를 품은 누군가가 움직이기 전까지는.

푹!

불현듯, 혈검마군은 생각지도 못한 불같은 통증을 느끼며 신형을 비틀거렸다.

그리고 불신이 담긴 눈동자로 자신의 발목을 깊게 관통한 거무스름한 도신(刀身)을, 그것을 쥔 흑야왕 사마공의 얼굴을 멍하니 바라보았다.

“이런 개…….”

가까스로 신음을 끄집어낸 그 순간.

“말했지. 전부 뒈졌다고.”

퍼엉! 콰드드득!

적천강의 서늘한 음성과 함께, 혈검마군의 시야가 뒤집혔다.

어두운 하늘, 피와 눈으로 뒤덮인 땅. 그 안에서 죽고 죽이는 전투를 이어 가는 수많은 이들.

그 모든 것이 온통 새하얗게, 붉게 물들었다.

화염신장(火焰神掌).

서늘했던 음성과는 달리 살을 녹이고 뼈를 부수며 몸속 깊숙이까지 파고든 그 끔찍한 열기 앞에서, 무시무시한 고통에 속박당한 혈검마군이 할 수 있는 것은 아무것도 없었다.

다만, 그 자신조차도 예상치 못했던 뜻밖의 행운이 있었을 뿐.

쾅! 콰앙! 콰드드득!

거대한 힘을 감당하지 못한 채 포탄처럼 쏘아지던 몸뚱어리가 한참을 구르고 부딪혀 가며 마침내 어딘가에 처박힌 그때.

“이런.”

내장 조각이 뒤섞인 핏물을 토해 내던 혈검마군의 귓가로, 누군가의 음성이 아스라이 울려 퍼졌다.

“크게 당하셨군요, 마군(魔君).”

환청인가?

힘없이 눈을 깜빡이며 생각하던 혈검마군은 이내 깨달았다.

자신의 몸뚱어리가 처박힌 이곳이 경사진 언덕이며, 조금 전의 목소리가 퍽 생생하면서도 낯익다는 것을.

“크, 크하하하!”

혈검마군은 자신도 모르게 광소를 터트렸다.

목구멍에서는 피가래가 들끓고, 몸을 들썩이며 웃을 때마다 부러진 사지에서 엄청난 충격과 통증이 전해졌지만 조금도 개의치 않았다.

그는 미친 듯이 소리 내어 웃었다.

마치 세상에서 가장 즐거운 사람처럼, 죽음의 끝자락에서 가까스로 구원받은 사람처럼.

그렇게 환희에 몸을 떨며, 눈앞의 구원자를 향해 피에 젖은 손을 내밀었다.

아니, 상관으로서 명령했다.

“나를 치유해라. 지금 당장.”

그리고 그런 혈검마군의 모습을 물끄러미 응시하던 구원자, 대술사(大術士)가 천천히 입술을 떼려던 그 순간.

슈확!

불현듯 울려 퍼진 한 줄기의 파공성과 함께, 혈검마군의 눈동자가 부릅떠졌다.

그는 보았다.

대술사의 어깨너머, 어느샌가 쓰러져 있던 신형을 일으켜 세운 채 타오르는 듯한 눈빛으로 창날을 내리긋는 한 청년을.

실낱같은 공력도, 평소와 같은 힘과 속도도 깃들어 있지 않은.

그저 자신에게 남은 모든 마지막 기력을 쥐어 짜내어, 혼신의 일격을 펼치는 진태경의 모습을.

‘이런 미친……!’

혈검마군이 소리 없는 비명을 내지른 그때.

카앙!

대술사를 둘러싼 무형(無形)의 방어막이, 은백색의 창날을 튕겨 냈다.

마치 창날에 실려 있던 필사적인 염원을 비웃기라도 하듯, 놀라울 정도로 손쉽게.

그리고.

그것이 전부였다.

툭.

모든 힘을 잃은 주인의 손아귀에서 굴러떨어진 창대.

찰나의 경악으로 부릅떠져 있던 혈검마군의 눈동자에는, 지금 이 순간 서서히 기울어지는 누군가의 신형이 비치고 있었다.

털썩.

끝끝내 허물어지는 몸뚱어리.

형편없는 몰골로 쓰러진 채 힘없이 이쪽을 노려보는 진태경의 모습에, 혈검마군은 자신도 모르게 헛숨을 삼켰다.

‘끈질긴 놈 같으니.’

이미 저 정도의 한계에 다다라 있었음에도 기회를 엿보다니.

감탄이, 아니 소름이 돋을 정도로 무시무시한 집념이 아닐 수 없었다.

그러나…….

‘그 발악도, 이제는 끝이다.’

혈검마군은 피에 젖은 이빨을 드러내며 웃었다.

본래의 그였다면. 아니, 최소한 피륙으로 이루어진 인간이라면 이미 몇 번이나 죽어도 이상하지 않을 정도의 부상.

하지만 극도로 강화된 신체는 촌각에 불과한 짧은 시간을 허락해 주었고, 그것이 모든 이들의 운명을 뒤바꿀 터였다.

지금 이 순간에도 온 힘을 다해 이곳으로 들이닥치는 화왕과 궁성도.

시산혈해 속에서 날붙이를 휘두르는 수만 명의 적과 아군도.

그리고, 그 무엇보다 중요한 혈검마군 자신의 생사(生死)도.

“이제…… 이 지긋지긋한 전투를 끝낼 때가 되었다.”

눈에 띄게 가빠진 숨결로 한마디를 내뱉은 혈검마군을 향해, 대술사가 담담한 얼굴로 고개를 끄덕였다.

“물론입니다.”

그 순간.

화악.

대술사의 손끝에서 환한 빛이 번졌다.

정오의 햇볕처럼 따스하고, 깊은 산 속의 연못보다 맑은 치유의 빛이.

‘아.’

자신도 모르게 감긴 두 눈.

혈검마군은 잠시 그 빛줄기가 주는 평온함에 몸을 맡겼다.

그리고 찰나인 듯 영원 같은 그 순간이 흐르고 마침내 눈을 떴을 때.

그는 믿을 수 없다는 눈빛으로 바라보았다.

“이게…… 무슨?”

조금도 치유되지 못한, 처참하기 그지없는 자신의 몸뚱어리를.

더불어 조금씩 사그라지고 있는 광휘에 휩싸인 채, 조금 전과는 달리 안정된 숨결을 내뱉고 있는 한 사람을.

아니.

진태경을.
```

## Final English reading copy

```markdown
# Chapter 1048

The Blood-Sword Demon Lord stared, his gaze wavering, at the two figures before him.

It was a strange sensation—one even he, a fiend who had made his mark on an entire age, had experienced only a handful of times.

Beneath a sky buried in storm clouds, countless enemies and allies were locked in a desperate battle. And yet it seemed as though those two alone filled his field of vision.

That was how much weight and meaning their titles carried: Fire King and Bow Saint.

All the more so when two living legends appeared in one place.

*I can’t see an opening…*

The Blood-Sword Demon Lord swallowed without realizing it.

Not a hundred enemies. Not a thousand. There were only two people before him.

And yet those two made him feel as if he were surrounded on all sides by an army of more than ten thousand.

No—that wasn’t all. There was even greater pressure than that.

Step.

For an instant, three footsteps overlapped.

Jeok Cheongang and the Bow Saint slowly closed in from either side. The Blood-Sword Demon Lord instinctively stepped back, then belatedly realized what he’d done and flushed.

He’d been pushed back.

By their aura. By their fighting spirit.

And Fire King Jeok Cheongang was not the sort of man to politely overlook it.

“What happened? A moment ago, you said you’d take us all on. Changed your mind already?”

“…You damn old bastard.”

“Sounds pretty good today. Go on, say some more.”

“What?”

“Has that young brat’s hearing gone bad already? I said keep running your mouth.”

Jeok Cheongang grinned and continued.

He was visibly wounded, but a fierce heat still burned in his voice and across his face.

“Come to think of it, every bastard who’s talked to this old man like that has ended up dead. Every last one.”

“……!”

The Blood-Sword Demon Lord’s eyelids quivered.

It was an obvious taunt, but he knew from experience that Jeok Cheongang wasn’t just putting on a show.

No matter how far he’d surpassed his former limits, it was hard to imagine him gaining the upper hand against both the Fire King and the Bow Saint at once.

Shwaak!

And then, at that very moment, a streak of light cut through the air. For all its dazzling brilliance, it was more than enough to deepen the Blood-Sword Demon Lord’s unease.

Rrrr, KWA-BOOM!

A Force arrow came flying without warning.

The Blood-Sword Demon Lord reacted at once, batting away the terrifying streak of light. As he tightened his grip on the sword hilt trembling from the impact, a graceful figure emerged through the cloud of dust.

Swish.

Her steps were so light they seemed weightless.

Her dust-covered clothes fluttered, proof of the punishing journey she’d made across half the land without a moment to catch her breath.

But the woman’s face, visible above them, was flawless, and her gaze fixed on the enemy beyond the dust cloud shone cold and bright.

*Three jang straight ahead. Three chi to the left.*

So Gyo—no, the great martial artist known by the title Bow Saint—thrust herself forward and gripped her beloved weapon.

At the same time, three streaks of Force gathered along her white fingers as they flashed into motion.

Pa-pa-pat!

The dust cloud split apart. Force arrows, carrying power greater than lightning, cut through everything in their path.

The Blood-Sword Demon Lord felt the surging power beyond them before he could even see it. He whipped his sword through the air with all his strength.

Whoooom!

A horizontal slash that seemed capable of cutting through even Mount Tai.

Dark-red Force swelled around the blade, then swept aside the Force arrows with speed and strength far beyond human limits.

KWA-BOOOOM!

The air burst in every direction. The Force that had swallowed the streaks of light shot straight ahead.

Rrrrmmble!

It didn’t merely shake the earth. The strike laid waste to everything in its path.

But the destructive trail of that bloody flash held no sign of the enemies the Blood-Sword Demon Lord was looking for.

Only two different whistles tore in from the blind spot he couldn’t see.

Fwoosh! Shing!

In a world that seemed to slow, the Blood-Sword Demon Lord’s eyes flew wide.

One attack was as fierce as could be. The other was so stealthy it raised goose bumps.

Their energies were opposites—he could tell that from the sound alone. But the Blood-Sword Demon Lord knew better than anyone what they had in common.

*If I let even one strike through, it’s over.*

How many martial artists in this vast land could withstand the attacks coming at him now, even if the whole world were turned upside down?

The Fire King and the Bow Saint.

The Bow Saint and the Fire King.

They weren’t merely relics of a distant past.

They had written their own legends then, and carried those legends into the present. In the distant future, countless people who loved to tell a story would sing of their deeds and praise them.

That was how legends lasted. How giants were remembered forever.

And perhaps, here today, a new verse would be written in that legend.

Two great martial artists had felled the fiend known as the Blood-Sword Demon Lord on the open plain of the Great Snow Mountain, amid blood and snow.

But…

*That will never happen.*

The Blood-Sword Demon Lord clenched his teeth. As the flow of time slowly returned, he pushed every ounce of strength and every sense he possessed to its limit and twisted his body.

It was a nimble movement he believed he would never be able to repeat in his life.

Slice!

A sudden, burning pain ran along his arm and the side of his neck.

The Bow Saint.

She had separated her beloved weapon, which had been shaped like a bow, into two curved swords. She had already passed him by.

The two flashes she’d swung, secretive yet swift as lightning, had torn away part of his nape and the shoulder of his left arm.

But the attack, which should have been enough to take his life outright, had done surprisingly little. Before the pain could fully register in his mind, the Blood-Sword Demon Lord felt an appalling heat rush at him from the side.

Fwoosh! Poom!

*Hng…!*

It all happened almost at once.

Jeok Cheongang’s Flame-Extinguishing Divine Fist had swept fiercely past his flank.

The heat from that glancing blow had melted away a fistful of flesh.

And the unbearable pain had made the Blood-Sword Demon Lord suck in a breath and stop moving without realizing it.

But that was all.

At that moment, the Blood-Sword Demon Lord was cheering deep down at the fact that he’d survived.

Even though the Bow Saint had taken one of his arms, and the heat from Jeok Cheongang’s fist had melted part of his flank and reached his innards as well.

*That’s enough.*

The Blood-Sword Demon Lord had something to fall back on. An injury like this was something he could endure.

What mattered more than anything was that he hadn’t fallen to the combined attack of the Fire King and the Bow Saint—and that, unlike them, who had already missed their perfect chance, he still had one move left.

*I’ll kill them. I swear it!*

A decisive strike always left an opening.

The Blood-Sword Demon Lord suppressed the pain surging through him and slashed his sword down at Jeok Cheongang, who watched him with eyes wide open.

No—more precisely, he tried to slash down.

But before he could, someone moved with a desperate resolve equal to—or perhaps greater than—his own moments earlier.

Thuk!

A fierce, unexpected pain shot through him. The Blood-Sword Demon Lord staggered, then stared in disbelief at the dark blade that had pierced his ankle—and at the face of the man holding it.

Black Night King Sima Gong.

“You son of a—”

The moment he managed to force out a groan—

“I told you. Every last one of them died.”

Poom! Krrrcrack!

At Jeok Cheongang’s cold voice, the Blood-Sword Demon Lord’s vision flipped over.

The dark sky. The ground covered in blood and snow. The countless people fighting and killing one another across it.

Everything turned blindingly white, then red.

Flame Divine Palm.

The dreadful heat, unlike Jeok Cheongang’s cold voice, melted flesh and broke bones as it sank deep into his body. Paralyzed by the excruciating pain, the Blood-Sword Demon Lord could do nothing.

Except that an unexpected stroke of luck awaited him—something even he hadn’t foreseen.

KWA-BOOM! KWA-BOOM! Krrrcrack!

His body shot away like a cannonball, unable to withstand the tremendous force. It rolled and crashed along the ground before finally slamming into something.

“Well.”

The Blood-Sword Demon Lord spat blood mixed with bits of his innards. A voice drifted faintly into his ear.

“You’ve been badly hurt, Demon Lord.”

Was it an illusion?

The Blood-Sword Demon Lord blinked weakly as he wondered. Then he realized the slope beneath his battered body was a hillside, and that the voice he’d just heard sounded uncannily familiar.

“Guh, hahahaha!”

The Blood-Sword Demon Lord burst out laughing without meaning to.

Blood bubbled in his throat, and every time his body shook with laughter, tremendous jolts of pain shot through his broken limbs. He didn’t care in the least.

He laughed like a madman.

Like the happiest person in the world. Like someone who had been rescued at the very edge of death.

Trembling with joy, he stretched a bloodied hand toward his savior.

No—he gave his subordinate an order.

“Heal me. Right now.”

The savior, the Grand Mage, gazed silently at the Blood-Sword Demon Lord. She slowly parted her lips to speak—

Shwaak!

A streak of light whistled through the air. The Blood-Sword Demon Lord’s eyes flew wide.

He saw a young man beyond the Grand Mage’s shoulder, hauling himself up from where he had fallen. With a fiery gaze, the young man brought his spearhead down.

There was not even a thread of internal energy in it. No trace of his usual strength or speed.

It was Jin Taekyung, squeezing out every last bit of strength he had left to unleash a strike with all his might.

*You’ve got to be fucking kidding me…!*

The Blood-Sword Demon Lord screamed soundlessly.

Clang!

An invisible barrier around the Grand Mage knocked away the silver-white spearhead.

It did so with astonishing ease, as if mocking the desperate hope behind the blow.

And then—

That was all.

Thud.

The spear shaft rolled from its owner’s powerless hand.

In the Blood-Sword Demon Lord’s eyes, still wide with a moment’s shock, someone’s figure was slowly tipping over.

Thump.

The body finally crumpled.

Jin Taekyung lay in a wretched heap, glaring weakly at him. The Blood-Sword Demon Lord sucked in a breath without realizing it.

*You stubborn bastard.*

He’d already reached his limit, and still he’d waited for a chance to strike.

His persistence was so terrifying it inspired awe—or rather, sent a chill down the Blood-Sword Demon Lord’s spine.

But…

*That desperate struggle ends here.*

The Blood-Sword Demon Lord bared his bloodied teeth in a grin.

If he were his former self—or even just an ordinary flesh-and-blood human—those injuries would have killed him several times over.

But his body, strengthened to an extreme degree, had granted him a brief handful of moments. Those moments would change everyone’s fate.

The Fire King and the Bow Saint, both rushing here with all their strength even now.

The tens of thousands of enemies and allies swinging their weapons amid the sea of corpses and blood.

And, most important of all, the Blood-Sword Demon Lord’s own life and death.

“It’s time… to put an end to this damned battle.”

The Blood-Sword Demon Lord spoke, his breathing visibly growing more labored. The Grand Mage nodded calmly.

“Of course.”

At that moment—

Fwoosh.

A brilliant light spread from the Grand Mage’s fingertips.

A healing light, warm as the midday sun and clear as a pond deep in the mountains.

*Ah.*

The Blood-Sword Demon Lord’s eyes closed without his meaning to.

For a moment, he let himself sink into the peace the light brought.

Then, after a moment that felt both brief and eternal, he opened his eyes.

He stared, unable to believe what he saw.

“What… is this?”

His body was still horribly mangled, not healed in the slightest.

And someone else, wrapped in the fading glow, was breathing more steadily than before.

No.

Jin Taekyung.
```
