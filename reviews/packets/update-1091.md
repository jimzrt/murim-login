<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1091.txt",
      "sha256": "4572564b18796069a75f9b3e1b5da68ef644aba3d0b0468d6b0fd572d6f3e9f7",
      "bytes": 11918
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "51c51282d4f33ebad3465723e134acb17b4e232ffb04f9faf3c30bd146a885d2",
      "bytes": 1698
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "bee69e076364377f31e7856d6f9b353d3362d24e22138f2ec1d79723928adc10",
      "bytes": 243843
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "5e8720c7c380d7a5068e52d9aef13774e364688c6040fc043e5070383dc0f1dc",
      "bytes": 916
    },
    {
      "path": "characters/Blood-Sword Demon Lord.md",
      "sha256": "8c36a7a432027def7e2ca9e9c44bd5925b67b8ff572ca7c003088f7fc757e404",
      "bytes": 920
    },
    {
      "path": "characters/Cang Gong.md",
      "sha256": "76287d93c925c401bd205eeb69f6758ac08f7fc763bcd90d73664d18e197a644",
      "bytes": 779
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "646fcc98bcf46cae20624fd67d69102850f541840d407e11818ffb3c3317e690",
      "bytes": 1120
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "3ccf7b44950eb81c23999ff15f036ef395f4a4a1f07062787cb9f767ff169237",
      "bytes": 1502
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "dc475b4c7412ed6642ffa370087118afbccfe6e7cb27cce779a83167146f25d4",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "8e423f15a945c1039fb76dd33f0a55f573547122597d0f4e5ccccf8f1d71f336",
      "bytes": 623
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ebe79c16d6adf08cf85ebe92be4ce390014b7513b9c2f13e94caedd0cd180dd5",
      "bytes": 287086
    }
  ],
  "estimated_tokens": 11168
}
-->

# Durable State Update — Chapter 1091

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
1 and safe_through 1091. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1091. Profile updates may replace only one
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
  "chapter": 1091,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1091,
    "continuity_sources": [1091],
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
    "The Blood Lord’s forces are marching on Xining to take Qinghai; securing Jin Taekyung is a further objective if possible.",
    "The Blood Lord’s forces have crossed Qinghai Lake using Blizzard, and the Grand Mage is with them.",
    "The Blood Lord released a Beggars’ Sect captive to carry his threat to destroy Xining; the messenger died upon arrival.",
    "Nearly thirty Beggars’ Sect disciples remained across Qinghai Lake; only the messenger returned to Xining.",
    "Jin Taekyung has chosen to remain in Xining and defend its civilians against the approaching forces.",
    "Jeok Cheongang supports Taekyung’s decision and intends to put his remaining strength to use.",
    "Most hidden magic formations retain one use; two or three used in the Shaolin attack may be spent.",
    "Mae Jonghak and the New Murim Alliance prepared an operation against Dark Heaven; Zhuge Feng has its intelligence and tasking to execute it.",
    "The Zhuge Clan left its ancestral home and fled to Mount Wudang.",
    "The city begins to shake as the enemy approaches; the cause and immediate consequences are not yet known."
  ],
  "continuity_sources": [
    1089,
    1090
  ],
  "open_questions": [
    "What is the black-robed captive in Qinghai’s identity and what does he know?",
    "Why did the Lord of Heaven spare Taekyung in Gansu, and what is his real purpose?",
    "Will the Alliance Leader and other righteous warriors reach Qinghai?",
    "What is the hidden ember Cheongheoja warned about?",
    "What caused the shaking in Xining, and how soon will the enemy arrive?"
  ],
  "safe_through": 1090,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 궁성     | **Bow Saint**                 | —              |
