<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0858.txt",
      "sha256": "cfe26206f363f6f5a238faea6b87bf79e4234ab6c58732a675b1a90ed73a7d17",
      "bytes": 13179
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b21f9599d6cb29c6982da43615354ad9c2f3be8d3d1f1d79404ca323bb8e054e",
      "bytes": 2043
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a64d49e7e1c20ab1e874c8ff940450d59f2831f857de305387093220f1603d55",
      "bytes": 228551
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "39bce5c54293e844edfc8f5e95698cef83c2e3a60f23f20d3cb29ee70e38f679",
      "bytes": 759
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "a5e8bded945cc257a0ae12fc369c497194e2a07d7ab2b81e6fdb8bf882bc78fb",
      "bytes": 1378
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "3d2a33958bfea0a0615e300f36bf7d52410a3bdf71b5c4adea0e38717118d547",
      "bytes": 1511
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "7a36f3f2d0b4dbaf9d8759270d4406029e5d65072e0c4488fda3e18c3353a48f",
      "bytes": 1782
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "59595ace05794f933f4b427c4e6024d4733caf11a38d839a4b2c26a3c23a1f2b",
      "bytes": 622
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "a6363dc423f3644a547c940324934a84ba21f1dcb840731b6930180d04235b14",
      "bytes": 699
    },
    {
      "path": "characters/Li Feng.md",
      "sha256": "a1a571ef080b68219982bc8cc0dd52437800d3b5fab97fe9253c24809a389d4f",
      "bytes": 888
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "497cda61d39e8c6617c08f2c84fbab1c79cb25ab29d9c3b1b720f1c86f445951",
      "bytes": 883
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ea85ad3c50cfb807e781896de86a71c14e55f4677ff88f4a620dfe4a3c9fef69",
      "bytes": 253815
    }
  ],
  "estimated_tokens": 12557
}
-->

