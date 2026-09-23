<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0872.txt",
      "sha256": "431ac8aa82f25777219ea2fb236d5de1561942da4837de2baec1809a1c9fa53e",
      "bytes": 12911
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ae3a16d6d5dcaf16c252fab058b3bd80e5d7d896c7c390e2c088f5448a69f53c",
      "bytes": 1543
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "3291b7833512bf663761c7378a7587b0bd5178a4c5aa15c6bd322bfc5ce0ac8f",
      "bytes": 229780
    },
    {
      "path": "characters/Baek Yeon.md",
      "sha256": "632cb5786137cfeedec258498041f8769724ffd5e88a202ed820969c0a282eb9",
      "bytes": 983
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "ae914477c595c0b6a4e7e174194570fae8fa3d8b6488441c25c43720b7e07299",
      "bytes": 759
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "a218a0b60ebb69175bb9744e82be7effce151181ba8629ad945a611d85835221",
      "bytes": 854
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "2a12b91e4fdb63061fb4fc58cf8ad66ae5dd3dbf3af0ba2b94cc690cb8aabc61",
      "bytes": 765
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "dcdc21d08fa28bd3371dd38f908bdfbc35632f6a14dcc0e2ea8d022e846facc0",
      "bytes": 920
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "53d6a127d30cdd906f56ad2abe13909beebdcad7686fde9662e186345021a814",
      "bytes": 257123
    }
  ],
  "estimated_tokens": 10121
}
-->

