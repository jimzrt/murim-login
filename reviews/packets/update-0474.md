<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0474.txt",
      "sha256": "e2389d58513f6df84b9e906c29d0fa54b6711e8ee2b0ad0dc67470cf982c8179",
      "bytes": 12599
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "5938e5f141880f7c7a089052e42813232d78d1b66d7b0a12ea78bca8a5e8f681",
      "bytes": 2934
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2eb39f40434261daff34b0e89bdff7969e6763e51476bfdfdfd3e18918cd4181",
      "bytes": 153030
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "c43059c92ef678094e1667d0bb3060ecda34707ebff60b036ff666d5406bac41",
      "bytes": 1006
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "df4c23c4c1896010e82e335ffdc7b64b38c43041170c83d21240b947626d2fc4",
      "bytes": 553
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "3137188df896c08faab2e7fddd7a3bc6926d9282dbdd6bc6fc91d8589f8003c7",
      "bytes": 1542
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "e2a39c5b1e1c61bf02bebdb65464447368033cbae65d1acdb2a7a71f1a1f9673",
      "bytes": 1646
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "abce5b82efc2cb85cbb2cd36eac5835908a87279ef19fdf5f71c9763198847df",
      "bytes": 622
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "bd58f3e585676d2a5992849310ef5085d8685021ac7c266d18d9c881eadf6fe3",
      "bytes": 734
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "bb882cf37f97b20509363dde65c544ab530ac7be2754709b99da838a8410a1ae",
      "bytes": 147867
    }
  ],
  "estimated_tokens": 11417
}
-->

# Durable State Update — Chapter 474

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 474. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 474. Profile updates may replace only one
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
  "chapter": 474,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 474,
    "continuity_sources": [474],
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
    "The battle remains active: Taekyung destroyed one eye with White Flame and is now tearing out the dragon's whiskers with his superhuman Strength.",
    "The dragon's Berserk Status increases all abilities but clouds combat judgment, and its rampage continues.",
    "Cheongpung remains resistant to Fear and fights with the Zaha Divine Technique; Mungyeong remains partially affected by Fear but continues fighting as the former Slaughter Saint.",
    "The dragon possesses extreme speed, immense durability, black scales, enormous whiskers, and centuries of accumulated qi.",
    "The dragon's whiskers possess cutting power above a Peak master's Sword Energy individually, while their combined force can overwhelm Taekyung's short sword.",
    "Mungyeong believes the dragon caused the destruction at Donghu Stronghold and the death of Yangtze One Saber.",
    "Jeok Cheongang can withstand the dragon's direct tail attack and considers it the strangest and most frightening monster he has encountered.",
    "Zhuge Feng remains under cover protecting the others, and the severely injured Dongting Fisherman remains alive for interrogation about Dark Heaven.",
    "Honglan is recovering and Ju Wongong remains unconscious under guard.",
    "An unidentified figure remains on the dragon's head and can tear out its whiskers barehanded."
  ],
  "continuity_sources": [
    473,
    472
  ],
  "open_questions": [
    "What is the Dongting Fisherman's exact role within Dark Heaven, and how was he connected to the earlier destruction inside the secret refuge?",
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Did the Mutated Water God Dragon destroy Donghu Stronghold and the related Yangtze River Channel League strongholds, and why was no Moving Formation trace left?",
    "What unknown power corrupted the Water God Dragon, and what are its true origin and purpose?",
    "Who is the unidentified figure hanging from the dragon's head, and why can that figure tear out its whiskers barehanded?"
  ],
  "safe_through": 473,
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
| 열화문    | **Fire Gate Clan**               |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 지능               | **Intelligence**               |
| 몬스터     | **monster**           |
| 산서     | **Shanxi**             |
| 노부      | **this old man / I**                                            |
| 귀가      | **your family**                                                 |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 고블린 | **goblin** | Monster species reported at the F-rank Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 용족 | **dragonkin** | Monster classification including wyverns and drakes. |
| 천년독각사 | **Thousand-Year Poison Horned Snake** | Extremely venomous horned snake used to make Hong Dao's thirty-year-old liquor. |
| 열화동 | **Fire Gate Cavern** | Ancestral cavern where the Fire Gate Clan began and its legacy continues. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 괴력난신 | **supernatural powers** | Term for extraordinary and unnatural powers. |
| 근력 | **Strength** | System attribute increased by Jin Taekyung. |
| 브레스 | **Breath** | Dragonkin power used by the Wyverns. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 천잠사 | **Heavenly Silkworm Thread** | Rare treasure used as the Dongting Fisherman’s fishing line and weapon. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
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
| 적천강 | 문가 | hostile_interlocutors | Mun | blunt and threatening | Jeok Cheongang addresses the Slaughter Saint as Mun while defending Jin Taekyung. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 진태경 | 미미 | rescuer to companion snake | Mimi or Mimi-chan | informal, pleading | Taekyung calls to Mimi while asking the snake to carry him and the survivors. |
| 진태경 | 수신룡 | hostile martial artist to monster | you, sibu-leol eel bastard | blunt, insulting, and fearless | Taekyung directly insults the emerged Water God Dragon before attacking it. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 472
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 473
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 472
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin and Furnace Fire Pure Blue, and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, and pathologically afraid of water. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 471
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, and is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 471
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 472
- **Aliases:** None
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, having passed the Divine Physician title to his Disciple, and he has reached the Returned to Youth realm.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, while Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

