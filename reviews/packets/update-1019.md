<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1019.txt",
      "sha256": "37ddb171a5996c5f4ab1c423a5567a6dbefbed4197b04027302f7705113f6b8c",
      "bytes": 12801
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ebcef8a11a246c6dbcc012a12baccb7721c4e398dce4c9afa675539ef69263da",
      "bytes": 1281
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "348ced6c9732bdd8a5469c80f31dda793893bf98b07230eb9fd287f48d71929c",
      "bytes": 238366
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "9f19ddcc59d6cd89fc7926fee57eedd8689388f2190da7252406b1f4312e1d7e",
      "bytes": 760
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "fbd3d7c3f94e0d6a0f2952ad6b7a294da760c287adc567bab129d0a669eab2dc",
      "bytes": 667
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "d1d7e824a3e6108dff64317c12012c6b88c0444f99864c1c336f4c6ce426b694",
      "bytes": 1375
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "485c8e42f0b871821fd5eb6c23a2403f790754d9e601dd9bc0e41e65ef98df18",
      "bytes": 1502
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "7762bd5d7011e084fbe28984a82a9f6f951310319110aa487d1fb44af6146852",
      "bytes": 1723
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "b7368f425504ae782b725f264e453db23c4587c5ff1475a8e0e984e9da0858cc",
      "bytes": 623
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "18d4121a3e7b6e8ce09d7003b8516c8b3ba431096610923568fa447196046e0a",
      "bytes": 778
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "7ac4f5937a2ac78af30a7e968d815ace5a4dd4bf3274c3fada85afdd20ee5bf9",
      "bytes": 904
    },
    {
      "path": "characters/Sima Gong.md",
      "sha256": "985dff1053d66ac9bb214649a64312460d423352d67f6a24117c2427b709d06c",
      "bytes": 778
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "107226d29d3a00596e274bb32d326b67d072d4bda85484b408975b0987bfdde5",
      "bytes": 277335
    }
  ],
  "estimated_tokens": 11602
}
-->

# Durable State Update — Chapter 1019

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
1 and safe_through 1019. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1019. Profile updates may replace only one
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
  "chapter": 1019,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1019,
    "continuity_sources": [1019],
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
    "Namho’s scent-based deduction suggests Sama Pyo received a secret letter sent from Gansu or Qinghai; Sima Gong is suspected, but the sender and contents are unconfirmed.",
    "Taishan appeared unusually gloomy and ate less as the group approached Gansu, though he still ate five meals a day; whether he knows about the letter is unknown.",
    "Jeok Cheongang once killed the Junzi Saber, a former ally who joined the Demonic Cult after his surviving elder brother sought refuge there for revenge.",
    "Taekyung remains unable to say whether he would kill Sama Pyo and Taishan if they were plotting on Sima Gong’s orders connected to Dark Heaven.",
    "The three thousand troops have reached the Qilian Mountains; Sima Gong is discussing a new plan with two old Daoists after Jeok Cheongang’s unexpected presence disrupted events."
  ],
  "continuity_sources": [
    1018
  ],
  "open_questions": [
    "Who sent Sama Pyo the secret letter, what did it say, and what was its purpose?",
    "Are Sama Pyo and Taishan acting on Sima Gong’s orders, and are those orders connected to Dark Heaven?",
    "What new plan will Sima Gong present to the two old Daoists?"
  ],
  "safe_through": 1018,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 사마공    | **Sima Gong**      |
