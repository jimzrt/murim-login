<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1014.txt",
      "sha256": "d85d2d542d725e4db1143a30f1b9136cec522e5f78019d62d74b8f6bb5b26797",
      "bytes": 14545
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "5b210390f8e98c20a6f0976a8bb2b50b92f6417662f869857c9763a606574ad3",
      "bytes": 924
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "30a1ac39205f115d497753cde782f960c1172e8e0adb18958de06997f7b51e57",
      "bytes": 237950
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "554cdac7b73460211bf8f6a10e0e17e0ae650ca30c6fba12e4cc6b729780be97",
      "bytes": 760
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "d7158a680f227a0f6d541877c3a229df95bb85d1de7a465dc073bc878c498c7c",
      "bytes": 937
    },
    {
      "path": "characters/Sima Gong.md",
      "sha256": "669b7b343dc9eaccde99edffb7ac0472baaaf8925185d73af94942959b36744d",
      "bytes": 733
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "b16defca783da7ac0273e6a0cc73ee2502631d4fffa7d52d97de81404153102a",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8a36c21af3e33ce8297d5a41a312212a7b74793dcd26a6bf5d9ca9c9372e2ef2",
      "bytes": 276653
    }
  ],
  "estimated_tokens": 10039
}
-->

# Durable State Update — Chapter 1014

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
1 and safe_through 1014. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1014. Profile updates may replace only one
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
  "chapter": 1014,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1014,
    "continuity_sources": [1014],
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
    "The Lord has advised Ma Junggeol and his sworn brothers for more than ten years and helped them form Baekma Bang and pursue a western trade route.",
    "Six of the Seven Masters have left to fetch the Lord within five days of the march’s halt; Ma Junggeol remains with Taekyung’s group.",
    "Namho has an important matter he says he can only disclose to Taekyung now."
  ],
  "continuity_sources": [
    1013
  ],
  "open_questions": [
    "Who is the Lord, and what are his motives and connection, if any, to Dark Heaven?",
    "Will the six Baekma Bang men return with the Lord within Taekyung’s deadline?",
    "What does Namho need to tell Taekyung, and why can he only tell him now?",
    "What is Dark Heaven’s full strength and objective in the western desert, and have its forces begun advancing?"
  ],
  "safe_through": 1013,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 사마공    | **Sima Gong**      |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 태원진가   | **Jin Family of Taiyuan**        |
| 남만야수궁  | **Nanman Beast Palace**          |
| 십봉룡    | **Ten Dragons and Phoenixes**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 살기     | **killing intent**                               |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 기루     | **pleasure house**                               |                                                       |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 제자     | **Disciple**                                 |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 감숙     | **Gansu**              |
| 청해     | **Qinghai**            |
| 본문      | **our sect / this sect**                                        |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 내당주 | **Inner Hall Master** | Title for the head of the Jin Family's Inner Hall. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 운남 | **Yunnan** | Region from which Jongni Chu comes. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 외당 | **Outer Hall** | The Tang Clan's outer hall area. |
| 내당 | **Inner Hall** | The Tang Clan's inner hall area. |
| 호위장 | **Captain of the Guards** | The Sichuan City Lord's guard captain. |
| 시산혈해 | **sea of corpses and blood** | Description of the preceding months of bloodshed. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 흑룡도 | **Black Dragon Saber** | Sama Pyo's sobriquet. |
| 흑야왕 | **Black Night King** | Epithet of Sima Gong, Sama Pyo's father and the Sect Leader who built the modern Black Dragon Demon Gate. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |
| 황도 | **Imperial Capital** | The capital where the imperial court resides. |
| 당주 | **Hall Master** | Murim Alliance office held by the envoy. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1012
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1012
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Sima Gong.md

# Sima Gong (사마공)

