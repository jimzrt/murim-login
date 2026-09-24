<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0979.txt",
      "sha256": "d586d28a78b863cbc2c16d606b7436b418ec275c0df2b938ff35c9eba0daa090",
      "bytes": 18348
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "90f0c5868cfc8f4e0c9dc294f87c03d6e88fa0b4534a684824262b5432993be6",
      "bytes": 1402
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "1ac22018e1d12d24593cd2030688d6383be2dc9a18973e1f53f623612d44e3bf",
      "bytes": 235849
    },
    {
      "path": "characters/Cheolyeong.md",
      "sha256": "40f44053a36ed14290ab08feb2b2c30271d34ab31fd3a1b9c6692988622034b5",
      "bytes": 342
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "23d6e912ac6673a10b24503f02f0ec8da917b8cf6307b8c8ea712d3cfcefe385",
      "bytes": 759
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "692f84d811d77ba58cb92ada119eb8c6f84e532e27c1a52cf75e5f142681ec4e",
      "bytes": 667
    },
    {
      "path": "characters/Jamukha.md",
      "sha256": "521bd38b0005b9c1de53883bc37791db150f009f7efbf0cc53bf6f4b4dbde351",
      "bytes": 611
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "2823cc50166ff00fb53d55ef97a4d5ddba7c79b1a43e8ca50a2949a4fa1c269c",
      "bytes": 1291
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "85c5142a391a70bc4bc33d818aceb578f6d123958bd119af0d55554e97517ac3",
      "bytes": 1405
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "926535cbd0f2bcda0e3e5524d9d741c014938c9497c7addfe49eeb9589970356",
      "bytes": 1479
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "8721ffd72f67b7e86e51051c6076e3498a98248d56f0b0656e93e7577762f249",
      "bytes": 1116
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "549fd7d4d5a1c79b4108d0db941f3ca659b0b12712bd2b1cf919210b42c5f73f",
      "bytes": 622
    },
    {
      "path": "characters/Murong Baek.md",
      "sha256": "e3807ebc72a171cc5dfe757c4fd52a042cb4e0792f2fd55cd58eead005557dab",
      "bytes": 660
    },
    {
      "path": "characters/Peng Cheolyeong.md",
      "sha256": "1ce66a104891cee912fb59e7ec97cf98d4b5cd0a03063f34eaf6f800fe813e52",
      "bytes": 679
    },
    {
      "path": "characters/Temur.md",
      "sha256": "1b3b31a74706f2b4bfeac4d59c1f83e6fad8ef38d802e4b01711ec8e8e93d1b6",
      "bytes": 676
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "aa4536cd403821fde2ec75674b715a1a6523f4329914df0af716afe436144dab",
      "bytes": 271557
    }
  ],
  "estimated_tokens": 15360
}
-->

