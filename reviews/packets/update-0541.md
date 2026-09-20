<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0541.txt",
      "sha256": "3a504815f57c249e15ae1fe063047f660cca922f123dff3a91f05748a6ac8bfa",
      "bytes": 15247
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "3512bc0c53197e0ff571e98ce12b15c665a2f22e63ee975c22ef0496c971d313",
      "bytes": 4048
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2e9a2a72c10fe019bd055b22edbad57a97f88807b4db79896966c264ea8295b0",
      "bytes": 171001
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "aceb92a9f8f77d4d6375c4b306d67a5fdea300985369ce7f04366a445ca32d4b",
      "bytes": 553
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "ae145403dff928df4e57382c21c0435d3960d6a7689c0ccf3a6e43c61a13f4fd",
      "bytes": 667
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "71518704447254e935cd4a0ebb4ca4bb4162261b8a16d586362c52b348923c67",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "3d8f8eafde1cd48a2ddb5a1df9a797cd443e37a55f64fd4d1621c0e4f5c10b29",
      "bytes": 1630
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "a811c8af30f87d7cf29ee9269890a44e27c1e13a62058a2d6f06fefab52e668b",
      "bytes": 2192
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "132c6a2a8713f77d309cdf938424cfe8dedc148a7c8e7b100840996620d7e340",
      "bytes": 622
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "15ac6e329987b2937a5cb607890264259883ca4f1986cc4eaea7b7489ec62855",
      "bytes": 162019
    }
  ],
  "estimated_tokens": 13068
}
-->