## Korean source

```text
＃474화



콰드드득!

진태경에 의해 수십 가닥의 수염이 단번에 뽑혀 나오는 순간, 변이된 수신룡은 하나밖에 남지 않은 눈동자를 부릅떴다.

- 크르르륵……!

믿을 수 없었다.

저 작고 하찮은 인간 따위가, 그것도 무기를 들지 않은 맨손으로 자신의 수염을 뽑아 버리다니.

그건 있을 수도 없고 있어서도 안 되는 일이었으며, 수백 년의 세월을 살아온 수신룡으로서도 처음 겪는 충격적인 사건이었다.

그리고 다음 순간, 수신룡은 깨달았다.

자신의 수염을 순수한 근력만으로 뽑아 버린 이 인간이 단단히 미친놈이라는 것을.

“민머리!”

뽁!

“대머리!”

뽀복!

“맨들맨들 빡빡이!”

뽀보보보복!

- 그워어어어어어!

영혼으로부터 우러나오는 비명. 변이된 수신룡은 고통에 찬 울부짖음과 함께 몸부림쳤다.

도대체 어떤 이유에서인지는 모르겠지만, 처음 눈을 잃었을 때보다 수십 배는 더 큰 고통과 슬픔이 치밀어 올랐다.

한시라도 빨리 이 미친 인간을 떼어 놔야 했다.

아니, 수염이 모조리 뽑혀 나가기 전에 한 가닥이라도 건져야 한다!

- 크롸아아아!

하지만 수신룡의 간절한 바람과 달리, 진태경은 전혀 그럴 생각이 없었다.

푸푹!

콧잔등을 뒤덮은 비늘 사이로 창날을 박아 넣어 신형을 고정한 진태경이 음산한 목소리로 입을 열었다.

“마, 네가 왜 못 걸어 다니는 줄 알아?”

- 크륵……?

“두발이 없어서.”

뽀보보보보복!

- 그워어어어!

“천하에 존재하는 모든 영물의 털을 곱해도 0개다. 왜냐하면 너는 털이 없으니까. 그냥 없으니까. 존나 하나도 없으니까!”

콰드드드득!

진태경의 손속은 그 어느 때보다 잔혹했다.

공격하기 위해 한데 뭉쳐 날아드는 수염을 한 손으로 잡아챈 뒤, 잡초 뽑듯이 쑥 당기자 무쇠처럼 단단한 피부가 쩍 벌어지고 천잠사(天蠶絲)보다 질기고 예리한 수염들이 모조리 뽑혀 나왔다.

그것도 단 한 가닥도 남기지 않고 모조리!

- 우어, 우워어어어어!

변이된 수신룡은 먹구름에 가린 하늘처럼 흐릿해진 이성 속에서도 극렬한 분노와 슬픔에 사로잡혔다.

이 수염이 어떤 수염인가. 수백 년간 자신과 함께 성장해 온, 그야말로 영혼의 동반자와도 같은 존재였다.

불손한 마음을 품은 침입자를 처치할 수 있는 훌륭한 무기인 동시에 자신의 힘과 위엄을 상징하는 징표이기도 했다.

그런 수염이 사라졌다. 나약하고 쓸모없는 해초처럼 힘없이 뽑혀 나갔다.

그것도 한참이나 작고 하찮은 인간의 손에 의해!

- 캬우우우우!

천지를 울리는 거친 포효.

수백 년에 달하는 기나긴 시간 동안 동정호와 장강을 지배했던 주인이 흉성(凶星)을 발산하자 주위의 모든 것이 숨을 죽였다.

아니, 주인의 분노에 따라 변화했다.

쿠르르릉, 콰광!

그것은 실로 두렵고도 기이한 광경이었다. 유독 짙은 먹구름에 휩싸인 하늘에서는 벼락이 쉴 새 없이 내리쳤고, 지난 오십여 년간 유례없던 폭우가 쏟아져 내렸다.

앞서 몇 시진 동안 이어진 이상 기후에 몇 배로 불어난 강물은 각각 크고 작은 회오리를 만들며 수신룡의 주위를 맴돌았다.

콰아아아아!

그리고 작은 재앙과도 같은 그 풍경 속에 철탑처럼 우뚝 선 거대한 동체.

온통 핏빛을 띤 눈동자를 빛내는 괴물의 모습에, 지상의 사람들은 작게 신음했다.

“허.”

“염병할. 노부가 오래 살긴 했군. 이런 말도 안 되는 걸 보게 될 줄이야.”

적천강과 문경은 아연한 눈빛으로 이 믿을 수 없는 광경을 바라보았다.

영물(靈物)이니, 악물(惡物)이니 하는 존재들이 놀라운 힘을 지녔다는 사실은 익히 알고 있었지만 지금 눈 앞에 펼쳐진 광경은 그들이 예상했던 범주를 아득하게 벗어난 것이었다.

작은 산과 비견될 만한 크기의 괴물. 꼬리를 휘두르면 절벽이 무너져 내리고, 울부짖으면 사방 천지가 울린다.

그뿐인가, 터져 나오는 흉성에 산천초목이 숨을 죽이며 그 분노에 벼락과 물이 감응한다.

그야말로 낡고 삭아 버린 옛이야기에서나 나올 법한 일이 현실에서 벌어지고 있었다.

지금 이 순간, 두 노고수의 머릿속에 떠오른 생각은 하나뿐이었다.

‘괴력난신(怪力亂神).’

괴이(怪異)와 용력(勇力)과 패란(悖亂)과 귀신에 관한 일.

그야말로 괴력난신이라는 네 글자가 품고 있는 뜻 그대로였다.

오랜 세월을 무림에 몸담은 그들조차 이해할 수 없는 불가사의한 존재와 현상이 벌어지고 있었다.

하지만 괴력난신이라는 단어는 비단 한 존재에게만 허락된 것이 아니었다.

콰드득!

뇌성벽력 사이에서도 선명히 들리는 파육음.

다음 순간 적천강과 문경의 머리 위로, 검푸른 핏물에 흠뻑 젖은 비늘이 쏟아져 내렸다.

하나, 둘, 셋…… 이내 소나기처럼 후두둑 떨어지는 수십여 개의 비늘.

맹금류와 같은 안력을 지닌 그들은 까마득한 상공에서 벌어지는 일을 확인하고 할 말을 잃었다.

“속살! 속살을 보자!”

“……!”

“……!”

콰드드드득!

광기 어린 외침과 함께 미친 듯이 손을 움직이는 한 청년.

한 손으로는 창대를 힘껏 움켜쥐고, 다른 한 손으로는 무기도 들지 않은 채 맨손으로 비늘을 잡았다.

이어 힘차게 잡아당기자 검푸른 핏물과 함께 힘없이 떨어져 나오는 비늘.

- 쿠워어어어어!

변이된 수신룡이 흉포한 울음과 함께 거대한 동체를 몸부림쳐도 소용없었다.

낌새가 보이면 눈동자가 녹아내린 뻥 뚫린 공간으로 귀신같이 내빼더니, 한바탕 난동이 끝나면 쏙 고개를 내밀고 작업을 시작했다.

분노에 찬 주먹질까지 곁들여 가면서.

“이 개새끼가!”

쾅! 콰앙! 콰지직!

열화문의 각종 절기 중에서도 파괴력으로는 다섯 손가락 안에 드는 멸염신권(滅炎神拳)과 초인이라 부를 만큼 엄청난 힘이 합쳐지자, 어지간한 선박에 버금가는 크기의 머리가 흔들리며 박살 난 비늘이 떨어져 내렸다.

- 캬우우우우!

변이된 수신룡은 미칠 노릇이었다.

그나마 수염이 있을 때는 공격이라도 할 수 있었지, 한 가닥도 안 남기고 모조리 뽑혀 나간 지금은 도무지 답이 나오지 않았다.

몸부림으로 떼어 내려고 하면 창을 박아넣은 채 버티고, 잠잠해졌다 싶으면 나와서 비늘을 죄다 잡아 뜯는데 어쩌란 말인가.

하도 절벽에 머리를 박아 대서 그런지 이제는 현기증마저 느껴질 지경이었다.

꽝! 꽈아아앙!

그 광경을 지켜보는 문경과 적천강은 그저 입만 벙긋거렸다.

‘이런 미친…….’

‘아니, 무슨 무 뽑는 것도 아니고…….’

두 사람 모두 저 비늘이 얼마나 대단한 강도를 지녔는지 알고 있었기에 더욱 놀랄 수밖에 없었다.

절정 초입의 어설픈 검기로는 제대로 절단하기조차 어렵고, 강기를 사용해야 확실하게 비늘을 가르고 내부에 타격을 입힐 수 있을 만큼 엄청난 강도를 자랑하는 해괴한 비늘이 아닌가.

그런데 저 핏덩이는 아예 부수고, 뜯어 버렸다. 심지어 무기도 들지 않은 텅 빈 맨손으로.

‘공력을 모조리 끌어올린 건가? 아무리 그렇다 해도 사람의 근력으로는 턱없이 부족할 텐데.’

‘이게 뭔…… 아니, 아니지. 저놈이라면 가능하지.’

문경은 꿈이라도 꾸는 것 같았고, 산서성에서부터 지금까지 진태경을 지켜본 적천강은 기가 차면서도 감탄했다.

“이런 미친놈을 보았나, 으하하!”

저 괴물이 사용하는 무기 중 하나인 수염을 몽땅 뜯어 버린 것으로도 모자라, 이제는 비늘 제거 작업까지 시작했다.

무인으로 치자면 병장기를 부러트리고 무복 위에 덧입은 갑옷까지 벗겨낸 꼴.

적천강의 시선으로 본 현재 진태경의 무공에 대한 깨달음은 명백히 그들 두 사람보다 하수요, 청풍보다도 밑줄에 있다고 할 수 있었으나 정작 근본부터 달랐다.

‘그저 강하다.’

진태경은 한 사람의 무림인으로서도 초절정의 경지를 이룬 강자.

그러나 수 갑자의 공력과 무공에 대한 깨달음이 사라진다 해도 그 자체로 강하다.

마치 한낱 피륙으로 이루어진 사람의 육신에 하늘의 힘이 깃든 것처럼.

“정녕, 저것이 가능한가?”

희미한 경악이 묻어나오는 문경의 목소리에, 적천강은 즐겁게 웃었다.

그건 열화동에서 수련할 당시 그가 수도 없이 떠올렸던 의문이었고, 그럴 때마다 진태경은 분노할 만큼 뻔뻔한 대답으로 일관했었다.

이제는 그 대답을 다른 이에게 들려줄 때다.

“응. 천무지체.”

“……!”

“어이가 없고 황당하지? 그럼 됐어. 섣부르게 이해하려고 하지 마. 저놈은 원래 그런 놈이니까.”

적천강이 어깨를 으쓱하던 그때, 청풍이 결의에 찬 표정으로 입을 열었다.

“자, 우리도 가요. 미미. 벼락치기! 회오리 일으키기!”

……취릭, 취리리릭?

“아, 못 하는구나.”

“……저놈도 마찬가지고.”

적천강이 청풍을 향해 한 번만 더 개소리를 지껄이면 천년독각사로 만든 뱀술을 마시게 될 거라며 으름장을 놓은 순간, 오싹한 적막과 기운이 반경 수십 장을 짓눌렀다.

구구구구궁!

적천강과 문경, 그리고 청풍은 등골을 타고 흐르는 한기를 느끼며 고개를 들었다.

고오오오옹.

공기의 파동.

어느덧 쉴새 없이 쏟아져 내리던 비바람도, 벼락도 멈췄다. 숨을 죽였다.

지상에 있던 모두는 그 너머에서 붉은 기운을 흩뿌리던 괴물의 핏빛 동공이 시커멓게 물드는 것을 볼 수 있었다.

그와 동시에 천천히 벌어지는 거대한 아가리와, 동굴처럼 컴컴한 어둠으로 빨려가듯 휘몰아치는 물의 구(球) 역시도.

‘저게 뭐지?’

모두의 머릿속의 스친 한 줄기 의문. 그리고 다음 순간, 까마득한 상공으로부터 들려오는 외침. 아니 비명이 있었다.

“피해-!”

그 다급한 목소리의 주인이 진태경이라는 걸 알아차리기도 전에, 세 사람의 신형은 바람처럼 쏘아지고 있었다.

비록 크고 작은 격차는 있을지언정 그들 한 사람, 한 사람은 초절정 고수이자 뛰어난 실전 감각을 지닌 무림인.

저것의 정체를 꿰뚫어 볼 수는 없어도, 저 알 수 없는 힘이 얼마나 무서운 힘을 지녔는지는 알 수 있었다.

그리고 그들의 예측은 정확히 맞아떨어졌다.

콰아아아아-!

귀가 먹먹해지는 굉음과 함께, 거대한 물의 구가 지상을 향해 쏘아졌다.



* * *



몬스터의 종류는 다양하다. 사람과 유사한 체격을 띤 이족보행 몬스터도 있고, 짐승처럼 네발로 걷고 뛰며 그보다 수백 배는 강한 야수형 몬스터도 있다.

종류에 따라 지능도 천차만별이다.

단순무식하지만 미친듯한 피지컬을 타고난 덕분에 상위 몬스터의 한 자리를 차지한 놈도 있고, 무리 사냥을 통해 독, 기습 등의 전술을 펼치지만 신체 능력이 부족한 탓에 최하급으로 분류되는, 고블린 같은 몬스터도 있다.

이처럼 몬스터들의 특성이 다양하니 실제 전문가들 사이에서도, 인터넷 좆문가들 사이에서도 만났다 하면 갑론을박이 오가기 마련이다.

하지만 그럼에도 불구하고, 가장 강력한 몬스터에 대해 말할 때 모두가 첫손가락에 꼽는 종류의 몬스터가 있다.

‘용족(龍族).’

축복받은 지능과 육체를 타고난 존재들. 그리고 오직 그들에게만 허락된 강대한 권능이자 전유물.

‘브레스.’

그런데 도대체. 어째서. 왜.

콰아아아아아!

……이 새끼가 브레스를 쓰는 걸까?
```

