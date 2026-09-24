<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0972.txt",
      "sha256": "ccee5ba3df71e448d2eee8e1effaf3f2c0ccc1492a8ab126b375cc737f721d4d",
      "bytes": 13362
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "c8b77055f0c736c5a510390a8f2032b69a68331c760a9bd73ddab7674b2649d4",
      "bytes": 1696
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "65892110351fce017f8020b13720d8c5e71418799da1db239060ea308ecc01e4",
      "bytes": 235501
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "5fad868d973b0669ea449fcb495b05580049409728b1b71015bcd332e6fa19cb",
      "bytes": 759
    },
    {
      "path": "characters/Jamukha.md",
      "sha256": "01e9b69508147a63cc69bead0ea2e46ae18fa2eacecd272119600b39c76be4c1",
      "bytes": 574
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "501345270f62d5346d523c731b1349b3e2c3b95c5ee9122c5b537c1d9934a180",
      "bytes": 1204
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "2b1f6a1899b99ab7a26891ab4f661fb4a328fd012f1c953fa5b7320693141f76",
      "bytes": 1481
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "c0a911977ebf9bd73543a9dc730ca72267c8d53464e5cb062afeea42c26922f7",
      "bytes": 622
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "7d9813734fcd8558edd3c9b89841fbb077d8b574e8a8caa5a57a6d5338ef12db",
      "bytes": 778
    },
    {
      "path": "characters/Peng Cheolhu.md",
      "sha256": "b9091263201294a92aff87b0bf4ffeaadbfa42adaba5a5611e1727649625a2c4",
      "bytes": 898
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "473e7916116ffb8b77eb1bd759ddad2da0aecf21857fc66c8b7f4ef53077786b",
      "bytes": 270884
    }
  ],
  "estimated_tokens": 11530
}
-->

