<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1094.txt",
      "sha256": "1a9bd53cdea683bdb94995b23e377b60dc4b765b541d1e74ea93c03610eb9d4c",
      "bytes": 12001
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "bb154b889fa007e605facf49c5be53204921a006710326950ec28935da1ce945",
      "bytes": 1217
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "aa2e383c274853719aee6fdad641fd15982ff6289e42ddd0f942d170d98f7815",
      "bytes": 243957
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "d2722312a41f8d57282204ddbfcffbcd569dcf9a447c5c293b9868a319b23d92",
      "bytes": 916
    },
    {
      "path": "characters/Cheongheoja.md",
      "sha256": "4fc26519970dac56352e8b1dad9aa570d5c951a54882600b64d27083f8c0cb68",
      "bytes": 544
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "77f5fc70dfcf8cf4ea992601678727d654a1115f2fe81d7cf3f704980f39bbb6",
      "bytes": 1120
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "fd3b7ecee1d8b1ad1bdfed7cb4b429d8f47fc4d0d11bb8681884122f70349bfa",
      "bytes": 760
    },
    {
      "path": "characters/Grand Mage.md",
      "sha256": "45b981d14e9d6d872050f311fb0ec7564943be718d1be39d49a38362cc4446ff",
      "bytes": 619
    },
    {
      "path": "characters/Hong Dao.md",
      "sha256": "50bed640baf95bf6ca6b57e77e0ed6e3e874758accde937ee52a91e378d03481",
      "bytes": 1001
    },
    {
      "path": "characters/Hyeoncheon.md",
      "sha256": "43b2998119547e0465b6668302ccab012989a9f15bb2eb1bbce9e5a33c7d69da",
      "bytes": 651
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "fcc8819a4c1558c2c1abf170c953d20b2f17e5d32c967de5cd1ca0d3c5d0aea2",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "24c563be88232827c6d78416a9d3e20a4713edb0f15c88f4762cd8c9a5de48ec",
      "bytes": 623
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ebe79c16d6adf08cf85ebe92be4ce390014b7513b9c2f13e94caedd0cd180dd5",
      "bytes": 287086
    }
  ],
  "estimated_tokens": 11255
}
-->

# Durable State Update — Chapter 1094

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
1 and safe_through 1094. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1094. Profile updates may replace only one
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
  "chapter": 1094,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1094,
    "continuity_sources": [1094],
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
    "Dark Heaven's army has arrived at Xining under the Blood Lord.",
    "Jin Taekyung chose to defend Xining's civilians and is fighting the Blood Lord, who is stronger than him.",
    "The Bow Saint is helping Taekyung.",
    "Jeok Cheongang and the Slaughter Saint are fighting Black Ghosts, who can rise again after apparently fatal injuries.",
    "Jeok's full-strength Flame-Extinguishing Divine Fist turned hundreds of enemies to ash; the Grand Mage survived behind an ice wall that is still melting.",
    "The Grand Mage vowed to kill Jeok Cheongang for that person; Jeok turned away after their standoff."
  ],
  "continuity_sources": [
    1093
  ],
  "open_questions": [
    "Who is the black-robed captive in Qinghai, and what does he know?",
    "Why did the Lord of Heaven spare Taekyung in Gansu, and what is his real purpose?",
    "Will the Alliance Leader and other righteous warriors reach Qinghai?",
    "What is the hidden ember Cheongheoja warned about?",
    "What are the outcomes of the fights involving Taekyung, Jeok Cheongang, the Slaughter Saint, the Blood Lord, and the Grand Mage?"
  ],
  "safe_through": 1093,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 청풍     | **Cheongpung**     |
