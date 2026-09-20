<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0540.txt",
      "sha256": "55209708fe9526fb11de57cd8a13d209c729fe2f6d1c70bb05e674bc5d79c089",
      "bytes": 13415
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "22516abafdc3814000bff631865d34ee994077215d49e3c7206b6ae33656bf43",
      "bytes": 3946
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "e9397927b5f6de538ecaf0b2ec39b18a1b2cb12efc493fae66e0b67de360bcf5",
      "bytes": 170804
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "5da6c1109da8f4d79de77a963a8e0898e5e18cd1eb105f7c0571a478a93caf73",
      "bytes": 803
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "0035ca0845c74e7c6cbf479e7b6643e043527c5cbfd90a3915ec27eea7172534",
      "bytes": 1370
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "afea08117b8d4fe14376a0c14f1f38f6c7a38a326a2c801b0a3ad28f7f920325",
      "bytes": 667
    },
    {
      "path": "characters/Hwangbo Ak.md",
      "sha256": "0f3aaece248e0ac2d606aedec3eff64726b48a23492c2e6e6424924a565bb074",
      "bytes": 846
    },
    {
      "path": "characters/Hwangbo Gun.md",
      "sha256": "64c453fb918f6b6294a0b4822b429f294230cc44e9eade11dc9cb21d0ad6127f",
      "bytes": 716
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "9dd6e012694fa2fd9c9f41f16ce48050f770c4f00c06acd68d1f5178e9e095ab",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "ab619ed0f1623d3741f8538c3b907ada0d31c9d159ec64b22ccdfec0c988d135",
      "bytes": 1630
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "69ba8bafef9747fde23edca5b2f52e0fbf91b3a7546b3ab34c89683a3771196c",
      "bytes": 2192
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "9f343c032e6b3a6eddf74f2f4fb3bd86571b930283d98a12ad7f206e690eaaea",
      "bytes": 622
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "6de0d00f5aabd840f47134cebfc21c75098cb1770e67ca18848f8073ffebbb9b",
      "bytes": 985
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "9830c88fa1989922f57ca5ec772a7492ea7b78084b60c1e564bd12a928655944",
      "bytes": 474
    },
    {
      "path": "characters/Unnamed.md",
      "sha256": "b2ce8977139e63b092b90e2fe909b2da23cfb2974b06dc41ab21b4ccbee7a565",
      "bytes": 750
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "15ac6e329987b2937a5cb607890264259883ca4f1986cc4eaea7b7489ec62855",
      "bytes": 162019
    }
  ],
  "estimated_tokens": 14650
}
-->

