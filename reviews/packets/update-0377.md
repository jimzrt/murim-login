<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0377.txt",
      "sha256": "aad748ef4ca121770de119ed545653b02c71c68db95dc06441a35780183f3036",
      "bytes": 16906
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "565c44424c21fbeb2ea2c56abd72465a1bd701383db8805504eb6bce01ff418c",
      "bytes": 2622
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "13a4f68a745930da40047aa6e437f29ae3f8dbafa76b5b207d5d0f06892ed1ee",
      "bytes": 130621
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "35dc220e0296f3ee0b853c365eef01368232b97e8bbbb804de2189c69e16f348",
      "bytes": 944
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "5834fec3b6df4d202d9d49c75fa9761d0343b50398e81f7e769ca83414ce4493",
      "bytes": 533
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "30ad7d55528997689aafc5b732c35d1996f1e62f927de225485d4c991c4bcb55",
      "bytes": 609
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "c0ed3b5d68ec37dd10772f65dc23df69a637ba274db26c37e98c676429af82c6",
      "bytes": 1108
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "332d2c73db1fb6a49eea306c7dab737404254f35b635c5ac8afe728d3c39f303",
      "bytes": 1129
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "aef9fbaf1b0981fdaf14c2af44a3c9be46b9a951e008f0f71200b7f2d8c5e588",
      "bytes": 622
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "025a1c2f0639ade81fcf6e81729d9d8f6d5e619e4908c80cbd167f2f0e3a2b09",
      "bytes": 666
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "f071277420833cea791b1922c1c367d6025facfe8b359d544761795c59d5380b",
      "bytes": 1019
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "040714611eeca6075fc47817f37917d302f70ee3e1194832e95531dcf298207a",
      "bytes": 888
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "b192324bf63195f62ba663135d14e9bb475383050782b1c1d2b79add2594022b",
      "bytes": 100705
    }
  ],
  "estimated_tokens": 13894
}
-->

# Durable State Update — Chapter 377

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 377. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 377. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 377,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 377,
    "continuity_sources": [377],
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

## Prior durable context

