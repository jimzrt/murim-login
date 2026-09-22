<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0698.txt",
      "sha256": "8f6a3764f06ccc9c5779f982b64234f524cc603066f6f7b1849119799574edca",
      "bytes": 12993
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "2945f31c593768e2f7eced6ec26d76acd1bef6cb6e6a374e7349c091cccfb577",
      "bytes": 2196
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "c5c36f4be27d07867e50108548bd6f75f099e17517bffaaa16221260eeb4bcce",
      "bytes": 205541
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "32229e3aa35ebf44b52260787b38f204df40839a0375797c1e333e9cac872e98",
      "bytes": 895
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "0b8ee596c23c844432d7d8b9ca8861bd4f7e7d477c5716ea0ed6ff1223109f76",
      "bytes": 553
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "a9cf02864a0b1e37be659ac842dd1daf6de0d006d0e49b4c4a691d9c253d7e18",
      "bytes": 667
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "7f8f6d0bbf8460dac4714c39afe740181fef98467c8f605e0f47f85cd8af4d52",
      "bytes": 1924
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "5645c67070642359befc96f11419612425cfb00aaea31c6f75947fde76fedbed",
      "bytes": 622
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "ca7d12f36149d750048390d94cd4ea1295236d43762f6c09d56182e158d76ac7",
      "bytes": 810
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "000b5610a65ee13a0424f5bf9b6cad61d22b5af956918434e5113fd905930b54",
      "bytes": 888
    },
    {
      "path": "characters/White Tiger.md",
      "sha256": "069318bd83d383b2fd77ade0fe8a823acf3ff4e9ca91e6170180623f6e2d402e",
      "bytes": 588
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "9bbd6c33b4e42087c264a79df4e0649e31b4c05e968065f0d0105904bb95a225",
      "bytes": 621
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "a9e60e63dddd29fcdc4029b8338f2e9cf61f581ee4663afc34fb1915e43ae831",
      "bytes": 215210
    }
  ],
  "estimated_tokens": 11940
}
-->

