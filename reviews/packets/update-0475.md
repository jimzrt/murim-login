<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0475.txt",
      "sha256": "4199e2129ed46b2014a4a988cf747951f167acd0ce46952ddce9e9f79aa57860",
      "bytes": 12909
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "740bd7985aa4e348ac4cc299bbe4455ab973b31b6754c9d31581a69dace10319",
      "bytes": 3089
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2eb39f40434261daff34b0e89bdff7969e6763e51476bfdfdfd3e18918cd4181",
      "bytes": 153030
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "92aa8c95aa855651c9999f3dca6edbaed8d5b2ef80f2c9775872ab22c0318944",
      "bytes": 1006
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "0dc5a783635e094e3c049eb614641f3e905082c41f0243d2914ddd23f5b889e1",
      "bytes": 553
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "74ca303551b2c224e105c8b86315616de32655b9eb175eff8301a1fc01c6f2ba",
      "bytes": 1542
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "0cfc73a60d679ff0c7e63a1e15349f7cd37a8b41cd79a86c9926db9ff9a4c2f2",
      "bytes": 1720
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "6206ec07ee18332073c6283677a12ce35d215301e59b907b6f000ddb39774623",
      "bytes": 622
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "e18dab9b86b3a4843a97ffdef7a6c7532cc8e6c733a28148414bb0f3a8dbd899",
      "bytes": 734
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "bb882cf37f97b20509363dde65c544ab530ac7be2754709b99da838a8410a1ae",
      "bytes": 147867
    }
  ],
  "estimated_tokens": 11494
}
-->

# Durable State Update — Chapter 475

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 475. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 475. Profile updates may replace only one
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
  "chapter": 475,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 475,
    "continuity_sources": [475],
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
    "The battle remains active: Taekyung destroyed one eye, tore out every whisker, and ripped away many scales from the dragon with his bare hands while using his spear as an anchor.",
    "The dragon's Berserk Status increases all abilities but clouds combat judgment, and its rampage continues.",
    "Taekyung possesses the Heavenly Martial Physique, giving him superhuman physical strength independent of his accumulated internal energy and martial enlightenment.",
    "The dragon's scales are so durable that early Peak Sword Energy cannot properly cut them; Force is normally required to split them and damage what lies beneath.",
    "Cheongpung remains resistant to Fear and fights with the Zaha Divine Technique; Mungyeong remains partially affected by Fear but continues fighting as the former Slaughter Saint.",
    "The dragon possesses extreme speed, immense durability, black scales, and centuries of accumulated qi.",
    "The dragon's anger manifests as violent storms, lightning, swollen river whirlpools, and other responses from the surrounding water and weather.",
    "The dragon has begun using Breath: its pupils turn black, it forms a massive sphere of water in its mouth, and it fires the sphere toward the ground.",
    "Zhuge Feng remains under cover protecting the others, and the severely injured Dongting Fisherman remains alive for interrogation about Dark Heaven.",
    "An unidentified figure remains on the dragon's head and can tear out its whiskers barehanded."
  ],
  "continuity_sources": [
    474,
    473
  ],
  "open_questions": [
    "What is the Dongting Fisherman's exact role within Dark Heaven, and how was he connected to the earlier destruction inside the secret refuge?",
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Did the Mutated Water God Dragon destroy Donghu Stronghold and the related Yangtze River Channel League strongholds, and why was no Moving Formation trace left?",
    "What unknown power corrupted the Water God Dragon, and what are its true origin and purpose?",
    "Who is the unidentified figure hanging from the dragon's head, and why can that figure tear out its whiskers barehanded?"
  ],
  "safe_through": 474,
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
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 제자     | **Disciple**                                 |
| 은인     | **Benefactor**                               |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 귀가      | **your family**                                                 |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 여의주 | **dragon pearl** | Legendary treasure requested by Jang Taebo. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 와이번 | **Wyvern** | High-tier dragonkin monster. |
| 용족 | **dragonkin** | Monster classification including wyverns and drakes. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 창천 | **azure heaven** | The cloudless sky seen by Namgung Ryong. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 천격 | **Heavenly Strike** | A Fire Dragon Divine Spear form used by Taekyung against Hwangbo Eom. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 브레스 | **Breath** | Dragonkin power used by the Wyverns. |
| 애틀랜타 | **Atlanta** | The U.S. city claimed as the Skeleton King's birthplace. |
| 조지아주 | **Georgia** | The U.S. state claimed as the Skeleton King's birthplace. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 수공 | **water arts** | Water-based martial arts; the Dongting Fisherman's specialty. |
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
| 진태경 | 문경 | young_martial_artist_to_medical_apprentice | Young Hero | formal-polite | Taekyung addresses the non-martial Mungyeong as 소협 while praising his actions. |
| 문경 | 진태경 | young_passenger_to_younger_martial_artist | Young Hero | deferential | Mungyeong uses 소협 while asking Taekyung for help boarding the ship. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 청풍 | 미미 | handler_to_companion_snake | Mimi | cheerful-commanding | Cheongpung repeatedly calls and commands the Thousand-Year Poison Horned Snake. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 진태경 | 미미 | rescuer to companion snake | Mimi or Mimi-chan | informal, pleading | Taekyung calls to Mimi while asking the snake to carry him and the survivors. |
| 진태경 | 수신룡 | hostile martial artist to monster | you, sibu-leol eel bastard | blunt, insulting, and fearless | Taekyung directly insults the emerged Water God Dragon before attacking it. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 474
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 474
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 474
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin and Furnace Fire Pure Blue, and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, and pathologically afraid of water. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 474
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, and is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 474
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 474
- **Aliases:** None
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, having passed the Divine Physician title to his Disciple, and he has reached the Returned to Youth realm.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, while Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