| 굉도     | **Hong Dao**       |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 궁성     | **Bow Saint**                 | —              |
| 살성     | **Slaughter Saint**           | —              |
| 삼성     | **Three Saints**    |
| 십왕     | **Ten Kings**       |
| 태원진가   | **Jin Family of Taiyuan**        |
| 소림     | **Shaolin**                      |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 은인     | **Benefactor**                               |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 곤륜     | **Kunlun**             |
| 도사      | **Daoist**                                                      |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 청허자 | **Cheongheoja** | Kunlun Sect Leader. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 현천진인 | **Perfected Being Hyeoncheon** | Current Sect Leader of Wudang and Hyeongong's Senior Brother. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 자하신공 | **Zaha Divine Technique** | Huashan internal-energy technique used by Cheongpung. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 잠룡 | **Hidden Dragon** | Epithet or metaphor for Jin Taekyung. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 석가 | **Shakyamuni** | Buddhist figure invoked by Hong Dao in his earlier conversation with Jeok Cheongang. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 소림혈사 | **Shaolin Bloodshed** | Past incident cited by Hwangbo Eom. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 무량수불 | **Infinite Life Buddha** | Buddhist invocation used by Taekyung. |
| 도산검림 | **a mountain of sabers and a forest of swords** | Idiom describing the lethal life of martial artists. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 진인 | **Perfected One** | Honorific for the two Kongtong Elders killed at Dunhuang. |
| 흑귀 | **Black Ghost** | The Blood-Sword Demon Lord’s name for the Death Knights. |
| 대술사 | **Grand Mage** | Title of the veiled woman leading the white-robed mages. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 굉도 | 진태경 | senior_monk_to_guest_benefactor | Benefactor | formal-polite and probing | Hong Dao repeatedly addresses Taekyung as 시주 while identifying him as the Master of Morning Star. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 혈주 | 청풍 | hostile_opponent_to_newly_revealed_identity | Huashan's Invincible Divine Sword; Sword Saint's Disciple or grandson | mocking and taunting | Recognizes Cheongpung's public identity and needles him with his Sword Saint lineage while dismissing the added threat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 혈주 | 천주 | servant_to_absolute_master | Lord of Heaven | worshipful and deferential | Blood Lord repeatedly addresses the Lord of Heaven while apologizing and receiving power. |
| 천주 | 혈주 | absolute_master_to_servant | Blood Lord | commanding and reproachful | The Lord of Heaven directly rebukes Blood Lord and then empowers him. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 살성 | 청풍 | senior martial figure to younger companion | you | blunt and familiar | The Slaughter Saint scolds Cheongpung for disappearing without a word. |
| 청풍 | 살성 | younger companion to senior martial figure | old man | polite and familiar | Cheongpung apologizes and explains why he wandered off. |
| 대마도사 | 진태경 | adversary_to_adversary | you | polite, teasing | She uses polite phrasing while taunting him and warning him not to overexert himself. |
| 진태경 | 대마도사 | adversary_to_adversary | you bitch | insulting-casual | He curses at her while refusing to give up. |
| 대마도사 | 궁성 | Adversaries | Bow Saint | Not established | She identifies him by title when recognizing the archer who struck the Hell Fire sphere. |
| 천주 | 대술사 | master to servant | you | commanding and authoritative | Addresses her through mind-voice, ordering her to report, raise her head, and depart. |
| 대술사 | 천주 | servant to master | Lord of Heaven | extremely deferential | Uses reverent titles and self-abasing language while reporting and pleading. |
| 혈주 | 대술사 | fellow servant of the same person | you; you bitch | insulting-casual | Blood Lord taunts the Grand Mage and uses a crude insult. |
| 대술사 | 혈주 | fellow servant of the same person | you | contemptuous-casual | The Grand Mage addresses the Blood Lord while rebuking him. |
| 진태경 | 현천진인 | young martial artist addressing a senior Daoist Sect Leader | Perfected Being | polite | Jin responds respectfully to Hyeoncheon's assessment of the retreat. |
| 현천진인 | 진태경 | Kongtong Sect Leader addressing an allied martial artist | Daoist Friend Jin | respectful and measured | Refers to Jin as 진 도우 while discussing the Zhongnan Disciples’ future. |
| 궁성 | 청허자 | fellow martial master and former acquaintance | Cheongheo | polite and familiar | Uses his shortened name and remarks on his graying hair. |
| 살성 | 청허자 | fellow martial master and former acquaintance | you | blunt and familiar | Recognizes him from a prior meeting. |
| 청풍 | 청허자 | younger martial artist to senior sect leader | Grandpa Cheongheoja | cheerful and polite | Uses a friendly, familial form because they share the surname Cheong. |
| 진태경 | 청허자 | younger martial artist to senior sect leader | Sect Leader | respectful | Uses a formal greeting and bow. |
| 청허자 | 진태경 | senior sect leader to younger martial artist | Fellow Daoist Jin | warm and polite | Greets Taekyung by surname and confirms Hak Woo is well. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1093
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who directs its sorcerers’ seed experiments and prepares their deployment for the Lord of Heaven’s great cause.
- **Personality:** Confident, cruel, and controlling; strategically manipulates allies and adversaries, and conceals failures from the Lord of Heaven when he fears being discarded.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven and seeks to advance the Lord’s great cause; he regards the deceased Western Heaven Demon Lord and Southern Heaven Demon Empress as powerful allies whose deaths cost Dark Heaven, and considers Jin Taekyung and Cheongpung formidable adversaries.

