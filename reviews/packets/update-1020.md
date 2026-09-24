<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1020.txt",
      "sha256": "58f6ad171e02f9b577ba808010d849d55e847389caf8063390cdacdad0d4cbec",
      "bytes": 14196
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "72525a6c07690ddf775c88bd74f61ae35bc5854ad19e6387b4a0b049aa64cce3",
      "bytes": 1225
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "348ced6c9732bdd8a5469c80f31dda793893bf98b07230eb9fd287f48d71929c",
      "bytes": 238366
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "9bd5c587c5bb129bfc50487283065c3d8b07e7e430cf7b5c6f06afa8400ec987",
      "bytes": 760
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "17309df54b1154a8ef10bc89e3c9b3ee62bdda2e4d758bd48bc78cfaecb1dd35",
      "bytes": 668
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "fe011328772cfb425542858d7e4d8597e5a4f17186980cbcc9ae5759f0f1b730",
      "bytes": 1375
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "748937d91f3b87152e26d41ac0e6ae73817b964077e504054ec2f7ea6bca2fb7",
      "bytes": 1502
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "de292d24a426c74846dff135c4789e7138dcea31609130c42826a17cf60fd28b",
      "bytes": 1682
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "98d937b52cc452063ca5788d09c1048aeed5f9fa711459a2d2aed88848a0267b",
      "bytes": 623
    },
    {
      "path": "characters/Sima Gong.md",
      "sha256": "f3069bed5041a85726357dbc6e28904f6d950bf4de25484346091cd4f4966d7e",
      "bytes": 778
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "107226d29d3a00596e274bb32d326b67d072d4bda85484b408975b0987bfdde5",
      "bytes": 277335
    }
  ],
  "estimated_tokens": 11856
}
-->

# Durable State Update — Chapter 1020

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
1 and safe_through 1020. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1020. Profile updates may replace only one
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
  "chapter": 1020,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1020,
    "continuity_sources": [1020],
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
    "A secret letter Sama Pyo received was suspected to have come from Gansu or Qinghai; its sender, contents, and purpose remain unknown.",
    "Taishan appeared unusually gloomy and ate less as the group approached Gansu; whether he knows about the letter is unknown.",
    "Taekyung remains unsure whether he would kill Sama Pyo and Taishan if they were acting on Sima Gong's orders connected to Dark Heaven.",
    "Sima Gong has reinforced the westbound force with three thousand troops from those stationed in the Qilian Mountains.",
    "Sama Pyo knows his father's ruthless calculations included sacrificing family and enabled his own rise as heir; Sima reads Pyo's recent deference as a return to his former self.",
    "A red flare burst above a distant hill as the force moved west through the Qilian Mountains."
  ],
  "continuity_sources": [
    1019
  ],
  "open_questions": [
    "Who sent Sama Pyo the secret letter, what did it say, and what was its purpose?",
    "Are Sama Pyo and Taishan acting on Sima Gong's orders, and are those orders connected to Dark Heaven?",
    "What did the red flare signal?"
  ],
  "safe_through": 1019,
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
| 일신     | **One God**         |
| 종남파    | **Zhongnan Sect**                |
| 소림     | **Shaolin**                      |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 중원     | **Central Plains**                               |                                                       |
| 장문인    | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 제자     | **Disciple**                                 |
| 상태               | **Status**                     |
| 명성               | **Fame**                       |
| 감숙     | **Gansu**              |
| 노부      | **this old man / I**                                            |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 서역 | **Western Regions** | Region from which the glasses were imported. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 허공답보 | **Stepping on Empty Air** | Technique that allows Jongni Chu to move through empty air as if climbing invisible stairs. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 기련산 | **Qilian Mountains** | Mountain range in Qinghai from which the Qilian Three Fiends emerged. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 한나절 | **half a day** | Elapsed duration in Jeok's first time-loss episode. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 답보 | **stagnation** | Taekyung's current lack of progress in martial arts. |
| 공동파 | **Kongtong Sect** | Sect belonging to the Nine Sects and One Gang. |
| 흑야왕 | **Black Night King** | Epithet of Sima Gong, Sama Pyo's father and the Sect Leader who built the modern Black Dragon Demon Gate. |
| 도산검림 | **a mountain of sabers and a forest of swords** | Idiom describing the lethal life of martial artists. |
| 대설산 | **Great Snow Mountain** | Mountain where Baeksang's wartime account reaches its next episode. |
| 파리 | **Paris** | The city containing Ares Guild's branch attacked at the chapter's end. |
| 종남 | **Zhongnan Sect** | Orthodox faction that fought in the historic battle. |
| 상산후 | **Marquis of Shangshan** | Title bestowed on Jin Taekyung by the Emperor. |
| 쇄월검진 | **Moon-Shattering Sword Formation** | Named sword formation of the Zhongnan Sect. |
| 돈황 | **Dunhuang** | City identified as the foremost defensive line in Gansu. |

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
| 적천강 | 풍운검군 | legendary_elder_to_Zhongnan_sect_leader | Wind-and-Cloud Sword Lord | familiar and commanding | Jeok Cheongang tells him to get the Zhongnan disciples moving. |
| 사마공 | 적천강 | unorthodox sect leader to senior martial master | Senior | formal and deferential | Greets Jeok Cheongang as 노선배. |
| 적천강 | 사마공 | senior martial master to longtime martial acquaintance | you | blunt and familiar | Uses direct, contemptuous language while teasing Sima Gong. |
| 진태경 | 사마공 | allied young martial artist to unorthodox sect leader | Great Hero Sima | polite and deferential | Addresses him as 사마 대협. |
| 사마공 | 진태경 | unorthodox sect leader to celebrated young martial artist | you | polite and familiar | Uses 자네 while speaking to Taekyung. |
| 풍운검군 | 적천강 | Zhongnan Sect Leader to legendary martial master | Senior Jeok | respectful | Refers to Jeok as 적 대협. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1019
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 1019
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1019
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1019
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1019
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him and feels no fear when Taekyung is with him; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1019
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Sima Gong.md

