<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0461.txt",
      "sha256": "2438f64da6ac79e90f70401c630642edb1a8c1b55f21a70501fd8bf9e1269ddc",
      "bytes": 14256
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b02c94380433be0dd906d8170741a620f85bcd009c3725b4e47de5b47225cf0f",
      "bytes": 4211
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "051dcda5a5afbb053ec80ba1e33e18e84fda5a4a0bb2ad6b76e727e314c32767",
      "bytes": 150136
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "5494819faee7770c076271ec0f3f6fc18e3b4e419c872b43fcbdeebc8af2c614",
      "bytes": 990
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "28c52d9ba1b789967d31c82726834f735c49c0c0890a7743ba77d64b6e489123",
      "bytes": 553
    },
    {
      "path": "characters/Dongting Fisherman.md",
      "sha256": "06e31c3b86f28506ca93286653fcf92a8d77b1f47135ef4184c9a38004aad240",
      "bytes": 703
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "66b0eb05fb6a3155025cb8f1926bd9a132873d1f3c486853bda53c6c67e152d5",
      "bytes": 662
    },
    {
      "path": "characters/Honglan.md",
      "sha256": "dec2e9f70434522692a763a118027d3c7dd748fc445760b166016f05bd586a5f",
      "bytes": 799
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "8753601e09b70f76900948402103bd529800796b59caab6b587e1fe9e342fe40",
      "bytes": 667
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "403dcd08f163bab17d12d27e0ea15efc2a368d0297026a95c1214f55f34b94aa",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "2b003771042613f2e2d7bb4636e27efee955f5a62cdc39f16c383d5181b6a7af",
      "bytes": 1470
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "27985967ce4d4d0808bced96ffa300c656cb388b35aaede18d3964cada8d71ff",
      "bytes": 1477
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "bfc261d7e738ba259411eb5cbdac861edc63b49dcd2204edfd24405d062d81f6",
      "bytes": 145368
    }
  ],
  "estimated_tokens": 12737
}
-->