# Durable State Update — Chapter 698

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 698. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 698. Profile updates may replace only one
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
  "chapter": 698,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 698,
    "continuity_sources": [698],
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
    "Jin Taekyung and the beast army have entered the Outer Palace and destroyed five watchtowers.",
    "Yohi has returned alive and is advancing beside Jin without restraints.",
    "The guardian spirit and Muyaho are accompanying Jin and Yohi at the head of the beast army.",
    "Baeksang has publicly acknowledged Yohi and admitted betraying everyone for a purpose pursued over decades.",
    "The Southern Heaven Demon Empress is revealed to be Honglan, the former Lower District Sect singing courtesan who deliberately approached Jin at Dongting Lake.",
    "The Southern Heaven Demon Empress is vastly stronger than Jin expected and can split the force of his Flame Divine Palm.",
    "The guardian spirit recognizes the Southern Heaven Demon Empress from the imugi's memories as an old, hideous, malicious human and condemns her as a Fiend.",
    "The Southern Heaven Demon Empress has created a massive rift behind the Inner Palace.",
    "The rift is releasing demonic qi that can corrupt living beings and is already affecting the humans and beasts nearby.",
    "The Southern Heaven Demon Empress regards the rift's transformation as evolution and as a blessing from the Lord of Heaven.",
    "An unidentified radiance has swallowed the darkness emerging from the rift."
  ],
  "continuity_sources": [
    697
  ],
  "open_questions": [
    "What is the unidentified radiance that swallowed the darkness?",
    "Will the rift fully open, and what changes will its demonic qi cause?",
    "Can Jin's hidden card stop the Southern Heaven Demon Empress or the rift?",
    "What is the full purpose of the Lord of Heaven's plan?",
    "What purpose did Baeksang pursue for decades?"
  ],
  "safe_through": 697,
  "temporary_decisions": [
    "Use Whitey for Jin's nickname 흰둥아.",
    "Use civil war for 내전 and fighting spirit for 전의.",
    "Use the quoted paraphrase “Do everything in your power, then leave the result to Heaven and wait” for 진인사대천명.",
    "Use rift for 균열 and evolution for 진화.",
    "Retain Guardian spirit for 수호령, Benefactor for 은인, and Great Chieftain for 대족장."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 상태               | **Status**                     |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 창룡후 | **azure dragon's roar** | Battle cry released by Tang Jinhu. |
| 지풍 | **Finger Qi** | Invisible qi attack fired by the Western Heaven Demon Lord. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 창룡 | **Azure Dragon** | Divine dragon form invoked in Hyeongong's blessing. |
| 장성 | **Great Wall** | Wall used in the discussion of the Outer Lands. |
| 영물 | **spiritual creature** | Known non-human creature contrasted with unheard-of monsters. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 서천 | **Western Heaven** | Short form used by the Lord of Heaven for the Western Heaven Demon Lord. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 백족 | **Bai people** | Ethnic group encountered in Yeongin. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 수왕석 | **Beast King Stone** | Legendary sacred treasure of the Nanman Beast Palace. |
| 외궁 | **Outer Palace** | The outer compound of the Nanman Beast Palace. |
| 대족장 | **Great Chieftain** | Title used for the senior Nanman leader who supposedly ordered the inspection. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 궁주 | **Palace Lord** | Title Yohi uses after realizing that Heugung is the Beast Miao King. |
| 수호령 | **guardian spirit** | Ancient title for the Black Tiger. |
| 신석 | **sacred stone** | Stone said to have existed alongside the Black Tiger's birth. |
| 동문 | **East Gate** | One of the Nanman Beast Palace's gates. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 서천마군 | 진태경 | hostile_opponents | you | calm and taunting | Uses 자네 while questioning Taekyung and offering to take him alive. |
| 진태경 | 서천마군 | hostile_opponents | Western Heaven Demon Lord | casual and defiant | Identifies the Demon Lord by title and answers his surrender demand with sarcasm. |
| 서천마군 | 신의 | hostile_invader_to_physician | Divine Physician | calm and mocking | Uses 신의 and 그대 while taunting the physician and dismissing his objections. |
| 신의 | 서천마군 | physician_to_invading_fiend | fiend | defiant and formal | Calls the Western Heaven Demon Lord an 악귀 and orders him to leave. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 요희 | 진태경 | Yao great chieftain to Murim Alliance pavilion master | Jin Taekyung | casual and probing | Identifies him by his full name while allowing him to keep the mask on. |
| 진태경 | 요희 | Fire Dragon Pavilion pavilion master to Yao great chieftain | you | guarded and blunt | Answers Yohi's probing questions directly while warning her about Ju Hwaran. |
| 백상 | 요희 | Bai great chieftain to Yao great chieftain | Yohi | cold and formal | Calls to Yohi from outside the tent at the chapter's end. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 진태경 | 백호 | human ally to intelligent spiritual beast | you | casual and familiar | Converses with White Tiger after interpreting its warning. |
| 백상 | 남천마후 | Nanman Great Chieftain to hostile demon empress | Southern Heaven Demon Empress | formal and shocked | Baeksang directly identifies the woman who appears before him. |
| 남천마후 | 백상 | Dark Heaven controller to coerced Nanman leader | Great Chieftain Baeksang / Palace Lord | playful, taunting, and threatening | She repeatedly addresses Baeksang while mocking his grief, acknowledging his effort, and issuing her order. |
| 백호 | 진태경 | guardian_spirit_to_human_ally | you | terse and irritated | The White Tiger responds telepathically after Jin calls it Whitey and jokes about its former name. |
| 진태경 | 수호령 | human ally to guardian spirit | guardian spirit | quiet and commanding | Jin whispers that they should go as they advance toward Baeksang. |
| 수호령 | 남천마후 | guardian_spirit_to_hostile_supernatural_opponent | you | terse, accusatory, and contemptuous | The guardian spirit tells the Southern Heaven Demon Empress that it knows her true essence and condemns her as a Fiend. |
| 남천마후 | 수호령 | hostile_supernatural_opponent_to_guardian_spirit | hideous beast | playful, taunting, and dismissive | She insults the guardian spirit while addressing it as a beast. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 697
- **Aliases:** None
- **Role:** Baeksang is the Palace Lord of the Nanman Beast Palace and sole Great Chieftain of Nanman, and he has publicly admitted betraying all Nanman people to pursue a purpose maintained for decades.
- **Personality:** Cold, rigid, meticulous, and strategically resolute, yet burdened by regret, grief over Hwi's death, and a final conflicted impulse to spare others from the coming bloodshed.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of deceased Baekhwi, whom the Great Snow Fiend killed; he cultivated Yohi with gold and influence and used her support to advance Dark Heaven's preparations.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 697
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 693
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 697
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, and the leader of the beast-army assault confronting Baeksang and the revealed Southern Heaven Demon Empress inside the Nanman Beast Palace.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 697
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 697
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress is Honglan, the former Lower District Sect singing courtesan, and the creator of the massive rift behind Nanman's Inner Palace that releases demonic qi under the will of the Lord of Heaven.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and regards Jin's destruction of her trap with amused surprise.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 684
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

### White Tiger.md

# White Tiger (백호)

- **Safe through:** Chapter 697
- **Aliases:** Whitey
- **Role:** The White Tiger is the guardian spirit of the sacred stone, restored to its former silver-white tiger form and leading Jin Taekyung and the vast beast army into the Outer Palace.
- **Personality:** Irritable and contemptuous of Jin Taekyung's jokes.
- **Voice:** Telepathic, terse, and easily exasperated.
- **Relationships:** The White Tiger carries Jin Taekyung and Yohi, guards the sacred stone, and advances with Jin's forces.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 696
- **Aliases:** None
- **Role:** Yohi is the female Great Chieftain of the Yao people who has returned to the Nanman Beast Palace with Jin Taekyung and now stands against Baeksang.
- **Personality:** Yohi is charismatic, proud, perceptive, and fiercely resistant to Heugung's betrayal and coercion.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people, hates Heugung after his betrayal, and is being coerced to support his false account by the threat against Boshan and her people.

## Korean source

```text
＃698화



저게 뭐지?

뇌리를 가득 채운 한 줄기 의문과 함께, 남천마후의 눈이 크게 뜨였다.

빛.

그것은 지금껏 보아 온 어떤 것보다 크고, 밝은 빛이었다.

갑작스럽게 터져 나온 거대한 광휘(光輝)가 터질 것처럼 부풀어 오르고, 다가오는 어둠을 집어삼키며 세상에 스며들고 있었다.

콰아아아아!

아득한 허공을 향해 솟구친 빛의 기둥이 하늘을 관통한다. 먹구름의 일부가 흩어진 틈새로 쏟아지는 햇볕.

석벽을 넘어 파도처럼 들이닥치던 어둠은 광휘에 닿은 순간 무언가에 가로막힌 것처럼 주춤거렸다.

‘……막혔다고? 그것도 균열에서 불러온 마기(魔氣)가?’

믿을 수 없는 현상.

‘균열’의 마기는 매우 강력하며 순수한 어둠의 힘이다. 수백 년간 수행을 쌓은 이무기조차 그 힘을 오롯이 감당하지 못해 타락해 버렸을 만큼.

하지만 지금 남천마후의 눈 앞에 펼쳐진 광경은 모두 틀림없는 현실이었다.

서서히 흩어져 가는 먹구름과, 광휘에 가로막혀 더 이상 나아가지 못하는 어둠의 파도.

그리고.

“이야. 이게 진짜 되네.”

“……!”

진태경.

광휘의 중심에서 우뚝 선 채, 씩 웃으며 자신을 바라보는 한 청년의 모습에 남천마후는 이를 악물었다.

“도대체…… 도대체 어떻게.”

말을 채 잇지 못하는 남천마후를 향해, 진태경은 어깨를 으쓱해 보였다.

“별거 아냐. 누구나 꿍쳐 둔 신물(神物) 하나쯤은 있잖아. 안 그래?”

“……!”

신물.

그 두 글자가 단단한 망치가 되어 남천마후의 뒤통수를 후려친다.

그제야 천천히 미끄러진 그녀의 시선에 진태경이 아닌, 또 다른 존재가 닿았다.

‘저 짐승.’

거대한 백호. 과거 남천마후가 타락시켰던 이무기처럼 영물(靈物)을 넘어선 것이 확실한 백호가 포효하듯 아가리를 벌리고 있다.

눈부신 광휘 사이로 영롱하게 빛나는 형체가 어렴풋이 보이는 듯했다.

그리고 동시에 스치듯 뇌리를 관통하는 이 땅의 옛 전설.

“……수왕석(獸王石).”

석류처럼 붉은 입술 사이로 흘러나온 목소리에, 진태경이 피식 웃었다.

“어. 아네?”

어찌 모를 수 있을까.

천하의 모든 짐승이 엎드려 복종한다는 왕의 증표. 장장 수백 년에 달하는 세월 속에서 사라진 남만의 신물을.

아니, 모를 수조차 없다. 남천마후는 수왕석을 찾기 위해 이 험준한 남만 땅을 이 잡듯 뒤졌던 장본인이었으니까.

그것도 무려 십 년이 넘는 시간 동안이나.

하지만 강산이 변할 만큼의 세월이 흘렀음에도 수왕석의 실체에 관한 작은 단서조차 얻지 못했고, 남천마후는 케케묵은 전설을 뒤로하고 대계(大計)를 시작해야 했다.

그런데. 그런데 어째서.

“네놈들이이이!”

후우우우웅! 콰지직!

끔찍할 만큼 거대한 기운이 일어나 사방을 짓누른다.

이빨을 드러내며 으르렁거리던 수많은 짐승들이 꼬리를 내리고, 주위를 가득 메운 전각이 거인의 발에 밟힌 것처럼 무너지기 시작한다.

비명을 지르며 외궁에서 뛰쳐나온 부족민들이 허공에 우뚝 선 존재를 발견하고 입을 벌렸다.

“아. 아아……!”

어둠.

넘실거리는 짙은 어둠을 전신에 두른 한 여인이 지상을 굽어보고 있었다.

마치 신처럼, 전설 속에 등장하는 악귀(惡鬼)처럼 남은 목숨을 가늠하고 있었다.

그러나 모두의 두려움과는 달리, 남천마후의 시선은 오직 한 곳에 못 박혀 있었다.

“내놓아라.”

쿠르릉.

하늘을 메운 먹구름이 커다란 울음소리를 토해 낸다.

빛과 어둠이 공존하는 세상 속에서 울려 퍼진 스산한 목소리가 모두의 귓가를 파고들었다.

“그것은 마땅히 천주(天主)께서 취하셔야 하는 것. 너희처럼 하찮은 존재가 지닐 수 있는 물건이 아니다.”

짐승도, 인간도.

그 압도적인 힘과 공포 앞에 모두가 얼어붙었다. 비명을 지르는 것도, 도망치는 것도 잊은 채 그저 넋 나간 눈빛으로 허공을 바라볼 뿐이었다.

단 두 사람. 아니, 두 존재를 제외한 모두가 그러했다.

“지랄한다, 미친년.”

- 한낱 인간 따위가 감히 신석(神石)을 탐하느냐.

진태경과 수호령은 허공에 우뚝 선 남천마후를 응시했다.

구구구궁!

느껴진다. 저 작은 몸뚱어리에 웅크린 미증유(未曾有)의 힘이.

주위를 짓누르는 기운의 크기는 수호령이 지난 수백 년간 마주했던 어떤 인간보다 강대했고, 과거 진태경이 몇 번이나 죽을 고비를 넘어가며 상대했던 서천마군을 뛰어넘었다.

‘강하다.’

그리고 두렵다.

살아 있는 생명체라면 누구나 떠올릴 감정. 하지만 두려움을 느끼는 것과 두려움에 사로잡히는 것은 근본적으로 다르다.

지금 이 순간에도 전신을 짓누르는 두려움을 견디고 나아가야 비로소 승리할 수 있다는 것을, 그들은 알고 있었다.

- 많은 피가 흐를 것이다, 인간이여.

“시벌. 이번에 살아남으면 남만 쪽으로는 오줌도 안 싼다.”

씹어뱉듯 중얼거린 진태경은 백염의 창대를 굳게 말아쥐었다.

그리고 자신의 등 뒤에서 굳어 있던 요희를 향해 나직히 말을 건넸다.

“뭘 해야 하는지 알고 있지?”

“……!”

“당장 사람들을 데리고 이곳을 벗어나. 죽을힘을 다해서. 최대한 멀리.”

외궁에는 당장 시야에 들어온 이들을 제외하더라도 수많은 부족민들이 거주하고 있다.

진태경으로서는 곧 이 자리에 펼쳐질 끔찍한 지옥도(地獄道)에 그들의 모습을 그려 넣는 것은 피하고 싶었다.

피를 흘리는 것은 힘 있는 자들만으로 족하다. 병장기도, 날카로운 이빨도 없는 부족민들은 살아남아야 한다.

설령 남천마후에 의해, 이 자리의 모두가 죽더라도.

‘하지만…… 내가. 우리가 막는다.’

현재 균열에서 흘러나온 마기는 신석의 힘에 가로막힌 상태.

이 팽팽한 대치가 얼마나 이어질지는 모르지만, 상황이 더 악화되기 전에 남천마후를 쓰러트리고 균열을 닫아야 한다.

‘무슨 수를 써서라도.’

후우.

크게 심호흡한 진태경은 허물어진 전각의 잔해 위, 까마득한 허공에 우뚝 선 존재를 노려보았다.

남천마후. 이 땅에서 일어난 모든 사건의 시작이자 끝.

누군가는 쓰러져야 이 잔혹한 이야기의 결말을 볼 수 있다.

“가자.”

낮은 목소리가 입술을 비집고 흘러나온 그 순간.

- 크와아아아앙!

맹렬한 포효가 바람을 찢었다.

어둠에 부딪혀 조금씩 사그라들던 광휘가 부풀어 오르고, 겁에 질려 있던 짐승과 인간들의 정신을 일깨운다.

화륵, 콰아아아!

포효와 함께 터져 나온 빛. 그리고 은빛 창날을 휘감으며 타오른 화염.

수백 년 만에 이 땅을 찾아온 이방인이 거대한 백호와 한 몸이 되어 솟구친다.

쾅!

땅을 박차고.

팟!

보이지 않는 공기와 바람을 밟고.

쐐애애액!

아득한 상공에 펼쳐진 어둠을 향해.

아니.

어둠을 받아 더욱 강력해진 한 존재를 향해.

“남천마후(南天魔后)-!”

화염을 머금은 창룡후(蒼龍吼)가 창날과 함께 공간을 가르며 날아든다.

더 이상 아름다움이라고는 찾아볼 수 없는, 악귀처럼 일그러진 여인의 얼굴에 섬뜩한 기운이 떠올랐다.

“천주께서 원하신다.”

그 순간.

파앗!

혼탁하게 뒤섞인 빛과 어둠이, 남만야수궁을 물들였다.



* * *



고오오오옹.

하늘이 갈라지는 듯한 굉음과 함께 사방을 휩쓰는 거대한 기운.

순간 터져 나오는 눈부신 섬광에 본능적으로 눈을 감은 백상은, 전신을 밀어 내는 광풍(狂風)을 느끼며 침음성을 삼켰다.

‘흡.’

이 얼마나 강대한 힘이란 말인가.

초절정 고수인 그조차 몸을 가누기 힘든 후폭풍.

마침내 눈을 떠 보니 이미 사방은 초토화되어 있었고, 맹수들의 보호로 인하여 간신히 목숨을 건진 부족민들은 비명을 지르며 도망치고 있었다.

“꺄아아아악!”

“호야! 호야! 어디 있느냐!”

“어, 어머니!”

긴 세월 동안 쌓아 올린 전각과 가옥은 하나둘씩 붕괴됐고, 허물어진 돌담에 깔려 신음하는 노모의 모습에 장성한 아들을 울부짖는다.

비명과 죽음. 피와 시신.

불과 며칠 전만 하더라도 웃음소리와 풍악으로 가득하던 거리의 모습은, 이제 어디에서도 찾아볼 수 없다.

그저 끊임없는 굉음과 비명만이 곳곳에서 흘러넘칠 뿐.

쾅. 콰아아앙!

찰나의 순간. 서로를 향해 쉼 없이 쏘아지고, 얽혀드는 빛과 어둠.

그 혼탁한 섬광과 하늘이 쪼개지는 듯한 굉음 아래에 펼쳐진 지옥도를 공허하게 바라보던 백상은, 불현듯 한 방향을 향해 손을 뻗었다.

퍼엉!

공간을 가로지르며 발출된 장력(掌力)이 커다란 바위를 걷어 낸다.

지옥도 속에서도 돌담에 깔린 노모를 구하기 위해 애쓰던 반백의 중년인이 눈을 부릅떴다.

“다, 당신은…….”

어디선가 마주치기라도 한 것인지. 왠지 모르게 낯익은 얼굴.

분노와 고마움이 뒤섞인 표정으로 노모를 부축하는 중년인을 물끄러미 바라보던 백상은, 이윽고 드러난 노파의 얼굴을 본 순간 깨달았다.

‘닮았구나, 많이.’

그녀다. 모든 것이 시작되기 전, 직접 명령을 내려 내궁에서 추방시켰던 늙은 궁인(宮人).

이제는 기억하는 이도 몇 남지 않은 자신의 옛 모습을 알고 있는 그녀가 피를 흘리며 신음하고 있었다.

“콜록. 으음…….”

“어, 어머니!”

자식이 있었던가.

황급히 노모의 상태를 살피는 중년인의 모습을 지켜보던 백상은 문득 걸음을 옮겼다.

왜인지는 모른다. 그저 그래야 한다고 생각했을 뿐이다.

“다, 다가오지 마!”

적의(敵意)로 가득한 외침.

문을 닫고, 자물쇠를 걸어 잠근다고 한들 귀는 열려 있다.

이제는 남만야수궁의 모두가 알고 있었다. 자신들의 궁주가, 백족의 대족장이 그들 모두를 배반했다는 것을.

지금 이 순간에도 계속되는 비명과 죽음의 원인이, 바로 백상에게 있다는 것을.

눈앞의 중년인도 그중 하나였다. 노모를 지키기 위해 백상을 가로막은 그의 손에는 언제 집어 들었는지 모를 뾰족한 돌조각이 들려 있었다.

“하, 한 걸음이라도 더 다가오면…….”

쉭, 퍽!

지풍(指風)에 관통당한 돌조각이 바스라진다. 순간 얼어붙은 중년인을 스치듯 지나간 백상이 노파를 향해 손을 뻗었다.

투둑. 툭!

흐릿해진 손이 섬전처럼 노파의 혈도(穴道)를 짚음과 동시에, 일그러져 있던 주름진 이마가 부드럽게 펴졌다.

“쿨럭.”

죽은 피를 토해 내자 한결 편안해지는 노파의 안색.

황급히 노모의 상태를 확인한 중년인이 이해할 수 없다는 눈빛으로 백상을 바라보았다.

“어, 어째서?”

어째서라.

그 간단한 물음에조차, 백상은 대답할 수 없었다.

어쩌면 앞으로 십 년, 백 년이 지난다 해도 답할 수 없을 것이다.

그 자신조차 답을 모르니까.

결국 짧은 침묵을 깬 그의 한 마디는, 질문에 대한 답이 아니었다.

“다른 이들과 함께 떠나라. 최대한 멀리 벗어나.”

“이, 이보시오!”

“이대로 어미를 죽일 셈이냐. 아니면…….”

백상의 눈이 깊숙이 가라앉았다.

“네가 죽는 것을, 어미가 지켜보게 만들 테냐.”

“……!”

“가라. 동문(東門)으로 향한다면 활로가 열릴 것이다.”

그 말을 끝으로 백상은 돌아섰다. 뒤늦게 새어 나온 중년인의 쉰 목소리가 그의 귓가를 파고든다.

“이런다고…… 이런다고 당신이 지은 죄가 용서될 것 같소!”

그 분노한 외침에, 백상은 마음속으로 대답했다.

아니라고. 자신은 단 한 번도 용서받으리라 생각한 적도 없다고.

구구궁!

내궁(內宮)으로 향하는 그의 등 뒤로, 굉음이 내리깔렸다.

그러나 쾌속하게 쏘아지는 그의 신형에는 한 줄기의 망설임조차 없었다.

수십여 년간 그리고 그렸던, 그 순간을 마주할 때였다.
```

## Final English reading copy

```markdown
# Chapter 698

*What is that?*

Along with the single question filling her mind, the Southern Heaven Demon Empress’s eyes widened.

Light.

It was larger and brighter than anything she had ever seen.

A tremendous radiance that had erupted without warning swelled as though it might burst, swallowing the approaching darkness as it seeped into the world.

Kwooooooo!

A pillar of light shot toward the distant sky and pierced the heavens. Sunlight poured through a gap in the dark clouds.

The darkness that had surged over the stone walls like a wave faltered the moment it touched the radiance, as though something had blocked its path.

*It was blocked? Even the demonic qi summoned from the rift?*

It was an unbelievable phenomenon.

The demonic qi of the rift was enormously powerful—the pure force of darkness. Even the imugi, which had cultivated for hundreds of years, had been corrupted because it could not withstand that power in its entirety.

And yet the scene unfolding before the Southern Heaven Demon Empress’s eyes was undeniably real.

The dark clouds slowly scattering.

The wave of darkness blocked by the radiance and unable to advance any farther.

And then—

“Wow. This really works.”

“……!”

Jin Taekyung stood tall at the center of the radiance, grinning as he looked at her.

The Southern Heaven Demon Empress clenched her teeth.

“How… How in the world?”

Before she could finish, Jin Taekyung shrugged.

“It’s nothing special. Everyone has at least one divine artifact stashed away, right? Don’t they?”

“……!”

Divine artifact.

Those two words struck the back of the Southern Heaven Demon Empress’s head like a solid hammer.

Only then did her gaze slowly slide away from Jin Taekyung and land on another existence.

*That beast.*

A gigantic White Tiger. Like the imugi the Southern Heaven Demon Empress had corrupted in the past, it was clearly something beyond a spiritual creature. It had its jaws open as though roaring.

Through the dazzling radiance, she could faintly make out a form that glimmered with a crystalline light.

And at the same time, an ancient legend of this land flashed through her mind.

“……The Beast King Stone.”

At the voice that slipped between her pomegranate-red lips, Jin Taekyung let out a quiet laugh.

“Oh. You know it?”

How could she not?

The symbol of a king before whom every beast in the world bowed and submitted. A sacred treasure of Nanman that had vanished over the course of several hundred years.

No. It was impossible for her not to know.

The Southern Heaven Demon Empress was the one who had searched every inch of this rugged land of Nanman for the Beast King Stone.

For more than ten years.

Yet even after enough time had passed for mountains and rivers to change, she had failed to find so much as the slightest trace of the Beast King Stone itself. In the end, she had left the ancient legend behind and begun her grand plan.

But why?

Why now?

“You bastaaaaards!”

Whoooooosh! Crack!

A terrifyingly immense surge of qi rose and pressed down on everything around it.

The countless beasts that had been baring their teeth and growling tucked their tails between their legs. The pavilions filling the area began to collapse as though they had been crushed beneath a giant’s foot.

Tribespeople fleeing the Outer Palace in terror discovered the existence standing tall in the air and gaped at it.

“A-Ah……!”

Darkness.

A woman with deep, surging darkness wrapped around her entire body looked down upon the ground.

Like a god—or a Fiend out of legend—she was gauging how much longer they had to live.

But unlike everyone else, the Southern Heaven Demon Empress’s gaze was fixed on only one place.

“Hand it over.”

Rumble.

The dark clouds filling the sky let out a tremendous cry.

In a world where light and darkness coexisted, a chilling voice rang out and pierced everyone’s ears.

“It is something the Lord of Heaven must rightfully take. It is not an object that insignificant beings like you are fit to possess.”

Beast and human alike.

Everyone froze before that overwhelming power and terror. They forgot how to scream and how to run, staring blankly at the figure in the air.

Everyone except two people.

No—two beings.

“Bullshit, you crazy bitch.”

—How dare a mere human covet the sacred stone?

Jin Taekyung and the guardian spirit stared at the Southern Heaven Demon Empress standing tall in the air.

Rumble, rumble, rumble!

They could feel it.

The unprecedented power crouching within that small body.

The weight of the qi pressing down around them surpassed that of any human the guardian spirit had encountered over the past several hundred years. It surpassed even the Western Heaven Demon Lord, whom Jin Taekyung had fought in the past while narrowly escaping death time and again.

*Strong.*

And frightening.

It was an emotion every living creature felt.

But feeling fear and being seized by fear were fundamentally different things.

They knew that even now, they had to endure the fear pressing down on their entire bodies and advance. Only then could they win.

—Much blood will flow, human.

“Fuck. If I survive this, I won’t even take a piss toward Nanman again.”

Jin Taekyung muttered the words through clenched teeth and gripped White Flame’s spear shaft tightly.

Then he spoke quietly to Yohi, who was frozen behind him.

“You know what to do, right?”

“……!”

“Get the people out of here right now. With everything you’ve got. As far away as possible.”

Even beyond the people currently within sight, countless tribespeople lived in the Outer Palace.

Jin Taekyung wanted to avoid drawing their figures into the horrific hellscape that would soon unfold here.

Only the powerful needed to bleed. The tribespeople, who had neither weapons nor sharp teeth, had to survive.

Even if the Southern Heaven Demon Empress killed everyone here.

*But… I’ll stop her. We’ll stop her.*

The demonic qi flowing from the rift was currently blocked by the power of the sacred stone.

He did not know how long this tense standoff would last, but before the situation grew any worse, they had to defeat the Southern Heaven Demon Empress and close the rift.

*No matter what it takes.*

Whoosh.

Jin Taekyung took a deep breath and glared at the existence standing high in the distant sky above the ruins of the collapsed pavilions.

The Southern Heaven Demon Empress.

The beginning and end of everything that had happened in this land.

Someone had to fall before they could see the conclusion of this cruel story.

“Let’s go.”

The low voice had just slipped between his lips when—

—Kraaaaaaang!

A fierce roar tore through the wind.

The radiance that had gradually faded after colliding with the darkness swelled, awakening the minds of the terrified beasts and humans.

Fwoosh! Kwoooooosh!

Light burst forth alongside the roar.

And flames rose around the silver spearhead.

An outsider who had come to this land after several hundred years surged upward as one with the enormous White Tiger.

Bang!

He kicked off the ground.

Pop!

He stepped on the invisible air and wind.

Whoooooosh!

Toward the darkness spread across the distant sky.

No.

Toward the existence that had grown even more powerful by receiving the darkness.

“Southern Heaven Demon Empress!”

The flame-wreathed azure dragon’s roar flew in with the spearhead, cleaving through space.

A chilling look crossed the woman’s face, now twisted like a Fiend’s, with not a trace of beauty left.

“The Lord of Heaven desires it.”

At that moment—

Flash!

The muddled mixture of light and darkness dyed the Nanman Beast Palace.

* * *

Groooooooan.

A tremendous wave of qi swept in every direction amid a deafening roar that seemed to split the sky.

Baeksang instinctively closed his eyes against the blinding flash that erupted in an instant. Feeling the gale pushing against his entire body, he swallowed a low groan.

*Hngh.*

What kind of overwhelming power was this?

Even he, a Supreme Peak master, could barely keep his balance against the aftershock.

When he finally opened his eyes, the area around him had already been reduced to ruins. The tribespeople who had barely survived thanks to the protection of the beasts were fleeing while screaming.

“Kyaaaaaa!”

“Hoya! Hoya! Where are you?”

“M-Mother!”

The pavilions and houses built over many long years collapsed one after another.

A grown son wailed as he saw his old mother pinned beneath a fallen stone wall.

Screams and death.

Blood and corpses.

The streets that had been filled with laughter and music only a few days ago could no longer be found anywhere.

Only endless roars and screams spilled out from every direction.

Bang! Kwoooooang!

In the space of an instant, light and darkness shot ceaselessly toward each other and tangled together.

Baeksang stared blankly at the hellscape spread beneath the muddled flashes and the deafening roars that seemed to split the sky.

Then, all at once, he stretched out a hand toward one direction.

Boom!

The palm force he released across space knocked away a massive boulder.

A half-gray-haired middle-aged man who had been struggling to save an old woman trapped beneath the stone wall widened his eyes.

“You… You’re…….”

Perhaps they had met somewhere before. The face seemed strangely familiar.

Baeksang silently watched as the middle-aged man supported the old woman, anger and gratitude mingling on the man’s face.

Then, the moment he saw the old woman’s revealed face, he understood.

*He resembles her. Very much.*

It was her.

The old palace attendant he had personally ordered expelled from the Inner Palace before everything had begun.

One of the few people who still knew what he had once been was now bleeding and groaning.

“Cough. Mmm…….”

“M-Mother!”

*Did she have a child?*

Baeksang watched the middle-aged man hurriedly check the old woman’s condition, then suddenly began to walk.

He did not know why.

He had simply felt that he had to.

“D-Don’t come any closer!”

A cry filled with hostility.

Even if they shut the doors and locked them, their ears were still open.

By now, everyone in the Nanman Beast Palace knew.

Their Palace Lord—the Great Chieftain of the Bai people—had betrayed them all.

They knew that Baeksang was the cause of the screams and deaths that continued even at this very moment.

The middle-aged man before him was one of them.

To protect his old mother, he had stepped in front of Baeksang. In his hand was a sharp fragment of stone he had picked up at some point.

“If you take even one more step…….”

Swish! Crack!

The stone fragment pierced by Finger Qi crumbled apart.

Baeksang passed the frozen middle-aged man and reached toward the old woman.

Tap. Tap.

The blurred hand moved like lightning, touching the old woman’s acupoints.

At the same time, the wrinkles furrowed across her brow slowly smoothed out.

“Cough.”

After she spat out the stagnant blood, the old woman looked much more at ease.

The middle-aged man hurriedly checked his mother’s condition, then looked at Baeksang with an expression of incomprehension.

“W-Why?”

Why?

Even that simple question was something Baeksang could not answer.

Perhaps he would still be unable to answer it even ten years or a hundred years from now.

He did not know the answer himself.

In the end, the single sentence that broke his brief silence was not an answer to the question.

“Leave with the others. Go as far away as possible.”

“S-Sir!”

“Do you intend to let your mother die like this? Or…….”

Baeksang’s eyes sank deeply.

“Do you intend to make your mother watch you die?”

“……!”

“Go. If you head for the East Gate, a way out will open.”

With those words, Baeksang turned away.

The middle-aged man’s hoarse voice escaped belatedly and pierced his ears.

“Do you think this will… Do you think this will make the sins you committed forgivable!”

At the angry shout, Baeksang answered inwardly.

No.

He had never once thought he would be forgiven.

Rumble, rumble!

A deafening roar descended behind him as he headed toward the Inner Palace.

But his figure streaked away without even a trace of hesitation.

It was time to face the moment he had pictured for decades.
```