### Cheongheoja.md

# Cheongheoja (청허자)

- **Safe through:** Chapter 1090
- **Aliases:** None
- **Role:** Cheongheoja is the Kunlun Sect Leader and Hak Woo’s master.
- **Personality:** Warm, composed, and patient, he faces setbacks with resolve and receives even startling company with good humor.
- **Voice:** Measured and gentle, using formal Daoist courtesies and calm metaphors.
- **Relationships:** Hak Woo is his Disciple; he knows Jin Taekyung by reputation and treats him warmly.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 1091
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, Sword Saint Mae Jonghak’s grandson and Disciple, a Supreme Peak master known as the Huashan Divine Dragon, creator of Mimi Step, and master of the Azure Dragon Pavilion; he has also learned concealment from the Slaughter Saint.
- **Personality:** Affable, dreamy, and childlike, with innocent curiosity, a deep love of martial arts, competitive pride, and compassion that leaves him unsettled by killing; he admires Taekyung’s resilience in the way he lives.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions; Taekyung is his true martial rival and the person whose way of life he admires, and the Slaughter Saint has become his mentor in concealment.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1093
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Grand Mage.md

# Grand Mage (대마도사)

- **Safe through:** Chapter 1087
- **Aliases:** None
- **Role:** A senior Dark Heaven sorcerer who directs its mages and participates in its plans to conquer the world.
- **Personality:** Strategic and ambitious, with a sharp temper when others squander opportunities or act without consulting her.
- **Voice:** Cutting and sardonic, using taunts and pointed questions to challenge others.
- **Relationships:** Serves the Lord of Heaven and is an antagonistic peer of the Blood Lord, whose unilateral decisions anger her.

### Hong Dao.md

# Hong Dao (굉도)

- **Safe through:** Chapter 1090
- **Aliases:** Dharma King
- **Role:** Abbot of Shaolin and the Murim's Dharma King; master of Unnamed and the only friend to whom Jeok Cheongang had opened his heart; after leaving the Star-Array Grand Banquet, he was found in a massive pit with both legs severed and catastrophic internal injuries, whispered final words to Jeok Cheongang, and died.
- **Personality:** Calm, responsible, quietly playful, and still regarded by Jeok as lazy for sleeping whenever possible.
- **Voice:** Quiet, deep, weighty, and resonant, with casual familiarity when speaking to Jeok Cheongang.
- **Relationships:** Old friend of Jeok Cheongang and close friend of Peng Cheolhu; master of Unnamed; before his death, entrusted the Green Jade Buddha Staff to Unnamed, warned Jeok about Jongni Chu, Dark Heaven, Unnamed, and the Buddhist Staff, and sent Unnamed to find the Master of Morning Star.

### Hyeoncheon.md

# Perfected Being Hyeoncheon (현천진인)

- **Safe through:** Chapter 1076
- **Aliases:** None
- **Role:** Perfected Being Hyeoncheon is the current Sect Leader of the Kongtong Sect, a veteran Daoist master, and a Supreme Peak martial artist.
- **Personality:** Grave and reflective, he bears the losses of the Great Faction War yet rejects punishing the innocent for their relatives’ crimes.
- **Voice:** Measured, solemn, and calm with the authority of a Sect Leader.
- **Relationships:** Hyeongong is his Junior Brother, and both studied under the same master from childhood.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1093
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1093
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
1094화




시간은 늘 절대적이다.

그러나 시간의 흐름을 느끼는 것은, 어디까지나 상대적인 영역에 있다.

고작 반 각 남짓한 짧은 시간 속, 마치 영원히 계속될 것만 같은 아슬아슬한 공방을 이어 가던 진태경에게는 더더욱 그랬다.

서걱!

옆구리를 타고 전해지는 불같은 통증을 느끼며, 진태경은 생각했다.

어느샌가 하나둘씩 상처가 늘어난 자신의 몸뚱어리가 둔해진 것인지. 아니면 혈주가 빨라진 것인지.

혹은, 둘 다인지.

하지만 이와 같은 진태경의 생각은, 지금 이 순간 혈주가 느끼고 있는 감정에 비하면 아무것도 아니었다.

‘이놈은…… 도대체 뭐지?’

