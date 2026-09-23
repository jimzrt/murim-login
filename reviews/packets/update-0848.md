<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0848.txt",
      "sha256": "e78f36973455f7f7c91c61ef971262902842878952c2e0525ba217bd1b889299",
      "bytes": 14300
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b905991bc70e30148b6204b4f117534e62b060b77daaa7439c0bc275208c6781",
      "bytes": 3061
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "4457e8b40f7f008b9e72cc675f97dd2a5d576cdb2837cd3b5a882f70cd6820b7",
      "bytes": 227587
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "06a4f06dafe9c03557f1a20ff57200e6b53d6ec3f55d2b9db4684fbc6fdcb74f",
      "bytes": 1325
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "18a7562ccf0607796b806474fffee34e4719f9440f7a6eaa820c446b93a94434",
      "bytes": 759
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "904c8a8894eb57c6ad3174c610672332f84667774b4a7160556f766f3bd06f25",
      "bytes": 1355
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "4ddc93dc14de6555d8be6edfe3e7898a087f76d92b246d4cf0edee42d774a3d9",
      "bytes": 1573
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "5bc8d44113c78a10300f41b0f93cf674114da1b22b8672e5b9e1101c5116f313",
      "bytes": 1782
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "6e21328c7706e1e043b62bdce54ea08229d9a8c693b5e89835ba5d53aba282e5",
      "bytes": 622
    },
    {
      "path": "characters/Pill Physician.md",
      "sha256": "6f6815f6d71599b0cbe10baf820906eb9d8d35085611f4dba676a563d123b912",
      "bytes": 554
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "af6a6d127637cf0b016994c53eade6bf776c416283521215adb85d0173879a02",
      "bytes": 787
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ef87894d7e6e58370eefc26a6e542406cf849311afb057ed00381198bbe91265",
      "bytes": 252436
    }
  ],
  "estimated_tokens": 13151
}
-->

