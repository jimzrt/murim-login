<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0973.txt",
      "sha256": "8a00c90422cc943666fd005c3d48c25149c6a5762f43d1caa84e767f967d91be",
      "bytes": 13069
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b1fde8d56c3dcaddbe52eb31a215952d34c9889837af94efec5a9481fe3fa850",
      "bytes": 1155
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "65892110351fce017f8020b13720d8c5e71418799da1db239060ea308ecc01e4",
      "bytes": 235501
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "9c152fda06a0f7d118b9d66a47eb2a17c388f8cc4abb0599ea954baffd23724e",
      "bytes": 927
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "41e7b8dc9496123391d2d37d6e559b9031084c399ba200cd9940c4f0048357ae",
      "bytes": 759
    },
    {
      "path": "characters/Eastern Heaven Demon Lord.md",
      "sha256": "534d05620de0eca975f2fba4a99891cdd92f6d476b8bc3a3c273115278b28820",
      "bytes": 838
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "6bf329ee9c2fd2fecc82b9d7e05634e218142596005e0c12c0d8bb5ec623e6bf",
      "bytes": 1204
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "c950321ba043b402ca12f34eaa02265a427a1ad47c60defc477ee1334d471b5a",
      "bytes": 1405
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "9049eeaebc2bde5d377d790ae664a8057e2fd2d45051f45d9b95851d4821058b",
      "bytes": 1481
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "2eb97815a5a7a7a59f7657ac45f42ce5c41a552abf46bc9bdbb110176a6e6a82",
      "bytes": 622
    },
    {
      "path": "characters/Pung Yang.md",
      "sha256": "7c715fed390a0e32a59cbcb69076779d9822462e4861ddbd047e4bbd52012e61",
      "bytes": 1446
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "bb9ae4b4022180edeb952c60153a025a69ca72f39ca59d3f134670173f85941c",
      "bytes": 715
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "bcca92aa48fa2e8e8d2fc4664c30a2e8a4bfadc09ddd635c07252aa4a7ba8b8c",
      "bytes": 888
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4ab770334cae05e602b597ac621bf33ba47f4c3e433b466c45967edfdcdd594f",
      "bytes": 271188
    }
  ],
  "estimated_tokens": 12719
}
-->

# Durable State Update — Chapter 973

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
1 and safe_through 973. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 973. Profile updates may replace only one
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
  "chapter": 973,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 973,
    "continuity_sources": [973],
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
    "The North Heaven Demon Lord’s pill-enhanced power has not yet decided the battle; Jeok Cheongang and Jin Taekyung survived his attack unharmed, and the Bow Saint is still fighting.",
    "Jamukha has been ordered to commit all forces; he and the responding Keshiks have taken or are taking Temporary Strength Pills, and red heat haze is rising across the battlefield.",
    "The conditions of Jin Mukyung, Cheol Mubaek, and Wipeng remain unknown; Peng Cheolhu’s condition beneath the rubble remains unknown.",
    "The Emperor remains gravely ill with Blood Soul Gu; the treatment said to require him to die once remains unresolved."
  ],
  "continuity_sources": [
    972
  ],
  "open_questions": [
    "How will the North Heaven Demon Lord’s enhanced power affect the battle, and can the opposing forces withstand the mobilized fighters?",
    "What are the conditions of Jin Mukyung, Cheol Mubaek, Wipeng, and Peng Cheolhu?",
    "Can the Emperor be treated for Blood Soul Gu, and what does the treatment requiring him to die once entail?"
  ],
  "safe_through": 972,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 진무경    | **Jin Mukyung**    |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 궁성     | **Bow Saint**                 | —              |
