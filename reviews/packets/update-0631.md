<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0631.txt",
      "sha256": "f18748229c1b9bd572f48a2c9e57f9aa196953dd2e0669eaaf8b4c00729989b5",
      "bytes": 13089
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "52ebe968762a48dea0457d5193ad99dbb41b4236fe07f016f5153e5011abe124",
      "bytes": 2360
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d0d5aa4142927c8a7e94eda12df80b7b7169af776c43a3937d11384348b44a40",
      "bytes": 193947
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "74538bfbc22cb1ca836397cdb567242d3dfd8830db9c343d5174a813dabc7ef4",
      "bytes": 735
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "5555e734e188d0b85a4e7a7cfec3c900daa8a87c292daf286f4ddf9236e00c1d",
      "bytes": 553
    },
    {
      "path": "characters/Heugung.md",
      "sha256": "2aa993caca8472aa3e9841f3d9d3153c8661c29e1a933211a93565e7bbd64d27",
      "bytes": 623
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "8c015cecec084e85cd4fda59b991d1d983528ad42d828ad7335c2669ae554333",
      "bytes": 1206
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "7064d9179d1201fd55592a3d6cd4aa74163c39fa1a90343aab889144749f4495",
      "bytes": 1702
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "80fa0908c14ef28d5ca4ec6d9e1284a3b4d12cc804d90b61751628d89663e6f6",
      "bytes": 1043
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "a935e784d0d7a95190b0dda991f75034ffdc1bbc4b503eb29d037f199b6bca43",
      "bytes": 871
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "a1d7815b697ed9215983f79d576194972a5763ffe9190b1ec2f38b2cb6d50169",
      "bytes": 542
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ebdc513f66332be7cdcfe203ceaa15eb6e3a3f96d0abb6d6c0706a6705c77a6e",
      "bytes": 200183
    }
  ],
  "estimated_tokens": 11412
}
-->

