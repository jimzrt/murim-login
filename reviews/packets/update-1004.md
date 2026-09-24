<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1004.txt",
      "sha256": "bfd3e1be9a63b97b070ddeafab111a4d265768d661a9f6926f72b4e8381d028a",
      "bytes": 14378
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "0466739263376e0f5832b215b2573db284eb36fc8d23b91e551f25bc48b5fcc7",
      "bytes": 1715
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b74c7a033bf83eabf70bfa6960aec25e0beac5a7f2b86c980a2c82f5d69182fb",
      "bytes": 237113
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "fec8eecdb644b48b19d9bd05f343676b9bbf1821e58c84610c769e1f3f0acccf",
      "bytes": 1375
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "293a7dcb892a0df0304c5d8492a18a2bd166d3b758a1cc9c9812333d8d49b960",
      "bytes": 1408
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "708b9490e34289eef732e65589927e5ffe1f7fb1d48c1a53cf15a09d7e588c2f",
      "bytes": 1613
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "27e77411ae4e0223816429571d21590dbeb6f4da81b35c673bbe66057e888ed6",
      "bytes": 622
    },
    {
      "path": "characters/Namho.md",
      "sha256": "3424bc867bba6cc6c818b1817e76c80951321865770e96925c200fd19df5b7ad",
      "bytes": 1092
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "5a8ef5304264df940eb438219882ffc872dcfb8e6f94207726335ebe9a8d32b8",
      "bytes": 937
    },
    {
      "path": "characters/Sima Gong.md",
      "sha256": "63019a5e50665351458044f80e0e1cd495bfe21ba17872ae5efbfc30c6b41000",
      "bytes": 641
    },
    {
      "path": "characters/Wolhwa.md",
      "sha256": "dccbc62aa2af46691d0edd47e3805f3bcd0ebd4860ae424bf59a71c076b77d4b",
      "bytes": 2458
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "afeffb3ea305c8845f5db1934d4fead68351bfc1c1b8648c3085723dff7f2d83",
      "bytes": 274761
    }
  ],
  "estimated_tokens": 13221
}
-->