# Durable State Update — Chapter 461

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 461. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 461. Profile updates may replace only one
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
  "chapter": 461,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 461,
    "continuity_sources": [461],
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
    "Taekyung completed the unavoidable Peak-grade Quest The Tragedy of Dongting Lake, rescued two people who were the only survivors found, and earned the Water Rescue Worker Title.",
    "Honglan survived the Dongting Lake disaster and regained consciousness; Ju Wongong also survived but remains unconscious under guard after passing the most dangerous stage of his injuries. Honglan is still recovering and is unfit for combat.",
    "Jin Wikyung is acting as an inspector for the new Murim Alliance and is cooperating with Taekyung's investigation.",
    "The shared symbols between the Arch Lich's magic circle and Dark Heaven's formations remain unexplained.",
    "The Sea Serpent Society and three Yangtze River Channel League strongholds, including Donghu Stronghold, were destroyed, with more than a thousand casualties, while the perpetrators' wider plans remain unknown.",
    "The Dongting Fisherman is a previous-generation Supreme Peak water-arts master comparable to the Seafaring King, remains in Hubei Province, and is suspected of Dark Heaven involvement and the Dongting Lake attack. The Hidden Shadow Ghost is the local name for an unseen killer of boatmen who may be connected to him.",
    "Taekyung, Cheongpung, Hyuk Mujin, Gung Gibang, and Honglan are pursuing the Dongting Fisherman's refuge by ferry through a narrow route inaccessible to large vessels.",
    "Wudang is responding to an unidentified killer demon responsible for more than thirty deaths, including twenty pilgrims on Mount Wudang.",
    "The Skeleton King's undead identity remains concealed, and Taekyung has ordered him to join Peace Guild under a prepared contract.",
    "Go Jun is expected to succeed Lee Jungryong as Ares Guild's captain and is searching China for Lee's holographic recorder.",
    "The captured Three Fiends is a former-generation great fiend and Supreme Peak Dark Heaven subordinate whom Taekyung is transporting alive to investigate possible codes or markings.",
    "Qingxia Hall is an influential Hubei social club formed by powerful families' children, and Ju Wongong is its exiled young master who defers to Prince Shangshan while Honglan conceals her real name; Beggars' Sect, Lower District Sect, and Zhuge Clan intelligence are searching for the people responsible for the Hubei massacres."
  ],
  "continuity_sources": [
    460,
    459
  ],
  "open_questions": [
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Who destroyed Donghu Stronghold and the related Yangtze River Channel League strongholds, why was no Moving Formation trace left, and was the destruction a diversion?",
    "What is the Dongting Fisherman's exact role in Dark Heaven and the Hubei atrocities, and is he the Hidden Shadow Ghost responsible for the boatmen's deaths?",
    "Is the killer demon attacking Wudang connected to Dark Heaven?",
    "What evidence is contained in Lee Jungryong's holographic recorder, and what are the terms of the Peace Guild–Wizard Guild agreement?"
  ],
  "safe_through": 460,
  "temporary_decisions": [
    "Render 익양루 as Yiyang Tower.",
    "Render 황철 as Hwang Cheol, 도립군 as Do Ripgun, 광수도귀 as Mad Water Saber Demon, 파랑호 as Wave Fox, 동정호 as Dongting Lake, and 사천혈사 as Sichuan Blood Tragedy.",
    "Render 살귀 as killer demon, 은영귀 as Hidden Shadow Ghost, 일급 낭인 as First Rate wandering martial artist, 삼괴 as Three Fiends, 대마두 as great fiend, and 마군 as Demon Lord.",
    "Render 시부럴 as “sibu-leol,” 시벌좌 as “Lord Fuck,” and 시부럴좌 as “Lord Sibu-leol.”",
    "Preserve the Skeleton King's grandiose, mock-offended voice and Taekyung's dry, profane humor; render 주원공 as Ju Wongong, 대죽산표국 as Daejuksan Escort Bureau, 형문검가 as Hyungmun Sword Family, 응성상회 as Eungseong Merchant Association, 천룡인 as Celestial Dragon, 사인교 as four-person sedan chair, 홍란 as Honglan, 가기 as singing courtesan, 구족 as the nine branches of kin, 수상 구조대원 as Water Rescue Worker, and 수공 as water arts."
  ],
  "version": 1
}
```

## Exact glossary matches

| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 하오문    | **Lower District Sect**          |
| 열화문    | **Fire Gate Clan**               |
| 화산파    | **Huashan**                      |
| 장강수로맹  | **Yangtze River Channel League** |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 사부     | **Master**                                   |
| 은인     | **Benefactor**                               |
| 시스템              | **System**                     |
| 스킬               | **Skill**                      |
| 퀘스트              | **Quest**                      |
| 칭호               | **Title**                      |
| 화산     | **Huashan**            |
| 소협      | **Young Hero**                                                  |
| 소저      | **Young Lady**                                                  |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동정어옹 | **Dongting Fisherman** | Publicly condemned the Yangtze River Channel League and disappeared three days before this chapter. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 홍란 | **Honglan** | Stage name of Ju Wongong's Lower District Sect singing courtesan; her real name is concealed. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 벽호공 | **Wall Lizard Technique** | Climbing martial art used to scale walls and cliffs. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 후개 | **Successor Beggar** | Title of the Beggars' Sect successor competing in the preliminaries. |
| 항룡십팔장 | **Eighteen Dragon-Subduing Palms** | Beggars' Sect martial art mentioned by Gung Gibang. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 화산신룡 | **Huashan Divine Dragon** | Title given to Cheongpung after the Star-Array Grand Banquet. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 수공 | **water arts** | Water-based martial arts; the Dongting Fisherman's specialty. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |
| 홍란 | 은인 | rescued_survivor_to_rescuer | Benefactor | humble-formal | Honglan addresses Taekyung as Benefactor after he rescued her. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 460
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 458
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Dongting Fisherman.md

# Dongting Fisherman (동정어옹)

- **Safe through:** Chapter 460
- **Aliases:** None
- **Role:** The Dongting Fisherman is a previous-generation Supreme Peak master whose water arts rival the Seafaring King; he is identified as Dark Heaven's tail and suspected perpetrator of the Dongting Lake attack, with hidden refuges throughout the lake.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** The Dongting Fisherman opposed the Yangtze River Channel League and was monitored by the Lower District Sect for several years after friction with it, while current records place him in Hubei Province.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 460
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung and uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and search for Dark Heaven’s Hubei forces.

### Honglan.md

# Honglan (홍란)

- **Safe through:** Chapter 460
- **Aliases:** None
- **Role:** Honglan is a Lower District Sect courtesan who uses a stage name while serving as Ju Wongong's singing courtesan.
- **Personality:** Discreet about her real identity and professionally alluring.
- **Voice:** Clear, pure, and alluring, with humble formal speech toward honored guests.
- **Relationships:** Honglan is kept at Ju Wongong's side as a singing courtesan, belongs to the Lower District Sect, lost her clan and parents overnight as a child, can respond to Taekyung through Sound Transmission, and is the sole surviving eyewitness to the Dongting Lake attack who knows several possible locations of the Dongting Fisherman's hidden refuges.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 460
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 460
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 452
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master, and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, and pathologically afraid of water. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 458
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather; more than forty years ago he sought Jeok Cheongang's help against the Demonic Cult, fought Jeok at Mount Jiuhua for seven days and seven nights, and drew with him; after the Great Faction War ended, he devoted himself to martial arts, reached Great Completion, attained higher enlightenment after encountering another wall, unexpectedly Returned to Youth, and traveled the world for a year under the name Jongni Chu while concealing his identity; at Mount Song he protected Cheongpung and attacked the Blood Lord with the divine Thirty-Six Plum Blossom Swords; after the Blood Lord escaped, he confirmed his identity to Jin Taekyung and Song Ho, and Song Ho identified Mae as the Great Hero who had saved his life.
- **Personality:** Not established in this chapter.
- **Voice:** Not established in this chapter.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

## Korean source

```text
＃461화



