<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0438.txt",
      "sha256": "d9690d94bed9de07a9a71e928df60e9ac654c18dbe6ab3a8d2ae12ce031c8cfc",
      "bytes": 13354
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "210c5df0aeee4823cc8f76c093818344844c24b503e9e88f0147be5c4b4262d8",
      "bytes": 2244
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "6542e5948c0a0e06062b035673e74493aa492af66e03e95e2af3660191678da8",
      "bytes": 143402
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "c11d5e32430e2a8ce6ac040fbdce9482a57dcef717fbd79bc8985b966cd28b2c",
      "bytes": 553
    },
    {
      "path": "characters/Hanga.md",
      "sha256": "6c899f82e7f7516dd6c3e90d8b19c1c35edf7cb71fd01090b4226815465389bb",
      "bytes": 568
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "23e584ade6b302ee4ee06f1cf067f06dc1c033b94f68baee0c4723502f32d33f",
      "bytes": 1390
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "455d2d21790b36efe9a7b1bb3db8412d3bd09443269c4463a245237f9ac6ec0e",
      "bytes": 1416
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "8e64a5a9e484f2e1fcb8bad00a8214237c52b253c4f61fe322a06b02cf055ee9",
      "bytes": 622
    },
    {
      "path": "characters/Mu Song.md",
      "sha256": "ebf8dc499296a5811c8111d11395683cdc9b25abe48f1650fbd0cfb17bfdaadc",
      "bytes": 792
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "bee6925ed15e0b16cf09b8b68fd7dc9540197a13223d0e5f8330ede80ff4757f",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "bc8c79344a1b13062844571c7a4109b2beefc98822e0698ed6958d88115245bb",
      "bytes": 136527
    }
  ],
  "estimated_tokens": 11541
}
-->