# Durable State Update — Chapter 1004

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
1 and safe_through 1004. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1004. Profile updates may replace only one
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
  "chapter": 1004,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1004,
    "continuity_sources": [1004],
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
    "The group has reached Tianshui in Gansu and encounters someone unexpected there.",
    "Dark Heaven’s forces are approaching from beyond the desert and may rival or exceed the Hundred Thousand Demonic Disciples; their destination and objective remain unknown, with multiple fronts possible.",
    "The Great Nation has joined the allied forces, and the Murim Alliance’s intelligence network is active under emergency orders.",
    "Wolhwa sent Taekyung a sealed bamboo tube; Ju Hwaran briefly watched it with a somber expression.",
    "Ningxia’s former mounted-bandit gangs disbanded long ago; survivors became horse caravans, merchant companies, or Escort Bureaus, with no suspicious signs found in the Lower District Sect’s review.",
    "An unidentified Supreme Peak master remains in Ningxia; the Lower District Sect reports he is not a fiend, but his identity is unknown.",
    "Sama Pyo and Taishan have returned to their home region after being away for a little over a year.",
    "The Demon-Sealing Formation may neutralize Moving Formations; Zhuge Feng’s clan used it to contain the rift at Dongting Lake."
  ],
  "continuity_sources": [
    1002,
    1003
  ],
  "open_questions": [
    "Where will Dark Heaven’s advancing army strike, and what is its objective?",
    "What caused the System malfunction, and is it connected to the Lord of Heaven?",
    "Why did Sama Pyo’s father order him to return immediately?",
    "Who is the unidentified Supreme Peak master who pacified Ningxia?",
    "What is in Wolhwa’s sealed bamboo tube, and why did Ju Hwaran react somberly to it?"
  ],
  "safe_through": 1003,
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
| 월화     | **Wolhwa**         |
| 태원진가   | **Jin Family of Taiyuan**        |
| 하오문    | **Lower District Sect**          |
| 열화문    | **Fire Gate Clan**               |
| 종남파    | **Zhongnan Sect**                |
| 무림맹    | **Murim Alliance**               |
| 장강수로맹  | **Yangtze River Channel League** |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 정파     | **orthodox faction**                             |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 문주     | **Sect Leader**                              |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 선배     | **Senior**                                   |
| 상태               | **Status**                     |
| 명성               | **Fame**                       |
| 태원     | **Taiyuan**            |
| 감숙     | **Gansu**              |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 본문      | **our sect / this sect**                                        |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 녹림맹 | **Green Forest Alliance** | Bandit alliance receiving Black Mountain Stronghold’s tribute. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 하오문도 | **Lower District Sect member** | Member of the Lower District Sect. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 지풍 | **Finger Qi** | Invisible qi attack fired by the Western Heaven Demon Lord. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 공동파 | **Kongtong Sect** | Sect belonging to the Nine Sects and One Gang. |
| 흑야왕 | **Black Night King** | Epithet of Sima Gong, Sama Pyo's father and the Sect Leader who built the modern Black Dragon Demon Gate. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |
| 종남 | **Zhongnan Sect** | Orthodox faction that fought in the historic battle. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 월화 | junior_to_older_female_acquaintance | Wolhwa noona | casual-but-junior | Taekyung uses this address while speaking in his sleep or delirium. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 월화 | 진태경 | Lower District Sect branch leader to Jin Family young master | Young Master Jin; our Young Master | polite and lightly playful | Uses 우리 공자님, 진 공자, and the teasing 잠룡 공자 while greeting and teasing Taekyung. |
| 월화 | 혁무진 | inn proprietress and branch leader to visiting martial artist | Young Martial Artist; Martial Artist | polite and teasing | Uses 젊은 무사님 and 무사님 while discussing her profession and correcting Mujin's conduct. |
| 혁무진 | 월화 | Jin Family retainer to Lower District Sect Branch Leader | Young Lady; Branch Leader | formal-polite, then deferential | Initially addresses Wolhwa as 소저, then corrects himself to 지부장님 after learning her identity. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 사마표 | 진태경 | prospective recruit to pavilion master | you | polite, controlled, and candid | Sama Pyo uses 자네 while asking about Taekyung's attitude and admitting his intention to use him. |
| 진태경 | 사마표 | pavilion master to prospective recruit | you / that guy | blunt, informal, and distrustful | Taekyung speaks to and about Sama Pyo with casual forms such as 녀석 and 저놈. |
| 남호 | 진태경 | Hidden_Shadow_Pavilion_agent_to_mission_leader | Jin Taekyung / you | guarded and familiar | Namho addresses Taekyung as 자네 while explaining the contact and offering guidance. |
| 진태경 | 남호 | mission_leader_to_hidden_shadow_agent | you / Namho | probing and respectful | Taekyung questions Namho’s affiliation and later discusses Dark Heaven’s threat to Nanman. |
| 남호 | 혁무진 | hidden_shadow_agent_to_pavilion_member | you there / Han bastard | performatively hostile and abusive | Namho attacks Mujin and insults him to make the meeting appear to be a genuine expulsion. |
| 혁무진 | 남호 | pavilion_member_to_hidden_shadow_agent | old man | indignant and insulting | Mujin protests Namho’s staged attack and objects to the insult about his parents. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 남호 | 사마표 | guide_to_young_sect_leader | Young Sect Leader | blunt and admonishing | Namho warns Sama Pyo that all grass and animals in the territory belong to the Nanman Beast Palace. |
| 사마표 | 남호 | young_sect_leader_to_guide | Elder Namho | formal and apologetic | Sama Pyo apologizes after Taishan attempts to seize the calf. |
| 남호 | 적천강 | junior_to_senior | Senior | respectful and formal | Namho refers to Jeok as 노선배님 while agreeing with him. |
| 적천강 | 풍운검군 | legendary_elder_to_Zhongnan_sect_leader | Wind-and-Cloud Sword Lord | familiar and commanding | Jeok Cheongang tells him to get the Zhongnan disciples moving. |

## Listed compact profiles

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1003
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1002
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 999
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Peng Cheolhu regarded Taekyung as a worthy successor, inheriting all that Peng had to pass on; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 999
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 1002
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years undercover in Nanman and maintained contact with Central Plains intelligence through the Pavilion’s Hidden Thread; he guides the Fire Dragon Pavilion and represents Jin Taekyung and the Murim Alliance in negotiating the survivors’ chance to rebuild the Murong household.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1003
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Sima Gong.md

# Sima Gong (사마공)

- **Safe through:** Chapter 893
- **Aliases:** Black Night King
- **Role:** Sima Gong is the Sect Leader who built the Black Dragon Demon Gate into a major unorthodox power and the father of its Young Sect Leader, Sama Pyo.
- **Personality:** Sly, cunning, and inscrutable, with a ruthless reputation for valuing talent above family ties.
- **Voice:** Not established.
- **Relationships:** Sama Pyo is his youngest son among seven older brothers and nine older sisters, and he is the father of the current Black Dragon Demon Gate Young Sect Leader.

### Wolhwa.md

# Wolhwa (월화)

