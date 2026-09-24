<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0986.txt",
      "sha256": "29e998edd21a2c6736a70a2d3d17f4aff4238ad25c7bd705442288acc3bed5ef",
      "bytes": 12608
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "7e667bda1a9fbd29fb9e7aa0f2861abb9f7debab904918d0947fd92835932b21",
      "bytes": 1212
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d13308fe31a2c64daebd8b79b1737ef2a4f6a2f6e86338670363f6d7acf5174f",
      "bytes": 236719
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "77bd8af664638bd8eebb1c6750e2b978c6c802da535d9ccc2d9fa23ba3bfd04a",
      "bytes": 927
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "df5ce9b3f04907f32cf47cb72a62914ca5c8d294d43bf7b8f97ba107dca7eb3c",
      "bytes": 1325
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "914e82535467ffebab677bad2699d5c504c30cec4c10b6b829dfa1ee979643c3",
      "bytes": 759
    },
    {
      "path": "characters/Heavenly Power Demon.md",
      "sha256": "098729c20bf2c92e7f584c680bc9d859c4046928aa2e2bb2fe42a64e263eb878",
      "bytes": 1018
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "97b66e708a6d7b445d259b7b5c1bc7138ddaa83e5a0149003da9d9befcd04123",
      "bytes": 1291
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "f543b87d05a2b40c51f20836a0f41fecf98175b4234df106b93811133772a46d",
      "bytes": 1479
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "724d1a461892d657c9222f652a5de17a9010c1d45bbd84817a3b09b71278c8bf",
      "bytes": 622
    },
    {
      "path": "characters/Murong Baek.md",
      "sha256": "f0364cb2051bbd6337d93d76bf5217d1385701fcd803b4b2e645cf42d9d789b7",
      "bytes": 660
    },
    {
      "path": "characters/Peng Cheolhu.md",
      "sha256": "ef7a776273999628fbb913960305ca769d4e952ba96450c4fba94631ca6f458f",
      "bytes": 898
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "94ad138f24aad806b86d9ad8e2d958a2dc46d0036f7af037e58ec62b81ad9c00",
      "bytes": 888
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "0383ccfd72d4fbc4b38d48993234603f14d1f5c66c449dca8bf366ced2819cb9",
      "bytes": 272663
    }
  ],
  "estimated_tokens": 12891
}
-->

# Durable State Update — Chapter 986

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
1 and safe_through 986. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 986. Profile updates may replace only one
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
  "chapter": 986,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 986,
    "continuity_sources": [986],
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
    "The Jin Family of Taiyuan is recognized as one of the Five Great Families; the fallen Murong Family is no longer among them.",
    "The System has granted Jin Taekyung a level-up, 10 bonus stat points, increased Fame, and the status of a feudal lord appointed by the Son of Heaven; Jin Wikyung and Jin Mukyung received undisplayed healing effects and bonus buffs.",
    "The Murong survivors’ innocence and whether they can rebuild as a household remain unresolved.",
    "A Murim Alliance envoy has arrived to deliver a message from the Alliance Leader to Jin Wikyung.",
    "Jeok Cheongang says someone wants to see Jin Taekyung."
  ],
  "continuity_sources": [
    984,
    985
  ],
  "open_questions": [
    "What is the Alliance Leader’s message to Jin Wikyung?",
    "Who wants to see Jin Taekyung?",
    "Why did Murong Baek suggest that the Western, Southern, and Eastern Heaven Demon Lords’ plans failed, and what did he mean by implying the situation may have been predetermined or that he was used?",
    "Why has Dark Heaven continued costly schemes without revealing its full strength?"
  ],
  "safe_through": 985,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 법왕     | **Dharma King**               | Hong Dao       |