속도로 치자면 나룻배는 장강수로맹의 쾌조선은 물론, 일반적인 선박에도 미치지 못한다. 특히 오늘처럼 험악한 날씨에는 더더욱.

후우우웅, 촤악!

거센 바람과 출렁이는 물살에 나룻배가 흔들린다.

선체가 작은 만큼 외부 요건에 대한 저항력도 부족한 법. 노를 잡은 늙은 사공의 팔근육에 핏대가 불끈 솟는다.

그는 노련한 사공답게 악천후 속에서도 나룻배를 잘 이끌었지만, 목적지에 가까워질수록 난폭해지는 물살로 인해 한계에 도달하고 있었다.

‘여기서부터는 무리겠지.’

정말 나룻배 한 척과 늙은 사공만 믿고 여기까지 왔다면 미친 짓일 것이다.

목을 좌우로 꺾은 내가 앞으로 나섰다.

“슬슬 시작할까?”

내 한 마디에, 선체가 흔들리는 와중에도 미동 없이 운기(運氣)를 하고 있던 세 사람이 눈을 떴다.

“전 준비됐어요, 은인.”

“대개방의 절기를 이런 일에 쓰다니, 사부님께서 보시면 한 소리 하시겠군.”

“조장님. 저는 뭘 해야 합니까?”

운기조식으로 기운을 보충한 청풍, 궁기방, 혁무진의 대답에 내가 빠르게 지시를 내렸다.

“청 소협은 나를 따라서 후미. 궁기방은 앞에 위치하고, 혁무진 너는 사공을 보호해. 필요할 때 부를 테니까 재깍재깍 움직이고.”

세 사람이 지시에 따라 움직이자 힘겹게 노를 젓고 있던 늙은 사공이 눈동자를 끔뻑였다.

“저, 지금 무슨 말씀을 하고 계시는……?”

하지만 사공의 말이 끝나기도 전에, 청풍의 양손에서 쏘아진 강맹한 장력(掌力)이 물살을 후려쳤다.

펑! 쐐애애액!

“으허어어억!”

일명 장력 부스터.

일반적인 선박보다 날렵한 선체를 지닌 쾌조선에도 미치지 못할 만큼, 훨씬 작고 가벼운 나룻배가 허공을 날았다.

맹렬하게 스쳐 지나가는 바람에 사공의 비명이 섞여들었다.

그리고 그 비명을 신호 삼아, 내가 나섰다.

‘지금.’

쉬이이익!

떠올랐던 나룻배가 수면에 내려앉으려던 순간, 나는 단전에 가득 찬 공력을 끌어올려 손바닥을 향해 쏘아 보냈다.

퍼펑! 퍼어엉!

어느덧 팔 성에 다다른 화염신장(火焰神掌)의 열기에 주위의 공기가 후끈 달아오르고, 내려가는 듯싶던 나룻배의 선체가 날치처럼 튀어 오른다.

눈을 부릅뜬 사공이 덜덜 떨리는 손가락으로 전방을 가리켰다.

“암초(暗礁)! 전방에 암초오오오!”

동정어옹이 자신만이 아는 비처를 만만한 곳에 마련했을 리가 있나.

우리가 향하는 길은 폭이 좁아 평범한 선박으로는 진입할 수 없고, 물살이 유독 강해서 나룻배처럼 가벼운 배로는 빠져나오기가 어렵다.

그렇게 한번 물살에 휘말리면 곳곳에 즐비한 암초를 피하지 못하고 박살 나기 딱 좋다.

“야, 이 후레새끼들아! 내가 안 온다고 했지!”

늙은 사공이 진심 가득한 비명을 내지른 그 순간. 나는 한 사람의 이름을 외쳤다.

“궁기방!”

“알았다!”

힘차게 대답한 궁기방이 누더기나 다름없는 소매를 떨쳤다.

십만의 방도를 보유한 개방에서도 오직 두 사람, 개방 방주와 후개에만 전해진다는 항룡십팔장(降龍十八掌)이 허공을 격하며 터져 나왔다.

콰과과과광!

소나기처럼 쏟아지는 장력에 철벽처럼 우뚝 서 있던 암초가 산산 조각나며 흩어진다.

곧이어 나타난 제이, 제삼의 암초도 항룡십팔장의 위력을 견딜 수는 없었다.

콰아아아!

잘게 조각난 암초의 잔해를 뚫고 나룻배가 수면 위로 착륙했다.

