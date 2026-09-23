<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0910.txt",
      "sha256": "3976ed021bb13cda28d263d05ab9f176454da7f0d46d473a552800266e6b4070",
      "bytes": 14599
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ee6fa61f2bc3228002c343d3d1f2c40f8060abe0fdfc608f60d9c828462cda27",
      "bytes": 1422
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "acd9684a058afcc0bbe3f5e01a5af4246b19251d761221cade8efde9fd414db4",
      "bytes": 231263
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "e3f840baae91ad762fae08f5d7fbe466a7abba5c06fee94da87a8da3ff0e6901",
      "bytes": 759
    },
    {
      "path": "characters/Hong Dao.md",
      "sha256": "e3d7b8dad2bc13a14fb0b46aa77bdfcacb78997b751311bf49ca71d5df688136",
      "bytes": 1000
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "424ed48af4991f7ccfbee58d5ebf0e508cb88478b7d02d7484091235177e3cd5",
      "bytes": 667
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "176ecfd58f7fbecf1bdcf002d4a24fcb2944a27aea5e55345cbae66b6a8f4e01",
      "bytes": 1445
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "f3d518c13952b64f67f165e66a0d70a5932fa1ded2b1cc734dc967c3009eeedb",
      "bytes": 1499
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "5b399fd1fc05b5feb7e1ed50ca1296e7380563f4d71cf0e92bde279b634f60e9",
      "bytes": 973
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "7c9d3cdf372b81992e7409b6d9e3fc5ed6161b66820cd0b95aaac9950e0631db",
      "bytes": 752
    },
    {
      "path": "characters/Namho.md",
      "sha256": "f2805afbc0c5a3271eb775e85e8e36d71e6a41bb1c38f79f89a78c0e65f74d0a",
      "bytes": 973
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "490cd68b2f7ca6348d73948ede1e4c19ca218dbb5c8eea5dfa40c729111f0d81",
      "bytes": 263127
    }
  ],
  "estimated_tokens": 12458
}
-->

# Durable State Update — Chapter 910

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
1 and safe_through 910. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 910. Profile updates may replace only one
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
  "chapter": 910,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 910,
    "continuity_sources": [910],
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
    "Taekyung has reunited with the Fire Dragon Pavilion members who were fleeing the black-clad pursuers.",
    "Taekyung used Fire Dragon’s Single Tail, the first form of the Blazing Flame Divine Spear; he is nearly out of internal energy, injured, and struggling to stay upright.",
    "More than a thousand pursuers appeared to remain after Taekyung’s attack; the group is still in danger.",
    "The scene revealed as the smoke clears may explain the urgency of Hwaran, Ilseom, and Sama Pyo and Ma Sanbao’s confidence in the rebellion, but has not yet been identified.",
    "Jeok Cheongang is fighting Cang Gong, the Eastern Heaven Demon Lord.",
    "Jeong Hogun and the Embroidered Uniform Guard are on the Emperor’s side and intervened to protect Taekyung.",
    "So Gyo’s identity and allegiance remain unknown.",
    "The Emperor and Cang Gong have not revealed all their forces."
  ],
  "continuity_sources": [
    908,
    909
  ],
  "open_questions": [
    "What is the scene revealed as the smoke clears?",
    "Who are the black-clad pursuers, and what are their capabilities?",
    "Who is So Gyo, and where does her allegiance lie?",
    "What is the nature of Cang Gong’s power and his relationship to the Lord of Heaven?",
    "What forces are the Emperor and Cang Gong still withholding?"
  ],
  "safe_through": 909,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 굉도     | **Hong Dao**       |