| 암천     | **Dark Heaven**                  |
| 하북팽가   | **Hebei Peng Family**            |
| 무인     | **martial artist**                               | Default term                                          |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 가주     | **Family Head**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 시스템              | **System**                     |
| 산서     | **Shanxi**             |
| 노부      | **this old man / I**                                            |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 괴력난신 | **supernatural powers** | Term for extraordinary and unnatural powers. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 모용세가 | **Murong Family** | One of the Five Great Families, based in Liaoning. |
| 사냥개 | **hunting dog** | Jin's demeaning metaphor for Ares personnel who obey Go Jun. |
| 서천 | **Western Heaven** | Short form used by the Lord of Heaven for the Western Heaven Demon Lord. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 북천 | **North Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 케식 | **Keshik** | Elite warriors serving the Golden Clan. |
| 모용백 | **Murong Baek** | Former northern rival and later comrade of Peng Cheolhu. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진무경 | 풍양 | challenger_to_bandit_leader | Pung Yang | challenge-shout | Mukyung calls out Pung Yang by name to begin the confrontation. |
| 풍양 | 진무경 | enemy_to_enemy | you / little brat | condescending and taunting | Uses 네놈 and 어린놈 while threatening to sever Mukyung's limbs. |
| 진태경 | 풍양 | enemy_to_enemy | you pill-popping bastard | insulting-casual | Taekyung openly insults Pung Yang while announcing that he will use a pill too. |
| 풍양 | 진태경 | enemy_to_enemy | little brat; wet-behind-the-ears fledgling | condescending and taunting | Pung Yang dismisses Taekyung as an inexperienced child while challenging his ability to intervene. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
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
| 적천강 | 동천마군 | enemies | you | blunt and informal | Jeok Cheongang addresses the Eastern Heaven Demon Lord with hostile familiarity. |
| 동천마군 | 적천강 | enemies | you | informal | The Eastern Heaven Demon Lord speaks to Jeok Cheongang during their duel. |
| 진태경 | 동천마군 | young martial artist confronting an enemy | ugly-ass big bro | casual, profane, and taunting | Jin calls out to the Demon Lord after returning to the hall. |
| 동천마군 | 진태경 | enemy recognizing the spear wielder | Jin Taekyung | shouted, informal | The Demon Lord cries Taekyung's name after identifying him as the spear's owner. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 진태경 | 모용백 | adversaries | you | informal and confrontational | Directly asks whether Murong Baek beat up his older brother. |
| 모용백 | 진태경 | adversaries | you | informal | Addresses Taekyung directly during their confrontation. |
| 진태경 | 북천마군 | hostile opponents | you | casual, taunting, and profane | Taekyung teases and insults him during their standoff. |
| 적천강 | 북천마군 | former battlefield adversaries | you; you pup | blunt, familiar, and taunting | Jeok addresses him informally while challenging his alliance with Dark Heaven. |
| 북천마군 | 궁성 | hostile martial opponents | Bow Saint | calm and formally familiar | Addresses her directly while acknowledging her effort. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 911
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who directs its sorcerers’ seed experiments and prepares their deployment for the Lord of Heaven’s great cause.
- **Personality:** Confident, cruel, and controlling; readily kills subordinates who disappoint him, but restrains his violence when preserving valuable sorcerers serves Dark Heaven’s goals.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven and seeks to advance the Lord’s great cause; he regards the deceased Western Heaven Demon Lord and Southern Heaven Demon Empress as powerful allies whose deaths cost Dark Heaven, and considers Jin Taekyung and Cheongpung formidable adversaries.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 972
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Eastern Heaven Demon Lord.md

# Eastern Heaven Demon Lord (동천마군)

- **Safe through:** Chapter 971
- **Aliases:** Wei Zhong
- **Role:** The Eastern Heaven Demon Lord was Wei Zhong, the East Depot’s Seal-Holding Eunuch and a former Maoshan Sect disciple who commanded the dead with a bell; Jin Taekyung killed him with blue-white flames.
- **Personality:** His hatred grew from losing his family and sect, but recognizing his own lonely childhood in Zhu Bao ultimately moved him to relinquish his vengeance and choose a less harmful final act.
- **Voice:** He speaks in measured, almost lyrical phrasing, recounting the past before turning to pointed accusations.
- **Relationships:** Ma Sanbao is his Disciple; he holds the Emperor responsible for Taizu’s actions against the Maoshan Sect.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 972
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and says they have shared everything since he accepted him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 971
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Jin Mukyung is the second son of the Jin Family of Taiyuan, a Supreme Peak swordsman known as the Heaven Shaking Sword, and Commander of the Heaven Shaking Squad.
- **Personality:** Reserved and disciplined, Jin Mukyung is devoted to swordsmanship and guided by a strong sense of chivalry, refusing to abandon what he believes is right.
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Jin Wikyung is his older brother and the Lesser Family Head who formed the Heaven Shaking Squad in his honor; Jin Taekyung is his younger brother, whom Mukyung loves and wanted to become a brother worthy of his pride.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 972
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor has appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and learning to trust his allies rather than carry every burden alone.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 972
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Pung Yang.md

# Pung Yang (풍양)

