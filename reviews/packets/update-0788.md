<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0788.txt",
      "sha256": "a0f8af90a1dabe4f974c3a1643be0764d8bd2c4aec740cb0c2c165825ffebca2",
      "bytes": 12682
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "a484272bf1227b6ea583bc82090a211924754738477d7c9557049547f9fd989e",
      "bytes": 931
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "47349c578ce3a378dc53173dec4002c0828b8095d08eadab83cdfaafdabfc433",
      "bytes": 223666
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "025849063cdf1a0b8076990a8341f9f392507073a23443e42318b690e5711e60",
      "bytes": 553
    },
    {
      "path": "characters/Huginn.md",
      "sha256": "1964b618124131fbc0057d494c9d62b6643136a91af00321277f8835cc7da0c3",
      "bytes": 674
    },
    {
      "path": "characters/Michael.md",
      "sha256": "eec3fed77a5b6ed57cfcaacb3a9410dbbc48e73e6236a565669ee0ae1ca788ff",
      "bytes": 820
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "b5425fdf87cec8e5eb27a41f761dcbd2cb589c29a8d93db52afeeaad90f33499",
      "bytes": 645
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "d6274f0e25394a05913c4344b2d4fda7ab36c8422a9c47945d18b0b7f03d3b27",
      "bytes": 243985
    }
  ],
  "estimated_tokens": 8720
}
-->

# Durable State Update — Chapter 788

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 788. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 788. Profile updates may replace only one
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
  "chapter": 788,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 788,
    "continuity_sources": [788],
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
    "Michael Silbert is dead; Huginn was captured alive, and the rest of Michael’s forces were killed or captured.",
    "The World Hunter Federation is established, and Jin Taekyung is its new Alliance Leader.",
    "Jin fell asleep from exhaustion after the battle; he still carries guilt over the deaths.",
    "The Skeleton King is Jin’s friend and ally; he reassures Jin that the deaths were not Jin’s fault.",
    "Felix has begun casting aside the royal conventions he once valued and treats the Skeleton King as a friend.",
    "The system warns of a great fire that could consume the forest, a danger greater than any disease."
  ],
  "continuity_sources": [
    787
  ],
  "open_questions": [
    "What is the great fire the system warns could consume the forest? "
  ],
  "safe_through": 787,
  "temporary_decisions": [
    "Keep magical power distinct from mana."
  ],
  "version": 1
}
```

## Exact glossary matches

| 최민우    | **Choi Minwoo**   |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 살기     | **killing intent**                               |                                                       |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 대격변     | **Great Cataclysm**   |
| 귀가      | **your family**                                                 |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 후긴 | **Huginn** | One of the two ravens associated with Odin in Norse mythology. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 스위스 | **Switzerland** | Country associated with the watchmaker. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 대통령 | **President** | Title for Korea's head of state. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |
| 파리 | **Paris** | The city containing Ares Guild's branch attacked at the chapter's end. |
| 프랑스 | **France** | Country containing Paris and Luxembourg Gardens. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |
| 임마누엘 | **Emmanuel** | The President of France who congratulates Michael Silbert directly. |
| 서울 | **Seoul** | Location announced for the World Hunter Federation's inaugural ceremony. |
| 한국 | **Korea** | Destination of the international Hunters and Guild Masters. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 상인 | 청년 | stranger_to_stranger | Young Brother | formal-polite | A merchant uses 소형제 after noticing the young man's sword, and the young man approves of the address. |
| 청년 | 상인 | stranger_to_stranger | friend | casual and shameless | The young man declares that they should be friends after drinking their Yeoahong. |
| 후긴 | 최민우 | Odin Guild messenger to Ares Guild's new master | Mr. Choi | formal-polite, diplomatic, and threatening | Huginn asks Choi to choose personally whether to stop the Mana Cultivation Method's release. |
| 미카엘 | 후긴 | Odin Guild Master to personally selected fixer | Huginn | formal, familiar, and commanding | Michael calls Huginn by name while inviting him into the study. |
| 후긴 | 미카엘 | loyal retainer to Guild Master | Guild Master | formal-polite and deferential | Huginn reports the Swiss investigation, accepts Michael's orders, and promises to complete the mission. |
| 최민우 | 존슨 | allied Hunter to allied Grand Mage | Mr. Johnson | formal-polite | Minwoo calls out to Johnson during the battle. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 787
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Huginn.md

# Huginn (후긴)

- **Safe through:** Chapter 786
- **Aliases:** None
- **Role:** Huginn is a powerful Odin Guild messenger, trusted field operative, and elite fixer personally selected and trained by Michael.
- **Personality:** Polished, condescending, calculating, overconfident, and absolutely loyal to his Guild Master.
- **Voice:** Formal and gentlemanly in presentation, indirect and theatrical at first, then blunt and coercive when delivering an ultimatum.
- **Relationships:** Huginn serves Odin Guild's Guild Master with absolute loyalty and acts as an adversary to Jin Taekyung and Choi Minwoo.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 787
- **Aliases:** None
- **Role:** Michael Silbert was the former Odin Guild Master, executed by Jin Taekyung after the World Hunter Federation’s first resolution.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 787
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Jin Taekyung's meticulous intelligence and operations lead, a trusted ally and natural leader capable of guiding the reestablished World Hunter Federation.
- **Personality:** Calm, pragmatic, meticulous, and emotionally steady under pressure.
- **Voice:** Measured, professional, and reassuring without minimizing responsibility.
- **Relationships:** A trusted ally and operational adviser to Jin Taekyung, and the maternal grandson of Cheon Taemin.

## Korean source

```text
＃788화



