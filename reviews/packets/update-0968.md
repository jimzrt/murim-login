<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0968.txt",
      "sha256": "6bb05e27fc772b8152741aedb776d2f58aa88227cdac4c6b89b9547474a2f813",
      "bytes": 17756
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "e779fd0269ddcbf7f28da8ad0b69249fda3d393f2a34f7aa56e6f8a627192bf0",
      "bytes": 2275
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b40e329f8ccc2725c247f21e7d735563c277525366768cd3625d9f3f4a508cda",
      "bytes": 235410
    },
    {
      "path": "characters/Chinggen.md",
      "sha256": "8f919e66cd1147275f06ade7d64201718d1aeb4d5a2c15d5ceb8e8f8e26a5e27",
      "bytes": 709
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "3e51c57d2efe0a12981b1f97849f75e2b76706d97558c39a8b656ca14acd72cf",
      "bytes": 759
    },
    {
      "path": "characters/Jamukha.md",
      "sha256": "0a40844f9a57e3d05cf801897ffc3ee9de3a8dba5ca0e5df0b385f0ce02252c5",
      "bytes": 566
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "e91fbfd6a46eba6d5d0eaccde90969d13a0e8d3552a4d5ff690b79619352791d",
      "bytes": 1204
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "7a0f1b5c7072076cca021b0b2ef4c8ddb82edcfe6670a3de3165f4554590f178",
      "bytes": 1481
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "040b72df7ff20631cddb4edb8fd32d6c36e861b389118931956900864012e05f",
      "bytes": 622
    },
    {
      "path": "characters/Peng Cheolhu.md",
      "sha256": "c8a66a946f945d9ed10e26708705528a77a7094e63a492ff6ca8ef99335f24a7",
      "bytes": 801
    },
    {
      "path": "characters/Pung Yang.md",
      "sha256": "ac65db7cc534c9f59966b804863546ba5ff65a32d1581c3679ff4f0abe1b8caf",
      "bytes": 1446
    },
    {
      "path": "characters/Temur.md",
      "sha256": "ee1e1a436e9d1e6c589d4894e1f132200e4f5292385fc4db4348dd590799ce4f",
      "bytes": 676
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "9dc188d4f1880094efb69f4bfef10ff8f765c15d7759e1169a87966f5df06849",
      "bytes": 269536
    }
  ],
  "estimated_tokens": 14965
}
-->