| 주화란    | **Ju Hwaran**      |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 법왕     | **Dharma King**               | Hong Dao       |
| 무신     | **Martial God**               | —              |
| 삼성     | **Three Saints**    |
| 소림     | **Shaolin**                      |
| 무림맹    | **Murim Alliance**               |
| 용봉표국   | **Yongbong Escort Bureau**       |
| 삼류     | **Third Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 낭인     | **wandering martial artist**                     |                                                       |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 정파     | **orthodox faction**                             |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 표국     | **Escort Bureau**                            |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 안휘     | **Anhui**              |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 방장      | **Abbot**                                                       |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 평화 | **Peace Guild** | Guild name. |
| 발설지옥 | **tongue-pulling hell** | Buddhist hell associated with punishment for liars and slanderers; explained in a footnote. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아미타불 | **Amitabha** | Buddhist invocation spoken by the unidentified arriving group. |
| 녹옥불장 | **Green Jade Buddha Staff** | Ancient Shaolin sacred treasure carried by Hong Dao. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 불장 | **Buddhist Staff** | Generic term in Hong Dao's final words; the specific treasure is 녹옥불장. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 교주 | **Cult Leader** | Leader of the Divine Cult. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 테스 | **Tess** | Figure invoked through Taekyung's quotation of “Know thyself.” |
| 도산검림 | **a mountain of sabers and a forest of swords** | Idiom describing the lethal life of martial artists. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 적천강 | 굉도 | old_friends | Hong Dao | familiar and teasing | Uses Hong Dao's personal name in their casual reunion. |
| 굉도 | 적천강 | old_friends | Fire Gate Sect Leader | familiar and teasing | Teases Jeok as the carefree Fire Gate Sect Leader. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 남호 | 혁무진 | hidden_shadow_agent_to_pavilion_member | you there / Han bastard | performatively hostile and abusive | Namho attacks Mujin and insults him to make the meeting appear to be a genuine expulsion. |
| 혁무진 | 남호 | pavilion_member_to_hidden_shadow_agent | old man | indignant and insulting | Mujin protests Namho’s staged attack and objects to the insult about his parents. |
| 주화란 | 남호 | pavilion_member_to_hidden_shadow_agent | you / Elder Namho | formal and appreciative | Hwaran respectfully praises the effort Namho invested in mapping Nanman. |
| 남호 | 주화란 | guide_to_escort_bureau_head | Escort King's granddaughter | approving and familiar | Namho praises Hwaran for recalling Ju Gongsan's records about Nanman. |
| 적천강 | 의원 | interrogator_to_physician | you; quack | blunt and threatening | Jeok shakes the physician and demands an explanation for Jin's seven-day sleep before ordering him to summon the Beast Miao King. |
| 적천강 | 법왕 | close deceased friend and peer | you | familiar and reflective | Jeok addresses the Dharma King in private thought while wishing he were present to clarify Jeok's confusion. |
| 혁무진 | 주화란 | Fire Dragon Pavilion member to fellow member | Young Lady Ju | polite and deferential | Mujin addresses Hwaran as 주 소저 while asking her to call a physician. |
| 주화란 | 적천강 | younger ally to legendary martial master | Great Hero Jeok | formal and deferential | Ju Hwaran addresses Jeok as 적 대협 while asking whether he is all right. |
| 신의 | 주화란 | senior physician to younger ally | Young Lady Ju | warm and teasing | The Divine Physician lightly teases Hwaran about being more worried for Jin than he is. |
| 남호 | 적천강 | junior_to_senior | Senior | respectful and formal | Namho refers to Jeok as 노선배님 while agreeing with him. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 909
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hong Dao.md

# Hong Dao (굉도)

- **Safe through:** Chapter 894
- **Aliases:** Dharma King
- **Role:** Abbot of Shaolin and the Murim's Dharma King; master of Unnamed and the only friend to whom Jeok Cheongang had opened his heart; after leaving the Star-Array Grand Banquet, he was found in a massive pit with both legs severed and catastrophic internal injuries, whispered final words to Jeok Cheongang, and died.
- **Personality:** Calm, responsible, quietly playful, and still regarded by Jeok as lazy for sleeping whenever possible.
- **Voice:** Quiet, deep, weighty, and resonant, with casual familiarity when speaking to Jeok Cheongang.
- **Relationships:** Old friend of Jeok Cheongang and close friend of Peng Cheolhu; master of Unnamed; before his death, entrusted the Green Jade Buddha Staff to Unnamed, warned Jeok about Jongni Chu, Dark Heaven, Unnamed, and the Buddhist Staff, and sent Unnamed to find the Master of Morning Star.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 905
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 909
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; he regards Taekyung as the person who has repeatedly saved him and now believes he may be able to save Taekyung in turn. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 907
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts Jin Taekyung, his publicly acknowledged Disciple and intended heir, regards him as the light of his later years, and will stand by him whatever path he chooses; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 909
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, and filial; remains controlled under pressure but has grown more assertive and openly impatient after the hardships she has endured.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 894
- **Aliases:** None
- **Role:** An unidentified legendary martial artist regarded as a pinnacle above the Ten Kings; more than fifty years ago, he defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, appearing first as a white-bearded elder and later as a young boy; Mae Jonghak received several teachings from him, while his identity, whereabouts, and possible connection to Cheon Taemin remain unknown.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 909
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years undercover in Nanman and maintained contact with Central Plains intelligence through the Pavilion’s Hidden Thread; he now guides the Fire Dragon Pavilion.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

## Korean source