| 벽력도왕   | **Thunderbolt Saber King**    | Peng Cheolhu   |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 구결     | **formula**                                      | Mnemonic/oral formula for a martial art               |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 마교     | **Demonic Cult**                                 |                                                       |
| 제자     | **Disciple**                                 |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 사천     | **Sichuan**            |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 도사      | **Daoist**                                                      |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 천력마 | **Heavenly Power Demon** | Formerly imprisoned Tang Clan criminal; distinct from 천력부, Heavenly Axe. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 모용백 | **Murong Baek** | Former northern rival and later comrade of Peng Cheolhu. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 약왕당 | **Medicine King Hall** | The Jin Family's medical hall. |
| 약왕당주 | **Medicine King Hall Master** | The unnamed physician who runs the Medicine King Hall. |
| 천자문 | **Thousand Character Classic** | Classical text Childeuk cannot complete. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 사천당문 | **Sichuan Tang Clan** | Martial clan cited for its poison-based cleansing method. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 성라대연 | **Star-Array Grand Banquet** | Major martial gathering held in Henan every two or three years. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 근골 | **Muscles and Bones** | System attribute increased by 2 during the climb. |
| 장유 | **Jangyu** | Martial artist eliminated during the fist-and-foot assessment. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 당문 | **Tang Clan** | Short form for the Sichuan Tang Clan. |
| 신력 | **divine strength** | Superhuman strength attributed to Taekyung. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 격체전공 | **Transmitting Internal Energy Across the Body** | Technique for transferring internal energy between bodies. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 도산검림 | **a mountain of sabers and a forest of swords** | Idiom describing the lethal life of martial artists. |
| 서천 | **Western Heaven** | Short form used by the Lord of Heaven for the Western Heaven Demon Lord. |
| 파리 | **Paris** | The city containing Ares Guild's branch attacked at the chapter's end. |
| 황도 | **Imperial Capital** | The capital where the imperial court resides. |
| 당주 | **Hall Master** | Murim Alliance office held by the envoy. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 적천강 | 벽력도왕 | rival_martial_master_to_rival_martial_master | Virility Saber King | insulting and taunting | Jeok coins 정력도왕 as a taunting replacement for the established title. |
| 벽력도왕 | 적천강 | rival_martial_master_to_rival_martial_master | Jeok Cheongang | boisterous and hostile-teasing | The Thunderbolt Saber King calls Jeok by name before their argument escalates. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 혈주 | 청풍 | hostile_opponent_to_newly_revealed_identity | Huashan's Invincible Divine Sword; Sword Saint's Disciple or grandson | mocking and taunting | Recognizes Cheongpung's public identity and needles him with his Sword Saint lineage while dismissing the added threat. |
| 진태경 | 천력마 | prisoner_feeder_to_prisoner | you | casual and mocking | Taekyung questions the Heavenly Power Demon and mocks him as the Kunlun Sect's public-pissing criminal. |
| 천력마 | 진태경 | prisoner_to_prisoner_feeder | you | gruff and self-possessed | The Heavenly Power Demon speaks of himself as 노부 while questioning Taekyung. |
| 서천마군 | 청풍 | commander_to_young_opponent | you | gentle and taunting | Uses 자네 while identifying Cheongpung and discussing the Blood Lord. |
| 서천마군 | 진태경 | hostile_opponents | you | calm and taunting | Uses 자네 while questioning Taekyung and offering to take him alive. |
| 진태경 | 서천마군 | hostile_opponents | Western Heaven Demon Lord | casual and defiant | Identifies the Demon Lord by title and answers his surrender demand with sarcasm. |
| 서천마군 | 신의 | hostile_invader_to_physician | Divine Physician | calm and mocking | Uses 신의 and 그대 while taunting the physician and dismissing his objections. |
| 신의 | 서천마군 | physician_to_invading_fiend | fiend | defiant and formal | Calls the Western Heaven Demon Lord an 악귀 and orders him to leave. |
| 서천마군 | 적천강 | hostile_invader_to_unconscious_patient | you | calm and predatory | Says someone wants to see Jeok Cheongang and attempts to move him with Seizing an Object Through Empty Space. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 서천마군 | hostile_opponents | you bastard | blunt and threatening | Jeok addresses the Western Heaven Demon Lord with 네놈 while defending Taekyung and ordering him not to touch his Disciple. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 벽력도왕 | 진태경 | elder martial master to younger rival | you | boisterous and confrontational | Peng addresses Taekyung as 네놈 while discussing Peng Dojin. |
| 적천강 | 의원 | interrogator_to_physician | you; quack | blunt and threatening | Jeok shakes the physician and demands an explanation for Jin's seven-day sleep before ordering him to summon the Beast Miao King. |
| 적천강 | 법왕 | close deceased friend and peer | you | familiar and reflective | Jeok addresses the Dharma King in private thought while wishing he were present to clarify Jeok's confusion. |
| 벽력도왕 | 모용백 | former rivals turned comrades and friends | Murong Baek; Family Head Murong | familiar and warm | Peng Cheolhu greets him by name and asks whether he should now use his family-head title. |
| 모용백 | 벽력도왕 | former rivals turned comrades and friends | you | familiar and cautionary | Murong Baek asks Peng Cheolhu whether he agrees that people like Jamukha require constant vigilance. |
| 진태경 | 모용백 | adversaries | you | informal and confrontational | Directly asks whether Murong Baek beat up his older brother. |
| 모용백 | 진태경 | adversaries | you | informal | Addresses Taekyung directly during their confrontation. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 973
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who directs its sorcerers’ seed experiments and prepares their deployment for the Lord of Heaven’s great cause.
- **Personality:** Confident, cruel, and controlling; readily kills subordinates who disappoint him, but restrains his violence when preserving valuable sorcerers serves Dark Heaven’s goals.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven and seeks to advance the Lord’s great cause; he regards the deceased Western Heaven Demon Lord and Southern Heaven Demon Empress as powerful allies whose deaths cost Dark Heaven, and considers Jin Taekyung and Cheongpung formidable adversaries.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 981
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak martial master known as the Huashan Divine Dragon, the creator of the snake-inspired Mimi Step footwork technique, and the master of the Azure Dragon Pavilion within the Alliance Leader's Two Dragons Pavilion.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi, now a large horned snake, to him, and Cheongpung is accompanying Mungyeong while learning his martial arts through observation to become stronger and adapt to this world.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 985
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Heavenly Power Demon.md