선체의 좌우로 물보라가 솟구치고 어디선가 튀어 오른 물고기 몇 마리가 늙은 사공의 뺨을 철썩 때렸다.

“허어, 으허어어어…….”

이거 완전히 맛이 갔는데. 나는 동공이 반쯤 풀린 침을 흘리는 사공의 어깨를 흔들었다.

“정신 차리세요. 정신.”

“허으, 으허어어. 이 쒸이벌…….”

“안 되겠네. 무진아.”

“존명.”

혁무진이 양 소매를 걷어 올리고 야무지게 따귀를 갈겼다.

쫙! 하는 소리와 함께 사공의 눈동자에 초점이 돌아온다.

“으억! 이게 무슨.”

쫙!

“……저, 정신 차렸는뎁쇼.”

“그만해라.”

“옙.”

역시 정신 돌아오게 하는 데에는 귀싸대기만 한 것이 없지.

나는 벌겋게 물든 뺨을 문지르는 사공을 향해 물었다.

“여기가 어디쯤인 것 같습니까?”

“아니, 아무리 귀인들이라 하셔도 그렇지 사람을 이렇게…….”

“무진아.”

“존명.”

“지금 즉시 확인해 보겠습니다요.”

벌떡 일어난 사공이 주위를 둘러보았다.

나룻배 두세 척만이 간신히 지나갈 수 있을 법한 강폭.

깎아내릴 듯한 절벽이 좌우로 늘어서 있고 수면 위로는 거센 물살이 휘몰아친다. 거기에 더해 자욱한 안개까지.

눈을 가늘게 뜨고 곳곳을 바라보던 늙은 사공이 고개를 끄덕였다.

“맞습니다. 말씀하셨던 곳 중에 첫 번째 장소입니다.”

홍란을 통해 전해 들은 하오문의 정보에 의하면 동정어옹의 비처로 유력한 장소는 총 다섯 군데.

현재 나룻배가 도달한 위치는 그중에서도 가장 가까운 곳이었다.

분명 희소식이었지만 아직 기뻐하기에는 일렀다.

“그, 빨리 온 건 좋은데…… 이제 어떻게 찾지?”

궁기방의 물음에 내가 사방을 훑으며 대답했다.

“글쎄. 홍 소저가 알려 준 정보도 정확한 건 아니었으니까. 인근을 샅샅이 뒤져 봐야지.”

“끙. 한참 걸리겠군.”

“재수 없는 소리 하지 마라. 그나마 홍 소저가 알려 준 덕분에 여기까지 온 걸 감사하게 여겨.”

비처가 괜히 비처인가.

비록 홍란이 전해 준 정보에는 정확한 위치가 나와 있지는 않았지만, 아무도 모르는 동정어옹의 은거지를 여기까지 파악했다는 것만으로도 큰 수확이다.

설령 첫 번째 장소에서 허탕을 치게 된다 해도, 그물을 천천히 좁혀 나가다 보면 물고기가 걸려들 테니까.

‘아니면 잡히기 전에 스스로 뛰쳐나오든가.’

그런 생각을 하면서 주위를 유심히 살피고 있는데, 어쩐지 얼굴이 따갑다.

슬쩍 고개를 돌리자 묘한 눈빛으로 나를 바라보고 있던 네 쌍의 시선들이 황급히 떨어졌다.

“뭐야?”

“뭐, 뭘 말이냐? 나, 난 그냥. 이 와중에도 홍 소저 생각하는 게 보기 좋아서 그런 거지.”

“커흠. 조장님. 전 응원합니다.”

“젊음이 좋긴 좋습니다그려. 소인도 한 삼십 년 전까지는 아낙들한테 인기가 많았었는데. 한때 별명이 동정호 여심 낚시꾼이었지요. 허허허.”

“…….”

다들 무슨 생각을 하는지 뻔히 알겠다.

내심 혀를 차는 나와 우연히 눈이 마주친 청풍이 총에 맞은 새처럼 퍼뜩 몸을 떨며 손을 내저었다.

“아니에요! 아니에요, 은인! 전 아무 생각도 안 했어요!”

“아니, 도대체 무슨 생각을 한 거야. 난 아직 아무 말도 안 했는데.”

“정말 아니에요! 저는 맹세코 홍 소저와 은인이 불같은 사랑에 빠져서 혼인식을 올리고, 두 아이를 낳아 알콩달콩 행복하게 사는 상상을 하지 않았어요! 제가 은인의 이웃집에 살면서 자주 놀러 가는 것도요!”

“…….”

“헙!”

그제야 자신의 실수를 깨달은 청풍이 두 손으로 입을 틀어막지만 이미 늦었다.

‘그 잠깐 사이에 저런 상상을 하다니.’

저 정도면 무인 때려치우고 소설가로 나가도 되겠다.

필명은 화산신룡. 화산파 이름으로 출판하고 검성 매종학이 추천사를 써 주면 불티나게 팔릴 거다.