- **Safe through:** Chapter 1011
- **Aliases:** Black Night King
- **Role:** Sima Gong is the Sect Leader who built the Black Dragon Demon Gate into a major unorthodox power and the father of its Young Sect Leader, Sama Pyo.
- **Personality:** Sly and calculating, yet outwardly gentle; he uses persuasive sophistry and a calming manner to justify hard choices.
- **Voice:** Polished and persuasive, with smooth rhetorical turns and a composed, gently teasing manner.
- **Relationships:** Sama Pyo is his youngest son among seven older brothers and nine older sisters; he is personally familiar with Jeok Cheongang, who openly dislikes him.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1012
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃1014화



두두두두!

드넓은 광야를 가로지르는 수천의 인마, 그중에서도 선두를 맡은 흑룡마문(黑龍魔門)의 무인들은 선봉이자 길잡이 역할을 톡톡히 해내고 있었다.

물론, 그보다는 호기심 어린 눈빛으로 저 멀리 떨어진 누군가를 곁눈질하기 바쁜 이들도 있었지만.

“말로만 들었지, 생각보다 훨씬 젊은데요. 저랑 몇 살 차이도 안 나는 것 같아요.”

“기껏해야 이립(而立) 언저리라고 했으니 그럴 만도 하지. 그나저나 확실히 핏줄은 못 속이겠군. 얼굴만큼은 문주님을 빼다 박았어.”

“흑룡도(黑龍刀)라…… 별호부터 끝장나네. 그럼 혹시 그 소문이 사실입니까?”

이제 겨우 약관이나 되었을까.

아직 솜털도 가시지 않은 젊은이의 뜬금없는 물음에, 중년인은 귀찮다는 듯이 얼굴을 찌푸렸다.

“무슨 소문을 말하는 것이냐? 어차피 나 역시 네 녀석처럼, 내부 사정에 까막눈이라는 걸 모르고 묻는 것은 아닐 테고.”

언짢은 기색을 숨기지 않고 드러내자, 젊은이가 황급히 손을 내저었다.

“별거 아니에요. 그냥 저희 소문주께서 중원의 십봉룡(十鳳龍)보다 강하다는 이야기를 들은 적이 있어서.”

“그야 모르지. 나야 십봉룡을 본 적도 없으니.”

“그렇죠. 십봉룡은.”

“뭐?”

“아니 뭐, 아저씨께서 꼭 소문주를 뵌 적이 있다는 뜻은 아니었고요.”

슬쩍 시선을 피하는 젊은이를 노려보던 중년인이 이내 고개를 절레절레 내저었다.

“어느 놈이 나불거렸는지 모르겠지만, 곧이곧대로 믿지 마라. 전부 말도 안 되는 개소리야.”

“개소리라고요?”

“그래.”

“이상하네. 지난번에 아저씨가 저한테 직접 얘기해 주셨잖아요. 잔뜩 취해서.”

“……!”

“그럼 확실한 거죠? 오 년 전, 단혈방의 방주였던 일도단애(一刀斷崖)와 그 수하 스무 명을 단신으로 쓸어 버린 사람이…….”

“그만. 거기까지 해라.”

중년인의 단호한 음성에 젊은이의 뒷말은 이어지지 못했지만, 경외가 깃든 그의 시선은 줄곧 곁눈질하던 한 사람에게서 떨어질 줄을 몰랐다.

흑룡도 사마표.

두 사람이 속한 흑룡마문의 소문주이자, 언젠가 흑야왕 사마공의 뒤를 이어 사파 무림을 이끌어갈 후계자.

흑룡마문에 입문(入門)한 지 얼마 되지 않았다는 것을 증명하듯, 아직 풀이 덜 빠진 빳빳한 무복을 걸친 젊은이는 경탄을 숨기지 못했다.

‘그 이야기가 전부 사실이었다니.’

과거 감숙 무림의 한 축을 담당했던 단혈방에서 벌어진 혈사(血史)는 모르는 이가 없을 만큼 유명했다.

감숙성에서 열 손가락 안에 드는 절정의 도객(刀客)이었던 단혈방주 일도단애와 그 수족들이 한날한시에 처참한 주검으로 발견되었기 때문이었다.

그 후?

말해서 무엇할까.

