<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1121.txt",
      "sha256": "8f951ebf49f34fb55398eaf6e68eeb255514854c4f27bb49812968c5f219b98c",
      "bytes": 11886
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "9045ecda7b56e976b18e8fd7f5c7edd79d396cf2ce2d03ba700df936483f47dc",
      "bytes": 1215
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "307189767337c5394589bdcaa7f59f3e28cdf1da9d380fecae4d63447025be4b",
      "bytes": 245178
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "ea6b46cb1fda0e09b6e4f138d6fbd00ca5c3f388d735d0526bc244acde1044fb",
      "bytes": 915
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "8820fe7d20fdac25038c5b685ce85db7e2739a14484399fa695f4dfa3328b0f1",
      "bytes": 1230
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "8eac9259253e4dd050a4f726ecf8007c2bf8b1e875294a9d2b7307a8a55ac332",
      "bytes": 1513
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "bdc13fa014bb8bb4fe14070491a59969349d476ae211d6b22546b84d3893127f",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "46fac61c3539ffb6cd34887f81c4459ea7b364b99588e417a0f42ea45ed95e3c",
      "bytes": 623
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "fbe26e0ec5f89ce57df0b052ec3ff3869882eaa7728f4db5939e2d5122fb744c",
      "bytes": 289919
    }
  ],
  "estimated_tokens": 10430
}
-->

# Durable State Update — Chapter 1121

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
1 and safe_through 1121. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1121. Profile updates may replace only one
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
  "chapter": 1121,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1121,
    "continuity_sources": [1121],
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
    "The Inner City crumbled while surrounded by enemy forces; several people who retreated from the other gates have not returned."
  ],
  "continuity_sources": [
    1119,
    1120
  ],
  "open_questions": [
    "Will Hyuk Mujin survive his chest wound?",
    "Who is the black-robed figure, and what was the outcome of the attack at the East Gate?",
    "Who has not returned to the Inner City, and what happened to them?",
    "What happened to Great Sir and Black Ghost?",
    "Who survived the collapse of the Inner City?"
  ],
  "safe_through": 1120,
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
| 암천     | **Dark Heaven**                  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 상태               | **Status**                     |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 기경팔맥 | **Eight Extraordinary Meridians** | The eight extraordinary meridians of wuxia physiology. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 내성 | **Inner City** | Fortified inner district of the Murim Alliance. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 동문 | **East Gate** | One of the Nanman Beast Palace's gates. |
| 파리 | **Paris** | The city containing Ares Guild's branch attacked at the chapter's end. |
| 육부 | **Six Ministries** | The central government ministries. |
| 천수 | **Tianshui** | City on Gansu’s eastern edge, bordering Shaanxi. |
| 대술사 | **Grand Mage** | Title of the veiled woman leading the white-robed mages. |
| 미친놈 | **Madman** | Insult Great Sir adopts as a name; also appears in the System display. |
| 서녕 | **Xining** | Capital of Qinghai. |
| 적도 | **Red Blade** | Named blade that shatters in Taekyung’s flames. |

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
| 혈주 | 천주 | servant_to_absolute_master | Lord of Heaven | worshipful and deferential | Blood Lord repeatedly addresses the Lord of Heaven while apologizing and receiving power. |
| 천주 | 혈주 | absolute_master_to_servant | Blood Lord | commanding and reproachful | The Lord of Heaven directly rebukes Blood Lord and then empowers him. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 살성 | 청풍 | senior martial figure to younger companion | you | blunt and familiar | The Slaughter Saint scolds Cheongpung for disappearing without a word. |
| 청풍 | 살성 | younger companion to senior martial figure | old man | polite and familiar | Cheongpung apologizes and explains why he wandered off. |
| 천주 | 대술사 | master to servant | you | commanding and authoritative | Addresses her through mind-voice, ordering her to report, raise her head, and depart. |
| 대술사 | 천주 | servant to master | Lord of Heaven | extremely deferential | Uses reverent titles and self-abasing language while reporting and pleading. |
| 혈주 | 대술사 | fellow servant of the same person | you; you bitch | insulting-casual | Blood Lord taunts the Grand Mage and uses a crude insult. |
| 대술사 | 혈주 | fellow servant of the same person | you | contemptuous-casual | The Grand Mage addresses the Blood Lord while rebuking him. |
| 진태경 | 혈주 | hostile_opponent_to_hostile_opponent | you; you son of a bitch | insulting-casual | Taekyung insults the Blood Lord while challenging his claim that he will kill him. |
| 궁성 | 살성 | allied martial masters | Slaughter Saint | formal-polite | The Bow Saint directly addresses him as 살성 and uses 당신 while urging him to stay and defend the South Gate. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1117
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure and formidable combatant who commands weapons telekinetically and absorbs blood to restore vitality.
- **Personality:** Cunning and controlling, he plans around opponents’ strengths and learns from past mistakes; his confidence in his overwhelming power is genuine rather than bluster, and he remains devoted to the Lord of Heaven despite resenting being treated as disposable and Taekyung’s apparent favor.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven and suspects the Lord wants Jin Taekyung above all else; he recognizes Cheongpung and remembers a debt to Sword Saint Mae Jonghak.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 1113
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, Sword Saint Mae Jonghak’s grandson and Disciple, a Supreme Peak master known as the Huashan Divine Dragon, creator of Mimi Step, and master of the Azure Dragon Pavilion; he has mastered the Slaughter Saint’s Ghost Illusory Slaughter Step and blended it with his Dark Fragrance Drift.
- **Personality:** Affable, dreamy, and childlike, with innocent curiosity, a deep love of martial arts, and compassion; guided by his grandfather’s righteousness and Taekyung’s chivalry, he meets danger with resolve and trusts Taekyung without wavering.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions; Taekyung is his true martial rival and the person whose way of life he admires, and the Slaughter Saint is his mentor in concealment and Ghost Illusory Slaughter Step.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1114
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and freely follows his own path rather than pursuing grand causes; he cares about protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1120
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1120
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃1121화