분노에 사로잡혀 핏빛 안광을 줄기줄기 흩뿌리던 혈주의 눈동자는, 어느덧 깊게 가라앉은 채 파르르 떨리고 있었다.

세 번.

진태경과는 오늘로 세 번째 만남이다.

처음에는 그저 멀리서 지켜보았다.

태원진가가 산서성의 패자로 우뚝 선 그 날, 가문의 수치에서 잠룡(潛龍)으로 거듭난 애송이는 혈주에게 있어 퍽 흥미로운 존재였으니.

일 년 뒤의 두 번째 만남에는 흥미 이상의 감정을 느꼈다.

아니, 솔직히 말하자면 내심 놀랐다.

화왕의 제자로 선택받은 진태경은 몰라볼 수 없을 만큼 강해져 있었고, 그보다 더한 독기(毒氣)를 품은 새끼 맹수였다.

그래서 짓밟았다.

더욱 철저하게.

비록 검성의 개입으로 치욕스럽게 후퇴할 수밖에 없었지만, 혈주에게 있어 진태경을 상대하는 것은 손쉬운 일이었다.

화왕의 가르침 덕분에 맹수로 성장했다고는 하나, 자신과의 격차는 하늘과 땅 차이였으니.

하지만 또다시 일 년의 시간이 흐른 지금 이 순간, 혈주는 지금까지의 흥미나 놀라움을 넘어선 새로운 감정과 직면하고 있었다.

그 감정의 이름은, 다름 아닌 경악이었다.

‘……어째서, 어째서 쓰러지지 않는 것이냐.’

물론 머리로는 알고 있었다.

한낱 애송이에 불과했던 진태경의 손에, 어느덧 네 명의 마군과 마후가 유명을 달리했다는 사실을.

그러나 가슴으로는 이해할 수 없었다.

어찌하여 그런 일이 벌어질 수 있는지.

과거보다도 진일보한 신위(神威)를 갖춘 자신에게 맞서, 이토록 물러섬 없이 맞설 수 있는 것인지.

“놈!”

가라앉아 있던 눈동자 위로 다시금 시뻘건 혈광이 솟구친다. 그보다 거대하고 강렬한 도강(刀罡)이 진태경을 향해 쏘아졌다.

쉭, 서걱!

잘려 나간 머리카락이 흩날린다. 이미 갈기갈기 찢어진 의복 사이로 드러난 살갖이 풍압(風壓)에 의해 찢어졌다.

그러나 그뿐이다.

불과 한 뼘 차이로 도강을 피해 낸 진태경은 아랑곳하지 않고 신형을 내뻗었다.

팟.

신형이, 두 사람 사이에 놓인 거리가 지워진다.

동시에 저 멀리서 터져 나온 빛살과도 같은 섬광이, 공간을 가르며 쇄도하는 진태경의 어깨너머로 번뜩였다.

이제는 지긋지긋하게까지 느껴지는 강기의 화살이.

‘궁성(弓星)……!’

혈주는 이를 악물며 적도(赤刀)를 내리그었다.

꽈앙!

강기과 강기의 격돌.

그리고 그 혼란한 찰나의 틈새를 비집고, 이글거리는 열기가 실린 일장(一掌)이 뻗어 나왔다.

화아악!

주위를 둘러싼 공간이 일렁이고, 올올이 피어오른 아지랑이가 꿈결처럼 시야를 어지럽힌다.

하지만 그에 맞서는 혈주의 움직임에는 조금의 망설임도 없었다.

“감히!”

공력을 실어 터트린 외침과 함께, 혈주는 남은 한 손을 뻗어 코앞까지 다가온 화염을 움켜쥐었다.

아니, 진태경의 일장을.

콰드득!

손과 손이, 핏빛 강기와 화염이 맞부딪히고 뒤얽혔다.

평범한 사람이었다면 그대로 까무러치고도 남았을 끔찍한 작열통(灼熱痛)도 함께.

치지직.

궁성의 개입으로 반 박자 늦을 수밖에 없었던 반격.

그러나 생살이 타들어 가는 고통 속에서도 혈주는 눈 하나 깜짝하지 않았다.

되려 공격을 봉쇄당한 진태경을 향해, 낮게 깔린 음성으로 으르렁거렸다.

마치 스스로에게 다짐하듯.

“고작, 이 정도로 날 꺾을 수 있으리라 생각했더냐.”

고통이라면 이미 이골이 났다.