# Heavenly Power Demon (천력마)

- **Safe through:** Chapter 463
- **Aliases:** None
- **Role:** Deceased former Elder of the Great Heavenly Demon Divine Cult who led the subjugation of Qinghai and opened the first front of its holy war before transferring three jiazi of internal energy to Jin Taekyung and asking him to kill the Western Heaven Demon Lord.
- **Personality:** Quiet and self-possessed despite his severe imprisonment, he is reflective about the moral ambiguity of the Great Faction War and disillusioned with the Divine Cult's corruption.
- **Voice:** Gruff and dry, with formal self-reference as 노부.
- **Relationships:** He was once an Elder and commander under the Great Heavenly Demon Divine Cult's Cult Leader, has spent more than forty years imprisoned by the Sichuan Tang Clan, and identifies the Western Heaven Demon Lord as one of the Divine Cult's four Protectors who served closest to and led astray the Cult Leader.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 985
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, remains Peng Cheolhu's rival, and once fought alongside Murong Baek, now his enemy.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 984
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor has appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 984
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Murong Baek.md

# Murong Baek (모용백)

- **Safe through:** Chapter 985
- **Aliases:** North Heaven Demon Lord, Divine Spear of the Imugi
- **Role:** Murong Baek was the North Heaven Demon Lord, known as the Divine Spear of the Imugi; Jin Taekyung killed him after he burned his life to gain power.
- **Personality:** He coveted the dragon pearl and the chance to become a dragon, rationalizing his pursuit while choosing to seize what belonged to others.
- **Voice:** Not established
- **Relationships:** Jeok Cheongang and the Bow Saint fought him alongside Jin Taekyung, who delivered the killing blow.

### Peng Cheolhu.md

# Peng Cheolhu (벽력도왕)

- **Safe through:** Chapter 982
- **Aliases:** Thunderbolt Saber King
- **Role:** Peng Cheolhu is the Thunderbolt Saber King, a Ten Kings master and Great Hero of the Hebei Peng Family.
- **Personality:** Boisterous, hot-tempered, argumentative, and protective toward those connected to his close friend Hong Dao; relentlessly disciplined in training, having continued every day after the Great Faction War.
- **Voice:** Loud, blunt, confrontational, and prone to disguising embarrassment or retreat as serious martial instruction.
- **Relationships:** Long-standing rival and friend of Jeok Cheongang; close friend of Hong Dao; protective toward Hong Dao's Disciple Unnamed; father of Peng Cheolyeong; longtime friend and former youthful rival of Murong Baek, who has now betrayed and attacked him.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 985
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃986화



사실, 처음부터 어느 정도는 짐작할 수 있었다.

평소와는 전혀 다른 적천강의 무거운 표정과 어조.

그리고 착 가라앉은 그의 목소리에 묻어나오는 비통함은 화왕(火王)이라는 거인이 쉽게 보이지 않는 모습이었으니.

하지만…….

언제나 그렇듯이, 불길한 직감은 늘 빗나가는 법이 없다.

“오셨구려.”

가장 먼저 우리를 맞이한 인물은 문 앞을 지키고 있던 약왕당주였다.

도착과 동시에 봇짐을 챙겨 떠나는 그를 향해, 적천강이 나직한 목소리를 건넸다.

“당부했던 대로, 아무에게도 알리지 말아 주게.”

“…….”

“고맙네. 자넨 훌륭한 의원이야.”

아무런 대답 없이 살짝 고개를 숙인 약왕당주가 떠나자, 우리는 비로소 문 안에서 기다리고 있던 한 사람을 마주할 수 있었다.

“오, 생각보다 일찍 데려왔군. 워낙 다리가 짧은 늙은이라 앞으로 칠 주야는 더 걸릴 줄 알았는데.”

며칠 만에 정신을 차린 또 한 명의 거인.

가벼운 농담과 함께 껄껄 웃는 벽력도왕(霹靂刀王)을 말없이 바라보던 나는, 어깨를 툭 치는 적천강의 손길에 뒤늦게 포권을 취했다.

