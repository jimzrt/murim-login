<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0711.txt",
      "sha256": "aa6d132af91d3ffc7a332822f199a1d9fd59f5350cb0d6a5e505c3ff40039549",
      "bytes": 12841
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "c28935a578f4e85e6abbb109c9c68db2554eab3c3b76bc317a7e4d9d95692365",
      "bytes": 1879
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "c1986676bc48fdff4fd48cf0f0b57f97ebad0bdfdd8467f01fb8d3155af76b6e",
      "bytes": 207119
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "162a4358263823b86fdc2534e0789a56c52f05287ebd5e6134b49762f22b645f",
      "bytes": 944
    },
    {
      "path": "characters/Blood Monk.md",
      "sha256": "470009ec42bd968a59bf4cde2fe9ab121601587664430397dae217a9422ef551",
      "bytes": 533
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "3740e87ee218cafc60b464c230a3ee779b0f78114693f1c1fe61cbdf3adab918",
      "bytes": 553
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "d996aedd1ae98a4277d0c660178d8eefef39ae95f82885a9c1c87a6da03d7907",
      "bytes": 1702
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "a45f76f9b9d5a974e71ad0787d15681d488e59c60a207c115535a4082234af20",
      "bytes": 953
    },
    {
      "path": "characters/Wang Ho.md",
      "sha256": "0915f0baec52dec75b14ec1c1e59adbda988b1cd8f00ac8b45e790fcfc0ae85d",
      "bytes": 543
    },
    {
      "path": "characters/White Tiger.md",
      "sha256": "b838f8260fb7c84446466c8e41ee8339ba7af26f938c33f1162b08b884142517",
      "bytes": 661
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "6f15dee36d5a032caa90af77c98394a0c535306a63b90c78ecec925d6c2845d1",
      "bytes": 217728
    }
  ],
  "estimated_tokens": 10660
}
-->