| 무신     | **Martial God**               | —              |
| 십봉룡    | **Ten Dragons and Phoenixes**    |
| 무인     | **martial artist**                               | Default term                                          |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 사파     | **unorthodox faction**                           |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 산서     | **Shanxi**             |
| 정마대전   | **Great Faction War**         |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 잠룡 | **Hidden Dragon** | Epithet or metaphor for Jin Taekyung. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 기련산 | **Qilian Mountains** | Mountain range in Qinghai from which the Qilian Three Fiends emerged. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 철구 | **iron balls** | Training weights attached to Taekyung. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 흑야왕 | **Black Night King** | Epithet of Sima Gong, Sama Pyo's father and the Sect Leader who built the modern Black Dragon Demon Gate. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 청룡각 | **Azure Dragon Pavilion** | Cheongpung's division within the Two Dragons Pavilion. |
| 황도 | **Imperial Capital** | The capital where the imperial court resides. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 사마표 | 진태경 | prospective recruit to pavilion master | you | polite, controlled, and candid | Sama Pyo uses 자네 while asking about Taekyung's attitude and admitting his intention to use him. |
| 진태경 | 사마표 | pavilion master to prospective recruit | you / that guy | blunt, informal, and distrustful | Taekyung speaks to and about Sama Pyo with casual forms such as 녀석 and 저놈. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 사마공 | 적천강 | unorthodox sect leader to senior martial master | Senior | formal and deferential | Greets Jeok Cheongang as 노선배. |
| 적천강 | 사마공 | senior martial master to longtime martial acquaintance | you | blunt and familiar | Uses direct, contemptuous language while teasing Sima Gong. |
| 진태경 | 사마공 | allied young martial artist to unorthodox sect leader | Great Hero Sima | polite and deferential | Addresses him as 사마 대협. |
| 사마공 | 진태경 | unorthodox sect leader to celebrated young martial artist | you | polite and familiar | Uses 자네 while speaking to Taekyung. |
| 사마공 | 사마표 | father to son | Pyo | intimate and familiar | Sima Gong calls him 표야 and 내 아들아. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1018
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 993
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1016
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1018
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1011
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Peng Cheolhu regarded Taekyung as a worthy successor, inheriting all that Peng had to pass on; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1011
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 997
- **Aliases:** None
- **Role:** An unidentified legendary martial artist regarded as a pinnacle above the Ten Kings; more than fifty years ago, he defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, Mae Jonghak received several teachings from him, and he left the Bow Saint a letter describing a chosen one; the Bow Saint says he chose her, while his identity, whereabouts, and possible connection to Cheon Taemin remain unknown.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1018
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader and heir of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Sima Gong.md

# Sima Gong (사마공)

- **Safe through:** Chapter 1018
- **Aliases:** Black Night King
- **Role:** Sima Gong is the Sect Leader who built the Black Dragon Demon Gate into a major unorthodox power and the father of its Young Sect Leader, Sama Pyo.
- **Personality:** Sly and calculating yet outwardly gentle; he calmly accepts sacrificing the rear population as the cost of a strategy he believes offers the best odds of victory.
- **Voice:** Polished and persuasive, with smooth rhetorical turns and a composed, gently teasing manner.
- **Relationships:** Sama Pyo is his youngest son among seven older brothers and nine older sisters; he is personally familiar with Jeok Cheongang, who openly dislikes him.

## Korean source