- **Safe through:** Chapter 969
- **Aliases:** Red Wind Band Leader
- **Role:** Former leader of the Red Wind Band, commanding at least two hundred mounted bandits; became a mounted bandit at thirteen, reached First Rate by age thirty, and rose from squad leader to band leader three years ago; discovered the Crimson Blood martial arts and a case containing five Temporary Strength Pills in a hidden plateau tomb, reached the Peak realm in two years, and could temporarily manifest imperfect Sword Force and powerful Body-Protecting Qi by taking a pill; reached approximately seventy percent mastery of the Crimson Blood Twelve Sabers; after secretly incapacitating Jin Mukyung, resumed killing Mount Heng Sword Sect martial artists; was seriously injured by Taekyung's dagger, defeated One Annihilation, seized Taekyung, and was killed by Taekyung after the Unnamed Sword's Ten-Thousand-Year Cold Iron destroyed his Body-Protecting Qi and pierced his chest; had fled from the steppe and commanded nearly four hundred subordinates before his death
- **Personality:** Foxlike, ruthless, observant, controlled, and willing to kill subordinates who disobey his orders
- **Voice:** Calm, concise, and authoritative when issuing orders
- **Relationships:** Leads the Red Wind Band and controls former members of other mounted-bandit groups who joined his force

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 915
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress was Honglan, the creator of the rift behind the Inner Palace, and was killed after the rift closed.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 915
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃973화



불가항력이라는 단어는 누구에게나 통용된다.

추수보다 가뭄을 먼저 맞닥트린 농민에게도, 병석에 누워 시시각각 다가오는 죽음을 기다리는 병자에게도.

그리고 그들과 같은 인간이라고는 믿기지 않을 만큼 놀라운 힘을 지닌 어느 여인에게도 마찬가지였다.

‘막았어야 했는데.’

궁성은 침음성을 흘렸다.

아득한 높이의 암벽 위, 지상을 응시하는 그녀의 눈동자에 비친 것은 섬뜩한 혈광(血光)을 줄기줄기 뿜어내는 일단의 무리였다.

서걱! 콰드드득!

하나같이 붉게 충혈된 눈. 거침없이 나아가는 창칼을 따라 자욱하게 맺혀 가는 피 안개.

물경 수만여 명이 뒤얽힌 이 드넓은 전장에서 이백이라는 숫자는 한 줌에 불과했지만, 잠력단(潛力團)의 효능으로 저마다의 한계를 벗어난 그들의 존재는 그 무엇보다 위협적이었다.

이제는 불과 이천여 명밖에 남지 않은 하북팽가의 무인들에게는 더더욱.

크아아악!

밤공기를 뚫고 울려 퍼지는 처절한 비명.

마침내 하북팽가가 자랑하는 연환패왕진(連環覇王陣)을 깨트린 적들의 모습에, 궁성은 팽팽하게 당겨진 활시위를 내리며 입술을 깨물었다.

적들은 위협적일 뿐만 아니라 영리했다.

이미 몇 차례에 걸쳐 퍼부어진 궁성의 공격으로 극심한 피해를 입자 즉각 분산을 택했고, 곧장 아군의 중심을 파고들어 잇따른 추가 공격을 대비하고 있었으니.

‘이대로 공격을 계속한다면, 아군마저 휘말린다.’

물론 이백여 명의 케식들을 제외하고서라도 처리해야 할 적들은 지금 이 순간에도 차고 넘쳤다.

죽여도 죽여도 끝이 없는 초원의 대군세.

이미 몇 시진 째 이어지는 전투에서 산서인들과는 비교도 안 될 만큼 큰 손해를 본 것이 틀림없음에도, 아직도 이만에 달하는 병력이 남아 있다.

지금처럼 암벽 위의 고지를 점한 채 온 힘이 바닥날 때까지 화살 비를 퍼붓는다면, 막대한 타격을 입힐 수 있을 거라는 것쯤은 자명한 사실.

그러나 궁성의 앞에 놓인 선택지는 하나뿐이었다.

하나를 얻으면 하나를 잃는 법.

이대로 공격을 계속한다면 수많은 적을 쓰러트릴 수는 있겠지만, 그때는 하북팽가의 무인들이 모조리 전멸한 후일 것이다.

뜻이 섰으니 더 이상의 망설임은 필요 없다.

‘나서야 한다. 내가 직접.’

철컥.

거대한 활을 힘주어 비틀자 나타난 기이한 형태의 곡도(曲刀) 두 자루.

