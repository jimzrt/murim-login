<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0929.txt",
      "sha256": "a1f530dedd1cb08d491613f1d689091e7c599c8a535f26a25c1ffe3f4702a937",
      "bytes": 12374
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "8d9e991756f7acb61ba45ff7cf4105122c6ea085bd39debb6922d81719500378",
      "bytes": 2117
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0666305ef3a14502bbfe5c72134a55888b76af6f3fad7264eaf0463c809292b0",
      "bytes": 231946
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "4ce0c30abe51c6e69909da37d4b57ae4fb3b9b02e232c605d6602a3055d235e8",
      "bytes": 628
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "bb1e6567089b98fd5b2c11d799efd2115fa18b003df9925971cc681067887afd",
      "bytes": 699
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "648341ab2436be9aa45449e1a17e4d9d7974da3049f9e5765340e64d9d23066b",
      "bytes": 1042
    },
    {
      "path": "characters/Wei Zhong.md",
      "sha256": "732686cd085c06270a2a677e1155c7b67ab78caa8bfe9fb574349aa76a964b76",
      "bytes": 714
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "0e2d532f2af4d7be69c6e65c1cef25321d7cf2235ebf140c6de94d6147d63060",
      "bytes": 266948
    }
  ],
  "estimated_tokens": 9207
}
-->

# Durable State Update — Chapter 929

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
1 and safe_through 929. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 929. Profile updates may replace only one
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
  "chapter": 929,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 929,
    "continuity_sources": [929],
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
    "Zhu Bao is Crown Prince; the Emperor is his older brother and supports his compassionate vision of rulership.",
    "The Emperor ordered a purge of treason suspects while promising to spare the innocent after their connections are established.",
    "The Martial God left the Bow Saint a letter describing a chosen one who would bring a new dawn; Taekyung concludes from the Martial God’s message that the Martial God was also a System user, a Player.",
    "The Bow Saint searched for the chosen one for decades, considered Taekyung and Cheongpung, and is now convinced Taekyung is the one; she tested Taekyung and relayed the Martial God’s message.",
    "The Bow Saint used the Imperial Palace’s information network while disguised as a palace attendant; the Emperor knows nothing of her mission beyond a vague suspicion.",
    "Aehyang, the City Lord of Sichuan Province’s favorite concubine, was a Dark Heaven agent who infected him with the Blood Soul Gu while he was in the Imperial Capital.",
    "Knowing the City Lord was likely to die, the Bow Saint sent him back to Sichuan so someone around Taekyung might discover the cause.",
    "The Bow Saint says Dark Heaven has infiltrated the Great Nation’s local officials and military leadership, potentially including provincial City Lords.",
    "Taekyung collapsed after hearing the Martial God’s message; Jeok Cheongang took him away to rest."
  ],
  "continuity_sources": [
    928
  ],
  "open_questions": [
    "What is the Martial God’s identity, and how did he know a chosen one would appear?",
    "How far has Dark Heaven infiltrated the Great Nation, and which officials or commanders are involved?",
    "What story has So Gyo kept to herself?",
    "Where is Ma Sanbao, and what is his current status?",
    "What did Wei Zhong tell Taekyung through Sound Transmission?"
  ],
  "safe_through": 928,
  "temporary_decisions": [
    "Keep “Force” for 강기 distinct from “death energy” for 사기.",
    "Render 황태제 as “Crown Prince” in this succession context."
  ],
  "version": 1
}
```

## Exact glossary matches

| 암천     | **Dark Heaven**                  |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 중원     | **Central Plains**                               |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 노부      | **this old man / I**                                            |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 위충 | **Wei Zhong** | The pledge’s first signer and the personal name of Lord Cang Gong. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 선황 | **the late Emperor** | The former Emperor whom Hong Jin served. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 창천 | **azure heaven** | The cloudless sky seen by Namgung Ryong. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 오악 | **Five Sacred Mountains** | Mountain grouping that includes Mount Song. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 정호군 | 상산왕 | imperial guard officer escorting the prince | His Highness | formal and deferential | Hogun formally reports that he has come to escort the prince. |
| 상산왕 | 황제 | younger brother addressing the Emperor | Your Majesty | deferential royal address | Shangshan addresses the Emperor as 폐하 while pleading for Taekyung. |
| 황제 | 위충 | Emperor addressing the East Depot’s Seal-Holding Eunuch | Cang Gong | familiar and authoritative | The Emperor addresses Wei Zhong by his East Depot title while asking after his recovery. |
| 위충 | 황제 | East Depot’s Seal-Holding Eunuch addressing the Emperor | Your Majesty | formal and deferential, with pointed flattery | Wei Zhong uses 폐하 while indirectly challenging the Emperor. |
| 황제 | 주표 | older brother addressing his younger brother and newly appointed Crown Prince | Bao’er | intimate and authoritative | The Emperor uses a warm childhood-style name before commanding Zhu Bao to accept the succession. |
| 주표 | 황제 | younger brother and Crown Prince addressing the Emperor | Your Majesty | formal and deferential | Zhu Bao formally accepts the Emperor’s command. |

## Listed compact profiles

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 923
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he follows imperial orders without hesitation and reads the political consequences of events with care.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Jeong Hogun serves under Baek Yeon’s command in the Embroidered Uniform Guard.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 923
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 927
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is the Emperor’s thirteen-year-old younger brother, an exceptionally skilled young swordsman, and the newly appointed Crown Prince.
- **Personality:** Earnest and compassionate, he takes responsibility for others’ suffering and dreams of a peaceful age founded on justice, care for the people, wise counsel, and accountability, even when doing so demands personal sacrifice.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Zhu Bao is the Emperor’s younger brother and Crown Prince, and Hong Jin has been his steadfast caretaker since childhood. He admires Jin Taekyung and calls him a friend; his compassion for the Eastern Heaven Demon Lord reflects the different path made possible by those who supported him.

### Wei Zhong.md

# Wei Zhong (위충)

- **Safe through:** Chapter 925
- **Aliases:** None
- **Role:** Wei Zhong, addressed as Cang Gong, was the East Depot’s Seal-Holding Eunuch and Eastern Heaven Demon Lord; Jin Taekyung killed him with White Flame.
- **Personality:** Politically perceptive and self-possessed, he uses courteous remarks and veiled barbs to challenge the Emperor.
- **Voice:** He speaks in formal, deferential language, using repeated praise and respectful address to deliver pointed challenges.
- **Relationships:** He has a long-standing connection to the Emperor, with whom he exchanges polite but adversarial remarks about the succession.

## Korean source

```text
＃929화



