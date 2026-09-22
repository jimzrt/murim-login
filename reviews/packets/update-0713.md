<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0713.txt",
      "sha256": "acadd0e713e18d61be3f1638838a404cf9ee0e26a59a6937855c9401e864a6ed",
      "bytes": 13901
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "26aefba1a56c0d02d24d58434c561a2e94862d6ab2a235d2fb4ad761c778a363",
      "bytes": 1296
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "8c6e87bbcde4b2bec20540fb345cb74ffa869c3c025181296a77831c980a7708",
      "bytes": 207251
    },
    {
      "path": "characters/Baekhwi.md",
      "sha256": "32c2bf303f15e3ad1b6ff528481bcc5690b199efce4492c33c20aefb5267706b",
      "bytes": 493
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "7f8bbc0ab01c2e1b840fb842d95c12e61d64a230a2ca6f41a727afe59a3699a3",
      "bytes": 910
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "546df9445219bcd560338314e13361a4db96ac0a91821eb9f8d5cf0b9979db76",
      "bytes": 792
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "8283c39fa2615f12c2934444a0e071812608dc9dfbb634ff71c47071985cc3ae",
      "bytes": 553
    },
    {
      "path": "characters/Great Snow Fiend.md",
      "sha256": "42b8b5c48d7de2d5e84e440ebb6d5a51e5cc56febcc25876108b966b2ac87556",
      "bytes": 898
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "5162fa27a4b6b21998d158682fd1c0b9aed7e04ad78706bb384b006c97f06bce",
      "bytes": 1702
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "f2ba79dfca6b09c015b14cb76a8ea97a0b087f218d5f489b0d31ca790e226d6e",
      "bytes": 1787
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "bece117bb99c9c67401b94aa6fb1cd7ad97d2eaa7d3f39e92826459f9405fbee",
      "bytes": 622
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "a16b5cbf28145355e4d0fdd964a5fd523465252f0a4b6e1c22ae99777cb4da09",
      "bytes": 676
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8ae62fdddb6bf29233c3958f1ed90caa4eb501d2d5a89d63ccbcc53ef92af4e7",
      "bytes": 218340
    }
  ],
  "estimated_tokens": 12657
}
-->