높이나 크기, 혹은 내구성을 떠나 성벽의 존재 유무는 공성전에서 매우 큰 지분을 차지한다.

제아무리 볼품없는 성벽이라 할지라도 벽은 벽이니까.

그리고 그런 의미에서, 외적과의 시가전까지 염두에 두고 지어진 서녕의 내성은 외성의 그것에 비할 수는 없을지언정 전투에 있어 상당한 이점을 지니고 있었다.

분명, 그랬어야 했다.

콰아아아앙!

그 모든 것은 찰나에 시작되어, 찰나에 끝났다.

오직 한 사람의.

아니, 한 괴물에 의해서.

구구구궁!

자욱하게 피어오른 먼지구름 속, 흡사 비명과도 같은 굉음과 함께 허물어지는 내성의 성벽을 바라보며 혈주(血主)는 광포하게 웃었다.

이미 인외(人外)의 힘을 얻었다고 자부하는 그로서는 지금 눈 앞에 펼쳐진 이 상황이 실로 우습기 짝이 없었다.

당장 사방으로 흩어져 꽁무니를 빼도 부족할 판국에, 기껏 도망쳐 온 곳이 내성이라니.

“고작 저런 돌무더기 따위로, 이 몸을 막을 수 있으리라 생각했더냐.”

나직한 뇌까림과 함께, 혈주는 다시금 적도(赤刀)를 들어 올렸다.

츠츠츠츠!

붉은 도신을 타고 솟구치는 핏빛 섬광.

삽시간에 반월의 형태를 갖춘 거대한 도강(刀罡)이 공간을 가로지르며 발출되려던 그 순간이었다.

“그만!”

불현듯 울려 퍼진 다급한 목소리.

그러나 갑작스럽게 나타난 누군가의 제지에도 불구하고, 혈주는 망설임 없이 적도를 내리그었다.

화아아악!

공간이 붉게 물든다.

마치 벼락이 치는 듯한 찰나의 번쩍임과 함께 수십여 장의 거리를 지워 낸 강기가 먼지구름 속으로 스며들었다.

아니, 집어삼켰다.

실로 괴물이라 부를 수밖에 없는 흉포한 기세로.

콰드드드득!