머리를 잃은 몸뚱어리가 고꾸라지는 것은 당연한 수순이었다.

더군다나 흑룡마문의 위세로 사파 무림의 총본산 격이 되어버린 감숙성에서라면 더더욱.

한때 삼백에 달하는 방도(方徒)를 거느렸던 단혈방은 그렇게 몰락했고, 오 년의 세월이 지난 지금은 사람들의 뇌리에서 자연스럽게 잊혔다.

아니, 그 누구도 구태여 기억하려 들지 않았다.

혈사가 일어나기 얼마 전, 단혈방과 흑룡마문 사이에 사소한 분쟁이 있었다는 사실도.

정체모를 흉수가 찾아온 그 날, 단혈방주와 수뇌부들이 한자리에 모여 술잔을 주고받던 기루를 지키고 있었어야 할 호위장이 수하들을 이끌고 자리를 비웠던 이유도.

그리고 문제의 그 호위장이, 불과 한 달이 지나기도 전에 흑룡마문의 외당주가 되었다는 것 역시도.

그렇게 전부 잊혔다. 잊어야 했다.

감숙 십대 도객을 죽일 만큼 뛰어난 실력을 지녔을 흉수의 정체와 이를 사주한 자의 배경은 물론, 단혈방의 모든 가산과 전답이 어디로 흘러갔는지도.

하지만 그것은 어디까지나 겉가죽에 불과할 뿐, 일련의 사정을 훤히 꿰뚫고 있던 사파의 무림인들은 확신하고 있었다.

동시에 경외했다.

지금 이 순간, 또 한 사람의 사파인으로서 경탄을 담아 사마표를 바라보는 젊은이가 그러하듯이.

“정말, 정말 대단하네요. 안 그렇습니까? 괜히 배다른 손위 형제들을 제치고 후계자가 된 게 아니…… 흡.”

젊은이는 자신도 모르게 헛숨을 삼켰다.

파르르 떨리는 그의 눈동자 비친 것은, 한껏 얼굴을 일그러트린 채 검파(劍把)를 붙잡은 중년인의 모습이었다.

“네놈이 정녕, 죽고 싶어 환장했구나.”

바로 옆에서 말머리를 나란히 한 채 달리던 젊은이조차 유심히 귀를 기울이지 않는다면 듣지 못했을 만큼 나직한 음성.

그러나 그 안에 담긴 살기(殺氣)는, 아직 풋내기에 불과한 젊은이의 심장을 쥐어 짜내는 듯했다.

“가, 갑자기 왜…….”

“그 주둥이 닥쳐라. 단 며칠이라도 더 연명하고 싶다면.”

더듬더듬 흘러나온 젊은이의 목소리를 단호하게 끊어 낸 중년인은 빠르게 주위를 훑었다.

드넓은 광야를 질주하고 있었던 덕분일까.

다행히도 인마 간의 간격은 멀었고, 쉼 없이 내달리는 수천의 말발굽과 맹렬한 바람 소리는 그들의 대화가 다른 이의 귓가에 닿기도 전에 가려 주고 있었다.

“멍청한 놈 같으니.”

“아, 아저씨.”

“두 번 말하지 않는다. 살고 싶으면 그 주둥이 다물어.”

“아, 알겠습니다.”

벌벌 떠는 젊은이를 뒤로한 채, 냉막한 얼굴로 말을 박차를 가한 중년인은 내심 한숨을 내쉬었다.

아마 녀석은 모를 것이다.

조금 전의 자신이 얼마나 경솔하고도 멍청한 실수를 저질렀는지.

만약 흑룡마문 내의 금기(禁忌)와도 같은 그 발언이 누군가의 입과 귀를 타고 상부로 전해졌다면, 덧없이 목숨을 잃었을 것이라는 사실도.

‘어쩌면…… 영원히 모를 수도 있겠지.’

한 인간이 성숙해지는 데까지는 제법 긴 시간이 필요하다.

하지만 불현듯 들이닥친 전쟁은, 적들은 그 시간이 무르익기도 전에 빼앗아 간다.

