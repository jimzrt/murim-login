<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0841.txt",
      "sha256": "3278fd6b7ce3fa6145a8dc610f5c477767e86ff09528f7e19213016decfdb769",
      "bytes": 12853
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "3f36c43d03b85ee84486f3f70081598d7653b93bbccc83922a714080ca2c2f6d",
      "bytes": 2734
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2ac235886e36b4a9cfac67990c4e303d5cbbbaacdc20104970ce04b7ba9ca08c",
      "bytes": 227427
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "d74f285b4294bb39fb6925e6c905ef98f2545ed8dbc55ff5a94c1a2e91a082f4",
      "bytes": 1355
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "8f9c5ff517e9669cc46e828b8e5a367fdaa6e5118b1a1b71e2e951522a349e0c",
      "bytes": 1848
    },
    {
      "path": "characters/Peng Cheolhu.md",
      "sha256": "a63960b2788360ea7852b2f86c93b2f26cb7782c8cff233af8726d6b567ae7d0",
      "bytes": 680
    },
    {
      "path": "characters/Tang Sadok.md",
      "sha256": "c94ca8cc4a6d2487b05238d30661072be18a1c5d83e7707cfa5b4b24b4b09926",
      "bytes": 925
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "4bcdb5e001be95ac270b11327a08919d028c5452998a7cf7f9880ea65e073923",
      "bytes": 888
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "2d3ba6654cdbcc372510ec72e3979b0d7dd3413b49d0a44c281c59171f618c6d",
      "bytes": 251874
    }
  ],
  "estimated_tokens": 10644
}
-->

