<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0989.txt",
      "sha256": "e24d242ef1466b182cc23ff99fc2e91349bbd071a601b53473dad2887581aab0",
      "bytes": 12656
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "798cbfbf3b9fad64274b2add1a0b6eea4f94c7957ace368de634d8133b39bcbd",
      "bytes": 1348
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d13308fe31a2c64daebd8b79b1737ef2a4f6a2f6e86338670363f6d7acf5174f",
      "bytes": 236719
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "93336c47a5885c6f87d88c8bc6a94e4547b5bd20f57c5b39c2dc466aa9aeba67",
      "bytes": 1325
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "fa88d79abc8b48141cf53b28212218832685e2a63672ac094d5c52fa2449f219",
      "bytes": 759
    },
    {
      "path": "characters/Hong Dao.md",
      "sha256": "232d33f730ec1568aed8e13d2ebf03080923d6c3816abbc6518ce5aaf0054f42",
      "bytes": 1000
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "42417751c2acfb73da3c793d34575bcb75e8817d9b738a161d034b691be80104",
      "bytes": 1391
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "b02080b0b97ed95ca6e5d4392eca5c5753e8635b7dc3330452edf34486d4795d",
      "bytes": 1574
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "e6da2167d090df7863f3db298a9b004c1ef027696021d085f3b292a2e652fdaf",
      "bytes": 622
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "dd7d0f6e788a035a6b534d730e6e5a1bd88d8923e9f8de1fe288c8e3cf76d683",
      "bytes": 1083
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "1fcbf2b86e2f521fa01663617877e20df4583a72e59db0e163550f5ffdf3adbf",
      "bytes": 778
    },
    {
      "path": "characters/Peng Cheolhu.md",
      "sha256": "19c8b2765822adbf1a7fb52e56a48d7ac2c93c4a5105b889e08d354395616f31",
      "bytes": 1001
    },
    {
      "path": "characters/Song Ho.md",
      "sha256": "68d345a951a0c2d51eaca880e6be9de27f5a4bf9b6a8885884bca4315c55066a",
      "bytes": 767
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "01eb505153b8bfb0f997a4ee2d2fc22bb3665499082f01713db4cac514f330d1",
      "bytes": 273291
    }
  ],
  "estimated_tokens": 13084
}
-->

# Durable State Update — Chapter 989

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
1 and safe_through 989. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 989. Profile updates may replace only one
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
  "chapter": 989,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 989,
    "continuity_sources": [989],
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
    "Peng Cheolhu died after his remaining strength was consumed in the flames of Taekyung’s advancement; he and Jeok Cheongang parted reconciled, with Jeok saving “younger brother” for a hoped-for reunion.",
    "Jin Taekyung reached Five Qi Returning to Origin and Supreme Peak and entered Bone Transformation.",
    "The System granted Jin Taekyung a level-up, 10 bonus stat points, increased Fame, and feudal-lord status; Jin Wikyung and Jin Mukyung received undisplayed healing effects and bonus buffs.",
    "A Murim Alliance envoy arrived to deliver the Alliance Leader’s message to Jin Wikyung.",
    "The Murong survivors’ innocence and whether they can rebuild as a household remain unresolved."
  ],
  "continuity_sources": [
    987,
    988
  ],
  "open_questions": [
    "What is the Alliance Leader’s message to Jin Wikyung?",
    "Are the Murong survivors innocent, and can they rebuild as a household?",
    "Why did Murong Baek suggest the Heaven Demon Lords’ plans failed and that he may have been used?",
    "Why has Dark Heaven continued costly schemes without revealing its full strength?",
    "Who was the unfamiliar, strangely familiar voice that called Taekyung’s choice wise “just like back then”?"
  ],
  "safe_through": 988,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 굉도     | **Hong Dao**       |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 법왕     | **Dharma King**               | Hong Dao       |