# Durable State Update — Chapter 713

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 713. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 713. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
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
  "chapter": 713,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 713,
    "continuity_sources": [713],
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
    "The rift is spreading from the Inner Palace toward the Outer Palace and emits demonic qi that can corrupt living beings.",
    "Only the sacred stone's power can withstand the rift's darkness.",
    "The guardian spirit has absorbed the sacred stone and entered the rift to seal it.",
    "The sacred stone's light purifies the darkness around the guardian spirit.",
    "The guardian spirit has recognized protecting the land as its true mission.",
    "The guardian spirit shared a roughly three-hundred-year friendship with Yayul Cheon.",
    "Jeok Cheongang has agreed to kill the guardian spirit if the rift corrupts it.",
    "The guardian spirit has released a massive shock wave at the rift's center."
  ],
  "continuity_sources": [
    712
  ],
  "open_questions": [
    "Will the guardian spirit survive after releasing the shock wave?",
    "Will the rift be sealed completely?",
    "Will the guardian spirit be corrupted, forcing Jin Taekyung or Jeok Cheongang to kill it?"
  ],
  "safe_through": 712,
  "temporary_decisions": [
    "Continue rendering the guardian spirit's 의념 as Will.",
    "Render the sacred stone's cleansing effect as purification.",
    "Retain Old Master as Jin Taekyung's address to Jeok Cheongang."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 하남     | **Henan**              |
| 정마대전   | **Great Faction War**         |
| 귀가      | **your family**                                                 |
| 백휘 | **Baekhwi** | Baeksang's deceased only child. |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 대설귀 | **Great Snow Fiend** | Fiend who ruled Great Snow Mountain and killed Baekhwi and Venerable Wusang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 새외 | **Outer Lands** | Lands outside the Central Plains and its Murim. |
| 암기 | **hidden weapon** | Term used in Mungyeong's promise not to throw one. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 휘아 | **Hwi** | Familiar vocative form of Baekhwi. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 궁주 | **Palace Lord** | Title Yohi uses after realizing that Heugung is the Beast Miao King. |
| 백천대 | **Baekcheon Unit** | Baeksang's secret elite unit, cultivated over decades and held in reserve. |
| 성지 | **Sacred Land** | Former name of the Poisonblood Grounds when beasts ruled Ailao Mountain. |
| 수호령 | **guardian spirit** | Ancient title for the Black Tiger. |
| 신석 | **sacred stone** | Stone said to have existed alongside the Black Tiger's birth. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |
| 신수 | **divine beast** | A more exalted category than a spiritual creature. |

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
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 적천강 | 남천마후 | legendary_martial_master_to_hostile_demon_empress | you bitch | blunt and threatening | Threatens to punish her and Lord of Heaven. |
| 남천마후 | 적천강 | hostile_demon_empress_to_legendary_martial_master | Fire King Jeok / you | flattering and mocking | Addresses Jeok Cheongang as the Fire King while praising Lord of Heaven. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 백상 | 야수묘왕 | Nanman great chieftain to the Nanman Beast Palace Lord | Palace Lord | restrained and apologetic | Apologizes for causing the disturbance after the Beast Miao King stops the fight. |
| 백상 | 백휘 | father_to_deceased_child | Hwi | emotionally charged and possessive | Baeksang directly invokes his deceased child's name while confronting Jin. |
| 백상 | 남천마후 | Nanman Great Chieftain to hostile demon empress | Southern Heaven Demon Empress | formal and shocked | Baeksang directly identifies the woman who appears before him. |
| 남천마후 | 백상 | Dark Heaven controller to coerced Nanman leader | Great Chieftain Baeksang / Palace Lord | playful, taunting, and threatening | She repeatedly addresses Baeksang while mocking his grief, acknowledging his effort, and issuing her order. |
| 진태경 | 대설귀 | hostile_martial_opponents | old man | mocking, casual, and profane | Jin taunts the Great Snow Fiend while preparing to continue the fight. |
| 대설귀 | 진태경 | hostile_martial_opponent | Jin Taekyung | cold, incredulous, and confrontational | The Great Snow Fiend addresses Jin while demanding an explanation for his survival. |
| 진태경 | 수호령 | human ally to guardian spirit | guardian spirit | quiet and commanding | Jin whispers that they should go as they advance toward Baeksang. |
| 수호령 | 남천마후 | guardian_spirit_to_hostile_supernatural_opponent | you | terse, accusatory, and contemptuous | The guardian spirit tells the Southern Heaven Demon Empress that it knows her true essence and condemns her as a Fiend. |
| 남천마후 | 수호령 | hostile_supernatural_opponent_to_guardian_spirit | hideous beast | playful, taunting, and dismissive | She insults the guardian spirit while addressing it as a beast. |
| 수호령 | 진태경 | guardian spirit to human ally | Human | terse and alarmed | The guardian spirit cries out to Jin as the Southern Heaven Demon Empress sends him crashing into the ground. |
| 야수묘왕 | 남천마후 | allied_Ten_Kings_master_to_hostile_Demon_Empress | you | cold and threatening | The Beast Miao King addresses the Southern Heaven Demon Empress while promising to tear off her limbs and kill her. |
| 수호령 | 적천강 | guardian_spirit_to_legendary_martial_master | old human | terse and contemptuous | The guardian spirit addresses Jeok as 늙은 인간 while recognizing that his essence has not changed. |

## Listed compact profiles

### Baekhwi.md

# Baekhwi (백휘)

- **Safe through:** Chapter 673
- **Aliases:** None
- **Role:** Baekhwi was Baeksang's only child, would have become the Beast Miao King's son-in-law, and was killed without leaving a corpse during the Great Snow Mountain battle.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Baeksang's only child; would have been the Beast Miao King's son-in-law if he had lived.

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 708
- **Aliases:** None
- **Role:** Baeksang is the Palace Lord of the Nanman Beast Palace and sole Great Chieftain of Nanman; after a long-awaited ambush against the Southern Heaven Demon Empress, he is flung away with catastrophic injuries.
- **Personality:** Cold, rigid, meticulous, and strategically resolute, yet burdened by regret, grief over Hwi's death, and a final conflicted impulse to spare others from the coming bloodshed.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of deceased Baekhwi, whom the Great Snow Fiend killed; he cultivated Yohi with gold and influence and used her support to advance Dark Heaven's preparations.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 712
- **Aliases:** Heugung
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, and Great Chieftain of the Miao people.
- **Personality:** The Beast Miao King is boisterous and warmhearted toward Nanman's people, but their corruption and destruction awaken fierce grief and wrath in him.
- **Voice:** Low, growling, and forceful.
- **Relationships:** Baeksang is his sworn younger brother and childhood companion, Yayul Mok is his Young Palace Lord, Jeok Cheongang is an old acquaintance, and Jin Taekyung is Jeok's Disciple whom he now fights beside against the Southern Heaven Demon Empress.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 712
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Great Snow Fiend.md

# Great Snow Fiend (대설귀)

- **Safe through:** Chapter 701
- **Aliases:** Hanbaek (한백)
- **Role:** The Great Snow Fiend was the former ruler of Great Snow Mountain and a Supreme Peak fiend who killed Baekhwi and Venerable Wusang during the Great Faction War before Jin Taekyung killed him.
- **Personality:** The Great Snow Fiend is cold, pragmatic, controlled, proud, and unwilling to risk his life foolishly when outnumbered.
- **Voice:** The Great Snow Fiend speaks in measured, archaic, calm, and authoritative language that becomes frost-cold when challenged.
- **Relationships:** The Great Snow Fiend was an enemy of Baeksang, Baekhwi, Venerable Wusang, the Beast Miao King, and the allied Southern Army; he was senior to Black Hand and served under the Southern Heaven Demon Empress before Jin Taekyung killed him.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 712
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 712
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, and a publicly recognized S-rank-level Hunter who formally retains an A-rank license.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 712
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 712
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress is Honglan, the creator of the rift behind the Inner Palace.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

## Korean source

```text
＃713화



기다림은 그리 길지 않았다.

내가 살아남은 이들을 한 곳으로 옮기고, 적천강의 도움으로 야수묘왕이 힘겹게 눈꺼풀을 들어 올리던 그 순간.

드득. 드드득.

변화가 시작되었다.

그것은 나도, 적천강도. 심지어는 아직 몸이 성치 않은 백천대원들과 이제 겨우 정신을 차린 야수묘왕조차 느낄 수 있는 울림이었다.

화아아악.

공간이 일그러진다. 살아 있는 것처럼 꿈틀거리던 어둠이 움직임을 멈추고, 바람이 한 방향으로 흐르기 시작했다.

수호령을 집어삼킨 짙은 어둠 너머, 태고의 짐승처럼 거대한 아가리를 벌린 절벽의 틈새 사이로.

동시에 똑똑히 보고 들을 수 있었다.

- 크아아아앙!

메아리처럼 울려 퍼지는 포효와 함께, 어둠을 밝히며 또렷해지는 한 줄기의 빛을.

‘이건…….’

나는 아연한 눈빛으로 그 빛을 바라보았다. 아니, 이 자리의 모두가 마찬가지였다.

크고 작은 부상을 입은 생존자들은 신음을 흘리는 것조차 잊었다.

이제 겨우 의식을 회복한 야수묘왕은 넋 나간 얼굴로 저 먼 곳에서 홀로 어둠을 밝히는 빛을 향해 손을 뻗었다.

햇살보다 따스하고, 물처럼 맑은 기운을 품은 빛.

마치 세상이 멈춘 듯한 정적이 찾아온 그때, 적천강의 나직한 목소리가 귓가를 파고들었다.

“온다.”

“……!”

그리고 그 한 마디와 함께, 멈춰 있던 시간이 흐르기 시작했다.

고오오오옹. 파아앙!

거대한 폭발.

모든 것이 응축되고, 일시에 터져 나와 사방을 휩쓸었다. 귀가 먹먹해질 만큼의 굉음과 함께 보이지 않는 충격파가 차도처럼 들이닥친다.

휘몰아치는 광풍(狂風) 너머로 적천강의 외침이 들려왔다.

“조심……!”

콰아아아!

바람, 아니 폭풍이 소리를 집어삼켰다.

어둠과 빛이 뒤섞인 아득한 섬광이 시야를 가리고, 거대한 충격파가 범위 안의 모든 것을 후려치고 날려 보냈다.

하지만.

‘지금.’

때가 왔음을 깨달은 나는, 백염을 비스듬히 내리그었다.

 투명한 창날을 타고 솟구친 겁화가 바람을 불태운다. 보이지 않지만 분명 존재하는 결을 파고든 불길이 충격파와 부딪쳤다.

아니, 상쇄했다.

콰아아아앙! 드드득!

굉음과 함께 지축이 흔들렸다. 단단하게 뿌리내린 두 다리가 밀려 나갈 정도의 충격.

나와 마찬가지로 생존자들을 지키기 위해 앞으로 나선 적천강이 양 소매를 떨쳤다.

화륵. 퍼어엉!

극의에 도달한 열화신장(烈火神掌).

내 것과는 달리 이미 완성된 두 마리의 화룡(火龍)이 흉포하게 날뛰며 폭풍을 물어뜯었다.

반경 수십 여장을 휘감으며 솟구친 불길이 바람을 살라 먹고, 충격파에 의해 암기(暗器)처럼 쏘아진 무수한 잔해의 파편들을 잿가루로 만들었다.

치지지지직!

매캐한 연기와 수증기가 사방을 가득 메운다. 온통 희뿌옇게 물든 세상 속, 나는 참았던 숨을 토해 내며 손을 뻗었다.

파앙!

압축된 공기가 터져 나가며 연기와 수증기를 밀어 낸다.

그리고 서서히 걷혀 나가는 시야 너머에는, 흩어져 가는 어둠과 이제 막 시작된 붕괴가 모두를 기다리고 있었다.

쿠웅. 쿠구구궁!

무너지고 있다. 이백여 장에 달하는 거대한 절벽이.

크고 작은 기암괴석(奇巖怪石)들이 하늘을 메우며 쏟아져 내리는 광경은 두려울 만큼 압도적이었고, 그 위로 조금씩 비추기 시작하는 햇살은 한 가지 사실을 의미했다.

‘균열이…… 닫혔다.’

끝났다.

길고 치열했던 전투가 마침내 막을 내렸다. 수십만, 어쩌면 수백만 명이 희생당했을지도 모를 재앙을 막았다.

하지만 어째서일까. 기쁨보다는 공허한 감정이 더욱 컸다.

아마도 그것은, 아직 끝내지 못한 일이 남아있다는 것을 누구보다 잘 알고 있기 때문일 것이다.

띠링.



- [균열]이 닫혔습니다.

- [마기]가 사라집니다.

- [신석]의 힘이 [마기]에 의해 오염된 기운을 정화합니다.

- 돌발 퀘스트, [희생과 안식]이 생성되었습니다. 당신은 해당 퀘스트를 거부할 수 없습니다.



귓가로 전해지는 시스템 알림에, 나는 문득 손을 뻗었다.

허공에서 살아 있는 생물처럼 고통스럽게 몸부림치던 어둠이 손가락 사이로 흩어진다.

서서히 걷혀 가는 먹구름 사이로 비친 햇살은 따스했고, 그 위로 떠올라 있는 반투명한 홀로그램 창에는 몇 줄 되지 않는 짤막한 글씨가 적혀 있었다.



퀘스트



[희생과 안식]



이제 그에게 안식을 주십시오.



등급 : 無

제한 : 無

임무 : [변이된 수호령] 처치 (미완료)

보상 : ???

실패 : ???





처음이다.

퀘스트 설명이 이렇게 짧았던 것도. 대부분 내 이름 세 글자가 적혀 있던 퀘스트 제한이 그 누구에게도 국한되지 않은 것도.

어쩌면 시스템 역시 그의 희생을 알고 있을지도 모른다.

신수(神獸)라 불러도 부족함이 없는 존재에서, 스스로를 바쳐 타락한 수호령의 선택을.

저벅.

나는 잿가루와 함께 바람에 흩날려 사라지는 어둠을 해치며 나아갔다.

조용히 뒤따르는 적천강의 걸음과, 지금 이 순간에도 끊임없이 무너져 내리고 있는 무수한 기암괴석 사이로 누군가의 존재감이 전해졌다.

아니, 보였다.



[Lv.155 변이된 수호령]



어둠 속에서도 은빛으로 빛나던 털도, 성지의 연못처럼 맑던 청백색의 눈동자도 이제는 검게 물들었다.

두 배는 길게 자라난 송곳니가 우리를 향해 번뜩인다.

- 크르르릉.

흉포함이 담긴 낮은 울음소리. 그리고 뒤이어 시작된 섬광과도 같은 움직임.

쐐애애애액!

흐릿해진 신형과 함께 십여 장의 거리가 지워지고, 피에 젖은 앞발이 땅을 밟으며 솟구친다.

파팟.

순간 머리 위로 그늘을 드리운 거대한 동체를 향해, 나와 적천강은 전력을 다한 일격을 쏟아 냈다.

그가 떠나기 전 건넸던 당부를 떠올리며.



‘나를 죽여라. 한 치의 망설임도 없이.’



그리고 우리는, 그 약속을 지켰다.

쉬이익, 서걱!



* * *



그곳은 아주 깊고 차가운 어딘가였다. 단 한 점의 빛도 흘러들어오지 못하고, 미약한 온기조차 느낄 수 없는.

‘그’는 그곳에 웅크린 채 쓰러져 있었다. 곧 찾아올, 혹은 이미 찾아왔을 죽음의 기운을 느끼며.

그리고 어느 순간, 문득 따스한 온기를 느끼며 눈을 떴다.

아니. 그것은 온기라 부를 수 없는 열기였고, 흐릿한 시야 속에서 그를 기다리고 있던 것은 낯익은 얼굴을 한 누군가였다.

“진태……경.”

갈라진 목소리가 입술 사이로 흘러나온다.

비로소 눈을 뜬 백상의 모습을 물끄러미 응시하던 청년, 진태경이 담담하게 대답했다.

“그래.”

그리고 그 한 마디에, 백상은 모든 것이 끝났음을 알았다.

어쩌면 그것은 진태경의 어깨너머로 비치고 있는 햇빛 때문일지도 몰랐다.

‘그래. 결국 그리 되었군.’

마음속에서 울려 퍼지는 뇌까림. 백상은 먹구름이 사라진 푸른 하늘을 바라보았다.

참으로 희한한 일이었다. 얻고자 했던 모든 것을 잃었음에도, 절망보다는 그저 공허했다.

“남천마후는 어찌 되었나.”

돌아온 대답은 짧았다.

“죽었어.”

“균열도 사라졌겠군.”

“……그래.”

망설임이 담긴 목소리와 함께 진태경의 고개가 움직인다. 그의 시선이 잠시 머문 곳에는 거대한 호랑이가 쓰러져 있었다.

아니, 지금 이 순간 백상의 눈에 비친 것은 무수히 많은 짐승과 인간의 사체였다.

“하나만 묻자.”

깊게 가라앉은 진태경의 목소리가 이어졌다.

“이렇게 될 거라는 걸, 처음부터 알고 있었나?”

백상은 텅 빈 눈동자로 사방을 가득 메운 사체들을 바라보았다. 그리고 대답했다.

“그래. 알고 있었다.”

“……!”

으득. 이를 악문 진태경이 백상을 노려보았다. 화염이 줄기줄기 쏟아지는 시선을, 백상은 피하지 않았다.

“정확히는 지금으로부터 몇 달 전, 중원에서 온 서신을 받고 나서 알게 되었지.”

그 서신은 하남에서 온 것이었고, 곧 탄생할 무림맹에 입맹(入盟)을 권하는 제안과 함께 호북에서 벌어진 일련의 사건이 소상히 적혀 있었다.

“그때 깨달았다. 암천이 왜 중원이 아닌 새외(塞外)에 속한 남만에 손을 뻗었는지. 남천마후가 말하는 대계(大計)가 무엇인지.”

“그럼 그 사실을 알면서도…….”

“명령에 따랐지. 나는 이미 사람이 아닌, 괴물이 되어 버렸으니까.”

십 년이면 강산(江山)도 바뀐다고 했다. 때로는 지진이 일어나 산을 허물고, 거센 홍수가 강의 흐름을 비튼다.

백상은 장장 사십여 년의 세월을 지진과 홍수 속에서 보내며 마음을 잃은 괴물이 되어 갔다.

하나뿐인 자식을 잃은 슬픔. 그리고 자식을 잃게 만든 중원인에 대한 복수심으로.

하지만 그것만이 전부는 아니었다.

“정마대전 이후, 나는 누구보다 마도(魔道)를 증오했다. 중원이 용서할 수 없는 변절자라면, 놈들은 반드시 죽여야 할 적이었지.”

백상의 말을 들은 진태경은 헛웃음을 흘렸다.

암천과 마교는 줄기만 다를 뿐, 한 뿌리를 가진 나무다. 마도를 증오했다면 제 자식을 죽인 암천과 붙어먹을 수는 없었다.

그런데 백상은 남천마후와 손을 잡고 재앙을 일으켰다.

암천이 균열을 여는 것을 방조했고, 수많은 죽음이 뒤따를 것을 알았음에도 끝끝내 총동원령을 내려 일만에 달하는 전사와 맹수들을 내궁으로 끌어모았다.

사실상 산 제물로 바치기 위해서.

“이 병신 같은 새끼. 그걸 지금 말이라고…….”

끓어오르는 목소리는 끝까지 이어지지 않았다.

무슨 이유에선지 문득 말꼬리를 흐린 진태경의 모습에, 백상이 피에 젖은 입술을 달싹였다.

“그래. 내게는 증오보다, 다른 그 무엇보다 중요한 것이 있었다.”

바로 그 순간이었다. 진태경의 뇌리에 누군가의 모습이 스쳐 지나간 것은.

복면 위로 드러난 그 눈동자가, 마치 어디선가 마주쳤던 것처럼 낯익게 느껴졌던 이유 역시도.

“……백휘(白輝).”

진태경이 한 말이 아니다.

백상은 흐릿한 눈을 들어 저 멀리로부터 다가오는 인영을 바라보았다. 비틀거리는 걸음으로 가까워지는 거한.

적천강의 만류에도 불구하고 코앞까지 다가온 야수묘왕이 신음하듯 물었다.

“그 아이가, 살아 있었느냐.”

백상은 힘없이 고개를 끄덕였고, 야수묘왕에게는 그것으로 충분했다.

그는 알고 있었다. 그 아이가 백상에게 어떤 존재였는지, 자신의 의제(義弟)가 하나뿐인 자식을 위해 무슨 일을 할 수 있는지.

그렇기에 누구보다 슬펐고, 분노할 수밖에 없었다.

“왜, 어찌하여 내게 말하지 않았느냐. 왜!”

“궁주를…… 형님을 죽게 하고 싶지 않았소.”

“……!”

“더불어 휘, 그 아이도 다시 잃게 되었겠지.”

백상의 눈동자에 과거의 기억이 아스라이 스쳤다.

어둠과 처음으로 대면한 그 날, 그는 손을 잡자는 남천마후의 제안을 일언지하에 거절했다.

대설귀에게 죽은 줄만 알았던 자식이 살아 있다는 이야기를 듣기 전까지는.

“나는 남천마후의 제안을 받아들였고, 모든 대계가 끝나면 휘아를 살려 주겠다는 약속을 믿었소.”

믿었다. 아니, 불신을 억누를 수밖에 없었다.

하나뿐인 자식과 재회하기 위해서는, 그 방법밖에는 없었으니까.

그 후 마음이 흔들릴 때면 그는 남천마후를 찾아갔다. 암천의 술사들에 의해 목숨을 부지한 채, 깊은 잠에 빠져 있는 자식의 얼굴을 보기 위해서였다.

“그러나 한편으로는 알고 있었소. 내가 무슨 짓을 하고 있는지, 이 선택으로 얼마나 많은 이들이 죽어 나갈지.”

그래서 백천대를 만들었다.

자신이 아닌, 다른 누군가를 위해서. 그가 이 재앙을 막아 주길 바라는 마음으로.

“그건…… 내가 할 수 없는 일이었소.”

자식이 부모를 죽일지언정, 자식을 죽이는 부모는 없다.

백상은 한 아이의 아버지였다. 설렁 수십, 수백 번을 그때로 돌아간다 해도 그의 선택은 같을 것이다.

쿨럭.

핏물을 토한 백상이 흐릿한 눈을 들어 야수묘왕을 바라보았다.

지금 이 순간, 그의 눈동자에는 인생에서 가장 슬픈 동시에 행복했던 어느 날의 기억이 스쳐 지나가고 있었다.

‘그래. 그날이었지.’

사랑하는 부인을 잃고, 누구보다 사랑하게 될 한 아이를 얻은 그 날, 백상은 울었다.

하나뿐인 의형과 마주 앉아서 오늘이 마지막인 것처럼 과실주를 들이켰다.

수십 년이 지나, 남천마후가 찾아왔던 그 날처럼.

“마지막 부탁이오.”

백상은 희미한 웃음과 함께 말을 이었다.

“날 죽여 주시오, 형님.”
```

## Final English reading copy

```markdown
# Chapter 713

The wait was not a long one.

It happened at the exact moment I had moved the survivors to one place and, with Jeok Cheongang’s help, the Beast Miao King finally managed to lift his heavy eyelids.

Crack. Crack-crack.

The change began.

It was a resonance that I could feel. So could Jeok Cheongang. Even the Baekcheon Unit warriors, whose bodies were still far from recovered, and the Beast Miao King, who had only just regained consciousness, felt it.

Whoooosh.

Space twisted. The darkness that had writhed as though it were alive stopped moving, and the wind began to flow in a single direction.

Beyond the thick darkness that had swallowed the guardian spirit, between the cracks in the cliff that had opened its enormous jaws like some primordial beast—

At the same time, I could clearly see and hear it.

—Kraaaang!

Along with the roar that echoed like thunder, a single streak of light grew clearer as it illuminated the darkness.

*This is…*

I stared at that light in bewilderment. No—everyone here was doing the same.

The survivors, covered in injuries both large and small, even forgot to groan.

The Beast Miao King had only just regained consciousness, but he reached out with a dazed expression toward the light that illuminated the distant darkness all by itself.

It was a light imbued with qi warmer than sunlight and as clear as water.

Just as a silence descended, as though the world itself had stopped, Jeok Cheongang’s quiet voice pierced my ears.

“It’s coming.”

“……!”

And with that single word, time—which had been frozen—began to move again.

Rumble. Boom!

A gigantic explosion.

Everything condensed, then burst outward all at once, sweeping across every direction. Along with a deafening roar, an invisible shock wave surged in, broad as a highway.

Beyond the raging gale, I heard Jeok Cheongang shout.

“Watch out—!”

Kuwaaaang!

The wind—no, the storm—swallowed his voice.

A distant flash of darkness and light mixed together, blocking my vision, while the enormous shock wave battered and flung away everything within its range.

But.

*Now.*

Realizing that the time had come, I brought White Flame down in a diagonal slash.

The hellfire surging along the transparent spearhead burned through the wind. The flames dug into a grain that was invisible but undeniably there, then collided with the shock wave.

No—it canceled it out.

Kuwaaaang! Crack!

The earth shook with a deafening roar. The impact was powerful enough to push back both of my firmly rooted legs.

Jeok Cheongang, who had stepped forward to protect the survivors just as I had, flung both sleeves.

Fwoosh. Boom!

The Blazing Flame Divine Palm, perfected to the pinnacle.

Unlike mine, two complete fire dragons rampaged ferociously, biting into the storm.

The flames surged upward, coiling across a radius of dozens of jang as they consumed the wind and reduced to ash the countless fragments of debris hurled like hidden weapons by the shock wave.

Ssszzzzzt!

Smoke and steam filled every direction. In a world dyed entirely pale white, I exhaled the breath I had been holding and reached out.

Boom!

Compressed air burst outward, driving back the smoke and steam.

And beyond the vision that slowly cleared, the darkness was dispersing, while a collapse that had only just begun awaited us all.

Rumble. Rumble-rumble!

It was collapsing.

A gigantic cliff stretching more than two hundred jang.

The sight of countless strange and enormous rocks pouring down and filling the sky was frighteningly overwhelming. The sunlight beginning to shine down over them little by little meant one thing.

*The rift… closed.*

It was over.

The long and fierce battle had finally come to an end. We had stopped a catastrophe that might have claimed hundreds of thousands—perhaps even millions—of lives.

But why?

Why was the emptiness greater than the joy?

Perhaps it was because I knew better than anyone that there was still something left unfinished.

Ding.

> **System**
>
> **Rift** has closed.
>
> **Demonic qi** is disappearing.
>
> The power of the **sacred stone** purifies energy corrupted by **demonic qi**.
>
> A sudden **Quest**, **Sacrifice and Rest**, has been generated. You cannot refuse this Quest.

As the System notification reached my ears, I suddenly reached out.

The darkness that had writhed painfully in the air like a living creature scattered between my fingers.

The sunlight shining through the slowly dispersing storm clouds was warm. Floating above it was a translucent holographic window displaying only a few short lines.

> **System**
>
> **Quest**
>
> **Sacrifice and Rest**
>
> Now grant him rest.
>
> **Grade:** None
>
> **Restriction:** None
>
> **Objective:** Defeat Mutated Guardian Spirit *(Incomplete)*
>
> **Reward:** ???
>
> **Failure:** ???

It was the first time.

The first time a Quest description had been this short. The first time the restriction field—which usually contained the three characters of my name—had not limited the Quest to anyone at all.

Perhaps even the System knew about his sacrifice.

The choice made by a being that could easily have been called a divine beast—a guardian spirit that had sacrificed itself and fallen into corruption.

Step.

I pushed through the darkness scattering into the wind along with the ash.

Between Jeok Cheongang’s quiet footsteps behind me and the countless strange rocks still collapsing around us, I sensed someone’s presence.

No.

I saw it.

> **System**
>
> **Lv. 155 Mutated Guardian Spirit**

The fur that had once shone silver even in darkness and the blue-white eyes that had been as clear as the Sacred Land’s pond had both turned black.

Its fangs, grown twice as long, flashed at us.

—Grrrrr.

A low growl filled with ferocity.

Then came a movement like a flash of light.

Screeeech!

Along with its blurred form, more than ten jang of distance vanished. Its blood-soaked forepaw struck the ground, and its enormous body sprang upward.

Pop.

Toward the giant body casting a shadow over our heads, Jeok Cheongang and I unleashed our full-strength strikes.

Remembering the request he had given us before he left.

*Kill me. Without the slightest hesitation.*

And we kept that promise.

Shhhk. Slash!

* * *

It was somewhere deep and cold.

Not a single point of light could reach it, and not even the faintest warmth could be felt.

*He* lay curled up there, sensing the presence of death that would soon arrive—or perhaps had already arrived.

Then, at some point, he suddenly felt a warm presence and opened his eyes.

No. It was not warmth. It was heat.

And waiting for him in his blurred vision was someone with a familiar face.

“Jin Tae… kyung.”

A cracked voice slipped between his lips.

The young man who had been quietly staring at Baeksang, now fully awake, answered calmly.

“Yes.”

And with that single word, Baeksang knew that everything was over.

Perhaps it was because of the sunlight visible over Jin Taekyung’s shoulder.

*Yes. So it came to this in the end.*

The words echoed inside his mind.

Baeksang gazed up at the blue sky where the storm clouds had vanished.

It was strange. He had lost everything he had sought, yet he felt no despair.

Only emptiness.

“What happened to the Southern Heaven Demon Empress?”

The answer he received was short.

“She’s dead.”

“The rift must have disappeared as well.”

“……Yes.”

Along with that hesitant answer, Jin Taekyung’s head moved.

His gaze lingered briefly on the enormous tiger lying collapsed nearby.

No.

What Baeksang saw in that moment was countless corpses of beasts and humans.

“Let me ask you one thing.”

Jin Taekyung’s voice continued, sunk deep with gravity.

“Did you know from the beginning that this was how it would turn out?”

Baeksang looked at the corpses filling every direction with hollow eyes.

Then he answered.

“Yes. I knew.”

“……!”

Jin Taekyung clenched his teeth and glared at Baeksang. Baeksang did not avoid the gaze, where flames seemed to pour down in streams.

“To be precise, I learned a few months ago, after receiving a letter from the Central Plains.”

The letter had come from Henan. Along with a proposal to join the Murim Alliance, which would soon be established, it contained a detailed account of the series of events that had taken place in Hubei.

“That was when I realized why Dark Heaven had reached into Nanman, which belonged to the Outer Lands rather than the Central Plains. I realized what the grand plan spoken of by the Southern Heaven Demon Empress was.”

“And even knowing that…”

“I followed orders. I had already ceased to be a human being and become a monster.”

They said that ten years was enough to change the mountains and rivers. Sometimes earthquakes struck and tore down mountains, while violent floods twisted the course of rivers.

Baeksang had spent more than forty years amid earthquakes and floods, gradually becoming a monster that had lost his heart.

Because of the grief of losing his only child.

Because of his desire for revenge against the people of the Central Plains who had caused his child’s death.

But that was not all.

“After the Great Faction War, I hated the Demonic Path more than anyone. If I was a turncoat the Central Plains could never forgive, then they were enemies who had to die.”

Jin Taekyung let out a hollow laugh as he listened to Baeksang.

Dark Heaven and the Demonic Cult were branches of the same tree, with only their limbs differing.

If Baeksang had hated the Demonic Path, he could never have joined forces with Dark Heaven—the ones who had killed his child.

And yet Baeksang had joined hands with the Southern Heaven Demon Empress and brought about this catastrophe.

He had stood by while Dark Heaven opened the rift. Even knowing that countless deaths would follow, he had issued a general mobilization order and drawn nearly ten thousand warriors and beasts into the Inner Palace.

To offer them as living sacrifices.

“You fucking idiot. And you call that something worth saying now…”

For some reason, Jin Taekyung’s words suddenly trailed off.

Baeksang’s bloodstained lips moved.

“Yes. To me, there was something more important than hatred—more important than anything else.”

At that exact moment, someone’s image flashed through Jin Taekyung’s mind.

It was also why the eyes revealed above the mask had felt so familiar, as though he had seen them somewhere before.

“……Baekhwi.”

It was not Jin Taekyung who said it.

Baeksang lifted his blurred eyes and looked toward the figure approaching from the distance.

A huge man drew near with unsteady steps.

Despite Jeok Cheongang’s attempts to stop him, the Beast Miao King came right up to them and asked with a groan.

“Was that child alive?”

Baeksang weakly nodded, and that was enough for the Beast Miao King.

He knew what that child had meant to Baeksang. He knew what his sworn younger brother could do for his only child.

That was why he could not help but feel more sorrow and anger than anyone else.

“Why? Why did you not tell me? Why!”

“I did not want the Palace Lord—my hyung—to die.”

“……!”

“And Hwi… that child. I would have lost him all over again.”

Memories of the past faintly flickered through Baeksang’s eyes.

On the day he first encountered the darkness, he had flatly refused the Southern Heaven Demon Empress’s proposal to join hands.

That was before he heard that his child, whom he had believed the Great Snow Fiend had killed, was still alive.

“I accepted the Southern Heaven Demon Empress’s proposal, and I believed her promise that she would let Hwi live once the grand plan was over.”

He had believed her.

No—he had had no choice but to suppress his distrust.

There had been no other way to reunite with his only child.

After that, whenever his resolve wavered, he went to see the Southern Heaven Demon Empress.

He went to see the face of his child, kept alive by Dark Heaven’s sorcerers and sunk in a deep sleep.

“But at the same time, I knew. I knew what I was doing, and how many people would die because of this choice.”

That was why he created the Baekcheon Unit.

Not for himself, but for someone else—for the hope that he would stop this catastrophe.

“That was something I could not do.”

A child might kill a parent, but there was no parent who could kill their child.

Baeksang was a father.

Even if he could return to that moment dozens or hundreds of times, his choice would remain the same.

Cough.

Baeksang spat up blood and lifted his blurred eyes toward the Beast Miao King.

At that moment, a memory of the saddest and happiest day of his life at once flickered in his eyes.

*Yes. It was that day.*

The day he lost his beloved wife and gained the child he would come to love more than anyone else, Baeksang had cried.

He had sat facing his one sworn elder brother and drunk fruit wine as though it were his last day.

Just as he had decades later, on the day the Southern Heaven Demon Empress came to him.

“I have one last request.”

Baeksang continued with a faint smile.

“Please kill me, hyung.”
```