몇 번, 아니 수십 번도 넘게 목숨을 잃었을 상황 속에서도 그는 죽지 않고 늘 일어섰다.

주인이 내려 준 축복으로. 그 자신의 의지로.

“감히, 감히 네놈 따위가-!”

그리고 그때. 진태경의 입술 사이로 나직한 음성이 흘러나왔다.

“정확히는 네놈들, 이라고 해야지. 네놈이 아니라.”

“뭐?”

혈주가 자신도 모르게 반문한 그 순간.

쉬이이익!

사방에서 힘찬 파공성이 휘몰아쳤다.

자욱하게 일어난 먼지구름이 서서히 흩어지고, 그 속에서 일어난 흐릿한 인영(人影)들이 비로소 본래의 모습을 드러냈다.

“늦어서 미안해요, 은인.”

평소와 다르게 착 가라앉은 목소리. 그리고 자줏빛으로 물든 두 눈동자.

자하신공(紫霞神功)의 기운을 전신에 두른 청풍의 어깨너머로, 노쇠하지만 맑은 두 줄기의 음성이 울려 퍼졌다.

“무량수불. 본산(本山)의 불청객을 이제야 뵙게 되는구려.”

“그래. 네놈이 바로 그 악독한 마두렷다.”

청허자와 현천진인.

청풍에 이어 곤륜과 공동의 두 장문인마저 모습을 드러내자 혈주의 눈썹이 꿈틀거렸다.

아니, 그보다는 더욱 신경 쓰이는 존재를 발견해서이기도 했다.

‘궁성.’

묵묵하면서도 한 치의 흔들림 없이 자신을 향해 대궁(大弓)을 겨누고 있는 저 여인은 혈주에게도 결코 방심할 수 없는 상대다.

이와 같은 상황이라면 더더욱.

그러나 아직 그것으로도 끝이 아니었다.

“어느 날 꿈을 꾸었는데, 석가인지 나발인지가 찾아와서 그러더군.”

저벅.

뒤늦게 혈주의 귓가에 닿은 발소리와 함께, 자신의 하나뿐인 제자에게 돌아온 스승이 들끓는 음성으로 말을 이었다.

“굉도. 그 땡중을 죽인 개자식을 털끝 하나 남기지 않고 태워 버리라고.”

“자네 입에서 나온 이상 당연히 헛소리겠지만, 이번만큼은 믿어 주도록 하지. 나도 조금 다르지만 비슷한 방법을 생각해 놨거든.”

“전부 사실이야.”

“그래, 그런 것으로 하자고. 아무리 그래도 석가모니가 개자식 운운하진 않았겠지만.”

별다른 인기척도 없이 유령처럼 나타난 살성까지 포위에 합류하자, 혈주는 문득 도산검림(刀山劍林)에 둘러싸인 듯한 착각에 사로잡혔다.

눈앞의 진태경까지 포함한다면 자신이 상대해야 할 초절정 고수만 무려 일곱.

심지어 그중 셋은 제각각 삼성의 일익이자 그들과 충분히 비견될 십왕의 수좌(首座)였으니, 이는 결코 단순한 착각이 아니었다.

“이것이었느냐? 네놈이 노린 것이.”

콰득.

뒤얽힌 손과 손 사이로 뼈가 어긋나는 소리가 울려 퍼진다.

새카맣게 타들어 가는 것으로도 모자라 금세 녹아 버릴 것만 같던 그의 손은, 믿을 수 없는 회복력으로 화염을 몰아내고 있었다.

치직. 스르륵.

이 순간에도 그을리고 회복하기를 반복하는 손아귀에 힘을 주며, 혈주는 으르렁거리듯이 웃음소리를 흘렸다.

“하지만, 보아라. 정작 포위당한 것이 누구인지.”

진태경은 대답하지 않았다.

아니, 정확히는 대답할 수 없었다.

서로를 향해 맞닿은 손을 타고 끝없이 흘러들어오는 혈주의 공력과 인간의 것이라 할 수 없는 괴력을 감당하는 것만으로도 힘에 벅찼으니까.

하지만 깊숙이 가라앉은 진태경의 눈동자와 예리하게 날이 서 있는 감각은, 지금도 주위에서 벌어지는 모든 상황을 빠짐없이 인식하고 있었다.

이를테면, 반경 수백 여장에 걸쳐 펼쳐진 또 다른 거대한 포위망을.

그리고 그 선두이자 중심에 선 존재들을.

‘흑귀(黑鬼).’

놈들이다.

