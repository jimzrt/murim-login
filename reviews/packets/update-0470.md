<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0470.txt",
      "sha256": "df251f6ca9dd1f1ade922df4afbf758e4c75468ace44398257da1ec34e221617",
      "bytes": 12828
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "45ebd2d7921567c5e411c49883b783972630978166dcc78f53467e9d36309b53",
      "bytes": 3936
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a7f5cad9a692409fa4912f9b98145afb8e8b89186b02866e98d6e5cc71b73552",
      "bytes": 152441
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "10710a863a33f5d604459e4a7d7286d5165a47ef08ab6e8237c71fdeb45d32ee",
      "bytes": 1006
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "11f364c61c18dacb207ad820b231b75509df90ec597da9a06ba9aa801610ad9d",
      "bytes": 553
    },
    {
      "path": "characters/Dongting Fisherman.md",
      "sha256": "349f60cd625b36c5c62c420e2c0fac7d4da51c2b6cd558341546bfbc23ce21c0",
      "bytes": 778
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "904b798bcb45bd3b32fff983f1814fd499c39843dc3390a0de7c797c7cc510c9",
      "bytes": 662
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "6f6c8595dcb246f1d36882d2386b14cb8f192580fcabc3b352e3285346930c68",
      "bytes": 1108
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "42089f10e34667cdf7d94a60943ce8eb041f0cc698d52185538fa450955fe593",
      "bytes": 1646
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "a5ce54d12bf628f63a8515fc58f7cc237c9fe131076c255484c327cb52b47bcd",
      "bytes": 622
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "02c75e82577b427aa72f777610f13623d2bfa8352fe24570f94fb4b00282bace",
      "bytes": 147215
    }
  ],
  "estimated_tokens": 11813
}
-->

