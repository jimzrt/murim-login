<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0469.txt",
      "sha256": "f475f336cd24af9e0637bb3ab280619af901f8fed9c06ecdcc14c64a2e19e1be",
      "bytes": 14079
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "de9e63e092562e86695910a378310da27d53f5e483f767e94211d2d576881bc8",
      "bytes": 3656
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "4d5b2f4901d31c8e040678970c8cb2d52c41106a26706a96ec847359de2d1300",
      "bytes": 151953
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "7902ef35bd98c4c3e59315541d47e28b3ef41d687cfa57c7d32796b2dfd2bf47",
      "bytes": 990
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "5cce339f0e767c172fb34d9eb3de9df919db6552589a11afed1b14a8d21425ff",
      "bytes": 553
    },
    {
      "path": "characters/Dongting Fisherman.md",
      "sha256": "7d570539d430512c32fc3dbfb1cb4263efe67d292a05fb95e63b38305902bf13",
      "bytes": 778
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "d875eab7d0c9ab4c14e5c0bd5d90236d384fa734957dc21345c16c055601a391",
      "bytes": 662
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "5d47bb163a1502bd9b47c12accdd28245eef90eb6827f2fa9837b917296ad7ac",
      "bytes": 1108
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "ab25b26a993fcbed7781b7374c654970f85f506363dece0baa73bb8b1f7f5316",
      "bytes": 1574
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "7d37176f83a28435eeb0556560e23580169450a60a0f882881574bde6062c249",
      "bytes": 622
    },
    {
      "path": "characters/Zhuge Feng.md",
      "sha256": "ee5d6364f3cb35f411327665ec0eb8d3d1b99bbedd1ac078a4381db384277f33",
      "bytes": 626
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "367da7ba1bdfa157221f6ab84d1304e2d68a2d174fe42001ce839c2ef253eaaa",
      "bytes": 146846
    }
  ],
  "estimated_tokens": 12210
}
-->