| 살성     | **Slaughter Saint**           | —              |
| 십왕     | **Ten Kings**       |
| 열화문    | **Fire Gate Clan**               |
| 소림     | **Shaolin**                      |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 정파     | **orthodox faction**                             |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 문주     | **Sect Leader**                              |
| 은인     | **Benefactor**                               |
| 감숙     | **Gansu**              |
| 청해     | **Qinghai**            |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 혈검마군 | **Blood-Sword Demon Lord** | Antagonist commanding the army advancing on the Great Snow Mountain. |
| 창공 | **Cang Gong** | The bedridden East Depot leader for whom Ma Sanbao acts. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |
| 황하 | **Yellow River** | River along which civilization began. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 검마 | **Sword Demon** | A Demonic Cult swordsman whose final technique is compared with One Annihilation. |
| 신인 | **divine man** | Descriptive term for a human who became something beyond humanity. |
| 미친놈 | **Madman** | Insult Great Sir adopts as a name; also appears in the System display. |
| 서녕 | **Xining** | Capital of Qinghai. |

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
| 적천강 | 창공 | hostile opponents | you; you bastard | blunt and threatening | Jeok Cheongang uses 네놈, 이 불알 없는 놈, and 호로새끼 while taunting Cang Gong. |
| 창공 | 적천강 | hostile opponents | Fire King Jeok Cheongang | taunting and sardonic | Cang Gong names Jeok by his title, then comments on how alike master and disciple are. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 살성 | 청풍 | senior martial figure to younger companion | you | blunt and familiar | The Slaughter Saint scolds Cheongpung for disappearing without a word. |
| 청풍 | 살성 | younger companion to senior martial figure | old man | polite and familiar | Cheongpung apologizes and explains why he wandered off. |
| 혈검마군 | 적천강 | former opposing martial masters | Senior Jeok | respectful and familiar | Addresses Jeok as 선배 while teasing him. |
| 적천강 | 혈검마군 | former opposing martial masters | you; you bastard | blunt and hostile | Uses 너 and 네놈 while confronting him. |
| 혈검마군 | 진태경 | enemy addressing a younger martial artist | you | familiar and measured | Uses 자네 while praising and assessing Taekyung. |
| 진태경 | 혈검마군 | young martial artist confronting an enemy | you | casual and challenging | Questions when the Blood-Sword Demon Lord and the Lord of Heaven appeared. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1090
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who directs its sorcerers’ seed experiments and prepares their deployment for the Lord of Heaven’s great cause.
- **Personality:** Confident, cruel, and controlling; strategically manipulates allies and adversaries, and conceals failures from the Lord of Heaven when he fears being discarded.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven and seeks to advance the Lord’s great cause; he regards the deceased Western Heaven Demon Lord and Southern Heaven Demon Empress as powerful allies whose deaths cost Dark Heaven, and considers Jin Taekyung and Cheongpung formidable adversaries.

### Blood-Sword Demon Lord.md

# Blood-Sword Demon Lord (혈검마군)

- **Safe through:** Chapter 1066
- **Aliases:** None
- **Role:** The Blood-Sword Demon Lord is a formidable martial master who commands the force advancing on the Great Snow Mountain and now serves the Lord of Heaven.
- **Personality:** Devoted to his master and proud of his abilities, he is deeply wounded by perceived distrust and resolves to prove his worth.
- **Voice:** Casually familiar and self-amused, addressing Jeok Cheongang respectfully as Senior while trading blunt insults; his easy laughter can turn to a low, cold intensity.
- **Relationships:** He serves the Lord of Heaven with deep devotion, but the Grand Mage says the Lord ordered his disposal; he has been ordered not to kill Jin Taekyung, admires Jeok Cheongang, and once shared the Demonic Cult with the fiends who became Black Ghosts.

### Cang Gong.md

# Cang Gong (창공)