# Durable State Update — Chapter 540

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 540. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 540. Profile updates may replace only one
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
  "chapter": 540,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 540,
    "continuity_sources": [540],
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
    "The Mount Song Resolution formally restored the Murim Alliance; Mae Jonghak is its Alliance Leader, and Song Ho commands the Hidden Shadow Pavilion under his authority.",
    "Mae Jonghak formally appointed Jin Taekyung and Cheongpung as the two pavilion masters of the Alliance Leader's direct Two Dragons Pavilion; each pavilion has a regiment and subordinate squads beneath it.",
    "Tang Sadok and the Sichuan Tang Clan publicly support Jin Taekyung and Cheongpung and acknowledge an unrepayable debt to them.",
    "Taekyung believes the Zhongnan Sect resents him, the Jin Family of Taiyuan, and Jeok Cheongang after its repeated humiliations and will obstruct them.",
    "Cheongpung created Mimi Step from Mimi's movements; it is a snake-like footwork technique fast enough that Taekyung could barely track it with his naked eyes, and Mungyeong recognizes Cheongpung as having the makings of a Grandmaster.",
    "Mimi is now a large horned snake under Cheongpung's care, eats dumplings, sweets, and Blood Fish, and has recently had her condition examined by Mungyeong.",
    "Mungyeong ended Taekyung's direct training and assigned him a final task of incorporating martial principles into his learned martial arts.",
    "Zhuge Feng's Demon-Sealing Formation still blocks all mana from the exposed Gate, while Jang Taebo is summoning artisans to process the Water God Dragon's remains.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "The Black Dragon Demon Gate remains a major unorthodox power descended from the Demonic Cult's Twelve Branches; Sama Pyo is its Young Sect Leader and Black Dragon Saber, and Taishan is his giant subordinate.",
    "Jin Taekyung remains a Supreme Peak master with Three Flowers Gather at the Crown, advanced qi perception, exceptional resistance to monster Fear, and public S-rank-level recognition despite retaining an A-rank license.",
    "The System has assigned Taekyung's first Two Dragons Pavilion Quest: recruit at least five companions and name the organization, or receive the Title Loner. Mungyeong has accepted Cheongpung's offer, and Taekyung is now seeking other recruits through public notices."
  ],
  "continuity_sources": [
    539,
    538
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, the Azure Sky Sword King?",
    "Why did Ju Hwaran and Sama Pyo's political engagement end?",
    "Which additional companions will join the Two Dragons Pavilion, what name will it receive, and can Taekyung complete the System Quest?"
  ],
  "safe_through": 539,
  "temporary_decisions": [
    "Render 고월루 as Gowolru, 곤륜운룡 as Kunlun Cloud Dragon, 학우 as Hak Woo, 이룡각 as Two Dragons Pavilion, 협 as chivalry, 인의 as humanity, and 협객 as knight-errant; render 전 정혼자 contextually as former fiancé or former fiancée.",
    "Render 탈진 as the capitalized system status Exhaustion; retain Ten Dragons and Phoenixes, Blazing Flame Divine Dragon, Dark Heaven, Murim Alliance, and Old Master.",
    "Render 황보세가 as Hwangbo Family, 소가주 as Lesser Family Head, 은비화 as Dagger Hidden Flower, and 전음 as Sound Transmission.",
    "Preserve the chapter's blunt profanity, financial-therapy humor, monster-comparison humor, and Mae Jonghak's carefree 'That can happen' refrain; render 고잉무림호 as Going Murim ship, 대종사 as Grandmaster, and 왕희지 as Wang Xizhi.",
    "Render 일기천룡 as One-Ride Heavenly Dragon and Taishan's speech as clipped, childlike, and literal."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 십봉룡    | **Ten Dragons and Phoenixes**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 주화입마   | **qi deviation**                                 |                                                       |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 낭인     | **wandering martial artist**                     |                                                       |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 정파     | **orthodox faction**                             |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 장문인    | **Sect Leader**                              |
| 대주     | **Squad Leader** / **Commander**             |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 하남     | **Henan**              |
| 화산     | **Huashan**            |
| 노부      | **this old man / I**                                            |
| 본문      | **our sect / this sect**                                        |
| 귀가      | **your family**                                                 |
| 형장      | **Brother** / **Brother [Name]**                                |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 황보악 | **Hwangbo Ak** | Lesser Family Head of the Hwangbo Family and member of the Ten Dragons and Phoenixes. |
| 황보군 | **Hwangbo Gun** | Family Head of the Hwangbo Family and father of its Lesser Family Head. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 무명 | **Unnamed** | Dharma name given by Hong Dao; literally means having no name. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 국밥 | **gukbap** | Korean dish of rice served in hot soup; footnoted in the reading copy. |
| 그리스 | **Grease** | Spell used to make the ogres lose their footing. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 중독 | **Poisoned** | System status abnormality caused by the poisons. |
| 하남성 | **Henan Province** | Province containing Luoyang. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 화산신룡 | **Huashan Divine Dragon** | Title given to Cheongpung after the Star-Array Grand Banquet. |
| 사백 | **Senior Martial Uncle** | Zhongnan Sect title used for a senior of the speaker’s Master’s generation. |
| 황보 | **Hwangbo** | Surname form used when addressing Hwangbo Eom. |
| 외당 | **Outer Hall** | The Tang Clan's outer hall area. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 이룡 | **Two Dragons** | Collective ranking beneath the Ten Kings in Murim gossip. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 한나절 | **half a day** | Elapsed duration in Jeok's first time-loss episode. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 검기상인 | **the level of injuring others with Sword Energy** | Realm description used for Moon Beauty Saber. |
| 맹주부 | **Alliance Leader's Office** | Office directly serving the Alliance Leader. |
| 황보세가 | **Hwangbo Family** | Hwangbo Ak's established martial family and the long-standing hegemon of Shandong. |
| 산동권룡 | **Shandong Fist Dragon** | Hwangbo Ak's sobriquet among the Ten Dragons and Phoenixes. |
| 이룡각 | **Two Dragons Pavilion** | Named pavilion whose masters are identified as Taekyung and Cheongpung at the chapter's close. |

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
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 상인 | 적천강 | merchant_to_legendary_martial_master | Great Hero Jeok | deferential and flattering | Praises Jeok Cheongang while presenting the Poison-Averting Ring and requesting help. |
| 적천강 | 상인 | legendary_guest_to_merchant | you | blunt and transactional | Cuts off the merchant’s praise, asks his identity and origin, and accepts the gift without committing to the requested favor. |
| 무명 | 진태경 | newly_met_monk_to_benefactor | Benefactor | formal-polite | Uses 시주 while asking Taekyung's name. |
| 무명 | 적천강 | junior_monk_to_legendary_martial_master | Great Hero Jeok Cheongang | formal-deferential | Identifies Jeok by the title Fire King and the honorific 대협. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 혈주 | 청풍 | hostile_opponent_to_newly_revealed_identity | Huashan's Invincible Divine Sword; Sword Saint's Disciple or grandson | mocking and taunting | Recognizes Cheongpung's public identity and needles him with his Sword Saint lineage while dismissing the added threat. |
| 매종학 | 혈주 | legendary_martial_master_to_enemy | you | cold and judgmental | After revealing himself, Mae Jonghak condemns the Blood Lord's accumulated sins and orders him to pay the price. |
| 혈주 | 매종학 | enemy_to_revealed_legendary_master | you | shocked and hostile | The Blood Lord addresses Mae Jonghak with 당신 immediately after recognizing him as the Sword Saint. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 매종학 | 적천강 | long-standing martial rival and friend | Great Hero Jeok | casual and familiar | Mae addresses Jeok as 적 대협 while discussing the Alliance Leader position. |
| 적천강 | 매종학 | long-standing martial rival and friend | you | blunt and familiar | Jeok addresses Mae as 당신 while recalling their meeting at Mount Jiuhua. |
| 황보악 | 진태경 | fellow_Ten_Dragons_and_Phoenixes_member | you; damned bastard | angry-insulting | Hwangbo reacts to Taekyung's barefoot-running joke with 이 빌어먹을 놈. |
| 진태경 | 황보악 | stronger_master_to_Hwangbo_Lesser_Family_Head | Hwangbo Ak | casual and taunting | Taekyung calls Hwangbo by name while ordering him to reconcile and warning him to leave. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 청풍 | 매종학 | grandson to grandfather | Grandpa | casual-familiar | Repeatedly calls Mae Jonghak 할아버지 while mistaking the Alliance Leader's summons as a family visit. |
| 진태경 | 매종학 | younger ally to newly installed Alliance Leader | Alliance Leader | formal and deferential | Uses 맹주님 while formally greeting Mae Jonghak as the Alliance Leader. |
| 황보군 | 매종학 | old_battlefield_comrade_to_current_alliance_leader | Great Hero Mae; Alliance Leader | formal-deferential | Hwangbo Gun begins with Great Hero Mae, then switches to the formal Alliance Leader. |
| 매종학 | 황보군 | old_battlefield_comrade_to_family_head | you | casual-familiar | Mae uses 자네 while addressing Hwangbo Gun. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 536
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who seeks Jin Taekyung, Cheongpung, and Jeok Cheongang after escaping the confrontation at Mount Song.
- **Personality:** Calm, confident, theatrically frivolous, casually cruel, and ruthlessly destructive; treats allies as disposable tools and enjoys provoking stronger opponents.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He and the Western Heaven Demon Lord serve the same master; he now seeks to personally kill Cheongpung, Jeok Cheongang, and Jin Taekyung, while his former contact Han Su is dead.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 539
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak martial master known as the Huashan Divine Dragon, the creator of the snake-inspired Mimi Step footwork technique, and now one of the two pavilion masters of the Alliance Leader's direct Two Dragons Pavilion.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi, now a large horned snake, to him, Mungyeong recently examined her condition, and Mungyeong accepted Cheongpung's offer to accompany him after Cheongpung pledged to learn by observation rather than formal instruction.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 527
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Hwangbo Ak.md

# Hwangbo Ak (황보악)

- **Safe through:** Chapter 531
- **Aliases:** Shandong Fist Dragon
- **Role:** Hwangbo Ak is the Lesser Family Head of the Hwangbo Family, a member of the Ten Dragons and Phoenixes, and a young martial prodigy.
- **Personality:** Proud, self-obsessed, status-conscious, and easily humiliated.
- **Voice:** Polite and ceremonious in public but sharp, dismissive, and indignant when challenged.
- **Relationships:** Baek Woo is his longtime friend and fellow Ten Dragons and Phoenixes member; he is infatuated with Ju Hwaran, resents her apparent preference for Jin Taekyung, carries a lasting grudge against Jin Mukyung after their Heaven's Gate Temple encounter, and now regards Taekyung with anger and fear after being publicly humiliated and warned.

### Hwangbo Gun.md

# Hwangbo Gun (황보군)

- **Safe through:** Chapter 537
- **Aliases:** None
- **Role:** Family Head of the Hwangbo Family and father of its late-born only son, the Lesser Family Head.
- **Personality:** Status-conscious, politically resentful, and fiercely protective of his only son; willing to exaggerate grievances to secure favorable treatment.
- **Voice:** Formally deferential toward superiors but aggrieved and forceful when defending his family's standing.
- **Relationships:** Old battlefield comrade of Mae Jonghak; father of the Hwangbo Family's Lesser Family Head; politically opposed to Jin Taekyung and the Black Dragon Demon Gate.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 539
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 536
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, and Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 539
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, can command coordinated raids against powerful monsters, and now serves as one of the two pavilion masters of the Alliance Leader's direct Two Dragons Pavilion.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 539
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 538
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader.
- **Personality:** Playful, easygoing, and teasing, but capable of handling heavy administrative responsibilities efficiently.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 534
- **Aliases:** None
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

### Unnamed.md

# Unnamed (무명)

- **Safe through:** Chapter 521
- **Aliases:** None
- **Role:** Unnamed is a young Shaolin monk and practical Disciple of the late Hong Dao who achieved enlightenment after three months of treatment and training in Repentance Cave, becoming a Supreme Peak master and Jung Ho's young Martial Uncle.
- **Personality:** Naturally timid and introverted, but unable to control himself once angered.
- **Voice:** His current voice is rough, formal, and polite, punctuated by Buddhist invocations.
- **Relationships:** Hong Dao was his Master; Jung Ho is his Martial Nephew; he carries Hong Dao's will and recognizes the Morning Star whom Hong Dao intended him to find.

## Korean source

```text
＃540화



옛말에 발 없는 말이 천 리를 간다고 했다.

하물며 지금의 하남성은 숯불 위의 가마솥처럼 들끓고 있는 형국.

수많은 이목 아래, 젊디젊은 두 신룡(神龍)이 무림 맹주의 특명에 의해 새로운 각주로 임명되었다는 소식은 불과 이틀이 지나기도 전에 하남 땅을 관통했다.

“자네, 그 소식 들었나?”

“이미 들었으니 말하지 말게. 저기 뒷골목 황구도 알고 있을걸.”

두 사람 이상 모이면 그에 관한 이야기로 입방아를 찧기 바빴다.

저마다 찬반은 갈렸지만, 상당수의 무림인들은 진태경과 청풍의 각주 임명에 관하여 호의적이었다.

“각주라. 암, 그 두 사람이라면 자격이 충분하지.”

“그래도 연배를 생각하면 너무 과한 중책을 맡은 것이 아닌가 싶은데…….”

“그러니 대단한 게지. 약관 어림에 누가 그 정도의 신위와 공을 세울 수 있단 말인가?”

“생각해 보니 그도 그렇군.”

“제기랄. 듣고 있자니 배가 아파서 못 참겠군.”

“……형장은 또 뉘시오?”

“아니, 그렇잖소. 누구는 좋은 집안에 좋은 스승 만나서 절세 신공을 익히는데, 이제는 무림맹 각주까지 해 먹어?”

“형장 말대로면 구파일방이나 오대세가의 후기지수들은 죄다 초절정 고수게? 그리고 그걸 왜 우리한테 지랄이신지…….”

“그냥 듣던 와중에 기분 더러워져서 끼어들었소.”

그러나 빛이 있으면 그늘도 있는 법이다.

진태경과 청풍의 이름은 동경의 대상인 동시에 질투의 대상이었고, 거칠게 살아온 낭인 무사뿐만이 아닌 명문 대파의 제자들에게도 마찬가지였다.

“제기랄. 이게 말이 되나?”

“별수 없지. 다른 사람도 아니고 맹주께서 친히 특명을 내리신 건데. 본문의 장문인께서도 이 일에 관해서는 일언반구 하지 말라 단단히 못 박아 두셨네.”

“그럼 자네는?”

“후우, 말해 봤자 뭐 하겠나. 나야 고작 삼대 제자인데. 안 그래도 몇 시진 전에 동기 놈 하나가 입을 잘못 놀리는 바람에 된통 당했네. 대노하신 사백(師伯)께서 니 위, 내 아래로 집합하라고 하셔서…….”

“알 만하군.”

“어느 미친놈이 스승님까지 불러오는 바람에 분위기가 끝내줬지. 혼백까지 탈탈 털렸네. 한참 나이가 어린 열화신룡과 화산신룡도 저렇게 잘나가는데, 너희는 뭐 하고 있냐는 소리까지 들었다니까.”

“그게 말인가, 방귀인가? 그 두 놈이 괴물인 걸 왜 우리한테 뭐라 해?”

“그러니까. 따지고 보면 본인들도 못 했으면서.”

“잠깐. 자네 설마…….”

“미쳤나? 난 안 했지. 그런데 앞에 스승님을 불러온 그 미친놈이 말릴 틈도 없이 딱 그러더군. 걔들 스승님은 화왕에 검성이잖아요.”

“세상에, 지금 내가 뭘 들은 거야. 내 팔뚝 좀 보게. 닭살 올라왔어.”

“자네도 이 지경인데 그걸 직접 들은 나나 다른 사형제들은 어땠겠나. 지금 생각해도 불알까지 닭살이 돋는군.”

“혹시나 해서 하는 말인데, 보여 줄 필요는 없네.”

“……보여 달라고 애걸복걸해도 절대 안 보여 줘. 어쨌건 그 두 사람 때문에 분위기가 장난이 아닐세. 물론 황보세가만큼은 아니겠지만.”

황보세가의 소가주이자 십봉룡(十鳳龍) 중 한 사람으로 꼽히는 산동권룡(山東拳龍)이 개망신을 당했다는 소문은 이미 모르는 사람이 없었다.

그런 와중에 무림맹 외당의 대주로 임명되었으니, 맹주부 직속의 각주인 진태경과의 격차는 하늘과 땅 차이라 할 수 있었다.

“일간에 떠도는 말로는 황보세가의 가주께서 직접 맹주를 독대하여 처벌을 요구했다던데…….”

“가주가 직접 말하고 다녔다니 아마 사실일걸세. 결과는 뭐, 자네도 이미 알겠지만.”

황보세가의 가주, 황보군은 무림 맹주와의 독대 내용을 득의양양하게 떠벌리고 다녔고, 불과 한나절도 되지 않아 전달된 징계 내용에 치욕을 감내해야 했다.



一. 이룡각주 진태경은 눈앞에서 다툼이 벌어지고 있음에도 사사로이 한쪽의 편만을 들었으므로, 한정된 기간 금식(禁食)을 명한다.

二. 흑룡마문의 호거아(虎巨兒) 태산은 두 가지 죄를 저질렀다.

대로변에서 분쟁을 일으키고 양민들에게 피해를 입힌 것이 첫 번째 죄요. 맹의 규율을 무시하고 먼저 병장기를 휘둘러 온당한 절차를 따르지 않았으니 이것이 두 번째 죄다.

하지만 여러 사람의 목격과 증언에 따라 일부 당위성을 인정한바. 그의 행동으로 손해를 입은 이들들에게 각각 열 배의 배상금을 치르도록 한다.

三. 산동권룡 황보악의 죄 또한 호거아 태산과 유사하다.

하지만 실질적인 분쟁 원인을 제공한 점, 그리고 문제가 될 만한 발언들을 한 점을 들어 일정 기간 근신을 명한다.



황보군으로서는 미치고 팔짝 뛸 일이었다.

다음 날 진태경이 앉은 자리에서 국밥 열 그릇을 비우고 배를 두드렸다는 소문이 퍼지자 더욱 그럴 수밖에 없었다.

그에 찬동하는 정파의 순혈주의자들 역시 불만을 내비쳤지만, 검성 매종학이라는 거인의 그림자는 짙었고 고작 이 정도 일로 맹주의 권위에 반할 수는 없었기에 속으로 삭이는 수밖에 없었다.

그리고 이처럼 동경과 질시가 뒤섞인 사람들의 관심 속에서, 이룡각주에 임명된 진태경은 불과 하루 만에 다시 한번 파격적인 행보를 선보였다.

그 시작은 수많은 사람이 오가는 대로변 벽면에 떡하니 붙여 놓은 하나의 방(訪)이었다.

“자네, 혹시 그거 봤나?”

“이룡각에 관한 이야기라면 이미 귀가 터질 정도로 들었, 잠깐. 보다니? 뭘 말하는 겐가?”

“반 시진 전쯤엔가. 혁, 혁 뭐시기라는 자가 대로변 곳곳에 커다란 방을 붙여놨다네.”

“그 혁 뭐시기에 관한 이야기를 내가 왜 들어야 하는데?”

“그 혁 뭐시기가 열화신룡 진태경의 수족이니까. 방을 읽어 보니 이룡각에서 사람을 구한다고 하더군.”

“뭣이? 그게 진정 사실인가!”

“틀림없다네. 그런데 방 내용이…… 좀 이상해. 다른 사람도 있는데 좀. 그냥 다 이상해.”

“무슨 소린가, 그건 또.”

“그게, 그러니까. 아, 아닐세. 차라리 직접 가서 보고 듣게.”

“……듣는 건 또 뭔가?”

지금 이룡각에 관련된 모든 소식은 하남에서 뜨거운 감자다.

그런데 무림의 유구한 역사를 되짚어 봐도 유례를 찾기 어려운 천재성과 공을 세운 최연소 각주가 또다시 일을 벌였다?

“아, 이건 못 참지!”

이미 소속이 정해진 무림인도, 아직 몸담을 곳을 찾지 못한 자도. 심지어는 호기심을 느낀 양민들조차 몰려들었다.

그리고 한자리에 모인 그들은 마침내 목격할 수 있었다.



★무명 소졸이었던 내가, 이룡각에서는 무림 영웅?!★



괴상한 문양과 함께 대문짝만하게 적힌 글귀를.

그 앞에 구름처럼 몰려든 사람들은 하나 같이 눈을 부릅뜨며 탄성을 토해 냈다.

“저, 저것은!”

“허어!”

어찌 이리도 쉽고, 간단하며 파격적인 문구란 말인가. 그 아래에 쭉 적혀 있는 글씨들 역시 한눈에 쏙쏙 들어왔다.



모집 요건(募集要件)

첫째. 무엇이든 하고자 하는 열의가 있는 자.

둘째. 심성이 올곧은 자.

셋째. 최소 검기상인(劍氣傷人)의 경지에 도달한 자.

＃십이시진(十二時辰) 상시 모집 ＃절정 미만 응 안 받아 ＃성별 및 출신 문파 안 따지고 ＃나이도 상관없음 ＃인생은 여든부터 ＃야, 너두 할 수 있어.



그야말로 하나하나 파격 그 자체!

단지 눈으로 읽는 것만으로도 피가 끓고 가슴이 뛰는 명문(名文)의 연속에 사람들 사이에선 뜨거운 외침이 터져 나왔다.

“그래, 나도 할 수 있다악!”

“너두? 나두!”

“으아아아! 이룡각이 나를 부른다!”

“젠장. 검기상인이라니!”

방의 내용을 확인한 수백여 명의 좌중들이 저마다 환호와 탄식을 내뱉던 바로 그 순간이었다.

띠리링.

어디선가 들려오는 맑고도 경쾌한 선율.

사람들이 약속이라도 한 것처럼 길을 트자, 어디선가 나타난 일단의 무리가 구름을 밟는 듯한 걸음걸이로 그 사이를 가로질렀다.

“저건…….”

“홍학루의 악단(樂團) 같은데?”

“아니, 여기서 악단이 왜 나와?”

하남에서도 열 손가락 안에 든다는 유명 악단의 난데없는 등장.

이어 어리둥절해하는 사람들 앞에 기가 막힌 용모의 미인이 나타나 싱긋 웃었다.

“홍매? 홍매다!”

“와아아아!”

홍학루 최고의 미인이자 황홀한 노래 실력으로 이름 높은 가기(歌妓)가 기품 있는 자세로 고개를 꾸벅 숙인 뒤 눈짓하자, 신호를 알아들은 악공들이 연주를 시작했다.

띠리링. 차랑!

맑고 경쾌하기 그지없는 노랫가락.

그리고 마침내 가기의 입술 사이로 흘러나온 노래의 첫 소절을 듣는 순간.

이 자리에 있던 무림인들은 홀린 듯이 깨달았다.

“무림맹 이룡각에 들어오고, 나의 성공 시대 시작됐다~”

“……!”

자신이 성공하기 위해서는, 반드시 이룡각에 들어가야 한다는 것을.



* * *



나는 예전부터 그랬다. 별다른 이유는 없다. 그저 전부터 노래도, 아이도 그다지 좋아하지 않았을 뿐이다.

하지만 오늘만큼은 예외다.

“껄껄. 녀석들.”

나는 창문 틈새로 새어 들어오는 소리를 들으며 흐뭇하게 웃음 지었다.

창밖에는 초등학생쯤 되어 보이는 어린애들이 활기차게 뛰어다니며 노래를 부르고 있었다.

“무림맹 이룡각에 들어오고, 나의 성공 시대 시작됐다~!”

“무림맹 이룡각에 들어오고, 나를 찾는 문파 많아졌다~!”

“무림맹 이룡각에 들어오고, 내 인생이 달라졌다~!”

“새로운 시대, 새로운 영웅!”

“무림맹 이룡각!”

마무리까지 완벽하다.

자축하는 의미로 작게 손뼉을 부딪친 나는 황당한 표정으로 이쪽을 바라보는 혁무진을 발견했다.

“뭐, 인마.”

“……그냥 황당해서요. 이런 방법은 듣도 보도 못했는데.”

“어때. 혁신적이지 않냐.”

혁무진이 떨떠름하게 고개를 끄덕였다.

“효과는 확실한 것 같습니다. 방금까지 주위를 살피고 왔는데, 아주 그냥 난리예요. 암천이라도 쳐들어온 줄 알았다니까요.”

“내 그럴 줄 알았지. 후후.”

“특히 그 노랫가락이 진짜…… 사방에서 난리입니다. 항간에는 조장님께서 무림에 독을 풀었다는 이야기도 나오고 있어요.”

“그건 또 뭔소리야. 웬 독?”

“그게, 아편보다 중독성이 심하답니다.”

“오오. 오오오.”

아, 뿌듯하다.

이 얼마나 보람찬 상황이란 말인가. 서울의 모 사이버 대학에서 표절 문제로 고소를 당할 수도 있겠지만 이곳은 무림이다.

‘미안하고 감사합니다. 노래 잘 쓰겠습니다.’

미개한 무림 촌놈들의 고막을 사정없이 유린할 이 시대 최고의 명곡은 그렇게 탄생했다.

처음 대충 떠올린 멜로디를 알려 주었을 때 악단장과 가기가 지었던 표정은 지금 떠올려도 짜릿하다.

‘불을 발견한 원시인의 표정이었지.’

그리스 로마 신화 속 프로메테우스가 이런 심정이었을까 싶다.

다만 차이가 있다면 내 경우에는 제우스가 보낸 독수리에게 장기 기부를 하는 대신, 밀려드는 지원자들을 상대해야 한다는 거다.

“지원 접수는. 다 끝났냐?”

내 물음에 혁무진이 제정신이냐는 표정으로 되물었다.

“진심이십니까?”

“생각했던 것보다 많나 보네.”

“미쳤습니다. 미쳤다고요. 암천 쪽에서도 지원서를 보낸 게 아닐까 의심이 될 정돕니다.”

음. 상상했던 것 이상으로 약발이 센 모양인데.

이런 일이 있을까봐 절정 고수라는 요건을 붙였는데, 역시 천하는 넓고 고수는 많은 모양이었다.

“그럼 이렇게 하자. 우선…….”

잠시 생각에 잠겨 있던 내가 입을 막 뗀 바로 그 순간.

쾅!

문이 부서지며 한 사람이 모습을 드러냈다.

“무림맹 이룡각에 들어오고. 나의 성공 시대 시작됐다.”

세상에서 가장 음산한 노랫가락. 오싹한 표정.

붉은 안광을 마주하고 꼼짝없이 굳어 버린 내게, 화왕 적천강이 씹어뱉듯 말을 이었다.

“이 빌어먹을 노래 때문에, 노부가 주화입마에 빠질 뻔했다.”

“……어서옵쇼.”
```

## Final English reading copy

```markdown
# Chapter 540

They say that words without feet can travel a thousand li.

And these days, Henan Province was boiling like a cauldron over a charcoal fire.

Under countless watchful eyes, news of two exceptionally young Divine Dragons being appointed pavilion masters by the Alliance Leader’s special order spread across Henan before even two days had passed.

“Have you heard the news?”

“I’ve already heard it, so don’t tell me. Even that yellow dog in the back alley probably knows.”

Whenever two or more people gathered, they were busy gossiping about it.

Opinions were divided, but a considerable number of martial artists viewed Jin Taekyung and Cheongpung’s appointments favorably.

“Pavilion masters, huh? Of course. Those two are more than qualified.”

“Still, considering their ages, haven’t they been given responsibilities that are a little too heavy?”

“That’s what makes it so impressive. Who can achieve that level of might and merit at barely twenty?”

“Now that you mention it, you’re right.”

“Damn it. Listening to this is making my stomach hurt.”

“…And who the hell are you, Brother?”

“No, but isn’t it true? Some people are born into good families, meet good masters, learn peerless martial arts, and now they even get to become pavilion masters of the Murim Alliance?”

“By your logic, the young prodigies of the Nine Sects and One Gang and the Five Great Families are all Supreme Peak masters. And why are you taking it out on us?”

“I just got pissed off listening to you and decided to butt in.”

But where there was light, there was bound to be shadow.

Jin Taekyung and Cheongpung were objects of admiration, but they were also objects of envy. That was true not only of wandering martial artists who had lived rough lives, but also of disciples from prestigious sects and families.

“Damn it. How does this make any sense?”

“There’s nothing we can do. It wasn’t just anyone who gave them the appointment—the Alliance Leader himself issued the order. Our Sect Leader firmly told us not to say a word about the matter.”

“And what about you?”

“Whew. What good would it do to say anything? I’m only a third-generation Disciple. Besides, one of my fellow disciples let his mouth run a few shichen ago and got it bad. The enraged Senior Martial Uncle ordered everyone above him and below me to assemble, so…”

“I can imagine.”

“Some madman even called our Master over, so the atmosphere was incredible. He wrung us out down to our souls. He even asked what we were doing when the much younger Blazing Flame Divine Dragon and Huashan Divine Dragon were doing so well.”

“What kind of nonsense is that? Why blame us because those two are monsters?”

“Exactly. When you think about it, they couldn’t do it either.”

“Wait. Don’t tell me…”

“Are you crazy? I didn’t say it. But before anyone could stop him, the madman who’d called our Master over blurted out, ‘Their masters are the Fire King and the Sword Saint.’”

“Good heavens. What am I hearing right now? Look at my arm. I’ve got goose bumps.”

“You think you’re bad? Imagine how I and the other Senior Brothers felt after hearing it directly. Even now, I’ve got goose bumps all the way down to my balls.”

“I’m only saying this in case you’re planning something, but you don’t need to show me.”

“…Even if you begged me to show you, I never would. Anyway, things are insane because of those two. Though perhaps not quite as insane as in the Hwangbo Family.”

By then, everyone had heard the rumor that the Lesser Family Head of the Hwangbo Family and one of the Ten Dragons and Phoenixes, the Shandong Fist Dragon, had suffered a spectacular disgrace.

And after he was appointed Commander of the Murim Alliance’s Outer Hall, the difference between him and Jin Taekyung, a pavilion master directly under the Alliance Leader’s Office, could only be described as the distance between heaven and earth.

“I heard that the Family Head of the Hwangbo Family personally met with the Alliance Leader and demanded punishment…”

“He went around telling everyone himself, so it’s probably true. As for the result, you already know.”

Hwangbo Gun, the Family Head of the Hwangbo Family, had proudly bragged about his private meeting with the Alliance Leader. Before even half a day had passed, however, the disciplinary decision reached him, and he was forced to swallow the humiliation.

I. Jin Taekyung, Pavilion Master of the Two Dragons Pavilion, improperly sided with only one party despite witnessing the dispute firsthand. He is therefore ordered to fast for a limited period.

II. Taishan of the Black Dragon Demon Gate committed two offenses.

His first offense was causing a dispute on a main road and harming innocent civilians. His second offense was disregarding the Alliance’s rules and wielding a weapon first, thereby failing to follow proper procedure.

However, in light of the numerous eyewitnesses and testimonies, some justification for his actions is acknowledged. He is ordered to pay each person who suffered losses because of his actions ten times the amount of their damages.

III. The offense committed by the Shandong Fist Dragon, Hwangbo Ak, is similar to Taishan’s.

However, because he substantially caused the dispute and made remarks liable to cause trouble, he is ordered to remain under disciplinary confinement for a fixed period.

For Hwangbo Gun, it was enough to drive him mad.

The next day, rumors spread that Jin Taekyung had polished off ten bowls of gukbap[^1] in one sitting and patted his stomach, which only made matters worse.

The orthodox purists who supported him also voiced their discontent, but the shadow cast by the giant known as the Sword Saint Mae Jonghak was too deep. They could not defy the Alliance Leader’s authority over something as minor as this, so they had no choice but to swallow their anger.

And amid all the attention of people whose admiration and envy were hopelessly mixed together, Jin Taekyung, newly appointed Pavilion Master of the Two Dragons Pavilion, made another extraordinary move only a day later.

It began with a single notice pasted conspicuously on the wall beside a main road crowded with passersby.

“Have you seen it?”

“If you mean the news about the Two Dragons Pavilion, I’ve heard enough to make my ears bleed. Wait. Seen what? What are you talking about?”

“About half a shichen ago, some fellow named Hyuk—Hyuk something—put up huge notices all over the main roads.”

“Why would I want to hear about that Hyuk-whatsisname?”

“Because that Hyuk-whatsisname is Blazing Flame Divine Dragon Jin Taekyung’s right-hand man. I read the notice, and apparently the Two Dragons Pavilion is recruiting people.”

“What? Is that really true?”

“Without a doubt. But the contents of the notice are… strange. Well, there are other people around, so… Ah, never mind. The whole thing is strange.”

“What are you talking about?”

“It’s, well… Never mind. You should go see and hear it for yourself.”

“…Hear it? What do you mean?”

Every piece of news related to the Two Dragons Pavilion had become a hot topic in Henan.

And now, the youngest pavilion master in Murim history—one who had achieved genius and great accomplishments rarely seen in the long history of the martial world—had caused another incident?

“Ah, I can’t miss this!”

Martial artists who already had affiliations, martial artists who had yet to find a place to belong, and even curious commoners all came rushing over.

And when they gathered in one place, they finally saw it.

★I Was a Nameless Foot Soldier, but in the Two Dragons Pavilion, I’m a Murim Hero?!★

The enormous words, written alongside a bizarre emblem.

The people gathered before it like clouds all widened their eyes and cried out in astonishment.

“Th-That!”

“Good heavens!”

How could a phrase be so easy, simple, and revolutionary? The lines written beneath it were just as easy to take in at a glance.

**Recruitment Requirements**

**First:** Someone with the passion to do whatever they set their mind to.

**Second:** Someone with an upright character.

**Third:** Someone who has reached at least the level of injuring others with Sword Energy.

# Recruiting around the clock # No one below Peak need apply # Gender and sect affiliation don’t matter # Age doesn’t matter # Life begins at eighty # Hey, you can do it too.

Every single part of it was outrageous!

The succession of magnificent lines was enough to make blood surge and hearts pound simply by reading them. A passionate cry erupted from the crowd.

“Yeah! I can do it too!”

“You too? Me too!”

“Aaaah! The Two Dragons Pavilion is calling me!”

“Damn it! The level of injuring others with Sword Energy!”

At that exact moment, the hundreds of people who had read the notice let out their own cheers and groans.

Ting-a-ling.

A clear, lively melody rang out from somewhere.

The people parted as if they had agreed beforehand, and a group that seemed to walk on clouds crossed through the crowd.

“What’s that?”

“Isn’t that the band from Honghakru?[^2]”

[^2]: Honghakru, literally “Red Crane Pavilion,” is a renowned entertainment house in Henan.

“Why would a band show up here?”

The sudden appearance of a famous band ranked among the top ten in all of Henan left everyone bewildered.

Then, before the confused crowd, a breathtakingly beautiful woman appeared and smiled sweetly.

“Hongmae? It’s Hongmae![^3]”

[^3]: Hongmae literally means “Red Plum.”

“Waaaaah!”

Hongmae was Honghakru’s most beautiful singer, a singing courtesan famous for her enchanting voice. She bowed her head with graceful poise, then gave a meaningful glance.

The musicians who understood her signal began to play.

Ting-a-ling. Chaarang!

A song melody as clear and lively as could be.

And the moment they heard the first line of the song flowing from the singer’s lips, the martial artists present were bewitched into understanding the truth.

“Join the Murim Alliance’s Two Dragons Pavilion, and my era of success begins~”

“……”

To succeed in life, they absolutely had to join the Two Dragons Pavilion.

* * *

I had always been that way. There was no particular reason. I simply hadn’t liked songs or children all that much.

But today was an exception.

“Heh heh. You little rascals.”

I smiled contentedly as I listened to the sounds slipping through the gap in the window.

Outside, children who looked to be around elementary school age were running around energetically and singing.

“Join the Murim Alliance’s Two Dragons Pavilion, and my era of success begins~!”

“Join the Murim Alliance’s Two Dragons Pavilion, and now more sects are looking for me~!”

“Join the Murim Alliance’s Two Dragons Pavilion, and my life has changed~!”

“A new era, a new hero!”

“The Murim Alliance’s Two Dragons Pavilion!”

The ending was perfect, too.

I lightly clapped my hands in celebration, then noticed Hyuk Mujin staring at me with an absurd expression.

“What is it, you bastard?”

“…I’m just stunned. I’ve never heard of anything like this.”

“What do you think? Innovative, isn’t it?”

Hyuk Mujin nodded with an awkward expression.

“It seems to be highly effective. I just went around checking the area, and it’s complete chaos. You’d think Dark Heaven had invaded.”

“I knew it would work. Heh heh.”

“Especially that song. It’s causing an uproar everywhere. People are even saying that the Captain has poisoned Murim.”

“What does that mean? What poison?”

“They say it’s more addictive than opium.”

“Oh. Ohoho.”

Ah, how satisfying.

What a rewarding situation this was. I might get sued for plagiarism by some cyber university in Seoul, but this was Murim.

*I’m sorry, and thank you. I’ll use the song well.*

And so, the greatest hit of the era—destined to mercilessly violate the eardrums of the primitive Murim bumpkins—was born.

Even now, remembering the expressions on the bandleader’s and singer’s faces when I first taught them the rough melody I had come up with made me shiver with excitement.

*It was the expression of primitive men who had discovered fire.*

I wondered if this was how Prometheus had felt in Greek mythology.

The difference was that instead of donating my organs to the eagle sent by Zeus, I had to deal with the flood of applicants.

“How is the application process? Are you done?”

Hyuk Mujin looked at me as though I had lost my mind.

“Are you serious?”

“I suppose there are more than you expected.”

“More? It’s insane. Completely insane. There are so many that I’m starting to suspect Dark Heaven may have sent in applications too.”

Hmm. It seemed the song was even more potent than I had imagined.

I had added the requirement of being a Peak master because I was worried something like this might happen, but the world was vast and apparently full of masters.

“Then let’s do this. First…”

I was just about to open my mouth after thinking for a moment when—

Boom!

The door shattered, and someone appeared.

“Join the Murim Alliance’s Two Dragons Pavilion. My era of success begins.”

The most ominous song in the world.

A chilling expression.

I froze completely when I met those glowing red eyes. Fire King Jeok Cheongang continued, spitting out each word.

“Because of this damn song, this old man almost suffered qi deviation.”

“…Welcome.”

[^1]: Gukbap is rice served in a bowl of hot soup, a common Korean meal.
```