| 무신     | **Martial God**               | —              |
| 벽력도왕   | **Thunderbolt Saber King**    | Peng Cheolhu   |
| 삼성     | **Three Saints**    |
| 십왕     | **Ten Kings**       |
| 태원진가   | **Jin Family of Taiyuan**        |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 정파     | **orthodox faction**                             |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 제자     | **Disciple**                                 |
| 선배     | **Senior**                                   |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 정마대전   | **Great Faction War**         |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 송호 | **Song Ho** | Elderly martial artist known as the Thousand-Faced Fox. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 환골탈태 | **Bone Transformation** | Advanced transformation described as optional in martial-arts novels. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 삼매진화 | **Samadhi True Fire** | Internal-energy flame demonstrated by the unnamed old man. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 천기 | **heavenly patterns** | Celestial patterns Hong Dao studies to perceive major changes and omens. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 천면호리 | **Thousand-Faced Fox** | Epithet of Song Ho. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 외당 | **Outer Hall** | The Tang Clan's outer hall area. |
| 내당 | **Inner Hall** | The Tang Clan's inner hall area. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 괴력난신 | **supernatural powers** | Term for extraordinary and unnatural powers. |
| 격체전공 | **Transmitting Internal Energy Across the Body** | Technique for transferring internal energy between bodies. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 천하제일검 | **Number One Sword Under Heaven** | Mae Jonghak's title. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |
| 진화 | **evolution** | The transformation the Southern Heaven Demon Empress claims the rift will produce. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 심해 | **deep sea** | Unexplored ocean depths where the ancient monster awakens. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 적천강 | 굉도 | old_friends | Hong Dao | familiar and teasing | Uses Hong Dao's personal name in their casual reunion. |
| 굉도 | 적천강 | old_friends | Fire Gate Sect Leader | familiar and teasing | Teases Jeok as the carefree Fire Gate Sect Leader. |
| 굉도 | 진태경 | senior_monk_to_guest_benefactor | Benefactor | formal-polite and probing | Hong Dao repeatedly addresses Taekyung as 시주 while identifying him as the Master of Morning Star. |
| 송호 | 청년 | elderly_martial_artist_to_younger_martial_artist | Young Hero | formal-polite | Song Ho calls out to the young man as 소협 at the chapter's end. |
| 적천강 | 벽력도왕 | rival_martial_master_to_rival_martial_master | Virility Saber King | insulting and taunting | Jeok coins 정력도왕 as a taunting replacement for the established title. |
| 벽력도왕 | 적천강 | rival_martial_master_to_rival_martial_master | Jeok Cheongang | boisterous and hostile-teasing | The Thunderbolt Saber King calls Jeok by name before their argument escalates. |
| 송호 | 진태경 | senior_martial_artist_to_junior_martial_artist | you | familiar-polite | Uses 자네 while recognizing Taekyung and discussing his preliminary performance. |
| 매종학 | 송호 | savior_to_survivor | you | casual-familiar | Mae uses 자네 while speaking to Song Ho after his identity is recognized. |
| 송호 | 매종학 | rescued_survivor_to_savior | Great Hero; you | formal-deferential and familiar | Song Ho credits Mae with saving his life and addresses him as 대협. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 매종학 | 적천강 | long-standing martial rival and friend | Great Hero Jeok | casual and familiar | Mae addresses Jeok as 적 대협 while discussing the Alliance Leader position. |
| 적천강 | 매종학 | long-standing martial rival and friend | you | blunt and familiar | Jeok addresses Mae as 당신 while recalling their meeting at Mount Jiuhua. |
| 벽력도왕 | 진태경 | elder martial master to younger rival | you | boisterous and confrontational | Peng addresses Taekyung as 네놈 while discussing Peng Dojin. |
| 천면호리 | 매종학 | intelligence_chief_to_alliance_leader | Alliance Leader | formal and deferential | Requests that Mae move elsewhere with the others before he reports further. |
| 벽력도왕 | 매종학 | Ten Kings peer to Ten Kings peer | Sword Saint | familiar and blunt | Asks Mae what was discussed in the sealed meeting. |
| 매종학 | 벽력도왕 | Ten Kings peer to Ten Kings peer | Peng | casual and admonitory | Calls him 팽가야 and tells him to remain quiet. |
| 청풍 | 매종학 | grandson to grandfather | Grandpa | casual-familiar | Repeatedly calls Mae Jonghak 할아버지 while mistaking the Alliance Leader's summons as a family visit. |
| 진태경 | 매종학 | younger ally to newly installed Alliance Leader | Alliance Leader | formal and deferential | Uses 맹주님 while formally greeting Mae Jonghak as the Alliance Leader. |
| 송호 | 적천강 | Hidden Shadow Pavilion Chief to legendary senior master | Great Hero Jeok | formal-deferential | Song Ho addresses Jeok while questioning the basis for his confidence in Taekyung. |
| 적천강 | 송호 | senior martial master to allied intelligence chief | you | blunt but reassuring | Jeok directly tells Song Ho to believe Taekyung. |
| 매종학 | 천면호리 | Alliance Leader to Hidden Shadow Pavilion Chief | Chief of the Hidden Shadow Pavilion | casual-but-commanding | Asks Song Ho's view of Taekyung's suspected target. |
| 적천강 | 법왕 | close deceased friend and peer | you | familiar and reflective | Jeok addresses the Dharma King in private thought while wishing he were present to clarify Jeok's confusion. |
| 진태경 | 벽력도왕 | younger martial artist to senior martial master | Great Hero Peng | formal and deferential | Taekyung offers a respectful salute and addresses Peng as 팽 대협. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 986
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak martial master known as the Huashan Divine Dragon, the creator of the snake-inspired Mimi Step footwork technique, and the master of the Azure Dragon Pavilion within the Alliance Leader's Two Dragons Pavilion.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi, now a large horned snake, to him, and Cheongpung is accompanying Mungyeong while learning his martial arts through observation to become stronger and adapt to this world.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 988
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hong Dao.md