프랑스 파리. 엘리제 궁전.

미식(美食)을 인생의 미덕 중 하나로 꼽는 프랑스인답지 않게, 짧고 간단한 아침 식사를 끝마친 임마누엘 대통령은 소중히 보관해 두었던 시가 상자를 바라보며 감회에 젖었다.

‘드디어 이걸 꺼내는 날이 오다니.’

이미 이십 년 전부터 금연(禁煙)을 이어 오던 임마누엘 대통령이다.

젊었을 적의 그는 주위에서도 알아주던 시가 애호가였지만, 한 사람을 만난 이후 모든 것이 뒤바뀌었다.



‘시가를 좋아한다고 들었네만.’

‘아, 취미로 가끔 즐기고 있습니다.’

‘그렇다면 꽤 값비싼 취미로군. 대부분의 사람들은 정원에 앉아 풀 태우는 일 따위에 매달 만 유로가 넘는 거금을 쏟아붓지 못하거든.’

‘……!’

‘정치를 하고 싶다고 했나? 그럼 시가부터 줄이는 게 좋아. 시간과 건강을 동시에 잡아먹는 몬스터니까. 게다가 기업가 가문 출신의 사치스러운 정치인만큼 물어뜯기 좋은 상대도 없지. 자, 이제 가 보게.’



가문의 인맥과 막대한 로비로 성사된 거물과의 첫 만남은 그렇게 허무하게 끝났다. 시가를 줄이라는, 어처구니없을 만큼 간단한 조언과 함께.

하지만 촉망받던 젊은 변호사 임마누엘은 그 조언을 잊지 않았다.

그는 저택으로 돌아가자마자 수십만 유로의 값어치를 지닌 시가들을 모조리 벽난로에 던져 넣었고, 전보다 훨씬 검소한 삶을 살기 시작했다.

그리고 몇 년 뒤 찾아온 부활절에, 두 마리의 까마귀가 그려진 카드를 전달받았다.



새로 태어난 걸 축하하네.

M. S.



그렇게 임마누엘은 미카엘 실베르트의 선택을 받았고, 이듬해 화려한 스포트라이트를 받으며 프랑스 정계(政界)에 데뷔했다.

그 후?

말해 무엇하겠는가.

임마누엘은 누구보다 승승장구했다.

그가 그 어떤 정치 거물도, 심지어 총리나 대통령조차 함부로 대할 수 없는 확고한 실력자로 자리매김하기까지 걸린 시간은 불과 십 년 남짓이었고, 미카엘 실베르트의 그림자는 모든 걸 뒤덮고도 남았다.



‘이번 대선에 도전하게. 최연소는 아니지만, 최장기 집권의 역사를 새로 쓸 수 있게 도와주지.’



도와주겠다.

미카엘 실베르트의 그 한 마디에, 어느덧 파리를 상징하는 상원의원이자 의회 내 최대정당을 이끄는 당수(黨首)가 된 임마누엘은 직감했다.