# Durable State Update — Chapter 972

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
1 and safe_through 972. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 972. Profile updates may replace only one
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
  "chapter": 972,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 972,
    "continuity_sources": [972],
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
    "Taekyung has returned after two years away and intervened to save Jin Mukyung, Cheol Mubaek, and Wipeng; their conditions remain unknown.",
    "Taekyung arrived severely exhausted but has recovered enough from his effort to save Mukyung to move and fight.",
    "Murong Baek is the North Heaven Demon Lord and a Dark Heaven agent; Jamukha is with him at the gorge.",
    "The Bow Saint and Jeok Cheongang have joined Taekyung; the Bow Saint’s attack killed hundreds of nomads and helped the Hebei Peng Family break free of its encirclement.",
    "The Murong Family betrayed Peng Cheolhu, who was left alive beneath rubble; his current condition is unknown.",
    "The North Heaven Demon Lord has swallowed a red pill, and Taekyung’s spear is flashing behind him; the result of their confrontation is unknown.",
    "Taekyung says the Eastern Heaven Demon Lord provided information that helped him discover Dark Heaven’s plan centered on the Imperial Palace.",
    "The Emperor remains gravely ill with Blood Soul Gu; the treatment said to require him to die once remains unresolved."
  ],
  "continuity_sources": [
    971
  ],
  "open_questions": [
    "What effect will the North Heaven Demon Lord’s red pill have, and what will happen in the confrontation?",
    "What are the conditions of Mukyung, Cheol Mubaek, and Wipeng?",
    "What is Peng Cheolhu’s condition beneath the rubble?",
    "Can the Emperor be treated for Blood Soul Gu, and what does the treatment requiring him to die once entail?"
  ],
  "safe_through": 971,
  "temporary_decisions": [
    "Use “hyung” for 진태경’s address to his older brother."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 무신     | **Martial God**               | —              |
| 궁성     | **Bow Saint**                 | —              |
| 벽력도왕   | **Thunderbolt Saber King**    | Peng Cheolhu   |
| 삼성     | **Three Saints**    |
| 열화문    | **Fire Gate Clan**               |
| 하북팽가   | **Hebei Peng Family**            |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 산서     | **Shanxi**             |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 노부      | **this old man / I**                                            |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 자무카 | **Jamukha** | Khan of the western grasslands and the steppe army’s practical leader. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 열화신공 | **Fire Gate Divine Technique** | Secret internal cultivation technique of the Fire Gate Clan, preserved through one-person succession without leakage. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 절강성 | **Zhejiang Province** | Province where the Geumwa Merchant Group ranks among the top three merchant groups. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 절강 | **Zhejiang** | Region from which the boat travels east. |
| 소평 | **So Pyeong** | Alliance office worker assigned to prepare a report. |
| 무적자 | **The Invincible** | Taekyung's desired status as an untouchable protector. |
| 사냥개 | **hunting dog** | Jin's demeaning metaphor for Ares personnel who obey Go Jun. |
| 북천 | **North Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 신강 | **Xinjiang** | Region beyond Qinghai described as the domain of the Demonic Path. |
| 케식 | **Keshik** | Elite warriors serving the Golden Clan. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 벽력도왕 | rival_martial_master_to_rival_martial_master | Virility Saber King | insulting and taunting | Jeok coins 정력도왕 as a taunting replacement for the established title. |
| 벽력도왕 | 적천강 | rival_martial_master_to_rival_martial_master | Jeok Cheongang | boisterous and hostile-teasing | The Thunderbolt Saber King calls Jeok by name before their argument escalates. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 벽력도왕 | 진태경 | elder martial master to younger rival | you | boisterous and confrontational | Peng addresses Taekyung as 네놈 while discussing Peng Dojin. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 진태경 | 북천마군 | hostile opponents | you | casual, taunting, and profane | Taekyung teases and insults him during their standoff. |
| 적천강 | 북천마군 | former battlefield adversaries | you; you pup | blunt, familiar, and taunting | Jeok addresses him informally while challenging his alliance with Dark Heaven. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 971
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jamukha.md

# Jamukha (자무카)

- **Safe through:** Chapter 971
- **Aliases:** None
- **Role:** Jamukha is the ruler of the western steppe and a former eastern-steppe chieftain recruited into Dark Heaven by Murong Baek.
- **Personality:** Patient and driven by a long-standing desire to avenge his defeat by Peng Cheolhu.
- **Voice:** Not established
- **Relationships:** Peng Cheolhu defeated him more than fifty years ago; Murong Baek spared him, recruited him into Dark Heaven, and commands him as a subordinate.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 971
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and says they have shared everything since he accepted him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 971
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor has appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and learning to trust his allies rather than carry every burden alone.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 971
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 948
- **Aliases:** None
- **Role:** An unidentified legendary martial artist regarded as a pinnacle above the Ten Kings; more than fifty years ago, he defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, Mae Jonghak received several teachings from him, and he left the Bow Saint a letter describing a chosen one; the Bow Saint says he chose her, while his identity, whereabouts, and possible connection to Cheon Taemin remain unknown.

### Peng Cheolhu.md

# Peng Cheolhu (벽력도왕)

- **Safe through:** Chapter 969
- **Aliases:** Thunderbolt Saber King
- **Role:** Peng Cheolhu is the Thunderbolt Saber King, a Ten Kings master and Great Hero of the Hebei Peng Family.
- **Personality:** Boisterous, hot-tempered, argumentative, and protective toward those connected to his close friend Hong Dao; relentlessly disciplined in training, having continued every day after the Great Faction War.
- **Voice:** Loud, blunt, confrontational, and prone to disguising embarrassment or retreat as serious martial instruction.
- **Relationships:** Long-standing rival and friend of Jeok Cheongang; close friend of Hong Dao; protective toward Hong Dao's Disciple Unnamed; father of Peng Cheolyeong; longtime friend and former youthful rival of Murong Baek, who has now betrayed and attacked him.

## Korean source

```text
＃972화



적천강과 진태경.

진태경과 적천강.

모든 것이 시작된 그 순간, 두 스승과 제자는 마치 한 몸처럼 움직였다.

그리고 단 한 걸음 만에 전신을 불사를 듯이 가까워진 열기를 느끼며, 북천마군은 다시금 깨달았다.

자신의 선택이 옳았다는 것을.

예상했던 것과 한참 뒤틀린 이 계획을 성공시키기 위해서는, 한시라도 빨리 그에게 주어진 모든 것을 활용해야 한다는 것을.

화아악.

뜨겁다. 눈앞이 붉게 물든다.

느려진 세상 속, 북천마군은 전신이 타들어 가는 듯한 열기를 느꼈다.

하지만 그것은 장장 삼백여 년간 이어져 내려온 열화신공(烈火神功)의 위력 때문만이 아니었다.

콰아아아아.

오직 북천마군만이 들을 수 있는, 몸속 깊숙한 곳에서 울려 퍼지는 굉음.

그와 동시에 전신의 기운이 들끓어 올랐다.

용암과도 같은 열기가 수백 개의 혈도를 치달으며 당장이라도 부풀어 올라 터질 것처럼 용솟음쳤다.

지금껏 단 한 번도 사용하지 않았던 어느 귀물(鬼物)로부터 비롯된 거대한 힘의 파도가, 북천마군을 가로막고 있던 높고 단단한 벽을 일부나마 허물어트리고 있었다.

‘아아……!’

북천마군은 아득한 고통과 환희 속에서 신음했다.

붉게 물든 시야에 비친, 아니 보이지 않는 모든 것마저 느리고 선명하게 느껴지고 있었다.

바람. 공기. 그 안에 담겨 있는 기운.

그리고 그 모든 것을 산산이 부수며 들이닥치는 두 줄기의 화염 또한.

‘그래, 이런 기분이었나. 이런 것이었나.’

북천마군은 생각했다.

하늘에 닿은 무위로 십만마도 위에 군림하며 천하를 도모했던 천마(天魔)가, 그랬던 그를 쓰러트리고 천하를 안정시켰던 무신(武神)이 바라보았던 세상을 조금이나마 알 것 같다고.

아마도 그래서였을 것이다.

우우웅.

호신강기(護身罡氣)마저 녹여 버리는 열기 속에서도 북천마군이 웃을 수 있는 것은.

저들의 움직임이 한없이 느리고 약하게 보이는 것은.

‘고작 이 정도였더냐.’

서 있는 자리에 따라 보이는 풍경도 변하는 법.

이 순간, 잠력단의 힘으로 봉우리를 넘어 구름 위에 다다른 듯한 감각에 사로잡힌 북천마군은 오시(傲視)하고 있었다.

비좁은 협곡을 넘어 전장 전체를, 이름만으로도 천하를 떨어 울리는 늙은 노괴(老怪)와 젊은 신룡(神龍)마저 굽어보고 있었다.

그와 동시에 지금껏 수없이 머릿속에 그려 왔던, 그러나 꿈처럼 멀게만 느껴졌던 힘과 속도로 두 팔을 떨쳤다.

화아아악.

미증유의 기운에 일그러진 공간 속, 어느덧 검붉은 강기에 뒤덮여 형체조차 보이지 않는 창날과 주먹이 각기 다른 방향으로 쏘아졌다.

감히 절대자의 힘을 알아보지 못한, 어리석은 열화문의 후예들을 향해.

‘죽어라.’

붉게 달아오른 북천마군의 시야에, 믿을 수 없을 만큼 강대한 힘 앞에서 눈을 부릅뜬 적천강과 진태경의 모습이 비쳤다.

그런 그들을 파도처럼 덮쳐가는 검붉은 강기도 함께.

콰아아아아앙!

협곡 전체가 뒤흔들렸다. 크게 부풀어 오르며 폭발한 충격파가 반경 십여 장을 휩쓸었다.

아니, 빼앗고 집어삼켰다는 표현이 더욱 어울렸다.

아득한 섬광과 굉음은 협곡 안에 있던 이들의 시각과 청각을 강탈했고, 충격파가 미치는 범위 안에 모든 것들이 형태를 지키지 못하고 지워졌으니까.

드드드드득!

힘의 여파를 감당하지 못한 암벽의 일부가 무너져내렸다.

사방에 고여 있던 핏물도, 수많은 시체도 먼지가 되어 사라진 그곳에서 북천마군은 천천히 호흡했다.

한바탕 쏟아냈음에도 몸속 깊숙한 곳에서 끊임없이 솟아오르는 힘을, 마치 천재지변과도 같은 재앙을 두 손으로 직접 펼쳐 낸 자신에 대해 전율했다.

그리고 문득 고개를 돌려, 숨 막히는 정적과 먼지구름에 휩싸인 저 너머 어딘가를 바라보았다.

아니, 느꼈다.

이 끔찍한 재앙 앞에서도 살아남은, 아직 완전히 사라지지 않은 인기척들을.

“용케도 살아남았군. 그래, 응당 그래야지.”

북천마군의 음성은 담담한 동시에 여유로웠다.

잠력단의 효능으로 불과 촌각 전의 자신을 훌쩍 뛰어넘는 무위를 얻은 그였지만, 단 일격에 승부를 볼 수 있을 거라는 기대는 처음부터 하지 않았다.

상대는 오십여 년 전보다도 강해져 돌아온 구화산의 노괴였고, 그 제자는 후기지수를 넘어 이 광활한 천하에 발자취를 남기고 있는 한 사람의 당당한 거인(巨人)이었으니.

그럼에도 북천마군이 여유로울 수 있는 것은, 이 순간에도 터질 듯이 맥동하는 이 거대한 힘의 크기를 누구보다 잘 알고 있기 때문이었다.

설령 또 다른 누군가가 개입한다 해도, 그 사실은 변하지 않을 터였다.

바로 지금처럼.

후웅. 콰아앙!

찰나의 순간, 보이지 않는 사각(斜脚)에서 소리 없이 들이닥친 기운의 응집체가 북천마군이 휘두른 창날에 부딪혀 튕겨 나간다.

곳곳이 갈라지고 허물어진 암벽 위, 삼십여 장 높이의 그곳에 우뚝 선 인영을 바라보는 북천마군의 입가에 흐릿한 미소가 맺혔다.

“고생이 많구려. 궁성(弓星).”

북천마군은 지금의 일격을 받아내며 다시금 확신할 수 있었다. 현재 자신의 무위는 삼성(三星)보다 윗줄에 있다는 것을.

무적자(無籍者), 혹은 절대자라 불리던 이들의 영역에 한 걸음이나마 발을 디뎠다는 것을.

카가가강!

화살이라 부르기에는 너무나도 크고 강력한 힘을 머금은 빛의 응집체.

뛰어난 절정 고수조차 일격에 격살시킬 무수한 빛의 소나기를 연달아 튕겨 낸 북천마군의 미소가 더욱 진해졌다.

“조금만 더 천천히 오지 그랬나. 서두르지 않고 충분한 여력을 남겨두었더라면 많은 것이 달라졌을 텐데.”

황도가 위치한 절강성에서 산서성까지의 거리는 장장 수천 리가 넘는다.

그리고 저들 세 사람이 그토록 먼 거리를 가로질러 이곳에 나타날 때까지 북천마군의 이목에 걸려들지 않았다는 것은, 전령이나 전서응보다도 신속하게 움직였다는 뜻이기도 했다.

촌각조차 아쉬워하며, 전투를 대비할 만한 제대로 된 휴식조차 없이.

그리고 그러한 짐작은, 북천마군에게 있어 곧 승리에 대한 확신을 심어 주기에 충분했다.

“안타깝지만, 되돌리기에는 늦었어.”

스아아아.

전신을 타고 아지랑이처럼 피어오르는 검붉은 기운.

극도로 유형화된 강기를 뚫지 못하고 튕겨 나가는 궁성의 공격을 바라보며, 북천마군은 그 어느 때보다 강렬한 고양감에 휩싸였다.

절대자.

오늘 이 자리에서만큼은 그가 절대자다.

저 먼지구름 너머에 쓰러져 신음하고 있을 열화문의 두 스승과 제자도, 궁성도 지금만큼은 자신의 상대가 될 수 없었다.

그들은 하나같이 지쳐 있었고, 그에게는 끊임없이 샘솟는 힘이 있었으니.

드득.

가볍게 내디딘 발끝에서 깊은 울림이 퍼져 나간다.

협곡 안의 모두를 얼어붙게 만든 거대한 힘.

한 인간이 지닐 수 있으리라고는 생각해 본 적 없는 미증유의 기운이 단전을 팽창시킨다. 수백 개의 혈도를 타고 치닫는다.

북천마군은 소리 내어 웃으며 생각했다.

지금이라면 무엇이든 할 수 있을 것만 같다고.

아니, 그럴 것이라고.

그리고 끝없이 뻗어 나간 북천마군의 감각이 협곡 전체를 휘감은 그 순간.

- 노야, 저 새끼 웃는데요?

- 놔둬라. 잠력단 좀 빨았다고 지가 천주(天主)라도 되는 줄 아나 보지.

아직 가라앉지 않은 먼지구름 속, 태연하게 대화를 주고받는 두 줄기의 전음(傳音)에 북천마군의 입가에 맺혀 있던 미소가 사라졌다.

- 어, 이제 안 웃는데요?

- 안 그래도 못생긴 놈이 정색까지 하니까 면상이 아주 좆 같구먼.

- 말씀을 왜 그렇게 하세요. 제 똘똘이가 얼마나 똘똘하게 잘 생겼는데.

- 알겠으니까 지금 당장 바지춤에서 그 염병할 손 떼라. 일장에 똘추로 만들어 버리기 전에.

북천마군의 눈동자가 깊게 가라앉았다. 숨길 수 없는 의문과 경악이 실린 그의 눈빛이 한 방향을 향해 움직였다.

- 어어, 이쪽 보는데요.

- 어쩌다가 얻어걸린 거겠지. 노부는 척 보면 척이니라.

- 한 번에 확 덮쳐야 하는데, 지금 들킨 거면 어떡해요? 그러지 말고 옆으로 좀 가 보세요.

- 안 그래도 그럴 생각이었으니 밀지 좀 마라. 감히 노부의 몸뚱어리에 손을 대?

- 그거 손 아닌데요.

- 어?

그 순간, 북천마군의 입꼬리가 파르르 떨렸다.

“나와.”

입술 사이로 흘러나온 나직한 한 마디에, 숨 막히는 침묵이 내려앉았다.

아니, 정확히는 그렇게 보였다.

- 나오라는데요. 아주 정확하게 이쪽을 보면서.

- 말하지 않았더냐, 찍은 것이 분명하다고.

- 아닌 것 같은데, 잠깐만. 지금 저희 전음 듣고 있는 거 아니에요?

- 약 좀 빨았기로서니 제깟 놈이 무슨. 절대 그럴 리 없다. 노부가 혁가 놈의 불알을 걸고 장담하지.

툭.

인내심의 끈이 끊어지는 소리와 함께, 북천마군의 악문 잇새 사이로 차가운 목소리가 흘러나왔다.

“참으로 안타깝군. 그자가 누구인지는 몰라도 불알을 잃게 될 테니.”

그리고 마침내, 기다리던 응답이 있었다.

퍼엉.

마치 검에 베인 것처럼 갈라지는 먼지구름 너머, 넝마가 된 옷차림으로 모습을 드러낸 적천강이 어깨에 묻은 흙을 털며 대꾸했다.

“상관없다. 혹시 몰라서 노부의 물건은 걸지 않았으니.”

쓸데없이 준엄한 얼굴로 낯부끄러운 말을 내뱉는 스승의 뒤로, 머리 서너 개는 더 큰 덩치의 제자가 떨떠름한 얼굴로 입을 열었다.

“왜 자리에도 없는 애 불알을 걸고 그래요. 어차피 쓸 데도 없는데 그냥 본인 거 거시면 되지.”

“그건 네 녀석도 마찬가지 아니냐?”

“아니, 선 넘으시네. 말씀을 왜 그렇게 하시…….”

콰아앙!

이어지려는 목소리를 집어삼키는 굉음.

그리고 이내 얼마 지나지 않아 들려오는 기침소리.

“콜록. 어우씨, 미세먼지 봐. 누가 짱깨 새끼 아니랄까 봐.”

“어허, 엄살떨지 마라. 열화문 위신 깎인다.”

“세상에, 여기서 더 깎일 게 남았어요?”

멀쩡하게 모습을 드러낸 진태경과 적천강의 모습에, 북천마군의 눈빛이 침잠하게 가라앉았다.

‘어떻게…….’

전력을 다한 것까지는 아니더라도, 칠 할 이상의 힘을 쏟아부은 일격을 피했다는 것은 충분한 여력이 있었다는 증거.

북천마군은 어느 순간 스스로에게 주어진 힘을 맹신했다는 사실을 인정할 수밖에 없었다.

그와 더불어, 눈앞의 적을 과소평가했다는 반성도 함께.

“자무카.”

북천마군의 입술 사이로 흘러나온 나직한 부름에, 그가 수십여 년간 부려 왔던 사냥개가 대답했다.

“하명하십시오. 주군.”

“더 이상 두고 볼 것 없다. 계획을 변경한다.”

“그 말씀은…….”

“더 이상의 방해는 용납하지 않는다. 일이 틀어지기 전에, 모든 전력을 다하여 놈들을 단숨에 쓸어버려라.”

전력을 다하라는 북천마군의 명령을, 자무카는 정확히 이해했다.

오늘 이 전장에서 벽력도왕과 하북팽가는 초대받은 손님이었으나, 뜻하지 않게 등장한 세 명의 초절정 고수는 불청객이다.

이미 주사위는 던져졌다. 판이 엎어지기 전에 승리를 확정 지어야 한다.

앞서 북천마군이 그러했듯이, 할 수 있는 모든 수단을 총동원해서.

“존명(尊命).”

짤막한 대답과 함께, 자무카는 망설임 없이 품 안에서 꺼낸 신호탄의 끈을 당겼다.

쉬쉬쉬쉭!

어둠 위로 솟아오르는 연기.

궁성이 신속하게 쏘아 보낸 빛의 화살이 그중 대부분을 휩쓸었으나, 허공에서 뿔뿔이 흩어진 일부마저 어찌할 수는 없었다.

퍼퍼퍼펑!

검게 물든 하늘 위를 화려하게 수놓은 불꽃.

주인의 명령에 따라 자신이 거느린 수많은 사냥개의 목줄을 풀어놓은 자무카는, 북천마군의 만류로 미처 복용하지 못했던 잠력단을 입안으로 털어 넣었다.

협곡 너머, 지금 막 신호를 확인한 케식들과 같이.

스륵. 스아아아.

붉은 아지랑이가 전장 곳곳에서 피어오르기 시작했다.
```

## Final English reading copy

```markdown
# Chapter 972

Jeok Cheongang and Jin Taekyung.

Jin Taekyung and Jeok Cheongang.

From the moment it all began, Master and Disciple moved as if they were one.

And as the heat drew close in a single step, hot enough to set his whole body ablaze, the North Heaven Demon Lord realized once more:

He had made the right choice.

To make this plan—which had gone wildly off course from what he’d expected—succeed, he had to use everything he’d been given as quickly as possible.

*Fwoosh!*

Hot. The world before him turned red.

As the world slowed, the North Heaven Demon Lord felt a heat that seemed to burn through his entire body.

But it wasn’t only the power of the Fire Gate Divine Technique, passed down for more than three hundred years, that made him feel that way.

*KABOOOOOM!*

A tremendous roar, audible only to the North Heaven Demon Lord, reverberated from deep within his body.

At the same time, the qi throughout his body surged.

Lava-hot energy raced through hundreds of acupoints, swelling and surging as if it might burst at any moment.

A colossal wave of power, born from some strange artifact he had never once used, was partly tearing down the high, sturdy wall that had always stood in his way.

*Ah…!*

The North Heaven Demon Lord groaned amid a haze of pain and ecstasy.

Everything in his reddened field of vision—or even things he couldn’t see—felt slow and vivid.

The wind. The air. The qi held within it.

And the two streams of flame rushing toward him, smashing everything in their path to pieces.

*So this is what it feels like. This is what it is.*

The North Heaven Demon Lord thought.

He felt he could almost understand the world the Heavenly Demon had seen as he ruled over the Ten Thousand Demonic Paths with heaven-reaching martial prowess and sought to conquer the world—and the world the Martial God had seen when he defeated him and brought peace to it.

Perhaps that was why he could smile, even amid heat so fierce it melted his Body-Protecting Qi.

*Whoooom.*

Perhaps that was why their movements looked so slow and weak.

*Is that all you’ve got?*

The scenery changed with the vantage point.

In that moment, seized by the sensation that the Temporary Strength Pill had carried him over the summit and above the clouds, the North Heaven Demon Lord looked down on them with disdain.

He surveyed the entire battlefield beyond the narrow gorge, even the old monster and the young Divine Dragon—men whose very names made the land tremble.

At the same time, he flung out both arms with a speed and power he had imagined countless times, yet always felt as distant as a dream.

*Fwoooosh!*

Space warped under the unprecedented energy. A spearhead and a fist, their forms obscured beneath dark crimson Force, shot in opposite directions.

Toward the foolish descendants of the Fire Gate Clan, who dared not recognize the power of an absolute being.

*Die.*

In the North Heaven Demon Lord’s red-hot vision, Jeok Cheongang and Jin Taekyung stared wide-eyed at the overwhelming power before them.

The dark crimson Force swept toward them like a wave.

*KABOOOOOM!*

The entire gorge shook. The shock wave swelled and exploded, sweeping everything within a radius of more than ten *zhang*.

No—“stole” and “swallowed” would have been better words for it.

The blinding light and thunderous noise robbed everyone in the gorge of sight and hearing. Everything within reach of the shock wave was erased, unable to hold its shape.

*Rrrrrumble!*

Part of the cliff collapsed, unable to withstand the aftershock.

The pools of blood and countless corpses scattered all around had vanished into dust. In their place, the North Heaven Demon Lord drew a slow breath.

He shuddered at the power welling up without end from deep inside him, even after that outburst—and at the thought that he himself had unleashed a calamity like a natural disaster with his own two hands.

Then he turned his head and looked somewhere beyond the choking silence and clouds of dust.

No—he sensed it.

The presences that had survived this horrific disaster, not yet entirely extinguished.

“You managed to survive. As you should have.”

The North Heaven Demon Lord’s voice was calm and relaxed.

The Temporary Strength Pill had given him martial prowess far beyond what he’d possessed only moments ago. Still, he had never expected to win with a single strike.

His opponent was the old monster of Mount Jiuhua, returned stronger than he’d been fifty years ago. And his Disciple had grown beyond a young prodigy into a towering figure, leaving his mark on this vast land.

Even so, the North Heaven Demon Lord could remain at ease because he knew better than anyone the size of the enormous power throbbing within him, ready to burst.

Even if someone else intervened, that wouldn’t change.

Just as it hadn’t now.

*Whoom! KABOOM!*

In the blink of an eye, a mass of concentrated energy struck the spearhead the North Heaven Demon Lord had swung, bouncing off from an unseen blind spot.

The North Heaven Demon Lord’s lips curved into a faint smile as he looked toward the figure standing atop a fractured, crumbling cliff, more than thirty *zhang* high.

“You’ve had a rough time, Bow Saint.”

The North Heaven Demon Lord had now taken the latest attack and confirmed it once more. His martial prowess was above the Three Saints.

He had set foot, if only by one step, into the realm of those called the Invincible or the absolute.

*KRAKAKAKANG!*

A mass of light packed with such tremendous power it could hardly be called an arrow.

The North Heaven Demon Lord deflected a barrage of those flashes, each powerful enough to kill even a skilled Peak master with one strike. His smile deepened.

“You should’ve come a little slower. If you’d taken your time and saved some strength, a lot might have turned out differently.”

The distance from Zhejiang Province, where the Imperial Capital stood, to Shanxi Province was well over a few thousand *li*.

And for those three to have crossed that distance and appeared here without catching the North Heaven Demon Lord’s attention meant they’d moved faster than a messenger eagle or a courier.

They had rushed here, unwilling to spare even a moment, without proper rest to prepare for battle.

That guess was enough to convince the North Heaven Demon Lord that victory was certain.

“Unfortunately, it’s too late to turn back now.”

*Shhhh…*

Dark crimson energy rose from his whole body like heat haze.

Watching the Bow Saint’s attacks bounce off without penetrating his highly condensed Force, the North Heaven Demon Lord was swept up in a stronger exhilaration than he’d ever felt.

An absolute being.

Here, today, he was the absolute being.

The two Master and Disciple of the Fire Gate Clan, who must be collapsed and groaning beyond that cloud of dust, and even the Bow Saint could not stand against him now.

They were all exhausted, while his power continued to well up without end.

*Crack.*

A deep rumble spread from the tip of his foot as he stepped forward lightly.

A colossal power that had frozen everyone in the gorge.

An unprecedented energy no one had ever imagined a human could possess expanded his dantian and raced through hundreds of acupoints.

The North Heaven Demon Lord laughed aloud, thinking:

*It feels like I could do anything right now.*

No—he could.

And just as the North Heaven Demon Lord’s senses stretched endlessly and wrapped around the entire gorge—

—Old Master, that bastard’s laughing.

—Leave him be. He must think he’s the Lord of Heaven just because he took a Temporary Strength Pill.

The North Heaven Demon Lord’s smile vanished as two voices exchanged words through Sound Transmission in the dust cloud that had yet to settle.

—Uh, he’s not laughing anymore.

—He was ugly to begin with, but now he’s scowling. His face looks like shit.

—Why would you say it like that? My little guy is handsome and looks plenty clever.

—All right, I get it. Take your damn hand off your pants right now, before I turn you into a eunuch with one palm strike.

The North Heaven Demon Lord’s eyes sank. His gaze, carrying unmistakable confusion and shock, turned in one direction.

—Uh, he’s looking this way.

—Must’ve just gotten lucky. This old man knows at a glance.

—We need to jump him all at once. What if he’s spotted us? Why don’t you move a little to the side?

—I was about to. Stop pushing me. How dare you touch this old man’s body?

—That’s not a hand.

—Huh?

At that moment, the North Heaven Demon Lord’s mouth twitched.

“Come out.”

At the low words that slipped between his lips, a breathless silence descended.

No—more precisely, it seemed to.

—He says come out. He’s looking right at us.

—Didn’t I tell you? He definitely guessed.

—I don’t think so. Wait, can he hear our Sound Transmission?

—So he took a little pill. So what? There’s no way that bastard can do that. I’ll stake that Hyuk bastard’s balls on it.

*Tap.*

As if the last thread of his patience had snapped, a cold voice slipped through the North Heaven Demon Lord’s clenched teeth.

“What a shame. Whoever that is, he’s going to lose his balls.”

At last, he received the answer he’d been waiting for.

*Poom!*

Beyond the dust cloud, which split as if a sword had cut through it, Jeok Cheongang emerged in tattered clothes. He brushed the dirt from his shoulder and replied:

“That’s fine. Just in case, I didn’t stake my own.”

Behind his Master, who’d uttered something so embarrassing with an unnecessarily solemn expression, his Disciple—several heads taller—spoke with an uneasy look.

“Why stake the balls of someone who isn’t even here? You won’t need them anyway. You might as well stake your own.”

“Isn’t that true of you, too?”

“Hey, now you’ve crossed a line. Why would you say—”

*KABOOM!*

A thunderous crash swallowed the words before they could continue.

And not long after, a cough sounded.

“Cough. Jeez, look at all this fine dust. Wouldn’t want anyone thinking you’re not a Chinese bastard.”

“Ahem. Don’t be a baby. You’ll bring shame on the Fire Gate Clan.”

“My God, is there even more shame left to bring?”

At the sight of Jin Taekyung and Jeok Cheongang standing there unharmed, the North Heaven Demon Lord’s gaze sank.

*How…?*

The attack hadn’t been at full power, but they’d dodged a strike backed by more than seventy percent of his strength. That proved they still had plenty in reserve.

The North Heaven Demon Lord had no choice but to admit that, at some point, he’d come to trust too much in the power he’d been given.

And with it came the realization that he’d underestimated the enemies before him.

“Jamukha.”

At the quiet call that slipped from the North Heaven Demon Lord’s lips, the hunting dog he’d commanded for decades answered.

“Give your command, my lord.”

“We won’t wait any longer. Change the plan.”

“You mean…”

“I will not tolerate any more interference. Before things go wrong, use every last bit of our strength and wipe them out at once.”

Jamukha understood exactly what the North Heaven Demon Lord meant by using every last bit of their strength.

Today, the Thunderbolt Saber King and the Hebei Peng Family had been invited guests on this battlefield. The three Supreme Peak masters who had appeared unexpectedly, however, were uninvited.

The die had been cast. They had to secure victory before the whole game was overturned.

As the North Heaven Demon Lord had just done, they would bring every means at their disposal to bear.

“Understood.”

With that curt reply, Jamukha pulled the cord of the signal flare he’d taken from his robes without hesitation.

*Fwish! Fwish! Fwish!*

Smoke rose into the night.

The Bow Saint’s arrows of light swiftly swept away most of the smoke, but even she couldn’t catch every wisp that scattered through the air.

*Poom! Poom! Poom!*

Fireworks blossomed across the blackened sky.

At his master’s command, Jamukha had let the countless hunting dogs under his command off their leashes. Now he tipped the Temporary Strength Pill he hadn’t been able to take because the North Heaven Demon Lord had stopped him into his mouth.

Beyond the gorge, the Keshiks who had just seen the signal did the same.

*Swish. Shhhh…*

Red heat haze began to rise throughout the battlefield.
```