그리고 곧 벌어질 전투를 떠올린 중년인의 눈빛이 심유하게 가라앉은 그때, 그의 신형이 흠칫 떨렸다.

‘뭐지?’

순간 전신을 사로잡은 알 수 없는 기시감.

그러나 황급히 고개를 돌려 사방을 살핀 중년인은, 결국 기시감의 정체를 알아내지 못하고 다시 본연의 임무에 집중해야 했다.

십여 장도 넘게 떨어진 거리에서, 두 쌍의 시선이 자신을 훑듯이 스쳐 지나갔다는 사실을 조금도 인지하지 못한 채.

“이럇!”

푸르륵, 푸륵.

거친 숨결을 토해 내며 내달리는 준마.

서서히 앞서 나가는 중년인의 모습에, 뒤늦게 정신을 차린 젊은이가 새하얗게 질린 얼굴로 뒤따랐다.

“같이, 같이 가요!”



* * *



한 사람이 홀로 입을 열면 그것은 단순한 말에 지나지 않지만, 열 사람이 모였을 때는 외침이 되고 일백을 넘기면 함성이 된다.

그러나 삼천을 헤아리는 인마가 동시에 한 방향을 향해 달려가고 있음에도, 두 부자(父子)의 대화는 서로의 귓가를 또렷하게 파고드는 중이었다.

“처음 보는 얼굴들이 많군요.”

“그렇게 되었다.”

“제법 쓸 만한 자도 보이고요.”

“급한 대로 끌어모은 진흙 속에도 진주는 있는 법이지. 별것 아닌 일에도 쉽게 깨지기도 하지만.”

뒷말에 담긴 의미를 알고 있는 아들은 침묵했고, 아버지는 그런 아들의 모습을 놓치지 않았다.

언제나, 지금껏 늘 그래 왔듯이.

“저자들이 신경 쓰이느냐?”

흑야왕 사마공의 나직한 물음에, 묵묵히 전방을 주시하던 사마표가 입을 열었다.

“무슨 말씀이신지 모르겠군요.”

“중원의 풍광(風光)을 보고 와서인지, 전과 달리 말장난이 늘었구나.”

“그리 볼만한 광경은 없었습니다. 액운(厄運)이라도 끼었는지, 가는 곳마다 시산혈해였지요. 물론 이미 알고 계시겠지만 말입니다.”

“그래, 보고를 들어 알고 있다. 한데 도중에 무슨 착오라도 있었는지, 어느 날부터는 전서구가 돌아오지 않아 직접 손을 써야 했지. 늦지 않게 정보를 얻기에는 거리가 먼 탓에 내당주(內堂主)가 제법 고생했다.”

“어쩔 수 없었습니다. 운남(雲南)은 소식을 주고받기에 그다지 좋은 환경이 아니었으니까요.”

“질책하는 것이 아니다. 남만야수궁(南蠻野獸宮)에서 어떤 일이 벌어졌는지는 이 아비 역시 잘 알고 있으니. 한데…….”

사마표는 침묵과 함께 귀를 기울였다.

뒤이어 들려 올 아버지의 말이, 자신이 바라는 내용이기를 바라면서.

그러나 기대했던 일은 벌어지지 않았다.

언제나 그래 왔듯이, 이번에도.

“그 이후에는 어찌 전서를 보내지 않았느냐.”

“전서…… 말입니까.”

“그래, 운남을 벗어난 이후로도 몇 번이나 기회가 있었던 것으로 안다. 황도(皇都)에서도, 태원진가에서도. 내 말이 틀렸느냐?”

무슨 말을 해야 할까.

입안이 모래알을 한 움큼 씹은 것처럼 까끌거린다. 사마표는 거세게 전신을 부딪쳐 오는 바람을 느끼며 입을 열었다.

“반은 맞고, 반은 틀렸습니다.”

“뭐라?”