양 손아귀로 전해지는 서늘한 그 감촉과 함께, 궁성은 암벽을 박차고 하늘 높이 솟구쳤다.

솨아악.

전신을 스치는 차가운 밤바람에 섬단 같은 머리카락이 휘날렸다.

마치 보이지 않는 계단이 있기라도 한 듯, 연달아 텅 빈 허공을 밟으며 지상으로 향하던 그녀의 고개가 문득 등 뒤를 향했다.

강대한 기운의 파동에 휩싸인 비좁은 협곡 내부.

이제는 어둠에 파묻혀 보이지 않는 그곳에 있을 누군가에게, 그녀는 마음속으로 뇌까렸다.

‘살아남아라. 그리고 다시 한번 증명해 보아라.’

선택받은 자.

열화신룡 진태경.

무겁게 마음 한구석을 짓누르는 그의 이름과 함께, 궁성의 신형이 아득한 지상으로 내리꽂혔다.

슈확!

그녀의 양손에 들린 두 자루의 곡도가 예리한 바람이 되어 공간을 난도질했다.



* * *



궁성이 떠났다.

협곡 너머에 펼쳐진 또 다른 전장으로.

이곳에 남아 있는 나와 적천강이 아니라, 하북팽가의 무인들을 돕기 위해서.

그러나 저 멀리 허공을 가로질러 사라지는 그녀의 뒷모습을 보면서도 서운한 감정은 들지 않았다.

나와 시선이 마주친 적천강 역시 담담한 얼굴로 고개를 끄덕였을 뿐이다.

물론 이 자리에 있는 또 다른 누군가의 생각은 달랐겠지만.

“어느 정도 예상은 했지만, 새삼 놀라움을 금치 못하겠군.”

불쑥 입을 연 북천마군은 대답을 기다리지 않고 말을 이었다.

“너희는 왜 매번, 항상 어찌 이리 어리석은 선택만을 골라서 하는 것인지.”

헛웃음과 함께 고개를 내젓는 놈의 모습에, 나는 담담하게 대꾸했다.

“그렇겠지. 어차피 너 같은 새끼들은 수십 번을 죽었다 깨어나도 모를 테니까.”

자신을 따르는 수하들을 그저 승리를 위한 장기 말로 생각하는 북천마군은 결코 이해할 수 없을 것이다.

나를 비롯한 이 자리의 모두가 목숨을 걸고 싸우는 이유는, 누군가를 죽이기 위해서가 아니라 지켜내기 위함이라는 것을.

그리고 그 작은 차이가 정(正)과 마(魔)를 구분 짓는 가장 중요한 척도라는 것을.

“말세야, 말세. 모용세가의 가주라는 인간이 뒤통수나 까고, 좀 후달린다 싶으니까 약이나 빨아 재끼고. 안 그래요?”

내 물음에 적천강이 입을 열었다.

“오래 살다 보면 종종 짐승보다 못한 것들을 마주치게 되는 법이지. 거죽을 뒤집어쓰고 사람인 척 흉내 내는, 번드르르한 말과 웃음으로 시커먼 속내를 감춘 채 살아가는 놈들을.”

목소리는 서늘하고 안광은 뜨겁게 타오른다.

지금 이 순간. 적천강의 분노는 오롯이 북천마군을 향해 있었다.

“과거에는 그저 음흉한 구석이 있는 놈이라고만 생각했는데……. 이럴 줄 알았다면 차라리 그때 죽여 버릴 걸 그랬군.”

내게는 북천마군이지만, 적천강에게는 모용백이다.

일면식도 없는 나와는 달리, 일찍이 전우로서 함께 전장을 누빈 적 있는 두 사람의 시선이 허공에서 부딪혔다.

“왜 그러지 않았나. 화왕. 그것이 날 죽일 수 있는 처음이자 마지막 기회였을 텐데.”

비웃음 섞인 북천마군의 대답에 적천강의 눈동자가 깊게 가라앉았다.

“처음이자 마지막이라. 진정으로 그리 생각하느냐?”

“당신은, 아니라고 생각하나?”

드드드득.

지진이라도 난 것처럼 뒤흔들리는 공간 속, 북천마군의 전신에서 솟아오른 막강한 기세가 사방을 짓눌렀다.

적천강의 그것보다도 더욱 거칠고 거대한, 미증유의 기운이.

“지금부터 똑똑히 알려 주지. 두 번째 기회는 영영 찾아오지 않는다는 것을.”

