<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1037.txt",
      "sha256": "384c2086c1001afef4de9ad2931c8087c0fe77fa66476f1f79507efa1efa7827",
      "bytes": 18474
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "c14621dc93eae097e6353b83340418076a3661fc0f9ecc6f29dd8e8cfa56ac7b",
      "bytes": 1828
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "383045aaa550afcd5ef9913b67eee36e7dfcbd478f5edeb7be10bfbb7930e01e",
      "bytes": 240741
    },
    {
      "path": "characters/Blood-Sword Demon Lord.md",
      "sha256": "84ead2b33a0a937fc331b0a16d407409e31b6bfb29952fe773b448bbedc2f582",
      "bytes": 914
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "a0b2c67d4d0840f001c13478ef88f4d0831f4a904b873803b4d07891740fa46a",
      "bytes": 760
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "7e421e9029ed2fb2a802d7d81128322e1e0be7234a3c8afd631a0cf1fb99d4b5",
      "bytes": 1502
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "31906a0a01bee7e9bd12be15e6fd62cb421ed0240b402ebc9e63c5c95fe7b074",
      "bytes": 1823
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "0305d167cc7d167b932a97475d86627a9664928744797fa103fcc606f58c1a34",
      "bytes": 623
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "f70a6c9f6575d3dfb8be1488f9a5cdef91a0b1d7289ef6124b801b3e2f54393c",
      "bytes": 1161
    },
    {
      "path": "characters/Sima Gong.md",
      "sha256": "125a07472d7fe681e77edbc07925d7775ab6ed874517be7227731084fb60f463",
      "bytes": 778
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "9fcdc873075b9cb2d4039976a1b6c6915530d22e136ba779219b7eb6f324ba96",
      "bytes": 279401
    }
  ],
  "estimated_tokens": 14235
}
-->

# Durable State Update — Chapter 1037

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
1 and safe_through 1037. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1037. Profile updates may replace only one
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
  "chapter": 1037,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1037,
    "continuity_sources": [1037],
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
    "The Blood-Sword Demon Lord serves the Lord of Heaven and commands the invading army.",
    "The Blood-Sword Demon Lord commands more than thirty thousand soldiers and seven Black Ghosts.",
    "Four Black Ghosts, former Demonic Cult fiends, were destroyed by Heavenly Strike.",
    "Jeok Cheongang and Jin Taekyung are fighting on the battlefield.",
    "Roughly twenty white-robed followers take orders from the Lord of Heaven through an unnamed woman who served him more closely than the Blood-Sword Demon Lord.",
    "The Blood-Sword Demon Lord believes the Lord of Heaven distrusts him and is resolved to prove himself.",
    "The Blood-Sword Demon Lord is Chuk Banghyeol; Qi Sense showed his level rising from 170 to 180 as he approached.",
    "A white-robed figure invoked the Wind Ghost’s power and imbued the Blood-Sword Demon Lord with it; Taekyung identified this power as Magic.",
    "Taekyung now recognizes the Moving Formation, corrupted creatures, the rift, and the Black Ghosts as evidence of Magic.",
    "A veiled white-robed woman uses gravity magic against Taekyung to delay his advance toward Jeok Cheongang.",
    "Taekyung awakens his Middle Dantian and Will, and summons one hundred blades from his Inventory; their attack’s outcome is unresolved."
  ],
  "continuity_sources": [
    1035,
    1036
  ],
  "open_questions": [
    "What are the identity and purpose of the Lord of Heaven?",
    "Did Dark Heaven cause the Great Faction War?",
    "Who is the unnamed white-robed woman, and what is the white-robed followers’ purpose?",
    "How do the white-robed followers’ Magic and the Wind Ghost’s power work?",
    "How were the former Demonic Cult fiends made into Black Ghosts?"
  ],
  "safe_through": 1036,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 사마공    | **Sima Gong**      |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 사파     | **unorthodox faction**                           |                                                       |
| 문주     | **Sect Leader**                              |
| 일격     | **One Strike**                         |
| 귀가      | **your family**                                                 |
| 혈검마군 | **Blood-Sword Demon Lord** | Antagonist commanding the army advancing on the Great Snow Mountain. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 나려타곤 | **Narye tagon** | Humiliating idiom comparing a fighter's evasive roll to a lazy donkey rolling on the ground. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 신력 | **divine strength** | Superhuman strength attributed to Taekyung. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 흑룡도 | **Black Dragon Saber** | Sama Pyo's sobriquet. |
| 식경 | **half an hour** | Time limit given for the requested reports. |
| 황하 | **Yellow River** | River along which civilization began. |
| 흑야왕 | **Black Night King** | Epithet of Sima Gong, Sama Pyo's father and the Sect Leader who built the modern Black Dragon Demon Gate. |
| 일기당천 | **One Against a Thousand** | Title that temporarily increases Taekyung’s attributes and Intimidation when facing many enemies. |
| 검마 | **Sword Demon** | A Demonic Cult swordsman whose final technique is compared with One Annihilation. |
| 흑귀 | **Black Ghost** | The Blood-Sword Demon Lord’s name for the Death Knights. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 사마표 | 진태경 | prospective recruit to pavilion master | you | polite, controlled, and candid | Sama Pyo uses 자네 while asking about Taekyung's attitude and admitting his intention to use him. |
| 진태경 | 사마표 | pavilion master to prospective recruit | you / that guy | blunt, informal, and distrustful | Taekyung speaks to and about Sama Pyo with casual forms such as 녀석 and 저놈. |
| 사마표 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | formal but sardonic | Sama Pyo addresses Jin as 각주 while questioning his account of the incident. |
| 사마공 | 적천강 | unorthodox sect leader to senior martial master | Senior | formal and deferential | Greets Jeok Cheongang as 노선배. |
| 적천강 | 사마공 | senior martial master to longtime martial acquaintance | you | blunt and familiar | Uses direct, contemptuous language while teasing Sima Gong. |
| 진태경 | 사마공 | allied young martial artist to unorthodox sect leader | Great Hero Sima | polite and deferential | Addresses him as 사마 대협. |
| 사마공 | 진태경 | unorthodox sect leader to celebrated young martial artist | you | polite and familiar | Uses 자네 while speaking to Taekyung. |
| 사마공 | 사마표 | father to son | Pyo | intimate and familiar | Sima Gong calls him 표야 and 내 아들아. |
| 혈검마군 | 적천강 | former opposing martial masters | Senior Jeok | respectful and familiar | Addresses Jeok as 선배 while teasing him. |
| 적천강 | 혈검마군 | former opposing martial masters | you; you bastard | blunt and hostile | Uses 너 and 네놈 while confronting him. |
| 혈검마군 | 진태경 | enemy addressing a younger martial artist | you | familiar and measured | Uses 자네 while praising and assessing Taekyung. |
| 진태경 | 혈검마군 | young martial artist confronting an enemy | you | casual and challenging | Questions when the Blood-Sword Demon Lord and the Lord of Heaven appeared. |