- **Safe through:** Chapter 1067
- **Aliases:** None
- **Role:** Cang Gong is the Eastern Heaven Demon Lord’s assumed identity, through which he became the East Depot’s Brush-Holding Eunuch and a power second only to the Emperor.
- **Personality:** Calculating and self-assured, he is driven by vengeance and believes the rulers and the world betrayed him first.
- **Voice:** Dry and sardonic, he delivers taunts and judgments in measured statements.
- **Relationships:** He was raised by a master and fellow disciples in the Maoshan Sect, whose members died resisting the forced relocation of the capital; Ma Sanbao is his disciple, and he regards Jin Taekyung as a potential recruit.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 1082
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, Sword Saint Mae Jonghak’s grandson and Disciple, a Supreme Peak master known as the Huashan Divine Dragon, creator of Mimi Step, and master of the Azure Dragon Pavilion; he has also learned concealment from the Slaughter Saint.
- **Personality:** Affable, dreamy, and childlike, with innocent curiosity, a deep love of martial arts, competitive pride, and compassion that leaves him unsettled by killing; he admires Taekyung’s resilience in the way he lives.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions; Taekyung is his true martial rival and the person whose way of life he admires, and the Slaughter Saint has become his mentor in concealment.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1090
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1089
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1089
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
1091화




청해성의 성도인 서녕은 까마득한 고원(高原)에 세워진 도시다.

동쪽과 서쪽으로는 중원으로까지 이어진 황하(黃河)의 지류가 흐르고, 주위는 온통 크고 작은 산으로 둘러싸여 있기에 보는 것만으로도 뭇사람들의 탄성을 자아낼 만큼 아름다운 경관을 지녔다.

그러나 지금 이 순간만큼은, 서녕의 높은 성벽 위를 메운 수많은 이들 중 그 누구도 눈앞의 풍경이 아름답다고 생각하지 못했다.

못한 것이 아니라, 그럴 수 없었다.

여느 때처럼 고고하게 우뚝 서 있어야 할 산이 움직이는 광경은, 단지 보는 것만으로도 등골을 얼어붙게 만들었으니까.

드득. 드드득.

지금껏 느껴본 적 없는 거대한 울림.

그에 따라 도시 전체가, 사람들의 몸과 마음이 뒤흔들린다.

그리고 숨길 수 없는 경악으로 물든 그 수많은 시선 끝에는, 저 멀리에서 가까워져 오는 칠흑색의 산이 있었다.

아니, 마치 하나의 산처럼 움직이는 적들의 군세가.

암천(暗天).

마침내 그들이 왔다.

푸른 하늘도, 청록의 대지도 검게 물들일 사막 너머의 악귀들이.



* * *



문득 세상이 어두워졌다고 느낀 것은 결코 나만의 착각이 아니었을 것이다.

어두웠다. 온 사방이.

먹구름이 태양을 가리고, 햇빛을 먹어치운 냉기가 그 빈자리를 채운다.

그리고.

그 모든 것의 중심에, 놈들이 있었다.

괴물과 인간이 뒤섞인 암천의 거대한 군세가.

“……은인.”

어느샌가 성벽 위로 올라온 청풍의 목소리는 평소와 달리 깊게 가라앉아 있었고, 미약한 떨림마저 묻어나왔지만 나는 대답하지 않았다.

정확히는, 대답할 수 없었다.

나 역시 성벽 너머를 가득 메우며 진군해 오는 적들의 모습에 압도당해 버린 후였으니까.

누구에게도 결코 그 사실을 들켜서는 안 되니까.

그러나 세상 모두의 이목을 속일 수 있을지라도, 한 사람만큼은 예외였다.

- 두려우냐?

귓가로 흘러들어온 적천강의 전음(傳音)에, 나는 조용히 입술을 깨물었다.

그래, 맞다.

지금 이 순간, 나는 몸서리쳐질 만큼 두렵다.

지금껏 단순히 짐작만 해 왔던 놈들의 전력이 생각 이상이라는 것이, 그 진정한 실체를 마주한 순간 본능적으로 패배라는 단어를 떠올렸다는 사실이 두려웠다.

꾸욱.

나도 모르는 사이에 힘이 들어간 주먹에서 뜨거운 감촉이 느껴진다. 방울방울 맺힌 핏물이 손가락 사이로 흘러나오지 않도록, 나는 더욱 힘주어 주먹을 말아쥐며 대답했다.

- 예. 두렵습니다.

- 무엇이 그리 두렵더냐.

- 이미 그토록 다짐하고 각오했음에도 위축되어버린 저 자신이, 그리고 그로 인한 결과가 가장 두렵습니다.