하늘과 땅을 뒤흔드는 굉음과 진동을 느끼며, 혈주는 부드럽게 웃었다.

그리고 감히 자신을 막으려 했던 불청객을 향해 시선을 옮겼다.

“늦었군. 조금 더 빨리 말하지 그랬나. 그랬다면 아슬아슬하게라도 멈출 수 있었을 텐데.”

짐짓 태연하기까지 한 혈주의 대답에, 대술사(大術士)의 눈빛이 차갑게 가라앉았다.

“이게 무슨 짓이지?”

“무슨 짓이긴, 보는 그대로지.”

어깨를 으쓱한 혈주가 턱짓으로 저 멀리 피어오른 먼지구름을 가리켰다.

“놈들의 마지막 희망을 부수고 있었다. 더는 저항할 마음조차 들 수 없도록.”

“너…….”

문득 흐려지는 말꼬리.

쉽사리 말을 잇지 못한 채, 여전히 웃고 있는 혈주를 말없이 응시하던 대술사가 이내 담담한 어조로 물었다.

가장 중요한, 한 사람의 생사 유무를.

“그래서, 아직 무사한 거겠지?”

“무사하다 못해 훌륭하지. 날 봐, 이 힘이 느껴지지 않나?”

마치 부모에게 무언가를 자랑하는 어린아이처럼 천진난만하게 두 팔을 펼치는 혈주의 모습에, 대술사의 가슴 한구석이 서늘해지는 것을 느꼈다.

다르다.

달라졌다.

평소에 비해 모든 것이.

완전한 핏빛에 물들여진 동공도, 인간과 괴물이 뒤섞인 것처럼 기괴한 몸뚱어리에서 자연스럽게 흘러나오는 미증유의 기세도 그러했지만 정작 가장 큰 변화는 따로 있었다.

광기(狂氣).

도무지 그 깊이와 농도를 짐작할 수 없는 끝 모를 광기를, 지금 이 순간 대술사는 느끼고 있었다.

그리고 자신이 그 사실을 인지했음을 절대 내색해서는 안 된다는, 본능적인 판단도 함께.

“시답잖은 헛소리는 집어치워. 그런 뜻으로 물어본 게 아니라는 것쯤은 누구보다 잘 알고 있을 텐데.”

“허, 이거 섭섭한데. 한 배를 탄 동료의 안위보다 중요한 게 있었다니.”

“우리가 언제부터 그리 살가운 사이였지?”

“뭐, 그렇게까지 말한다면 딱히 할 말은 없군. 좋아.”

과장 되리만치 한숨을 크게 내쉰 혈주가 말을 이었다.

“진태경, 그놈이라면 아직 살아있다. 아마도.”

“아마도, 라고?”

“그럼 분명히, 라고 정정하지. 저곳에 남아 있는 노괴(老怪)들이 그 핏덩이 하나를 지키지 못했을 리는 없을 테니.”

대술사가 듣기에도 그리 안일한 추측은 아니었다.

불과 일각 전, 동문을 제외한 삼면의 성벽에서 일제히 퇴각한 수비군들은 내성으로 집결했고 그중에는 궁성과 살성. 그리고 화왕 적천강 역시 포함되어 있었으니까.

비록 내성으로 물러나는 과정에서 하나같이 상당한 부상을 입었으나, 설령 그렇다 하여도 진태경의 안위를 보장하지 못할 정도는 아니었을 것이다.

그리고 그런 혈주의 말이 사실이라는 것을 증명하듯, 때마침 저 멀리 서서히 흩어지는 먼지구름 너머로 익숙한 얼굴들이 모습을 드러냈다.

결코 죽어서는 안 되는, 가장 중요한 한 사람 역시도.

“……!”

막대한 피로와 내상으로 안색이 파리해진 살성과 궁성.

혹은 그들보다도 상태가 안 좋아 보이는 적천강의 존재 따위는, 지금 이 순간 대술사의 시야에서 잊혔다.

오직 한 사람.

진태경.

마침내 그의 모습을 확인한 순간, 그녀는 참았던 안도의 한숨을 내뱉었다.

틀림없다.