그날 밤은 유난히도 어둡고 길었다.

타오르는 횃불과 날 선 병장기를 들고 서로를 향해 끊임없이 뒤엉킨 양측의 군사들에게도.

두려움에 떨며 이 갑작스러운 난리가 끝나기만을 기다리던 백성들에게도.

차차차창!

크아악!

그날의 전투는 비단 황궁 한 곳에만 국한된 것이 아니었다.

날붙이가 맞물리는 서늘한 마찰음과 비명은 장장 몇 시진 동안이나 황도(皇都) 전역을 뒤덮었고, 그 소리를 들은 수많은 이들은 그리 오래되지 않은 과거의 기억을 떠올렸다.

지금으로부터 불과 십여 년 전, 대국의 순리와 역사를 송두리째 뒤바꾸었던 사 황자의 정변(政變)을.

그리고 이 극심한 혼란 속에서, 누구보다 큰 분노와 두려움에 사로잡힌 이들이 있었다.

“이 씹어 죽여도 시원치 않을 놈들이 기어코……!”

“끄, 끝났소. 금의위에게 발각당한 것이 분명하단 말이오!”

먼지와 거미줄로 가득한 어느 버려진 사당 내부, 흐릿한 호롱불의 그림자가 일렁이는 탁자를 사이에 두고 마주한 수십여 명의 사람들.

복장도, 연령대도 다양한 그들이 토해 내는 외침을 듣고 있던 한 노인이 불현듯 입술을 뗐다.

“소란스럽군.”

나직하지만 힘 있는 목소리가 울려 퍼진 순간. 약속이라도 한 듯이 동시에 입을 다문 사람들의 시선이 노인을 향했다.

오랜 세월을 살아왔음을 증명하듯 자글자글한 주름으로 가득한 피부와 왜소한 체구.

그러나 노회한 눈동자는 맑으면서도 깊었고, 군데군데 기운 흔적이 있으나 한 치의 흐트러짐도 없는 의복과 태도는 노인이 어떤 인생을 살아왔는지 보여 주었다.