“황도에서는 감시의 눈길을 피하기 위해 신분을 숨기고 변복까지 해야 했습니다. 가는 길 역시 순탄치 않았지요. 물론 황궁 내에 들어선 이후로는 더 말할 것도 없었습니다.”

사마공은 아들의 옆모습을 물끄러미 응시했다.

마치 아주 작은 틈새 하나조차 빠짐없이 찾아내겠다는 듯이.

“계속해 보거라.”

“황궁에서의 사건이 마무리된 직후에도 사정은 나아지지 않았습니다. 저희는 짧은 시간 동안 황궁 안에 머물러 있어야 했고, 제대로 된 휴식도 하지 못한 채 곧장 산서로 향해야 했으니까요.”

“황궁에서와는 달리 산서에서는 별다른 부상도 입지 않은 것으로 아는데, 내가 잘못 알고 있는 것이냐?”

“아시는 바가 맞습니다. 하여 그제야 본문에서 온 전서를 받을 수 있게 된 것이지요.”

“하면, 틀림없이 명령을 확인했다는 뜻이로군.”

“예. 보았습니다. 틀림없이.”

일말의 망설임조차 느껴지지 않는 그 대답에, 사마공의 눈빛이 한층 더 깊숙하게 가라앉았다.

“화왕(火王)과 그 제자는 이곳이 아닌 청해로 향해야 했다. 네가 확인한 내용이 맞느냐?”

“그렇습니다.”

“본문이 위험에 처했으니, 너만큼은 무슨 수를 써서라도 감숙으로 돌아오라 했다. 이 또한 맞느냐?”

“정확합니다.”

“그렇다면 마지막으로, 내 직인을 보고도 명령을 이행하지 않은 것에 대해 합당한 이유나 근거가 있느냐?”

그 순간, 사마표는 고개를 돌려 아버지를 똑바로 응시했다.

“없습니다.”

“……!”

“그 어떤 변명도, 이유도 하지 않겠습니다. 명령을 제대로 이행하지 않았으니 그에 합당한 벌 역시 달게 받겠습니다. 부디 용서하십시오.”

생각지도 못한 아들의 모습에, 사마공은 잠시 침묵했다.

그리고 두 사람 사이에 이어진 그 찰나의 정적은, 이내 사마공의 입술을 비집고 흘러나온 나직한 웃음소리에 의해 끊어졌다.

“으하. 으하하하.”

갑작스러운 웃음소리에도 두 부자를 호위하듯 에워싸고 있던 이들 중 그 누구도 반응하지 않았다.

사마공의 수족인 그들은 하나같이 뛰어난 절정 고수였으나, 주군의 앞에서는 눈 뜬 소경이자 귀머거리나 다름 없었으니까.

하지만 사마표는 달랐다.

그는 담담한 눈빛으로 자신의 아버지를 응시했다.

어느 순간 웃음소리가 뚝 끊기고, 이어지는 목소리가 그 빈 자리를 채울 때까지.

“표야. 내 아들아.”

귓가로 전해지는 음성은 비단결처럼 부드러웠지만, 그 입술 사이로 드러난 눈동자는 칼날처럼 예리했다.

“만약 네가 감히 면전에서 거짓을 고했다면, 그리했다면…….”

미처 끝맺어지지 못하고 서서히 흐려지는 말꼬리와 함께, 사마공의 눈꼬리가 반달처럼 휘어졌다.

“오늘날에서야 비로소 깨달았다, 너를 중원으로 보낸 것이 참으로 옳은 결정이었음을.”

툭툭.

광야에 휘몰아치는 바람 때문일까.

유난히도 차가운 손길로 아들의 어깨를 두드린 사마공이 흡족한 얼굴로 입을 열었다.

“성장했구나. 아주 훌륭하게.”

그 말을 끝으로 말머리를 돌려 멀어지는 아버지의 뒷모습을, 아들은 그저 말없이 바라보았다.

“조금 전에 그 두 명, 알아서 조치하도록 하게.”