- **Safe through:** Chapter 1003
- **Aliases:** Eun Sowol (은소월); Wolhwa is the name used at Honghwaru
- **Role:** Shanxi’s foremost information merchant and Level 50 martial artist; Branch Leader of the Lower District Sect’s Shanxi branch with authority to mobilize more than thirty Shanxi branches; formerly posing as a high-ranking courtesan at Honghwaru, a pleasure house in central Taiyuan
- **Personality:** Striking, composed, observant, direct, quietly amused, and capable of ruthless, decisive violence when extracting information; comfortable teasing Taekyung while conducting serious information and negotiation work
- **Voice:** Polite and lightly playful; addresses Taekyung as Young Master Jin and delivers embarrassing observations without raising her voice
- **Relationships:** Knows Taekyung as a Honghwaru regular and the youngest son of the Jin Family; says she likes him, though her sincerity is unclear; has negotiated a mutually beneficial alliance with Jin Wikyung and the Jin Family

## Korean source

```text
＃1004화



세상 모든 것에는 저마다의 분위기가 있다.

어느 한 사람뿐만 아니라, 어떠한 장소나 물건에까지 깃든 고유한 느낌.

평범한 양민들은 그 분위기를 명확히 판가름하는 것에 있어 상당한 곤란함을 겪지만, 목숨을 건 싸움과 혹독한 수련을 바탕으로 오감(五感)을 극대화한 무인들은 다르다.

지금 이 순간, 침잠하게 가라앉은 눈빛으로 나를 바라보고 있는 적천강처럼.

‘어째서?’

그러나 뭐라 묻기도 전에, 머릿속에 떠오른 의문은 금세 사라졌다.

허허벌판의 중심에 우뚝 선 황토빛 성벽에 가까워질수록, 나 역시 적천강과 같은 감각을 공유할 수 있었으니까.

“음.”

얼마 떨어지지 않은 곳에서 들려오는 나지막한 침음성.

고개를 돌린 나는 이쪽을 빤히 바라보고 있던 풍운검군과 시선이 마주쳤다.

“자네도 느꼈나?”

“예.”

풍운검군을 향해 고개를 끄덕인 나는, 힘차게 내달리는 말발굽을 따라 빠르게 가까워지는 성벽을 응시하며 덧붙였다.

“조용하군요. 지나칠 만큼.”

무엇이든지 과한 것에는 독이 숨어 있는 법.

이제 백여 장 남짓까지 가까워진 소도시에서 뿜어져 나오는 분위기가 바로 그랬다.

여느 곳이나 그렇듯이 성벽 위에서 흩날리는 대국(大國)의 깃발과 그 아래 굳게 닫혀 있는 철문.

하지만 유달리 황량한 주위의 분위기를 제외하고서라도, 가장 중요한 것이 빠졌다.

‘사람.’

양민들은 성안에서만 살아가는 것이 아니다. 밖에서도 밭을 일구는 이들이 있고, 길을 오가는 행인들 또한 있다.

그러나 아직 해가 지기 전인데도 인적이 드물었다.

아니, 당장 보이는 모습으로는 단 한 명도 보이지 않았다.

사람이 없으니 소리도 없고, 그렇기에 더욱 스산할 수밖에.

그 사실을 눈치채지 못할 풍운검군이 아니었다. 한층 무거워진 목소리가 그의 입술 사이를 비집고 흘러나왔다.

“함정일 가능성도 있다고 보나?”

나는 잠시 침묵했다.

월화가 보낸 하오문도가 전해 준 정보에 따르면, 서쪽 일대에는 이미 무림맹의 감시망이 촘촘하게 깔려 있다고 했다.

그런데 작은 마을도 아닌 도시가 점령당한 마당에 그 사실을 모를 수 있었을까?

게다가…….

‘을씨년스럽지만, 단지 그뿐이다.’

외관상 전투의 흔적은 어디에서도 보이지 않고, 콧속에 스며드는 바람에는 한 줌의 혈향(血香)도 느껴지지 않았다.

지금껏 얼마나 많은 살과 뼈를 갈랐던가.

짙고 끈적거리는 핏물의 악취는 고작 하루 이틀 만에 사라질 수 없다.

하물며 한 도시를 점령하는 과정에 흘렀을 무수한 피를 생각한다면 더더욱.

‘함정은 아냐.’

그리고 짧은 고민 끝에 결론을 내린 그때. 말의 속도를 높여 가까이 다가온 사마표가 던진 한마디는 짐작을 확신으로 만들어 주었다.

“이대로 계속 가도 상관없다. 어차피 아무 일도 벌어지지 않을 테니.”

담담하기 그지없는 목소리와 눈빛.

그런 녀석의 모습에, 문득 뇌리를 스치는 한 가지 생각이 있었다.

“혹시?”

“그래. 제법 거창한 마중을 준비한 모양이야.”

바로 그 순간.

구구구궁.

수십여 장 밖, 굳게 닫혀 있던 철문이 천천히 열리기 시작했다.

그리고 천근(千斤)이 넘는 그 거대한 쇳덩어리가 벌어지며 생긴 틈새로, 냉막한 인상의 중년인이 모습을 드러냈다.

늘씬하면서도 강인함이 느껴지는 체구와 노인에 접어든 나이임에도 새치 하나 없이 가지런히 정돈된 칠흑색 머리카락.

마치 한 마리의 흑표범을 연상시키는 그의 모습에, 말로만 들었던 누군가의 별호와 이름이 벼락처럼 뇌리를 스쳤다.

‘흑야왕(黑夜王) 사마공.’

장강수로맹과 녹림맹이라는 사파의 거목들과 어깨를 나란히 한다는 흑룡마문(黑龍魔門)의 문주이자, 공동파와 함께 감숙성을 양분하는 또 하나의 패자.

하지만 나는 깨달음과 동시에 보았다.

그런 아버지의 모습이 가까워질수록, 어째서인지 깊게 가라앉아가는 아들의 눈동자를.



* * *



“무림 말학 사마공, 노선배를 뵙습니다.”

가장 먼저 적천강을 향해 건넨 사마공의 첫인사는, 공손한 것을 넘어 살짝 지나칠 정도였다.

그가 무림에서 가진 입지와 적지 않은 연배를 생각한다면 더더욱 그러했다.

물론 적천강은 눈곱만큼도 신경 쓰지 않았지만.

“무림 말학 같은 소리.”

코딱지가 튀진 않을까 염려가 될 정도로 세게 콧방귀를 뀐 그는 사마공을 바라보며 말을 이었다.

“그만큼 젊은 척을 하고 싶어 안달이 난 것이냐, 아니면 젊어지고 싶은 것이냐?”

포권을 거두어들이며 곧게 허리를 편 사마공이 대답했다.

“그런 뜻에서 드린 말씀은 아니나, 구태여 부끄러움을 무릅쓰고 말씀드리자면 둘 다라고 해야겠지요.”

“번지르르한 혓바닥은 여전하군.”

“선배께서도 여전하신 듯합니다. 비록 보이는 모습은 많이 변하셨지만 말입니다.”

“껍데기가 바뀌어도 알맹이는 그대로인 법. 그런 의미에서 보자면 네 녀석도 제법 껍데기가 거창해졌구나.”

문득 말을 멈춘 적천강이 천천히 주위를 훑었다.

정확히는 양민은 물론 쥐새끼 한 마리 보이지 않는 거리와 성문 근처를 가득 메운 일천여 명의 칼잡이들을.

그리고 새카만 무복을 걸친 그들이 흑룡마문의 문도임을 모르는 이는, 우리 중 아무도 없었다.

“많이도 데려왔군. 개떼처럼 드글거리는 꼴이 아주 볼만해.”

적천강의 눈빛과 음성에는 언짢음이 가득했다.

개파 이래 지난 삼백여 년간 정사지간(正邪之間)의 길을 걸어온 열화문이지만, 굳이 따지자면 그 본질은 정파에 조금 더 가깝다.

반면 흑야왕 사마공과 그가 이끄는 흑룡마문은 사마외도(邪魔外道)의 정통을 이은 자들.

더군다나 지금껏 함께하며 몇 번 들어 본 이야기를 통해 짐작해 보면, 사마공에 대한 적천강의 평가는 정마대전 당시부터 썩 좋지 않았다.

“근래 들어 동태가 심상치 않다 보니 그리되었습니다.”

“그래서, 그 심상치 않은 상황에 문파까지 비우고 이리 우르르 몰려왔더냐? 애꿎은 양민들까지 들쑤시면서.”

“오해가 있으신 모양이군요. 이 정도 병력이 빠져나갔다 한들 본문의 방비는 철저하고, 양민들은 각자의 생각으로 자리를 비켰을 뿐입니다. 만약 그들이 저희로 인해 두려움을 느꼈다면 어쩔 수 없는 일이지만…… 그것이 꼭 나쁜 일은 아니지 않겠습니까?”

“뭐라?”

적천강이 미간을 좁힌 순간, 사마공이 냉막한 인상과는 어울리지 않는 부드러운 웃음을 머금은 채 말을 이었다.

“선배께 무례를 저지르려는 것이 아닙니다. 다만 양민들도 이러한 낌새 속에서 더욱 큰 위기감을 느낄 테니, 그 역시 그들의 목숨을 구할 하나의 방편이라는 뜻에서 드린 말씀일 뿐입니다.”

“……!”

이쯤 되자 한 가지만큼은 인정할 수밖에 없었다.

이자, 달변이다.

말장난이나 궤변을 그럴듯하게 포장하는 솜씨가 매우 탁월하고 적당한 태도와 웃음으로 상대방의 기분을 가라앉힐 줄 안다.

거기에 더해 장강과 녹림의 두 맹주와 비견될 무공까지 갖추었으니, 이것이야말로 지금의 흑룡마문이 존재할 수 있는 가장 큰 이유였을 것이다.

‘부자지간이라 그런가? 이런 부분만큼은 확실히 닮았군. 처음 사마표를 만났을 때 딱 저랬는데.’

물론 그것은 과거의 일이다.

첫 대면 당시에만 하더라도 능구렁이 같은 화법과 태도를 보였던 사마표였지만, 함께 하는 시간이 길어질수록 그리 말수가 많은 녀석이 아니라는 것을 알게 되었으니까.

‘겉과 속을 다르게 하라는 건, 아버지한테 받은 가르침이었나?’

그런 생각과 함께 무심코 두 부자(父子)를 번갈아 바라보던 그때였다.

나와 사마공의 시선이 허공에서 맞닿은 것은.

“이런, 저 청년이로군요. 노선배께서 제자로 들이셨다는 천고의 기재(奇才)가.”

비록 목소리는 적천강을 향하고 있지만, 이채로 번뜩이는 눈빛은 다르다.

모른 척 시선을 회피하기에는 이미 늦은 상황.

슬쩍 옆에 있는 적천강을 바라보자, 눈살을 찌푸린 채 사마공을 바라보던 그가 고개를 끄덕였다.

“태원진가의 진태경이라고 합니다.”

“알지. 내 어찌 모를 수 있겠나. 자네에 관한 명성은 이미 이곳 감숙 땅에서도 모르는 이가 없을 정도인데.”

무림에서 누군가를 만날 때마다 늘상 주고받는 뻔한 허례허식(虛禮虛飾)이지만, 상대가 웃으며 이렇게 말할 때는 나 역시 그에 상응하는 대답을 해 줘야 한다.

더군다나 같은 편에 선 아군이라는 사실을 제외하고서라도, 눈앞의 사내는 사마표의 아버지니까.

“과찬이십니다. 저도 사마 대협의 위명은 익히 들어 알고 있었습니다.”

포권과 함께 건넨 공손한 대답에, 사마공이 웃으며 적천강을 바라보았다.

“이거 의외로군요. 노선배께서는 오래전부터 저를 썩 좋게 보지 않으시는 줄 알았는데.

“좋게 보지 않아? 노부가 네 녀석을?”

“아니었습니까?”

“당연히 아니지.”

하긴, 아무리 적천강이라고 해도 웃는 얼굴에 침 뱉을 수는 없는 노릇.

내가 그거 보라는 듯 사마공을 향해 흐뭇하게 웃어 보이던 그 순간, 적천강이 말을 이었다.

“썩 좋게 보지 않는 게 아니라, 그냥 별로 안 좋아한다.”

“…….”

“그래서 뒷담화 좀 했느니라.”

“…….”

“진태경 저놈이 입술에 침도 안 바르고 거짓말을 하는 게다. 위명은 뭔 개똥 쌈 싸 먹는 소리 하고 있…….”

쉭, 뻑!

“끄아아아악!”

미세한 파공성에 소리에 이어, 난데없이 터져 나온 누군가의 비명이 적천강의 목소리를 집어삼킨 그 순간.

차차차창!

동시에 사방에서 눈부신 검광(劍光)이 솟구치며 고함이 빗발쳤다.

“전투 준비!”

“흑룡마문은 적습에 대비하라!”

“장문인의 이름으로 명한다! 종남의 제자들은 지금 즉시 쇄월검진(碎月劍陳)을…… 그런데 자네 지금 뭐 하나?”

휘하의 제자들에게 검진 구축을 명령하던 풍운검군이 황당하다는 듯 말꼬리를 흐리자, 그제야 뭔가 이상함을 알아차린 좌중의 시선이 풍운검군을 따라 한 사람을 향해 쏠렸다.

벼락같은 비명과 함께 말안장에서 굴러떨어진 못생긴 놈.

아니, 혁무진을 향해.

“어우 씨, 갑자기 이게 뭔…….”

신음을 흘리며 비틀비틀 일어나던 신형이 석상처럼 굳었다.

마치 스포트라이트처럼 쏟아지는 무수한 시선의 한가운데, 말없이 눈만 끔뻑이던 혁무진이 뒤늦게 나를 발견하고 눈꼬리를 파르르 떨었다.

“조장님. 조장님 짓이죠.”

자연스럽게 옮겨지는 사람들의 시선.

그중에서도 특히 나를 뚫어져라 응시하는 사마공의 눈빛에, 나는 최대한 담담하게 입을 열었다.

“오해하지 마십시오. 저는 잘 모르는 사람입니다.”

사마공이 혁무진에게 물었다.

“자네는 누군가? 아무래도 종남파의 제자 같아 보이지는 않는데.”

혁무진이 씩씩거리며 대답했다.

“태원진가의 혁무진입니다.”

“그렇다는군.”

저 저, 쓸데없이 이럴 때만 눈치 없는 새끼 같으니라고.

‘한 방에 기절시켰어야 했는데. 저놈 저거 언제부터 저렇게 튼튼해졌지?’

나는 지풍(指風)을 제대로 쏘아 맞추지 못한 것을 내심 한탄하며 입을 열었다.

“약간 안면이 있긴 하죠. 완전히 모른다고는 안 했습니다.”

“결국 안다는 이야기로군.”

“음. 그렇게 되네요.”

“그래서, 저 젊은이가 갑자기 비명을 지르며 쓰러진 이유에 대해 어찌 생각하나?”

숨 막히는 침묵 속, 잠시 고민하던 나는 최선의 대답을 내놓았다.

“애가 원래 좀 아픕니다. 병이 있어요.”

혁무진이 입을 딱 벌렸다. 때마침 고통으로 자극된 침샘 때문인지, 반투명한 침 줄기가 턱을 타고 흘러내렸다.

“보세요. 하루에도 몇 번을 오락가락해서 이런 일이 아주 삼시세끼 챙겨먹듯이 일상다반사…….”

“와, 이럴 겁니까? 진짜 이럴 거예요? 끝까지 가요?”

정체 절명의 순간. 나는 혁무진의 어깨 너머를 향해 은밀히 전음을 날렸다.

정확히는 그의 뒤에서 동공 지진을 일으키고 있던 어느 눈치 빠른 은영각 요원을 향해.

- 지금!

다행히도 남호는 혁무진과 달랐다.

그는 나이가 믿어지지 않을 만큼 아주 빠르고 기민하게, 동시에 은밀한 솜씨로 손에 들고 있던 육포 쪼가리를 혁무진의 정수리 위로 떨어트렸다.

그리고 그 탐스러운 육포는, 무려 한 시진이나 공복 상태에 머물러 있던 누군가의 식탐을 자극하기에 충분했다.

“안 돼애! 육포오!”

빠악!

정수리를 내리찍는 솥뚜껑만 한 손바닥. 이내 털썩 쓰러지는 혁무진의 모습과 함께 죽음 같은 침묵이 흘렀다.

간신히 긴급 사태를 해결한 내가 입을 열기 전까지.

“자, 신경 쓰지 마시고 다들 이만 들어가시죠.”

“…….”

“…….”

아니, 왜 나를 미친놈 보듯이 바라보는 건데.
```

