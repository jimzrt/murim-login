<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0846.txt",
      "sha256": "92769cfe725d137b60b182dd4adee3b633850f7fefbb40f5b185b58b5bc5563d",
      "bytes": 13127
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "f29739d2a30df9cea80544e34b9077ffe11f7df04cdbddd3adfcd5306a6d7b72",
      "bytes": 2870
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2ac235886e36b4a9cfac67990c4e303d5cbbbaacdc20104970ce04b7ba9ca08c",
      "bytes": 227427
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "f1ce9c4cde41b2d0f22f880b95ec0b7726d3b05520d8d27f62416ed30a44558d",
      "bytes": 759
    },
    {
      "path": "characters/Jang Sam.md",
      "sha256": "cb54c4eb5fe9d3c07b38cd58fb3c1626fd83dc8d5615ed40b673744c7bbe753e",
      "bytes": 470
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "7477e34d4655c5d601b7f3b82e15fa29f1fa00f6d2c0d272269105d889cf5276",
      "bytes": 1573
    },
    {
      "path": "characters/Tang Sadok.md",
      "sha256": "3ca1844cef2a964fc8c30835cfb43f6eb429980d7871b2f72e1517e47821f15d",
      "bytes": 925
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "fd4790bf594f3f982af466f12b95b581c707ae942c0105f2f4d7be2cafb615a6",
      "bytes": 252065
    }
  ],
  "estimated_tokens": 10002
}
-->