“부화뇌동(附和雷同)하지 말게. 가야 할 길은 이미 정해져 있었으니.”

노인은 미지근한 찻잔을 기울였다.

창밖 멀리에서 조금씩 가까워지는 횃불의 꼬리와 거대한 함성 따위는 조금도 신경 쓰지 않는 듯한 태도로.

“저 밖에서 어떠한 변고가 벌어지고 있는지는 모르나, 오히려 잘되었네. 혼란이 일어난 지금이야말로 우리가 나서야 할 때야.”

때가 왔다.

노인의 짧은 한마디를 들은 누군가는 눈을 빛냈고, 누군가는 두려움을 억누르지 못하고 몸을 떨었다.

반정(反正).

그들이 오늘 이 자리에 모인 이유이자, 오직 한 사람을 구하기 위한 명분.

“이제…… 모든 것을 원래의 자리로 되돌려 놓아야겠네.”

노인의 눈동자가 번뜩였다. 구순(九旬)이라는 나이가 믿어지지 않을 만큼 힘 있게. 그리고 누구보다 올곧게.

“도리(道理)를 벗어나고 순리(順理)를 무너트린, 저 잔인무도한 역적들을 저 황궁에서 몰아내고 백성들의 힘으로 상산왕 전하를 옹립하세.”

“……!”

“……!”

보이지 않는 격동이 물결처럼 사당 내부를 휩쓸었다.

스스로의 각오와 의지로 이곳에 왔음에도, 솟구치는 흥분과 두려움에 잠시 잊고 있었다.

자신들이 도모하려는 대업이 어떤 의미를 지녔는지.

‘백성들의 힘으로. 백성들의 군주를 옹립한다.’

그들은 문득 서로를 바라보았다.

나이도, 신분도, 성별도 다르다.

그러나 이제는 한배를 탄 동지였다.

저마다 각자의 자리에서 각자의 인생을 살아가던 그들이 한자리에 모인 것은, 대국이라는 거대한 함선을 올바른 방향으로 나아가게 하기 위해서였다.

불과 며칠 전, 정체를 알 수 없는 누군가가 했던 말이 마음 깊숙한 곳에 숨겨두었던 도화선에 불을 붙였기 때문이었다.

“푸르렀던 창천(蒼天)이 쇠하고, 어두운 먹구름이 밀려온다.”

누군가의 입술 사이로 불현듯 흘러나온 노랫가락에, 젊은 유생이 홀린 듯이 입을 열었다.

“머지않아 불어올 비바람은 천하를 집어삼킬 터.”

“그러나 백성이여, 떨지 말라. 두려워하지 말라.”

피부가 검게 그을린 늙은 인부가 걸걸한 목소리로 중얼거렸다. 한때 일군(一軍)을 이끄는 장수였던 그의 손에는 시퍼렇게 날이 선 도끼가 들려 있었다.

“천하에서 가장 높은 산이 있으니.”

“그곳에는 마르지 않는 개울이 있고.”

“탐스러운 열매와 뛰노는 짐승이 있으며.”

“풍파(風波)를 막아 줄 집과 장작이 되어 줄 숲 또한 있으니.”

그것은 더 이상 누구 한 사람의 목소리라 부를 수 없었다.

그들은 지난 며칠간 황도의 저잣거리를 떠돌았던 노랫가락을 읊조리며, 무거운 몸을 일으켰다.

“능히 만백성을 품고도 남으리라.”

저벅. 끼이익.

줄지어 낡은 사당을 빠져나가는 사람들의 발걸음에 낡은 사당이 신음한다.

그러나 계속해서 울려 퍼지는 노랫가락은 더욱더 힘 있고 크게 울려 퍼졌다.

“그러니 백성이여. 떨지 말라. 두려워하지 말라.”

새하얀 백의(白衣)를 휘날리며 앞장선 노인의 발걸음이 축축하게 젖은 흙을 밟았다.

그리고 그의 왜소한 체구가 험한 산길을 따라 걸을 때마다, 어둠 너머에 웅크리고 앉아 있던 그림자들이 일어나 그 뒤를 따랐다.

수십에서 수백으로.

수백에서 수천으로.

어느덧 하나의 군세(軍勢)로 거듭난 그들의 손에는 흙 묻은 낫이, 붉게 녹슨 창칼과 도끼가 들려 있었다.