모두의 귓가를 파고드는 나직한 한 마디와 함께, 북천마군의 신형이 사라졌다.

쉭.

희미한 파공성을 앞질러 나아가는 움직임.

그러나 나는 희미하게나마 볼 수 있었다. 아니, 느낄 수 있었다.

음속(音速)마저 뛰어넘어 쏘아지는 북천마군의 신형을.

공간을 가르며 휘둘려지는 놈의 창날과 주인의 뒤를 따라 달려드는 충성스러운 사냥개의 존재를.

슈확!

내리그어진 창날을 따라 뒤늦은 바람이 일어난 그 순간.

나는 상반신으로 파고드는 섬광을 향해 손에 쥐고 있던 백염을 쳐올렸다.

콰앙!

창과 창이 부딪히며 난 소리라고는 믿을 수 없는 굉음.

백염의 창날을 타고 발끝까지 전해진 어마어마한 압력에 지면이 거미줄처럼 갈라졌다.

가로막힌 창날 너머, 찰나의 순간 마주친 북천마군의 눈동자에서 들리지 않는 목소리가 귓가에 울려 퍼지는 듯했다.

‘너 같은 핏덩이가 어떻게?’

더없이 익숙한 눈빛이다.

크게 뜨인 눈동자도, 그 안에 담겨 있는 물음표도.

그리고 지금껏 나를 맞닥트린 수많은 적들은, 자신들의 눈빛에 실린 물음표의 여운이 사라지기도 전에 느낌표를 피워 올려야 했다.

바로 지금처럼.

카드드득!

이를 악물며 창대를 쳐올렸다.

터질 듯이 부풀어 오른 전신의 근육이, 나를 제외한 그 누구도 이해할 수 없는 괴력난신(怪力亂神)의 힘이 솟아올라 창날을 짓누르던 거대한 압력을 떨쳐 냈다.

콰아아앙!

굉음과 함께 눈을 부릅뜬 북천마군의 신형이 밀려난 바로 그 순간이었다.

주인보다 한발 늦게 목적지에 도달한 사냥개가 이빨을 드러낸 것은.

쐐액!

충격파로 일어난 먼지구름이 솟구치기도 전에 갈라진다.

공간을 격하고 섬광처럼 휘둘려진 곡도(曲刀)가 내 정수리를 파고들려던 찰나, 등 뒤의 공기가 뜨겁게 타올랐다.

화아악.

닿는 것만으로도 누군가의 살과 뼈를 녹이고, 영혼마저 불사를 것 같은 끔찍한 열기.

‘화염신장(火焰神掌).’

순식간에 부풀어 오르는 그 익숙한 기운을 느낀 순간, 나는 한 치의 망설임도 없이 고개를 숙였다.

퍼어어엉!

뒤통수를 아슬아슬하게 스쳐 지나가는 화염의 응집체.

타들어 간 것처럼 뜨거워진 뒤통수를 느끼며 다시 고개를 들었을 때, 한 마리의 맹수처럼 곡도를 내리긋던 늙은 유목민의 신형은 이미 세찬 속도로 튕겨 나가는 중이었다.

콰드드득!

발끝을 따라 이어지는 깊은 고랑.

삼 장에 가까운 거리를 물러난 늙은 유목민을 향해 적천강이 코를 킁킁거렸다.

“염병할. 어디서 말똥 냄새가 진동한다 했더니 웬 오랑캐 놈 때문이었군.”

“……!”

“네놈 표정이 제법 볼만하구나. 왜, 한바탕 화끈한 맛을 보니 말똥과 잡초로 가득한 초원으로 돌아가고 싶어졌느냐?”

폼은 일시적이나 클래스는 영원한 법.

적천강의 신들린 혀 드리블에 늙은 유목민의 얼굴이 딱딱하게 굳은 그 순간.

낮게 가라앉은 목소리가 울려 퍼졌다.

“여전하군. 남의 속을 뒤집어 놓는 그 혓바닥은.”

적천강을 향한 한 마디. 동시에 내게 못 박힌 시선.

그런 북천마군의 모습을 본 적천강이 내 어깨를 툭 쳤다.

“주둥이 놀리는 솜씨는 이놈이 노부보다 몇 수 위지.”

“쓸데없는 부분에서 스승을 넘어섰군.”

적천강이 피식 웃었다.

“글쎄. 단지 그뿐만이 아니라는 것쯤은 네놈도 알고 있을 터인데.”