내가 죽는 것 따위는 조금도 두렵지 않다고 말하지는 않겠다.

그건 지금껏 어떻게든 살아남기 위해 발버둥 쳐 왔던 나 스스로에 대한 부정이자, 가소로운 위선이니까.

하지만 그보다 훨씬 두려운 것이 있다면, 지금 내가 서 있는 이 성벽 뒤에 머무르고 있는 수십 만의 목숨이 사라지는 것이었다.

다른 누구도 아닌, 내 잘못된 선택으로 인해.

그리고 적천강은 그런 내 마음을 꿰뚫어보고 있었다.

- 그래, 그것이 네 녀석과 노부의 차이겠지.

그게 무슨 뜻이냐고 묻기도 전에, 뒤이은 전음이 귓가로 전해졌다.

- 일평생 대의(大義)를 좇은 적은 단 한 번도 없었다. 그저 발걸음이 향하는 대로, 바람이 부는 대로 나아갔을 뿐. 따라서 일면식도 없는 타인의 죽음은그리 괴롭지도 않았다.

세인들은 적천강을 십왕(十王)의 수좌로, 정파를 대표하는 거인 중 하나로 인식하고 있지만 실상은 다르다.

그는 자유인이었다.

열화문의 역대 문주들이 그러했듯, 정사마(正邪魔) 어디에도 몸담지 않고 오직 자신만의 길을 걸어온.

- 아마도 그 때문이었을 것이다. 어느샌가 꼬리표처럼 붙어버린 대협이라는 호칭이 맞지 않는 옷처럼 불편하게 느껴진 것은.

- 하지만 그렇게 불릴 자격이 충분하십니다.

- 아니, 틀렸다.

단호하게 대답한 적천강이 심유한 눈빛으로 나를 응시했다.

- 타인의 고통을 두려워하고, 눈물 흘릴 줄 아는 자만이 대협이라 불릴 자격을 얻는다. 바로 네 녀석처럼.

- ……!

- 다만 이 한 가지만큼은 기억해 두거라. 후에 눈물을 흘리지 않기 위해서는, 당장 눈앞의 두려움부터 이겨 내야 한다는 것을.

다음 순간, 적천강이 나직이 덧붙였다.

- 그때서야 비로소 영웅(英雄)이 된다.

영웅. 영웅이라.

언제나 멀게 느껴지는 그 두 글자를 마음속으로 뇌까리며, 나는 쓴웃음을 지었다.

- 그런 것 따위는 원한 적도 없습니다.

- 상관없다. 영웅은 단지 원한다고 이루어지는 것이 아니니까. 세상이 네 녀석을 그리 부를 때 자격을 얻는 것이다.

- 노야께서 대협이라고 불리시는 것처럼요?

 -뭐라?

- 방금 말씀하셨잖습니까. 구태여 대의를 좇지 않아도, 그저 발걸음이 향하는 대로, 바람이 부는 대로 나아갔음에도 어느샌가 대협이라고 불리게 되었다고.

- ……!

크게 뜨인 눈으로 나를 바라보던 적천강이 입술을 핥았다.

- 이거 한 방 먹었군.

- 비긴 거로 하시죠.

- 혓바닥 놀리는 솜씨는 어디 안 가는구나. 이제야 노부가 알던 그 천둥벌거숭이로 돌아온 기분이야.

피식 실소를 흘린 적천강이 턱짓으로 성벽 너머를 가리켰다.

- 어떠냐, 아직도 두려우냐?

- 예.

망설임 없이 대답한 나는 담담하게 덧붙였다.

- 하지만 저는 그 두려움을 애써 외면하지 않겠습니다.

사람이라면 누구나 마음 한구석에 두려움을 간직하고 있다.

그러나 그 사실을 인정하고 똑바로 직시하는 자만이, 두려움을 딛고 일어설 힘을 얻을 수 있다.

바로 지금처럼.

구궁, 구구구궁!

어느덧 시시각각 더해 가는 울림에 지진이라도 난 것처럼 요동치는 지면.