저벅. 저벅.

동쪽에서 비쳐 오는 희미한 서광(曙光)과 마치 살아 있는 용처럼 산을 향해 기어오르는 횃불의 꼬리를 향해 나아가는 발걸음.

그와 더불어 그들의 입술 사이로 흘러나오는 노래는, 간절한 염원이자 거대한 울림이 되었다.

“상산(上山)으로, 상산으로 가거라.”

깊게 가라앉은 수천 쌍의 눈동자가, 어둠 속에서 빛난다.

“거센 비바람이 중원오악(中原五岳)을 집어삼킬지언정, 감히 상산에는 닿지 못할 테니.”

두두두두.

야트막한 산이 몸을 떨었다. 시시각각 가까워지는 저 횃불들의 정체는 아마도 반정을 알아차린 황제가 보낸 토벌군일 터.

그러나…….

“상산의 주인은 하늘의 보살핌을 받는 자!”

그들은 더욱더 목소리를 높였다.

신분의 고하를 막론하고 목에 핏대를 세워 가며, 지금 이 순간에도 울컥 차오르는 두려움을 애써 억누르며.

평소와 다름없었던 며칠 전의 어느 날, 정체를 알 수 없는 죽립 사내가 그들의 마음속으로 내던진 한 마디를 힘차게 부르짖었다.

“비와 낙뢰를 다스리는 용의 후손이요, 옳고 어진 군주의 그릇이로다!”

그리고 그들이 토해 낸 거대한 외침이 사방을 떨어 울린 그 순간.

쉭.

유난히도 날카롭게 느껴지는 한 줄기의 바람과 함께, 어스름한 새벽안개를 헤치며 불현듯 나타난 한 사내가 입을 열었다.

“노랫가락이 제법 듣기 좋구려.”

“……!”

“……!”

모두의 눈이 부릅떠졌다.

여기저기 말라붙은 핏물로도 감출 수 없는 황금빛 갑옷.

그것이 의미하는 단 한 가지뿐이었기에.

“금의위……!”

누군가가 신음처럼 토해 낸 그 세 글자에, 잘게 떨리는 눈동자들이 불과 수백여 장 밑에서 물결치는 횃불을 바라보았다.

의심이 확신으로 변하는 순간이다.

틀림없다.

저들은 반정을 토벌하기 위해 황제가 보낸 금의위들이다.

그리고 어쩌면 상산왕은 이미…….

“이 천인공노할 놈들! 하늘이 두렵지 않으냐!”

분노에 사로잡힌 반정군 중 일부가 금의위임이 확실한 사내를 향해 짓쳐 들려던 그때였다.

늙은 몸으로 반정군 모두를 앞장서서 이끌던 노인이 불현듯 입을 연 것은.

“그 갑옷에 묻은 피는, 누구의 것인가?”

당장이라도 달려들 것 같던 반정군이 움직임을 멈췄고, 사내의 담담한 목소리가 들려왔다.

“종묘사직(宗廟社稷)을 위태롭게 한 역적들의 것이오.”

“하면, 그대가 말하는 역적들이란 누구인가.”

“작게는 동창장인태감(東廠掌印太監) 위충과 그와 결탁한 무리들이며, 크게는 암천(暗天)이라 불리는 외적들이오.”

“……암천. 암천이라.”

노인은 작게 뇌까렸다. 근래 들어 강호를 피로 물들이고 있다는 그 이름은 결코 낯설지 않았다.

그와 더불어, 피에 물든 황금빛 갑옷을 걸친 저 사내의 목소리도.

“자네였나?”

뜻 모를 한 마디.

그러나 이 영문 모를 대화에 갈피를 잡지 못하는 반정군과 달리, 금의위 사내는 그 짧은 한마디에 담긴 의미를 알고 있었다.

“그렇소.”

“그렇다면 그날 자네가 저잣거리에서 했던 말과 행동은…….”

“모두 폐하의 뜻으로 이루어진, 황명(皇命)이었소.”

“아.”

노인은 탄식했고, 뒤늦게 사내의 정체를 알아차린 반정군 중 일부는 눈을 부릅떴다.

“설마…….”

“마, 맞아. 저 목소리였어.”

그들은 아직도 생생하게 기억하고 있었다.