# Durable State Update — Chapter 438

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 438. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 438. Profile updates may replace only one
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
  "chapter": 438,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 438,
    "continuity_sources": [438],
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
    "Mungyeong's Slaughter Saint identity remains concealed beneath his medical-apprentice persona, though Jeok Cheongang recognizes it.",
    "Mungyeong continues traveling with Jin Taekyung's group without understanding why he feels compelled to remain with them.",
    "Jin Taekyung has opened his Middle Dantian, and Mungyeong has now confirmed the change.",
    "Taekyung has given Mungyeong a fabricated account of a white-haired swordsman and a fortuitous encounter to conceal how his Middle Dantian opened.",
    "Mungyeong believes the swordsman was Lü Dongbin but has detected inconsistencies in Taekyung's description.",
    "Jeok Cheongang has arrived to confront Mungyeong aboard the fast ship.",
    "Taekyung's recent martial insight requires Jeok's instruction, and he intends to investigate mysterious patterns and symbols found in both worlds.",
    "The group will travel by water only as far as Sichuan, with Mu Song offering to escort them with his subordinates.",
    "Jin Wikyung is withholding an important matter for a later private discussion."
  ],
  "continuity_sources": [
    437
  ],
  "open_questions": [
    "Why does Mungyeong continue accompanying Jin Taekyung's group despite being unable to explain the impulse?",
    "How did Jin Taekyung open his Middle Dantian?",
    "What confidential matter is Jin Wikyung withholding?",
    "Are Taekyung's suspicions about the mysterious patterns and symbols found in both worlds correct?",
    "What will result from the confrontation between Jeok Cheongang and Mungyeong?"
  ],
  "safe_through": 437,
  "temporary_decisions": [
    "Render 노야 as “Old Master” and 스승님 as “Master” for Taekyung's address to Jeok Cheongang.",
    "Keep Mungyeong's medical-apprentice voice polite and concerned, while his Slaughter Saint voice remains terse, threatening, and coercive.",
    "Preserve the established renderings Middle Dantian, Slaughter Saint, Three Saints, Water Dragon Stronghold, and Guang'an.",
    "Retain the chapter's strong profanity and Taekyung's vulgar slang in confrontational dialogue.",
    "Render 여암 as “Lü Yan” and preserve the cancer pun in Taekyung's misunderstanding."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 살성     | **Slaughter Saint**           | —              |
| 해상왕    | **Seafaring King**            | Pa Ryun        |
| 장강수로맹  | **Yangtze River Channel League** |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 기연     | **fortuitous encounter**                         | Use sparingly                                         |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 제자     | **Disciple**                                 |
| 선배     | **Senior**                                   |
| 상태               | **Status**                     |
| 로그아웃             | **Logout**                     |
| 몬스터     | **monster**           |
| 사천     | **Sichuan**            |
| 노부      | **this old man / I**                                            |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 항아 | **Hanga** | Local village boy who lives near Jang Taebo. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 무송 | **Mu Song** | Lord of Water Dragon Stronghold and disciple of the Seafaring King. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 열화동 | **Fire Gate Cavern** | Ancestral cavern where the Fire Gate Clan began and its legacy continues. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 의생 | **medical apprentice** | Mungyeong's occupation. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 검남춘 | **Jiannan Chun** | Sichuan liquor offered to the Heavenly Power Demon. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 동빈 | **Dongbin** | Lü Yan's courtesy name. |
| 여동빈 | **Lü Dongbin** | The Sword Immortal identified by Mungyeong. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 항아 | visiting_adult_to_local_child | little one | friendly and coaxing | Questions Hanga and offers food in exchange for information. |
| 항아 | 노인 | child_to_elder_stranger | Grandpa | childlike-familiar | Hanga calls the unnamed old man 할부지 after he arrives at her family’s home; this is distinct from her address to Jang Taebo. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 진태경 | 무송 | junior_martial_artist_to_senior_martial_artist | Senior | formal-polite | Taekyung uses 선배님 after recognizing Mu Song as a senior martial artist and disciple of the Seafaring King. |
| 문경 | 무송 | survivor_to_savior_and_authority | Great Hero Mu Song | formal-deferential | Mungyeong credits Mu Song with saving him and asks him to spare Hwang Tae-gu. |
| 무송 | 문경 | stronghold_lord_to_young_passenger | you | gruff-but-considerate | Mu Song offers Mungyeong the right to decide Hwang Tae-gu's fate. |
| 진태경 | 문경 | young_martial_artist_to_medical_apprentice | Young Hero | formal-polite | Taekyung addresses the non-martial Mungyeong as 소협 while praising his actions. |
| 문경 | 진태경 | young_passenger_to_younger_martial_artist | Young Hero | deferential | Mungyeong uses 소협 while asking Taekyung for help boarding the ship. |
| 무송 | 진태경 | senior_martial_artist_to_junior_martial_artist | Junior | familiar-teasing | Mu Song calls Taekyung 후배 and jokes about his supposed taste for men. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 무송 | 적천강 | junior_martial_artist_to_legendary_martial_master | Great Hero Jeok | formal-deferential | Mu Song respectfully refers to Jeok Cheongang as 적 대협 while worrying that Jeok dislikes him. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 적천강 | 무송 | legendary martial master to stronghold lord | you | gruff, coercive, and dismissive | Uses 자네 while ordering Mu Song to take the group only as far as Sichuan and leave the fast ship. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 437
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hanga.md

# Hanga (항아)

- **Safe through:** Chapter 372
- **Aliases:** None
- **Role:** Local village girl, Jang-pal’s daughter, who lives near Jang Taebo and regularly visits him.
- **Personality:** Curious, energetic, observant, and already attentive to the value of information and food.
- **Voice:** Childlike, direct, and inquisitive, with an occasional surprisingly worldly remark.
- **Relationships:** Calls Jang Taebo Grandpa; Jang Taebo is his elderly neighbor and only conversational companion.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 436
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is a legendary wandering martial master and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, and casually threatening or violent when dissatisfied. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 437
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, and can perceive the texture of qi well enough to sever layered magic.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and student, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 437
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mu Song.md

# Mu Song (무송)

- **Safe through:** Chapter 436
- **Aliases:** Ship-Fire Boy
- **Role:** Lord of Water Dragon Stronghold, a Peak master and the Seafaring King's second martial Disciple who controls major Yangtze river traffic in Sichuan and belongs to the Yangtze River Channel League's moderate faction.
- **Personality:** Ambitious, domineering, impatient with interruptions, and capable of pragmatic cooperation when circumstances demand it.
- **Voice:** Deep and low in private, shifting to dry authority or boisterous command when addressing subordinates and rivals.
- **Relationships:** He has carried Jin Taekyung's party and Mungyeong from Guang'an to Chengdu and agreed to send subordinates to help them return.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 437
- **Aliases:** None
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, having passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, while Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

## Korean source

```text
＃438화



문경을 바라보는 적천강의 눈이 활활 타올랐다.

“잠시 노부가 자리를 비운 틈을 타서 감히 남의 제, 제…… 제태경을 핍박해?”

“……제태경은 또 뭐야.”

어이가 없어서 눈물이 쏙 들어간 내 중얼거림에, 적천강이 버럭 외쳤다.

“시끄럽다!”

나와 문경이 동시에 대답했다.

“노야가 더 시끄러운데요. 지금 거의 세상의 중심에서 제태경을 외치고 계신데.”

“목청을 보니 십 년은 더 살겠군.”

기차 화통을 에어 프라이어에 구워 드셨나.

아까부터 문경이 공력으로 기막(氣腸)을 펼쳐 소리가 새어 나가는 것을 막고 있어서 망정이지, 아니었다면 진작 사람들이 몰려오고도 남았다.

얼굴이 벌겋게 달아오른 적천강의 모습에 문경이 작게 혀를 찼다.

“잠시 대화를 나눈 것뿐이다. 노부가 이런 핏덩이를 핍박해서 무엇할까.”

적천강이 내게 고개를 돌렸다.

“네 녀석이 대답해 봐라. 저 늙은이의 말이 사실이냐?”

“대화만 나눈 건 사실인데, 제 대답이 마음에 안 들면 장강 밑바닥에 가라앉을 거라고 했어요.”

내 고자질에 문경이 뻔뻔한 표정으로 덧붙였다.

“물론 약간 겁을 주긴 했지.”

“이런 빌어먹을 늙은이를 봤나! 감히 이따위 짓을 벌이고도 무사할 줄 알았더냐!”

“흥분을 가라앉혀라. 중단전에 관해 물어볼 것이 있었을 뿐이다.”

당장이라도 달려들 것처럼 상체를 기울인 적천강이 우뚝 멈췄다.

“중단전?”

“그래. 설마 몰랐다고 하진 않겠지.”

“…….”

“이토록 짧은 시간에 중단전을 여는 것은 불가능한 일이다. 천운(天運)이라는 말로도 설명할 수 없지.”

나와 문경을 번갈아 바라보던 적천강이 피식 웃었다.

“별것도 아니었군.”

“……뭐?”

“그래서, 저 녀석이 마공(魔功)이라도 익혔다고 말하고 싶은 건가?”

“그건…….”

“짧게 말하지. 아니야.”

너무나도 확신에 찬, 태연한 반응에 문경의 말문이 막힌 순간. 적천강이 내게 손가락을 까딱거렸다.

“뭣 하느냐. 어서 이리 오지 않고.”

“예?”

“수련 봐 달라며? 지금부터 시작이다.”

“아, 예.”

너무 스무스하게 넘어가는 상황에 나조차도 내심 당황스러울 정도다. 그런 내 마음을 읽은 것처럼 적천강이 물었다.

“그래도 궁금하긴 하군. 당최 어떻게 중단전을 열었느냐?”

“어. 그게요. 꿈을 꿨는데 웬 검을 든 노인이…….”

“검선 여동빈이라도 만난 게냐?”

“……뭐, 저쪽 말을 들어 보면 그런 것 같기도 하고.”

“기연을 얻었구나. 하늘이 네 녀석을 돕는 모양이다. 세상에는 사람이 짐작할 수 없는 일들이 종종 벌어지기 마련이지.”

시선은 나를 바라보고 있지만, 대답이 향하는 곳은 문경이다.

마치 들으라는 듯이 한마디를 툭 던진 적천강이 돌연 주름진 손을 휘둘렀다.

딱!

“아야! 왜 때려요?”

“그냥 괘씸해서 한 번 쳐 봤다. 꼬우냐?”

“꼬우면요?”

“한 대 더 맞아야지.”

빡!

“아악!”

“돌대가리 같은 놈이 엄살은. 헛짓거리 그만하고 따라오거라.”

이대로 가도 되나?

속을 짐작할 수 없는 묘한 표정으로 서 있는 문경을 힐끔거리는 내게, 벼락같은 호통이 쏟아졌다.

“그런데도 이놈이!”

“아이고, 알겠어요. 소리 좀 그만 지르세요.”

“이리 미적대서야 수련할 생각이 있는 게냐?”

문경을 두고 돌아선 나는 적천강의 등을 바짝 쫓으며 속삭였다.

“그런데, 더 안 물어보세요?”

적천강이 고개도 돌리지 않고 퉁명스럽게 대답했다.

“무얼 말이냐.”

“아니, 그. 중단전…….”

“흰소리 그만하고 따라오기나 해라. 앞으로 저 늙은이 근처에는 얼씬도 하지 말고.”

“넵.”

그거야말로 내가 바라던 바다. 무슨 장강의 인어공주도 아니고, 괜히 잘못 걸렸다가 물고기들과 함께 호북까지 떠내려갈 생각은 추호도 없으니까.

“다음에 또 이런 모습이 눈에 띄면 아주 혼쭐을 낼 줄 알아라. 알겠느냐?”

“……아니, 저는 피해자인데 왜.”

“시끄럽다. 조금 전에도 모조리 박살을 내 버릴까 하다가 참았다.”

“그러고 보니까 진짜 용케 참으셨네요.”

“그랬다면 배가 남아났겠느냐?”

“하긴, 무송 선배 사정도 생각해 주긴 해야죠. 쾌조선 타오를 때 표정 보셨어요?”

홱 고개를 돌린 적천강이 눈살을 찌푸렸다.

“무슨 개소리냐? 노부가 수적 놈들 사정을 왜 생각해?”

“예?”

“여기서 또 배를 잃으면 타고 있던 놈들과 다른 배로 옮겨타야 할 테고, 무게가 늘어난 만큼 속도가 느려질 것이 아니냐.”

“……아.”

“생각을 좀 하고 말해라. 촌각이라도 빨리 이 지긋지긋한 장강을 벗어나야지. 축축하고, 흔들리고, 아주 끝이 없어.”

인성 수준 보소.

몸을 부르르 떨며 걸어가는 불 포켓몬을 바라보는데, 문득 한 가지 생각이 떠올랐다.

‘죄다 불태워 버리면 육로로 갈 수 있는 거 아닌가.’

이 말은 하지 말아야겠다. 적천강은 충분히 실행에 옮기고도 남을 위인이니까.

나는 뒤통수에 닿는 문경의 따끔거리는 시선을 애써 무시하며 적천강의 뒤를 따랐다.



* * *



쾌조선은 거침없이 나아갔다.

배 위로 높이 휘날리는 장강수로맹의 깃발을 본 배들은 황급히 길을 텄고, 그것은 끈끈한 유착 관계로 이어진 관부(官府)의 군함도 예외는 아니었다.

장강의 하류와 길을 손바닥 보듯이 꿰뚫고 있는 수적들은 무송의 명령에 따라 힘차게 노를 저었으며 저 멀리서 불어오는 바람을 받은 돛은 크게 부풀었다.

거칠게 움직이는 장강의 강물처럼, 그날 하루의 시간도 빠르게 흘렀다.

그리고…… 어제와 같이 뱃머리에 앉아 어둠에 잠긴 장강을 바라보고 있던 문경은 또다시 찾아온 불청객에게 낮은 목소리로 말했다.

“생각보다 늦었군.”

“무송인지 황송인지 하는 놈이 꿍쳐 둔 술을 찾느라 시간이 걸렸지. 마지막까지 안 내놓으려고 기를 쓰더라니까.”

난간에 턱 걸터앉은 적천강이 신줏단지 모시듯 꺼낸 작은 항아리의 밀봉을 뜯었다.

동시에 퍼져 나가는 향긋한 주향(酒香)에, 무미건조하던 문경의 표정에 실금이 갔다.

“검남춘(劍南春)?”

“역시 사천 하면 검남춘이지. 이 맛에 온다니까.”

“보통 검남춘은 아닌 것 같은데.”

“그놈 말로는 제 스승이 준 거라더군. 해상왕(海上王)씩이나 되는 인간이 제자에게 평범한 술을 선물했을 리는 없고…… 덕분에 모처럼 노부의 혀가 호강하는 거지.”

항아리 채로 들어 꿀꺽꿀꺽 들이킨 적천강이 입맛을 다셨다.

“허어, 끝내주는데. 한 잔 줘?”

검남춘이 담긴 항아리를 유심히 바라보던 문경이 고개를 저었다.

“……끊은 지 오래라고 했을 텐데.”

“대답이 늦어. 고금제일의 살수라는 늙은이가 그리 속이 훤히 보여서야.”

“그 나이에도 천둥벌거숭이처럼 날뛰는, 나잇값도 못 하는 늙은이보다는 낫지.”

“뭣이!”

“흰소리 그만하고 본론으로 들어갔으면 좋겠군. 내게 할 말이 있을 텐데?”

어제의 방문은 예고 없이 이루어진 것이었지만, 오늘은 아니었다.

몇 시진 전, 적천강은 전음으로 찾아가겠노라 전했고 문경은 그를 기다리고 있었다.

“성격도 급하긴. 이것 역시 살수답지 않아.”

“살수가 아니라 의생이니까.”

“그럼 살생이라고 하든지.”

“제자나 스승이나. 언행이 똑 닮았군.”

눈살을 찌푸리는 문경을 뒤로하고 술을 들이켠 적천강이 옷소매로 입가를 훔치며 대답했다.

“언행을 닮았을지 몰라도 천지 차이지. 그 녀석은 상리(常理)를 벗어난 괴물 같은 놈이거든.”

문경이 말없이 고개를 끄덕였다.

괴물이라는 말에 동의하지 않을 수 없다. 고작 약관을 갓 넘긴 나이에 초절정의 벽을 넘은 것도 경악할 만한 일이거늘, 진태경은 숨을 고르기도 전에 한 걸음을 더 내디뎠다.

‘초절정의 경지에 오른 것이 언제였지?’

문경은 먼 과거의 기억을 더듬었다.

지금보다 더 날카롭고 말이 없던 젊은 시절. 그는 오직 무(武)에 혼과 마음을 다했다.

때로는 은밀하게, 때로는 정면 승부를 통해 수많은 실전으로 경험을 쌓아 올렸고 마침내 선택받은 자들만이 들어설 수 있다는 지고한 경지에 발을 디뎠다.

‘그때가 이립 중반이었지.’

고금제일의 살수라 불리며 살성(殺星)이라 불리는 그조차 서른이 넘어서야 초절정의 경지에 올랐다.

그리고 중단전을 연 것은 그로부터 수년 후, 불혹이 가까운 나이가 되어서였다.

한데 진태경은 약관이 갓 넘은 나이로 유구한 무림 역사에 자신의 족적을 새겼다.

문경이 생각하기에 이것은 사마외도(邪魔外道). 그중에서도 천고의 마공이 아니고서야 불가능한 일이었다.

“아무래도…… 오늘 대화는 길어질 것 같군.”

“아니, 짧게 끝날 걸세. 노부로서도 그다지 해 줄 말이 없으니까.”

적천강의 대답에 문경의 눈빛이 깊게 가라앉았다.

“왜지?”

“보지도, 듣지도 못한 무언가에 대해 무슨 말을 할까. 그저 받아들이는 수밖에 없지.”

“설마 검선 여동빈이 꿈에 나와 깨달음을 줬다는 헛소리를 믿는 건 아니겠지.”

“그럴 수도 있고, 아닐 수도 있어. 하지만 설령 사실이라 하더라도 그리 놀랍지는 않구먼. 클클.”

“화왕!”

벼락같은 외침이 두 사람을 둘러싼 기막에 부딪쳐 웅웅 떨렸다.

그러나 문경이 순간 드러낸 노기(怒氣)는, 바로 이어진 적천강의 말에 씻은 듯이 사라지고 말았다.

“이 년.”

“……뭐라?”

“불과 이 년 만에 초절정의 벽을 허물고, 중단전을 열어 버린 놈이다. 노부가 여동빈이었다면 꿈이 아니라 직접 찾아왔을 거야. 하계(下界)에 엄청난 놈이 있구나, 하면서.”

문경은 첫 번째로 자신의 귀를, 두 번째로 적천강의 정신 상태를 의심했다.

하지만 눈앞의 자그마한 노인은 그 어느 때보다 투명하고 맑은 눈동자로 문경을 바라보며 말을 이어 가고 있었다.

“의심하지 마. 그 녀석을 대할 때는 지금까지 살면서 보고 들은 모든 것들을 머릿속에서 지우고 마주해. 무슨 뜻인지 알겠나?”

“……!”

“태경이. 그 아이와 검성의 제자는 말 그대로 신룡(神龍)이야. 누구도 본 적 없고, 그저 짐작할 수밖에 없는.”

쏴아아아.

새하얀 포말이 뱃머리에 튀었다. 문경이 긴 침묵을 깨고 입을 연 것은, 그로부터 한참의 시간이 흐른 뒤였다.

“믿을 수 없군.”

“믿으라고 하지 않았네. 받아들이라고 했을 뿐.”

“그건, 하나같이 불가능한 일이야.”

“하릴없이 나이를 먹으면서 깨달은 진리가 하나 있지. 바로 다른 사람의 마음까지 어쩌지는 못한다는 거야.”

적천강은 첫 제자를 떠나보낸 후에야 그 사실을 알았다.

그리고 우연히 만난 한 청년을 진심으로 마음 깊이 받아들인 어느 날에서야, 또 다른 사실도 문득 깨달았다.

그날을 떠올릴 때마다 욱신거리던 통증이 희미해졌다는 것을.

“지켜보면 알게 되겠지. 나처럼.”

난간에서 일어나 휘적휘적 걸음을 옮기는 적천강의 뒷모습을 말없이 응시하던 문경이 불쑥 입을 열었다.

“그놈은 지금 뭘 하고 있나?”

“태경이 녀석?”

고개를 돌린 적천강은, 달빛 아래에서 껄껄 웃었다.

“아주 죽은 듯이 자고 있지.”



* * *



열화동에서의 수련은 마라톤이라면, 이번에는 단거리 계주다.

호북으로 향하는 일주일 남짓한 기간 동안 현대와 무림을 오가며 두 집 살림을 하기로 마음먹었다.

띠링.



- [로그아웃]을 완료했습니다!



나는 익숙한 종소리와 함께 눈을 떴다. 한국으로 향하는 전용기 내부다.

지금까지 축적된 피로로 인해 곤히 잠든 사람들, 그리고 두 눈을 말똥말똥 뜬 채 나를 바라보는 한 몬스터가 보였다.

“뭘 봐. 인마.”

스켈레톤 킹이 대답했다.

“이런 거였군. 흠. 인간들은 모두 너처럼 죽은 듯이 자나?”

“내가 특별한 거야.”

“괴상한 게 아니고?”

뻑!

이 새끼가 꼭 매를 벌어요.
```

## Final English reading copy

```markdown
# Chapter 438

Jeok Cheongang’s eyes blazed as he glared at Mungyeong.

“How dare you threaten someone else’s dis, dis… disciple Taekyung while this old man was away?”

“…What the hell is a ‘disciple Taekyung’?”

Utterly dumbfounded, I muttered under my breath, my tears drying up at once. Jeok Cheongang roared.

“Quiet!”

Mungyeong and I answered at the same time.

“You’re louder, Old Master. You’re practically shouting ‘disciple Taekyung’ from the center of the world.”

“Judging by the volume of your voice, you’ll live another ten years.”

*Did he roast and eat a train smokestack in an air fryer?*

It was a good thing Mungyeong had been using his internal energy to maintain a qi barrier and keep any sound from escaping. Otherwise, people would have gathered around us long ago.

Jeok Cheongang’s face had turned bright red. Mungyeong clicked his tongue softly.

“We merely had a brief conversation. What would this old man gain by threatening such a young pup?”

Jeok Cheongang turned toward me.

“You answer me. Is what that old man said true?”

“It’s true that we only talked, but he said I’d sink to the bottom of the Yangtze if he didn’t like my answer.”

At my betrayal, Mungyeong shamelessly added,

“Of course, I did frighten him a little.”

“Would you look at this damned old man! You think you’ll get away with something like this?”

“Calm yourself. I merely had something to ask him about his Middle Dantian.”

Jeok Cheongang had leaned forward as though he were about to charge, but he stopped dead.

“Middle Dantian?”

“Yes. Surely you didn’t fail to notice.”

“…”

“Opening one’s Middle Dantian in such a short time is impossible. Even the phrase ‘heavenly fortune’ cannot explain it.”

Jeok Cheongang looked back and forth between Mungyeong and me, then let out a quiet laugh.

“So it was nothing.”

“…What?”

“So you’re trying to say that the boy learned demonic martial arts or something?”

“That’s…”

“I’ll put it simply. No.”

Mungyeong was left speechless by Jeok Cheongang’s calm, utterly confident response. At that moment, Jeok Cheongang crooked a finger at me.

“What are you waiting for? Come here.”

“Huh?”

“You asked me to watch your training, didn’t you? We’re starting now.”

“Oh. Right.”

The situation had moved on so smoothly that even I was caught off guard. As though he had read my thoughts, Jeok Cheongang asked,

“I am curious, though. How exactly did you open your Middle Dantian?”

“Uh, well. I had a dream, and there was this old man with a sword…”

“Did you meet the Sword Immortal Lü Dongbin?”

“…Well, judging by what that guy over there said, it might have been.”

“You gained a fortuitous encounter. It seems the heavens are helping you. Strange things that no one could ever imagine do happen in this world.”

Jeok Cheongang was looking at me, but his answer was directed at Mungyeong.

After tossing out that single remark as though he wanted Mungyeong to hear it, Jeok Cheongang suddenly swung his wrinkled hand.

*Smack!*

“Ow! Why did you hit me?”

“I felt like hitting you because you were irritating. Got a problem with that?”

“What if I do?”

“Then you can take another hit.”

*Whack!*

“Aaagh!”

“You blockheaded brat. What are you whining about? Stop fooling around and follow me.”

*Can I really just leave like this?*

I glanced at Mungyeong, who stood there with a strange expression that revealed nothing. A thunderous shout immediately crashed down on me.

“And yet this brat!”

“Okay, okay, I get it. Please stop shouting.”

“Dragging your feet like this, do you even intend to train?”

I turned my back on Mungyeong and followed close behind Jeok Cheongang, whispering,

“But aren’t you going to ask anything else?”

Jeok Cheongang answered gruffly without turning around.

“Ask about what?”

“No, I mean… the Middle Dantian…”

“Stop talking nonsense and follow me. From now on, don’t go anywhere near that old man.”

“Yes, sir.”

That was exactly what I wanted. I wasn’t some Mermaid Princess of the Yangtze, and I had absolutely no intention of getting on his bad side and drifting all the way to Hubei with the fish.

“If I catch you looking like this again, I’ll teach you a lesson. Understand?”

“…I’m the victim here. Why are you blaming me?”

“Quiet. I was about to smash everything to pieces earlier, but I held myself back.”

“Come to think of it, you really did show restraint.”

“Would the ship have survived if I hadn’t?”

“True. We should take Senior Mu Song’s circumstances into consideration. Did you see his face when we boarded the fast ship?”

Jeok Cheongang whipped his head around and frowned.

“What kind of nonsense are you talking about? Why should this old man care about the circumstances of those river bandits?”

“Huh?”

“If we lose another ship here, we’ll have to transfer everyone aboard to a different one. The extra weight would slow us down.”

“…Oh.”

“Think before you speak. We need to get off this wretched Yangtze as quickly as possible. It’s damp, it rocks, and it never seems to end.”

*What a lovely personality.*

I watched the Fire Pokémon walk away, shivering from head to toe, when a thought suddenly occurred to me.

*If we burn everything down, couldn’t we travel by land?*

I decided not to say it. Jeok Cheongang was more than capable of actually doing it.

I ignored Mungyeong’s prickling gaze on the back of my head as best I could and followed Jeok Cheongang.

* * *

The fast ship cut through the water without slowing.

Boats that saw the flag of the Yangtze River Channel League flying high above the deck hurriedly cleared a path. Even the government warships connected to the League through their sticky ties of collusion were no exception.

The river bandits knew the lower Yangtze and its waterways like the backs of their hands. Following Mu Song’s orders, they pulled hard on their oars, while the sails billowed wide in the wind blowing from far away.

Like the rough waters of the Yangtze, the hours of that day flowed by quickly.

And…

Just as he had the previous night, Mungyeong sat at the bow, gazing out at the Yangtze shrouded in darkness. When the uninvited guest who had come to see him again arrived, Mungyeong spoke in a low voice.

“You’re later than I expected.”

“It took time to find the liquor that fellow Mu Song—or whatever his name is—had hidden away. He fought to keep it from me until the very end.”

Jeok Cheongang perched himself on the railing and broke the seal on a small jar he had taken out as carefully as though it were a treasured family heirloom.

At the same time, the fragrant scent of liquor spread through the air. A crack appeared in Mungyeong’s usually expressionless face.

“Jiannan Chun?”

“Of course it’s Jiannan Chun when you come to Sichuan. This is what makes the trip worthwhile.”

“That doesn’t seem like ordinary Jiannan Chun.”

“According to that fellow, it was a gift from his Master. A man as eminent as the Seafaring King wouldn’t have given his Disciple ordinary liquor… Thanks to him, this old man’s tongue is enjoying a rare treat.”

Jeok Cheongang lifted the jar to his mouth and gulped down the liquor. Then he smacked his lips.

“Damn, that’s good. Want a drink?”

Mungyeong watched the jar of Jiannan Chun closely, then shook his head.

“…I believe I told you I quit drinking a long time ago.”

“Your answer was too slow. For an old man known as the greatest assassin in history, you make your thoughts awfully easy to read.”

“That still makes me better than an old man who carries on like a reckless brat at his age.”

“What did you say?”

“I’d like to dispense with the nonsense and get to the point. You have something to say to me, don’t you?”

Jeok Cheongang’s visit the previous day had been unexpected. Today was different.

Several shichen earlier, Jeok Cheongang had used Sound Transmission to tell Mungyeong that he would come. Mungyeong had been waiting for him.

“You’re impatient. That isn’t very assassin-like, either.”

“I’m a medical apprentice, not an assassin.”

“Then call yourself a killer of lives.”

“Disciple and Master alike. Your words and actions are exactly the same.”

Jeok Cheongang ignored Mungyeong’s frown, took another drink, and wiped his mouth with his sleeve before answering.

“Our words and actions may resemble each other, but we’re worlds apart. That brat is a monster who has strayed beyond all common sense.”

Mungyeong nodded silently.

He couldn’t disagree with the word *monster*. Reaching the Supreme Peak realm just after passing the age of twenty was astonishing enough, but Jin Taekyung had taken another step before he had even caught his breath.

*When did he reach the Supreme Peak realm?*

Mungyeong searched through memories of the distant past.

He had been younger then—sharper and quieter than he was now. He had devoted his soul and heart entirely to martial arts.

Sometimes covertly and sometimes through direct confrontation, he had accumulated experience through countless real battles. At last, he had set foot in that exalted realm that only the chosen could enter.

*It was sometime in my mid-thirties.*

Even Mungyeong, who had been called the greatest assassin in history and given the name Slaughter Saint, had not reached the Supreme Peak realm until after turning thirty.

And he had opened his Middle Dantian several years later, when he was nearing forty.

Yet Jin Taekyung had left his mark on Murim’s long history just after passing the age of twenty.

In Mungyeong’s estimation, this could only be the work of demonic, heterodox arts—and a legendary demonic martial art at that.

“I have a feeling this conversation will take a while.”

“No, it’ll be over quickly. This old man doesn’t have much to say, either.”

Mungyeong’s gaze sank deeply at Jeok Cheongang’s answer.

“Why not?”

“What can I say about something I’ve never seen or heard? There’s nothing to do but accept it.”

“Surely you don’t believe the nonsense that the Sword Immortal Lü Dongbin appeared in his dream and gave him enlightenment.”

“It may have happened, or it may not have. But even if it’s true, it isn’t all that surprising. Heh heh.”

“Fire King!”

The thunderous cry struck the qi barrier surrounding the two men and reverberated with a deep hum.

But the anger that had flashed across Mungyeong’s face vanished as though it had been washed away by Jeok Cheongang’s next words.

“Two years.”

“…What did you say?”

“It took that brat only two years to break through the wall of the Supreme Peak realm and open his Middle Dantian. If this old man were Lü Dongbin, I would have come to him in person—not in a dream—saying, ‘There’s an incredible fellow in the lower world.’”

Mungyeong first questioned his own ears, then Jeok Cheongang’s state of mind.

But the small old man before him continued speaking with eyes clearer and more transparent than ever.

“Don’t doubt him. When you face that brat, erase everything you’ve seen and heard throughout your life from your mind. Do you understand what I mean?”

“……!”

“Taekyung. That boy and the Sword Saint’s Disciple are, in the truest sense, divine dragons. No one has ever seen one. All anyone can do is guess.”

*Whoosh.*

White foam splashed against the bow. A long time passed before Mungyeong broke the silence.

“I can’t believe it.”

“I didn’t tell you to believe it. I only told you to accept it.”

“That’s impossible. Every part of it.”

“There’s one truth this old man learned while growing older for no reason. You can’t control another person’s heart.”

Jeok Cheongang had learned that only after sending his first Disciple away.

And it was only on the day he sincerely accepted a young man he had met by chance deep into his heart that he suddenly realized something else.

The pain that throbbed whenever he thought of that day had grown fainter.

“You’ll understand if you watch him. Just as I did.”

Mungyeong silently watched Jeok Cheongang’s back as he rose from the railing and shuffled away. Then he suddenly spoke.

“What is that brat doing right now?”

“Taekyung?”

Jeok Cheongang turned his head and laughed heartily beneath the moonlight.

“He’s sleeping like the dead.”

* * *

If training at Fire Gate Cavern had been a marathon, this was a short-distance relay.

During the little over a week it would take to reach Hubei, I decided to go back and forth between the modern world and Murim while maintaining two lives.

> **System**
>
> **Logout** complete!

I opened my eyes to the familiar chime. I was inside the private jet bound for Korea.

I saw people sleeping soundly from all the fatigue they had accumulated, along with one monster staring at me with his eyes wide open.

“What are you looking at, you punk?”

The Skeleton King answered.

“So that was what it was. Hmm. Do all humans sleep like the dead, just like you?”

“I’m special.”

“Not weird?”

*Whack!*

This bastard really went out of his way to get hit.
```
