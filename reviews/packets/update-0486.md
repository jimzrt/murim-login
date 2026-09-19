<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0486.txt",
      "sha256": "2d6cf62c81255905b0d95eaeb97bd3b9a194a1ebeebc6a082e988b63cff2c1df",
      "bytes": 13454
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "25a726dadb09774803382ee2f227a5e69929afb3e4bea30628569b177878934d",
      "bytes": 2712
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "f001922cd56cb48fa60ad335dcf50dba727de4c3009706b1e9f4b2409337b2cb",
      "bytes": 155381
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "b4fd86b2ba4961f602e23fc3d51aa19974061b8daa7a7189a39fb9296e22d3e8",
      "bytes": 803
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "4a05a1e6de679ca6d38d80593afac5629a945a210b20f36f4506ca4f31da6680",
      "bytes": 553
    },
    {
      "path": "characters/Hong Dao.md",
      "sha256": "83fffb8e39e5a41e33ecaa81dbe727f6f2aa5ea64d86f31fcb2b4647afd14b6f",
      "bytes": 1001
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "880b967c6a97418c2957c48195df5f827e34db100524a360b212a6c1b9474fcc",
      "bytes": 1547
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "cea498b041e11a266321067fbe1f71f4ff8e23f6014930052406b8d3f24f6a41",
      "bytes": 1777
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "831aeeff4e26d509cbc17db9657b6ca6eaf45f459357b806c45e9be879e30937",
      "bytes": 622
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "1145d99115f36a9b61fb12b97a0ec7375a3ffa2a1741b51af9ab465b7056a1ff",
      "bytes": 786
    },
    {
      "path": "characters/Pill Physician.md",
      "sha256": "820d8fafb67aa4682c414105173aa8440b3a59e073f0eb09e3e1a70c36b92608",
      "bytes": 554
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4f9a2b6f44f23a401944cbb3ff87467abd5f25164948ba8ba22aebcefbbab70a",
      "bytes": 151253
    }
  ],
  "estimated_tokens": 11608
}
-->