```text
＃910화



서당 개도 삼 년이면 풍월을 읊듯이, 헌터라는 특수 직업군에서 몇 년 정도 구르다 보면 어지간한 상황에는 눈 하나 깜짝하지 않게 된다.

몬스터의 몸뚱어리에서 풍겨 오는 끔찍한 악취? 그 정도는 애교다.

핏물이 분수처럼 뿜어져 나오고 누군가의 사지가 잘려 나가는 그로테스크한 장면을 게임이나 영화가 아닌 현실에서 보게 된다면.

더불어 그 누군가가 나 자신, 혹은 내 동료라면…… 두말할 필요도 없다.

전장에 들어서기 전부터 느껴지는 죽음에 대한 공포. 그리고 온갖 잔인한 광경을 밥 먹듯이 지켜보다 보면 모든 신경과 감각이 무뎌지기 시작하고, 그제야 비로소 진정한 의미의 헌터가 된다.

바로 내가 그랬듯이.

하지만 제법 잔뼈가 굵은 나조차도 지금 이 순간만큼은 뱃속 깊숙한 곳에서 치밀어오르는 욕지기를 참을 수 없었다.

“저건…….”

도대체 뭐지?

그 뒷말은 차마 소리 내어 내뱉지도 못했다. 울렁이는 속을 가라앉히기 위해 입을 꾹 다물어야 했으니까.

그리고 이와 같은 반응을 보이는 것은 비단 나 혼자뿐만이 아니었다.

“우욱.”

가장 먼저 허리를 굽힌 주화란이 창백하게 질린 얼굴로 입을 틀어막는다.

용봉표국의 후계자로서 또래의 후기지수들보다 훨씬 풍부한 경험을 쌓은 그녀였지만, 이 자리에 있는 다른 이들에 비하면 아직 실전 경험이 부족하니 당연한 일이었다.

아니, 사실은 구토하지 않은 것만으로도 대단한 일이다.

당장 온갖 수라장을 헤쳐 온 나를 포함한 모두가, 일그러진 얼굴로 간신히 구역질을 참고 있었으니까.

“이게, 이게 무슨……?”

신의가 억눌린 목소리로 중얼거렸다.

파르르 떨리는 노 의원의 눈동자에는 숨기지 못한 경악과 불가해(不可解)의 영역을 들여다본 자만이 가질 수 있는 두려움이 담겨 있었다.

도무지 믿을 수 없는 눈앞의 광경과 함께.

칙. 치이익.

불과 십여 장도 되지 않는 짧은 거리. 살이 타들어 가는 소리가 들리고 끔찍한 악취가 콧속을 파고든다.

그리고 남아 있는 화염의 잔재와 검게 그을린 잿더미 속, 비틀거리며 일어서는 형체들이 있었다.

- 끄으. 그어어.

비명도, 그렇다고 언어도 아닌 목소리.

녹아내린 입술 사이로 정체를 알 수 없는 괴성을 내뱉던 흑의인, 아니 이제는 ‘그것’이라고 불러야 할 존재들은 비틀거리며 걸음을 내디뎠다.

마치 일말의 고통조차 느끼지 못하는 것처럼.

자신들의 몸 상태가 어떤지조차 알지 못하는 것처럼.

우득, 푸스스.

이미 한 차례 휩쓸고 간 열양지기에 의해 검게 그을렸던 팔이, 다리가, 그도 아니면 또 다른 무언가가 부서지고 재가 되어 흩날린다.

중심을 잃고 쓰러진 그것 중 하나가 고개를 갸웃거렸다.

- 그워……?

왜 몸이 움직이지 않느냐고 묻는 듯한 몸짓을 보며, 나는 등골이 찌르르 울리는 것을 느꼈다.

‘움직인다고? 그 정도의 일격에 당하고도?’

물론 저들 전부가 내 공격에 휘말린 것은 아니다.

그러나 적어도 가장 선두에 있던 백여 명의 흑의인들은 창날에서 쏟아진 화염을 고스란히 뒤집어썼다.

그 끔찍한 열기를. 열양지기로 이루어진 막강한 일격을.

그것이 내 눈으로 똑똑히 보았고, 이 자리의 모두가 알고 있는 사실이었다.

바로 그랬기에, 더욱더 믿을 수 없었다.

‘분명히 절명했어도 이상하지 않을, 아니 오히려 살아남을 수 없는 위력이었을 텐데.’

비록 그리 좋지 않은 몸 상태였지만, 전력을 다했다.

남아 있던 공력 중 대부분을 쏟아부었고, 스스로도 확신이 있었다. 이 일격으로 최소한 저들 중 일 할은 죽일 수 있다는 확신이.

하지만 아니었다.

지금 내 눈앞에는, 선두의 백여 명 중 자그마치 절반에 달하는 인영들이 한때 동료였던 잿더미를 짓밟으며 몸을 일으키고 있었다.

그것도, 아직 숨이 붙어 있는 무언가라고는 생각할 수 없는 형태로.

“……미치겠군. 지금 내가 뭘 보고 있는 거지?”

정마대전이라는 끔찍한 역사를 몸소 겪었던 남호의 침음성은 모두의 심정을 대변하는 것이었지만, 나만큼은 예외였다.

더 정확히 말하자면, 지금 이 순간의 나는 그들이 모르는 또 다른 광경을 바라보고 있었다.

‘도대체 어떻게.’

죽음은 세상 모두에게 공평한 법이다.

초절정 고수도 삼류 칼잡이처럼 병장기에 베여 죽고, 저것들처럼 살갗이 녹아내리고 내장이 타들어 가면 두 번 다시 일어날 수 없다.

그러나 놈들은 살아남았다.

이런 상황에서도 그 어떤 비명이나 동요도, 심지어 당연히 느껴야 할 고통조차 보이지 않은 채.

‘이건.’

그때였다.

도저히 믿기 싫은, 그러나 자연스럽게 떠오른 한 단어가 벼락처럼 뇌리를 관통한 것은.

곧이어 멍하니 벌어진 입술 사이를 비집고 흘러나온 것은.

“언데드(Undead)…….”

죽지 않은, 그렇다고 살아 있는 것도 아닌.

안식 대신 죽음의 연장선에서 삶을 이어 가는 초자연적인 존재들. 이 세상에서만큼은 나타나지 말아야 할 괴물들.

답은 오직 그것뿐이었고, 지금부터 내가 해야 할 일은 정해져 있었다.

“엄대두요? 도대체 그게 뭡니…….”

“뛰어.”

“예?”

나는 눈을 동그랗게 뜬 혁무진을 향해, 그들 모두를 향해 억눌린 목소리로 말을 이었다.

“살고 싶으면 뛰라고. 지금 당장.”

“……!”

“……!”

그리고 다음 순간.

쿠우웅!

찌르르 울리는 공기 속, 아직 사방에 가득한 매캐한 연기와 불길이 타오르는 잿더미를 해치며 걸어 나온 망자들의 군단이 한 몸으로 나아가기 시작했다.

그아아아아!

죽음의 기운이 담긴 부르짖음과 함께.



* * *



아득한 과거부터, 무림(武林)이라 불리는 곳은 이 대륙의 호사가들에게 있어 참으로 흥미로운 이야깃거리였다.

왜 그렇지 않겠나.

국경도, 법도 없는 또 다른 울타리.

국가와 백성이라는 틀을 벗어난 무법자들이 판을 치는 곳.

정의로운 협객, 마두, 혹은 때에 따라 그중 무엇도 될 수 있는 자들이 넘쳐 나며 아무리 대단한 고수라 해도 언제든지 죽음을 맞이할 수 있는 진정한 도산검림(刀山劍林)의 세상.

바로 그런 이유로 무림에 속한 이들은 괄시와 동경을 한 몸에 받아 왔고, 뭐든 떠들기 좋아하는 호사가들은 자신들이 보고 들은 모든 정보를 합쳐 순위를 매겼다.

무림서열록(武林序列錄)이라는, 웃기지도 않은 제목의 서책이 탄생한 이유는 바로 그 때문이었다.

하지만 제아무리 발 넓고 귀 밝은 호사가들이라 하더라도 그들이 지닌 명백한 한계까지 어쩌지는 못했다.

누가 더 우위인가.

무림서열록에 한 번이라도 이름을 올린 이들은 모두 쟁쟁한 고수들이었고, 마지막 장에 가까워질수록 초인(超人)이라 불리는 자들이 적지 않게 등장했다.

정파. 사파. 마교. 혹은 정사지간에 속한 초절정 고수들.

그들 중에는 외로운 늑대처럼 홀로 무림을 떠도는 낭인도, 잘 알려지지 않은 신비 문파의 계승자도, 거대한 세력을 이끄는 우두머리와 교주(敎主)라 불리는 이가 있었고, 그들 대부분은 한 가지 공통점을 공유하고 있었다.

불침(不侵). 금투(禁鬪).

각자 서로를 향해 섣불리 대치하지도, 쉽게 싸우지도 않는 것.

한 사람 한 사람이 무림을 움직이는 거인(巨人)인 만큼 당연한 일이었으나, 호사가들 입장에서는 퍽 아쉬운 일이었다.

만약 초절정 고수 간의 생사결이 벌어진다면, 확실한 서열을 알 수 있음은 물론 평생 안줏거리로 쓸 만한 진귀한 경험을 하게 될 테니까.

하지만 무림의 분쟁은 그리 쉽게 벌어지지 않았고, 최고로 손꼽히는 강자들의 이름이 적힌 무림서열록의 마지막 장은 오랫동안 수정되지 않았다.

지금으로부터 오십여 년 전, 정마대전이라는 폭풍이 몰아치기 전까지는.

그리고 길게 이어졌던 평화를 비웃기라도 하듯, 상상할 수도 없었던 수많은 것들이 뒤바뀌기 시작했다.

강자로 추앙받던 어디의 누군가가 죽고, 죽고, 또 죽고.

해가 뜨고 질 때마다 전해지는 소식에, 호사가들의 붓이 닳아 없어질 지경이었다.

하지만 해가 뜨고 지듯이, 새롭게 등장한 이름 또한 존재했다.



‘이것 좀 봐 주게. 아무래도 정보가 잘못 들어온 모양이야.’

‘잘못 들어왔다니. 그럴 리가 없을 텐데?’

‘한 번 읽어 보게. 안휘(安徽)에서 일천에 달하는 마교도가 몰살당했다는데, 아무리 생각해도 영 신빙성이 떨어져.’

‘일천이라, 제법 규모가 크긴 하군. 하지만 딱히 의심할 것까진 없고, 이번에는 무림맹이 제대로 한 방 먹인 모양인데?’

‘무림맹이 아닐세.’

‘응?’

‘모두 단 한 사람이 한 일이라고 적혀 있네. 누구의 도움도 없이, 홀로 마교도 일천을 전멸시켰다고. 한 놈도 예외 없이.’

‘……뭐?’



적천강이라는 이름은 그렇게 처음 알려졌고, 몇 번의 해가 기울고 다시 뜬 어느 날부터는 화왕(火王)이라는 별호를 갖게 되었으며, 한바탕 천하를 뒤흔들었던 정마대전의 끝자락에 다다랐을 때는 무림서열록의 마지막 장에 이름을 올렸다.

무신과 삼성.

그리고 그 뒤를 잇는 열 명의 초절정 고수 중, 가장 흉포하고 강한 왕중왕(王中王).

화왕 적천강이라는 이름을.

하지만 정작 당사자는 이러한 사실을 조금도 자랑스러워하지 않았다.



‘무림서열록? 세상이 미쳐 돌아가는군. 요새는 땔감에 그따위 거창한 이름까지 붙이나?’



그리고 시큰둥해하는 적천강에게, 그에게 처음 이 사실을 알려 준 어느 땡중은 빙긋 웃으며 수상할 만큼 따끈한 곡차(穀茶)를 홀짝였었다.



‘글쎄. 그 정도인가? 그래도 빈승이 살펴보니 땔감치고는 제법 정확한 구석이 있던데.’

‘그야 전부 멋모르는 놈들이 지껄이는 헛소리지. 천하에 정파 무림인들밖에 없나? 사마외도 중에도 강한 놈들이 얼마나 많은데.’

‘그래도 정파 무림에선 자네가 네 번일세. 무신과 삼성 다음이라니. 역시 대단허이.’

‘됐네. 객쩍은 말은 이쯤 하고 노부도 술이나 한잔 줘 봐. 이번에는 뭐로 담갔다고 했지?’

‘아미타불. 큰일 날 소리를. 이건 술이 아니라 곡차일세.’

‘곡차는 뭔 시부럴. 부처 옆구리 걷어차는 소리 하고 있네.’

‘어허. 그 입 좀 조심하라니까. 나중에 발설지옥(拔舌地獄)에서 고통받고 싶나?’

‘알겠네. 알겠으니까 그 손에 들린 녹옥불장 부러트리기 전에 한 잔 줘. 이 나이 먹고 소림사 경내에 불 지르고 싶진 않으니까.’

‘껄껄. 농담도. 그나저나 빈승이 추측건대, 적어도 근 십 년 안에는 자네가 이 무림서열록의 순서를 뒤집을 걸세.’

‘음. 아마도 뒤집겠지. 십 년 안에 뒈져도 이상하지 않을 나이니까.’

‘……아미타불, 재수 없는 소리를 아무렇지 않게 하는군.’

‘사실 이만하면 오래 살았지 뭐. 우리가 언제 다시 만날지는 모르겠지만, 십 년 뒤에도 연락이 없으면 구화산에 찾아와서 내 시신이나 화장해 주게. 가장 높은 봉우리에서 뿌려 주면 더 좋고.’

‘흠. 자네도 보기보다 호사스러운 사람이었구먼. 소림사 방장에게 찾아와서 염불이나 외라니.’

‘염불도, 극락왕생(極樂往生)도 필요 없어. 그게 내가 살아온 방식이니.’

‘그럼 내기 하나 할까?’

‘내기? 무슨 내기 말인가?’

‘자네가 십 년 뒤에 삼성마저 뛰어넘을지, 아니면 자네 말처럼 죽을지. 참고로 빈승은 전자에 걸겠네.’

‘…….’

‘빈승을 믿게. 그리고 십 년 뒤에 이곳에서 다시 술 한잔하자고.’



오래전의 일이다.

약속했던 십 년의 세월이 세 번이나 반복되고, 실수로 거둬들인 못난 제자를 떠나보내고, 마주 앉아 술잔을 기울이던 벗마저 흙으로 돌아갈 만큼.

그러나 지금 이 순간, 적천강은 오랫동안 잊고 있었던 그 기억을 문득 떠올리고 있었다.

늘 사람 좋게 웃고 있던 법왕 굉도가 진지한 얼굴로 건넸던 그 한마디를.



‘자네는 삼성을 뛰어넘을 걸세.’



퍼엉!

흐릿한 벗의 목소리가, 강력한 장력(掌力)이 토해 낸 파공음에도 사라지지 않는다.

아니, 오히려 더더욱 또렷하게 들려왔다.



‘빈승을 믿게.’



쉬쉬쉬쉭!

칼날 같은 바람이 휘몰아쳤다. 그러나 창백한 피부의 노인, 동천마군의 맹렬한 공격은 적천강의 몸 어디에도 닿지 못했다.

그리고 그것이, 그에게는 너무나도 당연하게 느껴졌다.

‘아.’

적천강은 문득 가슴 깊숙한 곳에서 차오르는 고양감을 느꼈다.

어언 일백 하고도 수십 년을 살았다. 일평생 누군가에게 고통을 주었고, 고통을 받았고, 그 고통을 처음으로 나누기도 했다.

연로한 나이. 마음속에 들어찼던 심마.

‘천운으로 찾아온 지금의 이 경지가, 내 마지막 한계일 줄 알았거늘.’

이제는 안다.

자신이 틀렸음을. 떠나간 벗의 말이 옳았음을.

‘비록 아직 넘어서지는 못했으나.’

내 노력해 보지.

혀끝에서 흩어지는 그 한마디와 함께, 적천강의 입가에 흐릿한 웃음이 맺혔다.

그리고 그 순간.

화륵.

지금까지는 볼 수 없었던 거대한 화염이, 동천마군의 가슴을 강타했다.
```