단순한 실언(失言)을 짧게나마 입에 담은, 이름 모를 두 무인의 운명을 한 마디로 결정지은 사마공의 모습이 완전히 시야에서 사라질 때까지.

그리고 그 이름만큼이나 어릴 적부터 든든한 버팀목이 되어주었던 동무가 다가와, 떨리는 목소리로 이렇게 물어올 때까지.

“주, 주군. 괜찮나?”

걱정으로 가득한 태산의 물음에, 사마표가 담담하게 대답했다.

“그래, 난 괜찮아.”

참으로 모를 일이었다.

이토록 드넓은 광야를 내달리고 있음에도 가슴이 답답한 이유는.

모두의 머리 위로 펼쳐진 저 잿빛 하늘 위로, 몇 사람의 얼굴이 스쳐 지나가는 것은.

그러나 사마표는 말머리를 돌리지 않았다.

이제 그가 있어야 할 곳은 화룡각이 아닌, 흑룡마문이었으니까.
```

## Final English reading copy

```markdown
# Chapter 1014

*Thud-thud-thud!*

Thousands of men and horses raced across the vast open plain. At their head, the martial artists of the Black Dragon Demon Gate were doing an excellent job as both vanguard and guides.

Of course, some of them were more preoccupied with sneaking curious glances at someone far off to the side.

“I’d only heard about him, but he’s much younger than I expected. He doesn’t look much older than me.”

“They said he was around thirty at most, so that makes sense. Still, blood tells. His face is the spitting image of the Sect Leader.”

“The Black Dragon Saber… What a killer sobriquet. So, is that rumor true?”

The young man asking out of nowhere looked barely twenty.

The middle-aged man frowned as if annoyed by the question from the youngster, who still had the down on his cheeks.

“What rumor are you talking about? You know I’m just as clueless about the inner workings as you are, so you’re not asking because you think I’d know.”

When the older man openly showed his displeasure, the young one hurriedly waved his hands.

“It’s nothing. I just heard our Young Sect Leader is stronger than the Ten Dragons and Phoenixes of the Central Plains.”

“Who knows? I’ve never even seen the Ten Dragons and Phoenixes.”

“Right. The Ten Dragons and Phoenixes.”

“What?”

“No, I didn’t mean you’d necessarily met the Young Sect Leader, Uncle.”

The middle-aged man glared at the young one as he slyly looked away, then shook his head.

“I don’t know which idiot’s been running his mouth, but don’t believe everything you hear. It’s all ridiculous bullshit.”

“Bullshit?”

“Yeah.”

“That’s strange. You told me yourself last time, Uncle. When you were dead drunk.”

“……!”

“So it’s true, then? Five years ago, the man who single-handedly wiped out the One Saber Cuts the Cliff, the former chief of Danhyeol Bang, and twenty of his men…”

“That’s enough. Don’t say another word.”

The middle-aged man’s firm voice cut off the young one before he could finish. But the awe in his eyes never left the man he’d been sneaking glances at.

The Black Dragon Saber, Sama Pyo.

The Young Sect Leader of the Black Dragon Demon Gate, to which the two men belonged, and the heir who would one day follow the Black Night King, Sima Gong, in leading the unorthodox Murim.

The young man wore a stiff martial uniform that hadn’t yet lost its creases, proof he’d only recently joined the Black Dragon Demon Gate. He couldn’t hide his amazement.

*So the whole story was true.*

Everyone knew about the bloody tragedy that had unfolded at Danhyeol Bang, once one of the powers of Gansu Murim.

The chief of Danhyeol Bang, One Saber Cuts the Cliff, had been one of the ten greatest saber masters in Gansu. He and his closest men had all been found brutally murdered on the same day.

And after that?

What was there to say?

A body without a head was bound to fall. Especially in Gansu, which had become the de facto headquarters of the unorthodox Murim under the Black Dragon Demon Gate’s influence.

Danhyeol Bang had once commanded three hundred members. That was how it fell, and five years later, people had naturally forgotten it.

No. No one had bothered to remember.

Not that, shortly before the massacre, Danhyeol Bang and the Black Dragon Demon Gate had been involved in a minor dispute.