나는 높고 단단한 성벽을 타고 기어오르는 그 강렬한 진동을 온몸으로 느꼈다.

동시에 보았다.

감히 눈으로는 헤아릴 수 없을 정도로 무수한 적의 선두에서, 정확히 이곳을 향해 히죽 웃고 있는 한 사람을.

‘혈주(血主).’

마지막으로 기억하는 놈의 모습과는 상당한 괴리가 있었지만, 삐뚜름하게 비틀려 올라간 입매를 본 순간 본능적으로 깨달을 수 있었다.

마치 손을 대면 묻어나올 것만 같은 저 진득한 살의(殺意)와 광기는, 감숙성에서 쓰러트린 혈검마군조차 따라올 수 없을 정도였으니까.

그리고 서로를 알아본 그 찰나의 순간, 놈의 입술이 달싹였다.

“올려다보고 있자니 목이 아픈데, 잠시 내려와서 인사나 나누지?”

먹먹한 굉음과 먼지구름을 뚫고 울려 퍼진 그 한 마디에, 그렇지 않아도 혈주를 뚫어질 듯이 응시하던 적천강의 눈동자가 불그스름하게 달아올랐다.

“그렇지 않아도 몸이 근질거렸는데, 알아서 긁어 주는군.”

즉각 심상치 않은 낌새를 눈치챈 궁성이 한발 앞서 만류했다.

“격장지계(激將之計)예요. 뻔하디뻔한.”

거들어 보라는 궁성의 눈짓에, 언제부턴가 홀연히 나타나 성벽 위에 자리 잡고 있던 살성이 담담한 얼굴로 고개를 끄덕였다.

“미친 짓인 건 맞지.”

적천강이 미간을 찌푸린 그때, 살성이 덧붙였다.

“그것과는 별개로, 이중 제정신인 사람은 아무도 없고.”

곧바로 주름 잡힌 미간을 펴는 적천강을 향해, 내가 엄숙하게 결론을 내렸다.

“당장 하죠.”

“그래. 설마 죽기야 하겠나.”

파팟!

누가 말릴 틈새조차 없었다.

남자들의 유언 1순위를 읊으며, 우리는 동시에 성벽을 박차고 솟구쳤다.

지금껏 함께하며 들어 본 것 중, 가장 날카롭고 커다란 궁성의 외침을 뒤로한 채로.

“가지 말라니까!”

음.

미안합니다.



* * *



단숨에 아득한 창공을 가로질러 떨어져 내리는 세 개의 인영을 본 순간, 혈주는 자신도 모르게 중얼거렸다.

“미친놈들이군. 이걸 진짜 온다고?”

그냥 가볍게 툭 던진 말이었는데, 몇 마디 주고받나 싶더니 이렇게 망설임 없이 들이닥칠 줄은 몰랐다.

“무슨 반쯤 미친 투견(鬪犬)도 아니고…….”

적잖이 당황한 혈주가 말꼬리를 흐리던 그때, 마치 섬광처럼 십여 장 앞까지 다가온 세 사람이 동시에 입을 열었다.

“니가 내려오라며, 씹새야.”

“개보다 못한 새끼. 염병할 호로새끼. 태워 죽여도 시원치 않을 천하의…….”

“네가 말로만 듣던 혈주로군. 초면에 이런 부탁하긴 뭐하지만, 얌전히 목을 내놓고 물러날 생각은 없나?”

이상하리만치 입에 착 감기는 욕설을 구사하는 진태경을 시작으로, 자신이 아는 모든 쌍욕을 퍼붓는 적천강에 이어 처음으로 대면하는 살성까지.

혈주는 잠깐의 당혹스러움에 가려져 있던 분노가 솟구치는 것을 느꼈다.

“다 지껄였나?”

착 가라앉은 혈주의 음성에, 잠시 멈칫한 진태경이 살성을 힐끗 바라보았다.

“혹시 할 말 남으셨어요?”

“아마도. 어차피 초면이라 할 말도 딱히 없다.”