내가 할 수 있는 최선의 예의를 다해서.

“무림말학 진태경이 팽 대협을 뵙습니다.”

“아서라. 과한 겸손은 오히려 독이 되는 법. 네 녀석이 말학이면, 천하의 무림말학은 전부 뒈졌다더냐?”

나를 보며 흡족하게 웃은 벽력도왕의 시선이 적천강을 향했다.

“이제 보니 이 친구가 괜한 엄살을 떨었구먼. 날이 갈수록 위아래 없이 천둥벌거숭이처럼 날뛰는 녀석이라고 그렇게 투덜대더니만.”

“친구는 니미럴. 한참 어린놈이 웃어른한테 못하는 말이 없네.”

애써 평소처럼 퉁명스럽게 답하지만, 그럼에도 감출 수 없는 침잠한 눈빛.

그런 적천강의 모습을 아는지 모르는지, 벽력도왕의 웃음소리가 한층 더 커졌다.

“으허허. 뭐가 그리 억울해? 같이 늙어 가는 처지에.”

“네놈은 삼강오륜(三綱五倫)도 모르느냐? 장유유서 못 들어봤어?”

“그거 알면, 누가 대신 밥 먹여 주나? 아니면 무공이 더 강해져?”

“됐다. 무식하기 짝이 없는 팽가 놈이랑 이런 얘기를 하는 노부가 등신이지.”

“스스로의 부족함을 인정하는 모습, 보기 좋군. 쉰내 풀풀 풍기는 늙은이랑 대화하는 것도 슬슬 지겨워지던 참인데 잘됐어. 안 그러느냐?”

벽력도왕이 툭 던진 물음에, 내가 고개를 끄덕였다.

“뭐, 저희 스승님이 좀 늙긴 하셨죠.”

“뭐라? 으하하!”

쩌렁쩌렁한 웃음소리가 터져 나왔다.

벽력도왕의 창백한 안색과는 전혀 어울리지 않는, 그래서 억지로 쥐어 짜낸 것처럼 느껴지는 커다란 웃음소리였다.

‘아니, 분명 그렇겠지.’

나는 마음속으로 조용히 뇌까렸다.

당장 눈으로 보이는 것이 전부가 아니다. 느껴진다.

지금 이 순간에도 벽력도왕이 품은 기운은 위태롭게 흔들리고 있었다. 마치 곳곳에 금이 간 유리그릇처럼.

당장이라도 사그라질 불꽃처럼.

“저를 찾으셨다고 들었습니다.”

무거운 목소리로 꺼낸 한 마디에, 내가 자신의 상태를 알아차렸음을 직감한 벽력도왕이 웃음기 어린 얼굴로 입을 열었다.

“눈치 빠른 녀석 같으니. 확실히 마지막으로 보았을 때와 비교하면 천양지차로구나. 화왕이 다른 건 몰라도 제자 하나는 잘 키웠어.”

“…….”

“그리 죽상을 하고 있을 필요는 없다. 우리 같은 무림인에게 있어 살고 죽는 문제란 그런 것이니.”

맞다.

무림인의 삶이란 늘 그렇다.

그리고 숱한 위협과 암계가 도사린 도산검림(刀山劍林)을 일평생 헤쳐 나온 벽력도왕은, 담담하게 자신이 처한 현실을 받아들이고 있었다.

“참으로 긴 꿈을 꾸었다. 그 속에서 지난 일생을 되돌아볼 수 있었지. 물론 모용백, 그 친구의 젊을 적 모습도 오랜만에 봤고.”

“친구는 니미럴. 쳐죽일 놈이지.”

적천강이 툭 던진 그 말에, 피식 실소를 흘린 벽력도왕이 계속해서 말을 이었다.

“모두 지난 일이지. 어쩔 수 없는 일이야. 이미 엎질러진 물을 어찌 고스란히 주워 담겠나. 다만 결과적으로 암천의 흉계를 막고 더 많은 이들을 구할 수 있었으니 그것으로 족할 뿐.”

적천강만큼이나 불같은 성격으로 유명한 그는, 연못처럼 잔잔한 눈빛으로 나를 응시했다.

“성라대연(星羅大宴)에서 너를 처음 보았을 때, 머지않아 큰일을 해낼 녀석이라는 것을 직감했다. 검성의 제자와 함께 천하를 지켜 낼 동량이라는 것을 모두가 느낄 수 있었지.”

물론 그때만 해도 나는 미숙했다.

지금처럼 숱한 강자들과 어깨를 나란히 하지도 못했고, 혈주(血主)라는 괴물에 의해 처참하게 무너지기도 했다.

“하지만, 이토록 빨리 성장할 줄은 그 누구도 짐작하지 못했지.”