## Listed compact profiles

### Blood-Sword Demon Lord.md

# Blood-Sword Demon Lord (혈검마군)

- **Safe through:** Chapter 1036
- **Aliases:** None
- **Role:** The Blood-Sword Demon Lord is a formidable martial master who commands the force advancing on the Great Snow Mountain and now serves the Lord of Heaven.
- **Personality:** Devoted to his master and proud of his abilities, he is deeply wounded by perceived distrust and resolves to prove his worth.
- **Voice:** Casually familiar and self-amused, addressing Jeok Cheongang respectfully as Senior while trading blunt insults; his easy laughter can turn to a low, cold intensity.
- **Relationships:** He serves the Lord of Heaven with deep devotion but believes his master does not fully trust him; he has been ordered not to kill Jin Taekyung, admires Jeok Cheongang, and once shared the Demonic Cult with the fiends who became Black Ghosts.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1036
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1036
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1035
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him and feels no fear when Taekyung is with him; Taekyung trusts Sama Pyo and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1035
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1031
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader and heir of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Outwardly courteous and calculating, he is protective of Taishan and pragmatic in combat; he recognizes that his father's ruthless, survival-driven worldview shaped him, even as its influence weighs on him.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan and is Sima Gong's son and heir; his father's ruthless treatment of family shaped his rise and remains a source of inner constraint. He joined the Fire Dragon Pavilion intending to use Jin Taekyung, and Sima Gong has now ordered him to spy on Taekyung's group. Taekyung rejects defining him by his unorthodox affiliation, and Sama Pyo admires Taekyung. He was Ju Hwaran's former fiancé in a political engagement and is openly hostile toward fellow member Song Ilseom.

### Sima Gong.md

# Sima Gong (사마공)

- **Safe through:** Chapter 1033
- **Aliases:** Black Night King
- **Role:** Sima Gong is the Sect Leader who built the Black Dragon Demon Gate into a major unorthodox power and the father of its Young Sect Leader, Sama Pyo.
- **Personality:** Sly and calculating yet outwardly gentle; he calmly accepts sacrificing the rear population as the cost of a strategy he believes offers the best odds of victory.
- **Voice:** Polished and persuasive, with smooth rhetorical turns and a composed, gently teasing manner.
- **Relationships:** Sama Pyo is his youngest son among seven older brothers and nine older sisters; he is personally familiar with Jeok Cheongang, who openly dislikes him.

## Korean source