# Durable State Update — Chapter 968

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
1 and safe_through 968. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 968. Profile updates may replace only one
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
  "chapter": 968,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 968,
    "continuity_sources": [968],
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
    "Mukyung is alive but grievously internally injured; he has risen again near the battle at the gorge’s center.",
    "Peng Cheolhu and Jamukha continue their duel in the gorge; both are wounded, Jamukha’s crescent saber is shattered, and Jamukha has a grievous shoulder wound and internal injuries.",
    "Jamukha is the former eastern-steppe chieftain defeated by Peng Cheolhu more than fifty years ago; he rebuilt his power in the western steppe and waited for the Hebei Peng Family to appear so he could seek revenge.",
    "Peng Cheolhu continued training every day after the Great Faction War to surpass Jeok Cheongang.",
    "Wikyung leads Shanxi fighters toward the gorge’s center, believing their current momentum is temporary.",
    "The Hebei Peng Family fights the steppe army in the basin while outnumbered by more than ten to one; Cheolhu has gone to the gorge with some of its elite.",
    "Jamukha ordered his Keshik centurions not to use an unnamed weapon without his permission because more battles lie ahead.",
    "An unidentified force has appeared beyond the basin and fired thousands of arrows.",
    "The Emperor remains gravely ill with Blood Soul Gu; the treatment requiring him to die once remains unresolved.",
    "The improved Temporary Strength Pill’s source and effects remain unknown; Jang Sam remains unconscious.",
    "The Martial God’s identity and connection to the chosen one and the Bow Saint remain unknown.",
    "The Eastern Heaven Demon Lord’s papers and silk pouch remain unexplained."
  ],
  "continuity_sources": [
    966,
    967
  ],
  "open_questions": [
    "What will the unidentified force’s arrows do to the battle?",
    "What is the unnamed weapon the Keshik centurions were ordered not to use?",
    "How will the duel between Jamukha and Cheolhu, and the fighting in the gorge, unfold?",
    "Who gave Jang Sam the silk pouch, and what are the improved pill’s effects and distribution?",
    "What is the Martial God’s identity and connection to the chosen one and the Bow Saint?"
  ],
  "safe_through": 967,
  "temporary_decisions": [
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 팽철후    | **Peng Cheolhu**   |
| 남궁천    | **Nangong Cheon**  |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 벽력도왕   | **Thunderbolt Saber King**    | Peng Cheolhu   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 소림     | **Shaolin**                      |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 하북팽가   | **Hebei Peng Family**            |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 내공     | **internal energy**                              |                                                       |
| 살기     | **killing intent**                               |                                                       |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 중원     | **Central Plains**                               |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 가주     | **Family Head**                              |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 안휘     | **Anhui**              |
| 정마대전   | **Great Faction War**         |
| 귀가      | **your family**                                                 |
| 공자      | **Young Master**                                                |
| 칭겐 | **Chinggen** | Northern Gaoyuan chieftain commanding one hundred tribespeople; restrains Temur. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 자무카 | **Jamukha** | Khan of the western grasslands and the steppe army’s practical leader. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 테무르 | **Temur** | Northern Gaoyuan chieftain commanding one hundred tribespeople; claims descent from the khans. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 대초원 | **Great Steppe** | The steppe region from which Temur and Chinggen come. |
| 허공섭물 | **Seizing an Object Through Empty Space** | Technique Jeok Cheongang uses to lift Jang Taebo remotely. |
| 태상가주 | **Grand Family Head** | Title held by the Azure Sky Sword King as head of the Nangong Family. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 성라대연 | **Star-Array Grand Banquet** | Major martial gathering held in Henan every two or three years. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남궁 | **Namgung** | Surname of the family led by Namgung Ryong. |
| 잠룡 | **Hidden Dragon** | Epithet or metaphor for Jin Taekyung. |
| 검왕 | **Sword King** | Short form for the Azure Sky Sword King, Nangong Cheon. |
| 운남 | **Yunnan** | Region from which Jongni Chu comes. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 전광석화 | **Quick Attack** | Warlordmon’s rapid-movement command; used as a Pokémon-style gag. |
| 전광 | **Quick Attack** | Shortened form of Warlordmon’s rapid-movement command. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 소하 | **Xiao He** | Historical civil official invoked in the same exchange. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 장성 | **Great Wall** | Wall used in the discussion of the Outer Lands. |
| 모용세가 | **Murong Family** | One of the Five Great Families, based in Liaoning. |
| 단환 | **pill** | A martial elixir in pill form; Mungyeong gives Taekyung a custom-made one. |
| 사냥개 | **hunting dog** | Jin's demeaning metaphor for Ares personnel who obey Go Jun. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 심해 | **deep sea** | Unexplored ocean depths where the ancient monster awakens. |
| 육부 | **Six Ministries** | The central government ministries. |
| 중양절 | **Double Ninth Festival** | Festival used as the expected date for the invasion of the Central Plains. |
| 텡그리 | **Tengri** | Deity invoked by the steppe people. |
| 케식 | **Keshik** | Elite warriors serving the Golden Clan. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 마적 | 풍양 | mounted-bandit subordinate to bandit leader | Leader | deferential | Uses 단주 when reporting to Pung Yang. |
| 진태경 | 풍양 | enemy_to_enemy | you pill-popping bastard | insulting-casual | Taekyung openly insults Pung Yang while announcing that he will use a pill too. |
| 풍양 | 진태경 | enemy_to_enemy | little brat; wet-behind-the-ears fledgling | condescending and taunting | Pung Yang dismisses Taekyung as an inexperienced child while challenging his ability to intervene. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 테무르 | 칭겐 | fellow_chieftain | Chinggen | familiar and argumentative | Temur addresses his fellow chieftain by name while defending their khan lineage. |
| 칭겐 | 테무르 | fellow_chieftain | Temur | familiar and cautioning | Chinggen uses Temur's name while warning him not to act rashly. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 진태경 | 남궁천 | junior martial artist to legendary martial master | Great Hero Nangong Cheon | formal-deferential | Taekyung uses the title and honorific 대협 when formally greeting the Azure Sky Sword King. |
| 남궁천 | 진태경 | legendary martial master to audacious junior | you / brat | blunt and intimidating | Namgung Cheon uses 네 녀석 and 놈 while testing and threatening Taekyung. |
| 적천강 | 벽력도왕 | rival_martial_master_to_rival_martial_master | Virility Saber King | insulting and taunting | Jeok coins 정력도왕 as a taunting replacement for the established title. |
| 벽력도왕 | 적천강 | rival_martial_master_to_rival_martial_master | Jeok Cheongang | boisterous and hostile-teasing | The Thunderbolt Saber King calls Jeok by name before their argument escalates. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 가솔 | 진태경 | Zhuge Clan retainer to Great Hero | Great Hero Jin | polite and pleading | Uses 진 대협 while urging Taekyung to stop provoking Ju Wongong. |
| 벽력도왕 | 진태경 | elder martial master to younger rival | you | boisterous and confrontational | Peng addresses Taekyung as 네놈 while discussing Peng Dojin. |
| 진태경 | 부족장 | captor to captured tribal chieftain | tribal chieftain | casual, coercive, and mocking | Jin promises to spare the captured chieftain if he answers questions properly. |
| 부족장 | 진태경 | captured tribal chieftain to overpowering enemy | Jin Taekyung | alarmed and desperate | The chieftain recognizes Jin by name while fleeing and then begs for his life. |
| 칭겐 | 자무카 | fellow_khan_to_elder_khan | Khan Jamukha | formal-respectful | The impostor wearing Chinggen’s face addresses Jamukha with deference. |
| 테무르 | 자무카 | fellow_khan_to_elder_khan | Khan Jamukha | formal-respectful | Temur affirms Chinggen’s public praise of Jamukha. |
| 자무카 | 팽철후 | former battlefield opponents and current rivals | Thunderbolt Saber King Peng Cheolhu | informal and hostile | Jamukha first uses Cheolhu’s former title, then corrects himself to the current title. |

## Listed compact profiles

### Chinggen.md

# Chinggen (칭겐)

- **Safe through:** Chapter 962
- **Aliases:** None
- **Role:** The real Chinggen, a Khan of the eastern grasslands and Temur’s sworn brother, is dead; the impostor who wore his face has revealed himself as the Demon Bird, an elderly and overwhelmingly powerful martial artist.
- **Personality:** Prudent, restrained, and attentive to the danger posed by the gathering's other powers
- **Voice:** Measured, familiar, and cautioning
- **Relationships:** Temur was Chinggen’s cousin and sworn brother through the anda oath; the impostor who killed Chinggen and wore his face spared Temur to control the western tribes.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 967
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jamukha.md

# Jamukha (자무카)

- **Safe through:** Chapter 967
- **Aliases:** None
- **Role:** Jamukha is the ruler of the western steppe and a former eastern-steppe chieftain who leads a powerful steppe army.
- **Personality:** Patient and driven by a long-standing desire to avenge his defeat by Peng Cheolhu.
- **Voice:** Not established
- **Relationships:** Peng Cheolhu defeated him more than fifty years ago, and Jamukha rebuilt his power while waiting for a chance to confront the Hebei Peng Family.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 967
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and says they have shared everything since he accepted him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 960
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor has appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and learning to trust his allies rather than carry every burden alone.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 960
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Peng Cheolhu.md

# Peng Cheolhu (벽력도왕)

- **Safe through:** Chapter 967
- **Aliases:** Thunderbolt Saber King
- **Role:** Peng Cheolhu is the Thunderbolt Saber King, a Ten Kings master and Great Hero of the Hebei Peng Family.
- **Personality:** Boisterous, hot-tempered, argumentative, and protective toward those connected to his close friend Hong Dao; relentlessly disciplined in training, having continued every day after the Great Faction War.
- **Voice:** Loud, blunt, confrontational, and prone to disguising embarrassment or retreat as serious martial instruction.
- **Relationships:** Long-standing rival and friend of Jeok Cheongang; close friend of Hong Dao; protective toward Hong Dao's Disciple Unnamed; father of Peng Cheolyeong.

### Pung Yang.md

# Pung Yang (풍양)

- **Safe through:** Chapter 959
- **Aliases:** Red Wind Band Leader
- **Role:** Former leader of the Red Wind Band, commanding at least two hundred mounted bandits; became a mounted bandit at thirteen, reached First Rate by age thirty, and rose from squad leader to band leader three years ago; discovered the Crimson Blood martial arts and a case containing five Temporary Strength Pills in a hidden plateau tomb, reached the Peak realm in two years, and could temporarily manifest imperfect Sword Force and powerful Body-Protecting Qi by taking a pill; reached approximately seventy percent mastery of the Crimson Blood Twelve Sabers; after secretly incapacitating Jin Mukyung, resumed killing Mount Heng Sword Sect martial artists; was seriously injured by Taekyung's dagger, defeated One Annihilation, seized Taekyung, and was killed by Taekyung after the Unnamed Sword's Ten-Thousand-Year Cold Iron destroyed his Body-Protecting Qi and pierced his chest; had fled from the steppe and commanded nearly four hundred subordinates before his death
- **Personality:** Foxlike, ruthless, observant, controlled, and willing to kill subordinates who disobey his orders
- **Voice:** Calm, concise, and authoritative when issuing orders
- **Relationships:** Leads the Red Wind Band and controls former members of other mounted-bandit groups who joined his force

### Temur.md

# Temur (테무르)

- **Safe through:** Chapter 959
- **Aliases:** None
- **Role:** Temur is a Khan of the northern grasslands, ruling alongside Chinggen over tens of thousands of horses and warriors.
- **Personality:** Hot-tempered and proud of his khan lineage, Temur chose survival over loyalty and now recognizes with guilt that his actions have led his followers to slaughter.
- **Voice:** Blunt, heated, and confrontational
- **Relationships:** The real Chinggen was Temur’s cousin and sworn brother through the anda oath, but he was killed; an impostor wearing Chinggen’s face now deceives Temur.

## Korean source

```text
＃968화



누군가 그랬다.

삼인행(三人行) 필유아사(必有我師).

길을 지나가는 세 사람이 있다면, 그중에서 반드시 스승으로 받들 만한 이가 한 명쯤은 있다고.

물론 벽력도왕은 그 말을 남긴 것이 공자인지, 맹자인지도 정확히 몰랐다.

다만 지금 이 순간 그가 웃고 있는 가장 큰 이유는, 이 자리에 없는 누군가가 떠올랐기 때문이었다.

‘화왕, 그 미친 늙은이가 아니었다면 더 강해지지 못했겠지.’

언제나 주목받았던 삶을 살아왔던 그다.

단순히 천하 오대세가의 일원인 하북팽가에서 태어났기 때문만이 아니라, 그만한 재능과 실력을 지녔다는 점에서 더더욱 그러했다.

남궁천. 모용백. 그리고 팽철후.

이 세 명의 후기지수들은 수많은 명문 세가의 자제 중에서도 단연 으뜸이었고, 뜻하지 않은 불운으로 인하여 같은 반열에 들지 못한 모용백과 달리 나머지 두 사람은 각각 검왕(劍王)과 도왕(刀王)이라 불리게 되었다.

그러나 벽력도왕 스스로는 알고 있었다.

화왕 적천강.

틈만 나면 자신을 갈궈 대던 그 늙은이가 있었기에 제자리걸음만 반복하던 자신이 더욱 강해질 수 있었다는 사실을.

“알려 주지. 자네가 나고 자란 저 초원이 생각만큼 넓지 않다는 것을.”

벽력도왕은 천천히 대도를 들어 올렸다.

그의 도강(刀罡)에 의해 반쯤 잘려 나간 어깻죽지를 부여잡은 채 파르르 떨고 있는 자무카를 향해.

천하에 우뚝 선 거인의 앞에서 신음을 참고 있는 초원의 왕을 향해.

“이제, 끝을 보세.”

쉭.

일보(一步)에 사라지는 공간.

흐릿해졌던 벽력도왕의 신형은 그의 거대한 체구가 믿어지지 않을 정도로 빨랐고, 벼락처럼 내리꽂히는 대도가 그린 궤적은 정확하면서도 침착했다.

서걱!

한 줄기 절삭음과 함께 불길처럼 번지는 통증 속, 자무카는 터져 나오려는 비명을 참기 위해 이를 악물었다.

‘큭……!’

피했다. 분명 피했어야 했다.

그러나 지금 이 순간에도 끊임없이 고통을 호소하는 어깻죽지의 상처와 그 사이로 스며들어 오장육부를 뒤흔든 벽력도왕의 공력은 그의 발길을 붙들고 있었다.

우우웅.

모두의 귓가를 파고드는 공명음(共鳴音).

산산조각 난 자무카의 신월도와는 달리, 흠집 몇 개가 고작인 벽력도왕의 대도가 부르르 떨며 다시 한번 나아갔다.

아니, 나아가는 동시에 나뉘었다.

분명 하나뿐이어야 할 도신이 다섯으로, 열로, 이내 수십으로.

그리고 수십여 개로 나뉜 대도의 잔상(殘像)은 거대한 그물이 되어 전방을 향해 쏘아졌다.

벽력도왕의 나직한 한 마디와 함께.

“가시게.”

그 순간, 자무카를 향한 벽력도왕의 음성과 눈빛에 깃든 감정은 확신이었다.

극심한 부상으로 피를 흘리는 적을 향한 일말의 방심조차 담겨 있지 않은, 오직 자신의 일격과 무위에서 비롯된 확신.

화아아악!

강기의 그물이 덮쳐 온다. 뒤로 몸을 날린 자무카의 등 뒤를 바짝 쫓아온 막대한 기운은 자신에게 닿는 모든 것을 베어 갈랐다.

좌우로 늘어선 암벽. 곳곳에 널브러진 바위와 시체.

그리고 자무카를 구하기 위해 달려든 충직한 수하들까지.

“막아라! 칸께서 위험……!”

퍼걱, 푸화아아악!

그 끝에, 비명은 없었다.

급박한 외침과 함께 달려든 그들은 수십 조각의 육편(肉片)이 되어 허물어졌고, 이를 악문 자무카는 주인 잃은 병장기를 향해 손을 뻗었다.

우웅.

공기가 흔들린다. 허공섭물(虛空攝物)로 끌어당긴 신월도 한 자루가 손아귀에 빨려 들어옴과 동시에 강기를 뿜어냈다.

꽈앙!

강기의 그물이 일부 흩어졌으나, 전신을 뒤흔드는 거대한 충격에 자무카는 울컥 솟구치는 핏물을 삼켰다.

한쪽 팔만으로 펼치는 도법은 그만큼 느렸고, 일격 일격을 맞받아칠 때마다 진탕 하는 내부는 끊임없이 비명을 내질렀다.

하지만.

‘이대로, 그것도 네놈의 손에 죽을 성싶더냐.’

자무카는 마음속 외침과 함께 신월도를 흩뿌렸다.

연이어 울려 퍼지는 굉음과 함께 시야를 물들이는 섬광 너머에는 오래된 과거가 주마등처럼 스쳐 지나가고 있었다.

살기 위해 몸부림치고, 피가 흐르도록 이를 악물며 복수를 다짐하던 젊은 날의 기억과 그런 자신을 향해 기꺼이 손을 내밀어준 누군가의 목소리도 함께.



‘살고 싶지 않나?’



모든 것이 끝났다고 생각했다.

한때 수천에 달하던 전사들은 팽철후가 이끄는 하북팽가의 정예에 의해 전멸에 가까운 타격을 입었고, 자신의 몰락만을 기다리던 경쟁자들은 가축과 재물은 물론 얼마 남지 않은 부족민마저 노예로 빼앗아갈 테니까.

그것이 오직 약육강식(弱肉强食)으로 이어져 내려온 초원의 법칙이었으니까.

하지만 모든 것이 끝났다고 생각한 그 순간 마지막 기회가 찾아왔다.

그리고 산산이 부서진 야심과 수하들의 시체 앞에 주저앉아 있던 젊은 부족장은 자신을 향한 구원의 손길을, 하늘에서 내려온 동아줄을 온 힘을 다해 움켜잡았다.



‘살고 싶소. 아니, 기필코 살아남아야겠소!’

‘살고자 한다면, 무엇을 위함이냐.’

‘복수. 오늘의 치욕과 원한을 반드시 갚을 거요. 만약 당신이 나를 살려 준다면 텡그리께 맹세코…….’

‘돕는 것이 아니다.’

‘그게 무슨.’

‘부리는 것이다. 내가, 너를.’

‘……!’



고민은 그리 길지 않았고, 찰나의 순간 내려진 결심은 철탑처럼 굳건했다.



‘제가 가야 할 길을 알려 주십시오. 주군.’



노예처럼 엎드려 부복한 그의 모습에 구원자는 흡족하게 웃었고, 끝이 보이지 않는 지평선 너머를 가리키며 이렇게 말했다.



‘떠나라. 하북팽가의, 중원의 이목이 닿지 않는 곳에서 새로운 터전을 일구어라.’

‘서부로 향하란 말씀이십니까?’

‘걱정할 것 없다. 그곳은 아직 혼란스럽기 그지없고, 이제 그대는 혼자가 아닌 ‘우리’와 함께하고 있으니.’

‘우리…….’

‘그래, 우리가 돕겠다. 오늘 이 자리에서 새롭게 태어난 대초원의 전사, 자무카여.’



구원자의 말은 옳았다.

새로운 이름과 함께 떠난 젊은 부족장은 서부 초원에서도 금세 두각을 드러냈고, 그가 강대한 세력을 일구어 낼 수 있었던 가장 큰 이유는 구원자의 지원이 있었기 때문이었다.

수많은 가축과 재화. 심지어는 사람과 정보까지도.



‘제법 뛰어난 이들이니 중히 쓰도록 하거라.’



그렇게 자무카의 친위대, 케식이 탄생했고.



‘네가 익힐 만한 신공절학과 하북팽가의 무공이다. 비록 극소수에게만 전해지는 비전 절기까지는 아니지만, 이에 대해 분석한다면 반드시 큰 도움이 되겠지.’



어느덧 벽력도왕이라 불리게 된 일생일대의 대적과 맞설 수 있는 칼과 방패마저 쥐여 주었다.

카앙!

상념을 깨트리는 굉음과 함께 찢어진 손아귀에서 피가 터져 나온다. 자무카는 끝없이 덮쳐 오는 강기의 그물을 향해 미친 듯이 신월도를 휘둘렀다.

살과 뼈는 물론 근육마저 찢겨 나간 한쪽 팔은 사용할 수 없었지만, 기나긴 세월 동안 축적해 온 강대한 내공과 신공절학은 아직도 그의 손끝을 따라 흘러나오고 있었다.

서부에 자리 잡은 지 상당한 시간이 지난 어느 날의 기억도 함께.



‘말씀해 주십시오. 언제쯤 출진하면 되겠습니까.’

‘아직이니 때를 기다려라. 확실한 명령이 떨어지기 전까지 결코 서부를 벗어나서는 안 될 것이다.’

‘아직이라니, 도대체 언제까지 기다려야 합니까?’

‘뭐?’

‘그 명령만 기다리다가는 기회를 놓칠 겁니다. 차라리 정마대전으로 인해 중원이 혼란스러운 지금 하북을 노린다면…….’

‘놀랍군. 사냥개 주제에 사람의 말을 하다니.’

‘……!’

‘도를 뽑아라. 지금 당장.’



구원자의 살기 어린 눈빛에, 자무카는 거절하지 않고 그를 향해 달려들었다.

그리고 젊은 시절의 벽력도왕에게 느꼈던, 아니 그보다 더 높고 거대하게 느껴지는 벽과 마주하여 무릎을 꿇었다.

더불어 그제야 알게 되었다.



‘명심해라. ‘그분’의 명령이 있기 전까지, 우리는 결코 움직이지 않는다.’

‘……그분?’



하늘이나 다름없던 구원자 역시 또 다른 누군가의 사냥개에 불과하다는 것을.

처음부터 그가 말해 왔던 ‘우리’란, 자무카가 생각했던 것을 아득히 뛰어넘을 정도로 깊고 강력한 의미를 담고 있다는 사실을.



‘복수를 이루고 초원을 차지할 그 날까지 마음 깊이 새기거라. 두 번의 용서는 없다.’



그 순간 자무카가 느낀 것은 굴욕감이나 반발심이 아니었다.

그는 두려움과 기쁨으로 전율했다.

자신의 목에 채워진 이 목줄의 주인이 이끄는 대로 따라간다면, 점점 멀어져만 간다고 느껴졌던 목적지에 다다를 수 있을 테니까.

천하를 집어삼킨 목줄의 주인은, 훌륭하게 임무를 끝마친 사냥개에게 이 광활한 대초원을 상으로 던져 줄 테니까.



‘……존명.’



그날 이후 자무카의 마음속에 있던 반발심은 씻은 듯이 사라졌고, 그의 머리카락에 내려앉은 서리만큼의 시간이 흐른 어느 날 마침내 때가 왔다는 것을 깨달았다.



‘이건.’

‘일종의 단환이다. 일시적으로 한계 이상의 힘을 발휘할 수 있는 대신, 그만한 대가를 치러야 하는.’



영단이라고 칭하기에는 너무나도 불길한 효능을 지닌 그것을, 구원자는 잠력단(潛力團)이라 불렀다.



‘이것을 제게 주시는 이유가 무엇입니까?’

‘일종의 실험이라고 해 두지. 머지않은 미래를 위한.’

‘그렇다면 설마.’

‘그분께서 깨어나셨다. 지금부터 중원으로 향하는 교두보를 쌓아라.’

‘……!’



오십여 년의 기다림 끝에 덧붙여진 마지막 몇 년의 시간은, 그야말로 쏜살같이 흘러갔다.

자무카가 명령에 따라 일부 무공서와 함께 초원 곳곳에 흩뿌려둔 단환은 각각 저마다의 주인을 찾았고, 전에는 상상할 수도 없던 힘을 손에 넣은 그들은 온갖 혼란을 일으키며 질서를 어지럽혔다.

비단 초원뿐만이 아니라, 장성 너머의 중원에서도.

풍양.

동부 초원에서 적풍단(赤風團)이라 불리는 마적 떼를 이끌던 우두머리는 상당한 야심가였다.

잠력단의 힘을 빌어 놀라운 속도로 세력을 구축한 그는 마침내 산서성으로 말머리를 돌렸고, 그곳에서 죽음을 맞이했다.

산서잠룡(山西潛龍)이라는 생소한 별호를 지닌, 서서히 몰락해 가던 변방 무가의 핏줄에 의해.



‘진태경. 진태경이라.’



그렇게 흐른 약 이 년의 세월 동안, 참으로 많은 일이 있었다.

태원진가는 산서성의 패자로 우뚝 섰고, 그의 옛 이름이 잊혀진 동부 초원에서는 테무르와 칭겐이라는 두 애송이가 두각을 드러냈으며, 저 멀리 중원에서는 성라대연이 열렸다.

그리고 여러 개의 둑이 허물어지듯, 억눌려 왔던 모든 사건이 차례대로 터져 나왔다.

하남의 소림사를 첫 희생양으로 삼은 피바람은 곧이어 사천과 안휘를 휩쓸더니, 저 멀리 떨어진 운남으로까지 번졌다.

산서의 잠룡은 신룡(神龍)이라 불리게 되었고, 위험을 감지한 중원인들은 무림맹의 깃발 아래 뭉쳤으나 언제 들이닥칠지 모르는 적의 칼날에 명문 대파마저 몸을 움츠렸다.

물론, 자무카에게는 해당하지 않는 이야기였다.

중원의 모든 이들이 두려워하는 적, 암천은 그에게 있어 ‘우리’였으니까.

지금이야말로 자무카가 일평생 기다려 왔던 순간이었으니까.



‘다가오는 중양절까지, 동부 초원을 장악하고 모든 병력을 총동원하여 산서를 점령하라.’



자무카는 그 즉시 휘하의 전사들을 소집했다.

기다린 시간이 길었던 만큼, 그 움직임은 전광석화와 같았다.

그는 마침내 초원 전체를 아우르는 대군세를 결성했고, 구원자는 장성 너머의 상황을 때에 맞춰 전해 주었다.

태원진가를 중심으로 응집한 산서성의 전력. 격전지로 예상되는 장소.

거기에 더하여 마지막으로…….



‘벽력도왕은 반드시 그곳으로 향할 것이다.’



반드시 씻어 내야 할, 케케묵은 원한의 종착지까지도.

그리고 과연 그 말대로 되었다.

단 한 가지를 제외하고.

‘어째서, 어째서!’

혀끝에서만 맴도는 외침과 함께, 자무카는 자꾸만 균형을 잃고 비틀거리는 몸뚱어리를 뒤집었다.

서걱, 푸푸푹!

불로 지지는 듯한 통증.

눈으로 보고, 머리로 인식해도 움직임이 늦다.

끈질기게 쫓아오던 강기의 그물은 어느덧 그의 전신에 수십여 개의 크고 작은 상흔을 남기며 사그라졌지만, 그 너머에는 결코 사냥감을 놓치지 않는 한 마리의 대호(大虎)가 있었다.

굳게 다문 입술. 차가운 불꽃이 일렁이는 눈동자.

그와 함께 양 손아귀가 하얗게 물들도록 힘주어 움켜쥔 거대한 대도를 빈틈없이 휘감은, 휘황찬란한 섬광.

후우우웅.

벽력도왕은 망설임 없이 대도를 휘둘렀고, 자무카는 패(敗)와 쾌(快)가 합쳐진 그 어마 무시한 일격이 공간을 가로지르는 광경을 바라보았다.

그리고 깨달았다.

이제 자신에게 남은 선택지는 하나밖에 없음을.

설령 이 비좁은 협곡에서 힘을 잃고 쓰러지더라도, 지금부터 할 선택이 벽력도왕의 손에 죽는 것보다는 백배 천배 나으리라는 것을.

슥.

수 장 밖에서 날아드는 강기와 함께 느려진 세상 속, 자무카는 품 안에 간직하고 있던 무언가를 꺼냈다.

그리고 피처럼 붉은 그 자그마한 단환을 망설임 없이 입안에 털어 넣었다.

아니, 그러려고 했다.

바로 그 순간, 머리 위에서 한 줄기의 섬광이 떨어져 내리기 전까지는.

푹!

찰나의 고통과 불신으로 물든 자무카의 두 눈동자에 비친 그것은, 다름 아닌 오색 창연한 창날이었다.

그의 손등을 파고듦과 동시에, 그 안에 담겨 있던 마지막 희망인 잠력단마저 꿰뚫어 버린.

“……!”

자무카는 고통조차 잊은 채 고개를 쳐들었다.

짙은 어둠으로 물든 하늘 위에서 떨어져 내린 창의 주인은, 자무카가 아닌 벽력도왕을 향해 입을 열었다.

“이런 부류에 속한 놈들은 경계하고 또 경계해도 늘 부족한 법이지. 자네도 그렇게 생각하지 않나?”

솨악!

단숨에 모든 것을 휩쓸어 버릴 것 같던 대도가 파공성을 일으키며 허공에서 우뚝 멈췄다.

낯익은 얼굴을 발견한 벽력도왕의 입가에 놀라움이 담긴 미소가 떠올랐다.

“그래, 자네가 올 줄 알았지.”

본래의 나이에 비해 이십 년은 젊어 보이는 반백의 중년인을 향해, 벽력도왕은 감회에 찬 목소리로 말을 이었다.

“오랜만일세. 모용백. 아니, 이제는 모용가주라고 불러 드려야 하나?”

과거 북방의 패권을 두고 수없이 반목했던, 그러나 정마대전을 통해 진정한 전우이자 벗이 된 모용백의 모습에 벽력도왕은 환하게 웃으며 대도를 거두었다.

됐다.

이 전쟁은 끝났다.

자무카는 이미 전투 불능이 되었고, 모용백이 이끌고 왔을 모용세가의 정예들은 지금쯤 전장에 합류했을 것이다.

그리고 그의 예상대로, 협곡 너머로부터 울려 퍼지는 외침이 있었다.

“모용세가! 모용세가다!”

벽력도왕은 전신을 팽팽하게 감싸고 있던 긴장의 끈이 풀어지는 것을 느꼈다.

적어도 다음 순간, 하북팽가의 가솔임이 분명한 누군가의 다급한 외침이 이어지기 전까지는.

“태상가주님! 놈들이, 모용세가 놈들이……!”

뭐?

그 순간, 모든 사고가 정지한 벽력도왕은 불현듯 몸속을 파고드는 서늘한 한기를 느꼈다.

서걱!

아찔한 격통 너머로 울려 퍼지는, 나직한 목소리도 함께.

“말했잖나. 아무리 경계해도 부족하다고.”

“……!”

아득하게 흐려지는 시야 속, 벽력도왕은 문득 깨달았다.

자무카.

모든 세력을 잃고 패배자로서 죽음을 맞이했어야 할 젊은 부족장이, 어찌하여 추적을 뿌리치고 지금껏 살아남을 수 있었는지.

‘모용세가.’

그래.

오십여 년 전의 그 날, 놈을 쫓았던 것은 다름 아닌 모용백이었다.

이 모든 재앙의 진정한 화근(禍根).
```

## Final English reading copy

```markdown
# Chapter 968

Someone once said:

*When three people walk together, there is always one who can be my teacher.*

Of course, the Thunderbolt Saber King didn’t know for certain whether Confucius or Mencius had said it.

But the biggest reason he was smiling at that very moment was that someone who wasn’t there had come to mind.

*If not for the Fire King, that crazy old man, I wouldn’t have gotten any stronger.*

He had always lived a life in the spotlight.

Not only because he had been born into the Hebei Peng Family, one of the Five Great Families of the world, but even more because he had the talent and skill to deserve it.

Nangong Cheon. Murong Baek. And Peng Cheolhu.

Among the children of countless prestigious families, these three rising martial artists stood out above the rest. But while unexpected misfortune kept Murong Baek from reaching the same heights, the other two came to be called the Sword King and the Saber King.

But the Thunderbolt Saber King knew the truth.

Fire King Jeok Cheongang.

It was because that old man had constantly ridden him whenever he got the chance that he had grown stronger, instead of remaining stuck where he was.

“I’ll tell you something. That grassland where you were born and raised isn’t as vast as you think.”

The Thunderbolt Saber King slowly raised his great saber.

Toward Jamukha, trembling as he clutched the shoulder that had been half-severed by the Thunderbolt Saber King’s Force.

Toward the king of the steppe, holding back a groan before the giant who stood tall beneath heaven.

“Now, let’s see this through to the end.”

*Whoosh.*

Space disappeared with a single step.

The Thunderbolt Saber King’s blurred form moved so fast it was hard to believe his enormous frame could move that way. The great saber that plunged down like lightning traced a path that was precise and calm.

*Shhk!*

With a single slicing sound and a pain that spread like flames, Jamukha clenched his teeth to hold back the scream rising in his throat.

*Ghk…!*

He’d dodged. He should have dodged.

But even now, the wound in his shoulder kept crying out in pain, and the Thunderbolt Saber King’s internal energy had seeped through it and shaken his internal organs, holding his steps in place.

*Wooooom.*

A resonant hum burrowed into everyone’s ears.

Unlike Jamukha’s crescent saber, now shattered into pieces, the Thunderbolt Saber King’s great saber had only a few scratches. It trembled, then surged forward once more.

No—it split apart as it advanced.

The blade, which should have been one, became five, then ten, then dozens.

The dozens of afterimages formed a massive net and shot toward the space ahead.

Along with the Thunderbolt Saber King’s low voice.

“Go.”

At that moment, what filled the Thunderbolt Saber King’s voice and gaze as he faced Jamukha was certainty.

There wasn’t even a trace of carelessness toward the severely wounded, bleeding enemy—only certainty, born of his strike and his mastery.

*Fwoooosh!*

The net of Force descended. The tremendous energy hot on Jamukha’s heels as he leaped backward cut through everything it touched.

The cliffs lining both sides. The rocks and corpses scattered everywhere.

Even the loyal subordinates who had rushed in to save Jamukha.

“Stop him! The Khan is in danger—!”

*Puk! Fwoooooosh!*

In the end, there were no screams.

Those who had rushed forward with desperate cries crumpled into dozens of chunks of flesh. Jamukha, teeth clenched, reached for a weapon abandoned by its owner.

*Woom.*

The air shuddered. As a crescent saber he had drawn toward himself with Seizing an Object Through Empty Space flew into his grasp, he unleashed a burst of Force.

*BOOM!*

Part of the net of Force scattered, but the enormous impact that shook his whole body made Jamukha swallow the blood surging up his throat.

His saber techniques, wielded with only one arm, were slower. Every time he met a strike head-on, the impact battered his insides, which kept screaming in pain.

But—

*Do you think I’ll die like this? And at your hands?*

With that cry in his heart, Jamukha sent his crescent saber flashing in every direction.

The thunderous booms that followed filled his vision with flashes of light. Beyond them, the distant past swept through his mind like a lantern show.

Memories of his youth, when he had struggled to stay alive, clenched his teeth until they bled, and vowed revenge. And the voice of someone who had willingly reached out to him then.



*“Don’t you want to live?”*



He’d thought everything was over.

The warriors who had once numbered in the thousands had been all but wiped out by the Hebei Peng Family’s elite, led by Peng Cheolhu. His rivals, who had been waiting for him to fall, would take his livestock and possessions—and enslave the few members of his tribe who remained.

That was the law of the steppe, handed down through nothing but the survival of the fittest.

But just as he thought everything was over, his last chance came.

The young chieftain, slumped before his shattered ambitions and his subordinates’ corpses, seized the hand of salvation reaching toward him—the lifeline dropped from the heavens—with all his strength.



*“I want to live. No—I must survive, no matter what!”*

*“If you want to live, what for?”*

*“Revenge. I’ll repay today’s humiliation and grudge, no matter what. If you save me, I swear by Tengri…”*

*“I’m not helping you.”*

*“What do you mean?”*

*“I’m going to use you.”*

*“……!”*



He didn’t deliberate for long. The decision he made in that fleeting moment was as firm as an iron tower.



*“Show me the path I must follow, my lord.”*



The savior smiled, pleased at the sight of him prostrating himself like a slave. Pointing beyond the endless horizon, he said:



*“Go. Build a new home where neither the Hebei Peng Family nor the eyes of the Central Plains can reach you.”*

*“You mean I should head west?”*

*“Don’t worry. That land is still in utter chaos, and you won’t be alone anymore. You’ll be with ‘us.’”*

*“Us…”*

*“That’s right. We’ll help you. Jamukha, warrior of the Great Steppe, reborn here today.”*



The savior had been right.

The young chieftain who left with a new name soon made a name for himself on the western steppe, and the greatest reason he was able to build such a powerful force was the savior’s support.

Countless livestock and goods. Even people and information.



*“They’re quite capable. Make good use of them.”*



That was how Jamukha’s personal guard, the Keshik, came into being.



*“These are supreme martial arts and the Hebei Peng Family’s techniques, suitable for you to learn. They aren’t the secret techniques passed down to only a handful of people, but studying them will surely help you greatly.”*



Before long, he was even given a sword and shield to face the lifelong enemy who would come to be known as the Thunderbolt Saber King.

*Clang!*

A thunderous crash shattered his reverie. Blood burst from his torn palm. Jamukha swung his crescent saber like a madman at the net of Force bearing down without end.

One arm, its flesh, bones, and even muscles torn apart, was unusable. But the mighty internal energy and supreme martial arts he had built up over a long life still flowed through his fingertips.

Along with a memory from long after he had settled on the western steppe.



*“Tell me. When should we set out?”*

*“Not yet. Wait for the right moment. You must never leave the west until you receive a clear order.”*

*“Not yet? How much longer am I supposed to wait?”*

*“What?”*

*“If I wait only for that order, we’ll miss our chance. Now that the Central Plains are in turmoil because of the Great Faction War, we should strike at Hebei instead…”*

*“Amazing. A hunting dog that can talk like a person.”*

*“……!”*

*“Draw your saber. Right now.”*



Under the savior’s murderous gaze, Jamukha didn’t refuse. He charged.

And he met a wall—higher and more imposing than the one he had faced in his youth, when he had fought the Thunderbolt Saber King—and was forced to kneel.

Only then did he understand.



*“Remember this. Until we receive an order from ‘that person,’ we will never move.”*

*“……That person?”*



Even the savior, who had been like the heavens to him, was nothing more than someone else’s hunting dog.

And the “us” the savior had spoken of from the beginning held a meaning far deeper and more powerful than Jamukha had ever imagined.



*“Keep it in your heart until the day you take your revenge and claim the steppe. You will not be forgiven twice.”*



At that moment, Jamukha hadn’t felt humiliation or defiance.

He had shuddered with fear and joy.

If he followed the owner of the leash around his neck, he could reach the destination that had seemed to grow ever more distant.

The leash’s owner, who had swallowed the world, would toss this vast Great Steppe to a hunting dog who had completed his mission well.



*“…As you command.”*



From that day on, the defiance in Jamukha’s heart vanished without a trace. Then, after time had settled on his hair like frost, he realized at last that the moment had come.



*“What is this?”*

*“A kind of pill. It lets you temporarily wield more strength than your limit—but you’ll pay a price to match.”*



Its effects were far too ominous for it to be called a spiritual elixir. The savior called it a Temporary Strength Pill.



*“Why are you giving this to me?”*

*“Call it an experiment. For the near future.”*

*“Then could it be…”*

*“That person has awakened. From now on, build a bridgehead for our advance into the Central Plains.”*

*“……!”*



The final few years added to his fifty-year wait passed in a flash.

Following his orders, Jamukha scattered pills across the steppe, along with a few martial arts manuals. Each pill found its own owner, and those who gained power they could never have imagined before threw everything into chaos, disrupting the established order.

Not only on the steppe, but in the Central Plains beyond the Great Wall as well.

Pung Yang.

The leader of the mounted bandits known as the Red Wind Band on the eastern steppe was a man of considerable ambition.

With the aid of the Temporary Strength Pill, he built his forces at an astonishing pace. At last he turned his horse toward Shanxi Province, where he met his end.

At the hands of a member of a borderland martial family in slow decline, who bore the unfamiliar epithet Sleeping Dragon of Shanxi.



*“Jin Taekyung. Jin Taekyung…”*



About two years passed, and so much had happened.

The Jin Family of Taiyuan had risen to become the power of Shanxi Province. On the eastern steppe, where his old name had been forgotten, two young upstarts named Temur and Chinggen had begun to stand out. Far away in the Central Plains, the Star-Array Grand Banquet was held.

Then, like dams giving way one after another, all the events that had been held back burst forth in succession.

The bloodshed began with Shaolin Temple in Henan as its first victim, then swept through Sichuan and Anhui before spreading as far as distant Yunnan.

The Sleeping Dragon of Shanxi came to be called the Divine Dragon. The people of the Central Plains, sensing danger, gathered beneath the Murim Alliance’s banner, while even the great sects shrank back from the blades of enemies who might strike at any moment.

Of course, none of this applied to Jamukha.

The enemy everyone in the Central Plains feared, Dark Heaven, was “us” to him.

This was the moment Jamukha had waited for all his life.



*“By the coming Double Ninth Festival, seize the eastern steppe and gather every soldier to conquer Shanxi.”*



Jamukha immediately summoned his warriors.

His movements were as swift as lightning, all the quicker for the long wait.

At last, he raised a great army that encompassed the entire steppe, while the savior relayed news from beyond the Great Wall as it came.

Shanxi Province’s forces, gathered around the Jin Family of Taiyuan. The place expected to become the fiercest battlefield.

And finally…



*“The Thunderbolt Saber King will go there for certain.”*



Even the end point of a grudge grown stale with age, one he absolutely had to wipe away.

And it had all gone as predicted.

Except for one thing.

*Why? Why?!*

With a cry that circled only on the tip of his tongue, Jamukha twisted his unsteady body around.

*Shhk! Puh-puh-puk!*

Pain like a branding iron.

Even as his eyes saw it and his mind recognized it, his body moved too slowly.

The net of Force that had pursued him relentlessly had faded after leaving dozens of large and small wounds across his body. But beyond it stood a great tiger that would never let its prey escape.

Lips pressed tightly together. Eyes flickering with cold fire.

And in his hands, gripping the immense great saber so tightly that his palms had gone white, brilliant flashes wrapped around the blade without leaving a gap.

*Whoooom.*

The Thunderbolt Saber King swung without hesitation. Jamukha watched the terrible strike, a fusion of defeat and swiftness, cut through the air.

And understood.

He had only one choice left.

Even if he lost his strength and fell in this narrow gorge, the choice he was about to make would be a hundred, a thousand times better than dying at the Thunderbolt Saber King’s hands.

*Shk.*

With Force flying toward him from several yards away and the world slowing down, Jamukha pulled something from inside his robe.

He tossed the small, blood-red pill into his mouth without hesitation.

Or tried to.

Until, at that very moment, a flash of light came plunging down from above.

*Thuk!*

In Jamukha’s eyes, filled with a moment’s pain and disbelief, he saw a spearhead shining in five colors.

It pierced the back of his hand—and the Temporary Strength Pill he held in it, his last hope.

“……!”

Forgetting even the pain, Jamukha raised his head.

The owner of the spear, which had fallen from the sky shrouded in deep darkness, spoke not to Jamukha, but to the Thunderbolt Saber King.

“With people like this, no amount of caution is ever enough. Don’t you agree?”

*Shwaa!*

The great saber, which seemed poised to sweep everything away in a single stroke, let out a shrill whistle and stopped in midair.

At the sight of the familiar face, a smile of surprise appeared at the corner of the Thunderbolt Saber King’s mouth.

“I knew you’d come.”

The Thunderbolt Saber King continued, his voice thick with emotion, to the middle-aged man with graying hair who looked twenty years younger than his actual age.

“It’s been a long time, Murong Baek. Or should I call you Family Head Murong now?”

Seeing Murong Baek—once his rival for supremacy in the north, but now his true comrade-in-arms and friend after the Great Faction War—the Thunderbolt Saber King grinned broadly and lowered his great saber.

Good.

The war was over.

Jamukha was already out of action, and the elite Murong Family troops Murong Baek had brought with him must have joined the battlefield by now.

And just as he expected, a shout rang out from beyond the gorge.

“The Murong Family! It’s the Murong Family!”

The Thunderbolt Saber King felt the tension that had gripped his entire body slacken.

At least, until a panicked shout from someone who was surely a member of the Hebei Peng Family followed in the next moment.

“Grand Family Head! The enemy—the Murong Family—!”

What?

In that instant, the Thunderbolt Saber King’s mind went blank, and he felt a chill creep through his body.

*Shhk!*

Beyond the blinding pain, a quiet voice rang out.

“I told you. No matter how careful you are, it’s never enough.”

“……!”

As his vision blurred and faded, the Thunderbolt Saber King suddenly understood.

Jamukha.

The young chieftain who should have lost all his power and died a defeated man—how had he shaken off his pursuers and survived until now?

*The Murong Family.*

That was it.

On that day, more than fifty years ago, the one who had pursued him was none other than Murong Baek.

The true root of all this calamity.
```