물론 나를 주인공으로 썼다가는 불티나게 처맞겠지.

“아니, 인간들이 도대체…… 후, 됐다. 말을 말자.”

말해 봤자 입만 아프지. 한숨을 내쉰 나는 빠르게 지시를 내렸다.

아까부터 왠지 모르게 얼굴이 화끈거려서도 아니고, 홍란의 은비녀에 배어 있는 은은한 향기가 자꾸만 코끝을 맴돌아서도 아니다.

……정말이다.

“청 소협과 궁기방은 벽호공(壁虎功)으로 절벽을 조사하고, 혁무진은 배를 타고 돌아다니면서 아래쪽을 찾아봐. 언제 뭐가 나타날지 모르니까 한순간도 긴장을 풀지 말고.”

내 진중한 목소리에, 사람들의 입가에 살짝 맺혀 있던 웃음기가 씻은 듯이 사라졌다.

만약 정말로 이곳에 동정어옹이 있다면 전투는 불가피한 상황.

그의 무위가 정확히 어느 정도인지는 모르나, 동정어옹 정도의 초절정 고수가 기습해 온다면 제대로 받아칠 수 있는 건 나와 청풍 정도가 고작이다.

“명심해. 방심하면 죽는다.”

물론 그런 일이 생기지 않도록 최선을 다하겠지만 무인의 생사(生死)는 찰나에 갈리는 법이다.

무겁게 고개를 끄덕이는 사람들을 뒤로하고 돌아서려던 그때, 혁무진이 불쑥 입을 열었다.

“뭐 하십니까?”

“같이 찾아야지. 나 혼자 놀고 있을 줄 알았냐?”

“아니, 그 말이 아니고요. 나룻배에 남아 계시려던 거 아니었습니까?”

“절벽은 청 소협과 궁기방이 있으니 됐고, 아래에는 네가 남아 있을 테니까 나는 다른 곳을 찾아봐야지.”

“다른 곳이라뇨. 더 뭐가 남았…….”

뭔가 말을 이으려던 혁무진이 멈칫했다.

“혹시?”

“맞아.”

나는 출렁이는 강물을 내려다보며 말했다.

“물속도 찾아봐야지. 다른 사람도 아니고 동정어옹의 비처라면 충분히 가능성 있는 일이니까.”

“하지만 수공(水功)도 익히신 적 없잖아요?”

“음. 그럴걸?”

내 당당한 대답에 벽호공으로 절벽을 오르려던 청풍과 궁기방. 그리고 노를 무기처럼 바짝 치켜든 늙은 사공도 한마디씩 보탰다.

“은인. 전에 할아버지께서 그러셨는데, 물속에서 수공의 고수를 상대하는 건 반드시 피하라고 하셨어요.”

“내 생각도 같다. 수공을 익히지 않은 네가 넓은 구간을 모두 찾아볼 수도 없을 뿐더러, 상대가 동정어옹이라면 더더욱 피해야지.

“저, 귀인께서 뛰어난 무인이신 건 알겠지만 이곳은 수심이 깊고 물살이 강하여 까딱 잘못하면 정말 큰일이 날 수도 있습니다요.”

어느 것 하나 틀린 점을 찾기 힘든 말들이다.

초절정 고수 간의 싸움은 아주 사소한 한 가지로 승패가 가리는 법.

하물며 육지와 수중 전투는 그 차이가 하늘과 땅 차이라고 할 수 있었다.

‘내가 익힌 무공이 물속에서 유독 취약한 편이기도 하고.’

열화문의 무공 대부분은 열양지기. 즉 화기(火氣)를 바탕으로 이루어져 있다.

그러니 무공의 특성상 수중에서는 육지에서와 같은 위력을 발휘하기 어려울 수밖에 없었다.

적천강이 장강을 질색하는 이유 역시 생사결이 벌어지면 스스로에게 불리한 전장이라는 것을 알기 때문이다.

“…….”

음. 취소. 다시 생각해 보니 그냥 물 자체를 싫어하는 것 같다.

어쨌거나 동정어옹이 남들의 시선과 발길이 닿지 않는 비처를 물속에 마련했다고 해도 그리 놀라운 일은 아니었다.

그는 물고기처럼 호흡하고 그보다 더 빨리 움직일 수 있는 수공의 대가니까.

하지만 나 역시 아무 생각 없이 나선 것은 아니다.

수영 경력이라고는 일곱 살 때 다녔던 어린이 수영 교실이 전부인 내가, 저 깊고 거친 물속으로 들어가겠다고 마음먹은 이유는 따로 있었다.

‘아직 한 번도 써 보지는 못했지만…… 설명대로라면 가능성은 충분해.’

짧게 호흡을 내뱉은 나는 상의와 신발을 벗었다.

