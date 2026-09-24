<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0938.txt",
      "sha256": "419afc7af79e698297d659db81f970537b2d18499a3bb9170eff57acd9f1bb55",
      "bytes": 13585
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "69c72fb0d67865c80f2ae884c60c23398109ffaf3c0d9f6cc351b2078aa5ab5e",
      "bytes": 2495
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b51f7a56cfa82ca1164fe5c2453945cbf42f0adc0ae050d159295fd4e544b433",
      "bytes": 232009
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "c5dfcb389b598f9e0aa073774bc1c233e1f9886a9faf9b6c8aaff2493a02836e",
      "bytes": 759
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "01cd6e5b2c973ceacc749f7ea5110fbb6c5817ac3a2f1ee92c0d610e0c1f6299",
      "bytes": 1445
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "f197657c89a20c5971b639c26b4a00cf40df515e635829f3ee4b5a6b79fbdfef",
      "bytes": 1244
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "dd0cd5b87e5f4b75d13f6350969f9244e210b9f7305f7a4283c28c069382aff5",
      "bytes": 1343
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "fdfca5937c4bdabb07db10101394fad647fcbcadafe96a6c5577cf8a9d1937c0",
      "bytes": 622
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "b5b40acbb8cc9fef1701c9ae69c04ba5f0401e20c99b047e35b9ece28cf35191",
      "bytes": 839
    },
    {
      "path": "characters/Peng Cheolhu.md",
      "sha256": "7aa6894590216c21a6ff2537214757dff6f01270efb150ceddb05323503799f1",
      "bytes": 680
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "0e2d532f2af4d7be69c6e65c1cef25321d7cf2235ebf140c6de94d6147d63060",
      "bytes": 266948
    }
  ],
  "estimated_tokens": 12110
}
-->