# Sima Gong (사마공)

- **Safe through:** Chapter 1019
- **Aliases:** Black Night King
- **Role:** Sima Gong is the Sect Leader who built the Black Dragon Demon Gate into a major unorthodox power and the father of its Young Sect Leader, Sama Pyo.
- **Personality:** Sly and calculating yet outwardly gentle; he calmly accepts sacrificing the rear population as the cost of a strategy he believes offers the best odds of victory.
- **Voice:** Polished and persuasive, with smooth rhetorical turns and a composed, gently teasing manner.
- **Relationships:** Sama Pyo is his youngest son among seven older brothers and nine older sisters; he is personally familiar with Jeok Cheongang, who openly dislikes him.

## Korean source

```text
＃1020화



그것은 누구도 예측하지 못한 찰나의 순간에 벌어진 일이었다.

쉬이이익, 펑!

비록 수백 여장의 거리가 있었음에도 나를 포함한 모든 이는 똑똑히 보고, 들을 수 있었다.

저 멀리, 화려하게 허공을 수놓은 붉은 빛무리와 함께 전해지는 폭발음을.

‘신호탄!’

틀림없다.

저건 본대를 앞질러 간 척후조가 쏘아 올린 신호탄이다. 그것도 매우 위급함을 의미하는 붉은색 폭죽.

차차차창!

이 갑작스럽게 벌어진 상황에 굳어 있던 것도 잠시, 곧장 눈앞에 직면한 현실을 받아들인 이들은 망설임 없이 허리춤의 병장기를 빼 들었다.

“전투 준비!”

“무위검문의 문도들은 적들의 기습에 대비하라!”

“종남파의 제자들은 즉각 쇄월검진(碎月劍陳)을 펼쳐라!”

일순간 돌변한 기세에 찌르르 울리는 공기.

사방에서 번뜩이는 무수한 도산검림(刀山劍林) 속, 빗발치는 고함을 따라 일사불란하게 움직이는 아군의 모습을 보며 나는 말안장을 박찼다.

가장 가까이에 있던 혁무진에게 짤막한 한 마디를 남기는 것도 잊지 않고.

“현 위치 고수해. 내가 돌아올 때까지.”

“자, 잠까……!”

후웅, 쐐애애액!

이어지는 뒷말은 듣지 못했다.

휘몰아치는 거센 바람이 혁무진의 목소리를 집어삼키고, 십여 장에 달하는 거리가 단숨에 지워졌으니.

나는 전신을 사로잡은 부유감(浮游感)을 느끼며 가벼운 발끝으로 허공을, 바람을 밟으며 높이 솟구치는 동시에 나아갔다.

“저, 저거!”

“궁수! 궁수는 무엇 하는가! 적이 나타났다! 쏴라!”

“이 멍청한 놈들, 활 내려! 아군이다!”

어느새 아득해진 지상에서 아직 혼란에서 빠져나오지 못한 몇몇 이들이 착각할 만큼 자유로운 움직임.

그리고 그런 내 뒤를 바짝 뒤쫓는 누군가의 인기척이 있었다.

“도무지 맘 편히 쉴 틈을 안 주는군. 이게 대관절 무슨 일이냐?”

마치 지면을 내달리는 것처럼 편안한 허공답보(虛空踏步)와 함께 들려오는 익숙한 목소리.

나는 적천강의 물음에 고개도 돌리지 않고 대답했다.

“앞서 정찰 나간 척후조에 무슨 일이 생긴 것 같습니다.”

“무슨 일 생겼다는 건, 설마 노부가 생각하는 그것이냐?”

“아직은 모르죠. 다만 한 가지 확실한 건…….”

나는 저 멀리 굽이진 모래 언덕 위로 피어오르는 먼지구름을 응시하며 덧붙였다.

“어떤 상황이건 간에, 결코 좋은 소식은 아닐 겁니다.”

그리고 그로부터 일각의 시간이 흐른 뒤, 나는 다시 한번 새삼 깨달았다.

좋지 않은 예감은, 언제나 늘 그렇듯이 빗나가는 법이 없다는 것을.

“쿨럭. 도, 돈황(敦煌). 돈황이……!”

바짝 말라붙은 입술과 파리한 안색. 거기에 더해 넝마가 되다시피 한 의복까지.

뿌연 먼지를 뒤집어쓴 것 외에는 멀쩡한 신색을 유지하고 있는 척후조와 달리, 고난과 다급함이 온몸에 덕지덕지 들러붙은 낯선 사내는 파르르 떨리는 목소리로 말을 이었다.

“노, 놈들에게…… 함락되었습니다.”

“……!”

“……!”

그리고 그가 말하는 ‘놈들’이 누구를 가리키는 것인지 모르는 이는, 우리 중 아무도 없었다.

암천(暗天).

광활한 사막 너머의 악귀들이, 마침내 모래의 강을 넘어 인간들의 영역에 발을 디뎠다.



* * *



이름 모를 사내의 정체는 대설산(大雪山)에서 보낸 전령이었고, 그가 가져온 급보는 수뇌부 전체에 엄청난 충격을 안겨 주기에 충분했다.

“다, 다시 한번 말해 보게. 지금, 지금 뭐라고 했나?”

종남파라는 명문 대파의 장문인으로서 어느 상황에도 흔들리지 말아야 할 풍운검군이 말을 더듬었지만, 단 한 사람도 잠깐이지만 비웃는 기색을 내비치지 않았다.

아니, 못했다는 것이 더 정확한 표현일 것이다.

이 자리의 수뇌부 전체가 풍운검군과 다를 것 없는 심정이었으니까.

조금 전 전령의 입술 사이로 흘러나온 이야기는 모두의 귀를 의심케 만들 정도였으니까.

그러나 그런 그들의 반응에도, 전령이 재차 전한 정보는 처음과 달라지지 않았다.

“그, 그것이, 아뢰옵기 송구하오나.”

“처음부터 다시, 차근차근 설명해 보게, 어서!”

차마 말을 잇지 못하고 질끈 감은 두 눈.

하지만 이내 입술을 꽉 깨문 대설산의 전령은, 쏟아지는 불호령에 어렵사리 입을 열었다.

“옥문관(玉門關)이 돌파당한 것이 시작이었다고 합니다.”

내가 아는 바에 의하면 옥문관은 오랜 과거 서역과의 연결을 담당하던 비단길의 주요 관문.

사방이 탁 트인 사막지대에 위치한 데다, 비록 작게나마 토성(土城)이 세워져 있기에 일대를 감시하기에는 적격인 곳이었다.

‘한 마디로, 소규모 부대로 국경을 감시하게는 안성맞춤인 요충지.’

물론 감숙 무림이 동원한 총병력과 비교해서 소규모일 뿐이지, 일전에 수뇌부 회의에서 언급되기로는 옥문관에 배치된 척후병의 숫자는 최소 일백이다.

아니, 일백‘이었다.’

이제는 그들 모두 이 세상 사람이 아닐 테니까.

“모두 죽었단 말인가? 단 한 사람도 빠짐없이?”

“마땅히 확인해 볼 도리는 없었으나, 아마도 그럴 것입니다. 돈황의 삼백 리 앞까지 도달한 후에야 적들의 존재를 눈치챘다고 했으니 말입니다.”

“그렇다면 그것이, 돈황이 적들의 수중에 떨어진 것이 정확히 언제인가?”

“약 사흘 전이라고 했습니다.”

“사흘 전……!”

수뇌부들 사이에서 침음성이 터져 나온 그때, 내가 불현듯 입을 열었다.

“잠깐. 돈황이 아닌 대설산에서 왔다고 들었는데, 그 소식은 누구에게서 들었습니까?”

“도호(道號)는 듣지 못했지만, 돈황을 지키던 공동파의 도사였습니다.”

“도호를 모른다?”

“예, 예.”

나는 조용히 미간을 좁혔다.

공동파는 엄연한 도가 문파고, 그런 이들에게 있어 도호란 곧 자신의 이름이나 진배없다.

소림사의 승려들이 속세의 이름을 버리고 법명으로 자신을 소개하는 것처럼, 통성명을 기본 중의 기본으로 여기는 무림인들 사이에서 도호조차 알리지 않았다는 것은 나로 하여금 두 가지 추측을 떠올리게 만들었다.

첫째. 눈앞의 전령이 거짓 정보를 가져왔거나.

혹은…….

‘도호를 말할 틈도 없이 급박한 상황에서 죽었거나.’

그리고 뒤이어 이어진 전령의 말은, 내 두 번째 추측을 뒷받침해주고 있었다.

“조금 전에는 경황이 없어 미처 말씀드리지 못했지만, 그 도사는 이미 처음 봤을 때부터 심각한 부상을 입고 있었습니다. 대설산에 도착한 지 촌각도 지나지 않아 숨이 끊겼지요.”

“허어.”

누군가의 입술 사이로 흘러나온 신음.

지금 이 순간, 수뇌부의 분위기가 한층 더 무거워진 이유는 이름 모를 도사의 죽음 때문만은 아니다.

무림에서의 전령은 적들의 포위를 뚫을 만큼 날래고, 일신의 무위가 뒷받침되어야 하는 법.

한데 공동파에서 전령으로 보낸 이가 촌각도 지나지 않아 절명했을 정도라면, 도대체 돈황에 배치되어 있던 아군의 상황은 어느 정도란 말인가.

물론 나를 포함한 이 자리의 모두는 그들이 어찌 되었는지 이미 알고 있었다.

대부분이 앞서 들었던 충격적인 소식을, 마음속으로 애써 부정하고 있었을 뿐.

“사실이었군. 전부.”

차갑게 식은 적천강의 뇌까림에, 전령이 대답했다.

“믿기 힘들 정도로 참담한 소식이지만, 제가 전해 들은 바로는 그렇습니다.”

따지자면 그리 좋은 꿈도 아니었지만, 이제는 꿈에서 깨어나서 잔인한 현실을 마주할 때.

나는 아직도 믿을 수 없다는 표정으로 침묵하고 있는 수뇌부들을 뒤로한 채, 어렵사리 입술을 뗐다.

본능적으로 서늘해지는 등골을 느끼며.

“최소 이천이 죽고, 삼천이 크게 다치거나 실종…… 맞습니까?”

전령은 대답하지 않았다.

대신 힘없이 고개를 떨구었을 뿐이었고, 그 모습을 본 사람들은 마침내 미루고 미뤄 두었던 현실을 인정할 수밖에 없었다.

“이, 이 무슨 말도 안 되는……!”

“어쩌겠소. 이미 벌어진 일인 것을.”

“일만. 무려 일만이오! 한데 그 많은 병력이 그리 손쉽게 격파당했다니.”

그래, 일만.

무려 일만이다.

그런데 공동파를 중심으로 돈황을 지키던 그 대병력이, 심지어 수성전(守城戰)을 펼쳤음에도 절반이나 증발했다고 한다.

그것도 불과 반나절 만에.

하지만 비보(悲報)는 그뿐만이 아니었다.

“공동파의 전력 중 약 삼 할이 소실되었고, 다급하게 퇴각하는 과정에서 장로직을 맡고 계신 두 분의 진인(眞人)과 복마대(伏魔隊) 일백 전원이 돈황에 뼈를 묻었다고 합니다.”

“……!”

“……!”

곳곳에서 헛숨을 삼키는 소리가 울려 퍼졌다.

공동파가 어떤 곳인가.

구파일방의 일익이요, 천하 무림을 지탱하는 열다섯 개의 거목 중 하나다.

한데 그런 공동파가 무너졌다.

이미 십여 년 전에 초절정의 반열에 올랐다고 알려진 두 장로와, 중원에까지 명성이 자자한 복마대의 희생을 뒤로한 채 퇴각한 것이다.

“하면. 장문인, 장문인께서는 어찌 되셨는가!”

풍운검군의 다급한 물음에 모두가 숨을 죽인 채 전령의 대답을 기다렸다.

현대의 기준으로 삼 할의 손실은 전멸로 판단할 만큼 궤멸적인 피해지만, 무림의 기준은 조금 다르다.

결국 중요한 것은 고수의 존재.

비록 엄청난 타격을 입었다 하더라도 일군의 중심이, 머리가 살아있다면 희망은 있다.

감숙성 제일의 무인이자, 바로 그 흑야왕 사마공보다도 반 수 앞선다는 평가를 받는 공동파 장문인이 살아남았다면 반격의 여지는 충분하다.

그리고 수십여 쌍의 시선 속, 마른침을 꿀꺽 삼킨 전령의 한 마디는 불행 중 다행이라 할만했다.

“두 장로님과 복마대 전원이 옥쇄(玉碎)를 각오한 덕분에, 장문인께서는 무사히 전장에서 퇴각하셨다고 들었습니다.”

“아아.”

“천만다행이오. 하늘이 도우셨소.”

참았던 안도의 한숨이 곳곳에서 흘러나온 그 순간. 한 사람이 불현듯 입을 열었다.

“그리고?”

“예?”

“그리고 어찌 되었냐 물었네.”

전령이 전하는 말 한마디, 한마디에 요동치는 대부분의 수뇌부와 달리 침착함이 묻어 나오는 목소리.

사마공은 깊게 가라앉은 눈빛으로 전령을 응시하며 재차 입을 열었다.

“장문인께서 잔존 병력을 이끌고 퇴각하셨다면 분명 대설산(大雪山)으로 향하셨을 터, 한데 자네의 말을 들어 보니 그 후로 아직 아무런 소식도 없는 듯한데. 이게 어찌 된 일인가?”

다시금 찾아온 침묵 속, 전령이 어쩔 줄 몰라 하는 얼굴로 입을 열었다.

“그것이, 소인도 알 도리가 없습니다.”

“알 도리가 없다?”

“예. 순식간에 전황이 기울자 살아남은 아군은 절반으로 나뉘어 퇴각했고, 장문인께서는 그들 중 상당수를 이끌고 퇴각하시며 문하의 제자에게 이 소식을 전하라 명하셨다 합니다.”

죽은 자는 말이 없는 법.

장문인의 명을 받고 온 힘을 다해 대설산으로 향한 제자는 더 자세한 정보를 전해 주기도 전에 숨이 끊겼고, 돈황을 지키던 일만의 아군은 산산이 와해 되어 지금껏 아무런 소식도 없다.

“그러나 대설산을 떠난 것이 한나절 전이니, 지금쯤이면 돈황에 있던 아군이 합류했을 가능성도 있습니다.”

전령의 덧붙임에 몇몇 수뇌부가 희망 어린 얼굴로 고개를 끄덕였지만, 글쎄.

‘가장 빨리, 누구보다 앞서 전장을 벗어났을 전령이 그 정도로 큰 부상을 입은 상태였다면…….’

암천의 대군세는 이미 돈황 일대를 그물질하며 대설산으로 향하고 있을 것이다.

살아남은 아군을 쫓음과 동시에, 살아남은 아군을 쫓음과 동시에, 자신들을 가로막은 두 번째 전선을 무너트리기 위해.

‘놈들의 속도가 터무니없이 빠르다. 상상 이상으로.’

그리고 지금 이 순간, 나는 더는 선택의 여지가 없음을 깨달았다.

“아직 늦지 않았습니다. 지금 즉시 전령을 보내서 기련산의 모든 병력을 총동원하시죠.”

“뭐?”

불쑥 내뱉은 한 마디에 사마공이 눈살을 찌푸렸다.

“지금, 뭐라고 했나?”

“기련산에 배치된 병력을 총동원하라고 말씀드렸습니다. 대설산까지 무너지면 끝장이니까요.”

“그에 대해서는 이미 논의를 거쳐 결론을 도출한 것으로 아네만.”

착 가라앉은 눈빛을 한 사마공을 향해, 나는 어깨를 으쓱해 보였다.

“그럼 그 결론을 바꿔 보시죠.”

“……자네.”

“아, 착각하실까 봐 드리는 말씀인데.”

그리고 다음 순간, 품속에서 뭔가를 꺼내 들며 나직이 덧붙였다.

“이건 권유가 아니라, 명령입니다.”

상산후(上山后) 진태경.

유려한 필체가 음각된 호패(號牌)를 바라본 사마공의 눈동자가 크게 뜨였다.
```