# Hong Dao (굉도)

- **Safe through:** Chapter 985
- **Aliases:** Dharma King
- **Role:** Abbot of Shaolin and the Murim's Dharma King; master of Unnamed and the only friend to whom Jeok Cheongang had opened his heart; after leaving the Star-Array Grand Banquet, he was found in a massive pit with both legs severed and catastrophic internal injuries, whispered final words to Jeok Cheongang, and died.
- **Personality:** Calm, responsible, quietly playful, and still regarded by Jeok as lazy for sleeping whenever possible.
- **Voice:** Quiet, deep, weighty, and resonant, with casual familiarity when speaking to Jeok Cheongang.
- **Relationships:** Old friend of Jeok Cheongang and close friend of Peng Cheolhu; master of Unnamed; before his death, entrusted the Green Jade Buddha Staff to Unnamed, warned Jeok about Jongni Chu, Dark Heaven, Unnamed, and the Buddhist Staff, and sent Unnamed to find the Master of Morning Star.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 988
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 988
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor has appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Peng Cheolhu regarded Taekyung as a worthy successor, inheriting all that Peng had to pass on; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 988
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 950
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader and has ordered Jin Taekyung's first Fire Dragon Pavilion mission to Nanman.
- **Personality:** Playful and easygoing in ordinary company, yet guided by a principled commitment to chivalry that can outweigh strategic caution.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 977
- **Aliases:** None
- **Role:** An unidentified legendary martial artist regarded as a pinnacle above the Ten Kings; more than fifty years ago, he defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, Mae Jonghak received several teachings from him, and he left the Bow Saint a letter describing a chosen one; the Bow Saint says he chose her, while his identity, whereabouts, and possible connection to Cheon Taemin remain unknown.

### Peng Cheolhu.md

# Peng Cheolhu (벽력도왕)

- **Safe through:** Chapter 988
- **Aliases:** Thunderbolt Saber King
- **Role:** Peng Cheolhu was the Thunderbolt Saber King, a Ten Kings master and Great Hero of the Hebei Peng Family who died as his accumulated internal energy and remaining life force melted into the flames of Taekyung’s advancement.
- **Personality:** Boisterous and teasing with old friends, yet calm and accepting in the face of death; willing to give everything he has left to protect the world.
- **Voice:** Loud, blunt, confrontational, and prone to disguising embarrassment or retreat as serious martial instruction.
- **Relationships:** He was Jeok Cheongang’s long-standing rival and friend, Hong Dao’s close friend, protective toward Hong Dao’s Disciple Unnamed, father of Peng Cheolyeong, and longtime friend and former youthful rival of Murong Baek; Jeok and Peng parted reconciled as brothers in all but blood.

### Song Ho.md

# Song Ho (송호)

- **Safe through:** Chapter 950
- **Aliases:** Thousand-Faced Fox
- **Role:** Elderly Peak master known as the Thousand-Faced Fox, a martial artist with a prosthetic leg, and current Chief of the Hidden Shadow Pavilion, overseeing a vetted intelligence network that includes highly trained assassins.
- **Personality:** Outwardly genial and relaxed, but observant, forceful, and intimidating when pursuing information.
- **Voice:** Lightly genial and conversational, turning quietly coercive during interrogation.
- **Relationships:** He serves under Mae Jonghak's New Murim Alliance, commands the Hidden Shadow Pavilion, and recognizes Jin Taekyung as Jeok Cheongang's Disciple.

## Korean source