```text
＃1037화



사마표는 문득 생각했다.

이곳은 어디이며, 자신은 누구인지.

그리고 도대체, 지금 이 순간에도 끊임없이 몰려드는 적 앞에서 그가 어찌해야 하는지.

퍼걱!

그러는 와중에도 본능적으로 펼쳐 낸 일도(一刀)가 적의 목을 베어 냈지만, 사마표는 이미 알고 있었다.

설령 앞으로 수십, 수백을 쓰러트려도 그 뒤에는 수만에 달하는 적들이 남아 있다는 것을.

지금의 이 불리한 전황을 뒤집기에는, 자신이 지닌 힘이 너무나도 미약하다는 것을.

차창! 콰드드득!

“으아아악!”

“커헉……!”

온 사방에서 울려 퍼지는 끔찍한 비명.

아니, 정확히는 ‘아군’들만의 비명.

끊임없이 터져 나오는 피 분수 아래, 빠르게 분쇄되기 시작하는 전열(前列)의 중심에 선 사마표는 곧 벌어질 미래를 읽었다.

‘이대로라면…… 모든 것이 끝장이다.’

피로에 젖은 육신과 달리, 머릿속은 그 어느 때보다 차갑게 식어 있다.

그렇기에 사마표의 판단은 냉철했고, 정확했다.

비등비등한 머릿수를 지닌 두 무리가 격돌했을 때, 결국 승부를 결정짓는 것은 병력의 질과 기세.

그런 의미로 보자면 현재 암천의 군세는 모든 면에서 아군을 압도하고 있었다.

‘길어야 한 식경. 아니 일각. 그 안에 선두의 전열은 완전히 무너진다.’

아군 준 누군가가 들었다면 절망했을 그 말을, 사마표는 조용히 속으로 삼켜 내며 또 다른 적을 향해 달려들었다.

이미 적진 깊숙이 파고들어, 이제는 무수한 적들에 가려져 보이지도 않게 된 진태경을 떠올리며.

그리고 그런 그를 뒤따르기는커녕, 전열을 유지하고 있는 것이 고작인 자신에 대한 분노와 원망을 쏟아 내며.

서걱!

군더더기 없는 일격에 그대로 양단(兩斷)되는 상반신.

후두둑 쏟아지는 적의 핏물 아래에서, 이미 죽음을 직감한 채 벌벌 떨고 있던 젊은 무인이 반색했다.

“고, 고맙…… 어?”

동그랗게 떠진 두 눈과 얼떨떨한 목소리.

이제 겨우 약관이나 되었을까 싶은 젊은이가 곧장 사마표를 알아보았듯, 사마표 역시 그가 걸치고 있는 흑룡마문의 무복을 알아볼 수 있었다.

왠지 모르게 낯익은 느낌 또한 함께.

‘어디서 봤었지?’

그러나 머릿속을 스친 의문도 잠시뿐, 다음 순간 사마표는 황급히 몸을 틀며 도를 휘둘러야 했다.

쉬릭, 카가각!

쾌속하게 공간을 가르며 날아든 적의 검기(劍氣)와 도신이 맹렬하게 맞물린다.

서로를 향해 맞대어진 무기 사이로 비치는 시체처럼 공허한 눈동자와는 달리, 검기가 지닌 섬광은 휘황하고도 날카롭게 빛나고 있었다.

사마표 자신의 것보다도 더.

‘고수……!’

단 한 번의 짧은 격돌이었지만, 그 적지 않은 격차는 피부를 타고 뼛속까지 전해지기에 충분했다.

다만 사마표가 그 순간 느끼지 못했던 유일한 것이 있다면.

쩌적.

절정의 끝자락에 다다랐음을 증명하는 상대의 강렬한 검기를 버텨 내기에는, 이미 앞서 수십의 적들과 부딪히며 낡고 무뎌진 그의 도가 너무나도 연약해져 있다는 것이었다.

콰창!

짧지만 강렬했던 격돌.

그리고 그 끝을 알리듯 허공으로 높게 솟구쳐 오르는, 반 토막 난 도신과 곧장 표적을 향해 뻗어 오는 빛줄기.

‘위험!’

그 위험하기 그지없는 파괴적인 섬광을 직시한 순간, 사마표의 머릿속에서 붉은 경종이 울렸다.

동시에 이성보다 앞선 본능이 그에게 속삭였다.

당장 피하라고.

무슨 수를 써서라도, 어떤 추잡한 꼴을 보이더라도 살아남으라고.

하지만…….

‘도대체 어디로 피해야 하지?’

마치 주마등처럼 느릿하게 흘러가는 시간 속에서, 사마표는 주위를 둘러싼 모든 것을 또렷하게 느꼈다.

차차창! 푸푹!

크아악!

쉼 없이 터져 나오는 날붙이의 소음들. 그 위로 덧없이 흩뿌려지는 핏물과 단말마.

그리고 이러한 절망적인 상황 속에서도, 서로의 어깨가 스칠 만큼 빽빽하게 전열을 유지한 채 적들과 맞서고 있는 아군들.

그들의 입술 사이로 흘러나오는 떨리는 숨결들을 사마표는 똑똑히 느낄 수 있었고, 동시에 직감했다.

‘피할 곳이…… 없다.’

아니다. 틀렸다.

사실 피할 방법은 얼마든지 있었다.

지금 당장이라도 빠르게 좌우 어딘가로 몸을 날려 피하거나, 신형을 굽혀 최대한 적의 검기를 피해 구를 수도 있었다.

나려타곤(懶驢打滾)?

상관없었다. 죽음 앞에서 체면이라는 단어는 사치에 불과했으니까.

피투성이가 아니라 오물투성이가 된다 하여도, 설령 아군 중 누군가를 방패막이로 세워서라도 살아남는 것이 사파(邪派)의 방식이었으니까.

수단과 방법을 가리지 않는 것.

그것이야말로 자신에게 피를 물려준 아버지의, 흑야왕 사마공의 가르침이었으니까.

‘그래, 분명 그랬었지.’

그러나 이제는 아니다.

일 년.

평생 머리 위에 드리워져 있던 아버지의 짙은 그늘을 벗어난 아들은, 그 짧은 시간 동안 여러 사람을 만났고 많은 사건을 겪으며 달라져 있었다.

그렇기에, 지금 이 순간 사마표의 눈에는 보이지 않았다.

분명 피할 수 있었으나, 피할 수 없었다.

멈춰 버린 듯한 시간의 흐름 속에서도 아랑곳하지 않고 느릿하게 뻗어 나오는 저 검기를 피한다면, 반드시 아군 중 누군가가 죽을 테니까.

‘빌어먹을 일이로군.’

혀끝에서 소리 없이 감도는 욕설.

하지만 사마표는 알아차리지 못했다.

어느새 자신의 입가에 맺힌 흐릿한 미소를.

코앞까지 들이닥친 죽음을 보면서도, 이상하리만치 후련해진 마음을.

그리고 소매 밑에 감춰 두었던 비수를 쏘아 보내며 생각했다.

지금 문득 머릿속에 떠오른 누군가가 이 모습을 지켜보고 있다면, 제법 칭찬해 주지 않았을까 하고.

‘이만하면 사파 잡놈치고는 괜찮은 최후지, 안 그런가? 각주.’

사마표는 환하게 웃었다.

동시에 더욱 맹렬해진 적의 검기가, 날아드는 비수를 집어삼키며 자신의 가슴을 향해 짓쳐 드는 것을 느꼈다.

생각지도 못했던 두 줄기의 날카로운 파공성도 함께.

서걱! 푸푹!

사마표는 부릅뜬 눈으로 바라보았다.

최후를 직감한 마지막 순간, 자신의 앞에 뛰어든 누군가의 뒷모습을.

그리고 가슴에서 핏물을 흩뿌리며 비틀거리는 그의 어깨 위를 스쳐, 적의 목울대를 관통한 흑청색의 도신(刀身)을.

‘이건.’

그 익숙하기 그지없는 도신을, 사마표는 즉각 알아볼 수 있었다.

혈검마군과의 회담에 앞서 맡겨 놓고 왔던 자신의 애병, 흑룡도(黑龍刀)에 깃든 강기의 주인 역시도.

“우매한 놈 같으니.”

더없이 익숙한, 그러나 한편으로는 도무지 익숙해질 수 없는 서늘한 그 목소리.

퍼걱!

비틀린 흑룡도의 도신이 적의 목을 완전히 베어 내고, 뒤이어 들불처럼 일어난 흑색 강기가 고스란히 전방을 덮쳤다.

콰드드득!

거칠게 몰아치는 혈풍(血風)이 수십여 명의 적들을 휩쓸었다. 그 엄청난 무위를 눈앞에서 목격한 아군들이 너 나 할 것 없이 뒤늦은 외침을 토해 냈다.

“무, 문주!”

“문주께서 오셨다!”

그 말 그대로였다.

흑야왕 사마공.

사파 무림을 지탱하는 거목이 마침내 최전선에 모습을 드러냈다. 자신이 거느린 흑룡마문의 최정예 무인들과 함께.

“쳐라.”

굳게 다물려 있던 입술 사이로 짧은 명령이 흘러나온 그 순간.

쉬쉬쉬쉭! 콰앙!

수십여 명의 절정 고수가 적들 사이로 내리꽂혔다.

그 엄청난 광경에 곳곳에서 환호가 터져 나왔고, 그 순간만큼은 선두의 전열을 지키고 있던 아군들 중 그 누구도 감히 의심하지 않았다.

왜. 이제야 나타난 것인지.

분명 충분한 시간이 있었음에도, 어찌 지금껏 후방에 머물렀던 것인지.

그러나 한 사람만큼은 예외였다.

“늦으셨군요.”

아들은 전장에서 마주하게 된 아버지를 바라보지 않았다.

사마표의 시선은 조금 전 자신을 위해 몸을 날린, 이제는 차갑게 식어 가고 있는 누군가의 시신을 향하고 있었다.

앞서 한번 그가 구해 주었던, 아직 솜털도 가시지 않은 듯한 젊은 무인을.

하지만 아들의 시선을 따라 힐끗 시신을 바라본 아버지의 대꾸는, 냉담하기 그지없었다.

“네놈이 나약해서 죽은 것이다.”

“맞습니다. 제가 강했다면 살았겠지요.”

사마표는 담담하게 고개를 끄덕였다.

그리고 거침없이 내뱉었다.

“하면, 그토록 강한 당신께서는 무엇을 하고 계셨습니까?”

“뭐라?”

“흑귀(黑鬼)라 불리는 그 괴물들은 이쪽으로 오지 않았습니다. 아마도 때맞춰 전력을 이끌고 합류하셨다면, 충분히 적진을 허물어트릴 수 있었을 겁니다.”

왜 흑귀는 나타나지 않았는가.

흑야왕 사마공이 이끄는 삼만의 대병력이 있음에도, 이 전장의 핵심이라 할 수 있는 전력임에도 어찌 이곳만큼은 노리지 않았는가.

그리고 이 절호의 기회를, 왜 당신은 지금껏 방관하고 있었나.

모두가 잠시 잊고 있는 의문을 표하는 아들을 향한 아버지의 눈빛이, 깊숙이 가라앉았다.

- 무슨 말을 하고 싶은 것이냐.

불현듯 귓가를 파고드는 전음에, 아들이 피식 웃었다.

- 왜, 듣는 귀가 많아 겁나십니까?

- 네놈이 감히…….

- 다른 생각을 품고 계신다는 것은 이미 짐작하고 있었습니다. 하지만 설마, 했지요. 계속해서 믿고 싶었습니다.

아들은, 아니 사마표는 크게 숨을 삼켰다.

- 그래도 제 아버지시니까요.

- ……!

- 제가 왜 사지나 다름없는 그 자리에 가겠다며 자원했는지, 아직도 모르시겠습니까?

사마표는 이미 본능적으로 알고 있었다.

자신의 아버지가 이미 다른 마음을 품었음을.

만약 평생에 걸쳐 이룩한 모든 것을 물려줄 후계자가 위험에 처하지 않았다면, 지금 이 자리에도 나타나지 않았으리라는 것을.

“그러나 부디 안심하십시오. 이 전장의 승부가 어떻게 판가름 나도, 흑룡마문은 살아남을 테니.”

처음으로 아버지와 다른 길을 택한 아들은 망설임 없이 돌아섰다. 그리고 적들을 향해 뛰어들기 전, 어쩌면 마지막이 될지도 모르는 한 마디를 건넸다.

“다른 한 사람은 이미 죽은 모양이더군요. 안타깝게도.”

그렇게 뜻 모를 말을 남긴 채 아들은 떠났고, 아버지는 남았다.

그리고 이내 석상처럼 굳어 있던 사마공의 시선이 쓰러진 시신을 향했을 때, 그는 불현듯 떠올렸다.

지금으로부터 며칠 전, 사막을 가로지르던 도중 감히 흑룡마문과 사마표에 관련된 비사(祕史)에 대해 이야기했던 어느 중년인과 청년의 모습을.

그런 그들의 운명을 단번에 결정지었던 자신의 명령을.



‘알아서 조치하도록 하게.’



그때의 명령은 제대로 이루어졌다.

그들은 가장 위험한 선두의 전열에 배치되었고, 마침내 두 사람 모두 죽음을 맞이했으니.

하지만 흑야왕 사마공은 몰랐다.

아니, 그 누구도 몰랐을 것이다.

냉정한 아버지가 죽음으로 내몰았던 어느 젊은이가, 그의 아들을 구할 줄은.

“……빌어먹게도 얄궂은 운명이로군.”

작게 뇌까린 사마공은 문득 자신의 손에 들린 흑룡도를 물끄러미 내려다보았다.

처음이자 마지막 선물로 아들에게 주었던 그 보도(寶刀)는, 어느덧 복잡한 눈빛을 한 늙은 사내를 비추고 있었다.

바로 그 순간. 저 멀리 터져 나온 아득한 섬광도 함께.



* * *



그것은 마치 낙뢰(落雷)와도 같았다.

쉴 새 없이 떨어져 내리며, 저항할 수 없는 압도적인 힘으로 모든 것을 찢고 불태우는 낙뢰.

그러나 지금 이 순간, 저 멀리 펼쳐진 광경을 부릅뜬 눈으로 바라보던 모든 이들은 알고 있었다.

한껏 곤두선 전신의 감각으로, 무인으로서 지닌 본능과 상식으로 깨닫고 있었다.

쉴 새 없이 온 사방을 물들이며 터져 나가는 저 무수한 섬광의 정체가, 자신들의 손에 들린 날붙이와 같다는 것을.

슈확!

수십여 개의 휘황한 빛줄기가 공간을, 먹구름과 함께 드리워진 어둠을 찢었다.

마치 살아 있는 생물처럼 자유롭게 허공을 가로지른 그것들은, 감정을 느끼지 못하기에 더는 살아 있다고 말할 수 없는 존재들을 휩쓸었다.

콰드드드득!

비명 대신 섬뜩하기 그지없는 파육음이 울려 퍼졌다.

사막 너머의 땅에서 수백 번의 담금질을 거쳐 탄생한 병장기는 강철의 파도와 맞닿은 순간 조각조각 분쇄되었고, 그것을 소유하고 있던 주인의 몸뚱어리는 말할 것도 없었다.

촤악, 투두두둑!

마치 파도처럼 솟구치는 핏물.

수십여 명의 몸 안에서 터져 나와 사방을 적시는 그 붉은 소나기 아래, 천천히 걸음을 옮기는 한 사람이 있었다.

철벅.

끈적하다. 발목까지 고인 핏물이 출렁이고, 역한 피비린내가 콧속으로 스며든다.

그러나 머리부터 발끝까지 피를 뒤집어쓴 혈인(血人)의 행색이 되었음에도, 진태경의 발걸음은 계속해서 앞으로 나아갔다.

오직 그의 의지 아래 놓인, 거대한 강철의 파도와 함께.

철컥, 투투퉁!

무언가 맞물리는 소리와 함께 울려 퍼지는 파공성. 그와 동시에 진태경의 손가락이 미세하게 움직였다.

캉!

허공을 유영하던 다섯 자루의 대도(大刀)가 넓은 도신을 펼치며 측면을 감쌌다.

마치 활짝 만개한 꽃잎처럼 펼쳐진 그 강철의 방패가, 연이어 날아드는 화살촉을 막아 낸 것은 그야말로 눈 깜짝할 사이에 벌어진 일이었다.

카카카캉!

불똥을 토해 내며 튕겨 나가는 십여 개의 화살.

하지만 그 갑작스러운 기습에도 진태경은 아랑곳하지 않았다.

그는 이미 반경 삼 장을 완전히 자신의 공간으로 만들었으니까.

그리고 수많은 아군의 틈새에 숨어 연노(連弩)를 발사한 누군가는, 더 이상 앞서와 같은 기습을 펼치지 못할 테니까.

‘가라.’

고개를 돌려 적의 위치를 확인할 필요도 없었다.

진태경은 명령했고, 단지 그것만으로도 방패와 같은 역할을 했던 다섯 자루의 대도는 곧장 거대한 화살이 되어 쏘아졌다.

푸푸푹!

숨 한번 내뱉을 짧은 시간 동안 이십여 명의 목숨이 사라졌다.

연노를 쏜 적도, 날아드는 대도를 막아섰거나 그의 곁에 머무르던 또 다른 적들도.

그들 모두가 그렇게 죽었다.

다만 다섯 자루의 대도 역시 되돌아오지는 못했다.

제각각 수십 근의 무게를 지닌 강철을 벼락처럼 쏘아 보내기에는, 진태경 역시 한계가 명백했으니까.

으득.

불현듯 엄습해 오는 끔찍한 두통에, 진태경은 조용히 이를 악물었다.

‘너무 큰 욕심이었나.’

하단전과 달리 중단전은 의지의 영역이며 이는 곧 정신력을 뜻한다.

이 많은 병장기를 조종하는 것만으로도 이적(異蹟)이라 부르기에 일말의 부족함이 없지만, 모든 것 하나하나에 공력을 불어넣고 완벽하게 제어하는 것은 다른 문제였다.

어느 정도의 수준에 도달한 고수라면, 힘과 속도뿐인 병장기는 충분히 막아 낼 수 있으니까.

바로 지금처럼.

푸푹! 카카카캉!

의지를 받들어 다시금 쏘아진 병장기가 살과 뼈를 관통한다.

그러나 십여 장 남짓한 거리를 돌파하는 사이, 일백을 헤아리던 날붙이의 숫자는 어느덧 절반으로 줄어 있었고 절정의 경지에 도달한 일부 적들은 그것을 어렵지 않게 튕겨 내기 시작했다.

‘아직, 아직이다.’

전투가 시작된 직후, 이미 홀로 수백여 명의 적들을 쓰러트렸다.

아니, 어쩌면 일천이 넘어갈지도 모른다.

그야말로 일기당천(一騎當千)이라 칭해질 만한 신위.

하지만…….

‘이 정도로는 부족해.’

진태경은 알고 있었다.

적진 깊숙이 파고들수록, 혈검마군과 맞서고 있는 적천강을 향해 가까워질수록 적들은 더욱 강해지고 있다는 것을.

지금 이 순간에도 끝없이 밀려드는 적들을 모조리 쓰러트리기 위해서는, 자신에게 주어진 모든 것을 폭발시켜야 한다는 것을.

‘단 하나. 일격이면 충분하다.’

마음속에 떠오른 생각이 곧 의지가 되어 발현된 순간.

스륵. 차차차창!

진태경을 둘러싸고 있던 수십 개의 병장기가 허공에서 떨어져 내렸다.

그 어떤 날붙이보다 많은 피를 머금었음에도 여태껏 빛을 잃지 않은, 한 자루의 창을 제외하고.

‘지금.’

화륵.

흔들리는 공간 속, 강기에 휩싸인 백염(白炎)이 타오르며 쏘아졌다.

그리고 수백에 달하는 인의 파도를 가로지른 그 맹렬한 섬광의 끝에, 한 사람이 있었다.

콰아아앙!

하늘이 쪼개지는 듯한 굉음과 함께, 창날에 실린 거대한 힘에 의해 밀려나는 신형.

어느새 피투성이가 된 적천강을 향해 짓쳐 들려던 혈검마군이, 잘게 다진 육편(肉片)이 되어 흩어진 붉은 길에 우뚝 선 진태경을 보며 피에 젖은 이빨을 드러냈다.

“그래, 왔느냐?”
```