죽음의 위기는 몸집을 부풀리며 연이어 찾아왔고, 그로 인한 성장은 가팔랐다.

가장 가까이에서 나를 지켜본 이들조차 눈을 의심할 만큼.

“그것이 곧장 너를 찾은 이유다. 내게 얼마 남지 않은 시간과 기운을 가장 값지게 쓸 수 있는 마지막 기회이기도 하지.”

“……그 말씀은.”

“평범한 호랑이는 죽어서 가죽을 남긴다지만, 하북의 대호(大虎)는 다를 것이다.”

입가에 희미한 미소를 띤 벽력도왕의 모습에, 나는 뒤늦게나마 깨달을 수 있었다.

며칠 만에 겨우 정신을 차린 벽력도왕이, 죽음을 코앞에 둔 그가 왜 자신의 혈육이 아닌 나를 먼저 찾았던 것인지.

“가져가거라. 노부에게 남은 모든 것을.”

벽력도왕의 담담한 목소리가 울려 퍼진 그 순간.

띠링.



돌발 퀘스트, [격체전공(隔體傳功)]이 생성되었습니다.

!!경고, 경고!!

해당 퀘스트의 진행 과정에 있어 극도의 위험성이 동반됩니다.

돌발 퀘스트를 수락하시겠습니까?

Y / N



나는 맑은 종소리와 함께 떠오른 홀로그램 창 너머, 웃고 있는 벽력도왕의 얼굴을 말없이 바라보았다.

그리고 문득, 입을 열었다.

“왜, 왜 하필 저를 선택하신 겁니까?”

돌아오는 대답에는 일말의 망설임도 없었다.

“믿고 있으니까.”

“……!”

“나 한 사람만의 믿음이 아니다. 법왕(法王)이, 네 스승이, 이제는 온 천하가 너를 믿는다.”

숨이 막혔다.

심장이 조여들고 혈류가 빠르게 솟구치는 듯했다.

그 사이에서, 벽력도왕의 목소리가 또렷하게 귓가로 전해졌다.

“이 모든 것은 네가 아닌 천하를 위한 것. 그 이상의 이유가 더 필요하느냐?”

“아닙니다.”

작게 심호흡한 내가 말을 이었다.

“그것으로 충분합니다.”

벽력도왕의 파리한 안색 위로 웃음이 스쳤다.

“가부좌를 틀어라.”

띠링.



- 돌발 퀘스트, [격체전공]을 수락하셨습니다!



* * *



공력(功力)은 세상 어디에나 존재하는 무형의 기운이다.

무공을 익힌 이들은 이 공력을 신체 내부에 쌓아 육신과 정신을 더욱 강건하게 가다듬고, 인간의 한계를 벗어난 초인의 영역에 발을 딛기 위해 고된 수련을 반복한다.

그러나 누구나 그런 힘을 원하는 것은 아니었다.

몸 안에 축적된 기운이 커질수록, 그로 인한 후폭풍의 크기 역시 비례하여 부풀어 오르니까.

잘못된 구결을 따라 공력을 무리하여 운용했다가는 불구가 되기에 십상이요, 깨달음을 얻지 못하고 심마(心魔)에 빠져 반쯤 미치광이가 되는 경우도 허다하다.

하지만 그럼에도 불구하고, 더욱 드높은 경지를 갈망하는 무림인들의 욕구는 좀처럼 사그라지지 않았다.

철저한 약육강식의 세계.

그들은 보다 안정적으로, 빠르게 강해지기 위해 온갖 발상을 떠올렸고 그 과정에서 한 가지 놀라운 방법을 찾아낼 수 있었다.

‘오랜 세월에 걸쳐 공력을 쌓는 것이 아니라, 누군가에게 고스란히 넘겨받는다면?’

‘죽음을 목전에 둔 노고수의 힘을 이어받아? 엥? 이거 완전히 석청 아니냐?’

아득한 과거, 격체전공(隔體傳功)은 그렇게 탄생했다.

그리고 탄생과 동시에 결코 행동에 옮겨서는 안 되는 금기(禁忌)가 되었다.

이유는 간단했다.

겉보기에만 달콤했을 뿐, 실상은 양날의 검이었으니까.

아니, 양날의 검이라고 표현하는 것조차 우스울 정도로 실패한 사례가 압도적으로 많았으니까.

‘스, 스승님!’

‘안 돼!’

죽고, 죽고, 또 죽었다.

천운으로 살아남았다 하더라도 기혈이 뒤엉켜 폐인이 되거나 본래의 무위를 영영 되찾을 수 없었고, 그 과정에서 당대를 주름잡던 초절정 고수들과 뛰어난 후기지수들을 잃어야 했다.

