<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0476.txt",
      "sha256": "30fd27c91e53f2b0dd7b2315933b5d36a5b0d0ea97c4afd890301bb6357f9980",
      "bytes": 13607
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "180b6c7b22c4013036b1f5e0f1a54697bb5e792a42ced7cc81666e064c898d15",
      "bytes": 3161
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b4ec97582d1eaf6caf8a6643afcf334ebe239d11b66d53789340e994e21a3411",
      "bytes": 153122
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "d4d5936913665d8cfe7536d226b56febb0bcadff1b3c64093e939fe9f2685ea9",
      "bytes": 803
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "afba413819c7beb7a884378b0fdf43986b2ba29203697c4bda00d31cbfdecf2b",
      "bytes": 1006
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "1e00144d37600d3c30a42e16d6a34d9da353367e7d6a8d6ef45b45fd66780876",
      "bytes": 553
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "1f4a6f40afa560d7adaec8574c6a5a237f803cb526d45969e2c0b2fd60afb57b",
      "bytes": 1542
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "2ff06ea07e00b7bb56d1c125bc9851071664f96abf5f7a1ed3ade6f88788ea30",
      "bytes": 1720
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "49543f104bcee1b7b82d9ef083414c74979ce6482d328d1049369155d11c73b5",
      "bytes": 622
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "19b7f64f3fea668d794dd86fa883c5918ee9d964900b26a0ccfd75e164dac1ba",
      "bytes": 771
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "bb882cf37f97b20509363dde65c544ab530ac7be2754709b99da838a8410a1ae",
      "bytes": 147867
    }
  ],
  "estimated_tokens": 12403
}
-->