# Durable State Update — Chapter 470

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 470. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 470. Profile updates may replace only one
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
  "chapter": 470,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 470,
    "continuity_sources": [470],
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
    "The Dongting Fisherman remains severely injured, immobilized by Taekyung's seals, and held alive for interrogation about Dark Heaven.",
    "Taekyung believes the Dongting Fisherman encountered the Mutated Water God Dragon before the group and that its Fear caused his apparent mental disturbance.",
    "Taekyung suffered only a minor internal injury from the Dongting Fisherman's Inner-Family Heavy Hand and remains capable of fighting, but his iron spear cannot pierce the creature's scales.",
    "Honglan survived the Dongting Lake disaster and is recovering; Ju Wongong remains unconscious under guard after passing the most dangerous stage of his injuries.",
    "Jin Wikyung is acting as an inspector for the new Murim Alliance and is cooperating with Taekyung's investigation.",
    "The shared symbols between the Arch Lich's magic circle and Dark Heaven's formations remain unexplained.",
    "The Sea Serpent Society and three Yangtze River Channel League strongholds, including Donghu Stronghold, were destroyed with more than a thousand casualties, while the perpetrators' wider plans remain unknown.",
    "The captured Three Fiends is a former-generation great fiend and Supreme Peak Dark Heaven subordinate whom Taekyung is transporting alive to investigate possible codes or markings.",
    "An unprecedented storm over Dongting Lake prevented ordinary passage; Mu Song brought his best sailors from Water Dragon Stronghold, and Jeok Cheongang opened a route through the storm by destroying a waterspout.",
    "Jeok Cheongang, Mungyeong, and Zhuge Feng are moving toward Taekyung's location, while Hyeongong remains behind.",
    "A giant Mutated Water God Dragon, also known locally as Dongting Lake's Two-Horned Beast or Water God Dragon, has emerged and possesses a monster's Fear.",
    "The creature's Fear overwhelmed Hyuk Mujin and Gung Gibang, while Taekyung and Cheongpung resisted it."
  ],
  "continuity_sources": [
    469,
    468
  ],
  "open_questions": [
    "What is the Dongting Fisherman's exact role within Dark Heaven, what information will he reveal, what caused his involuntary movement and terrified warning, and was his prior mental disturbance caused by the creature's Fear?",
    "What caused the earlier deliberate destruction inside the refuge, and how was it connected to the Dongting Fisherman or another intruder?",
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Who destroyed Donghu Stronghold and the related Yangtze River Channel League strongholds, why was no Moving Formation trace left, and was the destruction a diversion?",
    "What is the sharp, armor-hard object carried by Jeok Cheongang, and what are the true origin, relationship to the known Sea Serpent, and purpose of the Mutated Water God Dragon?"
  ],
  "safe_through": 469,
  "temporary_decisions": [
    "Render 천잠사 as Heavenly Silkworm Thread, 운철 as meteorite iron, 초인 as superhuman, and 극쾌 as extreme swiftness.",
    "Render 노괴 as old monster, 신병이기 as divine weapon, 수상 구조대원의 물갈퀴 as Water Rescue Worker's Webbed Feet, and 수상 구조대원의 아가미 as Water Rescue Worker's Gills.",
    "Preserve Taekyung's dry contemporary humor and blunt profanity, render 씨부럴 as sibu-leol in direct abuse, and preserve the Dongting Fisherman's emotionless, inhuman presentation and violent combat voice.",
    "Continue rendering 오기조원 as Five Qi Returning to Origin, 노화순청 as Furnace Fire Pure Blue, 반로환동 as Returned to Youth, 복자 as diviner, 일위도강 as Single Reed Crossing the River, and 장제자 as Senior Disciple.",
    "Render 변이된 수신룡 as Mutated Water God Dragon, 이각수 as Two-Horned Beast, 수신룡 as Water God Dragon, 시 서펜트 as Sea Serpent, and 피어 as Fear."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 초식     | **form**                                         | Numbered technique movement                           |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 살기     | **killing intent**                               |                                                       |
| 제자     | **Disciple**                                 |
| 은인     | **Benefactor**                               |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 로그아웃             | **Logout**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 화산     | **Huashan**            |
| 귀가      | **your family**                                                 |
| 소협      | **Young Hero**                                                  |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동정어옹 | **Dongting Fisherman** | Publicly condemned the Yangtze River Channel League and disappeared three days before this chapter. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 화룡일미 | **Fire Dragon's Single Tail** | A form of the Fire Dragon Divine Spear. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 미미쨩 | **Mimi-chan** | Affectionate form used for Tang Mimi. |
| 삼괴 | **Three Fiends** | Collective form used by the Western Heaven Demon Lord for the Qilian Three Fiends. |
| 나룻배 | **ferryboat** | Small ferry used to reach the suspected refuge site. |
| 사공 | **boatman** | Old boatman piloting the ferryboat. |
| 호북성 | **Hubei Province** | Province where the chapter’s Dark Heaven incidents occurred. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |

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
| 청풍 | 미미 | handler_to_companion_snake | Mimi | cheerful-commanding | Cheongpung repeatedly calls and commands the Thousand-Year Poison Horned Snake. |
| 진태경 | 삼괴 | interrogator_to_captured_enemy | Three Fiends | threatening and coercive | Taekyung addresses the captured fiend by his collective sobriquet while demanding information about Dark Heaven, Hubei, and the Dongting Fisherman. |
| 삼괴 | 진태경 | captured_enemy_to_interrogator | you bastard | defiant and profane | The Three Fiends curses Taekyung, challenges him to remove the seal, and demands death rather than continued torture. |
| 진태경 | 미미 | rescuer to companion snake | Mimi or Mimi-chan | informal, pleading | Taekyung calls to Mimi while asking the snake to carry him and the survivors. |
| 진태경 | 사공 | passenger_to_boatman | Boatman | commanding | Taekyung orders the boatman to continue to the final site and asks how long the journey will take. |
| 혁무진 | 사공 | passenger_to_boatman | Boatman | weighty-commanding | Mujin presses the boatman to depart despite the worsening conditions. |
| 진태경 | 동정어옹 | hostile interrogator confronting a suspected perpetrator | you | blunt informal and abusive | Taekyung addresses the Dongting Fisherman without honorifics and calls him a sibu-leol bastard. |
| 궁기방 | 사공 | passenger to ferryboatman | Boatman | direct and formal-polite | Addresses the old boatman as 사공 while challenging his refusal to sail. |
| 사공 | 진태경 | ferryboatman to honored martial guest | Great Hero | fearful and deferential | Repeatedly addresses Taekyung as 대협 while explaining the storm and the boat’s limits. |
| 진태경 | 수신룡 | hostile martial artist to monster | you, sibu-leol eel bastard | blunt, insulting, and fearless | Taekyung directly insults the emerged Water God Dragon before attacking it. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 469
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 469
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Dongting Fisherman.md

# Dongting Fisherman (동정어옹)

- **Safe through:** Chapter 469
- **Aliases:** None
- **Role:** The Dongting Fisherman is a previous-generation Supreme Peak master whose water arts rival the Seafaring King; he joined Dark Heaven, committed the Dongting Lake massacre, and is now captured alive for interrogation.
- **Personality:** The Dongting Fisherman appears eerily emotionless and savage, eating live fish raw and reacting violently when provoked.
- **Voice:** Not established.
- **Relationships:** The Dongting Fisherman opposed the Yangtze River Channel League and was monitored by the Lower District Sect for several years after friction with it, while current records place him in Hubei Province.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 469
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung and uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and search for Dark Heaven’s Hubei forces.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 469
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 469
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, and is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 469
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃470화



아니, 이게 도대체 무슨 상황이야.

일 분 일 초가 급한 와중에도 잠깐 멍해진 내가 간신히 입을 열었다.

“자, 잠깐만. 청 소협.”

“태어나서 저런 건 처음 봤어요. 할아버지 말씀대로 역시 천하는 넓어요! 화산에서 나오길 잘했어요!”

“아니, 천하가 넓은 건 맞는데 저건 그거랑 아무런 상관이…….”

“와아아아! 방금 또 움직였어요!”

“…….”

귓등으로도 안 듣는군.

청풍이 살짝 맛이 간 놈이라는 건 진작부터 알고 있었지만, 이 정도일 줄은 상상도 못 했다.

‘뭐 이런 인간이 다 있냐.’

몬스터를 부모님보다 자주 만나는 베테랑 헌터도 저만한 크기의 초대형 몬스터를 마주한다면 저절로 공포심이 들기 마련이다.

그런데 피어(Fear)의 영향을 받기는커녕 신나서 날뛰는 모습이라니.

나도 모르게 청풍을 과소평가했다. 녀석은 약간 미친놈이 아니라 단단히 미친놈이었다.

‘그래도 다른 녀석들처럼 벌벌 떠는 것보다 훨씬 낫기는 한데.’

평범한 사람과는 시작점부터 다르다. 지금껏 듣도 보도 못한 존재에 대한 미지의 공포는 청풍에게 해당하지 않는다.

왜냐하면 저 자식은 모든 것이 신기하고 재미있는 놈이니까.

‘총이 뭔지도 모르는 갓난아이한테 총구를 들이대 봤자, 신기해서 웃기만 하지.’

혁무진의 불알을 걸고 장담하는데, 아마 저런 어마어마한 괴물을 보고도 이런 반응을 보일 수 있는 무림인은 천하를 거꾸로 뒤집어 탈탈 털어도 청풍 하나뿐이다.

‘……그래, 차라리 이게 훨씬 낫다.’

궁기방이나 혁무진은 여전히 반쯤 혼이 나가 있는 상황.

고양이 손이라도 빌려야 할 판국에 피어의 영향을 받지 않는 청풍의 존재는 큰 도움이 된다.

나는 잔뜩 위축된 미미쨩과 변이된 수신룡을 반짝이는 눈동자로 번갈아 바라보는 청풍의 어깨를 붙잡았다.

“그렇게 쳐다본다고 진화하는 거 아니니까 정신 차리고. 사공이랑 동정어옹부터 보호해.”

“은인은요?”

“저놈들 정신부터 돌아오게 해야지.”

말이 끝나기도 전에 달려나간 나는, 제자리에 멍하니 서 있는 궁기방과 혁무진의 뺨을 후려쳤다.

쫙! 쫙!

찰진 소리와 함께 나동그라지는 두 개의 신형.

악몽에서 깨어난 사람처럼 몸을 퍼덕거린 녀석들이 흔들리는 눈동자로 나를 올려다보았다.

“허억, 컥.”

“조, 조장님.”

적지 않은 힘을 실어 후려친 따귀다.

방금의 그 한 방으로 입안이 터져 나갔는지 벌어진 입술 사이로 피가 줄줄 쏟아졌지만, 궁기방과 혁무진에게는 고통을 느낄 만한 여유조차 남아 있지 않았다.

“……꿈인 줄 알았는데. 왜 아직도 헛것이 보이지?”

“저, 저게 도대체.”

내 도움으로 피어 상태에서 벗어났다 해도, 인간이 지닌 원초적인 공포심까지 완전히 지울 수는 없는 법.

두 사람이 넋 나간 눈빛으로 내 어깨너머를 바라보고 있을 때, 낮고 깊은 괴성이 사방을 울렸다.

- 크라아아아아!

빌어먹을. 굳이 돌아보지 않아도 저 엄청난 괴물이 단단히 화가 났다는 사실은 알겠다.

등 뒤에서부터 빠르게 가까워지는 무시무시한 파공성의 정체도.

“청풍!”

나는 외침과 함께 궁기방과 혁무진의 뒷덜미를 잡고 몸을 날렸다.

동시에 고작 거대한 무언가가 조금 전 우리가 있던 자리를 사정없이 후려쳤다.

후우우웅, 콰앙!

굉음과 함께 솟구치는 모래와 진흙.

고작 몇 걸음 차이로 빗나간 그것의 정체는 높이만 일 장에 달할 것 같은 기암괴석(奇巖怪石)이었다.

‘……이런 걸 여기까지 날렸다고?’

무게만 따져도 수천 근은 너끈히 나갈 것 같은 바위를 저 멀리에서 날리다니.

그 힘도 무시무시한 수준이지만 조준까지 정확하다. 내가 신속하게 움직이지 않았다면 그대로 압사(壓死)당했을 것이 분명하다.

‘제구력 보소. 메이저리그 출신인가.’

내가 질린 표정으로 괴물을 바라보던 그때, 분노에 찬 포효와 함께 익숙한 알림이 귓가를 파고들었다.

띠링.



- 돌발 퀘스트, [타락한 영물]이 생성되었습니다.

- 당신은 퀘스트를 거부할 수 없습니다. 퀘스트가 강제 수락되었습니다!

- 퀘스트가 진행되는 동안 [로그아웃]이 불가능합니다!



퀘스트



[타락한 영물]



오랜 세월, 깊은 강물 속에서 승천을 기다리던 이 고귀한 존재는 알 수 없는 힘으로 타락하고 말았습니다.

눈부시게 빛나던 지성과 아름다운 자태를 지녔던 영물은 추악한 악물(惡物)로 변했으며, 그가 불러일으킨 숱한 죽음으로 인해 두 번 다시 과거의 모습을 되찾을 수 없을 것입니다.

그리고 지금, 당신은 이 불행하고도 강력한 악물을 저지해야 합니다.

호북성에 드리운 먹구름을 걷어내십시오!



등급 : 초절정

제한 : 진태경

임무 : [변이된 수신룡] 처치(미완료)

보상 : 연계 퀘스트

  막대한 경험치와 명성

  ???

실패 : 죽음 혹은 그에 준하는 패널티





빛의 속도로 퀘스트 창을 빠르게 확인한 내 소감은 짧고 간결했다.

“……거지 같네.”

최악의 상황에 어울리는 최악의 퀘스트다.

퀘스트 강제 수락에 이어 로그아웃 금지. 거기에 더해 여차하면 도망칠 수도 없게 단단히 못까지 박아 뒀다.

저 엄청난 괴물을 처치하거나, 이 자리에서 죽거나.

지금 시스템은 내게 둘 중 하나를 선택하라고 요구하고 있었다.

‘게다가 죽음에 준하는 패널티 부여라니. 도대체 어떤 패널티길래.’

생각하기도 싫다. 아니, 정확히 말하자면 더 생각할 틈조차 주어지지 않았다고 해야 옳겠지.

꽈앙! 후우우웅!

다음 순간, 나는 볼 수 있었다.

반투명한 홀로그램 창 너머, 저 멀리에서 무너져 내리는 절벽과 까마득한 상공을 가득 메운 채 유성처럼 떨어져 내리는 수십여 개의 검은 점들을.

그 엄청난 광경에 혁무진과 궁기방이 멍하니 중얼거렸다.

“저거 별인가? 그래. 별이겠지.”

“별치고는 너무 어두운데요. 심지어 점점 가까워지네요.”

“요즘 별들이 다 그렇지.”

“생각해 보니 그러네요. 조장님이 저한테 항상 선입견을 버리라고 하셨는데…….”

“야, 이 미친놈들아!”

덥석, 쐐애액!

나는 아직도 정신을 차리지 못한 채 헛소리를 늘어놓는 두 녀석을 붙잡고 몸을 날렸다.

경고를 남기고 재차 혼절한 동정어옹과 늙은 사공을 각각 양 옆구리에 낀 청풍 역시 예외는 아니었다.

“은인! 커요! 그리고 많아요!”

초등학교 수준의 언어 구사력이었지만, 무슨 말인지 알아듣기에는 차고 넘쳤다. 내 눈에도 이곳을 향해 추락하는 저 기삼괴석들의 개수는 너무 많았으니까.

모르긴 몰라도 우리가 서 있는 좁은 지면을 빈틈없이 뒤덮고도 남을 것이 분명했다.

후우우웅!

빌어먹을, 피할 곳이 없다. 나는 붙잡고 있던 두 녀석을 등 뒤로 내던짐과 동시에 마음속으로 시동어를 읊조렸다.

‘인벤토리 오픈, 소환.’

잠시 인벤토리에 넣어 두었던 백염이 손아귀에 잡힘과 동시에 머리 위로 드리워지는 거대한 기암괴석의 그림자.

망설임 없이 전신의 공력을 끌어올린 내가 힘차게 창날을 흩뿌렸다.

쉬쉬쉬슁!

창날로부터 솟아오른 청백색의 강기가 허공을 찢었다.

까마득한 세월 동안 절벽의 일부로 퇴적과 풍화를 반복했을 기암괴석을 향해 쏘아졌다.

‘갈라져라.’

서걱!

강기는 강철도 순두부처럼 베어 버리는 기운의 집약체. 창날이 그리는 궤적에 걸려든 기암괴석들이 조각남과 동시에 추락했다.

꽈앙!

지축을 울리는 굉음과 함께 모래와 강물이 솟구친다.

혁무진과 궁기방이 내지르는 새된 비명들 사이로 나와 같은 방법으로 위기를 벗어난 청풍이 보였다.

그러나…….

콰직!

‘젠장. 저걸 깜빡했네.’

흔적도 찾아볼 수 없을 만큼 부서진 나룻배의 파편을 보자 속이 쓰리다.

배의 주인인 늙은 사공이 깨어 있었다면 졸도했을지도 몰랐다.

‘이대로 있다가는 놈의 표적밖에 안 돼. 급한 대로 파편이라도 이용해서 위치를 옮겨야……!’

생각이 이어지기도 전에 몸이 덜컥 굳었다.

스치듯이 확인한 수면 위, 응당 있어야 할 무언가가 보이지 않았다.

거칠게 휘몰아치는 강물과 번쩍이는 낙뢰 사이에 우뚝 서 있던 거대한 존재가 씻은 듯이 사라진 것이다.

‘이건.’

머릿속에 울려 퍼지는 적색경보.

눈을 부릅뜬 나는 비명과도 같은 고함을 내질렀다.

“온다!”

그리고 다음 순간.

콰아아아아!

십여 장에 달하는 물의 장벽이 솟구침과 동시에, 기암괴석과는 비교도 안 될 만큼 짙고 거대한 동체가 검게 물든 하늘을 가렸다.

세로로 길게 찢어진 핏빛 동공에 익숙한 얼굴이 비쳐졌다.

- 크르르르르.

타락한 악물(惡物)의 아가리에서 흘러나오는 숨결은 소름 끼칠 만큼 차가웠고, 지금껏 봐 왔던 어떤 몬스터보다 거대한 동체가 내뿜은 살기와 위압감은 사방을 짓눌렀다.

‘뭐 이런 괴물이……!’

경악 어린 시선으로 놈을 올려다보던 바로 그때였다.

촤라라라락!!

사방에서 쏟아지는 무수한 빛줄기.

단단한 비늘로 둘러싸인 콧잔등 주위를 뒤덮은 수염이 수백 갈래로 나뉘어 내리꽂혔다.

하나하나가 수 장에 이르는 그것들은 일직선으로 쏘아지기도 하고, 살아 있는 생물처럼 휘어지며 사각으로부터 날아들었다.

“……!”

외침을 토해 낼 틈도 주어지지 않았다.

전신의 털이 곤두서고 모든 감각이 활짝 열린다. 나는 느려진 세상 속에서 몸을 비틀었다.

퍼버버버벅! 촤악!

화끈한 통증이 어깨 어림으로부터 번져 나간다. 흙탕물 위로 점점이 흩뿌려지는 핏방울이 누구의 것인지는 보나 마나였다.

그래도 고작 이 정도 부상으로 예상치 못한 일격을 피했다면 싸게 먹혔다.

이제는 더욱 비싸게 돌려줄 차례다.

“하압!”

서걱!

기합성과 함께 휘두른 창날에 수십 가닥의 수염이 잘려 나갔다.

화룡일미(火龍一尾)라는 초식 명에 어울리는 긴 화염의 꼬리가 그것에 만족하지 않고 허공을 가르며 놈의 턱을 베어 가던 순간.

후우우웅!

귀가 먹먹해지는 파공성과 함께 내 주위를 둘러싼 모든 것이 검게 물들었다.

마치 모든 것이 정지한 것처럼 느릿해진 시간 속에서, 나는 비로소 볼 수 있었다.

거대한 궤적을 그리며 옆으로 날아드는 무언가를.

‘아, 씨발. 꼬리.’

깨달음과 동시에 엄청난 충격이 전신을 휩쓸었다.

꽈앙!

또렷하던 시야가 흐릿해졌다.

일 초도 안 되는 시간 동안 하늘과 땅이 수도 없이 뒤집히고 나를 둘러싼 모든 것이 지진이라도 난 것처럼 흔들렸다.

아니, 아니다. 뒤집히고 흔들리는 것은 나 혼자뿐이었다.

머릿속까지 뒤엉키게 만든 거대한 충격에서 빠져나왔을 때, 나는 십여 장의 공간을 섬광처럼 가로지르며 절벽을 향해 처박히고 있었다.

‘젠장. 지금이라도 피해야 하는데…….’

엄청난 힘이 실린 일격에 당한 탓에 쉽게 몸을 움직일 수가 없다.

나는 이를 악물며 곧 다가올 이차 충격에 대비했다.

아니, 대비하려고 했다.

퍽. 카가가가각!

등으로부터 전해지는 가벼운 충격. 그리고 지면을 갈아엎다시피 하며 줄어드는 속도.

눈을 깜빡이는 내 귓가에 누군가의 목소리가 닿았다.

“괜찮으세요, 은인?”

청풍이다.

나는 참았던 숨을 토해 내며 두 발로 땅을 딛고 섰다. 그리고 어째서 이 퀘스트의 등급이 물음표가 아니라 초절정인지 깨달았다.

“야, 이 빌어먹을 뱀장어 새끼야!”

익숙한 누군가의 목소리에, 나는 피식 웃었다.
```

## Final English reading copy

```markdown
# Chapter 470

No, what the hell was going on?

Even with every second counting, I blanked out for a moment before finally managing to open my mouth.

“W-Wait a second. Young Hero Cheongpung.”

“I’ve never seen anything like that in my life! Just as Grandfather said, the world really is vast! I’m so glad I left Huashan!”

“Yes, the world is vast, but that has absolutely nothing to do with—”

“Whoa! It moved again!”

“……”

He wasn’t listening to a word I said.

I had known for a long time that Cheongpung was a little unhinged, but I had never imagined he was this far gone.

*What kind of person is this?*

Even a veteran Hunter who encountered monsters more often than his own parents would naturally feel fear upon facing a supermassive monster of that size.

But Cheongpung wasn’t merely unaffected by Fear. He was running around excitedly.

I had underestimated him without realizing it. He wasn’t a little crazy. He was thoroughly insane.

*Still, it’s much better than having him tremble like the others.*

He was different from ordinary people from the very beginning. The fear of the unknown—of an existence no one had ever seen or heard of before—did not apply to Cheongpung.

Because everything was new and interesting to that bastard.

*If you pointed a gun at a baby who didn’t even know what a gun was, it would just smile because it found the gun fascinating.*

I’d stake Hyuk Mujin’s balls on this: even if you turned the entire world upside down and shook it out, Cheongpung would be the only martial artist in all of Murim capable of reacting this way to such an enormous monster.

*……Yeah. This is much better.*

Gung Gibang and Hyuk Mujin were still half out of their minds.

With the situation desperate enough to borrow even a cat’s paw, Cheongpung’s resistance to Fear was a tremendous help.

I grabbed Cheongpung by the shoulders as he stared back and forth between the thoroughly cowed Mimi-chan and the Mutated Water God Dragon with glittering eyes.

“Staring at it like that won’t make it evolve, so snap out of it. Protect the boatman and the Dongting Fisherman first.”

“What about you, Benefactor?”

“I need to get those two back to their senses first.”

Before I had even finished speaking, I raced forward and slapped Gung Gibang and Hyuk Mujin across the face.

*Smack! Smack!*

Two bodies went tumbling away to the accompaniment of sharp, satisfying sounds.

The two men flailed like people waking from nightmares, then looked up at me with unsteady eyes.

“Gasp—cough.”

“C-Captain.”

I had put a fair amount of strength into those slaps.

Their mouths must have split open from that single blow, because blood poured through their parted lips. But Gung Gibang and Hyuk Mujin didn’t even have enough room left in their minds to feel pain.

“I thought it was a dream. Why am I still seeing things?”

“W-What is that?”

Even if my help had pulled them out of Fear’s influence, it was impossible to erase the primitive fear inherent to being human.

As the two men stared blankly over my shoulder, a low, deep roar rang out in every direction.

—Kraaaaaaah!

Damn it. I didn’t need to turn around to know that the enormous monster was thoroughly enraged.

I also knew what that terrifying sound splitting the air and rapidly approaching from behind was.

“Cheongpung!”

I shouted as I grabbed Gung Gibang and Hyuk Mujin by the backs of their necks and threw myself aside.

At the same time, something enormous viciously struck the place where we had been standing.

*Whoooooosh—crash!*

Sand and mud erupted into the air with a deafening boom.

The thing that had missed us by only a few steps was a bizarre boulder that looked to be nearly one *jang* tall.

*……It threw that all the way here?*

The boulder must have weighed several thousand *geun* at least, yet it had been hurled from far away.

Its strength was terrifying, but its aim was accurate, too. If I hadn’t moved quickly, I would have been crushed to death on the spot.

*Look at that accuracy. Was it from the Major Leagues?*

Just as I stared at the monster with a horrified expression, a familiar notification pierced my ears alongside its enraged roar.

*Ding.*

> **System**
>
> - A sudden Quest, **Corrupted Spirit Beast**, has been generated.
>
> - You cannot refuse the Quest. The Quest has been forcibly accepted!
>
> - **Logout** is unavailable while the Quest is in progress!
>
> **Quest**
>
> **Corrupted Spirit Beast**
>
> For many years, this noble existence waited to ascend within the depths of a great river. But an unknown power corrupted it.
>
> The spirit beast, which once possessed dazzling intelligence and a beautiful form, has become an ugly evil beast. Because of the countless deaths it has caused, it will never be able to return to its former appearance.
>
> And now, you must stop this unfortunate yet powerful evil beast.
>
> Dispel the dark clouds hanging over Hubei Province!
>
> **Grade:** Supreme Peak
>
> **Restriction:** Jin Taekyung
>
> **Objective:** Defeat the **Mutated Water God Dragon** (Incomplete)
>
> **Reward:** Linked Quest
>
> &nbsp;&nbsp;Vast EXP and Fame
>
> &nbsp;&nbsp;???
>
> **Failure:** Death or an equivalent penalty

I checked the Quest window at lightning speed. My assessment was short and concise.

“……What a load of crap.”

It was the worst Quest imaginable for the worst possible situation.

First, the Quest had been forcibly accepted. Then Logout had been prohibited. On top of that, it had driven the final nail into the coffin so I couldn’t even run away if things went badly.

Either I killed that enormous monster or I died here.

The System was demanding that I choose one of those two options.

*And it says death or an equivalent penalty. What the hell kind of penalty is that supposed to be?*

I didn’t even want to think about it. No—to be precise, I wasn’t given so much as a moment to think any further.

*Boom! Whoooooosh!*

The next moment, I saw it.

Beyond the semitransparent holographic window, a cliff collapsing in the distance and dozens of black dots filling the vast sky overhead as they plunged downward like meteors.

Faced with that spectacular sight, Hyuk Mujin and Gung Gibang muttered blankly.

“Are those stars? Yeah. They must be stars.”

“They’re too dark to be stars. And they’re getting closer.”

“Stars have all been like that lately.”

“Come to think of it, that’s true. Captain, you always tell me to throw away my preconceptions, but……”

“You two crazy bastards!”

*Grab—whoooooosh!*

I seized the two men, who still hadn’t come to their senses and were spouting nonsense, and threw myself aside.

Cheongpung was no exception. He had the Dongting Fisherman, who had passed out again after giving his warning, tucked under one arm and the old boatman under the other.

“Benefactor! They’re big! And there are lots of them!”

His language skills were on an elementary-school level, but that was more than enough to understand what he meant. Even I could see that there were far too many of those bizarre boulders falling toward us.

There was no doubt they would cover every inch of the narrow patch of ground where we stood—and then some.

*Whoooooosh!*

Damn it. There was nowhere to dodge.

As I threw the two men I was holding behind me, I recited the activation command in my mind.

*Open Inventory. Summon.*

White Flame appeared in my hand, just as the shadow of an enormous bizarre boulder spread over my head.

Without hesitation, I pulled up all the internal energy in my body and swept the spearhead forward.

*Shh-shh-shh-shing!*

Blue-white Force erupted from the spearhead and tore through the air.

It shot toward the bizarre boulders, which must have spent countless ages as part of the cliff, undergoing layer after layer of deposition and weathering.

*Split apart.*

*Schk!*

Force was a concentrated manifestation of energy capable of cutting steel like soft tofu. The bizarre boulders caught in the arc traced by my spearhead broke into pieces and began to fall.

*Boom!*

Sand and river water surged upward with a boom that shook the ground.

Amid the shrill screams of Hyuk Mujin and Gung Gibang, I saw Cheongpung escaping the crisis by the same method I had used.

However……

*Crack!*

*Damn it. I forgot about that.*

My stomach twisted when I saw the shattered remains of the ferryboat, so thoroughly destroyed that not a trace of its original shape remained.

If the boat’s owner, the old boatman, had been awake, he might have fainted.

*If we stay here, we’ll be nothing more than targets. I need to use even the wreckage to move our position, at least for now—*

Before I could finish the thought, my body suddenly locked up.

I had only glanced across the surface of the water, but something that should have been there was missing.

The enormous being that had stood tall amid the raging river and flashing lightning had vanished without a trace.

*This is—*

A red alert rang out inside my head.

I widened my eyes and shouted at the top of my lungs.

“It’s coming!”

And in the next moment—

*Kwaaaaaaah!*

A wall of water more than ten *jang* high surged into the air, and a body far darker and larger than the bizarre boulders blocked out the blackened sky.

My familiar face was reflected in its long, vertical, blood-red pupils.

—Grrrrrrrr.

The breath spilling from the maw of that corrupted evil beast was chillingly cold. Its enormous body, larger than any monster I had ever seen, radiated killing intent and pressure that crushed down on everything around it.

*What kind of monster is this……!*

That was when it happened, as I stared up at it in shock.

*Shra-ra-ra-ra-ra!*

Countless streaks of light came raining down from every direction.

The whiskers surrounding the bridge of its nose, which was covered in hard scales, split into hundreds of strands and plunged toward me.

Each one was several *jang* long. Some shot straight forward, while others curved like living creatures and attacked from blind spots.

“……!”

I wasn’t even given time to shout.

Every hair on my body stood on end, and all my senses opened wide. I twisted my body in the slowed-down world.

*Thud-thud-thud-thud! Slash!*

A scorching pain spread from around my shoulder. It was obvious who the drops of blood spattering across the muddy water belonged to.

Still, if I had avoided an unexpected strike with no more than an injury like this, I had gotten off cheap.

Now it was time to make the monster pay a much higher price.

“Hah!”

*Schk!*

The spearhead I swung with a battle cry cut through dozens of whiskers.

The long, flaming tail of the **Fire Dragon’s Single Tail**, befitting the form’s name, did not stop there. It cut through the air and swept toward the monster’s jaw.

*Whoooooosh!*

Alongside a deafening sound of something splitting the air, everything around me turned black.

Time slowed until it felt as though everything had stopped. Only then did I see it clearly.

Something flying toward me from the side, tracing a massive arc.

*Ah, fuck. The tail.*

The instant I realized what it was, an enormous impact swept through my entire body.

*Boom!*

My clear vision blurred.

In less than a second, the sky and ground flipped over countless times, and everything around me shook as if an earthquake had struck.

No. That wasn’t right.

The only thing flipping and shaking was me.

When I finally escaped the enormous impact that had tangled even my thoughts, I was flying across more than ten *jang* of space in a flash, headed straight for the cliff.

*Damn it. I need to dodge, even now…….*

But I couldn’t move my body easily after taking a blow carrying such tremendous force.

I gritted my teeth and braced myself for the secondary impact that was about to come.

No.

I tried to brace myself.

*Thud. Krrrraaaack!*

A light impact reached me through my back. Then my speed began to decrease as the ground was churned up beneath me.

As I blinked, someone’s voice reached my ears.

“Are you all right, Benefactor?”

It was Cheongpung.

I exhaled the breath I had been holding and stood on both feet. Then I realized why the Quest’s Grade was Supreme Peak instead of a question mark.

“Hey, you goddamn eel bastard!”

At the sound of that familiar voice, I let out a quiet laugh.
```
