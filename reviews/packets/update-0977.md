<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0977.txt",
      "sha256": "8ec87e8aad6bbdbda22e8ae3fc9be29d9f6a99ebbbbd770f02da101ce06a0665",
      "bytes": 13934
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "25b38cc339a7b27ea4fa7d1198d468c081db1a7ead8574aae173db2ceb124faa",
      "bytes": 1118
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "4de0b4fbadec01764846e722e652a6e38dd708f35d7640cb2b357837c37368f1",
      "bytes": 235674
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "bd2bf95c1adae3462c85ffad383d42b6db3867dc96f3cea4cfcf06368dabb0b8",
      "bytes": 759
    },
    {
      "path": "characters/Eastern Heaven Demon Lord.md",
      "sha256": "0502aa43c672e7f8762394b22794214beed2ce03ea68ac208e3af81aedcb4f13",
      "bytes": 838
    },
    {
      "path": "characters/Jamukha.md",
      "sha256": "db6b0a68f12dc73e2946b1d29e65fe0012e395b2f4eccfbb22e51bda84f93e86",
      "bytes": 611
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "f32d05a0970481a6db00b6f2265927b030340d4303b9d67c069dbf7c3348448f",
      "bytes": 1291
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "13fc0138846ae01a78c373cb1d8a6bf30458912e0ef00cefb9e80c19c5cbdc85",
      "bytes": 1481
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "3e41eca8b8b8c5bb3cb6ee6f87b156b5b5104d121498911160eb21f4386352a4",
      "bytes": 622
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "5ccc74b7f5b2787c52387b5cf3025b0ee2fb2ccb7eba49f366d19dbd942f129c",
      "bytes": 778
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "0024ae00f563a576c2853725c8ba9d58c72c30d7ed34ef337186357d1b1f64fb",
      "bytes": 715
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "d9b1e22b9eb9b7a7d745d4d661bc9695939531ef3adc5ff138a6113d910e7516",
      "bytes": 888
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4ab770334cae05e602b597ac621bf33ba47f4c3e433b466c45967edfdcdd594f",
      "bytes": 271188
    }
  ],
  "estimated_tokens": 13039
}
-->