머리부터 발끝까지 온통 피로 뒤덮인, 영락없는 혈인(血人)의 몰골이었으나 진태경은 분명 살아 있었다.

비록 새하얀 빛을 띤 창을 지팡이 삼아, 청풍의 부축을 받으며 간신히 서 있는 것이 고작이었지만 대술사에게는 그것만으로도 충분했다.

그녀에게는 천주에게서 부여받은 불가사의한 힘, 마법(魔法)이 있었으니까.

하지만 멀리에서 보아도 위태롭게 느껴질 만큼, 진태경의 상태는 심각했다.

‘그분께 데려가야 해. 한시라도 빨리.’

어쩌면 마법으로도 완전한 치유가 불가능할 수도 있는 상황.

초조함을 느낀 대술사가 마음속으로 조용히 이동 주문을 읊으려던 그 순간이었다.

“왜, 무슨 급한 일이라도 있나?”

“……!”

불현듯 등 뒤에서 들려오는 혈주의 나직한 속삭임에, 대술사는 자신도 모르게 눈을 부릅떴다.

‘도대체 어떻게?’

무공의 핵심이자 뿌리가 기운의 축적이라면, 마법은 기운과의 감응.

그렇기에 기운의 파동에 누구보다 민감한 그녀다.

하지만 보이지도, 느끼지도 못한 사이에 혈주는 대술사의 후방을 점한 채 웃고 있었다.

마치 먹잇감을 입안에 넣은 맹수처럼.

“마법이라는 거, 생각할수록 재미있는 힘이더군. 수천수만 리를 눈 깜짝할 사이에 이동하는 것도 그렇고…… 반쯤 뒈져 가는 놈도 살릴 수 있고. 안 그래?”

목덜미에 닿는 뜨거운 숨결에, 대술사는 씹어뱉듯이 입을 열었다.

“이미 말했을 텐데. 시답잖은 헛소리는 집어치우라고.”

“헛소리?”

피식 실소를 흘린 혈주가 붉은 혀로 입술을 핥았다.

“아쉽지만 이번엔 아니야. 나는 다 잡은 먹잇감을 이런 식으로 놓치고 싶진 않거든.”

그 말에 담긴 의미를 깨달은 대술사는 이를 악물었다.

“혈주, 드디어 네놈이 미쳤구나.”

“그거참 희한하군. 네년은 언제나 나를 미친놈이라고 불렀던 것 같은데.”

“감히 그분의 뜻을…… 거스를 셈이냐?”

잠시의 침묵 후, 혈주가 선명한 미소를 머금은 채 대답했다.

마침내 가면과 족쇄를 벗어던진 그는 어느 때보다 자유롭고, 또한 강해져 있었다.

“괜찮잖아? 한 번쯤은.”

바로 그 순간.

서걱!

핏빛 섬광이 번뜩임과 동시에, 흐릿해진 대술사의 신형이 삼 장 밖에서 모습을 드러냈다.

그리고.

푸화아악!

피 분수를 내뿜으며 비틀거리던 몸뚱어리가, 실 끊긴 인형처럼 힘없이 허물어졌다.

철퍽.

그것으로 끝이었다.

피 웅덩이에 잠긴 몸은 미동조차 없었고, 부릅떠진 채 굳어 버린 눈에서는 한 줌의 생기(生氣)조차 찾아볼 수 없었다.

“죽일 생각까진 없었는데…… 뭐, 어쩔 수 없지.”

혼잣말처럼 중얼거린 혈주는 문득 주위를 둘러보았다.

어느덧 고요와 적막에 휩싸인 채 자신을 바라보는 무수한 시선들. 

내성을 빈틈없이 포위한 수만 명의 광신도가 크게 뜨인 눈으로 이 뜻하지 않은 상황을 지켜보고 있었다.

그리고 이번만큼은 쉽사리 동요를 숨기지 못하는 그들을 향해, 혈주는 담담하게 선언했다.

가장 짧으면서도 확실한, 오직 암천이기에 가능한 방식으로.

“위대하신 천주의 명을 받들어 배교자를 처단한 바, 이제 내가 전군을 지휘한다.”

“……!”

“……!”