## Final English reading copy

```markdown
# Chapter 474

*Kwadeudeuk!*

The instant dozens of whiskers were torn out all at once by Jin Taekyung, the Mutated Water God Dragon opened wide the one eye it had left.

—Krrrrrk…!

It could not believe it.

That some tiny, insignificant human had torn out its whiskers—and with his bare hands, without even a weapon.

It was something that could not happen and should never have happened. Even for the Water God Dragon, which had lived for hundreds of years, it was a shocking first.

And then, in the next moment, the Water God Dragon realized something.

The human who had ripped out its whiskers using nothing but pure physical strength was completely fucking insane.

“Baldy!”

*Ppok!*

“Bald!”

*Ppobok!*

“Smooth, shiny, shaved head!”

*Ppobobobobok!*

—Gwooooooooooar!

A scream rising from the depths of its soul.

The Mutated Water God Dragon thrashed about, howling in agony. For some reason, it did not know why, but the pain and sorrow welling up inside it were dozens of times greater than when it had first lost its eye.

It had to get this mad human off it as soon as possible.

No—before every last whisker was torn out, it had to save at least one!

—Kroaaaaaah!

But unlike the Water God Dragon’s desperate wish, Jin Taekyung had no intention of stopping.

*Puhuk!*

After driving the spearhead between the scales covering the bridge of its nose and pinning himself in place, Jin Taekyung spoke in a sinister voice.

“Hey, know why you can’t walk?”

—Krrk…?

“Because you don’t have two feet. Hell, you don’t even have two hairs.”

*Ppobobobobobok!*

—Gwooooooar!

“Even if you multiplied together all the fur belonging to every spirit beast in the world, the result would still be zero. Because you don’t have any fur. You just don’t. You don’t have a goddamn single hair!”

*Kwadeudeudeuk!*

Jin Taekyung’s hands were more ruthless than ever.

Whenever the whiskers flew toward him in a tangled mass to attack, he caught them with one hand and yanked them out like weeds. Iron-hard skin split open, and whiskers tougher and sharper than Heavenly Silkworm Thread were ripped out in their entirety.

Every last one of them. Without leaving even a single strand behind.

—Uooh, uwooooooar!

Even through the reason clouded like a sky hidden behind storm clouds, the Mutated Water God Dragon was consumed by furious rage and sorrow.

What kind of whiskers were these?

They had grown alongside it for hundreds of years. They were practically companions of its soul.

They were excellent weapons with which to destroy intruders who harbored impudent thoughts, as well as symbols of its power and majesty.

And now those whiskers were gone. They had been pulled out helplessly, like weak and useless seaweed.

And by the hands of a human much smaller and more insignificant than itself!

—Kyaaaaaaaaaow!

A savage roar that shook heaven and earth.

When the master who had ruled Dongting Lake and the Yangtze for hundreds of years began to radiate a baleful aura, everything around it held its breath.

No. Everything changed according to its anger.

*Krrrrrung! Kwa-gwang!*

It was a truly frightening and bizarre sight. Lightning struck without pause from the sky, which was covered in unusually thick black clouds, while rain poured down in a deluge unlike anything seen in the past fifty years.

The river, swollen several times over by the abnormal weather that had continued for several shichen, formed whirlpools of every size that circled around the Water God Dragon.

*Kwaaaaaaaaa!*

And in the middle of that landscape, which resembled a minor catastrophe, stood an enormous body towering like an iron monument.

At the sight of the monster, its eye glowing with an entirely blood-red light, the people on the ground let out quiet groans.

“Good heavens.”

“Damn it. This old man really has lived a long time. I never thought I’d see something this absurd.”

Jeok Cheongang and Mungyeong stared at the unbelievable scene with stunned expressions.

They had long known that beings called spirit beasts and evil beasts possessed astonishing power, but the sight unfolding before them was far beyond anything they had imagined.

A monster as large as a small mountain.

When it swung its tail, cliffs collapsed. When it roared, the world shook in every direction.

And that was not all. Plants, trees, mountains, and rivers held their breath beneath the baleful aura pouring from it, while lightning and water responded to its fury.

Something that belonged in an old, faded legend was happening in reality.

At that moment, a single thought arose in the minds of the two old masters.

*Supernatural powers.*

Things of the strange, prodigious force, rebellion, and ghosts.

It was exactly what those four characters meant.

Uncanny beings and phenomena beyond the understanding of even two men who had spent most of their lives in the Murim were unfolding before them.

But the words *supernatural powers* did not belong to only one being.

*Kwadeuk!*

The sound of flesh being torn was clearly audible even amid the thunder and lightning.

The next moment, scales drenched in dark-blue blood poured down over Jeok Cheongang and Mungyeong’s heads.

One, two, three…

Soon, dozens of scales began to patter down like a sudden shower.

With eyesight like birds of prey, the two men saw what was happening high above them and were rendered speechless.

“Let’s see the flesh underneath! Let’s see what’s inside!”

“……!”

“……!”

*Kwadeudeudeuk!*

Along with a crazed shout, a young man moved his hands like a madman.

One hand gripped the shaft of his spear with all his strength. The other held no weapon at all as his bare hand seized a scale.

Then he yanked hard.

The scale tore free helplessly, trailing dark-blue blood.

—Kwoooooooooar!

The Mutated Water God Dragon thrashed its enormous body and let out a savage cry, but it was useless.

Whenever it sensed something was wrong, Jin Taekyung darted like a ghost into the empty socket where its eye had melted away. Once the monster’s rampage ended, he popped his head back out and resumed his work.

He even threw in a few furious punches for good measure.

“You fucking bastard!”

*Kwaang! Kwang! Kwajijik!*

The Flame-Extinguishing Divine Fist, one of the five most destructive techniques among the Fire Gate Clan’s various secret arts, combined with strength tremendous enough to call him superhuman.

The monster’s head, nearly the size of an average ship, shook violently, and shattered scales rained down.

—Kyaaaaaaaaaow!

The Mutated Water God Dragon was at its wits’ end.

When it still had its whiskers, it had at least been able to attack.

But now that every last one had been pulled out, it had no idea what to do.

Whenever it thrashed to throw him off, he held on with the spear driven into its flesh. Whenever it seemed to calm down, he emerged and tore off more scales.

What the hell was it supposed to do?

Perhaps because it had smashed its head against the cliff so many times, it was beginning to feel dizzy.

*Kwaang! Kwaaaaaang!*

Mungyeong and Jeok Cheongang could only open and close their mouths as they watched.

*This fucking lunatic…*

*What is he doing? It’s not like he’s pulling a radish out of the ground…*

The two men knew how incredibly strong those scales were, which only made them more shocked.

A sloppy Sword Energy wielded by someone who had just entered the Peak realm could not even cut them properly. Only Force could reliably split the scales and damage what lay beneath them.

The scales were that absurdly hard.

And yet that young whelp had simply smashed them apart and ripped them off.

With nothing but his empty bare hands.

*Did he draw up all of his internal energy? Even so, a human’s physical strength should be nowhere near enough.*

*What the… No, wait. If it’s that bastard, then maybe he can.*

Mungyeong felt as though he were dreaming.

Jeok Cheongang, who had watched Jin Taekyung from Shanxi Province until now, found the whole thing both absurd and astonishing.

“What a goddamn lunatic! Hahahaha!”

It was not enough that Jin Taekyung had torn out every single whisker, one of the monster’s weapons. Now he had begun stripping away its scales too.

For a martial artist, it was like breaking all their weapons and stripping away the armor worn over their martial uniform.

From Jeok Cheongang’s perspective, Jin Taekyung’s current insight into martial arts was clearly inferior to that of both old masters—and even below Cheongpung’s.

But his foundation was entirely different.

*He’s simply strong.*

As a martial artist, Jin Taekyung was a powerful fighter who had reached the Supreme Peak realm.

Yet even without the internal energy and martial enlightenment accumulated over several jiazi, he was strong in his own right.

It was as though the power of the heavens had taken residence inside a human body made of nothing but flesh.

“Is that truly possible?”

There was faint astonishment in Mungyeong’s voice.

Jeok Cheongang laughed with delight.

It was a question he had asked himself countless times while training in the Fire Gate Cavern. And every time, Jin Taekyung had responded with an infuriatingly shameless answer.

Now it was time to give that answer to someone else.

“Yes. The Heavenly Martial Physique.”

“……!”

“You find it absurd and ridiculous, don’t you? Good. Don’t try to understand it too quickly. That bastard has always been like that.”

Just as Jeok Cheongang shrugged, Cheongpung spoke with a determined expression.

“Come on, let’s go too. Mimi! Strike with lightning! Whip up a whirlwind!”

……*Chirik, chiriririk?*

“Oh. You can’t.”

“……Neither can that idiot.”

Just as Jeok Cheongang threatened Cheongpung that if he spouted one more load of bullshit, he would make him drink liquor made from a Thousand-Year Poison Horned Snake, an eerie silence and pressure descended over an area several dozen *jang* wide.

*Gugugugugung!*

Jeok Cheongang, Mungyeong, and Cheongpung felt a chill run down their spines and raised their heads.

*Goooooooong.*

A ripple passed through the air.

By then, the wind and rain that had been pouring down without pause had stopped.

So had the lightning.

Everything held its breath.

Everyone on the ground saw the monster’s blood-red pupils, which had been scattering red energy, slowly turn pitch-black.

At the same time, its enormous maw slowly opened, revealing cavernous darkness, while a sphere of water churned as though being sucked into its depths.

*What is that?*

A single question flashed through everyone’s minds.

And then, from high above, came a shout.

No—a scream.

“Get out of the way—!”

Before they could even realize that the voice belonged to Jin Taekyung, the three figures shot forward like the wind.

There might have been differences, great and small, between them, but each one was a Supreme Peak master and an experienced martial artist with exceptional instincts in actual combat.

They could not see through the nature of that thing, but they could tell how terrifying the unknown power was.

Their prediction proved exactly right.

*Kwaaaaaaaaa—!*

Along with a deafening roar, the enormous sphere of water shot toward the ground.

* * *

There are many different kinds of monsters.

Some are bipedal, with bodies resembling human beings. Others are beast-type monsters that move and run on four legs like animals, yet are hundreds of times stronger.

Their Intelligence varies just as widely according to their species.

Some are simple-minded and crude but possess such insane physical abilities that they have earned a place among the high-level monsters.

Others, like goblins, hunt in packs and employ tactics such as poison and ambushes, but are classified as the lowest rank because their physical abilities are so poor.

With monsters possessing such diverse traits, arguments are inevitable whenever the topic comes up—both among actual experts and among every fucking know-it-all on the internet.

Even so, when people talk about the strongest monsters, there is one type that everyone names first.

*Dragonkin.*

Beings blessed with both Intelligence and extraordinary physiques.

And the mighty power granted exclusively to them.

*Breath.*

But seriously.

How?

Why?

*Kwaaaaaaaaaah!*

…Why the hell was this bastard using Breath?
```
