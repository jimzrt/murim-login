<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0852.txt",
      "sha256": "99ec4af092a8e82cd5c3a2a8ce5aa753791fb49a4e40d7eeee95402c2bfbad2f",
      "bytes": 13478
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "289bb4b08f7cb7c46ad334b3a04441063c7cf1580b1807d5bf9871293f604034",
      "bytes": 1640
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "fcf81807b73428765d3d534c4a0315c8f9b5b9a4a18c914cd12431279d0798f2",
      "bytes": 227824
    },
    {
      "path": "characters/Cheongpung the Ancient Sword.md",
      "sha256": "817b81ade301c6bc75b068b5a96b7231b9c1055e3bf2cd79c6ae340d6e5818be",
      "bytes": 583
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "5563a301b66b39ad68a49562a014901abf3f345379fa40a36925adaee4ad33a0",
      "bytes": 1325
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "e8f936c21be1072de448e18765a1896803034eb0eff6aee7228ffd45512aa7f0",
      "bytes": 759
    },
    {
      "path": "characters/Extinction Divine Nun.md",
      "sha256": "a6f4afee8f838ae16dd75bd11ef11e84525b0a130660cda030ca174bec6b18df",
      "bytes": 655
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "d1ee35de1a793dec27e3fd5caddc44eea365fe4bb7166c48dfc75e34f849a79b",
      "bytes": 686
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "e3e553cbfda399447d4246aa65ffc9c3bd07a6f4b582a602f692d9a33515b988",
      "bytes": 1573
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "a4d26dd5a1c9d2379d9976ae4ed170dcb43199eea94e979487489276de5c1cd6",
      "bytes": 1782
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "a33f5025030e43d7654ec10d573823ac1e0263a761e2d3394083da4ab40f870d",
      "bytes": 622
    },
    {
      "path": "characters/Namho.md",
      "sha256": "4420f04465fd25d478dc678cb16c6641d538deaef06781b65d0e46ef013d6fa8",
      "bytes": 936
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "53e5c95e9b214add5ca56fdc1e8e4ae8b6116ca815ce2134550804f183e8fca4",
      "bytes": 914
    },
    {
      "path": "characters/Tang Sadok.md",
      "sha256": "3100e9cb24cd7ab5889032a1f0646864f968e5e15e79de6a6981afa296bfb079",
      "bytes": 925
    },
    {
      "path": "characters/Wolhwa.md",
      "sha256": "b799e9851415d84a1dbeee5a3958feb66ddfeb52fca105f3baa8727a83a04e93",
      "bytes": 2457
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "e355e81484ae949dc8e78222090e84cb4d51822836709e9b1a9310bffea46b83",
      "bytes": 252668
    }
  ],
  "estimated_tokens": 14460
}
-->