## Final English reading copy

```markdown
# Chapter 1020

It happened in a fleeting instant no one could have predicted.

Whoosh—BOOM!

Even from several hundred *jang* away, everyone—including me—could see and hear it clearly.

A brilliant burst of red light embroidered the sky in the distance, followed by the sound of an explosion.

*A signal flare!*

No doubt about it.

It was a signal flare shot by the scouts who’d gone ahead of the main force. And not just any flare—it was red, the color for extreme danger.

Clang! Clang! Clang!

For a moment, everyone froze at the sudden turn of events. But those who’d quickly grasped the reality before them drew their weapons without hesitation.

“Prepare for battle!”

“Disciples of the Martial Might Sword Sect, prepare for an enemy ambush!”

“Zhongnan Sect Disciples, form the Moon-Shattering Sword Formation!”

The sudden shift in momentum sent a shiver through the air.

As countless blades flashed all around us, I watched our allies move in unison at the shouts ringing through the ranks and kicked off from the saddle.

I didn’t forget to leave a quick word for Hyuk Mujin, who was closest to me.

“Hold your position. Until I get back.”

“W-wait a—!”

I didn’t hear the rest.

A fierce gust swallowed Hyuk Mujin’s voice, and the distance of a dozen *jang* disappeared in an instant.

Feeling the buoyancy that took hold of my whole body, I stepped lightly on empty air, on the wind, and soared upward as I surged forward.

“Th-there!”

“Archers! What are you waiting for? The enemy’s here! Fire!”

“You idiots, lower your bows! He’s one of ours!”

My movements were so free that a few people below, still caught up in the confusion, mistook me for an enemy.

And someone was following close on my heels.

“You don’t give an old man a moment’s peace. What in the world is going on?”

The familiar voice came with the effortless Stepping on Empty Air, as if its owner were running along the ground.

I answered Jeok Cheongang’s question without turning around.

“Something must have happened to the scouts who went ahead.”

“Something happened? You don’t mean what this old man thinks you mean?”

“We don’t know yet. But one thing’s certain…”

I fixed my gaze on the dust cloud rising over the distant, winding sand dunes and added,

“Whatever’s happening, it can’t be good news.”

A quarter of an hour later, I realized once again that bad premonitions, as always, never missed.

“Cough. D-Dunhuang. Dunhuang has…”

His lips were parched, his face pale, and his clothes were little more than rags.

Unlike the scouts, who looked mostly unharmed apart from being covered in dust, the unfamiliar man was marked all over by hardship and desperation. His voice trembled as he continued.

“It’s been… taken by them.”

“……!”

“……!”

Not one of us had any doubt who he meant by “them.”

Dark Heaven.

The Fiends beyond the vast desert had finally crossed the river of sand and set foot in human territory.

* * *

The unknown man was a messenger sent from the Great Snow Mountain, and the urgent news he brought was enough to send a shock through the entire leadership.

“S-say that again. What, what did you just say?”

The Wind-and-Cloud Sword Lord, Sect Leader of the prestigious Zhongnan Sect, stammered despite the fact that he should have been unshakable in any situation. Not a single person so much as let a trace of amusement show.

No—that wasn’t quite right. They couldn’t.

Everyone in that room felt just as he did.

What they’d just heard from the messenger’s lips was enough to make them doubt their own ears.

Yet despite their reaction, the messenger’s account didn’t change when he repeated it.

“I-I regret to report that…”

“Start from the beginning and explain it slowly. Quickly!”

He squeezed his eyes shut, unable to bring himself to continue.

But the messenger from the Great Snow Mountain soon clenched his lips, then managed to speak under the barrage of sharp commands.

“It began when the Jade Gate Pass was breached.”

As far as I knew, in ancient times the Jade Gate Pass had been one of the main passes along the Silk Road, connecting the Central Plains with the Western Regions.

It stood in a wide-open stretch of desert, and though it was only a small earthen fortress, its position made it ideal for keeping watch over the surrounding area.

*In other words, it was a strategic position perfectly suited to monitoring the border with a small force.*

Small, of course, only in comparison to the total force Gansu’s Murim had mobilized. At the recent leadership meeting, we’d heard that at least a hundred scouts had been stationed at the Jade Gate Pass.

No—there *had* been at least a hundred.

By now, every last one of them was probably dead.

“Are you saying they all died? Every single one?”

“We had no way to confirm it, but that is likely. They said the enemy wasn’t detected until it had advanced to within three hundred *li* of Dunhuang.”

“Then when exactly did Dunhuang fall into enemy hands?”

“They said it was about three days ago.”

“Three days ago…!”

A murmur of disbelief rippled through the leadership. That was when I suddenly spoke up.

“Wait. I heard you came from the Great Snow Mountain, not Dunhuang. Who told you this?”

“I never learned his Daoist name, but he was a Daoist of the Kongtong Sect, defending Dunhuang.”

“You don’t know his Daoist name?”

“N-no.”

I quietly furrowed my brow.

The Kongtong Sect was a Daoist sect, and to its members, a Daoist name was as good as their own. Just as the monks of Shaolin Temple had abandoned their worldly names and introduced themselves by their Dharma names, Daoist names were basic introductions among martial artists.

That he hadn’t even given his Daoist name brought two possibilities to mind.

First, the messenger standing before us had brought false information.

Or…

*He died in such a desperate situation that he didn’t even have time to give his Daoist name.*

The messenger’s next words supported my second guess.

“I was too flustered to mention it earlier, but the Daoist was seriously injured when I first saw him. He’d barely arrived at the Great Snow Mountain when he breathed his last.”

“Good heavens.”

A groan escaped someone’s lips.

The leadership’s mood had grown even heavier, and it wasn’t only because the unknown Daoist was dead.

In Murim, a messenger had to be fast enough to break through enemy encirclement and skilled enough to hold his own.

So if the man the Kongtong Sect had sent as a messenger had died moments after arriving, what kind of state had the forces stationed at Dunhuang been in?

Of course, everyone in that room, myself included, already knew what had become of them.

They’d only been trying to deny the shocking news they’d just heard.

“So it was true. All of it.”

At Jeok Cheongang’s cold mutter, the messenger answered.

“It’s a terrible report, hard to believe, but that’s what I was told.”

It hadn’t exactly been a pleasant dream, but it was time to wake up and face the cruel reality.

Leaving the leadership behind as they sat in stunned silence, I managed to part my lips.

My spine was instinctively turning cold.

“At least two thousand dead, and three thousand seriously injured or missing. Is that right?”

The messenger didn’t answer.

He only lowered his head in exhaustion. Seeing him, everyone was finally forced to accept the reality they’d put off for as long as they could.

“H-how can this make any sense…?”

“What can we do? It’s already happened.”

“Ten thousand. A full ten thousand! How could a force that large be defeated so easily?”

Yes. Ten thousand. A full ten thousand.

And yet that massive force, defending Dunhuang under the leadership of the Kongtong Sect, had been wiped out by half—even though they’d fought a defensive battle.

In just half a day.

But that wasn’t the only bad news.

“About thirty percent of the Kongtong Sect’s strength has been lost. During the desperate retreat, two Perfected Ones serving as Kongtong Elders and all one hundred members of the Demon-Subduing Squad died at Dunhuang.”

“……!”

“……!”

Gasps rang out around the room.

What kind of sect was the Kongtong Sect?

One of the Nine Sects and One Gang, one of the fifteen great pillars that supported the martial world.

And now the Kongtong Sect had been broken.

They’d retreated, leaving behind two Elders said to have reached Supreme Peak more than a decade ago and the Demon-Subduing Squad, whose reputation was known even in the Central Plains.

“Then… what happened to the Sect Leader? What happened to the Sect Leader?”

At the Wind-and-Cloud Sword Lord’s urgent question, everyone held their breath and waited for the messenger’s answer.

By modern standards, a loss of thirty percent was catastrophic enough to be called annihilation. But Murim had a different standard.

What mattered, in the end, was whether they still had a master.

No matter how devastating the losses, if the force’s center—the head—survived, there was hope.

If the Sect Leader of the Kongtong Sect, the strongest martial artist in Gansu and someone said to be half a step ahead of even Sima Gong, the Black Night King, had survived, there was still room to counterattack.

And as dozens of pairs of eyes fixed on him, the messenger swallowed hard and gave an answer that could be called a small blessing amid misfortune.

“I heard that the Sect Leader managed to withdraw from the battlefield safely, thanks to the two Elders and the entire Demon-Subduing Squad being prepared to die there.”

“Ah…”

“Thank goodness. Heaven was watching over him.”

Sighs of relief escaped all around them. At that moment, someone suddenly spoke.

“And?”

“Pardon?”

“I asked what happened next.”

Unlike most of the leadership, whose emotions rose and fell with every word the messenger spoke, the voice was calm.

Sima Gong stared at the messenger with a deeply sunken gaze and spoke again.

“If the Sect Leader withdrew with the surviving troops, he must have headed for the Great Snow Mountain. But from what you’ve said, it seems there’s been no word since. How do you explain that?”

Silence fell once more. The messenger looked at a loss before answering.

“I—I have no way of knowing.”

“No way of knowing?”

“Yes. The tide of battle turned in an instant, so the surviving allies split into two groups and retreated. The Sect Leader led many of them away and ordered a Disciple of the sect to deliver this news.”

The dead could say nothing.

The Disciple, sent by the Sect Leader to the Great Snow Mountain, had pushed himself to the limit and died before he could provide any more information. The ten thousand troops defending Dunhuang had been scattered to the four winds, and no word had come from them since.

“However, I left the Great Snow Mountain half a day ago, so it’s possible that the troops from Dunhuang have joined up by now.”

A few members of the leadership nodded with hopeful expressions at the messenger’s addition, but…

*If even the wounded Kongtong messenger, who must have escaped the battlefield ahead of everyone else, was injured that badly…*

Dark Heaven’s great army would already be sweeping the Dunhuang area like a net as it advanced toward the Great Snow Mountain.

Chasing the surviving allies and, at the same time, chasing the surviving allies to break through the second line of defense in their path.

*Their speed is absurd. Far faster than I imagined.*

And at that moment, I realized there was no longer any choice.

“We’re not too late yet. Send a messenger at once and mobilize every force in the Qilian Mountains.”

“What?”

Sima Gong furrowed his brow at my abrupt declaration.

“What did you just say?”

“I said to mobilize every force stationed in the Qilian Mountains. If the Great Snow Mountain falls, it’s over.”

“We’ve already discussed that and reached a conclusion.”

I shrugged at Sima Gong’s steady gaze.

“Then change that conclusion.”

“……You.”

“Ah, just so there’s no misunderstanding.”

The next moment, I pulled something from inside my clothes and added in a low voice,

“This isn’t a suggestion. It’s an order.”

Marquis of Shangshan, Jin Taekyung.

Sima Gong’s eyes widened as he stared at the identity tablet, its characters engraved in elegant script.
```