## Final English reading copy

```markdown
# Chapter 1037

Sama Pyo suddenly wondered.

Where was this place? Who was he?

And what was he supposed to do, with enemies pouring in without end even now?

Thwack!

His body moved on instinct, and his saber cut through an enemy’s neck. But Sama Pyo already knew.

Even if he cut down dozens, even hundreds, tens of thousands of enemies would remain behind them.

His strength was far too meager to turn the tide of this disadvantageous battle.

Clang! Krrr-crack!

“Argh!”

“Gah…!”

Horrifying screams rang out from every direction.

No—more precisely, only their allies were screaming.

Standing at the center of the front line as it rapidly began to crumble beneath an endless spray of blood, Sama Pyo read the future about to unfold.

*At this rate… everything is finished.*

His body was soaked in exhaustion, but his mind was colder than ever.

That was why his judgment was clear and precise.

When two forces of roughly equal size clashed, the quality of their troops and their momentum ultimately decided the victor.

In that regard, Dark Heaven’s army was superior to their own in every way.

*We have half an hour at most. No—fifteen minutes. The front line will be completely broken by then.*

Sama Pyo quietly swallowed the words that would have filled anyone in his army with despair, then charged at another enemy.

He thought of Jin Taekyung, who had plunged deep into enemy territory and was now hidden from view by a sea of enemies.

And he poured out his anger and resentment at himself for barely managing to hold the line, let alone follow him.

Slice!

One clean strike cleaved the enemy’s upper body in two.

Beneath the shower of blood, a young martial artist who’d been trembling, already certain he was about to die, lit up with relief.

“Th-thank you… Huh?”

His eyes were wide, his voice dazed.

The young man looked barely twenty, and just as he recognized Sama Pyo at once, Sama Pyo recognized the Black Dragon Demon Gate uniform he wore.

The young man also seemed strangely familiar.

*Where have I seen him before?*

But the question only flickered through his mind. A moment later, Sama Pyo hurriedly twisted around and swung his saber.

Whish—Kkakak!

Sword Energy tore through the air and slammed against the blade of his saber.

The eyes reflected between the weapons were vacant as a corpse’s, but the Sword Energy gleamed bright and sharp.

Sharper than Sama Pyo’s own.

*A master…!*

It had been a brief clash, but the considerable difference in their strength was enough to travel through Sama Pyo’s skin and into his bones.

There was just one thing he hadn’t noticed in that moment.

Crack.

His saber had already grown too fragile to withstand the enemy’s fierce Sword Energy—a testament to the enemy’s mastery of the Peak realm. It had been battered and dulled by colliding with dozens of enemies already.

KWA-CLANG!

The brief but fierce clash came to an end.

A broken half of Sama Pyo’s blade spun high into the air, and a streak of light shot straight toward its target.

*Danger!*

The moment he saw that devastating flash, a red alarm blared in Sama Pyo’s mind.

At the same time, instinct whispered ahead of reason.

*Get out of the way.*

*Survive, whatever it takes. No matter how disgraceful you have to be.*

But…

*Where am I supposed to dodge?*

Time seemed to slow as if his life were flashing before his eyes. Sama Pyo could sense everything around him, clear as day.

Clang-clang! Thud!

“Gaaah!”

The ceaseless clash of blades. Blood scattering uselessly through the air, followed by dying screams.

And, even in this desperate situation, his allies standing shoulder to shoulder, packed so tightly that they brushed against one another, as they faced the enemy.

Sama Pyo could clearly sense the tremor in their breathing. And at the same time, he knew:

*There’s… nowhere to run.*

No. That was wrong.

There were plenty of ways he could dodge.

He could dart to either side right now, or duck and roll to avoid as much of the enemy’s Sword Energy as possible.

A Narye tagon?[^1]

Who cared? In the face of death, dignity was a luxury.

Even if he ended up covered in filth instead of blood, even if he used one of his allies as a shield, surviving was the way of the unorthodox faction.

Use any means necessary.

That was what his father, the Black Night King Sima Gong, had taught him—the man who’d passed his blood down to him.

*Yes. That’s what he taught me.*

But not anymore.

One year.

In that brief time, the son had stepped out from beneath his father’s deep shadow, which had hung over him all his life. He’d met many people, experienced a great deal, and changed.

That was why, at this moment, Sama Pyo could see no way out.

He could have dodged, but he couldn’t.

Even in this frozen moment, if he avoided the Sword Energy slowly stretching toward him, one of his allies would surely die.

*What a damn mess.*

The curse circled soundlessly on the tip of his tongue.

But Sama Pyo didn’t notice the faint smile that had formed at the corner of his mouth.

Nor the strange relief he felt as he watched death rush toward him.

He launched the dagger he’d hidden under his sleeve, thinking that if the person who’d suddenly come to mind were watching, they might even praise him for this.

*Not a bad way for an unorthodox punk to go, don’t you think, Pavilion Master?*

Sama Pyo smiled brightly.

At the same time, he felt the enemy’s Sword Energy grow even fiercer. It swallowed the dagger flying toward it and surged toward his chest.

He also heard two unexpected, sharp whistles cutting through the air.

Slice! Thud!

Sama Pyo stared with wide eyes.

At the very last moment, when he’d sensed his end, someone had leaped in front of him.

A blackish-blue saber blade passed over the shoulder of the man who staggered, blood spraying from his chest, and pierced the enemy’s throat.

*This is…*

Sama Pyo recognized the familiar blade at once.

And the owner of the Force within it: the same Force that dwelled in his treasured weapon, the Black Dragon Saber, which he’d left behind before the meeting with the Blood-Sword Demon Lord.

“You fool.”

The voice was chillingly familiar—and yet one he could never grow used to.

Thwack!

The warped blade of the Black Dragon Saber finished cutting through the enemy’s neck. Then black Force rose like a spreading wildfire and swept across the front.

KRRR-CRACK!

A fierce blood-red gale engulfed dozens of enemies. The allies who witnessed that overwhelming display of martial might cried out, one after another.

“L-Lord!”

“The Sect Leader is here!”

That was exactly right.

The Black Night King, Sima Gong.

The great tree that supported the unorthodox Murim had finally appeared on the front line, together with the elite martial artists of the Black Dragon Demon Gate under his command.

“Attack.”

The short command slipped through his tightly closed lips.

Whoosh-whoosh-whoosh! KABOOM!

Dozens of Peak masters plunged into the enemy ranks.

Cheers erupted here and there at the sight. And in that moment, not one of the allies holding the front line dared to wonder:

Why had he only appeared now?

Why had he remained in the rear until now, despite having plenty of time to join them?

But one person was the exception.

“You’re late.”

The son did not look at his father, whom he’d met on the battlefield.

Sama Pyo’s gaze was fixed on the corpse of the person who’d just thrown himself in front of him.

It was the young martial artist he’d saved once before, the one who still looked as if he hadn’t lost his baby fat.

His father followed his gaze and glanced at the corpse. His reply was cold.

“He died because you were weak.”

“That’s right. If I’d been stronger, he would’ve lived.”

Sama Pyo nodded calmly.

Then he spoke without restraint.

“Then what were you doing, you who are so strong?”

“What?”

“The monsters called Black Ghosts never came this way. If you’d brought your forces here in time, I think we could’ve broken through the enemy lines.”

Why hadn’t the Black Ghosts appeared?

Why hadn’t they targeted this place, when Sima Gong’s thirty-thousand-strong army was the key force on this battlefield?

And why had he stood by and watched this perfect opportunity pass?

His father’s gaze sank deep as he looked at his son, who’d given voice to the questions everyone else had momentarily forgotten.

*What are you trying to say?*

At the sudden Sound Transmission in his ear, his son gave a quiet laugh.

*What, are you afraid there are too many ears listening?*

*How dare you…*

*I’d already guessed you had other plans. But I didn’t want to believe it. I kept hoping I was wrong.*

His son—no, Sama Pyo—drew a deep breath.

*You’re still my father, after all.*

*……!*

*Do you still not understand why I volunteered for a place that was practically a death sentence?*

Sama Pyo had known instinctively.

His father was already harboring other intentions.

If the heir who would inherit everything he’d built over a lifetime hadn’t been in danger, he wouldn’t have shown up here now.

“But please, don’t worry. No matter how this battle ends, the Black Dragon Demon Gate will survive.”

For the first time, the son chose a path different from his father’s, then turned away without hesitation. Before charging at the enemy, he offered one last parting remark—perhaps the last he’d ever have the chance to make.

“It looks like the other one is already dead. Unfortunately.”

The son left those words, whose meaning was unclear, and was gone.

The father stayed behind.

When Sima Gong’s gaze, still frozen like a statue, finally settled on the fallen body, he suddenly remembered a middle-aged man and a young man from several days earlier, as they crossed the desert. They’d dared to speak of the Black Dragon Demon Gate’s and Sama Pyo’s hidden history.

And the command he’d given that had decided their fate in an instant.

*“See to it as you see fit.”*

His command had been carried out properly.

They’d been placed in the front line, the most dangerous position.

And, at last, both men had met their deaths.

But the Black Night King, Sima Gong, didn’t know.

No—no one could have known.

That a young man whom a cold-hearted father had sent to his death would save his son.

“……What a cruel twist of fate.”

Sima Gong murmured quietly, then looked down at the Black Dragon Saber in his hand.

The treasured blade he’d given his son as his first and last gift now reflected an old man with a troubled look in his eyes.

At that very moment, it also reflected a flash of light erupting far in the distance.

* * *

It was like a lightning bolt.

Lightning falling without end, tearing and burning everything beneath it with irresistible force.

But everyone staring wide-eyed at the scene unfolding in the distance knew, at that moment.

They knew through the heightened senses of their entire bodies, through the instincts and common sense of martial artists.

The countless flashes of light bursting across the battlefield weren’t ordinary bolts of lightning.

They were just like the blades in their own hands.

Fwoosh!

Dozens of brilliant streaks of light tore through the darkness beneath the heavy clouds.

They moved freely through the air, like living things, sweeping over beings that could no longer be called alive because they felt nothing.

KRRR-CRACK!

Instead of screams, a terrifying crunch of flesh rang out.

The weapons had been forged in the lands beyond the desert, through hundreds of rounds of tempering. The moment they met the steel wave, they shattered into pieces—and their owners’ bodies were no better off.

Splash. Thud-thud-thud!

Blood surged up like a wave.

Beneath that red rain, bursting from the bodies of dozens and soaking the ground, one man slowly walked forward.

Squish.

Sticky. Blood pooled up to his ankles and sloshed with each step. Its foul stench seeped into his nose.

But even with blood covering him from head to toe, Jin Taekyung kept walking forward.

Along with the enormous steel wave under his sole command.

Clack. Thud-thud-thunk!

A clattering sound rang out, followed by a whistle through the air. At the same moment, Jin Taekyung’s fingers moved slightly.

Clang!

Five great sabers floating through the air spread their broad blades to shield his flank.

Like petals in full bloom, the steel shield opened wide, blocking the arrowheads that came flying at him in quick succession. It all happened in the blink of an eye.

Kakakakclang!

A dozen arrows bounced away in showers of sparks.

But Jin Taekyung didn’t flinch at the sudden ambush.

He’d already made the space within a three-*jang* radius his own.

And whoever had hidden among their many allies to fire that repeating crossbow wouldn’t get the chance to spring another ambush.

*Go.*

He didn’t need to turn and check the enemy’s position.

Jin Taekyung gave the command. The five great sabers that had served as shields instantly became enormous arrows and shot away.

Thud-thud-thud!

In the time it took to exhale once, more than twenty lives disappeared.

The enemy who’d fired the repeating crossbow, and the other enemies who’d stood in the path of the flying sabers or lingered nearby.

They all died.

But the five sabers didn’t return, either.

Even Jin Taekyung had clear limits when it came to hurling steel weighing dozens of *geun* each like lightning.

Grit.

A terrible headache abruptly seized him. Jin Taekyung clenched his teeth in silence.

*Was that too ambitious?*

Unlike the Lower Dantian, the Middle Dantian was a domain of Will, which meant mental strength.

Just controlling this many weapons was nothing short of a miracle. But imbuing every single one with internal energy and controlling them perfectly was another matter.

A master who’d reached a certain level could block weapons that relied on nothing but force and speed.

Just as they were doing now.

Thud! Kakakakclang!

Weapons shot forward again at Jin Taekyung’s command, piercing flesh and bone.

But in the time it took them to cross a distance of barely ten *jang*, the number of blades that had once been close to a hundred had been cut in half. Some of the enemies who’d reached the Peak realm were beginning to deflect them without much trouble.

*Not yet. Not yet.*

Since the battle began, he’d already taken down hundreds of enemies alone.

No—perhaps more than a thousand.

An incredible feat, worthy of being called One Against a Thousand.

But…

*It’s not enough.*

Jin Taekyung knew.

The deeper he went into enemy territory, the closer he got to Jeok Cheongang fighting the Blood-Sword Demon Lord, the stronger the enemies became.

To cut down every enemy still surging toward him, he had to unleash everything he’d been given.

*Just one. One strike is enough.*

The instant the thought arose in his mind and took shape as Will—

Slip. Clang-clang-clang!

The dozens of weapons surrounding Jin Taekyung fell from the air.

All except one spear, which had held more blood than any of the other blades and still hadn’t lost its gleam.

*Now.*

Fwoosh.

White Flame, wrapped in Force, flared to life in the wavering space and shot forward.

At the end of that fierce streak of light, which tore through a human wave numbering in the hundreds, stood one man.

KWA-BOOM!

With a roar like the sky splitting apart, a figure was driven backward by the immense force carried in the spearhead.

The Blood-Sword Demon Lord had been rushing toward Jeok Cheongang, who was already drenched in blood.

Now, he bared his bloodstained teeth at Jin Taekyung, standing in a red path where enemies had been chopped into tiny pieces of flesh.

“So, you’ve come?”

[^1]: A humiliating idiom comparing a fighter’s evasive roll to a lazy donkey rolling on the ground.
```