이 대선은 시작되기도 전에 끝났다는 것을.

엘리제 궁전의 다음 주인은 바로 그가 되리라는 것을.

그리고 마침내 그 짐작이 현실로 이루어진 날, 임마누엘 대통령은 자신을 찾아온 후원자를 향해 용기 내어 물었다.



‘왜 그 많은 사람 중에 굳이 저를 선택하신 겁니까?’



돌아온 대답은 짤막했다.



‘말을 잘 듣더군.’

‘예?’

‘내가 원하는 건 하나뿐이야. 지금까지 해 왔던 것처럼 절대적인 충성을 바치게. 짖으라면 짖고, 물으라면 물어. 자네의 전임자가 했던 실수를 반복하지 않는다면 막대한 부와 명예는 물론 이 나라를 통째로 그 손에 쥐여 줄 테니.’

‘……!’

‘내게 충성하겠나?’

‘아닙니다. 복종하겠습니다.’



더할 나위 없는 그 대답에 미카엘 실베르트는 소리 내어 웃었고, 자신의 새로운 충견에게 금박으로 장식된 시가 한 상자를 건넸다.



‘이건…….’

‘선물일세. 내 목표가 이루어지는 날, 자네 역시 왕과 다름없는 존재가 될 거야. 이 시가는 그 순간을 위해 아껴 두도록 하게.’



아직도 생생한 그 날의 기억.

시가 상자를 바라보며 상념에 잠겨 있던 임마누엘 대통령은 가슴이 뛰는 것을 느꼈다.

‘왕이라, 왕.’

21세기 현대에서, 그것도 혁명에 미친 이 나라에서 왕이라니.

그야말로 미친 소리다.

하지만 미카엘 실베르트가 하는 말이라면 다르다. 그는 지금껏 수많은 불가능과 상상을 현실로 이루어 낸 사람이니까.

임마누엘 대통령은 문득 떠올렸다. 대격변이라는 혼란의 시기를 발판 삼아, 단숨에 천문학적인 부를 쌓아 올렸던 아버지의 유언을.



‘이 세상에서 벌어지는 모든 일이 투자고 거래다. 상대가 원하는 것이 있다면 아낌없이 내어주어라. 단, 반드시 내준 것 이상을 얻어내야 한다.’



세간에 ‘죽음의 상인’이라 불리며 멸시받던 아버지였지만, 설령 지옥에 떨어졌더라도 별다른 여한은 없을 것이다.

당신의 아들이 누구보다 성공적인 거래를 하는 것을 지켜보았을 테니까.

젊은 변호사 임마누엘은 한 사람에게 복종에 가까운 충성을 바쳤고, 그 대가로 대통령 임마누엘이 되었다.

그리고 곧 대통령을 넘어선 무소불위의 권력을 손에 넣게 될 것이다. 임마누엘 1세라 불러도 부족함이 없을, 그런 막강한 힘을.

“임마누엘 1세…….”

꿈에 젖은 임마누엘 대통령이 몽롱한 얼굴로 중얼거린 그때, 집무실 벽면에 놓여 있던 괘종시계가 울렸다.

뎅. 데에엥.

종소리와 함께 괘종시계에서 튀어나온 새와 난쟁이가 빙글빙글 돌아간다.

시침이 가리키는 숫자를 확인한 임마누엘 대통령이 눈을 깜빡였다.

“정오? 벌써?”

옛 추억에 잠겨 있느라 시간 가는 줄도 몰랐던 모양이다. 임마누엘 대통령은 느릿하게 집무실 책상을 두드리며 생각했다.

‘생각보다 늦어지는군.’

프랑스와 한국의 시차를 생각한다면, 지금쯤 세계 헌터 연맹의 발족식이 열리고 있을 서울은 오후 여덟 시.

혹시나 하는 마음에 스마트폰을 확인해 봤지만, 그가 기다리던 연락은 아직 들어오지 않은 상태였다.

‘하긴. 일찍 끝나는 것이 이상하지.’

다른 자리도 아니고, 세계 헌터 연맹의 첫 발족식이다.

향후 전 세계의 안보를 좌우할 중요한 자리인 만큼, 풀 코스 마라톤만큼이나 회의가 길어지는 건 그리 이상한 일이 아니었다.