북천마군은 대답 대신 이해할 수 없다는 듯한 눈빛으로 나를 바라보았다.

사실, 놈이 느끼는 저 감정은 당연한 일이었다.

비단 북천마군 뿐만이 아니라 누구나 마찬가지였다.

혈주도, 서천마군도, 남천마후와 동천마군도.

그리고 그 외의 또 다른 적들도.

그들에게 있어 내 존재는 어떤 식으로도 해석되지 않는 불가해(不可解)에 가까웠고, 지금껏 나를 거쳐 간 적들 중 누구도 답을 찾지 못한 그 의문은 시간이 흐를수록 더욱더 크기를 더해 갔다.

아니, 정확히는…….

‘내가 그만큼 강해진 거겠지.’

돌이켜 보면 지난 이 년 동안 수없이 겪었던 사건 속에서 벌어진 전투는 언제나 힘겨웠다.

적들은 항상 강했고, 나는 늘 그들보다 약했으니까.

살아남기 위해, 승리하기 위해 온 힘을 다해 발버둥 쳐야 했으니까.

하지만 그러던 어느 날 불현듯 깨달았다.

이토록 매번 생사의 기로를 오가는 이유는, 내가 약해서가 아니라 더욱더 강한 적들이 계속해서 나타났기 때문이라는 사실을.

어느 순간부터인가 나 역시 그들을 따라잡을 수 있게 되었다는 것을.

그토록 강대한 무위를 지녔던 대장로도, 진무경과의 합공으로 간신히 쓰러트릴 수 있었던 풍양도.

한 사람 한 사람이 악몽이나 다름없는 신위를 지녔던 암천의 마군(魔君)과 마후(魔后)들도.

매번 죽을 위기를 겪어야 했던 그들과의 전투를 머릿속으로 더듬어 보면, 문득 그런 생각이 들고는 했다.

‘그때. 그 순간, 이렇게 움직였다면 훨씬 수월하게 이길 수 있었을 텐데.’

이제야 알았다.

단순한 후회이자 미련이라고 생각했던 그것이, 내가 발전했다는 증거라는 것을.

단순히 시스템 창이 알려주는 수치를 떠나, 오롯이 한 사람의 무인(武人)으로서 성장했다는 확실한 지표였다는 것을.

그리고 어쩌면 이러한 성장은, 지금 이 순간에도 계속되고 있는지도 몰랐다.

“저기. 이건 그냥 개인적으로 궁금해서 묻는 건데.”

불쑥 입을 연 나는, 북천마군을 향해 조심스럽게 말을 이었다.

마치 어려운 과제를 낸 교수님을 향해 질문하는 학생처럼.

“조금 전에, 창을 위로 튕겨 내는 것보다 불알을 걷어차는 게 훨씬 더 나았겠지?”

그 순간, 교수님의 얼굴이 형용할 수 없을 만큼 일그러졌다.
```

## Final English reading copy

```markdown
# Chapter 973

The word *unavoidable* applied to everyone.

To farmers who faced drought before the harvest, and to the sick, lying in bed and waiting for death to draw closer by the moment.

And to a woman whose astonishing power made it hard to believe she was human like them.

*I should have stopped them.*

The Bow Saint let out a low groan.

High atop a sheer cliff, she stared down at the ground. Reflected in her eyes was a group of people spewing streams of ghastly blood-red light.

*Shhk! Krrrunch!*

Every one of them had bloodshot eyes. A thick mist of blood gathered in the wake of their heedlessly advancing spears and blades.

In this vast battlefield, where tens of thousands clashed, two hundred was only a handful. But thanks to the effects of the Temporary Strength Pill, each of them had broken past their limits—and they were more dangerous than anything else.

Especially to the Hebei Peng Family’s fighters, of whom only about two thousand remained.

*Graaaah!*

A harrowing scream rang through the night air.

As their enemies finally broke through the Hebei Peng Family’s vaunted Linked Tyrant King Formation, the Bow Saint lowered her taut bowstring and bit her lip.

The enemy was not only dangerous, but clever.

After suffering heavy losses from the Bow Saint’s attacks several times over, they had immediately split up. They had plunged straight into the heart of her allies’ formation to guard against her follow-up attacks.

*If I keep attacking like this, my allies will get caught in it too.*

Even without the two hundred or so Keshiks, there were more enemies than she could handle, and more appeared with every passing moment.

The steppe army seemed endless, no matter how many she killed.