그리고 갑작스러운 행동에 깜짝 놀란 혁무진이 만류할 틈도 없이, 곧장 강물을 향해 뛰어들었다.

첨벙, 촤아아악!

물속은 얼음장처럼 차가웠고, 동시에 맑았다.

무리 지어 헤엄치는 형형색색의 물고기들. 까마득한 아래에는 정체를 알 수 없는 해조류가 넘실거린다.

그리고…… 마침내 기다리던 소리가 울려 퍼졌다.

띠링. 띠링. 띠링.



- [수상 구조대원]의 칭호 효과가 발동되었습니다!

- 칭호에 내장된 특수 스킬이 적용됩니다!

- [수상 구조대원의 물갈퀴]가 생성되었습니다!

- [수상 구조대원의 아가미]가 생성되었습니다!

- 특수 스킬은 앞으로 24시간 지속 되며, 향후 일주일간 사용하실 수 없습니다!

- 당신이 익힌 무공이 주위 환경과 적합하지 않습니다. 수중에서 [열화문]의 무공을 발휘할 시, 그 위력이 20퍼센트 감소합니다!



시스템 알림과 동시에, 나를 둘러싼 변화가 시작되었다.

솨아아아.

나에게만 보이는 은은한 빛이 전신을 스치자, 발과 손가락 사이에 투명한 물갈퀴가 생성되었다.

‘이건…….’

분명 물 속임에도 움직임이 육지에서처럼 가볍다.

눈앞의 시야는 더욱 또렷해졌고 참고 있던 숨을 내뱉자 차가운 물이 공기가 되어 폐로 밀려 들어왔다.

‘효과가 생각 이상이야.’

돌발 퀘스트였던 [동정호의 비극]을 완료하고 얻었던 칭호, [수상 구조대원]이 이렇게 빨리 도움이 될 줄은 몰랐다.

‘이거라면 충분하지.’

씩 웃은 나는 부드럽게 헤엄치기 시작했다.

투명한 물갈퀴로 거센 물살을 가르며, 물고기보다 빠른 속도로 저 어딘가를 향해 나아갔다.
```

## Final English reading copy

```markdown
# Chapter 461

In terms of speed, a ferryboat was inferior not only to the Yangtze River Channel League’s swift ships but even to ordinary vessels. Especially in weather as foul as today’s.

*Hoooooosh, splash!*

The ferryboat rocked in the fierce wind and churning current.

A smaller hull meant less resistance to external conditions. Veins bulged on the arms of the old boatman gripping the oars.

As befitted an experienced boatman, he had guided the ferryboat skillfully despite the bad weather. But the closer we came to our destination, the more violent the current grew, and he was nearing his limit.

*This is probably too much for him from here on.*

It would have been insane to come this far relying on nothing but a single ferryboat and an old boatman.

I rolled my neck from side to side, then stepped forward.

“Shall we begin?”

At my single sentence, three people opened their eyes. They had been circulating their qi without moving an inch despite the rocking hull.

“I’m ready, Benefactor.”

“To use one of the Beggars’ Sect’s finest arts for something like this… Master would certainly have a thing or two to say if he saw me.”

“Captain. What should I do?”

Once Cheongpung, Gung Gibang, and Hyuk Mujin had replenished their qi by circulating it, I quickly gave them their orders.

“Young Hero Cheongpung, follow me to the stern. Gung Gibang, take the front. Mujin, you protect the boatman. I’ll call for you when I need you, so move the moment I do.”

As the three men moved according to my instructions, the old boatman, who had been struggling to row, blinked.

“E-excuse me, what exactly are you saying…?”

But before he could finish, the fierce palm force shot from Cheongpung’s hands slammed into the water.

*Boom! Fwoooooosh!*

“Waaaaaagh!”

The so-called palm-force booster.

Far smaller and lighter even than the sleek-hulled swift ships, the ferryboat shot into the air.

The boatman’s scream mingled with the wind that tore past us.

Using that scream as my signal, I stepped forward.

*Now.*

*Whoooosh!*

Just as the ferryboat that had risen into the air was about to settle back onto the surface, I drew up the internal energy filling my dantian and sent it toward my palms.

*Boom! Booooom!*

With my mastery of the Flame Divine Palm now at eighty percent, its heat made the surrounding air scorching hot. The ferryboat, which had seemed about to descend, sprang upward like a flying fish.

The boatman’s eyes widened. With trembling fingers, he pointed ahead.

“Reefs! There are reeeefs ahead!”

Did anyone really think the Dongting Fisherman would establish one of his secret refuges somewhere easy to reach?

The route we were taking was too narrow for ordinary vessels to enter. The current was also unusually strong, making it difficult for a light boat like a ferryboat to escape once it was caught in the flow.

Once the current swept a boat away, it would be easy for it to crash against one of the reefs scattered throughout the passage.

“You fucking bastards! I told you I wasn’t coming!”