## Final English reading copy

```markdown
# Chapter 910

Just as a dog in a village school can recite poetry after three years, a few years of working as a Hunter—a specialized profession—can make you stop batting an eye at most situations.

The awful stench coming off a monster’s corpse? That’s nothing.

If you see blood spraying like a fountain and someone’s limbs getting chopped off—not in a game or a movie, but in real life—

And if that someone is you or one of your companions… well, there’s no need to say more.

The fear of death you feel before even stepping onto a battlefield. Then, after watching all kinds of brutal scenes as often as you eat, every nerve and sense starts to grow numb. Only then do you become a Hunter in the truest sense.

That’s how it was for me.

But even I, with a fair amount of hard-earned experience under my belt, couldn’t hold back the nausea rising from the pit of my stomach right now.

“That’s…”

*What the hell is that?*

I couldn’t bring myself to say the rest aloud. I had to clamp my mouth shut to settle my churning stomach.

And I wasn’t the only one reacting that way.

“Ugh.”

Ju Hwaran was the first to bend over. Her face had gone pale as she covered her mouth.

As the heir to the Yongbong Escort Bureau, she’d had far more experience than other young prodigies her age. But compared to everyone else here, she still lacked real combat experience. It was only natural.

No, the fact that she hadn’t thrown up was impressive all by itself.

Everyone here—including me, who’d fought my way through all kinds of hellish situations—was barely holding back a gag, our faces twisted.

“What… What is this?”

The Divine Physician muttered in a strangled voice.

The old physician’s eyes trembled. They held undisguised shock and the fear of someone who’d glimpsed something beyond comprehension.

Along with a sight before us that was impossible to believe.

*Sizzle. Hissss.*

The distance was short—not even a dozen *jang*. We could hear flesh burning, and a horrible stench wormed its way into our noses.

Then, amid the remnants of the flames and the blackened ashes, shapes began to stagger to their feet.

“Grrr… Gaaah.”

Their voices were neither screams nor words.

The black-clad figures—no, the things we could no longer call people—let out strange, unrecognizable cries through their melted lips and staggered forward.

As though they couldn’t feel even the slightest pain.

As though they didn’t even know what state their bodies were in.

*Crack. Crumble.*

Arms, legs, or something else entirely—blackened by the scorching heat that had swept through once already—broke apart and scattered as ash.

One of the things that lost its balance and fell tilted its head.

“Grr…?”

Watching that gesture, as if it were asking why its body wouldn’t move, sent a shiver down my spine.

*They’re moving? Even after taking a blow like that?*

Of course, not all of them had been caught in my attack.

But at least a hundred black-clad figures at the very front had taken the flames pouring from my spearhead full on.

That terrible heat. That devastating strike made of Scorching Yang Qi.

I’d seen it with my own eyes. Everyone here knew it.

That was exactly why it was even harder to believe.

*It had enough power to kill them outright. No—it should’ve been impossible for them to survive.*

My body might not have been in good shape, but I’d given it everything I had.

I’d poured in most of my remaining internal energy, and I’d been sure of the result. I was certain that strike would kill at least one in ten of them.

But it hadn’t.

Right before my eyes, nearly half of the hundred figures at the front were getting back up, trampling the ashes of what had once been their comrades.

And in a state that made it impossible to think of them as anything that still had a breath of life in it.

“…This is insane. What am I looking at?”

Namho’s groan, from someone who’d personally lived through the terrible history of the Great Faction War, spoke for everyone. But not for me.

Or, to be more precise, at that moment I was seeing something else the others didn’t know.

*How is this possible?*

Death was fair to everyone in the world.

A Supreme Peak master could be cut down by a weapon just like a Third Rate knife-fighter. If your skin melted and your insides burned like theirs, you couldn’t get back up again.

But they had survived.

Even in a situation like this, they neither screamed nor showed any agitation—not even a sign of the pain they should’ve been feeling.

*This is…*

That was when it happened.

A word I desperately didn’t want to believe, but which had naturally surfaced in my mind, struck me like lightning.

Then it slipped through my parted lips.

“Undead…”

Not dead, but not alive either.

Supernatural beings who carried on existing at the end of death instead of finding rest. Monsters that should never have appeared in this world.

There could be only one answer. And from that moment on, I knew what I had to do.

“Eom Dae-du? What does that mea—”

“Run.”

“What?”

I looked at Hyuk Mujin, his eyes wide, and spoke in a low, tight voice to him and everyone else.

“If you want to live, run. Right now.”

“……!”

“……!”

And the next moment—

*Rumble!*

Through the ringing air, the dense smoke still hanging all around us, and the blazing piles of ash, an army of the dead came marching out and surged forward as one.

“Grrraaaaa!”

Their cries carried the chill of death.

* * *

From time immemorial, the Murim had been a fascinating subject for the gossips of this continent.

And why wouldn’t it be?

Another world within a boundary without borders or laws.

A place where outlaws who lived beyond the confines of nation and citizen ran rampant.

A world teeming with people who could be righteous heroes, fiends, or—depending on the moment—neither. A true mountain of sabers and forest of swords, where even the greatest master could meet his death at any time.

For those reasons, the people of the Murim had been scorned and admired in equal measure. The gossips, who loved to chatter about everything, gathered every bit of information they could see and hear, then ranked them.

That was how the book with the ridiculous title *Murim Ranking Record* came into being.

But even the gossips, with their far-reaching connections and keen ears, couldn’t overcome the obvious limits of what they knew.

Who was stronger than whom?

Everyone whose name had appeared in the *Murim Ranking Record* was a formidable master. And the closer you got to the last page, the more often you came across those called superhuman.

Supreme Peak masters from the orthodox faction, the unorthodox faction, the Demonic Cult, or somewhere between orthodox and unorthodox.

Among them were wandering martial artists who roamed the Murim alone like lone wolves, heirs to mysterious and little-known sects, leaders of great powers, and people called Cult Leaders. Most of them shared one thing in common.

Nonaggression. A ban on fighting.

They didn’t confront one another lightly, and they didn’t fight easily.

It was only natural, since every one of them was a giant who could move the Murim. But for the gossips, it was a real disappointment.

If a life-and-death duel broke out between Supreme Peak masters, they’d learn for certain who outranked whom—and gain a rare story they could dine out on for the rest of their lives.

But conflict in the Murim didn’t erupt so easily, and for a long time the last page of the *Murim Ranking Record*, where the names of the greatest warriors were written, went unchanged.

That is, until the storm of the Great Faction War swept through more than fifty years ago.

And as if to mock the long stretch of peace, countless things no one could have imagined began to change.

One revered master died, then another, and another.

With news arriving every day as the sun rose and set, the gossips’ brushes were nearly worn to nothing.

But just as the sun rose and set, new names appeared as well.

“Have a look at this. I think the information must be wrong.”

“Wrong? That can’t be right.”

“Read it. It says a thousand Demonic Cult members were massacred in Anhui. I can’t believe that’s true.”

“A thousand? That’s quite a large number. But I don’t see any reason to doubt it. Looks like the Murim Alliance finally landed a proper blow this time.”

“It wasn’t the Murim Alliance.”

“What?”

“It says it was all done by one person. He wiped out a thousand Demonic Cult members alone, without anyone’s help. Not a single one was spared.”

“…What?”

The name Jeok Cheongang was first made known that way. A few years later, he acquired the title Fire King. By the end of the Great Faction War, which had shaken the world of the Murim, his name had made it to the last page of the *Murim Ranking Record*.

The Martial God and the Three Saints.

And among the ten Supreme Peak masters who followed them, he was the fiercest and strongest of the kings: the King of Kings.

The name Fire King Jeok Cheongang.

But the man himself wasn’t proud of any of it.

“*Murim Ranking Record*? The world’s gone mad. These days, do they give firewood some grand name like that?”

In response to Jeok Cheongang’s indifference, the monk who’d first told him about it smiled and sipped some suspiciously warm grain tea.

“Is that so? Still, when I looked it over, I found it surprisingly accurate for firewood.”

“That’s just a bunch of fools talking nonsense. Are there only orthodox martial artists in the world? Plenty of powerful fighters practice demonic and heterodox arts, too.”

“Even so, in the orthodox Murim, you’re ranked fourth. After the Martial God and the Three Saints. You’re quite something.”

“Enough. That’s quite enough of your nonsense. Now pour this old man a drink. What did you brew it with this time?”

“Amitabha. You mustn’t say such things. This is grain tea, not alcohol.”

“What the hell’s grain tea? You sound like you’re kicking the Buddha in the ribs.”

“Now, watch your mouth. Do you want to suffer in tongue-pulling hell[^1] later?”

“Fine, fine. Give me a cup before I break that Green Jade Buddha Staff you’re holding. I don’t want to set fire to the Shaolin Temple at my age.”

“Ha ha! What a joke. In any case, judging by my guess, within ten years at most, you’ll overturn the order of this *Murim Ranking Record*.”

“Hmm. I probably will. I’m old enough that it wouldn’t be strange if I kicked the bucket within ten years.”

“…Amitabha. You say unlucky things so casually.”

“Well, I’ve lived a long time. I don’t know when we’ll meet again, but if you haven’t heard from me in ten years, come to Mount Jiuhua and cremate my body. Better yet, scatter my ashes from the highest peak.”

“Hm. You’re more extravagant than you look. Asking the Abbot of Shaolin to come chant sutras for you.”

“I don’t need sutras or a fortunate rebirth in paradise. That’s the way I’ve lived.”

“Then how about a wager?”

“A wager? What kind?”

“Whether you’ll surpass even the Three Saints in ten years or die as you said. For the record, I’m betting on the former.”

“……”

“Trust me. And in ten years, let’s meet here and have another drink.”

It had happened a long time ago.

Three sets of ten years had passed since they made that promise. He’d sent off an unworthy Disciple he’d taken in by mistake, and even the friend he’d sat across from and shared drinks with had returned to the earth.

Yet at this very moment, Jeok Cheongang suddenly remembered that long-forgotten memory.

The words Hong Dao, the Dharma King, had once spoken to him with a serious expression, though he’d always smiled so amiably.

*You’ll surpass the Three Saints.*

*Boom!*

His departed friend’s faint voice didn’t fade, even beneath the blast of air released by the powerful Palm Force.

No—instead, it sounded even clearer.

*Trust me.*

*Shh-shh-shh-shing!*

Wind sharp as blades whipped around him. But the Eastern Heaven Demon Lord’s fierce attack—the pale-skinned old man’s—didn’t touch a single part of Jeok Cheongang’s body.

And that felt entirely natural to him.

*Ah.*

Jeok Cheongang suddenly felt elation well up from deep in his chest.

He had lived a hundred years and then some. All his life, he’d inflicted pain on others, suffered pain himself, and, for the first time, shared that pain with someone.

His advanced age. The Heart Demon that had filled his mind.

*I thought this realm, which fortune brought me to, would be the last limit I could reach.*

Now he knew.

He had been wrong. His departed friend had been right.

*Though I haven’t surpassed them yet…*

I’ll try.

As the words scattered from the tip of his tongue, a faint smile formed on Jeok Cheongang’s lips.

And at that moment—

*Fwoosh.*

A massive blaze unlike anything he’d shown before slammed into the Eastern Heaven Demon Lord’s chest.

[^1]: A Buddhist hell associated with punishment for liars and slanderers.
```