The battle had already dragged on for several *shichen*. The steppe army had certainly suffered far greater losses than the people of Shanxi—and yet, nearly twenty thousand soldiers remained.

It was obvious that if she stayed on the high ground atop the cliff and rained arrows down on them until she ran out of strength, she could inflict tremendous damage.

But there was only one choice before her.

For every gain, there was a loss.

If she kept attacking, she could take down countless enemies. But by then, every last fighter of the Hebei Peng Family would be dead.

She had made up her mind. There was no need to hesitate any longer.

*I have to go. I have to do it myself.*

*Click.*

She twisted the enormous bow with all her strength. Two strangely shaped curved blades appeared.

Feeling their cool touch in both hands, the Bow Saint kicked off the cliff and soared into the sky.

*Whoosh.*

The cold night wind brushed her whole body, setting her long hair fluttering.

As if stepping on invisible stairs, she moved through the empty air toward the ground. Then she suddenly turned her head to look behind her.

Deep inside the narrow gorge, amid the waves of powerful qi, she silently addressed someone in a place now swallowed by darkness and hidden from view.

*Survive. Then prove yourself once more.*

The Chosen One.

The Blazing Flame Divine Dragon, Jin Taekyung.

With his name weighing heavily on her heart, the Bow Saint plunged toward the distant ground.

*Shwaa!*

The two curved blades in her hands became razor-sharp winds, carving through space.


* * *


The Bow Saint was gone.

She had left for another battlefield beyond the gorge.

Not to help me and Jeok Cheongang, who remained here, but to aid the Hebei Peng Family’s fighters.

Even as I watched her disappear far away across the open sky, I didn’t feel hurt that she’d left. Jeok Cheongang met my eyes and simply nodded, his expression calm.

Of course, there was someone else here who felt differently.

“I expected as much, but it still amazes me.”

The North Heaven Demon Lord spoke up out of nowhere, then continued without waiting for a reply.

“Why do you people always choose such foolish options? Every single time.”

He shook his head with a hollow laugh. I replied calmly.

“Sure. Guys like you would never understand, even if you died and came back dozens of times.”

The North Heaven Demon Lord thought of his followers as nothing more than pawns to secure victory. He could never understand that all of us here were risking our lives not to kill someone, but to protect someone.

And that the small difference between those two things was the most important measure separating the righteous from the demonic.

“What a rotten age. The Murong Family Head goes and stabs someone in the back, then starts popping pills the moment things get a little rough. Right?”

Jeok Cheongang spoke up in response to my question.

“If you live long enough, you’ll occasionally meet things worse than beasts. Creatures wearing human skin and pretending to be people, living with fine words and smiles while hiding the darkness in their hearts.”

His voice was cold, but his eyes burned hot.

At that moment, Jeok Cheongang’s anger was directed entirely at the North Heaven Demon Lord.

“I used to think you just had a sly streak… If I’d known it would come to this, I should have killed you back then.”

He was the North Heaven Demon Lord to me, but Murong Baek to Jeok Cheongang.

Unlike me, a man who had never met him before, Jeok Cheongang had once fought on battlefields alongside him as a comrade. The two men’s eyes met in midair.

“Why didn’t you, Fire King? That must have been your first and last chance to kill me.”

At the North Heaven Demon Lord’s mocking reply, Jeok Cheongang’s eyes sank.

“Your first and last, you say. Do you truly believe that?”

“You don’t?”

*Rrrrumble.*

The space around them shook as if an earthquake had begun. A mighty aura rose from the North Heaven Demon Lord’s whole body, pressing down on everything around him.

It was rougher and greater than Jeok Cheongang’s—an unprecedented force.

“I’ll make it clear to you now. You’ll never get a second chance.”

As his low voice sank into everyone’s ears, the North Heaven Demon Lord vanished.

*Swish.*

His movements outpaced even the faint whistle of his passage.

But I could see him, if only faintly. No—I could sense him.

The North Heaven Demon Lord’s figure shot forward, faster than the speed of sound.

I sensed his spearhead sweeping through space—and the loyal hunting dog rushing after its master.

*Shwaa!*

A belated gust of wind rose in the wake of the descending spearhead.

At that instant, I swung White Flame up toward the flash of light driving into my upper body.

*BANG!*

The roar was impossible to believe had come from two spears colliding.

The tremendous pressure traveled from White Flame’s spearhead to my toes. The ground split into a spiderweb of cracks.

Beyond the blocked spearhead, I met the North Heaven Demon Lord’s eyes for a split second. It felt as though an inaudible voice rang in my ears.