At the exact moment the old boatman let out a heartfelt scream, I shouted a name.

“Gung Gibang!”

“Got it!”

Gung Gibang answered energetically and flung his sleeves, which were little more than rags.

The Eighteen Dragon-Subduing Palms, said to be passed down only to two people in the Beggars’ Sect of a hundred thousand disciples—the Beggars’ Sect Leader and the Successor Beggar—burst through the air.

*Kwoooooo-boooom!*

Under the barrage of palm force pouring down like a rain shower, the reef standing like an iron wall shattered into countless fragments.

The second and third reefs that appeared soon afterward could not withstand the might of the Eighteen Dragon-Subduing Palms either.

*Kraaaaaash!*

The ferryboat broke through the scattered fragments of reef and landed on the surface.

Spray surged up on both sides of the hull, and several fish that had leaped from somewhere slapped the old boatman across the cheeks.

“Gah… Uhhh…”

He was completely out of it.

I shook the shoulder of the drooling boatman, whose eyes had gone half vacant.

“Wake up. Stay with us.”

“Ugh… Uhhh. You fucking…”

“This isn’t going to work. Mujin.”

“By your command.”

Hyuk Mujin rolled up both sleeves and delivered a solid slap.

*Smack!*

The boatman’s eyes refocused.

“Gah! What was that for?”

*Smack!*

“…But I was already awake.”

“Stop.”

“Yes, sir.”

Nothing brought someone to their senses like a good slap across the face.

I asked the boatman, who was rubbing his reddened cheeks,

“About where are we?”

“No matter how honored you are, how can you treat a person like this…?”

“Mujin.”

“By your command.”

“I’ll check right away, sir.”

The boatman sprang to his feet and looked around.

The river was narrow enough that only two or three ferryboats could barely pass through at once.

Sheer cliffs rose on both sides, while violent currents swirled across the surface. Thick fog hung over everything.

The old boatman narrowed his eyes and examined the area carefully before nodding.

“Yes. This is the first of the places you mentioned.”

According to the Lower District Sect’s information, which Honglan had passed on to us, there were five locations considered likely to be the Dongting Fisherman’s refuge.

The place we had reached was the closest of them.

It was certainly good news, but it was too early to celebrate.

“Coming here quickly is great and all, but… how are we supposed to find it now?”

At Gung Gibang’s question, I scanned our surroundings and answered,

“I don’t know. The information Young Lady Hong gave us wasn’t exact, either. We’ll have to search the area thoroughly.”

“Ugh. This is going to take forever.”

“Don’t say such unlucky things. At least be grateful that Young Lady Hong’s information got us this far.”

A secret refuge wasn’t called a secret refuge for nothing.

Honglan’s information had not given us its exact location, but merely narrowing down the Dongting Fisherman’s unknown hideout to this area was already a major gain.

Even if we came up empty-handed at the first location, we would eventually catch something if we kept narrowing the net.

*Or it might jump out on its own before we catch it.*

As I kept a close eye on our surroundings, I suddenly felt a prickling sensation on my face.

I turned my head slightly. The four pairs of eyes staring at me with strange expressions immediately darted away.

“What?”

“W-what are you talking about? I was just… I thought it was nice that you were thinking about Young Lady Hong even in the middle of all this.”

“Ahem. Captain, you have my support.”

“Ah, youth is a fine thing. I was popular with the ladies myself until about thirty years ago. They once called me the Dongting Lake Heart-String Fisherman. Hahaha.”

“…”

I knew perfectly well what they were thinking.

I was inwardly clicking my tongue when my eyes happened to meet Cheongpung’s. He flinched like a bird that had been shot and waved both hands.

“No! No, Benefactor! I wasn’t thinking about anything!”

“What on earth were you thinking about? I haven’t even said anything yet.”

“Really, I wasn’t! I swear I wasn’t imagining Young Lady Hong and Benefactor falling madly in love, getting married, having two children, and living happily ever after! I wasn’t imagining myself living next door to Benefactor and visiting you often, either!”

“…”

“Gasp!”

Only then did Cheongpung realize his mistake. He clapped both hands over his mouth, but it was already too late.

*He imagined all that in the space of a few seconds?*

At that level, he could quit being a martial artist and become a novelist.

His pen name would be Huashan Divine Dragon. If he published it under the Huashan Sect’s name and got Sword Saint Mae Jonghak to write a blurb, it would sell like hotcakes.

Of course, if he made me the protagonist, he would get the shit beaten out of him just as quickly.

“Good grief. What is wrong with you people…? Never mind. Forget it.”

There was no point in talking. My mouth would only hurt.

I sighed and quickly issued new orders—not because my face had felt inexplicably hot for some time, and not because the faint scent clinging to Honglan’s silver hairpin kept brushing against the tip of my nose.

*…Really.*