# Durable State Update — Chapter 979

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
1 and safe_through 979. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 979. Profile updates may replace only one
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
  "chapter": 979,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 979,
    "continuity_sources": [979],
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
    "Jin Taekyung killed Murong Baek, the North Heaven Demon Lord, with help from Jeok Cheongang and the Bow Saint.",
    "An unnamed being in the darkness awakened after sensing the fourth heaven had fallen and another faithful servant had disappeared; it believes its long-awaited day is near.",
    "Murong Baek said the Lord of Heaven had awakened, the war had begun, and at most half a year remained.",
    "The conditions of Jin Mukyung, Cheol Mubaek, Wipeng, and Peng Cheolhu remain unknown.",
    "The Hebei Peng Family’s fate against the pill-enhanced Keshiks remains unknown.",
    "The Emperor remains gravely ill with Blood Soul Gu; the treatment said to require him to die once remains unresolved."
  ],
  "continuity_sources": [
    978
  ],
  "open_questions": [
    "What does the Lord of Heaven intend, and how will the war unfold?",
    "Who is the being in the darkness, and what is the day it has awaited?",
    "What are the conditions of Jin Mukyung, Cheol Mubaek, Wipeng, and Peng Cheolhu?",
    "Can the Hebei Peng Family withstand the pill-enhanced Keshiks?",
    "Can the Emperor be treated for Blood Soul Gu, and what does the treatment requiring him to die once entail?"
  ],
  "safe_through": 978,
  "temporary_decisions": [
    "Render Taekyung’s mocking nickname 뽀삐 as “Poppy”; it is not an established name."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 궁성     | **Bow Saint**                 | —              |
| 태원진가   | **Jin Family of Taiyuan**        |
| 하북팽가   | **Hebei Peng Family**            |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 중원     | **Central Plains**                               |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 제자     | **Disciple**                                 |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 팔천협    | **Eight Spring Gorge** |
| 정마대전   | **Great Faction War**         |
| 본가      | **our family / this family**                                    |
| 공자      | **Young Master**                                                |
| 철영 | **Cheolyeong** | Peng Cheolhu’s eldest son and the current Family Head of the Peng Family. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 자무카 | **Jamukha** | Khan of the western grasslands and the steppe army’s practical leader. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 모용백 | **Murong Baek** | Former northern rival and later comrade of Peng Cheolhu. |
| 팽철영 | **Peng Cheolyeong** | Family Head of the Hebei Peng Family and successor to the Thunderbolt Saber King. |
| 테무르 | **Temur** | Northern Gaoyuan chieftain commanding one hundred tribespeople; claims descent from the khans. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 철혈도 | **Iron Blood Saber** | Epithet of Peng Cheolyeong. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 장성 | **Great Wall** | Wall used in the discussion of the Outer Lands. |
| 모용세가 | **Murong Family** | One of the Five Great Families, based in Liaoning. |
| 위압 | **Intimidation** | System attribute strengthened by the achievement reward. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 대족장 | **Great Chieftain** | Title used for the senior Nanman leader who supposedly ordered the inspection. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |
| 초일류 | **Supreme First Rate** | Realm attained by each Baekcheon Unit member. |
| 진중 | **Jinzhong** | County included in Taekyung’s fief. |
| 중양절 | **Double Ninth Festival** | Festival used as the expected date for the invasion of the Central Plains. |

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
| 테무르 | 인도 | hostile_strangers | you Han Chinese bastard | hostile and contemptuous | Temur insults the seated Han Chinese man before attempting to draw his curved saber. |
| 인도 | 테무르 | intimidating_rival_to_chieftain | friend | cold and taunting | The Human Butcher calls Temur a slow friend after forcing him to sit. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |
| 진위경 | 적천강 | host_to_legendary_guest | Great Hero Jeok | formal-deferential | Introduces himself and pays respects to Jeok Cheongang as the Fire King. |
| 적천강 | 진위경 | elder_to_younger_family_head | you | gruff and teasing | Uses 자네 while mistaking Wikyung for Taekyung’s father and questioning his age. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 가솔 | 진태경 | Zhuge Clan retainer to Great Hero | Great Hero Jin | polite and pleading | Uses 진 대협 while urging Taekyung to stop provoking Ju Wongong. |
| 진태경 | 부족장 | captor to captured tribal chieftain | tribal chieftain | casual, coercive, and mocking | Jin promises to spare the captured chieftain if he answers questions properly. |
| 부족장 | 진태경 | captured tribal chieftain to overpowering enemy | Jin Taekyung | alarmed and desperate | The chieftain recognizes Jin by name while fleeing and then begs for his life. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 테무르 | 자무카 | fellow_khan_to_elder_khan | Khan Jamukha | formal-respectful | Temur affirms Chinggen’s public praise of Jamukha. |
| 자무카 | 진무경 | hostile opponents | you | familiar, blunt, and patronizing | Jamukha uses 자네 while urging Mukyung to submit and become his hunting dog. |
| 모용백 | 자무카 | commander_to_subordinate | you | plain and authoritative | Murong Baek gives Jamukha direct orders and rebukes him without honorific speech. |
| 자무카 | 모용백 | subordinate_to_commander_and_savior | you | deferential and honorific | Jamukha thanks Murong and addresses him with honorific speech. |
| 진태경 | 모용백 | adversaries | you | informal and confrontational | Directly asks whether Murong Baek beat up his older brother. |
| 모용백 | 진태경 | adversaries | you | informal | Addresses Taekyung directly during their confrontation. |
| 궁성 | 모용백 | opponents | Murong Baek; North Heaven Demon Lord | calm, formal, and admonitory | The Bow Saint directly addresses Murong while telling him to accept the consequences of his choices. |

## Listed compact profiles

### Cheolyeong.md

# Cheolyeong (철영)

- **Safe through:** Chapter 971
- **Aliases:** None
- **Role:** Cheolyeong is the current Family Head of the Peng Family in Hebei.
- **Personality:** Not established.
- **Voice:** Not established
- **Relationships:** He is Peng Cheolhu’s eldest son.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 978
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 970
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jamukha.md

# Jamukha (자무카)

- **Safe through:** Chapter 978
- **Aliases:** None
- **Role:** Jamukha was the ruler of the western steppe and a former eastern-steppe chieftain recruited into Dark Heaven by Murong Baek; Jin Taekyung killed him.
- **Personality:** Patient and ambitious, he was willing to feign loyalty to gain the power to rule the steppe and north.
- **Voice:** Not established
- **Relationships:** Peng Cheolhu defeated him more than fifty years ago; Murong Baek spared and recruited him, but Jamukha’s loyalty to him was feigned.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 978
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, remains Peng Cheolhu's rival, and once fought alongside Murong Baek, now his enemy.

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 973
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Jin Mukyung is the second son of the Jin Family of Taiyuan, a Supreme Peak swordsman known as the Heaven Shaking Sword, and Commander of the Heaven Shaking Squad.
- **Personality:** Reserved and disciplined, Jin Mukyung is devoted to swordsmanship and guided by a strong sense of chivalry, refusing to abandon what he believes is right.
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Jin Wikyung is his older brother and the Lesser Family Head who formed the Heaven Shaking Squad in his honor; Jin Taekyung is his younger brother, whom Mukyung loves and wanted to become a brother worthy of his pride.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 978
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor has appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 976
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm and politically capable, Jin Wikyung takes responsibility for his people and prioritizes their lives; he commits firmly to his principles, even when doing so means remaining in a losing battle.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Jin Wikyung is Taekyung’s eldest brother and future Family Head, protects and mentors him, and commands the Jin Family’s forces; Jin Mukyung is his younger brother, and he considers the Jin Family indebted to the Dongting Fisherman and the other fallen defenders of Shanxi.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 978
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Murong Baek.md

# Murong Baek (모용백)

- **Safe through:** Chapter 978
- **Aliases:** North Heaven Demon Lord, Divine Spear of the Imugi
- **Role:** Murong Baek was the North Heaven Demon Lord, known as the Divine Spear of the Imugi; Jin Taekyung killed him after he burned his life to gain power.
- **Personality:** He coveted the dragon pearl and the chance to become a dragon, rationalizing his pursuit while choosing to seize what belonged to others.
- **Voice:** Not established
- **Relationships:** Jeok Cheongang and the Bow Saint fought him alongside Jin Taekyung, who delivered the killing blow.

### Peng Cheolyeong.md

# Peng Cheolyeong (팽철영)

- **Safe through:** Chapter 971
- **Aliases:** Iron Blood Saber
- **Role:** Family Head of the Hebei Peng Family; son and successor of the Thunderbolt Saber King.
- **Personality:** Calm and prudent under pressure, prioritizing consultation over risking his family’s lives on a hasty decision.
- **Voice:** He speaks calmly and deliberately, even when explaining grave decisions.
- **Relationships:** Son of the Thunderbolt Saber King; Jeok Cheongang says his past fight was followed by no further contact and that the Peng Family fabricated a later story about their encounter.

### Temur.md

# Temur (테무르)

- **Safe through:** Chapter 968
- **Aliases:** None
- **Role:** Temur is a Khan of the northern grasslands, ruling alongside Chinggen over tens of thousands of horses and warriors.
- **Personality:** Hot-tempered and proud of his khan lineage, Temur chose survival over loyalty and now recognizes with guilt that his actions have led his followers to slaughter.
- **Voice:** Blunt, heated, and confrontational
- **Relationships:** The real Chinggen was Temur’s cousin and sworn brother through the anda oath, but he was killed; an impostor wearing Chinggen’s face now deceives Temur.

## Korean source

```text
＃979화



어느 순간, 모두는 깨달았다.

- 와아아아아!

팔천협(八天峽)이라 이름 붙은 비좁은 협곡을 넘어, 천지를 떨어 울리는 거대한 함성.

광활한 분지에서 치열한 전투를 이어 가고 있던 그들은 동시에 고개를 돌렸다.

가뭄이 든 논밭처럼 쩍쩍 갈라진 입술. 극심한 피로와 죽음에 대한 공포로 파르르 떨리는 손발.

몇 시진 동안이나 계속된 전투로 혈인(血人)이나 다름없어진 그들은 간절한 눈빛으로 협곡의 입구를 바라보았다.

빠르게 가까워지는 저 거대한 함성이, 지면을 두드리는 무수한 발걸음이 부디 아군의 것이기를 바라며.

그리고 서서히 흩어지는 어둠 너머로, 불현듯 한 줄기의 빛이 번뜩였다.

쐐애애액, 콰앙!

찰나의 순간, 굉음과 비명이 뒤섞인다.

하지만 빛줄기의 정체를 알아본 하북팽가의 가주, 철혈도(鐵血刀) 팽철영은 마음껏 소리 내어 웃을 수 있었다.

“으하, 으하하하!”

퍼걱!

쩌렁쩌렁한 웃음소리와 함께 휘둘려진 그의 대도(大刀)가 단숨에 십여 명의 유목민들을 휩쓸었다.

허공으로 솟구치는 피 분수 아래, 고작 일천도 남지 않은 하북의 투사들이 자신들의 가주를 따라 전진했다.

촌각 전까지만 하더라도 물먹은 솜처럼 무겁던 육신도, 병장기도 지금은 가볍기 그지없다.

미친 듯이 웃으며 나아가는 발걸음을 따라, 짙은 피 안개가 몽글몽글 피어올랐다.

서걱! 푸푸푹!

“크아아악!”

“커헉!”

곳곳에서 비명이 솟구쳤다. 가문의 절학을 익힌 모용세가의 무인도, 한때 한 자루의 돌격창과 활로 천하를 질타했던 유목민들도 하북팽가를 막을 수는 없었다.

아니, 정확히는 눈 앞에 펼쳐진 믿기 힘든 현실에 얼어붙었다고 해야 옳았다.

드드득!

지면이 몸을 떨었다.

성큼 다가온 새벽과 함께 흐릿해진 어둠 너머, 비좁은 협곡의 입구로 쏟아져 나온 수천의 그림자들 위로 피에 젖은 깃발이 우뚝 솟아 있었다.

대(大) 태원진가(太原進家).

“……!”

“……!”

이것이 의미하는 바는 단 하나뿐.

깃발에 수 놓인 글자를 바라보는 시선들이 파르르 떨렸다.

누군가는 충격과 절망으로, 또 다른 누군가는 희망과 환희로.

그러나 양쪽 어디에도 속하지 않는 이들 역시 있었다.

“갈(喝)! 지금 무슨 생각들을 하는 것이냐!”

모용백을 대신해서 전장을 통제하고 있던 모용세가의 대장로, 모용위진이 공력을 실어 외쳤다.

독기로 물든 그의 눈동자를 마주한 휘하의 가솔들은 몸을 움찔 떨었다.

“놈들의 얕은 수작에 넘어가지 마라! 이건, 이건 그저……!”

모용위진은 차마 말을 잇지 못한 채 이를 악물었다.

더 이상 무슨 말을 할 수 있을까.

바보가 아닌 이상, 지금의 상황을 모를 리 없다.

현실은 몸서리칠 만큼 냉정했다.

그들은 패배했고, 적들은 승리했다.

모든 것을 끝내기 위해 되돌아온 것은 자무카도, 모용백도 아닌 산서인들이었다.

마치 하늘을 찌를 듯이 태원진가의 깃발을 높게 치켜세운 채, 단단한 진영을 갖춰 다가오는 그들의 발걸음에는 확신이 담겨 있었다.

승리를 향한 확신.

어쩌면, 자신들의 선두에 선 네 사람에 대한 확신이.

“가만있자. 저놈 저거 어디서 본 얼굴인데.”

마치 게으른 승려의 머리처럼, 까슬까슬하게 돋아난 머리카락이 타오르는 것처럼 붉다.

수십여 년의 세월을 되돌아간 노괴(老怪)를 마주한 모용위진이 몸을 떨었다.

“화, 화왕……!”

“아, 어렴풋이 생각나는구먼. 모용 뭐시기. 맞지?”

감 잡았다는 얼굴로 고개를 끄덕이는 적천강의 모습에, 옆에 서 있던 여인이 한숨을 내쉬었다.

“모용위진. 뭐시기가 아니라, 위진이에요. 모용세가의 무복을 입고 있으니 모용 씨인 건 당연한 거고.”

“위진? 그게 누군데.”

“그럴 수 있죠. 정마대전 당시에는 이립도 되지 않은 어린아이였으니.”

어언 팔순을 바라보는 나이가 되었음에도. 모용위진은 아무 말도 할 수 없었다.

화왕과 궁성이라는 두 괴물 앞에서, 그는 여전히 철없고 혈기왕성한 무림 초출이나 다름없었으니까.

나이도, 무공도.

그리고 이 자리에는, 그런 것 따위는 개나 줘 버린 누군가도 있었다.

“저기, 그 누구야. 모용 거시기.”

스승에 이어 제자에게까지 강제 개명을 당한 모용위진의 얼굴이 딱딱하게 굳은 그때. 성큼 앞으로 나선 진태경이 돌연 창을 휘둘렀다.

후웅!

맹렬한 파공성이 수십여 장의 거리를 가로지른다. 창날 끝에 꽂혀 있던 둥그런 형체가, 정확히 모용위진의 발치로 굴러떨어졌다.

툭.

발끝에 닿은 형체, 아니 한 사람의 머리를 본 모용위진이 자신도 모르게 신음했다.

“……가주.”

한 번 뱉은 말은 주워 담을 수 없는 법.

뒤늦게 실수를 깨달은 모용위진이 입을 다물었지만, 이미 물은 엎질러진 후였다.

“네놈이, 네놈이 감히…….”

“왜. 그 정도로는 부족해? 하나 더 줄까?”

진태경이 다시 한번 창을 휘둘렀고, 또 하나의 수급이 허공을 가로질렀다.

이번에는 초원 제일의 전사이자 대족장, 자무카의 얼굴을 알아본 유목민들이 입술을 깨물었다.

“더 필요하면 말해. 아니, 아니다. 방금 했던 말 취소.”

고개를 내저은 진태경이 걸음을 옮겼다.

저벅.

유난히도 무겁고, 선명하게 울려 퍼지는 발소리.

불그스름하게 달아오른 진태경의 눈동자가 너른 분지를 훑었다.

“너무 많아서 일일이 가져오기 힘드니까, 그냥 이 자리에서 만드는 게 낫겠다. 산지직송으로.”

“……!”

“……!”

모용세가와 유목민.

그 누구도 예외 없이, 모든 이가 본능적으로 뒷걸음질 쳤다.

아직 일만에 달하는 대병력이 남아있었음에도, 감히 대항할 수 없는 거대한 기세와 살기가 진태경의 중심으로 흘러나오고 있었다.

그리고 그 숨 막히는 침묵 속에서, 불현듯 울려 퍼진 목소리가 있었다.

“지금이라도 병장기를 내려놓고 투항한다면, 목숨만은 부지할 수 있다.”

세 초절정 고수의 존재에 가려져 있던 한 사람.

비록 수 갑자에 달하는 공력도, 그들과 어깨를 나란히 할 신위(神威)도 없었으나 알 수 없는 위압감이 있다.

어쩌면 그것은, 몰락해 가던 가문을 일으켜 세우고 산서성의 맹주(盟主)가 된 이만이 지닐 수 있는 위엄일지도 몰랐다.

“약조한다. 내 이름으로, 태원진가가 지닌 권위로.”

진위경은 담담하게 말을 이었다.

그의 시선이 향하는 방향 끝에는, 유난히도 초췌한 몰골을 한 젊은 부족장이 있었다.

“선택해라. 테무르.”

“……!”

“나는 그대를 안다. 자신의 의지로 이곳에 온 것이 아니라는 것 또한.”

테무르는 이를 악물었다.

“너무, 너무 멀리 와 버렸소.”

오랜 세월을 동고동락했던 형제가 죽었고, 그는 굴복했다.

테무르의 대답은 진심이었다.

초원으로, 고향으로 돌아가기에는 너무 멀리 와 버렸다.

하지만 그런 그를 향해, 진위경은 고개를 저었다.

“늦지 않았다. 적어도 아직까지는.”

“……어째서, 어째서 내게 이런 제안을 하는 거요.”

“이미 너무 많은 피를 흘렸으니까. 더 이상의 희생을 줄일 수 있다면, 무엇이든 할 수 있으니까.”

침착한 목소리와는 달리, 진위경의 볼을 타고 한줄기 눈물이 흘러내렸다.

“그뿐이다.”

눈물을 흘리는 진위경의 모습에, 오롯이 전해지는 그의 진심에 테무르는 숨이 막혔다.

그와는 너무나도 다른 길을 택한 자신이 떠올라서.

살기 위해 굴복하고, 그로 인해 오늘 이 자리에서 죽어 간 수많은 부족민들이 떠올라서.

“내가…… 어찌하길 바라시오.”

“놈!”

모용위진의 창노한 외침과 함께 모용세가의 무인들이 움직였지만, 어느새 빽빽한 돌격창의 숲이 그들을 에워싸고 있었다.

그리고 삽시간에 둘로 나뉜 일만의 군세 앞에서, 진위경은 입을 열었다.

“투항하고, 복속(服屬)하라. 완전히.”

“……!”

“과한가? 그렇다면 거절해도 좋다. 지금 당장 모용세가와 힘을 합친다 해도 상관없다. 다만.”

진위경의 목소리에 힘이 실렸다. 이내 거대한 외침이 되어 터져 나왔다.

“우리는 싸울 것이다. 반드시 장성을 넘어 초원을 짓밟고, 어떤 희생을 치르더라도 너희를 그곳에서 몰아낼 것이다!”

그 순간, 테무르는 등골을 타고 흐르는 한기를 느꼈다.

아니, 살아남은 수천의 유목민들 역시 마찬가지였다.

그들 모두는 똑똑히 듣고, 느꼈다.

설령 수백여 년이 걸리더라도. 헤아릴 수 없는 희생을 치른다고 해도 이 원한을 갚겠다는 진위경의 각오를.

악문 잇새 사이로 흘러나온 그 억눌린 목소리에 담긴 진심을.

그리고 이내, 선택할 수밖에 없었다.

“……황금씨족의 테무르.”

테무르는, 자무카의 빈자리를 채울 유일한 부족장은 고개를 숙였다.

장성 너머의 한족에게.

산서성의 맹주이자, 태원진가의 소가주에게.

“주군께 인사 올립니다.”

그 순간. 멈춰 있던 전장의 시간이 다시 흐르기 시작했다.

푸푸푸푹!

모용세가를 뒤덮는 돌격창의 숲. 그 뒤로 수천여 명의 산서인들이 태원진가의 깃발을 휘날리며 돌격했다.

피에 젖은 중양절(重陽節)의 밤이, 마침내 새벽을 맞아 깨어나고 있었다.



* * *



꿈인지 현실인지 분간조차 되지 않는 그 모호한 경계 안에서, 청년은 스스로의 존재조차 잊은 채 머릿속 켜켜이 쌓인 기억에 갇혀 있었다.

쐐액!

기껏해야 네다섯 살쯤 되었을까.

나이와는 어울리지 않는 진중한 표정으로, 제 키만 한 목검을 휘두르는 어린아이의 손끝을 따라 날카로운 파공성이 울려 퍼진다.

언제부터 몇 번이나 휘둘렀는지, 이미 자그마한 체구가 땀에 흠뻑 젖은 모습.

연무장 한 편에 서서 그 놀라운 광경을 지켜보던 이들이 연신 탄성을 흘렸다.



‘놀랍군. 검을 잡은 지 고작 반년밖에 안 된 어린아이가 저런 일검을 펼치다니.’

‘허어, 엄청난 무재(武才)가 나왔군.’

‘저 속도와 궤적을 보게. 빠르고 정확해. 나이가 믿어지지 않을 정도야.’

‘그보다 진정으로 놀라운 점은 노력할 줄 안다는 거겠지. 다들 한번 생각해 보게. 지금껏 살면서 저런 아이를 단 한 번이라도 본 적이 있었나?’

‘없었지. 소싯적 산서성 제일의 기재(奇才)로 불렸다는 대장로께서도 저 정도는 아니었을 걸세. 중원에 걸출한 인재가 워낙 많은 탓도 있었겠지만.’

‘어릴 적 많은 기대를 받았던 소가주님도 결국은 어느 날부터 무공보다 서책에 빠지지 않으셨나.’

‘아쉬운 일이지. 계속 검을 수련했다면 지금쯤 초일류의 경지에는 다다르셨을 테니.’

‘이미 지나간 일을 어쩌겠나. 가주께서도 워낙 종잡을 수 없는 분이시니, 그 핏줄을 고스란히 이어받으신 게지.’



가주.

한 사람이 무심코 흘린 그 두 글자에 모두가 입맛을 다셨다.

그러나 서로를 향한 묘한 눈빛과 함께 침묵이 흐른 것도 아주 잠시뿐.

쉴 새 없이 정확한 자세로 검을 펼치는 어린아이의 모습에, 사람들은 언제 그랬냐는 듯 대화를 이어 나갔다.



‘여하간 잘은 몰라도 중원의 명문대파에서도 저 정도 재목은 흔치 않을 걸세. 아니, 매우 드물겠지.’

‘본가에는 대단한 홍복이 틀림없네. 얼마 전 가모(家母)께서 산고로 돌아가신 이후부터 나이에 맞지 않게 어두워진 것이 마음에 걸리긴 하지만…….’

‘음.’



누군가가 흐린 말꼬리에, 모두의 얼굴이 어두워졌다.



‘안타깝지만, 어쩔 수 없는 일이지.’

‘어쩌겠나. 그것이 하늘이 정한 운명인 것을.’

‘운명이라. 무엇이?’



어디선가 들려온 목소리에, 두런두런 이어지던 대화가 뚝 끊겼다.

그리고 다음 순간, 약속이라도 한 것처럼 입을 다문 모두의 시선이 다급히 한 방향을 향해 쏠렸다.

가깝다고도, 멀다고도 할 수 없는 위치에서 이 모든 것을 지켜보던 청년 역시도.

‘가, 가주님!’

누군가가 황급히 토해 낸 외침을 들으며, 지금 막 고개를 돌린 청년은 문득 미간을 찡그렸다.

서쪽으로부터 번져오는 해 질 녘의 노을빛 때문일까. 천천히 가까워지는 한 사람의 얼굴을 똑바로 바라볼 수 없었다.

그저 왠지 모르게 익숙하고, 아련한 목소리만 귓가를 통해 전해질 뿐이었다.

‘어라, 반응들을 보니 내가 불청객이었던 모양이군.’

평범한 체구의 사내였다.

그 외에 더할 것도, 뺄 것도 없는.

그러나 얼굴이 보이지 않는 상황 속에서도, 청년은 뒤통수를 긁적이는 사내에게서 풍기는 독특한 분위기를 느낄 수 있었다.

물론 사내를 마주하게 된 다른 이들은 당혹스러움을 감추지 못했지만.



‘아, 아닙니다. 그럴 리가 있겠습니까.’

‘아니긴. 내가 그리 눈치 없는 사람으로 보이나?’



노을빛에 가려진 얼굴 아래, 희미하게 드러난 입술이 호선을 그린다.

말없이 눈치만 살피는 이들을 차례대로 훑은 사내가 재차 입을 열었다.



‘지나가는 길에 잠시 들른 것이니 신경 쓸 것 없네. 그보다 자네들이 둘째의 수련을 봐주고 있던 모양이군.’

‘어찌 그러겠습니까. 이공자께서는 타고난 무재가 워낙 뛰어나시니, 속하들로서는 감히 손을 댈 수 없을 지경입니다.’

‘그래, 당연히 그렇겠지. 누가 낳은 자식인데.’



짐짓 가슴을 내미는 사내의 모습에는 자랑스러워하는 기색이 역력했지만, 청년은 똑똑히 보았다.

그의 입가에 맺힌 미소가, 씁쓸하게 흐트러지는 것을.

그리고 사내가 나타난 그 순간부터 안절부절못하던 이들 역시 예외는 아니었다.



‘죄송합니다, 가주님.’

‘속하들이 그만 실언을 했습니다. 부디 벌을 내려 주십시오.’



무거운 목소리와 표정.

하나같이 고개를 떨군 그들의 모습에, 청년은 자신도 모르게 작게 혀를 찼다.

비록 자신이 누구인지, 이곳이 어디인지조차 모르는 그였지만 보고 들은 것이 있어 눈앞의 상황은 능히 짐작할 수 있다.

얼마 전 사별한 가주의 앞에서, 휘하의 가솔들이 감히 하늘의 운명을 운운하다니.

그 이야기에 담긴 의도를 떠나 벌을 받아 마땅한 일이었다.

국법(國法)이 지엄해야 나라가 바로 서는 것처럼, 한 가문에도 반드시 지켜야 할 것이 있는 법이니까.

그러나 가주라 불린 사내의 대답은, 청년의 예상을 한참이나 벗어났다.



‘벌이라니, 그게 갑자기 무슨 말인가?’

‘예?’

‘지나가는 길에 잠시 들른 것뿐이라니까. 아, 혹시 운명 어쩌고 하는 그 이야기가 나와 관련이 있었나? 무슨 심오한 대화를 하나 싶었는데.’

‘저, 그것이…….’

‘이렇게까지 나오니 슬슬 감이 잡히는군. 척하면 척이야. 또 매일 하릴없이 빈둥거리기만 하는 가주를 욕했겠지.’

‘가, 가주님. 그것이 아니고…….’

‘됐네. 거 사람들 하고는 참. 아무리 그래도 내가 명색이 가주인데, 이렇게 뒷담화나 하고 말이야.’



척하니 팔짱을 낀 사내의 모습에, 좌불안석이 된 이들이 서로의 얼굴을 힐끔거렸다.

사실대로 말을 해야 하나, 아니면 이대로 넘어가야 하나.

극심한 갈등 속에서 입술만 바짝 말라 가던 그때. 사내가 한숨을 푹 내쉬었다.

‘후우, 이렇게까지 실토를 하니 어쩔 수 없군. 가주 된 입장으로 모른 척 넘어가기도 뭐하니, 내 지금부터 자네들에게 벌을 내리지.’

곳곳에서 참았던 숨을 토해졌다.

마음의 짐을 안고 있는 것보다는 차라리 벌을 받는 것이 낫다. 한결 풀어진 얼굴을 한 그들을 향해 사내가 말을 이었다.



‘근신. 반나절.’

‘가, 가주님.’

‘요새 힘들어 보이던데. 반나절만 근신하고 다시 업무에 힘쓰게. 아, 특히 우리 첫째 좀 많이 도와주고.’



그것으로 끝이었다.

무어라 말하려는 가솔들을 향해 손을 내저어 축객령을 내린 사내는, 누가 온 것도 모르는 채 묵묵히 검을 휘두르고 있는 어린아이를 바라보았다.

비로소 주위의 모든 이목이 사라진 후에야, 작게 뇌까렸다.

‘운명이라. 운명…….’

문득 고개를 들어 하늘을 바라보는 눈빛은 공허하고, 이어지는 목소리에는 씁쓸한 감정만이 가득했다.

‘아니, 전부 내 탓이지.’

그리고 불현듯 고개를 돌리며 덧붙였다.

‘미안하구나, 무경아.’

자신을 똑바로 응시하는 그 시선에 청년의, 진무경의 눈앞이 새하얗게 물들었다.

‘아버지.’

그 순간.

드드드드득.

진무경을 둘러싼 모든 세상이 허물어졌다. 하늘 위에서 쏟아지는 눈부신 빛과 함께 낯익은 목소리가 귓가에 닿았다.

“어, 깼냐?”
```

## Final English reading copy

```markdown
# Chapter 979

At some point, everyone realized.

“Waaaaah!”

A tremendous roar shook heaven and earth as it rolled over the narrow gorge called Eight Spring Gorge.

The fighters who had been locked in fierce battle across the vast basin all turned their heads at once.

Their lips were cracked like drought-stricken fields. Their hands and feet trembled with utter exhaustion and fear of death.

After hours of fighting, they were covered in blood from head to toe. With desperate eyes, they stared toward the gorge’s entrance.

They prayed that the thunderous roar racing closer—and the countless footsteps pounding the earth—belonged to their allies.

Then, beyond the darkness slowly beginning to thin, a streak of light suddenly flashed.

*Shwaaaaa! BOOM!*

In an instant, a deafening crash mingled with screams.

But Iron Blood Saber Peng Cheolyeong, Family Head of the Hebei Peng Family, recognized the light—and laughed with all his might.

“Ha! Hahahaha!”

*Crack!*

With that booming laugh, he swung his great saber and swept through a dozen nomads in a single stroke.

Beneath the fountain of blood that soared into the air, the fewer than one thousand remaining warriors of Hebei pressed forward behind their Family Head.

Just moments ago, their bodies and weapons had felt as heavy as waterlogged cotton. Now, they were impossibly light.

As they advanced, laughing like madmen, a thick mist of blood rose around them.

*Shhk! Shhk-shhk!*

“Aaargh!”

“Guh!”

Screams erupted from every direction. Neither the Murong Family’s martial artists, trained in their clan’s secret arts, nor the nomads who had once struck fear across the land with lance and bow could stop the Hebei Peng Family.

No—more precisely, they had frozen at the sight of the unbelievable scene unfolding before them.

*Rumble!*

The ground shuddered.

With dawn approaching and the darkness fading, thousands of shadows poured from the narrow gorge’s entrance. A blood-soaked banner rose high above them.

The Great Taiyuan Jin Family.

“……!”

“……!”

It could mean only one thing.

Eyes fixed on the characters embroidered on the banner trembled.

Some with shock and despair. Others with hope and joy.

But there were also those who belonged to neither side.

“Enough! What do you think you’re doing?”

The Murong Family’s Head Elder, Murong Wijin, who had been directing the battlefield in Murong Baek’s place, shouted, channeling his internal energy into his voice.

His followers flinched beneath his venomous glare.

“Don’t fall for their petty tricks! This is—this is just…”

Murong Wijin clenched his teeth, unable to finish.

What else could he say?

Anyone who wasn’t a fool could see what was happening.

Reality was cruel enough to make them shudder.

They had lost. Their enemies had won.

And the ones who had returned to finish it all were neither Jamukha nor Murong Baek. They were the people of Shanxi.

The Taiyuan Jin Family’s banner was held so high it seemed to pierce the sky. Their ranks advanced in tight formation, their steps filled with certainty.

Certainty of victory.

Perhaps certainty in the four people leading them.

“Hold on. I’ve seen that guy’s face somewhere.”

His hair had grown into prickly stubble, like a lazy monk’s, and was so red it seemed to be on fire.

Facing the monster who looked decades younger than he ought to, Murong Wijin trembled.

“F-Fire King…!”

“Oh, now I vaguely remember. Murong… whatever. Right?”

At Jeok Cheongang’s nod, as if he’d finally figured it out, the woman beside him sighed.

“Murong Wijin. Not ‘whatever’—Wijin. And if he’s wearing the Murong Family’s uniform, obviously his surname is Murong.”

“Wijin? Who’s that?”

“That’s understandable. During the Great Faction War, he wasn’t even thirty. He was a child.”

Though Murong Wijin was nearing eighty, he couldn’t say a word.

In front of two monsters like the Fire King and the Bow Saint, he was still no more than a hot-blooded, inexperienced youth.

In age and in martial arts.

And there was someone else here who gave no damn at all about either.

“Hey, what’s your name again? Murong… thingy.”

Murong Wijin’s face had stiffened after being forcibly renamed by both Master and Disciple. Just then, Jin Taekyung stepped forward and suddenly swung his spear.

*Whoosh!*

A fierce roar split the air, crossing dozens of yards. The round object impaled on his spearhead fell right at Murong Wijin’s feet.

*Thump.*

When Murong Wijin saw what touched the tips of his shoes—an object that was, in fact, a person’s head—a groan escaped him before he could stop it.

“……Family Head.”

Once words were spoken, there was no taking them back.

Murong Wijin belatedly realized his mistake and clamped his mouth shut, but the damage was done.

“You… You dare…”

“What? Not enough? Want another?”

Jin Taekyung swung his spear again, and another head sailed through the air.

This time, the nomads bit their lips as they recognized Jamukha—the greatest warrior of the steppe and its Great Chieftain.

“If you need more, say so. No, wait. I take that back.”

Jin Taekyung shook his head and started walking.

*Thud.*

His footsteps rang out with unusual weight and clarity.

His reddish, smoldering eyes swept across the vast basin.

“There are too many to bring here one by one, so I guess it’d be better to make them right here. Fresh from the source.”

“……!”

“……!”

The Murong Family and the nomads—without exception, everyone instinctively took a step back.

Even though they still had an army of nearly ten thousand, an overwhelming aura and killing intent flowed from Jin Taekyung. No one dared challenge him.

And in the suffocating silence, a voice suddenly rang out.

“If you lay down your weapons and surrender now, I promise you’ll at least keep your lives.”

One man had been overshadowed by the three Supreme Peak masters.

He had neither several jiazi of internal energy nor the godlike power to stand shoulder to shoulder with them. Yet he commanded an inexplicable authority.

Perhaps it was an authority only someone who had raised a declining family and become the Alliance Leader of Shanxi Province could possess.

“I give you my word. In my name, and in the name of the authority held by the Jin Family of Taiyuan.”

Jin Wikyung continued calmly.

At the far end of his gaze stood a young chieftain who looked especially haggard.

“Choose, Temur.”

“……!”

“I know you. I know you didn’t come here of your own will.”

Temur clenched his teeth.

“We’ve… come too far.”

His brother, with whom he’d shared years of hardship, was dead. And Temur had submitted.

He meant what he said.

He had come too far to return to the steppe, to his homeland.

But Jin Wikyung shook his head.

“It’s not too late. Not yet.”

“……Why? Why are you offering me this?”

“Because too much blood has already been spilled. If I can prevent more people from dying, I’ll do anything.”

Unlike his composed voice, a tear ran down Jin Wikyung’s cheek.

“That’s all.”

Seeing Jin Wikyung weep—and feeling the sincerity behind it—left Temur breathless.

He thought of how different a path he’d chosen.

He thought of all the tribespeople who had died here today because he’d surrendered to survive.

“What… do you want me to do?”

“Bastard!”

At Murong Wijin’s furious shout, the Murong Family’s martial artists moved. But a dense forest of lances had already closed in around them.

Standing before the army of ten thousand, now split in two in the blink of an eye, Jin Wikyung spoke.

“Surrender and submit. Completely.”

“……!”

“Too much? Then you can refuse. I don’t care if you join forces with the Murong Family right now. But…”

Jin Wikyung’s voice hardened. Then it burst into a mighty shout.

“We will fight. We will cross the Great Wall and trample the steppe. Whatever the cost, we will drive you out of there!”

At that moment, a chill ran down Temur’s spine.

The thousands of surviving nomads felt it, too.

They all heard and felt Jin Wikyung’s resolve—to repay this grudge, even if it took hundreds of years and cost countless lives.

They heard the sincerity in his tightly restrained voice, seeping through clenched teeth.

And then, Temur had no choice but to decide.

“……Temur of the Golden Clan.”

Temur—the only chieftain who could fill Jamukha’s place—bowed his head.

To the Han Chinese beyond the Great Wall.

To the Alliance Leader of Shanxi and the Lesser Family Head of the Jin Family of Taiyuan.

“I offer my greetings, my lord.”

In that instant, time on the battlefield—which had stood still—began to flow again.

*Shhk-shhk-shhk!*

The forest of lances swallowed the Murong Family. Behind them, thousands of people of Shanxi charged beneath the fluttering banner of the Jin Family of Taiyuan.

The blood-soaked night of the Double Ninth Festival finally woke to the dawn.



* * *



In the hazy space between dream and reality, the young man had forgotten even that he existed, trapped in the layers of memory piled up in his mind.

*Shwaack!*

He looked no older than four or five.

The child’s hands swung a wooden sword as tall as he was, each stroke cutting the air with a sharp hiss. His face was serious in a way that didn’t suit his age.

No one knew when he’d begun or how many times he’d swung it. His tiny body was already soaked with sweat.

People standing at one side of the training ground watched in amazement, repeatedly letting out cries of admiration.

*“Incredible. A child who’s held a sword for only six months, and he can already deliver a strike like that.”*

*“Good heavens. What a martial talent.”*

*“Look at that speed and trajectory. Fast and precise. It’s hard to believe he’s so young.”*

*“More than anything, what’s truly amazing is that he knows how to work hard. Think about it, all of you. Have you ever seen a child like this in your life?”*

*“Never. Even the Head Elder, who was called Shanxi Province’s greatest prodigy in his youth, wasn’t like this. Though it’s true there are so many outstanding talents in the Central Plains.”*

*“The Lesser Family Head was so promising as a child, but then one day he got more interested in books than martial arts.”*

*“What a shame. If he’d kept training with the sword, he’d have reached at least the Supreme First Rate realm by now.”*

*“What can you do? It’s all in the past. The Family Head is so unpredictable, after all. I suppose his son inherited that from him.”*

Family Head.

At the two words someone let slip, everyone clicked their tongues.

But the silence, accompanied by strange glances exchanged between them, lasted only a moment.

As they watched the child practice his sword with flawless form, over and over, they resumed their conversation as if nothing had happened.

*“In any case, I don’t know much about the great sects of the Central Plains, but I doubt they have many talents like him. No, they must be quite rare.”*

*“Our family has surely been blessed. It does trouble me that he’s grown so gloomy for a child his age since the Family Head’s wife died in childbirth not long ago…”*

*“Mm.”*

At someone’s faltering words, everyone’s faces darkened.

*“It’s tragic, but there’s nothing to be done.”*

*“What can we do? It’s the fate ordained by Heaven.”*

*“Fate? What fate?”*

At the voice that came from somewhere, the murmured conversation abruptly stopped.

The next moment, as if they’d planned it, everyone fell silent and hurriedly turned their eyes in one direction.

So did the young man, who had been watching it all from a spot neither near nor far.

“F-Family Head!”

Hearing someone blurt out the cry in a rush, the young man—who had just turned his head—furrowed his brow.

Perhaps it was the sunset spreading from the west. He couldn’t make out the face of the man slowly approaching.

All he could hear was a voice that felt strangely familiar, tinged with a lingering sadness.

*“Well, judging by everyone’s reaction, I must be an unwelcome guest.”*

He was an ordinary-looking man.

Nothing more to add, nothing to take away.

But even though he couldn’t see the man’s face, the young man could sense the distinctive air around him as he scratched the back of his head.

The others facing the man, of course, couldn’t hide their confusion.

*“N-No, of course not.”*

*“Don’t give me that. Do I look that oblivious?”*

Beneath the face hidden by the sunset, his faintly visible lips curved into a smile.

The man looked over the people who were silently watching him, then spoke again.

*“I was just passing by and thought I’d stop in. Don’t mind me. It looks like you were watching my second son train.”*

*“We could hardly claim to be teaching him. The Second Young Master is so gifted that there’s nothing we dare try to correct.”*

*“Of course he is. Whose son do you think he is?”*

The man puffed out his chest as though he were proud, and he certainly looked it. But the young man saw clearly as the smile at the man’s lips turned bitter and fell apart.

Nor were the people who’d been restless ever since the man appeared any different.

*“We’re sorry, Family Head.”*

*“We spoke out of turn. Please punish us.”*

Their voices and expressions were heavy.

Watching them lower their heads one by one, the young man clicked his tongue softly without realizing it.

He didn’t know who he was or where he was, but he could infer what was happening from what he’d heard and seen.

To speak of Heaven’s fate in front of a Family Head who had recently lost his wife…

Whatever they’d meant by it, they deserved punishment.

Just as a nation needed strict laws to stand firm, a family had things it must uphold.

But the man called Family Head answered in a way that went far beyond the young man’s expectations.

*“Punishment? What are you talking about all of a sudden?”*

*“Pardon?”*

*“I told you, I just stopped by on my way past. Oh, was that talk about fate and all that related to me? I wondered what profound conversation you were having.”*

*“W-Well, that is…”*

*“Now that you’ve gone this far, I’m starting to get the picture. I know how this goes. You were bad-mouthing the Family Head who does nothing but laze around every day again, weren’t you?”*

*“F-Family Head, that’s not…”*

*“Enough. You people, honestly. I may be the Family Head, but you can’t just gossip about me behind my back.”*

The man folded his arms. The people, on tenterhooks, glanced at one another.

Should they tell the truth, or let it go?

As they agonized, their lips growing parched, the man let out a deep sigh.

*“Whew. You’ve confessed this much, so there’s no choice. As Family Head, I can’t just pretend I didn’t hear it. I’ll punish you now.”*

Here and there, people let out breaths they’d been holding.

Better to be punished than to carry the weight of guilt. Their faces relaxing, they listened as the man continued.

*“House arrest. Half a day.”*

*“F-Family Head…”*

*“You’ve looked tired lately. Stay under house arrest for half a day, then get back to work. Oh, and especially help our eldest a lot.”*

That was all.

The man waved away the family retainers trying to say something and dismissed them. Then he looked toward the child, who continued swinging his sword without even knowing anyone had arrived.

Only after every pair of eyes around them had turned away did he murmur softly.

*“Fate. Fate…”*

His eyes lifted suddenly to the sky, empty. His next words were filled with nothing but bitterness.

*“No. It’s all my fault.”*

Then he turned his head abruptly and added,

*“I’m sorry, Mukyung.”*

Under that gaze, fixed straight on him, the young man’s—Jin Mukyung’s—vision turned white.

*“Father.”*

At that moment—

*Rrrrrumble.*

The entire world surrounding Jin Mukyung crumbled away. Brilliant light poured down from above, and a familiar voice reached his ears.

“Hey, you awake?”
```