죽음의 구렁텅이에서 다시 태어난 존재들.

그렇기에 불사(不死)에 가까운 저주를 받은 죽음의 기사들.

다른 세계에서는 데스 나이트라 불리는 그들의 존재감을, 진태경은 선명하게 느낄 수 있었다.

그 숫자만 무려 십여 기에 달한다는 것과 철벽처럼 우뚝 선 채 숨 막히는 마기를 내뿜고 있는 그들의 뒤에 또 다른 누군가가 있다는 사실도 함께.

‘대마도사. 아니, 대술사.’

이미 예상했었던 바다.

그녀는 그토록 쉽게 죽을 만한 존재가 아니었으니까.

그러나 제아무리 한발 앞서 예측했다고 한들, 현실의 무거움이 사라지는 것은 아니었다.

‘이대로라면, 공멸(共滅)이다.’

아니, 어쩌면 그 이상으로 최악의 결과가 나올지도 모른다는 사실을 진태경은 직감했다.

소림혈사 때보다도 더욱 강한 무위와 이능(異能)을 갖추게 된 혈주와 대술사가 있는 한, 모든 흑귀를 쓰러트린다 해도 어떤 변수가 일어날지는 미지수였으니까.

그리고 이러한 선택의 기로 앞에서 갈등에 휩싸인 것은, 비단 진태경뿐만이 아니었다.

‘진정…… 이놈을 살려 두어야 한단 말입니까?’

주인에게 전하고 싶은 그 한마디를, 혈주는 마음속으로 뇌까렸다.

물론 그도 안다.

천주(天主).

세상 그 누구보다 그리 불릴 자격이 있는 자신의 주인이 눈앞의 저 빌어먹을 놈을 얼마나 원하고 있는지.

그렇기에 네 명의 마군과 마후들이 차례대로 죽음을 맞이했다는 소식을 들었을 때도, 되려 그들을 비웃고 욕했었다.

단지 그들의 나약함 때문에?

반은 맞고, 반은 틀렸다.

혈주가 죽은 이들을 욕했던 이유는, 그들이 주인의 명령과는 달리 진태경으로 하여금 몇 차례나 생사의 고비를 넘게 했기 때문이었다.

하지만…….

‘이제야 알겠군. 그 연놈들이 어찌하여 널 죽이려 했는지.’

지금 이 순간, 혈주는 그들의 마음을 비로소 이해했다.

또한 그와 동시에, 한편으로는 더욱더 이해할 수 없었다.

사사건건 암천의 행보를 방해하는 장애물이자, 고금(古今)을 통틀어 전례 없는 성장 속도를 보여 주고 있는 진태경을 그토록 원하고 있는 주인의 마음을.

언제나 변함없는 충성심으로 당신을 목숨 바쳐 섬기는 충복들보다, 진태경의 안위를 더욱 중요시하는 천주의 모습을.

‘천주시여. 내 하나뿐인 주인이시여. 부디 이 종에게 말씀해 주시옵소서.’

지금이라도 이 샛노란 싹을 잘라 내라고.

아니, 어느새 거목(巨木)이 되어 버린 진태경을 무슨 수를 써서라도 죽이라고.

혈주는 그 어느 때보다 간절하게 청했지만, 단지 그뿐이었다.

그의 음성은 주인에게 닿지 않을 것이고, 달라지는 것은 아무것도 없었다.

으득.

일순간, 이를 악문 혈주는 전신에 들끓어 오르는 분노를 실어 손을 떨쳤다.

쾅!

굉음과 함께 열 걸음을 물러난 진태경을 향해, 혈주가 씹어뱉듯이 입을 열었다.

“다음은 없다. 네놈을 죽일 것이다. 기필코.”

그리고 그 순간.

부우우우!

팽팽하게 당겨진 분위기를 단번에 끊어버리는, 웅혼한 뿔피리 소리가 저 멀리서 울려 퍼졌다.
```

## Final English reading copy

```markdown
# Chapter 1094

Time was always absolute.

But the way its passage felt was entirely relative.

Especially for Jin Taekyung, who had been locked in a desperate exchange that seemed destined to go on forever, all within a brief span of barely half a quarter-hour.

Slice!

Feeling the scorching pain along his side, Jin Taekyung thought:

Was his body growing sluggish as one wound after another piled up? Or was the Blood Lord getting faster?

Or was it both?

But compared to what the Blood Lord was feeling at that very moment, Taekyung’s thoughts were nothing.