# Durable State Update — Chapter 848

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
1 and safe_through 848. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 848. Profile updates may replace only one
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
  "chapter": 848,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 848,
    "continuity_sources": [848],
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
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader.",
    "The supernatural Rift began at 10%; its progress increases the distribution and concentration of magical power.",
    "The System’s Status Window is inaccessible; Jin suspects an update may be responsible.",
    "Jin’s vision of a black-haired man killing Ahomed after the ritual remains unexplained; Jin believes the man was not Asmodeus.",
    "Jin’s [Broken Body] injury and damaged vital essence remain unresolved; the Divine Physician said full recovery is impossible but improvement is possible. Jin was unconscious after treatment.",
    "Jeok Cheongang and Jin Taekyung trust each other deeply; their Master-Disciple bond remains unformalized.",
    "The Sichuan Tang Clan and Sichuan Murim are rebuilding after Dark Heaven’s attack; allied martial artists remain to treat patients and guard against another attack.",
    "Dark Heaven developed experimental seeds over years of research and scattered some across the Central Plains; some have already blossomed.",
    "The Blood Lord ordered sorcerers to prepare selected seeds for later deployment and sent missives by hawk.",
    "The Lord of Heaven recently ordered the Blood Lord to bring down the heavens, then returned to sleep.",
    "The City Lord is suffering from lovesickness after the Son of Heaven took Aehyang; a subordinate has arrived with an urgent report, not yet delivered.",
    "The Divine Physician remains with his current patients and may visit the City Lord if they improve."
  ],
  "continuity_sources": [
    846,
    847
  ],
  "open_questions": [
    "Why did the Main Quest fail despite the Doppelganger’s erasure, and who or what was summoned?",
    "Was Jin’s vision of the summoned being real, System-delivered, or prophetic?",
    "What will happen as the Rift progresses and more beings enter the world?",
    "Who or what chose Jin, what is the Ark, and how did Dark Heaven reach Murim?",
    "What are Dark Heaven’s seeds meant to enhance, what caused the City Lord’s illness, and what is the urgent report about?"
  ],
  "safe_through": 847,
  "temporary_decisions": [
    "Keep magical power distinct from mana; keep Blink distinct from Teleport and Warp. Extended-range Blink causes severe strain.",
    "Keep Fire Storm and Aqua Storm as distinct named spells; render [영웅의 검] as “Hero’s Sword,” 에어 슬래시 as “Air Slash,” and 실드 마법 as “Shield magic.”",
    "Render 선택받은 자 as “the Chosen One,” 방주의 주인 as “the Master of the Ark,” [격변] as [Cataclysm], [어데 도씹니꺼] as “Where’s Your Do Clan From?,” and [종족 학살자] as “Species Slayer.”",
    "Render 균열 as a social fracture or division, not the supernatural Rift; render 醜王 as “Disgrace King” when used as Jin’s mocking imagined epithet for Jeok Cheongang.",
    "Render 천자 as “Son of Heaven,” 애향 as “Aehyang,” and 동방삭 as “Dongfang Shuo.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 살성     | **Slaughter Saint**           | —              |
| 열화문    | **Fire Gate Clan**               |
| 암천     | **Dark Heaven**                  |
| 사천당가   | **Sichuan Tang Clan**            |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 대주     | **Squad Leader** / **Commander**             |
| 제자     | **Disciple**                                 |
| 시스템              | **System**                     |
| 사천     | **Sichuan**            |
| 노부      | **this old man / I**                                            |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 환의 | **Pill Physician** | Title of the current Family Head of the Seongsu Jang Family. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 심력 | **mental strength** | Inner mental capacity injured by Jongni Chu's feint. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 소주천 | **Small Circulation** | Circulation of qi according to the Jin Family's Cultivation Technique. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 당가 | **Tang Family** | Short form for the Sichuan Tang Clan when distinguished from 사천당문. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 사천성 | **Sichuan Province** | Province form used in the title of its chief official. |
| 사천성주 | **City Lord of Sichuan Province** | Title held by Won Gyun. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 호법 | **stand guard** | Mungyeong offers to protect Jeok during cultivation. |
| 단환 | **pill** | A martial elixir in pill form; Mungyeong gives Taekyung a custom-made one. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 사천성주 | 진태경 | official_to_imperial_messenger | Messenger of His Highness Prince Shangshan | formal-deferential | The City Lord addresses Taekyung deferentially after seeing Prince Shangshan's Token. |
| 진태경 | 사천성주 | visitor_to_city_lord | City Lord | sarcastic-polite | Taekyung jokingly praises him as our City Lord after making him fund the reward. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 적천강 | 의원 | interrogator_to_physician | you; quack | blunt and threatening | Jeok shakes the physician and demands an explanation for Jin's seven-day sleep before ordering him to summon the Beast Miao King. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 844
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak martial master known as the Huashan Divine Dragon, the creator of the snake-inspired Mimi Step footwork technique, and the master of the Azure Dragon Pavilion within the Alliance Leader's Two Dragons Pavilion.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi, now a large horned snake, to him, and Cheongpung is accompanying Mungyeong while learning his martial arts through observation to become stronger and adapt to this world.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 847
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 842
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 847
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; they trust each other deeply but have never formalized their bond. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to the late Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and is a long-standing rival of Peng Cheolhu.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 847
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; they trust each other deeply, though their bond remains unformalized. Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master; Ju Hwaran is a trusted Fire Dragon Pavilion member; Magic Johnson and Chuck Hagel are allied to him; his mother and sister Hayeon are among those he protects; the Skeleton King is his friend and ally; Xiao Shen regards him as an older brother; Jin-ho is his older friend and trusted confidant; he once saved Ju Wongong’s life.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 847
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Pill Physician.md

# Pill Physician (환의)

- **Safe through:** Chapter 845
- **Aliases:** None
- **Role:** Current Family Head of the Seongsu Jang Family in Shandong, who personally placed and signed the Thousand-Year Snow Ginseng in the casket entrusted to the Yongbong Escort Bureau.
- **Personality:** No personality traits are established.
- **Voice:** No voice traits are established.
- **Relationships:** The Pill Physician heads the Seongsu Jang Family, a prestigious medical family in Shandong.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 842
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion; he helped Jin escape the underground prison by blocking the stairs and overpowering the Bai warriors.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃848화



간혹 그런 생각을 하곤 한다.

나는 도대체 얼마나 자주, 몇 번이나 기절하는 것일까.

만약 시스템창이 내 인생을 요약한다면, 정신을 잃은 채 흘려보낸 시간은 얼마나 될까.

젠장. 모르겠다.

다만 중요한 사실은 내가 지금 막 깨어났고, 웬 괴물같이 생긴 못생긴 놈과 눈이 마주쳤다는 것뿐이었다.

“엇, 시벌. 깜짝이야. 누구세요?”

괴물이 웅얼거리는 목소리로 대답했다.

“접니다.”

“접니요?”

처음 들어 보는 특이한 이름에, 꿈에서도 마주치기 싫은 얼굴.

나는 당혹스러워하며 되물었다.

“혹시 사천당가 분이신가?”

“…….”

“당접니?”

“조장님, 장난이 과하신데요.”

조장님. 괴물의 입에서 튀어나온 그 세 글자에 나도 모르게 입이 딱 벌어졌다.

적어도 지금 나를 저런 호칭으로 부르는 놈은 단 한 사람뿐이었으니까.

“무진이냐? 혁무진?”

“예.”

“세상에, 너 얼굴이 왜 그래?”

“누구한테 얻어맞아서요.”

원래 바쁘게 살아가다 보면 사소한 일은 잊기 마련이다.

그제야 며칠 전 혁무진을 먼지 나게 두들겨 팼던 기억을 떠올린 나는 따뜻한 미소를 머금었다.

“아하. 하마터면 못 알아볼 뻔했네. 너무 잘생겨져서.”

“……감사 인사라도 드려요?”

“주면 나도 고맙게 받지. 그런데 마지막으로 봤을 때는 이 정도로 얼굴이 좆…… 아니, 잘생기진 않았던 것 같은데.”

“웬 미친놈이 절 영원히 잠재우려고 했습니다. 속수무책이었어요.”

“미친놈? 누구?”

“인생의 최우선 목표가 배 터지도록 처먹는 것밖에 없는 놈이요.”

내가 아는 이들 중 그런 미친놈은 딱 두 명밖에 없다.

청풍. 그리고 태산.

물론 지금쯤 살성과 함께 천하 곳곳을 누비며 암천의 흔적을 찾고 있을 청풍이 뿅 하고 사천당가에 올 리는 없으니, 남아 있는 미친놈은 하나뿐이다.

“지금 제 얼굴 보이세요? 태산이 그 미친놈이 붓기도 가라앉기 전에 때려서 세 배로 부었어요.”

“세 배로 잘생겨진 건 알겠으니까, 우선 얼굴 좀 치워 봐. 아니면 일으켜 세워 주든가.”

“죄송한데 그건 안 됩니다. 이 이상으로 가까워지면 조장님 입 냄새까지 나잖아요. 가뜩이나 지금 여기에서 버티는 것도 힘든데.”

“뭐?”

처음에는 무슨 소린가 했다.

그 말을 들은 순간, 콧속을 파고드는 끔찍한 악취를 인지하기 전까지는.

“으읍.”

나는 올라오려는 헛구역질을 간신히 참으며 몸을 일으켰다.

그럴 줄 알았다는 듯이 고개를 끄덕인 혁무진이 손에 들고 있던 물주머니와 천 쪼가리를 건넸다.

“냄새 장난 아니죠? 우선 저처럼 이걸로라도 코 막고, 물로 입 헹구세요. 그리고 가급적 말씀하실 때는 입을 가리…….”

“지금보다 더 잘생겨지기 싫으면 입 좀 다물어라. 속 울렁거려서 죽겠으니까.”

“죄송합니다. 그런데 진짜 지금 조장님 입 냄새 장난 아니에요. 도대체 뭘 드신 겁니까?”

“똥.”

“세상에, 그런 걸 왜 드셨어요?”

“…….”

혁무진 저 새끼는 정말 이걸 곧이곧대로 믿는 걸까. 아니면 날 조금이라도 엿 먹이고 싶어서 저러는 걸까.

잠시 고민하던 나는 한숨을 푹 내쉬었다. 혁무진이 건네준 천 쪼가리로 콧구멍을 단단히 틀어막고, 입 안을 몇 번이나 헹구고 나니 그제야 좀 숨통이 트이는 기분이었다.

‘그나저나, 정확히 무슨 일이 있었던 거지?’

적천강에 의해 그 끔찍한 단환을 강제로 삼켰던 것이 마지막 기억이다.

아니, 정확히는 정신을 잃기 직전 몸 안으로 스며드는 열기를 느끼긴 했었다.

마치 고향에 돌아온 것처럼 더없이 익숙한.

그렇기에 뜨겁다기보다는 따스하게만 느껴졌던 열기를.

‘노야의 열양지기(熱陽之氣)였어. 분명히.’

세상에 존재하는 모든 색이 일곱 빛깔 무지개가 아니듯, 기운이라는 것도 비슷한 맥락이다.

열양지기를 이용하는 문파가 천하에 몇 개나 되는지는 모르지만, 열화문(熱火門)이라는 뿌리는 달라지지 않는 법.

내가 느꼈던 그 기운은 틀림없이 적천강의 것이었다.

‘그렇다는 건…….’

나는 천천히 주위를 둘러보았다.

처음 들어왔을 때와 같이 말끔하게 정리된 내부. 그러나 공기 중에 스며든 악취와 바닥에 남은 거무스름한 자국은 여전했다.

“저거 닦는 데 엄청 힘들었습니다. 끈적거리고 냄새나서 죽는 줄 알았다고요.”

내 시선을 알아차린 듯, 눈치 빠르게 입을 연 혁무진이 볼멘소리를 늘어놓았다.

“신의께서 남기신 말씀에 의하면 몸 안의 노폐물이 점액 형태로 흘러나온 거라던데, 그. 정확히 뭐라 하셨더라. 아는 거였는데 갑자기 기억이 안 나네요. 추. 추…….”

“추궁과혈(推宮過穴).”

툭 던진 한마디에, 혁무진이 고개를 끄덕였다.

“아, 맞습니다. 말로만 듣던 그 추궁과혈이요.”

말로만 들을 수밖에 없다. 추궁과혈은 상당한 준비와 희생을 각오해야 하는 일이었고, 그만큼 쉽게 시도하지 않으니까.

설령 초절정의 경지에 오른 고수라 해도 예외는 아니었다.

극심한 심력(心力)을 소모하는 것은 물론이고, 자신의 공력 일부를 상대의 신체 안에 고루 흡수시켜야 하는 것이 추궁과혈이었다.

‘그마저도 실패하면 타격이 극심하지.’

하지만 적천강은 내가 정신을 잃은 사이에 추궁과혈을 실시했다. 상당한 위험과 공력 손실을 감수하면서까지.

물론 그에게 추궁과혈을 받은 것이 이번이 처음은 아니지만, 나로서는 감사와 미안함을 느낄 수밖에 없었다.

‘……이렇게까지 하지 않으셔도 되는데.’

사경(死境)을 넘나드는 상황이었다면 내가 먼저 부탁했을 수도 있겠으나, 지금까지는 그럭저럭 아무렇지 않게 버텨 왔다.

더군다나 지금은 당장 무슨 일이 벌어질지 모르는 상황.

모두를 위해서라면 열화신룡 진태경이 아닌, 화왕 적천강의 전력을 조금이라도 더 보존하는 것이 옳았다.

‘물론 노야 앞에서 이런 말을 했다가는 혼쭐이 나겠지.’

작게 실소를 흘린 나는 열양지기를 끌어올렸다. 눈에 띌 만큼은 아니어도 확실히 증가한 공력이 대번에 느껴졌다.

‘천천히. 신중하게.’

마치 용암을 흘려보내듯, 삼 갑자를 약간 웃돌게 된 열양지기를 전신 사지 백해로 퍼트렸다. 동시에 몸 깊숙한 곳에 존재하는 모든 것을 조용히 관조(觀照)했다.

더 넓고 튼튼해진 혈도. 노폐물의 배출로 맑아진 핏물과 정상적으로 움직이는 장기들까지.

흐읍.

나는 길게 숨을 삼키며 열양지기를 더욱 빠르게 흘려보냈다.

천천히 흐르던 용암이 들판을 휩쓰는 불길이 되기까지는 그리 오랜 시간이 걸리지 않았다.

스아아아아.

한 바퀴, 두 바퀴, 세 바퀴.

소주천(小周天)으로 시작했던 운기조식은 대주천(大周天)이 되었고, 수백 개의 크고 작은 혈도를 휩쓸며 다시 한번 신체 내부를 정리한 화룡은 마침내 하단전으로 돌아와 똬리를 틀었다.

그리고 모든 것이 완벽해 보였던 그 순간.

욱신.

불현듯 하단전을 엄습한 통증에, 운기조식을 끝마친 나는 씁쓸하게 입맛을 다셨다.

‘역시, 이 정도로는 부족한가.’

신의가 제조한 그 끔찍한 단환의 약효도, 적천강의 추궁과혈도 현재의 내게는 최선의 치료였을 것이다.

하지만 그런 그들의 노력에도 끝내 완치(完治)까지 이르지는 못했다.

신체가 감당할 수 없는 힘을 남발한 대가는 쓰디썼고, 아무리 아쉬워해 봐도 냉정한 현실은 변하지 않았다.

감당할 수 없는 양의 물을 받아낸 그릇의 운명은 둘 중 하나다.

가능한 만큼만 담아내거나, 쏟아지는 물의 무게를 이기지 못해 깨져 나가거나.

지금 내가 처한 상황은 후자였다.

“……아직까지는 금이 간 정도지만.”

나도 모르게 흘러나온 혼잣말에, 자연스럽게 호법을 서고 있던 혁무진이 반문했다.

“예? 뭐가요?”

“넌 몰라도 돼. 그냥 그런 게 있어.”

“와, 너무하시네. 저처럼 충성스러운 오른팔이 어디 있다고.”

“누누이 말하지만, 넌 끽해야 새끼발가락이야.”

“지금 생각해 보니까 그것도 나쁘지 않네요.”

“뭐?”

“새끼발가락이요. 문지방에 찧으면 제일 아픈 부위 아닙니까.”

“…….”

저 자식이 점점 강적이 되어가는 건 단순한 기분 탓일까.

잠시 말문이 막힌 나는 이내 고개를 절레절레 내저으며 입을 열었다.

“헛소리는 집어치우고, 먼저 가서 물이나 받아 놔. 찝찝해서 씻어야겠다.”

“어, 지금요?”

“그래, 냄새나서 못 살겠다.”

옷깃에 짙게 밴 악취를 맡으며 이마를 찡그린 그때, 혁무진이 뒤통수를 긁적이며 말했다.

“저기, 조장님. 그건 좀 곤란할 것 같은데요.”

“뭐라고?”

눈을 깜빡인 내가 진지한 목소리로 물었다.

“너 지금 반항하니? 고금 제일 미남이 되고 싶어서 얼굴이 근질거려?”

“그만 때리십쇼. 제발.”

“그럼 왜 헛소리야?”

“반항이 아니라, 시간상 곤란할 것 같다고요. 이미 다들 준비 끝마치고 조장님 깨어나시는 것만 기다리고 있었는데.”

“……준비? 내가 깨어나는 것만 기다려?”

“예. 냄새야 저희가 어떻게든 참아 볼 테니까, 그냥 바로 출발하시죠.”

이건 또 무슨 개소리야.

순간 어안이 벙벙해진 내게, 황급히 품 안을 뒤적거린 혁무진이 누런 종이를 꺼내 내밀었다.

“이게 뭐…….”

“신의 어르신과 적 대협께서 떠나시기 전에 남긴 서신입니다. 저희더러 미리 준비하고 있다가, 조장님 깨어나시면 늦지 않게 모셔 오라고 하셨어요.”

먼저 떠난 적천강과 신의. 그리고 그들이 남긴 서신.

도무지 해소되지 않는 의문을 느끼며 까슬까슬한 촉감의 누런 종이를 펼친 그 순간.

아마도 신의의 것이 분명할, 용사 비등한 필체로 적어 내린 한 줄의 글귀가 눈동자에 틀어박혔다.



사천성주(四川城主). 졸(卒).



“……!”



* * *



신의는 문득 떠올렸다.

무시무시한 살업(殺業)을 쌓은 동시에, 수많은 이들을 죽음의 구렁텅이에서 건져 올린 스승에게서 들었던 가르침을.



‘너는 이 세상에서 가장 무서운 병이 무엇이라 생각하느냐.’

‘적(積, 암)이 아닐까 싶습니다.’

‘어찌하여 그리 생각하느냐.’

‘육안으로 살필 수 없을 만큼 작은 종양이 몸속 깊숙한 곳에서 자라납니다. 초기에 징후를 알아차린다면 그나마 다행이지만, 손꼽히는 명의가 아닌 이상 제대로 된 치료도 못 해 보고 죽는 경우가 다반사지요.’

‘네 말도 옳다. 그러나 시기와 의원을 잘 만난다면, 하늘의 도움이 없어도 능히 치유할 수 있는 병이다.’

‘그건 스승님께서 신의(神醫)이시며, 종사(宗師)의 반열에 오르실 만큼 무공의 고수이시기 때문 아닙니까?’

‘그렇지 않다. 노부가 인정할 만큼 경지에 오른 의원이라면 충분히 해낼 수 있는 일이다. 물론 널 포함해서.’

‘과찬이십니다만, 이 제자는 아직도 스승님께서 원하시는 답을 잘 모르겠습니다.’

‘패이고 갈라진 살은 꿰매면 되는 것이요, 뒤틀리고 부러진 뼈는 붙이면 그만이다. 설령 장기가 다쳤다 해도 개복(開腹)하여 알아볼 수 있다.’

‘아, 이제 알겠습니다.’

‘무엇이냐?’

‘마음의 병입니다.’

‘맞다. 마음의 병은 보이지도 않고 꿰매거나 붙일 수도 없다. 살수보다 은밀하며 마두보다 잔인하게 환자를 죽인다.’

‘하면 그런 이들은 어찌해야 치료할 수 있겠습니까?’

‘첫째로는 의원과 환자가 아닌 사람으로 마주해라. 둘째로는 말없이 귀 기울이며, 셋째로는 친구가 되어라.’

‘만약 그렇게도 치료가 되지 않고 환자가 스스로 죽음을 택한다면…….’

‘정성을 다해 염(鹽)해 주고, 떠나는 길을 지켜보아라. 하지만 네가 그 어떤 환자를 대하건, 늘 한 가지만 명심하거라.’

‘무엇입니까?’

‘원인이 없는 죽음은 없다. 그 원인부터 파악하거라.’

‘……!’



과거의 상념에서 깨어난 신의는 감았던 눈을 떴다.

넓고 화려한 침상 위, 마치 깊은 잠에 빠진 것처럼 쓰러져 있는 시신 한 구가 보였다.

‘사천성주. 그대는 무슨 연유로 죽었소.’

사랑하는 애첩을 빼앗긴 비통함인가. 아니면 빼앗길 수밖에 없던 자신에 대한 분노인가.

그것조차 아니면…….

‘처음부터 상사병 따위가 아닌, 또 다른 무언가 때문인가.’

신의는 고요한 눈빛으로 사천성주의 시신을 내려다보았다.

사천성 내에서 이름난 명의는 이미 저 신분 높은 사내의 사인(死因)을 급사라 확신했지만, 장장 세 시진이 넘는 시간 동안 시신을 살핀 신의는 그 생각에 동의하지 않았다.

‘도대체, 어떤 원한을 산 거요.’

푹.

망자에게 닿지 않을 물음과 함께, 혈에서 뽑혀 나온 대침(大鍼).

그리고 그 날카로운 끝에 꿰어 꿈틀거리는 작은 무언가를 바라보며 중얼거렸다.

“……고독(蠱毒).”
```

## Final English reading copy

```markdown
# Chapter 848

Every now and then, I find myself wondering.

Just how often do I pass out? How many times?

If the System window summarized my life, how much of it would be time I’d lost while unconscious?

Damn it. I have no idea.

The important thing was that I’d just woken up—and found myself face-to-face with some ugly creature that looked like a monster.

“Whoa, shit! You scared me. Who are you?”

The monster answered in a mumbling voice.

“It’s me.”

“Me who?”

An unusual name I’d never heard before, attached to a face I wouldn’t want to see even in my dreams.

I asked again, baffled.

“Are you from the Sichuan Tang Clan, by any chance?”

“……”

“Is your name Tang Me?”

“Captain, that joke’s a bit much.”

Captain. The three syllables that came out of the monster’s mouth left me staring with my jaw hanging open.

There was only one person who called me that these days.

“Mujin? Hyuk Mujin?”

“Yes.”

“Good heavens, what happened to your face?”

“Someone beat me up.”

When you’re busy with life, it’s easy to forget the little things.

Only then did I remember pummeling Hyuk Mujin into the dirt a few days ago. I smiled warmly.

“Ah, I almost didn’t recognize you. You got so handsome.”

“Should I thank you?”

“If you do, I’ll gladly accept. But your face wasn’t this fu—this handsome when I last saw you.”

“Some lunatic tried to put me to sleep forever. I couldn’t do a thing.”

“A lunatic? Who?”

“Some guy whose only goal in life is to stuff himself until he bursts.”

Of the people I knew, only two lunatics came to mind.

Cheongpung. And Taishan.

Of course, Cheongpung was probably traveling all over the land with the Slaughter Saint, searching for traces of Dark Heaven. There was no way he’d just pop up at the Sichuan Tang Clan.

That left one lunatic.

“Can you see my face right now? That lunatic Taishan hit me before the swelling had even gone down. It got three times worse.”

“I get it, you’re three times more handsome. Now get your face out of mine. Or help me sit up.”

“Sorry, but I can’t. If I get any closer, I’ll smell your breath. It’s hard enough just standing here as it is.”

“What?”

At first, I didn’t understand what he meant.

Not until I noticed the terrible stench seeping into my nostrils.

“Ugh.”

I barely held back a gag and pushed myself upright.

As if he’d expected that, Hyuk Mujin nodded and handed me a waterskin and a scrap of cloth.

“It really stinks, doesn’t it? Plug your nose with this, like I did, and rinse your mouth out. And try to cover your mouth when you talk, if you can…”

“If you don’t want to get even more handsome, shut up. My stomach’s already turning.”

“Sorry. But your breath really is awful, Captain. What on earth did you eat?”

“Shit.”

“Good heavens, why would you eat that?”

“……”

Was that idiot Hyuk Mujin actually taking me seriously? Or was he just trying to mess with me even a little?

After a moment’s thought, I let out a deep sigh. I stuffed the scrap of cloth he’d given me up my nostrils and rinsed my mouth out several times. Only then did it feel like I could breathe again.

*Anyway, what exactly happened?*

My last memory was Jeok Cheongang forcing me to swallow that awful pill.

No—if I’m being precise, I’d felt a warmth seep through my body just before I lost consciousness.

A warmth more familiar than anything, as if I’d returned home.

That was why it felt warm rather than hot.

*It was Old Master’s Scorching Yang Qi. I’m sure of it.*

Just as not every color in the world is one of the seven colors of the rainbow, energy follows a similar principle.

I didn’t know how many clans in the world used Scorching Yang Qi, but its roots in the Fire Gate Clan were unmistakable.

The energy I’d felt had unquestionably belonged to Jeok Cheongang.

*Which means…*

I slowly looked around.

The place was as clean and tidy as when I’d first arrived. But the stench lingering in the air and the dark smudges on the floor were still there.

“It took ages to clean that up. It was sticky and smelled so bad I thought I was going to die.”

Hyuk Mujin, quick to catch my gaze, complained.

“According to what the Divine Physician left behind, it was the impurities in your body coming out in a mucus-like form. Um. What exactly did he call it? I knew the word, but it just slipped my mind. Push… push…”

“Pushing the meridians and passing through the acupoints.”

At my offhand reply, Hyuk Mujin nodded.

“Oh, right. That thing I’d only ever heard about.”

He could only have heard about it. Pushing the meridians and passing through the acupoints required extensive preparation and a willingness to make sacrifices. It wasn’t something people attempted lightly.

Not even masters who’d reached Supreme Peak were exceptions.

It took a tremendous amount of mental strength, and the practitioner had to infuse part of their own internal energy evenly throughout the other person’s body.

*And if it failed, the damage was severe.*

But Jeok Cheongang had performed the treatment while I was unconscious, accepting all that risk and the loss of internal energy.

It wasn’t the first time he’d treated me that way, but I couldn’t help feeling grateful—and guilty.

*…He didn’t have to go this far.*

If I’d been hovering between life and death, I might have asked him to. But until now, I’d been getting by just fine.

And we were in a situation where anything could happen at any moment. For everyone’s sake, it was better to preserve even a little more of the Fire King Jeok Cheongang’s strength than the Blazing Flame Divine Dragon Jin Taekyung’s.

*Of course, if I said that in front of Old Master, he’d tear into me.*

I let out a quiet laugh and drew up the Scorching Yang Qi. The increase in my internal energy wasn’t visible, but I could feel it at once.

*Slowly. Carefully.*

Like flowing lava, I spread the Scorching Yang Qi—now a little over three jiazi—through my limbs and every acupoint in my body. At the same time, I quietly surveyed everything deep within me.

My meridians were wider and sturdier. My blood had cleared now that the impurities were gone, and my organs were working normally.

I drew in a long breath and sent the Scorching Yang Qi flowing faster.

It didn’t take long for the slow-moving lava to become a blaze sweeping across a plain.

Sssshhhh.

Once around. Twice. Three times.

The cultivation that had begun as a Small Circulation became a Great Circulation. The fire dragon swept through hundreds of major and minor acupoints, putting my insides in order once more, then finally returned to my lower dantian and coiled up.

And just when everything seemed perfect—

Throb.

A sudden pain struck my lower dantian. I finished circulating my qi and clicked my tongue bitterly.

*So this still isn’t enough.*

The effects of that horrible pill the Divine Physician had made and Jeok Cheongang’s treatment must have been the best they could do for me right now.

But even with all their efforts, they hadn’t been able to heal me completely.

The price for using power my body couldn’t handle was bitter. No matter how much I regretted it, the cold reality wouldn’t change.

A vessel faced with more water than it could hold had only two choices.

Hold as much as it could, or break under the weight of the water pouring in.

I was in the latter situation.

“…It’s only a crack for now, though.”

At my involuntary mutter, Hyuk Mujin, who’d been standing guard, asked,

“Huh? What is?”

“You don’t need to know. It’s just something.”

“Wow, that’s cold. Where are you going to find a right-hand man as loyal as me?”

“As I’ve told you time and again, you’re barely my pinky toe.”

“Now that I think about it, that’s not so bad.”

“What?”

“Your pinky toe. It hurts the most when you stub it on a doorframe.”

“……”

Was it just me, or was that guy becoming a formidable opponent?

I was briefly at a loss for words. Then I shook my head and spoke.

“Cut the nonsense. Go fetch some water. I need to wash up. I feel disgusting.”

“Now?”

“Yeah. I can’t stand this smell.”

I wrinkled my brow at the stench clinging to my clothes. Hyuk Mujin scratched the back of his head.

“Um, Captain. That might be a little difficult.”

“What did you say?”

I blinked and asked in a serious voice,

“Are you talking back to me? Is your face itching because you want to be the most handsome man of all time?”

“Please stop hitting me. I’m begging you.”

“Then why are you talking nonsense?”

“I’m not talking back. I mean it’s going to be difficult time-wise. Everyone’s already prepared and waiting for you to wake up.”

“…Prepared? Waiting for me to wake up?”

“Yes. We’ll put up with the smell somehow, so let’s just leave now.”

What the hell was he talking about?

As I stared at him, bewildered, Hyuk Mujin hurriedly rummaged through his robes and pulled out a yellowed sheet of paper.

“What’s that…?”

“It’s a letter Sir Jeok and the Divine Physician left before they departed. They told us to get everything ready and bring you as soon as you woke up, without wasting any time.”

Jeok Cheongang and the Divine Physician had left ahead of us. They’d left a letter behind.

Trying to make sense of the questions that still wouldn’t go away, I unfolded the rough-textured yellow paper. At that moment, a single line written in a strikingly vigorous hand—presumably the Divine Physician’s—seared itself into my eyes.

> City Lord of Sichuan Province. Deceased.

“……!”

* * *

The Divine Physician suddenly remembered a lesson his Master had once taught him.

His Master had amassed a fearsome tally of killings—and rescued countless people from the brink of death.

*“What do you think is the most frightening illness in the world?”*

*“Cancer, I think.”*

*“Why do you think so?”*

*“Tumors too small to see with the naked eye grow deep inside the body. It’s fortunate if you notice the signs early, but unless you can find one of the most renowned physicians, people often die without ever receiving proper treatment.”*

*“You’re not wrong. But if you find a good physician at the right time, it’s an illness you can overcome without needing help from Heaven.”*

*“Isn’t that because you’re the Divine Physician, and a master of martial arts who’s reached the rank of Grandmaster?”*

*“No. Any physician whose skill I would recognize could do it. You included.”*

*“You flatter me, Master. But I still don’t know what answer you’re looking for.”*

*“Flesh that’s been gouged or torn can be stitched together. Twisted or broken bones can be set. Even if an organ is injured, you can open the body and examine it.”*

*“Ah, I understand now.”*

*“What is it?”*

*“An illness of the mind.”*

*“That’s right. A sickness of the mind can’t be seen, stitched up, or set. It kills patients more stealthily than an assassin and more cruelly than a fiend.”*

*“Then how should we treat people like that?”*

*“First, meet them as one person to another, not as physician and patient. Second, listen without a word. Third, become their friend.”*

*“And if even that doesn’t help, and the patient chooses to die…”*

*“Carefully prepare their body for burial, and see them off on their final journey. But whoever the patient may be, always remember one thing.”*

*“What is it?”*

*“There’s no such thing as a death without a cause. Find the cause first.”*

*“……!”*

The Divine Physician came back to himself and opened his eyes.

On the broad, lavish bed lay a corpse, sprawled as if in a deep sleep.

*City Lord of Sichuan Province. What caused your death?*

Was it the grief of having his beloved concubine taken from him? Or anger at himself for being powerless to stop it?

Or perhaps…

*Was it never lovesickness at all, but something else?*

The Divine Physician gazed down at the City Lord’s corpse, his eyes calm.

A renowned physician from Sichuan had already concluded that the high-ranking man had died suddenly. But after examining the body for more than three shichen, the Divine Physician disagreed.

*What grudge did you incur?*

Puk.

Along with a question that would never reach the dead man, a long needle was drawn from an acupoint.

The Divine Physician stared at the tiny thing writhing on its sharp tip and murmured,

“…A gu poison.”
```