수백여 명의 군중 속에서도 또렷하게 들리던 목소리를.

그들의 마음속에 커다란 바위를 던지고 홀연히 사라졌던 어느 죽립 사내를.

“노부는 과거 태사(太師)로서 선황을 섬겼던 이 모라고 하네. 그대의 이름은 무엇인가?”

노인의 물음에, 죽립 대신 황금빛 투구를 걸친 사내가 대답했다.

수십여 년 전, 환관을 멀리하라는 충언을 끊임없이 올리다 모함당하여 관직에서 쫓겨난 노신(老臣)을 향한 예의와 존경을 담아.

“금의위 천호 정호군. 황제 폐하의 명을 전하기 위해 왔습니다.”

공력이 실린 음성이, 새벽 공기를 뚫고 모두의 귓가에 닿았다.

“짐이 불민하여 태평성대를 이루지 못하였고, 불효하여 선황 폐하와 황실의 어른들을 잃어야만 했다. 허나 단 한 번도 불충하지 않았던바. 작금에 이르러 비로소 순리를 바로 잡으려 하니 그대는 황태제(皇太弟) 주표의 깃발을 들고 그대를 따르는 이들과 함께 역적들을 척결하라.”

“……!”

“……!”

공기가 멈췄다. 보이지 않는 충격이 거대한 파도처럼 반정군을 휩쓸었다.

황태제 주표.

모두가 그것이 의미하는 바를 알고 있었다.

천천히 걸음을 옮겨 다가온 정호군의 손에 들린 깃발이, 금실로 수 놓인 용의 옆에 적힌 주표의 이름이 일말의 의심마저 씻어 버렸다.

“아아.”

사방에서 터져 나오는 탄성 속, 노인은 숨을 삼켰다. 주름진 눈가에 차오르는 눈물을 억눌렀다.

그리고 다음 순간, 두 무릎을 꿇고 파르르 떨리는 손으로 황태제의 깃발을 전달받았다.

“명을, 지엄하신 황명을 받드옵니다.”

저 멀리 서쪽으로부터 선명해지는 서광(曙光)과 함께, 금의위와 합류한 수천의 군세가 내지르는 함성이 이른 새벽을 깨웠다.

겁에 질려 있던 백성들을, 이미 뜻을 놓아 버린 충의지사(忠義志士)들을 일으켜 세우고 황도 곳곳에서 아직 끝나지 않은 혈투를 이어 가고 있던 역적들을 덮쳤다.

수만. 아니, 수십만에 달하는 인(人)의 파도가 되어.

“와아아아아!”

“상산왕 전하 천세!”

“황제 폐하, 만만세!”

콰드드득!

“커헉!”

“후퇴, 후퇴하라!”

무수한 비명과 핏물로 점칠 된 새벽.

그렇게 유난히 어둡고 길었던 밤이 끝나고 빛이 밝았을 때, 더 이상의 전투는 벌어지지 않았다.

다만 전의를 상실하고 도처로 흩어지는 반란군들을 추격하는 이들이 내지르는 함성과, 흘러넘치는 기쁨만이 가득할 뿐이었다.

하루. 이틀.

그리고 사흘이라는 시간이 눈 깜짝할 사이에 흘렀을 무렵, 한 사람이 눈을 떴다.
```

## Final English reading copy

```markdown
# Chapter 929

That night was unusually dark and long.

It was long for the soldiers on both sides, who clashed again and again, wielding blazing torches and keen weapons.

It was long for the people, trembling with fear as they waited for the sudden upheaval to end.

*Clang! Clang! Clang!*

“Gah!”

The battle that night was not confined to the Imperial Palace.

The chilling clash of blades and the screams covered the entire imperial capital for hours. Countless people who heard them were reminded of a not-so-distant past: the fourth prince’s coup, which had overturned the Great Nation’s proper order and history from top to bottom.

And amid this utter chaos, some were gripped by greater anger and fear than anyone else.

“These bastards could be chewed to death and it still wouldn’t be enough…!”

“It’s over. The Embroidered Uniform Guard must have discovered us!”

Dozens of people faced one another across a table inside an abandoned shrine, filled with dust and cobwebs. The shadows of a dim oil lamp flickered between them. Their clothes and ages varied widely.

Listening to their cries, an old man suddenly spoke.