# Durable State Update — Chapter 486

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 486. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 486. Profile updates may replace only one
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
  "chapter": 486,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 486,
    "continuity_sources": [486],
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
    "The fissure at the Water God Dragon site is a mostly nonfunctional Gate: entry is impossible, the Gate Conquest Quest cannot be generated, and faint demonic qi leaks from it.",
    "Taekyung suspects Dark Heaven's regeneration, teleportation, and Moving Formation are manifestations of magic connected to the Gate.",
    "Taekyung believes the Gate signals collapsing world laws and an approaching disaster.",
    "Taekyung wonders whether the Lord of Heaven is connected to the dangerous force from his original world.",
    "Taekyung told Jeok that he came from another world, that an evil force from it is linked to Dark Heaven, that the corrupted imugi was their work, and that a fully opened Gate could release monsters.",
    "Jeok trusts Taekyung more deeply than anyone else, but interpreted Taekyung's attempted explanation of his origin as a drawn-out declaration that he wanted to die.",
    "Honglan corrupted the benevolent Dongting Lake imugi and used it to kill many people.",
    "The Dongting Fisherman is alive but severely injured and may be connected to Dark Heaven and the earlier destruction inside the secret refuge.",
    "Gung Gibang traced the vessel connected to Honglan to Red Cliffs.",
    "Cheongpung reported that Zhuge Feng found the Gate site from the Water God Dragon's memories.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Wikyung and Gung Gibang pledged the Jin Family of Taiyuan and the Beggars' Sect to Taekyung's defense."
  ],
  "continuity_sources": [
    484,
    485
  ],
  "open_questions": [
    "What lies beyond the exposed Gate, why has it lost most of its functions, and why can no Gate Conquest Quest be generated?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the Dongting Fisherman's exact role within Dark Heaven, and how was he connected to the earlier destruction inside the secret refuge?",
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations, and how do they relate to the Gate?"
  ],
  "safe_through": 485,
  "temporary_decisions": [
    "Render 기억의 파편 as Memory Fragment.",
    "Render 게이트 공략 as Gate Conquest.",
    "Render 텔레포트 as Teleport and 마법 as Magic.",
    "Render 시산혈해 as sea of corpses and blood.",
    "Retain Old Master for 노야 and the established rough, profane Taekyung-Jeok banter."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 굉도     | **Hong Dao**       |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 법왕     | **Dharma King**               | Hong Dao       |
| 살성     | **Slaughter Saint**           | —              |
| 소림     | **Shaolin**                      |
| 암천     | **Dark Heaven**                  |
| 삼류     | **Third Rate**    |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 영약     | **elixir**                                       |                                                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 제자     | **Disciple**                                 |
| 화신귀무   | **Dance of the Fire God and Demon** |
| 상태               | **Status**                     |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 환의 | **Pill Physician** | Title of the current Family Head of the Seongsu Jang Family. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 선천지기 | **innate qi** | Vital energy said to be damaged by the pill's aftereffects. |
| 설삼 | **snow ginseng** | Elixir compared with the chapter's three selected roots. |
| 천기 | **heavenly patterns** | Celestial patterns Hong Dao studies to perceive major changes and omens. |
| 노환 | **infirmities of old age** | Jeok Cheongang's age-related illness. |
| 태산북두 | **Mount Tai and Northern Dipper of the Murim** | Honorific description of Shaolin's standing in the Murim. |
| 천년설삼 | **Thousand-Year Snow Ginseng** | Secret Zhongnan Sect cargo; a fully digested specimen can grant a full jiazi of internal energy. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 굉도 | old_friends | Hong Dao | familiar and teasing | Uses Hong Dao's personal name in their casual reunion. |
| 굉도 | 적천강 | old_friends | Fire Gate Sect Leader | familiar and teasing | Teases Jeok as the carefree Fire Gate Sect Leader. |
| 굉도 | 진태경 | senior_monk_to_guest_benefactor | Benefactor | formal-polite and probing | Hong Dao repeatedly addresses Taekyung as 시주 while identifying him as the Master of Morning Star. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 진태경 | 문경 | young_martial_artist_to_medical_apprentice | Young Hero | formal-polite | Taekyung addresses the non-martial Mungyeong as 소협 while praising his actions. |
| 문경 | 진태경 | young_passenger_to_younger_martial_artist | Young Hero | deferential | Mungyeong uses 소협 while asking Taekyung for help boarding the ship. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 485
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who seeks Jin Taekyung, Cheongpung, and Jeok Cheongang after escaping the confrontation at Mount Song.
- **Personality:** Calm, confident, theatrically frivolous, casually cruel, and ruthlessly destructive; treats allies as disposable tools and enjoys provoking stronger opponents.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He and the Western Heaven Demon Lord serve the same master; he now seeks to personally kill Cheongpung, Jeok Cheongang, and Jin Taekyung, while his former contact Han Su is dead.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 483
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hong Dao.md

# Hong Dao (굉도)

- **Safe through:** Chapter 484
- **Aliases:** Dharma King
- **Role:** Abbot of Shaolin and the Murim's Dharma King; master of Unnamed and the only friend to whom Jeok Cheongang had opened his heart; after leaving the Star-Array Grand Banquet, he was found in a massive pit with both legs severed and catastrophic internal injuries, whispered final words to Jeok Cheongang, and died.
- **Personality:** Calm, responsible, quietly playful, and still regarded by Jeok as lazy for sleeping whenever possible.
- **Voice:** Quiet, deep, weighty, and resonant, with casual familiarity when speaking to Jeok Cheongang.
- **Relationships:** Old friend of Jeok Cheongang; master of Unnamed; before his death, entrusted the Green Jade Buddha Staff to Unnamed and used his final words to warn Jeok about Jongni Chu, Dark Heaven, Unnamed, and the Buddhist Staff; sends Unnamed to bring the Master of Morning Star to Shaolin.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 485
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin and Furnace Fire Pure Blue, and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 485
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, and can command coordinated raids against powerful monsters.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 485
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 485
- **Aliases:** None
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a former assassin who passed the Divine Physician title to his Disciple, and he has reached the Returned to Youth realm.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple; Jeok Cheongang is an old acquaintance, and Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

### Pill Physician.md

# Pill Physician (환의)

- **Safe through:** Chapter 383
- **Aliases:** None
- **Role:** Current Family Head of the Seongsu Jang Family in Shandong, who personally placed and signed the Thousand-Year Snow Ginseng in the casket entrusted to the Yongbong Escort Bureau.
- **Personality:** No personality traits are established.
- **Voice:** No voice traits are established.
- **Relationships:** The Pill Physician heads the Seongsu Jang Family, a prestigious medical family in Shandong.

## Korean source

```text
＃486화



“잠깐 이야기 좀 할까?”

“싫다. 꺼져라.”

“그렇군.”

한 치의 망설임도 없이 가까워지는 적천강의 모습에, 문경의 눈썹이 꿈틀거렸다.

“싫다고 했을 텐데.”

“들었다. 그래서?”

“역시 말이 안 통하는군. 나이는 뒷구멍으로 먹었나?”

“어린놈이 어르신한테 못하는 말이 없구나. 노부가 네놈보다 족히 예닐곱 살은 더 먹었느니라.”

“도대체 나이가 몇 살이길래 그런…….”

“허벅지 살이다. 이 대가리에 피도 안 마른 어린놈아.”

“참으로 개 같은…… 됐다. 말을 말아야지.”

순간 울컥했던 문경은 고개를 절레절레 저었다.

겉모습은 젊다 못해 어려 보이는 소년이지만 그 역시 장장 백여 년의 인생을 걸어온 노인.

하지만 적천강과 대화를 하고 있다 보면 평정심을 잃은 어린애가 되는 기분이었다.

‘사람 열 받게 하는 데에는 도가 텄군. 스승이나 제자나 아주 쏙 빼닮았어.’

적천강과 진태경. 이 두 사람이라면 세 치 혓바닥으로 누군가의 울화통을 터트려 죽일 수 있을 것도 같았다.

그에 비하면 지금쯤 사천에서 병자들을 돌보고 있을 늙은 제자는 부처의 환생이나 다름없었다.

‘보고 싶구나. 잘 지내고 있느냐?’

문경이 자신의 착한 제자를 그리워하는 사이. 휘적거리는 팔자걸음으로 다가온 적천강이 바위에 걸터앉았다.

“뭘 보고 있었나?”

“그걸 대답해 줘야 할 이유는 없지.”

“나쁘지 않은 선택이야. 그럼 날이 밝을 때까지 이러고 있자고. 늙은이 둘이서 오붓하게.”

“하나는 알고 둘은 모르는군. 떠나면 그만이다.”

“둘은 알고 셋은 모르나 본데, 노부가 오늘만 이럴 것 같나?”

“……!”

“오늘, 내일, 모레. 글피. 안 그래도 늙으니 잠이 없어져서 적적했는데, 이것도 나쁘지 않겠군.”

돌아서려던 문경의 신형이 우뚝 멈췄다. 파르르 떨리는 눈꺼풀로 적천강을 바라보던 그가 탄식하듯 중얼거렸다.

“악랄한 늙은이 같으니.”

“흠. 이제사 겨우 대화를 나눌 준비가 된 모양이로군.”

“……찾아온 용건을 말해라.”

“이야기가 좀 길어질 수도 있을 것 같은데.”

“최대한 짧게.”

“최대한 짧게라.”

새카맣게 물든 강물을 바라보던 적천강이 한마디를 툭, 내뱉었다.

“앞으로 그놈, 잘 봐줘.”

“뭐?”

잠시 미간을 좁혔던 문경이 입을 열었다.

“그놈이라면, 진태경?”

“그래. 진태경 그놈 말고 또 누가 있나?”

“그걸 왜 나한테 부탁하는 거지?”

“글쎄. 잘 모르겠군.”

적천강은 문득 고개를 들어 하늘을 바라보았다.

휘영청 떠 있는 보름달. 닿을 수 없는 그곳으로부터 쏟아진 빛이 유난히도 환하다.

“갑자기 그런 생각이 들었어. 노부가 언제까지 그놈과 함께할 수 있을까 하는, 그런 생각.”

일백 년의 세월, 참으로 길었다.

강산은 변했고 왕조(王朝)가 뒤바뀌었다. 그리고…… 어린 소년은 백발의 노인이 되었다.

적천강을 물끄러미 바라보던 문경이 나직하게 뇌까렸다.

“늙었군.”

“그래. 늙어 버렸어.”

세월의 흐름에 따라 늙고 해진 것은 몸뚱어리뿐만이 아니다. 보이지 않는 감정과 마음 역시 천천히 마모되어 닳아 없어진다.

어느 순간 문득 죽음을 떠올렸을 때, 누군가의 곁에 얼마나 더 오래 머무를 수 있을까 생각했을 때 사람은 늙었다는 사실을 깨닫는다.

바로 지금의 적천강처럼.

그리고 문경은 현재 적천강의 마음을 누구보다 잘 이해할 수 있는 유일한 사람이었다.

“심마(心魔)가 찾아왔나?”

“심마라, 오래됐지.”

적천강은 자조 섞인 웃음을 흘렸다.

자식처럼 키웠으나 살귀(殺鬼)로 자라난 옛 제자가 떠난 후부터, 그의 마음엔 진한 먹구름이 드리워져 있었다.

그리고 그때 느꼈던 슬픔과 죄책감은 수십여 년간 족쇄처럼 적천강의 심신을 옥죄었다.

어느 날 갑자기 나타난, 진태경이라는 빛이 내리쬐기 전까지.

“이제는 아픈 과거야. 그저 기억할 뿐, 고통스럽지는 않은.”

“그렇다면 왜?”

“초조해졌으니까.”

심마라는 놈은 형태가 정해져 있는 것이 아니다. 마음을 어지럽히고 깨달음을 방해하는 장애물.

지금 적천강을 사로잡은 심마는 초조함이라는 감정이었다.

“이십 년, 아니 십 년만 더 일찍 그 녀석을 만났다면 좋았을 텐데…… 너무 늦어 버렸어.”

적천강은 손을 들어 달을 가렸다. 자신과 달리 조금도 늙지 않은 저 환한 달빛이 주름진 얼굴을 비추는 것이 싫었다.

“예전 같지 않아. 몸도, 마음도. 그나마 지금까지 버틸 수 있었던 것도 녀석이 있었기에 가능했던 게지.”

구화산(九華山)에서 보낸 일 년 동안 성장한 것은 진태경만이 아니었다.

적천강 역시 가르침을 통해 약간의 깨달음을 얻었고, 그 덕분에 가파르게 달려가던 노환의 발걸음을 붙잡을 수 있었다.

하지만.

“이미 알고 있었잖나. 노부의 선천지기(先天眞氣)가 상했다는 것을.”

선천지기, 혹은 진원진기(眞元眞氣)라 불리는 기운은 인체를 이루는 모든 것의 원천이자 생명력, 그 자체다.

하남에서의 일을 떠올린 적천강의 입가에 씁쓸한 미소가 맺혔다.

“후회하진 않네. 그 아이를 살리기 위해서라면 뭐든 했을 테니까.”

적천강의 말은 진심이었다. 열 번, 백 번을 다시 돌아간다 해도 그는 같은 선택을 했을 것이다. 그만큼 당시의 상황은 절박했다.

생명력이나 다름없는 선천지기를 끌어올려 부족한 공력을 대신할 만큼.

그렇게 한때나마 혈주를 죽음의 문턱까지 끌어당겼던 화신귀무(火神鬼舞)에는, 자신의 생명력을 장작으로 불태운 늙은 스승의 결의가 깃들어 있었다.

“충분히 각오했던 일이었어. 설령 살아난다 해도 예전 같지는 않으리라 짐작했지.”

말없이 적천강을 바라보던 문경이 나직한 목소리로 입을 열었다.

“그랬을 거다. 그 녀석이 구해 온 천년설삼(千年雪蔘)이 아니었다면.”

“그래, 모두 천운이었지. 그 아이가 자네를 찾아낸 것도.”

그러나 두 사람은 알고 있었다.

희대의 영약인 천년설삼과 의술이 하늘에 닿았다는 신의의 치료로도 적천강의 선천지기를 되돌릴 수는 없다는 것을.

이 모든 것은 임시방편에 불과하다.

커다란 바위로 무너진 둑을 틀어막는다고 해도, 둑 안에 갇혀 있던 물줄기는 작은 빈틈을 통해 천천히 조금씩, 그리고 쉼 없이 흘러나오고 있었다.

“그것 때문에 나를 찾아온 건가? 그 녀석을 부탁하려고?”

“글쎄, 어떨 것 같나?”

되묻는 적천강을 보며 작게 혀를 찬 문경이 말을 이었다.

“늙어서 그런지 걱정도 많아졌군. 그런 고민은 몇 년 뒤에 해도 늦지 않는다.”

사람마다 품은 기운의 크기도, 그릇도 다르다.

평범한 양민이나 삼류 무인이 작은 개울이라면, 적천강은 끝없이 펼쳐진 바다였다.

계속되는 선천지기의 소실로 인해 천천히 힘을 잃겠지만, 이미 적천강의 몸 상태를 파악하고 있는 문경이 보기에 그의 걱정은 이른 감이 없지 않았다.

“노부의 몸이니 익히 알고 있네. 적어도 오늘 당장 죽지는 않겠지.”

“그러니 허튼 생각 그만하고 돌아가. 차라리 이 시간에 그 녀석을 붙잡고 한 수라도 더 가르치는 것이 나을 테니.”

“하지만 내일 무슨 일이 벌어질지는 모르는 일이지.”

“뭐?”

“선천지기가 조금씩 사라져서, 어느 날 갑자기 급사할까 봐 찾아온 거라 생각하나?”

미간을 좁히는 문경을 응시하며, 적천강이 천천히 말을 이었다.

“느껴져. 점차 쇠약해지고 있다는 것이. 이미 정마대전 때도 느끼지 못했던 죽을 고비를 여러 번 넘겼지. 이런 노부가 앞으로도 이어질 숱한 전투에서 버틸 수 있을지는…… 저 하늘 위에서 지켜보고 있을 빌어먹을 누군가만 알고 있겠지.”

“……!”

“굉도, 그 친구가 그런 말을 한 적이 있네. 천기(天氣)가 어그러지고, 정마대전 때보다 거대한 환란이 다가오고 있다고.”

법왕 굉도의 예측은 현실로 이루어졌다.

불과 일 년 뒤, 무림의 태산북두인 소림이 피와 시체로 뒤덮였고, 술과 고기를 좋아하던 현명한 고승은 죽음을 맞이했다.

어느덧 암천이라는 먹구름은 하남과 사천, 호북에까지 드리워졌다.

그리고 적천강은 알 수 있었다. 저 먹구름이, 곧 머지않아 천하를 뒤덮으리라는 것을.

“이보게, 살성.”

문경을 바라보는 적천강의 눈빛에 짙은 회한이 묻어 나왔다.

“알 수 없는 일들이 벌어지고 있네. 우리가 알고 있던 모든 것이 무너지고 있어.”

세인들은 흔히들 무림을 장강에 빗대어 말하고는 한다.

장강후랑추전랑(長江後浪推前浪). 장강의 뒷물결이 앞 물결을 밀어 낸다는 말이 있는 것도 그 때문이다.

그러나 지금 암천이 천하 곳곳에서 벌이고 있는 일들과 기이한 현상들은…… 장강이 아니라 하늘과 땅을 뒤엎는 역천(逆天)과도 같았다.

적천강과 문경. 장장 일백여 년의 세월을 살아온 두 노인이 알고 있던 모든 법칙은 산산이 부서져 무너지고 있었다.

‘만약 진태경. 그 아이가 한 말이 사실이라면 더더욱. 아니, 아니지. 그럴 리 없어. 아니어야 한다.’

적천강은 순간 뇌리에 스치는 생각을 애써 털어냈다.

진태경이 늘 그랬던 것처럼 농담처럼 던진 실없는 헛소리일 뿐이다.

정확히는 그렇게 믿고 싶었다.

이미 몸과 마음이 늙고 마모된 적천강은 아직 그러한 충격적인 이야기를 받아들일 준비가 되지 않았다.

“어쨌건 노파심에 부탁하는 거야. 이 지랄 같은 무림에서는 무슨 일이 벌어져도 이상하지 않으니까. 노부처럼 나날이 쇠약해지는 늙은이 하나 죽는다 한들, 그리 놀라운 일은 아니지.”

문경은 묘한 눈빛으로 적천강을 응시했다.

화왕(火王)이라 불리는 거인은 오늘따라 유독 작아 보였고, 언제 찾아올지 모르는 죽음을 입에 올리는 담담한 목소리는 유난히도 귓가에 맴돌았다.

‘부탁. 부탁이라.’

바로 그 화왕의 입에서 나온 단어라고는 믿어지지 않을 정도다.

천천히 몸을 일으키는 적천강을 말없이 바라보던 문경이 내심 중얼거렸다.

‘이런, 나도 늙었군.’

비록 몸은 어려졌지만, 마음은 낡았다.

오랜 세월 비 한 방울 내리지 않던 마음 한구석이 축축하게 젖어드는 것은 그러한 이유 때문일 것이다.

“……후.”

문경이 작게 한숨을 내쉰 그때, 무거운 엉덩이를 뗀 적천강은 이미 손을 흔들며 돌아서고 있었다.

“이만 가 보지. 달구경 잘하게.”

“뭐?”

이게 무슨 소린가.

잠시 뇌정지가 온 문경이 가까스로 입을 열었다.

“간다니?”

“가야지. 방해꾼이 사라져 준다는데 고맙지 않나?”

“난 아직 대답하지 않았다.”

“무슨 소리. 대답은 이미 들은 것 같은데.”

“잠깐. 그게 무슨…….”

“대답, 잘 들었네. 젊은 친구.”

“아니 뭐 이런 미친 늙은이가.”

어지간해서는 깨지지 않는 평정심이 와르르 무너진다.

황당한 표정으로 멀어지는 적천강의 뒷모습을 바라보던 문경이 외쳤다.

“나보고 어쩌란 말이냐!”

“이것저것 가르쳐 줘. 필요한 마음가짐이라든지, 독문 무공 중에 쓸 만한 거 있으면 비급 좀 찔러 주고.”

“독문 무공? 비급?”

문경은 순간 자신의 귀를 의심했다.

독문 무공은 한 사람, 혹은 문파의 모든 심득이 담긴 결정체나 다름없다. 만금을 줘도 가르쳐 줄 수 없고, 목숨보다 귀중한 것이기도 했다.

그런데 그 독문 무공을, 그것도 남의 제자에게 가르쳐 주라니.

문경은 진심을 담아 물었다.

“……혹시 노망이 나서 독문 무공이 뭔지 까먹었나?”

“아는데. 그거 뒀다가 똥 닦을 때 쓸 거 아니면 좀 알려 줘 봐.”

“이런 미친.”

“어차피 따로 알려 줄 만한 사람도 없잖나. 사천에 있는 늙은 제자는 계속 사람 살리게 놔두고, 우리 애한테 잘 죽이는 법 좀 가르쳐 달라고.”

그걸 지금 말이라고 하는 건가?

문경이 하도 어이가 없어 할 말을 잃은 사이, 제 할 말만 끝마친 적천강은 저 멀리 내빼고 있었다.

쐐애애액!

“이런…… 개 같은 일이.”
```

## Final English reading copy

```markdown
# Chapter 486

“Can we talk for a moment?”

“No. Get lost.”

“I see.”

At Jeok Cheongang’s approach without a moment’s hesitation, Mungyeong’s brow twitched.

“I said no.”

“I heard you. So?”

“You really are impossible to reason with. Did you eat your age through your ass?”

“Young punk, you really say anything to an elder. This old man is at least six or seven years older than you.”

“Just how old are you to say some—”

“Thigh meat, you wet-behind-the-ears brat.”[^1]

[^1]: The Korean word *sal* can mean both “years of age” and “flesh,” allowing Jeok Cheongang to twist Mungyeong’s question about his age into “thigh meat.”

“What a goddamn—Forget it. I shouldn’t bother talking to you.”

Mungyeong, who had felt his temper flare for a moment, shook his head over and over.

He looked like a boy—young enough to seem almost childish—but he had also lived a full century or more.

Yet whenever he spoke with Jeok Cheongang, he felt like a child who had lost his composure.

*He’s a master at pissing people off. Master and Disciple really are two peas in a pod.*

With those two—Jeok Cheongang and Jin Taekyung—it seemed entirely possible for them to talk someone to death with nothing but their three-inch tongues.

Compared to them, the old Disciple currently caring for patients in Sichuan was practically the reincarnation of Buddha.

*I miss him. I wonder if he’s doing well.*

As Mungyeong thought about his kind Disciple, Jeok Cheongang approached with a loose, shambling gait and sat down on a rock.

“What were you looking at?”

“There’s no reason I need to answer that.”

“Not a bad choice. Then let’s sit here until dawn. Just the two of us old men, enjoying some quality time together.”

“You understand one thing and miss the other. I can simply leave.”

“You seem to understand two things while missing three. Do you think this old man is only going to do this today?”

“...!”

“Today, tomorrow, the day after tomorrow. The day after that. I’ve already gotten old enough that I barely sleep and spend most of my time bored. This might not be so bad.”

Mungyeong, who had been about to turn away, stopped dead. He stared at Jeok Cheongang with trembling eyelids, then muttered with a sigh,

“You vicious old bastard.”

“Hm. Looks like you’re finally ready to talk.”

“Tell me why you came.”

“This might take a while.”

“Make it as short as possible.”

“‘As short as possible,’ huh?”

Jeok Cheongang gazed at the river, its waters dyed pitch-black, and tossed out a single sentence.

“Look after that brat from now on.”

“What?”

After furrowing his brow for a moment, Mungyeong spoke.

“By ‘that brat,’ you mean Jin Taekyung?”

“Yes. Who else would I mean besides that brat Jin Taekyung?”

“Why are you asking me to do that?”

“Who knows? I’m not sure myself.”

Jeok Cheongang suddenly lifted his head and looked up at the sky.

The full moon hung brilliantly overhead. Its light poured down from that unreachable place, unusually bright.

“I suddenly started wondering how long I’d be able to stay with that brat.”

A hundred years was a very long time.

Mountains and rivers had changed, and dynasties had risen and fallen. And… a young boy had become a white-haired old man.

Mungyeong gazed at Jeok Cheongang and murmured quietly,

“You’ve grown old.”

“Yes. I’ve grown old.”

It was not only the body that grew old and worn with the passing of time. Invisible emotions and the heart itself were also slowly ground down until they disappeared.

A person realized they had grown old when they suddenly thought of death, or wondered how much longer they could remain beside someone.

Just as Jeok Cheongang was doing now.

And Mungyeong was the only person who could understand Jeok Cheongang’s feelings better than anyone else.

“Has the Heart Demon come calling?”

“The Heart Demon? That was a long time ago.”

Jeok Cheongang let out a self-deprecating laugh.

After the former Disciple he had raised like a son grew into a murderous fiend and left, a thick cloud had hung over his heart.

The sorrow and guilt he had felt then had bound Jeok Cheongang’s body and mind like shackles for decades.

Until the light called Jin Taekyung suddenly appeared one day and shone down upon him.

“It’s a painful memory now. I only remember it. It doesn’t hurt anymore.”

“Then why?”

“Because I’ve grown anxious.”

The Heart Demon had no fixed form. It was any obstacle that disturbed the heart and interfered with enlightenment.

The Heart Demon that had seized Jeok Cheongang now was anxiety.

“I wish I’d met that boy twenty years earlier. No, even ten years earlier would have been good… But I met him too late.”

Jeok Cheongang raised a hand and covered the moon. He hated how that bright moonlight—which had not aged even a day, unlike him—illuminated his wrinkled face.

“I’m not what I used to be. Not my body, nor my heart. The only reason I’ve managed to endure this long is because of that boy.”

Jin Taekyung was not the only one who had grown during the year they spent on Mount Jiuhua.

Through teaching Taekyung, Jeok Cheongang had also gained a small measure of enlightenment, and thanks to that, he had managed to halt the rapid advance of his infirmities of old age.

But still—

“You already knew, didn’t you? That my innate qi had been damaged.”

Innate qi, also called true-origin qi, was the source of everything that made up the human body. It was life force itself.

Remembering what had happened in Henan, Jeok Cheongang wore a bitter smile.

“I don’t regret it. I would have done anything to save that boy.”

Jeok Cheongang meant every word. Even if he could go back ten times or a hundred times, he would have made the same choice. The situation had been that desperate.

He had drawn upon the innate qi that was practically his life force to make up for his insufficient internal energy.

The Dance of the Fire God and Demon, which had once dragged the Blood Lord to the brink of death, carried the resolve of an old Master who had burned his own life force as fuel.

“I had fully prepared myself for it. Even if I survived, I knew I wouldn’t be the same as before.”

Mungyeong watched Jeok Cheongang in silence before speaking in a low voice.

“You wouldn’t have been. Not without the Thousand-Year Snow Ginseng that boy brought back.”

“Yes. It was all heavenly luck. Even the fact that he found you.”

But the two men knew the truth.

Not even the Thousand-Year Snow Ginseng, a legendary elixir, or the treatment of the Divine Physician, whose medical skill was said to reach the heavens, could restore Jeok Cheongang’s innate qi.

All of it was merely a stopgap.

Even if one blocked a collapsed dam with a massive boulder, the water trapped behind the dam would continue to seep through a small gap—slowly, little by little, without pause.

“Is that why you came to me? To ask me to look after him?”

“Who knows? What do you think?”

Mungyeong clicked his tongue softly at Jeok Cheongang’s question and continued,

“You’ve grown more worried with age. It wouldn’t be too late to worry about that a few years from now.”

Every person possessed a different amount of qi and a different vessel to contain it.

If an ordinary commoner or Third Rate martial artist was a small stream, Jeok Cheongang was an endless sea.

He would slowly lose strength as his innate qi continued to disappear, but Mungyeong already understood the state of Jeok Cheongang’s body. From his perspective, there was no denying that Jeok Cheongang’s concern was premature.

“This is my body. I know it well. At least I won’t die today.”

“Then stop thinking foolish thoughts and go back. You’d be better off spending this time grabbing that brat and teaching him one more move.”

“But no one knows what might happen tomorrow.”

“What?”

“Do you think I came because I’m worried that my innate qi will gradually disappear and I’ll suddenly drop dead one day?”

Jeok Cheongang stared at Mungyeong’s furrowed brow and continued slowly.

“I can feel it. I can feel myself growing weaker. I’ve already survived several brushes with death unlike anything I faced even during the Great Faction War. Whether someone like me will be able to endure the countless battles ahead… Only some damned bastard watching from up in the heavens knows.”

“...!”

“Hong Dao once said something to me. That the heavenly patterns were becoming distorted, and a calamity greater than the Great Faction War was approaching.”

Dharma King Hong Dao’s prediction had become reality.

Only a year later, Shaolin—the Mount Tai and Northern Dipper of the Murim—had been covered in blood and corpses, and the wise high monk who loved alcohol and meat had met his death.

By then, the dark cloud called Dark Heaven had spread over Henan, Sichuan, and Hubei.

And Jeok Cheongang understood. That dark cloud would soon cover the entire world.

“Listen, Slaughter Saint.”

Deep regret showed in Jeok Cheongang’s eyes as he looked at Mungyeong.

“Things we cannot understand are happening. Everything we knew is collapsing.”

People often compared the Murim to the Yangtze.

*The waves behind on the Yangtze push the waves ahead.* That was why the saying existed.

But the strange phenomena and events Dark Heaven was causing throughout the world now… were not like the Yangtze. They were more like an act of defying heaven itself—turning heaven and earth upside down.

Everything Jeok Cheongang and Mungyeong had known, every law they had understood across more than a century of life, was shattering and collapsing.

*If what Jin Taekyung said is true, then even more so. No. No, that can’t be. It mustn’t be.*

Jeok Cheongang forcibly brushed the thought from his mind as it flashed through it.

It was nothing more than another ridiculous piece of nonsense tossed out like a joke, just as Jin Taekyung always did.

More precisely, that was what Jeok Cheongang wanted to believe.

His body and heart had already grown old and worn. He was not yet ready to accept such a shocking story.

“Anyway, I’m only asking to put my mind at ease. Anything can happen in this goddamn Murim. It would hardly be surprising if an old man growing weaker by the day were to die.”

Mungyeong stared at Jeok Cheongang with a strange look in his eyes.

The giant known as the Fire King seemed unusually small today, and his calm voice as he spoke of a death that could come at any moment lingered in Mungyeong’s ears.

*Asking. He’s asking me.*

It was hard to believe that word had come from the mouth of the Fire King himself.

Mungyeong silently watched Jeok Cheongang rise to his feet.

*Damn. I’ve grown old too.*

Though his body had grown young, his heart was old.

That must have been why one corner of his heart—which had not felt a single drop of rain in many years—was growing damp.

“...Hah.”

Just as Mungyeong let out a small sigh, Jeok Cheongang had already hauled his heavy backside to his feet and was turning away with a wave.

“I’ll be going. Enjoy the moonlight.”

“What?”

What was he talking about?

Mungyeong’s mind briefly stopped working. With difficulty, he opened his mouth.

“You’re leaving?”

“Of course. Shouldn’t you be grateful that this nuisance is leaving?”

“I haven’t answered you yet.”

“What do you mean? I believe I’ve already heard your answer.”

“Wait. What are you—”

“I heard your answer loud and clear, young friend.”

“No, what kind of crazy old bastard—”

The composure that rarely broke came crashing down all at once.

Mungyeong stared at Jeok Cheongang’s retreating back with an incredulous expression and shouted,

“What do you expect me to do?”

“Teach him a few things. The mindset he needs, for example. And if any of your secret martial arts might be useful, slip him a manual.”

“Your secret martial arts? A manual?”

For a moment, Mungyeong wondered if he had heard correctly.

An individual’s or sect’s secret martial arts were practically the crystallized essence of everything they had learned. They were too precious to hand over even for ten thousand pieces of gold and more valuable than one’s life.

Yet Jeok Cheongang was telling him to teach those secret arts to someone else’s Disciple.

Mungyeong asked with complete sincerity,

“...Have you grown senile and forgotten what secret martial arts are?”

“I know exactly what they are. Unless you’re planning to save them for wiping your ass, why don’t you teach him?”

“You insane bastard.”

“You don’t have anyone else to teach them to anyway. Let your old Disciple in Sichuan keep saving people, and teach our boy how to kill properly.”

Was that something he could say with a straight face?

Mungyeong was so dumbfounded that he lost the power of speech. Meanwhile, having finished saying everything he wanted to say, Jeok Cheongang was already sprinting away into the distance.

*Whoosh!*

“What the… Goddamn it.”
```