물론 미카엘 실베르트를 향한 굳건한 믿음과는 별개로 약간의 초조함이 드는 것은 어쩔 수 없었지만.

똑똑.

갑작스럽게 울려 퍼진 노크 소리에, 임마누엘 대통령이 눈살을 찌푸렸다.

“무슨 일인가?”

닫힌 문 틈새 사이로 수행원의 목소리가 들려왔다.

“식사하실 시간입니다, 대통령 각하.”

“필요 없네. 그리고 내가 직접 호출하기 전까지는 그 누구도 집무실 가까이 들이지 마. 알겠나?”

“예, 그렇게 전달하겠습니다.”

인생에서 가장 중요한 순간을 앞두고 식욕이 있을 리가.

내심 멍청한 수행원을 향해 욕설을 퍼부은 임마누엘 대통령은 손에 쥔 스마트폰을 빤히 내려다보았다.

그리고 망설임 끝에 한 사람의 번호를 터치했다.

뚜우. 뚜. 뚜.

하염없이 이어지는 통화 연결음.

임마누엘 대통령이 애써 초조함을 억누르며 시가 상자를 어루만지고 있던 그때, 마침내 달칵하는 소리와 함께 상대방이 전화를 받았다.

“발족식, 발족식은 어떻게 됐소?”

다짜고짜 던진 물음에, 잠시 침묵하던 상대방이 대답했다.

- 성공적으로 끝났지.

이 얼마나 기다려 왔던 말인가.

임마누엘 대통령은 전신에서 솟구치는 환희를 느끼며 크게 웃었다.

자신도 모르는 사이에 불끈 쥐어진 주먹을 허공에 휘두르며, 그토록 원했던 대답을 들려 준 상대에게 감사를 표했다.

“고맙소! 정말 고맙소! 후긴, 당신도 그간 정말 고생 많았……!”

- 고맙긴. 오히려 내가 더 고맙지.

“뭐?”

그 순간.

임마누엘 대통령은 불현듯 깨달았다.

상대방의 목소리가 평소와는 달리 굵고 거칠다는 것을.

더불어 그 목소리의 주인이, 지금 서울이 아닌 문밖에 서 있다는 것을.

그리고 뒤늦은 깨달음의 대가는, 지금부터 시작이었다.

쾅!

굉음과 함께 수백 여년의 역사를 간직한 집무실의 문이 가루가 되어 흩어진다.

그 너머로 성큼성큼 걸어들어온 반백의 거한이 얼어붙은 임마누엘 대통령을 향해 반갑게 웃어 보였다.

“오랜만이군, 임마누엘. 이 찢어 죽여도 시원치 않을 쥐새끼 같으니.”

“다, 당신은.”

“참 희한하지. 조금 전까지만 해도 삼 초 안에 잠들 수 있을 것 같았는데, 네놈 얼굴을 보니 피곤함이 싹 가시는군. 아마 지금쯤이면 스위스에 있을 존슨도 나랑 같은 기분일 거야. 응?”

척 헤이글은 껄껄거리며 웃었다.

손에 든 후긴의 스마트폰을 뒷주머니에 찔러넣은 그는 석상처럼 굳어 버린 임마누엘 대통령을 향해 말을 이었다.

조금 전까지와는 다른, 마치 무저갱처럼 깊고 어두운 목소리로.

“미카엘 실베르트는 죽었다. 세계 헌터 연맹의 이름으로. 우리가 직접 추대한 새로운 맹주의 손에 의해서.”

“……!”

“자, 이제 네놈이 선택해라. 사지가 부러진 채 끌려 나갈지. 아니면 그 면봉 같은 다리로 걸어 나갈지.”

끝이다. 전부 끝장이다.

지금까지 그가 쌓아 올린 모든 것이, 앞으로의 모든 미래와 함께 무너졌다.

이 믿을 수 없는 현실을 마주한 임마누엘 대통령은 숨 쉬는 것조차 잊은 채 몸을 떨었다.

그리고 수많은 고민과 상념 끝에, 간신히 한 마디를 토해 냈다.

“시, 시가.”

“뭐?”

“시가 한 대만 피우고 가도 되겠소?”

눈을 깜빡이던 척 헤이글이 호탕하게 웃었다.