```json
{
  "active_continuity": [
    "The Sichuan Tang Clan is rebuilding seven days after the Three-Gate Bloodbath, which caused catastrophic casualties and ongoing funerals.",
    "Most Dark Heaven attackers involved in the Sichuan assault are dead or captured; Mungyeong captured the Third Fiend in the hidden cavern, while the Second Fiend's fate is unknown.",
    "Jin Taekyung is awake, has reached Level 120 and the Supreme Peak realm, manifested Force, and is publicly known as the Blazing Flame Divine Dragon.",
    "Jeok Cheongang is alive but remains weakened and is recovering his strength.",
    "Dong Feng's dantian and martial arts were destroyed while shielding Jeok Cheongang.",
    "Mungyeong is the Divine Physician and former Slaughter Saint; he has sworn never to kill again and intends to live as a physician.",
    "Dong Feng is Mungyeong's Disciple and has served him for decades after Mungyeong saved him from an epidemic.",
    "Hyuk Mujin and Gung Gibang remain badly wounded after fighting the Third Fiend.",
    "Cheongpung remains a Supreme Peak master at the Sichuan Tang Clan with Mimi and is now Mimi's temporary guardian.",
    "The Lord of Heaven temporarily possessed the Western Heaven Demon Lord's body and escaped after One Annihilation.",
    "The Myriad-Poison Ring is now bound to Jin Taekyung, alongside White Flame and one unnamed bound item.",
    "Jin Taekyung's party is leaving Chengdu by ship, but an unidentified boy has arrived seeking passage."
  ],
  "continuity_sources": [
    376
  ],
  "open_questions": [
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "What is the true nature and purpose of the Lord of Heaven, and what became of the Western Heaven Demon Lord?",
    "What was the origin and purpose of the Moving Formation, and why did it lose its power?",
    "Who is the unidentified boy who arrives at Chengdu's western harbor?",
    "Will Mungyeong remain outside the coming war, or will the crisis force him to intervene?"
  ],
  "safe_through": 376,
  "temporary_decisions": [
    "Render 열화신룡 as Blazing Flame Divine Dragon, distinct from Huashan Divine Dragon.",
    "Use Mimi for 미미 and Mimi-chan for 미미쨩; render 삼괴 as Third Fiend in singular references and Three Fiends in collective references.",
    "Render 진인 as Perfected One, 도우 as Fellow Daoist, and 신니 as Venerable Nun in forms of address.",
    "Render 환영진 as illusion formation and 이동진 as Moving Formation.",
    "Render 독룡각 as Poison Dragon Pavilion and 가주 대행 as Acting Family Head."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 살성     | **Slaughter Saint**           | —              |
| 장강수로맹  | **Yangtze River Channel League** |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 구결     | **formula**                                      | Mnemonic/oral formula for a martial art               |
| 제자     | **Disciple**                                 |
| 시스템              | **System**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 아이템              | **Item**                       |
| 로그아웃             | **Logout**                     |
| 사천     | **Sichuan**            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소저      | **Young Lady**                                                  |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 아이템창 | **Item Window** | System window displaying an item's details. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 도지휘사 | **Military Commissioner** | Provincial military commander's office |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 열화신공 | **Fire Gate Divine Technique** | Secret internal cultivation technique of the Fire Gate Clan, preserved through one-person succession without leakage. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 중독 | **Poisoned** | System status abnormality caused by the poisons. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 수룡채 | **Water Dragon Stronghold** | Major river stronghold belonging to the Yangtze River Channel League. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 의생 | **medical apprentice** | Mungyeong's occupation. |
| 사천성 | **Sichuan Province** | Province form used in the title of its chief official. |
| 사천성주 | **City Lord of Sichuan Province** | Title held by Won Gyun. |
| 호위장 | **Captain of the Guards** | The Sichuan City Lord's guard captain. |
| 애향이 | **Aehyang** | Personal name of the Sichuan City Lord's favorite concubine. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 흑룡갑 | **Black Dragon Armor** | Defensive armor worn beneath the Western Heaven Demon Lord's yellow robe. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 시비 | 진태경 | household_servant_to_visiting_young_hero | Young Hero Jin | formal-polite | The maid summons Taekyung to meet the Family Head. |
| 궁기방 | 진태경 | rival_finalists | you bastard | insulting-casual | Gung Gibang answers Taekyung's collective insult with a profane threat. |
| 진태경 | 궁기방 | rival_finalists | you three idiots | insulting-casual | Taekyung addresses Gung Gibang as part of the trio and threatens them before a duel. |
| 진태경 | 문경 | young_martial_artist_to_medical_apprentice | Young Hero | formal-polite | Taekyung addresses the non-martial Mungyeong as 소협 while praising his actions. |
| 문경 | 진태경 | young_passenger_to_younger_martial_artist | Young Hero | deferential | Mungyeong uses 소협 while asking Taekyung for help boarding the ship. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 사천성주 | 진태경 | official_to_imperial_messenger | Messenger of His Highness Prince Shangshan | formal-deferential | The City Lord addresses Taekyung deferentially after seeing Prince Shangshan's Token. |
| 진태경 | 사천성주 | visitor_to_city_lord | City Lord | sarcastic-polite | Taekyung jokingly praises him as our City Lord after making him fund the reward. |
| 사천성주 | 애향이 | lord_to_favorite_concubine | Aehyang | affectionate-familiar | The City Lord uses her personal name while discussing the visitors. |
| 애향이 | 사천성주 | favorite_concubine_to_city_lord | My lord | seductive-deferential | Aehyang repeatedly addresses the City Lord as 대인 while persuading him to receive Taekyung. |
| 서천마군 | 청풍 | commander_to_young_opponent | you | gentle and taunting | Uses 자네 while identifying Cheongpung and discussing the Blood Lord. |
| 서천마군 | 진태경 | hostile_opponents | you | calm and taunting | Uses 자네 while questioning Taekyung and offering to take him alive. |
| 진태경 | 서천마군 | hostile_opponents | Western Heaven Demon Lord | casual and defiant | Identifies the Demon Lord by title and answers his surrender demand with sarcasm. |
| 서천마군 | 신의 | hostile_invader_to_physician | Divine Physician | calm and mocking | Uses 신의 and 그대 while taunting the physician and dismissing his objections. |
| 신의 | 서천마군 | physician_to_invading_fiend | fiend | defiant and formal | Calls the Western Heaven Demon Lord an 악귀 and orders him to leave. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 376
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 376
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who has sworn never to kill again.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 376
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Rival finalist alongside Baek Woo and Zhuge Gyun; trades insults with Taekyung and is helping investigate Tang Taesang’s murder through Beggars’ Sect intelligence.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 376
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 376
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother; Jeok Cheongang is his Master; Cheongpung is his trusted companion and only true martial rival; his mother and sister Hayeon are among those he protects.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 376
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 376
- **Aliases:** None
- **Role:** Mungyeong is the legendary physician known as the Divine Physician and former Slaughter Saint, and he has sworn never to kill again.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, while Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 350
- **Aliases:** None
- **Role:** The City Lord and a member of the imperial family; ten-year-old Prince Shangshan, whose personal name is Zhu Bao, is an exceptionally skilled young swordsman who has trained daily for three years.
- **Personality:** Earnest, admiring, and eager to emulate Jin Taekyung; despite his royal dignity, he shows openly childlike enthusiasm for martial arts and Taekyung's reputation.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Commands the unnamed Third-Rank Assistant Military Commissioner to attend the luncheon and hosts the gathering of young Murim prodigies; admires Jin Taekyung and seeks to emulate him; has been invited to the Jin Family's grand banquet in fifteen days, where Taekyung promises to obtain Jin Mukyung's autograph for him.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 375
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃377화



“그들은, 떠났나?”

살이 토실토실하게 오른 중년인, 사천성주의 긴장 어린 물음에 호위장이 대답했다.

“예. 한 식경 전에 그들이 탄 장강수로맹의 쾌조선이 출항했습니다.”

“휴우우.”

뱃살이 출렁일 만큼 깊은 안도의 한숨을 내쉰 사천성주가 손을 내저었다.

“알겠으니 이만 물러가게. 혹시 무림인들에 관련된 소식이 있다면 바로바로 보고하고.”

“알겠습니다. 한데 성도 인근에 주둔시켜 놓은 병력은…….”

사천성주가 눈살을 찌푸렸다.

“이봐, 호위장.”

“예?”

“내가 그런 시시콜콜한 부분까지 신경 써야 하나? 그 정도 뒤처리는 자네들끼리 처리하라고. 도지휘사(都指揮使), 그 꼬장꼬장한 작자와 잘 상의를 하든가 해서. 응?”

“…….”

호위장은 내심 어이가 없었다.

이게 말인가 방귀인가. 성주의 무능함과 아랫사람에게 일 떠넘기는 버릇이야 하루 이틀 일이 아니지만 이건 해도 해도 너무했다.

‘아무리 그래도 이 정도는 아니었던 것 같은데.’

어느 날부터 애첩 하나를 들이더니 벌써 수년째 여색에 빠져 공무는 뒷전이다.

내심 한숨을 푹 내쉰 호위장이 힘없이 군례를 취했다.

“……성주님의 명을 받들겠습니다.”

“당연히 그래야지. 그럼 수고하라고. 난 바쁜 용무가 있어서 이만.”

그제야 만족스럽게 고개를 끄덕인 사천성주가 자리에서 일어났다.

과도한 체중 탓에 가쁜 숨을 내쉬며 멀어지는 그의 뒷모습을 바라보던 호위장이 개미만 한 목소리로 중얼거렸다.

“바쁜 용무는 무슨. 또 애첩이나 안으러 가겠지.”

호위장의 예상은 적중했다. 대전을 떠난 사천성주가 가장 먼저 찾은 곳은 바로 화려하게 치장된 침소였다.

“애향아! 애향아!”

어지간한 방보다 큰 비단 침상 위, 반나체로 누워 있던 미녀가 몸을 일으켰다.

“가가(哥哥). 왜 이제야 오셨어요? 애향이가 얼마나 기다렸는데.”

“그, 그랬느냐?”

새치름한 눈매에 한 번, 이불 사이로 슬쩍슬쩍 보이는 새하얀 살결에 두 번 넋이 나간 사천성주의 입이 헤벌쭉 벌어졌다.

“미안하구나. 호위장이 귀찮게 구는 바람에.”

“또 그 사람이에요? 안 그래도 가가께서 얼마나 바쁘신데 왜 그리 못살게 군대요?”

“그러게나 말이다.”

“이래서 무능력한 아랫것들이 문제예요. 가가께서 없으시면 다들 아무것도 못 하잖아요?”

“역시, 이 가가를 생각해 주는 건 우리 애향이밖에 없다!”

호위장이 들었으면 눈을 까뒤집었을 대화였다.

감동으로 볼살을 부르르 떠는 사천성주를 향해 애첩이 두 팔을 벌렸다.

“이리 오세요, 가가. 고생하셨으니까 이 애향이가 꼭 안아 드릴게요.”

“애향아……!”

사랑하는 애첩의 끈적하고도 고혹적인 눈웃음에, 사천성주의 눈동자가 몽롱하게 풀어졌다.

“세상 천하에 너처럼 아름다운 여인이 있을 수 있단 말이냐!”

삼공(三公)을 배출한 세도가의 핏줄로 태어나 탄탄대로를 걸어온 사천성주다.

마르지 않는 재물을 바탕으로 숱하게 기방을 들락거리며 온갖 미녀들을 품에 안았다.

마음이 혹하면 첩으로 들인 것도 수차례, 그러나 워낙 많은 여인을 만난 탓에 한 해를 버티지 못하고 시들해지고는 했다.

‘하지만 이 아이는 달라!’

맹세코 이런 여인은 처음 보았다. 목소리와 눈빛, 손끝 하나의 움직임까지. 사천성주의 눈에는 애향이의 모든 것이 매혹적이고 사랑스러웠다.

벌써 수년째 보아 온 모습이지만 도무지 질리지 않는다. 아니, 오히려 무서울 만큼 깊숙이 빠져들고 있었다.

“사랑한다. 사랑한다, 애향아!”

막 오십 줄에 접어든 사천성주의 외침은 사랑에 빠진 젊은이의 그것처럼 절절했다.

홀린 듯이 다가가 애첩의 품에 안긴 그는 언제나 그래 왔듯 오늘 하루 있었던 일을 말하기 시작했다. 사천성주에게 있어 애첩은 가장 은밀한 비밀까지 털어놓을 수 있는 유일한 사람이었다.

“……해서, 드디어 그 골칫덩이 무뢰배들이 떠났다.”

“무뢰배들이라면, 그들을 말씀하시는 거죠? 지난번에 찾아왔던 무림인들.”

“그래. 상산왕 전하의 증표를 가져왔던 그자들 말이다.”

“흐음.”

“왜 그러느냐?”

“아니에요, 아무것도. 그나저나 이번 일로 가가께서 고생 많으셨겠다. 들어 보니 무림인들끼리 시비가 붙어서 많은 사람이 죽고 다쳤다면서요?”

사천성주가 질린 얼굴로 고개를 내저었다.

“말도 말거라. 어디서 구했는지 감히 관군의 복식까지 훔쳐 입고 대국의 질서를 어지럽히다니.”

“어머, 정말요?”

“믿기지 않겠지만 사실이다. 내 다른 건 몰라도 그에 관해서는 반드시 조정에 장계를…….”

“어쩜 이리 대장부 같으실까. 그런데 가가.”

싱긋 웃은 애첩이 무릎에 얹힌 사천성주의 머리를 쓰다듬었다.

“황실에서 알게 된다면 일이 커지지 않을까요?”

“으, 응?”

“그렇잖아요. 언젠가는 가가께서도 삼공(三公)의 지위에 올라 문무백관을 거느리며 황상을 보필하실 텐데…… 소첩은 가가를 시기하는 무리가 이번 일을 문제 삼지는 않을까 걱정이 되어요.”

“허허. 역시 날 이만큼 생각해 주는 것은 애향이, 너밖에 없구나.”

사천성주는 애정이 뚝뚝 묻어나는 눈빛으로 자신의 애첩을 바라보았다.

그러나 그 역시 아주 얼간이는 아니었다.

비록 관과 무림이 서로를 소 닭 보듯 하는 상호 불가침의 영역이라고는 하지만, 지난 칠 주야 동안 천 명이 훌쩍 넘는 사람들이 사천 땅 곳곳에서 죽어 나갔다.

자질구레한 뒤처리는 아랫놈들에게 떠넘기더라도 최소한 이것만큼은 직접 나서야 한다.

“네 마음씨가 갸륵하나, 지금처럼 큰 사안은 오히려 숨길수록 문제가 되기 마련이다.”

“가가도 참. 제가 그걸 모를 것 같아요?”

“음? 그럼 어쩌자는 것이냐?”

“숨길 건 숨기고, 공은 부풀려야죠.”

교태 가득한 목소리가 사천성주의 귓가를 간지럽혔다.

“무림인들 간에 큰 분쟁이 있었고, 가가께서 휘하의 관군을 움직여 이 사태를 진정시킨 것으로.”

“으음.”

“가가께서는 무뢰배들의 손에 어지럽혀진 대국의 질서를 바로 세우고, 민초들을 보살핀 어진 성주가 되시는 거예요. 물론 관의 무기와 의복에 관한 이야기는 빼놓는 게 좋겠죠? 오해를 살 수도 있으니까.”

“애향이 네 말대로만 된다면 좋겠지만. 아무리 그래도 장계를 거짓으로 꾸며 올리기에는 좀…….”

“가가, 절 보세요.”

머뭇거리던 사천성주는 흑요석처럼 아름답게 반짝거리는 눈동자를 보고 외마디 탄성을 흘렸다.

“아.”

“이 애향이를, 가가를 사모하는 제 뜻을 모르시나요?”

“그것이, 그러니까…….”

사천성주는 말을 잇지 못했다.

애첩과 눈이 마주친 순간, 이미 머릿속은 텅 비워진 지 오래였다.

고혹적인 자태에 가슴이 떨리고 꽃향기 같은 채취에 정신이 아득해진다.

어디에선가 불쑥 솟구친 무한한 신뢰와 애정, 그리고 참을 수 없는 욕망이 그를 지배했다.

“애향아, 애향아!”

간절한 목소리. 하지만 애첩은 자신의 몸을 더듬어 오는 사천성주의 손길을 붙잡았다.

“가가, 대답은요?”

“다, 당연히 네 뜻에 따르마. 너를 위해서라면 내 무엇이든 하겠다!”

애첩의 입가에 맺힌 웃음이 짙어졌다.

“잘하셨어요. 지금까지 그랬던 것처럼, 앞으로도 그렇게 하시면 되는 거예요. 아셨지요?”

“응, 응!”

강렬한 욕망에 사로잡힌 사천성주는 미처 볼 수 없었다.

자신이 그토록 사랑하는 애첩의 눈동자에 요사스러운 붉은빛이 스며드는 불길한 광경을.

“아이, 착해라. 우리 성주님. 말도 잘 듣네.”

애첩은 소리 내어 깔깔 웃었다.

모든 것은 그녀가, 아니 그분이 원하는 방향으로 흘러가고 있었다.



* * *



“음?”

“왜 그러세요?”

“아니, 방금 무슨 미친년 웃는 소리를 들은 것 같아서.”

“미친년이요? 여기서요?”

“응. 쎄하더라고.”

나와 혁무진은 주위를 둘러봤다. 드넓은 장강의 지류, 수룡채의 깃발을 내건 세 척의 쾌조선은 막힘없이 나아가고 있었고 당연하지만 그중 어디에도 여인은 없었다.

“잘못 들었나? 이상하네.”

요새 온갖 일을 다 겪었더니 이제 환청이 다 들리나.

고민하는 내게 혁무진이 심각한 얼굴로 입을 열었다.

“혹시 그…….”

“그, 뭐?”

“앞줄 우측 네 번째에 서 있던 소저를 잊지 못하신 것 아닙니까?”

궁기방이 고개를 저었다.

“헛소리. 좌측 세 번째야. 그 정도면 잊지 못할 미모지.”

“아, 뭔가 했더니 그 이야기였어?”

나는 인자하게 웃으며 두 녀석을 바라보았다.

“내 생각에는, 오늘이 너희 둘한테 잊지 못할 하루가 될 것 같은데.”

환히 웃는 얼굴로 손짓하자 그걸 보고 달려온 건장한 수적 여럿이 굽신굽신 고개를 조아렸다.

“부르셨습니까요, 진 대협.”

“혹시 쇤네들에게 뭐 시키실 일이라도.”

“저 새끼들 붙잡아서 장강에 찍먹 해 주세요.”

수적들이 어리둥절한 얼굴로 되물었다.

“어, 찍먹이라 하셨습니까?”

“죄송하지만 저희가 원체 무식한 놈들이라. 당최 찍먹이 무엇입니까?”

“찍먹은 올바른 문화……가 아니라, 그냥 제가 멈추라고 할 때까지 계속 머리통만 담갔다가 빼 주시면 됩니다.”

“아아, 예.”

“쉽구먼요.”

“자, 잠깐만!”

“조장님!”

궁기방과 혁무진은 저항하려 했지만 턱도 없는 일이었다.

한 놈은 다리 한 짝만 멀쩡하고, 다른 한 놈은 전신이 붕대로 감겨 있었으니까.

무공을 익힌 건장한 떡대들이 우르르 몰려와 사지를 붙들고 찍먹쇼를 시작하는 사이, 나는 앞서 허공에 띄워 둔 시스템창을 바라봤다.



- 아직 이름을 정하지 않은 종속 아이템이 있습니다. 확인하시겠습니까?



‘당연히 예스.’

띠링.



아이템창



[???]

종류 : 방어구

등급 : 신병이기

제한 : 진태경

설명 : 이름 모를 고대 야장의 혼이 깃든 갑옷. 실로 가공할 만한 방어력을 지녔으며, 현재는 전 주인이 사망함으로써 새로운 주인에게 소유권이 종속되었다. 이름을 지어 주면 어디에서나 자유롭게 사용할 수 있다.





‘전 주인이 사망해서 소유권이 종속되었다고?’

설마 했는데, 내가 생각하는 그 물건이 맞는 것 같다.

나는 인벤토리를 탈탈 털어 본 끝에 새로운 종속 아이템을 확인할 수 있었다. 그리고 저절로 흘러나오는 김빠진 소리.

“……에게?”

손바닥 위에 올려진 그것은 자그마한 파편에 불과했다. 본래는 흑룡갑(黑龍鉀)이라 불리던 물건이기도 했다.

‘분명히 마지막에 일섬으로 서천마군, 그놈과 함께 날려 버렸는데. 종속 아이템이라 인벤토리에 자동으로 들어온 건가.’

흑룡갑이 산산조각 나던 광경이 아직도 눈앞에 선하다.

그런데 겨우 이만한 파편으로 뭘 어떻게 하라는 건지 모르겠네.

‘팬티 앞부분에 넣어 두면 세상 든든하긴 할 것 같은데.’

아, 혹시 이래서 방어구인 건가.

슬쩍 바지 앞섬을 잡아당겨 적절한 위치를 살피던 그때였다.

“거기서 뭐 하…….”

“……아.”

순간 내려앉은 싸늘한 침묵.

풀어진 바지춤과 그 안에 쑥 들어간 내 손을 본 소년의 얼굴이 딱딱하게 굳는다.

주위에 아무도 없는 것을 확인한 쌀성, 아니 문경이 입을 열었다.

“이걸 하필, 여기서?”

“아니, 잠깐만. 이거 오해가 좀 있는 것 같은데요.”

내가 황급히 변명하려던 찰나, 문경의 눈빛이 착 가라앉았다.

“출발할 때 말했을 텐데. 화왕과 청풍을 제외한 다른 사람 앞에서는 문경으로 대하라고.”

나는 억울한 얼굴로 대답했다.

“너도 지금 반말하고 있잖아, 새꺄.”

“……!”

“아, 죄송.”

만감이 교차하는 표정을 짓던 문경이 근처로 다가온 수적들을 곁눈질하며 혀를 찼다.

무시무시한 살성이 신의의 제자이자 밝은 소년 의생의 모습으로 변하는 것은 순식간이었다.

“뭐 하고 계셨어요?”

“네가 알아서 뭐 하게.”

“……!”

이거 은근히 재밌네. 그런데 세 번은 못 하겠다.

나는 말문이 막힌 문경을 향해 얼른 손을 내밀었다.

“이게 바지춤에 들어가서.”

물론 사실과는 살짝 괴리감이 있지만, 문경은 그런 것 따위는 신경 쓰지 않았다. 정확히 말하자면, 흑룡갑의 파편에 시선이 고정되어 있었다.

“이건…….”

“혹시 아시는 물건. 아니, 아는 물건이냐?”

“어디서 얻었습니까?”

“그놈에게서.”

서천마군을 뜻한다는 것을 알아들은 문경이 고개를 끄덕였다.

“신병이기(神兵利器)를 얻으셨군요. 어쩌다가 파편만 남았는지는 모르겠지만.”

“놈은 이걸 흑룡갑이라고 부르던데.”

“흑룡갑?”

“왜, 알고 있던 이름이랑 달라?”

“오래된 비사(祕史)에서 읽은 적이 있습니다. 정해진 이름이 없으며, 소유자에 따라 형태와 성질이 바뀐다는 신비한 갑옷에 대한 이야기를.”

“형태와 성질이 바뀐다고? 어떻게?”

문경은 한심하다는 눈빛으로 대답을 대신했다. 그리고 나는 그제야 지금부터 무엇을 해야 할지 깨달았다.

‘공력.’

공력이야말로 소유자가 지닌 형태와 성질, 그 자체다.

스아아아.

팔 성에 오른 열화신공의 구결에 따라 용암 같은 기운을 흑룡갑의 파편을 향해 흘려보냈다.

파편의 표면에 감돌던 묵색 기운이 사라지고, 빈자리를 청백색의 열양지기가 채웠다.

불꽃이 이글거리는 듯한 문양이 새겨진 그것은, 더 이상 흑룡갑이라 부를 수 없는 물건이었다.

‘화룡갑(火龍鉀).’

단순하지만 이보다 적절한 이름은 존재하지 않을 것이다.

내가 만족스러운 미소를 머금음과 동시에 경쾌한 종소리가 울려 퍼졌다.

띠링.



- 당신은 종속 아이템, [???]에게 새로운 이름을 부여했습니다!

- 지금부터 [화룡갑]을 어디에서나 자유롭게 사용할 수 있습니다!

- [화룡갑]이 당신의 기운과 공명합니다! 스스로 파손 부위를 복구하기 위해 소유자의 힘을 원합니다!



쏴아악.

느껴진다. 체내로부터 빠져나간 막대한 공력이 화룡갑을 향해 몰려드는 것이.

나는 스펀지처럼 공력을 빨아들인 그것을 품에 넣는 척, 인벤토리에 수납했다.

‘자동 복구라, 끝내주는데.’

확실히 쓸모있는 물건을 얻었다.

다행이다. 이번 여정에서 얻은 마지막 선물이 화룡갑이라서.

돌아서려는 나를, 문경이 눈을 크게 뜨고 바라봤다.

“어딜 가느, 가십니까?”

“네가 알아서 뭐 하게.”

“……!”

아, 이거 어쩐지 중독 될 것 같아.

나는 속으로 ‘참을 인’ 자를 되새기고 있을 문경에게 손을 흔들어 주었다.

“한숨 자러 간다. 깨우지마라.”

“……?”

그래, 이제는 오랜 잠에서 깨어날 때다.

그런데…….

‘왜 이렇게 찝찝하지? 뭘 잊었나?’

갸웃거리며 쾌조선의 선실에 자리를 잡고 누운 나는 눈을 감았다. 깊이 심호흡하며 명령어를 외쳤다.

‘로그아웃.’

띠링.



- 10초 후 로그아웃합니다. 십, 구, 팔, 칠…….



마지막 카운트와 함께, 어디선가 물장구 소리와 누군가의 외침이 아련하게 귓가를 파고들었다.

첨벙, 푸하! 조장님, 살려, 푸하!
```