*How can a brat like you…?*

I knew that look all too well.

The wide-open eyes. The question mark within them.

And every enemy I’d faced up until now had to replace that question mark with an exclamation point before its echo had even faded.

Just like now.

*Ka-drrrk!*

I gritted my teeth and thrust the shaft of my spear upward.

The muscles throughout my body swelled as if they were about to burst. A power no one but me could understand—supernatural powers—surged up and shook off the tremendous pressure bearing down on the spearhead.

*KABOOOOOM!*

At the very moment the North Heaven Demon Lord’s eyes widened and his body was driven back by the thunderous crash, the hunting dog reached its destination a step behind its master and bared its teeth.

*Shwaek!*

Before the dust cloud kicked up by the shock wave could even rise, it split apart.

A curved blade swept through space in a flash, trying to split the top of my head. Then the air behind me flared with heat.

*Fwoosh.*

A terrible heat, as if a mere touch could melt someone’s flesh and bones and burn even their soul.

*Flame Divine Palm.*

The instant I felt that familiar energy swell, I ducked without a moment’s hesitation.

*Paaang!*

A mass of concentrated flame skimmed past the back of my head.

Feeling the back of my head grow hot, as if it had been scorched, I looked up again. The old nomad, who had been swinging his curved blade down like a beast, was already flying backward at tremendous speed.

*Krrrunch!*

A deep furrow stretched behind his heels.

Jeok Cheongang sniffed at the old nomad, who had been driven back nearly three *zhang*.

“Damn it. I was wondering where that horse shit smell was coming from. Turns out some barbarian wandered in.”

“……!”

“Your face is quite a sight. What, after getting a taste of that fiery welcome, do you miss the steppe, full of horse shit and weeds?”

Style may be temporary, but class is forever.

Just as the old nomad’s face went stiff at Jeok Cheongang’s inspired verbal assault, a low voice rang out.

“Still the same. That tongue of yours, always twisting people’s insides.”

One word for Jeok Cheongang. At the same time, the North Heaven Demon Lord’s gaze stayed fixed on me.

Jeok Cheongang tapped my shoulder.

“When it comes to running his mouth, this brat is several steps ahead of this old man.”

“He’s surpassed his Master in all the wrong ways.”

Jeok Cheongang let out a quiet laugh.

“Come now. You know it isn’t just that.”

The North Heaven Demon Lord said nothing. He simply looked at me with an expression that said he couldn’t make sense of me.

In truth, it was only natural that he felt that way.

And it wasn’t just the North Heaven Demon Lord. Anyone would.

The Blood Lord, the Western Heaven Demon Lord, the Southern Heaven Demon Empress, and the Eastern Heaven Demon Lord.

And all the other enemies I’d faced.

To them, my existence was an incomprehensible mystery, something they couldn’t make sense of no matter how they looked at it. Not one of the enemies I’d encountered had found the answer, and as time passed, the question had only grown.

No—more accurately…

*I’d gotten that much stronger.*

Looking back, every battle I’d fought amid the countless events of the last two years had been hard.

My enemies were always strong, and I was always weaker than they were.

I’d had to struggle with everything I had just to survive, just to win.

But then, one day, I suddenly realized something.

The reason I was constantly standing at the crossroads of life and death wasn’t that I was weak. It was that even stronger enemies kept appearing.

At some point, I’d started catching up to them.

The Head Elder, whose martial prowess had been so mighty. Pung Yang, whom I’d barely managed to defeat in a joint attack with Jin Mukyung.

The Demon Lords and Demon Empresses of Dark Heaven, each of whom had possessed power that made them nightmares all on their own.

When I traced back through those fights with the enemies who’d brought me to the brink of death time and again, I’d sometimes find myself thinking:

*Back then. If I’d moved like this in that moment, I could’ve won so much more easily.*

Now I understood.

What I’d thought was nothing more than regret and lingering misgivings was proof that I’d grown.

Beyond the numbers shown in the System window, it was a clear sign that I’d developed as a martial artist.

And maybe that growth was continuing even now.

“Hey. This is just something I’m curious about, so I’m asking.”

I spoke out of nowhere, then carefully directed my question at the North Heaven Demon Lord.

Like a student raising his hand to ask a professor about a difficult assignment.

“Wouldn’t it have been a lot better just now if I kicked you in the balls instead of knocking your spear up?”

At that moment, the professor’s face contorted beyond description.
```