“단 한 놈도 남김없이, 모조리 죽여라.”

마침내 무거운 침묵을 깨트리는 명령이 떨어진 그 순간.

두두두두!

천지를 뒤흔드는 함성과 함께, 물경 수만에 달하는 광신도들이 내성을 향해 돌격했다.

살아있는 신이자 유일한 절대자.

천주에게 맞서는 간악한 이교도들을 처단하기 위하여.

그리고 하나의 거대한 파도가 되어 나아가는 광신도들의 모습에, 크게 소리 내어 웃은 혈주는 발걸음을 뗐다.

그가 그토록 염원했던, 한 사람의 목숨을 빼앗기 위해.

“진태경-!”

미증유(未曾有)의 기운이 실린 괴물의 포효가, 전장을 집어삼키며 울려 퍼졌다.



* * *



“……!”

“……!”

공기가 떨린다. 귓가가 먹먹하다.

사방에서 쉴 새 없이 터져 나오는 함성과 비명이. 몸서리쳐질 만큼 차가운 강철의 소음이 전장을 휘감는다.

하지만 그 극심한 혼란과 흐릿한 감각 속에서도, 나는 느낄 수 있었다.

자신을 지키기 위해 수많은 적과 맞서 싸우는 이들에게서 뿜어져 나오는 온기를. 

동시에, 들었다.

기쁨과 광기에 물든 괴물의 포효를.

‘진태경.’

그래, 그건 내 이름이었다.

탄생과 동시에 주어진 것.

각기 다른 두 세계에서, 나는 하나이자 둘로 존재했다.

그리고 어쩌면, 오늘 이 자리가 내게 주어진 마지막일지도 몰랐다.

‘가야 해.’

어디서 그런 힘이 솟았는지, 나도 잘 모르겠다.

분명 오장육부가 뒤틀리고 기경팔맥(奇經八脈)이 갈기갈기 찢어졌을 텐데, 한 줌밖에 되지 않는 공력으로는 아무것도 하지 못할 것이 분명한데.

하지만 그럼에도, 청풍의 부축을 뿌리친 나는 무언가에 홀린 듯이 비틀비틀 걸음을 옮겼다.

서걱!

눈먼 칼이 어깨를 스친다.

아직 남아 있는지조차 몰랐던 핏물이 흘렀지만, 나는 고통도 느끼지 못한 채 손을 뻗었다.

우드득.

번들거리는 광신도의 눈동자가 고통으로 부릅떠진다. 

본능적으로 온 힘을 다해 내게 잡힌 손목을 빼내려 하지만, 그보다 한발 앞서 뻗어 나온 뜨거운 열기가 놈을 휘감았다.

퍼엉!

누군가에게는 타들어 갈 것 같은 불길이, 나에게 있어서는 더없는 온기처럼 느껴지는 이유는 나를 구해 준 이의 모습 때문일지도 모른다.

“노……야.”

온 힘을 다해 쥐어 짜낸 음성과 함께, 나는 적천강의 어깨를 붙잡으며 속삭였다.

“길을. 길을 열어 주십시오.”

“……!”
```

## Final English reading copy

```markdown
# Chapter 1121

Regardless of a wall’s height, size, or durability, whether it existed at all made a huge difference in a siege.

Even the shabbiest wall was still a wall.

And in that regard, Xining’s Inner City—built with the possibility of street fighting against foreign invaders in mind—had a considerable advantage in battle, even if it couldn’t compare to the Outer City’s walls.

It should have, anyway.

KWA-BOOOOM!

It all began in an instant, and ended in an instant.

At the hands of one man.

No—a monster.

Rumble.

As the Inner City wall crumbled amid a thick cloud of dust, a deafening roar like a scream, the Blood Lord laughed wildly.

To him, a man who prided himself on having gained power beyond human limits, the scene unfolding before his eyes was nothing short of laughable.

They should have scattered in every direction and run for their lives. And yet the best they could do was flee to the Inner City?

“Did you think a pile of rocks like that could stop me?”

With a low mutter, the Blood Lord raised the Red Blade once more.

Shhhhh!

A blood-red flash surged along its blade.

A massive half-moon of Force took shape in an instant, about to rip across the space between them—

