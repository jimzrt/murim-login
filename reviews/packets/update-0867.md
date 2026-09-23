<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0867.txt",
      "sha256": "5eee62b13c4494943f4d8702158d7919a090db590e29308ee6a0ccf470c51ab7",
      "bytes": 12931
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "8c72cb4c8435ee61f18b738b61852a9a4d736a14fae65737fdc644b39d77108e",
      "bytes": 1438
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "f990480d7090aa110383ec384ffc835ece1946f76ccca1e244240ed57ba826bf",
      "bytes": 229463
    },
    {
      "path": "characters/Baek Yeon.md",
      "sha256": "b19f0beed6b0a6bd286ea0818108f5b249aeb0093a1e0e61657dc4fa1f99aa5d",
      "bytes": 819
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "5c1a5d42630ffca2670d6d199705becfd12dc08255e53ff2f8c6c5433a08bcdc",
      "bytes": 759
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "271d8e4c27f2cbf0f5ce7e731a5e8d9ddb139ee814d5a1c0faf1b7a2158ce864",
      "bytes": 1782
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "b3ccb45344dd2d168a911958fce870756a1b9527e7c31a5754464837c8db9910",
      "bytes": 622
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "c609fae89a797441f7a632584451b60702336265530d16171f187a72d803e007",
      "bytes": 920
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "337fbd5979683a22d3e45562c9af0c9fc50fa54b7d10c11fa54bae123bd03181",
      "bytes": 255937
    }
  ],
  "estimated_tokens": 9943
}
-->