그렇기에 벽력도왕이 진태경에게 격체전공하겠다는 뜻을 밝히자, 적천강은 반사적으로 되물을 수밖에 없었다.



‘미쳤나?’

‘전혀.’

‘아니, 미친 게 확실해. 예전 같았으면 이쯤에서 길길이 날뛰었을 테니.’

‘내 비록 깨어난 지 반 시진밖에 안 됐지만, 머릿속은 터무니없이 맑아. 일평생 이 정도로 총명했던 적이 있었나 싶을 정도니까.’

‘그거참 빌어먹게 축하할 일이로군. 그럼 이제 겨우 천자문을 뗄 수 있게 된 건가?’

‘흰소리는 집어치우게. 이게 마냥 미친 짓이 아니라는 것쯤은 자네도 알고 있지 않나.’



사실, 벽력도왕의 말이 맞았다.

적천강도 처음에만 반사적으로 그렇게 대꾸했을 뿐, 마음속으로는 이 미친 짓거리가 얼마나 가능성이 있는 일인지 가늠하고 있었으니까.



‘인정하기는 싫지만, 자네의 그 잘난 제자라면 격체전공을 감당할 수 있을 걸세. 청풍 그 아이와 함께 천무지체(天武肢體)라는 천운을 타고난 녀석 아닌가.’

‘……천무지체라.’

‘그뿐만이었다면 나도 이런 이야기를 하지 않을 걸세. 녀석은 하늘이 내린 근골에, 무인으로서 지닌 역량과 깨달음의 깊이도 충분해.’



아마 몇 달 전이었다면, 적천강은 그 어떤 강권에도 제자의 목숨을 위태롭게 만드는 이 제안을 받아들이지 않았을 것이다.

설령 그 제안을 한 이가, 수십여 년간 미운 정을 쌓아 온 끝에 죽음을 목전에 둔 벽력도왕이라 할지라도.

하지만 진태경에게 직접 진실을 전해 들은 적천강은 달랐다.

‘가능성이 있다. 아니, 충분해.’

기나긴 무림사에서도 유례가 없었던, 경지에 오른 두 초절정 고수 간의 격체전공.

거기에 더해 천무지체라고밖에 여길 수 없는 초인의 육신을 가진 진태경에게는, 또 하나의 기이한 힘이 존재했다.

뇌반업(牢倍業).

육신을 정화하고, 부상마저 회복시킬 수 있다는 신력(神力).

그 힘만 있다면, 목숨이 붙어 있는 한 기회는 있다.

더군다나…….

‘이미 녀석은 격체전공에 한 번 성공한 전력이 있다.’

적천강도 뒤늦게서야 들었던 이야기였다.

진태경이 사천당문의 지하 뇌옥에 갇혀 있던 마교의 대마두, 천력마(天力魔)의 공력을 받아 서천마군을 쓰러트렸다는 것은.

처음 그 얘기를 들었을 때는 제자가 죽을 뻔했다는 사실에 심장이 터질 만큼 놀랐지만, 그 당시와 지금의 차이는 명백했다.

위급했던 상황도. 진태경이 한 사람의 무인으로서 이룩해 낸 무위도.

‘할 수 있다. 아니…….’

해낼 것이다.

반드시.

굳은 의지로 흔들리는 마음을 다잡은 적천강은, 깊게 가라앉은 눈빛으로 거궐혈(巨闕穴)을 통해 맞닿은 두 사람을 바라보았다.

화아아악.

미증유(未曾有)의 공력이, 사방으로 흘러넘치고 있었다.
```

## Final English reading copy

```markdown
# Chapter 986

Truth be told, I’d had a pretty good idea from the start.

The heaviness in Jeok Cheongang’s expression and voice, so unlike his usual self.

And the grief carried in his low, subdued voice was something the giant known as the Fire King rarely let show.

But…

As always, a bad feeling never misses.

“You’ve arrived.”

The first person to greet us was the Medicine King Hall Master, who had been standing guard at the door.

As the man gathered his bundle and left the moment we arrived, Jeok Cheongang spoke to him in a quiet voice.

“As I asked, please don’t tell anyone.”

“…”

“Thank you. You’re an excellent physician.”

The Medicine King Hall Master bowed his head slightly without a word and left. Only then could we face the man waiting inside.

“Oh, you brought him back sooner than I expected. That old man’s legs are so short, I figured it’d take another seven days and nights.”

Another giant had come to his senses after several days.

I silently watched the Thunderbolt Saber King laugh heartily at his own lighthearted joke. Only when Jeok Cheongang gave my shoulder a nudge did I belatedly clasp my hands in a salute.

I gave him the utmost respect I could.

“I am Jin Taekyung, an insignificant martial artist of Murim. It’s an honor to meet you, Great Hero Peng.”

