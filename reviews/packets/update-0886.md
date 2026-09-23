<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0886.txt",
      "sha256": "7be57693f234f06d967e4af352d802b127082b2513208417e124f9a86b67acc0",
      "bytes": 12846
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "e2cf5ba5693a51cdf70d346d0784692aeb77fac9c4b8c03162f891a9f7f32525",
      "bytes": 3022
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "77f7f9625d663fdeec408b3696199ba3f21d98f335ae9eae4e9465caec345d0f",
      "bytes": 230213
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "8804712b408a422e1ea811acb027105005d5d90c232ece812e3f450861e3c6e9",
      "bytes": 1325
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "0e05c9f125c1df5dfc7132280418a5855982cd8591ecfe9a6e3de6bcc2704351",
      "bytes": 759
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "ed1703a86c1d89eaa02fb30b5499c95a211a225c9fc58333d239578b1590b437",
      "bytes": 667
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "94f1c5e940b2901a6c2ce5c71ca17b63215f00cc479e7ab32bf0681e4f36c5e9",
      "bytes": 1511
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "e29a0ad39a0409a71e36898e3c6a07efcb266f688c9e4851d35f59d5b7aa1c04",
      "bytes": 1782
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "671182cddd96c4d27e9c0536736109dfcf75dc9b777beb4bd7506c235f7427fb",
      "bytes": 622
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "9cb49a9019d211034e7eee21db67b5d14b2f980b49185a556b35dc9008becfdb",
      "bytes": 796
    },
    {
      "path": "characters/So Gyo.md",
      "sha256": "3ae2cb54e77ba04cc03a5e2a8cc811083699d27c060691ef79a6aa9b4c2e579f",
      "bytes": 567
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "09b53280f2f55380f3c06063ad7ba1703945c2a87f5ff6dbfc057024484b3303",
      "bytes": 259022
    }
  ],
  "estimated_tokens": 11701
}
-->

