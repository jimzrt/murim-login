<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1050.txt",
      "sha256": "f0df68500283f78e110ceb402c7bc0910dddf51a478235e56fe235e62d760938",
      "bytes": 12740
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "f2cd30e60b9a098b3ecb15ea1f436489a7ab70d62239eff1721e826a48aebbf4",
      "bytes": 1294
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "91edff1ea0e7f2d1bdf20f77998a86f250b89f1bc3f043cd106289bea1e118b4",
      "bytes": 240895
    },
    {
      "path": "characters/Blood-Sword Demon Lord.md",
      "sha256": "2f53377eb5501f0f02c36baf2463bd3fbd038ca03abd9356f3fedd39524174bc",
      "bytes": 920
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "93bb0ca1758891dbaaec60f79f4be2238a2eca87866da1d8ad225d075cb88801",
      "bytes": 760
    },
    {
      "path": "characters/Grand Mage.md",
      "sha256": "022d0db3df5a9814b97011a12805996957d56e651424305e13c7ad38eb517be9",
      "bytes": 569
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "dedff12ce258a7c1f6f3aa0a0d255d3f5121d74c61bf7835125279f868837105",
      "bytes": 1502
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "c41a1fb86e663e1da4d122d60aecbc8e8667afce615c465b52344c1e8b0355f5",
      "bytes": 1823
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "ff90393590eabbef07abf603fb22e6c6c828e381fdd568811b6383569eea3d0f",
      "bytes": 623
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "856cd612d215439798310c900a537086710189a2bdd550aeffc50210820fc16b",
      "bytes": 779
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "e476e49cdcddf6de4980fb9437ae78bed54ffc02a595fe7c61e28608999f8e34",
      "bytes": 281989
    }
  ],
  "estimated_tokens": 11051
}
-->