# Durable State Update — Chapter 469

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 469. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 469. Profile updates may replace only one
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
  "chapter": 469,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 469,
    "continuity_sources": [469],
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
    "The Dongting Fisherman remains severely injured and immobilized by Taekyung's Paralysis, Mute, and Sleep Acupoint seals after accepting Dark Heaven's hand.",
    "Taekyung intends to interrogate the Dongting Fisherman about Dark Heaven before allowing him to die.",
    "Taekyung suffered only a minor internal injury from the Dongting Fisherman's Inner-Family Heavy Hand and remains capable of fighting.",
    "Hyuk Mujin and Gung Gibang disregarded Taekyung's order to wait because they sensed he was in danger, while Cheongpung remained confident that Taekyung would return.",
    "Honglan survived the Dongting Lake disaster and is recovering; Ju Wongong remains unconscious under guard after passing the most dangerous stage of his injuries.",
    "Jin Wikyung is acting as an inspector for the new Murim Alliance and is cooperating with Taekyung's investigation.",
    "The shared symbols between the Arch Lich's magic circle and Dark Heaven's formations remain unexplained.",
    "The Sea Serpent Society and three Yangtze River Channel League strongholds, including Donghu Stronghold, were destroyed with more than a thousand casualties, while the perpetrators' wider plans remain unknown.",
    "The captured Three Fiends is a former-generation great fiend and Supreme Peak Dark Heaven subordinate whom Taekyung is transporting alive to investigate possible codes or markings.",
    "An unprecedented storm over Dongting Lake prevented ordinary passage; Mu Song brought his best sailors from Water Dragon Stronghold, and Jeok Cheongang opened a route through the storm by destroying a waterspout.",
    "Jeok Cheongang, Mungyeong, and Zhuge Feng are moving toward Taekyung's location, while Hyeongong remains behind.",
    "A cliff has collapsed and a Mutated Water God Dragon with an unreadable level has emerged before Taekyung."
  ],
  "continuity_sources": [
    468,
    467
  ],
  "open_questions": [
    "What is the Dongting Fisherman's exact role within Dark Heaven, what information will he reveal, and what caused his involuntary movement and terrified warning?",
    "What caused the earlier deliberate destruction inside the refuge, and how was it connected to the Dongting Fisherman or another intruder?",
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Who destroyed Donghu Stronghold and the related Yangtze River Channel League strongholds, why was no Moving Formation trace left, and was the destruction a diversion?",
    "What is the sharp, armor-hard object carried by Jeok Cheongang, and what are the identity, origin, and purpose of the Mutated Water God Dragon?"
  ],
  "safe_through": 468,
  "temporary_decisions": [
    "Render 천잠사 as Heavenly Silkworm Thread, 운철 as meteorite iron, 초인 as superhuman, and 극쾌 as extreme swiftness.",
    "Render 노괴 as old monster, 신병이기 as divine weapon, 수상 구조대원의 물갈퀴 as Water Rescue Worker's Webbed Feet, and 수상 구조대원의 아가미 as Water Rescue Worker's Gills.",
    "Preserve Taekyung's dry contemporary humor and blunt profanity, render 씨부럴 as sibu-leol in direct abuse, and preserve the Dongting Fisherman's emotionless, inhuman presentation and violent combat voice.",
    "Continue rendering 오기조원 as Five Qi Returning to Origin, 노화순청 as Furnace Fire Pure Blue, 반로환동 as Returned to Youth, and 복자 as diviner.",
    "Render 일위도강 as Single Reed Crossing the River, 장제자 as Senior Disciple, and 변이된 수신룡 as Mutated Water God Dragon."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 제갈세가   | **Zhuge Clan**                   |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 창기     | **Spear Energy**                                 | Explicit system skill for Taekyung                    |
| 가주     | **Family Head**                              |
| 은인     | **Benefactor**                               |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 대격변     | **Great Cataclysm**   |
| 소협      | **Young Hero**                                                  |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동정어옹 | **Dongting Fisherman** | Publicly condemned the Yangtze River Channel League and disappeared three days before this chapter. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 제갈풍 | **Zhuge Feng** | Current Family Head of the Zhuge Clan. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 고블린 | **goblin** | Monster species reported at the F-rank Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 내신 | **school grades** | School-record grades referenced in Taekyung’s insult. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 신력 | **divine strength** | Superhuman strength attributed to Taekyung. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 와룡객 | **Crouching Dragon Guest** | Epithet of Zhuge Feng. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 나룻배 | **ferryboat** | Small ferry used to reach the suspected refuge site. |
| 사공 | **boatman** | Old boatman piloting the ferryboat. |
| 호북성 | **Hubei Province** | Province where the chapter’s Dark Heaven incidents occurred. |

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
| 궁기방 | 진태경 | rival_finalists | you bastard | insulting-casual | Gung Gibang answers Taekyung's collective insult with a profane threat. |
| 진태경 | 궁기방 | rival_finalists | you three idiots | insulting-casual | Taekyung addresses Gung Gibang as part of the trio and threatens them before a duel. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 제갈풍 | 진태경 | senior strategist_to_younger_martial_artist | you | calm and familiar | Uses 자네 while inviting Taekyung to continue questioning the Hubei incident. |
| 제갈풍 | 궁기방 | family_head_to_beggars_sect_successor | Successor Beggar | calm and conversational | Uses 후개 when confirming Gung Gibang's guess about the broken weapon. |
| 진태경 | 사공 | passenger_to_boatman | Boatman | commanding | Taekyung orders the boatman to continue to the final site and asks how long the journey will take. |
| 혁무진 | 사공 | passenger_to_boatman | Boatman | weighty-commanding | Mujin presses the boatman to depart despite the worsening conditions. |
| 진태경 | 동정어옹 | hostile interrogator confronting a suspected perpetrator | you | blunt informal and abusive | Taekyung addresses the Dongting Fisherman without honorifics and calls him a sibu-leol bastard. |
| 궁기방 | 사공 | passenger to ferryboatman | Boatman | direct and formal-polite | Addresses the old boatman as 사공 while challenging his refusal to sail. |
| 사공 | 진태경 | ferryboatman to honored martial guest | Great Hero | fearful and deferential | Repeatedly addresses Taekyung as 대협 while explaining the storm and the boat’s limits. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 467
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 468
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Dongting Fisherman.md

# Dongting Fisherman (동정어옹)

- **Safe through:** Chapter 467
- **Aliases:** None
- **Role:** The Dongting Fisherman is a previous-generation Supreme Peak master whose water arts rival the Seafaring King; he joined Dark Heaven, committed the Dongting Lake massacre, and is now captured alive for interrogation.
- **Personality:** The Dongting Fisherman appears eerily emotionless and savage, eating live fish raw and reacting violently when provoked.
- **Voice:** Not established.
- **Relationships:** The Dongting Fisherman opposed the Yangtze River Channel League and was monitored by the Lower District Sect for several years after friction with it, while current records place him in Hubei Province.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 467
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung and uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and search for Dark Heaven’s Hubei forces.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 467
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 468
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, can perceive the texture of qi well enough to sever layered magic, and is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 468
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Zhuge Feng.md

# Zhuge Feng (제갈풍)

- **Safe through:** Chapter 468
- **Aliases:** Crouching Dragon Guest
- **Role:** Zhuge Feng is the current Family Head of the Zhuge Clan and father of its Lesser Family Head, Zhuge Gyun.
- **Personality:** Analytical and disarmingly casual, he treats comfort and time as principles while delivering grave intelligence with unsettling directness.
- **Voice:** Clear, calm, polished, and conversational, with understated humor and pointed questioning.
- **Relationships:** Zhuge Gyun is his son, and Zhuge Gonghu was his grandfather.

## Korean source

```text
＃469화



모두가 보았다. 볼 수 있었다.

검게 물든 하늘과 거세게 몰아치는 비바람 사이, 쏟아지는 기암괴석(奇巖怪石)의 소나기를.

쿠구구구구궁!

커다란 바위가 수면을 때리자 수 장 높이의 물보라가 솟구쳤다. 무너지는 절벽에서는 보금자리를 잃은 새들이 날카로운 울음소리와 함께 추락하고, 폭우와 낙뢰가 쉴 새 없이 내리쳤다.

그리고…… 모든 것이 무너지는 가운데 홀로 몸을 일으키는 한 존재가 있었다.

콰아아아아-!

몸뚱어리를 타고 흘러내린 강물이 폭포수처럼 쏟아졌다.

까마득한 저 아래, 작은 점이 되어 버린 인간들은 아연한 눈동자로 마침내 모습을 드러낸 존재를 바라보았다.

그것은 거대했다.

그 표현조차 부족하다고 느낄 만큼, 그러나 그 외에는 어떤 말도 떠오르지 않을 만큼.

모두의 머릿속에는 오직 단 하나의 의문으로 가득했다.

‘저게 뭐지?’

불길하리만치 아름다운 흑색 광택을 띤 비늘, 건장한 장정 열 명이 양팔을 벌려야만 감싸 안을 수 있을 만큼 굵은 몸통.

수면 위로 드러난 것만 해도 삼십여 장에 달하는, 길고 유연한 몸뚱어리를 타고 올라가자 이마 위로 솟아오른 두 개의 뿔이 보였고, 그 아래에 안광(眼光)이 있었다.

세로로 죽 찢어진 핏빛 동공. 천천히 벌어지는 비늘 사이로는 톱날 같은 이빨과 컴컴한 동굴을 옮겨 놓은 듯한 짐승의 아가리가 모습을 드러냈다.

- 크르르르.

까마득한 상공으로부터 울려 퍼진 흉성(凶聲)에, 와룡객 제갈풍은 뼛속 깊이 스며드는 한기를 느꼈다.

‘이게 무슨…….’

갓난아기 시절부터 가문 제일의 천재라 불리던 제갈풍이다.

한 번 본 것은 절대로 잊지 않는 뛰어난 두뇌는 물론이요, 지식에 대한 열망도 갖춘 그는 지금껏 수만 권에 달하는 서책을 탐독하며 천하의 숱한 지식을 자신의 것으로 만들었다.

제갈풍이 품은 지식의 강은 끝없이 넓고 깊었다.

아니, 그렇다고 생각했다.

저것을 보기 전까지는.

‘이럴 수가.’

난생처음 마주한 미지(未知)에 대한 공포.

그 순간, 제갈풍은 자신이 지금껏 쌓아 올린 지식과 정보가 물거품이 되었다는 사실을 깨달았다.

그동안 헛소리로 치부했던 숱한 설화와 전설의 일부분이 그의 눈앞에 나타났다는 사실 역시.

‘정녕…… 그 허무맹랑한 이야기들이 사실이었단 말인가.’

제갈풍은 자신이 가진 지식의 힘을 굳게 믿었었다.

그는 한 사람의 무림인이기 이전에 제갈세가라는 명문대파의 주인이었고, 숱한 식솔과 가문의 힘을 지키기 위해서 확실한 정보와 지식을 활용해 왔다.

그런 그에게 있어 검증되지 않은 미신 따위는 고려 대상이 아니었다. 누구도 본 적 없는 허상을 믿는 건 멍청한 짓이었으니까.

하지만 제갈풍으로부터 백여 장 밖에 있는 누군가는 달랐다.

그는 제갈풍과 달리 일가를 책임져야 할 가주도 아니었고, 오직 자신의 경험과 나룻배 한 척에 의지하여 살아온 늙은 뱃사람이었으니까.

“……!”

늙은 사공은 떨리는 눈동자로 허공을 바라보았다.

무너져 내리는 모든 것들 사이로 홀로 우뚝 선 거대한 존재. 보는 것만으로도 다리가 굽혀지고, 감당할 수 없는 경외심과 두려움이 그의 초라한 두 어깨를 짓눌렀다.

중압감에 미처 토해 내지 못한 외침이 그의 마음속에서만 울려 퍼졌다.

‘시, 신령이다. 동정호의 신령께서 모습을 드러내신 게야!’

천하에는 헤아릴 수 없을 만큼 수많은 미신이 가득하다. 당연히 호북성 역시 예외는 아니었다.

늙은이가 아이에게, 그 아이가 늙어 또 다른 아이에게. 입에서 입으로 수백 년간 전해져 내려오는 이야기들.

늙은 사공 역시 다르지 않았다.

호북성 토박이로 일평생을 뱃사람으로 살아온 그는, 자신이 신령이라 칭한 저 존재의 정체를 알고 있었다.

동정호의 이각수(二角獸), 혹은 수신룡(水神龍)이라 불리는 동정호의 진정한 주인을.

‘아아, 아아아…….’

늙은 사공은 몸을 부르르 떨었다. 알 수 없는 감정에 휩싸인 전신이 요동치고 가슴 한구석이 북받쳤다.

그것은 이 자리에 있는 이들 중 오직 그만이 느낄 수 있는 감정이었다.

감히 말로는 표현할 수 없는 경외와 두려움.

뼛속까지 뱃사람인 그는 자신이 동정호의 주인과 마주했다는 사실이 믿어지지 않았고, 그 존재로부터 흘러나오는 기세에 숨이 막혔다.

‘시, 신령께서 노하셨구나. 모두 신령께서 진노하셨기에 벌어진 일이었어!’

늙은 사공은 자신의 짐작이 사실이었음을 깨달았다.

지난 한 달간 잇따른 숱한 죽음들. 무슨 이유에서인지는 몰라도 신령께서 단단히 화나신 것이 틀림없다.

그리고 결국 자신에게도 그들과 같은 벌을 내리실 것이다.

죽음이라는 벌을!

이대로 죽을 수는 없다. 어떻게든 신령을 진노를 가라앉혀야 했다.

홀린 듯이 서 있던 늙은 사공의 입에서 갈라진 외침이 터져 나왔다.

“시, 신령이시여! 소인에게는 아무런 죄가 없습니다!”

좌중에 내려앉았던 침묵이 깨져 나갔다. 늙은 사공의 외침이 비바람에 섞여 흩어졌다.

거대한 존재의 등장과 함께 우뚝 굳어 버린 다른 이들이 말릴 새도 없이, 늙은 사공은 파들파들 떨리는 두 다리로 물가를 향해 달려 나갔다.

“신령이시여어-!”

타다닥, 첨벙!

늙은 사공의 허름한 짚신이 동정호의 강물을 밟은 바로 그때.

스으윽.

한없이 느려진 세상 속, 거대한 한 쌍의 눈동자가 늙은 사공을 향했다.

세로로 죽 찢어진 핏빛 동공에 비친 늙은 사공의 모습. 한없이 작고 보잘것없는 인간의 존재를 인지한 그것의 안광이 붉게 타올랐다.

쏴아아아악!

삼십여 장에 이르는 거체에서 흘러나온 오싹한 기운이 사방을 향해 쏘아졌다.

날아오르던 새들이 힘을 잃음과 동시에 추락했고, 동정호의 강물 깊숙한 곳에서 무리 지어 도망치던 수천 마리의 물고기들이 배를 까뒤집은 채 수면 위로 둥둥 떠 올랐다.

몸뚱어리만큼이나 거대하고, 죽음에 가까운 기운.

한낱 미물은 물론이요, 인간조차 그 앞에서 무사할 수 없었다.

보이지 않는 그 기운이 닿기도 전에, 이미 늙은 사공의 전신은 석상처럼 굳어 있었다.

멍하니 벌어진 입과 부릅뜬 두 눈. 마침내 공포에 휩싸인 그의 동공이 허옇게 뒤집히려던 바로 그 순간.

쉭! 투두둑!

날카로운 파공성과 함께, 늙은 사공의 신형이 그 자리에서 스르륵 허물어졌다.

노쇠한 그의 육신을 부드럽게 받아든 청년이 고개를 들어 거대한 존재를 응시했다.

“야, 이 씨부랄 뱀장어 새끼야.”

- ……!

또렷하게 들려오는 목소리에, 무언가를 깨달은 거대한 존재의 동공이 크게 부풀었다.

다르다.

지상의 모든 인간이 충격과 공포로 인해 얼어붙어 있었지만, 저 젊은 인간은 달랐다. 그는 충격을 받지도 않았고 두려움에 떨지도 않았다.

미지의 공포는 알 수 없는 존재를 마주함에 있어 기인하는 법.

그러나 저 젊은 인간은 그 모든 것에서 자유로운 존재였다. 겁이 없다기보다는 오히려 익숙해 보일 지경이었다. 바로 지금처럼.

“눈깔 똑바로 안 떠?”

청년, 진태경이 툭 내뱉은 한마디와 함께, 한 줄기 섬광이 공간을 가로질렀다.

쐐애애애액! 뻑!



* * *



놈을 처음 봤을 때, 내 머릿속을 스친 생각은 단 하나였다.

‘내가 헛것을 보나?’

그렇게 생각할 수밖에 없었다. 현대도 아닌 무림에, 그것도 어디선가 많이 봤던 괴물이 떡 하니 눈앞에 나타났으니까.

단순히 판타지 소설에 끼워 넣은 삽화라면 모르겠는데, 애석하게도 그 출처는 지난 수십 년간 숱한 석학들과 대격변 참전 헌터들이 달라붙어 완성한 [몬스터 대백과]였다.

‘저거 설마.’

비록 지금까지의 헌터 생활 중 가장 많이 상대한 것은 고블린과 같은 하급 몬스터가 대부분이지만, [몬스터 대백과]에서 가장 많이 본 것은 최상위 몬스터들이 정리된 부분이다.

그리고 저놈은 그중에서도 크게 한 자리를 차지하고 있는 존재고.

‘……시 서펜트(Sea Serpent).’

시 서펜트는 이름에서 알 수 있듯이 해양 몬스터다.

대격변 초창기, 미 항모전단을 격침함으로써 자신의 존재를 전 세계에 알린 시 서펜트는 무슨 이유에서인지 대격변 직후 자취를 감추었다.

아니, 정정한다. 적어도 방금 전까지는 그랬다.

‘무림에 시 서펜트라니. 이게 도대체 무슨…….’

놀라움에 굳어 있던 나는 곧 이상함을 알아차렸다.

‘잠깐, 뭔가 다른데?’

내가 나고 자란 현대에서 시 서펜트는 신화에서나 등장하는 허구의 괴물이 아니다.

마왕 아스모데우스를 따르는 최상위 몬스터 중 하나이자 인류에게 심각한 피해를 입힌 주범 중 하나.

당연히 시 서펜트의 실물을 고스란히 담은 고화질 사진도 있고, 영상 전투 기록도 보존되어 있다.

그러나 지금 눈앞에 모습을 드러낸 저 괴물은 [몬스터 대백과]에 실린 시 서펜트의 모습과는 확연한 차이가 있었다.

‘시 서펜트는 오히려 바다뱀에 가까운 형태인데, 저놈은 오히려 동양적 이미지의 용에 가까워.’

자세히 보니 확실히 알 것 같았다. 몸통의 크기와 길이도, 얼굴의 생김새도 미세한 차이가 있었다.

이 비슷하지만 다른 두 마리의 괴물 사이에 가장 중요한 공통점 한가지가 있다면…….

쏴아아아악!

바로 저것이다. 무림인들이 부르는 살기와는 본질적으로 다른, 몬스터만이 타고난 흉포한 기운.

‘피어(Fear).’

피어는 말 그대로 공포요, 두려움이다.

몬스터라면 누구나 갖고 있는 것이지만 상위 몬스터일수록 그 위력은 극대화된다.

상대에게 공포와 두려움을 부여하여 적의 몸을 속박하고, 정신을 붕괴시키는 것이다.

‘그래, 동정어옹처럼 말이지.’

머릿속에서 혼잡하게 흩어져 있던 퍼즐이 맞춰진다.

어딘가 제정신이 아닌 것 같았던 동정어옹의 상태. 모든 힘이 빠져나간 후에야 돌아왔던 맑은 눈동자.

‘분명 우리보다 앞서 놈을 만났던 거야.’

높은 무위와 굳건한 정신력의 초절정 고수라 해도 난생처음 마주한 미지(未知)가 주는 공포는 상상을 훌쩍 뛰어넘는다.

오히려 피어에 한해서는 무림의 초절정 고수보다, S급 헌터가 훨씬 더 잘 대처할 수 있을 것이다.

그리고…….

‘그건 나도 마찬가지지.’

띠링.



- 당신은 [피어]에 저항했습니다!

- 강력한 정신이 공포를 이겨 냅니다!



쉭, 투둑!

혈을 짚음과 동시에 허물어지는 늙은 사공의 몸을 받아 안았다.

일 초. 아니 그 반의반만 늦었더라도 이 가엾은 노인은 피어에 미치거나, 그대로 죽어 버렸을지도 모른다.

나는 고개를 들어 저 멀리 우뚝 선 거대한 존재를 바라보았다.

‘빌어먹을. 더럽게 크네.’

시 서펜트를 상대해 본 적은 없지만, 이놈도 분명 만만찮은 놈이 확실하다.

지금 막 내가 온 힘을 실어 쏘아 보낸 창을 맞고도 쓰러지지 않을 정도니까.

뻐억!

육중한 타격음과 함께 삼십여 장에 이르는 거체가 작게 휘청인다.

마치 작은 산 하나가 움직이는 듯한 광경에, 나는 지그시 입술을 깨물었다.

‘비늘을 뚫지 못했어.’

소리만 들어도 안다. 순간 인벤토리에서 꺼낸 철창에 온 힘을 실어 쏘아 보냈음에도 큰 타격을 주지 못했다는 것을.

만년한철로 이루어진 백염을 사용했다면 보다 확실한 타격을 줄 수 있었겠지만…… 단 일격에 끝낼 수 없다면 멍청한 짓이다.

그보다는 저 엄청난 괴물이 혼란에서 빠져나오기 전에 움직이는 것이 급선무였다.

고개를 돌린 나는 심호흡과 동시에 단전에서 공력을 끌어올렸다.

“청풍! 혁무진! 궁기방!”

“흡!”

“허업!”

내 입에서 나왔다고는 믿기 힘들 만큼 거대한 고함이 터져 나오자, 석상처럼 굳어 있던 세 녀석의 신형이 움찔 떨렸다.

아니, 셋이 아니라 둘이다.

반쯤 혼이 빠져나간 눈동자를 한 궁기방, 혁무진과 달리 청풍은 깜짝 놀란 얼굴로 나를 바라보고 있었다.

“깜짝이야. 왜요, 은인?”

“……?”

이 인간은 도대체 뭐지?

저런 괴물을 보면 굳는 것이 당연하다. 현대에서 몬스터를 지긋지긋하게 접하며 성장한 나는 예외지만, 청풍은 엄연히 무림에서 나고 자란 사람. 이렇게 쉽게 피어를 이겨 낼 수 있다는 건 신기할 지경이다.

“청 소협. 정말 괜찮아?”

“네? 뭐가요?”

“그러니까 저기 보이는 저놈이…….”

“아, 맞아요. 저 진짜 깜짝 놀랐어요.”

청풍이 양팔을 펼치며 격하게 외쳤다.

“커요! 진짜 커요! 태어나서 저런 건 처음 봐요!”

“…….”

내 생각이 짧았다. 청풍은 처음부터 정신이 나간 놈이었다.
```

## Final English reading copy

```markdown
# Chapter 469

Everyone saw it. They could see it.

Amid the blackened sky and the violent rain and wind, they saw the shower of bizarre rocks pouring down from above.

*Rumble-rumble-rumble, crash!*

When a massive boulder struck the surface of the lake, spray erupted several *jang* into the air. Birds that had lost their nests tumbled from the collapsing cliff with sharp cries, while torrential rain and lightning battered the world without pause.

And as everything collapsed around them… one being alone reared up.

*Whoooooosh!*

Water streamed down its body like a waterfall.

Far below, the humans reduced to tiny dots gazed up at the being that had finally revealed itself, their eyes filled with stunned disbelief.

It was enormous.

The word felt insufficient, yet no other word came to mind.

Only one question filled everyone's head.

*What is that?*

Scales with an ominously beautiful black sheen. A sturdy torso so thick that ten large men would have to stretch out their arms to encircle it.

As their gazes traveled up the long, flexible body rising more than thirty *jang* above the surface, they saw two horns jutting from its forehead.

And beneath them, a pair of eyes.

Blood-red pupils stretched into long vertical slits. Between the slowly parting scales, saw-edged teeth emerged, along with a beast's maw that looked like a dark cave had been transplanted into its face.

“Grrrrr.”

The ominous growl that echoed down from the distant sky sent a chill deep into the bones of Crouching Dragon Guest Zhuge Feng.

*What is this…?*

Zhuge Feng had been called the greatest genius in his clan since infancy.

He possessed an exceptional mind that never forgot anything he had seen, as well as an insatiable thirst for knowledge. Over the years, he had read tens of thousands of books and made the world's vast knowledge his own.

The river of knowledge within Zhuge Feng was endlessly broad and deep.

Or so he had thought.

Until he saw that.

*This can't be.*

It was the fear of facing the unknown for the first time in his life.

At that moment, Zhuge Feng realized that all the knowledge and information he had accumulated had turned to foam.

He also realized that fragments of the many myths and legends he had dismissed as nonsense had appeared before his eyes.

*Could those absurd stories… really have been true?*

Zhuge Feng had always firmly believed in the power of his knowledge.

He was a martial artist, but first and foremost, he was the Family Head of the distinguished Zhuge Clan, and he had used reliable information and knowledge to protect his many clansmen and his family’s power.

To a man like him, unverified superstition was not worth considering. Believing in an illusion no one had ever seen was simply foolish.

But someone standing a hundred *jang* away from Zhuge Feng was different.

Unlike Zhuge Feng, he was not a Family Head responsible for an entire household. He was merely an old boatman who had survived by relying on his own experience and a single ferryboat.

“……!”

The old boatman stared into the sky with trembling eyes.

A colossal being stood tall amid the collapse of everything around it. The sight alone made his legs buckle, while unbearable awe and fear pressed down on his shabby shoulders.

The cry that the pressure kept him from releasing echoed only inside his heart.

*It’s the divine spirit. The spirit of Dongting Lake has revealed itself!*

The world was filled with more superstitions than anyone could count. Hubei Province was no exception.

An old man told a child, and when that child grew old, he told another child. Stories passed from mouth to mouth for hundreds of years.

The old boatman was no different.

A native of Hubei Province who had spent his entire life on the water, he knew the identity of the being he called a divine spirit.

The Two-Horned Beast of Dongting Lake.

The Water God Dragon.

The true master of Dongting Lake.

*Ah… ahhh…*

The old boatman trembled violently. His entire body shook beneath an incomprehensible emotion, and something surged in one corner of his chest.

It was an emotion only he, among everyone present, could feel.

Awe and fear that could never be expressed in words.

A boatman to the very marrow of his bones, he could not believe that he had come face-to-face with the master of Dongting Lake. The aura flowing from that being made it difficult to breathe.

*The divine spirit is angry. All of this happened because the divine spirit was enraged!*

The old boatman realized that his guess had been correct.

The countless deaths that had occurred one after another over the past month. He did not know why, but the divine spirit had certainly been angered beyond measure.

And in the end, it would punish him just as it had punished the others.

With death!

He could not die like this. Somehow, he had to calm the divine spirit's anger.

A cracked cry burst from the old boatman's mouth as he stood there as if entranced.

“D-Divine spirit! I have committed no sin!”

The silence that had settled over everyone shattered. The old boatman's cry scattered into the rain and wind.

Before the others, frozen rigid by the giant being's appearance, had a chance to stop him, the old boatman ran toward the water on trembling legs.

“Divine spiriiit!”

*Tap-tap-tap, splash!*

The instant the old boatman's shabby straw sandals touched the water of Dongting Lake—

*Swish.*

In a world that had slowed to a crawl, a gigantic pair of eyes turned toward him.

The old boatman's reflection appeared in the vertical, blood-red pupils. As the being recognized the tiny, insignificant human, the light in its eyes began to burn red.

*Whoooooosh!*

A chilling aura erupted in every direction from the thirty-*jang*-long body.

Birds that had been taking flight lost their strength and fell. Thousands of fish fleeing in schools through the depths of Dongting Lake floated belly-up to the surface.

An aura as immense as its body, an aura akin to death.

Neither insignificant creatures nor even humans could remain unharmed before it.

Before that invisible aura even reached him, the old boatman's entire body had already stiffened like a stone statue.

His mouth hung open, his eyes bulged wide. Just as his pupils began to roll white beneath the grip of terror—

*Whoosh! Thud!*

With a sharp whistle of something cutting through the air, the old boatman's body crumpled where he stood.

A young man gently caught his frail body, then raised his head and stared at the enormous being.

“Hey, you sibu-leol eel bastard.”

“……!”

At the clearly audible voice, the enormous being's pupils swelled as though it had realized something.

Different.

Every human on the ground had frozen from shock and fear, but that young human was different. He had neither been shocked nor trembled in fear.

Fear of the unknown came from facing something incomprehensible.

But that young human was free from all of it. It was not merely that he had no fear. He looked almost familiar with it.

Just like now.

“Can't you open those eyes properly?”

With that offhand remark from the young man, Jin Taekyung, a streak of light cut across the air.

*Whoooooosh! Thud!*

* * *

When I first saw the thing, only one thought flashed through my mind.

*Am I seeing things?*

I had no choice but to think that. A monster I had seen somewhere before had appeared right in front of me—not in the modern world, but in the Murim.

If it had merely been an illustration inserted into a fantasy novel, that would have been one thing. Unfortunately, its source was the *Monster Encyclopedia*, completed over the past several decades by countless leading scholars and Hunters who had fought in the Great Cataclysm.

*Could that be…?*

Although the monster I had fought most often during my Hunter career had been low-level creatures like goblins, the section I had looked at most in the *Monster Encyclopedia* was the one covering the highest-level monsters.

And that thing was one of the monsters given a particularly large entry.

*…A Sea Serpent.*

As its name suggested, a Sea Serpent was a marine monster.

In the early days of the Great Cataclysm, a Sea Serpent announced its existence to the entire world by sinking a US carrier battle group. For some reason, it vanished shortly after the Great Cataclysm.

No, let me correct that.

At least, that had been the case until a moment ago.

*A Sea Serpent in the Murim? What the hell is going on…?*

I stood frozen in shock, but I soon noticed something strange.

*Wait. Something's different.*

In the modern world where I had been born and raised, the Sea Serpent was not some fictional monster that appeared only in mythology.

It was one of the highest-level monsters serving the Demon King Asmodeus, as well as one of the major culprits responsible for inflicting terrible damage on humanity.

Naturally, high-resolution photographs of the Sea Serpent itself had been preserved, along with video records of its battles.

But the monster that had appeared before me now was clearly different from the Sea Serpent shown in the *Monster Encyclopedia*.

*The Sea Serpent is shaped more like a sea snake, but that thing looks closer to an Eastern dragon.*

Now that I looked closely, I was certain. The size and length of its body were slightly different, as were the shape of its face.

If there was one crucial similarity between these two monsters that were alike, yet different…

*Whoooooosh!*

It was that.

An inherently ferocious aura possessed only by monsters—fundamentally different from the killing intent martial artists called killing intent.

*Fear.*

Fear was exactly what it sounded like: terror, dread.

Every monster possessed it, but the stronger the monster, the more powerful it became.

It shackled an enemy's body by instilling fear and terror, then shattered the enemy's mind.

*Just like the Dongting Fisherman.*

The scattered puzzle pieces in my head began falling into place.

The Dongting Fisherman's state, which had seemed almost insane. His clear eyes returning only after all his strength had drained away.

*He must have encountered that thing before us.*

Even a Supreme Peak master with immense martial prowess and an unshakable mind could be overwhelmed by the fear of facing the unknown for the first time.

In terms of Fear alone, an S-rank Hunter would probably be much better equipped to deal with it than a Supreme Peak martial artist.

And…

*That goes for me, too.*

*Ding.*

> **System**
>
> - You resisted **Fear**!
> - A powerful mind overcomes terror!

*Whoosh, thud!*

I caught the old boatman's collapsing body as I struck his pressure points.

One second. No—even a quarter of a second later, and this poor old man might have gone mad from Fear or simply died.

I raised my head and looked at the enormous being standing in the distance.

*Damn. It's huge.*

I had never fought a Sea Serpent, but this thing was clearly no pushover.

It had just taken a spear I had hurled with all my strength and still had not fallen.

*Bam!*

With a heavy impact, the colossal body, more than thirty *jang* long, swayed slightly.

The sight was like watching a small mountain move. I bit down gently on my lip.

*I couldn't pierce its scales.*

I could tell from the sound alone. Even after pouring all my strength into the iron spear I had just taken from my Inventory, I had failed to inflict any meaningful damage.

If I had used White Flame, forged from Ten-Thousand-Year Cold Iron, I could have dealt a more decisive blow.

But if I could not finish it in One Strike, that would be a foolish move.

It was more urgent to act before the enormous monster recovered from its confusion.

I turned my head and drew a deep breath as I pulled internal energy up from my dantian.

“Cheongpung! Hyuk Mujin! Gung Gibang!”

“Hup!”

“Urgh!”

A thunderous shout burst from my mouth, so massive that it was hard to believe it had come from me. The bodies of the three men, who had been frozen like stone statues, flinched.

No.

Not three. Two.

Unlike Gung Gibang and Hyuk Mujin, whose eyes looked as though half their souls had left their bodies, Cheongpung was staring at me with a startled expression.

“You startled me. What is it, Benefactor?”

“……?”

*What the hell is this guy?*

Anyone would naturally freeze upon seeing a monster like that. I was the exception because I had been exposed to monsters to the point of loathing them while growing up in the modern world.

But Cheongpung had been born and raised in the Murim. The fact that he could overcome Fear so easily was astonishing.

“Young Hero Cheongpung. Are you really all right?”

“Huh? What about it?”

“I mean, that thing over there…”

“Oh, right. I was really surprised.”

Cheongpung spread both arms and cried out emphatically.

“It’s huge! Really huge! I’ve never seen anything like that in my life!”

“……”

*I hadn’t thought that through.*

*Cheongpung had been out of his mind from the beginning.*
```