## Korean source

```text
＃475화



변이된 수신룡.

따지고 보면 이 자식도 용은 용이다.

비록 창천을 누비지도 못하고, 여의주도 없는 걸 보면 진짜 용이라기보다는 이무기에 가까운 것 같지만.

다만 문제는…… 이 정체성 흐릿한 놈이 브레스(Breath)를 쓸 줄 안다는 거다.

그것도 존나 강한 브레스를.

콰아아아아아!

나는 입을 벌린 채 거대한 물의 구가 반경 수십여 장을 뒤덮는 광경을 바라보았다.

오랜 세월 동안 장강으로부터 흘러나와 쌓이고 쌓인 지면이 단번에 절반 가까이 붕괴하는 모습도.

‘이런 미친.’

일반적인 수압(水壓)을 아득히 벗어난 힘.

저건 그저 어마어마한 양의 물을 끌어모아 일거에 쏘아 낸 것이 아니다.

변이된 수신룡이 지닌 강대한 기운이 물의 구에 깃든 이상, 이제부터는 워터 브레스라고 불러야 옳다.

‘무림에서 워터 브레스라니.’

차라리 어떤 미친 언데드 몬스터가 미국 조지아주 애틀랜타 출신이라고 우기는 것이 더 자연스럽겠다.

나는 경악 어린 눈빛으로 수신룡이 토해 낸 워터 브레스가 모든 것을 가루로 만드는 광경을 바라보았다.

다음 순간 초토화되는 지면을 피해 어딘가로 쏘아지는 세 개의 신형도 함께.

“미미, 물공 터트리기!”

“……단단히 미친놈이로군. 나도 모르게 잠깐 살심이 들었다.”

“그게 정상이야. 노부도 지금까지 다섯 번 정도 죽이고 싶었거든.”

뿔 달린 뱀에게 진상짓을 벌이는 미친놈 하나에 회춘한 노인 하나. 그리고 이제는 더 늙어 보이기도 힘든 노인 하나.

세 사람의 모습을 확인하자 안도의 한숨이 흘러나왔다.

‘다행히 피했구나.’

이 정도 파괴력을 지닌 브레스에 직격당한다면 제아무리 초절정 고수라고 해도 무사할 수 없다.

변이된 수신룡이 쏘아 보낸 워터 브레스는 그만큼 강력했고, 과거 내 손으로 직접 숨통을 끊었던 블랙 와이번의 그것을 훌쩍 뛰어넘는 기운을 품고 있었다.

‘뭐지? 강하긴 했어도 이 정도까지는 아니었던 것 같은데…….’

광폭화의 영향인가? 아니면 이제야 내재되어 있던 모든 힘을 끌어올린 걸까?

정확히 무엇이 원인인지는 몰라도, 돌연 검은빛으로 물든 눈동자와 모종의 관련이 있는 것이 틀림없다.

그리고 무슨 수를 써서라도 이놈을 쓰러트리는 것이 지금의 내 목표고.

- 크르르르륵.

온통 시커멓게 물든 눈동자가 번들거린다.

빛살과도 같은 속도로 자신의 공격을 피한 인간들을 향해 낮은 울음소리를 토해 낸 괴물은 재차 아가리를 벌렸다.

고오오옹.

막대한 기의 흐름과 함께 놈의 주위를 맴돌던 용오름이 쩍 벌어진 아가리를 향해 빨려들 듯 솟아올랐다.

‘벌써……!’

두 번째 워터 브레스다.

현대의 대표적인 용족 몬스터인 와이번도 브레스를 이렇게 빠르게, 자주 사용하지는 못하는데 이놈은 차원이 달랐다.

나는 완성된 워터 브레스가 쏘아지기 전에, 서서히 벌어지고 있는 놈의 콧잔등을 있는 힘껏 후려쳤다.

“이 쩍벌충 새끼가!”

쾅!

굉음과 함께 흔들리는 거대한 대가리.

갑작스럽게 동체가 흔들리자 빠르게 완성되어 가던 물의 구가 주춤했지만, 소기의 목적을 달성한 내 얼굴은 딱딱하게 굳었다.

‘다르다.’

온 힘을 실은 일권.

그러나 주먹에서 느껴지는 반발력은 불과 촌각 전에 비교할 바가 아니었다.

변이된 수신룡에게 일어난 변화에는 브레스뿐만이 아니라, 육체의 강화 역시 포함되어 있었던 것이다.

간단하게 예를 들자면 송판 열 장을 부쉈어야 하는 주먹이 다섯 장에서 멈춘 기분.

나는 이를 악물었다.

‘빌어먹을.’

상황에 따라 대처도 바뀌어야 했는데, 내 생각이 너무 안일했다. 나는 놈의 비늘 사이에 쑤셔 넣어 두었던 백염을 붙잡았다.

‘인벤토리 수납. 오픈. 소환.’

스슥!

찰나의 순간, 허공에 녹아들 듯이 사라졌던 백염이 인벤토리를 거쳐 다시 내 손아귀로 소환된다.

모든 동작을 최소화한 움직임. 그건 시스템 없이는 불가능한 일이었고, 나조차도 비교적 최근에서야 숙달되기 시작한 응용법이었다.

그리고 백염의 창대가 손아귀 잡힌 그 순간, 나는 이미 모든 준비를 끝마친 채 일격을 내리긋고 있었다.

화르륵-!

투명한 창날 위로 피어오른 청백색의 화염이 공기를 태우고 주변에 가득한 수분을 증발시킨다.

짙은 안개와도 같은 수증기를 가른 화염이 나아가는 방향의 끝에, 검은 비늘에 뒤덮인 괴물의 콧잔등이 있었다.

“아가리 닫아.”

천격(天格).

콰아아아아, 서걱!

공력을 태워 불러일으킨 강대한 화염이 비늘을 가른다. 살을 태우고, 뼈를 부수었다. 엄청난 강도를 자랑하는 피륙으로도 만년한철과 강기가 융합된 일격을 막을 수는 없었다.

창날을 따라 좌우로 갈라지는 모든 것의 뒤에, 완성을 코앞에 둔 물의 구가 있었다.

‘벤다.’

수백 년간 존재했던 수신룡의 워터 브레스와, 하늘로부터 낙뢰처럼 내리꽂히는 화룡의 발톱이 만났다.

아니, 격돌했다.

고오오오옹-

귀가 먹먹해지는 굉음과 함께, 붉고 푸른 섬광이 눈앞을 가득 메웠다.



* * *



그날, 정체불명의 굉음을 들은 것은 그 자리에 있던 이들뿐만이 아니었다.

동정호에 인접한 곳에 머무르던 모두가 그 소리를 들을 수 있었다.

쿠구구구궁!

뇌성벽력과는 차원이 다른 거대한 굉음에 산천초목이 허리를 숙였다.

흉흉한 분위기를 피해 칩거 중이던 양민들은 화들짝 놀라 그 자리에 엎드렸고, 사건의 조사를 위해 동정호 인근을 배회하던 관군들은 창까지 놓치며 혼비백산했다.

나이 지긋한 늙은이들은 울음을 터트리는 손주들을 토닥이며 근심 어린 표정으로 하늘을 바라보며 중얼거렸다.

“신령이시다. 신령께서 노하셔서 누군가에게 천벌을 내리신 게야. 이놈의 세상이 어찌 될는지…….”

반은 맞고, 반은 틀린 말이었다.

아득한 과거로부터 지금까지. 수백 년의 세월 동안 입에서 입으로 전해지던 신령스러운 존재는 분명 실존했으니까.

그러나 신령으로 추앙받던 영물은 이제 추악한 악물(惡物)로 타락했고, 분노한 변이된 수신룡이 내린 천벌은 한 인간에 의해 가로막혔다.

그 누구도 찾지 않는 동정호 깊숙한 어느 곳에서, 인간과 악물의 전투는 지금 이 순간에도 이어지고 있었다.

- 크롸아아아아!

사방 천지를 울리는 고통에 찬 괴성. 아가리가 찢어진 괴물이 몸부림치며 동정호의 강물 위로 몸을 내던졌다.

콰과과과과!

검푸른 핏물과 뒤섞인 강물이 단번에 아득한 높이까지 솟구쳤다.

저 머나먼 대해(大海)에서나 볼 법한 파도가 일어나 사방을 덮치자, 괴물의 거대한 동체에 비하면 작은 점과도 같은 세 사람의 신형이 그보다 한발 앞서 움직였다.

쐐애애애액!

화살처럼 쏘아지는 세 개의 신형. 그러나 한 사람이 선택한 방향은 다른 두 사람과 정반대였다.

피하기는커녕 홀로 괴물을 향해 돌격하는 적천강의 모습에 문경이 전음을 날렸다.

- 화왕!

그러나 적천강은 대답 대신 덮쳐 오는 파도를 향해 일장을 내뻗었다.

퍼엉!

묵직한 파공성과 함께 작달막한 노구(老軀)를 집어삼키려던 거대한 파도의 중심이 뻥 뚫리며 수증기가 되어 증발했다.

고통에 찬 괴물의 끊임없는 몸부림에 곧이어 몰려온 제이, 삼의 파도가 몰려왔지만, 다음 순간 깨끗하게 잘려 나갔다.

촤악!

파도의 허리 부분을 정확히 끊어 낸 것은 새하얀 빛줄기였다.

이어 청풍이 흩뿌린 검기가 물보라 사이에 섞여 날아드는 자갈들을 가루로 만들자, 소검에 묻은 물기를 털어 낸 문경이 적천강을 향해 입을 열었다.

“몇 가지 묻고 싶은 게 있는데. 혹시 못 본 사이에 수공(水功)이라도 익혔나?”

문경을 힐끗 바라본 적천강이 툭 내뱉었다.

“노부가 세상에서 제일 싫어하는 게 뭔지 아나?”

“……?”

“첫째, 물에 젖는 것. 둘째, 산에 불 지르는 것. 마지막 셋째. 물에 젖은 상태로 불타는 산을 보는 것. 이거 세 가지야.”

“그게 무슨.”

“오십 년 전쯤이었지. 근처 계곡에서 하기 싫은 목욕을 억지로 끝마치고 나왔더니 구화산이 활활 불타고 있더라고. 결국 그 천하의 호래 새끼들을 다 잡아 죽였지.”

무림인이라면 누구나 아는 이야기다.

그날 이후 구화산 깊은 산속에서 무공을 연마하던 어느 늙은이는 화왕(火王)이라는 이름을 얻었다.

“뭐, 그럭저럭 잘 풀려서 화왕이니 뭐니 주위에서 추켜세우긴 했지만 몇몇 정신 나간 놈들은 뒤에서 손가락질하더군. 천 명을 죽이고도 눈썹 하나 까딱하지 않는 살귀(殺鬼) 같은 늙은이라고.”

쳐다보지도 않고 제 할 말만 하는 적천강의 태도에 문경이 눈살을 찌푸렸다.

“도대체 무슨 이야기를 하는 건지 모르겠군. 이게 무슨 헛소…….”

“별거 아니야. 간단히 하자면 노부는 구화산이 좋았고. 살면서 처음 생긴 내 집이라 더 좋았다는 거지. 정마대전을 통해 내 것을 건드리는 놈은 무슨 수를 써서라도 족친다는 걸 온 천하의 호래 새끼들에게 각인시켜 주었고. 그런데…….”

적천강이 활활 타오르는 눈동자로 몸부림치는 괴물을 향해 걸음을 옮기며 말을 이었다.

“저 염병할 놈은 그걸 모르는 것 같아. 하긴, 몰랐으니까 겁대가리 없이 노부의 제자를 건드렸겠지.”

“정말이지 제멋대로군. 결국 수공을 익히지 않았다는 이야기로 들리는데.”

“염병할. 어떻게든 되겠지.”

“우리 사이에 우정 따위는 없지만, 조심하라고 말해 주고 싶군.”

“저깟 뱀장어 하나 처리하는데 수공 따위가 대수일까. 무슨 수를 써서라도 잡아 족칠 것이야.”

청풍이 천진난만한 목소리로 끼어들었다.

“와아. 뱀장어가 다 저렇게 커요? 정말 하나같이 오십 장쯤 되나요?”

“살심이 치미는군.”

“죽일 거면 검성에게 양해를 구하고 은밀하게 처리해. 물론 그전에 한 손 거들고.”

소검을 가볍게 고쳐잡은 문경이 문득 입을 열었다.

“혹시, 진태경 그 녀석이 수공을 배웠나?”

“구화산 깊은 계곡에서 놈을 수련시켰던 기억이 새록새록 나는군. 그렇게 헤엄 못 치는 놈은 난생처음 봤어.”

“……당장 저 괴물을 뭍으로 끄집어내야겠군.”

“동의하네. 제자를 두 번이나 잃고 싶지는 않거든.”

수중에서 전투가 벌어진다면 수신룡에게 전투가 유리해지는 것은 당연지사.

그러나 또 다른 선택지 따위는 존재하지 않았다.

그들이 나서지 않는다면 진태경이 익사하고 말 테니까.

그리고 적천강과 문경이 결의에 찬 표정으로 시선을 부딪친 그때, 청풍이 불쑥 입을 열었다.

“어? 아닌데. 은인은 헤엄도 되게 잘 치는데요.”

“……?”

“……?”

“진짜예요. 오는 길에 은인이. 어, 그러니까…… 맞다. 자기를 아구아맨이라고 불러 달라고 했어요.”

이게 무슨 개소리란 말인가.

멈칫한 두 노고수의 눈동자에 의문이 떠오른 바로 그 순간이었다.

- 구워어어어어!

촤아아아아악!

강물 깊은 곳에서 울려 퍼지는 괴성과 함께, 수면 위로 솟구치는 한 사람의 신형.

사방으로 튀어오르는 물보라 사이로 익숙한 얼굴을 마주한 적천강이 입을 딱 벌렸다.

“너, 너…….”

“어푸, 갖춰!”

“뭐, 뭣이라?”

의문을 해소할 틈도 없었다.

말이 끝나기가 무섭게, 출렁이는 수면 위로 거대한 그림자가 어른거렸다.

동시에 지면 위로 내려선 진태경의 입에서 천둥 같은 외침이 튀어나왔다.

“공격 대형, 갖춰!”

타오르는 눈동자에 서린 것은 무인이 아닌, 능숙한 헌터의 그것이었다.
```