# Durable State Update — Chapter 711

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 711. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 711. Profile updates may replace only one
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
  "chapter": 711,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 711,
    "continuity_sources": [711],
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
    "Jeok Cheongang is the Blood Monk and has arrived at the battlefield to confront the Southern Heaven Demon Empress.",
    "The Southern Heaven Demon Empress has lost both arms and her remaining innate qi, leaving her unable to evade Jeok's attack.",
    "Jeok Cheongang struck the Southern Heaven Demon Empress with the twelve-tenths Flame Divine Palm.",
    "Jin Taekyung shielded the Southern Heaven Demon Empress from Jeok's attack and tore into her throat because her death would kill him.",
    "Jeok's Flame Divine Palm inflicted catastrophic injuries on Jin Taekyung.",
    "A clear bell and warmth followed Jin's injuries, after which he was conscious and his hand appeared restored.",
    "Jeok Cheongang believed Jin Taekyung had died and grieved over him before discovering that he survived.",
    "Jin Taekyung remains bound to the Southern Heaven Demon Empress's survival or death through the life-threatening consequence he identified."
  ],
  "continuity_sources": [
    710
  ],
  "open_questions": [
    "What is the Southern Heaven Demon Empress's final status after the throat wound and Jeok Cheongang's Flame Divine Palm?",
    "What caused the bell and warmth that followed Jin Taekyung's injuries, and how fully has he recovered?",
    "Will Baeksang survive his catastrophic injuries?",
    "Will Yayul Cheok and the White Tiger survive their wounds?",
    "What will happen to the diminished sacred stone and the guardian spirit?"
  ],
  "safe_through": 710,
  "temporary_decisions": [
    "Retain Blood Monk as Jeok Cheongang's revealed sobriquet.",
    "Render Flame Divine Palm and Zen staff consistently with the established glossary.",
    "Preserve Jeok Cheongang's gruff, profane dialogue and Jin Taekyung's dry first-person voice.",
    "Render 십이성 as twelve-tenths of its normal limit."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 사파     | **unorthodox faction**                           |                                                       |
| 대주     | **Squad Leader** / **Commander**             |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 스킬               | **Skill**                      |
| 레벨               | **Level**                      |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 혈승 | **Blood Monk** | Sobriquet of the unidentified bald martial artist active in Guizhou. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 왕호 | **Wang Ho** | Commander of the Baekcheon Unit who arrives leading white-armored reinforcements. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 평화 | **Peace Guild** | Guild name. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 박도 | **broad-bladed saber** | Rough weapon swung by the bald swordsman. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 표왕 | **Escort King** | Epithet of Ju Gongsan. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 기문진 | **Mystic Gate Formation** | Formation concealing Dong Feng's clinic in Sichuan. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 광서 | **Guangxi** | Region bordering Nanman. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 영인 | **Yeongin** | Remote county seat in Yunnan and the party's immediate destination. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 궁주 | **Palace Lord** | Title Yohi uses after realizing that Heugung is the Beast Miao King. |
| 백천대 | **Baekcheon Unit** | Baeksang's secret elite unit, cultivated over decades and held in reserve. |
| 수호령 | **guardian spirit** | Ancient title for the Black Tiger. |
| 신석 | **sacred stone** | Stone said to have existed alongside the Black Tiger's birth. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 백천대주 | **Commander of the Baekcheon Unit** | Title used for Wang Ho. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 적천강 | 남천마후 | legendary_martial_master_to_hostile_demon_empress | you bitch | blunt and threatening | Threatens to punish her and Lord of Heaven. |
| 남천마후 | 적천강 | hostile_demon_empress_to_legendary_martial_master | Fire King Jeok / you | flattering and mocking | Addresses Jeok Cheongang as the Fire King while praising Lord of Heaven. |
| 수호령 | 남천마후 | guardian_spirit_to_hostile_supernatural_opponent | you | terse, accusatory, and contemptuous | The guardian spirit tells the Southern Heaven Demon Empress that it knows her true essence and condemns her as a Fiend. |
| 남천마후 | 수호령 | hostile_supernatural_opponent_to_guardian_spirit | hideous beast | playful, taunting, and dismissive | She insults the guardian spirit while addressing it as a beast. |
| 왕호 | 야수묘왕 | Baekcheon Unit Commander to Nanman Beast Palace Palace Lord | Palace Lord | formal and deferential | Wang Ho bows and formally reports his arrival to the Beast Miao King. |
| 야수묘왕 | 남천마후 | allied_Ten_Kings_master_to_hostile_Demon_Empress | you | cold and threatening | The Beast Miao King addresses the Southern Heaven Demon Empress while promising to tear off her limbs and kill her. |

## Listed compact profiles

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 709
- **Aliases:** Heugung
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, and Great Chieftain of the Miao people; after shielding Jin Taekyung from the Southern Heaven Demon Empress's explosion, he lies unconscious with sword fragments embedded throughout his body.
- **Personality:** The Beast Miao King is boisterous and warmhearted toward Nanman's people, but their corruption and destruction awaken fierce grief and wrath in him.
- **Voice:** Low, growling, and forceful.
- **Relationships:** Baeksang is his sworn younger brother and childhood companion, Yayul Mok is his Young Palace Lord, Jeok Cheongang is an old acquaintance, and Jin Taekyung is Jeok's Disciple whom he now fights beside against the Southern Heaven Demon Empress.

### Blood Monk.md

# Blood Monk (혈승)

- **Safe through:** Chapter 710
- **Aliases:** Jeok Cheongang; Fire King
- **Role:** The Blood Monk is Jeok Cheongang, the Fire King and legendary martial master who uses a steel Zen staff and the Flame Divine Palm.
- **Personality:** Unknown; the captured witness who described him was unable to provide further information before dying.
- **Voice:** Not established.
- **Relationships:** His connection to Dark Heaven and Nanman is unknown.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 710
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 710
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 710
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress is Honglan, creator of the rift behind the Inner Palace; she survives the explosion that follows Baeksang's ambush, is critically wounded after Jin Taekyung drives White Flame through her chest, loses both arms, has her remaining innate qi stripped away, and is struck by Jeok Cheongang's Flame Divine Palm before Jin attacks her throat.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

### Wang Ho.md

# Wang Ho (왕호)

- **Safe through:** Chapter 709
- **Aliases:** None
- **Role:** Wang Ho is the Commander of the Baekcheon Unit; after Jin Taekyung returns to fight, he joins fewer than twenty surviving warriors in their assault on the Southern Heaven Demon Empress.
- **Personality:** Not established.
- **Voice:** Formal and deferential when addressing the Palace Lord.
- **Relationships:** He commands the Baekcheon Unit and acknowledges Yayul Cheok as its Palace Lord.

### White Tiger.md

# White Tiger (백호)

- **Safe through:** Chapter 708
- **Aliases:** Whitey
- **Role:** The White Tiger is the guardian spirit of the sacred stone and leads the Sacred Land beasts; after shielding Jin Taekyung from the Southern Heaven Demon Empress's explosion, it lies gravely wounded while the sacred stone has shrunk to child-fist size.
- **Personality:** Irritable and contemptuous of Jin Taekyung's jokes.
- **Voice:** Telepathic, terse, and easily exasperated.
- **Relationships:** The White Tiger carries Jin Taekyung and Yohi, guards the sacred stone, and advances with Jin's forces.

## Korean source

```text
＃711화



때로 어떤 종류의 침묵은, 수많은 감정과 말을 대신하기도 한다.

바로 지금처럼.

“그, 우선 손부터 좀 빼고 얘기할까요?”

“…….”

결론부터 말하자면 적천강은 손을 빼지도, 그렇다고 뭐라 대답하지도 않았다. 그저 넋이 나간 사람처럼 멍하니 내 얼굴과 전신 곳곳을 훑어볼 뿐이었다.

이 새끼 뭐지? 설마 이게 다 꿈인가?

딱 그런 눈빛이었고, 나는 적천강의 심정을 십분 이해했다.

‘이런 반응을 보일 수밖에 없지.’

눈앞에서 다 죽어 가던 놈이 멀쩡히 살아났다.

십자가에 못 박혀 죽은 뒤 사흘 만에 부활했다던 옆 동네 예언자도 손바닥에 상처는 남아 있었는데, 다섯 번의 레벨 업은 나를 상처 하나 없는 애기 피부로 만들어 줬다.

심지어 적천강이 지켜보는 앞에서.

쫙!

난데없이 울려 퍼지는 찰진 소리.

온 힘을 다해 셀프 귀싸대기를 날린 적천강이 눈을 깜빡이며 나를 바라보더니, 침중한 표정으로 입을 열었다.

“하나만 묻자. 노부가 지금 꿈을 꾸고 있는 것이냐?”

내가 조심스럽게 대답했다.

“아뇨.”

“아무리 생각해 봐도 꿈 같은데.”

“그럼 뺨 한 대 더 때려 보세요.”

쫘악!

역시 노빠꾸.

어지간히도 강하게 때린 모양이다.

입에 고인 핏물을 걸쭉하게 뱉어 낸 적천강이 심호흡했다.

“……염병할. 꿈은 아니로군. 그럼 기문진(奇門陣)에 의한 환영인가?”

“어, 그것도 아닐걸요. 만약에 제가 환영이면 지금 노야가 잡고 있는 손은 누구 겁니까.”

“네 환영을 덧씌운 암천의 술사겠지. 아니면 죽은 줄 알았던 남천마후거나. 노부가 환영에 홀린 틈을 타 일격을 준비하고 있을 거야.”

“상상력 한번 끝내주시네. 노망나셨어요?”

“말하는 싸가지만 보면 영락없이 네놈이긴 한데. 허어. 정말이지 미치겠군.”

“저도 미치겠습니다.”

진심이다.

지금까지 시스템에 관해서는 철저하게 숨겨 왔는데, 이제는 빼도 박도 못하게 발각당했으니까.

한숨을 내쉰 나는 여전히 혼이 나간 듯한 표정을 짓고 있는 적천강을 바라보았다.

대충 빡빡 밀어 버린 민머리에 낡은 승복을 걸친 그의 모습은 봐도 봐도 적응이 되지 않았다.

“그건 그렇고. 도대체 그 꼴은 뭡니까?”

“보면 모르겠느냐? 변복(變服)이지. 이 정도면 그럭저럭 승려 같지 않으냐?”

“절간에 불 지르고 도망친 파계승 같은데요.”

“……빌어먹을 놈. 노부라고 땡중 흉내를 내고 싶었겠느냐? 암천의 눈을 피하려면 어쩔 수 없었다. 특히 머리카락이 워낙 눈에 띄는 바람에 싹 밀어 버렸지.”

하긴, 천하가 아무리 넓다 해도 붉은색 머리카락을 가진 사람은 흔치 않다. 어디에 가도 눈에 띄기 마련이고, 소문이 퍼지는 건 당연지사다.

물론 그렇다고 해서 모든 것이 설명되는 것이 아니다.

최소한 내가 아는 혈승(血僧)은, 단신으로 광서성을 피로 물들인 무시무시한 대마두니까.

“그래서 암천의 눈을 피해서 승려로 변복까지 하셨다는 분이, 무고한 무림인 수백 명을 때려죽였습니까?”

“그건 그놈들이 하는 짓거리가 워낙…… 뭐?”

뭐라 말을 이으려던 적천강이 눈살을 찌푸렸다.

“무고한 무림인이라니. 그게 무슨 헛소리냐?”

“……?”

“노부가 광서성에서 뜻하지 않게 이목을 끈 것은 사실이다. 사파 잡놈들이 혼란스러운 틈을 타 별의별 개짓거리를 다 하고 있길래 손 좀 봐줬지.”

“사파? 지금 사파라고 하셨어요?”

“그래. 암천의 소행인 것처럼 위장해서 온갖 패악질을 부리고 있었다. 직접 찾아가서 방파 여섯 개 정도를 박살 내 버렸더니 나머지 잔챙이들이 사방으로 도망치더군.”

“……!”

입을 벌린 채 적천강의 이야기를 듣고서야 나는 전후 사정을 알아차렸다.

‘광서성에서 도망쳐 왔다는 그 무림인.’

남만에 입갤하자마자 풍토병에 걸려 죽었다던 그 무림인이, 알고 보니 적천강의 불주먹을 피해 도망쳤던 사파 잔챙이였던 거다.

자고로 가재는 게 편이고, 사람은 눈치가 있어야 하는 법.

가뜩이나 외지인이 배척받는 남만에서 스스로 나쁜 놈이라는 걸 밝힐 수도 없었을 테고, 그 과정에서 적천강에게 죽은 사파 무림인들은 정의와 평화를 사랑하는 협객들로 둔갑했다.

워낙 폐쇄적이고 외부와 교류가 없는 남만이었기에 벌어진 일이다.

‘이게 시발, 이렇게 되나.’

멍하니 적천강을 바라보던 나는, 순간 뇌리를 스치는 어떤 생각에 황급히 입을 열었다.

“그럼 혹시 오는 길에…….”

“누굴 말하는지는 모르겠지만, 다 만났다. 장강에서 물질하는 수적 놈들부터 난데없이 창칼부터 들이댄 남만 놈들. 그리고 네놈의 수하들까지.”

“아.”

“표왕(漂王)의 손녀가 노부를 보자마자 그러더군. 네놈이 위험에 처했다고. 혁가 놈은 바짓가랑이를 붙잡고 질질 짜는 통에 손목을 부러트릴 뻔했다.”

말만 들어도 눈앞에 선하게 떠오른다. 누구보다 간절했을 그들의 모습이.

그리고 내가 위험하다는 말에 어떤 의문도, 망설임도 없이 곧장 달려왔을 적천강의 모습이.

“한데, 왜 이야기가 이쪽으로 빠진 거냐? 설명이 필요한 건 되레 노부이거늘.”

짐짓 인상을 구기는 적천강을 보며, 나는 문득 실소를 흘렸다.

“……웃어?”

황당해하는 적천강의 모습에 웃음이 더욱 짙어진다.

“당연히 웃어야죠. 이렇게 살아서 다시 만났는데.”

“……!”

“죄송하고, 감사합니다. 궁금하신 점이 많겠지만 나중에 다 설명해 드릴게요. 반드시.”

내 말을 들은 적천강은 할 말이 많은 듯한 표정이었지만, 이내 가라앉은 목소리로 대답했다.

“염병할 놈 같으니.”

수많은 감정이 뒤섞인 한마디였다.

마치 내게 살아 있어 줘서 고맙다고 하는 것처럼 들리기도 했고, 그와 나 사이에는 그것만으로 충분했다.

“자꾸 웃지 마라. 정든다.”

“정이 안 든 것치고는 꽤 서럽게 우시던데. 아, 물론 노야 얘기는 아니고요.”

“……그 주둥이 닥치지 못할까.”

이제야 조금 전 자신의 모습이 생각났는지, 씨근덕거리면서도 손을 붙잡아 일으켜 세워 주는 적천강이었다.

투둑.

내 전신을 뒤덮고 있던 먼지와 돌가루가 쏟아져 내린다. 통증은 사라진 지 오래였지만, 순간 눈앞이 흐릿해졌다.

‘음.’

나는 침음성을 삼켰다.

무려 다섯 번의 레벨 업으로 멀쩡하게 회복된 몸은 의지에 따라 움직였지만, 쉴 새 없이 반복된 전투로 시달린 정신은 피로하기 그지없었다.

‘아, 자고 싶다.’

당장이라도 쓰러지고 싶은 마음이 간절했다.

몸도 마음도 개운하게 푹 자고 일어나, 맑은 하늘을 바라보며 조금씩 잠기운에서 벗어나는 그런 하루를 보내고 싶었다.

하지만…… 아직은 아니다.

머리 위로 펼쳐진 하늘은 여전히 먹구름으로 가득했고, 각기 크고 작은 부상을 입은 이들은 신음을 내뱉으며 곳곳에 쓰러져 있었다.

저들을 이대로 내버려 둔다면, 영영 깨울 수 없는 잠에 빠지고 만다.

뒤늦게 주위를 둘러본 적천강 역시 좋지 않은 표정이었다.

“……노부가 더 서둘렀다면 좋았을 것을.”

부질없는 후회고, 괜한 자책이다. 적천강이 오지 않았다면 나를 포함한 모두가 이 자리에서 뼈를 묻었을지도 몰랐으니까.

“서두르자. 더 늦기 전에.”

적천강의 말에 고개를 끄덕인 나는, 가장 정확하고 빠른 방법을 선택했다.

‘스킬, [기감] 발동.’

띠링.

시스템이 작동했음을 알리는 맑은 종소리와 함께, 나를 중심으로 뻗어 나간 푸른 원이 일정한 범위를 감싸 안았다. 그와 동시에 곳곳에서 솟아오른 레벨 표시 창들을 보자 가슴이 답답해진다.

‘너무 적어.’

눈으로 확인한 레벨 창의 개수는 삼십여 개가 전부였다.

일천을 헤아리던 남만 전사들도, 삼백 명의 백천대도 이 자리에 뼈를 묻었다는 뜻이다.

이 와중에도 그나마 한 가지 다행인 점은, 지금까지 숨이 붙어 있는 이들의 상태가 그리 위중하지 않다는 것이었다.

‘마지막에는 남천마후 역시 힘을 최대한 아껴야 했을 테니까.’

무거운 마음을 담아 뇌까린 나는 가장 가까운 곳에 쓰러진 이를 향해 신형을 날렸다.

백천대주 왕호. 마지막 순간까지 남천마후를 향해 달려들었던 그의 완맥을 붙잡고, 다른 한 손으로 등줄기를 통해 공력을 흘려 보냈다.

스아아아아.

“쿠, 쿨럭.”

죽은 핏물을 한 움큼 뿜어낸 왕호의 창백한 얼굴에 붉은 핏기가 돌기 시작한다.

백천대 중 가장 치열하게 싸웠던 만큼 타격을 입었던 그였으나, 이것으로 한시름 놓을 수 있을 것이다.

그러나 이런 왕호와 달리, 한눈에 보기에도 막중한 부상을 입은 이들 역시 있었다.

흐으으. 흐으.

코끝에서 흘러나오는 숨이 가늘다. 무릎을 꿇은 채 쓰러진 거한의 정체를 알아본 적천강이 침음성을 흘렸다.

“……된통 당했군. 이놈 이거, 정마대전 때도 이 정도 부상을 입은 적은 없었는데.”

목숨마저 내걸었던 남천마후의 일격은 그만큼 무시무시했다.

전신에 깊숙이 틀어박힌 무수한 검의 파편과 잔해.

거기에 더해 나를 보호하는 과정에서 입은 막대한 내상으로 정신까지 잃은 야수묘왕의 상태는 처참하기 그지없었다.

“노야, 혹시.”

내 말이 이어지기도 전에, 목소리에 담긴 우려를 알아차린 적천강이 고개를 저었다.

“야수묘왕은 무쇠처럼 단단한 놈이니 걱정 말거라. 노부가 최선을 다한다면 능히 살아남겠지. 한데…….”

길게 늘어지는 말꼬리. 확신이 담겨 있던 첫 마디와 달리, 망설이는 듯한 눈빛이 몇 걸음 떨어진 곳에 쓰러져 있는 거대한 백호를 향한다.

“저 짐승은 모르겠다. 보아하니 짐승치고는 범상치 않아 보인다만, 꼭 살려야 하는 녀석이냐?”

살려야 합니다. 무슨 수를 써서라도.

하지만 내 생각이 입술 밖으로 흘러나오기도 전에, 나지막한 의념이 울려 퍼졌다.

- 만약 그리된다면. 그 역시 내게 주어진 운명이겠지.

“……!”

- 제법 오랜 세월을 살았구나, 늙은 인간이여. 비록 이무기의 기억 속에서 보았던 얼굴과는 다르지만, 본질은 달라지지 않지.

눈을 부릅뜬 적천강에게서 고개를 돌린 수호령의 시선이 나를 향해 옮겨진다.

- 가까이 오너라.

나는 입술을 깨물며 수호령에게 다가갔다.

머리맡에 앉아 핏물로 흠뻑 젖은 목덜미를 쓰다듬어 주자, 낮은 울음소리가 흘러나왔다.

- 건방지구나. 감히 이 몸에게 손을 대다니.

무슨 말을 해야 할까.

그저 말없이 목덜미만 쓰다듬는 내게, 수호령이 의념을 흘려 보냈다.

- 사실 썩 기분이 나쁘지만은 않구나. 아주 오래전에도 너처럼 괘씸한 인간이 있었지.

누구인지 알 것 같다.

남만야수궁의 초대 궁주. 아득한 세월을 살아온 수호령이 마음을 열었던 유일한 인간.

- 참으로 이상한 일이지. 모든 것이 다른데, 너를 보고 있자면 이미 수백 년 전 흙이 되어 버린 그가 떠오른다는 것이.

“……!”

- 아마도 그래서였을지도 모르겠구나. 본능적으로 널 구한 것도, 인간에 불과한 네게 신석(神石)을 맡긴 것도.

손에 닿아 있는 백호의 거대한 몸뚱어리가 크게 들썩인다.

거칠게 호흡한 수호령이 청백색의 눈을 들어 나를 바라보았다.

그 순간, 나는 본능적으로 알아차렸다.

수호령이 왜 신석을 필요로 하는지. 그것으로 무엇을 하려 하는지.

‘균열.’

수호령은 스스로 저 짙은 어둠을, 균열을 닫으려 하고 있었다.

수 개월 전, 어느 이무기가 그러했듯이.
```

## Final English reading copy

```markdown
# Chapter 711

Sometimes, a certain kind of silence can take the place of countless emotions and words.

Just like now.

“Um… how about you let go of my hand first, then we talk?”

“……”

To give you the conclusion first, Jeok Cheongang neither let go of my hand nor answered. He simply stared blankly, sweeping his gaze over my face and every part of my body like a man who had lost his soul.

*What the hell is with this guy? Could all this really be a dream?*

That was exactly what his eyes seemed to say, and I understood Jeok Cheongang’s feelings perfectly.

*He can’t possibly react any other way.*

The guy who had been dying right before his eyes had come back to life perfectly intact.

Even that prophet from the neighborhood over who was said to have risen three days after being nailed to a cross still had wounds on his palms. But five level-ups had turned me into a baby’s smooth, unblemished skin.

And Jeok Cheongang had watched the whole thing happen.

Smack!

A crisp sound rang out of nowhere.

Jeok Cheongang had slapped himself across the face with all his strength. He blinked at me, then opened his mouth with a solemn expression.

“Let this old man ask you one thing. Am I dreaming right now?”

I answered carefully.

“No.”

“No matter how I think about it, this feels like a dream.”

“Then try slapping yourself one more time.”

Smack!

Of course he didn’t hesitate.

He must have hit himself pretty damn hard.

Jeok Cheongang spat out a thick mouthful of blood that had gathered in his mouth, then took a deep breath.

“……Damn it. It isn’t a dream. Then is this an illusion created by a Mystic Gate Formation?”

“Uh, I don’t think so. If I were an illusion, whose hand would the Old Master be holding right now?”

“A Dark Heaven sorcerer has overlaid your illusion on himself. Or perhaps it’s the Southern Heaven Demon Empress, whom we thought was dead. They must be preparing a killing blow while this old man is caught in the illusion.”

“Your imagination is incredible. Have you gone senile?”

“Judging by the way you talk, you’re unmistakably you. Haaah. This is truly driving me mad.”

“It’s driving me mad too.”

I was serious.

I had kept the System completely hidden until now, but now I’d been caught red-handed with no way to deny it.

I sighed and looked at Jeok Cheongang, who still wore an absent expression.

I still couldn’t get used to his appearance, no matter how many times I looked at him. He had a roughly shaved bald head and wore a threadbare monk’s robe.

“Putting that aside, what the hell is with your outfit?”

“Can’t you tell by looking? It’s a disguise. Don’t I look more or less like a monk?”

“You look like a defrocked monk who set fire to a temple and ran away.”

“……You insolent brat. Do you think this old man wanted to imitate some bald-headed monk? It couldn’t be helped if I wanted to avoid Dark Heaven’s eyes. My hair was especially conspicuous, so I shaved it all off.”

He had a point. No matter how vast the world was, people with red hair were uncommon. He would stand out wherever he went, and rumors spreading was inevitable.

Of course, that didn’t explain everything.

At least, the Blood Monk I knew was a terrifying great fiend who had dyed Guangxi red with blood all by himself.

“So the man who disguised himself as a monk to avoid Dark Heaven’s eyes went around beating hundreds of innocent Murim practitioners to death?”

“The things those bastards were doing were so—what?”

Jeok Cheongang’s brow furrowed as he tried to continue.

“Innocent Murim practitioners? What nonsense are you talking about?”

“……?”

“It is true that this old man unintentionally attracted attention in Guangxi. The unorthodox faction bastards were taking advantage of the chaos to get up to all kinds of despicable nonsense, so I taught them a lesson.”

“Unorthodox faction? Did you just say unorthodox faction?”

“That’s right. They were committing all kinds of atrocities while disguising them as the work of Dark Heaven. This old man went to find them himself and destroyed about six of their organizations. The remaining small fry fled in every direction.”

“……!”

Only after listening to Jeok Cheongang’s story with my mouth hanging open did I understand what had happened.

*That Murim practitioner who fled from Guangxi.*

The Murim practitioner who had allegedly caught some endemic disease and died as soon as he entered Nanman had actually been a small-time member of the unorthodox faction fleeing Jeok Cheongang’s fiery fists.

A crayfish sides with a crab, and people need to know how to read the room.

Nanman already shunned outsiders. There was no way those people could admit that they were bad guys, and in the process, the unorthodox practitioners killed by Jeok Cheongang had been transformed into righteous heroes who loved justice and peace.

It had happened because Nanman was so isolated and had so little contact with the outside world.

*How the fuck did things turn out like this?*

As I stared blankly at Jeok Cheongang, a thought suddenly flashed through my mind, and I hurriedly opened my mouth.

“Then, on your way here, did you happen to—”

“I don’t know who you mean, but I met them all. The bandits diving for things in the Yangtze, the Nanman people who suddenly came at me with spears and swords, and even your subordinates.”

“Oh.”

“The Escort King’s granddaughter told me the moment she saw me that you were in danger. That Hyuk fellow grabbed me by the trouser leg and cried so hard I nearly broke his wrist.”

I could see it all so clearly just from hearing him describe it. Their appearance, their desperation more than anything else.

And Jeok Cheongang, who had come rushing here without a single question or hesitation the instant he heard that I was in danger.

“But why did the conversation turn this way? I’m the one who needs an explanation.”

Seeing Jeok Cheongang deliberately frown, I suddenly let out a quiet laugh.

“……Are you laughing?”

The absurdity on Jeok Cheongang’s face made my smile grow wider.

“Of course I’m laughing. We survived and met again like this.”

“……!”

“I’m sorry, and thank you. I’m sure you have a lot of questions, but I’ll explain everything later. I promise.”

Jeok Cheongang looked as though he had a great deal to say, but soon answered in a subdued voice.

“You damn brat.”

It was a single sentence filled with countless emotions.

It even sounded as if he were thanking me for staying alive, and that was enough for the two of us.

“Stop smiling. I’ll get attached.”

“For someone who supposedly isn’t attached, you were crying pretty bitterly. Of course, I’m not talking about you, Old Master.”

“……Can you shut that mouth of yours?”

Perhaps he had finally remembered how he had acted a moment ago. Still huffing, Jeok Cheongang took my hand and helped me to my feet.

Pat pat.

The dust and stone grit covering my entire body fell away. The pain had been gone for a long time, but my vision blurred for a moment.

*Hmm.*

I swallowed a groan.

My body, healed perfectly by no fewer than five level-ups, moved according to my will. But my mind, battered by one battle after another without a moment’s rest, was exhausted beyond measure.

*Ah, I want to sleep.*

I desperately wanted to collapse right then and there.

I wanted to sleep deeply, body and mind refreshed, then spend a day gazing at a clear sky as I slowly shook off the drowsiness.

But… not yet.

The sky overhead was still filled with dark clouds, and people covered in injuries both great and small lay scattered everywhere, groaning.

If we left them like this, they would fall into a sleep from which they could never be woken.

Jeok Cheongang looked around belatedly, and his expression darkened as well.

“……If only this old man had hurried more.”

It was pointless regret and needless self-reproach. If Jeok Cheongang hadn’t come, all of us—including me—might have been buried here.

“Let’s hurry. Before it gets any later.”

I nodded at Jeok Cheongang’s words and chose the most accurate and fastest method.

*Skill: Qi Sense activated.*

Ding.

Along with the clear ringing of a bell announcing that the System had activated, a blue circle spread outward from me and enclosed a set area. At the same time, Level display windows rose here and there, and my chest tightened.

*There are too few.*

There were only about thirty Level windows visible to my eyes.

That meant the Nanman warriors, once nearly a thousand strong, and the three hundred members of the Baekcheon Unit had fallen here.

Even in the midst of all this, there was at least one fortunate thing: the condition of those who still had breath was not particularly critical.

*The Southern Heaven Demon Empress must have had to conserve as much strength as possible at the end, too.*

Muttering with a heavy heart, I shot toward the person lying closest to me.

Wang Ho, Commander of the Baekcheon Unit.

I grasped his wrist pulse as he had charged at the Southern Heaven Demon Empress until the final moment, then sent internal energy through his back and along his spine with my other hand.

Ssshhhhhh.

“C-cough.”

After Wang Ho spat out a mouthful of dark blood, color began to return to his pale face.

He had been struck particularly hard because he had fought the fiercest battle among the Baekcheon Unit, but this should let us breathe a little easier.

However, unlike Wang Ho, there were also people whose injuries were grave at a single glance.

Hhh… hhh…

His breath came faintly through his nose. Jeok Cheongang recognized the giant who had collapsed on his knees and let out a low groan.

“……He really got beaten to hell. This fellow never suffered injuries this bad, not even during the Great Faction War.”

The Southern Heaven Demon Empress’s One Strike, delivered with her very life on the line, had been that terrifying.

Countless fragments and pieces of swords were lodged deep throughout the giant’s body.

On top of that, the Beast Miao King had lost consciousness from the severe internal injuries he had suffered while protecting me. His condition was utterly wretched.

“Old Master, what if—”

Before I could finish, Jeok Cheongang realized the concern in my voice and shook his head.

“The Beast Miao King is as tough as iron, so don’t worry. If this old man does his best, he should be able to survive. But…”

His words trailed off.

Unlike his confident first sentence, his hesitant gaze turned toward the enormous White Tiger lying several steps away.

“I don’t know about that beast. It doesn’t seem like an ordinary creature, even for a beast, but is it something you absolutely have to save?”

*We have to. No matter what.*

But before my thoughts could escape my lips, a quiet Will rang out.

—If that is how it turns out, then that too must be the fate given to me.

“……!”

—You have lived a rather long time, old human. Though your face differs from the one I saw in the imugi’s memories, your essence has not changed.

The guardian spirit turned its head away from Jeok Cheongang, whose eyes had widened, and shifted its gaze toward me.

—Come closer.

I bit my lip and approached the guardian spirit.

When I sat beside its head and stroked the back of its neck, which was drenched in blood, a low growl escaped it.

—How insolent. How dare you lay a hand on this body?

What should I say?

As I silently stroked only its neck, the guardian spirit sent another thought to me.

—It is not entirely unpleasant, in truth. A human just as obnoxious as you existed a very long time ago.

I thought I knew who it meant.

The first Palace Lord of the Nanman Beast Palace. The only human to whom the guardian spirit, which had lived for an age beyond imagining, had ever opened its heart.

—It is truly strange. Everything is different, yet when I look at you, I am reminded of him—the one who became earth hundreds of years ago.

“……!”

—Perhaps that is why. Perhaps that is why I saved you on instinct, and entrusted the sacred stone to you, a mere human.

The enormous body of the White Tiger beneath my hand heaved violently.

The guardian spirit breathed roughly, then lifted its blue-white eyes to look at me.

At that moment, I understood instinctively.

Why the guardian spirit needed the sacred stone. What it intended to do with it.

*The rift.*

The guardian spirit was trying to close that dense darkness—the rift—all by itself.

Just as an imugi had done several months ago.
```