# Durable State Update — Chapter 852

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
1 and safe_through 852. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 852. Profile updates may replace only one
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
  "chapter": 852,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 852,
    "continuity_sources": [852],
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
    "Namho links Blood Soul Gu to the Five Poisons Sect’s ancient war with the Nanman Beast Palace; Jin believes Dark Heaven brought it from Nanman to the Central Plains.",
    "Jin suspects Dark Heaven’s covert killing of the City Lord is part of a scheme targeting the Great Nation, possibly its imperial family.",
    "Jin considers Prince Shangshan Zhu Bao a key to the suspected scheme; the token Zhu Bao gave him seems to tremble inside the Inventory.",
    "Hong Jin asked the Lower District Sect’s Shanxi branch to find Jin Taekyung, whom he trusts to protect Prince Shangshan.",
    "An imperial party took Hong Jin under an imperial decree; Prince Shangshan was unharmed at that moment."
  ],
  "continuity_sources": [
    850,
    851
  ],
  "open_questions": [
    "Why did Dark Heaven secretly kill the City Lord of Sichuan Province?",
    "Is Dark Heaven targeting the Great Nation’s Emperor or imperial family, and what is its intended scheme?",
    "How is Prince Shangshan Zhu Bao connected to the suspected scheme?",
    "What prompted the imperial decree against Hong Jin, and what will happen to him and Prince Shangshan?"
  ],
  "safe_through": 851,
  "temporary_decisions": [
    "Render 혈혼고 as “Blood Soul Gu.”",
    "Render 독혈지 as “Poisonblood Grounds.”",
    "Render 대국 as “Great Nation.”",
    "Render 금의위 as “Embroidered Uniform Guard.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 월화     | **Wolhwa**         |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 하오문    | **Lower District Sect**          |
| 암천     | **Dark Heaven**                  |
| 사천당가   | **Sichuan Tang Clan**            |
| 남만야수궁  | **Nanman Beast Palace**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 기루     | **pleasure house**                               |                                                       |
| 기녀     | **courtesan**                                    |                                                       |
| 가주     | **Family Head**                              |
| 문주     | **Sect Leader**                              |
| 장문인    | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 지부장    | **Branch Leader**                            |
| 선배     | **Senior**                                   |
| 상태               | **Status**                     |
| 산서     | **Shanxi**             |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 안휘     | **Anhui**              |
| 노부      | **this old man / I**                                            |
| 본문      | **our sect / this sect**                                        |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 도사      | **Daoist**                                                      |
| 청풍고검 | **Cheongpung the Ancient Sword** | Alias of the Qingcheng Sect's Sect Leader; distinct from Cheongpung. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 멸절신니 | **Extinction Divine Nun** | Presumed-dead Supreme Peak master and Heaven-Shaking Venerable Nun’s only Senior Aunt. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 당사독 | **Tang Sadok** | Current Family Head of the Sichuan Tang Clan; also called the Myriad-Poison Asura. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 청성파 | **Qingcheng Sect** | Sect named in Baek Museong's comparison about disciplinary rules. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아미타불 | **Amitabha** | Buddhist invocation spoken by the unidentified arriving group. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 절강성 | **Zhejiang Province** | Province where the Geumwa Merchant Group ranks among the top three merchant groups. |
| 후개 | **Successor Beggar** | Title of the Beggars' Sect successor competing in the preliminaries. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 반로환동 | **Returned to Youth** | Possible explanation for an apparently young Supreme Peak master. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 아미파 | **Emei Sect** | Murim sect in Sichuan. |
| 청성 | **Qingcheng** | Short form for Qingcheng Sect. |
| 하오문도 | **Lower District Sect member** | Member of the Lower District Sect. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 당가 | **Tang Family** | Short form for the Sichuan Tang Clan when distinguished from 사천당문. |
| 사천성 | **Sichuan Province** | Province form used in the title of its chief official. |
| 사천성주 | **City Lord of Sichuan Province** | Title held by Won Gyun. |
| 호위장 | **Captain of the Guards** | The Sichuan City Lord's guard captain. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 사천혈사 | **Sichuan Blood Tragedy** | Earlier incident in which Taekyung witnessed the strange formation. |
| 절강 | **Zhejiang** | Region from which the boat travels east. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 독혈지 | **Poisonblood Grounds** | Hidden poisonous region created by the Five Poisons Sect inside Ailao Mountain. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |
| 혈혼고 | **Blood Soul Gu** | Rare gu poison found deep in Nanman. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 월화 | junior_to_older_female_acquaintance | Wolhwa noona | casual-but-junior | Taekyung uses this address while speaking in his sleep or delirium. |
| 월화 | 진태경 | Lower District Sect branch leader to Jin Family young master | Young Master Jin; our Young Master | polite and lightly playful | Uses 우리 공자님, 진 공자, and the teasing 잠룡 공자 while greeting and teasing Taekyung. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 진태경 | 주표 | visitor to prince | His Highness, Prince Shangshan | formal-deferential | Addresses Zhu Bao as 상산왕 전하 after kneeling to meet his gaze. |
| 주표 | 진태경 | prince to visiting young hero | Jin Taekyung | formal and inquisitive | Uses the formal second-person address before asking Taekyung's name and requesting an autograph. |
| 주표 | 청풍 | prince_to_young_martial_artist | you | formal and gatekeeping | Refuses Cheongpung's autograph until he acquires a martial title. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 상인 | 적천강 | merchant_to_legendary_martial_master | Great Hero Jeok | deferential and flattering | Praises Jeok Cheongang while presenting the Poison-Averting Ring and requesting help. |
| 적천강 | 상인 | legendary_guest_to_merchant | you | blunt and transactional | Cuts off the merchant’s praise, asks his identity and origin, and accepts the gift without committing to the requested favor. |
| 점소이 | 상인 | waiter_to_customers | gentlemen | formal-polite | The waiter addresses the merchants as 손님들 while charging them for their supposed friend's bill. |
| 궁기방 | 진태경 | rival_finalists | you bastard | insulting-casual | Gung Gibang answers Taekyung's collective insult with a profane threat. |
| 진태경 | 궁기방 | rival_finalists | you three idiots | insulting-casual | Taekyung addresses Gung Gibang as part of the trio and threatens them before a duel. |
| 진태경 | 당사독 | visitor_to_Sichuan_Tang_Family_Head | Great Hero Tang Sadok | formal-deferential | Taekyung formally introduces himself and addresses Tang Sadok as 대협. |
| 당사독 | 진태경 | Family_Head_to_visiting_younger_martial_artist | you; fearless brat | blunt and threatening | Tang Sadok uses 너 and later calls Taekyung 겁 없는 놈 while rejecting his challenge. |
| 청풍 | 당사독 | young_martial_artist_to_Sichuan_Tang_Family_Head | Family Head | formal-deferential | Cheongpung addresses Tang Sadok as 가주님 while appealing for help. |
| 사천성주 | 진태경 | official_to_imperial_messenger | Messenger of His Highness Prince Shangshan | formal-deferential | The City Lord addresses Taekyung deferentially after seeing Prince Shangshan's Token. |
| 진태경 | 사천성주 | visitor_to_city_lord | City Lord | sarcastic-polite | Taekyung jokingly praises him as our City Lord after making him fund the reward. |
| 호위 | 당사독 | guard_to_Family_Head | Family Head | formal-deferential | Uses 가주님 while reporting Jin Taekyung's request. |
| 당사독 | 청풍 | family_head_to_younger_ally | greenhorn | blunt and protective | Tells Cheongpung not to interfere while calling him a 핏덩이. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |
| 청풍고검 | 진태경 | senior_sect_leader_to_younger_martial_artist | Fellow Daoist Jin | familiar-polite | Cheongpung the Ancient Sword greets Jin as 진 도우. |
| 진태경 | 청풍고검 | younger_martial_artist_to_senior_sect_leader | Perfected One | formal-deferential | Jin greets the Qingcheng Sect Leader as 진인. |
| 멸절신니 | 진태경 | senior_sect_leader_to_younger_martial_artist | Benefactor Jin | familiar-polite | Extinction Divine Nun addresses Jin as 진 시주. |
| 청풍고검 | 멸절신니 | sect_leader_to_senior_sect_leader | Venerable Nun | formal-deferential | Cheongpung the Ancient Sword addresses her as 신니 while praising Jin and Cheongpung. |
| 사천성주 | 호위장 | provincial_city_lord_to_guard_captain | Captain of the Guards | imperious and dismissive | The City Lord directly orders the Captain of the Guards to handle the troops stationed near Chengdu. |
| 적천강 | 궁기방 | overwhelming_elder_to_younger_martial_artist | you | blunt and threatening | Jeok Cheongang rebukes Gung Gibang for speaking informally and orders him to lie down. |
| 남호 | 진태경 | Hidden_Shadow_Pavilion_agent_to_mission_leader | Jin Taekyung / you | guarded and familiar | Namho addresses Taekyung as 자네 while explaining the contact and offering guidance. |
| 진태경 | 남호 | mission_leader_to_hidden_shadow_agent | you / Namho | probing and respectful | Taekyung questions Namho’s affiliation and later discusses Dark Heaven’s threat to Nanman. |
| 적천강 | 호위장 | martial artist to official subordinate | you; bastard | blunt and threatening | Jeok uses familiar, insulting address while interrogating the Captain of the Guards. |
| 호위장 | 적천강 | official subordinate to senior martial artist | Sir | deferential | The Captain shifts to respectful speech after sensing Jeok’s status and danger. |
| 호위장 | 남호 | government guard captain to visiting martial artist | Great Hero Nam | formal and courteous | The Captain of the Guards identifies Namho by his title while recognizing him among Jin Taekyung’s companions. |

## Listed compact profiles

### Cheongpung the Ancient Sword.md

# Cheongpung the Ancient Sword (청풍고검)

- **Safe through:** Chapter 373
- **Aliases:** None
- **Role:** Sect Leader of the Qingcheng Sect and a Supreme Peak martial artist investigating Dark Heaven's strange formation alongside Extinction Divine Nun.
- **Personality:** Straightforward, genial, and willing to help with matters he considers worthwhile.
- **Voice:** Warm, plainspoken, and good-humored.
- **Relationships:** He is investigating Dark Heaven's strange formation alongside Extinction Divine Nun.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 848
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak martial master known as the Huashan Divine Dragon, the creator of the snake-inspired Mimi Step footwork technique, and the master of the Azure Dragon Pavilion within the Alliance Leader's Two Dragons Pavilion.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi, now a large horned snake, to him, and Cheongpung is accompanying Mungyeong while learning his martial arts through observation to become stronger and adapt to this world.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 851
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Extinction Divine Nun.md

# Extinction Divine Nun (멸절신니)

- **Safe through:** Chapter 373
- **Aliases:** None
- **Role:** Living Emei Sect Leader and Supreme Peak master who joins Cheongpung the Ancient Sword in investigating a strange formation linked to Dark Heaven.
- **Personality:** Not established beyond the fear and shock her sudden reappearance caused among the Emei disciples and the Third Fiend.
- **Voice:** Not established.
- **Relationships:** She is Heaven-Shaking Venerable Nun’s only Senior Aunt and was believed to have died after withdrawing from worldly affairs thirty years earlier.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 671
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung, uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and Dark Heaven’s Hubei forces, and has now found a trace of Honglan.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 850
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; they trust each other deeply but have never formalized their bond. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to the late Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and is a long-standing rival of Peng Cheolhu.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 851
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; they trust each other deeply, though their bond remains unformalized. Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master; Ju Hwaran is a trusted Fire Dragon Pavilion member; Magic Johnson and Chuck Hagel are allied to him; his mother and sister Hayeon are among those he protects; the Skeleton King is his friend and ally; Xiao Shen regards him as an older brother; Jin-ho is his older friend and trusted confidant; he once saved Ju Wongong’s life.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 851
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 850
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 851
- **Aliases:** None
- **Role:** The City Lord and a member of the imperial family; ten-year-old Prince Shangshan, whose personal name is Zhu Bao, is an exceptionally skilled young swordsman who has trained daily for three years.
- **Personality:** Earnest, admiring, and eager to emulate Jin Taekyung; despite his royal dignity, he shows openly childlike enthusiasm for martial arts and Taekyung's reputation.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor's only younger full brother, and his token commands immediate deference from distant imperial relatives such as Ju Wongong; he admires Jin Taekyung and seeks to emulate him.

### Tang Sadok.md

# Tang Sadok (당사독)

- **Safe through:** Chapter 846
- **Aliases:** Myriad-Poison Asura
- **Role:** Current Family Head of the Sichuan Tang Clan, overseeing its recovery and relying on allied martial artists to help treat patients and guard against another Dark Heaven attack.
- **Personality:** Blunt and unsentimental, yet grateful to those who remain with the Tang Clan; he has consciously chosen to change and speaks candidly about the clan’s vulnerability.
- **Voice:** Hissing, curt, authoritative, and threatening.
- **Relationships:** Tang Taesang was his father and predecessor, his unnamed nephew serves as Master of the Gatekeeper Pavilion, Mimi is his cherished old friend and companion temporarily entrusted to Cheongpung, and he regards Jin Taekyung and Cheongpung as benefactors, openly welcoming Jin with a warmth he usually conceals.

### Wolhwa.md

# Wolhwa (월화)

- **Safe through:** Chapter 454
- **Aliases:** Eun Sowol (은소월); Wolhwa is the name used at Honghwaru
- **Role:** Shanxi’s foremost information merchant and Level 50 martial artist; Branch Leader of the Lower District Sect’s Shanxi branch with authority to mobilize more than thirty Shanxi branches; formerly posing as a high-ranking courtesan at Honghwaru, a pleasure house in central Taiyuan
- **Personality:** Striking, composed, observant, direct, quietly amused, and capable of ruthless, decisive violence when extracting information; comfortable teasing Taekyung while conducting serious information and negotiation work
- **Voice:** Polite and lightly playful; addresses Taekyung as Young Master Jin and delivers embarrassing observations without raising her voice
- **Relationships:** Knows Taekyung as a Honghwaru regular and the youngest son of the Jin Family; says she likes him, though her sincerity is unclear; has negotiated a mutually beneficial alliance with Jin Wikyung and the Jin Family

## Korean source

```text
＃852화



무림인이 정보를 얻는 방법을 지극히 한정되어 있다.

우선 첫 번째로 가장 만만한 것은 바로 객잔과 기루다.

다양한 직업군을 가진 인간군상들이 가득 차 있다 보니 조금만 귀를 기울여도 수많은 이야기를 들을 수 있다.

단점이 있다면 그중에 정작 중요한 정보는 없고, 대부분이 확인되지 않은 헛소문이라는 것이다.

그래서 머리가 장식품이 아니고, 칼밥 좀 먹었다 싶은 무림인들은 정보 상인들을 찾아간다.

전문적으로 정보를 사고파는 그들은 각 지역마다 존재하며, 상당한 금액을 부르는 만큼 정보의 신빙성도 높다.

문제는 그들이 정보를 수집할 수 있는 한계가 명확하다는 것이다.

자리 잡은 지역에 한해서는 질 높은 정보를 제공할 수 있지만, 결국 딱 거기까지다.

그렇기에 돈 많고, 적당히 괜찮은 문파 출신에 어느 정도의 연줄이 있는 이들의 발걸음은 자연스럽게 두 갈래로 나뉘기 마련이었다.

하오문(下汚門).

그리고 개방(丐幇).

천하 곳곳에 뿌리내린 이들. 하나둘 모여 자신들만의 거대한 숲을 일군 이 땅의 잡초들.

구파일방 중 하나인 개방이야 말할 것도 없지만, 하오문도 결코 무시할 수는 없는 세력이다.

점소이와 기녀, 마부와 소매치기. 뒷골목의 도박꾼에 크고 작은 점포를 운영하는 상인들까지.

개방의 거지들처럼, 세상 어디에나 그들이 있다.

그렇게 방대한 정보망을 바탕으로 천하를 그물질하며 숱한 정보를 건져 올리니, 설령 무림에서 손꼽는 명문대파(名門大波)의 장문인이라 해도 그들을 함부로 대할 수는 없었다.

물론, 어느 경우에나 예외는 있기 마련이다.

“집합.”

“예?”

“집합. 반나절 준다. 사천당가로.”

적어도 오늘만큼은 적천강이 대마도사였다.

정확히 반나절 만에 하오문과 개방, 거기에 더해 청성파와 아미파까지 한 자리에 불러 앉혔으니까.

“아니, 갑자기 무슨 이유로 부르신 건지…….”

“조용히 구석에 처박혀 앉아 있어라. 네놈도 들어야 하니까.”

물론 사천당가의 가주인 당사독도 함께였다.

하지만 적천강을 제외한 모두를 놀라게 했던 것은, 청성과 아미에서 장문인이 직접 행차했다는 사실이었다.

“무림말학 벽운자(碧雲子)가 노 선배께 인사 올립니다.”

청성파 장문인이고 나발이고, 적천강 앞에서는 무림말학이다.

발바닥에 땀이 나도록 달려온 기색이 역력한 벽운자. 아니 무림에는 청풍고검(靑風高劍)이라는 별호로 잘 알려진 그의 포권지례에 적천강이 고개를 끄덕였다.

“그래, 네 스승은 요즘도 잘 지내고?”

“……이미 이십 년 전에 돌아가셨습니다만.”

잠시 침묵하던 적천강이 눈 하나 깜짝하지 않고 입을 열었다.

“벌초 상태를 물어본 게다. 아무리 바빠도 자주자주 찾아가서 잡초도 뽑고 해.”

“……예. 명심하겠습니다.”

누가 봐도 까먹은 게 틀림없었지만, 청풍고검은 도인다운 인내심을 발휘하며 자리에 앉았다.

아니, 이건 그냥 상대가 화왕 적천강이라 넘어갔다고 봐야 한다.

무림에서 따지는 배분으로는 따라올 자가 없고, 연배며 무공까지 압도적이니까.

그러나 사천혈사 이후 공석이 된 아미파의 장문직을 맡게 된 멸절신니(滅絶神尼)는, 그 연배로 인해 적천강으로서도 함부로 대할 수 없는 인물이었다.

“왔소. 할망구.”

“…….”

“…….”

정정한다. 그냥 내 착각이었던 것 같다.

‘존나 함부로 대하네, 진짜.’

나는 이마를 짚었고 다른 이들은 입을 딱 벌렸다.

그나마 다행인 것은, 전장에서 미친 듯이 날뛰기로 유명한 멸절신니가 평소에는 지극히 온화한 성품의 소유자라는 것이었다.

“적 시주는 언제 만나도 참 여전하구려. 여러 의미로.”

“할망구는 못 본 사이 더 늙었군. 넉 달이 아니라 사십 년 만에 다시 만난 기분이오. 있는 그대로의 의미로.”

“아미타불. 그 나이면 진즉 어른이 되고도 남았을 텐데, 그대는 언제쯤 철이 들 거요?”

“얼추 백 년쯤 어려졌으니 앞으로 백 년은 더 이렇게 살 예정이오. 물론 그때는 신니가 이 세상 사람이 아니겠지만.”

“……아미타불. 말이 너무 심하구려.”

“억울하면 당신도 반로환동하든지.”

“아미타부우우울!”

좆 됐음을 감지한 나는 황급히 두 사람 사이를 가로막았고 그건 최고의 선택이었다.

한 마디만 더 섞었어도 멸절신니의 목탁이 적천강의 뚝배기로 내리꽂혔을 테니까.

물론 곧이곧대로 맞아 줄 적천강은 아니지만, 중요한 건 내 등장으로 멸절신니의 분노가 급격하게 가라앉았다는 점이었다.

“오, 진 시주.”

“잘 지내셨습니까. 신니. 아니, 장문인.”

“너무 불편해할 필요 없으니 편히 부르시게. 그나저나 못 본 사이 더욱 헌앙해지셨군. 머리털도 풍성하고.”

적천강을 바라보며 뒷말을 덧붙인 멸절신니는 주름이 자글자글한 손으로 내 어깨를 두드렸다.

사천혈사 당시 조금이라도 피해를 줄이기 위해 동분서주한 나를 매우 좋게 봐서인지, 청풍고검이나 그녀나 눈에서 꿀이 뚝뚝 떨어져 내렸다.

“우선 이야기를 나누기에 앞서 참으로 고생 많았네. 남만에서 암천의 마두들을 상대로 크게 활약하고, 남만야수궁을 입맹(入盟) 시켰다지?”

“진 도우의 협기(俠氣)가 실로 대단하네. 빈도 역시 감탄을 금치 못했어.”

두 다리 없이도 능히 천 리를 가는 것이 바로 말이다.

어느 정도 정보력을 갖춘 이들 사이에서는 이미 알음알음 이야기가 돌고 있었고, 오늘 이 자리에 모인 사람들은 말할 것도 없었다.

구파일방에 속한 장문인 둘. 그리고 천하제일을 다투는 정보 단체의 수뇌부들까지 와 있으니까.

“늦었지만 감축드립니다, 진태경 대협. 본문의 섬서지부장께서도 그 소식을 듣고 참으로 기뻐하셨습니다.”

“궁기방 그 녀석, 아니 후개(後丐)가 자네의 절반이라도 따라갔으면 좋겠군. 여하튼 대단해.”

하오문의 사천지부장은 섬서에 있을 월화를 언급하며 공손히 축하 인사를 건넸고, 개방의 장로는 껄껄 웃으며 내 옆구리를 찌르다가 적천강의 한마디에 웃음을 뚝 멈췄다.

“방주는 어디 가고 장로 나부랭이가 얼쩡거려?”

“……저, 적 대협. 아무리 그래도 하남에 계신 방주를 어떻게 반나절 만에 모셔 옵니까.”

“하남? 그놈이 지금 하남에 있어?”

“예.”

사실 하남에서 사천까지 반나절 만에 오려면 제트기를 타지 않는 이상 불가능하다.

그 말이 일리가 있다 여겨졌는지 적천강은 다른 먹잇감을 물색했다.

“마, 하오문.”

“옙.”

“문주는?”

“마음 같아서는 모셔 오고 싶은 마음이 굴뚝 같지만, 어디 계신지는 저도 모릅니다. 점조직으로 이루어진 본문의 사정상 극비 중의 극비라…….”

“그래서, 문주가 어디 있는지도 모르는 말단이 나왔다?”

수많은 문도를 거느린 하오문에서 지부장급이라면 개방의 장로나 마찬가지다. 사천지부장은 적천강의 압박에 마른침을 꿀꺽 삼켰다.

“그럴 리가 있겠습니까. 원하시는 정보라면 뭐든! 무슨 수를 써서라도 알아내어 최대한 빠르게 알려 드리겠습니다!”

“뭐든. 무슨 수를 써서라도 빠르게?”

“옙.”

“그거 썩 괜찮군. 노부가 똑똑히 기억해 둘 테니 네놈도 이것 하나만 기억해라. 알겠느냐?”

“그게 무슨 말씀이신지…….”

하오문 사천지부장의 눈빛이 흔들린 그때. 깊게 가라앉은 적천강의 목소리가 나직이 울려 퍼졌다.

“만약 오늘 이 자리에서 나오는 이야기가 단 하나라도 외부에 알려졌다가는…….”

화아아악.

뒷말은 이어지지 않았지만, 그것만으로도 충분했다.

적천강을 중심으로 흘러나온 무시무시한 기파(氣波)는 무언의 경고였다. 그럴 리는 없겠지만 만에 하나 일어날 불상사를 대비한 경고.

그리고 그 뜻을 알아차리지 못할 만큼 눈치 없는 이들은 단 한 명도 없었다.

그만큼 중요한 이야기가 시작되리라는 것 역시도.

“오늘 정오 무렵에, 사천성주가 죽었다.”

적천강의 첫 마디를 시작으로 무대의 막이 오른다. 때맞춰 앞으로 나선 신의와 남호를 향해 모든 시선이 쏠렸다.

“죽은 성주의 사인(死因)은 병사입니다. 지난 몇 달간 심신의 기력이 급격히 쇠한 탓에 벌어진 일이지요.”

“인근의 명의들이 이미 성주부에서 시신을 확인했고, 여기 계신 신의께서도 그리 결론 내리셨소.”

내가 나직이 덧붙였다.

“아무런 의심의 여지도 없는 병사. 그렇게 알려질 겁니다. 적어도 공식적으로는.”

주위의 공기가 흔들리는 것이 느껴진다.

공식적으로는.

누가 들어도 의미심장한 말이다. 저 짧은 한마디에는 외부에는 알려지지 않은 비밀이 존재한다는 뜻이 담겨 있으니까.

그리고 내가 조용히 건넨 눈짓에, 고개를 끄덕인 신의가 품에서 작은 목함을 꺼내 조심스럽게 열었다.

“혈혼고(血魂蠱)라 불리는 것입니다.”

지금까지 봤던 어느 벌레보다 작고, 핏물처럼 붉은 그것을 확인한 사람들의 눈동자가 크게 뜨였다.



* * *



모두가 떠났을 때쯤에는 이미 어두운 저녁이었다.

나는 단둘이 남게 된 적천강과 함께, 사방에 내려앉은 새카만 어둠을 바라보며 대화를 나누었다.

“얼마나 걸릴까요?”

“그 누가 알겠느냐. 남은 것은 믿고 기다리는 것뿐이지.”

“기다리면 늦습니다. 움직여야 해요.”

“길을 한번 잘못 들었다간, 돌아오는 시간이 더 걸릴 것이다. 더군다나 이미 그들의 정보로 어느 정도의 소득을 얻지 않았더냐?”

나는 말 없이 고개를 끄덕였다.

적천강의 말대로, 이미 하오문과 개방을 통해 입수된 정보가 있었다.

‘금의위(錦衣衛).’

이 땅에 살아가는 이들이라면 모를 수 없는 그 이름.

오직 한 사람의 명령에 따라 움직이는, 대국(大國)에서 가장 강력하고 비밀스러운 집단 중 하나.

그들이 모습을 드러냈다. 그것도 이미 우리가 사천에 도착하기 한참 전에.

대국의 수도이자 천자가 머무르는 황도가 위치한 절강성(浙江省)도 아닌 안휘성에서.

‘심지어 평소와 달리 변복(變服)까지 한 상태였다고 했지.’

황제 직속 기관인 금의위가, 그것도 신분까지 바꿔 가며 안휘성에 나타난 이유가 무엇이었을까.

냄새를 맡고 그들의 뒤를 쫓던 정보원들이 살해당한 채 발견되었기 때문에 더 이상의 진실은 알려지지 않았으나, 나는 문득 불길한 가정을 떠올릴 수밖에 없었다.

‘만약 그들이 안휘에서 멈추지 않고, 계속해서 북서쪽으로 거슬러 올라갔다면…….’

그곳이 바로 산서성이고, 산서성에는 바로 그가 있다.

‘상산왕(上山王) 주표.’

황위를 둘러싸고 벌어진 끔찍한 권력 다툼 속에서 지금의 천자가 승리한 후 유일하게 살려 두었던 황실의 직계 혈족.

천하에 단 하나뿐인 번왕(藩王)이자, 현재로서는 후사가 없는 천자의 뒤를 이을 대국의 후계자.

‘그런데 잠잠하던 황제가 금의위를 움직였다. 그것도 이리 은밀하게.’

만약 금의위의 목적지가 산서성이라면…… 나로서는 최악의 상황을 예견할 수밖에 없었다.

바로 대국의 황실에까지 암천의 그림자가 드리워졌다는 것을.

‘호위장은 사천성주는 천자에게 애첩을 빼앗긴 직후부터 광증(狂症)을 보였다고 했지. 그 성주의 몸 속에서 나온 혈혼고는 내가 남만의 독혈지에서도 보지 못했을 만큼 희귀한 고독이고.’

증거는 충분하다. 나는 흐릿한 달빛만이 비추는 밤하늘을 말없이 노려보았다.

어디에도 닿지 않을 물음과 함께.

‘도대체 뭘 노리는 거냐.’

그리고 그 순간.

하늘 어디에선가 들려온 미세한 소음이 내 귓가에 닿았다.

아니, 우리 둘 모두의 귓가에 닿았다.

푸득.

“노야.”

“이건…….”

바람 소리가 아니다. 바람을 가르며 날아드는 무언가의 날갯짓 소리다.

‘전서구!’

깨달음과 동시에, 나와 적천강은 하늘 저편을 응시했다. 그리고 눈을 부릅떴다.

쉬이이익!

세차게 바람을 가르며 이곳을 향해 날아드는 새의 그림자는, 무려 십여 마리에 달했다.
```

## Final English reading copy

```markdown
# Chapter 852

The ways a Murim martial artist could get information were extremely limited.

The easiest place to start was an inn or a pleasure house.

They were packed with all kinds of people from all kinds of professions, so you could hear countless stories just by listening a little.

The downside was that none of the important information was there. Most of it was unverified rumor.

So martial artists with heads that weren’t just for decoration, and who’d spent some time earning their keep with a sword, went to information merchants instead.

These professionals bought and sold information in every region. Their prices were steep, but their information was reliable.

The problem was that there were clear limits to what they could gather.

They could provide high-quality information about the region where they were based, but that was as far as it went.

And so, the paths of those with money, a respectable sect behind them, and a few useful connections naturally split in two.

The Lower District Sect.

And the Beggars’ Sect.

They had taken root throughout the land. The weeds of this world, gathering one by one until they’d grown into vast forests of their own.

The Beggars’ Sect was one of the Nine Sects and One Gang, so there was no need to explain its importance. But the Lower District Sect was a force that couldn’t be dismissed, either.

Waiters and courtesans, coachmen and pickpockets. Back-alley gamblers and merchants running shops of every size.

Like the beggars of the Beggars’ Sect, they were everywhere in the world.

With such vast networks, they combed the land and hauled in information by the basketful. Even the Sect Leaders of the most prestigious Murim sects couldn’t treat them carelessly.

Of course, there were exceptions to every rule.

“Gather everyone.”

“Pardon?”

“Gather everyone. You have half a day. To the Sichuan Tang Clan.”

At least for today, Jeok Cheongang was a Grand Mage.

In precisely half a day, he’d summoned the Lower District Sect and the Beggars’ Sect, along with the Qingcheng and Emei Sects, and seated them all in one place.

“Um, may I ask why you’ve called us here so suddenly…?”

“Quietly plant yourself in a corner and sit there. You need to hear this, too.”

Of course, Tang Sadok, the Family Head of the Sichuan Tang Clan, was there as well.

But what surprised everyone except Jeok Cheongang was that the Sect Leaders of Qingcheng and Emei had come in person.

“I, Bicheonja of the Qingcheng Sect, a junior of the Murim, pay my respects to you, Senior.”

Sect Leader of the Qingcheng Sect or not, in front of Jeok Cheongang, he was a junior of the Murim.

Bicheonja was clearly fresh from a desperate, sweat-soaked dash. Jeok Cheongang nodded at his cupped-fist greeting. No—at the greeting of Cheongpung the Ancient Sword, as he was better known in the Murim.

“So, is your master still doing well these days?”

“……He passed away twenty years ago.”

After a brief silence, Jeok Cheongang spoke without batting an eye.

“I was asking whether you’ve been tending his grave. No matter how busy you are, visit often and pull the weeds.”

“……Yes. I’ll remember that.”

Anyone could see Jeok Cheongang had forgotten, but Cheongpung the Ancient Sword showed the patience of a Daoist and took his seat.

No, maybe it was more accurate to say he let it slide because his opponent was the Fire King, Jeok Cheongang.

There was no one in the Murim who could match his seniority, and he was overwhelming in both age and martial arts.

But Extinction Divine Nun, who’d taken the vacant post of Emei Sect Leader after the Sichuan Blood Tragedy, was someone even Jeok Cheongang couldn’t treat carelessly—at least, given her age.

“You’re here, old hag.”

“……”

“……”

I take it back. I must’ve been mistaken.

*He’s treating her however the fuck he wants. Seriously.*

I pressed a hand to my forehead, while everyone else’s mouths fell open.

At least there was one saving grace: Extinction Divine Nun, who was famous for rampaging like a madwoman on the battlefield, was usually an exceptionally gentle person.

“Benefactor Jeok, you’re just as I remember you, no matter how long it’s been. In more ways than one.”

“Old hag, you’ve gotten older since I last saw you. It feels like forty years, not four months. I mean that literally.”

“Amitabha. At your age, you should’ve grown up long ago. When are you going to start acting your age?”

“I’ve grown about a hundred years younger, so I plan to live like this for another hundred. Though by then, Venerable Nun, you’ll no longer be of this world.”

“……Amitabha. That was too harsh.”

“If you’re that offended, you should Return to Youth yourself.”

“Amitabhaaaaa!”

I sensed we were in deep shit and hurriedly stepped between them. It was the best move I could’ve made.

If they’d traded one more line, Extinction Divine Nun’s wooden prayer block would’ve come down on Jeok Cheongang’s skull.

Of course, Jeok Cheongang wouldn’t have just let her hit him. The important thing was that Extinction Divine Nun’s anger quickly subsided when I appeared.

“Oh, Benefactor Jin.”

“Have you been well, Venerable Nun? No—I mean, Sect Leader.”

“You needn’t be so formal. Call me whatever feels comfortable. In any case, you’ve become even more striking since I last saw you. And your hair’s still so thick.”

Extinction Divine Nun added that last part while glancing at Jeok Cheongang, then patted my shoulder with her wrinkled hand.

Perhaps because she’d thought so highly of the way I’d rushed around trying to minimize the damage during the Sichuan Blood Tragedy, both she and Cheongpung the Ancient Sword were looking at me with stars in their eyes.

“Before we begin, I must say you’ve been through a great deal. I hear you distinguished yourself against Dark Heaven’s fiends in Nanman and even brought the Nanman Beast Palace into the alliance?”

“Fellow Daoist Jin’s chivalrous spirit is truly remarkable. I, too, can’t help but admire you.”

Words could travel a thousand li without legs.

Word had already spread among those with even a halfway decent information network. And that went double for the people gathered here today.

Two Sect Leaders from the Nine Sects and One Gang, not to mention the heads of the most powerful information organizations in the land.

“Congratulations, though belated, Great Hero Jin Taekyung. Our Shaanxi Branch Leader was delighted when he heard the news.”

“I only wish that brat Gung Gibang—or rather, the Successor Beggar—could follow your example, even halfway. Anyway, what you did was incredible.”

The Lower District Sect’s Sichuan Branch Leader politely offered his congratulations, mentioning Wolhwa, who was in Shaanxi. An Elder of the Beggars’ Sect chuckled and jabbed me in the side, but at a single remark from Jeok Cheongang, his laughter stopped dead.

“Where’s the Sect Leader? Why’s some no-name Elder hanging around?”

“……Sir Jeok, even so, how could we bring the Sect Leader from Henan in half a day?”

“Henan? Is that bastard in Henan right now?”

“Yes.”

Getting from Henan to Sichuan in half a day would’ve been impossible without a jet.

Jeok Cheongang seemed to accept that the Elder had a point and started looking for another target.

“Hey, you. Lower District Sect.”

“Yes, sir.”

“Where’s the Sect Leader?”

“I’d be more than happy to bring him here, but even I don’t know where he is. Our sect is organized into cells, so his location is top secret…”

“So a nobody who doesn’t even know where his own Sect Leader is showed up?”

For a Lower District Sect with countless members, a Branch Leader was on the same level as a Beggars’ Sect Elder. The Sichuan Branch Leader swallowed hard under Jeok Cheongang’s pressure.

“Of course not. Whatever information you want, we’ll get it by any means necessary and bring it to you as quickly as we can!”

“Whatever you want. By any means necessary. As quickly as you can?”

“Yes, sir.”

“That sounds pretty good. I’ll remember it clearly, so you remember this one thing, too. Understand?”

“I’m not sure what you mean…”

The Lower District Sect Branch Leader’s eyes wavered. Just then, Jeok Cheongang’s voice rang out, low and heavy.

“If even a single word of what’s said here today gets out…”

Whoooosh.

He didn’t finish the sentence, but he didn’t need to.

The terrifying wave of energy that rolled out from Jeok Cheongang was a wordless warning—a precaution against the unlikely but possible mishap.

And there wasn’t a single person here too slow to understand what he meant.

They all understood that something important was about to be discussed.

“Around noon today, the City Lord of Sichuan Province died.”

With Jeok Cheongang’s first words, the curtain rose. Every eye turned toward the Divine Physician and Namho as they stepped forward.

“The late City Lord died of illness. His physical and mental strength had declined sharply over the past few months, and that led to his death.”

“The renowned physicians in the area have already examined the body at the City Lord’s Residence and reached the same conclusion. The Divine Physician here has as well.”

I added quietly, “There’s no room for suspicion. It’ll be reported as a natural death. At least, officially.”

I could feel the air around us shift.

*Officially.*

Anyone could tell those words carried weight. They implied a secret that wasn’t meant to reach the outside world.

At my subtle glance, the Divine Physician nodded, took a small wooden case from his robe, and carefully opened it.

“This is known as Blood Soul Gu.”

The people who saw it stared wide-eyed. It was smaller than any bug I’d ever seen, and red as spilled blood.

* * *

By the time everyone had left, evening had fallen.

Jeok Cheongang and I were the only ones left. We stood together, looking out at the pitch-black darkness all around us as we talked.

“How long do you think it’ll take?”

“Who can say? All we can do now is trust them and wait.”

“If we wait, we’ll be too late. We need to move.”

“If we take one wrong turn, it’ll take even longer to get back. Besides, haven’t we already gained something from their information?”

I nodded without a word.

Just as Jeok Cheongang said, we’d already received information from the Lower District Sect and the Beggars’ Sect.

*The Embroidered Uniform Guard.*

No one living in this land could fail to recognize that name.

One of the Great Nation’s most powerful and secretive forces, acting only on the orders of a single person.

They’d shown themselves—and well before we arrived in Sichuan.

In Anhui Province, not Zhejiang Province, where the Great Nation’s capital and the Emperor’s residence were located.

*And they’d been disguised, unlike usual.*

Why had the Embroidered Uniform Guard—an agency directly under the Emperor—appeared in Anhui Province, even changing their identities?

We had no way to learn more. The informants who’d caught their scent and followed them had been found dead. But I couldn’t help making a grim assumption.

*If they hadn’t stopped in Anhui and had kept heading northwest…*

That would take them to Shanxi Province. And he was in Shanxi Province.

*Prince Shangshan, Zhu Bao.*

The only direct member of the imperial family the current Son of Heaven had spared after winning the horrific power struggle over the throne.

The only vassal king in the land, and—since the Son of Heaven had no heir—the current successor to the Great Nation’s throne.

*But the Emperor, who’d been quiet until now, has set the Embroidered Uniform Guard in motion. And so secretly, too.*

If their destination was Shanxi Province… I couldn’t help anticipating the worst.

That the shadow of Dark Heaven had reached the Great Nation’s imperial family.

*The Captain of the Guards said the City Lord of Sichuan Province had started showing signs of madness after the Son of Heaven took his favorite concubine. And the Blood Soul Gu found in his body was so rare that I’d never even seen one in the Poisonblood Grounds in Nanman.*

There was enough evidence. I silently stared up at the night sky, lit only by the hazy moonlight.

A question that would reach no one.

*What the hell are you after?*

And then, at that very moment—

A faint sound came from somewhere in the sky and reached my ears.

No. It reached both our ears.

Flutter.

“Old Master.”

“This is…”

It wasn’t the wind. Something was flying toward us, beating its wings through the air.

*A messenger pigeon!*

The moment I realized it, Jeok Cheongang and I both looked toward the distant sky. Our eyes widened.

Whooosh!

The shadow of a bird raced toward us, slicing through the wind. There were more than ten of them.
```