Not that, on the day the mysterious killer came, the Captain of the Guards—who should have been protecting the pleasure house where the chief and leaders of Danhyeol Bang had gathered to drink—had left with his men.

And not that, less than a month later, that same Captain of the Guards had become the Black Dragon Demon Gate’s Outer Hall Master.

It had all been forgotten. It had to be.

The identity of the killer skilled enough to slay one of Gansu’s ten greatest saber masters, the background of whoever had ordered the killing, and even where all of Danhyeol Bang’s property and farmland had gone.

But that was only the surface. The unorthodox martial artists who knew the whole story were certain of what had happened.

And they were in awe.

Just like the young man who, as an unorthodox martial artist himself, now looked at Sama Pyo with admiration.

“That’s really, really incredible. Don’t you think? It’s no wonder he became the heir over his older half-brothers—”

The young man drew in a sharp breath.

Reflected in his trembling eyes was the middle-aged man, face twisted as he gripped his sword hilt.

“You really have a death wish, don’t you?”

The voice was so low that even the young man riding right beside him wouldn’t have heard it if he hadn’t been listening closely.

But the killing intent in it seemed to squeeze the heart of the young man, still a raw novice.

“W-why all of a sudden…?”

“Shut your mouth if you want to live even a few more days.”

The older man cut off his stammering without mercy, then quickly scanned their surroundings.

Perhaps it was because they were racing across such a vast plain.

Fortunately, there was plenty of distance between the riders, and the thunder of thousands of hooves and the fierce wind swallowed their conversation before anyone else could hear it.

“You idiot.”

“U-Uncle.”

“I won’t say it twice. Keep your mouth shut if you want to live.”

“I-I understand.”

Leaving the trembling young man behind, the middle-aged man kicked his horse into a faster pace, his cold expression unchanged as he sighed inwardly.

The kid probably didn’t know.

He had no idea what a careless, stupid mistake he’d just made.

Nor that if those words—practically taboo within the Black Dragon Demon Gate—made their way up to the higher-ups, passed from one person’s mouth to another’s ears, he’d lose his life in vain.

*Maybe he’ll never know.*

It takes quite a while for a person to mature.

But the war that came out of nowhere—and the enemies—would take that time away before it could run its course.

The middle-aged man’s eyes sank into thought as he considered the battle about to begin. Then his body flinched.

*What was that?*

An inexplicable sense of déjà vu seized him for an instant.

He hurriedly turned his head to look around, but in the end, he couldn’t figure out where the feeling had come from. He had to refocus on his duty.

He never realized that two pairs of eyes had swept over him from more than thirty yards away.

“Hyah!”

The fine horse raced on, breathing hard.

The young man, who had only just come back to his senses, hurried after the middle-aged man as his face turned deathly pale.

“W-wait for me!”

* * *

One person speaking alone produced only speech. Ten voices became a shout, and more than a hundred became a roar.

Yet even as three thousand men and horses raced in the same direction, the conversation between father and son carried clearly to each other’s ears.

“There are a lot of faces I don’t recognize.”

“That’s how things turned out.”

“And a few who look useful, too.”

“Even when you scrape together mud in a hurry, you can find a pearl or two. Though they can crack easily over nothing.”

The son knew what his father meant by that last remark, and fell silent. His father didn’t miss it.

Just as always. Just as he always had.

“Are those people bothering you?”

At the Black Night King Sima Gong’s quiet question, Sama Pyo—who’d been silently watching the road ahead—spoke.

“I don’t know what you mean.”

“After seeing the sights of the Central Plains, you’ve gotten better at playing with words.”

“There wasn’t much worth seeing. Maybe bad luck was following me. Everywhere I went, I found a sea of corpses and blood. Though I’m sure you already knew that.”

“Yes, I heard the reports. But for some reason, the messenger pigeons stopped returning one day, and I had to take matters into my own hands. The distance made it difficult to get information in time, and the Inner Hall Master had quite a hard time of it.”