“Stop!”

A voice suddenly rang out, urgent and sharp.

But even as someone appeared out of nowhere to stop him, the Blood Lord brought the Red Blade down without hesitation.

WHOOOSH!

The space turned red.

In a flash like a bolt of lightning, the Force swept across a distance of dozens of jang and sank into the dust cloud.

No—it swallowed it whole.

With a ferocity that could only be called monstrous.

KRRRUNCH!

Feeling the earth and sky shake with the deafening crash, the Blood Lord smiled smoothly.

Then he turned to look at the uninvited guest who had dared try to stop him.

“You’re late. You should’ve said something sooner. Then I might’ve stopped in the nick of time.”

At the Blood Lord’s almost nonchalant reply, the Grand Mage’s gaze turned cold.

“What have you done?”

“What does it look like?”

The Blood Lord shrugged and pointed with his chin at the distant cloud of dust.

“I was crushing their last hope. So they wouldn’t even want to resist anymore.”

“You…”

Her voice trailed off.

The Grand Mage stared silently at the still-smiling Blood Lord, unable to find the words. Then, at last, she asked in a calm voice about the one thing that mattered most: whether one person was still alive.

“So he’s still safe, right?”

“Safe? I’m better than fine. Look at me. Can’t you feel this power?”

The Blood Lord spread his arms with the innocent pride of a child showing off something to a parent. A chill crept into the Grand Mage’s chest.

He was different.

He’d changed.

Everything about him had changed.

His pupils, now completely blood-red. The unfathomable aura flowing naturally from his grotesque body, as if a human and a monster had been fused together. Those things had changed, but the greatest difference lay elsewhere.

Madness.

At that moment, the Grand Mage felt a bottomless madness whose depth and intensity she couldn’t begin to fathom.

And with it came the instinctive judgment that she must never let him know she’d noticed.

“Cut the pointless nonsense. You know better than anyone that’s not what I meant.”

“Now that’s disappointing. So something mattered more to you than the well-being of a comrade who’s in the same boat?”

“Since when were we so close?”

“Well, if you put it like that, I don’t have much to say. Fine.”

The Blood Lord let out an exaggerated sigh before continuing.

“Jin Taekyung’s still alive. Probably.”

“Probably?”

“Then let me correct that to definitely. There’s no way those old monsters still in there couldn’t protect one little brat.”

Even to the Grand Mage, it didn’t sound like an unreasonable guess.

Just fifteen minutes earlier, the defending forces had retreated at once from the walls on three sides, excluding the East Gate, and gathered in the Inner City. Among them were the Bow Saint, the Slaughter Saint, and the Fire King, Jeok Cheongang.

They’d all suffered serious injuries while withdrawing to the Inner City, but even so, their wounds shouldn’t have been severe enough to prevent them from keeping Jin Taekyung safe.

And as if to prove the Blood Lord was right, familiar faces appeared just then, beyond the thinning cloud of dust in the distance.

Including the one person who absolutely could not die—the most important one.

“……!”

The Slaughter Saint and Bow Saint were pale with exhaustion and Internal Injuries.

But the Grand Mage’s attention had already forgotten about them—and even Jeok Cheongang, who looked to be in worse shape than either of them.

There was only one person.

Jin Taekyung.

The moment she finally saw him, she let out the breath of relief she’d been holding.

There was no mistaking it.

He was covered in blood from head to toe, looking every bit the blood-soaked man he was—but Jin Taekyung was alive.

He could barely stand, using a white-glowing spear as a cane and leaning on Cheongpung for support. But that was enough for the Grand Mage.

She had the Lord of Heaven’s mysterious power: Magic.

Still, Jin Taekyung’s condition looked so grave she could sense his precarious state even from this far away.

*I have to take him to that person. As soon as possible.*

His injuries might be beyond even Magic’s ability to fully heal.

Just as the anxious Grand Mage was about to quietly recite a teleportation spell in her mind—

“What’s the rush?”

“……!”

At the Blood Lord’s low whisper, suddenly coming from behind her, the Grand Mage’s eyes widened before she could stop herself.

*How?*