초면인 것치고는 이미 상당한 무례를 범했던 살성이었지만, 진태경은 대수롭지 않게 고개를 끄덕인 뒤 혈주에게 대답했다.

“이쪽 분은 끝나셨대.”

으득.

그 태연한 태도에 이를 악문 혈주는 입을 열었다.

아니, 정확히는 그러려고 했다.

바로 그 순간 아직 끝나지 않은 육두문자의 파도가 그를 덮치기 전까지는.

“네놈의 뼈마디 하나 남기지 않고 자근자근 갈아 주마. 살점은 남만야수궁에 먹이로 쓰라고 던져 주고, 유골은 소림사 뒷간에 뿌려서…….”

“아, 이쪽 분께서는 아직 안 끝나셨네. 조금만 기다려 봐. 솔직히 너도 은근히 뒷 내용이 궁금하지 않냐?”

그 순간, 이성의 끈이 끊어져 버린 혈주의 눈앞이 새하얗게 물들었다.

“갈(喝)-!”

콰아아아!

막강한 기파(氣波)가 사방을 휩쓴다. 

그 외마디 고함에 담긴 거대한 공력에 끝없이 진군할 것만 같던 암천의 군세도, 일백여 장이나 떨어져 있는 성벽 위의 사람들도 숨을 삼켰다.

그러나 정작, 가장 가까운 곳에서 그 기파를 온전히 느낀 세 사람만큼은 예외였다.

솨악!

자욱하게 솟아오른 흙먼지를 가르는 한 줄기의 예리한 바람.

그 중심에서, 어느덧 투명하리만치 맑은 창날을 내리그은 진태경이 히죽 웃었다.

그들이 성벽을 내려오기 전, 혈주가 그러했던 것처럼.

“왜 흥분하고 그러냐. 간만에 보니까 반가워서 그러는 건데.”

폭발은 파괴를 의미하지만, 이는 곧 소멸과도 연결된다.

분노를 끌어모아 단숨에 폭발시킨 혈주는 되려 차갑게 가라앉은 눈빛으로 진태경을 응시했다.

“그때와 똑같군. 그 빌어먹을 혓바닥은.”

그 순간, 진태경의 입가에 맺혀 있던 미소가 사라졌다.

“그때와는 다를 거야. 그 외의 모든 것이.”
```

## Final English reading copy

```markdown
# Chapter 1091

Xining, the capital of Qinghai, was a city built on a vast plateau.

Tributaries of the Yellow River, which flowed east and west all the way to the Central Plains, ran through the region. Mountains large and small surrounded it on every side, giving it scenery beautiful enough to draw gasps from anyone who saw it.

But at that moment, not one of the countless people crowding Xining’s high walls could think the view before them was beautiful.

It wasn’t merely that they failed to see its beauty. They couldn’t.

The sight of a mountain that should have stood tall and still, as always, now in motion was enough to freeze the spine.

Rrrk. Rrrrk.

A tremendous rumble unlike anything they had ever felt.

The city shook with it. So did the people, body and soul.

And at the end of all those gazes, filled with undisguised horror, was a pitch-black mountain drawing closer from the distance.

No—a force of enemies moving as one, like a mountain.

Dark Heaven.

At last, they had come.

Fiends from beyond the desert, come to blacken the blue sky and the green earth alike.

* * *

The world had suddenly grown dark. I knew I wasn’t the only one who felt it.

Dark. In every direction.

Dark clouds hid the sun, and a chill that seemed to swallow the sunlight filled the space it left behind.

And—

At the center of it all, they stood.

Dark Heaven’s vast army, where monsters and humans mingled.

“……Benefactor.”

Cheongpung’s voice came from somewhere behind me on the wall. It was lower than usual, with the faintest tremor in it, but I didn’t answer.

More precisely, I couldn’t.

I, too, had been overwhelmed by the sight of the enemy filling the horizon beyond the wall as they advanced.

I couldn’t let anyone find out. Not ever.

I might have been able to fool the whole world, but there was one person I couldn’t fool.

*—Are you afraid?*