# Durable State Update — Chapter 872

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
1 and safe_through 872. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 872. Profile updates may replace only one
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
  "chapter": 872,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 872,
    "continuity_sources": [872],
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
    "Taekyung and Prince Shangshan have reached the Emperor’s bedchamber; their gaunt Supreme Peak guide is alone there and says he enjoyed a brief diversion.",
    "The guide’s identity and what happened to the Emperor are unknown.",
    "Taekyung is moved by Shangshan’s fear and is unsure he could leave the boy if forced to choose between rebellion and submission.",
    "Taekyung’s System and Inventory remain unavailable during the update, and his condition worsens without the Divine Physician’s pills.",
    "Ma Sanbao secretly remained in the palace, leads a group seeking to enthrone Prince Shangshan, and offered Taekyung a reward for helping; Taekyung has not accepted.",
    "Hong Jin left the East Depot to serve Prince Shangshan, while Ma Sanbao stayed behind."
  ],
  "continuity_sources": [
    870,
    871
  ],
  "open_questions": [
    "Who is the gaunt Supreme Peak guide, and what does he mean by having enjoyed a diversion?",
    "Where is the Emperor, and what does he intend for Prince Shangshan and Taekyung?",
    "Who are the twin Supreme Peak masters, and why have they blocked the procession?",
    "Will Taekyung agree to help Ma Sanbao enthrone Prince Shangshan, and what would the plan require?",
    "What does Ma Sanbao know about Dark Heaven, and what reward is he offering?"
  ],
  "safe_through": 871,
  "temporary_decisions": [
    "Render 흠천감 as “Imperial Astronomical Bureau.”",
    "Render 형부 as “Ministry of Punishments.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 살성     | **Slaughter Saint**           | —              |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 큰형     | **eldest brother**                           |
| 산서     | **Shanxi**             |
| 백연 | **Baek Yeon** | Commander of the Embroidered Uniform Guard. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 선황 | **the late Emperor** | The former Emperor whom Hong Jin served. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 근골 | **Muscles and Bones** | System attribute increased by 2 during the climb. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 인자 | **ninja** | Japanese assassin skilled in concealment and concealed weapons. |
| 은잠술 | **concealment technique** | Technique used by Hidden Shadow Pavilion agents to hide their presence. |
| 심해 | **deep sea** | Unexplored ocean depths where the ancient monster awakens. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 태조 | **Taizu** | The Great Nation’s founding emperor. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |
| 건청궁 | **Qianqing Palace** | The Emperor's palace, where Baek Yeon meets him. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 홍진 | 주표 | servant and political aide to prince | His Highness | formal-deferential | Uses the elongated royal call 전하 while summoning Zhu Bao. |
| 주표 | 홍진 | prince to loyal subject | you | formal and reassuring | Zhu Bao refers to Hong Jin as 그대 while apologizing for the hardship he has endured. |
| 주표 | 백연 | prince addressing an imperial military officer | Commander Baek Yeon | formal and authoritative | Addresses Baek Yeon by name and office while insisting that he answer. |
| 백연 | 주표 | imperial officer addressing a prince | Your Highness | formal and deferential | Uses 전하 when apologizing to and answering Prince Shangshan. |
| 홍진 | 백연 | imperial aide confronting a senior military officer | you | angry and confrontational | Uses 당신 in an indignant outburst. |
| 홍진 | 마삼보 | Longtime friend and former East Depot cohort | Ma Constable; Eunuch Ma | Familiar and respectful | Hong uses both forms while acknowledging Ma’s former and current standing. |
| 마삼보 | 홍진 | Longtime friend and former East Depot cohort | Hong Constable | Familiar and respectful | Ma addresses Hong by his former East Depot title. |
| 백연 | 천자 | imperial officer addressing the Emperor | Your Majesty | formal, deferential in address but openly defiant in private counsel | Baek uses formal honorifics while sharply confronting the Emperor over their shared undertaking. |
| 천자 | 백연 | Emperor addressing his military commander | Baek Yeon | familiar and authoritative | The Emperor addresses Baek by name and gives him a direct warning. |
| 중년인 | 상산왕 | unknown imperial subject addressing a prince | His Highness, Prince Shangshan | formal and deferential | Addresses him as 상산왕 전하 while remarking on seeing him grown. |

## Listed compact profiles

### Baek Yeon.md

# Baek Yeon (백연)

- **Safe through:** Chapter 871
- **Aliases:** Blood Envoy
- **Role:** Baek Yeon is the Commander of the Embroidered Uniform Guard, a former martial arts instructor to the Crown Prince, and the Blood Envoy who helped the fourth prince seize the throne and led the purge.
- **Personality:** Politically assured and controlled, he enforces authority with ruthless decisiveness but speaks with striking defiance to the Emperor in private when their shared undertaking is at stake.
- **Voice:** Not established
- **Relationships:** He commands the Embroidered Uniform Guard and serves the Emperor; they share an old promise tied to a great undertaking, and Baek urges the Emperor to restore matters before their adversaries' moves unravel it. He orders Jeong Hogun to surveil Prince Shangshan’s party while leaving openings for an approach, and treats Taekyung as a dangerous potential obstacle.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 870
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 871
- **Aliases:** None
- **Role:** Hong Jin is a Level 22 Deputy Military Commissioner of Shanxi Province, a eunuch and trusted aide to Prince Shangshan, and a former member of the East Depot.
- **Personality:** Composed, socially deft, and ambitious, Hong Jin became a eunuch to escape poverty and save his family, then used his abilities to pursue a broader life.
- **Voice:** Delicate and deferential, using formal, self-effacing language with Prince Shangshan.
- **Relationships:** Hong Jin is devoted to Prince Shangshan, whom the late Emperor entrusted to his care, and trusts Jin Taekyung to help protect him; he left the palace to serve the prince, while his longtime friend and former East Depot cohort Ma Sanbao stayed behind.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 871
- **Aliases:** None
- **Role:** Ma Sanbao is the East Depot’s Brush-Holding Eunuch and second-in-command, a Supreme Peak martial artist who has secretly remained in the imperial palace.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks casually and directly with longtime companions, while remaining alert and controlled with new acquaintances.
- **Relationships:** Ma Sanbao is a longtime friend and former East Depot cohort of Hong Jin; he stayed behind to await Prince Shangshan's return and is leading a group seeking to enthrone him.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 871
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is an early-adolescent member of the imperial family and an exceptionally skilled young swordsman who has trained daily for three years.
- **Personality:** Earnest and compassionate, he takes responsibility for his loyal subjects’ hardship, admires Jin Taekyung, seeks candid counsel, and shows composure beyond his years in the face of death and political danger.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s only younger full brother; the late Emperor entrusted Hong Jin with his care, and Zhu Bao admires Jin Taekyung and seeks to emulate him.

## Korean source

```text
＃872화



“짧은 여흥이었으나, 제법 즐거웠다.”

그 한마디를 듣는 순간, 나는 등골을 타고 찌르르 울리는 전율을 느꼈다.

아무리 생각해도 알 수 없었던, 중년인의 정체를 비로소 깨달았기 때문이었다.

‘천자(天子)……!’

천하를 다스리는 대륙의 지배자.

지금으로부터 십여 년 전, 황도를 피로 씻으며 옥좌에 올랐던 역모의 주인공.

나는 눈을 부릅뜨며 눈앞의 중년인, 아니 황제를 바라보았다.

‘어떻게?’

이 모든 상황이 그의 신분을 증명하고 있음에도 그러한 의문이 떠오르는 것은, 이미 알고 있던 정보 때문이었다.

‘분명 아직 불혹(不惑) 어림의 나이일 텐데.’

젊고 야심만만했던 대국의 사 황자가 역모를 일으켰을 당시 그의 나이는 불과 이십 대 후반.

그로부터 십 년이 조금 넘는 시간이 흐른 지금은 기껏해야 불혹. 즉 마흔에 접어들었다고 봐야 한다.

그런데…….

‘아무리 좋게 봐줘도 오십 줄은 넘어 보여.’

단순히 노안(老顔)이라고 치부하기 어렵다.

뙤약볕 아래서 농사만 짓는 촌 무지렁이도 아닌 만인지상의 황제가, 거기에 더해 초절정의 경지에 오른 고수가 어찌 이렇게 겉늙을 수 있단 말인가.

그에 비하자면 대국의 황제가 초절정 고수라는 사실에서 받은 충격은 그리 크지 않았다.

사 황자로 불리던 시절, 뛰어난 무재(武才)를 바탕으로 숱한 군공을 세웠다는 황제였으니까.

하지만 그 사실 역시 예상을 벗어나기에는 마찬가지.

나는 불현듯 한 사람의 존재를 떠올렸다.

마삼보. 동창의 이 인자이자 지난 십여 년간 황제의 수족 노릇을 하며 역심(逆心)을 숨겨 온 그를.

‘그는 이 사실을 알고 있었을까?’

스스로에게 던진 의문에 대한 답은 순식간에 나왔다.

마삼보가 이 사실을 알고 있었다면 진작 알려 주었을 터.

따라서 결론은 하나밖에 없었다.

‘마삼보조차 몰랐다. 아니, 황제가 의도적으로 숨겼다고 해야 정확하겠지.’

순간 등골이 서늘해졌다. 전날 밤 마삼보와 나누었던 대화 중 일부가 섬광처럼 뇌리를 스쳤기 때문이었다.



‘황제는 음험하고 심계가 깊은 자일세. 십 년이 넘는 세월이 흘렀음에도 금의위로 하여금 동창을 견제하고 있는 것만 봐도 알 수 있지.’

‘하지만 동창도 황제의 수족이 아닙니까?’

‘맞네. 정확히는 선황(先皇) 폐하의 수족이었지만.’

‘……!’

‘권력자들의 공통점이 무엇인지 아나? 그들은 의심하고 또 의심해. 현 황제와 백연이 어떻게 손을 잡았는지는 아직도 알아내지 못했으나, 금의위가 주도한 역모가 성공한 이후부터 동창은 계륵(鷄肋)과 같은 존재였네. 황제는 건청궁에서 모든 업무를 처리하며 이미 수년째 두문불출하는 중이지.’

‘건청궁?’

‘황제의 거처일세. 그럴 가능성은 거의 없겠지만…… 만약 자네가 황제를 대면하는 상황이 된다면, 짧은 대답 하나에도 신중을 기하고 몸가짐을 조심하도록 하게.’



말이 이 인자지, 사실상 동창의 수장이라 할 수 있는 마삼보에게조차 진실을 숨긴 황제다.

한데 왜, 도대체 무슨 이유로 내게는 이런 자신의 모습을 드러낸 것일까.

지금으로서는 무엇 하나 확신할 수 없었으나, 적어도 그날 마삼보에게 들었던 정보 중 일부는 정확했다.

황제는 음험하고 심계가 깊은 자였다.

지금 이 순간, 내 마음속을 꿰뚫어 보는 듯한 저 눈빛만으로도 그 사실을 깨달을 수 있을 만큼.

“하하. 어지간히 놀란 모양이군.”

입꼬리는 올라가 있지만, 눈은 아니다.

굳어 버린 내 모습에 소리 내어 웃던 황제가 문득 낮게 깔린 목소리로 말을 이었다.

“왜. 지금 짐의 모습이, 다른 누군가에게 들었던 것과는 많이 달라서 그런 것이냐?”

“……!”

순간 숨이 턱 막혔다. 삽시간에 무거워진 주위의 공기 너머로 황제의 의중이 고스란히 전해진다.

‘나를…… 의심하고 있다.’

하지만 이럴 때일수록 침착해야 한다. 나는 그런 마음을 내색하지 않으려 애쓰며 대답했다.

“그렇습니다.”

“뭐라?”

“사실 홍진, 아니 산서성 도지휘동지에게 이미 몇 가지 이야기를 들었습니다.”

“홍진, 홍진이라. 오랜만에 듣는 이름이군.”

잠시 옛 기억을 추억하듯, 허공을 응시하던 황제가 날카롭게 빛나는 눈빛으로 내게 시선을 돌렸다.

“그래, 그가 뭐라 했지?”

“일찍이 무(武)로 두각을 드러내셨고, 이립도 되지 않은 젊은 나이에 황위를 얻으셨다 했습니다.”

“그리고?”

“그게 전부입니다.”

“그럴 리가 없을 텐데?”

물론 그게 끝이 아니다.

하지만 피붙이까지 죽여 가며 황위에 오른 장본인 앞에서 ‘존나 씹새끼라던데요.’ 같은 말을 어떻게 하겠나.

그렇다고 이대로 뚝 잡아떼기에도 뭐하다.

홍진은 상산왕을 맡길 만큼 선황이 아끼던 충복이고, 그런 자가 자신에 대한 감정이 좋을 리 없다는 것쯤은 황제도 진작 알고 있을 테니까.

결국 나는 황제의 의심을 피하면서, 동시에 홍진이 금의위에 붙잡혀 가지 않을만한 대답을 찾아내야 했다.

문제는 이게 통하냐는 건데…….

‘시벌, 모르겠다.’

이럴 때는 눈 딱 감고 질러야 하는 법.

나는 마른침을 꿀꺽 삼키며 입을 열었다.

“사실 더 말해 준 게 있긴 합니다만.”

“말하라.”

“그게, 제 입으로 말씀은 못 드리겠습니다.”

“뭐라?”

“정 궁금하시면 나중에 직접 불러서 물어보시는 편이…….”

말꼬리를 흐린 그 순간.

쉬쉬쉬쉭!

날 선 바람이 사방에서 휘몰아쳤다. 아무것도 없는 허공에서 뚝 떨어져 내린 수십의 흑의인들은 나를 에워싼 채 손에 든 각각의 무기를 들이밀었다.

스륵.

처음부터 의도한 것일까. 아니면 황제를 향한 충심에서 비롯된 분노였을까.

예리한 날붙이에 베인 살갗에서 몽글몽글 피어오른 핏방울이 목덜미를 타고 굴러떨어진다.

‘이놈들…… 진심이다.’

주위를 빈틈없이 에워싼 흑의인들로부터 마치 가축을 도살하는 백정처럼 무감각한, 그러나 명령이 떨어지는 즉시 죽이겠다는 필사(必死)의 의지가 느껴진다.

동시에 옷소매를 강하게 움켜잡는 손길도 함께.

꾸욱.

상산왕 주표.

중년인의 정체가 황제였다는 사실이 밝혀진 그 순간부터 얼어붙어 있던 어린 왕을 향해, 나는 안심하라는 듯 미소지었다.

그리고 말없이 그 모습을 바라보던 황제가 불현듯 풍성한 소매를 떨쳤다.

펄럭.

나부끼는 옷자락과 함께 무기를 거둬들인 흑의인들이 허공으로 솟구쳤다.

희미한 인기척만 남긴 채 처소 곳곳으로 녹아들 듯 사라지는 은잠술은 가히 신기(神技)에 가까웠다.

“다들 충성심이 대단하군요.”

이번만큼은 비꼬는 것이 아니다.

내 순수한 감탄에 황제가 건조한 목소리로 대꾸했다.

“충성심만 대단한 것은 아니지. 그대와 가까운 사이인 살성(殺星)만큼은 아니겠지만.”

“……!”

“왜, 그 정도도 모를 줄 알았더냐?”

나는 잠시 침묵했다. 이번만큼은 진심으로 놀랐기 때문이다.

살성이라는 별호는 천하에 모르는 사람이 없지만, 오래전 자취를 감춘 그가 다시 모습을 드러냈다는 사실을 아는 이들은 그야말로 극소수.

그런데 황제는 살성의 존재는 물론이고, 나와 인연이 있다는 것까지 파악하고 있었다.

천하에 펼쳐놓은 광활한 정보망을 이용했음이 틀림없다.

“금의위가 전한 정보입니까?”

침묵 끝에 흘러나온 내 물음에, 황제의 낯빛 위로 불쾌함과 흥미가 뒤섞였다.

“담대하기가 이를 데 없는 놈이로군. 감히 짐에게 그런 것을 묻다니.”

앞선 상황은 어떻게든 넘어갔다 치더라도, 더 이상 황제의 심기를 거슬러서 좋을 게 없다.

보이지 않는 선을 직감한 나는 고개를 숙였다.

“죄송합니다.”

“황공하옵니다.”

“예?”

“죄송한 것이 아니라, 황공해야 한다는 말이다. 짐을 대하는 모두가 그렇게 하는 것처럼.”

황공(惶恐)이라는 두 글자는 각각의 의미로 따져보아도 두렵다는 뜻이다.

그야말로 무소불위의 절대자인 황제의 권위를 엿볼 수 있는 최고의 경어.

말이 끝난 후에도 뚫어져라 나를 응시하는 황제의 모습에, 나는 재차 입을 열었다.

“황공하옵니다.”

“그나마 낫군. 강호의 무뢰배이니 부족함은 어쩔 수 없지만, 지금부터라도 하나하나 배워 가면 될 것이다.”

황제의 주름진 입가에 흐릿한 웃음이 번지는 것을 보니 위장이 뒤틀리는 듯한 기분이다.

하지만…….

‘우선은 살아남아야 한다.’

지금 위험에 처한 것은 나뿐만이 아니다. 내 말 한마디, 행동 하나하나에 모두의 목숨이 걸려 있다.

파르르 떨리는 손길로 내 옷소매를 꼭 움켜잡고 있는 이 어린 왕도 포함해서.

그리고 바로 그때, 줄곧 무심하던 황제의 눈길이 마침내 하나뿐인 동생에게 닿았다.

“이리 오너라.”

그 한 마디에, 옷자락을 통해 전해지던 떨림이 우뚝 멎었다.

침착함을 되찾은 것이 아니다. 황제는 마치 석상처럼 굳어 버린 상산왕을 향해 낮은 목소리로 말을 이었다.

“짐으로 하여금 두 번이나 말하게 만들 셈이냐.”

“……!”

떨리는 눈빛으로 황제를 바라본 상산왕이 고개를 들어 나를 올려다보았다.

그리고 거친 심호흡과 동시에 옷소매를 쥔 손을 놓고 황제를 향해 걸음을 옮겼다.

아니, 오체투지(五體投地)하며 절했다.

“시, 신. 상산왕 주표가 형님 폐하를 뵈옵니다.”

잠시. 혹은 어쩌면 꽤 오랫동안 무거운 침묵이 내려앉았다.

도무지 의중을 짐작하기 어려울 만큼 깊게 가라앉은 눈빛으로, 더불어 한참 어린 막냇동생을 대하는 것이라고는 믿어지지 않을 만큼 차가운 얼굴로 상산왕을 내려다보던 황제가 문득 입을 열었다.

“올해 나이가 몇이냐.”

“여, 열둘이옵니다.”

“근골이 제법이다. 무공을 수련했더냐?”

“예.”

“우리 형제는 늘 어릴 적부터 무공에 몰두했었지. 다만 큰형님만큼은 문관(文官)에 가까웠다.”

상산왕은 작게 숨을 삼켰다. 어느 정도 자라기 시작하면서부터 홍진에게 이런저런 이야기를 들었을 테지만, 하나뿐인 형에게 듣는 가족사는 그 의미가 남다른 법이었다.

그 하나뿐인 형이, 평범한 형제로 대할 수 없는 대국의 황제이자 가족들을 죽음으로 몰아간 원수라면 더더욱.

“그렇……습니까.”

“조부이신 태조 역시 무(武)로 대국을 일으켰으니 이 역시 황가의 전통. 너를 보니 본래 핏줄은 타고나는 것이 맞는 듯하구나.”

황제가 건조한 음성으로 덧붙였다.

“그것이 독이 될지, 득이 될지는 모르겠지만.”

“……!”

“……!”

나는 입술 밖으로 흘러나오려는 침음성을 간신히 억눌렀다.

황도에 도착하기 전부터 이미 황제의 의중이 결코 호의적이 아니라는 것쯤은 짐작하고 있었지만, 그럼에도 불구하고 황제가 상산왕을 향해 보인 반응은 너무나도 노골적이었다.

‘그 정도로 경계하는 건가? 한참이나 어린 동생을?’

권력은 비정하다.

얼마 안 되는 재산을 두고 부모 형제와도 아귀다툼을 벌이는데 거대한 대륙, 하나의 제국이라면 어떻겠나.

하지만 그렇다 해도 고작 열두 살밖에 되지 않은 막냇동생을 향한 황제의 경계는 너무나도 철저했고, 한편으로는 정확하기도 했다.

마삼보를 필두로 이미 역모를 꿈꾸는 이들이 나타나고 있었으니.

그리고 다음 순간 이어진 황제의 한 마디는, 그의 경계심이 이미 돌이킬 수 없는 지경에 이르렀다는 명백한 증거나 다름없었다.

“지금부터는, 짐이 널 보살펴 주겠다.”

“……!”
```

## Final English reading copy

```markdown
# Chapter 872

“It was a brief diversion, but I enjoyed it.”

The moment I heard those words, a shiver ran down my spine.

At last, I’d figured out the middle-aged man’s identity. No matter how hard I’d tried, I hadn’t been able to place him before.

*The Son of Heaven…!*

The ruler of the continent, who governed all under heaven.

The man who’d seized the throne in a coup after bathing the imperial capital in blood a little over ten years ago.

I stared wide-eyed at the middle-aged man before me—no, at the Emperor.

*How?*

Even though everything that had happened proved who he was, that question still sprang to mind. It was because of what I already knew.

*He should still be somewhere around forty, shouldn’t he?*

When the young, ambitious fourth prince of the Great Nation launched his coup, he’d been no older than his late twenties.

A little over ten years had passed since then. At most, he should have just turned forty.

And yet…

*Even being generous, he looks over fifty.*

It was hard to write it off as mere premature aging.

How could the Emperor, the person above all others—not some country bumpkin who’d spent his life farming under the blazing sun—look this old? And on top of that, he was a master who’d reached Supreme Peak.

By comparison, the fact that the Emperor of the Great Nation was a Supreme Peak master wasn’t all that shocking.

Back when he was known as the fourth prince, he’d earned many military merits thanks to his exceptional martial talent.

Even so, that fact had also defied my expectations.

Suddenly, I thought of someone.

Ma Sanbao. The East Depot’s second-in-command, who’d spent the past decade and more serving as the Emperor’s right hand while hiding his own rebellious ambitions.

*Did he know about this?*

The answer to my question came instantly.

If Ma Sanbao had known, he would have told me long ago.

So there could only be one conclusion.

*Even Ma Sanbao didn’t know. No—that’s not quite right. The Emperor must have deliberately kept it hidden.*

A chill ran down my spine. Part of my conversation with Ma Sanbao the night before flashed through my mind.



‘The Emperor is a sinister man, and deep in his schemes. You can see it in how he still has the Embroidered Uniform Guard keeping the East Depot in check, even after all these years.’

‘But isn’t the East Depot also the Emperor’s right hand?’

‘Yes. More precisely, it was the late Emperor’s right hand.’

‘…!’

‘Do you know what all powerful people have in common? They’re suspicious. And then they’re suspicious some more. I still haven’t figured out how the current Emperor and Baek Yeon joined forces, but after the coup led by the Embroidered Uniform Guard succeeded, the East Depot became something the Emperor had little use for but couldn’t simply discard. He handles all his duties from Qianqing Palace and has been keeping to himself for years.’

‘Qianqing Palace?’

‘The Emperor’s residence. It’s almost impossible, but…if you ever find yourself face-to-face with him, be careful with your manners and think before you give even a short answer.’



The Emperor had hidden the truth even from Ma Sanbao, who was nominally the East Depot’s second-in-command but was, in practice, its leader.

So why—why on earth had he shown me this side of himself?

I couldn’t be certain of anything just yet, but at least some of what Ma Sanbao had told me that day was right.

The Emperor was sinister and deep in his schemes.

I could tell from the way he looked at me now, as if he could see straight into my heart.

“Ha ha. You look rather surprised.”

The corners of his mouth were raised, but not his eyes.

The Emperor had laughed aloud at my frozen expression, then continued in a low voice.

“Why? Is this quite different from what someone else told you about me?”

“……!”

For a moment, I couldn’t breathe. Through the air that had suddenly grown heavy around us, I could sense the Emperor’s intentions all too clearly.

*He suspects me…*

But now, more than ever, I had to stay calm. I tried not to let it show and answered him.

“Yes.”

“What?”

“I’ve already heard a few things from Hong Jin—or rather, the Deputy Military Commissioner of Shanxi Province.”

“Hong Jin, Hong Jin. It’s been a long time since I heard that name.”

The Emperor gazed into empty space as if reminiscing about old memories. Then he turned his sharp, shining eyes on me.

“So, what did he say?”

“He said Your Majesty distinguished yourself in martial arts early on and gained the throne at a young age, before you’d even turned thirty.”

“And?”

“That was all.”

“That can’t be all.”

Of course, it wasn’t.

But how was I supposed to say, “He said you were a fucking bastard,” right in front of the man who’d risen to the throne by killing even his own blood relatives?

Still, I couldn’t deny everything outright.

Hong Jin was a loyal retainer the late Emperor had cherished enough to entrust with Prince Shangshan’s care. The Emperor must have known long ago that someone like him wouldn’t have warm feelings toward him.

In the end, I had to come up with an answer that would keep the Emperor from suspecting me without getting Hong Jin hauled off by the Embroidered Uniform Guard.

The question was, would that even work…

*Fuck, I don’t know.*

At times like this, you just had to close your eyes and take the plunge.

I swallowed dryly and spoke.

“Actually, he did tell me more.”

“Speak.”

“Well, I can’t bring myself to say it myself.”

“What?”

“If you’re really curious, perhaps you could summon him later and ask him directly…”

The instant my voice trailed off—

Whoosh! Whoosh! Whoosh!

Sharp winds swept in from every direction. Dozens of men dressed in black dropped out of empty air, surrounding me as they leveled the weapons in their hands.

Shhk.

Had this been planned from the start? Or had anger, born of loyalty to the Emperor, driven them to it?

Blood welled from the cuts left by their keen blades, then rolled down my neck.

*These bastards… They’re serious.*

The black-clad men had me surrounded without leaving a gap. They felt as impassive as butchers slaughtering livestock, yet I sensed their desperate resolve to kill me the moment they received the order.

At the same time, a hand gripped my sleeve hard.

Squeeze.

It belonged to Prince Shangshan Zhu Bao.

The young prince had been frozen since the moment we learned the middle-aged man was the Emperor. I smiled at him, as if to tell him not to worry.

The Emperor had been watching us in silence. Suddenly, he shook out his voluminous sleeve.

Flap.

The black-clad men withdrew their weapons and leaped into the air with the flutter of his robes.

Their concealment technique was almost a divine skill. They seemed to melt away throughout the Emperor’s quarters, leaving behind only the faintest trace of their presence.

“Your Majesty’s men are certainly loyal.”

This time, I wasn’t being sarcastic.

At my genuine admiration, the Emperor replied in a dry voice.

“Loyalty isn’t all they have. They’re no match for the Slaughter Saint you’re close to, of course.”

“……!”

“What, did you think I wouldn’t know even that much?”

I fell silent for a moment. This time, I was genuinely surprised.

Everyone under heaven knew the title Slaughter Saint, but only a tiny handful knew that he’d reappeared after vanishing long ago.

Yet the Emperor knew not only that the Slaughter Saint was around, but that he and I had a connection.

He must have been drawing on the vast intelligence network he’d laid across the continent.

“Was that information from the Embroidered Uniform Guard?”

At my question, which slipped out after a moment of silence, the Emperor’s expression turned to a mix of displeasure and interest.

“You have remarkable nerve, asking me that.”

Even if I’d managed to get through what had just happened, there was no point in irritating the Emperor further.

Sensing an invisible line, I lowered my head.

“I’m sorry.”

“I stand in fear and awe, Your Majesty.”

“Pardon?”

“Not sorry. You should be in fear and awe. As everyone who addresses me is.”

The two characters for *hwanggong* each meant fear. It was the highest form of deference, befitting the Emperor’s absolute authority over all things.

The Emperor continued to stare at me intently even after he’d finished speaking. I spoke again.

“I stand in fear and awe, Your Majesty.”

“Better. You’re a lawless thug from the martial world, so I can’t expect much. But from now on, you can learn one thing at a time.”

A faint smile spread across the Emperor’s wrinkled lips. My stomach twisted.

But…

*First, I have to survive.*

I wasn’t the only one in danger. Everyone’s lives depended on my every word and action.

That included this young prince, who was clutching my sleeve with a trembling hand.

Just then, the Emperor’s gaze, which had been indifferent until now, finally settled on his only younger brother.

“Come here.”

At those words, the trembling I could feel through the fabric stopped.

It wasn’t because Prince Shangshan had regained his composure. He stood rigid as a statue as the Emperor spoke in a low voice.

“Do you intend to make me say it twice?”

“……!”

Prince Shangshan looked at the Emperor with trembling eyes, then lifted his head to look up at me.

He took a ragged breath, let go of my sleeve, and walked toward the Emperor.

No—he threw himself down in a full prostration and bowed.

“I-I, your subject, Prince Shangshan Zhu Bao, pay my respects to Your Majesty, my imperial brother.”

A heavy silence fell over the room, for a moment—or perhaps for quite some time.

The Emperor looked down at Prince Shangshan with eyes so deeply sunken that it was impossible to guess what he was thinking. His expression was cold enough to make it hard to believe he was facing his much younger brother.

Then he spoke.

“How old are you this year?”

“T-Twelve, Your Majesty.”

“You have good Muscles and Bones. Have you trained in martial arts?”

“Yes.”

“My brothers and I were always devoted to martial arts, even when we were young. Only our eldest brother was more like a civil official.”

Prince Shangshan drew in a small breath. He must have heard this and that from Hong Jin as he grew older, but hearing his family’s history from his only brother would have a different weight.

All the more so when that only brother was the Emperor of the Great Nation—a man he couldn’t treat like an ordinary sibling, and an enemy who’d sent his family to their deaths.

“I… see.”

“Taizu, our grandfather, founded the Great Nation through martial force, too. It’s part of the imperial family’s tradition. Looking at you, it seems blood really does tell.”

The Emperor added in a dry voice,

“Though I don’t know whether that will prove a poison or a boon.”

“……!”

“……!”

I barely managed to suppress the groan that was about to escape me.

Even before we reached the imperial capital, I’d already guessed that the Emperor’s intentions toward Prince Shangshan were anything but friendly. Even so, his response to the prince was far too blatant.

*Is he really that wary of him? His little brother, who’s so much younger?*

Power was ruthless.

People fought like beasts over the little wealth they had, even with their own parents and siblings. What would it be like over a vast continent, an entire empire?

But even so, the Emperor was far too thorough in his suspicion of his youngest brother, who was only twelve years old. In a way, he was right to be.

People were already emerging who dreamed of rebellion, led by Ma Sanbao.

And the Emperor’s next words were unmistakable proof that his wariness had already reached a point of no return.

“From now on, I’ll take care of you.”

“……!”
```
