<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0661.txt",
      "sha256": "0f09a29385737b864818d4dcdcbb670ce974595f5d1dfde5f4107c93270a744d",
      "bytes": 12969
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "c0181a2a07e34ef1b6548232383a44b2d57014b21950ffe2f8c89f87a0931a9a",
      "bytes": 2011
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "aa09fe9264d1605c6d8316c15ac2ec14070082e6f52eea1795793801ec67719c",
      "bytes": 201081
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "b18b703521394b5348add28dbdd08ae56bbdda7dd6ddaedfc31cc4e7a0ba674d",
      "bytes": 893
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "1cad61ace58846901dbf60fe6886caaf462be377d19f7f3dd478b1b8a7ba02fe",
      "bytes": 814
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "9103b0e30080f490d2e6f80542b8ef787c648131141f2d91cee44fcee4f04fcb",
      "bytes": 1325
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "ca0514b6ee46a580c4eaf5030ab4a70cbd0c960faf627554992e045ff6a339c3",
      "bytes": 553
    },
    {
      "path": "characters/Heugung.md",
      "sha256": "346ed05f81f1bd191886ca9ec60786c7255f30c4ead4a4266924d830a35d09bd",
      "bytes": 769
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "2a8f8c8dbbe5498c17d0a095678e258503fbb755ba64940e1db1d51decc89e11",
      "bytes": 1464
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "c42354de7c883290457cb387e6d2e580067b538ee10ed78ecd363b01b2e6c94b",
      "bytes": 1886
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "54de6db56c7668b74bcfb8e3c492d6fca7b9088ea0e33e9bd776a82c2c4ab85e",
      "bytes": 622
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "567f0b941eba8eec9df5d1bbbade0c8b14ceefe7a106bb3b5e3b8d3bcb898d53",
      "bytes": 626
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "327aad1d2bd85c666aee21eb75fd16b9a4872fb210467ada5b9e4855732922cb",
      "bytes": 871
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "f82cb4dd923b462216143e921491f262451f4d8ba001d2b5ca14205ecbc83cd1",
      "bytes": 645
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "c992eb564fa2be29ef70d87aa51e35ee3f5d2d5eb3ffb8a73495b3e7dcbbb0e8",
      "bytes": 206515
    }
  ],
  "estimated_tokens": 12912
}
-->