“You’re making too much noise.”

His voice was low, but forceful. At once, as if on cue, everyone fell silent and turned to look at him.

His skin was covered in deep wrinkles, and his frame was slight—proof of the long years he had lived.

But his experienced eyes were clear and deep. His clothes showed signs of mending here and there, yet his bearing was perfectly composed. Both told the story of the life he had led.

“Don’t be swept up in the commotion. The path we must take was decided long ago.”

The old man lifted his lukewarm teacup.

He seemed not to care in the least about the trail of torches drawing closer outside, or the great roar of the crowd.

“I don’t know what disaster is unfolding out there, but it’s worked out well for us. Now that chaos has broken out, this is exactly when we must act.”

The time had come.

At the old man’s brief words, some eyes lit up. Others trembled, unable to suppress their fear.

Restoration.

It was why they had gathered here today—and their justification for saving one person alone.

“Now…we must set everything back where it belongs.”

The old man’s eyes flashed with a strength unimaginable at ninety years of age. And with a conviction more unwavering than anyone’s.

“We will drive those cruel, ruthless traitors—who have strayed from what is right and overturned the natural order—out of the Imperial Palace, and raise His Highness Prince Shangshan to the throne with the strength of the people.”

“……!”

“……!”

An unseen surge swept through the shrine like a wave.

Though they had come here with their own resolve and determination, for a moment they had forgotten, in their rising excitement and fear, what the great undertaking they meant to pursue truly signified.

*With the strength of the people. Raise a ruler of the people.*

They looked at one another.

They differed in age, status, and gender.

But now they were comrades in the same boat.

They had each lived their own lives in their own places. Now they had gathered together to set the Great Nation’s enormous ship on the right course.

A few days earlier, an unknown person’s words had lit the fuse hidden deep in their hearts.

“The azure heaven that once shone blue is fading, and dark clouds are rolling in.”

At the tune that suddenly slipped from someone’s lips, a young Confucian scholar spoke as though entranced.

“The storm soon to come will swallow the world.”

“But, people, do not tremble. Do not be afraid.”

An old laborer, his skin darkened by the sun, muttered in a rough voice. In his hand was an axe with a keen, blue-steel edge. Once, he had led an army.

“For there is a mountain, the highest in all the world.”

“There, a stream that never runs dry.”

“Luscious fruit, and beasts that frolic.”

“And a home to keep out the storms, and a forest to provide firewood.”

It could no longer be called the voice of just one person.

Reciting the tune that had wandered through the imperial capital’s marketplaces these past few days, they rose to their feet.

“It can shelter all the people—and more.”

*Step. Creak.*

The old shrine groaned as the people filed out.

But the tune that rang on grew louder and stronger.

“So, people. Do not tremble. Do not be afraid.”

The old man, leading the way with his white robes fluttering, stepped onto the damp earth.

And whenever his slight frame moved along the rugged mountain path, shadows crouched beyond the darkness rose and followed him.

From dozens to hundreds.

From hundreds to thousands.

Before long, they had become an army. In their hands were dirt-stained sickles, and spears, swords, and axes red with rust.

*Step. Step.*

They marched toward the faint light of dawn shining from the east, toward the trail of torches creeping up the mountain like a living dragon.

And the song rising from their lips became a fervent prayer, a mighty roar.

“Go to Mount Shangshan, go to Mount Shangshan.”

Thousands of pairs of solemn eyes gleamed in the darkness.

“Though the raging storm should swallow the Five Sacred Mountains of the Central Plains, it will never dare reach Mount Shangshan.”

*Thud-thud-thud-thud.*

The low mountain trembled. Those torches drawing closer by the moment were likely the punitive force sent by the Emperor, who had realized a restoration was underway.

But…

“The lord of Mount Shangshan is one who has Heaven’s protection!”

They raised their voices even higher.

Regardless of status, they strained their throats, fighting to suppress the fear welling up even now.

On an ordinary day just a few days earlier, a man in a bamboo hat whose identity they did not know had cast a single sentence into their hearts. Now they shouted it with all their strength.

“He is the descendant of the dragon who commands rain and lightning, and a vessel fit for a righteous and benevolent ruler!”

And just as their great shout shook the land around them—

*Whoosh.*

With a gust of wind that felt unusually sharp, a man suddenly appeared through the gray dawn mist and spoke.