## Final English reading copy

```markdown
# Chapter 377

“Have they left?”

The Captain of the Guards answered the tense question from the plump, middle-aged City Lord of Sichuan Province.

“Yes. The fast ship of the Yangtze River Channel League carrying them departed half an hour ago.”

“Whew.”

The City Lord let out such a deep sigh of relief that his belly jiggled, then waved a hand.

“All right, you may withdraw. If you hear any news related to the martial artists, report it immediately.”

“Understood. But what about the troops stationed near Chengdu…?”

The City Lord frowned.

“Listen, Captain of the Guards.”

“Yes?”

“Do I need to worry about such trivial details? Handle that kind of cleanup among yourselves. Consult the Military Commissioner, that stubborn bastard, if you have to. Hmm?”

“…”

The Captain of the Guards was speechless.

*Were those words or a fart?*

The City Lord’s incompetence and habit of dumping work on his subordinates were nothing new, but this was too much, even for him.

*He wasn’t always this bad. Was he?*

Several years ago, he had taken a favorite concubine, and ever since then, he had been lost in women, putting his official duties aside.

The Captain of the Guards sighed inwardly and gave a dispirited military salute.

“…I will carry out Your Excellency’s orders.”

“Of course you will. Then get to work. I have an important matter to attend to.”

Only then did the City Lord nod in satisfaction and rise from his seat.

The Captain of the Guards watched his retreating back as he huffed and puffed beneath his excessive weight, then muttered in a voice barely louder than an ant’s.

“Important matter, my ass. He’s probably going to embrace his favorite concubine again.”

The Captain of the Guards’ prediction was correct. The first place the City Lord visited after leaving the great hall was a lavishly decorated bedchamber.

“Aehyang! Aehyang!”

A beauty lying half-naked on a silk bed larger than most rooms sat up.

“My lord. Why did you take so long? Aehyang has been waiting for you.”

“Y-You have?”

The City Lord was dazed once by her coy eyes and twice by the pure white skin that flashed between the sheets. His mouth fell open in a foolish grin.

“I’m sorry. The Captain of the Guards kept bothering me.”

“That man again? My lord is already so busy. Why does he keep harassing you?”

“I know, right?”

“This is why incompetent underlings are such a problem. Without my lord, none of them could do anything.”

“You’re the only one who truly understands me, Aehyang!”

It was the sort of conversation that would have made the Captain of the Guards roll his eyes if he had heard it.

As the City Lord’s cheeks trembled with emotion, his favorite concubine opened both arms toward him.

“Come here, my lord. You’ve had such a hard time. Let Aehyang hold you.”

“Aehyang…”

At the seductive, lingering smile in his beloved concubine’s eyes, the City Lord’s gaze grew hazy.

“Could there possibly be a woman in all the world as beautiful as you?”

The City Lord had been born into a powerful family that had produced members of the Three Excellencies[^1] and had walked a smooth path throughout his life.

Backed by inexhaustible wealth, he had visited pleasure quarters countless times and held every kind of beauty in his arms.

He had taken several women as concubines whenever they caught his fancy. But because he had met so many women, his interest never lasted a year before fading.

*But this girl is different!*

He swore he had never seen a woman like her. Her voice, her gaze, even the slightest movement of her fingertips—everything about Aehyang was enchanting and lovable in the City Lord’s eyes.

He had been looking at her for several years already, yet he could not grow tired of her. No—if anything, he was sinking into her more deeply, almost frighteningly so.

“I love you. I love you, Aehyang!”

The City Lord, who was just entering his fifties, cried out with the passion of a young man in love.

As though bewitched, he approached and settled into his favorite concubine’s embrace. As he always did, he began telling her about everything that had happened that day. To the City Lord, she was the only person to whom he could confide even his most secret thoughts.

“…And so, those troublesome ruffians finally left.”

“You mean those people, don’t you? The martial artists who came here last time.”

“That’s right. The ones who brought His Highness Prince Shangshan’s Token.”

“Hmm.”

“What is it?”

“Nothing. I was just thinking that you must have had a difficult time because of this. I heard the martial artists got into a fight and many people were killed or injured.”

The City Lord shook his head with a disgusted expression.

“Don’t remind me. They dared to steal government uniforms from who knows where, put them on, and disrupt the order of the Great Nation.”

“Oh my. Is that true?”

“You may find it hard to believe, but it is. Regardless of everything else, I will certainly submit a report to the imperial court about this…”

“How gallant of you. But, my lord…”

With a sweet smile, Aehyang stroked the City Lord’s head where it rested on her lap.

“Wouldn’t things become serious if the imperial court found out?”

“H-Hmm?”

“Think about it. One day, my lord will rise to the position of one of the Three Excellencies, command all the civil and military officials, and assist the Emperor… I’m worried that the people who envy you might use this incident against you.”

“Heh heh. You truly are the only one who thinks of me this much, Aehyang.”

The City Lord gazed at his favorite concubine with overflowing affection.

But he was not a complete fool.

Though the government and Murim occupied mutually noninterfering spheres and generally ignored each other, well over a thousand people had died throughout Sichuan over the past seven days and nights.

He could leave the trivial cleanup to his subordinates, but this was something he needed to handle personally.

“Your concern is admirable, but the bigger the matter, the more trouble it causes if you try to hide it.”

“My lord, do you really think I don’t know that?”

“Hmm? Then what do you suggest?”

“Hide what must be hidden, and exaggerate your accomplishments.”

Her coquettish voice tickled the City Lord’s ear.

“Say that there was a major conflict among the martial artists, and that my lord mobilized the government troops under your command to calm the situation.”

“Hmm.”

“You will become a benevolent City Lord who restored the Great Nation’s order after it was disrupted by ruffians and cared for the common people. Of course, it would be best to leave out the part about the government weapons and uniforms. They might cause misunderstandings.”

“It would be nice if things went exactly as you say, Aehyang. But even so, submitting a false report to the court…”

“My lord, look at me.”

The hesitant City Lord let out a short exclamation when he saw her eyes, beautiful and gleaming like polished obsidian.

“Ah.”

“Do you not understand how I feel about you, my lord? How much I adore you?”

“I… That is…”

The City Lord could not finish his sentence.

The moment his eyes met his concubine’s, his mind had already gone blank.

His heart trembled at her alluring figure, and the flowerlike fragrance of her body made his senses swim.

An immense trust and affection that had risen from somewhere, along with unbearable desire, seized control of him.

“Aehyang, Aehyang!”

His voice was desperate. But the concubine caught the City Lord’s hand as it reached over to grope her body.

“My lord, what is your answer?”

“Of course I’ll do as you say. I’ll do anything for you!”

The smile at the corner of his concubine’s mouth deepened.

“Well done. Just keep doing as you have until now. Do you understand?”

“Yes, yes!”

Overcome by intense desire, the City Lord failed to notice.

He could not see the ominous sight of an eerie red light seeping into the eyes of the concubine he loved so deeply.

“Oh, what a good boy. Our City Lord listens so well.”

His favorite concubine laughed aloud.

Everything was proceeding in the direction she wanted—or rather, that person wanted.

* * *

“Hmm?”

“What is it?”

“Nothing. I thought I heard some crazy bitch laughing just now.”

“A crazy woman? Here?”

“Yeah. It gave me a bad feeling.”

Hyuk Mujin and I looked around. Three fast ships flying the flags of the Water Dragon Stronghold were moving smoothly along a broad tributary of the Yangtze, and naturally, there was not a woman aboard any of them.

“Did I hear wrong? That’s strange.”

*After everything I’ve been through lately, am I hallucinating now?*

As I was pondering this, Hyuk Mujin spoke with a serious expression.

“Could it be that…”

“That what?”

“You have been unable to forget the Young Lady standing fourth from the right in the front row?”

Gung Gibang shook his head.

“Bullshit. It was the third from the left. A beauty like that would be hard to forget.”

“Oh, so that’s what this was about?”

I smiled benevolently as I looked at the two of them.

“I think today is going to be a day neither of you forgets.”

With a bright smile, I beckoned. Several burly river pirates came running over and bowed repeatedly.

“Did you call for us, Great Hero Jin?”

“Is there something you need this humble one to do?”

“Grab those two bastards and give them a little dip in the Yangtze.”

The river pirates looked at each other in confusion.

“Uh, did you say dip?”

“We’re ignorant men, I’m afraid. What exactly does ‘dip’ mean?”

“Dipping is the proper culture… No, I mean just keep dunking their heads in and pulling them out until I tell you to stop.”

“Ohhh, understood.”

“That sounds easy enough.”

“W-Wait a minute!”

“Captain!”

Hyuk Mujin and Gung Gibang tried to resist, but it was hopeless.

One of them had only one good leg, while the other was wrapped in bandages from head to toe.

As several large, martial-arts-trained river pirates swarmed over, grabbed their arms and legs, and began the dunking show, I looked at the System Window I had already left floating in the air.

> **System**
>
> There is a bound Item whose name has not yet been decided. Would you like to check it?

*Obviously, yes.*

Ding.

> **System**
>
> **Item Window**
>
> **???**
>
> **Type:** Armor  
> **Grade:** Divine Weapon  
> **Restriction:** Jin Taekyung  
> **Description:** An armor containing the spirit of an unknown ancient master smith. It possesses truly formidable defensive power. Since its former owner has died, ownership has been bound to a new owner. Once given a name, it can be freely used anywhere.

*Its ownership was bound to me because its former owner died?*

I had wondered if that was the case, and it seemed that the item was exactly what I thought it was.

After turning my inventory upside down, I found the new bound Item. A flat, deflated sound escaped me.

“…What?”

The thing resting on my palm was nothing more than a tiny fragment. It had originally been called the Black Dragon Armor.

*I definitely blasted it away along with that bastard, the Western Heaven Demon Lord, in the final One Annihilation. Did it automatically enter my inventory because it was a bound Item?*

I could still vividly see the Black Dragon Armor shattering into pieces.

But I had no idea what I was supposed to do with a fragment this small.

*It would certainly make me feel safe if I put it in the front of my underwear.*

Ah. Was that why it was classified as armor?

I had just tugged at the front of my pants to check the most suitable position when—

“What are you doing—”

“…Ah.”

A chilly silence descended over the scene.

The boy’s face stiffened when he saw my loosened waistband and my hand shoved inside it.

After making sure no one else was nearby, the Slaughter Saint—no, Mungyeong—spoke.

“Of all places, here?”

“No, wait. I think there’s been a misunderstanding.”

I was about to hurriedly explain when Mungyeong’s gaze turned cold.

“I told you before we departed. In front of anyone other than the Fire King and Cheongpung, you are to treat me as Mungyeong.”

I answered with an aggrieved expression.

“You’re speaking informally too, asshole.”

“…!”

“Ah. Sorry.”

Mungyeong wore an expression of mixed emotions, then clicked his tongue as he glanced at the river pirates who had approached.

The transformation from a terrifying killing fiend into the Divine Physician’s Disciple and a bright young medical apprentice happened in an instant.

“What were you doing?”

“What business is it of yours?”

“…!”

This was surprisingly fun. But I couldn’t do it three times.

I quickly held out my hand toward the speechless Mungyeong.

“This got into the waistband of my pants.”

That was not entirely true, of course, but Mungyeong did not care about any of that. More precisely, his gaze had locked onto the fragment of the Black Dragon Armor.

“This is…”

“Do you happen to know this item? No, do you recognize it?”

“Where did you get it?”

“From that guy.”

Mungyeong understood that I meant the Western Heaven Demon Lord and nodded.

“You acquired a Divine Weapon. I do not know how only a fragment remains, though.”

“He called it the Black Dragon Armor.”

“The Black Dragon Armor?”

“What? Is that different from the name you knew?”

“I read about it in an old secret history. It was said to be a mysterious armor without a fixed name, one whose form and properties changed according to its owner.”

“Its form and properties change? How?”

Mungyeong answered with a look that suggested I was an idiot.

Only then did I realize what I needed to do.

*Internal energy.*

Internal energy was the very form and nature of its owner.

Ssshhh.

Following the formula of the eighth-stage Fire Gate Divine Technique, I sent lava-like energy flowing toward the fragment of the Black Dragon Armor.

The ink-black energy swirling over the fragment’s surface disappeared, and bluish-white Scorching Yang Qi filled its place.

With a pattern that looked as though flames were blazing across it, the object could no longer be called the Black Dragon Armor.

*Fire Dragon Armor.*

It was simple, but there could be no more fitting name.

At the same moment that I smiled in satisfaction, a cheerful chime rang out.

> **System**
>
> You have given the bound Item ??? a new name!
>
> You can now freely use Fire Dragon Armor anywhere!
>
> Fire Dragon Armor is resonating with your energy! It wants its owner’s strength in order to repair its damaged sections on its own!

Whoosh.

I could feel the vast amount of internal energy leaving my body and rushing toward the Fire Dragon Armor.

I pretended to tuck the energy-draining object into my arms before storing it in my inventory.

*Automatic repair? That’s incredible.*

I had definitely acquired something useful.

Thank goodness the last gift I received on this journey was the Fire Dragon Armor.

Mungyeong stared at me with wide eyes as I turned away.

“Where are you go—where are you headed?”

“What business is it of yours?”

“…”

I was starting to think I might get addicted to this.

I waved at Mungyeong, who was probably repeating the character for patience in his head.

“I’m going to take a nap. Don’t wake me.”

“…?”

Yes. Now it was time to awaken from a long sleep.

But…

*Why do I feel so uneasy? Did I forget something?*

Frowning, I found a place in the fast ship’s cabin and lay down. I closed my eyes, took a deep breath, and spoke the command.

*Logout.*

Ding.

> **System**
>
> Logging out in ten seconds. Ten, nine, eight, seven…

With the final count, the sound of splashing water and someone’s distant cries seeped faintly into my ears.

Splash! Gasp! Captain, save—gasp!

[^1]: The Three Excellencies were the highest-ranking offices in the imperial government.
```