# Durable State Update — Chapter 661

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 661. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 661. Profile updates may replace only one
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
  "chapter": 661,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 661,
    "continuity_sources": [661],
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
    "Jin remains the Third Young Master of the Jin Family of Taiyuan, head of the Fire Dragon Pavilion, and a Supreme Peak master.",
    "The Fire Dragon Pavilion was attacked after Jin left, and Dark Heaven is suspected of organizing or enabling the assault.",
    "Heugung and Yohi remain missing after the destruction of Yohi's Western Yao Estate.",
    "Baeksang has imprisoned Jin in the Nanman Beast Palace's underground prison and scheduled his public execution for noon in two days.",
    "Jin is bound with massive iron balls and cannot use internal energy because of a Force-Sealing Pill.",
    "Chief Jang and Chief Go are secretly keeping the three Han Chinese reconnaissance-squad captives away from the Inner Palace to protect them.",
    "Song Ilseom and Hyuk Mujin are bound and unconscious after being struck at their Sleep Acupoints.",
    "Ju Hwaran remains among the captives held by the reconnaissance squad.",
    "The reconnaissance squad is traveling through Nanman while guarding against the Blood Monk.",
    "Jin accuses Baeksang of betraying Nanman to Dark Heaven and remains committed to protecting his people."
  ],
  "continuity_sources": [
    660
  ],
  "open_questions": [
    "What happened in the Inner Palace, and why did the Nanman Beast Palace issue the sealed order?",
    "Where is Ju Hwaran being held, and what will happen to her?",
    "Can Song Ilseom and Hyuk Mujin escape captivity?",
    "Can Jin survive Baeksang's scheduled public execution?",
    "What role did Baeksang play in the attacks and the alleged collusion with Dark Heaven?"
  ],
  "safe_through": 660,
  "temporary_decisions": [
    "Retain Force for 강기 and Supreme Peak for 초절정.",
    "Retain Sound Transmission for 전음 and Either-Or for 양자택일.",
    "Retain underground prison for 뇌옥 and iron balls for 철구.",
    "Use Chief Jang for 장 족장 and Chief Go for 고 족장.",
    "Use Force-Sealing Pill for 금력단."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 무신     | **Martial God**               | —              |
| 삼성     | **Three Saints**    |
| 십왕     | **Ten Kings**       |
| 태원진가   | **Jin Family of Taiyuan**        |
| 종남파    | **Zhongnan Sect**                |
| 무림맹    | **Murim Alliance**               |
| 사천당가   | **Sichuan Tang Clan**            |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 정파     | **orthodox faction**                             |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 상태               | **Status**                     |
| 로그아웃             | **Logout**                     |
| 태원     | **Taiyuan**            |
| 사천     | **Sichuan**            |
| 감숙     | **Gansu**              |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 흑웅 | **Heugung** | Great chieftain of the Yi people; his name literally means Black Bear. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 당가 | **Tang Family** | Short form for the Sichuan Tang Clan when distinguished from 사천당문. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |
| 사혈 | **lethal acupoint** | An acupoint whose strike can kill. |
| 시리 | **City** | Second word in one of the necromantic chants. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 철구 | **iron balls** | Training weights attached to Taekyung. |
| 장성 | **Great Wall** | Wall used in the discussion of the Outer Lands. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 대회의 | **Tribal Grand Council** | Nanman's council of great chieftains. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |

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
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 야율목 | 진태경 | Nanman_Beast_Palace_Young_Palace_Lord_to_Han_intruder_and_Murim_Alliance_Pavilion_Master | you | formal but hostile | Asks Jin's identity and orders him to follow after learning he belongs to the Murim Alliance. |
| 진태경 | 야율목 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Young_Palace_Lord | Mok | casual, teasing, and insulting | Calls him rude and later addresses him as 목아 while jokingly claiming they are friends. |
| 야율목 | 백상 | nephew_to_father's_sworn_younger_brother | Uncle Baeksang | ceremonial and deferential | Yayul Mok formally greets Baeksang as he arrives at the stone door. |
| 백상 | 야율목 | father's_sworn_brother_to_nephew | you | cold and formal | Baeksang questions Yayul Mok about his return, the pasture fire, and the Palace Lord's whereabouts. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 요희 | 흑웅 | Yao great chieftain to Yi great chieftain | big brother | seductive and falsely affectionate | Uses 오라버니 to flatter and manipulate Heugung. |
| 흑웅 | 요희 | Yi great chieftain to Yao great chieftain | my dear | adoring and deferential | Responds to Yohi's manipulation with open infatuation. |
| 요희 | 진태경 | Yao great chieftain to Murim Alliance pavilion master | Jin Taekyung | casual and probing | Identifies him by his full name while allowing him to keep the mask on. |
| 진태경 | 요희 | Fire Dragon Pavilion pavilion master to Yao great chieftain | you | guarded and blunt | Answers Yohi's probing questions directly while warning her about Ju Hwaran. |
| 백상 | 요희 | Bai great chieftain to Yao great chieftain | Yohi | cold and formal | Calls to Yohi from outside the tent at the chapter's end. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 야율목 | 야수묘왕 | son_to_father | Father | formal and deferential | Yayul Mok calls out to the Beast Miao King after the rescue party arrives. |
| 흑웅 | 백상 | younger_great_chieftain_to_senior_great_chieftain | Uncle Baek | deferential and nervous | Heugung addresses Baeksang as 백 숙부 after being confronted by his icy stare. |
| 백상 | 야수묘왕 | Nanman great chieftain to the Nanman Beast Palace Lord | Palace Lord | restrained and apologetic | Apologizes for causing the disturbance after the Beast Miao King stops the fight. |
| 흑웅 | 진태경 | Nanman great chieftain to Central Plains ally and covert contact | you | cautious and informal | Heugung uses 자네 in private Sound Transmission while explaining the missive and Baeksang's alleged collusion. |
| 진태경 | 흑웅 | Central Plains investigator to covert informant and prospective witness | Heugung | blunt and confrontational | Jin questions Heugung's reliability, challenges his claims, and demands proof. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 660
- **Aliases:** None
- **Role:** Baeksang is the middle-aged great chieftain of the Bai people, one of Nanman's four most powerful great tribes, and one of only two Supreme Peak masters in Nanman; he has imprisoned Jin Taekyung and ordered his public execution.
- **Personality:** Cold, rigid, meticulous, politically resolute, and strategically manipulative, with a deep but guarded attachment to his sworn elder brother.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion and Yayul Mok's sworn uncle, opposes the Nanman Beast Palace joining the Murim Alliance, remains distrustful of the Central Plains, and is alleged by Heugung to have colluded with Dark Heaven.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 660
- **Aliases:** None
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, the great chieftain of the Miao people, a master among the Ten Kings, and one of only two Supreme Peak masters in Nanman.
- **Personality:** Fierce and vigilant when confronting threats to the Nanman Beast Palace.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace, is Baeksang's sworn elder brother and childhood companion, is responsible for the forces stationed at Ailao Mountain, has ordered Ju Hwaran, Song Ilseom, and Hyuk Mujin to investigate the Blood Monk in Guizhou, and met the Martial God twice more than fifty years ago.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 551
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak martial master known as the Huashan Divine Dragon, the creator of the snake-inspired Mimi Step footwork technique, and the master of the Azure Dragon Pavilion within the Alliance Leader's Two Dragons Pavilion.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi, now a large horned snake, to him, and Cheongpung is accompanying Mungyeong while learning his martial arts through observation to become stronger and adapt to this world.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 660
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Heugung.md

# Heugung (흑웅)

- **Safe through:** Chapter 660
- **Aliases:** None
- **Role:** Heugung is the middle-aged great chieftain of the Yi people, one of Nanman's four great tribes.
- **Personality:** Heugung presents as foolish and easily flattered in public but is capable of concealed planning, disguise, and covert contact.
- **Voice:** Heugung speaks with warm enthusiasm and genuine, openly devoted affection toward Yohi.
- **Relationships:** Heugung genuinely loves Yohi and had promised to cooperate with Jin Taekyung; he disappeared alongside Yohi after the assault on the Fire Dragon Pavilion, and his death remains unconfirmed after a severed wrist believed to be his was found at her estate.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 660
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and a member of the Fire Dragon Pavilion; he is currently bound and unconscious under the reconnaissance squad's guard after being struck at a Sleep Acupoint.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 660
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance; he is a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license, and he is currently imprisoned under Baeksang's order with a public execution scheduled.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 660
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 647
- **Aliases:** None
- **Role:** The Martial God is an unidentified legendary martial artist who defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone more than fifty years ago.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, appearing first as a white-bearded elder and later as a young boy; his identity, whereabouts, and possible connection to Cheon Taemin remain unknown.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 658
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, a spear-wielding warrior who rides a white tiger, and a halting but capable speaker of Han Chinese.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King and Yayul Mok's father; Yayul Mok is his only surviving son after three older siblings died in the Great Faction War, Baeksang is his father's sworn younger brother, and his white tiger is a long-bonded companion.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 660
- **Aliases:** None
- **Role:** Yohi is the female great chieftain of the Yao people, one of Nanman's four great tribes.
- **Personality:** Yohi's public presence is charismatic and captivating, drawing widespread admiration and affection.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people, seeks to unite Nanman's four great tribes under Yao leadership, manipulates Heugung alongside Baeksang, and has disappeared from the Inner Palace alongside Heugung after the assault on the Fire Dragon Pavilion.

## Korean source

```text
＃661화



이틀 뒤 정오. 그리고 처형.

백상의 입술 사이로 흘러나온 그 짧은 두 개의 단어가, 총알처럼 쏘아져 뇌리를 관통한다.

‘이틀 뒤 처형? 내가?’

목구멍을 비집고 솟구치는 물음을 참았다. 적어도 이 자리에서, 그것도 백상에게 흔들리는 모습을 보여 줄 수는 없었으니까.

나는 절망하는 대신, 혹시나 하는 마음으로 이미 몇 번이나 가로막힌 탈출구를 두드렸다.

‘로그아웃.’

삐빅!



- [로그아웃]에 실패했습니다!

- 특정 상황에서는 [로그아웃]이 불가능합니다!



좆 됐다. 아직도 안 되네.

나는 애써 담담한 목소리로 입을 열었다.

“이틀이라. 생각보다 빠른데.”

“선친께서는 항상 말씀하셨지. 한번 뜻을 정했다면, 망설임 없이 검을 뽑으라고.”

“그 검, 혼자 뽑는 건 아니고?”

“가장 먼저 검파를 쥔 것은 나지만, 네 목을 휘두를 때는 혼자가 아닐 것이다. 설령 궁주라 해도 막을 수 없어.”

검을 휘두르는 것은 혼자가 아니다…….

조용히 그 말의 의미를 되새긴 나는 혼잣말처럼 중얼거렸다.

“어지간히 바쁘게도 돌아다닌 모양이군. 그새 여기저기 손을 뻗은 걸 보면.”

백상이 건조한 목소리로 대답했다.

“이미 나를 포함한 스무 명의 부족장들이 뜻을 모았다. 그리고 대회의 마지막 날의 안건은…….”

“태원진가의 진태경. 아니, 이제 천인공노할 죄인이 되어 버린 내 처형에 관한 거겠지.”

“잘 아는군.”

“일이 여기까지 왔는데도 모르면 병신 아닐까. 어쨌든 그러기 위해서 나를 우선 뇌옥에 처넣었던 건가?”

“물론, 가장 손쉬운 방법이었지. 네놈이 이렇게 쉽게 투항할 줄은 몰랐지만.”

백상은 부정하지 않았다. 그리고 마치 사냥감을 포획한 엽사(獵師)처럼, 만근에 달하는 철구로 속박된 나를 내려다보며 나직한 음성으로 말을 이었다.

“호랑이를 잡기 위해서는 산으로 가서 위험을 감수해야 하지만, 철창 안에 갇혀 있는 호랑이라면 이야기가 다르지 않겠느냐.”

“그렇겠지. 게다가 사냥꾼이 혼자도 아니고 스물이라면.”

백상을 따르는 부족장의 숫자는 본래에도 적지 않았다. 하지만 스물이라니.

이는 흑웅과 요희가 실종된 이후 서른 명으로 줄어든 인원의 과반수를 뛰어넘는 숫자였고, 야수묘왕의 편에 서 있던 부족장 중 일부가 말을 바꿔 탔음을 뜻했다.

“도대체 그들에게 얼마나 대단한 걸 약속한 거지?”

“일족의 부흥. 더욱 큰 영향력과 막대한 재화.”

“그것참. 예상은 했는데 빌어먹게 간단하네.”

“하지만 무엇보다 효과적이지.”

단둘만이라는 확신이 있어서일까.

오늘 백상의 대답은 그 어느 때보다 솔직했고, 한편으로는 부정할 수 없는 사실들로 이루어져 있었다.

안타깝지만 놈의 말이 맞다. 남만야수궁은 엄연한 부족 연합체고, 각자 나름대로 현재 돌아가는 판세를 파악한 부족장들은 가장 승산 있는 쪽에 배팅했을 것이다.

자신이 다스리는 부족의 미래. 자신들이 얻을 부귀영화를 위해서.

그리고…….

“그중에서도 가장 큰 대가를 받을 사람이 지금 내 눈앞에 있네. 남만 전체를 손에 넣을 테니까. 안 그래?”

내 물음에 백상은 대답 대신 입을 다물었고, 나는 헛웃음을 흘렸다.

“재미있네. 아주 뿌리부터 썩을 대로 썩은 게.”

바로 그 순간이었다. 마음을 꿰뚫어 보는 듯한 시선으로 나를 응시하던 백상이 불쑥 한마디를 내뱉은 것은.

“전란을 겪은 적이 있느냐?”

“뭐?”

“전란을 겪은 적이 있느냐 물었다.”

왜 갑자기 이런 이야기를 시작하는 걸까.

하지만 백상의 의도를 알건 모르건, 창살에 갇힌 호랑이 신세가 된 내게는 듣는 것 외에 별다른 선택지가 없었다.

“나는 그 모든 것을 직접 겪어 보았다. 오십여 년 전, 궁주와 함께 일만의 전사들을 이끌고 중원에 도착한 내가 처음 목격한 것은, 인세에 도래한 지옥이었지.”

백상은 천천히, 또 담담하게 말을 이어갔다.

“논밭은 짓밟혔고 푸른 강은 핏물와 시체로 잠겼다. 매일. 혹은 매 순간 사람들이 천하 곳곳에서 죽어 나갔고, 전쟁으로 부모를 잃고 굶주림에 사로잡힌 아이들은 제 이빨이 뽑히는 것도 모르는 채 나무껍질을 뜯어 먹었지.”

전쟁은 언제나 참혹하다. 끝내 누군가는 승리할지라도 그 과정에는 숱한 비명과 죽음이 쌓여 있다.

승자도, 패자도 피해 갈 수 없는 하나뿐인 길이다.

“그것은 나도, 궁주로서도 처음 보는 지옥도(地獄道)였다. 하지만 우리는 싸워야 할 이유가 있었기에 그 누구도 물러서지 않았다. 만일 마교가 중원을 지배한다면, 그다음은 남만이 될 테니까. 내 가족과 벗이 머무르고 있는 고향을 지키기 위해 우리는 그곳에 있었다.”

백상의 목소리가 어두컴컴한 뇌옥을 울렸다.

“헤아릴 수도 없을 만큼 많은 목숨이 사라졌다. 전장에서 적과 싸우다 목숨을 잃고, 전투가 끝난 뒤 멍하니 하늘을 바라보다가 스스로 자결하고, 고통에 몸부림치는 전우를 대신해 그의 사혈(死穴)을 짚어 주기도 했지.”

“…….”

“수 없이 반복되는 전투에 누군가는 죽고 누군가는 지쳐 갔지만, 전세가 유리해질수록 마음 한구석에 품은 희망은 커져만 갔다. 이제 곧 고향으로 돌아갈 수 있을 거라고. 사랑하는 여인과 연로한 부모. 혹은 부쩍 장성했을 아이들을 만날 수 있을 거라고.”

겪지 않았어도 느껴진다.

보지 못했어도 눈앞에 그려진다.

밀림을 지나 장강을 건너고, 평야와 산을 넘어 머나먼 중원에 막 도착한 그들의 모습이. 그리고 매일 같이 사방에서 몰려드는 마교의 십만마도(十萬魔徒)에 맞서 싸우는 전장의 광경이.

“문득 숫자를 헤아려 보니 일만의 전사 중 살아남은 이는 일 할도 채 되지 않더군. 서서히 유리해지던 전황마저 어느 순간 고착 상태에 빠졌고, 궁주와 나는 생각했다. 왜 우리가 이곳에 있어야 하는지.”

세월은 누구도 대적할 수 없는 법칙이다. 산을 움직이고 강물을 마르게 만드는 그 절대적인 법칙 앞에서는, 초절정의 경지에 다다른 고수도 어찌할 수 없었다.

‘마음이 마모됐겠지. 천천히. 이 이상은 버틸 수 없을 만큼.’

내심 중얼거린 그때, 백상의 목소리가 이어졌다.

“그렇게 십여 년이 지난 어느 날이었다. 무신(武神)이 천마(天魔)를 쓰러트린 것은.”

두 절대자의 격돌.

이 경천동지할 생사결(生死決)의 결과는 무신의 승리였고, 한때 천하의 절반을 집어삼켰던 마교는 천마라는 구심점을 잃자 모래성처럼 무너져 내렸다.

“마교의 잔당들은 서쪽으로 퇴각했고, 무림맹은 놈들을 끝까지 추격하여 섬멸하고자 했다. 이제 그 누구도 막을 수 없는 무신을 필두로 삼성(三星)과 십왕(十王). 그리고 무림맹에 속한 수많은 정파 무림인들이 사방에서 진격했지. 우리 역시 예외는 아니었다.”

그렇지 않아도 서서히 정파 무림으로 기울던 저울추는 천마의 죽음으로 인하여 존재 의미를 상실했다.

이제 남은 것은 패잔병으로 전락한 십만 마도를 추격, 섬멸하여 중원 땅에서 뿌리 뽑는 것뿐이었다.

“전쟁은 이미 끝난 것이나 다름없었다. 아니, 반드시 그랬어야 했어.”

불현듯 말을 멈춘 백상은 공허한 눈빛으로 허공 어딘가를 응시했다.

미세하게 갈라진 천장 틈새로 흘러나온 물방울이 차가운 바닥 위로 떨어진다.

툭. 투둑.

잠시 무거운 침묵이 흘렀다. 기다려도 입을 열지 않는 백상을 가만히 바라보던 나는, 이내 불쑥 입을 열었다.

“백휘(白輝). 맞지?”

“……!”

덜컥 굳은 신형과 요동치는 눈동자. 그 어느 때보다 동요하는 백상의 모습에 나는 작게 고개를 끄덕였다.

“맞나 보네. 혹시 이름을 헷갈렸나 했는데.”

으득.

다물어져 있던 입술 사이로 뭔가가 부서지는 소리가 들린다. 백상이 차갑게 가라앉은 눈빛으로 입을 열었다.

“그 이름, 누구에게 들었지?”

내게 그 이름을 말해 준 사람은 야율목이었지만, 굳이 그 사실을 알려 줄 필요는 없다.

나는 담담하게 대꾸했다.

“그게 그렇게 중요한가? 지금까지도 백휘라는 이름을 기억해 주는 사람이 있다는 게 중요한 거지.”

“……감히 네놈 따위가 입에 담을 수 있는 이름이 아니다.”

화아아악!

백상의 전신에서 일어난 칼날 같은 살기가 쇠창살 틈새로 쏘아진다.

하지만 어째서일까. 이상하게도 두려움은 들지 않았다.

그리고 아마도 그건…… 오래전에 어린 핏줄을 먼저 떠나보내야 했던 아비를 향한 한 줄기 연민일지도 모르겠다.

모든 것을 떠나 적어도 지금 이 순간만큼은 그랬다.

‘백휘.’

흰 백. 빛날 휘.

그건 한 사람의 이름이었다. 백상이 끔찍하게 아끼던 하나뿐인 자식이자, 살아 있었다면 야수묘왕의 사위가 되었을 누군가의 이름.

‘그래. 살아 있었다면, 말이지.’

마음속으로 작게 뇌까린 나는, 백상이 뿜어내는 살기를 무시하며 물었다.

“마교를 추격하던 도중에 목숨을 잃었나? 아니면…….”

쾅! 구구궁!

이어지려는 목소리를 굉음이 집어삼킨다. 그와 동시에 엄청난 충격파에 의해 거세게 뒤흔들리는 뇌옥.

일권으로 뇌옥의 벽면을 가루로 만들어 버린 백상이 서릿발 같은 눈으로 나를 응시했다.

“당장 이 자리에서 죽고 싶으냐?”

현재의 내 처지를 생각한다면 제법 위협적인 한 마디다. 아마 혁무진이었다면 오줌을 지리고 묵언 수행에 들어갔겠지.

하지만 어디에나 예외는 있는 법이다.

죽는 것조차 처음이라며 살짝 설레할지도 모르는 청풍도 있고…….

뭐, 하도 여기저기에서 구르다 보니 간 비대증에 걸린 나도 마찬가지다.

“그것도 나쁘진 않지. 어차피 당장은 죽이지도 못하겠지만.”

“뭐라?”

“내 처형을 굳이 이틀 뒤로 미룬 이유가 있을 거 아냐. 물론 그것 역시 당신 혼자서 내린 결정은 아니겠지. 남천마후의 명령인가? 내가 듣기로는 매달 초하루마다 전서를 주고받는다던데.”

“……!”

“그러니까 허세 그만 부리고 썰이나 풀어 봐. 뇌옥에 혼자 갇혀 있으니까 외롭고 심심하더라. 그나마 사천당가에는 다른 죄수들이라도 있어서 괜찮았는데.”

“놈!”

쩌렁쩌렁한 외침이 메아리처럼 울려 퍼진다. 분노로 파르르 몸을 떤 백상이 손을 뻗어 쇠창살을 움켜쥐었다.

그그그극!

어른 팔뚝만 한 강철이 엿가락처럼 휘어진다. 그 사이로 성큼 걸어들어온 백상의 눈동자가 시리도록 차갑게 빛났다.

“휘. 그 아이의 죽음이 네게는 그리 재미있고 궁금하더냐?”

당장이라도 검을 뽑아 베어 버릴 것만 같은 흉흉한 기세. 하지만 나는 개의치 않았다.

어차피 놈은 남천마후가 두려워서라도 당장 이 자리에서 나를 죽이지 못할 것이고, 나는 알아야 할 사실이 있었다.

“재미있는 건 모르겠고. 궁금한 부분은 있지.”

“네놈이 정녕…….”

“말해.”

무덤덤한 목소리로 백상의 말을 자른 내가, 천천히 말을 이었다.

“당신의 하나뿐인 자식이 어떻게 죽었는지가 아니라, 어떤 미친놈들이 당신 같은 미친놈을 만들었는지.”

“……!”

“그걸 말하라고.”

그리고 일 초가 일각처럼 느껴질 만큼 무거운 침묵 끝에, 마침내 백상의 입술이 열렸다.

“감숙(甘肅). 대설산(大雪山).”

후우.

파르르 떨리는 호흡. 얼음장처럼 차가운 뇌옥에 새하얀 입김이 쏟아진다. 마치 그날에 내렸을 함박눈처럼.

“그때의 우리는, 종남파와 함께 남군(南軍)을 이끌고 있었다.”

귓가를 파고드는 한 마디에, 나는 본능적으로 튀어나오려는 목소리를 삼켰다.

아, 시발 종남파.
```

## Final English reading copy

```markdown
# Chapter 661

Two days later, at noon.

And then, execution.

The two short words that slipped between Baeksang’s lips shot through my mind like bullets.

*Execution in two days? Me?*

I swallowed the question rising up my throat. At least here—not in front of Baeksang—I couldn’t afford to show him that he had shaken me.

Rather than despair, I once again knocked on the escape route that had already been blocked several times.

*Logout.*

Beep!



> **System**
>
> - **Logout** failed!
>
> - **Logout** is unavailable in certain situations!

*I’m fucked. Still not working.*

I forced myself to speak in a calm voice.

“Two days. That’s sooner than I expected.”

“My late father always used to say this: once you have made up your mind, draw your sword without hesitation.”

“You’re not drawing that sword alone, are you?”

“I may be the first to take hold of the hilt, but when the sword swings for your neck, I will not be alone. Not even the Palace Lord can stop it.”

*I will not be alone when I swing it.*

I quietly mulled over the meaning of those words, then muttered as if speaking to myself.

“You must have been awfully busy running around. Judging by how many places you’ve reached out to in the meantime.”

Baeksang answered in his dry voice.

“Twenty tribal chieftains, including myself, have already joined forces. And the matter on the agenda for the final day of the Tribal Grand Council will be…”

“Jin Taekyung of the Jin Family of Taiyuan. No—my execution, now that I’ve become a criminal guilty of a crime that outrages heaven and humanity.”

“You understand quickly.”

“I’d have to be a fucking idiot not to, with things already this far along. Anyway, is that why you threw me into the underground prison first?”

“Of course. It was the easiest way. I didn’t expect you to surrender so readily, though.”

Baeksang did not deny it. Like a hunter looking down at captured prey, he gazed at me, bound by iron balls weighing nearly ten thousand geun, and continued in a low voice.

“To catch a tiger, you have to venture into the mountains and take the risk. But a tiger locked inside a cage is a different matter, wouldn’t you say?”

“I suppose it is. Especially when the hunter isn’t alone, and there are twenty of them.”

The number of tribal chieftains following Baeksang had never been small. But twenty?

That was more than half of the thirty chieftains remaining after Heugung and Yohi disappeared. It meant that some of the chieftains who had stood on the Beast Miao King’s side had switched allegiances.

“What exactly did you promise them?”

“Revival for their tribes. Greater influence and enormous wealth.”

“Well, that’s something. I expected as much, but it’s damn simple.”

“But more than anything, it is effective.”

Perhaps because he was certain we were truly alone.

Baeksang’s answers today were more honest than ever. At the same time, they consisted of facts I could not deny.

Unfortunately, he was right. The Nanman Beast Palace was, after all, an alliance of tribes, and the tribal chieftains—each of whom had assessed the situation in his own way—had bet on the side with the greatest chance of victory.

For the future of the tribes they ruled.

For the riches and glory they would gain.

And…

“Among them, the person who will receive the greatest reward is standing right in front of me. You’ll take all of Nanman for yourself. Isn’t that right?”

Baeksang said nothing in response. I let out a hollow laugh.

“Interesting. It’s rotten right down to the roots.”

That was when Baeksang, who had been staring at me as if he could see straight through my heart, suddenly spoke.

“Have you ever experienced a war?”

“What?”

“I asked whether you have ever experienced a war.”

Why had he suddenly started talking about this?

But whether I understood Baeksang’s intentions or not, I had little choice but to listen. I was a tiger trapped inside a cage, after all.

“I experienced all of it firsthand. More than fifty years ago, when I arrived in the Central Plains with the Palace Lord and ten thousand warriors, the first thing I saw was hell brought into the human world.”

Baeksang continued slowly and calmly.

“Farmlands were trampled, and blue rivers were choked with blood and corpses. Every day—or sometimes every moment—people died all across the land. Children who had lost their parents to the war and been consumed by hunger tore at tree bark and ate it without even realizing that their own teeth were being torn out.”

War was always horrific. Even if someone ultimately emerged victorious, the process was built upon countless screams and deaths.

It was the one path neither victor nor loser could avoid.

“It was a hellscape unlike anything I—or even the Palace Lord—had ever seen before. But we had a reason to fight, so none of us retreated. If the Demonic Cult took control of the Central Plains, Nanman would be next. We were there to protect the homeland where my family and friends lived.”

Baeksang’s voice echoed through the dark underground prison.

“An uncountable number of lives disappeared. Some died fighting the enemy on the battlefield. Others stared blankly at the sky after the fighting ended, then took their own lives. At times, we even had to strike the lethal acupoints of comrades writhing in pain.”

“…”

“Someone died in one battle after another, while others grew exhausted. But as the tide of war gradually turned in our favor, the hope held in a corner of our hearts only grew stronger. Soon, we would be able to return home. Soon, we would see the women we loved and our aging parents. Or the children who had grown so much in our absence.”

I had never experienced it, yet I could feel it.

I had never seen it, yet it appeared before my eyes.

Their figures as they crossed the jungles, passed over the Yangtze, and crossed plains and mountains before finally arriving in the distant Central Plains. The battlefield where they fought the Demonic Cult’s hundred thousand practitioners of the Demonic Path, who came rushing from every direction day after day.

“When I stopped to count, fewer than one-tenth of the ten thousand warriors were still alive. Even the tide of battle, which had been slowly turning in our favor, eventually fell into a stalemate. The Palace Lord and I began to wonder why we had to remain there.”

Time was a law no one could oppose. Before that absolute law, which could move mountains and dry up rivers, even a master who had reached the Supreme Peak realm could do nothing.

*Their hearts must have been worn away. Slowly. Until they could no longer endure any more.*

Just as I muttered that inwardly, Baeksang’s voice continued.

“More than a decade had passed when, one day, the Martial God defeated the Heavenly Demon.”

The clash between two absolute beings.

The result of that life-and-death duel that shook heaven and earth was the Martial God’s victory. Once the Demonic Cult—which had devoured half the world—lost its central figure, the Heavenly Demon, it collapsed like a sandcastle.

“The remnants of the Demonic Cult retreated west, and the Murim Alliance sought to pursue and annihilate them to the very end. Led by the Martial God, whom no one could stop anymore, the Three Saints and the Ten Kings advanced from every direction, along with countless orthodox martial artists belonging to the Murim Alliance. We were no exception.”

The scales, which had already been gradually tipping toward the orthodox factions, lost all meaning with the Heavenly Demon’s death.

All that remained was to pursue the hundred thousand practitioners of the Demonic Path, now reduced to defeated soldiers, annihilate them, and uproot them from the Central Plains.

“The war was as good as over. No—it should have been.”

Baeksang suddenly stopped speaking and stared blankly at some point in the air.

A drop of water leaked through a tiny crack in the ceiling and fell onto the cold floor.

Drip. Drip-drip.

A heavy silence settled over the underground prison.

I quietly watched Baeksang, who did not open his mouth even after I waited for him to continue. Then, all at once, I spoke.

“Baekhwi. That was his name, wasn’t it?”

“……!”

Baeksang’s body went rigid, and his eyes began to tremble. Seeing him more shaken than ever before, I gave a small nod.

“So I got it right. I wondered if I had mixed up the name.”

Crunch.

Something broke between Baeksang’s tightly closed lips. He opened his mouth, his eyes cold and sunken.

“Who told you that name?”

Yayul Mok was the one who had told me, but there was no reason to reveal that.

I answered calmly.

“Does that really matter? What matters is that there’s still someone who remembers the name Baekhwi.”

“Someone like you has no right to speak that name.”

Whoosh!

Killing intent as sharp as a blade erupted from Baeksang’s entire body and shot through the gaps between the iron bars.

But why?

Strangely, I wasn’t afraid.

Perhaps it was a thread of compassion for a father who had lost his young child long ago.

At least, that was how I felt in this moment.

*Baekhwi.*

*Baek, white. Hwi, shining.*

It was one person’s name. The name of Baeksang’s only child, whom he had cherished terribly—the name of someone who, had he lived, would have become the Beast Miao King’s son-in-law.

*If he had lived.*

I muttered the words inwardly, then ignored the killing intent pouring from Baeksang and asked,

“Did he lose his life while pursuing the Demonic Cult? Or…”

Boom! Rumble!

The roar swallowed the words that were about to follow.

At the same time, the underground prison shook violently beneath an immense shock wave.

Baeksang had pulverized part of the prison wall with a single punch. He stared at me with eyes cold as frost.

“Do you want to die here and now?”

Considering my current situation, it was a fairly threatening statement. If Hyuk Mujin had been in my place, he probably would have pissed himself and begun practicing silent meditation.

But there were exceptions to everything.

There was also Cheongpung, who might even have been a little excited at the thought of dying because it would be his first time…

And then there was me, whose liver had probably enlarged from being knocked around everywhere.

“That wouldn’t be so bad. Though you can’t kill me right now anyway.”

“What did you say?”

“There must be a reason you put off my execution for two days. Of course, that wasn’t a decision you made alone, either. Was it an order from the Southern Heaven Demon Empress? I heard you exchange missives on the first day of every month.”

“……!”

“So stop posturing and tell me the story. Being locked alone in an underground prison gets lonely and boring. The Sichuan Tang Clan at least had other prisoners, so it wasn’t so bad.”

“You bastard!”

His roar rang out like thunder, echoing through the prison.

Baeksang’s body trembled with rage as he reached out and gripped the iron bars.

Groan!

The steel, as thick as an adult’s forearm, bent like taffy. Baeksang stepped through the opening, and his eyes shone with a chill that stung my skin.

“Hwi. Is the death of that child so amusing and intriguing to you?”

His aura was so vicious that it seemed he might draw his sword and cut me down at any moment.

But I did not care.

He could not kill me here and now, if only because he feared the Southern Heaven Demon Empress. And there was something I needed to know.

“I don’t know if amusing is the right word. But there is one thing I’m curious about.”

“You really are…”

“Tell me.”

I cut him off in a flat voice, then continued slowly.

“Not how your only child died. What I want to know is what kind of lunatics turned a lunatic like you into what you are.”

“……!”

“Tell me that.”

After a heavy silence in which every second felt like fifteen minutes, Baeksang’s lips finally parted.

“Gansu. Great Snow Mountain.”

Haa…

His breath trembled. White vapor spilled from his mouth in the ice-cold underground prison, like the heavy snow that must have fallen that day.

“At that time, we were leading the Southern Army alongside the Zhongnan Sect.”

At the single sentence that pierced my ears, I instinctively swallowed the words trying to burst from my mouth.

*Oh, fuck. The Zhongnan Sect.*
```