“시가라, 그거 좋지.”

그리고 곧장 임마누엘 대통령의 얼굴에 쇠뭉치 같은 주먹을 꽂아 넣었다.

뻑! 콰창!

우수수 튀어나온 이빨과 핏물이 허공에 흩날린다. 포탄처럼 튕겨 나간 임마누엘 대통령이 창문을 박살 내며 시야에서 사라졌다.

“개자식. 그걸 말이라고.”

작게 중얼거린 척 헤이글이 창밖을 내려다봤다.

밑에서 대기하고 있던 수십 명의 아레스 길드원들이 하늘에서 뚝 떨어진 임마누엘 대통령의 몸에 포션을 들이붓고 있었다.

“살았나?”

“아, 예. 충분합니다.”

“그럼 됐어. 숨만 붙여 놔.”

“알겠습니다. 그런데 미스터 헤이글. 혹시 다음 행선지는…….”

“신경 쓰지 말게. 우리 임무는 끝났어.”

“그럼 바로 복귀하는 겁니까?”

“아니. 조금만 기다리게. 아직 할 일이 남았으니까.”

척 헤이글은 테이블 위에 곱게 올려진 시가 상자를 열며 흐뭇하게 웃었다.

“아주 중요한 일이지, 음.”

잠시 후, 때아닌 소란에 몰려든 사람들은 볼 수 있었다.

전신이 으스러진 채 실려 나가는 자신들의 대통령과 엘리제 궁전의 부서진 창밖으로 흘러나오는 희뿌연 연기를.

하지만 사람들이 느낄 충격은 그것으로 끝이 아니었다.

두 눈으로도 보고도 믿을 수 없는 이 희대의 범죄 행위를 신고하기 위해 스마트폰을 들었을 때, 그 누구도 예상치 못했던 거대한 폭탄이 세상을 뒤흔들었으니까.



- 긴급 속보) 세계 헌터 연맹 첫 공식 발표, “두 시간 전, 인류를 배신한 미카엘 실베르트와 그 일당을 즉결 처단했으며 지금도 현재 진행 중.”

- 사상 초유의 유혈 사태. 구세주의 핏줄이자, 세계 헌터 연맹의 임시 대변인 Choi, “모든 증거 자료와 함께 진실을 밝히겠다.”

- [Live] 세계 헌터 연맹 공식 기자회견



사상 초유라 불러도 부족하지 않을, 극심한 혼란과 충격 속에서 시작된 기자회견.

그리고 수백 개의 카메라 렌즈를 통해 모두의 앞에 선 최민우가 담담히 말을 이어 가던 그 순간에도, 바람을 탄 민들레 씨처럼 전 세계 곳곳으로 퍼져 나간 신(新) 세계 헌터 연맹의 핵심 인사들은 미카엘 실베르트가 남긴 잡초를 뿌리 뽑았다.

하루. 이틀. 사흘…….

마침내 깊은 잠에 빠졌던 한 청년이 깨어나던 그 날까지도.
```

## Final English reading copy

```markdown
# Chapter 788

Paris, France. The Élysée Palace.

Unlike most French people, who counted fine food among life’s virtues, President Emmanuel had finished a short, simple breakfast. Now he gazed wistfully at a box of cigars he’d kept safely stored away.

*At last, the day has come to take these out.*

President Emmanuel had been a nonsmoker for twenty years.

In his youth, he’d been known to those around him as a cigar aficionado. But everything changed after he met one man.

“I hear you like cigars.”

“Ah, I enjoy one now and then as a hobby.”

“Then that’s quite an expensive hobby. Most people can’t spend over ten thousand euros a month just to sit in their garden and burn weeds.”

“……!”

“You said you wanted to go into politics, didn’t you? Then you’d be wise to cut back on the cigars. They’re a monster that devours both your time and your health. And there’s no easier target to tear apart than a wasteful politician from a family of businesspeople. All right, you may go.”

His first meeting with the powerful man, arranged through his family’s connections and enormous lobbying efforts, ended just like that—with an absurdly simple piece of advice to cut back on cigars.

But Emmanuel, a promising young lawyer, didn’t forget that advice.

As soon as he returned to his mansion, he threw every last one of his cigars—worth hundreds of thousands of euros—into the fireplace and began living a far more modest life.

