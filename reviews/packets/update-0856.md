<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0856.txt",
      "sha256": "44226bd18a2df9cdb51399c8810312148eda78f04ae43199925ba352f86d8609",
      "bytes": 14237
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "90dbc5e508e51a5b1599d2146ff4f443dcb01117f2bf362f1985791fe3ca9189",
      "bytes": 2326
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "c71f13dfc442c6e46aa85633ed364d93f329588811e408d32dcd5604f9a1a746",
      "bytes": 228458
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "d0c0b40cb886e79e69bd3a491b1db7164b9c8912bcf0e347f309cea402fcfb22",
      "bytes": 759
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "1f736c3e1658a007ad4d487ad02965c0cc31a8e639ceb82ded7590e4c7d02dc3",
      "bytes": 973
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "d3e8223ed2aa786035bea977cbc1314e9c2bc6b216eb4700b7251a469979483e",
      "bytes": 1355
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "4c6f6f7ec5257bc658e1381ae15a32b3cc786317c2ce113dc6413569ca8a3139",
      "bytes": 1511
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "e79b971156d71f8941cb5e529b7a073cd1267deafae007dd5de9184530f78d0c",
      "bytes": 973
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "29f5eaf8616811388e3741e2f0d816b1f8800f339fb7294d031ab465d7c26797",
      "bytes": 914
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "3e45d7f52c86f535aff585272183762caa91b6bcec9d25da3c6848e2e9942984",
      "bytes": 253432
    }
  ],
  "estimated_tokens": 11595
}
-->