# Durable State Update — Chapter 886

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 886. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 886. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
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
  "chapter": 886,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 886,
    "continuity_sources": [886],
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
    "The Emperor has confined Prince Shangshan in Qianqing Palace; Taekyung returned without him, and the Emperor plans a banquet attended by Shangshan and officials.",
    "Ma Sanbao leads a covert faction seeking to enthrone Shangshan; its members signed a pact and expect the banquet to become a confrontation.",
    "Ma Sanbao’s faction includes assassins disguised as laborers working inside the palace; their mission is unclear, and Ma told Taekyung to return and wait.",
    "Ma Sanbao says the person his allies asked about is safe and expects a young martial artist to help; he believes that martial artist’s master could be decisive.",
    "Ma Sanbao spread rumors using Taekyung’s information; the Emperor ordered the arrested rumor-spreaders released.",
    "Taekyung suspects the Emperor is connected to Dark Heaven, but this is unconfirmed.",
    "The late Emperor died after a period of mental confusion while confined; Taekyung suspects Blood Soul Gu may have been involved, but this is unconfirmed.",
    "The City Lord of Sichuan Province showed strange symptoms before his death, and Blood Soul Gu was found in his corpse.",
    "Jeok Cheongang received and burned two letters, then said the group was formally invited to the imperial palace; their contents remain unknown.",
    "Taekyung’s group has an official invitation to perform as the Blazing Flame Troupe at the imperial banquet and entered the Outer Palace disguised as a circus troupe.",
    "The Divine Physician gave Taekyung’s group Energy-Dispersing Poison to conceal their martial skill during screening; Jeok Cheongang can conceal his aura without it.",
    "A courtesan seeking revenge against the Emperor died by her own hand during Jeong Hogun’s screening; her companions were taken to prison."
  ],
  "continuity_sources": [
    884,
    885
  ],
  "open_questions": [
    "Is Aehyang pregnant, and what does the Emperor intend for her and Shangshan?",
    "Will the banquet become a confrontation, and what does the Emperor intend?",
    "Did the Emperor or Dark Heaven use Blood Soul Gu against the late Emperor and the City Lord of Sichuan Province?",
    "Who is the person Ma Sanbao’s allies asked about, and what preparations has the faction made?",
    "Who is the familiar young man who approached Jeong Hogun, and what will happen when Hogun questions Taishan?"
  ],
  "safe_through": 885,
  "temporary_decisions": [
    "Render 기관진식 as “mechanisms and formations”; retain “Third Shadow,” “First Shadow,” “No Shadow,” and “Marquis Within the Passes.”",
    "Use “imugi,” not “dragon,” for the creature Taekyung killed at Dongting Lake.",
    "Render 연판장 as “a pact bearing their signatures”; retain “Hongmen Banquet” for 홍문연.",
    "Treat 거산 as Taishan’s uncertain name variant, not a confirmed separate person; render 열화단 as “Blazing Flame Troupe” and 마희단 as “circus troupe.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 삼류     | **Third Rate**    |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 신법     | **movement technique**                           |                                                       |
| 영약     | **elixir**                                       |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 기루     | **pleasure house**                               |                                                       |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 시스템              | **System**                     |
| 스킬               | **Skill**                      |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 화산     | **Huashan**            |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 소교 | **So Gyo** | The palace attendant leading the group assigned to serve Prince Shangshan. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 선황 | **the late Emperor** | The former Emperor whom Hong Jin served. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 박도 | **broad-bladed saber** | Rough weapon swung by the bald swordsman. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 화산신룡 | **Huashan Divine Dragon** | Title given to Cheongpung after the Star-Array Grand Banquet. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 황족 | **Huang tribe** | Nanman tribe involved in a recently settled dispute. |
| 외궁 | **Outer Palace** | The outer compound of the Nanman Beast Palace. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 건청궁 | **Qianqing Palace** | The Emperor's palace, where Baek Yeon meets him. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 관리 | 진태경 | official_to_young_martial_artist | Young Master | formal-polite | The official addresses Taekyung as 공자 while explaining the consequences of Prince Shangshan's displeasure. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 관리 | 적천강 | government official to legendary martial master | you | formal, then alarmed and deferential | The official questions Jeok Cheongang, insults him as an old man, and later learns that he is the Fire King. |
| 적천강 | 관리 | legendary martial master to government official | you | blunt and mocking | Jeok Cheongang repeatedly echoes the official's formal phrasing while challenging his authority. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 소교 | 진태경 | palace attendant addressing a martial artist and guest under escort | Young Master Jin | formal and respectful, but firm | Addresses him as 진 공자 while escorting him and warning him not to investigate. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 859
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak martial master known as the Huashan Divine Dragon, the creator of the snake-inspired Mimi Step footwork technique, and the master of the Azure Dragon Pavilion within the Alliance Leader's Two Dragons Pavilion.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi, now a large horned snake, to him, and Cheongpung is accompanying Mungyeong while learning his martial arts through observation to become stronger and adapt to this world.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 885
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 883
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 884
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts his publicly acknowledged Disciple and intended heir Jin Taekyung, warmly regards Ju Hwaran and hopes she and Jin grow closer, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 879
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; they trust each other deeply, though their bond remains unformalized. Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master; Ju Hwaran is a trusted Fire Dragon Pavilion member; Magic Johnson and Chuck Hagel are allied to him; his mother and sister Hayeon are among those he protects; the Skeleton King is his friend and ally; Xiao Shen regards him as an older brother; Jin-ho is his older friend and trusted confidant; he once saved Ju Wongong’s life.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 879
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 885
- **Aliases:** None
- **Role:** Ma Sanbao is the East Depot’s Brush-Holding Eunuch and second-in-command, a Supreme Peak martial artist who has secretly remained in the imperial palace.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks in measured, courteous language, using calm reassurances and strategic metaphors to maintain unity while keeping sensitive details guarded.
- **Relationships:** Ma Sanbao is a longtime friend and former East Depot cohort of Hong Jin; he stayed behind to await Prince Shangshan's return and is leading a group seeking to enthrone him.

### So Gyo.md

# So Gyo (소교)

- **Safe through:** Chapter 875
- **Aliases:** None
- **Role:** A palace attendant loyal to the Emperor who leads the attendants assigned to Prince Shangshan.
- **Personality:** Loyal and vigilant, she remains controlled while firmly enforcing the Emperor’s orders.
- **Voice:** Measured and formal, using deferential official phrasing that can turn into pointed warnings.
- **Relationships:** She serves the Emperor and leads the palace attendants assigned to Prince Shangshan.

## Korean source

```text
＃886화



“멈춰요.”

생각지도 못했던 그 낭랑한 목소리를 듣는 순간, 머리보다 앞서 솟구친 본능이 전신을 지배했다.

팟.

흐릿해지는 신형. 삼 장의 거리를 순식간에 지우며 쇄도한 나는 본능이 시키는 대로 손을 뻗었다.

목소리의 주인을 향해.

저 새하얀 목을 향해.

후웅.

속도를 이겨 내지 못한 바람이 뒤늦게 도착한다. 묵직한 파공성과 함께 섬단 같은 머리카락이 흩날렸다.

마지막 순간, 본능을 밀어내고 허공에서 손을 멈춰 세운 나는 낯익은 상대의 얼굴을 응시했다.

그리고 물었다.

“뭡니까?”

“그건 제가 드리고 싶은 말씀입니다만.”

담담하게 대꾸한 여인, 소교(小嬌)가 자신의 목 앞에서 멈춘 내 손을 힐끗 바라보았다.

“이처럼 난데없는 출수(出手)라니, 보이는 것처럼 성급한 분이시군요.”

“보기보다, 를 잘못 말씀하신 것 같은데.”

“이 경우에는 옳게 말한 것 같네요. 그보다 이 흉흉한 손은 언제쯤 치우실 생각인지.”

“확신이 들면.”

“확신?”

나는 대답 대신 끌어올린 공력을 사방으로 퍼트렸다.

시스템 업데이트로 인해 스킬이 봉인되었다고 해서, 한 사람의 무인으로서 지닌 본연의 기감(氣感)이 사라진 것은 아니다.

솨아아악.

공기가 물결처럼 출렁인다. 반경 삼십여 장을 순식간에 훑은 나는 더 이상의 인기척이 없음을 깨닫고 천천히 손을 내렸다.

그제야 서서히 가라앉기 시작하는 심장박동을 느끼며.

‘만약 이게 함정이었다면…….’

빌어먹을.

너무 방심하고 있었다.

깊은 상념에 빠져 근처에 누가 있는 줄도 모를 정도였으니, 설령 함정에 걸려들었다고 해도 변명의 여지가 없다.

‘그보다…… 이 여자는 왜 여기 있는 거지?’

내가 알기로 소교는 건청궁에만 머무르는 황제의 사람.

혹시 나도 모르는 사이에 내궁(內宮) 깊숙이까지 들어온 것은 아닐까, 하는 생각이 얼핏 들었지만 이내 고개를 저었다.

말도 안 되는 소리다.

애초에 외궁과 내궁의 경계 수준은 천지 차이니까.

제아무리 운신의 폭이 넓어졌다 한들, 내궁을 지키는 금의위가 애견 유치원 다니는 골드 리트리버마냥 단체로 낮잠을 자지 않는 한은 불가능한 일이다.

아무리 깊은 생각에 잠겨 있다고는 해도 내궁의 그 많은 사람을 내가 모르고 지나치는 것 역시도.

‘그렇다면 아직 외궁이라는 건데. 황궁 안에 이런 곳이 있었나?’

나는 천천히 주위를 훑었다.

사방을 빽빽하게 메운 기화요초(琪花瑤草)와 이끼 가득한 연못. 그리고 그 중심에 산처럼 우뚝 서 있는 거대한 전각 한 채.

이 드넓은 공간에는 황량함만이 가득했고, 주위에는 소교를 제외한 그 누구도 보이지 않았다.

“여기가 어딥니까?”

솔직히 물어보면서도 답을 들을 수 있을 거라는 기대는 딱히 하지 않았는데, 다음 순간 들려온 소교의 목소리에 내 예상은 보기 좋게 빗나갔다.

“금지(禁地).”

“금지?”

“누구도 들어오려 하지 않는, 모두가 쉬쉬하는 황실의 금지죠.”

“그런 것치고는 이미 두 사람이나 들어와 있는데?”

“혹시 않는다와 못 한다의 차이를 모르시는지?”

“아.”

“이곳은 이미 오래전에 버려졌어요. 아무도 접근하려 들지도 않고, 따라서 지키는 사람도 없죠.”

“나 같은 외부인도 말입니까?”

“황궁은 철저하게 검증된 사람만이 들어올 수 있는 곳입니다. 설령 금지의 존재에 대해 모르는 외부인이라 할지라도, 최소한의 상식이 있다면 일정 장소를 벗어나진 않아요.”

“그러니까, 나더러 최소한의 상식도 없는 놈이다?”

“스스로 말해 주니 고맙네요.”

한 방 먹었군.

하지만 앞서 그녀가 했던 말 덕분에, 내가 우연히 들어선 이 장소가 어디인지 문득 짐작할 수 있을 것 같았다.

“혹시 사람들이 이곳을 찾지 않는 이유가, 십여 년 전의 사건과 관련이 있습니까?”

“……!”

“표정을 보니 제대로 짚었나 보네요.”

시종일관 담담하던 소교의 낯빛이 살짝 변했다. 의외라는 듯한 눈빛으로 나를 바라보던 그녀가 작게 고개를 끄덕였다.

“보기보다 눈치가 빠르군요.”

“이번에는 보이는 것처럼, 을 잘못 말한 것 같은데.”

“옳게 말했어요. 조금 전과 같이.”

소교의 단호하게 대답에, 나는 발끈하는 대신 눈 앞에 펼쳐진 황량한 풍경을 다시 한번 눈에 담았다.

‘그나저나, 여기가 바로 그곳이란 말이지.’

어쩐지 처음 봤을 때부터 뭔가 이상하다 했다.

인적도 없고, 관리도 심하다 싶을 만큼 안 되어 있었으니까.

하지만 이제는 어느 정도 이해가 된다.

지금 내가 발을 딛고 서 있는 이곳이 십여 년 전의 반란 직후 선황을 비롯한 직계 황족들이 유폐(幽閉)되었던 그 장소라면, 황궁의 그 누구도 감히 가까이 오려 하지 않았을 테니까.

그런데…….

“당신은 왜 여기 있는 겁니까?”

쉽게 이해가 되지 않았다.

황제가 거느린 충복 중 하나인 소교가, 왜 황제의 역린(逆鱗)이나 다름없는 이 장소를 찾은 것인지.

그리고 어찌하여 적이나 다름없는 내 질문에 순순히 답해 주었던 것인지.

“설마?”

“당신을 쫓아온 건 아니에요. 조만간 다시 만날 거라고는 생각했지만, 하필 이곳에서 맞닥트릴 줄도 몰랐고.”

“그럼 뭡니까?”

“내가 왜 그걸 말해 줘야 하죠?”

“그건…….”

말문이 막힌 내가 입맛만 다시던 그때, 차분한 눈으로 나를 응시하던 소교가 불쑥 입을 열었다.

“한 가지만 사실대로 대답해 준다면, 그 이유를 알려 줄 수도 있어요.”

“네?”

“약속드리죠.”

이 여자, 도대체 뭐지?

나는 잠시 고민했지만, 망설임은 그리 길지 않았다.

꼭 알고 싶은 것이 하나 있었으니까.

“그 대가로, 내가 다른 것을 질문하더라도 상관없습니까?”

“물론.”

도무지 저 담담한 표정 뒤에 숨어있는 속뜻을 알 수가 없다. 미간을 좁힌 채 소교를 응시하던 나는 작게 한숨을 내쉬며 말했다.

“일단 들어나 봅시다. 뭡니까? 당신이 알고 싶다는 게.”

“간단해요.”

그리고 다음 순간 이어진 소교의 한 마디에, 나는 조금 전보다 더욱 큰 혼란에 휩싸였다.

“무공을 익힌 지 얼마나 됐죠?”

“뭐……라고요?”

“했던 말 그대로예요. 무공을 언제부터 익혔는지에 대해 물었어요.”

문득 할 말을 잃은 나는 눈을 깜빡였다.

그만큼 소교가 던진 질문은 예상했던 범위를 아득하게 벗어나는 것이었으니까.

최소한 ‘마삼보랑 어디까지 붙어먹었냐’와 같은 말이 나올 것을 대비해 표정 관리를 하고 있던 나는 맥이 탁 풀림과 동시에 의문을 느꼈다.

“아니, 갑자기 그건 왜…….”

“조금 전 나눴던 대화를 벌써 잊었나요? 그저 사실대로 대답해 주기만 하면 해결될 문제예요.”

맞는 말이다.

나는 사실대로 답하기만 하면 된다. 도대체 무슨 이유로 소교가 이런 질문을 던졌는지는 몰라도, 내 대답이 나를 비롯한 아군 모두에게 해가 될 만한 이유는 하나도 없으니까.

문제는…….

‘그걸 누가 믿냐는 거지.’

지금껏 무림과 현대를 바쁘게 오가며 시간을 보냈다고는 해도, 두 세상의 시간을 모두 합쳐 봐야 고작 이 년 남짓.

그런데 고작 이 년 만에 지금의 경지에 다다랐다는 것을 누가 믿겠나.

진실을 아는 극소수의 몇몇 인물들조차 그 사실을 완전히 믿기보다는 그저 묵인했을 뿐이었다.

어떤 사정이 있겠구나, 하고.

심지어는 가장 오랫동안 나를 곁에서 지켜봐 온 적천강 역시도.

‘시스템과 현대에 대해 알게 된 후에야 완전히 납득했었지.’

향락에 찌든 삼류 양아치가 불과 이 년 만에 중원을 떨어 울리는 초절정 고수가 되었다는 것은, 그만큼 받아들일 수 없는 불가해(不可解)의 영역이다.

진실과는 한참 벗어난 소문이 정설(定說)로 자리잡은 것 역시 그런 이유에서였다.

- 진태경이 태원진가가 가문의 사활을 걸고 키워 낸 비밀병기라더라.

- 항산검문과 대장로의 눈에 띄지 않게 일찌감치 한량으로 위장시켰다더라.

- 그렇게 기루에 바치는 척하며 빼돌린 재물로 뭔 놈의 영약을 그리 사 먹였는지, 진태경은 다리가 세 개라더라.

마지막이 좀 이상하긴 한데 어쨌든.

이와 같은 소위 ‘카더라’ 식의 소문들이 괜히 생겨난 것이 아니다.

이 년 만에 초절정 고수가 된다는 건 하늘이 두 쪽 나도 일어날 수 없는 일이니 헛소문은 금세 정설로 굳혀졌고, 그것이 내게도 유리했다.

곧이곧대로 진실을 밝혔다간 빼도 박도 못하는 사마외도(邪魔外道), 그중에서도 엄청난 마공을 익힌 무림공적으로 낙인찍혀도 이상하지 않을 테니까.

‘그러니 사실대로 말해 봤자, 소교 입장에서는 믿지도 않을 게 뻔하지.’

내가 파악한 바에 의하면 소교 역시 엄연한 일류의 무인.

가끔은 ‘완전한 진실’보다 ‘진실처럼 보이는 것’이 중요할 때가 있는 법이다.

바로 지금처럼.

“십오 년.”

불쑥 입을 연 나는, 안색 하나 변하지 않은 얼굴로 소교를 바라보며 말을 이었다.

“향간에 떠도는 이야기로는 내가 한 살에 솔방울로 호랑이를 잡고 두 살 때 축지법을 익혔다는데…… 그건 뭐 모자란 인간들이나 믿는 개소리고. 머릿속에 남아 있는 기억으로만 따지면 십오 년쯤 됩니다.”

말없이 이야기를 듣고 있던 소교가 작게 뇌까렸다.

“십오 년이라.”

“알고 있는지 모르겠지만 내 바로 위에 몇 살 차이 안 나는 형님이 하나 있는데, 이리저리 처맞으면서 열심히 했죠. 물론 재능도 있었고.”

“화산신룡 청풍처럼?”

“맞아요. 청풍처…… 잠깐. 그 사람 알아요? 별호까지?”

“당신이 생각하는 것보다 훨씬 잘 알고 있죠. 무림에 대한 소식은 계속해서 듣고 있었으니까.”

“아니, 그러니까 굳이 왜?”

“찾아야 할 사람이 있거든요. 반드시 찾아내야 할 사람이.”

담담하게 대꾸한 소교가 돌아섰다.

아니, 정확히는 돌아서려 하던 그 순간. 내가 섬전과도 같은 속도로 팔을 뻗었다.

“대답했으니 약속을 지켜야…….”

그리고.

쉭, 사락.

한 줄기 바람이 불었다.

“어?”

나는 석상처럼 굳은 채. 아슬아슬하게 손끝을 스쳐 지나가는 옷자락을 멍하니 바라보았다.

‘뭐지?’

물론 전력을 다한 것은 아니었지만, 그래도 일류 고수를 상대하기에는 차고 넘치는 속도였다.

하지만 소교는 미끄러지는 듯한 신법으로 내 손을 피했다. 마치 이것이 당연하다는 듯.

‘내 단순한 착각? 아니면…….’

머릿속에서 이어진 어떤 생각에, 몸 안의 피가 차갑게 식는 듯했다. 나는 깊숙하게 가라앉은 눈빛으로 소교를 노려보았다.

“이런 재주가 있을 줄은 몰랐는데.”

소교가 차분하게 대꾸했다.

“재주가 많은 편이죠. 보이는 것처럼.”

“신법도 일류 수준은 절대 아닌 것 같고…… 거짓말로 사람 약 올리고 튀는 것도 잘하나?”

“거짓말이라, 당신이 할 말은 아닌 것 같은데.”

“뭐?”

“십오 년 전부터 무공을 익혔다는 말. 전부 거짓이잖아요.”

“……!”

“황실의 정보력을 우습게 보지 말아요. 내가 이곳에 머무르는 이유 역시 그 때문이니까.”

등골이 서늘해졌다.

지금 이 순간 나를 바라보는 저 고요한 눈동자가, 마치 화살처럼 마음을 꿰뚫는 것 같아서.

그리고 소교라는 이름의 저 여인이, 단순한 황제의 충복이 아닐 것이라는 직감 때문에.

“당신…… 도대체 뭐야?”

스아아아.

삼 갑자의 열양지기가, 주위의 공기를 뜨겁게 달구었다.
```

## Final English reading copy

```markdown
# Chapter 886

“Stop.”

The moment I heard that clear, bright voice—the last thing I’d expected—instinct surged ahead of thought and took over my whole body.

Whoosh.

My figure blurred. I closed the distance of three zhang in an instant, thrusting out my hand as instinct commanded.

Toward the owner of that voice.

Toward that snow-white neck.

Whoom.

The wind, unable to keep up with my speed, arrived a beat late. With a heavy whoosh, her hair fluttered.

At the last moment, I pushed back against instinct and stopped my hand in midair. Then I stared at the familiar face before me.

And asked,

“What is it?”

“That’s what I’d like to ask you.”

The woman who answered calmly—So Gyo—glanced at my hand, halted just in front of her throat.

“To strike so suddenly, without warning. You’re as rash as you look.”

“I think you meant ‘more rash than I look.’”

“In this case, I think I said it right. More importantly, when are you planning to move that threatening hand?”

“When I’m sure.”

“Sure?”

Instead of answering, I sent the internal energy I’d drawn up spreading in every direction.

The System update had sealed my Skills, but that didn’t mean I’d lost the Qi Sense that was part of me as a martial artist.

Whoooosh.

The air rippled like water. I swept the area within a radius of thirty or so zhang in an instant and, finding no other presence, slowly lowered my hand.

Only then did I feel my heartbeat begin to settle.

*If this had been a trap…*

Shit.

I’d let my guard down too much.

I’d been so lost in thought that I hadn’t even realized someone was nearby. Even if I’d walked right into a trap, I’d have had no excuse.

*More importantly… why is she here?*

As far as I knew, So Gyo was one of the Emperor’s people and stayed in Qianqing Palace.

For a moment, I wondered if I’d somehow wandered deep into the Inner Palace without realizing it. But I quickly shook my head.

That made no sense.

The boundary between the Outer Palace and Inner Palace was like the difference between heaven and earth.

No matter how much wider my freedom of movement had become, there was no way I could get into the Inner Palace unless the Embroidered Uniform Guard protecting it had all taken a group nap like a pack of golden retrievers at doggy daycare.

And no matter how deep in thought I was, I couldn’t have passed by that many people in the Inner Palace without noticing them.

*Then I’m still in the Outer Palace. Was there a place like this inside the imperial palace?*

I slowly looked around.

Strange flowers and rare plants crowded the grounds in every direction. A moss-covered pond lay nearby, and at the center stood a huge pavilion, rising like a mountain.

The vast space was desolate. There wasn’t another soul in sight besides So Gyo.

“Where are we?”

To be honest, I hadn’t expected an answer when I asked. But So Gyo’s next words proved me very wrong.

“A forbidden ground.”

“A forbidden ground?”

“A place in the imperial household that no one wants to enter, and everyone avoids talking about.”

“But two people have already entered.”

“Do you perhaps not know the difference between ‘won’t’ and ‘can’t’?”

“Oh.”

“This place was abandoned a long time ago. No one tries to come near it, so no one guards it.”

“Even outsiders like me?”

“Only people who have been thoroughly vetted can enter the imperial palace. Even an outsider who doesn’t know this place is forbidden wouldn’t go beyond a certain point if they had the slightest bit of common sense.”

“So you’re saying I’m an idiot with no common sense?”

“Thanks for saying it yourself.”

She got me there.

But thanks to what she’d said earlier, I thought I could guess where I’d wandered by chance.

“Is the reason people don’t come here connected to what happened more than ten years ago?”

“……!”

“Your expression tells me I got it right.”

So Gyo’s face, calm until now, changed ever so slightly. She looked at me in surprise, then gave a small nod.

“You’re more perceptive than you look.”

“This time, I think you meant ‘as perceptive as I look.’”

“I said it right. Just like a moment ago.”

At So Gyo’s firm reply, I resisted the urge to snap back and looked once more at the desolate scene before me.

*So this is the place.*

Something had seemed off from the moment I first saw it.

There was no one around, and it had been left to decay to an unreasonable degree.

But now I understood, at least somewhat.

If this was the place where the late Emperor and the direct imperial bloodline had been confined after the rebellion more than ten years ago, then no one in the imperial palace would dare come near it.

But…

“Why are you here?”

I couldn’t make sense of it.

Why had So Gyo, one of the Emperor’s trusted followers, come to a place that might as well have been the Emperor’s greatest sore spot?

And why had she answered my questions so readily, when I was practically her enemy?

“Could it be…?”

“I didn’t come after you. I thought we’d meet again soon, but I didn’t expect to run into you here of all places.”

“Then what is it?”

“Why should I tell you?”

“Well…”

I was at a loss for words and could only smack my lips. Then So Gyo, who had been watching me with composed eyes, suddenly spoke.

“If you answer one question honestly, I might tell you why I’m here.”

“What?”

“I promise.”

What the hell was this woman?

I thought it over for a moment, but I didn’t hesitate long. There was something I really wanted to know.

“In exchange, can I ask you something else?”

“Of course.”

I couldn’t make out the intent behind that calm expression of hers. I watched So Gyo with my brows drawn together, then let out a small sigh.

“Fine. Let’s hear it. What do you want to know?”

“It’s simple.”

And with So Gyo’s next words, I was even more confused than before.

“How long have you been studying martial arts?”

“What…?”

“I mean exactly what I said. I asked when you started learning martial arts.”

I blinked, momentarily at a loss for words.

So Gyo’s question had gone far beyond anything I’d expected.

I’d been keeping my expression in check, expecting a question like, *How deep are you in with Ma Sanbao?* Instead, all the tension drained out of me—and I was left wondering.

“No, why would you suddenly ask that…?”

“Have you already forgotten our conversation a moment ago? You only need to answer honestly.”

She was right.

All I had to do was answer honestly. Whatever her reason for asking, there was no reason my answer would harm me or my allies.

The problem was…

*Who’d believe it?*

I’d spent all this time going back and forth between Murim and the modern world, but add the time in both together and it came to barely two years.

Who’d believe I’d reached my current realm in just two years?

Even the handful of people who knew the truth hadn’t fully believed it. They’d simply let it pass, thinking there must be some circumstances behind it.

Even Jeok Cheongang, who’d watched me from closer than anyone else for the longest time.

*He didn’t fully accept it until he learned about the System and the modern world.*

The idea that a Third Rate punk steeped in pleasure had become a Supreme Peak master who shook the Central Plains in only two years was simply beyond the bounds of what anyone could accept.

That was why rumors so far from the truth had become accepted as fact.

—Jin Taekyung is a secret weapon the Jin Family of Taiyuan raised at the cost of the family’s survival.

—They had him pretend to be a layabout early on, so he wouldn’t catch the eye of the Mount Heng Sword Sect or the Head Elder.

—They funneled money to him under the pretense of paying a pleasure house. God knows how many elixirs they bought him with it. Jin Taekyung has three legs, they say.

That last one was a little strange, but anyway.

Rumors like those didn’t come out of nowhere.

Becoming a Supreme Peak master in two years was impossible even if the heavens split in two. So the lies had quickly become accepted as fact—and that worked in my favor.

If I told the truth outright, I could be branded an irredeemable practitioner of demonic, heterodox arts—or worse, an enemy of all Murim who’d mastered terrifying demonic martial arts.

*So even if I tell the truth, there’s no way So Gyo will believe me.*

As far as I could tell, So Gyo was also a First Rate martial artist.

Sometimes, what matters more than the complete truth is what looks like the truth.

Like right now.

“Fifteen years.”

I spoke up and looked at So Gyo without changing my expression.

“The story going around is that I caught a tiger with a pinecone when I was one, and learned the art of shrinking space when I was two… but that’s a load of bullshit only idiots believe. Going by the memories I still have, it’s been about fifteen years.”

So Gyo had been listening without a word. She murmured,

“Fifteen years.”

“You might not know this, but I have an older hyung just a few years above me. I worked hard, taking beatings from him left and right. And I had talent, too.”

“Like Cheongpung, the Huashan Divine Dragon?”

“Right. Cheongpung—wait. You know him? Even his title?”

“I know far more than you think. I’ve continued to hear news from Murim.”

“No, I mean, why would you need to?”

“There’s someone I need to find. Someone I absolutely must find.”

So Gyo answered calmly and turned away.

Or, more precisely, she was about to turn away when I thrust out my arm as fast as lightning.

“I answered, so you have to keep your promise…”

And then—

Swish. Rustle.

A breeze blew past.

“Huh?”

I stood frozen like a statue, staring dumbly at the hem of her robe as it brushed past my fingertips.

*What was that?*

I hadn’t used my full strength, of course, but it had still been more than fast enough to catch a First Rate martial artist.

Yet So Gyo had slipped past my hand with a movement technique so smooth she seemed to glide. As though it were only natural.

*Was that just my imagination? Or…*

A thought took shape in my mind, and the blood in my body seemed to turn cold. I glared at So Gyo, my eyes sinking deep.

“I didn’t know you had a trick like that.”

So Gyo replied calmly,

“I have quite a few tricks. Just as you can see.”

“Your movement technique is definitely beyond First Rate… Are you good at lying, getting under people’s skin, and running off, too?”

“Lying? I don’t think you’re in a position to say that.”

“What?”

“That claim that you’ve been practicing martial arts for fifteen years. It’s all a lie.”

“……!”

“Don’t underestimate the imperial family’s intelligence network. That’s why I’m staying here, too.”

A chill ran down my spine.

Her calm eyes, fixed on me right now, seemed to pierce my heart like arrows.

And I had a feeling the woman named So Gyo wasn’t merely one of the Emperor’s trusted followers.

“You… what are you, exactly?”

Ssshhh.

Three jiazi of Scorching Yang Qi heated the air around me.
```