# Durable State Update — Chapter 938

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
1 and safe_through 938. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 938. Profile updates may replace only one
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
  "chapter": 938,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 938,
    "continuity_sources": [938],
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
    "The Emperor was poisoned with Blood Soul Gu after the coup; it has reached his marrow, and he has endured its effects for more than ten years.",
    "The Divine Physician says the Emperor’s vitality is at its limit and cannot guarantee he will survive another couple of months.",
    "The Myriad-Poison Ring failed against the Emperor’s Blood Soul Gu; the gu thrashed more violently when it sensed the ring’s energy.",
    "Taekyung’s System quest requires him to remove the Blood Soul Gu from the Emperor’s head and successfully treat him; the reward and failure consequence are unknown.",
    "The Emperor prepared for his death by transferring loyal retainers and his power base to Zhu Bao, and avoids meeting his younger brother to spare him the grief of an impending farewell.",
    "Taekyung told Jeok Cheongang about the Emperor’s Blood Soul Gu poisoning, breaking his promise to keep it secret.",
    "The System update reward is a durable pocket watch that appears broken and bears the faint inscription “A broken clock is right twice a day”; its significance is unknown.",
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin.",
    "Hong Jin is Eunuch Hong, responsible for the East Depot; the Cang Gong post remains vacant.",
    "Ma Sanbao escaped and evaded the Imperial Army’s three-day search.",
    "The Emperor has publicly exposed Dark Heaven and declared his intent to crush it; war against Dark Heaven has begun.",
    "Taekyung found the Eastern Heaven Demon Lord’s hidden iron chest and opened it; it contains old bamboo slips, recent papers, and a small silk pouch, whose significance is unknown."
  ],
  "continuity_sources": [
    936,
    937
  ],
  "open_questions": [
    "What is the Martial God’s identity, and how did he know a chosen one would appear?",
    "How far has Dark Heaven infiltrated the Great Nation, and which officials or commanders are involved?",
    "Where is Ma Sanbao, and what is his current status?",
    "What do the papers, bamboo slips, and silk pouch from the Eastern Heaven Demon Lord’s chest contain, and what is their significance?",
    "What is the significance, if any, of the broken pocket watch given as the System update reward?"
  ],
  "safe_through": 937,
  "temporary_decisions": [
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 진백양    | **Jin Baekyang**   |
| 적천강    | **Jeok Cheongang** |
| 화양검    | **Blade of Flowers**          | Jin Baekyang   |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 무신     | **Martial God**               | —              |
| 궁성     | **Bow Saint**                 | —              |
| 벽력도왕   | **Thunderbolt Saber King**    | Peng Cheolhu   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 곤륜파    | **Kunlun Sect**                  |
| 하북팽가   | **Hebei Peng Family**            |
| 남궁세가   | **Nangong Family**               |
| 삼류     | **Third Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 정파     | **orthodox faction**                             |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 문주     | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 제자     | **Disciple**                                 |
| 사제     | **Junior Brother**                           |
| 태원     | **Taiyuan**            |
| 사천     | **Sichuan**            |
| 감숙     | **Gansu**              |
| 청해     | **Qinghai**            |
| 안휘     | **Anhui**              |
| 화산     | **Huashan**            |
| 곤륜     | **Kunlun**             |
| 구화산    | **Mount Jiuhua**       |
| 노부      | **this old man / I**                                            |
| 공자      | **Young Master**                                                |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 남궁 | **Namgung** | Surname of the family led by Namgung Ryong. |
| 천면호리 | **Thousand-Faced Fox** | Epithet of Song Ho. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 섬서성 | **Shaanxi Province** | Source form specifying Shaanxi as a province. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 신력 | **divine strength** | Superhuman strength attributed to Taekyung. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 역용술 | **disguise technique** | Technique used by the Third Fiend to conceal his identity. |

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
| 적천강 | 벽력도왕 | rival_martial_master_to_rival_martial_master | Virility Saber King | insulting and taunting | Jeok coins 정력도왕 as a taunting replacement for the established title. |
| 벽력도왕 | 적천강 | rival_martial_master_to_rival_martial_master | Jeok Cheongang | boisterous and hostile-teasing | The Thunderbolt Saber King calls Jeok by name before their argument escalates. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 결사대 | commander_to_subordinates | you bastards | blunt and commanding | Jin orders the suicide squad to exploit the opening and wipe out the surrounding monsters. |
| 벽력도왕 | 진태경 | elder martial master to younger rival | you | boisterous and confrontational | Peng addresses Taekyung as 네놈 while discussing Peng Dojin. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 936
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 937
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; he regards Taekyung as the person who has repeatedly saved him and now believes he may be able to save Taekyung in turn. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 936
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts Jin Taekyung, his publicly acknowledged second Disciple and intended heir; warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, remains Peng Cheolhu's rival, and is the target of an attack by the assassin Heaven's Slaughter.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 936
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 936
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 930
- **Aliases:** None
- **Role:** An unidentified legendary martial artist regarded as a pinnacle above the Ten Kings; more than fifty years ago, he defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, appearing first as a white-bearded elder and later as a young boy; Mae Jonghak received several teachings from him, and he left the Bow Saint a letter describing a chosen one who would bring a new dawn, while his identity, whereabouts, and possible connection to Cheon Taemin remain unknown.

### Peng Cheolhu.md

# Peng Cheolhu (벽력도왕)

- **Safe through:** Chapter 841
- **Aliases:** Thunderbolt Saber King
- **Role:** Peng Cheolhu is the Thunderbolt Saber King, a Ten Kings master and Great Hero of the Hebei Peng Family.
- **Personality:** Boisterous, hot-tempered, argumentative, and protective toward those connected to his close friend Hong Dao.
- **Voice:** Loud, blunt, confrontational, and prone to disguising embarrassment or retreat as serious martial instruction.
- **Relationships:** Long-standing rival and friend of Jeok Cheongang; close friend of Hong Dao; protective toward Hong Dao's Disciple Unnamed.

## Korean source

```text
＃938화



“한 오십 년쯤 지났나?”

적천강은 형형색색의 기화요초(琪花瑤草)로 가득한 정원을 바라보며 중얼거렸다.

“그 무렵 섬서성의 여산(驪山)이 딱 이런 모습이었지. 완연한 봄이라 온갖 초목이 흐드러지게 피어 있었어.”

단순히 옛 추억에 잠긴 늙은이의 혼잣말이 아니다.

이끼로 가득한 담벼락에 기대어 앉아 있는 누군가에게 건네는 말이기도 했다.

“소화산(小華山).”

“응?”

“소화산이에요. 여산이 아니라.”

담담하면서도 맑은 음성.

궁성의 반박에 적천강이 고개를 저었다.

“그럴 리가. 뜨끈한 온천물에 몸을 담갔던 기억이 생생한데. 자고로 옛날부터 온천 하면 여산이었어.”

“온천이 아니라 작은 연못이었어요. 누군가가 차가운 물은 질색이라면서 열양지기로 연못을 달구기 전까지는.”

“그랬나?”

“벽력도왕(霹靂刀王)이 길길이 날뛰는 바람에 한바탕 싸움이 벌어질 뻔했던 건 까맣게 잊은 모양이군요.”

“팽가 놈이?”

고개를 끄덕이는 궁성의 모습에, 적천강이 눈살을 찌푸렸다.

“기억은 안 나지만 지금이나 그때나 머저리인 건 한결같았군. 그깟 물 좀 덥혔다고 법석을 떨다니.”

“충분히 그럴 만했어요. 벽력도왕은 그때 이미 연못 안에 들어가 있었던 상황이었으니까.”

“워낙 한 덩치 하는 놈이라 곰으로 착각했던 모양이지.”

적천강의 뻔뻔한 대답에 궁성은 작게 한숨을 내쉬었다.

“여전하군요. 당신은.”

“사람도 결국 저 꽃들과 별다를 거 없어. 밤낮으로 비바람을 맞고 갑작스럽게 환경이 변하면 죽기 마련이지. 노부처럼 언제나 한결같아야 하루라도 오래 살지 않겠나.”

“그래서, 장수하는 비결이라도 알려 주려고 날 찾아왔나요?”

“노부가 그리 한가해 보이나?”

“이렇게 불쑥 찾아와서 떠올리기 싫은 옛이야기까지 꺼내는 것을 보면, 그리 바빠 보이지도 않는군요.”

적천강은 귓가로 흘러 들어오는 건조한 목소리에 쓴웃음을 머금었다.

이번만큼은 궁성의 말에 동의할 수밖에 없었다.

아무리 생각해도 즐거운 추억은 아니었으니까.

이제는 시기도 정확히 기억나지 않는 오십여 년 전의 봄, 그들은 단지 웃고 떠들기 위해 그곳에 모인 것이 아니었다.

“삼천 명의 결사대가 함께 산을 올랐고, 하루가 채 지나기도 전에 그들 중 절반이 그곳에 뼈를 묻었지.”

그리고 화창한 봄을 맞아 푸르렀던 소화산(小華山)은, 온통 붉게 물든 화산(火山)이 되었다.

지금도 눈앞에 선하다.

산자락을 타고 솟구치던 불길이.

핏물은 계곡물과 뒤섞였고, 헤아릴 수도 없을 만큼 무수한 시체가 사방에 뒹굴었다.

종남. 화산. 하북팽가.

그와 더불어 세인들의 뇌리에 그리 오랫동안 각인되지 못했던 정파의 중소 세력들.

이를테면 당시 태원진가의 이공자였던 화양검 진백양 또한 그곳에 있었다.

삼천의 정예 결사대는 다섯 명의 대마두가 이끄는 일만의 마교도를 향해 파도처럼 나아갔고, 새하얀 포말 대신 핏물을 흩뿌리며 스러졌다.

그리고 동틀 무렵 산처럼 쌓인 마교도들의 시체 위에서 승리의 함성을 내지르는 그들의 중심에는, 두 명의 왕과 하나의 별이 있었다.

“천삼백십구 명.”

“……!”

“그날 죽은 사람들의 숫자예요.”

불현듯 밤공기를 뚫고 울려 퍼지는 나지막한 목소리.

순간 멈칫한 적천강은 천천히 돌아섰다.

“기억하고 있었나. 그들 모두를?”

비록 몸은 젊어졌으나 눈빛에 담긴 세월만은 여전하다.

노회한 적천강의 두 눈에, 자신과 닮은 눈빛을 한 여인의 모습이 비쳤다.

“잊은 적 없어요. 한순간도.”

“……몰랐군. 이런 사람이었는지.”

“안다고 해서 달라지는 건 아무것도 없어요. 제가 그들을 그저 기억만 하는 것처럼.”

잠시 침묵하던 궁성이 덧붙였다.

“그저, 그런 시절이었으니까.”

적천강은 작게 고개를 끄덕이며 뇌까렸다.

“그래, 그랬지.”

그 시절 마교의 기세는 무시무시했다.

아니, 압도적이었다.

파도처럼 들이닥친 십만마도(十萬魔道)는 곤륜파를 박살 내며 청해성을 넘었고, 이어 세 갈래로 나뉘어 거침없이 진군했다.

사천으로. 감숙으로. 그리고 섬서를 넘어 이른바 중원(中原)이라 불리는 대륙의 심장부까지.

그것은 구파일방과 오대세가조차 막아설 수 없는 거대한 파도였고, 규합되지 못한 채 각자의 영역을 지키고 있던 정파 세력은 순식간에 허물어졌다.

마교가 오랜 세월 동안 갈망해 왔던 마도천하(魔道天下)의 위업도 더는 허무맹랑한 이야기가 아니었다.

한 사람이 등장하기 전까지는.

“감히 구화산에 불을 지른 그 잡것들을 모조리 잡아 죽이고 하산한 그날, 노부가 무슨 생각을 하고 있었는지 아나?”

적천강은 궁성의 대답을 기다리지 않고 말을 이었다.

“마음 깊이 다짐했지. 이 목숨이 끊어지는 마지막 순간까지, 한 놈이라도 더 많은 마교도를 죽이겠다고.”

이미 전세가 기울어진 상황에서, 그것도 혈혈단신의 몸으로 마교와 맞서는 것은 미친 짓이었다.

다른 누구도 아닌 화왕 적천강이기에 할 수 있었던 미친 짓.

“그런데 노부보다 더 정신 나간 작자가 있더라고.”

적천강은 껄껄 웃었다.

남궁세가마저 몰아내고 안휘성을 점령한 마교도들에게 곧장 쳐들어가려던 그때의 기억이 떠올라서였다.

“도무지 믿을 수 없었지. 삼천이나 되는 마교도가 한 사람에게 패퇴했다는 사실을.”

그 삼천의 마교도들은 이제 고작 삼류를 벗어난 어중이떠중이들이 아니었다.

마교의 혹독한 훈련을 거쳐 탄생한 정예들이자, 천마에게 절대적인 충성을 맹세한 광신도들.

거기에 더하여 초절정의 경지에 오른 대마두(大魔頭)가 둘씩이나 포함되어 있었다.

“물론, 나중에는 믿을 수밖에 없었지.”

좀처럼 믿을 수 없는 이야기였기에 도망치던 마교도 여럿을 붙잡아 심문했고, 우두머리 격이었던 두 명의 대마두와 절반에 달하는 병력이 증발했다는 사실을 확인할 수 있었다.

그것도 정체 모를 누군가에 의해.

“그 순간, 돌아가신 스승님께서 종종 하시던 말씀이 문득 생각났지. 천하는 넓고 고수는 많으니 더욱 정진해야 한다는 그 말씀이.”

그러나 얼마 지나지 않아 알게 되었다.

적천강이 부족한 것이 아니라, 정체를 알 수 없는 그자가 특출난 것이었다는 것을.

아니, 그 누구라 해도 그자에 비하면 평범해질 수밖에 없다는 것을.

“무신(武神).”

출신이나 이름도, 나이도 모른다.

심지어는 얼굴조차도 제대로 알려진 바가 없다.

그는 모든 종류의 무공을 자유자재로 다루었고 역용술(易用術) 또한 예외는 아니었으니까.

그럼에도 모든 이가 무신을 믿고 따랐다.

그는 그런 존재였다.

어둠에 잠긴 천하를 밝히는 유일한 등불이었고, 홀로 하늘 위에 떠 있는 태양이었다.

그러나 바로 그랬기에, 본능처럼 그에게 가까이 다가서지 못하고 주위만 맴돌 수밖에 없었다.

조심스럽게 내뻗은 손짓에 실린 바람이 자신들의 유일한 등불을 꺼트리지는 않을까 하는 염려에.

한 걸음만 더 다가서면 태양이 발산하는 강렬한 열기에 되레 타들어 가지는 않을까 하는 우려에.

“그렇게 무신의 정체는 끝까지 드러나지 않았지. 아니, 감히 상상할 수조차 없었을 게야. 그 누구보다 가까이에서 그를 섬겼던 천면호리(天面狐狸)조차도.”

하지만 이제는 안다.

세상에 알려지지 않았던 무신의 비밀을.

더불어 적천강은 비로소 이해할 수 있었다.

어찌 그가 무신이라 불릴 수 있었는지.

“신력(神力)이라 했던가. 그 알 수 없는 힘.”

마치 혼잣말 같은 적천강의 뇌까림에, 궁성은 천천히 자리에서 일어났다.

“왜, 여기저기 소문이라도 내실 생각인가요?”

“이제 겨우 말년에 다시 사람 구실 하며 사는데, 노망난 늙은이 취급받을 수는 없지.”

피식 실소를 흘린 적천강이 입을 열었다.

“그래서 노부가 듣고 있다는 걸 빤히 알면서도 이야기를 멈추지 않았던 건가? 단지 그 녀석의 스승이라서?”

“굳이 감출 이유가 없다고 생각했을 뿐이에요.”

궁성이 적천강을 응시하며 말을 이었다.

“이미 전장에서 봤거든요. 서로를 구하기 위해 기꺼이 목숨마저 내던지는 스승과 제자의 모습을.”

“……!”

“그때 깨달았어요. 두 사람 사이의 신뢰가 어느 정도인지. 그러니 진실을 감추는 건 무의미했죠.”

숨기는 것이 없으니, 비밀도 없다.

궁성은 두 사제(師弟)의 관계를 정확히 간파해 냈고, 믿을 수 없는 이야기가 오가는 와중에도 한 치의 흔들림 없이 묵묵하게 상황을 지켜보던 적천강의 기파를 느끼고 확신했다.

“언제부터 알고 있었죠? 당신의 제자가 남들보다 특별하다는 사실을.”

적천강이 담담한 목소리로 대답했다.

“처음부터 지금까지. 언제나 항상.”

“약간의 오해가 있는 것 같은데, 제 말은 그 아이에 관한 진실을 언제부터 알고 있었…….”

“그것이 그리 중요한가?”

이어지려는 말을 끊어낸 적천강이 궁성을 바라보았다.

어느샌가 깊게 가라앉은 눈동자에 그녀의 모습이 비쳤다.

“변하는 건 아무것도 없어. 노부가 녀석을 제자로 받아들인 그 날부터, 우리는 모든 것을 나누고 함께했으니.”

그 순간, 궁성은 문득 미간을 좁혔다.

자신이 원했던 대답을 듣지 못해서가 아니라, 서서히 달아오르는 주위의 공기를 느꼈기 때문이었다.

우우웅.

바람이 멈췄다. 대기가 몸을 떨었다.

그리고 그 모든 것의 중심에, 화왕(火王) 적천강이 있었다.

“한데.”

줄곧 정원을 향하고 있던 고개가 천천히 돌아선다.

불그스름하게 물든 안광(眼光)이, 어둠 속에서 도깨비불처럼 일렁였다.

“그런 노부의 제자를, 고작 그 별것 아닌 확인을 위해 위험에 빠트린 것이냐.”

진태경이 핏물을 흩뿌리며 쓰러지던 그 순간, 전신을 지배했던 분노와 절망을 적천강은 잊지 않았다.

설령 자신의 제자가 명문대파의 장로, 아니 어쩌면 문주들과 어깨를 나란히 할 만큼 강해졌다 해도.

또래와 같은 치기 어린 청년이 아니라, 일문의 종사(宗師)를 자처할 만큼의 그릇이라 해도.

진태경은 그의 하나뿐인 제자였다.

화아아아악.

회오리치듯 솟아오른 백색의 겁화.

끔찍한 열기로 인해 피어오르는 그 아지랑이 속에서, 궁성은 담담히 입을 열었다.

“이천오백육십이 명.”

궁성을 향해 나아가려던 적천강의 발걸음이 우뚝 멈췄다.

이천오백육십이 명. 저 알 수 없는 대답이 무엇을 의미하는지 알 것 같았기 때문이다.

“사흘 전, 대연회장에서 죽은 아군의 숫자입니다.”

“잘 아는군. 하지만…….”

적천강의 입술 사이로 그가 지닌 기운과는 다른 서늘한 음성이 흘러나왔다.

“누군가가 한발 먼저 나섰다면, 그중 절반도 죽지 않았을 것이다.”

“네. 분명 그랬겠지요.”

“뭐라!”

화륵.

적천강의 전신에서 피어오르는 화염의 열기가 더욱 강해진 그때, 궁성이 침착하게 말을 이었다.

“그럼에도 이 두 눈으로 직접 확인해야 했습니다. 진정 그 아이가 선택받은 자가 맞는지. 어떤 힘과 심성을 지녔는지.”

“감히……!”

“전투가 끝나면 언제나 죽은 이들의 숫자를 헤아렸어요. 이렇게라도 그들을 기억하기 위해서.”

“그 입 닥치지 못할까!”

“하지만 사흘 전의 열 배, 백 배……. 아니, 천 배가 넘는 사람들이 죽는다면, 그때에도 당신은 지금처럼 분노할 수 있을까요?”

“……!”

“당신에게는 아끼는 제자를 위험에 빠트린 별것 아닌 확인이었을지 모르지만, 내게는 아니었습니다.”

파르르 떨리는 적천강의 눈동자를 바라보며, 궁성은 입을 열었다.

“그보다 훨씬 더 많은, 어쩌면 이 세상 모두를 위해 내린 결정이었어요.”

그것이 그분께서, 무신이 나를 선택한 이유이기도 하니까.

작게 읊조린 뒷말이 서늘한 밤공기를 타고 퍼져 나간 그 순간이었다.

사박.

어둠 속 저 멀리, 어렴풋이 들려온 미세한 인기척.

동시에 고개를 돌린 두 사람의 시선에, 온 힘을 다해 달려오는 혁무진의 모습이 비쳤다.
```

## Final English reading copy

```markdown
# Chapter 938

“Has it been about fifty years?”

Jeok Cheongang murmured as he looked out over the garden, filled with flowers and rare plants of every color.

“Back then, Mount Li in Shaanxi looked just like this. It was the height of spring, and all kinds of plants were in full bloom.”

It wasn’t simply an old man talking to himself as he reminisced.

He was also speaking to someone sitting with their back against a moss-covered wall.

“Mount Small Hua.”

“Hmm?”

“It was Mount Small Hua, not Mount Li.”

Her voice was calm and clear.

Jeok Cheongang shook his head at the Bow Saint’s correction.

“That can’t be right. I remember soaking in steaming hot spring water. Mount Li has been famous for its hot springs since ancient times.”

“It wasn’t a hot spring. It was a small pond—until someone heated it with Scorching Yang Qi, claiming he couldn’t stand cold water.”

“Was it?”

“You seem to have completely forgotten how the Thunderbolt Saber King went berserk and nearly started a fight.”

“That Peng bastard?”

The Bow Saint nodded. Jeok Cheongang furrowed his brow.

“I don’t remember it, but he’s been an idiot then and now. Making a fuss because someone warmed up a little water.”

“He had every reason to. The Thunderbolt Saber King was already in the pond.”

“He was so big I must’ve mistaken him for a bear.”

At Jeok Cheongang’s shameless reply, the Bow Saint let out a small sigh.

“You haven’t changed.”

“People aren’t so different from those flowers. They’re battered by wind and rain, day and night, and die when their surroundings suddenly change. To live even one day longer, you have to stay the same—like this old man.”

“So, did you come to tell me the secret to a long life?”

“Does this old man look like he has that much free time?”

“You showed up out of nowhere and brought up old stories I’d rather not remember. You don’t look that busy, either.”

Jeok Cheongang wore a bitter smile at the dry voice reaching his ear.

This time, he couldn’t help agreeing with the Bow Saint.

No matter how he looked at it, those weren’t happy memories.

It was a spring day more than fifty years ago, though he couldn’t remember exactly when. They hadn’t gathered there simply to laugh and talk.

“Three thousand members of the death squad climbed the mountain together. Before even a day had passed, half of them had been buried there.”

And Mount Small Hua, green beneath the bright spring sky, became a mountain of fire, dyed entirely red.

He could still see it clearly.

Flames surging up the mountainside.

Blood mingling with the stream water, and countless bodies scattered in every direction.

The Zhongnan Sect. The Huashan Sect. The Hebei Peng Family.

Alongside them were the smaller orthodox factions, whose names had not been etched in people’s memories for nearly as long.

Among them was the Blade of Flowers, Jin Baekyang, then the Second Young Master of the Jin Family of Taiyuan.

The three thousand elite members of the death squad surged like a wave toward ten thousand Demonic Cult followers led by five great fiends—and fell, spraying blood instead of white foam.

At dawn, as they stood atop a mountain of Demonic Cult corpses and roared their victory, two kings and one star stood at their center.

“One thousand three hundred and nineteen.”

“……!”

“That’s how many people died that day.”

A quiet voice suddenly rang through the night air.

Jeok Cheongang paused, then slowly turned around.

“You remembered? Every one of them?”

Though his body had grown young again, the years in his eyes remained unchanged.

In Jeok Cheongang’s seasoned eyes was reflected a woman whose gaze resembled his own.

“I never forgot. Not for a moment.”

“……I didn’t know you were like this.”

“Knowing doesn’t change anything. Just as remembering them is all I can do.”

The Bow Saint fell silent for a moment, then added,

“That was simply the kind of time it was.”

Jeok Cheongang nodded faintly and muttered, “Yes. It was.”

The Demonic Cult’s momentum had been terrifying back then.

No—it had been overwhelming.

The hundred thousand of the Demonic Path swept in like a wave, crushing the Kunlun Sect as they crossed Qinghai. Then they split into three forces and advanced without resistance.

Toward Sichuan. Toward Gansu. And through Shaanxi toward the very heart of the continent, the land known as the Central Plains.

It was a massive wave that not even the Nine Sects and One Gang and the Five Great Families could stop. The orthodox factions, unable to unite and each guarding its own territory, crumbled in an instant.

The Demonic Cult’s long-coveted dream of ruling the world through the Demonic Path was no longer some far-fetched fantasy.

Not until one man appeared.

“Do you know what I was thinking the day I came down from Mount Jiuhua, having killed every last one of those bastards who dared set it ablaze?”

Jeok Cheongang continued without waiting for the Bow Saint to answer.

“I swore deep in my heart that I’d kill as many Demonic Cult followers as I could until the very last moment of my life.”

With the tide of war already turned against them, facing the Demonic Cult alone was madness.

Madness that no one but Jeok Cheongang, the Fire King, could pull off.

“But there was someone even crazier than this old man.”

Jeok Cheongang laughed heartily.

He was remembering how he’d been about to charge straight at the Demonic Cult forces occupying Anhui after driving even the Nangong Family from their territory.

“I just couldn’t believe it. Three thousand Demonic Cult followers defeated by one man.”

Those three thousand weren’t a ragtag bunch who’d only just advanced beyond Third Rate.

They were elites forged through the Demonic Cult’s brutal training, fanatics who’d sworn absolute loyalty to the Heavenly Demon.

And among them were two great fiends who’d reached the Supreme Peak realm.

“Of course, I had no choice but to believe it eventually.”

The story was too incredible to accept, so he’d caught several Demonic Cult followers as they fled and interrogated them. He confirmed that their two leading great fiends and nearly half their forces had vanished.

At the hands of someone whose identity was unknown.

“In that moment, I suddenly remembered something my late Master used to say. The world is vast and there are many masters, so you must keep striving.”

But it hadn’t taken long for him to learn the truth.

It wasn’t that Jeok Cheongang was lacking. That unknown man was simply exceptional.

No—compared to him, anyone would seem ordinary.

“The Martial God.”

No one knew his origin, his name, or his age.

Even his face was scarcely known.

He could freely use every kind of martial art, and the disguise technique was no exception.

And yet everyone believed in and followed the Martial God.

That was the kind of person he was.

He was the only lamp illuminating a world steeped in darkness, the sun shining alone above the heavens.

And that was precisely why they could never approach him on instinct. They could only circle around him.

They feared that the wind from a cautious outstretched hand might snuff out their only light.

They worried that if they took just one more step, the sun’s fierce heat might burn them alive.

“So the Martial God’s identity remained a mystery to the very end. No—no one could even dare imagine it. Not even the Thousand-Faced Fox, who served him more closely than anyone.”

But now he knew.

The secret of the Martial God that had never been revealed to the world.

And at last, Jeok Cheongang understood.

How he could have been called the Martial God.

“Was it divine strength? That incomprehensible power.”

At Jeok Cheongang’s muttering, which sounded almost like he was talking to himself, the Bow Saint slowly rose to her feet.

“Why? Planning to spread rumors about it?”

“This old man’s only just started acting like a proper person again in his old age. I can’t have people thinking I’ve lost my mind.”

Jeok Cheongang let out a quiet laugh.

“So you kept talking even though you knew full well I was listening. Just because I’m that brat’s Master?”

“I just didn’t see any reason to hide it.”

The Bow Saint looked at Jeok Cheongang and continued.

“I already saw it on the battlefield. A Master and Disciple willing to throw away their lives for each other.”

“……!”

“That’s when I understood how much trust there was between you two. So there was no point hiding the truth.”

There was nothing hidden, so there were no secrets.

The Bow Saint had seen the bond between Master and Disciple clearly. And as the unbelievable story unfolded, she sensed Jeok Cheongang’s qi remain steady while he silently watched, confirming what she had understood.

“When did you know your Disciple was special?”

Jeok Cheongang answered in a calm voice.

“From the beginning to now. Always.”

“I think there’s been a slight misunderstanding. I meant, when did you learn the truth about that boy……?”

“Does that matter?”

Jeok Cheongang cut her off and looked at the Bow Saint.

Her reflection appeared in his eyes, which had grown dark and solemn.

“Nothing changes. From the day I took that brat as my Disciple, we’ve shared everything and faced it all together.”

The Bow Saint’s brow drew together.

Not because she hadn’t gotten the answer she wanted, but because she felt the air around them slowly heating up.

*Rumble.*

The wind stopped. The air trembled.

And at the center of it all stood Jeok Cheongang, the Fire King.

“Still……”

The head that had been turned toward the garden slowly swung around.

His eyes glowed red, flickering in the darkness like ghost fires.

“Did you put my Disciple in danger just to make that trivial confirmation?”

Jeok Cheongang had not forgotten the rage and despair that had seized him when Jin Taekyung collapsed, spraying blood.

Even if his Disciple had grown strong enough to stand shoulder to shoulder with Elders of great sects—or perhaps even their Sect Leaders.

Even if he were no longer a young man acting on the rashness of his peers, but someone with the stature to call himself a Sect Patriarch.

Jin Taekyung was his one and only Disciple.

*Whoosh!*

White hellfire surged upward in a spiraling column.

Through the heat haze rising from its terrible warmth, the Bow Saint spoke calmly.

“Two thousand five hundred and sixty-two.”

Jeok Cheongang’s steps toward her came to an abrupt halt.

He thought he knew what that incomprehensible answer meant.

“That’s how many of our people died in the grand banquet hall three days ago.”

“You know the number well. But……”

A cold voice, unlike the energy he wielded, slipped between Jeok Cheongang’s lips.

“If someone had acted first, not even half of them would have died.”

“Yes. That’s surely true.”

“What!”

*Whoosh.*

The flames rising from Jeok Cheongang grew hotter, but the Bow Saint continued steadily.

“Even so, I had to see it with my own eyes. Whether that boy truly was the chosen one. What kind of power he had—and what kind of heart.”

“How dare you……!”

“After every battle, I counted the dead. It was my way of remembering them.”

“Will you shut your mouth!”

“But if ten times as many people died as they did three days ago—one hundred times as many…… No, more than a thousand times—would you still be able to be this angry?”

“……!”

“To you, it may have been a trivial confirmation that put your precious Disciple in danger. But it wasn’t trivial to me.”

The Bow Saint looked at Jeok Cheongang’s trembling eyes and spoke.

“It was a decision I made for far more people than that. Perhaps even for everyone in this world.”

“That was also why that person—the Martial God—chose me.”

Her quiet murmur spread through the cold night air.

*Step.*

From far away in the darkness came the faint sound of someone approaching.

At the same moment, both of them turned. Hyuk Mujin was running toward them with all his might.
```
