<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0493.txt",
      "sha256": "36f418bb0cc68029e9c0e67bedf364a5531eb7299e01895eb349a08cc625d0d3",
      "bytes": 13433
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b183906c24bbb727251d2f52599877ce0e65ac8835848a1f3d1a04c2e5c6ecf2",
      "bytes": 4359
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "71caa938c88fc9963a8a5f7d5e44f28b779026105d5cfc40328c71f2f6b13eea",
      "bytes": 157207
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "d3860665e51f7c594f184801895b4591bb2712b120cf960f8771dd97824503ba",
      "bytes": 1006
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "6b31e33902e7e42ebc08fce6254137702e8fbf0d6f3e9ea11f9da00dc8c41e75",
      "bytes": 553
    },
    {
      "path": "characters/Hyeongong.md",
      "sha256": "91a0e58acc7d0d0d51ed0983aad4163d10de4d2ebe7c91d64614f09fdc803150",
      "bytes": 768
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "739f2bf7547bf8fb14e7d2bfdcbbed849a63b03da49611c1cfe5ed2ae9036321",
      "bytes": 1108
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "43bc64331bfa1b0cebe5aba4ced9de476375057f273bc5ecd0b2f526528231f8",
      "bytes": 1777
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "452ae85f335e813cc076c99f25ce62cf3d0e37a94dd326664c9c8ea0d7b3413c",
      "bytes": 622
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "ad419c7bc243e08e878c8787bce89ea6fcf006f3900c0ede92d0b6a3e6499fd1",
      "bytes": 885
    },
    {
      "path": "characters/Zhuge Feng.md",
      "sha256": "3c11835053bbb8b614abe6eaa0b72ff1edea0a6846e5fe3894bea837291fec20",
      "bytes": 649
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "75d2fc0e87a4c34f13935fced5c1c68cdcadc831e21af3bd589a931a711c934e",
      "bytes": 153277
    }
  ],
  "estimated_tokens": 12471
}
-->