“That’s quite a good tune.”

“……!”

“……!”

Everyone’s eyes widened.

The golden armor on him could not be concealed, even beneath the dried blood in several places.

It meant only one thing.

“The Embroidered Uniform Guard…!”

At someone’s groan-like whisper, trembling eyes turned toward the torches undulating a few hundred *jang* below.

The moment suspicion became certainty.

There was no doubt.

Those were the Embroidered Uniform Guards sent by the Emperor to put down the restoration.

And perhaps Prince Shangshan had already…

“You shameless bastards! Aren’t you afraid of Heaven?”

Some of the restoration army, consumed by rage, were about to rush at the man who was clearly an Embroidered Uniform Guard when the old man, who had led them all despite his age, suddenly spoke.

“The blood on your armor—whose is it?”

The restoration army, poised to charge, stopped moving. The man answered in an even voice.

“It belongs to traitors who endangered the ancestral temples and the state.”

“Then who are these traitors you speak of?”

“On the small scale, Wei Zhong, the East Depot’s Seal-Holding Eunuch, and those in league with him. On the larger scale, the foreign enemy called Dark Heaven.”

“……Dark Heaven. Dark Heaven, is it?”

The old man murmured softly. That name, which had recently drenched the martial world in blood, was not unfamiliar to him.

Neither was the voice of the man standing there in bloodstained golden armor.

“Was it you?”

The words were cryptic.

But unlike the restoration army, who could make no sense of this strange exchange, the Embroidered Uniform Guard understood what the old man’s brief question meant.

“It was.”

“Then what you said and did in the marketplace that day…”

“It was all done at His Majesty’s command—the imperial decree.”

“Ah.”

The old man sighed. Some among the restoration army belatedly recognized the man, and their eyes widened.

“Could it be…?”

“Th-that’s right. It was that voice.”

They still remembered it clearly.

The voice that rang out distinctly even among hundreds of people.

The man in a bamboo hat who had cast a great stone into their hearts, then vanished without a trace.

“I am Lee, once Grand Preceptor to the late Emperor. What is your name?”

At the old man’s question, the man—now wearing a golden helmet instead of a bamboo hat—answered.

With the respect due to an elder official driven from his post decades ago after being falsely accused for repeatedly advising the Emperor to keep eunuchs at a distance.

“Jeong Hogun, Thousand Captain of the Embroidered Uniform Guard. I have come to deliver His Majesty the Emperor’s command.”

His voice, charged with internal energy, pierced the dawn air and reached everyone’s ears.

“I was unwise and failed to bring about an age of peace and prosperity; I was unfilial and lost the late Emperor and the elders of the imperial family. Yet I have never once been disloyal. Now, at long last, I seek to set the natural order right. Raise the banner of Crown Prince Zhu Bao, and together with those who follow you, eliminate the traitors.”

“……!”

“……!”

The air stopped.

An unseen shock swept over the restoration army like a giant wave.

Crown Prince Zhu Bao.

Everyone knew what that meant.

Jeong Hogun walked slowly toward them, carrying a banner. Beside the dragon embroidered in gold thread was the name Zhu Bao. At the sight of it, even the slightest doubt vanished.

“Ah…”

As cries of wonder rose all around him, the old man swallowed. He fought back the tears welling in his wrinkled eyes.

Then, in the next moment, he fell to both knees and accepted the Crown Prince’s banner with trembling hands.

“I receive and obey His Majesty’s most solemn imperial command.”

With the light of dawn growing clear in the far west, the roar of thousands who had joined forces with the Embroidered Uniform Guard woke the early morning.

They roused the people who had been paralyzed with fear, and the loyal men who had already lost all hope. Then they fell upon the traitors, who were still fighting bloody battles throughout the imperial capital.

They became a wave of people numbering tens of thousands—no, hundreds of thousands.

“Waaah!”

“Long live His Highness Prince Shangshan!”

“Long live the Emperor!”

*Crack!*

“Gah!”

“Retreat! Retreat!”

That dawn was painted with countless screams and blood.

And when the unusually dark, long night ended and daylight broke, no more battles were fought.

Only the shouts of those pursuing the rebel forces, who had lost the will to fight and scattered in every direction, and their overflowing joy remained.

One day. Two.

Then three days passed in the blink of an eye, and one person opened his eyes.
```
