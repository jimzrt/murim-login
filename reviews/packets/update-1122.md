<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1122.txt",
      "sha256": "c015f0241d5f97782351febabecff3a1e983cebc0c1f91741bf912545094d1a0",
      "bytes": 11224
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "9f9949441aab5be650f7efdfbc9bfc9f19963f06898d3c95d9588601388ff1a5",
      "bytes": 1418
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "307189767337c5394589bdcaa7f59f3e28cdf1da9d380fecae4d63447025be4b",
      "bytes": 245178
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "01b39b977ac9eb98fa9088b558b7cbb89566615bb5b5330c74805370bc27a3a2",
      "bytes": 944
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "97566fdfd8c93f77b7f8055d7300aadfdf993c78690263e61954f22a4b89aa02",
      "bytes": 1230
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "e7662fec45b6a4c4c302c4e511b55d52d9109a6993c40e1c17ffcc12c12485b8",
      "bytes": 760
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "e2843b217a176fe1d083ea10916ddc335ea1cffaa84a92c6db98b631aa2916f6",
      "bytes": 1513
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "492525e2a2d9f78746957246ee9195513d31fdae2b563b88a033433c65908fca",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "7604691602ee23c4d5e703c6304ed6de4236c13e9f6a075ff2c579196dde7f70",
      "bytes": 623
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "fbe26e0ec5f89ce57df0b052ec3ff3869882eaa7728f4db5939e2d5122fb744c",
      "bytes": 289919
    }
  ],
  "estimated_tokens": 10578
}
-->