*What… the hell is this guy?*

The Blood Lord’s eyes, once blazing with rage and spattering streaks of crimson light, had sunk deep. Now they trembled faintly.

Three times.

This was the third time he’d met Jin Taekyung.

The first time, he’d merely watched from afar.

On the day the Jin Family of Taiyuan rose to become the preeminent clan of Shanxi Province, the young upstart who’d gone from a disgrace to the family to a Hidden Dragon had struck the Blood Lord as quite interesting.

At their second meeting a year later, he’d felt more than interest.

No, to be honest, he’d been surprised.

Chosen as the Fire King’s Disciple, Jin Taekyung had grown so strong he was almost unrecognizable. More than that, he was a young beast brimming with a venomous ferocity.

So the Blood Lord had crushed him.

Thoroughly.

Though the Sword Saint’s intervention had forced him to retreat in humiliation, facing Jin Taekyung had still been easy.

The Fire King’s teachings might have helped the young beast grow, but the gulf between them was like the distance between heaven and earth.

But now, another year later, the Blood Lord was confronted with a new emotion, beyond the interest and surprise he’d felt until now.

That emotion was none other than astonishment.

*…Why? Why won’t you fall?*

Of course, he knew the facts.

Four Demon Lords and Demon Empresses had met their ends at the hands of Jin Taekyung, who’d once been nothing more than a young upstart.

But he couldn’t understand it in his heart.

How could something like that happen?

How could Taekyung face him so unflinchingly, when the Blood Lord’s might had advanced even further than before?

“You!”

Crimson light surged once more over his sunken eyes. A larger, more powerful blade-force shot toward Jin Taekyung.

Whoosh—slice!

Cut strands of hair fluttered through the air. The pressure of the wind tore at the skin showing through his already-ragged clothes.

But that was all.

Jin Taekyung dodged the blade-force by barely a handspan and lunged forward without a care.

Pop.

His figure shot forward, erasing the distance between them.

At the same time, a flash like a beam of light burst from far away and streaked through the space over Taekyung’s shoulder.

A Force arrow—by now, one he’d grown sick of seeing.

*The Bow Saint…!*

The Blood Lord gritted his teeth and swung his red blade down.

KWA-ANG!

Force clashed with Force.

And through the chaos of that split-second opening, a palm wreathed in searing heat shot out.

Fwoosh!

The space around them wavered, and wisps of rising heat shimmered through his vision like a dream.

But the Blood Lord’s movements showed not a hint of hesitation.

“How dare you!”

His shout burst with internal energy as he reached out his remaining hand and seized the flames just before they reached him.

No—the palm strike Jin Taekyung had launched.

KRRK!

Hand met hand. Crimson Force and flame collided and twisted together.

With them came a terrible burning pain that would have made an ordinary person faint on the spot.

Sizzle.

The Bow Saint’s intervention had forced the Blood Lord’s counterattack half a beat late.

But even as his flesh burned, the Blood Lord didn’t so much as blink.

Instead, he growled at Jin Taekyung, whose attack had been stopped, his voice low and heavy.

As if making a vow to himself.

“Did you really think this would be enough to break me?”

He was well accustomed to pain.

He’d faced death—not just a few times, but dozens—and always risen again.

By the blessing his master had bestowed upon him. By his own Will.

“How dare a wretch like you—!”

Just then, Jin Taekyung spoke in a quiet voice.

“More precisely, ‘you lot.’ Not ‘you.’”

“What?”

The Blood Lord’s startled question escaped him before he realized it.

Whoooosh!

Powerful whooshes swept in from every direction.

The thick cloud of dust slowly dispersed. In its depths, blurry figures stirred, finally revealing themselves.

“Sorry I’m late, Benefactor.”

Cheongpung’s voice was unusually subdued. His eyes had turned a deep purple.

Over Cheongpung’s shoulder, two voices rang out, old yet clear. The qi of the Zaha Divine Technique enveloped his entire body.

“Infinite Life Buddha. It seems we’re only now meeting the unwelcome guest at our mountain.”

“So you’re the fiend who’s been causing all this trouble.”

Cheongheoja and Perfected Being Hyeoncheon.

With Cheongpung followed by the Sect Leaders of Kunlun and Kongtong, the Blood Lord’s brow twitched.

Though it was also because he’d spotted someone even more troubling.

*The Bow Saint.*

The woman silently aiming her great bow at him, without a hint of wavering, was no one the Blood Lord could afford to underestimate.

