<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0705.txt",
      "sha256": "7b6fa206ebc31657ca2eb45bfdbfb3ba03d352e1866e275eae7d6c6c50c520fe",
      "bytes": 14547
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b9687c398b362cb9da84d818af7cd692826c8d2387c22552c745c9fb154c68d1",
      "bytes": 2049
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "11a95624b72d4ce658b16e7eda8991ca1afdd254409655d5779ef9fbebb4655b",
      "bytes": 206510
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "b6253b7f72bbc9f896eb17f365fae1687dbc5764014d09e7bcffe891699c41db",
      "bytes": 919
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "0ced174bb4110b0a94d202383b6aa53fd6c350dd3fd8ec5506ed34acea258782",
      "bytes": 859
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "6089720454309cdd111396702df56f363f4ef3752f774dbcb0242247e855816e",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "f83f4993fbe3eed673eceb65234c46952372ca1d1aa2921b42a2682a0a7dd28e",
      "bytes": 1907
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "82ffb7387ca416c1c07d7d0419dec9839c39e8fd34f0f96ab060627d2529491d",
      "bytes": 622
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "1a9817db4310234d37be42195d76d05689afe6c8911958e7d9d2dec98cd7024d",
      "bytes": 853
    },
    {
      "path": "characters/Wang Ho.md",
      "sha256": "8e3f7aa2a5a93c11a65f1a56d5bc9763feb22b1865eb716f1b0b59a5f5e7e7e9",
      "bytes": 475
    },
    {
      "path": "characters/White Tiger.md",
      "sha256": "f70d4aab6f089fe13d33503ed5ee5f0b67297db6b461929ea85d5028a8cc703b",
      "bytes": 603
    },
    {
      "path": "characters/Yayul Cheok.md",
      "sha256": "fabd0fec0187e77b5b2c766fe419776fcb9ebfe6e63de6b574c52944b1665a6f",
      "bytes": 899
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "c1bc45bc5b6686ae9866a499f07be1c2fba17ad90d86c37d772579eec9f5f4d8",
      "bytes": 216607
    }
  ],
  "estimated_tokens": 13054
}
-->