# Durable State Update — Chapter 631

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 631. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 631. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
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
  "chapter": 631,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 631,
    "continuity_sources": [631],
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
    "The Fire Dragon Pavilion is staying in temporary lodging within the Nanman Beast Palace after being welcomed by Yayul Cheok.",
    "Nanman's first tribal council opposed joining the Murim Alliance; all thirty-two tribes will meet in three days for a second council.",
    "Jin Taekyung is in Nanman to contain a spreading crisis and is attempting to assess whether Nanman can be persuaded to join the Murim Alliance.",
    "Jin Taekyung is using a tiger mask and has now been privately identified by Yohi.",
    "Baeksang is the great chieftain of the Bai people and Yayul Cheok's sworn younger brother; he opposes Nanman joining the Murim Alliance.",
    "The Miao, Bai, Yi, and Yao peoples are Nanman's four great tribes.",
    "Yohi is the female great chieftain of the Yao people and is pursuing Yao dominance over the four great tribes.",
    "Heugung is the great chieftain of the Yi people and is easily manipulated by Yohi and Baeksang.",
    "Yohi says the great chieftains generally oppose joining the Murim Alliance because they fear weakening their tribes within Nanman.",
    "Jin has confirmed through Qi Sense that Yohi is fundamentally different from the Southern Heaven Demon Empress.",
    "Baeksang has arrived at Yohi's tent after her private conversation with Jin."
  ],
  "continuity_sources": [
    630,
    629
  ],
  "open_questions": [
    "Why does Baeksang oppose joining the Murim Alliance despite his lifelong bond with Yayul Cheok and their shared service in the Great Faction War?",
    "What will Baeksang say or do after finding Yohi with Jin Taekyung?",
    "Can Jin persuade Nanman to join the Murim Alliance despite the great chieftains' opposition?",
    "Will the remaining tribes follow Baeksang and the other opposing great chieftains at the council in three days?",
    "What does Yohi ultimately intend to gain from identifying and questioning Jin?"
  ],
  "safe_through": 630,
  "temporary_decisions": [
    "Use Baeksang for 백상 and do not treat White Elephant as a separate alias.",
    "Use sworn younger brother for 불알 동생 in the relationship between Yayul Cheok and Baeksang.",
    "Use Jiang Taigong for 강태공 and Jindro for 진드로.",
    "Render 황개 as Hwang Gae and 똥개 as Ddong Gae.",
    "Render 입맹 as joining the alliance."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 진백양    | **Jin Baekyang**   |
| 적천강    | **Jeok Cheongang** |
| 주화란    | **Ju Hwaran**      |
| 화양검    | **Blade of Flowers**          | Jin Baekyang   |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 태원진가   | **Jin Family of Taiyuan**        |
| 열화문    | **Fire Gate Clan**               |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 중원     | **Central Plains**                               |                                                       |
| 가주     | **Family Head**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 제자     | **Disciple**                                 |
| 상태               | **Status**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 정마대전   | **Great Faction War**         |
| 소협      | **Young Hero**                                                  |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 흑웅 | **Heugung** | Great chieftain of the Yi people; his name literally means Black Bear. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 수문위사 | **gate guard** | Jin Family guard stationed at the gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 백족 | **Bai people** | Ethnic group encountered in Yeongin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 야율목 | 백상 | nephew_to_father's_sworn_younger_brother | Uncle Baeksang | ceremonial and deferential | Yayul Mok formally greets Baeksang as he arrives at the stone door. |
| 백상 | 야율목 | father's_sworn_brother_to_nephew | you | cold and formal | Baeksang questions Yayul Mok about his return, the pasture fire, and the Palace Lord's whereabouts. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 요희 | 흑웅 | Yao great chieftain to Yi great chieftain | big brother | seductive and falsely affectionate | Uses 오라버니 to flatter and manipulate Heugung. |
| 흑웅 | 요희 | Yi great chieftain to Yao great chieftain | my dear | adoring and deferential | Responds to Yohi's manipulation with open infatuation. |
| 백상 | 요희 | Bai great chieftain to Yao great chieftain | Yohi | cold and formal | Calls to Yohi from outside the tent at the chapter's end. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 630
- **Aliases:** None
- **Role:** Baeksang is the middle-aged great chieftain of the Bai people, one of Nanman's four most powerful great tribes.
- **Personality:** Cold, rigid, meticulous, and politically resolute, with a deep but guarded attachment to his sworn elder brother.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion and Yayul Mok's sworn uncle; he lost a beloved son in the Great Faction War, opposes the Nanman Beast Palace joining the Murim Alliance, and helps Yohi keep Heugung under control.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 630
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Heugung.md

# Heugung (흑웅)

- **Safe through:** Chapter 630
- **Aliases:** None
- **Role:** Heugung is the middle-aged great chieftain of the Yi people, one of Nanman's four great tribes.
- **Personality:** Heugung is foolish, easily flattered, and politically dependent on stronger personalities despite leading a powerful tribe.
- **Voice:** Heugung speaks with warm enthusiasm and exaggerated devotion toward Yohi.
- **Relationships:** Yohi and Baeksang keep Heugung under their control, while Heugung responds to Yohi's manipulation with apparent infatuation.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 627
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and a member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 627
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 630
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, a member of the Fire Dragon Pavilion, an experienced Nanman escort guide with route knowledge from the Escort King's records, and someone who can understand the Miao and Bai languages.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 630
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, a spear-wielding warrior who rides a white tiger, and a halting but capable speaker of Han Chinese.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King and Yayul Mok's father; Yayul Mok is his only surviving son after three older siblings died in the Great Faction War, Baeksang is his father's sworn younger brother, and his white tiger is a long-bonded companion.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 630
- **Aliases:** None
- **Role:** Yohi is the female great chieftain of the Yao people, one of Nanman's four great tribes.
- **Personality:** Yohi's public presence is charismatic and captivating, drawing widespread admiration and affection.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people, seeks to unite Nanman's four great tribes under Yao leadership, and manipulates Heugung alongside Baeksang.

## Korean source

```text
＃631화



그런 느낌을 받을 때가 있다.

눈만 마주쳤음에도 상대가 나를 싫어하는 것 같은 느낌. 도무지 친해지려야 친해질 수 없을 것 같은 느낌.

백족의 대족장, 백상과의 두 번째 만남이 그랬다.

“넌…….”

가면으로 얼굴을 가린 상태임에도 백상은 나를 정확히 알아봤다. 하긴, 그의 무위를 생각하면 그리 놀랄 만한 일은 아니었다.

‘최소 초절정 초입.’

그것이 내가 짐작하는 백상의 무위였다.

초절정 고수는 중원에서도 절대 쉽게 찾아볼 수 없는 수준의 고수. 조잡한 호랑이 가면 따위로 얼굴을 가렸다고 해서 못 알아보는 게 더 이상한 거다.

어느 정도 경지에 오른 무인들은 상대를 기도(氣度)로 판별하기 마련이니까.

하지만 중요한 건 백상이 나를 한눈에 알아봤다는 것이 아니라, 조금도 반가워하지 않았다는 거다.

“불청객이 있었군.”

선객도 아니고 불청객이라. 초면에 이랬다면 내 여린 마음에 스크래치가 났겠지만, 사전에 여러 정보를 들은 후라 비교적 담담하다.

나는 뒤통수를 긁적이며 대답했다.

“입이 비뚤어져도 말을 바로 하랬다고, 있는 사실 그대로를 말씀드리자면 제가 불청객은 아니죠. 엄연히 초대받고 온 거니까.”

“초대?”

자연스럽게 옮겨 가는 시선. 백상과 눈이 마주친 요희가 싱긋 웃으며 입을 열었다.

“사실이에요. 제가 불렀으니까.”

아름다운 여인의 미소는 대부분의 경우에서 큰 효력을 발휘하는 법이지만, 적어도 백상은 그런 부류가 아니었다.

“한족과 결탁할 셈이냐?”

더욱 냉담해진 목소리에 요희가 과장된 동작으로 어깨를 으쓱했다.

“결탁이라니, 약간 호기심이 생겼을 뿐이랍니다. 처음부터 단둘이서 만난 것도 아니었고요.”

“하지만 흑웅을 내보내고 무슨 이야기를 나누었는지는, 너희 둘과 하늘만이 알겠지.”

“괜한 우려는 접어 두세요. 그날 했던 약조는 잊지 않았으니.”

그날의 약조가 무엇인지는 모르겠지만, 듣는 것만으로도 수상한 냄새가 풀풀 풍긴다. 백상의 눈빛이 더욱 깊게 가라앉았다.

“한족 놈 앞에서 쓸데없는 말을 하는구나, 요희.”

쏴아아악!

백상의 전신으로부터 보이지 않는 기파(氣波)가 흘러나와 막사 내부를 휘감았다.

삽시간에 무거워진 공기 속. 사방에서 압박해 오는 초절정 고수의 기세에 요희의 입가에 걸려 있던 미소가 처음으로 흐릿해진 그때, 내가 불쑥 입을 열었다.

“거, 눈앞에서 뻔히 듣고 있는 한족 놈도 있는데 자꾸 놈놈거리지 맙시다.”

스아아아.

점점 묵직해지던 공기가 순간 힘을 잃는다. 말과 동시에 주위의 기파를 흐트러트린 내 모습에, 백상의 눈썹이 움찔거렸다.

“네놈.”

“진 소협. 진 각주. 열화신룡. 자네. 이 넷 중에 마음에 드는 호칭으로 아무거나 하나 고르시죠. 이쯤 되니까 내가 태원진가 출신인지, 태원놈가 출신인지 헷갈려서.”

“……!”

“말 잘하죠? 압니다. 물론 주둥이로 무림맹 각주가 된 게 아니라는 것 정도는 아실 거라 믿습니다. 만약 그랬으면 제 별호가 열화신룡이 아니라 풍둔 주둥아리룡. 뭐 그런 거였겠죠.”

지금의 내 언행으로 백상은 두 가지를 확실히 깨달았을 것이다. 첫째는 내 무위가 결코 자신의 아래가 아니라는 것.

둘째로는 내가 단순히 새파랗게 젊은 한족이 아니라, 중원 무림이 모여 탄생한 무림맹에서도 각주라는 고위 직책을 갖고 있다는 것.

이 두 가지 중 하나만 사실이라고 해도 어디 가서 무시당할 입장은 아니다.

그런 나를 한동안 말없이 응시하던 백상이 불쑥 입을 열었다.

“다시 보니 열화문의 계승자가 확실하군. 그 앞뒤 가리지 않는 언행이며 행동이, 실로 화왕(火王)의 제자다워.”

“노야, 아니. 제 스승님을 뵌 적이 있습니까?”

“궁주와 나는 늘 함께였다. 말로만 듣던 화왕을 처음 만난 그날에도 마찬가지였고.”

나는 설마 하는 마음으로 물었다.

“어. 그럼 혹시?”

“미처 손 쓸 새도 없이 순식간에 궁주가 쓰러졌고, 그다음은 나였다. 미친 늙은이라고 불렀다는 게 그 이유였지.”

백상이 자신이 입고 있던 백의(白衣)를 살짝 들추자, 옆구리 부분에 남아 있는 화상이 드러났다.

“…….”

아니, 무슨 소고기 등급 매겨놓은 것도 아니고.

‘이 정도면 거의 인증 마크 수준인데.’

수십 년 전 먹었던 따끈따끈한 화왕손파이의 흔적을 내게 보여 준 백상이 차가운 음성으로 말을 이었다.

“이미 오래전의 일이지. 하지만 상처를 볼 때마다 그때가 생각나더군.”

적천강이 예전에 내게 그런 말을 했었다. 무림에서는 은원(恩怨)을 조심하라고.

그런데 지금은 과거 적천강이 쌓은 은원이 부메랑이 되어 내게 돌아오는 중이다.

‘이게 무림식 은원 페이백인가 하는 그거냐.’

순간 할 말을 잃은 나를, 백상은 깊게 가라앉은 시선으로 응시했다.

“네놈이 화왕의 제자건, 무림맹의 각주건 상관없다. 남만은 이미 중원을 위해 많은 피를 흘렸고 궁주의 판단은 틀렸다.”

“…….”

“네놈에게 해 줄 말은 그뿐이니라. 그러니 당장 눈앞에서 사라져라. 내 직접 손을 쓰기 전에.”

백상의 분위기는 흉흉하기 그지없었고, 나는 반박하는 대신 자리에서 일어났다.

그가 두려워서가 아니라, 얻을 것보다 잃을 것이 많아서였다. 지금은 냉정하게 생각해야 할 때다.

저벅.

곧장 막사를 빠져나가려던 나는 문득 걸음을 멈췄다. 언제 다시 만날 수 있을지 모를 백상에게 하고 싶은 말이 생각나서였다.

“중원을 위해 흘린 피가 아닙니다.”

“뭐라?”

“당신들이 흘린 피는 중원이 아니라, 천하를 위해 흘린 겁니다.”

나는 담담하게 한마디를 덧붙였다.

“누군가의 아들도 마찬가지고요.”

화아아악!

거칠면서도 강대한 기파가 돌풍이 되어 휘몰아친다.

숨죽인 채 우리 두 사람의 대화를 지켜보던 요희의 얼굴이 순간 창백해지고, 커다란 막사 전체가 태풍에 휘말린 낙엽처럼 휘청거렸다.

그리고 그 모든 것의 중심에, 분노로 몸을 떨고 있는 한 사람이 있었다.

“놈……!”

화염이 깃든 두 눈동자와 끓어오르는 듯한 음성. 나는 그런 백상의 눈빛을 피하지 않았다.

나를 향해 쏟아지는 그 격렬한 감정 앞에서, 문득 기억 저편에 숨어 있던 누군가를 떠올렸을 뿐이었다.

‘이건.’

모르겠다. 지금 이 짐작이 사실일지, 아니면 단순한 짐작으로 끝날지.

하지만 그전에 내가 건드린 역린(逆鱗)에 대한 예의는 갖춰야 한다.

나는 백상에게 작게 고개를 숙여 보인 뒤 그대로 막사를 빠져나왔다. 그리고 처소로 향하는 내내 분명히 다르지만, 백상과 닮아 있는 한 사람을 떠올렸다.

‘……대장로.’

화양검(火魎劍) 진백양.

산서성이 낳은 정마대전의 영웅 중 한 사람이자, 차남임에도 불구하고 태원진가의 가주가 될 뻔했던 자.

그리고 수십 년의 세월을 암천의 그늘 아래에서 살았던 배신자.

왜 하필 지금, 이 타이밍에 그가 생각났는지는 모르겠다.

하지만, 하지만 어쩌면…….

‘젠장. 모르겠다.’

내가 깊은 한숨을 내쉰 그때, 임시로 배정받은 내궁의 처소 앞에서 어디서 가져왔는지 모를 멧돼지를 통으로 굽고 있는 혁무진이 보였다.

‘짜식. 기특하네.’

심심하면 구박하긴 해도, 태원진가에서부터 산전수전을 함께한 녀석이다.

무엇보다 가문의 수문위사 출신답게, 지금 나와 함께하는 화룡각 대원들 중 대장로에 관하여 가장 잘 아는 사람이기도 했다.

‘어쩌면 괜찮은 조언을 해 줄지도.’

내가 반갑게 손을 흔들려던 그때, 다가오는 나를 발견한 혁무진이 번쩍 손을 치켜들었다.

불그스름하게 달아오른 쇠꼬챙이를 든 채.

“웬 놈이냐?”

“…….”

조언은 니미럴 거.

나는 호랑이 가면을 벗으며 대답했다.

“대가리 박아.”

“엇. 허허. 농담이었습니다.”

“그래. 난 농담 아니니까 대가리 박아.”

“…….”

쩔그럭.

축 늘어진 혁무진의 손아귀에서 쇠꼬챙이가 미끄러졌다.



* * *



눈 깜짝할 사이에 이틀이라는 시간이 흘렀다.

첫 만남 당시 곧 부를 테니 기다리라던 야수묘왕은 그 말이 무색할 만큼 우리를 찾지 않았고, 의외로 야율목의 방문 횟수가 늘었다.

쿵.

입에 물고 있던 멧돼지를 땅에 내던진 백호가 자랑스럽게 가슴을 쭉 앞으로 내민다. 나는 백호의 목덜미를 쓰다듬고 있는 야율목을 향해 물었다.

“이번에는 어디서 잡았냐?”

“서쪽 풀숲.”

무심코 대답한 야율목이 아차 싶은 얼굴로 황급히 말을 이었다.

“……이 아니라, 오는 길에 주운 거다.”

“주운 걸 왜 여기로 가져와?”

“음. 버리기도 뭣해서?”

“근데 주운 것 치고는 목덜미에 이빨 자국이 딱 호랑인데?”

“우리 애는 훈련이 잘 되어 있어서 아무거나 안 문다. 짐승이든 사람이든.”

“…….”

이게 무슨 개소리야.

이 세상에 나쁜 호랑이는 없다. 뭐 그런 건가.

나는 피와 살점이 덕지덕지 묻어 있는 백호의 이빨을 유심히 살피며 중얼거렸다.

“짐승이든 사람이든 안 가리고 한입에 씹어먹게 생겼는데. 편식을 안 한다는 소린가?”

“아무튼 아니다. 다른 호랑이인가 보지.”

“그런 것치고는 이빨 자국이 하난데?”

“그건, 모르겠다. 그냥 길가에서 죽어 있길래 가져온 것뿐이다.”

“아하. 씩씩하고 건강하게 살아가던 멧돼지가 길가에서 자연사했다? 그걸 백호가 앙, 물어서 가져왔고?”

“바로 그거다.”

“…….”

뻔뻔한 것도 정도를 넘으면 대꾸할 여력이 없어진다.

황당한 눈빛으로 야율목을 바라보던 나는, 산더미 같은 덩치의 멧돼지를 보며 한숨을 내쉬었다.

“그나저나 또 멧돼지야?”

“멧돼지인데. 무슨 문제라도 있나?”

“그 또 멧?”

“……한족에게는 양심이라는 것이 없나? 잡아서 가져온 수고를 생각해서라도 닥치고 처먹어라.”

“주웠다며?”

“아. 착각했다. 주운 거다.”

이 새끼도 어지간하네.

나중에야 안 사실이지만, 이틀 전 혁무진이 굽고 있던 고기는 바로 야율목이 가져다준 것이었다.

물론 당시에는 아무도 본 사람이 없었고, 야율목도 자신이 아니라면서 박박 우기긴 했었지만 말이다.

“멧돼지도 하루 이틀이지. 며칠째 이것만 먹으니까 물린다. 물려.”

“그럼 도로 가져가고.”

“무진아. 고기 챙겨라.”

“옙.”

야율목과 백호가 짜게 식은 눈빛으로 나를 바라봤지만, 철면피를 뒤집어쓴 지 오래라 이 정도로는 얼굴이 따끔거리지도 않는다.

요리를 위해 분주하게 움직이는 혁무진의 모습을 보며 작게 혀를 찬 야율목이 내게 시선을 돌렸다.

“하고 있는 일은 잘 되어 가고 있나?”

나는 대답 대신 고개를 가로저었다.

“어떤 성과도 없단 뜻이군.”

“적어도 아직까지는.”

이틀 동안 놀고 있었던 것만은 아니다. 나와 화룡각 대원들은 남만야수궁의 안팎을 살피고 있었다.

주화란과 혁무진으로 하여금 내궁에서 벌어지는 일들을 조사하고, 나는 나머지 인원을 이끌고 인근 지역을 정찰했다.

‘혹시 암천의 흔적을 발견할 수도 있으니까.’

하지만 방금 했던 말처럼, 노력과는 달리 별다른 성과는 없었다.

남만야수궁 인근에 암천의 흔적이 없다는 건 좋은 일이지만, 없는 것이 아니라 찾지 못한 것이라면 이야기는 달라진다.

“일단은 계속해 볼 생각이다. 적어도 부족 대회의 전까지는.”

남만의 모든 부족이 한자리에 모이는 부족 대회의는 바로 내일이다. 그런 내 말에 고개를 끄덕인 야율목이 한껏 낮춘 목소리로 입을 열었다.

“오늘은 미루는 게 좋겠군.”

“미뤄? 왜?”

“내궁(內宮)에서 너희를 불렀다.”
```

## Final English reading copy

```markdown
# Chapter 631

There are times when you get that kind of feeling.

The feeling that someone dislikes you even though all you’ve done is meet their eyes. The feeling that no matter how hard you try, you could never become friends.

My second meeting with Baeksang, the great chieftain of the Bai people, was like that.

“You…”

Even with my face concealed behind a mask, Baeksang knew exactly who I was. Then again, considering his martial prowess, it wasn’t all that surprising.

*At least the early stage of Supreme Peak.*

That was my estimate of Baeksang’s level.

A Supreme Peak master was someone whose level couldn’t easily be found even in the Central Plains. It would have been stranger if he failed to recognize me just because I had covered my face with a crude tiger mask.

Martial artists who had reached a certain realm could identify their opponents by their aura.

But the important thing wasn’t that Baeksang had recognized me at a glance. It was that he showed no pleasure at seeing me.

“So we have an unwelcome guest.”

Not a welcome guest, but an unwelcome one.

If he had said that during our first meeting, it would have scratched my tender heart. But after hearing all sorts of information beforehand, I remained relatively calm.

I scratched the back of my head and answered.

“As they say, even if your mouth is crooked, you should still speak plainly. To state the facts exactly as they are, I’m not an unwelcome guest. I was invited here.”

“Invited?”

His gaze shifted naturally.

Yohi, whose eyes had met Baeksang’s, smiled sweetly and opened her mouth.

“It’s true. I called him here.”

A beautiful woman’s smile was usually highly effective, but Baeksang was clearly not that sort of man.

“Are you planning to collude with the Han Chinese?”

At his even colder tone, Yohi gave an exaggerated shrug.

“Collude? I was merely a little curious. It’s not as though we met alone from the beginning.”

“But only the two of you—and the heavens—know what you discussed after sending Heugung away.”

“Please put your needless concerns aside. I haven’t forgotten the promise we made that day.”

I didn’t know what promise they had made that day, but even hearing about it gave off a distinctly suspicious odor.

Baeksang’s gaze sank even deeper.

“You’re saying pointless things in front of a Han Chinese man, Yohi.”

*Fwoosh!*

An invisible wave of aura flowed from Baeksang’s entire body and swept through the tent.

The air grew heavy in an instant. As the pressure of a Supreme Peak master bore down from every direction, the smile on Yohi’s lips finally began to fade.

That was when I abruptly opened my mouth.

“Come on. There’s a Han Chinese guy standing right in front of you, hearing all this, so let’s stop calling me ‘bastard’ over and over.”

*Whoosh.*

The air, which had been growing heavier by the moment, suddenly lost its force.

Baeksang’s eyebrows twitched as my words simultaneously disrupted the aura surrounding us.

“You bastard.”

“Jin Young Hero, Pavilion Head Jin, Blazing Flame Divine Dragon, or you. Pick whichever title you like and use it. At this point, I’m getting confused about whether I’m from the Jin Family of Taiyuan or the Bastard Family of Taiyuan.”

“……!”

“I do speak well, don’t I? I know. Of course, I trust you understand that I didn’t become a Pavilion Head of the Murim Alliance just by running my mouth. If I had, my sobriquet wouldn’t be Blazing Flame Divine Dragon. It would have been something like Wind Style: Mouth Dragon.”

From my behavior and words, Baeksang must have realized two things for certain.

First, my martial prowess was by no means inferior to his.

Second, I wasn’t merely some green young Han Chinese. I held a high-ranking position as a Pavilion Head in the Murim Alliance, which had been formed from the martial world of the Central Plains.

Even if only one of those facts were true, I was not someone who could be casually dismissed.

Baeksang stared at me in silence for a while before abruptly opening his mouth.

“Now that I see you again, there’s no doubt that you’re the successor of the Fire Gate Clan. Your words and actions, which disregard all consequences, are truly worthy of the Fire King’s Disciple.”

“Old Master—no. Have you met my Master before?”

“The Palace Lord and I were always together. That was true even on the day I first met the Fire King I had only heard about.”

I asked on a sudden hunch.

“Oh. Then, could it be…?”

“Before we had time to do anything, the Palace Lord fell in an instant. Then I was next. It was because I called him a crazy old man.”

Baeksang slightly lifted the white robe he was wearing, revealing the burn scar remaining along his side.

“……”

What was this? It wasn’t as though someone had graded a piece of beef.

*At this point, it’s practically a certification mark.*

Baeksang showed me the traces of the piping-hot Fire King hand pie he had eaten decades ago, then continued in a cold voice.

“It happened a long time ago. But whenever I look at the scar, I remember that day.”

Jeok Cheongang had once told me to be careful of gratitude and grudges in the Murim.

And now, the gratitude and grudges Jeok Cheongang had accumulated in the past were coming back to me like a boomerang.

*Is this that Murim-style gratitude-and-grudges payback thing?*

I was momentarily at a loss for words. Baeksang stared at me with deeply sunken eyes.

“I don’t care whether you’re the Fire King’s Disciple or a Pavilion Head of the Murim Alliance. Nanman has already shed enough blood for the Central Plains, and the Palace Lord’s judgment was wrong.”

“……”

“That is all I have to say to you. So disappear from my sight at once. Before I take matters into my own hands.”

Baeksang’s mood was extremely menacing, and instead of arguing, I rose from my seat.

Not because I was afraid of him, but because there was more to lose than to gain. This was a time to think calmly.

*Step.*

I was about to leave the tent when I suddenly stopped.

I had thought of something I wanted to say to Baeksang, whom I might not see again for some time.

“The blood wasn’t shed for the Central Plains.”

“What?”

“The blood you shed wasn’t for the Central Plains. It was shed for the world.”

I calmly added one more thing.

“It was the same for someone’s son.”

*Whoosh!*

A fierce and mighty aura swept through the tent like a raging gale.

Yohi’s face, which had been watching our conversation in silence, instantly turned pale. The entire massive tent swayed like a leaf caught in a typhoon.

And at the center of it all stood one man, trembling with rage.

“You…!”

His eyes blazed with fire, and his voice seemed to boil.

I didn’t avoid Baeksang’s gaze.

In the face of the violent emotions pouring toward me, I merely remembered someone who had been hiding in a distant corner of my memory.

*This…*

I didn’t know.

I didn’t know whether this suspicion was true or whether it would end as nothing more than a guess.

But before that, I had to show the proper respect for the reverse scale I had touched.[^1]

I inclined my head slightly toward Baeksang, then left the tent.

All the way to my quarters, I thought of someone who was clearly different from Baeksang, yet resembled him in some way.

*……Head Elder.*

The Blade of Flowers, Jin Baekyang.

One of the heroes of the Great Faction War born in Shanxi Province, and a man who, despite being the second son, had nearly become the Family Head of the Jin Family of Taiyuan.

And a traitor who had lived for decades beneath the shadow of Dark Heaven.

I didn’t know why I had thought of him at that exact moment.

But perhaps, perhaps…

*Damn it. I don’t know.*

Just as I let out a deep sigh, I saw Hyuk Mujin roasting an entire wild boar in front of my temporarily assigned quarters in the Inner Palace.

I didn’t know where he had gotten it.

*Look at this thoughtful little punk.*

I often berated him when I was bored, but he was someone who had shared every kind of hardship with me since our days in the Jin Family of Taiyuan.

More importantly, as a former gate guard of the family, he was the person among the Fire Dragon Pavilion members accompanying me who knew the most about the Head Elder.

*He might be able to give me some decent advice.*

Just as I was about to wave at him happily, Hyuk Mujin spotted me approaching and abruptly raised one hand.

He was holding a reddish-hot iron skewer.

“Who goes there?”

“……”

Advice, my ass.

I took off the tiger mask and answered.

“Put your head to the ground.”

“Uh. Ha ha. I was joking.”

“Good. I wasn’t, so put your head to the ground.”

“……”

*Clank.*

The iron skewer slipped from Hyuk Mujin’s limp hand.

* * *

Two days passed in the blink of an eye.

The Beast Miao King, who had told us at our first meeting to wait because he would summon us soon, had yet to summon us. Instead, Yayul Mok’s visits became more frequent than expected.

*Thump.*

White Tiger tossed the wild boar he had been carrying in his mouth onto the ground, then proudly thrust out his chest.

I asked Yayul Mok, who was stroking White Tiger’s neck.

“Where did you catch it this time?”

“In the western grass.”

Yayul Mok answered without thinking, then hurriedly continued with a look of sudden realization.

“……No. I found it on the way here.”

“Why did you bring something you found here?”

“Hmm. I felt bad throwing it away?”

“But for something you found, the bite marks on its neck look exactly like a tiger’s.”

“My child is well trained, so he doesn’t bite just anything. Whether it’s a beast or a person.”

“……”

What kind of bullshit was this?

Was this one of those ideas that there were no bad tigers in the world?

I carefully examined White Tiger’s teeth, which were caked with blood and scraps of flesh, and muttered.

“He looks like he’d bite and chew up anything in one bite, whether it was a beast or a person. Are you saying he doesn’t discriminate when it comes to food?”

“Anyway, that isn’t true. It must have been another tiger.”

“If that’s the case, why are there only one set of bite marks?”

“I don’t know. I simply found it dead on the roadside and brought it here.”

“Oh, I see. A wild boar that had been living hale and healthy somehow died of natural causes on the roadside? Then White Tiger just went *chomp* and brought it here?”

“Exactly.”

“……”

When someone’s shamelessness went beyond all limits, I no longer had the energy to answer.

I stared at Yayul Mok with an incredulous look, then sighed as I gazed at the wild boar, which was large enough to form a mountain.

“By the way, another wild boar?”

“It’s a wild boar. Is there a problem?”

“Another wild boar?”

“……”

“Do Han Chinese people have no conscience? At least shut up and eat it, considering the effort I went through to catch and bring it here.”

“I thought you said you found it?”

“Ah. My mistake. I found it.”

This guy was something else, too.

I only learned later that the meat Hyuk Mujin had been roasting two days ago had been brought by Yayul Mok.

Of course, no one had seen him at the time, and Yayul Mok had stubbornly insisted that it wasn’t him.

“Even wild boar gets old after a day or two. I’ve been eating nothing but this for days, and I’m sick of it. Sick of it.”

“Then take it back.”

“Mujin. Take care of the meat.”

“Yes, sir.”

Yayul Mok and White Tiger looked at me with flat, thoroughly chilled eyes, but I had been wearing a thick skin for so long that my face didn’t even sting at this level.

Yayul Mok clicked his tongue softly as he watched Hyuk Mujin hurry about preparing the meat, then turned his gaze toward me.

“Is the work you’re doing going well?”

Instead of answering, I shook my head.

“So that means you haven’t achieved anything.”

“At least not yet.”

It wasn’t as though I had spent the past two days doing nothing. The Fire Dragon Pavilion members and I had been investigating both inside and outside the Nanman Beast Palace.

I had Ju Hwaran and Hyuk Mujin investigate what was happening in the Inner Palace, while I led the remaining members in scouting the surrounding area.

*We might find a trace of Dark Heaven.*

But as I had just said, despite our efforts, we had achieved no notable results.

The absence of any trace of Dark Heaven near the Nanman Beast Palace was a good thing. But if the traces weren’t absent and we simply hadn’t found them, then it was a different story.

“For now, I plan to keep going. At least until the tribal council.”

The tribal council where all the tribes of Nanman would gather in one place was tomorrow.

Yayul Mok nodded at my words, then opened his mouth in a voice lowered as far as it could go.

“It would be better to postpone it today.”

“Postpone it? Why?”

“The Inner Palace has summoned you.”

[^1]: In East Asian lore, a dragon’s “reverse scale” is a uniquely dangerous vulnerable spot; touching it is said to provoke the dragon’s rage.
```