Especially not in a situation like this.

But that wasn’t the end of it.

“I had a dream one day. Some guy called Shakyamuni, or whatever the hell his name was, showed up and told me this.”

Step. Step.

Footsteps belatedly reached the Blood Lord’s ears. The master who’d returned to his one and only Disciple continued, his voice churning with fury.

“Hong Dao. He told me to burn the bastard who killed that monk to a crisp, without leaving so much as a hair.”

“I figured it had to be nonsense, coming from you. But I’ll believe you this once. I had a similar idea myself, though not quite the same.”

“It’s all true.”

“Sure, let’s say it is. Still, I doubt Shakyamuni went around calling people bastards.”

The Slaughter Saint had joined the encirclement, appearing like a ghost without the slightest warning. The Blood Lord suddenly felt as though he were surrounded by a mountain of sabers and a forest of swords.

Including Jin Taekyung before him, he now had to face no fewer than seven Supreme Peak masters.

Among them were members of the Three Saints and the foremost of the Ten Kings, a master fully their equal. This was no mere illusion.

“So this was what you were after?”

Crack.

A bone shifted in the Blood Lord’s hand, where their palms were locked together.

His hand, so badly charred it seemed certain to melt away at any moment, was forcing the flames back with an unbelievable rate of recovery.

Sizzle. Slither.

As his grip tightened, even while it alternately charred and healed, the Blood Lord let out a growl of laughter.

“But look around. Which of us is actually surrounded?”

Jin Taekyung didn’t answer.

No—more precisely, he couldn’t.

Just handling the Blood Lord’s internal energy pouring endlessly through their joined hands—and his inhuman strength—was already pushing him to his limit.

But Taekyung’s gaze, sunk deep, and his keen senses still took in every detail of what was happening around him.

Such as the other vast encirclement, stretching hundreds of yards in every direction.

And the figures at its head and center.

*Black Ghosts.*

It was them.

Beings reborn from the pit of death.

Death Knights cursed with something close to immortality.

In another world, they were called Death Knights. Jin Taekyung could sense their presence clearly.

There were a dozen or so of them, standing like an iron wall and exuding suffocating demonic qi. He could sense someone else behind them, too.

*The Grand Mage. No—the Grand Mage.*

He’d already expected it.

She wasn’t someone who would die that easily.

But no matter how far ahead he’d predicted things, that didn’t make reality any less grim.

*At this rate, we’ll all die together.*

No—Jin Taekyung had a feeling the outcome might be even worse than that.

As long as the Blood Lord and the Grand Mage were here, with greater martial might and supernatural abilities than they’d possessed during the Shaolin Bloodshed, no one could say what might happen even if they took down every Black Ghost.

And Jin Taekyung wasn’t the only one torn at this crossroads.

*Must I truly let this man live?*

The Blood Lord repeated the question in his heart, wanting to relay it to his master.

Of course, he knew.

The Lord of Heaven.

The master who deserved that title more than anyone in the world wanted that accursed man before him.

That was why, when he’d heard that four Demon Lords and Demon Empresses had died one after another, he’d mocked and cursed them instead.

Was it simply because they were weak?

Half right, half wrong.

The Blood Lord had cursed the dead because, contrary to their master’s command, they’d let Jin Taekyung come close to death again and again.

But…

*Now I understand why those bastards tried so hard to kill you.*

At this moment, the Blood Lord finally understood how they’d felt.

And at the same time, he understood even less.

Why his master wanted Jin Taekyung so badly, when he was an obstacle who kept interfering with Dark Heaven’s plans and was growing at a rate unprecedented throughout history.

Why the Lord of Heaven cared more for Jin Taekyung’s safety than for the loyal servants who’d always served him, willing to give their lives.

*Lord of Heaven. My one and only master. Please, tell this servant.*

Tell him to cut down this bright-yellow sprout now, before it was too late.

No—to kill Jin Taekyung, who had somehow already grown into a towering tree, by any means necessary.

The Blood Lord pleaded more desperately than ever.

But that was all.

His voice would never reach his master, and nothing would change.

Gritting his teeth, the Blood Lord wrenched his hand free with all the fury surging through him.

KWA-ANG!

Jin Taekyung was driven back ten steps with a thunderous boom. The Blood Lord spoke as if spitting out the words.

“There won’t be a next time. I’ll kill you. No matter what.”

And at that moment—

Bwoooooo!

A deep, resonant horn sounded in the distance, cutting straight through the taut tension.
```