# Durable State Update — Chapter 705

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 705. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 705. Profile updates may replace only one
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
  "chapter": 705,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 705,
    "continuity_sources": [705],
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
    "Yayul Cheok has arrived at the Inner Palace and joined Jin Taekyung and the guardian spirit against the Southern Heaven Demon Empress.",
    "Yayul Cheok recognizes the mutants as Nanman tribespeople he still loves and is consumed by grief and fury over their corruption and deaths.",
    "Jin Taekyung has expelled stagnant blood and recovered enough strength to fight alongside Yayul Cheok and the guardian spirit.",
    "The Southern Heaven Demon Empress has lost one arm and considerable strength and now faces the combined threat of Jin, Yayul, and the guardian spirit.",
    "The nearly one thousand mutants hesitate because their instincts sense the changed battlefield and the Empress's silence.",
    "The Empress's approximately five hundred elite subordinates have not appeared despite the rift being open for more than half a shichen.",
    "Someone foresaw the disaster and retained hope despite guilt and an irreversible path, but that person's identity is unstated.",
    "Wang Ho leads the white-armored Baekcheon Unit and has arrived as reinforcements for the Palace Lord."
  ],
  "continuity_sources": [
    704
  ],
  "open_questions": [
    "Why have the Southern Heaven Demon Empress's five hundred elite subordinates not arrived?",
    "Who is the person Yayul Cheok says foresaw the disaster and retained hope until the end?",
    "Can the Baekcheon Unit change the battle's outcome?",
    "Can Jin Taekyung, Yayul Cheok, and the guardian spirit defeat the Southern Heaven Demon Empress and stop the mutants?"
  ],
  "safe_through": 704,
  "temporary_decisions": [
    "Retain Fist Force, Force, Moving Formation, demonic martial arts, and Baekcheon Unit as established terminology.",
    "Render 궁주 as Palace Lord and 백천대주 as Commander of the Baekcheon Unit.",
    "Retain shichen for 시진 and the time it takes to drink a cup of tea for 일다경.",
    "Preserve Jin Taekyung's conversational profanity and the guardian spirit's terse, telepathic voice."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 초식     | **form**                                         | Numbered technique movement                           |
| 영약     | **elixir**                                       |                                                       |
| 살기     | **killing intent**                               |                                                       |
| 대주     | **Squad Leader** / **Commander**             |
| 정마대전   | **Great Faction War**         |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 왕호 | **Wang Ho** | Commander of the Baekcheon Unit who arrives leading white-armored reinforcements. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 야율척 | **Yayul Cheok** | Beast Miao King and lord of the Nanman Beast Palace. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 호위장 | **Captain of the Guards** | The Sichuan City Lord's guard captain. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 비도 | **throwing blade** | Mungyeong throws one past Taekyung's neck. |
| 변이체 | **mutant** | Taekyung's classification for the monster. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 사냥개 | **hunting dog** | Jin's demeaning metaphor for Ares personnel who obey Go Jun. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 백족 | **Bai people** | Ethnic group encountered in Yeongin. |
| 애뇌산 | **Ailao Mountain** | Mountain crossed by the party on the route to the Nanman Beast Palace. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 수왕석 | **Beast King Stone** | Legendary sacred treasure of the Nanman Beast Palace. |
| 대족장 | **Great Chieftain** | Title used for the senior Nanman leader who supposedly ordered the inspection. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 궁주 | **Palace Lord** | Title Yohi uses after realizing that Heugung is the Beast Miao King. |
| 백천대 | **Baekcheon Unit** | Baeksang's secret elite unit, cultivated over decades and held in reserve. |
| 수호령 | **guardian spirit** | Ancient title for the Black Tiger. |
| 신석 | **sacred stone** | Stone said to have existed alongside the Black Tiger's birth. |
| 동문 | **East Gate** | One of the Nanman Beast Palace's gates. |
| 신물 | **divine artifact** | General term for a sacred or divine object, distinct from 신석. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 야율척 | 진태경 | Nanman_Beast_Palace_Palace_Lord_to_Jeok_Cheongang's_Disciple | you / Disciple of Old Master Jeok / Jin Taekyung | rough, testing, and later welcoming | Yayul Cheok questions Taekyung as a suspected culprit, strikes him as a test, and then welcomes him after recognizing Jeok's Disciple. |
| 진태경 | 야율척 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Palace_Lord | Great Hero Yayul Cheok | formal and deferential | Taekyung gives Yayul Cheok a formal greeting as the nineteenth successor of the Fire Gate Clan. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 진태경 | 백호 | human ally to intelligent spiritual beast | you | casual and familiar | Converses with White Tiger after interpreting its warning. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 백상 | 야수묘왕 | Nanman great chieftain to the Nanman Beast Palace Lord | Palace Lord | restrained and apologetic | Apologizes for causing the disturbance after the Beast Miao King stops the fight. |
| 백상 | 남천마후 | Nanman Great Chieftain to hostile demon empress | Southern Heaven Demon Empress | formal and shocked | Baeksang directly identifies the woman who appears before him. |
| 남천마후 | 백상 | Dark Heaven controller to coerced Nanman leader | Great Chieftain Baeksang / Palace Lord | playful, taunting, and threatening | She repeatedly addresses Baeksang while mocking his grief, acknowledging his effort, and issuing her order. |
| 진태경 | 부족장 | captor to captured tribal chieftain | tribal chieftain | casual, coercive, and mocking | Jin promises to spare the captured chieftain if he answers questions properly. |
| 부족장 | 진태경 | captured tribal chieftain to overpowering enemy | Jin Taekyung | alarmed and desperate | The chieftain recognizes Jin by name while fleeing and then begs for his life. |
| 백상 | 호위장 | Palace Lord to Captain of the Guards | Captain of the Guards | formal and commanding | Baeksang issues orders concerning Ailao Mountain, the missing chieftains, and the pursuit of Yayul Cheok. |
| 호위장 | 백상 | Captain of the Guards to Palace Lord | my lord | formal and deferential | The Captain reports the wildfire and missing chieftains while questioning Baeksang's orders. |
| 백호 | 진태경 | guardian_spirit_to_human_ally | you | terse and irritated | The White Tiger responds telepathically after Jin calls it Whitey and jokes about its former name. |
| 진태경 | 수호령 | human ally to guardian spirit | guardian spirit | quiet and commanding | Jin whispers that they should go as they advance toward Baeksang. |
| 수호령 | 남천마후 | guardian_spirit_to_hostile_supernatural_opponent | you | terse, accusatory, and contemptuous | The guardian spirit tells the Southern Heaven Demon Empress that it knows her true essence and condemns her as a Fiend. |
| 남천마후 | 수호령 | hostile_supernatural_opponent_to_guardian_spirit | hideous beast | playful, taunting, and dismissive | She insults the guardian spirit while addressing it as a beast. |
| 백상 | 중년인 | Nanman Palace Lord to civilian tribesman | you | controlled and grave | Baeksang orders the middle-aged man to flee with his mother and the other civilians through the East Gate. |
| 중년인 | 백상 | Nanman civilian to betrayed Palace Lord | you | hostile, fearful, and grieving | The middle-aged man confronts Baeksang while protecting his mother and condemns him for the deaths and destruction. |
| 백상 | 부족장 | Palace Lord to subordinate tribal chieftain | you | cold, final, and detached | Baeksang refuses the chieftain's plea for mercy and tells him not to consider the exchange unjust. |
| 수호령 | 진태경 | guardian spirit to human ally | Human | terse and alarmed | The guardian spirit cries out to Jin as the Southern Heaven Demon Empress sends him crashing into the ground. |
| 왕호 | 야수묘왕 | Baekcheon Unit Commander to Nanman Beast Palace Palace Lord | Palace Lord | formal and deferential | Wang Ho bows and formally reports his arrival to the Beast Miao King. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 704
- **Aliases:** None
- **Role:** Baeksang is the Palace Lord of the Nanman Beast Palace and sole Great Chieftain of Nanman, and after betraying Nanman to pursue a decades-old promise, he witnesses a dark figure emerge from the mirror in his office.
- **Personality:** Cold, rigid, meticulous, and strategically resolute, yet burdened by regret, grief over Hwi's death, and a final conflicted impulse to spare others from the coming bloodshed.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of deceased Baekhwi, whom the Great Snow Fiend killed; he cultivated Yohi with gold and influence and used her support to advance Dark Heaven's preparations.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 704
- **Aliases:** Heugung
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, and the Great Chieftain of the Miao people who has returned to confront the Southern Heaven Demon Empress.
- **Personality:** The Beast Miao King is boisterous and warmhearted toward Nanman's people, but their corruption and destruction awaken fierce grief and wrath in him.
- **Voice:** Low, growling, and forceful.
- **Relationships:** Baeksang is his sworn younger brother and childhood companion, Yayul Mok is his Young Palace Lord, Jeok Cheongang is an old acquaintance, and Jin Taekyung is Jeok's Disciple whom he now fights beside against the Southern Heaven Demon Empress.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 704
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 704
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, and a publicly recognized S-rank-level Hunter who formally retains an A-rank license; he is recovering from severe injuries sustained when One Annihilation failed to kill the Southern Heaven Demon Empress.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 704
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 704
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress is Honglan, creator of the rift behind the Inner Palace; One Annihilation shattered her cultivated youth, leaving her aged, maimed, and scarred, but the rift's demonic qi is restoring her strength as she continues attacking Jin Taekyung.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

### Wang Ho.md

# Wang Ho (왕호)

- **Safe through:** Chapter 704
- **Aliases:** None
- **Role:** Wang Ho is the Commander of the Baekcheon Unit and leads its white-armored reinforcements to the Nanman Beast Palace.
- **Personality:** Not established.
- **Voice:** Formal and deferential when addressing the Palace Lord.
- **Relationships:** He commands the Baekcheon Unit and acknowledges Yayul Cheok as its Palace Lord.

### White Tiger.md

# White Tiger (백호)

- **Safe through:** Chapter 704
- **Aliases:** Whitey
- **Role:** The White Tiger is the guardian spirit of the sacred stone and leads the Sacred Land beasts, but both the stone's power and the White Tiger's strength are weakening under the rift's demonic qi.
- **Personality:** Irritable and contemptuous of Jin Taekyung's jokes.
- **Voice:** Telepathic, terse, and easily exasperated.
- **Relationships:** The White Tiger carries Jin Taekyung and Yohi, guards the sacred stone, and advances with Jin's forces.

### Yayul Cheok.md

# Yayul Cheok (야율척)

- **Safe through:** Chapter 704
- **Aliases:** Beast Miao King
- **Role:** Yayul Cheok is the over-eighty former Palace Lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, and Great Chieftain of the Miao people.
- **Personality:** Boisterous, warmhearted, forthright, playful, and politically conscious of the tribal coalition he leads.
- **Voice:** Rough, loud, convivial, and teasing, becoming authoritative when discussing Nanman's laws or political decisions.
- **Relationships:** Jeok Cheongang is an old acquaintance whom he respects; Baeksang is his sworn younger brother and childhood companion, and they fought together during the Great Faction War; Yayul Mok serves as his Young Palace Lord; Jin Taekyung is Jeok's Disciple whom he welcomes into the Nanman Beast Palace.

## Korean source

```text
＃705화



“백천대주 왕호, 궁주를 뵙습니다.”

그 첫마디를 듣는 순간, 남천마후는 세상이 멈췄다고 생각했다.

동시에 느려진 시간 속에서 주위를 둘러싼 모든 것들이 파도처럼 몰려와 그녀의 눈 앞을 가렸다.

암천의 상징이나 다름없는 칠흑색 무복이 아닌, 눈처럼 새하얀 의복과 갑주.

거기에 더해 백족임이 분명한 복색과 이목구비를 지닌 삼백 명의 전사들과 낮은 울음소리를 흘리는 맹수들.

그리고…….

펄럭.

어디선가 불어온 바람에 흩날리는 하나의 깃발과 누군가 용사비등(龍蛇飛騰)한 필체로 휘갈긴 세 글자.

백천대(白天隊).

“……!”

남천마후의 눈동자가 파르르 떨렸다.

알 수 없었다.

끝없이 펼쳐진 어두운 하늘 아래로 보이는 저 글씨가, 적지 않은 세월 속에 누렇게 변색 되어 버린 채 흩날리는 있는 저 낡은 비단 따위가 무엇이길래 이토록 마음을 불안하게 하는지.

그리고 대수롭지 않게 넘겼던 지난날의 기억이, 왜 지금 이 순간 다시 떠오르는지.



‘마후시여. 백상이 은밀히 전사와 맹수들을 육성하고 있습니다. 오직 백족으로만 이루어진 자들인데, 면밀하게 조사해 본 결과 그들 중 대부분이…….’

‘정마대전이나, 역병으로 부모를 잃은 고아들이지. 몇 년 전 일어난 대화재 이후 종적이 묘연해졌고.’

‘호, 혹시 알고 계셨습니까?’

‘그래, 오래전부터. 문산(文山)이라는 곳에 은거지를 마련했지, 아마?’

‘하, 하면 이 미천한 종이 마후께 감히 한 가지만 여쭈어도 되겠습니까?’

‘너, 궁금하구나? 왜 모든 걸 알면서도 지켜만 보는지.’

‘외람되지만 그렇습니다. 현재에도 백상에게 흘러 들어간 막대한 물자 중 상당수가 전사들의 육성에 쓰이고 있는 상황입니다. 만약 언젠가 놈이 다른 마음을 품는다면…….’

‘뭐 어때, 재미있잖아.’

‘예?’

‘생각해 보렴. 기껏해야 갈 곳 없는 고아들에게 영약을 먹이고, 무공 몇 초식 가르친다고 해서 뭐가 달라질까?’

‘그, 그건.’

‘잡철은 아무리 두드려 봤자 잡철이란다. 그 정도로는 절대 신병이기를 만들 수 없어. 그런데…… 난 그게 제법 즐겁더라고. 헛된 꿈에 부풀어서 잡철을 붙잡고 아등바등 애쓰는 백상의 모습을 지켜보는 것이. 그 희망이 절망으로 바뀌었을 때 그가 어떤 표정을 지을지 상상하는 것도.’

‘……!’

‘그리고 백상은 결코 다른 마음을 품지 못해. 만에 하나 그런 일이 생긴다 해도, 내게는 그저 또 다른 즐거움이 되겠지.’



어언 십수여 년 전의 일이다.

그날 젊은 나이에 대족장의 자리에 오른 어느 간자(間者)는 이마에 피가 나도록 머리를 찧은 뒤 돌아갔고, 남천마후는 자연스럽게 그에 관한 기억을 잊었다.

아니, 아예 뇌리에서 지웠다.

더불어 사람의 발길이 닿지 않은 심산유곡에서 벌어지는 일 역시 남천마후의 관심에서 서서히 멀어졌다.

‘계속해서 지켜보기에는, 그러기에는 너무나도 하찮은 일이었으니까.’

당연한 일이었다. 그녀는 백상의 목줄을 쥐고 있었고, 만약 그가 스스로 목줄을 끊고 자신에게 달려든다 해도 단숨에 짓눌러 죽일 만한 힘이 있었다.

오직 강자만이 보일 수 있는, 압도적인 힘에서 비롯된 광오(狂傲)와 여유.

하지만 지금에서야 남천마후는 깨달았다.

결코 배신하지 못하리라 생각했던 백상이라는 사냥개가, 어느 날 스스로 목줄을 끊었다는 것을.

자신의 광오함이 오늘 이 자리에 저들을 불러 왔다는 것을.

“……백천. 백천대.”

남천마후는 신음처럼 뇌까렸다.

그녀가 곧 도래할 어두운 하늘을 꿈꿀 때, 또 다른 누군가는 새하얀 구름이 떠다니는 하늘을 바라보고 있었다.

아니, 마음속에 간직하고 있었다.

원한 적 없던 목줄을 찬 사냥개가 되어 누군가의 뒤를 따르면서도. 그 길이 잘못되었다는 것을 알면서도 이렇게 할 수밖에 없는 자책과 분노를 담아 글자를 써 내려갔을 것이다.

한때는 눈부시도록 희었을 저 누렇게 낡은 비단에, 자신이 보고 싶었던 하늘을 그려 넣었을 것이다.

그리고 그의 손으로 이루지 못할 염원은, 한 사람에게 전해졌다.

“떠나시오. 이미 동문을 비워 두었소. 뇌옥의 경비도 평소보다 허술할 테니 한족들 역시 어렵지 않게 이곳을 빠져나갈 수 있을 거요.”

“……!”

공간을 울리는 나직한 목소리에, 크게 뜬 눈으로 백천대와 야수묘왕을 번갈아 바라보던 진태경이 침음성을 흘렸다.

“설마.”

흩어졌던 조각들이 천천히 끼워 맞춰지는 듯한 기분.

야수묘왕이 붉게 충혈된 눈으로 남천마후를 응시하며, 며칠 전 누군가의 입을 통해 들었던 말을 이어 나갔다.

“곧장 북동쪽에 위치한 문산(文山)으로 가시오. 그리고 그중 가장 높은 봉우리에 머무르는 이들에게 이것을 보여 주시오.”

휙, 툭.

야수묘왕의 손을 빠져나온 무언가가 곡선을 그리며 남천마후의 발치에 떨어진다.

옥으로 만들어진 그것은 반으로 갈라진 누군가의 신패(信牌)였고, 백천대를 움직일 수 있는 하나뿐인 증표였다.

“나는 이미 돌이킬 수 없는 길을 걸었소. 스스로의 의지로 멈출 수도 없고, 만약 멈춘다 해도 대계(大系)를 막기에는 역부족이겠지.”

야수묘왕의 목소리가 파르르 떨렸다.

흐릿한 불빛이 감돌던 침소 내부, 검수(劍手)의 생명과도 같은 손목을 스스로 끊어 버린 의형제의 얼굴이 눈앞을 스치는 듯했다.

그가, 백상이 마지막으로 건넸던 한 마디와 함께.

“나는 결코 멈추지 않겠소. 그러니…… 궁주도 멈춰서는 안 되오. 진태경, 그 아이와 함께 끝까지 나아가시오. 나와는 다른 길로.”

그것이 전부였다. 의형(義兄)은 떠났고, 의제(義弟)는 남았다.

그리고 사흘 뒤, 백천대는 야수묘왕의 손에 들린 신패 앞에 무릎을 꿇었다.

집과 가족을 잃은 자신들에게 아버지이자 스승이 되어준 한 사람의 당부를 떠올리며.



‘만약 언젠가, 내가 아닌 다른 누군가가 이 신패를 가져온다면…… 그가 바로 너희가 모셔야 할 주군이다.’



그렇게 수십 년간 심산유곡에 잠들어 있던 삼백 명의 전사들은 야수묘왕을 따라 하산(下山)했고, 거침없이 광야를 질주하는 어느 전사들에 관한 소문은 조용히. 동시에 빠르게 퍼져나갔다.



‘궁주께서 돌아오셨다!’

‘우리 태족(傣族)은 궁주께 합류한다! 암천과 결탁하여 궁주의 자리를 찬탈하고, 남만을 배신한 역도들로부터 이 땅을 지켜라!’

‘당장 모든 전사를 동원해라. 어서 전령을 띄워!’



자그마치 일만에 달하는 전사가 남만야수궁으로 향했으니, 그만큼의 공백이 생겨난 상황.

백상에게 반기를 들고 남만야수궁을 빠져나온 부족장들은, 휘하의 전사들을 이끌고 자신들의 진정한 궁주에게 합류했다.



‘자네들…….’

‘목숨 바쳐 따르겠습니다, 궁주.’



하루. 그리고 또 하루.

어느덧 거대한 군세(軍勢)로 거듭난 그들은 남만야수궁을 향해 달려나갔고, 예상치 못한 적과 마주쳤다.

아니, 적이라고 생각했다.

어림잡아 삼천에 달하는 대병력. 그들의 선두에 선 백족 사내가 홀로 앞으로 나서서 무릎을 꿇기 전까지는.



‘투항하겠습니다.’



야수묘왕은 이유를 물었고, 백족 사내는 혼이 나간 듯한 표정으로 답했다.



‘신물(神物)을 지키는 존재께서 저를 비롯한 모두를 일깨워 주셨습니다. 무엇이 옳은 길이며 어떤 선택을 해야 하는지.’



수왕석은 전설이자, 기적이다.

그리고 그날, 애뇌산에서 그 경이로운 광경을 목격한 것은 백족 사내. 아니, 호위장만이 아니었다.



‘그 한족 놈. 아니, 진태경 대협께서 말씀하셨습니다. 속히 궁주님을 찾으라고. 더 늦으면 모든 것이 끝장이라고.’



그렇게 애뇌산을 포위했었던 삼천의 전사들마저 합류하자, 그들을 막을 수 있는 것은 아무것도 없었다.

험준한 산도, 깊은 늪과 풀숲이 우거진 밀림도.

그리고 그것은, 일이 틀어졌음을 깨닫고 황급히 남만야수궁으로 향하던 일단의 무리 역시 마찬가지였다.

“급하게 내궁으로 향하느라 끝을 보지 못했다. 전투는 어찌 되었느냐?”

남천마후에게 시선을 고정시킨 야수묘왕이 불현듯 던진 물음에, 백천대주 왕호가 뺨에 묻은 핏물을 닦으며 대답했다.

그의 눈동자는 아직 가시지 않은 전투의 열기로 달아올라 있었다.

“아군의 사상자는 이백입니다.”

“놈들은?”

“전멸입니다. 단 한 놈도 빠짐없이 죽이거나 사로잡았습니다.”

이 모든 상황을 지켜보던 진태경이 피식 웃었다. 자세한 내막은 몰라도, 일이 어떻게 흘러가는지는 충분히 짐작하고도 남는다.

“할망구. 좆 됐네?”

“……!”

으득.

순간 자신도 모르게 이를 악문 남천마후의 입안에서 비릿한 혈향이 맴돌았다.

죽었다. 모조리.

자그마치 오백에 달하는 정예가 몰살당했다.

야수묘왕과 함께 들이닥친 수천의 군세가, 이 불안한 상황을 단번에 타개할 수 있었던 마지막 한 수를 짓밟아 버린 것이다.

‘이런. 이런 말도 안 되는……!’

참을 수 없는 분노가 끓어오른다. 동시에 그보다 더한 불안감과 서늘한 한기가 가슴을 맴돌았다.

지금 남천마후의 뇌리를 가득 채운 것은 죽음이라는 두 글자였다.

‘……죽어? 죽는다고? 내가?’

믿을 수 없었다.

무려 일백하고도 삼십 년이 넘는 세월을 살아온 그녀다.

젊을 적부터 아름다워지기 위해, 젊음을 유지하기 위해 수단과 방법을 가리지 않았고 수도 없이 인륜(人倫)을 저버리는 과정에서 고강한 무위를 쌓았다.

만약 언젠가 최후를 맞이한다 해도, 그것이 다른 누군가의 손에 죽는 것이라고는 상상해 본 적이 없었다.

하지만 해 본 적도 없던 그 허무맹랑한 상상이, 지금 이 순간 현실이 되어 눈앞으로 성큼 다가오고 있었다.

마치 날카로운 송곳처럼 첨예한 살기와 함께.

구궁.

동시에 내디딘 수백의 걸음이 거대한 울림이 되어 퍼져 나가고.

크르릉.

전사들을 등에 태운 맹수들이 낮은 울음소리를 토해 낸다.

그중에서도 가장 거대한 백호를 중심으로 흘러나온 빛이, 그들 모두를 감싸 안고 어둠으로부터 보호했다.

화아아악.

흐릿하지만 분명한 빛. 아득한 세월 동안 이 땅과 운명을 함께한 신석(神石)의 힘을 느낀 변이체들이 본능적으로 뒷걸음질 친다.

아니, 어쩌면 그들 역시 느꼈을지도 몰랐다.

저들과의 전투에서 승리할 수 없다는 것을. 더욱 흉포하고 강력해진 이 몸뚱어리로도, 설령 자신들을 이끄는 남천마후가 나선다 해도 결과는 달라지지 않으리라는 것을.

- 크륵.

- 큭.

흡사 신음처럼 울려 퍼지는 괴성. 그리고 괴성만큼이나 흉측한 외형을 지닌 괴물들이 무려 일천에 달한다.

그러나 백천대는 한 치의 흔들림도 없이 변이체들을 향해, 앞서 상대한 적의 피로 흥건한 병장기를 겨누었다.

스릉.

흐릿한 빛을 받아 번쩍이는 수백의 창검.

지금으로부터 수십여 년 전, 그들을 잡철(雜鐵)이라 칭하며 한낱 유흥거리로 여기던 누군가의 생각은 틀렸다.

아니, 적어도 그때만큼은 사실이었을지도 모른다.

하지만 끊임없이 두드리고, 식히고, 달구어진 잡철은 어느 순간부터 새롭게 거듭났다.

단단하고 강철로, 강철마저 끊어 낼 수 있는 예리한 명검으로.

그리고 백천대라는 이름의 명검을 휘두를 수 있는 자는, 천하를 통틀어 오직 한 사람뿐이다.

“명을 내려 주십시오, 궁주. 아니…….”

흐르는 세월 속에 반백의 머리가 되어 버린 중년인. 백천대주 왕호가 묵직한 음성을 토해 냈다.

“주군.”

동시에 그의 시선이, 백천대 전원의 시선이 한 방향으로 흐른다.

그리고 모두의 앞에 철탑처럼 우뚝 서 있던 거한. 야수묘왕(野獸苗王) 야율척의 입술이 열렸다.

“나아갈 테니, 따르라.”

“존명(尊命).”

그것이 전부였다.

다음 순간, 그들은 동시에 나아갔다. 대해(大海)에서 시작된 파도처럼. 활시위를 떠난 화살처럼. 한 줄기의 벼락처럼.

그리고 그 선두에, 야수묘왕과 함께 나란히 쏘아지는 거대한 백호의 신형이 있었다.

- 크아아아앙!

콰드드드득!

천지를 떨어 울리는 포효와 함께 휘둘려진 앞발이, 막아서는 모든 것을 찢고 부순다.

자신의 혈색만큼이나 새하얀 수호령의 갈기를 힘껏 움켜잡으며, 진태경이 작게 중얼거렸다.

“아니 시팔. 힘들어 죽겠는데 나는 왜…….”

하지만 갑작스러운 급발진 현상에 떨떠름한 기분도, 수호령이 혹시 국산 호랑이인가 하는 의심도 다음 순간 사라졌다.

정확히 말하자면, 사라질 수밖에 없었다.

고오오오옹.

삽시간에 얼어붙는 공기. 주위의 어둠을 끌어당기며 솟아오르는 용권풍(龍卷風)의 중심에서 고개를 드는 남천마후의 모습에, 진태경은 섬전 같은 속도로 수호령의 갈기를 뒤로 잡아당겼다.

회심의 후진 기어.

그리고 수호령은 진태경의 뜻을 정확히 알아듣고 몸을 날렸다.

앞으로.

쉬쉬쉭!

- 꽉 붙잡아라. 인간!

“…….”

아니, 씹.
```

## Final English reading copy

```markdown
# Chapter 705

“Commander of the Baekcheon Unit Wang Ho, paying his respects to the Palace Lord.”

The moment she heard those first words, the Southern Heaven Demon Empress thought the world had stopped.

At the same time, within the slowed passage of time, everything surrounding her surged toward her like waves and obscured her vision.

Not the pitch-black martial uniforms that were practically the symbol of Dark Heaven, but clothing and armor as white as snow.

Three hundred warriors whose clothing and features clearly marked them as Bai people, along with beasts that let out low growls.

And then…

Flap.

A single flag fluttered in a breeze that had blown in from somewhere, bearing three characters scrawled in a vigorous, soaring hand.

Baekcheon Unit.

“……!”

The Southern Heaven Demon Empress’s pupils trembled.

She did not understand.

Why did those characters beneath the endless dark sky, or that old silk fluttering in the wind after having yellowed with the passage of considerable time, unsettle her so deeply?

And why were memories she had once dismissed as insignificant surfacing again at this very moment?

*Demon Empress. Baeksang is secretly training warriors and beasts. They are made up exclusively of Bai people, but after investigating them thoroughly, most of them…*

*Orphans who lost their parents in the Great Faction War or to the plague. Their whereabouts became unknown after the great fire several years ago.*

*Y-you knew?*

*Yes. For a long time. He probably established a hideout in a place called Wenshan, didn’t he?*

*Th-then, may this lowly servant dare ask the Demon Empress just one thing?*

*You’re curious, aren’t you? Why I only watch even though I know everything.*

*Forgive my impertinence, but yes. Even now, a considerable portion of the vast supplies flowing to Baeksang is being used to train warriors. If he should ever harbor different intentions…*

*So what? It’s amusing.*

*Pardon?*

*Think about it. What could possibly change just because he feeds elixirs to orphans who have nowhere to go and teaches them a few forms of martial arts?*

*Th-that…*

*No matter how many times you hammer scrap iron, it remains scrap iron. You can never create a divine weapon from that. But… I find it rather entertaining. Watching Baeksang struggle desperately to hold on to scrap iron while inflated with a vain dream. Imagining the expression he’ll make when that hope turns into despair is amusing, too.*

*……!*

*And Baeksang could never harbor different intentions. Even if something like that happened, it would merely become another source of amusement for me.*

That had happened more than a dozen years ago.

That spy who had risen to the position of Great Chieftain at a young age had beaten his head against the floor until blood ran from his forehead before leaving, and the Southern Heaven Demon Empress had naturally forgotten about him.

No—she had erased him from her mind entirely.

The events taking place in a remote mountain valley untouched by human footsteps had gradually faded from the Southern Heaven Demon Empress’s attention as well.

*It was far too insignificant to keep watching.*

It was only natural. She held Baeksang’s leash, and even if he cut it himself and charged at her, she possessed more than enough power to crush him to death in an instant.

The arrogance and leisure born from overwhelming strength—things only the powerful could display.

But only now did the Southern Heaven Demon Empress realize.

The hunting dog named Baeksang, whom she had believed could never betray her, had cut his own leash one day.

Her own arrogance had brought them all here today.

“……Baekcheon. The Baekcheon Unit.”

The Southern Heaven Demon Empress muttered the words like a groan.

While she dreamed of the dark sky that would soon arrive, someone else had been looking up at a sky with white clouds drifting across it.

No. He had kept it in his heart.

Even while following someone as a hunting dog wearing a leash he had never wanted, even while knowing that path was wrong, he must have written those characters while filled with guilt and anger at having no choice but to continue.

On that yellowed, worn silk that had once been dazzlingly white, he must have drawn the sky he had wanted to see.

And the wish he could not fulfill with his own hands had been passed on to one person.

“Leave. I have already cleared the East Gate. The guards at the underground prison will be more lax than usual, so the Han Chinese should be able to escape this place without much difficulty.”

“……!”

At the low voice that echoed through the space, Jin Taekyung let out a groan as he stared wide-eyed, alternating his gaze between the Baekcheon Unit and the Beast Miao King.

“No way.”

It felt as though the scattered pieces were slowly fitting together.

The Beast Miao King stared at the Southern Heaven Demon Empress with bloodshot eyes and continued the words he had heard from someone’s mouth several days earlier.

“Go straight to Wenshan, which lies to the northeast. Then show this to those staying on its highest peak.”

Whoosh. Clatter.

Something slipped from the Beast Miao King’s hand, traced an arc through the air, and landed at the Southern Heaven Demon Empress’s feet.

Made of jade, it was one half of someone’s split identification token—and the sole token of authority capable of mobilizing the Baekcheon Unit.

“I have already walked an irreversible path. I cannot stop of my own will, and even if I did stop, it would not be enough to prevent the grand scheme.”

The Beast Miao King’s voice trembled.

Inside the sleeping quarters, where dim light lingered, the face of his sworn brother seemed to flash before his eyes—the man who had severed with his own hand the wrist a swordsman valued as much as life itself.

Along with the last words Baeksang had spoken to him.

“I will never stop. So… Palace Lord, you must not stop either. Continue to the end with that boy, Jin Taekyung. Take a different path from mine.”

That was all.

The sworn elder brother had left, and the sworn younger brother had remained.

And three days later, the Baekcheon Unit had knelt before the token in the Beast Miao King’s hand.

They remembered the request of the one man who had become a father and teacher to them after they lost their homes and families.

*If someday someone other than me brings this token, he is the lord you must serve.*

Thus, the three hundred warriors who had slept in a remote mountain valley for decades descended from the mountains behind the Beast Miao King.

Rumors of warriors racing fearlessly across the wilderness spread quietly—and swiftly.

*The Palace Lord has returned!*

*Our Dai people will join the Palace Lord! Protect this land from the traitors who colluded with Dark Heaven, usurped the Palace Lord’s position, and betrayed Nanman!*

*Mobilize every warrior at once. Send out the messengers!*

As many as ten thousand warriors headed for the Nanman Beast Palace, leaving behind a vacuum of equal size.

The tribal chieftains who had rebelled against Baeksang and left the Nanman Beast Palace led their warriors to join their true Palace Lord.

*You all…*

*We will follow you with our lives, Palace Lord.*

One day. Then another.

Before long, they had become a massive army and were racing toward the Nanman Beast Palace when they encountered an unexpected enemy.

No—they thought it was an enemy.

A large force numbering roughly three thousand.

That was how they saw it until a Bai man at the head of the army stepped forward alone and knelt.

*We surrender.*

The Beast Miao King asked him why, and the Bai man answered with a vacant expression.

*The being who protects the divine artifact awakened everyone, including me. It showed us which path was right and what choice we needed to make.*

The Beast King Stone was a legend and a miracle.

And that day, the Bai man—no, the Captain of the Guards—was not the only one who witnessed the wondrous sight on Ailao Mountain.

*That Han Chinese bastard. No, Great Hero Jin Taekyung told us to find the Palace Lord as quickly as possible. He said that if we delayed any longer, everything would be over.*

Once the three thousand warriors who had surrounded Ailao Mountain joined them, there was nothing capable of stopping them.

Not the rugged mountains, nor the deep swamps and dense jungles.

The same was true of the group that realized something had gone wrong and hurried toward the Nanman Beast Palace.

“I had to rush to the Inner Palace and didn’t see it through to the end. How did the battle turn out?”

At the Beast Miao King’s sudden question, his gaze fixed on the Southern Heaven Demon Empress, Commander of the Baekcheon Unit Wang Ho wiped the blood from his cheek and answered.

The heat of the battle that had yet to fade still burned in his eyes.

“We suffered two hundred casualties.”

“And them?”

“Annihilated. We killed or captured every last one of them.”

Watching the entire situation unfold, Jin Taekyung let out a quiet laugh. He did not know the details, but he could more than guess how things were going.

“Old hag. You’re fucked, huh?”

“……!”

The Southern Heaven Demon Empress clenched her teeth before she could stop herself.

A bitter scent of blood filled her mouth.

Dead. Every last one of them.

No fewer than five hundred elites had been slaughtered.

The thousands of warriors who had stormed in with the Beast Miao King had trampled the final move that could have overturned this precarious situation in an instant.

*No. No, this is impossible…!*

Unbearable fury boiled within her. At the same time, an even greater sense of unease and a cold chill lingered in her chest.

The two characters filling the Southern Heaven Demon Empress’s mind now were death.

*…Die? I’m going to die? Me?*

She could not believe it.

She had lived for more than one hundred and thirty years.

Since her youth, she had used every means available to become beautiful and preserve her youth, building formidable martial prowess in the process of repeatedly abandoning all human morality.

Even if she were to meet her end someday, she had never imagined dying at someone else’s hands.

But that absurd fantasy—something she had never once considered—was now becoming reality and striding toward her eyes.

Along with killing intent as sharp as a pointed awl.

Thump.

Hundreds of feet stepped forward at once, their combined impact spreading as a tremendous echo.

Grrrr.

The beasts carrying the warriors on their backs let out low growls.

Light flowed outward from the largest White Tiger among them, wrapping around them all and protecting them from the darkness.

Fwoooosh.

It was faint, but unmistakable.

The mutants felt the power of the sacred stone that had shared its fate with this land throughout the distant ages, and instinctively stepped backward.

No—perhaps they had felt it, too.

That they could not win a battle against these people.

That even with bodies made more vicious and powerful, the outcome would not change—not even if the Southern Heaven Demon Empress leading them joined the fight.

—Krrk.

—Kk.

The bizarre cries echoed like groans.

There were nearly a thousand monsters, each with an appearance as hideous as the sounds they made.

Yet the Baekcheon Unit did not waver even a fraction as they aimed their weapons, drenched in the blood of the enemies they had faced before, at the mutants.

Shing.

Hundreds of spears and blades flashed in the hazy light.

Several decades ago, someone had been wrong to call them scrap iron and regard them as nothing more than a form of entertainment.

No.

Perhaps it had been true—at least back then.

But the scrap iron that was endlessly hammered, cooled, and heated was transformed anew at some point.

Into hard steel.

Then into sharp, famed swords capable of cutting even steel.

And there was only one person in all the world capable of wielding the famed sword known as the Baekcheon Unit.

“Give us your command, Palace Lord. No…”

A middle-aged man whose black hair had turned half gray with the passage of time—the Commander of the Baekcheon Unit, Wang Ho—spoke in a weighty voice.

“My lord.”

At the same time, his gaze—and the gaze of every member of the Baekcheon Unit—shifted in one direction.

Then the lips of the giant who had stood tall before them all like an iron tower opened.

The Beast Miao King, Yayul Cheok.

“I will advance. Follow me.”

“As you command.”

That was all.

The next moment, they advanced together.

Like a wave beginning in the middle of the ocean.

Like an arrow leaving its bowstring.

Like a single bolt of lightning.

And at the front, alongside the Beast Miao King, was the enormous body of a White Tiger shooting forward.

—Kraaaaaaang!

Krrrunch!

With a roar that shook heaven and earth, its forepaw swung down and tore apart and crushed everything in its path.

Gripping the guardian spirit’s mane, white enough to match his own pallor, Jin Taekyung muttered,

“No, fuck. I’m exhausted enough to die, so why the hell am I—”

But his dismayed mood at the sudden acceleration, along with his suspicion that the guardian spirit might be some kind of Korean-made tiger, vanished the very next moment.

To be precise, they had no choice but to vanish.

Gooooong.

The air froze in an instant.

At the center of a dragon-tornado rising as it pulled in the surrounding darkness, the Southern Heaven Demon Empress lifted her head.

Jin Taekyung yanked the guardian spirit’s mane backward at lightning speed.

His ace in the hole: reverse gear.

The guardian spirit understood his intention perfectly and hurled its body away.

Forward.

Whoosh!

—Hold on tight, human!

“……”

No, fuck.
```