## Final English reading copy

```markdown
# Chapter 1004

Everything in the world has its own atmosphere.

A distinctive feeling that clings not only to a person, but even to a place or an object.

Ordinary civilians have considerable trouble judging that atmosphere clearly, but martial artists are different. Years of life-or-death battles and grueling training have heightened their five senses.

Like Jeok Cheongang, who was looking at me right now with a deeply sunken gaze.

*Why?*

But before I could ask, the question that had surfaced in my mind quickly vanished.

The closer we came to the ocher-colored walls standing tall in the middle of the vast plain, the more I began to share Jeok Cheongang’s sense of things.

“Hmm.”

A low hum came from not far away.

I turned my head and met the gaze of the Wind-and-Cloud Sword Lord, who had been staring in our direction.

“You feel it too?”

“Yes.”

I nodded to him, then watched the walls drawing closer as the horses’ hooves thundered beneath us.

“It’s quiet. Too quiet.”

Anything in excess had poison hidden in it.

That was exactly the feeling coming from the small city, now barely a hundred *jang* away.

As in any other place, the Great Nation’s flag fluttered atop the walls, and beneath it stood a firmly shut iron gate.

But even setting aside the unusually desolate mood of the surroundings, something essential was missing.

*People.*

Civilians didn’t live only inside city walls. Some worked fields outside, and travelers passed along the roads.

Yet though the sun had not set, there were few signs of anyone.

No—not a single person was visible.

No people meant no noise, and that only made the place feel more desolate.

The Wind-and-Cloud Sword Lord wasn’t someone who’d fail to notice. His voice emerged between his lips, heavier than before.

“Do you think it could be a trap?”

I fell silent for a moment.

According to the information Wolhwa’s Lower District Sect member had brought us, the Murim Alliance already had a tight surveillance network throughout the western region.

Could the Murim Alliance really have failed to notice a city—not just a small village—being occupied?

Besides…

*It’s bleak, but that’s all.*

There were no visible signs of battle, and the wind slipping into my nostrils carried not a hint of blood.

How much flesh and bone had I cut through by now?

The thick, cloying stench of blood couldn’t disappear in just a day or two.

Even less so when I considered how much blood must have been spilled in taking an entire city.

*It’s not a trap.*

And just as I reached that conclusion after a brief moment’s thought, Sama Pyo rode up beside us and tossed out a single line that turned my guess into certainty.

“There’s no harm in continuing on as we are. Nothing’s going to happen anyway.”

His voice and eyes were completely calm.

At the sight of him, a thought suddenly crossed my mind.

“Could it be?”

“That’s right. It looks like they’ve prepared quite an extravagant welcome.”

Right then—

Rumble.

Several dozen *jang* ahead, the firmly shut iron gate began to slowly open.

As the enormous mass of iron, weighing over a thousand *geun*, parted, a middle-aged man with a cold expression appeared in the widening gap.

He was slender but sturdy, and though he was old enough to be nearing his twilight years, his neatly groomed hair was still jet-black, without a single white strand.

The sight of him called to mind, like a bolt of lightning, the epithet and name I’d heard only in stories.

*The Black Night King, Sima Gong.*

Sect Leader of the Black Dragon Demon Gate, a giant of the unorthodox faction who stood shoulder to shoulder with the Yangtze River Channel League and the Green Forest Alliance. Alongside the Kongtong Sect, he was one of the two powers that divided Gansu Province between them.

But at the same time I realized who he was, I also saw something else.

For some reason, the closer that man—his father—came, the deeper his son’s eyes sank.



* * *



“This lowly martial artist, Sima Gong, pays his respects to you, Senior.”

Sima Gong’s first greeting, offered to Jeok Cheongang, was more than polite. It was almost excessive.

All the more so considering his standing in the Murim and his not-inconsiderable age.

Of course, Jeok Cheongang didn’t care in the slightest.

“Save me the ‘lowly martial artist’ nonsense.”

He snorted so hard I worried a booger might fly out, then continued, looking at Sima Gong.

“Are you so desperate to seem young, or do you want to be young again?”

Sima Gong withdrew his clasped hands and straightened his back before answering.

“That wasn’t what I meant, but if I may speak despite the embarrassment, I suppose the answer is both.”

“Your silver tongue hasn’t changed.”

“Nor have you, Senior. Though your appearance has changed quite a lot.”

“Change the shell and the contents stay the same. And in that regard, your shell has grown quite impressive too.”

Jeok Cheongang paused and slowly surveyed the area.

More precisely, he looked over the streets, where not even a single rat could be seen, and the thousand or so men with swords filling the area around the city gate.

And not one of us could mistake the men in black martial uniforms for anything but disciples of the Black Dragon Demon Gate.

“You brought quite a crowd. Swarming around like a pack of dogs. Quite a sight.”

There was nothing but displeasure in Jeok Cheongang’s eyes and voice.

Ever since its founding over three hundred years ago, the Fire Gate Clan had walked the line between the orthodox and unorthodox factions. But if one had to choose, it leaned a little closer to the orthodox side.

The Black Night King Sima Gong and the Black Dragon Demon Gate he led, by contrast, carried on the orthodox tradition of demonic, heterodox arts.

And judging from the things I’d heard about Sima Gong in the time we’d spent together, Jeok Cheongang’s opinion of him had been poor ever since the Great Faction War.

“Things have been looking rather strange lately, so it came to this.”

“So you emptied your sect and came pouring over here in a crowd because things look strange? Stirring up innocent civilians in the process.”

“You seem to have misunderstood. Even with this many troops away, our sect’s defenses remain secure. The civilians left of their own accord. If they were frightened because of us, then there’s nothing we can do about that… but it isn’t necessarily a bad thing, is it?”

“What?”

As Jeok Cheongang narrowed his eyes, Sima Gong continued, wearing a gentle smile that seemed out of place on his cold face.

“I have no intention of being disrespectful to you, Senior. I only meant that, with this sense of danger hanging over them, the civilians would feel an even greater urgency to protect themselves. That, too, could be a way to save their lives.”

“……!”

By that point, I had to admit one thing.

*This guy can talk.*

He was exceptionally good at dressing up word games and sophistry to sound convincing, and at calming people down with just the right manner and smile.

On top of that, he had martial arts that could rival the two Alliance Leaders of the Yangtze and the Green Forest. That was probably the biggest reason the Black Dragon Demon Gate was what it was today.

*Is that what comes of being father and son? They definitely resemble each other in that regard. Sama Pyo was exactly like that when I first met him.*

Of course, that was in the past.

When I’d first met him, Sama Pyo had spoken and behaved like a slippery eel. But the longer we spent together, the more I realized he wasn’t actually all that talkative.

*Was “keep your outside and inside different” something his father taught him?*

I was thinking that as my gaze moved unconsciously between the father and son.

That was when Sima Gong and I met eyes.

“Well, well. So that’s the young man. The rare genius the Senior took in as a Disciple.”

His voice was directed at Jeok Cheongang, but his eyes, gleaming with interest, were fixed elsewhere.

It was already too late to pretend I hadn’t noticed his gaze and look away.

I glanced at Jeok Cheongang. He was looking at Sima Gong with a frown, but gave a nod.

“My name is Jin Taekyung, of the Jin Family of Taiyuan.”

“I know. How could I not? There’s hardly anyone in Gansu who hasn’t heard of your fame.”

It was the same tired pleasantry people in the Murim always exchanged when they met. But when someone said it with a smile, I was expected to give an answer in kind.

Especially since, aside from the fact that we were on the same side, the man before me was Sama Pyo’s father.

“You’re too kind. I’ve heard a great deal about your reputation too, Great Hero Sima.”

I clasped my hands and answered politely. Sima Gong smiled and looked at Jeok Cheongang.

“This is unexpected. I thought you hadn’t thought much of me for a long time, Senior.”

“Hadn’t thought much of you? Me?”

“Didn’t you?”

“Of course not.”

Well, even Jeok Cheongang couldn’t spit in the face of a smiling man.

I smiled warmly at Sima Gong as if to say, *See?* Just then, Jeok Cheongang continued.

“It’s not that I think poorly of you. I just don’t like you.”

“……”

“So I’ve talked behind your back a little.”

“……”

“Jin Taekyung there is lying through his teeth. ‘Your reputation’ my ass—what kind of bullshit is—”

*Whoosh. Thwack!*

“Gyaaaah!”

The faint sound of something cutting through the air was followed by a sudden scream that swallowed Jeok Cheongang’s voice.

*Clang! Clang! Clang!*

At the same time, dazzling flashes of swordlight sprang up in every direction, and shouts rang out.

“Prepare for battle!”

“The Black Dragon Demon Gate, prepare for an enemy attack!”

“By order of the Sect Leader! Zhongnan Disciples, form the Moon-Shattering Sword Formation at once! …What are you doing?”

The Wind-and-Cloud Sword Lord had been ordering his Disciples to form a sword formation, but his voice trailed off in bafflement. Only then did everyone realize something was strange. Following the Wind-and-Cloud Sword Lord’s gaze, they all looked toward one person.

A homely-looking guy who’d fallen from his saddle with a thunderous scream.

No, Hyuk Mujin.

“Ugh, what the hell was that all of a—”

He groaned and staggered to his feet, then froze like a statue.

At the center of countless gazes pouring down on him like a spotlight, Hyuk Mujin had been blinking silently. Then he belatedly spotted me, and the corners of his eyes twitched.

“Captain. That was you, wasn’t it?”

Everyone’s gaze naturally shifted.

Sima Gong’s eyes in particular were fixed on me. I did my best to keep my expression calm as I opened my mouth.

“Don’t misunderstand. I barely know him.”

Sima Gong asked Hyuk Mujin,

“Who are you? You don’t look like a Disciple of the Zhongnan Sect.”

“I’m Hyuk Mujin, of the Jin Family of Taiyuan.”

“So that’s what he says.”

*That idiot. He’s only ever oblivious at the worst possible times.*

*I should’ve knocked him out in one shot. Since when did that guy get so sturdy?*

I cursed myself inwardly for failing to hit him properly with the Finger Qi, then spoke.

“I know him a little. I didn’t say I didn’t know him at all.”

“So you do know him.”

“Hmm. I suppose I do.”

“Then what do you think caused that young man to suddenly scream and fall over?”

In the suffocating silence, I thought for a moment and came up with the best possible answer.

“He’s always been a bit sick. He has a condition.”

Hyuk Mujin’s mouth fell open. Maybe because the pain had stimulated his salivary glands, a translucent string of drool ran down his chin.

“See? He goes back and forth a few times a day. This sort of thing happens as often as he eats three meals—”

“Wow, you’re really going to do this? You’re seriously going to do this? You want to take it all the way?”

At this critical moment, I sent a discreet Sound Transmission over Hyuk Mujin’s shoulder.

To be precise, I sent it to a quick-witted Hidden Shadow Pavilion agent behind him, whose pupils were shaking in alarm.

*Now!*

Fortunately, Namho was different from Hyuk Mujin.

He moved with a speed and agility that belied his age, and with a stealth that matched, dropping the strip of jerky in his hand onto the crown of Hyuk Mujin’s head.

And that tempting piece of jerky was enough to stir the appetite of someone who’d been hungry for a whole *shichen*.

“Nooo! Jerky!”

*Whack!*

A palm as big as a cast-iron pot slammed down on the crown of his head. Hyuk Mujin promptly collapsed, and a deathly silence followed.

Until I, having barely dealt with the emergency, spoke up.

“Now, don’t mind him. Let’s all go inside.”

“……”

“……”

No, why are you all looking at me like I’m crazy?
```