# Durable State Update — Chapter 476

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 476. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 476. Profile updates may replace only one
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
  "chapter": 476,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 476,
    "continuity_sources": [476],
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
    "Taekyung's forced System Quest, Corrupted Spirit Beast, remains active with Logout disabled and the Mutated Water God Dragon as its target.",
    "The Water God Dragon was once a noble spirit beast awaiting ascension before an unknown power corrupted it into an evil beast.",
    "The battle remains active: Taekyung destroyed one eye, tore out every whisker, ripped away many scales with his bare hands, and has now met the dragon's Water Breath with Heavenly Strike.",
    "The dragon's Berserk Status increases all abilities but clouds combat judgment, and its rampage continues.",
    "Taekyung possesses the Heavenly Martial Physique, giving him superhuman physical strength independent of his accumulated internal energy and martial enlightenment.",
    "The dragon's scales are so durable that early Peak Sword Energy cannot properly cut them; Force is normally required to split them and damage what lies beneath.",
    "Cheongpung remains resistant to Fear and fights with the Zaha Divine Technique; Mungyeong remains partially affected by Fear but continues fighting as the former Slaughter Saint.",
    "The dragon possesses extreme speed, immense durability, black scales, and centuries of accumulated qi.",
    "The dragon's anger manifests as violent storms, lightning, swollen river whirlpools, and other responses from the surrounding water and weather.",
    "The dragon's black pupils accompany Breath: it forms massive water spheres, can fire them repeatedly in rapid succession, and has now shown a corresponding increase in physical strength.",
    "Zhuge Feng remains under cover protecting the others, and the severely injured Dongting Fisherman remains alive for interrogation about Dark Heaven.",
    "An unidentified figure remains on the dragon's head and can tear out its whiskers barehanded."
  ],
  "continuity_sources": [
    475,
    474
  ],
  "open_questions": [
    "What is the Dongting Fisherman's exact role within Dark Heaven, and how was he connected to the earlier destruction inside the secret refuge?",
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Did the Mutated Water God Dragon destroy Donghu Stronghold and the related Yangtze River Channel League strongholds, and why was no Moving Formation trace left?",
    "What unknown power corrupted the Water God Dragon, and is it related to the black pupils and sudden increase in power?",
    "Who is the unidentified figure hanging from the dragon's head, and why can that figure tear out its whiskers barehanded?"
  ],
  "safe_through": 475,
  "temporary_decisions": [
    "Render 광폭화 as Berserk and preserve the System Status distinction.",
    "Render 활어회 as live-fish sashimi and 세꼬시 as bone-in sashimi with an explanatory footnote.",
    "Preserve Taekyung's profane, improvisational combat humor and Jin-ho's deliberately absurd USB-related saying.",
    "Continue rendering 수염 as whiskers and distinguish the dragon's anomalous qi from Force and Sword Energy.",
    "Retain jang and geun measurements."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 살성     | **Slaughter Saint**           | —              |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 제자     | **Disciple**                                 |
| 은인     | **Benefactor**                               |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 탱커      | **tank**              |
| 힐러      | **healer**            |
| 대격변     | **Great Cataclysm**   |
| 노부      | **this old man / I**                                            |
| 대사      | **Master** for a senior Buddhist monk                           |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 트롤 | **Troll** | Monster species with extraordinary regenerative ability. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 노환 | **infirmities of old age** | Jeok Cheongang's age-related illness. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 브레스 | **Breath** | Dragonkin power used by the Wyverns. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 상인 | 적천강 | merchant_to_legendary_martial_master | Great Hero Jeok | deferential and flattering | Praises Jeok Cheongang while presenting the Poison-Averting Ring and requesting help. |
| 적천강 | 상인 | legendary_guest_to_merchant | you | blunt and transactional | Cuts off the merchant’s praise, asks his identity and origin, and accepts the gift without committing to the requested favor. |
| 상인 | 청년 | stranger_to_stranger | Young Brother | formal-polite | A merchant uses 소형제 after noticing the young man's sword, and the young man approves of the address. |
| 청년 | 상인 | stranger_to_stranger | friend | casual and shameless | The young man declares that they should be friends after drinking their Yeoahong. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 혈주 | 청풍 | hostile_opponent_to_newly_revealed_identity | Huashan's Invincible Divine Sword; Sword Saint's Disciple or grandson | mocking and taunting | Recognizes Cheongpung's public identity and needles him with his Sword Saint lineage while dismissing the added threat. |
| 진태경 | 문경 | young_martial_artist_to_medical_apprentice | Young Hero | formal-polite | Taekyung addresses the non-martial Mungyeong as 소협 while praising his actions. |
| 문경 | 진태경 | young_passenger_to_younger_martial_artist | Young Hero | deferential | Mungyeong uses 소협 while asking Taekyung for help boarding the ship. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 청풍 | 미미 | handler_to_companion_snake | Mimi | cheerful-commanding | Cheongpung repeatedly calls and commands the Thousand-Year Poison Horned Snake. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 힐러 | 진태경 | healer addressing the rescuer who stabilized the survivor | sir | deferential and grateful | The healer thanks Jin as 선생님 after witnessing his rescue and treatment. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 진태경 | 미미 | rescuer to companion snake | Mimi or Mimi-chan | informal, pleading | Taekyung calls to Mimi while asking the snake to carry him and the survivors. |
| 진태경 | 수신룡 | hostile martial artist to monster | you, sibu-leol eel bastard | blunt, insulting, and fearless | Taekyung directly insults the emerged Water God Dragon before attacking it. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 442
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who seeks Jin Taekyung, Cheongpung, and Jeok Cheongang after escaping the confrontation at Mount Song.
- **Personality:** Calm, confident, theatrically frivolous, casually cruel, and ruthlessly destructive; treats allies as disposable tools and enjoys provoking stronger opponents.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He and the Western Heaven Demon Lord serve the same master; he now seeks to personally kill Cheongpung, Jeok Cheongang, and Jin Taekyung, while his former contact Han Su is dead.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 475
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 475
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 475
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin and Furnace Fire Pure Blue, and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, and pathologically afraid of water. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 475
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, and is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 475
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 475
- **Aliases:** None
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, having passed the Divine Physician title to his Disciple, and he has reached the Returned to Youth realm.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple; Jeok Cheongang is an old acquaintance, and Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

## Korean source

```text
＃476화



언제쯤이었더라.

이제는 제목도 기억나지 않는 케케묵은 고전 무협 영화에서 그런 대사를 봤다.

무공은 오직 수직과 수평이라고. 상대와 나, 둘 중 누군가는 쓰러지고 다른 하나는 서 있는 것이 싸움의 끝이라고.

맞는 말이다. 내가 지금껏 무림에서 치른 수많은 전투의 결과 역시 항상 두 가지 중 하나였다.

‘쓰러트리거나, 쓰러지거나.’

팔 하나를 잃으면서까지 도망친 혈주(血主)를 제외하면 결과는 늘 양자택일이었고, 쓰러지는 것은 언제나 내가 아닌 상대였다.

하지만 변이된 수신룡에게 매달린 채로 깊은 강물에 빠졌을 때, 나는 잠시 잊고 있던 또 다른 결과의 가능성을 떠올렸다.

‘만약 이놈이 도망친다면?’

사실상 수백 년간 동정호와 장강의 주인이나 다름없었던 녀석이다.

똥개도 제 앞마당에서는 반은 먹고 들어간다는데, 놈이 도망치고자 마음먹는다면 나로서도 막을 수 없었다.

동시에 깨달았다. 한동안 큰 착각에 빠져 있었다는 사실을.

‘전투가 아니라, 사냥이었어야 했어.’

이건 무인 대 무인의 생사결(生死結)이 아니다.

눈앞의 괴물을 쓰러트리기 위해서는 수단과 방법을 가리지 않고 무엇이든지 해야 했다.

꼬박 7년 동안을 사냥꾼으로 살아왔는데, 나도 모르는 사이에 고지식한 무인 흉내를 내고 있었다니. 내심 실소를 터트리지 않을 수 없었다.

‘멍청한 짓거리를 했어.’

헌터와 무림인. 무림인과 헌터.

두 가지 모두 내가 지닌 정체성이다. 유일무이(唯一無二)한 현대의 무림인이자, 무림의 헌터.

나는 어느덧 흐릿하게 지워진 경계선에서 다시금 그 사실을 되새겼다.

‘그래, 이거지.’

아주 오랜 잠에서 새롭게 깨어난 듯한 기분. 가볍게 뭍으로 착지한 나는 천둥 같은 외침을 토해 냈다.

“공격 대형, 갖춰!”

“……!”

“……!”

“……!”

한순간에 뒤바뀐 공기의 흐름에, 세 사람의 눈이 크게 뜨였다. 그중에서도 파르르 떨리는 눈빛으로 나를 응시하던 적천강과 문경이 입을 열었다.

“오냐오냐했더니, 아직 대가리에 피도 안 마른 새파란 놈이 노부에게 말을 까?”

“화왕이 제자 교육을 개판으로 시켰군.”

“……죄송합니다. 저도 모르게 그만.”

깜빡했다. 이 자리에 있는 사람들이 누구인지.

순간적으로 분위기를 너무 타는 바람에 정신이 나갔던 모양이다.

그나마 눈에 쌍심지를 켠 두 노인과는 달리 청풍은 열렬하게 호응해주었다.

“은인, 완전 멋있어요! 미미! 공격 대형 갖춰!”

취릭!

“노부가 천지신명께 맹세하건대, 언젠가는 반드시 저 뱀 새끼로 술을 담가 버릴…….”

적천강의 맹세는 이어지지 못했다.

출렁이는 물결 위로 어른거리던 거대한 그림자가 마침내 수면을 터트리며 모습을 드러냈기 때문이었다.

- 크라아아아!

그 어느 때보다 흉포한 괴성이 천지를 울린다.

작은 산과 같은 거체에서 폭발하듯 터져 나온 막강한 기운이 사방을 짓누르고, 발산된 피어(Fear)에 대기가 흔들렸다.

그 모든 것의 중심에는 수십여 장 위, 까마득한 상공에서 우리를 굽어보는 새카만 동공이 있었다.

한 톨의 빛도 존재하지 않는 캄캄한 암흑으로 이루어진 외눈이 빛나자, 누군가의 입술 사이로 신음이 흘러나왔다.

“으음……!”

미지에 대한 공포.

나와 청풍을 제외한 다른 사람들은 변이된 수신룡이 내뿜는 피어의 영향에서 완전히 자유롭지 못하다.

그것이 설령 천하에서 손에 꼽히는 초절정 고수라고 해도 마찬가지다.

하지만…….

‘내가 있지.’

몬스터라면 지긋지긋하게 상대해 본 베테랑 헌터. 그게 바로 나다.

썩은 살덩이를 주렁주렁 매달고 달려드는 수만의 언데드 군단과도 흔들림 없이 맞서 싸웠는데, 항공모함 크기의 뱀장어쯤 하나 추가된다고 해서 두려움에 벌벌 떨 이유가 없다.

“다시 보니까 선녀 같네.”

중얼거리기 무섭게 뒤통수가 따가워진다. 듣는 사람 입장에서는 이게 웬 미친 소리냐 싶겠지.

하지만 방금 했던 말은 순도 100%의 진심이다.

‘놈이 강력한 존재인 것은 사실이지만, 아크 리치는 이보다 훨씬 더 까다롭고 강했어.’

그때 스켈레톤 킹의 도움이 없었다면 나는 필시 죽었을 거다.

하지만 중요한 것은 결국 살아남아 놈을 쓰러트렸다는 것이고, 아크 리치를 상대했을 당시 느꼈던 두려움은 경험이 되어 고스란히 내 몸과 마음에 아로새겨졌다.

‘그리고 나는 빨리 배우는 편이지.’

좋은 경험도, 좋지 않은 경험도 피와 살이 되기 마련이다. 지난 7년간, 나는 그렇게 살아남는 법을 익혔고 승리하는 방법을 배웠다.

흐읍. 크게 심호흡함과 동시에 백염의 창대를 높이 들어 올렸다.

곧이어 힘차게 내리찍은 창대의 끝에는 미증유의 공력이 실려 있었다.

쿠우웅-!

굉음과 함께 뻗어 나간 기의 파동이 놈이 발산하는 피어를 밀어 낸다.

마치 보이지 않는 유리창이 깨진 것처럼, 빈틈없이 주위를 에워싸고 있던 묵직한 중압감이 해소되었다.

“이건.”

“네 녀석…….”

적천강과 문경의 놀란 눈빛이 얼굴에 닿는다. 나는 놈을 똑바로 직시하며 입을 열었다.

“첫 번째. 괜히 쫄지 말 것.”

“……!”

“……!”

사람은 누구나 마음속에 크고 작은 두려움을 품고 있고, 피어는 그 두려움을 자극시켜 공포를 느끼게끔 만드는 기운이다.

그러나 두려움을 지운다면 비로소 잊고 있던 사실을 깨닫게 된다.

- 크르르르르.

낮은 울음소리를 흘리는 저 거대한 괴물이, 생각했던 것만큼 강하고 두려운 존재가 아니라는 사실을.

나는 칠흑빛으로 번들거리는 동공을 똑바로 응시하며 말을 이었다.

“둘째. 지금부터 제 지시에 따라, 저 새끼를 인정사정없이 조질 것.”

문경의 메마른 목소리가 귓가를 파고들었다.

“과정은 별로 마음에 안 들지만, 결과는 제법 듣기 좋군.”

“그래서 싫으신 건 아니죠?”

“내가 누구라 생각하느냐?”

“제가 멍청한 질문을 했네요.”

살성(殺星). 아득한 무림의 역사에서도 최고라 불리는 고금제일의 살수.

무슨 수를 써서라도 표적을 제거하는 살수에게 과정은 중요하지 않다. 오직 결과뿐이다.

“노야.”

“노부가 기억하기로 저런 악물(惡物)을 상대하는 법을 가르쳐 준 적은 없는 것 같은데…… 우선 저놈을 끝장낸 후에 듣도록 하마.”

츠츠츠!

적천강의 퉁명스러운 목소리에 이어 청풍이 자줏빛 검강으로 대답을 대신했다.

힐러도, 탱커도 없이 오직 딜러들로만 이루어진 극악의 조합이지만 이렇게 강력한 레이드 팀도 없을 거다.

‘초절정 고수가 자그마치 넷이라.’

별 다섯 개짜리 장수 돌침대도 울고 갈 만한 조합.

변이된 수신룡의 거체에 비하면 개미나 다름없는 존재지만, 한 사람 한 사람의 몸 안에는 미증유의 힘을 품은 거인이 웅크리고 있다.

그리고 이제, 네 명의 거인은 거대한 괴물을 사냥할 것이다.

“넌 이제 뒈졌어.”

마치 내 말을 알아들은 것처럼, 변이된 수신룡은 수면 아래 감춰 두었던 자신의 거대한 몸뚱어리를 일으켜 세우며 포효했다.

- 구워어어어어!

쿠르릉, 콰아아아아!

단 한 번, 포효를 내지른 것만으로 수십 개의 용오름이 솟아오르며 우리를 향해 덮쳐 온다. 그 사이로 걸레짝이 된 놈의 아가리가 쩍 벌어졌다.

고오오오옹-!

처음보다 더욱 빠르고 강하게 진동하는 대기.

그러나 세 번째 워터 브레스가 형태를 갖추기도 전에, 내 입술 사이로 뛰쳐나온 외침이 비바람을 뚫고 모두의 귓가를 파고들었다.

“산개(散開)!”

쉬쉬쉬쉬쉭!

약속이라도 한 것처럼 사방을 점하며 각기 쏘아지는 네 개의 신형.

바야흐로, 사냥의 시간이었다.



* * *



레이드(Raid).

비현실이 현실을 침범하고, 헌터와 몬스터가 서로를 향해 죽고 죽이는 싸움을 시작하자 판타지 게임 속에서만 통용되던 이 단어는 세 살배기 어린아이도 아는 것이 되어 버렸다.

하지만 대격변으로부터 살아남은 수십억 명의 인류 중 누구도 짐작하지 못했을 것이다.

시간과 공간을 넘어선 또 다른 곳에서, 용을 닮은 어느 낯선 괴물을 상대로 레이드가 벌어지고 있으리라는 것을.

그리고 그 모든 일의 중심에 익숙한 얼굴이 끼어 있다는 사실을.

타탁, 쐐애애액!

흩날리는 돌조각을 밟으며 허공을 향해 쏘아지는 육중한 체구.

아슬아슬하게 스쳐 지나간 거대한 꼬리가 반쯤 무너진 절벽을 부수고 풍압을 일으킨다.

흩날리는 머리카락 사이로 청년, 진태경의 눈동자가 빛났다.

‘지금 저 꼬리를 벤다면…… 아니, 아니다.’

진태경은 본능적으로 창을 휘두르려는 손을 억제했다.

그는 이번 레이드에서 가장 중요한 부분을 정확히 알고 있었다.

변이된 수신룡의 도주를 차단하고, 최대한 뭍으로 유인한 다음 번개처럼 처치해야 한다.

그전에 맞받아쳐 타격을 입힌다면 오히려 괴물의 경각심을 깨울지도 모른다.

물론, 그 광경을 지켜보는 누군가의 생각은 조금 달랐다.

“저런 개썅호로……!”

말년에 겨우 얻은 제자를 이렇게 허무하게 잃을 수는 없다!

그러나 걸쭉한 욕설과 함께 괴물을 향해 일장을 내지르려던 적천강의 움직임은, 다음 순간 들려온 외침에 덜컥 멈췄다.

“노야!”

“……!”

화륵, 콰아아아!

황급히 선회한 열양지기가 애꿎은 지면을 불태웠다.

아주 잠깐 괴물의 칠흑빛 눈동자에 의아함이 스치더니, 이내 흉포한 맹수의 그것으로 변했다.

- 구워어어어!

후웅, 쾅!

괴성과 함께 빗자루처럼 지면을 쓸어 버리는 거대한 꼬리. 찰나의 순간 허공으로 도약하여 공격을 피한 적천강이 분통을 터트렸다.

“언제까지 물러나기만 하란 말이냐!”

꽈앙!

까마득한 상공 위, 전신으로 부딪쳐 오는 괴물의 몸통을 회피한 진태경이 대답했다.

“제가 신호한다니까요!”

“그러니까 그게 언제냐고!”

“아, 어련히 알아서 할 테니까 제발 똥 좀 그만 싸십쇼! 트롤 짓도 한두 번이지! 다른 사람들처럼 시키는 대로 하세요!”

“……!”

적천강의 눈빛이 파르르 떨렸다.

몇몇 괴상한 단어가 섞인 탓에 무슨 말을 하는지 정확히 이해하진 못했지만, 하나는 정확히 들었다.

‘똥? 노부가 똥을 싸고 있다고?’

안 그래도 얼마전까지 노환으로 벽에 똥칠하는 건 아닌가 걱정했었는데, 제자라고 생각한 놈이 저렇게 심한 말을 하다니.

충격에서 헤어나오지 못하는 적천강을 깨운 것은 이어진 진태경의 외침이었다.

“노야, 지금! 뒤로 삼십 장 후퇴! 청풍은 놈의 후방으로 이동, 문경은 측면으로!”

“네, 은인!”

“웃긴 놈이군. 뜻을 따르겠다는 거였지, 반말을 해도 된다는 뜻은 아니었는데.”

“아니 시벌, 소통 안 되는 원딜충 개극혐이네 진짜. 말 좀 들으라고!”

“……!”

순간 말문이 막힌 문경이 입을 꾹 다문 채 잠자코 시키는 대로 하는 것을 보자, 적천강의 기분이 약간 나아졌다.

‘그래, 그나마 노부한테는 노야라고 불러 주긴 하는구나.’

분명 화가 나야 정상인데, 옆집 개똥이 마냥 이름을 불리는 문경의 꼴을 보니 천강이라고 안 부른 것만으로도 감사할 지경이다.

동시에 별말 없이 움직이는 문경의 심정을 어느 정도 알 것 같았다.

‘뭐지, 이 묘한 기분은?’

뭐랄까, 지금의 진태경은 이상할 정도로 박력을 뿜어내고 있었다.

그리고 적천강이 느끼기에 그것은 초절정 고수가 지니는 위압감이나 풍모 따위가 아니었다.

이건 마치…….

‘백전노장. 그래, 딱 그런 느낌이다.’

일평생을 무인으로 살아온 적천강으로서는 관부와 연도 없고 병졸이었던 적도 없지만, 어째서인지 막 전장에 배치된 신병이 백전노장을 마주했을 때의 느낌을 알 것 같았다.

“허 참, 아무리 봐도 참으로 희한한 놈…….”

“야, 적천강! 정신 안 차리냐!”

“……!”

적천강의 눈가가 파르르 떨리던 그 순간, 미처 분노를 터트리기도 전에 그가 그토록 기다리던 한 마디가 울려 퍼졌다.

“지금, 쳐!”

쉬쉬쉬쉭!

어느덧 동정호의 물가를 벗어나 뭍에 오른 수신룡을 향해, 네 사람의 거인이 동시에 쏘아졌다.
```

## Final English reading copy

```markdown
# Chapter 476

When was it?

I once saw a line like that in an old wuxia film whose title I no longer remember.

“Martial arts are only vertical and horizontal. In the end, one of us falls and the other remains standing.”

It was true. The countless battles I had fought in the Murim had always ended in one of two ways.

*Either I knocked them down, or they knocked me down.*

Except for the Blood Lord, who had escaped even after losing an arm, the result had always been one or the other—and it had never been me who fell.

But when I plunged into the deep river while clinging to the Mutated Water God Dragon, I remembered another possibility I had temporarily forgotten.

*What if this bastard runs?*

He had effectively been the master of Dongting Lake and the Yangtze for hundreds of years.

They said even a mutt had half the battle won in its own yard. If the bastard decided to run, there was no way I could stop him.

At the same time, I realized that I had been laboring under a serious misconception.

*This shouldn’t have been a battle. It should have been a hunt.*

This was not a life-and-death duel between two martial artists.

To bring down the monster before me, I had to do whatever it took, without caring about the means.

I had lived as a Hunter for seven solid years, yet without realizing it, I had been pretending to be some hidebound martial artist. I couldn’t help letting out a quiet laugh at myself.

*What a stupid thing to do.*

Hunter and martial artist. Martial artist and Hunter.

Both were part of my identity. I was the one and only modern martial artist—and the Murim’s Hunter.

At the indistinct boundary that had nearly been erased, I reminded myself of that fact once more.

*That’s right. This is it.*

It felt like I had awakened from a very long sleep. I landed lightly on the shore and let out a thunderous shout.

“Form an attack formation!”

“……!”

“……!”

“……!”

The flow of the air changed in an instant, and three pairs of eyes widened. Of the three, Jeok Cheongang and Mungyeong stared at me with trembling eyes before speaking.

“I coddle you a little, and now a greenhorn still wet behind the ears dares speak to this old man like we’re equals?”

“The Fire King did a terrible job teaching his Disciple.”

“…I apologize. It slipped out.”

I’d forgotten who was standing here.

I must have lost my head after getting swept up in the moment.

Unlike the two old men glaring at me with sparks in their eyes, Cheongpung responded enthusiastically.

“Benefactor, that was so cool! Mimi! Form an attack formation!”

*Chirik!*

“I swear to heaven and earth that one day, I will turn that snake bastard into liquor—”

Jeok Cheongang’s oath never reached its conclusion.

The enormous shadow wavering across the rolling surface finally burst through the water and revealed itself.

—Kroaaaaaaaaah!

A more savage roar than any before shook heaven and earth.

Powerful qi exploded from the body as large as a small mountain, pressing down on everything around it. The air trembled beneath the Fear it released.

At the center of it all, dozens of *jang* above us in the distant sky, was a pitch-black pupil looking down at us.

When the single eye, formed from darkness without even a speck of light, gleamed, a groan escaped someone’s lips.

“Ugh…!”

Fear of the unknown.

Everyone except Cheongpung and me remained at least partly vulnerable to the Fear emitted by the Mutated Water God Dragon.

Even if they were Supreme Peak masters counted among the greatest in the world, it made no difference.

But…

*I’m here.*

I was a veteran Hunter who had fought monsters until I was sick of them. That was who I was.

I had stood my ground against an undead army numbering in the tens of thousands, with rotten flesh dangling from their bodies as they charged. I had no reason to tremble in fear just because one eel the size of an aircraft carrier had joined the fight.

“Now that I look at you again, you’re practically a fairy.”

The words had barely left my mouth before the back of my head began to prickle. From the listener’s perspective, it probably sounded like complete madness.

But what I had just said was one hundred percent sincere.

*It’s true that this bastard is powerful, but the Arch Lich was much more difficult—and much stronger.*

If the Skeleton King hadn’t helped me back then, I would have died without question.

But the important thing was that I had survived and brought the bastard down. The fear I had felt while facing the Arch Lich had become experience, carved into my body and mind in its entirety.

*And I’m a fast learner.*

Good experiences and bad experiences alike become flesh and blood. Over the past seven years, I had learned how to survive and how to win.

I drew a deep breath.

At the same time, I raised White Flame’s shaft high into the air.

Then I slammed the end down with all my strength. A level of internal energy never seen before rode the shaft.

*Goooooong!*

The wave of qi that shot outward with the deafening boom pushed back the Fear radiating from the dragon.

The heavy pressure that had surrounded us without a single gap dissipated as though an invisible pane of glass had shattered.

“This is…”

“You…”

The astonished gazes of Jeok Cheongang and Mungyeong touched my face. I stared directly at the dragon and opened my mouth.

“First. Don’t get scared for no reason.”

“……!”

“……!”

Everyone carried fears, great and small, inside their hearts. Fear was a force that stimulated those fears and made people experience terror.

But once those fears were erased, we could finally recognize something we had forgotten.

—Krrrrrrrr.

The enormous monster letting out that low growl was not as powerful or frightening as we had imagined.

I kept my gaze fixed on its gleaming, pitch-black pupil and continued.

“Second. From this point on, follow my instructions and beat the shit out of that bastard without mercy.”

Mungyeong’s dry voice pierced my ears.

“I do not particularly care for the process, but the result sounds rather pleasant.”

“You don’t dislike it because of that, do you?”

“What do you take me for?”

“That was a stupid question.”

The Slaughter Saint.

The greatest assassin in all of Murim history.

To an assassin who eliminated a target by any means necessary, the process did not matter. Only the result mattered.

“Old Master.”

“As far as this old man remembers, I never taught you how to deal with an evil beast like that… We can discuss it after we finish the bastard off.”

*Chiriririk!*

After Jeok Cheongang’s curt reply, Cheongpung answered with purple Sword Force instead of words.

It was an atrocious composition consisting entirely of DPS, without either a healer or a tank. Even so, there could not have been a more powerful raid team.

*Four Supreme Peak masters.*

A combination impressive enough to make even a five-star Jangsu stone bed weep.[^1]

Compared to the enormous body of the Mutated Water God Dragon, we were no more than ants. But inside each of us crouched a giant carrying an unprecedented power.

And now, the four giants were going to hunt a colossal monster.

“You’re dead now.”

As if it understood me, the Mutated Water God Dragon raised its enormous body from beneath the surface and roared.

—Gwooooooooooar!

*Krrrrung, kwaaaaaaaaaang!*

With a single roar, dozens of waterspouts rose and came crashing toward us. Between them, the dragon’s battered jaws opened wide.

*Gooooooooong—!*

The air vibrated faster and more powerfully than before.

But before the third Water Breath could take shape, a shout burst from between my lips and pierced everyone’s ears through the wind and rain.

“Spread out!”

*Shwish-shwish-shwish-shwish!*

As though following a prearranged signal, four figures shot away in different directions and took positions around the dragon.

At last, it was time for the hunt.

* * *

Raid.

As reality was invaded by the unreal and Hunters and monsters began killing one another, this word—once used only in fantasy games—became something even a three-year-old child knew.

But none of the billions of people who had survived the Great Cataclysm could have imagined that a raid was taking place somewhere else, beyond time and space, against a strange monster resembling a dragon.

Nor could they have imagined that a familiar face was caught up at the center of it all.

*Tat-tat, shweeeeeek!*

A heavy body shot toward the air, stepping on fragments of stone as they scattered through the sky.

A massive tail passed within a hair’s breadth, smashing into a half-collapsed cliff and raising a blast of wind pressure.

Through his streaming hair, the eyes of the young man Jin Taekyung gleamed.

*If I cut that tail now… No. Don’t.*

Jin Taekyung restrained the hand that instinctively wanted to swing his spear.

He knew exactly what mattered most in this raid.

He had to block the Mutated Water God Dragon’s escape, lure it as far onto land as possible, and kill it like lightning.

If he struck back and wounded it before then, he might instead alert the monster to the danger.

Of course, someone watching the scene had a slightly different opinion.

“You fucking piece of—!”

*I can’t lose the Disciple I only managed to gain in my old age like this!*

But Jeok Cheongang’s movement as he prepared to launch a palm strike at the monster, accompanied by a thick curse, abruptly stopped at the shout that rang out the next moment.

“Old Master!”

“……!”

*Fwoosh, kwaaaaaaaaaang!*

The Scorching Yang Qi that hastily changed direction burned the innocent ground.

For the briefest instant, puzzlement passed through the dragon’s pitch-black eye. Then it changed into the eye of a savage beast.

—Gwoooooooooar!

*Whoom, bang!*

With a roar, the enormous tail swept across the ground like a broom.

Jeok Cheongang leaped into the air at the last instant to evade the attack and exploded in frustration.

“How long are you planning to make us retreat!”

*Kwaang!*

Far above the ground, Jin Taekyung avoided the monster’s body as it came hurtling toward him and answered,

“I told you I’d give the signal!”

“And when is that going to be?”

“I’ll handle it when the time comes, so please stop shitting all over the place! There’s only so much trolling I can take! Do what you’re told like everyone else!”

“……!”

Jeok Cheongang’s eyes trembled.

Some of the strange words prevented him from understanding exactly what Taekyung meant, but he had heard one thing perfectly clearly.

*A dump? This old man is taking a dump?*

He had only recently been worrying that his infirmities of old age might progress to the point where he started smearing feces on the walls. Now the boy he considered his Disciple was saying something that vile to him.

The shout that followed jolted Jeok Cheongang out of his shock.

“Old Master, now! Retreat thirty *jang* to the rear! Cheongpung, move to the bastard’s rear! Mungyeong, take the flank!”

“Yes, Benefactor!”

“What a strange fellow. I said I would follow your intentions, not that you could speak casually to me.”

“For fuck’s sake, I really can’t stand ranged-DPS assholes who refuse to communicate. Just listen to me!”

“……!”

Seeing Mungyeong struck speechless, press his lips firmly together, and silently do as he was told improved Jeok Cheongang’s mood slightly.

*At least he calls me Old Master.*

He should have been angry. Under normal circumstances, he should have been furious.

But seeing Mungyeong called by his bare name like some nobody from next door made Jeok Cheongang grateful that Taekyung had not simply called him Cheongang.

At the same time, he thought he understood Mungyeong’s feelings as he moved without another word.

*What is this strange feeling?*

How should he put it?

Jin Taekyung was radiating an oddly powerful presence right now.

And in Jeok Cheongang’s estimation, it was not the pressure or bearing possessed by a Supreme Peak master.

It was more like…

*A veteran. Yes, exactly. A battle-hardened veteran.*

Jeok Cheongang had lived his entire life as a martial artist. He had never had any connection to the authorities, nor had he ever been a soldier.

Yet for some reason, he felt as though he understood what it was like for a newly deployed recruit to face a battle-hardened veteran.

“What an incredibly strange fellow, no matter how many times I look at him…”

“Hey, Jeok Cheongang! Snap out of it!”

“……!”

At the moment Jeok Cheongang’s eyelids began to tremble, the words he had been waiting for finally rang out—before he could even unleash his anger.

“Now, strike!”

*Shwish-shwish-shwish-shwish!*

The four giants shot forward at the same time toward the Water God Dragon, which had finally left the waters of Dongting Lake and climbed onto land.

[^1]: Jangsu is a Korean brand known for stone beds marketed for their health benefits.
```