# Durable State Update — Chapter 977

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
1 and safe_through 977. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 977. Profile updates may replace only one
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
  "chapter": 977,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 977,
    "continuity_sources": [977],
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
    "The North Heaven Demon Lord is severely injured and cornered by the Bow Saint after failing to escape Jeok Cheongang and Jin Taekyung; what happens next is unknown.",
    "The conditions of Jin Mukyung, Cheol Mubaek, Wipeng, and Peng Cheolhu remain unknown.",
    "The Hebei Peng Family’s fate against the pill-enhanced Keshiks remains unknown.",
    "The Emperor remains gravely ill with Blood Soul Gu; the treatment said to require him to die once remains unresolved."
  ],
  "continuity_sources": [
    975,
    976
  ],
  "open_questions": [
    "What happens to the North Heaven Demon Lord now that the Bow Saint blocks his escape?",
    "What are the conditions of Jin Mukyung, Cheol Mubaek, Wipeng, and Peng Cheolhu?",
    "Can the Hebei Peng Family withstand the pill-enhanced Keshiks?",
    "Can the Emperor be treated for Blood Soul Gu, and what does the treatment requiring him to die once entail?"
  ],
  "safe_through": 976,
  "temporary_decisions": [
    "Render Taekyung’s mocking nickname 뽀삐 as “Poppy”; it is not an established name."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 무신     | **Martial God**               | —              |
| 궁성     | **Bow Saint**                 | —              |
| 삼성     | **Three Saints**    |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 정파     | **orthodox faction**                             |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 가주     | **Family Head**                              |
| 제자     | **Disciple**                                 |
| 산서     | **Shanxi**             |
| 정마대전   | **Great Faction War**         |
| 대사      | **Master** for a senior Buddhist monk                           |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 자무카 | **Jamukha** | Khan of the western grasslands and the steppe army’s practical leader. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 평화 | **Peace Guild** | Guild name. |
| 선천지기 | **innate qi** | Vital energy said to be damaged by the pill's aftereffects. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 여의주 | **dragon pearl** | Legendary treasure requested by Jang Taebo. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 쫄보 | **Coward** | Song associated with Won Myunghoon. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 계도 | **precept blades** | Blades carried by the Hundred and Eight Arhats. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 장성 | **Great Wall** | Wall used in the discussion of the Outer Lands. |
| 암기 | **hidden weapon** | Term used in Mungyeong's promise not to throw one. |
| 모용세가 | **Murong Family** | One of the Five Great Families, based in Liaoning. |
| 요녕 | **Liaoning** | Northeastern region from which the Murong Family arrives. |
| 서천 | **Western Heaven** | Short form used by the Lord of Heaven for the Western Heaven Demon Lord. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 북천 | **North Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 선비족 | **Xianbei** | People whose descendants ruled Liaoning and became one of the Five Great Families. |
| 요녕성 | **Liaoning Province** | Province ruled by the Murong Family. |
| 모용백 | **Murong Baek** | Former northern rival and later comrade of Peng Cheolhu. |
| 북천마군 | **North Heaven Demon Lord** | Title of Murong Baek. |
| 뽀삐 | **Poppy** | Taekyung’s mocking nickname for the North Heaven Demon Lord in this scene. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 서천마군 | 진태경 | hostile_opponents | you | calm and taunting | Uses 자네 while questioning Taekyung and offering to take him alive. |
| 진태경 | 서천마군 | hostile_opponents | Western Heaven Demon Lord | casual and defiant | Identifies the Demon Lord by title and answers his surrender demand with sarcasm. |
| 서천마군 | 신의 | hostile_invader_to_physician | Divine Physician | calm and mocking | Uses 신의 and 그대 while taunting the physician and dismissing his objections. |
| 신의 | 서천마군 | physician_to_invading_fiend | fiend | defiant and formal | Calls the Western Heaven Demon Lord an 악귀 and orders him to leave. |
| 서천마군 | 적천강 | hostile_invader_to_unconscious_patient | you | calm and predatory | Says someone wants to see Jeok Cheongang and attempts to move him with Seizing an Object Through Empty Space. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 서천마군 | hostile_opponents | you bastard | blunt and threatening | Jeok addresses the Western Heaven Demon Lord with 네놈 while defending Taekyung and ordering him not to touch his Disciple. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 적천강 | 남천마후 | legendary_martial_master_to_hostile_demon_empress | you bitch | blunt and threatening | Threatens to punish her and Lord of Heaven. |
| 남천마후 | 적천강 | hostile_demon_empress_to_legendary_martial_master | Fire King Jeok / you | flattering and mocking | Addresses Jeok Cheongang as the Fire King while praising Lord of Heaven. |
| 남천마후 | 천주 | devoted_servant_to_revered_master | Lord of Heaven | reverent and prayerful | The Southern Heaven Demon Empress prays that the Lord of Heaven will remember her loyalty and love. |
| 적천강 | 동천마군 | enemies | you | blunt and informal | Jeok Cheongang addresses the Eastern Heaven Demon Lord with hostile familiarity. |
| 동천마군 | 적천강 | enemies | you | informal | The Eastern Heaven Demon Lord speaks to Jeok Cheongang during their duel. |
| 진태경 | 동천마군 | young martial artist confronting an enemy | ugly-ass big bro | casual, profane, and taunting | Jin calls out to the Demon Lord after returning to the hall. |
| 동천마군 | 진태경 | enemy recognizing the spear wielder | Jin Taekyung | shouted, informal | The Demon Lord cries Taekyung's name after identifying him as the spear's owner. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 모용백 | 자무카 | commander_to_subordinate | you | plain and authoritative | Murong Baek gives Jamukha direct orders and rebukes him without honorific speech. |
| 자무카 | 모용백 | subordinate_to_commander_and_savior | you | deferential and honorific | Jamukha thanks Murong and addresses him with honorific speech. |
| 진태경 | 모용백 | adversaries | you | informal and confrontational | Directly asks whether Murong Baek beat up his older brother. |
| 모용백 | 진태경 | adversaries | you | informal | Addresses Taekyung directly during their confrontation. |
| 진태경 | 북천마군 | hostile opponents | you | casual, taunting, and profane | Taekyung teases and insults him during their standoff. |
| 적천강 | 북천마군 | former battlefield adversaries | you; you pup | blunt, familiar, and taunting | Jeok addresses him informally while challenging his alliance with Dark Heaven. |
| 북천마군 | 궁성 | hostile martial opponents | Bow Saint | calm and formally familiar | Addresses her directly while acknowledging her effort. |
| 북천마군 | 자무카 | lord to subordinate | my lord | formal-deferential | Jamukha answers the Demon Lord’s command with 하명하십시오. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 976
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Eastern Heaven Demon Lord.md

# Eastern Heaven Demon Lord (동천마군)

- **Safe through:** Chapter 973
- **Aliases:** Wei Zhong
- **Role:** The Eastern Heaven Demon Lord was Wei Zhong, the East Depot’s Seal-Holding Eunuch and a former Maoshan Sect disciple who commanded the dead with a bell; Jin Taekyung killed him with blue-white flames.
- **Personality:** His hatred grew from losing his family and sect, but recognizing his own lonely childhood in Zhu Bao ultimately moved him to relinquish his vengeance and choose a less harmful final act.
- **Voice:** He speaks in measured, almost lyrical phrasing, recounting the past before turning to pointed accusations.
- **Relationships:** Ma Sanbao is his Disciple; he holds the Emperor responsible for Taizu’s actions against the Maoshan Sect.

### Jamukha.md

# Jamukha (자무카)

- **Safe through:** Chapter 976
- **Aliases:** None
- **Role:** Jamukha was the ruler of the western steppe and a former eastern-steppe chieftain recruited into Dark Heaven by Murong Baek; Jin Taekyung killed him.
- **Personality:** Patient and ambitious, he was willing to feign loyalty to gain the power to rule the steppe and north.
- **Voice:** Not established
- **Relationships:** Peng Cheolhu defeated him more than fifty years ago; Murong Baek spared and recruited him, but Jamukha’s loyalty to him was feigned.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 976
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, remains Peng Cheolhu's rival, and once fought alongside Murong Baek, now his enemy.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 976
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor has appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and learning to trust his allies rather than carry every burden alone.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 976
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 972
- **Aliases:** None
- **Role:** An unidentified legendary martial artist regarded as a pinnacle above the Ten Kings; more than fifty years ago, he defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, Mae Jonghak received several teachings from him, and he left the Bow Saint a letter describing a chosen one; the Bow Saint says he chose her, while his identity, whereabouts, and possible connection to Cheon Taemin remain unknown.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 973
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress was Honglan, the creator of the rift behind the Inner Palace, and was killed after the rift closed.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 973
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃977화



수치심은 인간이라면 누구나 갖고 있는 수많은 감정 중 하나에 불과하지만, 느끼는 사람에 따라 그 크기는 천양지차로 달라진다.

어미의 뱃속에서부터 천대받는 노비에게 있어 수치심이 숙명과 다름없다면, 고귀하고 부유한 이들에게는 그 어떤 칼날보다 날카롭고 잔혹하게 마음을 헤집으니까.

그리고 북천마군은 명백한 후자였다.

“우리 뽀삐, 어딜 그렇게 헐레벌떡 뛰어가나 했더니 여기 있었어?”

걱정 가득한 표정과 목소리.

더불어 이러한 모습이 무색해질 만큼, 비뚜름하게 솟아오른 입꼬리.

“많이 걱정했잖아. 혹시 이대로 영영 잃어버리는 줄 알고.”

비웃음이 담긴 진태경의 한마디, 한마디를 들을 때마다 북천마군의 눈가가 파르르 떨렸다.

뻔히 놓여 있는 덫에 스스로 걸려든 것으로도 모자라, 이제는 숫제 집 나간 개 취급을 받는 상황.

지금 북천마군의 전신을 감싼 수치심과 절망감은, 지금껏 그가 단 한 번도 느껴 본 적 없는 무언가였다.

“네놈 따위가 감히…….”

“닥쳐라.”

아스라이 흩어지는 먼지구름 너머.

이어지려던 북천마군의 목소리를 가볍게 끊어 내며 나타난 적천강의 눈빛이 깊숙이 가라앉았다.

“어디서 함부로 주둥이를 놀리느냐. 네놈 따위가.”

북천마군은 이를 악물었다.

어째서일까.

어느덧 그의 눈동자에 비친 적천강의 모습은, 오래전 정마대전에서 보았던 그때처럼 크고 강렬하게 빛나고 있었다.

마치, 화왕(火王)이라는 거인 앞에서 은연중 위축되었던 과거의 자신을 떠올리게 할 만큼.

저벅.

유난히도 선명히 귓가에 울려 퍼지는 발소리.

그러나 북천마군을 향해 다가가던 적천강은 문득 걸음을 멈춘 채 실소를 흘렸다.

“족히 십보(十步)를 걸었음에도 도무지 거리가 좁혀지지 않으니, 꼭 귀신에 홀린 기분이로군. 그렇지 않으냐?”

스승의 물음에, 진태경이 짐짓 눈살을 찌푸렸다.

“에이, 그럴 리가요. 착각하신 거 아닙니까?”

“착각?”

“말이 안 되잖아요. 무슨 제자리걸음도 아니고, 왜 거리가 안 좁혀져요?”

턱을 긁적인 진태경이 천연덕스럽게 말을 이었다.

딱딱하게 굳은 얼굴을 한 북천마군을 힐끔 바라보며.

“어느 쫄보 새끼가 무서워서 뒷걸음질 쳤다면 또 모를까.”

“……!”

“어, 이게 맞나? 진짜로?”

으득.

살갗이 찢어지고 피가 흐른다.

입술이 터지도록 이를 악문 북천마군은 본능적으로 뒷걸음질 친 자신의 다리를 내려다보았다.

아니, 어쩌면 그가 시선을 돌린 이유는 비웃음으로 가득한 저 핏덩이의 얼굴을 마주할 자신이 없어서였는지도 몰랐다.

이렇게라도 하지 않는다면, 정말 마지막 남은 이성의 끈마저 놓아 버릴 것 같았으니까.

“이야, 진짜였네. 조금 전에는 약 좀 빨았다고 온갖 있는 척에 개지랄을 다 떨더니.”

비아냥과 함께 또다시 성큼 가까워지는 발걸음.

그러나 이번만큼은 북천마군도 물러서지 않았다.

아니, 물러설 수 없다는 것이 옳았다.

사박.

앞을 가로막은 두 스승과 제자와는 달리, 등 뒤에서 울려 퍼지는 발걸음 소리는 깃털처럼 가볍다.

반쯤 신형을 돌려세운 북천마군의 시야에 산들바람처럼 다가오는 한 여인의 모습이 비치고 있었다.

‘궁성.’

진퇴양난. 사면초가.

그 어떤 표현으로도 지금의 상황을 담기에는 역부족이다.

무려 세 명의 초절정 고수.

그중 한 사람은 천하에 모르는 이가 없는 삼성(三星)의 일원이며, 또 다른 하나는 그런 그녀와 어깨를 나란히 하는 늙은 제왕(帝王)이며, 마지막으로는 늙은 제왕의 가르침을 여의주 삼아 하늘로 솟구쳐 오르는 젊은 신룡(神龍)이 있다.

‘이럴 수는, 이럴 수는 없는데.’

공허한 마음 한구석에서 홀로 내뱉은 뇌까림.

그러다 어느 순간, 떨림이 잦아든 북천마군의 눈동자가 깊숙이 가라앉았다.

“오늘, 이 자리에서 나를 쓰러트린다고 해도 달라지는 것은 아무것도 없다.”

진태경이 망설임 없이 되물었다.

“너네 혹시 대사 암기하고 다니냐? 토씨 한 글자라도 틀리면 일주일 동안 공력 압수. 뭐 그런 벌칙 있어?”

“무슨 말을 하더라도 상관없다. 그것만이 유일한 진실이니까.”

“그런 것치고는 지금까지 꽤 잘 막아 낸 것 같은데. 오늘도 포함해서.”

진태경의 대답을 들은 북천마군은 자신도 모르게 피식 실소를 흘렸다.

“너희가 그렇게 믿는다면, 그래. 계속해서 희망을 품는 것도 나쁘지는 않겠지.”

“뭐?”

“이런 상황에 처하고 나니 문득 그런 생각이 들더군. 서천마군이, 남천마후가, 그리고 동천마군이 왜 실패했을까. 오랫동안 준비했던 계획이 어찌하여 한순간에 수포로 돌아간 것일까.”

예상치 못한 그 말에 진태경이, 아니 모두가 얼굴을 굳혔다.

“무슨 말을 하고 싶은 것이냐.”

서늘한 음성.

당장이라도 산 채로 불태워 버릴 것 같은 기세로 묻는 적천강을 향해, 북천마군은 담담하게 입을 열었다.

“글쎄. 나도 모르겠군. 무슨 말을 하고픈 것인지.”

“놈……!”

“구태여 서두르지 말게, 화왕. 당신이 그리 재촉하지 않더라도 우리에게 남은 시간은 많지 않으니.”

마음을 비우니 목소리 또한 담담하다. 북천마군의 자신의 몸 안에 남아 있는 기운을 관조하며 말을 이었다.

“길어야 반년. 그것이 전부다.”

전쟁은 이미 시작되었다.

암흑 속의 절대자가 긴 잠에서 깨어난 그 날부터.

아니, 그보다 훨씬 전부터.

“십만마도(十萬魔道)와는 비교도 되지 않는 힘. 믿을 수 없는 권능. 새로운 하늘이란 바로 그분을 가리키는 것이다.”

북천마군이 입에 담은 ‘그분’이 누구를 뜻하는지 모르는 사람은 이 자리에 없다.

“천주(天主)…….”

혼잣말처럼 뇌까린 궁성이 맑은 눈을 들어 북천마군을 응시했다.

“그것이 생사고락을 함께한 동도를 저버리고, 천하를 배신한 이유였더냐.”

“동도? 지금 동도라고 했나?”

북천마군은 불현듯 너털웃음을 터트렸다.

동도(同道). 같은 길을 함께 걷는 이.

그 두 글자에 담긴 의미를, 그 무의미하고도 하잘것없는 가치와 지난날의 과거를 떠올리자 실소가 터져 나왔다.

“아무래도 나와 다른 세상을 살아온 모양이군. 하기야, 뿌리도 없이 심산유곡에 틀어박힌 채 천하를 등지고 살아오던 당신들이 무엇을 알겠나.”

붉게 충혈된 눈동자가 적천강과 궁성을 차례대로 스쳤다.

두 사람 모두 정마대전이 벌어지기 전까지는 이름조차 제대로 알려진 적 없던 기인이사(奇人異士)들.

그러나 북천마군은, 모용백은 달랐다.

그는 천하 오대세가의 일익인 모용세가의 직계로서 세상을 겪었다. 한 울타리 안에 공존하는 그들과 함께 암투를 치러야 했다.

“모두가 웃는 얼굴로 올바름을 논하면서도, 보이지 않는 칼날을 소맷자락에 감춰두었지. 그것이 너희가 말하는 동도인가? 이것이 정파인가?”

하늘 위에서 천하를 굽어보는 별들도 언젠가는 빛을 잃고 스러지는 법.

모든 것은 언젠가 늙고, 쇠한다.

무림인들의 세계도 마찬가지였다.

흐르는 시간 속에 어느덧 강호는 사라졌다. 차가운 무림만이 남았다.

협(俠)의 가치는 점차 흐릿해져 가고 있었고, 구파일방과 오대세가를 비롯한 정파 무림은 알력 다툼에 힘을 쏟았다.

수많은 속가제자(俗家弟子)를 받아들여 산하의 문파를 늘리는 것은 예삿일이었다.

사파를 포섭하는 금기를 벌이는 이도 있었고, 암암리에 벌인 충돌 끝에 여러 사상자를 내기도 했다.

팽창의 끝은 결국 폭발.

그들이 오랜 세월 쌓아 올린 힘은, 곧 분쟁이라는 형태로 정파 무림을 갉아먹고 있었다.

그리고 그것은 중원(中原)에서 멀리 떨어진, 북방의 땅이라고 한들 예외일 수 없었다.

아니, 오히려 더욱 혹독했다.

적어도 모용세가에게는.

“당신들도 모른다고 하지 않겠지. 내가, 아니 우리 모용세가가 어떠한 뿌리를 지녔는지.”

북천마군은 발아래에 고여 있는 피 웅덩이를 내려다보았다.

명문대파의 가주로서 살아온 일생을 증명하듯, 그에 어울리는 권위와 힘이 느껴지는 준수한 용모.

그러나 모용세가가 요녕성에 뿌리내린 지 오랜 세월이 지났음에도, 여전히 그의 혈관에 흐르는 이방인의 특징은 흐릿하게나마 남아 있었다.

누군가로 하여금, 숨이 끊긴 채 쓰러져 있는 자무카의 얼굴을 언뜻 떠올리게 할 만큼.

“유목민?”

혼잣말처럼 흘러나온 진태경의 뇌까림에, 본능처럼 힘이 들어간 북천마군의 주먹이 하얗게 물들었다.

수도 없이 들었던 말이다.

보이지 않는 곳에서, 끊임없이 들려오던 손가락질과 목소리들은 여전히 그의 눈과 귀에 남아 있다.

유목민. 침략자. 이방인.

그리고, 오랑캐.

먼 과거, 모용선비(慕容鲜卑)라 불리던 동북의 이민족들은 대륙의 끄트머리를 차지했고 일국을 세웠다.

난세였다.

다섯 이민족과 열여섯 개의 소국이 난립했으니.

그러나 분열되었던 천하는 안정을 되찾았고, 혼란을 틈타 돌격창과 각궁으로 대륙을 질타했던 침략자들은 장성 너머로 쫓겨나거나 흡수되었다.

모용선비족은 후자였다.

그들은 요녕성에 남아 새로이 초석을 다졌고, 그렇게 세가(世家)의 기틀을 세웠다.

모용세가의 탄생이었다.

오랑캐의 피를 이어받은 침략자들의 가문.

고절한 무공과 뛰어난 기마술로 무림의 거목이 되어 우뚝 섰으나, 구파일방과 오대세가라는 또 다른 거목들에게 보이지 않는 무시와 천대를 받았던.

“가끔 그런 생각이 들더군. 만약 정마대전이 일어나지 않았다면, 모용세가가 지금까지도 살아남을 수 있었을지.”

팽창의 끝은 폭발이지만, 상상치도 못했던 거대한 폭발의 끝에는 화해와 평화가 남는다.

마교라는 외적의 등장은 그렇게 모든 것을 뒤바꾸었다.

살아남기 위해서는 모두가 힘을 합쳐 함께 싸워야 했고, 무신(武神)을 중심으로 탄생한 무림맹은 반목하던 정파 무림을 하나로 뭉치게 만들었으니.

그러나 모용백은, 모용세가는 잊지 않았다.

똑똑히 기억하고 있었다.

“협(俠)도, 인의(仁義)도 더는 없다. 오랜 세월 끝에 살아남는 것은, 결국 강자뿐이다.”

약육강식(弱肉强食).

오직 그것만이 북천마군이 깨달은 이 세상의 본질이다.

폭력으로 세워진 무림의 유일한 가치이며, 목적이었다.

그렇게 모용백은 북천마군이 되었다.

“그래서였다. 오직 그뿐이었다.”

드득. 드드득.

지면으로 퍼져 나가는 거센 진동.

더는 충혈되었다고 표현할 수 없을 정도로 붉게 물든 핏빛 안광(眼光)을 흩뿌리며, 북천마군은 협곡 안의 모두를 향해 부르짖었다.

“한데 감히 누가! 그 어떤 위선자가 나를 비난할 수 있단 말인가!”

콰아아!

창노한 외침에 실린 공력이 막강한 음파(音波)가 되어 터져 나왔다.

실로 가공할 만한 기세.

석상처럼 굳어 있던 산서인들의 귓가에서 피가 흘렀다. 외침을 들은 것만으로도 내부가 진탕된 몇몇 이들은 토혈(吐血)까지 하며 무릎을 꿇었다.

우우웅.

한 사람을 중심으로 요동치는 무시무시한 힘.

극심한 부상을 입었음에도 온 사방의 공기를 저릿하게 조여드는 그의 거대한 기파(氣波)에, 적천강은 북천마군이 이미 돌아올 수 없는 강을 건넜음을 깨달았다.

선천지기(先天眞氣).

앞서 저승으로 떠난 암천의 수괴들이 그러하듯이, 이 순간의 북천마군 또한 자신에게 주어진 모든 것을 불태우고 있었다.

그 끝에 죽음이 있으리라는 사실을 알면서도.

“물러나라면, 물러나겠느냐.”

적천강의 입술 사이로 흘러나온 나직한 음성에, 그의 제자는 말없이 손을 뻗었다.

쐐애액, 탁.

등 뒤에서 화살처럼 쏘아진 창 자루가 단단한 손아귀에 잡힌다. 곧이어 투명하리만치 맑은 창날 위를 휘감으며 솟구친 청백색의 불꽃은, 무언의 대답이나 다름없었다.

“개소리를 하도 오랫동안 들었더니 삭신이 쑤시네요.”

“새파란 놈이 삭신은 무슨.”

피식 웃는 적천강을 따라, 진태경도 웃었다.

“먼저 갑니다. 두 분은 천천히 따라오세요.”

그와 동시에, 진태경의 발끝에서 흙과 바위가 바스라졌다.

콰득, 퍼어엉!

거미줄처럼 갈라지는 지면. 그리고 쏘아지는 한 줄기의 불꽃.

그 어느 때보다 빠르고 강렬한 기세를 흩뿌리며 나아가는 신룡의 뒤를 따라, 두 노괴의 신형이 흐릿해졌다.

팟.

순식간에 지워지는 거리 속에서, 시뻘건 혈광이 솟구쳤다.
```

## Final English reading copy

```markdown
# Chapter 977

Shame was only one of the many emotions every human being felt, but its weight varied enormously from person to person.

For a slave scorned from the moment they were in their mother’s womb, shame might be no different from fate. For the noble and the wealthy, it could tear at the heart more cruelly and sharply than any blade.

And the North Heaven Demon Lord was very much the latter.

“Our Poppy! I was wondering where you’d run off to in such a panic. There you are.”

A face and voice full of concern.

And a smile whose lopsidedly raised corners made that concern look all the more absurd.

“I was so worried. I thought I might’ve lost you for good.”

With every mocking word Jin Taekyung spoke, the North Heaven Demon Lord’s eyelids twitched.

As if it weren’t bad enough that he’d walked into an obvious trap of his own accord, now he was being treated like a dog that had run away from home.

The shame and despair wrapping around the North Heaven Demon Lord’s entire body were unlike anything he had ever felt before.

“How dare a nobody like you—”

“Shut up.”

Beyond the faintly scattering cloud of dust, Jeok Cheongang appeared. His gaze sank deep as he cut off the North Heaven Demon Lord’s voice.

“Who do you think you are, running your mouth like that? You’re a nobody.”

The North Heaven Demon Lord gritted his teeth.

Why was this happening?

Somehow, Jeok Cheongang’s figure in his eyes had grown large and blazed as fiercely as it had long ago, during the Great Faction War.

As if he were looking once again at his former self, unconsciously shrinking before the giant known as the Fire King.

*Step.*

The sound of footsteps rang unusually clear in his ears.

But Jeok Cheongang, walking toward the North Heaven Demon Lord, suddenly stopped and let out a short laugh.

“I’ve walked a good ten paces, yet the distance hasn’t closed at all. I feel like I’ve been bewitched. Don’t you?”

At his Master’s question, Jin Taekyung furrowed his brow as if puzzled.

“Come on, that can’t be right. Maybe you’re imagining it?”

“Imagining it?”

“That makes no sense. It’s not like you’re walking in place. Why wouldn’t the distance get smaller?”

Scratching his chin, Jin Taekyung continued as casually as could be, glancing at the North Heaven Demon Lord’s stiff face.

“Unless some coward got scared and started backing away.”

“……!”

“Oh, wait. Is that it? Seriously?”

*Crack.*

The skin split and blood flowed.

The North Heaven Demon Lord clenched his teeth until his lips burst, then looked down at his own legs, which had instinctively stepped backward.

Or perhaps he’d looked away because he couldn’t bear to face that bloodied brat’s mocking expression.

If he didn’t do at least that much, he felt he might truly lose the last thread of reason he had left.

“Wow, it really was true. A minute ago, you were acting all high and mighty and throwing a damn fit just because you’d taken a pill.”

With that taunt, Jin Taekyung’s footsteps once again drew nearer, one confident stride at a time.

But this time, the North Heaven Demon Lord didn’t retreat.

No—that wasn’t it. He couldn’t retreat.

*Shhk.*

Unlike the master and disciple blocking his path, the footsteps behind him were light as feathers.

The North Heaven Demon Lord half-turned, and in his field of vision appeared a woman approaching like a gentle breeze.

*The Bow Saint.*

Caught between them. Surrounded on all sides.

No expression could begin to describe the situation.

Three Supreme Peak masters.

One was a member of the Three Saints, known to all under heaven. Another was an old sovereign who stood shoulder to shoulder with her. And the last was a young Divine Dragon, soaring toward the heavens with the dragon pearl of that old sovereign’s teachings in his grasp.

*This can’t be happening. It can’t.*

The words slipped out alone from a hollow corner of his heart.

Then, at some point, the trembling in the North Heaven Demon Lord’s eyes subsided. His gaze sank deep.

“Even if you defeat me here today, nothing will change.”

Jin Taekyung shot back without hesitation.

“Do you people go around memorizing speeches or something? Is there some kind of punishment if you get even one word wrong? Like losing your internal energy for a week?”

“Say whatever you want. It makes no difference. That is the only truth.”

“For something that won’t change anything, we’ve done a pretty good job stopping you so far. Today included.”

At Jin Taekyung’s reply, the North Heaven Demon Lord let out a short laugh without meaning to.

“If that’s what you believe, then so be it. There’s nothing wrong with holding on to hope.”

“What?”

“Being in this situation made me wonder. Why did the Western Heaven Demon Lord, the Southern Heaven Demon Empress, and the Eastern Heaven Demon Lord fail? How did a plan they’d spent so long preparing fall apart in an instant?”

At those unexpected words, Jin Taekyung’s face hardened. So did everyone else’s.

“What are you trying to say?”

Jeok Cheongang’s voice was cold.

Jeok Cheongang looked ready to burn him alive on the spot, but the North Heaven Demon Lord answered calmly.

“I don’t know. I’m not sure what I’m trying to say.”

“You bastard—!”

“Don’t rush, Fire King. Even if you don’t push me, we don’t have much time left.”

With his mind emptied, his voice was calm as well. The North Heaven Demon Lord looked inward, contemplating the energy that remained in his body, and continued.

“Half a year at most. That’s all.”

The war had already begun.

From the day the absolute ruler in the darkness awoke from a long slumber.

No—from much earlier than that.

“Power beyond anything the hundred thousand followers of the Demonic Path possessed. Unbelievable powers. ‘A new heaven’ refers to that person.”

No one here could mistake who the North Heaven Demon Lord meant by “that person.”

“The Lord of Heaven…”

The Bow Saint murmured to herself, then lifted her clear eyes to look at the North Heaven Demon Lord.

“Was that why you abandoned the comrades who shared life and death with you, and betrayed the world?”

“Comrades? Did you just call them comrades?”

The North Heaven Demon Lord suddenly burst into a hearty laugh.

Comrades. People walking the same path together.

The meaning held in those two words—their utterly worthless value and the past they called to mind—made him laugh in spite of himself.

“It seems you lived in a different world from me. Well, what could you possibly know, when you shut yourselves away in remote mountain valleys without roots, turning your backs on the world?”

His bloodshot eyes passed over Jeok Cheongang and the Bow Saint in turn.

Neither of them had been known by name before the Great Faction War. They had been eccentric, reclusive masters.

But the North Heaven Demon Lord—Murong Baek—was different.

As a direct descendant of the Murong Family, one of the Five Great Families, he had seen the world. He had to wage covert battles against others who shared the same orthodox fold.

“Everyone smiled and talked about righteousness, all while hiding invisible blades in their sleeves. Is that what you call comrades? Is this the orthodox faction?”

Even the stars looking down on the world from the heavens would one day lose their light and fade.

Everything grew old and withered in time.

The world of martial artists was no different.

As time flowed on, the martial world had disappeared. All that remained was the cold world of Murim.

The value of chivalry had grown dimmer and dimmer, while the orthodox faction—including the Nine Sects and One Gang and the Five Great Families—poured their strength into settling scores with one another.

It was commonplace for them to take in countless lay disciples and expand the sects under their control.

Some even committed the taboo of bringing the unorthodox faction into their fold. Others caused numerous casualties in clashes waged in secret.

Expansion could only end in an explosion.

The power they had accumulated over the years was now eating away at the orthodox faction in the form of conflict.

And the lands of the north, far from the Central Plains, were no exception.

If anything, it was worse there.

At least for the Murong Family.

“You can’t claim you don’t know, either. You know what kind of roots I—or rather, the Murong Family—have.”

The North Heaven Demon Lord looked down at the pool of blood gathered beneath his feet.

He had the handsome features and imposing presence of a man who had spent his life as the Family Head of a prestigious great house.

Yet even after all the years the Murong Family had been rooted in Liaoning Province, the faint traces of his foreign ancestry still flowed through his veins.

Enough to bring to mind, for a moment, the face of Jamukha lying dead.

“Nomad?”

At Jin Taekyung’s half-muttered question, the North Heaven Demon Lord’s fist tightened by instinct until his knuckles turned white.

He’d heard that word countless times.

The pointing fingers and voices from out of sight, always there, remained in his eyes and ears.

Nomad. Invader. Outsider.

And barbarian.

Long ago, the people of the northeast who were called the Murong Xianbei had occupied the edge of the continent and founded a nation.

It was a time of chaos.

Five foreign peoples and sixteen small kingdoms had struggled for supremacy.

But the divided land found stability again, and the invaders who had taken advantage of the turmoil to charge across the continent with spears and composite bows were either driven beyond the Great Wall or absorbed.

The Murong Xianbei were the latter.

They remained in Liaoning and laid new foundations there, establishing the framework of a great family.

The Murong Family was born.

A family of invaders descended from barbarian blood.

They had risen to become a towering force in Murim through their peerless martial arts and superb horsemanship. Yet the other towering forces—the Nine Sects and One Gang and the Five Great Families—had looked down on them and treated them with contempt, though never openly.

“Sometimes I wondered: if the Great Faction War had never happened, would the Murong Family have survived to this day?”

Expansion ended in an explosion, but the aftermath of an explosion beyond anyone’s imagination could leave reconciliation and peace behind.

The arrival of the Demonic Cult, an external enemy, changed everything.

To survive, everyone had to join forces and fight together. The Murim Alliance, formed around the Martial God, brought the feuding orthodox faction together as one.

But Murong Baek—and the Murong Family—hadn’t forgotten.

They remembered it all clearly.

“There is no more chivalry. No more benevolence or righteousness. In the end, after all these years, the only ones who survive are the strong.”

The strong prey on the weak.

That was the only truth of the world the North Heaven Demon Lord had learned.

The only value and purpose of Murim, built on violence.

And so Murong Baek became the North Heaven Demon Lord.

“That was why. Nothing else.”

*Rumble. Rumble.*

A powerful tremor spread across the ground.

The North Heaven Demon Lord’s eyes were now so red that “bloodshot” no longer described them. His blood-red gaze swept over everyone in the gorge as he roared.

“Who dares! What hypocrite has the right to condemn me!”

*BOOOOM!*

The force behind his aged shout exploded into a mighty sonic wave.

The aura was truly terrifying.

Blood flowed from the ears of the people of Shanxi, frozen like statues. Several who had been shaken to their cores by the roar alone coughed up blood and dropped to their knees.

*Vrrrrm.*

A terrifying power churned around one man.

Though gravely wounded, his immense aura squeezed the air all around him until it tingled. Jeok Cheongang realized the North Heaven Demon Lord had already crossed the point of no return.

Innate qi.

Just like the heads of Dark Heaven who had gone to the afterlife before him, the North Heaven Demon Lord was burning up everything he had been given in that moment.

Even knowing death waited at the end.

“If I tell you to back off, will you?”

At Jeok Cheongang’s quiet question, his Disciple wordlessly reached out.

*Whoosh—tap.*

A spear shaft shot from behind him like an arrow and was caught in his firm grip. Blue-white flames surged upward, winding around the almost transparent spearhead—a wordless answer.

“I’ve been listening to this bullshit for so long my whole body aches.”

“You’re too young to have aches all over.”

Jeok Cheongang gave a short laugh, and Jin Taekyung laughed along with him.

“I’ll go on ahead. You two can take your time catching up.”

At the same moment, dirt and rock crumbled beneath Jin Taekyung’s toes.

*Crack—BOOM!*

The ground split like a spiderweb. A streak of flame shot forward.

The two old monsters blurred, following the Divine Dragon as he charged ahead with greater speed and force than ever.

*Flash.*

Within the distance that vanished in an instant, a blood-red glow surged upward.
```