“Young Hero Cheongpung and Gung Gibang, use the Wall Lizard Technique to search the cliffs. Mujin, circle around in the boat and search below. We don’t know what might appear or when, so don’t let your guard down for even a moment.”

At my serious voice, the faint smiles at the corners of everyone’s mouths vanished as though they had been washed away.

If the Dongting Fisherman really was here, a battle would be unavoidable.

I did not know exactly how powerful he was, but if a Supreme Peak master of the Dongting Fisherman’s caliber launched a surprise attack, Cheongpung and I were probably the only ones who could properly meet it.

“Keep this in mind. If you let your guard down, you die.”

Of course, we would do everything in our power to prevent that from happening. But in the world of martial artists, life and death could be decided in an instant.

I turned away from the people nodding heavily, but Hyuk Mujin suddenly spoke.

“What are you doing?”

“We’re searching together. Did you think I was going to sit around and have fun by myself?”

“No, that’s not what I meant. Weren’t you planning to stay on the ferryboat?”

“Cheongpung and Gung Gibang are covering the cliffs, and you’ll be down below, so I have to search somewhere else.”

“Somewhere else? What else is left…?”

Hyuk Mujin stopped mid-sentence.

“Could it be?”

“That’s right.”

I looked down at the churning river and said,

“We have to search underwater too. If it were anyone else, I might not consider it, but this is the Dongting Fisherman’s refuge. It’s a perfectly reasonable possibility.”

“But you’ve never learned water arts, have you?”

“Hmm. I don’t think so.”

At my confident answer, Cheongpung and Gung Gibang, who had been about to climb the cliffs with the Wall Lizard Technique, added their own comments. Even the old boatman, who had raised his oar as if it were a weapon, joined in.

“Benefactor, my grandfather told me that one must absolutely avoid fighting a master of water arts underwater.”

“I agree. You haven’t learned water arts, so you can’t search this entire stretch. And if your opponent is the Dongting Fisherman, you should avoid it all the more.”

“I know that you’re a skilled martial artist, honored sir, but the water is deep here and the current is strong. If you make even one mistake, you could truly be in grave danger.”

There wasn’t a single flaw in any of their arguments.

Battles between Supreme Peak masters could be decided by one tiny detail.

And the difference between fighting on land and fighting underwater was like the difference between heaven and earth.

*The martial arts I’ve learned are especially vulnerable underwater, too.*

Most of the Fire Gate Clan’s martial arts were based on Scorching Yang Qi—in other words, fire qi.

By their very nature, those martial arts could not help but lose power underwater compared to their performance on land.

That was also why Jeok Cheongang hated the Yangtze so much. He knew that if a life-and-death duel took place there, it would be a battlefield disadvantageous to him.

“…”

Hmm. I take that back. Thinking about it again, he probably just hated water itself.

Regardless, it would not have been particularly surprising if the Dongting Fisherman had established a secret refuge underwater, away from other people’s eyes and footsteps.

He was a master of water arts who could breathe like a fish and move even faster than one.

But I had not stepped forward without a plan.

My entire swimming career consisted of the children’s swimming class I had attended when I was seven. There was another reason I had decided to enter those deep, raging waters.

*I haven’t used it even once yet, but if the explanation is accurate, it should be more than possible.*

I let out a short breath and removed my shirt and shoes.

Before Hyuk Mujin could stop me, startled by my sudden action, I jumped straight into the river.

*Splash! Whoooooosh!*

The water was as cold as ice, and crystal clear at the same time.

Schools of brightly colored fish swam together. Far below, unidentifiable aquatic plants swayed in the depths.

And then… at last, the sound I had been waiting for rang out.

*Ding. Ding. Ding.*

> **System**
>
> - The **Water Rescue Worker** Title’s effect has activated!
>
> - The special Skill embedded in the Title has been applied!
>
> - **Water Rescue Worker’s Webbing** has been generated!
>
> - **Water Rescue Worker’s Gills** have been generated!
>
> - The special Skill will last for 24 hours and cannot be used again for the next week!
>
> - The martial arts you have learned are incompatible with the surrounding environment. When using **Fire Gate Clan** martial arts underwater, their power is reduced by 20 percent!

At the same time as the System notification, changes began around me.

*Shhhhhhh.*

A faint light visible only to me swept across my entire body. Transparent webbing formed between my fingers and toes.

*What is this…?*

Even though I was underwater, my movements felt as light as they did on land.

My vision grew even clearer. When I exhaled the breath I had been holding, the cold water turned into air and rushed into my lungs.

*The effect is even better than I expected.*

I had never imagined that the Title I had earned after completing the sudden Quest *The Tragedy of Dongting Lake*—**Water Rescue Worker**—would become useful so quickly.

*This is more than enough.*

Grinning, I began to swim smoothly.

I cut through the fierce current with my transparent webbed feet and moved toward somewhere in the distance at a speed faster than a fish.
```