“Don’t bother. Excessive humility can be a poison in its own right. If you’re an insignificant martial artist, does that mean every other one beneath Heaven is dead?”

The Thunderbolt Saber King smiled at me with satisfaction, then turned his gaze to Jeok Cheongang.

“Now that I see him, you were whining for nothing. You kept complaining that he ran wild like a reckless brat, with no respect for his elders, more and more as the days went by.”

“Friend, my ass. You’ve got a lot of nerve talking to someone so much older than you like that.”

Jeok Cheongang managed to answer in his usual gruff tone, but the weight in his eyes was impossible to hide.

Whether he noticed Jeok Cheongang’s state or not, the Thunderbolt Saber King laughed even louder.

“Wahaha! What are you so sore about? We’re both getting old.”

“Don’t you know the Three Bonds and Five Relationships? Never heard of respect for elders?”

“If knowing that meant someone else would feed me, maybe. Or would it make my martial arts stronger?”

“Forget it. I’m the fool for having this conversation with an ignorant Peng.”

“Admitting your own shortcomings. I like it. I was just getting tired of talking to a stinky old man, so this works out nicely. Don’t you agree?”

At the Thunderbolt Saber King’s tossed-off question, I nodded.

“Well, my Master is a little old.”

“What did you say? Hahaha!”

His laugh burst out, loud enough to shake the room.

It didn’t suit the Thunderbolt Saber King’s pallid complexion at all. It sounded so loud, it was almost as if he’d forced it out.

*No. That’s probably exactly what he did.*

I murmured silently to myself.

What you could see with your eyes wasn’t everything. I could feel it.

Even now, the energy within the Thunderbolt Saber King was wavering precariously, like a glass vessel cracked all over.

Like a flame that could go out at any moment.

“I heard you wanted to see me.”

At my heavy-voiced remark, the Thunderbolt Saber King seemed to realize I’d noticed his condition. He spoke, still smiling.

“You’re a perceptive one. You’re worlds apart from the last time I saw you. The Fire King may not be good at much else, but he’s certainly raised his Disciple well.”

“…”

“There’s no need to look so miserable. For martial artists like us, life and death are just part of the deal.”

He was right.

That was the life of a martial artist.

And the Thunderbolt Saber King had spent his life making his way through a mountain of sabers and a forest of swords, beset by countless threats and schemes. He accepted the reality of his situation with calm composure.

“I had a very long dream. I was able to look back on my whole life in it. I even got to see my friend Murong Baek as a young man again, for the first time in ages.”

“Friend, my ass. That bastard deserved to die.”

At Jeok Cheongang’s casual remark, the Thunderbolt Saber King let out a quiet laugh and continued.

“That’s all in the past. It couldn’t be helped. You can’t put spilled water back where it was. But in the end, we stopped Dark Heaven’s plot and saved more people. That’s enough for me.”

He was famous for having a temper as fiery as Jeok Cheongang’s. But he looked at me with eyes as still as a pond.

“When I first saw you at the Star-Array Grand Banquet, I had a feeling you’d accomplish great things before long. Everyone could tell you’d become a pillar capable of protecting the world, together with the Sword Saint’s Disciple.”

Of course, I’d been inexperienced back then.

I hadn’t stood shoulder to shoulder with all those powerful masters like I did now, and I’d been brutally defeated by a monster called the Blood Lord.

“But nobody could have guessed you’d grow this much, this quickly.”

The threats to my life had come one after another, each one growing more dangerous, and I’d grown at a staggering pace as a result.

Enough to make even those who’d watched me from the closest distance question their own eyes.

“That’s why I asked for you right away. It’s also my last chance to make the best use of the time and energy I have left.”

“…You mean…”

“They say an ordinary tiger leaves its hide behind when it dies. But the great tiger of Hebei will leave something else.”

At the Thunderbolt Saber King’s faint smile, I finally understood why he’d sought me out first, rather than his own flesh and blood, after barely regaining consciousness—and with death right before him.

“Take it. Everything I have left.”

At the very moment the Thunderbolt Saber King’s calm voice rang through the room—

*Ding.*

> **System**
>
> An emergency Quest, **Transmitting Internal Energy Across the Body**, has been created.
>
> **!!Warning, warning!!**
>
> The process of completing this Quest carries an extreme risk.
>
> Do you accept the emergency Quest?
>
> Y / N

I stared silently at the Thunderbolt Saber King’s smiling face through the holographic window that had appeared with a clear chime.

Then, all at once, I spoke.

“Why… Why did you choose me?”

The answer came without the slightest hesitation.

“Because I believe in you.”

“…!”

“That belief isn’t mine alone. The Dharma King believes in you. Your Master believes in you. Now, the whole world believes in you.”

I could hardly breathe.