## Final English reading copy

```markdown
# Chapter 475

The Mutated Water God Dragon.

When you got right down to it, this bastard was a dragon too.

It might have been closer to an *imugi* than a true dragon, considering it could neither roam beneath the azure heavens nor wield a dragon pearl.

But there was one problem…

This identity-confused bastard knew how to use Breath.

And not just any Breath. A fucking powerful one.

*Kwaaaaaaaaaah!*

I stared with my mouth hanging open as an enormous sphere of water spread across a radius of several dozen *jang*.

The ground, built up layer upon layer over centuries by sediment flowing down from the Yangtze, collapsed by nearly half in an instant.

*What the hell…*

A force far beyond ordinary water pressure.

That was not merely an enormous quantity of water gathered together and fired all at once.

Since the immense qi belonging to the Mutated Water God Dragon had infused the sphere of water, it was only right to call it Water Breath from now on.

*Water Breath in the Murim.*

It would have been more natural if some insane undead monster had insisted it was from Atlanta, Georgia, in the United States.

I stared in horror as the Water Breath vomited by the Water God Dragon pulverized everything in its path.

At the same moment, three figures shot away from the ground being reduced to a wasteland.

“Mimi, blow up the water orb!”

“…You’re completely insane. I felt murderous intent for a moment there without even realizing it.”

“That’s normal. This old man has wanted to kill you about five times already.”

One lunatic provoking a horned snake. One rejuvenated old man. And one old man who could hardly look any older.

When I confirmed the three of them were safe, a sigh of relief escaped me.

*Thank goodness they dodged it.*

If they took a direct hit from Breath with that level of destructive power, even a Supreme Peak master could not escape unharmed.

The Water Breath fired by the Mutated Water God Dragon was that powerful. It contained qi that far surpassed the Breath of the Black Wyvern I had personally killed in the past.

*What the hell? It was strong, but I don’t remember it being this strong…*

Was it the effect of Berserk? Or had it finally drawn out all the power lying dormant within it?

I did not know the exact cause, but it unquestionably had something to do with the pupils that had suddenly turned black.

And my goal right now was to bring this bastard down by any means necessary.

—Krrrrrrk.

Its utterly black pupils gleamed.

The monster let out a low growl at the humans who had dodged its attack at the speed of light, then opened its maw again.

*Goooooong.*

Along with an immense flow of qi, the waterspouts circling around it surged upward as though being sucked into its wide-open jaws.

*Already…?*

A second Water Breath.

Even the Wyvern, the modern world’s most prominent dragonkin monster, could not use Breath this quickly or this frequently.

This thing was on an entirely different level.

Before the completed Water Breath could be fired, I swung with all my strength and struck the bridge of its nose, which was slowly spreading wider.

“You wide-mouth bastard!”

*Kwaang!*

The enormous head shook with a deafening boom.

The sudden jolt to its body made the sphere of water, which had been nearing completion, falter. But despite accomplishing what I’d intended, my expression hardened.

*It’s different.*

A punch thrown with everything I had.

Yet the resistance I felt through my fist was incomparable to what I had experienced only moments earlier.

The changes that had occurred in the Mutated Water God Dragon did not consist solely of Breath. Its body had also grown stronger.

To put it simply, it felt like my fist, which should have smashed through ten wooden boards, had stopped after breaking only five.

I clenched my teeth.

*Damn it.*

I should have changed my approach according to the situation, but my thinking had been too complacent. I grabbed White Flame, which I had shoved between the dragon’s scales.

*Store in Inventory. Open. Summon.*

*Shhk!*

In the blink of an eye, White Flame, which had melted into empty space, passed through my Inventory and reappeared in my grasp.

It was a movement that minimized every action. That would have been impossible without the System, and even I had only recently begun mastering this advanced application.

The moment the shaft of White Flame settled into my hand, I had already finished preparing and was bringing it down in a single strike.

*Fwoosh!*

Blue-white flames rose over the transparent spearhead, burning the air and evaporating the moisture filling the surroundings.

Beyond the flames slicing through the dense, foglike steam stood the bridge of the black-scaled monster’s nose.

“Shut your mouth.”

Heavenly Strike.

*Kwaaaaaaaaaah—schk!*

The immense flames summoned by burning internal energy split the scales. They burned through flesh and shattered bone.

Even flesh of astonishing toughness could not stop a strike that fused Ten-Thousand-Year Cold Iron with Force.

Behind everything cleaved apart to either side of the spearhead was the nearly completed sphere of water.

*Cut.*

The Water Breath of the Water God Dragon, which had existed for hundreds of years, met the fire dragon’s claw plunging down like lightning from the heavens.

No.

They collided head-on.

*Gooooooong—*

Along with a deafening boom that numbed my ears, red and blue flashes filled my vision.

* * *

That day, the people present at the scene were not the only ones who heard the mysterious roar.

Everyone staying near Dongting Lake heard it.

*Gugugugugung!*

The mountains, rivers, and trees bowed beneath a tremendous boom unlike any peal of thunder.

Commoners who had secluded themselves indoors to avoid the ominous atmosphere were startled and threw themselves facedown on the spot. Government troops wandering near Dongting Lake to investigate the incident dropped even their spears and fled in terror.

Old men patted grandchildren who had burst into tears and gazed at the sky with worried expressions as they muttered,

“It’s a divine spirit. The divine spirit has grown angry and brought down heavenly punishment on someone. What is going to become of this wretched world…?”

They were half right and half wrong.

From the distant past until now, the supernatural being passed down by word of mouth for hundreds of years had truly existed.

But the spirit beast once worshiped as a divine spirit had fallen into an ugly evil beast, and the heavenly punishment delivered by the enraged Mutated Water God Dragon had been blocked by a single human.

Deep in a part of Dongting Lake that no one ever visited, the battle between the human and the evil beast continued even now.

—Kroaaaaaaaaah!

A pained roar shook heaven and earth in every direction.

The monster, its maw torn open, writhed and threw its body onto the waters of Dongting Lake.

*Kwa-gwa-gwa-gwa!*

The river water, mixed with dark-blue blood, surged to a distant height in an instant.

Waves such as one might see only on the distant open sea rose and crashed in every direction. Three figures no larger than specks beside the monster’s enormous body moved one step ahead of them.

*Shweeeeeek!*

Three figures shot forward like arrows.

But one person chose a direction completely opposite to the other two.

Seeing Jeok Cheongang charge alone toward the monster instead of dodging, Mungyeong sent a Sound Transmission.

—Fire King!

But rather than answer, Jeok Cheongang thrust one palm toward the approaching wave.

*Poom!*

With a heavy sound of splitting air, a hole opened through the center of the enormous wave that had been about to swallow his small, aged body. The water evaporated into steam.

A second and third wave soon came rolling in, driven by the monster’s ceaseless, pain-filled thrashing.

But the next moment, they were cleanly sliced apart.

*Shraak!*

A pure-white streak of light had severed the waves through their middles.

Then the Sword Energy scattered by Cheongpung mingled with the spray and reduced the pebbles flying through it to dust. Mungyeong shook the water from his short sword and spoke to Jeok Cheongang.

“There are a few things I want to ask. Did you happen to learn water arts since we last saw each other?”

Jeok Cheongang glanced at Mungyeong and answered bluntly.

“Do you know what this old man hates most in the world?”

“…?”

“First, getting wet. Second, setting a mountain on fire. And third—the last one—watching a mountain burn while I’m soaking wet. Those three things.”

“What does that have to do with—”

“It was about fifty years ago. I had just finished taking a bath I didn’t want in a nearby valley when I came out and saw Mount Jiuhua burning like a torch. In the end, I hunted down and killed every last one of those bastards.”

It was a story every martial artist knew.

After that day, an old man who had been practicing martial arts deep in the mountains of Mount Jiuhua gained the name Fire King.

“Well, things worked out, more or less, and people around me started praising me as the Fire King and whatnot. But some insane bastards pointed fingers behind my back. They called me a murderous old man like a death fiend who could kill a thousand people without even blinking.”

Mungyeong frowned at Jeok Cheongang’s attitude. The old man was not even looking at him and simply continued saying whatever he wanted.

“I have no idea what you’re talking about. What kind of nonsense is—”

“It’s nothing. To put it simply, this old man liked Mount Jiuhua. I liked it even more because it was the first home I had ever had in my life. Through the Great Faction War, I made sure every bastard in the world understood that anyone who touched what belonged to me would be crushed by any means necessary. But…”

Jeok Cheongang walked toward the writhing monster, his eyes blazing as he continued,

“That damned bastard doesn’t seem to know that. Then again, if it had known, it wouldn’t have touched my Disciple without a shred of fear.”

“You really do whatever you please. It sounds like you never learned water arts after all.”

“Damn it. We’ll figure it out somehow.”

“We have no friendship between us, but I would like to tell you to be careful.”

“Do water arts really matter when dealing with one lousy eel? I’ll hunt it down and crush it by any means necessary.”

Cheongpung joined in with an innocent voice.

“Wow. Do eels really get that big? Are they all about fifty *jang* long?”

“I feel murderous intent rising.”

“If you’re going to kill him, ask the Sword Saint for permission and deal with it quietly. Of course, lend a hand before that.”

Mungyeong lightly adjusted his grip on his short sword, then suddenly spoke.

“Did that fellow Jin Taekyung happen to learn water arts?”

“I remember training him in the deep valleys of Mount Jiuhua. I’ve never seen anyone who was that bad at swimming.”

“…Then we’ll have to drag that monster onto land.”

“I agree. I don’t want to lose my Disciple twice.”

If the battle took place underwater, it went without saying that the Water God Dragon would have the advantage.

But there was no other choice.

If they did not step in, Jin Taekyung would drown.

And just as Jeok Cheongang and Mungyeong exchanged determined looks, Cheongpung suddenly spoke.

“Huh? That’s not right. Benefactor is really good at swimming.”

“……?”

“……?”

“It’s true. On the way here, Benefactor… Uh, what was it again? Oh, right. He asked me to call him Aguaman.”

What the hell was that supposed to mean?

The two old masters stopped short, confusion rising in their eyes.

At that very moment—

—Gwoooooooooar!

*Shraaaaaaaaaah!*

Along with a roar echoing from deep beneath the river, a human figure shot up through the surface.

Jeok Cheongang’s jaw dropped when he recognized the familiar face amid the spray exploding in every direction.

“You, you…”

“*Hk—* form up!”

“What did you say?”

There was no time to resolve his confusion.

The instant the words left his mouth, a huge shadow rippled across the rolling surface.

At the same time, a thunderous shout burst from Jin Taekyung’s lips as he landed on the ground.

“Form an attack formation!”

What burned in his eyes was not the look of a martial artist.

It was the look of a seasoned Hunter.
```