# Durable State Update — Chapter 493

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 493. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 493. Profile updates may replace only one
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
  "chapter": 493,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 493,
    "continuity_sources": [493],
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
    "The functionally crippled Gate continues leaking faint mana; its residual mana is mutating local life, and the Water God Dragon absorbed all of that mana.",
    "Around one hundred Level 5 Mutated Minnows, locally called Blood Fish, have been captured in the Gate's entrance waterways; the remaining population is unknown, and the fish fight and kill one another.",
    "Taekyung suspects Dark Heaven's regeneration, teleportation, and Moving Formation are manifestations of Magic connected to the Gate.",
    "Taekyung told Jeok that he came from another world, that an evil force from it is linked to Dark Heaven, that the corrupted imugi was their work, and that a fully opened Gate could release monsters.",
    "Honglan corrupted the benevolent Dongting Lake imugi and used it to kill many people; the severely injured Dongting Fisherman may be connected to Dark Heaven and the earlier destruction inside the secret refuge.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Wikyung and Gung Gibang pledged the Jin Family of Taiyuan and the Beggars' Sect to Taekyung's defense.",
    "Jeok's innate qi is damaged and steadily diminishing despite the Thousand-Year Snow Ginseng and the Divine Physician's treatment.",
    "Mungyeong is the Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history; before becoming the Slaughter Saint, he was called Killing Ghost, and he saved countless people as the Divine Physician.",
    "Mungyeong has agreed to teach Taekyung his secret martial arts without forming a formal Master-Disciple relationship and is testing him through successive poisoned traps; Taekyung has survived the first night's traps and has now been affected by Potent Energy-Dispersing Poison.",
    "Jeok has withdrawn from the Water God Dragon expedition and told the group not to seek him until everything is finished.",
    "The Water God Dragon's spirit has departed; its enormous corpse remains at Dongting Lake and is now being negotiated as spoils for dismantling and distribution."
  ],
  "continuity_sources": [
    492,
    491
  ],
  "open_questions": [
    "What lies beyond the exposed Gate, why has it lost most of its functions, and how far has its residual mana's mutation spread?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the Dongting Fisherman's exact role within Dark Heaven, and how was he connected to the earlier destruction inside the secret refuge?",
    "What further poison tests will Mungyeong impose on Taekyung, and what secret martial arts will he teach him?"
  ],
  "safe_through": 492,
  "temporary_decisions": [
    "Render 산공독 as Energy-Dispersing Poison, 강력한 산공독 as Potent Energy-Dispersing Poison, 고기 방패 as Meat Shield, 독 장아찌 as Poisoned Pickle, and 독의 as Poison Physician; retain secret martial arts, Master-Disciple relationship, Killing Ghost, and Fake Murim Martial Artist, and preserve 악 as Agh in the Quest interface.",
    "Render 기억의 파편 as Memory Fragment, 게이트 공략 as Gate Conquest, 텔레포트 as Teleport, 마법 as Magic, 혈어 as Blood Fish, and 변이된 송사리 as Mutated Minnow; render 강력한 마비산 as Potent Paralysis Powder, 강력한 미혼산 as Potent Soul-Bewitching Powder, 전신 마비 as Full-Body Paralysis, 독성 흡수 as Poison Absorption, and 해독 as Detoxification.",
    "Render 시산혈해 as sea of corpses and blood and retain Old Master for 노야 with the established rough, profane Taekyung-Jeok banter; render 해시 as hour of the Pig, 한 식경 as half an hour, 타구봉 as Dog-Beating Staff, 창룡 as Azure Dragon, and 무량수불 as Infinite Life Buddha.",
    "Render 선천지기 as innate qi, 진원진기 as true-origin qi, and 천기 as heavenly patterns.",
    "Render 심마 as Heart Demon, 비급 as martial arts manual, 송문고검 as Pine-Pattern Ancient Sword, 반로환동 as Returned to Youth, 강강수월래 as Ganggangsullae, 생사부 as Book of Life and Death, and 기막 as qi curtain."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 십왕     | **Ten Kings**       |
| 태원진가   | **Jin Family of Taiyuan**        |
| 무당파    | **Wudang**                       |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 영약     | **elixir**                                       |                                                       |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 큰형     | **eldest brother**                           |
| 은인     | **Benefactor**                               |
| 상태               | **Status**                     |
| 태원     | **Taiyuan**            |
| 청해     | **Qinghai**            |
| 화산     | **Huashan**            |
| 소협      | **Young Hero**                                                  |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 현공진인 | **Perfected Being Hyeongong** | Veteran Wudang Daoist master and the current Sect Leader's Junior Brother. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 제갈풍 | **Zhuge Feng** | Current Family Head of the Zhuge Clan. |
| 원시천존 | **Primordial Heavenly Venerable** | Daoist deity invoked alongside the Jade Emperor. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 환골탈태 | **Bone Transformation** | Advanced transformation described as optional in martial-arts novels. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |
| 무극 | **Martial Extremity realm** | Realm associated with opening the upper dantian. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 송문고검 | **Pine-Pattern Ancient Sword** | Willow-Cloud Divine Dragon’s sword. |
| 태극혜검 | **Taiji Wisdom Sword** | Wudang’s supreme sword technique. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 화산신룡 | **Huashan Divine Dragon** | Title given to Cheongpung after the Star-Array Grand Banquet. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 동정채 | **Donghu Stronghold** | Stronghold where Mu Song's Uncle Hwang is based. |
| 제갈 | **Zhuge** | Surname used for Sir Zhuge. |
| 무량수불 | **Infinite Life Buddha** | Buddhist invocation used by Taekyung. |

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
| 진태경 | 문경 | young_martial_artist_to_medical_apprentice | Young Hero | formal-polite | Taekyung addresses the non-martial Mungyeong as 소협 while praising his actions. |
| 문경 | 진태경 | young_passenger_to_younger_martial_artist | Young Hero | deferential | Mungyeong uses 소협 while asking Taekyung for help boarding the ship. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 제갈풍 | 진태경 | senior strategist_to_younger_martial_artist | you | calm and familiar | Uses 자네 while inviting Taekyung to continue questioning the Hubei incident. |
| 현공진인 | 제갈풍 | senior Wudang master to Zhuge Clan Family Head | Family Head Zhuge | formal-respectful | Uses 제갈가주 while discussing the fast ship and the route. |
| 제갈풍 | 현공진인 | Zhuge Clan Family Head to senior Wudang master | Perfected Being Hyeongong | formal-deferential | Addresses Hyeongong with marked respect and calls his presence a great reinforcement. |
| 제갈풍 | 문경 | old acquaintance to revealed legendary assassin | Slaughter Saint | excited and respectful | Zhuge Feng identifies Mungyeong by his established sobriquet after recognizing his identity. |
| 문경 | 제갈풍 | legendary_senior_to_younger_family_head | you; burden | blunt, insulting, and commanding | Mungyeong orders Zhuge Feng onto his back and dismisses his objections. |
| 청풍 | 제갈풍 | young_martial_artist_to_family_head | Great Hero Zhuge Feng | cheerful and polite | Cheongpung addresses Zhuge Feng as 제갈풍 대협, but deliberately mispronounces the name once as 제갈퐁 for comic effect. |
| 제갈풍 | 청풍 | family_head_to_younger_martial_artist | you | familiar and polite | Zhuge Feng uses 자네 while instructing Cheongpung and responding to his advice. |
| 현공진인 | 진태경 | senior Wudang master to younger martial artist | young friend | gentle and polite | Hyeongong uses 진 도우 and 젊은 도우 while greeting and worrying about Taekyung. |
| 진태경 | 현공진인 | younger martial artist to senior Daoist master | Perfected Being | respectful and polite | Uses 진인 while responding to Hyeongong's religious instruction. |
| 진태경 | 제갈풍 | younger martial artist to senior clan head | Sir Zhuge | blunt and challenging | Uses 제갈 대협 while disputing Zhuge Feng's attempted ten-percent claim. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 491
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 491
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hyeongong.md

# Perfected Being Hyeongong (현공진인)

- **Safe through:** Chapter 492
- **Aliases:** None
- **Role:** Perfected Being Hyeongong is a veteran Wudang Daoist master of the previous generation, the current Sect Leader's Junior Brother, and a Supreme Peak swordsman who reached the ultimate stage of the Taiji Wisdom Sword.
- **Personality:** Hyeongong is humble and self-deprecating about his limited worldly knowledge, carries the authority of an experienced senior master, and openly covets exceptional weapons.
- **Voice:** Measured, respectful, and lightly self-deprecating.
- **Relationships:** Hyeongong is the current Wudang Sect Leader's Junior Brother and a respected senior to Zhuge Feng.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 492
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 490
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, and can command coordinated raids against powerful monsters.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 490
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 491
- **Aliases:** Killing Ghost
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history who passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, Jeok Cheongang is an old acquaintance who asked him to look after and instruct Jin Taekyung, and Mungyeong is currently testing Taekyung before teaching him secret martial arts without a formal Master-Disciple relationship.

### Zhuge Feng.md

# Zhuge Feng (제갈풍)

- **Safe through:** Chapter 492
- **Aliases:** Crouching Dragon Guest
- **Role:** Zhuge Feng is the current Family Head of the Zhuge Clan and father of its Lesser Family Head, Zhuge Gyun.
- **Personality:** Analytical, disarmingly casual, eccentric, and inventive; he treats comfort and time as principles while delivering grave intelligence with unsettling directness.
- **Voice:** Clear, calm, polished, and conversational, with understated humor and pointed questioning.
- **Relationships:** Zhuge Gyun is his son, and Zhuge Gonghu was his grandfather.

## Korean source

```text
＃493화



기회는 모든 사람에게 공평하게 주어지지 않는다.

그런 의미에서 보자면 불과 열 살의 나이로 무당파 장문인의 적전 제자가 된 현공진인(玄空眞人)은 다른 이들에 비해 많은 기회를 얻은 인물이라 할 수 있었다.

그야말로 탄탄대로.

당대에 손꼽히는 무재를 타고난 데다 성정도 올곧은 현공진인은 늘 전폭적인 지원을 받았다.

그것은 반대로 말하자면, 그가 일평생 부족함을 느껴본 적이 없다는 뜻이기도 했다.

하지만…….

‘갖고 싶다.’

현공진인의 눈동자가 잘게 흔들렸다. 그건 실로 오랜만에 느끼는 물질적인 욕망이었다.

‘이런 적이 없었거늘.’

황금과 부귀영화? 그런 것 따위는 필요 없었다.

한번 받은 도포는 닳아 없어질 때까지 입었고 늘 정갈하고 단출한 식사로 끼니를 때웠다.

영약, 비급도 마찬가지다. 초절정의 경지에 오른 뒤부터는 정신 수양에 힘썼던 그다.

장문 사형이 영약을 권해도 앞길 창창한 귀여운 사손들에게 양보했고, 비급은 지금까지 익힌 무당파의 절기로도 차고 넘쳤다.

하지만, 하지만 이건.

“후우, 무량수불. 무량수불.”

현공진인은 거칠게 자신의 수염을 쓸어내리며 법문을 외웠다.

그러나 애써 다스리려는 마음과는 달리 눈길은 자꾸만 이무기의 사체를 향하고 있었다.

‘저게 그렇게 단단하다던데.’

갈라진 비늘과 쩍 벌어진 상흔(傷痕) 사이로, 은은한 빛을 뿌리는 거대한 뼈가 보인다.

오백 년 묵은 이무기라 그런지 때깔부터 다른 저 뼈는, 어지간한 검기로도 베어 내지 못할 만큼의 강도를 자랑한다고 들었다.

‘만약 저 뼈로 검을 만든다면 기가 막힐…… 아니, 아니다. 지금 무슨 생각을 하는 것이냐. 현공아!’

현공진인은 눈을 질끈 감았다. 태원진가의 두 형제에 의해 제갈풍이 너덜너덜해진 꼴을 목격한 직후라 더더욱 그랬다.

그나마 제갈풍은 전투가 벌어질 때 함께 있기라도 했지, 그는 수백 리 떨어진 동정채의 본거지에 있었다.

현공진인에게는 무언가를 요구할 만한 명분도, 부끄러움을 무릅쓰고 부탁할 만한 염치도 없었다.

‘무량수불, 무량수불. 도사씩이나 되어 이런 삿된 욕망에 정신을 빼앗기다니. 정신 차리거라, 현공아.’

현공진인이 남몰래 속앓이만 하고 있던 바로 그때였다.

“진인. 바쁘십니까?”

“음?”

현공진인은 감았던 눈을 번쩍 떴다. 낯익은 얼굴의 젊은이가 그를 은근한 시선으로 바라보고 있었다.

‘진태경.’

젊은이의 정체는 검성의 제자인 화산신룡 청풍과 함께 무림을 뒤흔들고 있는 돌풍의 주역이었다.

떠들기 좋아하는 호사가들 사이에서는 이미 십왕(十王) 아래에 이룡(二龍)이 있다는 말까지 돌고 있을 정도다.

‘대단한 젊은이지. 믿기 힘들 정도로.’

하지만 지금 현공진인에게 중요한 것은 진태경에 대한 평가가 아니었다.

‘혹시?’

약간의 희망과 설렘. 노 도사는 두근거리는 마음을 안고 진태경을 바라보았다.

“무슨 일인가. 진 도우?”

진태경이 부드럽게 웃으며 대답했다.

“바쁘시지 않다면 대화를 청해도 될까 싶어서요.”

“대화라면, 어떤 용무인가.”

“이제 사체를 처리해야 하는데, 생각보다 양이 많지 뭡니까.”

“그, 그래서?”

“다른 분도 아니고 현공진인께서 직접 여기까지 오셨는데, 당연히 얻어 가시는 게 있어야 하지 않겠습니까.”

“허어!”

대번에 초롱초롱해지는 현공진인의 눈동자. 그 모습에 빙긋 웃은 진태경이 재차 말을 이었다.

“저희 태원진가는 늘 무당파의 도사님들을 존경해 온 바, 같은 무림 동도로서 기쁜 마음으로 이번 수확을 조금이나마 나누고자 합니다.”

“그, 그것이 참말인가?”

“어휴, 그럼요. 혁무진의 불알을 걸고 맹세합니다. 그리고 이건 제 큰형님께서도 적극 찬성한 사안입니다.”

“세상에나, 무량수불!”

차마 염치가 있어 부탁하지 못한 가려운 부분을 살살 긁어 주니, 현공진인은 기뻐서 어쩔 줄을 몰랐다.

혁무진이 누구인지, 왜 그의 불알을 걸고 맹세하는지는 몰라도 일단 나눠 준다는 게 중요하다.

‘이토록 선량할 수가!’

말만 번지르르한 위선자들과는 격이 다르다.

몰염치한 인간군상들이 득실거리는 이 차가운 무림에 내리쬔 한 줄기 빛.

이제 현공진인은 진태경의 머리 위로 후광마저 보일 지경이었다.

“참으로 고맙네! 원시천존께서 진 도우와 태원진가를 보우하시길! 무량수불!”

“아멘.”

뭔가 이상했지만 현공진인에게는 아무런 상관도 없었다.

그리고 만면에 웃음을 가득 머금고 있던 그를 향해, 진태경의 부드러운 목소리가 이어졌다.

“그런데 사소한 문제가 하나 있습니다.”

“으응? 사소한 문제라니?”

“아무래도 사체가 워낙에 크다 보니 저 혼자는 처리하기 벅차지 뭡니까. 그렇다고 이걸 통째로 옮길 수도 없고요.”

“그렇지. 그렇고말고.”

머리부터 꼬리까지, 장장 백여 장에 달하는 거체다.

이런 걸 통째로 옮길 수 있는지도 의문이거니와, 그만한 인력이 투입될 테니 기밀 유지는 더더욱 불가능했다.

“해서 진인께 작은 부탁을 하나 드리고자 합니다.”

순간 멈칫한 현공진인의 눈동자에 의혹의 빛이 스쳤다.

“잠깐. 진 도우. 그 부탁이라는 게 혹시……?”

“예. 힘 좀 써 주셔야겠습니다. 이대로 가다가는 며칠씩 걸리겠어요.”

이거였구나! 호의를 베푼 이유가!

현공진인은 배신당한 표정으로 진태경을 노려보았다.

“그러니까 지금, 저 이무기의 사체를 분리하는 것에 무당파의 검공을 사용하라는 말인가?”

“쉽게 생각하시면 됩니다. 작업이죠.”

“쉽게 생각하라니, 작업이라니! 빈도는 이런 일을 위해 무공을 수련한 것이 아닐세!”

누군가 초절정의 경지에 올랐다는 것은 그의 인생 대부분을, 아니 인생 전부를 무공에 바쳤다는 뜻이다.

현공진인 역시 마찬가지였다. 한 자루 검을 벗 삼아, 정인 삼아 보낸 세월이 몇 년인가.

컴컴한 어둠 속에서 면벽수련(面壁修練)까지 해 가며 무공을 갈고 닦았던 그에게 있어 진태경의 부탁은 모욕이나 다름없었다.

‘괘씸한지고.’

현공진인은 딱딱하게 굳은 얼굴로 입을 열었다.

“무량수불. 진 도우. 자네는 지금 빈도는 물론이고 대무당파의 검공을 욕보인 걸세.”

“욕을 보이다니, 그럴 리가 있겠습니까. 그저 한 손 거들어 주십사 청하는 것뿐입니다.”

“하지만 빈도의 검을 고작 이런 일에 쓸 수는 없…….”

현공진인의 목소리가 높아지려던 그 순간, 진태경이 불쑥 한마디를 툭 던졌다.

“지금 보니 검이 상당히 낡았네요.”

“뭣이?”

“슬슬 바꾸실 때가 된 것 같은데. 어떻게 생각하십니까?”

“……!”

현공진인의 동공이 지진이라도 난 것처럼 흔들렸다.

자신도 모르게 허리춤에 매인 낡은 송문고검을 바라본 그의 뇌리에 문득 한 가지 생각이 스쳤다.

‘확실히 낡긴 했…… 아니, 지금 내가 무슨 생각을!’

열 살 때부터 늘 몸에 지니고 있던 검이다. 돌아가신 스승님께 받은 귀중한 물건이기도 했다.

황급히 고개를 흔들어 정신을 차린 현공진인이 눈을 부릅떴다.

“안 낡았네!”

“낡았습니다. 직접 보세요. 우선 검파(劍把)만 봐도 완전 너덜거리는데.”

“그런 것 같기도 하…… 아닐세! 잘못 본 게야!”

“그럼 그건 그렇다 치고, 검갑에도 금이 잔뜩 갔는데요. 가뭄 들었습니까?”

“아앗. 이건 또 언제…….”

“아, 이거 상태가 심각하네. 검 좀 뽑아 보시겠어요?”

“빈도가 왜 그래야 하나!”

스릉!

호통을 친 현공진인은 뒤늦게 자신이 검을 뽑았다는 사실을 알고 경악했다.

‘도대체 언제!’

하지만 그러거나 말거나, 마귀의 속삭임은 계속되고 있었다.

“검신도 영 상태가 좋지 못한데요.”

“작고하신 스승님께서 주신 물건일세!”

진태경이 태연한 표정으로 대꾸했다.

“제 몸도 부모님께서 주셨는데, 쓰다 보니 망가지더라고요. 바꿀 수만 있었으면 진작 바꿨을 겁니다.”

“하긴 빈도도 요즘 삭신이 쑤셔서 환골탈태(換骨奪胎)가 마려울 지경…… 지금 뭐 하자는 겐가!”

“뭐 하긴요. 냉정한 현실을 알려 드리는 겁니다. 오, 날 부분은 아직 예리한데요?”

정신 차리자. 정신 차려야 한다, 현공아.

호흡으로 흐트러지는 정신을 가다듬은 현공진인이 자부심 넘치는 목소리로 대답했다.

“당연하지. 다른 것도 아닌 만년한철을 넉 냥이나 섞어 검날을 벼렸으니까.”

“세상에. 그 귀하다는 만년한철을 넉 냥이나요?”

“이제 알겠나? 이 검이 보기에는 낡았을지 몰라도 보검(寶劍)이라 불리기에 조금도 부족함이 없다는 것을.”

“아하. 그렇습니까?”

“물론일세! 이미 누구나 탐낼 만큼 좋은 검을 가졌는데 뭣 하러 다른 검을…….”

철컹!

“아, 죄송합니다. 손이 미끄러워서 그런지 창을 떨어트렸네요. 말씀 계속하세요.”

머쓱하게 웃는 진태경의 얼굴은 눈에 들어오지도 않는다.

은은한 빛을 뿌리는 한 자루의 창을 바라보는 현공진인의 눈꺼풀이 파르르 떨렸다.

“지, 진 도우. 그거 설마…….”

“별거 아닙니다. 이것도 만년한철로 만든 건데, 진인께서 갖고 계시는 검에 비하면 아무것도 아니죠.”

전혀 안 그래 보이는데.

마른침을 꿀꺽 삼킨 현공진인이 조심스럽게 물었다.

“혹시…… 몇 냥?”

“통짜. 날부터 창대까지 전부.”

“이런 미친. 무량수불.”

“예? 뭐라고요?”

“아, 아닐세. 아무것도.”

마귀다. 이건 마귀의 속삭임이다.

하지만 홀린 듯이 법문을 외는 현공진인의 시선은 진태경의 창, 백염(白炎)에 고정되어 있었다.

“가볍기는 깃털 같고, 단단하기는 또 얼마나 단단합니까. 심지어 예리하기까지 해요. 그런데.”

이어 노 도사의 귓가를 파고드는 나긋나긋한 유혹의 음성.

“저는 이무기의 뼈로 만든 병장기가 갖고 싶더라고요.”

“무량수불. 나는 아닐세.”

“잘 생각해 보십시오. 다른 것도 아니고 자그마치 오백 년이나 살아온 신령스러운 이무기의 기운이 고스란히 깃들어 있는 병장기라면?”

당연히 끝내주겠지. 진짜 갖고 싶다.

치미는 말을 간신히 삼킨 현공진인이 미친 듯이 고개를 흔들었다.

“불가! 빈도는 결코 스승님께서 주신 검을 버릴 수 없…….”

“누가 그 소중한 걸 버립니까. 둘 다 가지면 되는 거죠.”

“이런 씨발 그런 방법이! 아아 원시천존이시여!”

“예?”

“그만! 이제 그만하시게! 무량수부울!”

“도와주시면 무당파에 섭섭지 않게 떼 드립니다. 제가 설마 검 한 자루로 퉁 치겠습니까?”

“빈도는 이미 만년한철로 만든 검을 갖고 있네!”

“네. 이무기의 뼈.”

“스승님이 주신 검을 두고 어찌 다른 검을!”

“예. 다다익선.”

“이런 일을 위해 익힌 무공이 아니란 말일세!”

마지막 자존심을 붙들고 탄식하는 현공진인의 모습에, 진태경이 어딘가를 향해 외쳤다.

“어이, 청 소협! 잘되고 있지?”

거대한 사체 뒤, 해맑은 얼굴 하나가 쏙 나타났다. 함께 싸운 대가로 상당 지분을 약속받은 청풍이었다.

“네, 은인! 지금 허리 부분 작업하고 있어요!”

“그래? 그 부분이 특히 두꺼울 텐데 힘들지는 않고?”

“아니에요. 무극태을검(無極太乙劍)으로 잘 베고 있어요!”

“좋아. 금방 갈 테니까 계속 작업하고 있어.”

“네, 은인!”

성실한 작업꾼을 향해 흐뭇하게 웃어 보인 진태경이 현공진인을 돌아보며 물었다.

“아, 죄송합니다. 진인. 제가 감히 한눈을 팔았네요.”

“…….”

“그런데 무슨 얘기 중이었죠? 제가 요새 자주 깜빡깜빡해서.”

현공진인은 열심히 작업 중인 청풍과 진태경을 번갈아 바라보았다.

그리고 그로부터 반 시진 뒤.

서걱!

무당파가 자랑하는 최고의 검공, 태극혜검(太極慧劍)이 비늘과 뼈를 분리하고 있었다.

“무림이 미쳐 돌아가는군.”

이 모든 상황을 지켜보던 문경의 짧은 소감이었다.
```

## Final English reading copy

```markdown
# Chapter 493

Opportunity is not given equally to everyone.

In that sense, Perfected Being Hyeongong, who had become the Wudang Sect Leader’s direct Disciple at the age of ten, was someone who had received far more opportunities than most.

His path had been smooth from the very beginning.

Born with martial talent that ranked among the best of his generation and blessed with an upright character, Hyeongong had always received wholehearted support.

But that also meant he had never experienced a lack of anything in his entire life.

However…

*I want it.*

Perfected Being Hyeongong’s eyes trembled faintly. It was a material desire he had not felt in a very long time.

*I’ve never felt this way before.*

Gold and wealth? Fame and glory? He had never needed any of that.

Whenever he received a Daoist robe, he wore it until it was completely worn out, and he always got by on neat, simple meals.

Elixirs and martial arts manuals had been the same. After reaching the Supreme Peak realm, he had devoted himself to cultivating his mind.

Whenever his Senior Brother, the Sect Leader, offered him an elixir, Hyeongong gave it to his promising grand-disciples instead. And the Wudang techniques he had mastered were more than enough martial arts for one lifetime.

But this—this was different.

“Hoo… Infinite Life Buddha. Infinite Life Buddha.”

Hyeongong roughly stroked his beard and recited the invocation.

Yet despite his efforts to control himself, his gaze kept drifting toward the imugi’s corpse.

*They say those bones are incredibly hard.*

Between the split scales and the wide, gaping wounds, enormous bones radiated a faint glow.

Perhaps because they had belonged to a five-hundred-year-old imugi, the bones had a luster unlike anything else. He had heard they were so hard that even ordinary Sword Energy could not cut through them.

*If I made a sword from those bones, it would be incredible… No, no. What am I thinking? Get a grip, Hyeongong!*

Hyeongong squeezed his eyes shut. He had just witnessed Zhuge Feng being reduced to tatters by the two brothers of the Jin Family of Taiyuan, which only made matters worse.

At least Zhuge Feng had been there when the battle broke out. Hyeongong, on the other hand, had been at the Donghu Stronghold headquarters, hundreds of li away.

He had neither the justification to ask for anything nor the nerve to make a request despite his embarrassment.

*Infinite Life Buddha, Infinite Life Buddha. How can a Daoist allow himself to be distracted by such a base desire? Get a hold of yourself, Hyeongong.*

That was when he was suffering in silence.

“Perfected Being. Are you busy?”

“Hm?”

Hyeongong’s eyes flew open. A familiar young man was looking at him with a knowing gaze.

*Jin Taekyung.*

The young man was one of the driving forces behind the whirlwind shaking Murim alongside the Sword Saint’s Disciple, Cheongpung—the Huashan Divine Dragon.

Among gossip-loving raconteurs, people were already saying that the Ten Kings had the Two Dragons beneath them.

*He’s an incredible young man. Almost unbelievably so.*

But Hyeongong’s opinion of Jin Taekyung was not what mattered to him at that moment.

*Could it be?*

With a sliver of hope and excitement in his heart, the old Daoist looked at Jin Taekyung.

“What is it, Young Friend Jin?”

Jin Taekyung answered with a gentle smile.

“If you’re not busy, I wanted to ask if I could have a word with you.”

“A conversation? What do you need?”

“We have to deal with the corpse now, but there’s a lot more of it than we expected.”

“Th-That’s why?”

“Of all people, you came all the way here in person. Naturally, you ought to have something to take home with you.”

“Oh!”

Hyeongong’s eyes immediately lit up. Jin Taekyung smiled and continued.

“Our Jin Family of Taiyuan has always respected the Daoists of Wudang. As fellow martial artists of Murim, we would be delighted to share even a small portion of this harvest with you.”

“I-Is that really true?”

“Of course. I swear on Hyuk Mujin’s balls. And my eldest brother is fully in favor of it too.”

“Good heavens! Infinite Life Buddha!”

By gently scratching the itch Hyeongong had not had the nerve to ask anyone else to scratch, Jin Taekyung left the old Daoist beside himself with joy.

Hyeongong did not know who Hyuk Mujin was or why Jin Taekyung was swearing on the man’s balls. All that mattered was that he was being given a share.

*How can anyone be this kind?*

He was on an entirely different level from the hypocrites who only knew how to make pretty speeches.

A ray of light shining down on this cold Murim, crawling with shameless masses.

Hyeongong could practically see a halo over Jin Taekyung’s head.

“Thank you so much! May the Primordial Heavenly Venerable protect you and the Jin Family of Taiyuan, Young Friend Jin! Infinite Life Buddha!”

“Amen.”

Something about it seemed strange, but Hyeongong did not care in the slightest.

And as he stood there with a broad smile on his face, Jin Taekyung continued in a gentle voice.

“However, there is one small problem.”

“Hm? What sort of small problem?”

“The corpse is so enormous that I can’t handle it alone. And we can’t exactly move the whole thing.”

“That’s true. Quite true.”

From head to tail, the giant creature stretched for more than a hundred zhang.[^1]

It was questionable whether it could even be moved in one piece. And since doing so would require a great deal of manpower, keeping the matter secret would become even more impossible.

“So I wanted to ask you for a small favor, Perfected Being.”

A glimmer of suspicion passed through Hyeongong’s eyes.

“Wait. Young Friend Jin. This favor of yours wouldn’t happen to mean…”

“Yes. You’ll have to lend us a hand. At this rate, it’ll take several days.”

So that was it! That was why he had shown Hyeongong such kindness!

Hyeongong glared at Jin Taekyung with an expression of betrayal.

“So you’re saying that you want me to use Wudang’s sword techniques to take that imugi’s corpse apart?”

“Think of it simply. It’s just a job.”

“Think of it simply? A job? I did not train my martial arts for this!”

When someone reached the Supreme Peak realm, it meant that they had devoted most of their life—no, their entire life—to martial arts.

Hyeongong was no different. How many years had he spent with one sword as his companion and beloved?

He had even trained in the pitch-black darkness, facing a wall as he honed his martial arts. To him, Jin Taekyung’s request was no different from an insult.

*How outrageous.*

With his face stiff as a board, Hyeongong opened his mouth.

“Infinite Life Buddha. Young Friend Jin. You have insulted not only me but also the sword arts of all Wudang.”

“Insulted you? How could that be? I’m merely asking you to lend us a hand.”

“But I cannot use my sword for something as trivial as—”

At the moment Hyeongong’s voice began to rise, Jin Taekyung casually tossed out a single remark.

“Now that I look at it, your sword is pretty worn.”

“What?”

“It seems like it’s about time you replaced it. What do you think?”

“……”

Hyeongong’s pupils shook as if an earthquake had struck.

Without realizing it, he looked down at the old Pine-Pattern Ancient Sword hanging from his waist. A thought suddenly passed through his mind.

*It is definitely worn… No! What am I thinking?*

It was the sword he had carried ever since he was ten years old. It was also a precious gift from his late master.

Hyeongong hurriedly shook his head, pulled himself together, and glared.

“It is not worn!”

“It is. Take a look for yourself. The hilt alone is completely ragged.”

“It does look a little… No! You saw it wrong!”

“Fine, let’s set that aside. The scabbard is covered in cracks too. Has it been through a drought?”

“Ah! When did this happen…?”

“Whoa, this is in serious condition. Would you draw the sword?”

“Why should I?”

*Shing!*

Hyeongong had shouted before belatedly realizing that he had drawn his sword. He was horrified.

*When did I do that?*

But regardless of that, the devil’s whisper continued.

“The blade doesn’t look to be in very good condition either.”

“It was given to me by my late master!”

Jin Taekyung answered with an utterly calm expression.

“My body was given to me by my parents, but it broke down with use. If I could have replaced it, I would have done so long ago.”

“Well, this old Daoist’s joints ache these days too. I’m practically itching for Bone Transformation… What are you trying to do?”

“I’m just telling you the cold reality. Oh, the edge is still sharp, at least.”

Get a grip. Hyeongong had to get a grip.

Hyeongong steadied his breathing and answered in a voice filled with pride.

“Of course it is. The blade was forged with four nyang of Ten-Thousand-Year Cold Iron mixed into it.”

“Good heavens. You used four nyang of that precious Ten-Thousand-Year Cold Iron?”

“Do you understand now? This sword may look worn, but it is in no way lacking when it comes to being called a treasured sword.”

“Oh. Is that so?”

“Of course! I already possess a sword so fine that anyone would covet it. Why would I need another sword…”

*Clang!*

“Oh, sorry. My hand must have slipped. I dropped my spear. Please continue.”

Jin Taekyung’s sheepish smile did not register in Hyeongong’s eyes.

His eyelids trembled as he stared at the spear radiating a faint glow.

“Y-Young Friend Jin. Is that, by any chance…”

“It’s nothing special. This is made from Ten-Thousand-Year Cold Iron too, but compared to the sword you have, it’s nothing.”

It certainly did not look that way.

Hyeongong swallowed hard and cautiously asked,

“How many nyang?”

“It’s solid. The entire thing, from the blade to the shaft.”

“You’ve got to be kidding me. Infinite Life Buddha.”

“Pardon? What did you say?”

“Ah, nothing. It was nothing.”

A devil. This was the devil’s whisper.

Yet Hyeongong’s eyes remained fixed on Jin Taekyung’s spear, White Flame, as he recited the invocation as if possessed.

“It’s as light as a feather, but how incredibly hard it is. And it’s sharp too. But…”

Then the gentle voice of temptation slipped into the old Daoist’s ear.

“I’ve found myself wanting a weapon made from an imugi’s bones.”

“Infinite Life Buddha. I don’t.”

“Think about it carefully. Not just any weapon, but one containing all the qi of a sacred imugi that lived for no less than five hundred years.”

*Of course it would be incredible. I really want it.*

Hyeongong barely swallowed the words rising to his lips and shook his head frantically.

“Impossible! I can never abandon the sword my master gave me—”

“Who said anything about abandoning such a precious thing? You can have both.”

“What the fuck? That’s an option? Ah, Primordial Heavenly Venerable!”

“Pardon?”

“Stop! That’s enough! Infinite Life Buddhaa!”

“If you help us, we’ll give you a share generous enough that Wudang won’t feel slighted. Do you think I’d settle this with a single sword?”

“I already have a sword made from Ten-Thousand-Year Cold Iron!”

“Yes. And an imugi’s bones.”

“How could I use another sword when I have the one my master gave me?”

“Yes. The more, the better.”

“I did not learn martial arts for this sort of thing!”

As Hyeongong clung to his last shred of pride and lamented, Jin Taekyung suddenly shouted toward somewhere behind the corpse.

“Hey, Young Hero Cheongpung! Is everything going well?”

A bright face popped out from behind the enormous corpse. It was Cheongpung, who had been promised a considerable share as payment for fighting alongside them.

“Yes, Benefactor! I’m working on the waist right now!”

“Really? That part must be especially thick. Isn’t it difficult?”

“No! I’m cutting through it just fine with the Martial Extremity Grand Unity Sword!”

“Good. I’ll be there soon, so keep working.”

“Yes, Benefactor!”

After giving the diligent worker a pleased smile, Jin Taekyung turned back to Hyeongong.

“Ah, sorry, Perfected Being. I took my eyes off the work for a moment.”

“……”

“But what were we talking about? I’ve been forgetting things a lot lately.”

Hyeongong looked back and forth between Cheongpung, who was working diligently, and Jin Taekyung.

And half a shichen later…

*Slash!*

The Taiji Wisdom Sword, Wudang’s finest sword technique, was separating the imugi’s scales from its bones.

“Murim has gone completely mad.”

That was Mungyeong’s brief assessment as he watched the entire situation unfold.

[^1]: A zhang is a traditional East Asian unit of length, roughly 3.3 meters.
```