# Durable State Update — Chapter 1122

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
1 and safe_through 1122. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1122. Profile updates may replace only one
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
  "chapter": 1122,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1122,
    "continuity_sources": [1122],
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
    "The East Gate has fallen; Pa Ryun and Tae Gunak arrived with an army of about thirty thousand.",
    "Hyuk Mujin was struck in the chest and collapsed; his condition is unknown.",
    "An unidentified black-robed figure suspected to be a key Dark Heaven member displayed overwhelming power; the outcome is unknown.",
    "Cheongheoja confronted Pa Ryun, Tae Gunak, and the black-robed figure at the East Gate.",
    "Great Sir was still fighting Black Ghost during the East Gate confrontation.",
    "The Inner City is under siege; the Blood Lord breached its wall and sent the fanatics in to kill everyone inside.",
    "Jin Taekyung is alive but critically injured; he asked Jeok Cheongang to open a path.",
    "The Grand Mage is dead, killed by the Blood Lord, who claimed command of the Dark Heaven army."
  ],
  "continuity_sources": [
    1120,
    1121
  ],
  "open_questions": [
    "Will Hyuk Mujin survive his chest wound?",
    "Who is the black-robed figure, and what was the outcome of the attack at the East Gate?",
    "Who has not returned to the Inner City, and what happened to them?",
    "What happened to Great Sir and Black Ghost?",
    "Will Jin Taekyung and the others survive the Dark Heaven assault?"
  ],
  "safe_through": 1121,
  "temporary_decisions": [
    "Render 부각주 as “Vice Captain” when Taishan addresses Hyuk Mujin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 궁성     | **Bow Saint**                 | —              |
| 살성     | **Slaughter Saint**           | —              |
| 절정     | **Peak**          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 가주     | **Family Head**                              |
| 문주     | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 은인     | **Benefactor**                               |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 청해     | **Qinghai**            |
| 노부      | **this old man / I**                                            |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 시산혈해 | **sea of corpses and blood** | Description of the preceding months of bloodshed. |
| 내성 | **Inner City** | Fortified inner district of the Murim Alliance. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 동문 | **East Gate** | One of the Nanman Beast Palace's gates. |
| 서문 | **West Gate** | One of the Nanman Beast Palace's gates. |
| 흑귀 | **Black Ghost** | The Blood-Sword Demon Lord’s name for the Death Knights. |
| 대술사 | **Grand Mage** | Title of the veiled woman leading the white-robed mages. |

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
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 혈주 | 청풍 | hostile_opponent_to_newly_revealed_identity | Huashan's Invincible Divine Sword; Sword Saint's Disciple or grandson | mocking and taunting | Recognizes Cheongpung's public identity and needles him with his Sword Saint lineage while dismissing the added threat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 결사대 | commander_to_subordinates | you bastards | blunt and commanding | Jin orders the suicide squad to exploit the opening and wipe out the surrounding monsters. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 살성 | 청풍 | senior martial figure to younger companion | you | blunt and familiar | The Slaughter Saint scolds Cheongpung for disappearing without a word. |
| 청풍 | 살성 | younger companion to senior martial figure | old man | polite and familiar | Cheongpung apologizes and explains why he wandered off. |
| 혈주 | 대술사 | fellow servant of the same person | you; you bitch | insulting-casual | Blood Lord taunts the Grand Mage and uses a crude insult. |
| 대술사 | 혈주 | fellow servant of the same person | you | contemptuous-casual | The Grand Mage addresses the Blood Lord while rebuking him. |
| 진태경 | 혈주 | hostile_opponent_to_hostile_opponent | you; you son of a bitch | insulting-casual | Taekyung insults the Blood Lord while challenging his claim that he will kill him. |
| 궁성 | 살성 | allied martial masters | Slaughter Saint | formal-polite | The Bow Saint directly addresses him as 살성 and uses 당신 while urging him to stay and defend the South Gate. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1121
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure and formidable combatant who commands weapons telekinetically and absorbs blood to restore vitality; after killing the Grand Mage, he claims command of the Dark Heaven army.
- **Personality:** Cunning and controlling, he plans around opponents’ strengths and trusts his overwhelming power; his newly unrestrained madness leads him to defy the Lord of Heaven’s will and seize command for himself.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He has served the Lord of Heaven but now openly defies his will; he is fixated on killing Jin Taekyung, killed the Grand Mage, and recognizes Cheongpung from his connection to Sword Saint Mae Jonghak.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 1121
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, Sword Saint Mae Jonghak’s grandson and Disciple, a Supreme Peak master known as the Huashan Divine Dragon, creator of Mimi Step, and master of the Azure Dragon Pavilion; he has mastered the Slaughter Saint’s Ghost Illusory Slaughter Step and blended it with his Dark Fragrance Drift.
- **Personality:** Affable, dreamy, and childlike, with innocent curiosity, a deep love of martial arts, and compassion; guided by his grandfather’s righteousness and Taekyung’s chivalry, he meets danger with resolve and trusts Taekyung without wavering.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions; Taekyung is his true martial rival and the person whose way of life he admires, and the Slaughter Saint is his mentor in concealment and Ghost Illusory Slaughter Step.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1120
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1121
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and freely follows his own path rather than pursuing grand causes; he cares about protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1121
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1121
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃1122화



무너진 성벽을 등지고 선 수비군의 저항은 그 어느 때보다 장렬했고, 또한 격렬했다.

천신만고 끝에 살아남아 내성으로 퇴각한 그들의 머릿수는 오천 남짓.

온 사방을 새카맣게 물들인 수만의 광신도들에 비하면 고작이라는 표현이 어울릴 정도의 격차였지만, 그에 맞서 싸우는 최후의 결사대는 조금도 물러서지 않았다.

아니, 물러설 수 없었다.

자신들의 등 뒤에는, 이 무너진 성벽의 잔해 너머에는 시시각각 다가오는 죽음의 공포에 떨고 있을 수많은 백성이 있었으니까.

그러나 더는 물러설 곳이 없다 한들, 나아갈 수 있는 것 또한 아니었다.

콰드드득!

살이 갈라지고 새하얀 뼈가 드러난다. 격돌과 동시에 전장을 휘감은 붉은 피 안개 속, 고통에 찬 비명과 고함이 먹먹하게 울려 퍼졌다.

“크아아악!”

“버티게! 반드시 버텨야 하……!”

푹!

정수리를 쪼개는 도끼날과 함께 끊기는 외침.

힘없이 허물어지는 이는 지난 수십여 년간 청해성에서 협객으로 이름을 떨친 절정 고수였으나, 이 끔찍한 혼전과 죽음 속에서는 모든 것이 무의미했다.

어찌 그 한 사람뿐만이겠는가.

일문(一門)의 문주도, 여러 식솔을 거느린 가주도.

아직 채 솜털도 가시지 않은 어느 젊은 청년도.

광신도들의 눈먼 칼날에 휩쓸린 순간, 그저 한낱 고깃덩어리가 되어 쓰러질 뿐이었다.

퍼걱! 푸푸푹!

어쩌면 이 처절한 마지막 전투의 결과는, 시작하기도 전에 정해졌을지도 모른다.

결사대를 짓누르고 있는 피로는 이미 한계를 아득히 넘어선 지 오래.

오늘의 전투에서 지금껏 살아남았다는 것은 곧 강하다는 증거였으나, 그들의 앞에 놓인 현실은 의지로 극복할 수 있는 것이 아니었다.

남아 있는 기운, 병력의 숫자.

모든 것이 부족했다. 턱없이.

죽은 이들은 힘없이 지면을 나뒹굴었고, 살아남은 자들은 죽은 전우의 시체를 짓밟으며 밀려드는 적들의 모습에 본능적으로 몸을 떨 수밖에 없었다.

공포와 분노, 더불어 아무것도 할 수 없는 무력함을 느끼며.

아마도 그래서였을 것이다.

몸도 마음도, 온 세상도 칠흑 같은 어둠에 잠겨 가던 그때.

누군가가 피워 올린 불꽃이 더욱 환하게 빛난 것은.

화륵, 퍼어엉!

공기가 타오른다. 태양과도 같은 열기가 빗줄기를 증발시키고 광신도들을 집어삼켰다.

그리고 넘실거리며 나아가는 그 맹렬한 화염의 중심에, 타들어 가는 안광을 번뜩이는 불의 거인이 있었다.

“감히 그 누가!”

화왕(火王) 적천강은 성마른 포효와 함께 소매를 떨쳤다. 

거센 바람에 휩쓸린 화염이 강철을 녹이고 광신도들의 살과 뼈를 불살랐다.

“우리의 앞길을 막아서는가-!”

언제나 스스로를 노부(老夫)라 칭해 왔던 적천강이었으나, 이번만큼은 아니었다.

더는 혼자 걷는 길이 아니다.

이제, 함께 걷는 길이다.

적천강이 늘 외롭게 나아가야 했던 그 위태롭고 가파른 사선(死線)에는, 어느덧 그의 일부이자 전부가 되어 버린 한 사람이 곁에 있었다.

“물러서지도, 두려워하지도 말라!”

비틀거리는 진태경의 신형을 부축하며, 사방에서 달려드는 적들을 불태우며 적천강은 힘주어 외쳤다.

평소였으면 코웃음을 치며 피했을 칼날들이 전신을 스치고, 공력을 일으킬 때마다 뒤엉킨 혈도에서 불같은 고통이 전해졌으나 지금의 그에게 그런 것 따위는 상관없었다.

“길을 열어라-!”

진태경의, 하나뿐인 제자의 부탁이었다.

너무나도 무모한, 어쩌면 진정 마지막이 될지도 모를 부탁.

하지만 이미 생사의 기로에 선 제자의 청을, 늙은 스승은 거절할 수 없었다.

그리고 이는 비단 그 혼자만의 의지가 아니었다.

서걱!

눈부신 섬광과 함께 허공으로 솟구치는 수십여 개의 목.

때마침 울컥 솟구치는 핏물을 삼키던 적천강이 그 광경을 보며 흐릿하게 웃었다.

“이제 오다니. 느려 터졌군.”

돌아온 핀잔에, 살성(殺星)이 백지장처럼 창백한 안색으로 입을 열었다.

내성으로 퇴각하는 과정에서 대술사와 흑귀들을 막아서기 위해 고군분투한 그 역시, 이미 상당한 부상을 입은 후였다.

“환자가 안 보이길래 찾아 나섰지. 멱살이라도 잡고 끌고 오려고.”

“그래서, 어쩔 셈인가?”

슈확!

살성은 대답 대신 소도(小刀)를 내리그었다.

유령처럼 쾌속하고 정확한 일격에, 찰나의 공백을 메우며 들이닥치던 광신도들이 짚단처럼 와르르 허물어진다.

마치, 진태경의 상태를 확인한 순간 느꼈던 그의 마음처럼.

“더 늦기 전에…… 내가 앞장서지.”

살성의 나직한 대답에, 적천강의 가슴 한구석이 찌르르 울렸다.

어쩌면, 그는 지금 당장이라도 이 전장을 빠져나갈 수 있을 것이다.

고금제일의 살수니까.

그렇기에 살성이라 불리는 것일 테니까.

하지만 그와 더불어, 적천강은 무겁게 가슴을 짓누르는 무언가를 느끼며 이를 악물어야 했다.

‘더 늦기 전에.’

그렇게 말했다. 분명히.

또한 이것이 살성으로서가 아니라, 신의(神醫)로서 내린 진단이라는 것을 그는 본능적으로 깨닫고 있었다.

저 대답에 혹시 모를 희망이 아닌 절망이 담겨 있었다는 것도.

‘죽는다, 녀석이.’

도저히 믿을 수 없는, 믿고 싶지 않은 잔인한 진실.

그러나 자신의 팔에 붙들려, 혼절한 듯 축 늘어진 진태경의 모습을 멍하니 바라보던 적천강은 이내 주먹을 움켜쥐었다.

지금의 그들에게 있어, 남아 있는 선택지 따위는 없었다.

그저 모두가 온 힘을 다해, 최후가 될지 모를 마지막 불꽃을 피워 올릴 뿐.

그리고 그 불꽃의 크기는, 지금 이 순간에도 서서히 그 크기와 열기를 더해 가고 있었다.

솨아아악!

어디선가 불현듯 뻗어나와 공간을 뒤덮는 강기(罡氣).

보는 것만으로도 베일 것처럼 예리한 살성의 그것과는 달리, 바람처럼 자유롭게 느껴지는 강기의 그물은 적들을 휘감았다.

침착하고 부드럽게.

동시에 그 찰나의 느낌을 송두리째 잊게 만들 정도의 파괴력으로.

서걱, 푸화아악!

피 분수가 솟구친다.

힘없이 허물어지는 적들 사이로 나타난 궁성(弓星)의 손끝을 따라, 서문에서 펼쳐진 격렬한 전투 속에서 두 동강 난 활대가 쾌속하게 움직였다.

콰드드득!

비록 본래의 형태를 잃었으나, 애당초 그녀의 활은 결합과 해체를 통해 두 자루의 곡도(曲刀)로도 쓰여왔던 것.

일언반구조차 없이 폭풍처럼 광신도들을 휩쓸며 힘을 보태는 궁성의 뒤를 따라, 익숙한 얼굴 역시 모습을 드러냈다.

“은인!”

다급한 외침과 달리, 청풍이 펼치는 검결은 마치 화선지를 누비는 화공의 붓처럼 유려했다.

쉬쉬쉭!

노을을 닮은 자줏빛 강기가 한 움큼의 꽃을 그려 냈다.

아름답게 느껴지는 수십여 개의 매화는 광신도들에게 닿은 순간, 더욱 붉게 물들며 흐드러지게 피어났다.

“왜 네 녀석까지…….”

그리고 이 위험천만한 동행을 위해 적진 깊숙이 파고든 그를 살성이 만류하기도 전에, 저 멀리에서 울려 퍼진 함성이 전장을 집어삼켰다.

“……!”

“……!”

소리라는 것이 거인의 형태로 드러난다면 이랬을까.

이미 터져 나간 누군가의 고막마저 뒤흔드는 그 함성은 그만큼 거대했고, 한편으로는 악에 받친 듯 처절하기까지 했다.

그랬기에 함성의 근원지를 찾아 고개를 돌린 이들 모두가 눈을 부릅뜰 수밖에 없었다.

성치 않은 몸으로 진태경을 부축한 채 적들을 상대하던 적천강과 청풍도.

마침내 동문을 점령한 적들의 지원군이 도착했음을 직감한 살성과 궁성도.

그리고 그런 그들을 향해, 막강한 기운을 흩뿌리며 천천히 걸음을 옮기고 있던 한 사람.

아니, 괴물도.

“저건…….”

채 끝맺어지지 못하고 흐려지는 말꼬리.

뭐라 형용할 수 없는 표정으로 함성의 근원지를 바라보던 혈주가, 이내 폭소를 터트렸다.

“푸핫, 푸하하하하!”

시산혈해로 뒤덮인 전장에 조금도 어울리지 않는 커다란 웃음소리.

하지만 혈주는 아랑곳하지 않고 미친 듯이 웃어 젖혔다.

허리를 숙이고 배꼽까지 부여잡은 채, 마치 살아생전 이보다 재미있는 일은 듣도 보도 못했다는 듯이.

그리고 언제 그랬냐는 듯, 차갑게 굳은 얼굴로 고개를 들어 바라보았다.

저 멀리, 하늘을 찌를듯한 함성과 함께 다가오는 수많은 이들의 모습을.

지금껏 상대한 그 어떤 적들보다 나약하고 하찮은, 그렇기에 더욱더 그를 분노하게 만드는 저 빌어먹을 부나방들을.

“이런…… 정신 나간 것들을 보았나.”

혈주는 진심으로 의심했다.

그렇지 않고서야 지금 이 순간, 핏빛으로 물든 그의 동공에 비치고 있는 저 말도 안 되는 광경을 설명할 수 없을 것 같았으니까.

하지만 아무리 의심하고 또 생각해 보아도, 그는 이 문제에 대한 답을 찾을 수 없었다.

아니, 그것은 혈주가 진정한 불로불사(不老不死)의 힘을 손에 넣는다 하더라도 깨달을 수 없는 종류의 것이었다.

늙고, 힘없고, 혹은 너무나도 어린 저들이.

오직 일평생 짓밟히고 두려움에 떠는 운명을 타고난 약자들이 누군가를 지키기 위해 목숨을 건다는 것은, 그로서는 상상도 할 수 없었으니까.

하지만 그들은 여전히 그곳에 있었다.

필사의 각오와 차마 완전히 떨쳐내지 못한 두려움으로 뒤섞인, 굳은 얼굴과 떨리는 목소리로 함성을 내지르며.

조잡한 죽창과 녹이 슨 도끼를 온 힘을 다해 움켜쥔 채.

자신들을 위해 각자의 운명을 내건 이들을 돕고자, 일평생 순응해오던 운명을 거스른 이들이.

태어나 처음으로 자신들의 가족이 아닌 누군가를 지키고자 하는 수많은 백성(百姓)들이.

바로 오늘, 이곳에 있었다.

“감-히!”

그리고 미증유의 기운이 담긴 괴물의 포효가, 영원히 계속될 것만 같던 백성들의 함성을 짓누른 그 순간.

“……해라.”

극소수의 사람만이 들을 수 있는 희미한 음성과 함께, 스승의 품에서 온 힘을 다해 눈꺼풀을 들어 올린 진태경이 힘겹게 말을 이었다.

“조용히 좀 해라…… 이 시벌 놈아.”
```

## Final English reading copy

```markdown
# Chapter 1122

The defenders at the backs of the collapsed walls fought more fiercely and more valiantly than ever.

After surviving against impossible odds and retreating to the Inner City, they numbered a little over five thousand.

Compared to the tens of thousands of fanatics blackening the land on every side, the gap was so vast that *a mere handful* seemed an apt description. Yet the last-ditch defenders who stood against them didn’t give an inch.

No—they couldn’t.

Behind them, beyond the rubble of the fallen walls, countless civilians trembled before the specter of death drawing closer by the second.

But even if there was nowhere left to retreat, that didn’t mean they could advance.

KRRRUNCH!

Flesh split, revealing white bone. Amid the red mist that swirled over the battlefield at the moment of impact, anguished screams and shouts rang out, muffled and dull.

“Graaaagh!”

“Hold the line! We have to hold—!”

Stab!

The shout ended with an axe blade cleaving through the crown of his head.

The man who crumpled to the ground had been a Peak master renowned as a hero of Qinghai for decades. But in this horrific melee, amid all this death, none of that meant anything.

And he wasn’t the only one.

The Sect Leader of a school. The Family Head of a household surrounded by relatives.

A young man whose downy cheeks hadn’t even lost their softness.

The moment the fanatics’ blind blades swept them up, they became nothing more than lumps of meat, collapsing to the ground.

CRUNCH! Stab-stab-stab!

Perhaps the outcome of this desperate final battle had been decided before it even began.

The exhaustion crushing the defenders had long since gone far beyond its limit.

Surviving this long in today’s battle was proof of their strength. But what lay before them couldn’t be overcome by sheer will.

Their remaining energy. The number of soldiers.

They were short on everything. Desperately short.

The dead rolled limply across the ground. Those still alive could only tremble on instinct as they watched the advancing enemy trample over the bodies of their fallen comrades.

They felt fear and anger, along with the helplessness of being unable to do anything.

Perhaps that was why.

When their bodies, their hearts, the whole world around them seemed to sink into pitch-black darkness—

A flame kindled by someone shone all the brighter.

Fwoosh—BOOM!

The air caught fire. Heat like the sun evaporated the rain and swallowed the fanatics whole.

At the heart of the fierce flames, surging forward in waves, stood a giant of fire, his burning eyes flashing.

“Who dares!”

With a furious roar, Jeok Cheongang, the Fire King, swept his sleeve.

The flames, whipped up by a fierce wind, melted steel and burned the fanatics’ flesh and bones.

“Stand in our way?!”

Jeok Cheongang had always referred to himself as “this old man,” but not this time.

He wasn’t walking alone anymore.

Now, they walked together.

Along the perilous, steep path to the brink of death that Jeok Cheongang had always been forced to walk alone, there was now someone at his side—a man who had become both a part of him and his whole world.

“Don’t retreat! Don’t be afraid!”

Supporting Jin Taekyung’s unsteady frame as he burned the enemies rushing in from every direction, Jeok Cheongang shouted with all his might.

The blades he’d normally have scoffed at and dodged grazed his body. Every time he summoned his internal energy, tangled acupoints sent pain blazing through him. But none of that mattered to him now.

“Open a path!”

It was a request from Jin Taekyung, his one and only Disciple.

A reckless request. One that might truly be his last.

But the old Master couldn’t refuse his Disciple, already standing at death’s door.

And this wasn’t the will of Jeok Cheongang alone.

Slice!

Dozens of heads shot into the air in a dazzling flash.

Jeok Cheongang swallowed the blood that suddenly surged into his mouth, then watched the sight with a faint smile.

“Took you long enough. You’re slow as hell.”

At the familiar reproach, the Slaughter Saint spoke, his face pale as a sheet.

He, too, had suffered serious injuries while fighting to hold back the Grand Mage and the Black Ghosts during the retreat to the Inner City.

“I couldn’t see the patient, so I went looking. Figured I’d drag him back by the collar.”

“And what do you intend to do?”

SHWICK!

The Slaughter Saint answered by bringing down his small knife.

His strike was as swift and precise as a ghost. The fanatics rushing in to fill the momentary gap crumpled like bundles of straw.

Just as his heart had crumpled when he saw Taekyung’s condition.

“Before it’s too late…I’ll take the lead.”

At the Slaughter Saint’s quiet reply, something tightened in Jeok Cheongang’s chest.

Perhaps the man could escape this battlefield right now.

He was the greatest assassin of all time.

That had to be why they called him the Slaughter Saint.

And yet Jeok Cheongang gritted his teeth, feeling something heavy press down on his heart.

*Before it’s too late.*

That was what he’d said. Clear as day.

Jeok Cheongang instinctively understood that this wasn’t a diagnosis from the Slaughter Saint, but from the Divine Physician.

And that the reply had held not the faintest hope, but despair.

*He’s going to die.*

A cruel truth too hard to believe, too hard to accept.

But as Jeok Cheongang stared blankly at Jin Taekyung, limp in his grasp as if unconscious, he clenched his fist.

There were no choices left for them now.

All they could do was give everything they had and kindle one last flame—perhaps their final one.

And even as they stood there, that flame was slowly growing larger and hotter.

SHWAAAA!

Force suddenly shot out from somewhere, spreading across the space.

Unlike the Slaughter Saint’s Force, so keen it seemed it could cut you just by looking at it, this web of Force felt as free as the wind. It wrapped around the enemies.

Calmly. Gently.

With a force so devastating it wiped away even that brief impression.

Slice—SPLAAASH!

A fountain of blood burst into the air.

Among the enemies crumpling to the ground, the Bow Saint appeared. Following the movement of her fingers, the broken bowstaff—split in two amid the fierce battle at the West Gate—moved with blinding speed.

KRRRUNCH!

Though it had lost its original shape, her bow had always been used in both forms: assembled, or separated into a pair of curved swords.

The Bow Saint swept through the fanatics like a storm, without a word. Close behind her, another familiar face appeared.

“Benefactor!”

Despite his urgent shout, Cheongpung’s sword technique moved as gracefully as a painter’s brush across white paper.

SHSHSHK!

A handful of purple Force, the color of sunset, sketched out flowers.

The dozens of plum blossoms seemed beautiful—until they touched the fanatics. Then they turned an even deeper red and bloomed in a glorious spray.

“Why’d you have to come along too…?”

The Slaughter Saint hadn’t even had time to stop him from plunging deep into enemy lines for this perilous journey when a roar from far away swallowed up the battlefield.

“……!”

“……!”

If a sound could take the shape of a giant, would it look like this?

The roar was so immense it shook even the eardrums of someone whose hearing had already burst. And there was a desperate, almost spiteful edge to it.

Everyone who turned to find its source could only stare, wide-eyed.

Jeok Cheongang and Cheongpung, wounded themselves, supporting Jin Taekyung as they fought off their enemies.

The Slaughter Saint and Bow Saint, realizing that the enemy reinforcements who had finally taken the East Gate had arrived.

And, walking slowly toward them as he scattered an overwhelming aura—

One man.

No, one monster.

“That’s…”

The words trailed off before they could be finished.

Watching the source of the roar with an indescribable expression, the Blood Lord suddenly burst into laughter.

“Pfft—hahahahaha!”

His booming laughter didn’t belong on a battlefield covered in a sea of corpses and blood.

But the Blood Lord didn’t care. He laughed like a madman.

Bent over, clutching his stomach, as if he’d never heard anything funnier in his life.

Then, as abruptly as he’d started, he lifted his head and looked over with a cold expression.

From far away came a host of people, shouting as if to pierce the heavens.

More pathetic and insignificant than any enemy he’d faced so far—and all the more infuriating for it. Those damn moths flying into the flame.

“What in the… Have I ever seen such a bunch of lunatics?”

The Blood Lord genuinely wondered if they had lost their minds.

Otherwise, he couldn’t explain the absurd sight reflected in his blood-red eyes.

But no matter how much he questioned it or thought it over, he couldn’t find an answer.

No—even if the Blood Lord gained the power of true immortality, he could never understand it.

That the old, the weak, and the very young—

The weak, born to spend their whole lives being trampled and trembling in fear, would risk their lives to protect someone.

He couldn’t even imagine it.

And yet they were still there.

They raised their voices, their faces set and their voices trembling, a mixture of desperate resolve and fear they couldn’t quite shake.

They gripped crude bamboo spears and rusty axes with all their strength.

They had spent their lives yielding to fate. Now they were defying it, trying to help those who had staked their own fates on protecting them.

Countless civilians, seeking for the first time in their lives to protect someone beyond their own families.

They were here.

Today. Right here.

“How—dare you!”

And then, as the monster’s roar, filled with an unprecedented aura, crushed the civilians’ seemingly endless shouts—

“…down.”

With a faint voice only a handful of people could hear, Jin Taekyung forced his eyelids open in his Master’s arms and struggled to speak.

“Would you shut up already…you son of a bitch.”
```