```text
＃1019화



둥, 둥, 둥.

거친 북소리가 기련산의 험준한 산등성이를 울리기 시작하자, 달콤한 휴식이 끝났음을 깨달은 사람들이 하나둘씩 자리에서 일어나 집결하기 시작했다.

당연하게도 나와 적천강. 그리고 화룡각 대원들 역시 결코 예외는 아니었다.

차이점이 있다면, 인원이 소수인 덕분에 조금 더 여유가 있다는 것 정도.

“어우, 그래도 잠깐 눈 좀 붙였더니 훨씬 낫네요. 안 그렇습니까?”

막 잠에서 깨어나 늘어지라 기지개를 켜던 혁무진의 물음에, 나는 담담한 목소리로 대꾸했다.

“그러게.”

“어라, 그렇게 말씀하시는 것치고는 안색이 영 어두우신데요.”

“기분 탓이야.”

“기분 탓이 아닌 것 같은데. 한숨도 안 주무신 것 같은데.”

“아니. 아직 잠이 덜 깨서 그래.”

“아이고, 짧게라도 좀 주무시지. 이럴 때는 잠이 보약인데.”

“……혹시 내 목소리 안 들리냐?”

이 새끼는 뭐 음소거 설정이라도 해 놨나.

어이없이 바라보는 내 눈빛에 혁무진이 어깨를 으쓱해 보였다.

“에이, 조장님 얼굴 보자마자 딱 느낌이 오는데 어떻게 모른 척합니까. 무슨 고민 있으시죠?”

촉 날카로운 거 보소.

하지만 저렇게 묻는다고 곧이곧대로 털어놓을 수는 없는 것이 현재의 내 입장이었다.

생각해 봐라.

당장 화룡각 대원들이 사마표에 관한 진실을 알게 된다면 어떤 반응을 보일지.

‘아는 사람이 많아질수록. 감추기도 어려워지는 법이지.’

조금 전 혁무진이 내 얼굴을 보자마자 뭔가를 눈치챈 것처럼, 우리를 주시하고 있을 누군가도 마찬가지일 것이다.

마음속 근심은 어떤 방식으로든 은연중에 드러나기 마련이니까.

결국, 지금 같은 상황에서 내가 혁무진에게 할 수 있는 대답은 처음부터 정해져 있었다.

“언제 무슨 일이 터질지 모르는데, 아무런 걱정도 없으면 그게 사람이냐? 어?”

“그야 뭐, 하긴 그렇네요. 저는 다름이 아니라, 이상하게 그냥 조장님 분위기가 평소랑 좀 다른 것 같아서.”

흠잡을 데 없는 정론(正論)에 뒤통수를 긁적이던 혁무진이 슬그머니 입을 열었다.

“그런데요, 조장님.”

“왜. 중요한 할 말이라도 있냐?”

“아뇨. 크게 중요하지는 않은데, 그냥 저는 아무것도 걱정 안 한다는 말씀을 드리고 싶어서요.”

“뭐?”

“그, 조금 전에 그러셨잖습니까. 지금 같은 상황에 걱정이 없으면 그게 사람이냐고.”

“그게 왜.”

“어떻게 생각하실지는 모르겠는데, 저는 조장님을 모시기 시작한 후로는 이상하게 그런 마음이 잘 안 들더라고요. 하도 별의별 일을 겪다 보니 간덩이가 퉁퉁 불어 터진 탓도 있겠지만, 음.”

말하는 와중에도 내 눈치를 살피며 쭈뼛거리던 혁무진이, 먼 산을 바라보며 혼잣말처럼 중얼거렸다.

“조장님이 항상 곁에 계시니까, 매 순간 같이 싸워 주실 거라는 걸 믿고 있으니까 그 어떤 위험한 상황이 와도 무섭지는 않더라고요.”

“…….”

“아, 물론 지금 한 말로 괜히 더 부담 갖거나 그러지는 마세요. 그러니까 제가 말씀드리고 싶은 거는. 그러니까 그게.”

어색해진 분위기 때문인지. 아니면 머릿속이 꼬였는지.

쉽게 말을 잇지 못하는 혁무진을 물끄러미 바라보던 나는, 녀석을 대신해 입을 열었다.

평소와 다름없는, 애써 퉁명스러운 목소리로.

“괜히 깊은 고민에 사로잡히지 마라. 나는 항상 당신을 믿는다. 결국은 뭐 그런 말 아냐.”

“그렇……죠.”

“그게 뭐 어려운 말이라고 우물쭈물하고 있냐. 나이도 먹을 만큼 먹은 놈이.”

갑작스러운 나이 공격을 받은 혁무진이 울컥한 표정으로 대꾸했다.

“아니, 연장자 대우부터 해 주시고 그런 말씀을 하십시오. 양심에 털 나셨습니까?”

“무진아.”

“왜요.”

“아랫도리에 난 털 싹 다 뽑아 버리기 전에 먼저 가서 대열이나 갖춰. 집결하라는 북소리 안 들려?”

“……참 내, 모르는 사람이 들으면 나 혼자 실컷 떠든 줄 알겠네. 본인도 할 말 다 해 놓고.”

“뭐라고?”

“아, 갑니다. 간다고!”

주둥이를 삐쭉 내민 채 후다닥 달려가는 혁무진의 모습에, 나는 실소를 감추지 못하며 작게 뇌까렸다.

“간다고는 반말이고, 인마.”

그러나 어디에도 닿지 못한 혼잣말은 허공으로 흩어졌고, 소리와 함께 흘러나온 희뿌연 입김은 머리 위에서 떨어져 내리던 무언가를 잠시나마 가려 주었다.

툭.

뒤늦게 전해지는 차가운 감촉.

고개를 들어 바라본 하늘에는, 크고 작은 구름들 사이로 점점이 쏟아져 내리는 무수한 눈송이가 있었다.

둥, 둥, 둥.

때맞춰 재차 울려 퍼지는 북소리를 쫓아, 나는 잠시 멈췄던 걸음을 옮겼다.

그 어떤 상황에서도 나를 믿는다 했던 혁무진의 목소리를 마음속으로 되뇌이며.

그와 동시에, 이 자리에 없는 두 사람을 떠올리며.

‘내가 보여 준 모습들이 부족했던 탓에 너희에게 믿음을 주지 못했던 걸까. 아니면…….’

이제는 든든한 전우이자 친구가 되었다고 생각한 것은, 나만의 어리석은 착각이었을까.

사박.

어느덧 새하얗게 덮여 가는 지면을, 나는 힘주어 밟았다.



* * *



쉼 없이 울려 퍼지던 북소리가 멎었을 때, 기련산을 넘어 서쪽으로 향하는 인마(人馬)의 숫자는 누가 보아도 눈치챌 수 있을 정도로 확연히 불어나 있었다.

드득. 드드득.

물경 수천을 아우르는 대병력의 이동에 산등성이가 신음한다.

앙상한 나뭇가지들 사이로 보이는 깃발 수를 헤아리던 사마표가 불쑥 입을 연 것은, 그들이 몇 번째인지 모를 언덕을 넘어 다시금 황야(荒野)로 들어선 직후였다.

“의외군요.

아무런 서두 없이 던진 한마디.

그러나 사마표도, 상대방도 이런 상황을 대수롭지 않게 받아들였다.

두 부자(父子)에게는 익숙한 일이었으니.

“무엇이 말이냐.”

고개조차 돌리지 않고 대꾸하는 아버지의 옆모습을, 아들은 조용히 응시했다.

“저들의 요구를 들어주신 것 말입니다.”

“요구?”

“회의 때는 설전(舌戰)까지 벌여 가며 뜻을 관철하시더니, 결국 기련산의 병력 중 일부를 충원하지 않으셨습니까. 그것도 무려 삼천이나.”

사마표의 말은 사실이었다.

짧은 휴식이 끝났음을 알리는 북소리가 멎었을 때, 그곳에는 이미 기련산에 배치된 흑룡마문의 무인 중 절반에 달하는 병력이 앞서 집결해 있었다.

“무슨 문제라도 있더냐?”

“평소답지 않으셔서 의아할 따름입니다.”

“평소답지 않다?”

그제야 고개를 돌려 똑바로 자신을 응시하는 아버지의 모습에, 사마표는 작게 고개를 숙였다.

“그저 약간의 의문이 들었을 뿐입니다.”

“말해 보거라. 네 의중을.”

“앞서 내리신 결정을 결코 철회하지 않으실 거라고 생각했습니다. 특히 외인(外人)들을 상대로는.”

“그렇게 생각한 이유는?”

“지금껏 줄곧 그런 모습을 봐 왔기 때문입니다.”

“고개를 들어라.”

사마표는 아버지의 건조한 음성을 순순히 따랐다. 어느새 흑요석처럼 새카만 눈동자가 그를 향해 번뜩이고 있었다.

“벌써 잊었더냐, 그 어떤 상황도, 사람에 대해서도 확신하지 말라 그리 일렀거늘.”

“……!”

“때때로 주위의 상황이 급변할 때가 있다. 그리고 이 험난한 천하에서 살아남아 강해지기 위해서는 끊임없이 의심하고 새로운 변화에 맞춰 계산해야 하지. 이번에도 마찬가지다.”

아마도 몇 년 전, 아니 불과 일 년 전이었다면 사마표는 침묵을 지킨 채 아버지의 말을 경청했을 것이다.

하지만 어째서일까.

오늘따라 코앞에서 들려오는 사마공의 목소리는 메아리처럼 멀게만 느껴졌고 그는 마음속으로 뇌까렸다.

‘끊임없이 의심하고 계산해라…… 여전하시군요.’

사마표는 새삼 뼈저리게 느꼈다.

자신의 아버지가 어떤 사람인지. 어떤 삶을 살아왔는지.

모든 것을 의심하고 경계했기에 흑룡마문(黑龍魔門)이 정마대전에서도 살아남을 수 있었고, 한 치의 오차도 없는 철저한 계산을 통해 엄청난 번영을 누리게 되었다.

그러나 강호의 사정에 이목이 밝은 이라면 누구나 알고 있었다.

지금의 사마공을 있게 만든 의심과 계산 속에는, 혈육(血肉)이라는 단어 역시 포함되어 있다는 것을.

일곱 명의 형님과 아홉 명의 누이들.

한 아버지 아래, 제각기 다른 배에서 태어난 그들의 현재 처지를 떠올린 사마표는 마음속으로 읊조렸다.

‘그래. 바로 그 철저한 계산 덕분에 나 또한 소문주가 될 수 있었지.’

흑야왕 사마공은 그런 사람이었다.

생존과 군림을 위해서라면 수단과 방법을 가리지 않는.

피를 나눈 가족조차 저울에 올려 무게를 가늠하고, 가장 뛰어난 열일곱 번째 자식을 소문주에 임명하기 위해 또 다른 자식들을 거리낌 없이 내칠 수 있는.

그렇기에 진정한 의미의 사파(邪派)였고, 사마표의 살갗 아래에는 그에게서 물려받은 피가 흐르고 있었다.

마치, 아무리 발버둥 쳐도 흠집조차 가지 않는 족쇄처럼.

그리고 그 족쇄에 연결된 철구의 막중한 무게 앞에, 한껏 짓눌린 사마표의 몸과 마음은 자연스럽게 굽혀졌다.

“금과옥조(金科玉條)와도 같은 그 말씀, 가슴 깊이 새기겠습니다.”

그것은 한낱 입에 발린 말이나 눈속임 따위가 아닌, 마음 깊은 곳에서 우러나온 진심이었고 그런 아들의 감정은 아버지에게로 고스란히 전해졌다.

‘표아, 저 아이도 이제 조금씩 정신이 드는 모양이군.’

내심 중얼거린 사마공은 마음이 한결 가벼워지는 것을 느꼈다.

사마표가 누구인가.

늘그막에서야 겨우 얻은, 언젠가 자신의 뒤를 이어 모든 것을 물려받을 만한 후계자다.

타고난 무재(武才)는 중원 최고의 후기지수라는 십봉룡에 비교해도 결코 뒤떨어지지 않는, 아니 그 이상이라 해도 과언이 아니며 심계(心戒) 또한 깊으니 그야말로 타고난 지도자라 할 수 있었다.

‘그랬던 녀석이, 화룡각(火龍閣)에 몸을 담으면서부터 뭔가 이상해지기 시작했지.’

첫 항명(抗命).

문주인 그의 어떤 명령도, 허락도 없었음에도 아들은 독단으로 화룡각의 일원이 되었고 그 사실을 사마공이 알았을 때는 이미 엎질러진 물이었다.

화룡각은 청룡각과 더불어 새롭게 창설된 맹주 직속의 별동대.

이른바 이각(二閣)이라 명명된 그들의 행보를 수많은 이목이 지켜보고 있었고, 사마표가 몸담게 된 화룡각에는 ‘그’가 있었으니까.

‘진태경.’

산서의 잠룡에서, 천하의 신룡으로 발돋움한 무림의 젊은 거인.

그가 옮기는 보보(步步)마다 깊고 거대한 족적이 새겨졌다.

향하는 걸음마다 적들의 무수한 시체와 핏물이 들어찼고, 천하인들의 칭송과 환호가 뒤따랐다.

사마공은 그저 지켜볼 수밖에 없었다.

아들의 이 갑작스러운 항명이, 흑룡마문이 다시 한번 비상하는 계기가 될 수 있을지도 모른다는 기대와 함께.

그러나 응당 돌아와야 할 밀서(密書)는 묵묵부답이었고, 일 년 만에 마주한 사마표의 태도는 어딘가 달라져 있었다.

적어도 조금 전까지는.

‘물론 앞으로도 계속해서 지켜봐야겠지만…… 당분간은 한시름 놓아도 되겠군.’

그리고 이제야 조금씩 과거의 모습을 찾아가는 아들의 모습에, 사마공이 내심 실소를 흘린 바로 그 순간이었다.

쉬이이익, 펑!

수백여 장 밖, 황량한 언덕 위로 솟구침과 동시에 폭발한 붉은 불꽃이 그의 눈동자를 화려하게 물들였다.

아니, 그들 모두를.
```