My chest tightened, and it felt as if my blood were surging through my veins.

Amid it all, the Thunderbolt Saber King’s voice rang clearly in my ears.

“This is all for the world, not for you. Do you need any other reason?”

“No.”

I took a small, steadying breath and continued.

“That’s reason enough.”

A smile crossed the Thunderbolt Saber King’s pallid face.

“Sit in the lotus position.”

*Ding.*

> **System**
>
> You have accepted the emergency Quest, **Transmitting Internal Energy Across the Body**!

* * *

Internal energy was an intangible force that existed everywhere in the world.

Those who practiced martial arts accumulated it within their bodies, strengthening their bodies and minds. They repeated grueling training in hopes of stepping beyond human limits and into the realm of the superhuman.

But not everyone wanted that kind of power.

The greater the energy accumulated within the body, the greater the backlash it could unleash.

If someone tried to circulate their internal energy recklessly by following an incorrect formula, they were likely to end up crippled. And without enlightenment, many fell into a heart demon and became half-mad.

Even so, the desire of martial artists to reach ever greater realms rarely faded.

A world ruled by the law of the jungle.

They came up with all kinds of ideas to grow stronger, faster and more safely. In the process, they discovered one astonishing method.

*What if, instead of spending years accumulating internal energy, you inherited it all from someone else?*

*Inherit the power of an old master on the verge of death? Huh? Isn’t that basically rock honey?*

In the distant past, Transmitting Internal Energy Across the Body was born that way.

And from the moment it was born, it became a taboo that must never be put into practice.

The reason was simple.

It only looked sweet on the surface. In truth, it was a double-edged sword.

No—it was so much worse that calling it a double-edged sword was laughable. The failures far outnumbered the successes.

“Master!”

“No!”

They died, and died, and died again.

Even those who survived through sheer luck would end up crippled, their qi and blood snarled together, or lose their original martial prowess forever. In the process, they lost Supreme Peak masters who had dominated their era and gifted young prodigies.

So when the Thunderbolt Saber King told Jin Taekyung he intended to transmit his internal energy to him, Jeok Cheongang could only ask in disbelief:

*“Have you gone mad?”*

*“Not at all.”*

*“No, you’re definitely mad. Normally, you’d be flying into a rage by now.”*

*“I may have been awake for only half a shichen, but my mind has never been clearer. I can’t remember ever being this sharp in my life.”*

*“Well, that’s a hell of a thing to celebrate. So does that mean you can finally finish the Thousand Character Classic?”*

*“Cut the nonsense. You know this isn’t just a mad idea.”*

In truth, the Thunderbolt Saber King was right.

Jeok Cheongang had only answered that way on reflex at first. In his heart, he was already weighing the chances of this insane undertaking.

*“I hate to admit it, but your precious Disciple could withstand Transmitting Internal Energy Across the Body. Isn’t he blessed with the Heavenly Martial Physique, along with that child Cheongpung?”*

*“…The Heavenly Martial Physique.”*

*“If that were all, I wouldn’t be having this conversation with you. He has the Muscles and Bones Heaven granted him, as well as enough potential and insight as a martial artist.”*

If this had happened a few months ago, Jeok Cheongang would never have accepted a proposal that put his Disciple’s life at risk, no matter how strongly anyone urged him.

Not even if it came from the Thunderbolt Saber King, a man he’d spent decades trading barbs with and grown fond of despite himself—and who was now on the verge of death.

But Jeok Cheongang was different after Jin Taekyung had told him the truth himself.

*There’s a chance. No—it’s more than enough.*

A transfer of internal energy between two Supreme Peak masters who had reached their realms—a feat with no precedent in the long history of Murim.

And Jin Taekyung, with a superhuman body that could only be called the Heavenly Martial Physique, possessed yet another strange power.

The Prison of Karma.

A divine strength that could purify the body and even heal injuries.

As long as he remained alive, that power gave him a chance.

And besides…

*He’s already succeeded at Transmitting Internal Energy Across the Body once.*

Jeok Cheongang had only heard the story much later.

Jin Taekyung had received the internal energy of the Heavenly Power Demon, a great fiend of the Demonic Cult imprisoned in the Sichuan Tang Clan’s underground prison, then defeated the Western Heaven Demon Lord.

When he first heard it, the shock of learning his Disciple had nearly died had made his heart feel ready to burst. But the difference between that time and now was clear.

The circumstances were different. So was the martial prowess Jin Taekyung had achieved since then.

*He can do it. No…*

He *will* do it.

He had to.

Jeok Cheongang steadied his wavering heart with firm resolve, then watched the two men, joined at the Great Palace acupoint, with a deeply troubled gaze.

*Whoosh.*

Unprecedented internal energy surged out in every direction.
```