At Jeok Cheongang’s Sound Transmission in my ear, I quietly bit my lip.

*Yes. I am.*

At this moment, I was terrified enough to shudder.

I was terrified that their strength was far greater than I’d merely guessed up until now. That, the moment I saw what they truly were, my instincts had made me think of the word defeat.

Squeeze.

I felt a warm sensation in my fist, clenched so tightly I hadn’t even realized it. I tightened it further, keeping the beads of blood from slipping between my fingers, and answered.

*—Yes. I’m afraid.*

*—What are you so afraid of?*

*—I’m most afraid of myself—of how I’ve shrunk back, even after making up my mind and preparing myself for this. And of what will happen because of it.*

I wouldn’t say I wasn’t afraid of dying.

That would be denying the person I’d been all this time, fighting tooth and nail just to survive. It would be a laughable lie.

But there was something I feared far more: the hundreds of thousands of lives behind the wall I stood on, vanishing.

Because of my own bad decision. No one else’s.

Jeok Cheongang saw right through me.

*—Yes. That’s the difference between you and this old man.*

Before I could ask what he meant, his next Sound Transmission reached my ear.

*—I’ve never once pursued some grand cause in my life. I simply went where my feet took me, where the wind blew. So the deaths of strangers I’d never met didn’t trouble me much.*

People saw Jeok Cheongang as the foremost of the Ten Kings, one of the towering figures representing the orthodox faction. But in truth, he was different.

He was a free man.

Like the Sect Leaders of the Fire Gate Clan before him, he belonged to none of the orthodox, unorthodox, or demonic factions. He had walked only his own path.

*—Maybe that’s why the title of Great Hero, which stuck to me like a label before I knew it, always felt like an ill-fitting suit.*

*—But you deserve to be called one.*

*—No. That’s wrong.*

Jeok Cheongang answered firmly and looked at me with deep, thoughtful eyes.

*—Only those who fear the pain of others, and know how to shed tears, deserve to be called Great Heroes. Just like you.*

*—……!*

*—But remember this one thing. If you don’t want to shed tears later, you have to overcome the fear right in front of you first.*

Then Jeok Cheongang added in a low voice,

*—Only then do you become a hero.*

A hero. A hero, huh.

I mouthed those two words in my mind. They had always felt so far away. Then I gave a bitter smile.

*—I never wanted any of that.*

*—It doesn’t matter. You don’t become a hero just because you want to. You earn the title when the world calls you one.*

*—Like how they call you a Great Hero, Old Master?*

*—What?*

*—You just said it yourself. You didn’t go out of your way to pursue some grand cause. You just went where your feet took you, where the wind blew—and before you knew it, people were calling you a Great Hero.*

*—……!*

Jeok Cheongang stared at me, eyes wide. Then he licked his lips.

*—You got me with that one.*

*—Let’s call it even.*

*—You haven’t lost your knack for running that mouth. Now you’re finally starting to feel like the little hellion I knew.*

Jeok Cheongang let out a quiet laugh and gestured with his chin toward the other side of the wall.

*—Well? Still afraid?*

*—Yes.*

I answered without hesitation, then added calmly,

*—But I won’t try to look away from that fear.*

Everyone carries some fear in a corner of their heart.

But only those who admit it and face it head-on can find the strength to stand up to it.

Just as I was now.

Rumble. Rrrumble!

The rumbling grew stronger by the moment, and the ground shook as if an earthquake had struck.

I felt the powerful vibrations climb through my whole body as they traveled up the tall, sturdy wall.

And at the same time, I saw him.

At the head of the enemy forces, so numerous I couldn’t begin to count them, one man was grinning as he looked straight at us.

*The Blood Lord.*

He looked quite different from the last time I’d seen him, but the moment I saw that crooked smile, I knew by instinct.

That thick, viscous killing intent and madness, so palpable it seemed like you’d get it on your hand if you touched him, outstripped even the Blood-Sword Demon Lord I’d taken down in Gansu.

And in the instant we recognized each other, his lips moved.

“Looking up at you is a pain in the neck. Why don’t you come down for a bit and say hello?”