## Final English reading copy

```markdown
# Chapter 1019

Boom, boom, boom.

As the rough beat of drums began to echo across the rugged ridges of the Qilian Mountains, one by one, the people who’d realized their sweet rest was over got to their feet and began to assemble.

Naturally, Jeok Cheongang and I—and the members of the Fire Dragon Pavilion—were no exception.

The only difference was that, thanks to our small numbers, we had a little more breathing room.

“Whew. Still, even a quick nap helped a lot. Don’t you think?”

Hyuk Mujin had just woken up and stretched until he was practically dangling when he asked me. I answered in a calm voice.

“Yeah.”

“Huh? You say that, but you look awfully gloomy.”

“Your imagination.”

“Doesn’t look like my imagination. You don’t seem to have slept at all.”

“No. I’m just not fully awake yet.”

“Man, you should’ve slept, even if it was only for a little while. Sleep is the best medicine at a time like this.”

“……Are you not hearing me?”

Did this bastard have himself on mute or something?

At my incredulous stare, Hyuk Mujin shrugged.

“Oh, come on. I could tell the moment I saw your face, Captain. You’ve got something on your mind, right?”

Sharp as a tack, isn’t he.

But no matter how he asked, my current position meant I couldn’t just come out and tell him the truth.

Think about it.

What would the Fire Dragon Pavilion members do if they learned the truth about Sama Pyo right now?

*The more people who know, the harder it is to keep a secret.*

Just as Hyuk Mujin had picked up on something the moment he saw my face, someone watching us might do the same.

Worries in your heart tended to show through, one way or another.

In the end, my answer to Hyuk Mujin in a situation like this had been decided from the start.

“When anything could happen at any moment, is it even human to have nothing to worry about? Huh?”

“Well, I guess you’ve got a point. It’s just that you seem a little different from usual, Captain.”

Hyuk Mujin scratched the back of his head at my unassailable logic, then hesitantly opened his mouth.

“But, Captain.”

“What? You have something important to say?”

“No, it’s not that important. I just wanted to tell you that I’m not worried about anything.”

“What?”

“You said it just now, didn’t you? If you have nothing to worry about in a situation like this, are you even human?”

“So?”

“I don’t know what you’ll think of this, but ever since I started following you, for some reason I haven’t really felt that way. Maybe it’s because I’ve been through so much that my guts have swollen up like a waterlogged balloon, but, well…”

Even as he spoke, Hyuk Mujin kept glancing at me, fidgeting. Then he looked toward a distant mountain and murmured as if to himself.

“Since you’re always by my side, and I trust that you’ll fight alongside me every time, I’m not afraid no matter how dangerous things get.”

“……”

“Ah, of course, don’t let what I just said put any extra pressure on you. What I mean is… Well, I mean…”

Maybe the awkwardness had gotten to him. Maybe his thoughts had gotten tangled up.

I watched Hyuk Mujin struggle to find the words, then spoke for him.

In my usual, deliberately curt voice.

“Don’t get caught up in pointless worries. I’ve always trusted you. That’s basically what you’re trying to say, right?”

“That’s… right.”

“What’s so hard about saying that? You’re old enough to know better.”

Hyuk Mujin looked indignant at my sudden attack on his age.

“Hey, show me some respect as your senior before you say that. What, has your conscience sprouted hair?”

“Mujin.”

“What?”

“Get in formation before I pluck every last hair from down below. Can’t you hear the drums telling everyone to assemble?”

“……Honestly, if someone who didn’t know us heard that, they’d think I was the only one who talked the whole time. You said plenty yourself.”

“What was that?”

“Ah, I’m going! I said I’m going!”

Watching Hyuk Mujin dash off with his lips stuck out, I couldn’t hide my quiet laugh. I muttered under my breath,

“You can speak casually when you say you’re going, huh?”

But my words reached no one. They scattered into the air, and the pale breath that escaped with them briefly obscured something falling from overhead.

Plop.

A moment later, I felt a cold touch.

I looked up. Between the clouds of every size scattered across the sky, countless snowflakes were falling.

Boom, boom, boom.

Following the drums as they sounded again right on cue, I resumed the steps I’d paused.

Repeating in my heart Hyuk Mujin’s words: that he trusted me, no matter the situation.

And at the same time, thinking of the two people who weren’t here.

*Was it because I hadn’t shown them enough that they couldn’t trust me? Or…*

Had I been the only fool to think that we’d become dependable comrades and friends?

Crunch.

I stamped down hard on the ground, which was already turning white beneath the falling snow.

* * *

When the nonstop drumbeats finally stopped, the number of people and horses heading west over the Qilian Mountains had swelled so noticeably that anyone could see the difference.

Grind. Grrind.

The mountain ridges groaned under the movement of a massive force numbering thousands.

Sama Pyo had been counting the flags visible between the bare branches. He spoke abruptly just after they crossed yet another hill and emerged onto the wilderness once more.

“That’s unexpected.”

He offered no preamble.

But neither Sama Pyo nor the person he was speaking to thought anything of it.

It was normal between father and son.

“What is?”

His father answered without even turning his head. His son quietly watched his profile.

“That you agreed to their demands.”

“Their demands?”

“At the meeting, you even argued with them to get your way. Yet in the end, you reinforced our troops with part of the force stationed in the Qilian Mountains. Three thousand of them, no less.”

Sama Pyo was right.

When the drums announcing the end of the brief rest stopped, nearly half the Black Dragon Demon Gate’s martial artists stationed in the Qilian Mountains had already assembled ahead of them.

“Is that a problem?”

“I only find it surprising. It’s not like you.”

“Not like me?”

Only then did his father turn his head and look straight at him. Sama Pyo lowered his head slightly.

“It was only a small question that occurred to me.”

“Go on. Tell me what’s on your mind.”

“I thought you would never withdraw a decision you’d already made. Especially when dealing with outsiders.”

“Why did you think that?”

“Because that’s what I’ve seen you do all this time.”

“Raise your head.”

Sama Pyo obediently did as his father’s dry voice commanded. His father’s eyes, black as obsidian, were already gleaming at him.

“Have you forgotten already? I told you never to be certain about any situation—or any person.”

“……!”

“Sometimes the situation around you changes drastically. To survive and grow stronger in this harsh world, you must question everything and keep recalculating to account for new developments. This time is no different.”

A few years ago—or even just one year ago—Sama Pyo would have remained silent and listened to his father.

But why?

Today, Sima Gong’s voice, coming from right in front of him, seemed distant as an echo. Sama Pyo muttered inwardly,

*Keep questioning everything and calculating… You haven’t changed at all.*

Sama Pyo was reminded, painfully, of what kind of person his father was—and the kind of life he’d lived.

By questioning and guarding against everything, the Black Dragon Demon Gate had survived even the Great Faction War. Through calculations so precise there wasn’t a hair’s breadth of error, it had prospered immensely.

But anyone well-informed about the martial world knew.

The blood of one’s own family was included in the calculations and suspicions that had made Sima Gong who he was.

Seven older brothers and nine older sisters.

Thinking of the present circumstances of the children born to different mothers under the same father, Sama Pyo murmured inwardly,

*That’s right. It was thanks to that thorough calculation that I, too, became the Young Sect Leader.*

Sima Gong, the Black Night King, was that kind of man.

A man who stopped at nothing to survive and rule.

A man who would put even his blood relatives on the scales to weigh their worth, and unhesitatingly cast aside his other children to appoint the most capable, his seventeenth child, as Young Sect Leader.

That was what made him a man of the unorthodox factions in the truest sense. And beneath Sama Pyo’s skin ran the blood he’d inherited from him.

Like shackles that wouldn’t suffer even a scratch, no matter how desperately he struggled.

And beneath the immense weight of the iron ball chained to those shackles, Sama Pyo’s body and mind bent naturally under the pressure.

“I will keep those words, precious as gold and jade, deeply in my heart.”

It wasn’t a mere empty platitude or a ruse. The words came from deep within his heart, and his father sensed his son’s feelings just as clearly.

*Pyo, it seems that boy is finally coming to his senses.*

Sima Gong murmured inwardly and felt his spirits lift.

Who was Sama Pyo, after all?

The heir he’d finally managed to have in his old age, the one who would someday inherit everything from him.

His innate martial talent was no less than that of the Ten Dragons and Phoenixes, the greatest young prodigies in the Central Plains—no, it wouldn’t be an exaggeration to say it surpassed theirs. And his strategic mind was deep as well. He was a born leader.

*But something started to change in him after he joined the Fire Dragon Pavilion.*

His first act of defiance.

Without any command or permission from Sima Gong, the Sect Leader, his son had joined the Fire Dragon Pavilion on his own. By the time Sima Gong found out, the deed was done.

The Fire Dragon Pavilion and the Azure Dragon Pavilion were newly established strike forces under the Alliance Leader’s direct command.

A great many eyes were watching the actions of the two pavilions, as they were called. And the Fire Dragon Pavilion Sama Pyo had joined had *him*.

*Jin Taekyung.*

The Hidden Dragon of Shanxi, who’d risen to become the Divine Dragon of the world—a young giant of Murim.

Every step he took left a deep and massive imprint.

Wherever he went, the path behind him filled with the corpses and blood of countless enemies, followed by the praise and cheers of people throughout the land.

Sima Gong could only watch.

He’d hoped that his son’s sudden act of defiance might give the Black Dragon Demon Gate another chance to rise.

But the secret correspondence he should have received never came, and Sama Pyo’s attitude, when they met for the first time in a year, had seemed somehow different.

At least, until just now.

*Of course, I’ll have to keep watching him. But for the time being, I can breathe a little easier.*

And it was just as Sima Gong let out a quiet laugh to himself at the sight of his son gradually returning to his old self that it happened.

Shhhwick—BOOM!

A burst of red flame shot up over a barren hill several hundred *jang* away, then exploded, brilliantly coloring his eyes.

No—everyone’s.
```