# Durable State Update — Chapter 841

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
1 and safe_through 841. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 841. Profile updates may replace only one
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
  "chapter": 841,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 841,
    "continuity_sources": [841],
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
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader.",
    "Jin erased the Doppelganger, but Main Quest [Cataclysm] and its “Stop the Summoning” mission failed.",
    "The supernatural Rift began at 10%; its progress increases the distribution and concentration of magical power.",
    "The System’s Status Window is inaccessible; Jin suspects an update may be responsible.",
    "Jin saw a vision of a black-haired man killing Ahomed after the ritual. Whether it was real is unknown; Jin believes the man was not Asmodeus.",
    "Jin’s [Broken Body] injury around his lower dantian remains unresolved; leveling up did not heal it.",
    "Jin is awake and at the Sichuan Tang Clan after being unconscious for three days.",
    "Jeok Cheongang is at the Sichuan Tang Clan and is pressing a physician to treat Jin; the physician is staying to care for patients who still need treatment.",
    "Ju Wongong remains temporarily appointed acting City Lord of Sichuan Province by imperial order while under exile.",
    "The Sichuan Tang Clan and Sichuan Murim are rebuilding after Dark Heaven’s attack; allied martial artists remain to help and guard against another attack.",
    "Tang Sadok is the Sichuan Tang Clan’s Family Head and welcomes Jin as its Benefactor.",
    "Jeok Cheongang and Jin have reunited; Jin overheard Jeok’s argument with the physician."
  ],
  "continuity_sources": [
    839,
    840
  ],
  "open_questions": [
    "Why did the Main Quest fail despite the Doppelganger’s erasure, and who or what was summoned?",
    "Was Jin’s vision of the summoned being real, System-delivered, or prophetic?",
    "What will happen as the Rift progresses and more beings enter the world?",
    "Who or what chose Jin, and what is the Ark?",
    "What changed in the System update, and when will its functions return?"
  ],
  "safe_through": 840,
  "temporary_decisions": [
    "Keep magical power distinct from mana; keep Blink distinct from Teleport and Warp. Extended-range Blink causes severe strain.",
    "Keep Fire Storm and Aqua Storm as distinct named spells.",
    "Render [영웅의 검] as “Hero’s Sword,” 에어 슬래시 as “Air Slash,” and 실드 마법 as “Shield magic.”",
    "Render 선택받은 자 as “the Chosen One,” 방주의 주인 as “the Master of the Ark,” [격변] as [Cataclysm], [어데 도씹니꺼] as “Where’s Your Do Clan From?,” and [종족 학살자] as “Species Slayer.”",
    "In chapter 839, render 균열 as a social fracture or division, not the supernatural Rift; render 醜王 as “Disgrace King” when used as Jin’s mocking imagined epithet for Jeok Cheongang."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 벽력도왕   | **Thunderbolt Saber King**    | Peng Cheolhu   |
| 독왕     | **Poison King**               | Tang Taesang   |
| 십왕     | **Ten Kings**       |
| 열화문    | **Fire Gate Clan**               |
| 사천당가   | **Sichuan Tang Clan**            |
| 살기     | **killing intent**                               |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 가주     | **Family Head**                              |
| 문주     | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 사제     | **Junior Brother**                           |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 사천     | **Sichuan**            |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 본문      | **our sect / this sect**                                        |
| 당사독 | **Tang Sadok** | Current Family Head of the Sichuan Tang Clan; also called the Myriad-Poison Asura. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 환골탈태 | **Bone Transformation** | Advanced transformation described as optional in martial-arts novels. |
| 태상가주 | **Grand Family Head** | Title held by the Azure Sky Sword King as head of the Nangong Family. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 태양권 | **Solar Fist** | Martial art mentioned in Taekyung's joke about Unnamed's forehead strike. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 당가 | **Tang Family** | Short form for the Sichuan Tang Clan when distinguished from 사천당문. |
| 만독수라 | **Myriad-Poison Asura** | Epithet of Tang Sadok. |
| 만독지환 | **Myriad-Poison Ring** | Quest title concerning a legendary treasure said to detoxify any poison. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 독의 | **Poison Physician** | Taekyung's mocking description of Mungyeong after learning how aggressively he uses poison. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 서천 | **Western Heaven** | Short form used by the Lord of Heaven for the Western Heaven Demon Lord. |
| 선계 | **realm of immortals** | The other world that Jin travels to and from. |
| 소신선 | **Little Immortal** | Jeok Cheongang's private speculation about Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 적천강 | 벽력도왕 | rival_martial_master_to_rival_martial_master | Virility Saber King | insulting and taunting | Jeok coins 정력도왕 as a taunting replacement for the established title. |
| 벽력도왕 | 적천강 | rival_martial_master_to_rival_martial_master | Jeok Cheongang | boisterous and hostile-teasing | The Thunderbolt Saber King calls Jeok by name before their argument escalates. |
| 서천마군 | 당사독 | hostile_opponents | you | calm and taunting | The Western Heaven Demon Lord uses 자네 while answering Tang Sadok's question. |
| 당사독 | 서천마군 | hostile_opponents | you bastard | hostile and threatening | Tang Sadok uses 네놈 after recognizing the disguised infiltrator. |
| 서천마군 | 적천강 | hostile_invader_to_unconscious_patient | you | calm and predatory | Says someone wants to see Jeok Cheongang and attempts to move him with Seizing an Object Through Empty Space. |
| 적천강 | 서천마군 | hostile_opponents | you bastard | blunt and threatening | Jeok addresses the Western Heaven Demon Lord with 네놈 while defending Taekyung and ordering him not to touch his Disciple. |

## Listed compact profiles

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 840
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 840
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Peng Cheolhu.md

# Peng Cheolhu (벽력도왕)

- **Safe through:** Chapter 547
- **Aliases:** Thunderbolt Saber King
- **Role:** Peng Cheolhu is the Thunderbolt Saber King, a Ten Kings master and Great Hero of the Hebei Peng Family.
- **Personality:** Boisterous, hot-tempered, argumentative, and protective toward those connected to his close friend Hong Dao.
- **Voice:** Loud, blunt, confrontational, and prone to disguising embarrassment or retreat as serious martial instruction.
- **Relationships:** Long-standing rival and friend of Jeok Cheongang; close friend of Hong Dao; protective toward Hong Dao's Disciple Unnamed.

### Tang Sadok.md

# Tang Sadok (당사독)

- **Safe through:** Chapter 840
- **Aliases:** Myriad-Poison Asura
- **Role:** Current Family Head of the Sichuan Tang Clan, overseeing its recovery and relying on allied martial artists to help treat patients and guard against another Dark Heaven attack.
- **Personality:** Blunt and unsentimental, yet grateful to those who remain with the Tang Clan; he has consciously chosen to change and speaks candidly about the clan’s vulnerability.
- **Voice:** Hissing, curt, authoritative, and threatening.
- **Relationships:** Tang Taesang was his father and predecessor, his unnamed nephew serves as Master of the Gatekeeper Pavilion, Mimi is his cherished old friend and companion temporarily entrusted to Cheongpung, and he regards Jin Taekyung and Cheongpung as benefactors, openly welcoming Jin with a warmth he usually conceals.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 839
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃841화



당사독은 나와 적천강을 내원(內院) 깊숙이 자리한 어느 전각으로 안내해 주었다. 혹 불편하거나 필요한 부분이 있다면 뭐든 말하라는 말과 함께.

“그럼 이만…….”

“잠깐.”

적천강의 나직한 부름에, 아직 성치 않은 몸을 이끌고 황급히 전각을 빠져나가려던 당사독의 몸이 석상처럼 굳었다.

이내 서서히 고개를 돌린 그가 나오지 않는 목소리를 힘겹게 쥐어 짜냈다.

“무슨 연유로 부르셨는지…….”

심유하게 가라앉은 눈빛. 말없이 당사독을 응시하던 적천강이 불쑥 입을 열었다.

“잊어라.”

“예?”

“잊으라고 했다. 지금껏 네놈이 보고 들은 것 전부.”

만독수라(萬毒修羅)고 나발이고, 상대는 화왕 적천강이다.

꼭 잊을 만하면 한 번씩 튀어나와 무림을 뒤집어 놓는 유서 깊은 개깡패 문파, 열화문의 당대 문주.

사문부터가 삼백여 년간 대대로 천하 곳곳에 불을 싸질러 놨으면서, 본인 처소에 불 좀 붙었다고 천 명이 넘는 마교도를 깡그리 전멸시킨 내로남불의 결정체.

또르륵.

언제 맺혔는지 모를 식은땀 한 방울이 당사독의 목덜미를 타고 굴러떨어졌다. 마른침을 꿀꺽 삼킨 그가 대답했다.

“무, 물론입니다. 이 후배가 보고 들은 것을 모두 잊겠습니다.”

“잊어? 애초에 보고 들은 게 없는데 뭘 잊는단 말이냐?

“아.”

“조심하자, 어? 눈치 챙기자고.”

당사독의 목덜미를 살살 주무르면서 속삭이는 적천강의 모습이 어딘지 모르게 낯이 익다 싶더니, 나 초등학교 다닐 때 골목길에 죽치고 있던 고등학생 일진 형들이 딱 저랬다.

문제는 당시 그 일진 형들이 열일곱 살 정도였고, 현재 적천강의 나이가 최소 117세는 넘을 거란 사실이다.

‘아니, 무슨 백 년을 회춘해 버리네.’

척 봐도 한두 번 해 본 솜씨가 아니다.

낮은 어조와 게슴츠레하게 뜬 눈동자, 거기에 더해 상황에 맞는 훌륭한 어휘 선택까지.

“노부가 요새 좀 기분이 안 좋다. 그런데 이런 상황에서 어떤 종류의 이야기가 무림에 나돌아. 그러면 어떨 것 같으냐?”

“부, 불쾌하실 것 같습니다.”

“불쾌 정도가 아니지. 아주 기분 잡치는 거지. 완전히 꼭지가 돌아 버리는 거야.”

“죄, 죄송합니다. 노야.”

“죽은 네 선친, 독왕과 노부는 그럭저럭 연이 있었다. 절친하다고 말할 정도까지는 아니었지만, 적어도 등을 맡길 만한 녀석이었어.”

몇 달 전, 만독지환을 노리던 서천마군(西天魔君)에 의해 죽음을 맞이한 독왕은 사천당가의 태상가주이자 당사독의 아버지였지만, 그 이전에 적천강과 함께 십왕(十王)이라는 이름으로 정마대전을 승리로 장식한 영웅이기도 했다.

“약간 음울한 구석이 있었지만, 똑똑하고 눈치 빠른 친구였지. 어느 날 노부가 마시려던 술에 독을 탔는데, 벽력도왕(霹靂刀王) 그놈이 신나게 처맞는 걸 보더니 자연스럽게 술잔을 엎지르더군. 그 후에 어떻게 됐는지 아나?”

당사독이 잔뜩 쉰 목소리로 대답했다.

“예. 이번 한 번은 넘어가 주시겠다고 하시더니, 석 달 뒤에 갑자기 제 선친을 두들겨 패셨다고…….”

“노부가 그리 한 이유를 아느냐?”

“모, 모릅니다. 아버님께서도 몇 년 전까지 줄곧 그 이유를 궁금해하셨습니다.”

“기분이 아주 더러운 날이었는데, 주위에 때릴 놈이 없었다. 그래서 때렸어.”

“……!”

“노부가 그런 놈이다. 이제 감이 좀 잡히느냐?”

오십여 년간이나 베일에 싸여 있던 폭행 원인을 알아낸 당사독은 입을 쩍 벌렸고, 나는 본능적으로 입을 열었다.

“그건 그냥 미친놈 아니에요?”

“…….”

“…….”

“아.”

순간 숨 막히는 침묵이 내리 깔렸다. 말없이 나를 응시하던 적천강이 천천히 입술을 달싹였다.

“나가라.”

“예?”

“나가!”

“예, 옛!”

천둥 같은 고함에, 오십 년 묵은 체증이 내려간 사람처럼 시원한 표정으로 나를 바라보던 당사독이 빛살처럼 전각을 빠져나갔다.

아니, 도망쳤다.

나만 두고.

‘도마뱀인가?’

하지만 남 탓하기에는 앞서 혼자 싸질러 놓은 똥이 너무나도 크고 아름답다. 호흡을 가다듬은 내가 침착하게 입을 열었다.

“노야, 오햅니다.”

“뭐가 말이냐?”

“처음부터 끝까지 모두 다요.”

“본문의 문규(門規)에는 처음부터 끝까지 개소리를 지껄이면 두 배로 처맞는다는 조항이 있다.”

“……정말 그런 문규가 있습니까?”

“있다.”

“어느 정신 나간. 아니, 어느 분께서 그런 문규를 만드셨습니까?”

“노부가 만들었다. 조금 전에.”

좋아, 좆 됐군.

변명이 통하지 않는다면 유연하게 대처해야 할 때다. 나는 혁무진에게 빙의된 것처럼 빠르게 무릎을 꿇고 앉았다.

“죄송합니다.”

“생각보다 인정이 빠르구나.”

“아직 살날도 많은데, 여기서 맞아 죽을 수는 없잖습니까.”

“네놈과는 달리 노부는 살날이 얼마 남지 않을 것 같다.”

“왜요?”

“그래도 명색이 제자라는 놈에게 미친놈 소리를 들었으니 나가 뒈져야지. 그렇지 않느냐?”

나는 한껏 조아렸던 고개를 슬그머니 들었다. 최소 E컵은 되어 보이는 적천강의 우람한 대흉근이 보였다.

환골탈태(換骨奪胎)를 통해 과거의 젊음과 총기를 되찾은 그다.

저 정도면 어디 가서 나가 뒈지는 게 아니라, 나 빼고 다 뒈지라고 해도 무방하다.

“아닙니다. 노야는 장수하실 겁니다. 이미 장수하셨지만요.”

“그렇구나. 한데 노부가 보기에 네놈은 단명할 것 같다.”

“그런 말씀 마십시오. 섭섭합니다.”

“섭섭한 건 노부가 더 섭섭해야지. 멀쩡한 머리털까지 박박 밀고 땡중 행세해 가며 남만까지 갔는데, 감히 이런 식으로 뒤통수를 쳐?”

나는 슬그머니 고개를 들었다.

그리고 창밖으로 쏟아지는 햇빛을 받아 번쩍이는 적천강의 기습 태양권 공격에 본능적으로 눈살을 찌푸렸다.

“어이쿠. 눈 부셔.”

“…….”

“아, 죄송합니다. 그리고 노야께서 절 생각해 주시는 마음은 항상 감사히 생각하고 있습니다.”

“늦었다.”

“누가 그런 말을 했습니다. 늦었다고 생각할 때가 시작하기에 가장 좋을 때라고.”

“늦었다고 생각할 때가 진짜 늦었다. 그런 헛소리를 한 놈은 이미 옛날옛적에 뒈졌을 거고.”

“그렇다면 거듭 죄송합니다.”

“뭘 하든, 그 전에 한 가지만 물어보자.”

나를 차분하게 내려다보며, 적천강이 말을 이었다.

“노부가 보기에 네 녀석은 사람보다 소신선(小神仙)에 가깝다. 그럼 죽어도 다시 살아날 수 있느냐?”

“아니, 그런 흉악한 질문을 왜…….”

“그저 궁금해서 물어보는 것이다.”

“그러니까 왜 그런 걸 궁금해하시는데요…….”

“네 녀석은 선계(仙界)에서 왔다 했으니, 달라도 뭐가 다를 것 아니냐.”

“죽습니다. 진짜 죽어요.”

“선계에 있는 네놈도?”

“뒈져요. 저 1코인밖에 없습니다. 처음부터 이게 찐찐막이었어요.”

“또 요상한 소리를 하는구나.”

아니, 제발. 왜 저런 걸 물어보는 건데.

오금이 저린 나는 벌떡 일어나서 적천강에게 넙죽 절을 올렸다. 딱 한 번으로 끝내면 부족할 것 같아서 두 번이나 했다.

그리고 다시 무릎을 꿇자마자, 잠시 잊고 있던 사실을 깨달았다.

“지금 제사 지내냐?”

“아.”

“이 꽉 깨물어라. 깔끔하게 끝내자.”

후웅.

말이 끝나기도 전에 무지막지한 파공성이 울려 퍼졌다.

반사적으로 눈을 질끈 감은 나는 문득 혁무진을 떠올렸다. 만약 살아나가면 전보다 훨씬 잘해 줘야겠다는 다짐과 함께, 이를 악물고 호흡을 삼켰다.

‘흡……!’

그리고 그 순간.

툭.

화아아악!

이마에 닿은 미세한 감촉과 함께, 미친 듯이 휘몰아친 바람이 머리카락을 뒤흔들었다.

‘어?’

서서히 가라앉는 열풍(熱風) 속, 의문을 느끼며 눈을 뜬 나는 볼 수 있었다.

손가락으로 내 이마를 누른 채, 짜증이 가득한 표정으로 한숨을 푹푹 내쉬는 적천강의 모습을.

그러나 그와는 반대로 애정과 반가움이 묻어나오는 그의 눈빛을.

“이 천인공노할 놈 같으니. 엄살떨지 말고 냉큼 일어나지 못하겠느냐.”

“예?”

“할 거면 제대로 하란 말이다. 이를테면…… 그래, 절이라든지.”

나는 멍하니 눈을 깜빡였고, 적천강은 햇빛이 쏟아지는 창가로 슬쩍 시선을 돌리며 중얼거렸다.

“거, 날씨 한번 좋다.”

모르겠다. 왜 갑자기 그 순간 웃음이 흘러나왔는지.

아니, 사실은 이미 알고 있었다.

오늘도, 그제도. 어쩌면 아주 오래전부터.

“하하.”

“이놈이, 웃어?”

“아닙니다. 제 절이나 받으세요. 야무지게 구배지례(九拜之禮) 한번 올리겠습니다.”

구배지례라는 말에 잠시 움찔한 적천강이 콧방귀를 뀌었다.

“정식으로 사제지연을 맺은 것도 아닌데 그따위 허례허식은 무슨. 평소에나 잘해라.”

맞다. 적천강과 나는 정식으로 맺어진 사제지연이 아니다.

한때 피붙이 같던 제자를 없애기 위해 세상으로 나온 노인에게는 사문의 가르침을 이어 갈 새로운 계승자가 필요했고, 살기 위해 발버둥 치던 어느 청년에게는 더욱 강한 힘이 필요했을 뿐이다.

그들은 서로가 가진 것을 필요로 했기에 맺어졌고, 그렇기에 구배지례는 아무런 의미도 없는 허례허식에 불과했다.

그래, 분명 그랬었다.

하지만…….

‘살짝 서운하네. 막상 저런 말을 들으니까.’

어느 순간부터 당연했던 것이 서운해지고, 서운했던 것은 당연해졌다.

그리고 이처럼 변화한 감정은 오롯이 나에게만 허락된 것이 아니었다.

“나중에.”

불현듯 귓가에 닿은 한 마디.

적천강은 햇빛이 쏟아지는 창가를 바라보며 말을 이었다. 그의 눈빛은 마치 저 멀리 떨어진 무언가를 응시하는 듯했다.

“나중에 때가 온다면, 모든 것이 제자리로 돌아간다면…….”

조금씩 흐려지던 목소리가 바람에 섞여 흩어진다.

하지만 나는 똑똑히 들었다.

끝맺어지지 않은 그의 뒷말을, 귀를 통해서가 아니라 마음으로 들었다.

그리고 그것만으로 충분했다.

적어도 오늘만큼은.

“노야.”

“왜 부르느냐.”

내 부름에 적천강이 고개도 돌리지 않고 대답했다. 어쩌면 고개를 돌려 얼굴을 마주할 자신이 없었는지도 모른다.

“노야.”

“아, 왜.”

뻔히 예상되는 그 반응이 재미있어서, 나는 소리 내어 웃었다. 그리고 오랫동안 마음에 담아 두었던 한 마디를 건넸다.

“좋네요. 이렇게 다시 뵙게 되어서. 여전히 가까이에 계셔서.”

“……!”

“다녀왔습니다.”

그 순간, 덜컥 굳어 있던 적천강의 어깨가 부드럽게 풀렸다.

천천히 고개를 돌린 그가 알 수 없는 얼굴로 나를 바라봤다.

마치 이럴 때는 어떤 표정을 지어야 하는지 단 한 번도 경험해 보지 못한 사람처럼 억지로 눈살을 찡그리기도 하고, 입술을 삐뚜름하게 실룩거리기도 했다.

하지만 사람이라면 누구나 경험을 통해 배움을 얻는 법.

아무리 스스로가 부정하고, 낯설게 느껴져도 결국 진심을 감출 수 없다.

천하가 화왕(火王)이라 이름 붙인, 뜨겁고 단단한 철면을 뒤집어쓴 채 한 세기가 넘는 삶을 살아온 이도 예외는 아니었다.

“잘…….”

머뭇거리는 목소리. 아직 방향을 정하지 못하고 우스꽝스럽게 감정이 뒤섞인 표정.

그러나 다음 순간, 고집스럽던 그의 눈매가 부드럽게 호선을 그렸다.

햇빛 만큼이나 따뜻한 음성이 산들바람이 되어 귓가에 닿았다.

“잘 돌아왔다.”

우리는 서로를 바라보며 웃었다.
```

## Final English reading copy

```markdown
# Chapter 841

Tang Sadok led Jeok Cheongang and me to a pavilion deep in the Inner Court, telling us to let him know if anything was uncomfortable or if we needed anything.

“Then I’ll be going…”

“Wait.”

At Jeok Cheongang’s quiet call, Tang Sadok—still not fully recovered—froze like a statue as he hurried to leave the pavilion.

He slowly turned around and struggled to squeeze out a voice that wouldn’t come.

“May I ask why you called me…?”

Jeok Cheongang’s gaze was deep and still. After staring at Tang Sadok in silence, he suddenly spoke.

“Forget it.”

“Pardon?”

“I said forget it. Everything you’ve seen and heard up to now.”

Myriad-Poison Asura, my ass. The man standing before him was Jeok Cheongang, the Fire King.

The current Sect Leader of the Fire Gate Clan, a venerable sect of complete thugs that popped up every now and then to turn Murim upside down whenever people least expected it.

The sect had been setting fires all over the world for more than three hundred years, generation after generation. Yet when his own residence caught fire, Jeok Cheongang had wiped out more than a thousand Demonic Cult members. The very embodiment of hypocrisy.

A bead of cold sweat he hadn’t even noticed forming rolled down Tang Sadok’s neck. He swallowed hard and answered.

“O-of course. This junior will forget everything he saw and heard.”

“Forget? You didn’t see or hear anything in the first place. What’s there to forget?”

“Ah.”

“Let’s be careful, okay? Read the room.”

Jeok Cheongang gently massaged Tang Sadok’s neck as he whispered. I’d thought he looked strangely familiar, and now I knew why. He was exactly like the high school bullies who used to hang around the alleys near my elementary school.

The only problem was that those bullies had been around seventeen, while Jeok Cheongang was at least a hundred and seventeen.

*How does someone rejuvenate a hundred years?*

He clearly wasn’t new to this.

The low voice. The half-lidded eyes. And on top of that, a masterful choice of words for the situation.

“This old man’s been in a bit of a bad mood lately. So, how do you think I’d feel if a certain kind of story got around Murim right now?”

“I-I think you’d be displeased.”

“Not just displeased. It’d ruin my whole day. I’d completely lose it.”

“I-I’m sorry, Old Master.”

“Your late father, the Poison King, and I had a decent history together. We weren’t close enough to call each other best friends, but he was someone I could trust with my back.”

The Poison King, who’d died a few months earlier at the hands of the Western Heaven Demon Lord, who was after the Myriad-Poison Ring, had been the Sichuan Tang Clan’s Grand Family Head and Tang Sadok’s father. But before that, he’d been a hero who, alongside Jeok Cheongang, had brought the Great Faction War to a victorious close as one of the Ten Kings.

“He had a bit of a gloomy streak, but he was smart and quick on the uptake. One day, he poisoned the liquor I was about to drink. Then, when he saw that Peng Cheolhu, the Thunderbolt Saber King, was getting the hell beaten out of him, he casually knocked over my cup. Do you know what happened after that?”

Tang Sadok answered in a hoarse voice.

“Yes. You said you’d let it go this once, then suddenly beat my father up three months later…”

“Do you know why I did that?”

“N-no. My father wondered about it for years, right up until a few years ago.”

“I was in a foul mood, and there wasn’t anyone around to hit. So I hit him.”

“……!”

“That’s the kind of man I am. Starting to get the picture?”

Tang Sadok’s jaw dropped as he learned the reason behind a beating that had remained a mystery for more than fifty years. And I instinctively opened my mouth.

“Isn’t that just being a lunatic?”

“……”

“……”

“Ah.”

A suffocating silence descended. Jeok Cheongang stared at me wordlessly, then slowly parted his lips.

“Get out.”

“What?”

“Get out!”

“Y-yes!”

At Jeok Cheongang’s thunderous shout, Tang Sadok looked at me with the relieved expression of a man whose fifty-year-old indigestion had finally cleared up, then shot out of the pavilion like a streak of light.

No—he ran away.

Leaving me behind.

*Was he a lizard?*

But I could hardly blame him when I’d just made a huge, beautiful mess all by myself. I took a steadying breath and spoke calmly.

“Old Master, it’s a misunderstanding.”

“What is?”

“Everything. From beginning to end.”

“Our sect’s rules say anyone who spouts bullshit from beginning to end gets beaten twice as much.”

“……Is that really one of the sect’s rules?”

“It is.”

“What lunatic—no, what esteemed person came up with that rule?”

“I did. Just now.”

*Well, I’m fucked.*

If excuses weren’t going to work, it was time to adapt. I dropped to my knees as fast as if Hyuk Mujin had possessed me.

“I’m sorry.”

“You’re admitting it faster than I expected.”

“I’ve still got a lot of life ahead of me. I can’t get beaten to death here.”

“Unlike you, this old man doesn’t think he has much life left.”

“Why not?”

“I was called a lunatic by the brat who’s supposed to be my Disciple. I ought to go die, don’t you think?”

I slowly lifted my deeply bowed head. Jeok Cheongang’s massive pectorals looked like they were at least an E-cup.

He’d recovered his youth and sharpness through Bone Transformation.

At that point, rather than him going off somewhere to die, he could tell everyone except me to go die instead.

“No, Old Master. You’ll live a long life. Though you’ve already lived one.”

“I see. But from where I’m standing, you look like you’ll die young.”

“Please don’t say things like that. You’re hurting my feelings.”

“I’m the one who ought to be more hurt. I shaved my perfectly good head clean and went all the way to Nanman pretending to be a monk, and you dare stab me in the back like this?”

I cautiously raised my head.

Then sunlight poured through the window and flashed off Jeok Cheongang’s forehead in a surprise Solar Fist attack. I reflexively squinted.

“Whoa. That’s bright.”

“……”

“Ah, sorry. And I’ve always been grateful for how much you care about me, Old Master.”

“Too late.”

“Someone once said, ‘The best time to start is when you think it’s too late.’”

“When you think it’s too late, it really is too late. Whoever said that nonsense must’ve died ages ago.”

“Then I’m sorry again.”

“Before I do anything, I want to ask you one thing.”

Jeok Cheongang looked down at me calmly and continued.

“To this old man, you seem closer to a Little Immortal than a human. So if you die, can you come back to life?”

“Why would you ask such a terrifying question…?”

“I’m simply curious.”

“But why are you curious about that…?”

“You said you came from the realm of immortals. You must be different in some way.”

“I die. I really die.”

“You, even in the realm of immortals?”

“I’m dead. I’ve only got one coin left. That was my last life from the very beginning.”

“You’re saying strange things again.”

Come on. Why would he ask something like that?

With my knees knocking, I sprang to my feet and bowed deeply to Jeok Cheongang. Once didn’t seem like enough, so I did it twice.

And as soon as I knelt again, I remembered something I’d briefly forgotten.

“Are you holding a memorial service?”

“Ah.”

“Clench your teeth. Let’s get this over with.”

Whoom.

A tremendous sound of breaking air rang out before he’d even finished speaking.

I squeezed my eyes shut on instinct and suddenly thought of Hyuk Mujin. If I made it out alive, I resolved to treat him much better than before. Then I gritted my teeth and swallowed a breath.

*Hngh…!*

And in that instant—

Tap.

Whoosh!

Along with a faint touch against my forehead, a fierce gust of wind whipped my hair around.

*Huh?*

As the hot wind died down, I opened my eyes in confusion and saw Jeok Cheongang pressing a finger to my forehead, sighing heavily with an irritated look on his face.

His eyes, however, held affection and joy at seeing me again.

“You little monster. Stop making such a fuss and get up already.”

“What?”

“If you’re going to do it, do it properly. Like…bowing, for instance.”

I blinked dumbly. Jeok Cheongang glanced toward the window, where sunlight streamed in, and muttered:

“Sure is a nice day.”

I didn’t know why laughter suddenly escaped me at that moment.

No—that wasn’t true. I already knew.

Today. The day before yesterday. Maybe for a long time now.

“Haha.”

“You little brat. What are you laughing at?”

“Nothing. Let me give you my bow. I’ll make it a proper nine-bow ritual.”

Jeok Cheongang flinched at the mention of the nine-bow ritual, then scoffed.

“We never formally established a Master-Disciple bond. What’s the point of that kind of empty ritual? Just behave yourself from now on.”

He was right. Jeok Cheongang and I had never formally established a Master-Disciple bond.

An old man who had come out into the world to eliminate the Disciple who had once been like family to him needed a new successor to carry on his sect’s teachings. And a young man struggling to stay alive needed greater strength.

They’d come together because each needed what the other had. And so the nine-bow ritual was nothing but meaningless ceremony.

Yes, that was definitely how it had been.

But…

*It stings a little, hearing him say that.*

At some point, what had once felt natural began to sting, and what had stung began to feel natural.

And this changed feeling wasn’t something only I was allowed to have.

“Later.”

A single word suddenly reached my ear.

Jeok Cheongang continued, gazing at the sunlit window. His eyes seemed to be looking at something far away.

“When the time comes, if everything returns to its proper place…”

His voice gradually grew faint, then scattered into the breeze.

But I heard him clearly.

The rest of what he’d left unsaid—not with my ears, but with my heart.

And that was enough.

At least for today.

“Old Master.”

“Why are you calling me?”

Jeok Cheongang answered without turning his head. Maybe he couldn’t bring himself to turn and face me.

“Old Master.”

“What? Why?”

His reaction was exactly what I’d expected, and it made me laugh out loud. Then I said the words I’d kept in my heart for a long time.

“It’s good to see you again. To have you still here, close by.”

“……!”

“I’m back.”

At that moment, Jeok Cheongang’s shoulders, which had gone rigid, relaxed.

He slowly turned to look at me with an expression I couldn’t quite read.

As though he’d never once had to figure out what expression to make in a moment like this, he forced his brows into a frown and twisted his lips awkwardly.

But everyone learns from experience.

No matter how much a person denies it, no matter how unfamiliar it feels, they can’t hide what’s in their heart.

That was true even of the man who had lived for more than a century with a hot, hard mask over his face—the face Murim had named the Fire King.

“Welcome…”

His voice faltered. His expression was still awkwardly tangled with feelings he hadn’t yet decided how to handle.

But the next moment, his stubborn eyes curved into a gentle arc.

A voice as warm as the sunlight reached my ear like a soft breeze.

“Welcome back.”

We smiled at each other.
```