His words rang out through the deafening rumble and clouds of dust. Jeok Cheongang, who had already been staring hard at the Blood Lord, had a reddish gleam in his eyes.

“My body was getting restless anyway. He’s doing me the favor of scratching the itch.”

Bow Saint immediately sensed the danger and tried to stop him.

“It’s goading you. Obvious as can be.”

At her expectant glance, the Slaughter Saint, who had appeared out of nowhere at some point and taken up a place on the wall, calmly nodded.

“Yeah, it’s crazy.”

Then, as Jeok Cheongang furrowed his brow, the Slaughter Saint added,

“But it’s not like anyone here is thinking straight.”

My expression solemn, I drew the obvious conclusion.

“Let’s do it now.”

“Right. It’s not like we’ll die or anything.”

Whoosh!

There wasn’t even time for anyone to stop us.

Reciting the number-one last words of men everywhere, the three of us sprang off the wall at the same time.

Behind us came the sharpest, loudest shout I’d ever heard from Bow Saint.

“I said don’t go!”

Uh.

Sorry.

* * *

The Blood Lord watched three figures plummet across the distant sky in an instant. Without thinking, he muttered,

“They’re crazy. They’re really coming?”

He’d only tossed out a casual remark. They’d traded a few words, and now the three of them were charging straight at him without the slightest hesitation.

“Like half-mad fighting dogs or something…”

The Blood Lord trailed off, considerably taken aback. Then the three men—now over thirty yards away, moving like flashes of light—spoke at once.

“You told us to come down, you son of a bitch.”

“You worthless bastard. You goddamn bastard. You piece of shit. You’re the kind of bastard I’d burn alive and still not be satisfied—”

“So you’re the Blood Lord I’ve heard about. I know this is a strange request for a first meeting, but would you mind calmly offering your neck and stepping aside?”

First came Jin Taekyung, whose curses had an oddly satisfying ring to them. Then Jeok Cheongang, hurling every obscenity he knew. And finally the Slaughter Saint, whom the Blood Lord was meeting for the first time.

For a moment, surprise had covered the Blood Lord’s anger. Now he felt it surge back to the surface.

“Are you done talking?”

At the Blood Lord’s low voice, Jin Taekyung hesitated briefly and glanced at the Slaughter Saint.

“Do you have anything else to say?”

“Probably not. We’ve only just met, so I don’t have much to say.”

The Slaughter Saint had already been remarkably rude for someone who’d just met him. Jin Taekyung nodded as if it were nothing, then answered the Blood Lord.

“He says he’s done.”

Crack.

The Blood Lord gritted his teeth and opened his mouth at that nonchalant response.

Or tried to.

Before he could, another wave of obscenities swept over him.

“I’ll grind every bone in your body to dust. I’ll toss your flesh to the Nanman Beast Palace to feed their beasts, and scatter your bones in the Shaolin Temple latrines, and—”

“Ah, this one isn’t done yet. Wait a bit. Honestly, aren’t you kind of curious what comes next?”

At that moment, the Blood Lord’s last thread of reason snapped. His vision went white.

“Hah!”

KWA-A-A!

A powerful wave of energy swept out in every direction.

The immense internal energy packed into that single shout made Dark Heaven’s army, which had seemed as though it would march on without end, and the people on the wall over three hundred yards away, all hold their breath.

But the three men closest to him, who felt the full force of that wave, were the exception.

Whoosh!

A single sharp gust cut through the dust that had billowed into the air.

At its center, Jin Taekyung had already brought his clear, almost transparent spearhead slashing down. He grinned.

Just as the Blood Lord had before they came down from the wall.

“Why are you getting so worked up? I’m just glad to see you after all this time.”

An explosion meant destruction, but it was also tied to erasure.

The Blood Lord had drawn his anger together and unleashed it all at once. Now he stared at Jin Taekyung with eyes gone cold.

“You’re just the same as before. That damned mouth of yours.”

At that moment, the smile on Jin Taekyung’s lips disappeared.

“This time will be different. Everything else will be.”
```