# Durable State Update — Chapter 541

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 541. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 541. Profile updates may replace only one
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
  "chapter": 541,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 541,
    "continuity_sources": [541],
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
    "Mae Jonghak formally appointed Jin Taekyung and Cheongpung as the two pavilion masters of the Alliance Leader's direct Two Dragons Pavilion, and their appointments are now public throughout Henan.",
    "Tang Sadok and the Sichuan Tang Clan publicly support Jin Taekyung and Cheongpung and acknowledge an unrepayable debt to them.",
    "Taekyung believes the Zhongnan Sect resents him, the Jin Family of Taiyuan, and Jeok Cheongang after its repeated humiliations and will obstruct them.",
    "Cheongpung created Mimi Step from Mimi's movements; it is a snake-like footwork technique fast enough that Taekyung could barely track it with his naked eyes, and Mungyeong recognizes Cheongpung as having the makings of a Grandmaster.",
    "Mimi is now a large horned snake under Cheongpung's care, eats dumplings, sweets, and Blood Fish, and has recently had her condition examined by Mungyeong.",
    "Mungyeong ended Taekyung's direct training and assigned him a final task of incorporating martial principles into his learned martial arts.",
    "Zhuge Feng's Demon-Sealing Formation still blocks all mana from the exposed Gate, while Jang Taebo is summoning artisans to process the Water God Dragon's remains.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "The Black Dragon Demon Gate remains a major unorthodox power descended from the Demonic Cult's Twelve Branches; Sama Pyo is its Young Sect Leader and Black Dragon Saber, and Taishan is his giant subordinate.",
    "Jin Taekyung remains a Supreme Peak master with Three Flowers Gather at the Crown, advanced qi perception, exceptional resistance to monster Fear, and public S-rank-level recognition despite retaining an A-rank license.",
    "The System has assigned Taekyung's first Two Dragons Pavilion Quest: recruit at least five companions and name the organization, or receive the Title Loner. Mungyeong has accepted Cheongpung's offer, and Taekyung's public notices and promotional song have produced an overwhelming flood of applicants."
  ],
  "continuity_sources": [
    540,
    539
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, the Azure Sky Sword King?",
    "Why did Ju Hwaran and Sama Pyo's political engagement end?",
    "Which additional companions will join the Two Dragons Pavilion, what name will it receive, and can Taekyung complete the System Quest?"
  ],
  "safe_through": 540,
  "temporary_decisions": [
    "Render 고월루 as Gowolru, 곤륜운룡 as Kunlun Cloud Dragon, 학우 as Hak Woo, 이룡각 as Two Dragons Pavilion, 협 as chivalry, 인의 as humanity, 협객 as knight-errant, 홍학루 as Honghakru, 홍매 as Hongmae, and 호거아 as Tiger Giant Child; render 전 정혼자 contextually as former fiancé or former fiancée.",
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
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 열화문    | **Fire Gate Clan**               |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 신법     | **movement technique**                           |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 낭인     | **wandering martial artist**                     |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 기루     | **pleasure house**                               |                                                       |
| 문주     | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 극양                        | **Extreme Yang**      |
| 하남     | **Henan**              |
| 노부      | **this old man / I**                                            |
| 본문      | **our sect / this sect**                                        |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 천하제일인 | **greatest under heaven** | Superlative martial distinction used in Hong Jin and Jin Wikyung's banter. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 낙양 | **Luoyang** | Historic city in Henan Province and the chapter’s setting. |
| 천기 | **heavenly patterns** | Celestial patterns Hong Dao studies to perceive major changes and omens. |
| 개봉 | **Kaifeng** | City where the preliminary competition will be held. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 이룡 | **Two Dragons** | Collective ranking beneath the Ten Kings in Murim gossip. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 이룡각 | **Two Dragons Pavilion** | Named pavilion whose masters are identified as Taekyung and Cheongpung at the chapter's close. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 539
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 540
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 540
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 540
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, and Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 540
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, can command coordinated raids against powerful monsters, and now serves as one of the two pavilion masters of the Alliance Leader's direct Two Dragons Pavilion.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 540
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃541화



하남은 유구한 역사를 지닌 땅이다.

개봉(開封), 낙양(洛陽)과 같은 여러 왕조가 도읍으로 삼았던 천년 고도의 대도시. 그리고 네 개의 명산을 비롯하여 기가 막힌 자연경관과 각종 명승고적을 구경할 수 있다.

그렇다 보니 사시사철 사람들이 끊이질 않았고, 당연하게도 객잔과 기루 등 유흥 및 숙박을 위한 곳이 많았다.

하지만 지금처럼 이 거리가 들끓었던 적은 없었노라고, 삼대째 한 자리에서 객잔을 운영 중인 늙은 주인장은 자신 있게 말할 수 있었다.

‘이, 이게 도대체.’

아연한 눈빛으로 주위를 바라보는 늙은 객잔 주인의 눈동자에 비친 것은, 그야말로 인산인해(人山人海)라 불릴 만큼 엄청난 인파였다.

“거기 잠깐! 은근슬쩍 새치기하지 마시오!

“어허, 누가 자꾸 미는가!”

“하룻강아지 같은 놈이 아까부터 건방진 눈빛을 보내는군. 진정 관을 봐야 정신을 차리겠나?”

“뭐라? 보자 보자 하니 이 낭인 나부랭이가…….”

“허허. 다들 혈기가 넘치는군. 보기 좋으이.”

“보기 좋긴요. 아까부터 시끄러워서 견딜 수가 없는데.”

흡사 거친 늑대를 연상시키는 낭인 무사와 이름 있는 명가(名家)의 핏줄로 보이는 사내가 서로를 향해 날카로운 눈빛을 쏘아 보낸다.

눈앞에서 벌어지는 광경에 반백의 중년인이 너털웃음을 터트리고, 나이를 짐작할 수 없는 미부인은 혀를 찼다.

거기에 더해, 멀찍이 떨어진 곳에서 그들을 바라보며 수군거리는 수많은 사람들까지.

‘이, 이것이 당최 무슨 일이여.’

극심한 혼란 속, 반쯤 혼백이 빠져나가던 객잔 주인의 귓가를 파고드는 목소리가 있었다.

“너무 걱정할 것 없네.”

“예?”

“거기 말고. 이쪽일세.”

깜짝 놀라 재차 돌아선 객잔 주인의 눈에 한 사람이 닿았다.

길게 줄을 서고 있던 다른 이들과는 달리 탁자 한 자리를 차지하고 앉아 느긋하게 술잔을 기울이던 노인이었다.

“저들도 다 생각이 있을 테니, 별다른 소란은 일어나지 않을게야.”

작은 체구에 제멋대로 자라난 흰 수염. 그리고 취기로 벌겋게 달아오른 안색.

혹시 무림인인가 하는 생각이 스쳤지만 영락없는 주정뱅이 노인네다. 슬쩍 노인을 살핀 객잔 주인이 한껏 낮춘 목소리로 속삭였다.

“이, 이게 도대체 무슨 일이랍니까?”

“저마다 성공 시대를 시작하고 싶은 사람들이 모인 게지. 자네도 그 노래를 들어 봤을 텐데. 무림맹 이룡각에 들어오고-”

이내 노인의 입술 사이로 흘러나오는 흥겨운 곡조에, 반사적으로 어깨를 들썩이던 객잔 주인이 눈을 동그랗게 떴다.

“아. 혹시 그, 이룡각인가 하는?”

“바로 맞췄네. 그 이룡각의 젊은 각주가 바로 이곳에 머무르고 있지.”

“허어.”

객잔 주인이 외마디 탄성을 흘렸다.

별채에 머무르는 이가 강호에서 이름 높은 청년 협객이라는 것 정도는 알고 있었지만, 바로 그 소문의 이룡각주라고는 상상치 못했다.

“하여 저토록 많은 무림인들이 찾아온 게로군요. 하지만 아무리 그래도 이 정도일 줄은…….

“끌끌. 좋은 기회 아니겠나. 출신 성분도, 성별과 나이도 따지지 않는 곳은 흔치 않지.”

“그렇지요. 듣자 하니 팔순 먹은 노인도 지원할 수 있다던데.”

노인이 조용히 대꾸했다.

“안 그래도 그럴 생각일세.”

“껄껄. 농담도 잘 하십니다.”

“농담으로 들리나?”

“예?”

“농담으로 들리느냐 물었네.”

순간 웃음소리가 뚝 그쳤다. 객잔 주인이 떨리는 눈동자로 노인을 응시했다.

“하, 하면 노인장, 아니 어르신께서도?”

“그야 뻔하지 않나.”

노인이 술에 흠뻑 젖은 수염을 소매로 훔쳤다. 동시에 슬쩍 들린 옷 사이로 낡은 검갑이 모습을 드러냈다.

“나 역시 무림인이라네. 저들과 같은. 그리고 자네와 다른.”

“헙.”

“그리 겁먹을 필요 없네. 노부는 양민을 건드리지 않거든.”

잠시 뭔가를 생각하던 노인이 나직하게 덧붙였다.

“어지간해서는 말일세.”

“……!”

부드러운 목소리에는 이제 한 방울의 취기도 느껴지지 않았고, 순간 스쳐 지나간 눈빛은 광포한 맹수의 그것과 같았다.

은연중 오싹한 한기를 느낀 객잔 주인이 자신도 모르게 뒷걸음질 친 바로 그때, 계단을 내려오는 인기척이 있었다.

저벅, 저벅.

누군가의 발걸음 소리. 노인의 눈동자가 번쩍 빛났다.

“슬슬 시작인가?”

그리 짐작한 것은 노인뿐만이 아니었다. 길게 줄을 선 채 기다리던 수십여 명의 절정 고수부터, 그보다 열 배는 되는 듯한 구경꾼들까지.

순식간에 내려앉은 침묵 속에서 한 사람이 모습을 드러냈다.

“얼마나 왔는…… 어이쿠, 깜짝이야.”

화들짝 놀라는 청년, 혁무진의 모습을 확인한 사람들의 표정 위로 작은 실망감이 스쳤다.

하지만 일찌감치 기파를 느끼고 있던 절정 고수들은 담담하게 중얼거렸다.

“열화신룡이 아니군.”

“심부름꾼을 대신 내려보내다니. 벌써부터 상전 행세를 하는 건가?”

“심부름꾼치고는 제법인데요. 저 나이에 저만한 기세라면 어지간한 명문 대파의 이대 제자보다 뛰어나요.”

“동의하오. 그리고 열화신룡이라면 그럴 수도 있지.”

곳곳에서 흘러나오는 목소리들. 웅성거리는 엄청난 인파를 떨떠름하게 쳐다보던 혁무진이 목을 가다듬었다.

“어, 면접을 시작하라는 조장, 아니 각주님의 명령이 있으셨습니다. 고로 지금부터 한 분씩 호명할 테니, 정해진 순서에 따라 차례대로 저를 따라오시면 됩니다.”

절정의 경지에 올랐다는 것은 무림 어디에서도 인정받는 고수라는 뜻.

저마다 자신의 실력에 자부심을 가진 절정 고수들은 또다시 기다려야 한다는 말에 입맛을 다셨지만, 그 이상으로 불만을 표하지는 않았다.

목마른 자가 우물을 파는 법. 이 자리에 온 이상 감내해야 할 일이었다.

“충분히 알겠으니, 흰소리는 그만 지껄이고 어서 호명하거라.”

거친 인상을 한 중년 낭인의 말에, 혁무진이 눈을 동그랗게 떴다.

“오, 진짜네.”

“뭐가 말이냐?”

“아. 별건 아니고요. 각주님께서 말씀하시길 초면에 반말하고 예의 없게 구는 사람이 있으면 무조건 떨어트리라고 하셨거든요. 저도 이렇게 빨리 나올 줄은 몰랐네요.”

“……어?”

“어디 보자, 흑혈도 노귀산 대협 맞으시죠? 이만 돌아가시면 됩니다.”

말없이 눈을 깜빡이던 중년 낭인, 흑혈도가 버럭 외쳤다.

“이런 개 같은 법이 어디 있느냐!”

옆구리에 찬 전낭에서 흑혈도의 신상명세가 적힌 죽간을 빼낸 혁무진이 고개를 끄덕였다.

“여기 있네요. 그런 법이.”

“자그마치 한 시진을 기다렸다!”

“아이고, 유감입니다.”

“네놈이 상전을 믿고 이리 안하무인 격으로 굴다니, 이러고도 무사할 성싶으냐!”

“아마 무사할 것 같은데요.”

“이, 이놈이!”

“계속 이러시면 우리 각주님께서 직접 내려오셔서 이놈! 하십니다.”

뭐 이런 놈이 다 있지?

흑혈도는 물론, 이 광경을 지켜보던 사람들까지 입을 딱 벌렸다.

흑혈도는 거친 낭인 세계에서도 알아주는 강자.

지랄 맞은 성격만 아니라면 당장 일문(一門)의 문주가 되어도 중견 문파로 키워 낼 수 있을 거라는 게 세간의 평이었다.

그런데도 혁무진은 그가 뿜어내는 기파 앞에서도 눈 하나 깜빡하지 않았다.

“탈락입니다. 가십쇼.”

하지만 어떻게 보면 진태경을 따라다니며 온갖 매운맛을 겪은 혁무진으로서는 당연한 일이었다.

그의 무덤덤한 모습에 지랄 맞은 성격을 가진 흑혈도마저 할 말을 잃은 그 순간이었다.

“으하! 으하하하!”

드드드득!

어디선가 터져 나온 앙천대소에 공기가 터져 나가고 지면이 잘게 흔들린다.

주위를 짓누르는 엄청난 기파의 주인을 확인한 절정 고수들의 얼굴이 딱딱하게 굳었다.

‘엄청난 공력……!’

‘나보다 한 수. 아니 두 수 위.’

‘이, 이게 도대체.’

경악이 가득 담긴 시선들이 향한 곳에는, 조금 전만 해도 한가로이 술잔을 기울이던 노인이 천천히 자리에서 일어나고 있었다.

“너무 소란 떨지 말게. 자네들은 주인장이 불쌍하지도 않나.”

엎드린 채 벌벌 떠는 객잔 주인을 향해 부드럽게 웃는 노인을 바라보던 시선들 속, 누군가의 비명 같은 외침이 튀어나왔다.

“이, 일양노(一陽老)!”

일양노. 그 세 글자면 족했다.

한 시대를 풍미했던 정사지간의 고수. 강대한 열양지기로 자신에게 맞서는 숱한 적들을 태워 죽였던 괴물의 별호가 바로 일양노다.

이처럼 난데없는 초절정 고수의 등장에, 좌중이 삽시간에 얼어붙었다.

‘진정 일양노란 말인가?’

‘저, 저 노괴가 어찌 이곳에…….’

이 자리의 누구도 일양노의 이름에 비견될 수는 없다. 아니, 모두가 합공을 가해도 쓰러트릴 수 있을지조차 의문이었다.

불과 단 하나의 벽. 하지만 절정과 초절정의 격차는 그토록 멀고도 아득한 것이었다.

저벅저벅.

침묵 속에서 느긋하게 걸음을 옮긴 일양노가 혁무진을 응시하며 웃었다.

“가서 전하게. 이 늙은이가 뵙고자 청한다고.”

“……!”

다시 한번 잔잔한 충격이 주위를 휩쓸었다. 다른 사람도 아닌 일양노다.

거칠 것 없는 초절정 고수인 그가 핏덩이나 다름없는 이룡각주의 밑에 들어온다는 것만으로도 놀라운데, 저토록 정중한 태도를 보이다니.

“아, 알겠습니다. 잠시만 기다려 주십시오.”

당황 섞인 대답과 함께 돌아선 혁무진은 보지 못했다. 일양노의 눈빛에 어린 불길한 열기를.

‘열화문. 열화문이라. 허허. 이 늙은이에게도 마침내 기회가 오는구나.’

열화신룡 진태경? 그를 둘러싼 소문의 진위 여부는 상관없다.

그래 봤자 고작 약관을 넘긴 어린놈. 이 나이에 그런 핏덩이를 상관으로 깍듯이 모실 생각 역시 추호도 없었다. 다만…….

‘대대로 한 사람에게만 전승된다는 열화문의 신공(神功). 그것만은 반드시 노부의 것으로 만들고 말리라.’

평생 강자가 되기 위해 살아왔건만, 열양지기의 극에는 도달하지 못한 열양노였다.

그러나 열화문의 무공이 있다면 가능하다. 천하제일(天下第一)이라는 이름 역시 가질 수 있었다.

‘믿을 만한 소문에 따르면 화왕 적천강은 이룡각에 들어가지 않는다고 했지. 그럼 남은 것은 어린 제자와 다른 떨거지들뿐.’

이룡각이 임무를 하달받아 하남을 벗어나는 그때가 바로 천기(天氣)다.

암천? 무림맹? 천하 무림의 운명이 어찌 되건 무슨 상관인가. 검버섯이 가득한 입가가 씰룩거렸다.

“허허. 허허허.”

일양노의 눈앞에는, 이미 천하제일인(天下第一人)이라는 다섯 글자가 어른거리고 있었다.



* * *



나이 여든다섯.

이름은 원철.

별호는 일양노. 무공은 초절정.

그야말로 완벽에 가까운, 어느 것 하나 흠잡을 것 없는 프로필이다.

하지만 갑작스럽게 모시게 된 특별 심사위원의 생각은 달랐다.

“눈빛이 딱, 기회만 오면 뒤통수칠 호로 새끼 같은데.”

“예?”

되물을 필요도 없었다.

한마디만 툭 던진 적천강이 이미 공간을 좁혀 일양노의 아구창을 후려갈기고 있었으니까.

후우웅!

막아서는 모든 것을 잿더미로 만들어버릴 극양의 기운.

헛숨을 삼킨 일양노가 황급히 두 팔을 교차시켰지만, 힘의 차이는 극명했다.

‘저러면 안 되는데.’

열양지기에도 급이 있는 법이다.

일양노가 평범한 화염이라면, 화왕 적천강이 지닌 기운은 용암. 그러한 극명한 힘의 차이는 한순간에 드러났다.

우득. 뻑!

뼈가 아작 나는 소리와 함께 일양노의 눈동자가 힘없이 풀린다.

그 광경을 바라보던 나는 안타까운 마음을 담아 외쳤다.

“안 돼. 에이스으-!”

하지만 한번 불을 뿜기 시작한 적천강의 주먹은 쉬지 않았다.

뻑! 뻐벅! 뻐버버벅!

팔, 다리, 배, 등, 얼굴.

되찾은 청춘을 과시하듯 옹골찬 기운이 담긴 일권이 전신 곳곳을 야무지게 후드려 팬다.

그럴 때마다 유형화된 열양지기가 주위를 감쌌다.

‘와, 저 불구덩이를 여기서 보네.’

이 오디션 장르가 힙합이었나.

목걸이를 받지 못한 원썬, 아니 일양노는 반격 한 번 제대로 못 하고 정신을 잃었다.

털썩.

바스라지는 재처럼 쓰러진 일양노를 가만히 내려다보던 적천강이 문득 중얼거렸다.

“생각났다, 이놈. 일전에 본문의 무공을 노린다고 했던 그 육시랄 놈이다.”

“……이유가 있으니 그나마 다행이네요. 전 노야가 미쳐 버린 줄 알았습니다.”

“나중에라도 알았느니 됐다. 꼴도 보기 싫으니 눈앞에서 치워라.”

일양노의 시신, 아니 몸뚱어리가 실려 나간 지 얼마 되지 않아 바깥이 시끄러워졌다.

슬쩍 창밖을 내다보니 공포에 질린 지원자들이 신법까지 발휘해 가며 도망치는 중이다.

“……아니, 시발.”

이게 어떻게 마련된 자린데. 오디션 개망했네. 진짜.

내 원망 어린 눈빛을 받은 적천강이 퉁명스럽게 대꾸했다.

“뭐 어쩌라고.”

“좀 살살하시지 그러셨어요. 무공 좀 탐내는 게 죽을죄는 아니잖아요. 아직 뭔 짓을 한 것도 아니고. 조용히 탈락만 시키면 되는 건데.”

“쯧쯧. 순진한 녀석 같으니. 저런 놈들은 꼭 일을 치기 마련이다. 불씨는 미리미리 밟아 놔야지.”

“……보통은 잡초를 뿌리 뽑는다고 하지 않습니까?”

“잡초는 놔둬도 그만이지만, 불씨는 산을 태우는 법이니라.”

아니, 무슨 산림 보호 협회 회장도 아니고.

어이가 없어진 내심 중얼거리던 바로 그때였다.

“그리고…….”

“또 뭐요.”

적천강이 창밖을 향해 턱짓했다.

“가는 놈이 있으면, 오는 놈도 있는 법이다.”

“어?”
```

## Final English reading copy

```markdown
# Chapter 541

Henan was a land with a long and storied history.

It was home to sprawling thousand-year-old capitals such as Kaifeng and Luoyang, cities that had served as the seats of numerous dynasties. It also offered breathtaking natural scenery and all sorts of famous landmarks, including four great mountains.

As a result, people never stopped visiting throughout the year. Naturally, there were plenty of inns, pleasure houses, and other places for entertainment and lodging.

But the old innkeeper, whose family had run the same inn for three generations, could confidently say that the street had never once boiled over like this.

*What in the world…?*

The old innkeeper stared around in bewilderment.

What he saw was a truly enormous crowd—so large that it could only be described as a sea of people.

“Hey, wait a minute! Don’t try to cut in line!”

“Good grief, who keeps shoving me?”

“You little pup. You’ve been giving me insolent looks for a while now. Do I have to show you a coffin before you come to your senses?”

“What did you say? I was willing to let it go, but this lowly wandering martial artist is—”

“Heh heh. Everyone’s certainly full of energy. It’s a pleasant sight.”

“Pleasant? It’s been so noisy that I can hardly stand it.”

A wandering martial artist who looked like a wild wolf and a man who appeared to be the scion of a prestigious family glared sharply at each other.

The sight made a middle-aged man with half-white hair burst into hearty laughter, while a beautiful woman whose age was impossible to guess clicked her tongue.

And that was not all. Countless people stood farther away, watching them and whispering among themselves.

*What on earth is going on here?*

In the middle of the chaos, just as the innkeeper felt his soul halfway leaving his body, a voice reached his ears.

“There’s no need to worry so much.”

“Pardon?”

“Not over there. This way.”

The innkeeper turned around in surprise and saw a person sitting at a table, leisurely sipping from a wine cup.

Unlike everyone else, who had been standing in a long line, this old man had claimed a seat and seemed completely at ease.

“They all know better, so there won’t be any serious trouble.”

He was small in stature, with a wild white beard and a face flushed red with drink.

For a moment, the innkeeper wondered if he might be a martial artist. But at first glance, he was nothing more than an utterly ordinary drunken old man.

The innkeeper discreetly looked him over, then whispered in a lowered voice.

“W-What in the world is going on?”

“They’re all people who want to begin their era of success. You must have heard that song, too. ‘Join the Murim Alliance’s Two Dragons Pavilion, and—’”

The old man began humming a lively tune.

The innkeeper’s shoulders instinctively began to sway. Then his eyes widened.

“Ah. Are you talking about that… Two Dragons Pavilion?”

“You got it in one. The young Pavilion Master of that Two Dragons Pavilion is staying right here.”

“Good heavens.”

The innkeeper let out a short gasp.

He had known that the person staying in the detached building was a young knight-errant famous throughout the martial world. But he had never imagined that he was the Pavilion Master of the Two Dragons Pavilion everyone was talking about.

“So that’s why so many martial artists have come here. But even so, I never imagined there would be this many…”

“Heh heh. Isn’t it a fine opportunity? It’s rare to find a place that doesn’t care about your background, gender, or age.”

“That’s true. I heard even an eighty-year-old can apply.”

The old man quietly answered.

“As it happens, that’s exactly what I intend to do.”

“Hahaha! You certainly know how to make a joke.”

“Does that sound like a joke?”

“Pardon?”

“I asked whether that sounded like a joke.”

The laughter stopped at once.

The innkeeper stared at the old man with trembling eyes.

“Th-Then, Old Sir… I mean, Your Excellency is applying as well?”

“Isn’t that obvious?”

The old man wiped his beard, drenched in wine, with his sleeve.

At the same time, his robe shifted slightly, revealing a worn scabbard beneath it.

“I am a martial artist as well. Just like them. And unlike you.”

“Gasp.”

“There’s no need to be so frightened. This old man doesn’t lay a hand on commoners.”

After thinking for a moment, the old man added in a low voice.

“Most of the time, anyway.”

“……!”

Not a trace of drunkenness remained in his gentle voice.

For an instant, his eyes flashed with the ferocity of a wild beast.

The innkeeper felt a chill run through him and unconsciously took a step backward.

That was when he heard someone coming down the stairs.

Thud. Thud.

The sound of approaching footsteps.

The old man’s eyes flashed.

“Is it about to begin?”

The old man was not the only one who had reached that conclusion.

The dozens of Peak masters waiting in the long line and the spectators who seemed to number ten times as many all fell silent.

In the silence that descended in an instant, someone appeared.

“How many people have come— Oh my, that startled me.”

A young man jumped in surprise.

When everyone realized that it was Hyuk Mujin, a trace of disappointment passed over their faces.

But the Peak masters, who had sensed his aura long before he appeared, merely muttered calmly.

“He’s not the Blazing Flame Divine Dragon.”

“He sent a messenger down in his place. Is he already throwing his weight around?”

“He’s quite impressive for a messenger. With that kind of aura at his age, he’s better than most second-generation Disciples from prestigious sects.”

“I agree. And if it’s the Blazing Flame Divine Dragon, I suppose that’s possible.”

Voices drifted in from every direction.

Hyuk Mujin looked sourly at the enormous crowd murmuring around him and cleared his throat.

“Ahem. I was ordered by the Captain—I mean, the Pavilion Master—to begin the interviews. Therefore, I will call each person by name from this point onward. Please follow me one at a time in the designated order.”

Reaching the Peak realm meant being recognized as a master anywhere in Murim.

The Peak masters all took pride in their abilities. They clearly disliked being told they would have to wait again, but none of them complained beyond that.

A thirsty man had to dig his own well. Since they had come here, this was something they had to endure.

“I understand perfectly well, so stop spouting nonsense and call the names already.”

Hyuk Mujin’s eyes widened at the rough-looking middle-aged wandering martial artist’s words.

“Oh. It’s true.”

“What is?”

“Ah, it’s nothing. The Pavilion Master told me to reject anyone who uses informal speech and acts rudely the first time they meet someone, no exceptions. I didn’t expect to find someone so quickly.”

“……What?”

“Let’s see. You’re Great Hero No Guisan, the Black Blood Saber, correct? You may go home now.”

The middle-aged wandering martial artist, the Black Blood Saber, blinked at him in silence.

Then he roared.

“What kind of bullshit rule is that?”

Hyuk Mujin pulled a bamboo slip bearing the Black Blood Saber’s personal details from the purse at his waist and nodded.

“It’s right here. That kind of rule.”

“I waited for an entire shichen!”

“Oh dear. That’s unfortunate.”

“You insolent little bastard! You’re relying on your master and behaving this arrogantly. Do you really think you’ll be safe after this?”

“I think I’ll probably be fine.”

“You little—!”

“If you keep this up, our Pavilion Master will come down himself and say, ‘You bastard!’”

What kind of person was this?

The Black Blood Saber and everyone watching the spectacle stood with their mouths hanging open.

The Black Blood Saber was a renowned powerhouse even among the rough-and-tumble world of wandering martial artists.

People said that if not for his foul temper, he could become the Sect Leader of a school that very day and build it into a mid-level sect.

Yet Hyuk Mujin did not even blink before the aura he released.

“You’re rejected. Off you go.”

But for Hyuk Mujin, who had followed Jin Taekyung around and experienced every kind of hell, this was only natural.

Even the foul-tempered Black Blood Saber was left speechless by Hyuk Mujin’s composure.

That was when—

“Ha! Hahaha!”

Rumble, rumble!

A thunderous laugh erupted from somewhere.

The air seemed to burst, and the ground trembled in tiny, violent shudders.

The Peak masters who sensed the owner of the overwhelming aura pressing down on the surroundings went rigid.

*What incredible internal energy…!*

*One level above me. No—two levels.*

*What in the world…?*

Every horrified gaze turned toward the old man who, only moments earlier, had been leisurely sipping his wine.

He was slowly rising from his seat.

“Don’t make such a commotion. Don’t you feel sorry for the innkeeper?”

The old man smiled gently at the innkeeper, who was lying facedown and trembling.

As everyone stared at him, a cry like a scream burst from somewhere in the crowd.

“T-The Old Man Ilyang!”

Old Man Ilyang.

Those three words were enough.

He was a master between the orthodox and unorthodox paths who had once dominated an entire era. His sobriquet belonged to a monster who had burned countless opponents to death with his mighty Scorching Yang Qi.

The sudden appearance of such a Supreme Peak master froze the entire gathering in an instant.

*Is that truly Old Man Ilyang?*

*Th-That old monster… What is he doing here?*

No one present could compare to Old Man Ilyang.

No—given the difference between Peak and Supreme Peak, it was questionable whether they could bring him down even if they joined forces.

It was only one wall.

But the gap between Peak and Supreme Peak was that vast and distant.

Step. Step.

Old Man Ilyang leisurely walked through the silence, then looked at Hyuk Mujin and smiled.

“Go and tell him that this old man wishes to meet him.”

“……!”

A second quiet shock swept through the surroundings.

It was Old Man Ilyang, of all people.

It was astonishing enough that such an unrestrained Supreme Peak master would seek to join the Two Dragons Pavilion under someone who was barely more than a boy.

Yet he was behaving with such courtesy.

“U-Understood. Please wait a moment.”

Hyuk Mujin turned away with a flustered answer.

He did not see the ominous heat burning in Old Man Ilyang’s eyes.

*The Fire Gate Clan. The Fire Gate Clan, huh? Heh heh. At long last, an opportunity has come even to this old man.*

Blazing Flame Divine Dragon Jin Taekyung?

The truth behind the rumors surrounding him was irrelevant.

He was still nothing more than a young brat barely past twenty. Old Man Ilyang had no intention whatsoever of respectfully serving such a fledgling as his superior at his age.

However…

*The Fire Gate Clan’s divine technique, passed down to only one person in each generation. That alone will become mine, no matter what.*

He had spent his entire life pursuing strength, yet he had never reached the pinnacle of Scorching Yang Qi.

But if he obtained the Fire Gate Clan’s martial arts, it would be possible.

He could even claim the title of the greatest under heaven.

*According to reliable rumors, Fire King Jeok Cheongang has no intention of joining the Two Dragons Pavilion. Then all that remains is his young Disciple and a few other riffraff.*

The moment the Two Dragons Pavilion received a mission and left Henan would be his chance.

Dark Heaven? The Murim Alliance?

What did it matter what became of the martial world’s fate?

The corner of his mouth, covered in age spots, twitched.

“Heh heh. Hahaha.”

Before Old Man Ilyang’s eyes, the five characters meaning *greatest under heaven* were already shimmering.

* * *

Eighty-five years old.

His name was Won Cheol.

His sobriquet was Old Man Ilyang.

His martial arts realm was Supreme Peak.

It was practically a perfect profile. There was not a single thing to criticize.

But the special judge he had suddenly found himself facing had a different opinion.

“Those eyes are exactly the kind that belong to a bastard who’d stab you in the back the second an opportunity arose.”

“Pardon?”

There was no need to ask what he meant.

Jeok Cheongang had already closed the distance and was smashing his fist into Old Man Ilyang’s mouth.

Whoosh!

A surge of Extreme Yang energy that would turn everything in its path to ash.

Old Man Ilyang sucked in a sharp breath and hurriedly crossed both arms in front of himself, but the difference in strength was obvious.

*That’s bad.*

Even Scorching Yang Qi had different levels.

If Old Man Ilyang’s qi was an ordinary flame, the qi possessed by Fire King Jeok Cheongang was lava.

The vast difference in power revealed itself in an instant.

Crunch. Wham!

As the sound of bones being shattered rang out, Old Man Ilyang’s eyes went limp.

Watching the scene, I shouted with genuine concern.

“No! The ace—!”

But once Jeok Cheongang’s fist began spitting fire, it did not stop.

Wham! Wham! Wham-wham-wham!

Arms, legs, stomach, back, face.

As though showing off his regained youth, Jeok Cheongang’s powerful strikes, packed with vigorous qi, pounded every part of Old Man Ilyang’s body.

Each time, tangible Scorching Yang Qi wrapped around them.

*Wow. I get to see a fire pit right here.*

Was this audition genre hip-hop?

One Sun—no, Old Man Ilyang, who had not even received a necklace, lost consciousness without managing a single proper counterattack.

Thud.

Jeok Cheongang stood quietly over Old Man Ilyang, who had collapsed like crumbling ash.

Then he suddenly muttered.

“Now I remember, you bastard. You’re that son of a bitch who said he was after our sect’s martial arts.”

“……It’s a relief that there was at least a reason. I thought you’d gone mad, Old Master.”

“Better late than never. I can’t stand the sight of him, so get him out of here.”

Not long after Old Man Ilyang’s corpse—or rather, his body—was carried away, the area outside grew noisy.

I glanced out the window.

Applicants were fleeing in terror, even using their movement techniques to get away.

“……Oh, for fuck’s sake.”

How much effort had gone into arranging this?

The audition was completely fucked. Seriously.

Jeok Cheongang answered my resentful stare bluntly.

“What do you want me to do?”

“You could’ve gone a little easier on him. Wanting to get his hands on some martial arts isn’t a capital crime. He hadn’t actually done anything yet. You could’ve just rejected him quietly.”

“Tsk, tsk. What an innocent fool. People like that always cause trouble eventually. You have to stamp out a spark before it becomes a fire.”

“……Don’t people usually say you should uproot weeds?”

“Weeds can be left alone, but a spark can burn down a mountain.”

I mean, what was he, the chairman of a forest conservation society?

I was muttering inwardly in disbelief when Jeok Cheongang continued.

“And…”

“What now?”

Jeok Cheongang jerked his chin toward the window.

“When someone leaves, someone else comes.”

“Huh?”
```