“It couldn’t be helped. Yunnan wasn’t exactly a good place for sending messages back and forth.”

“I’m not scolding you. Your father knows well what happened at the Nanman Beast Palace, too. But…”

Sama Pyo listened in silence.

He hoped his father’s next words would be what he wanted to hear.

But it didn’t happen.

As always, not this time either.

“Why didn’t you send a missive after that?”

“A missive…?”

“Yes. I understand you had several chances even after leaving Yunnan. In the Imperial Capital, and at the Jin Family of Taiyuan. Am I wrong?”

What was he supposed to say?

His mouth felt gritty, as if he’d chewed a fistful of sand. Sama Pyo felt the wind battering his whole body and spoke.

“You’re half right and half wrong.”

“What?”

“In the Imperial Capital, I had to hide my identity and even disguise myself to avoid the eyes watching me. The journey there wasn’t smooth, either. And once we entered the Imperial Palace, things only got worse.”

Sima Gong studied his son’s profile.

As if he meant to find even the tiniest crack.

“Go on.”

“Things didn’t improve right after the incident in the Imperial Palace was over. We had to remain inside the palace for a short time, and then we had to head straight for Shanxi without getting proper rest.”

“I was under the impression that you suffered no serious injuries in Shanxi, unlike at the Imperial Palace. Am I mistaken?”

“You’re right. That’s when I was finally able to receive the missive from our sect.”

“Then you certainly saw the order.”

“Yes. I saw it. There’s no doubt.”

At that answer, given without even a hint of hesitation, Sima Gong’s eyes sank deeper.

“The Fire King and his Disciple were supposed to go to Qinghai, not here. Was that what the order said?”

“It was.”

“It said our sect was in danger, and that you, at least, were to return to Gansu by any means necessary. Was that right, too?”

“Exactly.”

“Then, lastly—do you have a proper reason or justification for seeing my seal and still not carrying out the order?”

At that moment, Sama Pyo turned his head and looked his father straight in the eye.

“No.”

“……!”

“I won’t make excuses. I won’t give you any reason. I failed to carry out the order properly, so I’ll accept whatever punishment I deserve. Please forgive me.”

Sima Gong fell silent for a moment, surprised by the son before him.

Then the brief silence between them was broken by the low laugh that slipped from Sima Gong’s lips.

“Ha. Hahaha.”

None of the men surrounding the two of them like a guard reacted to the sudden laughter.

They were all Peak masters, the Black Night King’s loyal hands and feet, but before their lord they were little better than the blind and deaf.

Sama Pyo was different.

He watched his father with calm eyes.

The laughter abruptly stopped, and a voice filled the silence.

“Pyo. My son.”

The voice at his ear was soft as silk, but the eyes revealed between those lips were sharp as blades.

“If you dared to lie to my face—if you did…”

His voice trailed off before he could finish, fading as Sima Gong’s eyes curved into crescents.

“Only now do I realize how right I was to send you to the Central Plains.”

Pat. Pat.

Perhaps it was the wind sweeping across the open plain.

With an unusually cold hand, Sima Gong patted his son on the shoulder and spoke with satisfaction.

“You’ve grown. Very well.”

With that, he turned his horse and rode away. His son simply watched his father’s back in silence.

“Take care of those two from a moment ago.”

Sima Gong had decided the fate of the two nameless martial artists with a single sentence, for a careless remark they’d made, however briefly. Sama Pyo watched until his father had completely disappeared from view.

Then Taishan came over—an old friend who had been as steady as the mountain he was named for since childhood—and asked in a trembling voice,

“M-My lord. Are you all right?”

At Taishan’s worried question, Sama Pyo answered calmly.

“Yes. I’m fine.”

It was strange.

Why did his chest feel so tight as they rode across this vast plain?

Why did a few faces flit through his mind beneath the gray sky stretching over everyone?

But Sama Pyo didn’t turn his horse around.

The place he belonged now was the Black Dragon Demon Gate, not the Fire Dragon Pavilion.
```