```text
＃989화



천면호리(千面狐狸) 송호는 그날도 눈코 뜰 새 없는 하루를 보내고 있었다.

아니, 정확히는 그럴 예정이었다.

고작 한 시진도 되지 않는 숙면을 끝내고 자리에서 일어날 때만 하더라도, 그의 머릿속에는 일각(一刻) 단위로 나뉜 하루의 일과가 빼곡하게 정리되어 있었으니까.

그러나 해가 떠오르기도 전에 상관을 찾은 은영각 요원의 손에 들린 붉은색 전서(傳書)의 내용을 확인한 순간, 천면호리는 깨달았다.

오늘의 일과가, 결코 계획대로 흘러가지 못하리라는 것을.

“잡혀 있던 회의는 취소일세. 대신 일 다경 안에 내당(內堂)의 간부들을 소집하게.”

“한 사람도 예외 없이 전달토록 하겠습니다.”

“외당(外堂)은 어찌 되어 가고 있나.”

“이미 경계 태세에 들어갔습니다. 각 성으로 보낼 전서응 역시 모든 준비를 끝낸 채로 각주님의 명을 기다리…….”

“당장 출발시키도록 하게. 나는 그사이에 맹주(盟主)님을 뵙고 오도록 하지.”

그 외에도 여러 가지 명령을 전달한 천면호리는 바쁜 걸음으로 목적지를 향해 걸음을 옮겼다.

그리고 언제나 그렇듯, 검성(劍星) 매종학은 가부좌를 튼 채 그를 기다리고 있었다.

“좋지 않은 소식을 듣기에는 아직 이른 시간인데. 해 뜰 때까지만이라도 기다리지 그랬나.”

호숫가의 물처럼 투명한 목소리와 눈빛.

평소에는 그저 세상 태평하게만 보였던 천하제일검(天下第一劍)의 침착한 모습에, 천면호리가 조심스럽게 입을 열었다.

“이미…… 알고 계셨습니까.”

“글쎄, 잘은 모르겠네. 다만 오늘따라 쉽게 잠을 이룰 수 없더군.”

천천히 눈을 뜬 매종학이 천면호리를 응시했다.

아니, 정확히는 그의 손에 들린 붉은색 전서를.

“그래, 이번에는 누구인가.”

매종학의 목소리는 깊게 가라앉아 있었다.

비록 오랜 세월이 흐르고, 많은 부분이 바뀌었지만 변치 않고 그대로인 것 또한 있는 법.

비보(悲報)를 의미하는 붉은 서신도 그중 하나였다.

과거 정마대전에서 중요한 인물이 죽거나, 큰 인명 피해가 발생했을 때마다 그들은 침통한 마음으로 붉은색의 전서를 작성하고는 했다.

바로 지금, 천면호리의 손에 들린 그것처럼.

“맹주님.”

“괜찮으니 말하게. 그 적서(赤書)에 적힌 이름을.”

잠시 망설이던 천면호리가 침통한 음성으로 입을 열었다.

“태원진가에 머무르고 계시던 벽력도왕(霹靂刀王)께서 결국…….”

“그만. 되었네.”

손을 내저은 매종학이 씁쓸한 얼굴로 뇌까렸다.

“그래, 결국 그리되었군.”

“이런 소식을 전하게 되어 죄송할 따름입니다.”

“자네가? 아니야. 굳이 누군가를 탓해야 한다면 그건 바로 맹주인 나겠지.”

천면호리는 말없이 고개를 숙였다.

구파일방과 오대세가의 촉망받는 후기지수로, 함께 힘을 합쳐 전란을 헤쳐 나온 전우로 수십여 년간 교분을 쌓아 온 두 사람이다.

지금만큼은 맹주가 아닌 고인의 벗으로 이 소식을 받아들일 시간을 주어야 했고, 다행히 침묵은 그리 길지 않았다.

“팽 선배는, 어찌 가셨다던가.”

“마지막까지 웃으며 떠나셨다고 합니다. 시간이 얼마 남지 않았다는 것을 스스로 아시고, 격체전공(隔體傳功)으로 당신의 모든 것을 남기셨습니다.”

이 놀라운 소식에는 가장 중요한 누구에게, 가 빠져 있었으나 매종학은 구태여 되묻지 않았다.

천면호리의 대답이 채 끝나기도 전에 뇌리에 떠오른 한 사람의 이름이 있었기에.

“진태경. 분명 그 아이겠군.”

“예. 매우 위험한 시도이긴 했으나, 대법은 성공적으로 마무리되었다고 합니다.”

매종학은 조용히 고개를 끄덕였다.

비록 짧은 시간이었지만, 진태경을 직접 겪어 본 그로서는 이번 격체전공의 성공을 어렴풋이 짐작하고 있었다.

“그 아이라면 충분히 그러고도 남지. 도무지 깊이를 알 수 없을 정도니.”

그러나 다음 순간 이어진 천면호리의 보고에는, 매종학마저 헛웃음을 흘릴 수밖에 없었다.

“허, 환골탈태(換骨奪胎)라.”

천무지체가 선천적으로 타고난 것이라면, 환골탈태는 강대한 공력과 깨달음을 바탕으로 후천적으로 신체를 완벽하게 재조립하는 과정.

설령 죽음을 앞둔 백발의 노인이라 해도 젊음을 되찾고, 놀라운 무공의 증진을 겪을 수 있는 것이 바로 환골탈태다.

한데 누구나 꿈꿔 마지않은 그 환골탈태의 행운이 고작 약관 어림의 청년에게 주어졌다니.

전서에 쓰인 내용을 직접 두 눈으로 확인하고 읽어 준 천면호리마저 믿기 힘들어하는 기색이 역력했다.

“이것이 진정…… 가능한 일입니까?”

“믿지 못하는 눈치로군.”

“저뿐만 아니라, 대부분이 마찬가지일 것입니다.”

“어째서 불가능하다고 생각하나?”

“장장 천 년에 달하는 무림사(武林史)를 통틀어 환골탈태를 경험한 이가 몇이나 되겠습니까. 제가 아는 바로는 고작 스물도 채 되지 않습니다.”

“그 말도 일리가 있군. 하지만 자네가 간과하고 있는 사실이 있네.”

“무엇입니까?”

되묻는 천면호리를 향해, 매종학은 대답 대신 한 손을 펼쳤다.

“다섯.”

“그게 무슨…….”

“고작 스무 명도 되지 않는 그들 중, 작금의 이 시대에서만 벌써 다섯 명이라는 뜻이지.”

“……!”

“아니, 이제 여섯 명이 되겠군.”

무신과 삼성.

화왕 적천강과 그의 제자인 열화신룡 진태경까지.

읊조림과 함께 한 손가락을 더한 매종학이 담담하게 말을 이었다.

“참으로 희한한 일이지 않나? 환골탈태를 겪은 이들은 지난 천년을 통틀어도 고작 스물 남짓에 불과한데, 정파 무림으로만 쳐도 이미 여섯이니.”

“그건…….”

“자네도 스스로 이미 충분히 느끼고 있을 걸세. 다만 겉으로는 쉽게 받아들이지 못할 뿐이지.”

매종학이 가부좌를 풀며 자리에서 일어났다.

당장 어디에서나 마주칠 수 있을 것처럼 평범한 용모와 분위기. 그러나 천면호리를 응시하는 그의 눈동자는 투명하리만치 맑았다.

“우리는 실로 괴이한 시대를 살아가고 있네. 상식의 경계선은 이미 허물어진 지 오래고, 상상할 수 없었던 거대한 암운(暗雲)이 천하에 드리워졌지.”

과거 오십여 년 전, 무신과 천마라는 두 절대자가 동시대에 등장했다.

그뿐인가.

정사마를 아울러 수십여 명의 초절정 고수들이 그 언저리를 장식했고, 전례 없던 힘을 지닌 초인들의 대전이 시작되었다.

삼성과 십왕, 경천동지할 힘을 지닌 마교와 사파의 대마두들.

그리고…….

“이제는 그 시절의 마교를 아득히 뛰어넘는, 암천(暗天)이 나타났지.”

시대가 사람을 만드는 것인가, 혹은 사람이 시대를 만드는 것인가.

지금껏 수많은 갑론을박을 낳은 그 화두의 명확한 답은 그 누구도 찾지 못했고, 검성 매종학 역시 예외는 아니었다.

다만 그는 자신이 살아가는 지금의 이 시대가, 그저 단순한 난세(亂世)가 아니라는 것을 내심 깨닫고 있었다.

혼란한 시대로 인해 탄생한, 혹은 그런 시대를 만들어 가는 초인들 간의 대립으로 가려진 무언가가 느껴졌다.

“이해하지 못할 괴력난신(怪力亂神)의 힘과 끔찍한 형태의 괴물들. 그리고 그 중심에 있는 천주라는 자.”

깊어진 눈동자로, 매종학은 혼잣말처럼 뇌까렸다.

“간혹 그런 생각을 떠올리곤 한다네. 어쩌면 이 모든 것이, 우리로서는 상상할 수도 없는 누군가에 의해 짜인 농간이 아닌가 하는.”

매종학은 문득 고개를 돌려 창밖을 바라보았다.

머나먼 동쪽으로부터 번져오는 햇살을 빼곡히 가리며, 천천히 떨어져 내리는 새하얀 눈송이들이 보였다.

초가을의 눈. 그것도 엄청난 폭설(暴雪).

따뜻한 기후를 지닌 하남에서는 쉽게 볼 수 없는, 아니 유례없었던 현상이 몇 달 전을 기점으로 벌어지고 있었다.

비단 하남뿐만이 아니라, 천하 각지에서.

변화는 지상에서만 벌어지는 것이 아니었다.

언제나 모두의 머리 위에 놓여 있던 하늘이, 법왕 굉도가 일찍이 예견했던 천기(天氣)가 급속도로 변화하고 있었다.

“자네는 이해할 수 있겠나? 이 모든 것을.”

매종학의 물음에, 천면호리 송호는 말없이 입술을 깨물었다.

어느덧 그의 등허리는 식은땀으로 축축하게 젖어 있었다.

“저는, 저는 도저히 모르겠습니다. 대관절 무슨 일이 벌어지려는 것인지 짐작조차 할 수 없습니다.”

잘게 떨리는 음성.

무신을 가까이에서 보필하며 천마가 이끄는 십만 마도와 맞서 싸웠던 그조차도, 앞에 놓인 미래를 떠올리자 침착함을 유지할 수 없었다.

이건 마치…….

‘인세(人世)의 경계를 벗어난 무언가.’

혀끝에 맴도는 그 한마디를, 천면호리는 차마 토해 내지 못하고 삼켰다.

믿을 수 없었으니까.

아니, 믿기 싫었으니까.

그리고 이처럼 동요하는 천면호리의 모습을, 매종학은 투명한 눈동자로 들여다보고 있었다.

“송 각주. 자네의 상관이자 무림맹의 맹주로서 한마디만 해도 되겠나?”

“말씀하십시오.”

“두려움을 인정하고 받아들이게.”

“……!”

“다른 그 누구보다 두려워하게. 늘 적들을 경계하고, 의심해야만 해. 자네와 나는 그럴 수밖에 없는 자리에 있네.”

매종학의 말에 담긴 의미를, 천면호리는 즉시 알아들었다.

“맹주님의 말씀, 가슴 깊이 새기겠습니다.”

“고맙군. 자네는 냉철하고 영민한 사람이야. 내가 봐 왔던 사람 중에서도 가장……은 아니고 열 손가락 안에 들지.”

천면호리가 실소를 흘렸다.

“제 위로 제법 많은 모양이군요.”

“계산은 정확해야 하지 않겠나. 섭섭해도 이해하게.”

“그 말씀은 안 새기도록 하겠습니다.”

“좋은 소식이로군. 당장 처리해야 하는 일만으로도 이미 자네 머릿속은 정신없이 바쁠 테니.”

“물론입니다. 그럼 이만.”

흐릿하게 웃은 매종학은, 처음 왔을 때처럼 바쁜 걸음으로 떠나가는 천면호리를 붙잡지 않았다.

그리고 그가 남기고 간 붉은 전서를 천천히 읽은 뒤, 작은 목소리로 중얼거렸다.

“결국 이렇게, 다시 한번 누군가를 떠나보내는군.”

벽력도왕과의 교분을 떠나, 그의 죽음은 정파 무림 전체에 있어 크나큰 손실이었다.

유구하게 흘러간 세월 속에서 십왕(十王)의 절반이 스러졌고, 다섯 명밖에 남지 않았던 그들 중 또 한 명의 희생자가 나왔다.

다만 벽력도왕의 죽음으로 인한 슬픔을 조금이나마 잊을 수 있는 것은, 거인의 마지막 발걸음이 남긴 흔적 때문이리라.

“열화신룡 진태경.”

줄곧 뇌리에 맴돌던 그 이름을, 매종학은 조용히 읊조렸다.

비록 벽력도왕이라는 큰 별이 졌으나, 새롭게 떠오른 별이 그 빈자리를 채웠다.

아니, 이미 그 전부터 환하게 빛나고 있었다.

신룡(神龍)이라는 별호를 증명하듯이.

‘머지않아 두 마리의 용이, 마침내 하늘에 오르겠구나.’

매종학은 조금도 의심하지 않았다.

천하 무림의 거인으로 거듭난 진태경과, 자신이 친손자처럼 키워 낸 마지막 후인이 이 괴이한 시대의 중심이 되리라는 사실을.

그리고 지금쯤 아주 먼 곳에서 뒤늦게나마 산서성의 소식을 접했을 청풍을 떠올리며, 손에 쥔 전서에 공력을 주입했다.

화륵. 파스슥.

삼매진화(三昧眞火)의 불꽃이, 매종학의 투명한 눈동자를 불그스름하게 물들였다.
```