If the core and root of martial arts was the accumulation of energy, Magic was a matter of attunement to energy.

That was why she was more sensitive than anyone to the fluctuations of energy.

Yet without seeing or sensing him, the Blood Lord had moved behind her and was smiling.

Like a predator with its prey already in its mouth.

“Magic really is an interesting power, the more I think about it. Being able to travel thousands and tens of thousands of ri in the blink of an eye…and bring back someone who’s half dead. Right?”

Feeling his hot breath against the back of her neck, the Grand Mage spat out her reply.

“I already told you. Cut the pointless nonsense.”

“Nonsense?”

The Blood Lord gave a short laugh and licked his lips with his red tongue.

“Sorry, but not this time. I don’t want to let prey I’ve already caught get away like this.”

Understanding what he meant, the Grand Mage gritted her teeth.

“Blood Lord, you’ve finally gone mad.”

“That’s strange. I could’ve sworn you’ve always called me a madman.”

“You dare go against that person’s will…?”

After a brief silence, the Blood Lord answered with a bright smile.

At last, he’d cast aside his mask and shackles. He was freer—and stronger—than ever.

“Why not? Just this once.”

At that very moment—

Slice!

A streak of red flashed. The Grand Mage’s hazy figure appeared three jang away.

And then—

SPLAAASH!

Her body staggered, spraying blood, then collapsed like a puppet with its strings cut.

Thud.

That was the end.

Her body lay in a pool of blood without so much as a twitch. Her eyes were frozen wide open, without a trace of life left in them.

“I wasn’t planning to kill her…but, well, can’t be helped.”

The Blood Lord muttered to himself, then looked around.

Countless eyes stared at him from every direction, in a silence that had settled over the scene. Tens of thousands of fanatics had surrounded the Inner City without leaving a single gap, and they watched this unexpected turn of events with wide eyes.

The Blood Lord spoke calmly to the fanatics, who couldn’t quite hide their agitation this time.

It was the shortest, surest method—one only Dark Heaven could use.

“By the command of the great Lord of Heaven, I have executed the apostate. From now on, I will command the entire army.”

“……!”

“……!”

“Kill them all. Every last one.”

The order finally broke the heavy silence.

Rumble!

With a roar that shook the earth and sky, tens of thousands of fanatics charged toward the Inner City.

To punish the wicked heretics who dared oppose the Lord of Heaven—the living god and sole absolute ruler.

Watching the fanatics surge forward like a giant wave, the Blood Lord laughed aloud and began to walk.

Toward taking the life of the one man he’d longed to kill for so long.

“Jin Taekyung—!”

The monster’s roar, imbued with an unprecedented aura, rang across the battlefield and swallowed it whole.

* * *

“……!”

“……!”

The air trembled. My ears were muffled.

Shouts and screams burst without pause from every direction. The bone-chilling clang of steel engulfed the battlefield.

But even through the chaos and my fading senses, I could feel it.

The warmth radiating from the people fighting countless enemies to protect me.

At the same time, I heard it.

The monster’s roar, steeped in joy and madness.

*Jin Taekyung.*

Right. That was my name.

The name I’d been given at birth.

Across two different worlds, I existed as one person—and two.

And maybe today was the last moment I’d been given.

*I have to go.*

I didn’t know where I’d found the strength.

My organs must have been twisted, and my Eight Extraordinary Meridians torn to shreds. With only a handful of internal energy, there was nothing I could do.

And yet, shrugging off Cheongpung’s support, I staggered forward as if in a trance.

Slice!

A stray blade grazed my shoulder.

Blood flowed—blood I hadn’t even known was still there—but I felt no pain as I reached out.

CRACK.

The fanatic’s gleaming eyes widened in pain.

He instinctively tried to wrench his wrist out of my grasp with all his strength, but before he could, a surge of scorching heat reached out and engulfed him.

BOOM!

To someone else, it might have felt like flames hot enough to burn them alive. To me, it felt like the warmest thing in the world.

Maybe because of who had saved me.

“El…der.”

Squeezing out every last bit of my voice, I grabbed Jeok Cheongang’s shoulder and whispered.

“A path. Please open a path for me.”
```