Then, a few years later, at Easter, he received a card bearing the image of two ravens.

> Congratulations on your rebirth.
>
> M. S.

That was how Emmanuel was chosen by Michael Silbert. The following year, he made his dazzling debut in French politics, basking in the spotlight.

And after that?

What more was there to say?

Emmanuel rose faster than anyone.

It took barely a decade for him to establish himself as a force no political heavyweight—not even a prime minister or president—could treat lightly. Michael Silbert’s shadow was more than enough to cover everything.

“Run in the next presidential election. You won’t be the youngest, but I’ll help you make history as the longest-serving president.”

*I’ll help you.*

At those words from Michael Silbert, Emmanuel—now a senator who embodied Paris and the leader of the largest party in parliament—had a sudden certainty.

The election was over before it even began.

He would be the next master of the Élysée Palace.

And at last, on the day that prediction came true, President Emmanuel mustered the courage to ask the benefactor who had come to see him:

“Why did you choose me, of all those people?”

The answer was brief.

“You listened well.”

“Pardon?”

“I want only one thing: give me your absolute loyalty, just as you have until now. If I tell you to bark, bark. If I tell you to bite, bite. As long as you don’t repeat your predecessor’s mistake, I’ll place not only enormous wealth and honor in your hands, but this entire country.”

“……!”

“Will you be loyal to me?”

“No. I’ll obey you.”

At that flawless answer, Michael Silbert laughed aloud and handed his new watchdog a box of cigars decorated with gold leaf.

“These are……”

“A gift. When my goal is realized, you’ll be as good as a king. Save these cigars for that moment.”

The memory of that day was still vivid.

As President Emmanuel gazed at the box and sank into thought, he felt his heart pound.

*A king. A king.*

A king in the modern twenty-first century—in a country obsessed with revolution, no less.

It was insane.

But when Michael Silbert said it, that was different. He was a man who had made countless impossibilities and wild imaginings come true.

President Emmanuel suddenly recalled the last words of his father, who’d used the chaos of the Great Cataclysm as a springboard to amass an astronomical fortune in no time.

> Everything that happens in this world is an investment and a deal. If someone wants something, give it to them freely. But you must always get back more than you gave.

People had despised his father, calling him the “Merchant of Death.” But even if he had gone to hell, he probably had few regrets.

He must have watched his son make the most successful deal of anyone.

Young lawyer Emmanuel had given one man a loyalty bordering on obedience, and in return he became President Emmanuel.

Soon, he’d possess power beyond the presidency—such overwhelming might that he could rightly be called Emmanuel the First.

“Emmanuel the First……”

President Emmanuel murmured dreamily, lost in his fantasy, when the grandfather clock against the office wall chimed.

*Dong. Dooong.*

With the chimes, a bird and a dwarf popped out of the clock and spun around.

President Emmanuel blinked as he checked the hour hand.

“Noon? Already?”

He must have lost track of time while reminiscing. President Emmanuel slowly tapped the desk in his office and thought:

*It’s taking longer than I expected.*

Taking the time difference between France and Korea into account, it was now eight in the evening in Seoul, where the World Hunter Federation’s inaugural ceremony was likely underway.

He checked his smartphone just in case, but the message he’d been waiting for hadn’t arrived.

*Well, it would be strange if it ended early.*

This wasn’t just any gathering. It was the first inaugural ceremony of the World Hunter Federation.

Given the importance of the event, which would shape the future of security around the world, it was hardly surprising that the meeting was dragging on like a full-course marathon.

Of course, even with his unwavering faith in Michael Silbert, he couldn’t help feeling a little anxious.

*Knock, knock.*

President Emmanuel frowned at the sudden knock.

“What is it?”

An attendant’s voice came through the crack in the closed door.

“It’s time for your meal, Mr. President.”

“I don’t need it. And don’t let anyone near my office until I call for them myself. Understood?”

“Yes, I’ll pass that along.”

How could he have an appetite with the most important moment of his life just ahead?

President Emmanuel cursed inwardly at his dim-witted attendant, then stared down at the smartphone in his hand.

After hesitating, he tapped one person’s number.

*Brr. Brr. Brr.*

The call rang on and on.