# Durable State Update — Chapter 846

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
1 and safe_through 846. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 846. Profile updates may replace only one
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
  "chapter": 846,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 846,
    "continuity_sources": [846],
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
    "The supernatural Rift began at 10%; its progress increases the distribution and concentration of magical power.",
    "The System’s Status Window is inaccessible; Jin suspects an update may be responsible.",
    "Jin’s vision of a black-haired man killing Ahomed after the ritual remains unexplained; Jin believes the man was not Asmodeus.",
    "Jin’s [Broken Body] injury and damaged vital essence remain unresolved; the Divine Physician says full recovery is impossible but improvement is possible.",
    "Jin is at the Sichuan Tang Clan, where the Divine Physician’s pill was absorbed through Jeok Cheongang’s treatment; Jin is unconscious.",
    "Jeok Cheongang and Jin Taekyung trust each other deeply; their Master-Disciple bond remains unformalized.",
    "The Sichuan Tang Clan and Sichuan Murim are rebuilding after Dark Heaven’s attack; allied martial artists remain to treat patients and guard against another attack.",
    "Dark Heaven developed experimental seeds over years of research and scattered some across the Central Plains; some have already blossomed.",
    "The Blood Lord ordered sorcerers to prepare selected seeds for later deployment and sent missives by hawk.",
    "The Lord of Heaven recently ordered the Blood Lord to bring down the heavens, then returned to sleep.",
    "An urgent arrival is suggested by a door bursting open and the sound of horses’ hooves outside."
  ],
  "continuity_sources": [
    845
  ],
  "open_questions": [
    "Why did the Main Quest fail despite the Doppelganger’s erasure, and who or what was summoned?",
    "Was Jin’s vision of the summoned being real, System-delivered, or prophetic?",
    "What will happen as the Rift progresses and more beings enter the world?",
    "Who or what chose Jin, what is the Ark, and how did Dark Heaven reach Murim?",
    "What are Dark Heaven’s seeds, and what are the two effects the experiments seek to enhance?"
  ],
  "safe_through": 845,
  "temporary_decisions": [
    "Keep magical power distinct from mana; keep Blink distinct from Teleport and Warp. Extended-range Blink causes severe strain.",
    "Keep Fire Storm and Aqua Storm as distinct named spells.",
    "Render [영웅의 검] as “Hero’s Sword,” 에어 슬래시 as “Air Slash,” and 실드 마법 as “Shield magic.”",
    "Render 선택받은 자 as “the Chosen One,” 방주의 주인 as “the Master of the Ark,” [격변] as [Cataclysm], [어데 도씹니꺼] as “Where’s Your Do Clan From?,” and [종족 학살자] as “Species Slayer.”",
    "Render 균열 as a social fracture or division, not the supernatural Rift; render 醜王 as “Disgrace King” when used as Jin’s mocking imagined epithet for Jeok Cheongang."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 암천     | **Dark Heaven**                  |
| 사천당가   | **Sichuan Tang Clan**            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 낭인     | **wandering martial artist**                     |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 가주     | **Family Head**                              |
| 제자     | **Disciple**                                 |
| 상태               | **Status**                     |
| 사천     | **Sichuan**            |
| 귀가      | **your family**                                                 |
| 대사      | **Master** for a senior Buddhist monk                           |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 당사독 | **Tang Sadok** | Current Family Head of the Sichuan Tang Clan; also called the Myriad-Poison Asura. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 백주 | **baijiu** | Strong distilled liquor ordered at the inn. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 당가 | **Tang Family** | Short form for the Sichuan Tang Clan when distinguished from 사천당문. |
| 만독수라 | **Myriad-Poison Asura** | Epithet of Tang Sadok. |
| 호위장 | **Captain of the Guards** | The Sichuan City Lord's guard captain. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 골골 | **Golgoli** | Jin's nickname for the Skeleton King. |
| 사천혈사 | **Sichuan Blood Tragedy** | Earlier incident in which Taekyung witnessed the strange formation. |
| 독의 | **Poison Physician** | Taekyung's mocking description of Mungyeong after learning how aggressively he uses poison. |
| 심해 | **deep sea** | Unexplored ocean depths where the ancient monster awakens. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 호위 | 당사독 | guard_to_Family_Head | Family Head | formal-deferential | Uses 가주님 while reporting Jin Taekyung's request. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 적천강 | 의원 | interrogator_to_physician | you; quack | blunt and threatening | Jeok shakes the physician and demands an explanation for Jin's seven-day sleep before ordering him to summon the Beast Miao King. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 845
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jang Sam.md

# Jang Sam (장삼)

- **Safe through:** Chapter 652
- **Aliases:** Killing Ghost
- **Role:** A Hubei fisherman who disappeared for a month and returned as the Killing Ghost, a monster that grew stronger and more grotesque with each appearance.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** No relationships established.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 845
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; they trust each other deeply but have never formalized their bond. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to the late Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and is a long-standing rival of Peng Cheolhu.

### Tang Sadok.md

# Tang Sadok (당사독)

- **Safe through:** Chapter 841
- **Aliases:** Myriad-Poison Asura
- **Role:** Current Family Head of the Sichuan Tang Clan, overseeing its recovery and relying on allied martial artists to help treat patients and guard against another Dark Heaven attack.
- **Personality:** Blunt and unsentimental, yet grateful to those who remain with the Tang Clan; he has consciously chosen to change and speaks candidly about the clan’s vulnerability.
- **Voice:** Hissing, curt, authoritative, and threatening.
- **Relationships:** Tang Taesang was his father and predecessor, his unnamed nephew serves as Master of the Gatekeeper Pavilion, Mimi is his cherished old friend and companion temporarily entrusted to Cheongpung, and he regards Jin Taekyung and Cheongpung as benefactors, openly welcoming Jin with a warmth he usually conceals.

## Korean source

```text
＃846화



두두두두!

이십여 기의 기병은 거침없이 내달렸다.

깊게 눌러쓴 투구 아래로 드러난 얼굴들은 다급했고 숨 가쁘게 호흡하는 말들의 입가에는 허연 침이 말라붙어 있었으나 그들은 단 한 순간도 고삐를 늦추지 않았다.

마치 하나의 요새처럼 석벽으로 둘러싸인 목적지에 도달하기 전까지는.

그리고 그런 그들을 가장 먼저 맞이한 것은, 경계 가득한 외침이었다.

“멈추어라!”

그야말로 순식간이었다.

석벽 위에서 터져 나온 고함과 함께, 섬광처럼 쏘아진 십여 발의 화살이 기마병들의 투구 깃을 관통한 것은.

쐐애애액! 푸푸푹!

신기(神機)에 가까운 정확도와 강맹한 위력.

지면에 틀어박힌 채 파르르 떨리는 화살을 확인한 기마병들의 눈동자가 흔들렸다.

실수?

아니다. 이건 경고다.

만약 경고를 무시하고 더 가까이 접근한다면, 그때는 투구 깃이 아닌 목젖을 꿰뚫으리라는 협박이기도 했다.

“흡……!”

사방에서 터져 나온 탄식.

약속이라도 한 듯 제자리에 멈춰 선 이십여 기의 기마병들은 두려움을 숨기지 못했지만, 그 중심에 선 한 사내는 달랐다.

‘과연, 명불허전.’

사내는 경탄과 긴장이 뒤섞인 눈빛으로 석벽 위를 바라보았다. 이른 아침의 햇빛을 등진 채 활시위를 겨누고 있는 일단의 무리.

녹색 무복을 걸친 그들의 머리 위에는, 일필휘지로 써 내려간 네 글자가 적힌 깃발이 펄럭이고 있었다.

사천당가(四川唐家).

구파일방과 오대세가. 작금의 천하 무림을 지탱하는 열다섯 개의 기둥.

그리고 그중에서도 가장 폐쇄적이고, 교활하기로 이름난 이들.

하지만…….

‘바로 이곳에, 그가 있다.’

마음을 다잡은 사내는 홀로 앞으로 나섰다. 언제 날아들지 모를 화살을 막아 줄 든든한 방패 대신, 품에서 꺼내든 은패(銀牌)를 높게 치켜들며.

“공격하지 마시오! 성주부(星州府)에서 왔소!”



* * *



“누구라고?”

“황 모라고 하오. 성주님의 호위장을 맡고 있소.”

“성주? 아, 그 골골대고 있다는 그놈?”

“……뉘신지는 모르나, 언행을 조심하는 것이 좋을 거요.”

“상대가 뉘신지 모르면 네놈이 말을 조심해야지. 척 보아하니 무림에서 어느 정도 굴러먹었던 놈 같은데. 그리 간단한 것도 깨닫지 못했느냐?”

사내, 호위장은 자신도 모르게 마른침을 꿀꺽 삼켰다.

다분히 시비조인 말을 들었음에도 전혀 기분이 나쁘지 않다.

아니, 정확히 말하자면 그것이 너무나도 당연하게 느껴질 만큼 상대의 태도와 분위기가 자연스러웠다.

‘이자는 누구지?’

호위장은 임무도 잠시 잊은 채 눈앞의 상대를 바라보았다.

거한(巨漢)이라 부를 정도는 아니지만, 단단하고 균형 잡힌 체격과 불혹 언저리로 보이는 얼굴.

여기까지만 보면 무림 어디에서나 마주칠 법한 인상이다.

그러나 형형하다 못해 흉흉하게까지 느껴지는 안광(眼光)은, 낭인 시절부터 수많은 인간군상을 겪은 호위장조차 움찔하게 했다.

‘게다가 대머리.’

햇살을 받아 번쩍이는 중년인의 머리를 확인한 호위장은 위험을 직감했다.

그가 파악한 무림인이란 대체로 뭔가 중요한 것들이 결여된 존재들이었다.

마냥 근심 걱정 없고 행복하기만 한 사람이라면 무엇 하러 이 살벌한 풍진 강호에 몸을 내던지겠는가.

그리고 그런 의미에서 호위장의 기억 속에 존재하는 대머리의 무림인들은 유독 종잡을 수 없었다.

다른 무림인들처럼 마음속 무언가가 결여되어 있는 것은 똑같은데, 억울하게도 머리털까지 결여되어 있었으니까.

“마.”

“예?”

화들짝 놀란 호위장이 반사적으로 대답했다.

어느덧 하오체에서 존대로 뒤바뀐 말투는 호위장 자신도 알아채지 못할 만큼 자연스러웠다.

“너, 나 아냐?”

“모, 모릅니다.”

“그런데 왜 초면에 머리를 빤히 쳐다봐. 사람 기분 더럽게.”

초면에 놈놈거리는 것과 머리를 쳐다보는 것 중 무엇이 더 실례인지는 모르겠지만, 이미 위험을 직감한 호위장에게 남아 있는 선택지는 하나뿐이었다.

“죄, 죄송합니다.”

“웬 개뼈다귀 같은 놈이 다짜고짜 찾아와서 지랄인가 싶었는데…… 그나마 눈치는 있군.”

호위장은 내심 억울했다.

그는 중년인의 존재도, 신상도 알지 못했다. 이른 아침부터 말을 몰아 달려온 것은 다른 누군가를 만나기 위해서였다.

‘그런데 일이 왜 이렇게 된 거지? 처음부터 잘못된 정보였나?’

사천당가의 가주인 당사독의 허락하에 이루어진 자리다. 한데 만나려고 한 사람은 코빼기도 안 보이고, 맞은편에는 흉흉한 대머리가 자신을 빤히 노려보고 있다.

마치 잡아먹을 것처럼.

하지만 그것은 엄연히 호위장만의 생각이었다.

콧방귀를 뀐 중년인, 적천강은 깊게 가라앉은 눈빛으로 호위장을 응시하며 생각에 잠겨 있었다.

벌건 대낮부터 들이닥친 불청객들.

평소였다면 엉덩이부터 걷어찼겠지만, 관(官)의 인물이라면 이야기가 다르다. 더군다나 성주의 최측근 중 하나인 호위장이라면 더더욱.

‘찾아온 이유야 뻔하겠지.’

적천강도 눈이 있고 귀가 있다.

제아무리 주위 상황에 관심이 없어도 풍문은 익히 들었다. 두어 달 전부터 병상에 누워 있다는 성주에 관한 이야기 역시 그중 하나였다.

“신의(神醫)를 만나러 왔느냐?”

불쑥 던진 물음에 전전긍긍하고 있던 호위장이 눈을 크게 떴다.

지금 이 순간 그는 두 번 놀랐다.

황실이 나서도 찾지 못했던 신의가 정말 사천당가에 머무르고 있다는 사실에 한 번. 그리고 그 명망 높은 신의를 옆집 장삼이마냥 대수롭지 않게 부르는 적천강의 모습에 또 한 번.

“사실 반신반의하고 있었습니다만, 정말 이곳에 계신 겁니까?”

“싸가지를 소면에 말아 처먹은 놈이로고. 앞서 물은 것에나 답해라.”

“마, 맞습니다.”

“이유는? 성주의 병환 때문이냐?”

“예. 귀하께서도 이미 들어 보셨는지는 모르겠으나…… 성주님의 병환을 치료하기 위함입니다.”

“의원이라면 차고 넘칠 텐데?”

“그건…….”

호위장은 잠시 머뭇거렸지만, 망설임은 그리 길지 않았다.

눈앞의 중년인이 정확히 누구인지는 모르겠으나, 무림에서도 상당한 거물임이 분명했다.

사천당가의 가주가 주선한 자리에 아무렇지 않게 끼어드는 것부터가 심상치 않았다.

제아무리 사천당가가 큰 타격을 입었어도, 만독수라(萬毒修羅) 당사독의 권위에 도전하는 것은 배짱만으로 할 수 있는 미친 짓이 아니었으니까.

그리고 다음 순간 들려온 적천강의 한 마디는, 호위장을 천하에서 가장 솔직한 사람으로 만들어 주기에 충분했다.

“굳이 억지로 말하지 않아도 괜찮다. 어차피 정신없이 처맞다 보면 잊었던 기억까지 떠오를 테니까.”

“……!”

“이제 헛것까지 보이는구나. 아직도 주둥이가 닫혀 있는 걸 보면.”

수하들이 이 자리에 없다는 사실에 깊이 감사하며, 호위장은 냉큼 입을 열었다.

“성주님의 병환이 그만큼 깊습니다.”

“다섯 대.”

“예?”

“다섯 대짜리 대답이라는 뜻이다. 지금부터 제대로 된 대답이 나올 때마다 한 대씩 차감해 주지.”

미친놈인가?

눈 하나 까딱하지 않고 으름장을 놓는 적천강의 모습에, 호위장은 오금이 저렸다.

낭인 세계에서도 내로라하는 고수였던 자신이지만, 어째서인지 비슷한 연배로 보이는 눈앞의 중년인에게는 뼈도 못 추릴 것 같았다.

“자, 이제 어디 한번 제대로 씨부려 보거라.”

적천강이 한 손을 펼치자, 호위장이 목소리를 쥐어 짜냈다.

“세간에 알려진 것과는 많이 다릅니다. 이미 인근에서 내로라하는 명의(名醫)들도 두 손 두 발 다 들었을 정도지요.”

“그래서? 반드시 신의가 있어야 한다?”

“예. 이 정도로 노력을 기울였으면 최소한의 차도는 있어야 하는데, 점점 상태가 악화되고 있는 중입니다.”

“그 정도면 경각(頃刻)을 다투는 모양이군.”

“맞습니다. 한데…….”

바싹 마른 입술을 핥은 호위장이 조심스럽게 말을 이었다.

“성주께서 앓고 계신 병세가 조금, 아니 많이 희한합니다.”

“희한하다라…….”

작게 뇌까린 적천강이 손가락을 하나 접었다.

“네 대. 계속하거라.”

“어느 때는 의식이 또렷하고 거동도 할 수 있으신데, 또 어느 때는 광증(狂症)에 걸린 사람처럼 날뛰십니다.”

“그건 광증에 걸린 사람처럼 이 아니라, 광증에 걸린 것이 아니냐?”

“저 역시 처음에는 그렇게 생각했습니다. 황도(皇都)에 다녀오신 직후부터 뚜렷한 징후가 보였으니까요.”

“황도?”

“예. 넉 달 전 일어난 혈사(血史)에 관하여 조정의 부름을 받으셨습니다.”

사천혈사는 무림과는 아무런 연관도 없는 제삼자의 시선으로 보아도 엄청난 파란을 일으킨 대사건이었다.

제아무리 관과 무림이 불가침의 관계라 해도 그 여파가 미칠 수밖에 없을 만큼.

엄연히 대국의 영토인 사천에서, 그것도 무려 일만이 넘는 무림인들이 뒤얽혀 전투를 벌였다.

그 과정에서 무수한 이들이 죽거나 다쳤으며, 이후 시신들을 화장하는 연기는 사흘이 넘도록 사라지지 않을 정도였다.

“소문이 빠르게 퍼졌습니다. 성도에서도 그리 멀지 않은 곳에서 벌어진 일이었고, 이목들이 워낙 많았으니 당연한 일이었지요. 다만 가장 큰 문제는…….”

가만히 호위장의 말을 듣고 있던 적천강이 한 마디를 툭 내뱉었다.

“암천.”

“예. 그 과정에서 암천이라 불리는 자들이 관군으로 위장했다는 사실이 조정의 귀에 들어간 겁니다.”

“높은 것들이 단단히 화가 났겠군.”

“저도 무림에 몸담았던 몸이지만, 솔직히 어느 곳에서나 권위와 체면이 중요한 것 아니겠습니까.”

칼밥을 먹나 글밥을 먹나, 결국 사람이라는 점에서는 다를 바가 없다.

그런 의미에서 치열한 군웅할거의 시대를 거쳐 대국(大國)을 설립한 통일왕조의 체면과 권위는 결코 건드려선 안 되는 것이었다.

그런데 암천이 바로 그 권위에 손상을 입혔다. 백주 대낮에 관군으로 위장한 채 거리를 활보하고, 끝내는 끔찍한 학살극까지 일으키며.

‘그렇다는 건…….’

적천강은 머릿속에 뒤엉킨 생각을 정리하며 입을 열었다.

“생각했던 것 이상으로 흥미롭구나. 좋다, 세 대. 계속해 보거라.”

“황도에 다녀오신 뒤, 성주께서는 앓아누우셨습니다. 정확히는 사천으로 돌아오실 때부터 그러셨지요.”

“높은 놈들에게 제대로 탈탈 털린 모양이군.”

“조정의 질책도 질책이지만, 가장 아끼던 것을 황도에서 잃었기 때문입니다.”

“가장 소중한 것?”

“예.”

짤막하게 대답한 호위장이 지그시 적천강을 응시했다. 정확히는 아직 접히지 않은 그의 손가락 세 개를.

“……이런 영악한 놈을 봤나.”

“성주께서 괜히 저를 아끼신 게 아닙니다.”

“알았다. 두 개.”

“좀 더 쓰시지요. 한 개.”

“눈깔 한 개로 남은 여생을 보내고 싶으냐?”

“…….”

“알았다. 한 개.”

마지막 남은 손가락을 바라보며 마른침을 꿀꺽 삼킨 호위장이 입을 열었다.

“애첩입니다.”

“애첩?”

“예. 애향(愛香)이라고, 죽고는 못 살던 애첩이 있었습니다.”

“그 지랄 같은 상황에서 황도까지 데려갈 정도면 알 만하다. 그래서, 그 애첩을 길거리에서 잃어버리기라도 했단 말이냐?”

“아닙니다. 정확히 말씀드리자면 황도의 어느 높은 분께 빼앗겼지요.”

“성주의 애첩을 빼앗아 갈 만큼 높은 분이겠군. 누구냐?”

“그것이…….”

망설이는 호위장의 모습에, 적천강은 마지막 남은 손가락을 접었다. 그리고 생각지도 못한 대답을 듣고 눈을 부릅떴다.

“천자(天子)입니다.”
```

## Final English reading copy

```markdown
# Chapter 846

Dududududu!

More than twenty horsemen charged ahead without slowing.

The faces beneath their low-pulled helmets were tense. White foam had dried around the mouths of their panting horses, but the riders never once eased their reins.

Not until they reached their destination, surrounded by stone walls like a fortress.

And the first thing to greet them was a wary shout.

“Stop!”

It happened in an instant.

At the shout from atop the stone wall, a dozen or so arrows flashed through the air and pierced the edges of the horsemen’s helmets.

Shaaak! Thunk, thunk, thunk!

Their accuracy was almost supernatural, and their force tremendous.

The horsemen’s eyes wavered as they saw the arrows quivering where they’d struck the ground.

A mistake?

No. A warning.

It was also a threat: if they ignored the warning and came any closer, the arrows would pierce their throats instead of the edges of their helmets.

“Gasp…”

Sighs erupted from all around.

The more than twenty horsemen stopped where they stood as if on cue. They couldn’t hide their fear, but the man at their center was different.

*As expected. The reputation is well deserved.*

The man stared up at the stone wall, his gaze a mix of admiration and tension. A group stood there with their bows drawn, backlit by the early morning sun.

Above their heads fluttered a banner bearing four characters written in one fluid stroke.

Sichuan Tang Clan.

The Nine Sects and One Gang. The Five Great Families. Fifteen pillars that upheld the Murim of today.

And among them, the most insular and cunning of all.

But…

*He’s here. Right here.*

The man steeled himself and stepped forward alone. Instead of a sturdy shield to protect him from the arrows that could fly at any moment, he raised a silver token high above his head.

“Don’t attack! I’ve come from Seongju Prefecture!”

* * *

“Who did you say?”

“Hwang. I’m the City Lord’s Captain of the Guards.”

“The City Lord? Ah, that sickly fellow?”

“…I don’t know who you are, but you’d do well to watch your tongue.”

“If you don’t know who I am, you’re the one who should watch his tongue. You look like you’ve spent a fair bit of time in Murim. How have you not figured out something that simple?”

The man—the Captain of the Guards—swallowed hard before he even realized he was doing it.

He’d been spoken to in a thoroughly provocative manner, but he didn’t feel offended at all.

No, to be precise, the other man’s attitude and presence felt so natural that it seemed perfectly right.

*Who is this man?*

For a moment, the Captain of the Guards forgot his mission and studied the man in front of him.

He wasn’t quite a giant, but he had a solid, well-proportioned build and a face that looked around forty.

On its own, he looked like someone one might encounter anywhere in Murim.

But his gaze was so piercing it bordered on menacing. Even the Captain of the Guards, who’d seen all sorts of people since his days as a wandering martial artist, flinched.

*And he’s bald.*

The Captain of the Guards saw the middle-aged man’s scalp gleaming in the sunlight and sensed danger.

The martial artists he’d known were, for the most part, people with something important missing.

Why would anyone with a carefree, happy life throw himself into this brutal, turbulent martial world?

And in that regard, the bald martial artists in the Captain of the Guards’ memory were especially hard to read.

They were just as lacking in something inside as any other martial artist—but, unfairly, they were missing their hair, too.

“Hey.”

“Yes?”

The Captain of the Guards jumped and answered on reflex.

His speech had slipped from polite address into outright deference so naturally that even he hadn’t noticed.

“You know me?”

“N-no.”

“Then why are you staring at my head like that? It’s making me uncomfortable.”

It was hard to say which was ruder: calling someone “you” and “that bastard” the moment you met, or staring at his head. But for the Captain of the Guards, who’d already sensed danger, there was only one option left.

“I-I’m sorry.”

“Some stray mutt barges in out of nowhere, running his mouth… At least you know when to back down.”

The Captain of the Guards felt aggrieved.

He didn’t know the middle-aged man, or anything about him. He’d ridden hard since early morning to meet someone else.

*How did things go this wrong? Was the information bad from the start?*

This meeting had been arranged with the permission of Tang Sadok, Family Head of the Sichuan Tang Clan. But the person he’d come to meet was nowhere to be seen, and across from him stood a menacing bald man staring right at him.

As if he meant to eat him alive.

But that was all in the Captain of the Guards’ imagination.

The middle-aged man—Jeok Cheongang—snorted and fixed his gaze on the Captain of the Guards, his eyes sinking into thought.

Uninvited guests showing up in broad daylight.

Normally, he’d kick them out on their asses. But if they were officials, that changed things. Especially if one of them was the Captain of the Guards, one of the City Lord’s closest men.

*I can guess why they’re here.*

Jeok Cheongang had eyes and ears.

No matter how little he cared about what was going on around him, rumors still reached him. He’d heard the stories about the City Lord, who’d been confined to his sickbed for a couple of months.

“You came to see the Divine Physician?”

The Captain of the Guards, who’d been on edge, stared at him in surprise.

At that moment, he was startled twice.

First, that the Divine Physician, whom even the imperial court had failed to find, really was staying at the Sichuan Tang Clan. Then again, that Jeok Cheongang would refer to the renowned physician as casually as if he were some guy next door.

“I wasn’t sure whether to believe it, but is he really here?”

“What an ill-mannered bastard. Answer what I asked first.”

“Y-yes.”

“Why? Is it because the City Lord is ill?”

“Yes. I don’t know if you’ve already heard, but… We’re here to treat the City Lord’s illness.”

“Surely you have plenty of physicians.”

“That’s…”

The Captain of the Guards hesitated for a moment, but not for long.

He didn’t know exactly who the middle-aged man in front of him was, but he was clearly a major figure in Murim.

The fact that he’d casually inserted himself into a meeting arranged by the Family Head of the Sichuan Tang Clan was enough to raise questions.

No matter how badly the Sichuan Tang Clan had been struck, challenging Tang Sadok—the Myriad-Poison Asura’s—authority wasn’t something a man would do on a whim. It would be madness.

And then Jeok Cheongang spoke one sentence, enough to make the Captain of the Guards the most honest man in the world.

“You don’t have to force yourself to talk. Once you’ve been beaten senseless, you’ll start remembering things you’d forgotten.”

“…!”

“I must be seeing things. Your mouth still looks shut to me.”

Deeply grateful that his subordinates weren’t here, the Captain of the Guards hurriedly opened his mouth.

“The City Lord’s condition is that serious.”

“Five.”

“Pardon?”

“That answer was worth five hits. I’ll take one off for every proper answer you give from now on.”

Is this man insane?

The Captain of the Guards’ legs trembled as Jeok Cheongang threatened him without so much as blinking.

He’d been a well-known master among wandering martial artists, but for some reason, he felt like he wouldn’t stand a chance against the middle-aged man before him, who looked to be about his age.

“Now, go on. Spit it out properly.”

Jeok Cheongang held out one hand, and the Captain of the Guards squeezed his words out.

“It’s quite different from what people say. Even the renowned physicians nearby have given up.”

“So? You have to have the Divine Physician?”

“Yes. After all the effort we’ve put in, there should have been at least some improvement. Instead, his condition keeps getting worse.”

“Then it must be a race against time.”

“It is. But…”

The Captain of the Guards licked his dry lips and continued carefully.

“The City Lord’s illness is a little—no, very strange.”

“Strange…”

Jeok Cheongang murmured and folded one finger.

“Four. Keep going.”

“Sometimes he’s conscious and can move about, but at other times he thrashes around like someone who’s gone mad.”

“Isn’t that because he has gone mad, rather than being like someone who has?”

“I thought so at first, too. The clear symptoms started right after he returned from the Imperial Capital.”

“The Imperial Capital?”

“Yes. He was summoned to court over the Blood Tragedy that happened four months ago.”

The Sichuan Blood Tragedy had caused an enormous upheaval, even from the perspective of a third party with no ties to Murim.

The relationship between the authorities and Murim might have been one of noninterference, but its effects couldn’t help but spread.

In Sichuan, which was unquestionably part of the Great Nation’s territory, more than ten thousand martial artists had fought one another.

Countless people had died or been wounded in the fighting, and the smoke from the cremation of the bodies afterward had lingered for more than three days.

“The rumors spread quickly. It happened not far from Chengdu, and there were so many witnesses, so of course they did. But the biggest problem was…”

Jeok Cheongang, who’d been listening quietly, tossed out a single word.

“Dark Heaven.”

“Yes. The court learned that the people called Dark Heaven had disguised themselves as government soldiers.”

“The higher-ups must have been furious.”

“I used to be part of Murim myself, but honestly, don’t authority and saving face matter wherever you go?”

Whether you lived by the sword or by the pen, people were still people.

In that sense, the dignity and authority of a unified dynasty that had been established after an age of fierce warring states were things one simply did not touch.

And yet Dark Heaven had damaged that very authority. In broad daylight, they’d walked the streets disguised as government soldiers and ultimately carried out a horrific massacre.

*That means…*

Jeok Cheongang sorted through his tangled thoughts and spoke.

“This is more interesting than I expected. Fine. Three. Go on.”

“After returning from the Imperial Capital, the City Lord fell ill. To be exact, it started on his way back to Sichuan.”

“The higher-ups must have given him a thorough dressing-down.”

“The court’s reprimand was part of it, but he also fell ill because he lost what he cherished most in the Imperial Capital.”

“Something he treasured most?”

“Yes.”

The Captain of the Guards answered briefly, then stared intently at Jeok Cheongang. At his three fingers, to be precise.

“…You’re a crafty bastard.”

“The City Lord wouldn’t have favored me otherwise.”

“Fine. Two.”

“Give me a little more. One.”

“Want to spend the rest of your life with one eye?”

“…”

“Fine. One.”

The Captain of the Guards stared at the last finger still raised and swallowed hard before speaking.

“His favored concubine.”

“His favored concubine?”

“Yes. Her name was Aehyang. He couldn’t bear to be without her.”

“If he brought her all the way to the Imperial Capital in that damn situation, I can guess how attached he was. So what, did he lose her on the street?”

“No. To be precise, a high-ranking person in the Imperial Capital took her from him.”

“Must’ve been someone pretty important to take the City Lord’s concubine. Who?”

“Well…”

At the Captain of the Guards’ hesitation, Jeok Cheongang folded his last raised finger. Then, at the unexpected answer, his eyes widened.

“The Son of Heaven.”
```