# Durable State Update — Chapter 856

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
1 and safe_through 856. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 856. Profile updates may replace only one
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
  "chapter": 856,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 856,
    "continuity_sources": [856],
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
    "The Divine Physician secured the Blood Soul Gu found in the deceased City Lord of Sichuan Province; it weakens hosts, causes episodes of madness, and eventually kills them.",
    "Jin suspects Dark Heaven’s covert killing of the City Lord is part of a scheme targeting the Great Nation, possibly its imperial family.",
    "Prince Shangshan Zhu Bao is traveling with fifty Embroidered Uniform Guard members; their expected route from Shanxi passes through Shandong and Jiangsu toward Zhejiang.",
    "Hong Jin joined Prince Shangshan in Shanxi after requesting support from the Lower District Sect.",
    "A Shanxi tracking team was wiped out while following the group, and its operation was suspended over concern about official intervention.",
    "The Hidden Shadow Pavilion issued an Alliance Leader-approved order for Jeok Cheongang, Jin Taekyung, and the entire Fire Dragon Pavilion to escort Prince Shangshan.",
    "Jin and his party are traveling toward Jiangsu to intercept Prince Shangshan before the first of next month.",
    "Jin Taekyung says he is currently well, but may hit a wall again; the Divine Physician is accompanying the party to treat him.",
    "The party has been traveling for seven days since leaving the Sichuan Tang Clan by remote routes; Ju Hwaran estimates Jiangsu is about three days away, and Jin intends to arrive in two."
  ],
  "continuity_sources": [
    854,
    855
  ],
  "open_questions": [
    "Why did Dark Heaven secretly kill the City Lord of Sichuan Province?",
    "Is Dark Heaven targeting the Great Nation’s Emperor or imperial family, and is it influencing the Son of Heaven?",
    "What is the Embroidered Uniform Guard’s purpose in traveling with Prince Shangshan, and can Jin’s party reach him in time?",
    "What prompted the imperial decree against Hong Jin, and what will happen to him and Prince Shangshan?",
    "What explains the attackers’ unnatural ferocity during the caravan assault?"
  ],
  "safe_through": 855,
  "temporary_decisions": [
    "Render 혈혼고 as “Blood Soul Gu.”",
    "Render 독혈지 as “Poisonblood Grounds.”",
    "Render 대국 as “Great Nation.”",
    "Render 금의위 as “Embroidered Uniform Guard.”",
    "Render 옥화산 as “Yuhua Mountain.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 주화란    | **Ju Hwaran**      |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 암천     | **Dark Heaven**                  |
| 사천당가   | **Sichuan Tang Clan**            |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 상태               | **Status**                     |
| 체력               | **Stamina**                    |
| 매력               | **Charm**                      |
| 사천     | **Sichuan**            |
| 안휘     | **Anhui**              |
| 노부      | **this old man / I**                                            |
| 귀가      | **your family**                                                 |
| 소협      | **Young Hero**                                                  |
| 소저      | **Young Lady**                                                  |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 선황 | **the late Emperor** | The former Emperor whom Hong Jin served. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 당가 | **Tang Family** | Short form for the Sichuan Tang Clan when distinguished from 사천당문. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 강소 | **Jiangsu** | Province at the eastern end of the Yangtze route. |
| 홍건 | **Red Turbans** | Historical red-turbaned bandits described as widespread raiders. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 홍진 | 주표 | servant and political aide to prince | His Highness | formal-deferential | Uses the elongated royal call 전하 while summoning Zhu Bao. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 주화란 | 조장님 | pavilion member to squad leader | Captain | familiar and deferential | Hwaran asks Captain where he is going before he confronts the mistreatment. |
| 혁무진 | 주화란 | Fire Dragon Pavilion member to fellow member | Young Lady Ju | polite and deferential | Mujin addresses Hwaran as 주 소저 while asking her to call a physician. |
| 주화란 | 적천강 | younger ally to legendary martial master | Great Hero Jeok | formal and deferential | Ju Hwaran addresses Jeok as 적 대협 while asking whether he is all right. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 855
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 853
- **Aliases:** None
- **Role:** Level 22 Deputy Military Commissioner of Shanxi Province and a eunuch who has served beside Prince Shangshan since infancy; he formerly served the late Emperor, who ordered him to assist Prince Shangshan, and came to the frontier in something like exile; he remains the power behind the Shanxi Provincial Office, manages the City Lord's luncheon, and redirects a planned Shaanxi–Shanxi trade project toward Huashan.
- **Personality:** Composed and socially deft, Hong Jin is considerate toward those beneath him and dislikes excessive deference, which recalls his impoverished past.
- **Voice:** Delicate, complimentary, and conversational.
- **Relationships:** Hong Jin has served Prince Shangshan since infancy and is devoted to protecting him; he trusts Jin Taekyung as the person best able to keep the prince safe.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 855
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 855
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts his publicly acknowledged Disciple and intended heir Jin Taekyung, warmly regards Ju Hwaran and hopes she and Jin grow closer, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 855
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, and filial; remains controlled under pressure but has grown more assertive and openly impatient after the hardships she has endured.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 853
- **Aliases:** None
- **Role:** The City Lord and a member of the imperial family; ten-year-old Prince Shangshan, whose personal name is Zhu Bao, is an exceptionally skilled young swordsman who has trained daily for three years.
- **Personality:** Earnest, admiring, and eager to emulate Jin Taekyung; despite his royal dignity, he shows openly childlike enthusiasm for martial arts and Taekyung's reputation.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor's only younger full brother, and his token commands immediate deference from distant imperial relatives such as Ju Wongong; he admires Jin Taekyung and seeks to emulate him.

## Korean source

```text
＃856화



사천당가를 떠난 직후, 칠 주야라는 시간이 눈 깜짝할 사이에 흘러갔다.

마치 보보(步步)마다 뒤바뀌는 주위의 풍경과 사람들처럼.

하지만 안심하기에는 일렀다.

남은 시간을 이틀로 줄여 보겠다는 내 호언장담과 달리 현실은 냉정했고, 세간을 이목을 피하고자 깊은 곳으로 숨어들어 갈수록 더 많은 시간을 소요할 수밖에 없었다.

“속도를 올려야겠습니다.”

“지금보다 더?”

“네. 생각했던 것 이상이에요.”

“지금 속도를 유지만 한다면 초하루까지는 도착할 수 있다. 이미 무리하고 있는 상황이야.”

“압니다. 그런데 금의위라고 저희와 다를까요?”

“……!”

“이동하고 있는 건 저희만이 아닙니다. 무리해서라도 놈들의 앞을 가로막아야죠.”

내 말이 사실이라는 것을 이미 알고 있던 적천강은 아무 말도 하지 않았다.

정보는 중요하다. 그러나 완벽한 정보는 어디에도 없다.

우리가 어떠한 정보를 입수했다면, 그건 상대도 마찬가지다.

분, 초 단위로 정보를 전달할 수 있는 현대에서도 그러할진대 무림이라면 오죽할까.

어디로 향하건 결국 대국(大國)의 영토다. 사방에 눈과 귀가 깔린 만큼 처음부터 변수는 무궁무진했고, 그 변수를 최소화할 방법은 오직 하나뿐이었다.

최대한 빠르게, 죽어라 달리는 것.

물론 그 과정에는 엄청난 고난과 인내가 필요했다.

보름 남짓한 시간 동안 대륙의 절반을 가로질러야 하는 미친 짓이었으니까.

“조장님, 이러다가 진짜 죽겠습니다.”

“그럼 쉬어야지.”

“정말요?”

“응. 강소성에서.”

“아니, 농담이 아니라 죽는다니까요?”

“무진아. 혁무진.”

“예?”

“우리가 가지 않으면, 무슨 일이 벌어질 것 같냐?”

“…….”

“쉬고 싶으면 쉬어. 이건 비꼬는 것도 아니고 돌려 말하는 것도 아냐. 안 되겠다 싶으면 빠지는 게 서로를 위해서 나아.”

혁무진은 그 후로 아무 말도 하지 않았다.

아니, 녀석을 포함한 모두가 마찬가지였다.

그들은 투정 대신 침묵을 입에 머금은 채 이동을 계속했다.

험준한 산맥을 넘고, 굽이치는 강물을 건넜다.

광활한 대륙은 지방마다 기후도, 지형도 조금씩 달랐다.

호북의 대낮은 용광로처럼 뜨거웠고, 안휘의 밤은 서늘한 칼바람이 휘몰아쳤다.

비바람이 한바탕 스쳐 지나간 어느 날에는 피로를 이기지 못한 이들이 쓰러지기도 했다.

“진 소협, 이번 사안의 중함은 알고 있지만…… 더 이상은 어렵습니다.”

빠르게 지쳐 가는 대원들의 모습을 보다 못한 신의의 한마디에, 나는 짧은 대답을 돌려주었다.

“일각 휴식 후 다시 출발합니다.”

나는 혁무진을, 적천강은 주화란을 등에 업었다.

두 사람 모두 처음에는 거부했지만, 이번만큼은 내 의지가 강경했다. 언뜻 봐도 그들의 상태는 농담으로라도 좋다고 할 수 없을 정도였으니까.

‘공력과 체력이 바닥날 때까지 이동했으니, 당연한 일이지.’

그리고 화왕(火王)이라는 별호와는 달리 냉소적인 성정을 지닌 적천강은, 웬일인지 신의의 치료에도 전신이 펄펄 끓어오르는 주화란을 안쓰럽게 생각했다.

“이럴 필요까지 있겠느냐? 차라리…….”

“저희 둘만 따로 이동하자고 얘기하실 거라면, 지금 미리 거절하겠습니다.”

“어째서냐?”

“함께 해내야 하니까요. 이 정도도 못 버틴다면 결국 머지않아 죽을 겁니다.”

나를 위해서가 아니라, 우리 모두를 위해서다.

전쟁은 이미 시작됐고 사방에는 거센 환란(患亂)이 도사리고 있다.

그 누구도 겪어 보지 못한 참혹하고 거대한 재앙들.

암천과의 전쟁에서 살아남기 위해서는 나뿐만이 아니라 함께 강해져야 한다. 수없이 두드리고 담금질한 날붙이는 바위와 부딪혀도 부러지지 않으니까.

그리고 적천강은 누구보다 내가 한 말의 의미를 잘 알고 있는 극소수의 인물 중 하나였다.

그 역시 뼈를 깎는 노력과 고난으로 거듭난, 그리하여 마침내 자신의 앞을 가로막는 수많은 바위를 베어 버린 명검(名劍)이었으니.

“함께 해내야 한다…….”

앞서 내게 들은 말을 천천히 뇌까린 적천강이 실소를 흘렸다.

“다 컸구나.”

“저야 항상 노야보다 컸죠. 예전이나, 지금이나.”

내 대답을 들은 적천강이 고개를 절레절레 내저었다.

“넌 역시 시건방진 놈이다. 예전이나, 지금이나.”

“그게 또 매력 아닙니까.”

“하지만 아무리 생각해도 이건 과하다. 이 피도 눈물도 없는 녀석 같으니.”

“주 소저가 원한 겁니다. 저는 그 뜻을 존중했고요. 정말 죽을 정도로 아팠다면 오히려 제 쪽에서 말렸을 겁니다.”

“집어치워라. 여하튼 네 녀석의 생각이 옳을지는 몰라도, 하나는 확신할 수 있을 것 같다.”

“예? 뭐가요?”

“노부가 장담컨대, 네놈은 죽을 때까지 짝을 찾을 수 없을 것이다.”

“아니, 갑자기 그 얘기가 왜 나와요?”

“됐다. 주둥이 놀릴 힘이 있으면 한 걸음이라도 더 걸어라.”

뜬금없이 극딜을 넣고 바람처럼 달려가는 적천강의 뒷모습을 바라보던 나는, 문득 시야가 서서히 환해지는 것을 느끼며 고개를 들었다.

‘이건.’

공력을 끌어 올려 땅을 박찼다. 가장 가까운 거목(巨木)의 나뭇가지를 밟으며 나무 위로 솟구치자, 비로소 저 멀리 번져 오는 빛이 보였다.

그건 서광(曙光)이었다.

사천당가를 떠난 그 날로부터 열하루 동안 매일 보았던, 열한 번째 서광.

하지만 새로운 아침을 알리는 저 빛이 오늘따라 유난히도 반갑게 느껴지는 이유는, 사방을 메운 풀숲과 물줄기 너머로 모습을 드러낸 무언가 때문이었다.

“아.”

귓가를 울리는 희미한 탄성.

등에 업혀 있던 혁무진이 반쯤 죽어 가는 목소리로 물었다.

“조, 조장님. 여기 어디예요? 저게 뭡니까?”

나는 소리 내어 웃었다.

그리고 나무 아래의 모두가 들을 수 있도록, 큰 목소리로 대답했다.

“강소성(江蘇省).”



* * *



제국(帝國)은 장엄하며 위대하다.

그러나 결코 영원할 수는 없다.

대륙이 간직한 역사에 비하면 그리 오래되지 않은 과거, 초원의 유목민들이 세운 제국 역시 마찬가지였다.

그들은 한 사람, 한 사람이 뛰어난 전사이자 목동이었고 하늘과 땅을 숭배하며 매와 말의 절친한 벗이었으나 훌륭한 경영자는 아니었다.

불과 일백여 년.

초원의 침략자들이 세운 거대한 제국은 그렇게 몰락했다.

영웅이자 악마. 끝끝내 신화로 남은 위대한 정복자도, 내실을 다지고 신하와 백성들을 다독이던 명군(名君)도 있었다.

그러나 그 무대의 끝에는 끔찍한 기근(飢饉)과 부패, 그리고 무수한 붉은 깃발만이 나부낄 뿐이었다.

‘굶주린 자들이여, 봉기(蜂起)하라!’

전란의 시대가 시작되었다. 피처럼 붉은 깃발과 두건을 두른 이들이 사방에서 들불처럼 일어나 대륙을 휩쓸었다.

세상은 그들을 홍건적(紅巾賊)이라 칭했고, 그들은 스스로를 홍건군(紅巾軍)이라 불러 주길 원했으나 실상은 전자에 가까웠다.

그들은 도적이었다.

주린 배를 채워 줄 곡식과 재물을 훔치는 도적.

그리고 이 나라의 강산마저 훔치고자 하는 도적.

‘왕후장상(王侯將相)의 씨가 어찌 따로 있단 말이냐!’

겉이 비루하다 한들, 그 속살마저 작고 초라하랴.

좁쌀 한 줌을 훔치면 도적이지만, 대륙을 훔친다면 천자(天子)가 된다.

길었던 전란의 끄트머리에서, 마침내 천하를 거머쥔 어느 영웅이 바로 그러했듯이.

‘왕이시여, 부디 제위(帝位)에 오르소서!’

그렇게 새로운 하늘이 열렸다.

가난한 농부의 아들로 태어나 탁발승으로 천하를 떠돌던 이는 온 천하를 손에 넣었고, 수많은 신하와 백성을 거느린 만인지상(萬人之上)의 자리에 올랐다.

그러나 그로부터 긴 세월이 흐르고, 그의 피를 이은 자식 중 하나가 황위를 이어받은 후에도 바뀌는 것은 아무것도 없었다.

적어도 강소성(江蘇省)에 살아가던 어느 소년에게는 그랬다.

‘야, 이 거지새끼야!’

거지새끼.

살면서 가장 많이 들어 본 말 중 하나다. 수십여 년이 흐른 지금에도 그 순간만큼은 또렷하게 뇌리에 박혀 있었다.

지금처럼 악몽을 꿀 때마다 빠지지 않고 등장할 만큼.

“……아.”

불현듯 잠에서 깨어난 홍진은 눈을 깜빡였다. 그리고 말없이 자신을 바라보고 있던 한 소년을 향해 공손히 고개를 숙였다.

“감히 전하의 앞에서 미몽(迷夢)을 꾸었나이다. 부디 신의 불충을 용서하소서.”

소년, 상산왕(上山王) 주표가 대답했다.

“용서라니, 당치도 않다.”

아직 십 대 중반도 되지 않은 소년이라고는 믿을 수 없을 만큼 침착한 태도와 위엄 어린 음성.

나이에 비해 훨씬 크고 균형 잡힌 체구를 지닌 어린 왕은, 자신의 신하를 향해 말을 이었다.

“오히려 사과해야 할 것은 그대가 아닌 과인이다. 충성스러운 신하를 이토록 고생시키고 있으니.”

“고생이라니요. 감히 바라옵건대 말씀을 거둬 주십시오.”

“아니다. 이 모든 것은 과인의 부덕함 탓이니라.”

“전하…….”

“허나 괜한 걱정은 접어 두거라. 그대가 우려하는 일은 절대로 일어나지 않을 테니까.”

홍진은 대답 대신 두 손을 모아 길게 읍했다.

하지만 천천히 이동 중인 마차의 바닥을 바라보는 그의 눈에는, 어린 왕을 향한 대견함과 씁쓸함이 뒤섞여 있었다.

‘소신 역시 간절히 그러길 바라옵니다만…… 전하의 형님께서는 다르실 것입니다.’

홍진은 가슴 깊숙한 곳에서 치미는 목소리를 애써 억눌렀다.

그의 주군인 상산왕은 어릴 적부터 총명하고 성숙한 소년이었지만, 세상의 비정함을 알기에는 너무나도 어렸다.

마치 죄인이 압송당하듯 금의위에 둘러싸여 황도(皇道)로 향하는 지금에도 자신의 하나뿐인 친혈육을 굳게 믿고 있었으니.

그러나 홍진은 아니었다.

‘이미 천하를 손에 넣었거늘 여기서 더 무엇을 얻고자 하십니까, 황상.’

누구에게도 닿지 않을 물음과 함께, 홍진은 지그시 눈을 감았다.

캄캄한 어둠 속에서 떠오른다. 들린다.

피가 마르지 않던 그 시절이. 수백이 사지가 뜯겨 죽고, 수천이 효수되었던 숙청의 나날들이.

그리고 선황(先皇)의 마지막 유언이.



‘표(豹). 그 아이를 부탁한다.’



쿵.

마차로 전해지는 작은 진동에, 홍진은 감았던 눈을 떴다. 고개를 돌려 옆을 바라보자 창틈으로 누군가의 옆모습이 보였다.

“무슨 일이냐.”

홍진의 나직한 물음에, 금의위(錦衣衛)라는 이름과는 어울리지 않게 허름한 무복을 걸친 상대가 대답했다.

“알 것 없소.”

별다른 감정조차 느껴지지 않는 무뚝뚝한 목소리. 그러나 홍진은 그 안에 스며 있는 서늘한 칼날을 느꼈다.

낯설면서도 익숙한 감각.

지금의 금의위가 그랬듯이, 과거 선황의 손발 노릇을 했던 홍진은 십여 년간 잊고 있던 익숙한 느낌을 떠올렸다.

더불어 일말의 의아함도 함께.

‘왜 멈춘 거지?’

이 은밀한 행렬은 이미 강소성에 접어들었고, 금의위로서는 멈출 이유가 없었다. 그들은 황명(皇命)을 수행하기 위해서라면 목숨까지 바치는 이들이니까.

‘뭔가 있다.’

홍진은 조용히 촉각을 곤두세웠다. 비록 일가(一家)를 이룰 정도는 아니라고는 하나 그 역시 무공을 익힌 몸.

다행히 전음을 사용할 만큼의 사안이 아니라고 판단했는지, 금의위들이 나누는 대화 소리가 창문 틈새로 흘러 들어왔다.

“척후조가 확인한 바에 따르면 삼백여 장 앞에 신원불명의 시신이…….”

“혹시 함정일지 몰라 가까이 접근하지는 않았지만 별다른 상흔은 보이지 않아…….”

“……병력 분산을 노린 것일 수도 있으니 계속해서 이동한다. 마차에서 떨어지지 마라.”

두런두런 들려오던 대화가 어느 순간 뚝 끊기고, 잠시 멈췄던 마차가 다시 나아가기 시작했다.

다그닥. 다그닥.

조용히 울려 퍼지는 말발굽 소리를 들으며 홍진은 생각했다.

‘신원불명의 시신이라.’

그리 이상한 일은 아니다. 대륙은 광활하고 유리걸식하는 이들은 어디에나 있었으니까. 설령 황도와 인접한 강소성이라 해도 예외는 아니었다.

하지만 어째서일까.

지금 이 순간, 문득 한 사람의 이름이 뇌리를 스치는 이유는.

동시에 왠지 모르게 가슴 한구석에서 솟구치는 이 기대감은.

‘설마.’

홍진이 불현듯 고개를 든 그때였다.

“시체……라고 하지 않았나?”

금의위 중 누군가의 중얼거림과 함께, 홍진이 어디선가 들어 본 익숙한 목소리가 홍진의 귓가에 닿았다.

“조장님. 저 맹세코 안 졸았습니다. 그냥 잠깐 누워만 있었……. 헉, 누구세요?”

그 순간, 홍진은 어린 왕이 앞에 있다는 사실도 잠시 잊은 채 크게 소리 내어 웃었다.
```

## Final English reading copy

```markdown
# Chapter 856

Seven days and nights passed in the blink of an eye after we left the Sichuan Tang Clan.

The scenery and the people around us changed with every step.

But it was too soon to relax.

Despite my boast that we’d cut the remaining time down to two days, reality was cold. The farther we ventured into the wilderness to avoid drawing attention, the more time we inevitably lost.

“We’ll have to pick up the pace.”

“Even faster than this?”

“Yes. Faster than I thought we’d have to.”

“If we keep up this pace, we can arrive by the first of the month. We’re already pushing ourselves too hard.”

“I know. But do you think the Embroidered Uniform Guard is any different from us?”

“……!”

“We’re not the only ones on the move. We have to push ourselves and get in their way before they reach their destination.”

Jeok Cheongang already knew I was right, so he said nothing.

Information was important. But perfect information didn’t exist.

If we’d picked up some information, then so had our opponents.

That was true even in the modern world, where information could be relayed by the minute or even the second. How much more so in Murim?

Wherever they were headed, they were still within the Great Nation’s territory. Eyes and ears were everywhere, and there had been countless variables from the start. There was only one way to minimize them.

Move as fast as possible. Run ourselves into the ground.

Of course, that meant enduring tremendous hardship.

It was insane to try to cross half the continent in a little over half a month.

“Captain, we’re actually going to die at this rate.”

“Then we should rest.”

“Really?”

“Sure. In Jiangsu.”

“No, I’m not joking. I mean we’re going to die!”

“Mujin. Hyuk Mujin.”

“Yes?”

“If we don’t go, what do you think will happen?”

“……”

“If you want to rest, rest. I’m not being sarcastic or trying to hint at anything. If you think you can’t go on, drop out. It’ll be better for all of us.”

Hyuk Mujin said nothing after that.

No—neither did anyone else.

Instead of complaining, they held their tongues and kept moving.

We crossed rugged mountain ranges and forded winding rivers.

The vast continent’s climate and terrain varied a little from one region to the next.

The midday heat in Hubei was like a blast furnace, while the night wind in Anhui cut like a cold blade.

One day, after a storm swept through, some of the party finally collapsed, unable to overcome their exhaustion.

“Young Hero Jin, I understand how important this matter is, but… we can’t go on any longer.”

At the Divine Physician’s words, spoken after watching the members grow exhausted by the day, I gave him a short reply.

“We’ll set out again after fifteen minutes.”

I carried Hyuk Mujin on my back, and Jeok Cheongang did the same with Ju Hwaran.

Both of them refused at first, but this time I wouldn’t budge. It was obvious at a glance that neither of them was in any condition to be called well, even as a joke.

*Of course they’re exhausted. We’ve been moving until our internal energy and stamina were completely spent.*

And though his title was the Fire King, Jeok Cheongang was a man of cold disposition. For some reason, he felt sorry for Ju Hwaran, who was burning up from head to toe despite the Divine Physician’s treatment.

“Was this really necessary? We could—”

“If you’re about to suggest the two of us travel separately, I’ll refuse right now.”

“Why?”

“Because we have to make it through this together. If we can’t endure even this much, we’ll die before long anyway.”

This wasn’t for my sake. It was for all of us.

The war had already begun, and upheaval lurked all around us.

Catastrophes so terrible and vast that no one had ever experienced anything like them.

To survive the war against Dark Heaven, all of us had to grow stronger—not just me. A blade hammered and tempered countless times won’t break even when it strikes a rock.

And Jeok Cheongang was one of the very few people who understood the meaning of my words better than anyone.

He, too, had been remade through bone-deep effort and hardship. In the end, he’d become a peerless blade that cut through countless rocks blocking his way.

“We have to make it through this together…”

Jeok Cheongang slowly repeated the words he’d heard from me, then gave a dry chuckle.

“You’ve grown up.”

“I’ve always been taller than you, Old Master. Then and now.”

Jeok Cheongang shook his head at my answer.

“You’re still an arrogant brat. Then and now.”

“Isn’t that part of my charm?”

“But no matter how I look at it, this is too much. You heartless little bastard.”

“Miss Ju wanted it. I respected her wishes. If she were in enough pain to actually die, I’d have stopped her myself.”

“Cut the crap. Anyway, your idea might be right, but I can be sure of one thing.”

“Yes? What?”

“This old man guarantees you’ll never find a partner before you die.”

“Hey, why are you suddenly bringing that up?”

“Enough. If you have the energy to flap your gums, take one more step.”

Jeok Cheongang suddenly landed a brutal verbal blow, then darted away like the wind. As I watched his back, I noticed my view gradually growing brighter and raised my head.

*This is…*

I gathered my internal energy and pushed off the ground. Stepping onto the branch of the nearest great tree, I sprang up into its crown. At last, I saw a glow spreading in the distance.

It was the dawn light.

The eleventh dawn I’d seen, one each day since we’d left the Sichuan Tang Clan.

But the reason that light heralding a new morning felt especially welcome today was something coming into view beyond the grass and streams stretching all around us.

“Ah.”

A faint exclamation rang in my ears.

Hyuk Mujin, slung over my back, asked in a voice that sounded half dead,

“C-Captain. Where are we? What’s that?”

I laughed out loud.

Then, loud enough for everyone below the tree to hear, I answered:

“Jiangsu.”

* * *

Empires are majestic and great.

But they can never last forever.

Not so long ago, by the continent’s standards, the empire founded by the nomads of the grasslands had been no different.

Each of them was a fine warrior and herdsman. They worshiped heaven and earth and were close companions to hawks and horses, but they were not good rulers.

A little over a hundred years.

That was all it took for the vast empire founded by the invaders from the grasslands to fall.

There had been a great conqueror who was both hero and devil, destined to remain a legend to the very end. There had also been a wise ruler who strengthened the empire from within and cared for his subjects and people.

But when that age drew to a close, all that remained were horrific famine, corruption, and countless red flags fluttering in the wind.

*“You who hunger, rise up!”*

An age of war began. Figures wearing blood-red flags and headscarves rose like wildfires from every direction and swept across the continent.

The world called them the Red Turban Bandits. They wanted to be called the Red Turban Army, but in truth, the former name suited them better.

They were bandits.

Bandits who stole grain and treasure to fill their empty stomachs.

Bandits who wanted to steal this nation’s mountains and rivers, too.

*“How can the blood of kings, nobles, generals, and ministers be any different from anyone else’s?”*

Even if they were shabby on the outside, did that mean their insides had to be small and shabby, too?

Steal a handful of millet and you’re a bandit. Steal a continent and you become the Son of Heaven.

Just as one hero had done at the end of that long age of war, at last grasping all under heaven.

*“Your Majesty, please ascend the throne!”*

And so a new heaven opened.

Born the son of a poor farmer, he had wandered the land as a mendicant monk. Now he held all under heaven in his hands and occupied the highest position of all, with countless subjects and commoners beneath him.

But even after many years had passed and one of his own children inherited the throne, nothing changed.

At least, not for one boy living in Jiangsu.

*“Hey, you filthy beggar!”*

Filthy beggar.

It was one of the things he’d heard most often in his life. Even now, decades later, the memory was etched clearly into his mind.

So clearly that it appeared without fail whenever he had a nightmare like this one.

“……Ah.”

Hong Jin abruptly woke from his sleep and blinked. Then he respectfully bowed his head to the boy watching him in silence.

“I dared to fall into a dream before Your Highness. Please forgive your unfaithful servant.”

“Forgive you? There’s no need.”

The boy, Prince Shangshan Zhu Bao, replied.

His composure and dignified voice were hard to believe in someone who wasn’t even midway through his teens.

The young prince, taller and more solidly built than most boys his age, continued speaking to his servant.

“If anyone should apologize, it’s me, not you. I’ve put a loyal subject through so much hardship.”

“Hardship? I beg Your Highness to take back those words.”

“No. This is all because of my own shortcomings.”

“Your Highness…”

“But set aside any needless worry. What you’re afraid of will never happen.”

Hong Jin answered by bringing his hands together and bowing deeply.

But as he stared at the floor of the slowly moving carriage, his gaze held both pride in the young prince and a hint of bitterness.

*I earnestly pray it will be so as well, Your Highness… But your elder brother will not see it that way.*

Hong Jin forced down the voice rising deep in his heart.

His master, Prince Shangshan, had been an intelligent, mature boy from a young age. But he was far too young to understand the cruelty of the world.

Even now, as they traveled toward the imperial capital surrounded by the Embroidered Uniform Guard as if he were a prisoner being taken away, he still had unwavering faith in his only blood relative.

But Hong Jin did not.

*You already have all under heaven. What more could you possibly want, Your Majesty?*

With that question, which would reach no one, Hong Jin closed his eyes.

In the pitch-darkness, memories surfaced. Sounds returned.

Those days when the blood never dried. Days of purges when hundreds had their limbs torn off and died, and thousands were beheaded and displayed.

And the late Emperor’s final words.

*“Bao. I entrust that child to you.”*

Thump.

Hong Jin opened his eyes at a small jolt that traveled through the carriage. He turned to look beside him and saw someone’s profile through a narrow gap in the window.

“What’s going on?”

At Hong Jin’s low question, the man beside the carriage, dressed in shabby martial robes ill-suited to the name Embroidered Uniform Guard, replied,

“None of your business.”

His voice was blunt, without even the hint of emotion. But Hong Jin sensed the cold blade lurking beneath it.

A feeling both unfamiliar and familiar.

Just like the Embroidered Uniform Guard now, Hong Jin had once served as the late Emperor’s hands and feet. The sensation brought back something familiar that he hadn’t felt in over a decade.

Along with a hint of puzzlement.

*Why have we stopped?*

This covert procession had already entered Jiangsu, and the Embroidered Uniform Guard had no reason to stop. They were people who would gladly give their lives to carry out the Emperor’s orders.

*Something’s going on.*

Hong Jin quietly sharpened his senses. He might not be skilled enough to have established his own school, but he had still learned martial arts.

Thankfully, the guards seemed to judge that the matter wasn’t serious enough to require Sound Transmission. Their conversation drifted through the gap in the window.

“According to the scouts, there’s an unidentified corpse about three hundred zhang ahead…”

“We didn’t approach in case it was a trap, but there don’t seem to be any obvious wounds…”

“It could be an attempt to split up our forces. We’ll keep moving. Stay close to the carriage.”

The murmuring conversation abruptly stopped. After a brief pause, the carriage started moving again.

Clip-clop. Clip-clop.

As he listened to the quiet sound of hooves, Hong Jin thought,

*An unidentified corpse.*

It wasn’t that strange. The continent was vast, and there were people begging their way across it everywhere. Not even Jiangsu, so close to the imperial capital, was an exception.

But why?

Why did one man’s name suddenly come to mind at this very moment?

And why did an inexplicable hope well up in one corner of his heart?

*Could it be…*

Hong Jin had just lifted his head when—

“Didn’t you say it was a corpse…?”

With one of the Embroidered Uniform Guard’s men murmuring the words, a familiar voice Hong Jin had heard somewhere reached his ears.

“Captain. I swear I wasn’t dozing off. I was just lying down for a second… Huh? Who are you?”

At that moment, Hong Jin burst out laughing, briefly forgetting that the young prince was right in front of him.
```