# Durable State Update — Chapter 858

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
1 and safe_through 858. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 858. Profile updates may replace only one
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
  "chapter": 858,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 858,
    "continuity_sources": [858],
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
    "The Divine Physician secured the Blood Soul Gu found in the deceased City Lord of Sichuan Province; it weakens hosts, causes madness, and eventually kills them.",
    "Jin suspects Dark Heaven’s covert killing of the City Lord is part of a scheme targeting the Great Nation, possibly its imperial family.",
    "Prince Shangshan Zhu Bao is traveling toward the imperial capital with Hong Jin and fifty Embroidered Uniform Guard members.",
    "The late Emperor entrusted Hong Jin with Zhu Bao’s care; Hong Jin fears the current Emperor intends harm, while Zhu Bao trusts his elder brother.",
    "Jin’s party reached Jiangsu after an arduous journey and is exhausted; Jin insists the group stay together, and the Divine Physician is traveling with them to treat Jin.",
    "Hyuk Mujin has encountered Commander Jeong and the Embroidered Uniform Guard while separated from the person he serves; he is carrying a stolen Guard badge.",
    "An unidentified young man appeared above the Guard procession, claimed to be its mastermind, and addressed Commander Jeong as if familiar with him before denying that he knew him."
  ],
  "continuity_sources": [
    856,
    857
  ],
  "open_questions": [
    "Why did Dark Heaven secretly kill the City Lord of Sichuan Province, and is it targeting the Emperor or imperial family?",
    "What does the Emperor intend for Prince Shangshan, and what prompted the imperial decree against Hong Jin?",
    "Who is the young man who appeared above the Guard procession, and what is his connection to the apparent ambush?",
    "What explains the attackers’ unnatural ferocity during the caravan assault?"
  ],
  "safe_through": 857,
  "temporary_decisions": [
    "Render 혈혼고 as “Blood Soul Gu.”",
    "Render 대국 as “Great Nation.”",
    "Render 금의위 as “Embroidered Uniform Guard.”",
    "Render 강소 as “Jiangsu.”",
    "Distinguish 홍건적 as “Red Turban Bandits” from 홍건군 as “Red Turban Army.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 일신     | **One God**         |
| 태원진가   | **Jin Family of Taiyuan**        |
| 화산파    | **Huashan**                      |
| 삼류     | **Third Rate**    |
| 이류     | **Second Rate**   |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 낭인     | **wandering martial artist**                     |                                                       |
| 제자     | **Disciple**                                 |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 경험치              | **EXP**                        |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 사천     | **Sichuan**            |
| 화산     | **Huashan**            |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 이풍 | **Li Feng** | Shanxi Province's Assistant Military Commissioner; former Huashan lay disciple |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 평화 | **Peace Guild** | Guild name. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 도지휘첨사 | **Assistant Military Commissioner** | Military office held by the unnamed official responsible for training soldiers. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 허공답보 | **Stepping on Empty Air** | Technique that allows Jongni Chu to move through empty air as if climbing invisible stairs. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 사천성 | **Sichuan Province** | Province form used in the title of its chief official. |
| 사천성주 | **City Lord of Sichuan Province** | Title held by Won Gyun. |
| 호위장 | **Captain of the Guards** | The Sichuan City Lord's guard captain. |
| 강소 | **Jiangsu** | Province at the eastern end of the Yangtze route. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 답보 | **stagnation** | Taekyung's current lack of progress in martial arts. |
| 심해 | **deep sea** | Unexplored ocean depths where the ancient monster awakens. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 관리 | 진태경 | official_to_young_martial_artist | Young Master | formal-polite | The official addresses Taekyung as 공자 while explaining the consequences of Prince Shangshan's displeasure. |
| 이풍 | 진태경 | senior_official_to_respected_young_martial_artist | Young Hero Jin | formal and respectful | Addresses Taekyung as 진 소협 after praising his reputation. |
| 진태경 | 주표 | visitor to prince | His Highness, Prince Shangshan | formal-deferential | Addresses Zhu Bao as 상산왕 전하 after kneeling to meet his gaze. |
| 주표 | 진태경 | prince to visiting young hero | Jin Taekyung | formal and inquisitive | Uses the formal second-person address before asking Taekyung's name and requesting an autograph. |
| 진태경 | 이풍 | junior_to_respected_official_and_martial_ally | Great Hero Li | polite and respectful | Agrees with Li Feng's proposal that Zhu Bao visit the Jin Family's banquet. |
| 이풍 | 주표 | official_to_prince | Your Highness | formal-deferential | Suggests that Zhu Bao visit the Jin Family's grand banquet in fifteen days. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 사천성주 | 진태경 | official_to_imperial_messenger | Messenger of His Highness Prince Shangshan | formal-deferential | The City Lord addresses Taekyung deferentially after seeing Prince Shangshan's Token. |
| 진태경 | 사천성주 | visitor_to_city_lord | City Lord | sarcastic-polite | Taekyung jokingly praises him as our City Lord after making him fund the reward. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 사천성주 | 호위장 | provincial_city_lord_to_guard_captain | Captain of the Guards | imperious and dismissive | The City Lord directly orders the Captain of the Guards to handle the troops stationed near Chengdu. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 관리 | 적천강 | government official to legendary martial master | you | formal, then alarmed and deferential | The official questions Jeok Cheongang, insults him as an old man, and later learns that he is the Fire King. |
| 적천강 | 관리 | legendary martial master to government official | you | blunt and mocking | Jeok Cheongang repeatedly echoes the official's formal phrasing while challenging his authority. |
| 정호 | 진태경 | Shaolin Discipline Hall Master to patient and Benefactor | Benefactor Jin | formal-polite | Jung Ho repeatedly uses 진 시주 and 시주. |
| 진태경 | 정호 | patient to Shaolin Discipline Hall Master | Monk | polite and familiar | Taekyung addresses Jung Ho as 스님. |
| 경호원 | 진태경 | government_security_officer_to_protected_Hunter | Hunter Jin Taekyung | formal and deferential | The security officers repeatedly address Jin as 진태경 헌터님 while explaining his temporary protection and legal status. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 적천강 | 호위장 | martial artist to official subordinate | you; bastard | blunt and threatening | Jeok uses familiar, insulting address while interrogating the Captain of the Guards. |
| 호위장 | 적천강 | official subordinate to senior martial artist | Sir | deferential | The Captain shifts to respectful speech after sensing Jeok’s status and danger. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 857
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 857
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; loyal even when left behind, irreverently self-deprecating, and willing to face danger rather than abandon the person he serves. He is proud, glory-seeking, suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 856
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts his publicly acknowledged Disciple and intended heir Jin Taekyung, warmly regards Ju Hwaran and hopes she and Jin grow closer, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 855
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; they trust each other deeply, though their bond remains unformalized. Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master; Ju Hwaran is a trusted Fire Dragon Pavilion member; Magic Johnson and Chuck Hagel are allied to him; his mother and sister Hayeon are among those he protects; the Skeleton King is his friend and ally; Xiao Shen regards him as an older brother; Jin-ho is his older friend and trusted confidant; he once saved Ju Wongong’s life.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 855
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 838
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Li Feng.md

# Li Feng (이풍)

- **Safe through:** Chapter 184
- **Aliases:** None
- **Role:** Assistant Military Commissioner of Shanxi Province; former Huashan lay disciple who left the sect nearly ten years ago
- **Personality:** Resolute, proud, blunt, and hostile toward political and martial rivals
- **Voice:** Formal and restrained in official settings; dry and cutting with opponents
- **Relationships:** Former lay disciple of Huashan; visited the hidden residence of his Grandmaster Mae Jonghak and saw ten-year-old Cheongpung there; recognizes Cheongpung as his Martial Uncle; direct subordinate and political rival of Hong Jin, the Deputy Military Commissioner; agrees to act as Hong Jin's intermediary with Huashan and send a messenger pigeon to his Master; bears a humiliating martial grievance involving Gong Ilhyuk

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 856
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is an early-adolescent member of the imperial family and an exceptionally skilled young swordsman who has trained daily for three years.
- **Personality:** Earnest, compassionate, and eager to emulate Jin Taekyung; he takes responsibility for his loyal subjects’ hardship, though his trust in his elder brother shows his youth.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s only younger full brother; the late Emperor entrusted Hong Jin with his care, and Zhu Bao admires Jin Taekyung and seeks to emulate him.

## Korean source

```text
＃858화



이럴 때는 시스템의 빈자리가 크게 느껴진다.

그 지랄 맞은 업데이트만 아니었더라면, 지금쯤 특유의 맑은 종소리와 함께 홀로그램 창이 떴을 텐데.

띠링.



- 퀘스트, [상산왕 일병 구하기]를 성공적으로 완수하셨습니다!

- 퀘스트 완료 보상이 주어집니다!

- 대량의 경험치를 획득했습니다!



뭐 이런 식으로.

하지만 문득 떠올린 상상과는 달리 현실은 고요했고, 수십여 명의 금의위로부터 흘러나온 냉엄한 살기(殺氣)는 바늘처럼 내 전신을 쿡쿡 찔렀다.

“그만하면 됐으니까 적당히 하고 갈무리해라. 자꾸 이러면 나도 기분이 더러워지잖아.”

한 마디를 툭 던진 나는, 나뭇가지를 박차고 지면으로 떨어져 내렸다.

아니, 텅 빈 허공을 마치 계단처럼 밟으며 걸어 내려갔다.

“허공답보(虛空踏步)……!”

누군가의 탄식이 귓가에 닿는다. 예리한 칼날 같던 금의위의 기세가 흔들리는 것이 피부로도 느껴지는 듯했다.

‘공력 소모는 끔찍하지만, 확실히 이것만 한 게 없지.’

제아무리 적의를 띤 상대라 해도 이런 광경을 본 이상은 감히 이빨을 들이대지 못한다.

허공답보는 초절정 고수들만의 전유물이니까.

사박.

그리고 사뿐히 지면을 밟으며 내려선 나를 기다리고 있던 건, 서럽게 울부짖는 한 마리의 짐승이었다.

“으허엉, 조장니임!”

“멈춰. 오지 마. 입 다물어.”

“어디 갔다가 이제 오신 겁니까! 제가 얼마나 무서웠는데!”

“…….”

이 새끼가 기껏 분위기 잡아 놨더니.

한숨을 푹 내쉰 나는 자꾸만 껴안으려는 혁무진을 밀어 내며 대답했다.

“아, 그만 좀 징징대. 버리고 간 적 없으니까.”

“예?”

“그냥 위에서 한숨 잤어. 피곤해서.”

장장 열흘이 넘도록 이어진 강행군이다.

삼 갑자의 공력과 인간의 한계를 벗어난 신체 능력으로도 수면욕은 이길 수 없었다. 사실 지금까지 버틴 것부터가 기적에 가까운 일이긴 하다.

혹시 모를 상황을 대비한 척후와 불침번. 일행들의 상태 체크 및 관리. 거기에 더해 심적 부담감까지.

아마도 신의의 만류와 적천강의 도움이 아니었더라면 강소성에 도착하기도 전에 쓰러졌을지도 모른다.

몸도 성치 않은 상황에서 사흘에 반 시진 꼴로 잤으니까.

그렇게 개고생을 해 가며 목적지에 도착한 직후, 금의위보다 한발 앞서 도착했다는 확신이 들자 잠이 쏟아진 건 당연한 일이었다.

“……그래서, 주무셨다고요? 그것도 나무 위에서?”

“어. 길에서 자면 입 돌아가잖아. 곯아떨어진 상태에서 습격당할지도 모르고.”

“그럼 저는요?”

“너? 너 뭐?”

“아니, 저는 왜 길 한복판에 던져 놓고 혼자서 안전한 곳에서 주무셨냐는 거죠.”

“누구는 길을 지키고 있어야지. 그리고 안 던졌어.”

“그럼요?”

“내려놨어. 조심스럽게.”

사실 대충 내던졌다. 하도 힘들어서.

약간의 거짓이 섞인 내 대답을 들은 혁무진이 입을 딱 벌렸다.

“저는 입 돌아가도 상관없는 놈입니까?”

“입이 삐뚤어져도 말은 바로 하는 남자. 그게 바로 혁무진 아니냐.”

“습격당할 수도 있다면서요!”

“그 소리를 듣고 내가 깨어나겠지. 지금처럼.”

“하마터면 죽을 뻔했잖습니까! 촌각만 늦게 일어나셨으면 저는 완전히 죽은 목숨이었다고요!”

“그래서 촌각 일찍 일어났잖아. 살았고.”

“세상에. 조장님 진짜 사람 맞습니까?”

저게 내 등에 업혀 코까지 골며 자던 새끼가 할 말인가 싶지만, 나는 한 줄기 자비를 발휘해서 넘어가 주기로 마음먹었다.

워낙 강행군이기도 했고, 또…….

조금 전 보았던 녀석의 모습이, 상당히 감명 깊었으니까.

“잘했다.”

불쑥 내뱉은 칭찬에, 혁무진이 눈살을 찌푸렸다.

“예?”

“잘했다고. 이런 상황에서도 버틴 거.”

“……!”

“그래도 다음부터는 그러지 마라. 도저히 이기지 못할 것 같으면, 한 걸음 물러서서 다른 방법을 생각해 봐야지.”

혁무진의 어깨를 두드려 준 나는 천천히 돌아서며 덧붙였다.

“그렇지? 금의위 나으리.”

허공에서 시선과 시선이 부딪친다.

별다른 감정이 느껴지지 않는 무덤덤한 눈동자. 동요하는 다른 이들과는 달리 내 등장에도 눈 하나 깜짝하지 않고 있던 선두의 사내가 입을 열었다.

“그걸 알고 있음에도 앞길을 막아서다니. 실로 무모하기 짝이 없군.”

“아저씨. 말조심해. 나 아직 숱 많아.”

“무슨 헛소리인지는 모르겠지만, 그대는 지금 황명(皇命)을 받드는 금의위와 맞서고 있다. 알고 있는가?”

“설마 모르겠냐?”

“알겠다. 그렇다면 역모(逆謀)를 인정하겠다는 거군.”

역모?

이게 그렇게 되나.

잠시 고민하던 나는 앞서 내뱉은 말을 정정할 필요성을 느꼈다.

“음. 그럼 아까 했던 말 취소.”

“……?”

“잠깐 가던 길에 피곤해서 잠을 잤는데, 때마침 당신들이 지나가고 있던 거지. 어때, 이거 괜찮냐?”

앞서 들었던 칭찬 때문인지, 살짝 감동한 표정으로 날 바라보고 있던 혁무진이 잽싸게 대답했다.

“제가 듣기에는 괜찮은 것 같은데요.”

“그렇지?”

“예. 설득력이 있잖습니까. 풍진 노숙 하는 사람이 한둘도 아니고.”

“네가 뭘 아는구나. 하긴, 우연이라는데 뭐 어쩔 거야.”

“그럼요. 강소성이 지들 땅도 아닌데.”

“잠깐만. 그건 사실이지 않냐? 어차피 강소성이든 어디든 대국에 속한 영토일 텐데.”

“어라, 그게 그렇게 됩니까?”

“아니야? 내가 아는 상식으로는 그런데.”

“조장님이 그런 상식도 있으셨습니까?”

“개새끼가.”

“죄송합니다. 여하튼 일단 기억해 뒀다가 나중에 남 노인께 물어 보…… 어, 그런데 다들 어디 있어요?”

내가 막 대답해 주려던 찰나. 사내가 한 박자 먼저 입을 열었다.

“이게 무슨 짓거리들이냐.”

“아, 미안. 잠깐 다른 얘기 좀 하느라. 그나저나 말이 나왔으니 말인데, 강소성도 당신네들 땅 맞지?”

“천하의 강산은 모두 지엄하신 황제 폐하께서 다스리시는…… 아니, 도대체 내가 왜 이런 걸 대답해 줘야 하는지 모르겠군.”

“서로 돕고 살면 좋지 뭘.”

“그만!”

우리의 정신없는 대화를 듣다 보니 멘탈이 흔들린 모양이다.

나는 어느덧 서릿발 같은 기세를 뿜어내는 사내를 바라보며 눈을 가늘게 떴다.

“거기 금의위 나으리, 정 천호(千戶)라고 했지? 왜 그렇게 퍽퍽하게 굴고 그래. 막말로 여기서 붙어 봤자 서로 득 볼 것도 없는데.”

스릉.

대답 대신 서늘한 날붙이가 모습을 드러냈다. 등에 메어 놓았던 거대한 태도(太刀)를 뽑은 정 천호가 딱딱한 음성으로 입을 열었다.

“그대가 누구인지는 상관없다. 금의위는 황상 폐하의 명을 따를 뿐, 황명에 반하여 앞길을 막아선다면 죽음뿐이다.”

스아아아아.

보이지 않는 기운이 그를 중심으로 뻗어 나온다. 지극히 정순하면서도 무거운 기파(氣波)를 느낀 나는 마른 입술을 핥았다.

‘이것 봐라…….’

처음 봤을 때부터 짐작은 했지만, 정 천호라 불린 저 사내는 상당한 고수였다.

아니, 일반적인 기준에서는 상당하다는 표현마저도 부족할 것이다. 그는 내가 내심 품고 있던 편견을 깨트릴 정도의 실력자였으니까.

‘아직 초절정의 벽은 넘지 못한 것 같지만, 어림잡아도 절정의 끝자락.’

관과 무림은 언제나 가까우면서도 멀다.

무림은 대국(大國)이라는 울타리 안에 존재하는 하나의 숲이지만, 그 안에는 용과 호랑이 같은 맹수들이 득실거린다.

그러나 정작 관에 속한 이들 중, 제대로 된 고수는 지금까지도 몇 보지 못했다.

일반 병졸들은 삼류에서 이류, 무관들은 끽해야 일류였으니 군문(軍門)에 몸담은 이들 중 절정 고수는 흔치 않았다.

‘그마저도 대부분이 무림에 몸담았던 이들이었지.’

전(前) 사천성주의 호위장은 유명한 낭인 출신에 사실상 개인 경호원에 가까웠고, 산서성 도지휘첨사(都指揮僉事)라는 요직을 맡고 있는 이풍은 화산파의 속가제자에서 무과를 통해 군문에 투신한 케이스다.

그런데…….

‘저 정도 수준의 고수가 어디서 튀어나온 거지?’

비록 내 견문(見聞)이 그리 넓은 편은 아니지만, 명색이 초절정 고수답게 척 보면 금방 견적이 나온다.

그리고 내 시선으로 확인한 정 천호는 무림인 특유의 흔적이 조금도 묻지 않은, 그야말로 장군이라는 두 글자를 머리부터 발끝까지 쏟아부은 듯한 인물이었다.

‘심지어 공력까지 정순하고.’

더 놀라운 것은, 다른 금의위들조차 예외가 아니라는 점이다.

이십 대로 보이는 젊은이부터 사십 언저리로 보이는 중년인까지. 각자의 수준 차이는 있지만 그들 중 대부분이 절정 고수라는 것쯤은 어렵지 않게 파악할 수 있었다.

‘절정 고수만 수십이라…….’

어지간한 중견 문파와 맞먹는, 아니 그 이상의 전력.

천자의 손발 노릇을 하는 금의위답게 그만한 이름값을 하는 것인지, 혹은 천자가 아닌 누군가에 의해 길러진 것인지는 나중에 생각해야 할 문제다.

나는 서로 얻을 것이 없는 이 팽팽한 대치를 계속해서 이어 갈 생각이 없었으니까.

“기세는 좋은데, 각자 들고 있는 그 흉한 물건들은 곱게 집어넣는 게 좋을 거야. 다치기 전에.”

경고와 함께 발걸음을 뗀 순간.

슈확!

강맹한 파공성과 함께 코앞으로 쇄도한 빛줄기를, 나는 부드럽게 감싸 안듯이 잡아채어 날아왔던 방향으로 쏘아 보냈다.

푹! 쿠웅!

단말마 대신 땅을 타고 전해지는 진동.

미간 정중앙에 화살을 박아넣은 채 쓰러진 준마(駿馬)의 말안장에서 뛰어오른 궁수가 믿을 수 없다는 듯한 시선으로 나를 바라보았다.

“손에 든 그거, 곱게 집어넣으랬지.”

“……!”

“너 때문에 죽은 거야. 이 동물 학대범 새끼야.”

마치 이럴 줄 알았다는 듯, 땟국물 가득한 몸을 긁적이고 있던 혁무진이 말했다.

“왜 저 사람 때문이에요? 조장님이 죽이신 거잖아요.”

“굳이 따지면 그게 맞지. 그런데 무진아.”

“예.”

“너도 죽일 수 있어.”

“죄송합니다. 제가 실언을 했네요.”

“그래, 알았다.”

여느 때와 같은 평화로운 대화였지만, 이미 장내의 분위기는 팽팽하다 못해 터질 것처럼 부풀어 올라 있었다.

푸륵. 푸르륵.

수십 필의 말들이 거친 숨을 뿜어낸다. 있는 힘껏 고삐를 움켜쥔 손들은 새하얗게 물들어 있었고, 그들이 내뿜는 기세는 흔들릴지언정 갈무리되지 않았다.

그리고 그 선두에, 정 천호가 있었다.

“끝내 건너서는 안 될 강을 건너는구나.”

“아직 그 강을 건너진 않았지만, 그거랑은 별개로 다들 자신 있나 보네. 제아무리 한 가락 하는 실력이어도 나랑 붙으면 좋은 꼴은 못 볼 텐데.”

“나와 저들이 믿는 것은 일신의 무예 따위가 아니다. 지엄하신 황제 폐하의 명을 받드는 신하로서의 충심(忠心)일 뿐.”

“당신, 이름이 뭐지?”

“정호군.”

예상했던 것보다 훨씬 순순히 이름을 알려 준 정 천호, 아니 정호군이 나를 향해 되물었다.

“그대는?”

“진태경.”

지금 이 대답은 내가 한 것이 아니다.

나와 정호군은 동시에 고개를 돌렸다. 그리고 동시에 한쪽 무릎을 꿇으며 예를 갖추었다.

저벅.

내리깐 시선 속, 기억 속에 존재하는 마지막 모습보다 훨씬 커진 누군가의 발이 시야에 들어온다.

이제는 어린아이를 넘어, 보다 성숙해진 목소리도 함께.

“오랜만이구나. 태원진가의 진태경.”

상산왕 주표.

훌쩍 자라난 용의 핏줄이 나를 일으켜 세운다.

그리고 뭐라 대답하기도 전에, 손에 쥐고 있던 무언가를 건넸다.

‘이건.’

밀서(密書).

그 은밀한 단어가 뇌리를 관통한 순간. 상산왕 주표가 귓가에 대고 속삭였다.

“서명을 부탁한다.”

“…….”

아니 씨발, 전하.
```

## Final English reading copy

```markdown
# Chapter 858

This was when I really felt the System’s absence.

If it weren’t for that damn update, a holographic window would’ve appeared by now, accompanied by its signature clear chime.

*Ding.*

> **System**
>
> Quest **Saving Prince Shangshan** successfully completed!
>
> Quest completion rewards have been granted!
>
> You have gained a large amount of EXP!

Something like that.

But reality was quiet, unlike the scene I’d just imagined. The cold killing intent pouring from dozens of Embroidered Uniform Guard members pricked my entire body like needles.

“That’s enough. Take it down and put it away. Keep this up and you’ll put me in a bad mood.”

I tossed out a few words, then pushed off a branch and dropped toward the ground.

No—I walked down through empty air, stepping on it as if it were a staircase.

“Stepping on Empty Air……!”

Someone’s gasp reached my ears. I could almost feel the Embroidered Uniform Guard’s blade-sharp aura waver.

*It burns through internal energy like crazy, but nothing beats it for this.*

No matter how hostile someone was, after seeing something like that, they wouldn’t dare bare their teeth at me.

Stepping on Empty Air was a technique exclusive to Supreme Peak masters.

*Tap.*

I landed lightly on the ground. Waiting for me there was a beast howling miserably.

“Waaah, C-Captain!”

“Stop. Don’t come over here. Shut up.”

“Where have you been all this time?! I was so scared!”

“……”

I’d gone to all that trouble to set the mood, and this bastard—

I let out a deep sigh and pushed Hyuk Mujin away as he kept trying to hug me.

“Ah, quit whining. I didn’t leave you behind.”

“What?”

“I just took a nap up there. I was tired.”

We’d been on the move for over ten days straight.

Even with three jiazi of internal energy and a body beyond human limits, I couldn’t beat the need for sleep. The fact I’d made it this long without collapsing was practically a miracle.

Scouting and night watch, just in case. Checking on the others and looking after them. And on top of that, the mental strain.

If the Divine Physician hadn’t tried to stop me and Jeok Cheongang hadn’t helped, I might have collapsed before we ever reached Jiangsu.

I wasn’t exactly in good shape, either. I’d been sleeping for half a shichen every three days.

After going through all that hell, it was only natural that sleep had hit me the moment we reached our destination and I was sure we’d arrived ahead of the Embroidered Uniform Guard.

“……So you slept? In a tree?”

“Yeah. If I slept on the road, my mouth would get crooked. And I might get attacked while I was out cold.”

“What about me?”

“You? What about you?”

“I’m asking why you threw me down in the middle of the road while you went somewhere safe to sleep by yourself.”

“Someone had to keep watch on the road. And I didn’t throw you.”

“Then what did you do?”

“I set you down. Carefully.”

I’d actually more or less tossed him down. I was that tired.

Hyuk Mujin’s mouth fell open at my slightly dishonest answer.

“So it doesn’t matter if my mouth goes crooked?”

“You’re the kind of man who speaks the truth even with a crooked mouth. That’s Hyuk Mujin.”

“You said we could be attacked!”

“And I’d wake up when I heard it. Like I did just now.”

“I almost died! If you’d woken up moments later, I’d have been a dead man!”

“But I woke up moments earlier. You’re alive.”

“My God. Captain, are you even human?”

I wasn’t sure what gave the bastard who’d been snoring on my back the right to say that, but I decided to show him a little mercy and let it slide.

We’d been pushing ourselves hard, and besides……

The way he’d looked a little while ago had been pretty impressive.

“Good job.”

At my sudden praise, Hyuk Mujin furrowed his brow.

“What?”

“I said you did a good job. Holding on even in a situation like that.”

“……!”

“But don’t do that again. If you think you can’t win, take a step back and think of another way.”

I patted Hyuk Mujin on the shoulder, then slowly turned around and added,

“Right, Your Excellency from the Embroidered Uniform Guard?”

Our eyes met in midair.

His eyes were impassive, showing no particular emotion. Unlike the others, the man at the head of the procession hadn’t so much as blinked at my appearance. He spoke.

“You know that, and yet you blocked our way. Reckless, to say the least.”

“Mister, watch your mouth. I’ve still got plenty of hair.”

“I don’t know what nonsense you’re talking about, but you are standing against the Embroidered Uniform Guard, who are carrying out the Emperor’s command. Do you understand that?”

“Of course I do.”

“I see. So you admit to treason.”

“Treason?”

Could it really be called that?

After a moment’s thought, I decided I ought to take back what I’d said.

“Uh. Then I retract what I said earlier.”

“……?”

“I was walking along, got tired, and took a nap. And then, by coincidence, you happened to pass by. How’s that?”

Hyuk Mujin, who’d been looking at me as though my earlier praise had touched him a little, answered quickly.

“Sounds fine to me.”

“Right?”

“Yes. It’s convincing. Plenty of people sleep rough while traveling.”

“You know what you’re talking about. What can they do if it was an accident?”

“Exactly. Jiangsu isn’t their land.”

“Wait. Isn’t that true, though? Jiangsu or anywhere else, it all belongs to the Great Nation.”

“Huh. Does it work like that?”

“Doesn’t it? That’s what I understand.”

“Captain, since when do you know things like that?”

“You little shit.”

“Sorry. Anyway, I’ll remember that and ask Old Man Nam later…… Hey, where is everybody?”

Just as I was about to answer, the man spoke first.

“What is the meaning of this?”

“Oh, sorry. We got sidetracked for a second. Anyway, now that you mention it, Jiangsu belongs to you lot too, right?”

“All the mountains and rivers under heaven are ruled by His Imperial Majesty, whose authority is—no, why am I even answering this?”

“It’s nice to help each other out.”

“Enough!”

Our frantic conversation seemed to have rattled him.

I narrowed my eyes at the man, whose aura had grown as cold as frost.

“You there, Your Excellency from the Embroidered Uniform Guard. You said you were Commander Jeong, right? Why are you being so stiff about this? Frankly, neither of us stands to gain anything by fighting here.”

*Shing.*

A cold blade appeared in place of an answer. Commander Jeong drew the enormous saber from his back and spoke in a rigid voice.

“It makes no difference who you are. The Embroidered Uniform Guard obeys His Imperial Majesty. If you oppose his command and stand in our way, you will die.”

*Fwoooooosh.*

An invisible force spread out from him. I licked my dry lips as I felt his aura—pure and overwhelmingly heavy.

*Well, look at that……*

I’d suspected it from the moment I first saw him, but the man called Commander Jeong was a formidable master.

No—by ordinary standards, even “formidable” was an understatement. His skill was enough to shatter a prejudice I’d held deep inside.

*He hasn’t crossed the Supreme Peak threshold yet, but he’s at least at the very top of Peak.*

The authorities and Murim were always close and yet far apart.

Murim was one forest within the Great Nation’s borders, but it was full of beasts like dragons and tigers.

And yet, even among those serving the authorities, I’d rarely seen a proper master.

Common soldiers were Third Rate or Second Rate, while martial officers were First Rate at best. Peak masters were rare among those in the military.

*And most of them had been part of Murim before.*

The former Captain of the Guards to the City Lord of Sichuan Province had been a famous wandering martial artist, practically a personal bodyguard. Li Feng, Assistant Military Commissioner of Shanxi Province, was a former lay disciple of Huashan who’d joined the military after passing the military service examination.

But……

*Where’d a master of his caliber come from?*

My experience might not have been all that broad, but as a Supreme Peak master, I could get a rough measure of someone’s ability at a glance.

And Commander Jeong, as I saw him, bore not the slightest trace of a Murim martial artist. He was the very embodiment of a general, from head to toe.

*Even his internal energy is pure.*

What was more surprising was that the other Embroidered Uniform Guard members were no exception.

From young men who looked to be in their twenties to middle-aged men around forty. They varied in skill, but it wasn’t hard to tell that most of them were Peak masters.

*Dozens of Peak masters……*

Their strength matched that of a mid-sized sect—or more.

Whether they lived up to their reputation as the Son of Heaven’s hands and feet, or had been trained by someone other than the Son of Heaven, was a question for later.

I had no intention of letting this standoff continue when neither side stood to gain anything.

“You’ve got a nice aura, but you’d better put away those ugly weapons before someone gets hurt.”

The instant I stepped forward after warning them—

*Whoosh!*

A shaft of light shot straight at my face with a powerful crack of air. I caught it as gently as if I were cradling it, then sent it flying back in the direction it had come from.

*Thud! Boom!*

Instead of a final scream, a tremor rolled through the ground.

The archer, who’d leapt from the saddle of his fallen steed, stared at me in disbelief. An arrow was lodged in the center of the horse’s forehead.

“I told you to put away what you were holding.”

“……!”

“You’re the reason it died, you animal-abusing bastard.”

Hyuk Mujin, scratching his grime-covered body as if he’d known this was coming, said,

“Why is it his fault? You’re the one who killed it, Captain.”

“If we’re getting technical, sure. But Mujin.”

“Yes?”

“I can kill you too.”

“I’m sorry. I spoke out of turn.”

“Good. I’ll accept that.”

It was a peaceful conversation, as usual. But the tension in the courtyard was already so taut it felt ready to burst.

*Snort. Snort.*

Dozens of horses breathed heavily. The hands gripping their reins with all their strength had gone white, and the aura pouring from them wavered but didn’t subside.

At the head of them all stood Commander Jeong.

“You’re crossing a river that should never be crossed.”

“I haven’t crossed it yet, but that aside, you all seem pretty confident. No matter how good you are, you won’t have a good time fighting me.”

“What I and these men place our faith in is not our personal martial skill. It is our loyalty as officials who serve His Imperial Majesty’s command.”

“What’s your name?”

“Jeong Hogun.”

Commander Jeong—Jeong Hogun—had given me his name much more readily than I expected. Then he asked me in return,

“And yours?”

“Jin Taekyung.”

I wasn’t the one who gave that answer.

Jeong Hogun and I both turned our heads. Then we both dropped to one knee and bowed.

*Step.*

Beneath my lowered gaze, someone’s foot came into view—much larger than it had been in the last glimpse I remembered.

With it came a voice that had grown more mature, too. No longer the voice of a little child.

“It’s been a long time, Jin Taekyung of the Jin Family of Taiyuan.”

Prince Shangshan Zhu Bao.

The bloodline of a dragon, grown so much taller, helped me to my feet.

And before I could even answer, he handed me something he’d been holding.

*This is……*

A secret letter.

The moment that secretive word pierced my mind, Prince Shangshan leaned close to my ear and whispered,

“Please give me your autograph.”

“……”

No, Your Highness. What the fuck.
```