# Durable State Update — Chapter 1050

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
1 and safe_through 1050. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1050. Profile updates may replace only one
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
  "chapter": 1050,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1050,
    "continuity_sources": [1050],
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
    "The battle at the Great Snow Mountain continues.",
    "The Blood-Sword Demon Lord is gravely injured; the Grand Mage says the Lord of Heaven ordered his disposal after his role was fulfilled.",
    "Jin Taekyung is conscious but weakened and bound by the Grand Mage’s plant magic; she urges him to kill the Blood-Sword Demon Lord and grow stronger.",
    "Jeok Cheongang and the Bow Saint have reached the hill and seen Jin bound.",
    "Sima Gong remains gravely wounded and missing an arm; his fate is unresolved."
  ],
  "continuity_sources": [
    1048,
    1049
  ],
  "open_questions": [
    "What are the identity and purpose of the Lord of Heaven?",
    "Why did the Lord of Heaven order the Blood-Sword Demon Lord’s disposal?",
    "Did Dark Heaven cause the Great Faction War?",
    "Who are the white-robed mages, and what is their purpose?",
    "How were the former Demonic Cult fiends made into Black Ghosts?"
  ],
  "safe_through": 1049,
  "temporary_decisions": [
    "Render 대마도사 as Grand Mage.",
    "Use Fire Ball, Stone Wall, and Magic Arrow for the named spells.",
    "Render 헬 파이어 as Hell Fire; use hellfire for descriptive 겁화.",
    "Render 쇄월검진 as Moon-Shattering Sword Formation."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 무신     | **Martial God**               | —              |
| 궁성     | **Bow Saint**                 | —              |
| 삼성     | **Three Saints**    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 암천     | **Dark Heaven**                  |
| 무인     | **martial artist**                               | Default term                                          |
| 마교     | **Demonic Cult**                                 |                                                       |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 태원     | **Taiyuan**            |
| 정마대전   | **Great Faction War**         |
| 도사      | **Daoist**                                                      |
| 혈검마군 | **Blood-Sword Demon Lord** | Antagonist commanding the army advancing on the Great Snow Mountain. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 구주 | **Nine Provinces** | Traditional geographic expression used in a threat. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |
| 여의주 | **dragon pearl** | Legendary treasure requested by Jang Taebo. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 잠룡 | **Hidden Dragon** | Epithet or metaphor for Jin Taekyung. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 심맥 | **heart meridian** | Meridian severed by an infiltrator to commit suicide. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 사냥개 | **hunting dog** | Jin's demeaning metaphor for Ares personnel who obey Go Jun. |
| 검마 | **Sword Demon** | A Demonic Cult swordsman whose final technique is compared with One Annihilation. |
| 신인 | **divine man** | Descriptive term for a human who became something beyond humanity. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 역천 | **defying heaven** | Supernatural power that regenerates the masked man's body. |
| 대술사 | **Grand Mage** | Title of the veiled woman leading the white-robed mages. |

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
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 혈검마군 | 적천강 | former opposing martial masters | Senior Jeok | respectful and familiar | Addresses Jeok as 선배 while teasing him. |
| 적천강 | 혈검마군 | former opposing martial masters | you; you bastard | blunt and hostile | Uses 너 and 네놈 while confronting him. |
| 혈검마군 | 진태경 | enemy addressing a younger martial artist | you | familiar and measured | Uses 자네 while praising and assessing Taekyung. |
| 진태경 | 혈검마군 | young martial artist confronting an enemy | you | casual and challenging | Questions when the Blood-Sword Demon Lord and the Lord of Heaven appeared. |
| 혈검마군 | 천주 | servant_to_master | Lord of Heaven | deferential | In his inner monologue, he addresses his absent master as 당신 and refers to himself as 속하. |
| 대마도사 | 진태경 | adversary_to_adversary | you | polite, teasing | She uses polite phrasing while taunting him and warning him not to overexert himself. |
| 진태경 | 대마도사 | adversary_to_adversary | you bitch | insulting-casual | He curses at her while refusing to give up. |
| 대마도사 | 궁성 | Adversaries | Bow Saint | Not established | She identifies him by title when recognizing the archer who struck the Hell Fire sphere. |
| 대술사 | 혈검마군 | subordinate_to_commander | Demon Lord | respectful and formal | Addresses him as 마군 while acknowledging his injuries. |
| 혈검마군 | 대술사 | commander_to_subordinate | Grand Mage | blunt and commanding | Orders her to heal him immediately. |

## Listed compact profiles

### Blood-Sword Demon Lord.md

# Blood-Sword Demon Lord (혈검마군)

- **Safe through:** Chapter 1049
- **Aliases:** None
- **Role:** The Blood-Sword Demon Lord is a formidable martial master who commands the force advancing on the Great Snow Mountain and now serves the Lord of Heaven.
- **Personality:** Devoted to his master and proud of his abilities, he is deeply wounded by perceived distrust and resolves to prove his worth.
- **Voice:** Casually familiar and self-amused, addressing Jeok Cheongang respectfully as Senior while trading blunt insults; his easy laughter can turn to a low, cold intensity.
- **Relationships:** He serves the Lord of Heaven with deep devotion, but the Grand Mage says the Lord ordered his disposal; he has been ordered not to kill Jin Taekyung, admires Jeok Cheongang, and once shared the Demonic Cult with the fiends who became Black Ghosts.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1049
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Grand Mage.md

# Grand Mage (대마도사)

- **Safe through:** Chapter 1049
- **Aliases:** None
- **Role:** The Grand Mage leads the white-robed mages and is a formidable mage who has reached the edge of truth.
- **Personality:** She remains composed and curious even as her own forces die, showing little concern for their suffering.
- **Voice:** Calm and politely phrased, with teasing remarks and a hint of excitement.
- **Relationships:** She commands the white-robed mages and is an adversary of Jin Taekyung.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1049
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1049
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him and feels no fear when Taekyung is with him; Taekyung trusts Sama Pyo and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1049
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 1034
- **Aliases:** None
- **Role:** An unidentified legendary martial artist regarded as a pinnacle above the Ten Kings; more than fifty years ago, he defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, Mae Jonghak received several teachings from him, and he left the Bow Saint a letter describing a chosen one; the Bow Saint says he chose her, while his identity, whereabouts, and possible connection to Cheon Taemin remain unknown.

## Korean source

```text
＃1050화



예상을 아득히 벗어난 진실과 마주했을 때, 사람들의 반응은 크게 두 가지로 나뉜다.

진실을 이해하지 못한 채 혼란에 빠지거나, 혹은 그 진실에 담긴 엄청난 충격과 무게감을 짐작하고 얼어붙거나.

혈검마군은 전자(前者)였다.

“그게 무슨……?”

그는 고통조차 잊은 채 멍하니 뇌까렸다.

신처럼 떠받들던 주인에게 버림받았다는 절망적인 현실에 직면한 대마두의 귓가에는, 조금 전 들었던 목소리가 계속해서 울려 퍼지고 있었다.



‘당신은 여기에서 쓰러져서는 안 되니까. 지금보다도 더 강해져야 하니까.’



진태경을 향한 대술사의 그 한마디는, 혈검마군이 몇 번을 되새겨 생각해 보아도 도무지 이해할 수 없는 종류의 것이었다.

토사구팽?

배신감이 든다 해도 어쩔 수 없었다.

강자가 피를 원한다면, 약자는 그 피를 흘려야 하니까.

일평생 마도(魔道)를 걸어온 그 역시도 잘 알고 있는 세상의 법칙이니까.

천주와 암천을 위해 헌신한 자신이 제거당하는 이유는 아직도 모르겠지만, 여기까지 온 이상 받아들이는 수밖에 없었다.

하지만 그것과는 별개로.

왜, 어째서, 무엇 때문에.

그가 따르던 주인은, 이토록 큰 손해를 감수하면서까지 충성스러운 사냥개의 처형을 적에게 맡기려 하는가.

그것도 천하의 그 누구보다 암천의 행보를 번번이 가로막았던, 고작 이립도 되지 않은 핏덩이의 손에.

그리고…….

‘나를 죽이고, 더 강해지라고?’

대관절 자신의 죽음이, 이 일방적인 처형식이 진태경이 강해지는 것과 무슨 연관이 있다는 것인지.

혈검마군으로서는 대술사의 마지막 말에 담긴 의미를 조금도 짐작할 수 없었고, 그것이 당연했다.

그가 떠올릴 수 있는 상상의 범주에는 한계가 있었으니까.

하지만 적어도 이 자리에 함께 있는 또 다른 누군가는, 혈검마군이 알 수 없는 진실을 알고 있었다.

“……너.”

새하얗게 질린 입술과 딱딱하게 굳어 버린 안면의 근육.

숨을 쉬는 것조차 잊은 채, 넋 나간 눈동자로 눈앞의 여인을 응시하던 청년은 간신히 목소리를 쥐어짜 냈다.

“지금 도대체…… 무슨 말을 하는 거야.”

이건 묻는 것이 아니다. 부정하는 것이다.

이루어질 수 없는 현실을 믿고 싶지 않기에, 애써 부정하고자 하는 것이다.

그리고 그런 청년을, 진태경을 바라보는 대술사의 눈매가 반달처럼 휘었다.

“이미 알고 있잖아요, 당신도.”

“……!”

“이 자리에서 알려 드려야 하나요? 내가 말하고자 하는 것이 무엇인지.”

불길한 짐작을 확신으로 바꿔 주는 한 마디가 귓가에 닿은 순간, 진태경은 새하얗게 물들어 가는 머릿속을 느꼈다.

텅 비어 버린 뇌리에 유일하게 남아 있는 세 글자도 함께.

‘레벨 업.’



* * *



전신의 피가 차갑게 식어 버린다면 이런 느낌일까.

그 순간만큼은 마치 온 세상이 멈춘 듯했다.

아니, 어쩌면 정말로 그렇게 착각했을지도 모른다.

얼어붙어 버린 몸뚱어리와 달리, 누군가가 인두로 지지는 것처럼 뜨거워진 머리가 아니었다면.

‘이건…… 말도 안 돼.’

나는 극심한 혼란 속에서 허우적거렸다.

수많은 의문 부호가 떠오르다 사라지길 반복하고, 이성과 감정은 방향을 잃고 서로를 향해 충돌했다.

무림(武林)이라 불리는 이 낯선 세상이 게임이 아닌 또 다른 현실이라는 것을 인지했을 때와 같은, 혹은 그 이상의 충격이 내 정신을 뒤흔들고 있었다.

그러나 이건 엄연한 현실.

나는 사그라지지 않는 경악을 온 힘을 다해 억누르며, 목소리를 쥐어 짜냈다.

“도대체, 어떻게?”

남의 것처럼 낯선, 잔뜩 쉬고 갈라진 목소리가 입술 사이로 흘러나온다.

그리고 그런 나와는 달리, 곧이어 돌아온 여인의 음성은 평온하고 담담했다.

“글쎄요. 미천한 제가 모든 것을 알 수는 없지요. 그러나…….”

대술사, 혹은 대마도사.

이 세상의 것이 아닌 힘을 얻은 그녀가 나를 똑바로 응시한다. 광신(狂信)이라 부를 수밖에 없는 굳건한 믿음이 깃든 눈빛과 목소리가 눈과 귀를 어지럽힌다.

“천주(天主)께서는 위대하십니다. 저는 단지 그분의 뜻과 말씀을 전하는 종복일 뿐이고요.”

“천주, 천주…….”

나는 무언가에 홀린 사람처럼 그 빌어먹을 두 글자를 중얼거렸다.

무림에서 첫걸음을 떼기 시작한 그 순간부터 지금까지, 여러 사람의 입을 통해 수없이 들어왔음에도 단 한 번도 진정한 실체를 마주하지 못했던 존재.

암천의 우두머리, 아니 그들의 왕이자 신이며 역천(逆天)을 바라는 절대자.

바로 그였다.

오직 그였다.

내가 가진 가장 은밀한 비밀 중 하나를, 그는 손바닥을 들여다보듯 훤히 알고 있던 것이다.

하지만 그것이, 앞서 내가 던진 물음에 대한 답은 될 수 없었다.

지금의 나는, 태원진가의 진태경은 하루아침에 뒤바뀐 존재였기에.

“나를 감시했던 건가? 처음부터?”

“감시? 당신을?”

백색의 면사 아래, 붉은 입술이 부드럽게 호선을 그렸다.

“솔직히 말해서, 불과 몇 년 전의 당신이 신경 쓸 필요조차 없는 존재였다는 건 모두가 알고 있는 사실 아닌가요?”

“그렇다는 건…….”

“간단한 이야기예요. 우리는 천하를 굽어보고 있었고, 당신은 그 안에서 스스로 빛났던 거죠. 멀리서도 또렷하게 알아볼 수 있을 만큼.”

“……!”

“흥미롭더군요. 서서히 몰락해 가던 변방 무가의 망나니가 잠룡(潛龍)이 되고, 화왕이라는 여의주를 얻어 신룡(神龍)이 되어 가는 과정이. 그리고 그 유례없는 성장 속도가.”

장장 수백 년간 수행을 쌓은 이무기는 여의주만 얻는다면 용이 될 수 있으나 태원진가의 진태경은 기껏해야 흙탕물 속의 토룡(土龍), 즉 지렁이에 불과했다.

그러나 시스템은 내게 무궁무진한 성장의 기회를 부여해 주었고, 세상 사람들은 굳이 내가 뭐라 변명하지 않아도 그 이유를 끊임없이 만들어 냈다.

하늘이 내린 무재(武才).

더할 나위 없이 완벽한 육신인 천무지체(天武肢體).

거기에 화왕 적천강이라는 위대한 무인의 가르침까지 더해져 지금의 무위를 지닐 수 있게 되었다고.

하여 그 누구도 의심하지 않았다.

아니, 의심할 수 없었다.

이 원초적인 야만이 남아 있는 세상에도, 상식의 선이 존재했으니까.

하지만 그들 이외의 누군가는, 천주만큼은 예외였노라고 지금 이 순간 대마도사는 말하고 있었다.

또 다른 뜻밖의 사실도 함께.

“우리는 그분의 명령에 따라 계속해서 지켜봐 왔고, 마침내 알게 되었죠. 누가 선택받은 자인지.”

그 순간, 나도 모르게 눈가가 파르르 떨렸다.

“지금…… 뭐라고?”

“왜, 이 표현이 마음에 들지 않나요? 개인적으로는 꽤 괜찮은 명칭이라고 생각했는데.”

나는 대마도사의 물음에 답하지 않았다.

그저 굳게 입을 다문 채, 지금 막 들었던 말을 마음속으로 되뇔 뿐이었다.

‘선택받은 자, 라고?’

앞서 나도 모르게 되물었던 이유는 한 가지뿐이었다.

누군가가 나를 이러한 명칭으로 부른 것이 이번이 처음은 아니었으니까.

가장 먼저 나를 선택받은 자라 칭한 이는, 지금 이 순간에도 저 멀리에서 이쪽을 향해 팽팽한 활시위를 겨누고 있었으니까.

‘궁성(弓星).’

물경 십만에 달하는 마교도로부터 구주 천하를 지켜 낸 정마대전의 영웅.

어디에서나 늘 눈부시게 빛났던, 그렇기에 삼성(三星)의 일원이라 칭해진 위대한 무인.

그리고 그런 궁성이 장장 수십여 동안 정체를 감춘 채 천하를 떠돌았던 이유는, 다름 아닌 한 사람이 남긴 서신 때문이었다.

‘……무신(武神).’

열 명의 왕. 세 사람의 별.

그 위에서 모든 것을 굽어보는 하늘, 우주, 혹은 천하 무림 그 자체.

과거에도 없었고, 이후에도 없을 고금제일의 영웅이자 무인.

바로 그가, 무신이 궁성에게 서신을 남겼다고 했다.

도대체 언제, 어디에서 나타날지 모를 한 사람을 찾으라고.

선택받은 자, 즉.

나를.

그렇기에 더욱더 이해할 수 없었다.

무신이 나라는 존재의 등장을 예견하고 궁성에게 서신을 남겼다는 것까지는 그렇다 치더라도.

어째서, 왜.

“너희는, 천주는 무슨 이유로 나를 살려 두는 거지?”

그 누구보다 암천의 행보를 번번이 가로막았던 나다.

가장 가까운 측근이자 수족이라 할 수 있는 네 명의 마군과 마후의 죽음에도 직접적으로 관여했고, 그 외에도 수많은 피해를 입혔다.

그야말로 천주의 입장에서는 백번을 죽여도 시원치 않을 존재.

그러나 대마도사는 앞서 똑똑히 말했다.

그녀의 주인은 내가 이곳에서 죽기를 원치 않는다고.

지금보다도 더, 더 강해져서 살아남기를 바란다고.

나는…… 반드시 이 의문에 대한 답을 들어야 했다.

천주가 내 생존을 바란다면, 그것은 분명 내 존재 자체가 언젠가 모두에게 위협이 되어 돌아온다는 뜻일 테니까.

“대답해, 어서.”

어느덧 경악도, 떨림도 사라진 지 오래다.

이제 남은 것은 눈앞의 현실과 이를 직시할 수 있는 냉정함 뿐.

나는 서늘한 눈빛으로 대마도사를 응시했다.

촘촘하게 짜인 백색 면사 너머로 어른거리듯 비치는, 주인을 향한 충성심으로 번뜩이는 그 눈동자를.

그리고 마침내, 굳게 다물려 있던 그녀의 붉은색 입술이 달싹였다.

“그분의 깊은 뜻은 천하의 그 누구도 감히 짐작할 수 없죠. 하지만 한 가지는 확실해요.”

천천히 내뱉는 호흡.

슬며시 올라간 입꼬리에 담겨 있는 것은, 명백한 비웃음이다.

“설령 모든 진실을 듣더라도, 너 따위가 저항할 수 있을까?”

“……!”

“솔직해지자고. 우리.”

거추장스러운 의복을 벗어 던지듯, 예의를 내려놓은 대마도사가 웃으며 말을 이었다.

“사람들이 기우제를 지내서 비가 내리는 것 같아? 아니야. 먹구름이 몰려오고 하늘이 원하면 내리는 거야. 그게 바로 이 세상의 이치고, 섭리(攝理)라고.”

쿠득.

면사 너머로 형형한 안광이 번뜩인 그때, 몸뚱어리를 타고 스멀스멀 기어오른 두꺼운 줄기가 내 목을 옥죄었다.

천천히. 동시에 강하게.

“죽고 싶다면 죽여 줄 수도 있어. 하지만 넌 그분의 뜻대로 살아남아야 해. 당장 너부터가 살고 싶을 거고. 안 그래?”

숨이 막혔다.

이미 전신이 속박당한 상황 속, 나는 서서히 숨통을 조여 오는 초목의 줄기를 느끼며 목소리를 쥐어 짜냈다.

“그럼…… 죽여.”

“뭐?”

“죽여, 보라고.”

“……!”

그 순간, 나를 바라보던 대마도사의 시선이 잘게 흔들렸다.

가쁘게 내뱉어진 내 음성에, 그와 달리 깊게 가라앉은 눈빛에 담긴 진심을 읽었기 때문이었다.

“너…….”

흐려지는 말꼬리와 함께 느슨해지는 압박. 나는 그런 그녀를 보며 피식 웃었다.

“왜, 못 하겠냐? 이 미친년아.”

쿠득!

언제 그랬냐는 듯이 다시 강하게 조여드는 줄기.

그럼에도 불구하고, 나는 숨을 헐떡이면서도 소리 내어 웃었다.

그래, 지금의 나는 명백한 약자다.

하지만, 목숨이 걸린 이 팽팽한 줄다리기에서 승리하는 것은 내가 될 것이다.

대마도사가 미친년이라면, 나는 또 다른 부류의 미친놈이었으니까.

‘이렇게 된 거, 못할 것도 없지.’

나는 눈을 부릅뜬 대마도사를 향해 환하게 웃었다.

그리고 온 힘을 다해, 전신의 심맥을 끊었다.

그녀가 내게 부여해 주었던, 바로 그 미세한 회복의 힘으로.

으득!
```

## Final English reading copy

```markdown
# Chapter 1050

When people faced a truth that went far beyond anything they’d expected, their reactions tended to fall into one of two camps.

They either fell into confusion, unable to understand it, or froze as they grasped the immense shock and weight it carried.

The Blood-Sword Demon Lord belonged to the first.

“What does that…?”

He muttered blankly, having forgotten even his pain.

Confronted with the despairing reality that the master he’d worshiped like a god had abandoned him, the fiend could hear the Grand Mage’s words from a moment ago ringing in his ears again and again.

*You can’t fall here. You have to get stronger than you are now.*

No matter how many times the Blood-Sword Demon Lord turned over the Grand Mage’s words about Jin Taekyung in his mind, he couldn’t understand them.

Used up and thrown away?

He couldn’t help feeling betrayed.

But if the strong wanted blood, the weak had to bleed.

That was a law of the world he knew well, having walked the Demonic Path all his life.

He still didn’t know why he, who had devoted himself to the Lord of Heaven and Dark Heaven, was being discarded. But now that things had come this far, he had no choice but to accept it.

And yet, quite apart from that…

Why? How? For what reason?

Why would the master he served entrust the execution of his loyal hunting dog to an enemy, even at such a great cost?

And not just any enemy, but a brat who wasn’t even thirty years old—someone who had thwarted Dark Heaven at every turn more than anyone else in the world.

And…

*Kill me, and get stronger?*

What on earth did his death—this one-sided execution—have to do with Jin Taekyung getting stronger?

The Blood-Sword Demon Lord couldn’t begin to guess what the Grand Mage’s final words meant. That was only natural.

There were limits to what he could imagine.

But at least one other person here knew the truth the Blood-Sword Demon Lord couldn’t.

“…You.”

The young man’s lips had gone white, and the muscles in his face had stiffened.

He stared at the woman before him with vacant eyes, having even forgotten to breathe. At last, he managed to squeeze out a voice.

“What are you even… talking about?”

This wasn’t a question. It was a denial.

He couldn’t bear to believe in a reality that couldn’t possibly come true, so he was desperately trying to deny it.

The Grand Mage looked at the young man—Jin Taekyung—and her eyes curved into crescents.

“You already know, don’t you?”

“…!”

“Do I have to spell out what I mean, right here?”

The words that turned his ominous suspicion into certainty reached his ears. Jin Taekyung felt his mind turning white.

Only one phrase remained in his empty head.

*Level Up.*

* * *

Was this what it felt like when all the blood in your body turned cold?

For that moment, it was as if the whole world had stopped.

No—maybe I really had mistaken it for that.

If not for my head, which had grown hot as if someone were searing it with a branding iron, while my body remained frozen.

*This… can’t be real.*

I floundered in a storm of confusion.

Question marks appeared and disappeared, over and over, while reason and emotion lost their bearings and crashed into each other.

The shock rocking my mind was like—or perhaps greater than—the shock I’d felt when I realized this strange world called Murim wasn’t a game, but another reality.

And yet this was undeniably real.

I forced down my undying shock with everything I had and squeezed out a voice.

“How? How is this possible?”

A hoarse, cracked voice, so unfamiliar it might have belonged to someone else, slipped between my lips.

Unlike me, the woman’s answer came back calm and composed.

“Who knows? I’m too insignificant to know everything. But…”

The Grand Sorceress—or the Grand Mage.

She had gained power that didn’t belong to this world. Now she stared straight at me. Her eyes and voice were filled with such steadfast faith that it could only be called fanaticism, and they set my senses reeling.

“The Lord of Heaven is great. I am merely a servant who conveys His will and His words.”

“The Lord of Heaven. The Lord of Heaven…”

Like a man under a spell, I muttered the damn name.

Ever since the day I’d taken my first steps in Murim, I’d heard it from countless people. And yet I’d never once encountered its true form.

The leader of Dark Heaven—or rather, their king and god, the absolute being who sought to defy heaven.

It was Him.

Only Him.

He knew one of my most closely guarded secrets as clearly as if he were looking at the palm of his hand.

But that still didn’t answer the question I’d asked before.

Because I—Jin Taekyung of the Jin Family of Taiyuan—had become someone else overnight.

“Were you watching me? From the beginning?”

“Watching you?”

Beneath the white veil covering her face, her red lips curved gently.

“To be honest, everyone knows that just a few years ago, you weren’t even worth worrying about.”

“Then that means…”

“It’s simple. We were looking down upon the world, and you shone on your own within it. Bright enough to see clearly, even from far away.”

“……!”

“It was fascinating. Watching the spoiled son of a declining frontier family become a Hidden Dragon, then gain the Fire King as his dragon pearl and become a Divine Dragon. And watching you grow at a pace without precedent.”

An imugi that had cultivated itself for hundreds of years could become a dragon if it obtained a dragon pearl. But Jin Taekyung of the Jin Family of Taiyuan had been, at best, an earthworm wriggling in muddy water.

And yet the System had given me boundless opportunities to grow. People had come up with reason after reason for my progress, without me having to offer a single excuse.

Heaven-given martial talent.

The Heavenly Martial Physique, a body as perfect as could be.

And the teachings of the great martial artist Jeok Cheongang, the Fire King.

They said all of that had brought me to my current level of strength.

So no one had suspected a thing.

No—they couldn’t have suspected.

Even in this world, with its primitive savagery, there were limits to what people considered possible.

But the Grand Mage was telling me now that someone outside their reach—at least, the Lord of Heaven—had been the exception.

And she’d revealed another unexpected truth, too.

“We continued to watch under His command, and at last we learned who the Chosen One was.”

My eyes trembled before I could stop them.

“What… did you just say?”

“Why? You don’t like the expression? I thought it was rather good.”

I didn’t answer the Grand Mage’s question.

I simply shut my mouth and repeated the words I’d just heard to myself.

*The Chosen One?*

There was only one reason I’d repeated her question without thinking.

This wasn’t the first time someone had called me that.

The first to call me the Chosen One was, even now, far off in the distance with his bowstring taut, aimed in this direction.

*The Bow Saint.*

A hero of the Great Faction War, who had protected the Nine Provinces from the hundred thousand members of the Demonic Cult.

A great martial artist who had always shone brilliantly, wherever he went, and was therefore called one of the Three Saints.

And the reason the Bow Saint had spent decades wandering the land, concealing his identity, was a letter left behind by one person.

*…The Martial God.*

Ten Kings. Three Saints.

Above them all, a heaven looking down on everything—the universe, or perhaps Murim itself.

The greatest hero and martial artist of all time, with no equal before or since.

The Martial God had left a letter for the Bow Saint.

He’d told him to find someone who might appear at any time, in any place.

The Chosen One—that is…

Me.

That only made it harder to understand.

I could accept that the Martial God had foreseen my appearance and left the Bow Saint a letter about me.

But why? How?

“Why would you—or the Lord of Heaven—keep me alive?”

I was the one who’d stood in Dark Heaven’s way more than anyone else.

I’d been directly involved in the deaths of four Demon Lords and the Demon Empress, his closest subordinates and limbs. I’d caused him countless other losses, too.

From the Lord of Heaven’s perspective, I was someone he could kill a hundred times and still not be satisfied.

And yet the Grand Mage had said it plainly.

Her master didn’t want me to die here.

He wanted me to survive, and grow stronger. Stronger than before.

I had to hear the answer to this question.

If the Lord of Heaven wanted me alive, then it meant my very existence would one day become a threat to everyone.

“Answer me. Now.”

The shock and trembling were long gone.

All that remained was the reality before me, and the coldness to face it.

I stared at the Grand Mage with icy eyes.

At the eyes glimmering dimly through the densely woven white veil, burning with loyalty to their master.

At last, her tightly closed red lips moved.

“No one in the world would dare presume to guess His deep intentions. But one thing is certain.”

She breathed out slowly.

The corner of her mouth lifted. The expression there was unmistakable scorn.

“Even if you heard the whole truth, could you resist? You?”

“……!”

“Let’s be honest with each other.”

As if she were throwing off some cumbersome garment, the Grand Mage cast aside her manners. Smiling, she continued.

“You think it rains because people pray for rain? It doesn’t. The clouds gather, and when the heavens will it, the rain falls. That’s the way of this world. Its natural order.”

Crack.

A sharp gleam flashed behind her veil. A thick vine crept up my body and tightened around my neck.

Slowly. And powerfully.

“If you want to die, I can kill you. But you have to survive, according to His will. You want to live, too. Don’t you?”

I couldn’t breathe.

My whole body was already bound. As the plant stem slowly tightened around my windpipe, I squeezed out my voice.

“Then… kill me.”

“What?”

“Go on. Kill me.”

“……!”

The Grand Mage’s gaze wavered.

She’d heard the sincerity in my breathless voice and seen it in my eyes, which were steady despite my labored breathing.

“You…”

Her words trailed off, and the pressure around my neck loosened. I looked at her and gave a short laugh.

“What? Can’t do it, you crazy bitch?”

Crack!

The vine tightened again, as hard as before.

Even so, I laughed aloud, gasping for breath.

Yeah, I was unquestionably the weaker one now.

But in this tug-of-war with our lives on the line, I was going to win.

If the Grand Mage was a crazy bitch, then I was a different kind of crazy bastard.

*Now that it’s come to this, I can do it.*

I smiled brightly at the Grand Mage, her eyes wide open.

Then I severed the heart meridians throughout my body with all my strength.

Using that faint power to heal me—the very power she had given me.

Crack!
```