## Final English reading copy

```markdown
# Chapter 989

The Thousand-Faced Fox, Song Ho, was having another day so busy he couldn’t catch his breath.

Or, more accurately, he was supposed to be.

When he got up after less than two hours of sleep, his day’s schedule had already been neatly laid out in fifteen-minute increments.

But the moment he read the message in the red missive brought by a Hidden Shadow Pavilion agent who had sought him out before sunrise, the Thousand-Faced Fox realized:

Today was not going to go according to plan.

“Cancel the meeting already on the schedule. Instead, summon the Inner Hall’s officers within fifteen minutes.”

“I’ll make sure every one of them is notified.”

“What’s the Outer Hall doing?”

“They’re already on alert. The messenger eagles to be sent to each province are fully prepared and waiting for your orders, Pavilion Master—”

“Send them out at once. In the meantime, I’ll go see the Alliance Leader.”

After giving several more orders, the Thousand-Faced Fox set off briskly toward his destination.

And, as always, Sword Saint Mae Jonghak was waiting for him, seated cross-legged.

“It’s early for bad news. You could’ve waited until sunrise, at least.”

His voice and gaze were as clear as water by a lake.

Faced with the Number One Sword Under Heaven’s calm, which usually made him seem utterly at ease with the world, the Thousand-Faced Fox cautiously spoke.

“Had you already… heard?”

“I can’t say I know. I just found it hard to sleep last night.”

Mae Jonghak slowly opened his eyes and looked at the Thousand-Faced Fox.

Or, more precisely, at the red missive in his hand.

“So. Who is it this time?”

Mae Jonghak’s voice had sunk low.

Though many years had passed and much had changed, some things remained just as they were.

Red letters bearing bad news were one of them.

Whenever an important figure died or there were heavy casualties during the Great Faction War, they would write a red missive with heavy hearts.

Just like the one in the Thousand-Faced Fox’s hand now.

“Alliance Leader.”

“It’s all right. Tell me the name written in that red letter.”

After hesitating for a moment, the Thousand-Faced Fox spoke in a heavy voice.

“The Thunderbolt Saber King, who was staying with the Jin Family of Taiyuan, has finally…”

“Enough. That will do.”

Mae Jonghak waved a hand and muttered with a bitter expression.

“So it came to this, after all.”

“I can only apologize for bringing you such news.”

“You? No. If someone has to be blamed, it should be me—the Alliance Leader.”

The Thousand-Faced Fox bowed his head without a word.

They had spent decades building a bond: as promising young martial artists of the Nine Sects and One Gang and the Five Great Families, and as comrades who joined forces to weather the war.

For now, he had to give Mae Jonghak time to take in the news as the deceased man’s friend, not as the Alliance Leader. Fortunately, the silence didn’t last long.

“How did Senior Peng pass?”

“They say he left smiling to the very end. He knew for himself that he didn’t have much time left, so he passed on everything he had through Transmitting Internal Energy Across the Body.”

The astonishing news left out one crucial detail: to whom.

But Mae Jonghak didn’t bother to ask.

Before the Thousand-Faced Fox could finish answering, one name had already come to mind.

“Jin Taekyung. It must’ve been that boy.”

“Yes. It was an extremely dangerous attempt, but I’m told the technique was completed successfully.”

Mae Jonghak quietly nodded.

Though he’d spent only a short time with Jin Taekyung, he’d had a vague sense that the transfer would succeed.

“That boy could certainly pull it off. You can’t fathom how deep he goes.”

But the Thousand-Faced Fox’s next report drew a hollow laugh from even Mae Jonghak.

“Bone Transformation, you say?”

If the Heavenly Martial Physique was something one was born with, Bone Transformation was the process of completely rebuilding the body after birth, through immense internal energy and enlightenment.

Even a white-haired old man on the verge of death could regain his youth and see a remarkable increase in his martial arts—that was the power of Bone Transformation.

And yet the good fortune everyone dreamed of had been granted to a young man barely past twenty.

Even the Thousand-Faced Fox, who had read the report with his own eyes, looked like he could hardly believe it.

“Is this truly… possible?”

“You don’t seem convinced.”

“I doubt most people would be.”

“Why do you think it’s impossible?”

“In the entire thousand-year history of Murim, how many have experienced Bone Transformation? As far as I know, fewer than twenty.”

“You have a point. But there’s something you’re overlooking.”

“What is it?”

Mae Jonghak spread one hand instead of answering.

“Five.”

“What does that—”

“I mean that of those fewer than twenty, five have already appeared in this age alone.”

“……!”

“No—now there’ll be six.”

The Martial God and the Three Saints.

The Fire King, Jeok Cheongang, and his Disciple, the Blazing Flame Divine Dragon, Jin Taekyung.

As he spoke, Mae Jonghak raised one more finger and continued calmly.

“Isn’t it strange? In the last thousand years, only around twenty people have undergone Bone Transformation, yet six have appeared in the orthodox Murim alone.”

“That’s…”

“You’ve felt it yourself, I’m sure. You just can’t easily accept it out loud.”

Mae Jonghak unfolded his legs and stood.

His appearance and presence were so ordinary he looked like someone you might run into anywhere. But as he gazed at the Thousand-Faced Fox, his eyes were clear as glass.

“We’re living in a truly strange age. The boundaries of common sense collapsed long ago, and a vast, unimaginable shadow has fallen over the world.”

More than fifty years ago, two supreme figures had appeared in the same age: the Martial God and the Heavenly Demon.

And that wasn’t all.

Dozens of Supreme Peak masters from the orthodox, unorthodox, and Demonic factions had gathered around them, and a battle had begun between superhumans wielding unprecedented power.

The Three Saints and the Ten Kings. The great fiends of the Demonic Cult and the unorthodox factions, wielding earth-shaking power.

And…

“Now Dark Heaven has appeared, surpassing even the Demonic Cult of that era by far.”

Does the age make the people, or do the people make the age?

No one had ever found a clear answer to that question, which had prompted countless debates. Sword Saint Mae Jonghak was no exception.

But deep down, he understood that the age he lived in was more than a simple time of chaos.

He sensed something hidden behind the conflict between superhumans—born of a chaotic age, or perhaps bringing one into being.

“The supernatural powers we can’t understand, the grotesque monsters. And the man at their center—the Lord of Heaven.”

With a deepening gaze, Mae Jonghak muttered as if to himself.

“Sometimes I find myself wondering if all this is some sort of scheme, laid out by someone beyond anything we could imagine.”

Mae Jonghak suddenly turned to look out the window.

Snowflakes drifted slowly down, thickly covering the sunlight spreading from the distant east.

Snow in early autumn. A tremendous snowfall, at that.

It was a phenomenon rarely seen in Henan’s warm climate—or rather, one never seen before—that had begun several months ago.

And it wasn’t just Henan. It was happening throughout the world.

The changes weren’t limited to the ground, either.

The sky that had always stretched above them—the heavenly patterns Dharma King Hong Dao had once predicted—was changing at an alarming rate.

“Can you make sense of any of this?”

At Mae Jonghak’s question, the Thousand-Faced Fox, Song Ho, bit his lip without a word.

By now, cold sweat had dampened his back.

“I—I can’t understand it at all. I can’t even begin to guess what’s about to happen.”

His voice trembled.

Even he, who had served the Martial God at close quarters and fought against the hundred thousand under the Heavenly Demon’s command, couldn’t stay calm when he thought of the future ahead.

This was like…

*Something beyond the bounds of the human world.*

The words hovered on the tip of his tongue, but the Thousand-Faced Fox couldn’t bring himself to let them out. He swallowed them instead.

He couldn’t believe it.

No—he didn’t want to believe it.

Mae Jonghak watched the Thousand-Faced Fox’s agitation with clear eyes.

“Chief Song. May I say something to you as your superior and as the Alliance Leader?”

“Please.”

“Admit your fear and accept it.”

“……!”

“Be more afraid than anyone else. Always be on guard against our enemies and distrust them. You and I have no choice. We’re in positions where we have to.”

The Thousand-Faced Fox understood the meaning behind Mae Jonghak’s words at once.

“I’ll take your words to heart, Alliance Leader.”

“Thank you. You’re a coolheaded, intelligent man. One of the most… well, not the best, but certainly among the top ten I’ve known.”

The Thousand-Faced Fox gave a dry chuckle.

“So there are quite a few above me, then.”

“Wouldn’t the ranking have to be accurate? Don’t take it personally.”

“I’ll try not to take that part to heart.”

“That’s good news. Your mind is already busy enough with the work you need to handle right away.”

“Of course. Then I’ll take my leave.”

Mae Jonghak smiled faintly but didn’t stop the Thousand-Faced Fox as he hurried away, just as briskly as he’d arrived.

After reading the red missive he had left behind, Mae Jonghak murmured in a low voice.

“So, in the end, I’m losing someone again.”

Apart from his friendship with the Thunderbolt Saber King, Peng’s death was a tremendous loss to the orthodox Murim as a whole.

Over the long years, half of the Ten Kings had fallen. And now another had been lost from the five who remained.

But perhaps the sorrow of the Thunderbolt Saber King’s death could be eased, if only a little, by the mark left behind by that giant’s final step.

“The Blazing Flame Divine Dragon, Jin Taekyung.”

Mae Jonghak quietly spoke the name that had lingered in his mind.

Though a great star named the Thunderbolt Saber King had fallen, a new star had risen to fill his place.

No—he had already been shining brightly long before this.

Just as his title, Divine Dragon, promised.

*Before long, two dragons will finally ascend to the heavens.*

Mae Jonghak had not the slightest doubt.

Jin Taekyung, who had become a giant of Murim, and the last successor he had raised like his own grandson would become the center of this strange age.

Thinking of Cheongpung, who must by now have finally heard the news from Shanxi Province even where he was so far away, Mae Jonghak poured internal energy into the missive in his hand.

*Fwoosh. Crackle.*

The flames of Samadhi True Fire tinted Mae Jonghak’s clear eyes red.
```