# Durable State Update — Chapter 867

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
1 and safe_through 867. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 867. Profile updates may replace only one
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
  "chapter": 867,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 867,
    "continuity_sources": [867],
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
    "Prince Shangshan and his party remain inside the imperial palace under surveillance; the Emperor postponed Shangshan’s audience until the next day.",
    "Baek Yeon helped the fourth prince seize the throne, betrayed the late Emperor and Crown Prince, and led a purge in which 30,000 people were arrested and killed.",
    "Hong Jin is devoted to protecting Shangshan and trusts Jin Taekyung to help keep him safe.",
    "Ma Sanbao, the East Depot’s second-in-command, has secretly remained in the palace loyal to the late Emperor and is now ready to act against the current ruler.",
    "Ma Sanbao and Hong Jin are longtime friends and allies; Ma’s secret intelligence about disguised Embroidered Uniform Guard members heading toward Shanxi helped Hong prepare before seeking Taekyung’s aid."
  ],
  "continuity_sources": [
    866
  ],
  "open_questions": [
    "What action do Ma Sanbao and Hong Jin intend to take against the current ruler, and when?",
    "What does the Emperor intend for Prince Shangshan, and why was his audience postponed?",
    "What happened between Hong Jin and the old eunuch, and why did Hong Jin leave the East Depot?"
  ],
  "safe_through": 866,
  "temporary_decisions": [
    "Render 동창 병필태감 as “Brush-Holding Eunuch of the East Depot.”",
    "Render 첩형 as “Constable” and 태감 as “Eunuch” in forms of address."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 일신     | **One God**         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 곰방대   | **long-stemmed tobacco pipe**                    |                                                       |
| 제자     | **Disciple**                                 |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 백연 | **Baek Yeon** | Commander of the Embroidered Uniform Guard. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 기관진식 | **mechanisms and formations** | Fifth preliminary assessment category. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 소하 | **Xiao He** | Historical civil official invoked in the same exchange. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 장성 | **Great Wall** | Wall used in the discussion of the Outer Lands. |
| 복마전 | **demon-slaying battleground** | A possible description for Sichuan if Dark Heaven attacks it. |
| 도산검림 | **a mountain of sabers and a forest of swords** | Idiom describing the lethal life of martial artists. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 화원 | **Fire Courtyard** | Courtyard associated with Jin Taekyung and Ju Hwaran's final walk before leaving Sichuan. |
| 궁인 | **palace attendant** | Former Inner Palace attendant expelled by Baeksang. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 주표 | visitor to prince | His Highness, Prince Shangshan | formal-deferential | Addresses Zhu Bao as 상산왕 전하 after kneeling to meet his gaze. |
| 주표 | 진태경 | prince to visiting young hero | Jin Taekyung | formal and inquisitive | Uses the formal second-person address before asking Taekyung's name and requesting an autograph. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 주표 | 백연 | prince addressing an imperial military officer | Commander Baek Yeon | formal and authoritative | Addresses Baek Yeon by name and office while insisting that he answer. |
| 백연 | 주표 | imperial officer addressing a prince | Your Highness | formal and deferential | Uses 전하 when apologizing to and answering Prince Shangshan. |
| 진태경 | 백연 | young martial artist confronting an imperial military commander | you | casual and insulting | Refers to Baek as 이 양반 while challenging his conduct. |

## Listed compact profiles

### Baek Yeon.md

# Baek Yeon (백연)

- **Safe through:** Chapter 866
- **Aliases:** Blood Envoy
- **Role:** Baek Yeon is the Commander of the Embroidered Uniform Guard, a former martial arts instructor to the Crown Prince, and the Blood Envoy who helped the fourth prince seize the throne and led the purge.
- **Personality:** Politically assured and controlled, he asserts imperial authority while tactically conceding the prince’s authority and enforcing protocol with ruthless decisiveness.
- **Voice:** Not established
- **Relationships:** He commands the Embroidered Uniform Guard and serves the Emperor; he orders Jeong Hogun to surveil Prince Shangshan’s party while leaving openings for an approach, and treats Taekyung as a dangerous potential obstacle.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 866
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 864
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; they trust each other deeply, though their bond remains unformalized. Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master; Ju Hwaran is a trusted Fire Dragon Pavilion member; Magic Johnson and Chuck Hagel are allied to him; his mother and sister Hayeon are among those he protects; the Skeleton King is his friend and ally; Xiao Shen regards him as an older brother; Jin-ho is his older friend and trusted confidant; he once saved Ju Wongong’s life.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 864
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 866
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is an early-adolescent member of the imperial family and an exceptionally skilled young swordsman who has trained daily for three years.
- **Personality:** Earnest and compassionate, he takes responsibility for his loyal subjects’ hardship, admires Jin Taekyung, seeks candid counsel, and shows composure beyond his years in the face of death and political danger.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s only younger full brother; the late Emperor entrusted Hong Jin with his care, and Zhu Bao admires Jin Taekyung and seeks to emulate him.

## Korean source

```text
＃867화



쿠르릉.

하늘이 울었다. 눈부신 낙뢰와 함께 쏟아져 내리는 폭우에 궁인(宮人)들의 움직임이 바빠졌다.

여러 환관과 궁녀들은 자신들이 모시는 후궁의 처소에 혹여 빗물이라도 샐까 하는 걱정에 종종걸음으로 달려갔고, 황궁 곳곳을 지키는 금의위들은 죽립을 눌러쓴 채 제자리를 지켰다.

황궁에 속한 모두에게는 각자의 역할이 있다.

자신에게 주어진 역할을 잘 수행한다면 상을, 그 반대라면 벌을 받는다.

그리고 쉼 없이 퍼붓는 빗물 속, 홀로 느긋하게 걸음을 옮기는 한 사내는 이 드넓은 황궁에서 상벌의 구애를 받지 않는 몇 안 되는 인물 중 하나였다.

아니, 오히려 그 반대에 가까웠다.

그에게는 천자의 재가(裁可) 없이도 다른 누군가에게 상벌을 내릴 수 있는 막강한 권한이 있었으니까.

하지만 황궁에서 일하는 궁인 중 그 누구도 감히 사내의 눈에 들기 위해 노력하거나 가까워지려 애쓰지 않았다.

심지어는 지금 이 순간에도 하염없이 쏟아져 내리는 저 빗물조차도.

솨아아아.

폭우 속을 거닐고 있음에도 사내의 전신에는 한 방울의 물기도 찾아볼 수 없었다.

제멋대로 흐트러진 반백의 머리카락은 바짝 메말라 있고, 기름 먹인 천으로 닦아 낸 황금빛 갑옷은 여전히 눈부신 광택을 뿜어냈다.

그것은 참으로 기이하고도 비현실적인 광경이었지만, 사내는 달랐다.

애초부터 그가 가진 것은 막강한 권력만이 아니었으니.

원초적인 힘.

인간의 한계를 아득히 뛰어넘은 일신의 무력.

비현실을 현실로 바꿀 수 있는 능력이 사내에게는 있었고, 중요한 만남을 앞둔 그는 자신의 몸이 젖는 것을 원치 않았을 뿐이었다.

우우웅.

웅혼한 공력에 대기가 파르르 떨렸다. 보이지 않는 막에 가로막힌 빗줄기는 이번에도 사내의 몸에 닿지 못한 채 사방으로 튕겨나갔다.

“요새 잠잠하다 싶더니…… 한바탕 제대로 퍼부어 대는군.”

낙뢰로 번쩍이는 하늘을 바라보며 중얼거린 사내는 잠시 멈추었던 걸음을 옮겼다. 거침없이 나아가는 그의 앞을 막아서는 이는 아무도 없었다.

과거에도 그러했고, 현재에도 그러하며, 앞으로도 그렇듯이.

철컥. 구구구궁.

그저 사내가 저 멀리서 모습을 드러내는 것만으로도 충분했다.

깊게 눌러쓴 죽립 아래로 예리한 눈빛을 흘리던 금의위들은 한 치의 망설임도 없이 굳게 닫혀 있던 문을 열고, 그가 지나갈 때까지 목례를 거두지 않았다.

보이지 않는 곳에서 묵묵히 자신의 역할을 수행하던 이들 역시 상황은 다르지 않았다.

“길을 터라.”

사내가 불쑥 내뱉은 한 마디에, 온갖 기화요초(琪花瑤草)로 가득했던 넓은 화원이 아지랑이처럼 일렁였다.

스아아아.

세찬 비바람 앞에서도 꼿꼿이 서 있던 이국(異國)의 나무와 꽃이 고개를 숙인다.

스르륵 움직이는 무성한 잎사귀와 가지들 사이로, 허락된 자만이 발을 디딜 수 있는 숨겨진 길이 열렸다.

아름다운 꽃에는 가시가 있다.

황궁의 화원 역시 다르지 않았다. 겉모습에 속아 함부로 발을 디딘 불청객은 무수한 기관진식(機關陣式)에 둘러싸여 벌집이 되고 만다.

아니, 비단 화원뿐만이 아니었다.

황궁은 그 자체로 온갖 위험이 득실거리는 복마전(伏魔殿)이자 진정한 의미의 도산검림(刀山劍林).

허락받지 않은 자는 죽음을 피할 수 없다.

설령 일신의 무위가 하늘에 닿은 이라 해도 절대 생사를 장담하지 못할 것이다.

사내는 다섯 개의 문과 수십에 이르는 전각을 가로지르며 그 사실을 다시 한번 깨달았고, 마침내 목적지에 이르러 걸음을 멈추었다.

건청궁(乾淸宮).

용사비등한 필체로 적힌 현판 아래, 철탑처럼 서 있던 두 중년인이 고개를 숙이며 인사를 건넸다.

“오셨습니까.”

“오셨습니까.”

마치 한 사람이 말하는 듯한 목소리와 표정.

거기에 더하여 같은 날, 한 배에서 태어났다는 것을 알려 주듯 서로를 쏙 빼닮은 이목구비까지.

쌍둥이인 그들은 사내를 향해 공손히 말을 이었다.

“잠시 기다려 주십시오.”

“잠시 기다려 주십시오.”

사내는 문득 눈살을 찌푸렸다. 지금껏 수없이 당부했음에도 같은 말을 동시에 하는 쌍둥이가 못마땅해서가 아니라, 그들의 몸에서 풍겨 오는 짙은 피비린내 때문이었다.

“선객이 있었던 모양이군.”

“예.”

“예.”

“죽였나? 배후는?”

“사로잡히기 직전에 스스로 목숨을 끊었습니다.”

“사로잡히기 직전에 스스로…….”

“그만. 한 번이면 족하다고 몇 번을 말했나. 그래서 침입자를 생포하지 못했다고?”

어찌해야 할지 모르겠는 표정으로 눈을 깜빡거린 쌍둥이가 작게 웅얼거렸다.

“극독을 숨기고 있었습니다. 어금니 아래에요.”

“극독을 숨기고 있었, 아니 최선을 다했지만 막지 못했습니다. 송구합니다.”

사내가 작게 혀를 찼다.

이곳까지 도달했다는 것부터가 침입자가 대단한 무위의 소유자라는 증거.

생포하여 배후를 알아내지 못한 것은 뼈아픈 실책이지만, 지금은 질책보다 중요한 것이 있었다.

“설마 궁 안까지 발을 디딘 것은 아니겠지.”

“그럴 리 있겠습니까.”

“그럴 리 있겠습니까.”

그나마 다행이군. 내심 중얼거린 사내는 재차 입을 열었다.

“안에 계신가?”

“기다리고 계십니다.”

“기다리고 계십니다.”

고개를 끄덕인 사내는 머리 위의 현판을 힐끗 바라본 뒤 걸음을 옮겼다.

건청궁. 건청. 맑은 하늘을 뜻하는 저 두 글자가 오늘만큼은 참 어울리지 않는다는 생각을 하면서.

저벅. 저벅.

궁 내부는 고요했다.

사람은 물론 쥐새끼 한 마리 보이지 않는 그곳에는 벽에 걸린 수많은 그림과 공예품들만이 흐릿한 불빛을 받아 번들거렸다.

그러나 보이는 것이 전부가 아니다.

사내는 걸음을 옮길 때마다 따라붙는 시선을 느꼈다. 상대가 누구든, 조금이라도 위협이 될 만한 자라면 언제든지 달려들어 자신의 전신을 난도질할 그림자들을.

그리고 어느덧 멈춘 그의 발걸음 끝에는, 오직 한 사람을 위해 마련된 거대한 공간과 그곳의 주인이 기다리고 있었다.

아니, 광활한 천하의 주인이.

“신, 금의위 지휘사 백연. 지엄하신 황제 폐하의 부름을 받고 왔나이다.”

그 순간.

사락.

사방에 드리워진 형형색색의 비단이 흔들렸다.

은은한 향을 머금은 채 곳곳에서 피어오르는 연기 속, 얇은 비단 사이로 눈부신 백의(白衣)를 걸친 누군가의 뒷모습이 비쳤다.

“왔는가.”

나직한 음성이 내부를 울렸다. 언뜻 들어보면 담담하면서도 나른한 목소리.

대국의 천자(天子)는 혼잣말처럼 천천히 말을 이었다.

“좋지 않은 꿈을 꾸었다. 다른 누군가가 과인을 해하려 하는 꿈을.”

“……!”

“그렇게 피를 뒤집어쓴 채 한참을 싸웠다. 그들은 어디에선가 끝없이 몰려왔고, 과인 역시 그들을 끝없이 베어 넘겼다. 그리고 마침내 깨어난 후에야 그것이 한낱 미몽(迷夢)이 아니었음을 깨달았다.”

말없이 고개를 든 사내, 백연은 천자의 입술 사이로 흘러나오는 희끄무레한 연기를 바라보며 입을 열었다.

“하여 또 다시 앵속(罌粟)에 손을 대신 겝니까.”

“그대는 이것이 앵속으로 보이는가?”

“송구하오나, 소신의 눈에는 틀림없이 그리 보입니다.”

“틀렸다. 이것은 앵속이 아닌 약이다. 과인을 치유해 줄 수 있는 유일한 것이지.”

그 순간, 백연의 눈썹이 꿈틀거렸다.

“폐하, 신이 긴히 한 말씀만 올려도 되겠습니까?”

천자는 대답하지 않았다. 그 대신 길고 넓은 소매를 펄럭였다.

스륵.

스치는 소리와 함께 주위를 에워싸고 있던 인기척이 썰물처럼 사라진 그때. 천자를 향해 굽혀져 있던 백연의 허리가 곧게 펴지고 서늘한 목소리가 흘러나왔다.

“대업(大業)의 완성이 코앞이거늘, 폐하께서는 어찌하여 이런 추태를 보이시오.”

만약 누군가가 이 자리에 있었다면, 자신의 눈을 가리고 귀를 막았을 것이다.

그만큼 백연의 어조는 군주를 대하는 신하가 보일 수 없는 날 선 것이었고, 무엄한 것을 넘어 도전적이기까지 했으니까.

그러나 천자는 이번에도 대답하지 않았다. 낮은 웃음소리를 흘리는 것으로 답을 대신한 세상의 주인은 한참의 시간이 흐른 후에야 불쑥 입을 열었다.

“대업이라, 그래. 대업이 있었지.”

“부디 잊지 마시오. 그날의 약조를.”

“잊어?”

천자가 실소하듯 중얼거렸다.

“과인은 잊지 않았다. 그날 이후 단 한시도 잊은 적이 없지.”

마치 병을 앓는 이처럼 힘없는 목소리.

그러나 천자를 바라보는 백연의 눈동자는 한 치의 흔들림도 없이, 동시에 깊숙이 가라앉아 있었다.

“이미 놈들이 움직이기 시작했소. 모든 것이 어그러지기 전에, 본래의 자리로 되돌려 놓아야 한다는 사실을 명심하시오.”

잠시 침묵하던 천자는 조용히 고개를 끄덕였다.

되돌리기에는 이미 너무나도 멀리 와 버렸다. 사 황자에 불과했던 그는 어느덧 광활한 천하를 다스리는 천자가 되었고, 앵속 따위에 의지할 수밖에 없는 몸이 되어버렸다.

광야를 달리는 말은 뒤돌아보지 않는다 했던가.

만인지상(萬人之上)의 위치에 오른 천자조차 예외는 아니었다.

그는 말이었다. 더는 자신의 의지로 멈출 수 없게 된, 피를 토하며 쓰러지더라도 목적지를 향해 내달려야 하는 한 마리의 말.

우두둑.

자연스럽게 힘이 들어간 손아귀에서 화려하게 치장된 곰방대가 부러진다. 천자는 손바닥 위에 놓인 그것을 물끄러미 바라보다, 이내 굳게 말아쥐었다.

푹.

손을 파고드는 거친 감촉과 불에 덴 듯한 통증. 그리고 아주 조금씩 깨어나는 정신.

“아.”

하늘에게 경배하듯, 천장을 향해 고개를 높게 들어 올린 천자는 눈 감은 채 신음했다.

무표정하게 그 광경을 지켜보던 백연이 물었다.

“어의를 불러드리리까.”

“필요 없다, 어의 따위.”

눈을 뜬 천자는 또렷해진 목소리로 말을 이었다.

“내일, 대전에서 그 아이를 만나겠다.”

“그 아이라면.”

“주표. 과인의…… 하나뿐인 동생이 얼마나 장성했는지 궁금하구나.”

백연이 고개를 끄덕였다.

“기대해도 좋을 거요. 폐하께서 기대하는 것 이상으로 장성하셨으니.”

“그만큼 더 위험해졌다는 뜻이군.”

“…….”

백연은 입을 굳게 다물었지만, 천자는 그 의미를 알고 있었다.

먹음직스러운 음식에는 온갖 벌레가 꼬이는 법.

상산왕 주표가 황도에 모습을 드러낸 이상, 그에게 불만을 품고 있던 적들은 소매 밑에 숨겨 두었던 칼날을 드러낼 것이 분명했다.

바로 오늘, 백연보다 앞서 이곳을 찾았던 이름 모를 암살자처럼.

“백연, 두 번 다시 오늘 같은 일이 벌어져서는 안 될 것이다. 명심하라.”

지금까지와는 다른, 얼음장처럼 서늘한 목소리에 멈칫한 백연이 희미하게 웃으며 대답했다.

“소신, 폐하의 말씀을 뼈에 새기겠나이다. 부디 지금까지의 불충함을 용서하소서.”

펄럭.

대답 대신 내저어진 천자의 소맷자락에, 백연은 천천히 뒤돌아서 걷기 시작했다.

그리고 불과 몇 걸음 만에 제자리에 멈춰 섰다.

“한데, 그자는 어떠한가?”

“그자라면…….”

“주표. 그 아이와 함께 온 무림인 말이다.”

열화신룡 진태경.

불현듯 떠오른 한 사람의 존재에 대해 곰곰이 생각하던 백연이 입을 연 것은 한참의 시간이 흐른 후였다.

“모르겠습니다.”

전장에서 수만을, 황궁에서 또 수만을 취조하고 죽였다.

그러나 그것이 백연이 할 수 있는 최선의 대답이었다.
```

## Final English reading copy

```markdown
# Chapter 867

*Rumble.*

Thunder rolled across the sky. As dazzling lightning flashed and torrential rain came pouring down, the palace attendants hurried about.

Eunuchs and palace maids scurried toward the quarters of the consorts they served, worried that rain might be leaking in somewhere. The Embroidered Uniform Guards stationed throughout the imperial palace stood their ground beneath their broad-brimmed hats.

Everyone who worked in the imperial palace had a role to play.

Do your job well, and you were rewarded. Fail to, and you were punished.

And in the relentless downpour, one man strolled at his leisure. He was one of the few people in this vast imperial palace who needn’t concern himself with rewards or punishments.

No—in fact, it was closer to the opposite.

He wielded such immense authority that he could reward or punish others without the Son of Heaven’s approval.

Yet not one palace attendant dared try to catch his eye or get close to him.

Not even the rain pouring ceaselessly down at that very moment.

*Whoosh.*

Though he walked through the downpour, not a drop of water touched the man.

His half-white hair, tousled as it pleased, was bone-dry. His golden armor, polished with oil-treated cloth, still gleamed brilliantly.

It was a strange, almost unreal sight, but the man was different.

After all, immense authority wasn’t all he possessed.

Raw power.

Martial prowess far beyond the limits of human ability.

He had the strength to make the unreal real. And with an important meeting ahead of him, he simply didn’t want to get wet.

*Vwoom.*

The air trembled before his profound internal energy. The rain struck an invisible barrier and ricocheted away in every direction, unable to touch him.

“It’s been quiet lately, but now it’s really coming down…”

Muttering as he looked up at the sky flashing with lightning, the man resumed his steps. No one dared stand in his way.

They hadn’t in the past. They didn’t now. And they never would.

*Clank. Rumble.*

The mere sight of the man approaching from afar was enough.

The Embroidered Uniform Guards peered out from beneath their deeply lowered hats. Without a moment’s hesitation, they opened the firmly shut gates and kept their heads bowed until he had passed.

The same was true of those quietly performing their duties out of sight.

“Open the way.”

At the man’s sudden command, the vast garden, filled with all manner of rare flowers and plants, shimmered like a heat haze.

*Whoosh.*

Even the foreign trees and flowers that had stood tall against the fierce rain and wind lowered their heads.

Thick leaves and branches stirred aside, revealing a hidden path where only those granted permission could set foot.

Beautiful flowers have thorns.

The imperial palace’s gardens were no different. An unwelcome guest who was fooled by their appearance and stepped inside recklessly would be surrounded by countless mechanisms and formations and riddled like a beehive.

And it wasn’t just the gardens.

The imperial palace itself was a den of countless dangers, a demon-slaying battleground and a mountain of sabers and a forest of swords in the truest sense.

Anyone without permission would die.

Even someone whose martial prowess reached the heavens could never be sure they would survive.

As the man passed through five gates and dozens of pavilions, he was reminded of that once more. At last, he reached his destination and stopped.

Qianqing Palace.

Beneath the signboard, its characters written in a bold, soaring hand, two middle-aged men stood like iron towers. They lowered their heads in greeting.

“You’ve arrived.”

“You’ve arrived.”

Their voices and expressions were as alike as if they were one person.

And their features were so strikingly similar that anyone would know they had been born of the same womb on the same day.

The twins continued, speaking politely to the man.

“Please wait a moment.”

“Please wait a moment.”

The man frowned. It wasn’t because he disliked the twins speaking in unison, despite his countless reminders not to. It was the strong smell of blood coming from them.

“Looks like you had a guest.”

“Yes.”

“Yes.”

“Did you kill him? Who was behind it?”

“He took his own life just before we could capture him.”

“He took his own life just before—”

“Enough. How many times have I told you that once is enough? So you failed to take the intruder alive?”

The twins blinked at him, looking unsure what to do, then mumbled under their breath.

“He had hidden a potent poison beneath one of his molars.”

“He had hidden a potent poison—no, we did everything we could, but we couldn’t stop him. We beg your forgiveness.”

The man clicked his tongue softly.

The fact that the intruder had made it this far was proof of his extraordinary martial prowess.

Failing to capture him and discover who was behind him was a painful mistake, but there was something more important than reprimanding the twins right now.

“Don’t tell me he got inside the palace.”

“Of course not.”

“Of course not.”

At least that was a relief, the man thought to himself, then asked another question.

“Is he inside?”

“He’s waiting.”

“He’s waiting.”

The man nodded, glanced up at the signboard above him, then stepped forward.

Qianqing Palace. Qianqing—“clear sky.” He couldn’t help thinking that those two characters were a poor fit for a day like this.

*Step. Step.*

The palace interior was quiet.

Not a person—or even a rat—could be seen. Only the countless paintings and works of art hanging on the walls glimmered in the faint light.

But there was more than met the eye.

With every step, the man felt eyes following him. Shadows poised to rush in and tear him apart the moment they sensed even the slightest threat, whoever he might be.

At the end of his path, he came to a stop. A vast space had been prepared for one person alone, and its master was waiting.

No—the master of all under heaven.

“I, Baek Yeon, Commander of the Embroidered Uniform Guard, have come at the summons of Your Majesty, the august Emperor.”

At that moment—

*Rustle.*

The colorful silk curtains draped around the room stirred.

Amid the smoke rising here and there, carrying a faint fragrance, the back of a figure dressed in dazzling white showed through the thin curtains.

“You’ve come.”

A quiet voice reverberated through the room. At first, it sounded calm and languid.

The Son of Heaven of the Great Nation continued slowly, as if speaking to himself.

“I had a bad dream. A dream that someone was trying to harm me.”

“……!”

“I fought for a long time, drenched in blood. They kept coming from somewhere, without end, and I kept cutting them down. Only when I finally woke did I realize it hadn’t been some idle dream.”

Baek Yeon raised his head in silence and looked at the pale smoke drifting from between the Son of Heaven’s lips.

“So you’ve turned to opium again.”

“Does this look like opium to you?”

“Forgive me, but that is exactly what it looks like to me.”

“You’re wrong. This isn’t opium. It’s medicine—the only thing that can heal me.”

At that, Baek Yeon’s brow twitched.

“Your Majesty, may I speak with you about something important?”

The Son of Heaven didn’t answer. Instead, he flicked his long, wide sleeve.

*Swish.*

With a faint rustle, the presences surrounding them withdrew like the tide. Baek Yeon straightened from his bow, his voice turning cold.

“Your Majesty, with the great undertaking nearly complete, why would you disgrace yourself like this?”

If anyone else had been there, they would have covered their eyes and ears.

Baek Yeon’s tone was far too sharp for a subject speaking to his ruler. It was more than insolent—it was defiant.

Yet the Son of Heaven didn’t answer this time, either. The ruler of the world gave a low laugh instead. Only after a long while did he suddenly speak.

“The great undertaking. Yes. There was a great undertaking.”

“Please don’t forget the promise from that day.”

“Forget?”

The Son of Heaven muttered with a short, incredulous laugh.

“I haven’t forgotten. I haven’t forgotten for even a moment since that day.”

His voice was as weak as that of a sick man.

But Baek Yeon’s eyes, fixed on the Son of Heaven, didn’t waver. They were sunk deep and steady.

“They’ve already begun to move. Before everything falls apart, remember that you must put things back where they belong.”

After a brief silence, the Son of Heaven nodded quietly.

It was already too late to turn back. He had been no more than the fourth prince, but now he ruled all under heaven. He had become a man who couldn’t help but rely on opium.

Did they say that a horse racing across the wilderness never looked back?

Even the Son of Heaven, who stood above all people, was no exception.

He was a horse. A horse that could no longer stop of its own will, that had to keep running toward its destination even if it collapsed, coughing up blood.

*Crack.*

His hand clenched instinctively, snapping the ornate long-stemmed tobacco pipe. The Son of Heaven stared at the broken pieces in his palm, then closed his fist tightly around them.

*Thump.*

The rough sensation digging into his palm. A pain like a burn. And, little by little, his mind began to clear.

“Ah.”

As if worshiping the heavens, the Son of Heaven tilted his head back toward the ceiling and groaned with his eyes closed.

Baek Yeon watched impassively.

“Shall I call for the imperial physician?”

“No need. Not for an imperial physician.”

The Son of Heaven opened his eyes and continued, his voice clearer now.

“Tomorrow, I’ll meet that child in the audience hall.”

“That child would be…”

“Zhu Bao. I wonder how much my… only younger brother has grown.”

Baek Yeon nodded.

“You can look forward to it. He’s grown even more than Your Majesty expects.”

“Which means he’s become even more dangerous.”

“……”

Baek Yeon pressed his lips together, but the Son of Heaven understood what that meant.

Wherever there’s a delicious meal, all sorts of bugs gather.

Now that Prince Shangshan Zhu Bao had appeared in the imperial capital, his enemies—those who resented him—would surely draw the blades they’d kept hidden beneath their sleeves.

Just like the nameless assassin who had come here before Baek Yeon today.

“Baek Yeon, this must never happen again. Remember that.”

The voice was different now, cold as ice. Baek Yeon hesitated, then answered with a faint smile.

“I will engrave Your Majesty’s words into my bones. Please forgive my disloyalty until now.”

*Flutter.*

In response, the Son of Heaven merely waved his sleeve. Baek Yeon turned and began walking away.

After only a few steps, he stopped.

“And what of that man?”

“If you mean…”

“Zhu Bao. The Murim martial artist who came with him.”

The Blazing Flame Divine Dragon, Jin Taekyung.

Baek Yeon thought carefully about the man who had suddenly come to mind. A long while passed before he spoke.

“I don’t know.”

He had interrogated and killed tens of thousands on the battlefield, and tens of thousands more in the imperial palace.

But that was the best answer Baek Yeon could give.
```