President Emmanuel was doing his best to suppress his anxiety as he ran his hand over the cigar box when, at last, there was a click and someone answered.

“How did the ceremony go? The inaugural ceremony?”

After a brief silence, the other person replied.

“It ended successfully.”

The words he’d been waiting so long to hear.

President Emmanuel felt joy surge through his whole body and burst out laughing.

He swung the fist he’d clenched without even realizing it and thanked the man who’d given him the answer he’d wanted so badly.

“Thank you! Thank you so much! Huginn, you’ve been through so much, too—!”

“Thank me? I’m the one who should be thanking you.”

“What?”

At that moment, President Emmanuel suddenly realized.

The voice on the other end was deeper and rougher than usual.

And the owner of that voice wasn’t in Seoul.

He was standing outside the door.

The price for realizing it too late was about to be paid.

*Crash!*

With a thunderous boom, the door to the office, which had stood for hundreds of years, burst into dust.

A broad-shouldered man, his hair half gray, strode through the wreckage and gave the frozen President Emmanuel a friendly smile.

“Long time no see, Emmanuel. You little rat—I could tear you apart and kill you, and it still wouldn’t be enough.”

“You—you’re……”

“Funny, isn’t it? A moment ago, I thought I could fall asleep in three seconds. But looking at your face has driven the tiredness right out of me. Johnson, who should be in Switzerland right now, probably feels the same way. Don’t you think?”

Chuck Hagel laughed heartily.

He shoved Huginn’s smartphone into his back pocket, then continued speaking to President Emmanuel, who stood frozen like a statue.

This time, his voice was as deep and dark as an abyss.

“Michael Silbert is dead. In the name of the World Hunter Federation. By the hand of the new Alliance Leader we chose ourselves.”

“……!”

“Now, you can choose. Do you want to be carried out with every limb broken, or do you want to walk out on those swizzle-stick legs of yours?”

It was over. All of it was over.

Everything he’d built, along with every future he could have had, had collapsed.

Facing this unbelievable reality, President Emmanuel trembled, unable even to remember how to breathe.

After countless thoughts and doubts, he managed to force out a single word.

“C-cigar.”

“What?”

“Would you mind if I smoked one cigar before I go?”

Chuck Hagel blinked, then burst into a hearty laugh.

“A cigar, huh? That sounds good.”

Then he drove a fist like a lump of iron straight into President Emmanuel’s face.

*Wham! Crash!*

Teeth and blood sprayed into the air. President Emmanuel shot away like a cannonball, smashed through the window, and disappeared from sight.

“Asshole. What kind of question was that?”

Chuck Hagel muttered, then looked down through the window.

Dozens of Ares Guild members waiting below were pouring potions over President Emmanuel’s body, which had dropped out of the sky.

“Is he alive?”

“Yes, sir. He’s alive, all right.”

“Good. Just keep him breathing.”

“Understood. But, Mr. Hagel, where are we headed next?”

“Don’t worry about it. Our mission is over.”

“So we’re heading straight back?”

“No. Wait a little. There’s still something to do.”

Chuck Hagel opened the cigar box, set neatly on the table, and smiled with satisfaction.

“Something very important, yes.”

A little while later, people drawn by the unexpected commotion saw their president being carried away, his entire body crushed, and pale smoke drifting out through the broken window of the Élysée Palace.

But that wasn’t the last shock they would face.

When they picked up their smartphones to report this unprecedented crime, an enormous bomb no one could have foreseen rocked the world.

> **Breaking News:** World Hunter Federation’s first official announcement: “Two hours ago, we summarily executed Michael Silbert and his followers, who betrayed humanity. The operation is still ongoing.”
>
> **Unprecedented bloodshed.** Choi, descendant of the Savior and interim spokesperson for the World Hunter Federation: “We will reveal the truth, along with all the evidence.”
>
> **[Live] World Hunter Federation Official Press Conference**

The press conference began amid such confusion and shock that “unprecedented” hardly did it justice.

And even as Choi Minwoo calmly continued speaking before everyone, captured by hundreds of camera lenses, the key figures of the New World Hunter Federation spread across the globe like dandelion seeds on the wind, uprooting the weeds Michael Silbert had left behind.

One day. Two days. Three……

Even on the day a young man finally woke from his deep sleep, they were still at it.
```
