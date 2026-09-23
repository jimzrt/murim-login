<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0897.txt",
      "sha256": "11de8905f0cd27276eddea975d6b831cabad96d1e09e08b13800adb648b017e7",
      "bytes": 12692
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b254e0207a03706a7ac911c927be6ebb11e097dd9159b6c1514c4ec679afe573",
      "bytes": 2009
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b095c036feda74e09729daf1aa6d95a5b05b56fa871d442cbb7c8b98f5da42ef",
      "bytes": 230750
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "cc4561ca839ad6b05a773638cbc9c8d1b265bff2556b3de8a33ce243fa439cc9",
      "bytes": 952
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "14d55d63395199592974009a3d1551b1cbbc0fd43f58c8f35b0cbefcf3523753",
      "bytes": 685
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8ead4207b37bea0c8bdc317b844fae2124946506bd434491dd7489b0ce8d1c7b",
      "bytes": 261385
    }
  ],
  "estimated_tokens": 8935
}
-->

# Durable State Update — Chapter 897

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
1 and safe_through 897. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 897. Profile updates may replace only one
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
  "chapter": 897,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 897,
    "continuity_sources": [897],
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
    "Wei Zhong, Lord Cang Gong and head of the East Depot, was the pledge’s first signer; he survived a severe Internal Injury but has not fully recovered.",
    "A bargain secured Prince Shangshan’s life when he was an infant, at the cost of nearly a hundred loyal officials and their families; the late Emperor formally abdicated, and Cang Gong quieted opposition to the new Emperor.",
    "The Emperor and the restoration faction have faced off for more than a decade, with assassination attempts by both sides but neither the Emperor nor Cang Gong killed.",
    "The Twelve Palaces of the Zodiac are twelve Supreme Peak masters protecting the capital; half belong to Ma Sanbao’s faction, and some stay with Cang Gong.",
    "Jin signed the restoration pledge using only his name, withholding his family and affiliations in case the coup fails; he insists the coup must succeed.",
    "Jin gave Ma a cipher and a location for a messenger to deliver it; he expects Murim Alliance reinforcements for the grand banquet, possibly including the Slaughter Saint or a Ten King.",
    "Ma suspects the Emperor has allied with Dark Heaven and that Baek Yeon and So Gyo are connected to it; these remain unconfirmed allegations.",
    "After a severe flood, rumors about a giant venomous serpent and Prince Shangshan’s supposed influence spread to the palace; the Emperor says the time has come."
  ],
  "continuity_sources": [
    896
  ],
  "open_questions": [
    "Who is the cipher’s intended recipient, and what information does it contain?",
    "Will the expected Murim Alliance reinforcements arrive for the banquet, and who will be among them?",
    "Are Ma’s suspicions about the Emperor, Baek Yeon, and So Gyo’s ties to Dark Heaven correct?"
  ],
  "safe_through": 896,
  "temporary_decisions": [
    "Use “Twelve Palaces of the Zodiac” for 黃道十二宮.",
    "Use “Seal-Holding Eunuch of the East Depot” for 東廠掌印太監."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 소림     | **Shaolin**                      |
| 중원     | **Central Plains**                               |                                                       |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 화산     | **Huashan**            |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 평화 | **Peace Guild** | Guild name. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 선황 | **the late Emperor** | The former Emperor whom Hong Jin served. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 백주 | **baijiu** | Strong distilled liquor ordered at the inn. |
| 숭산 | **Mount Song** | Mountain where Shaolin Temple is located. |
| 창천 | **azure heaven** | The cloudless sky seen by Namgung Ryong. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 오악 | **Five Sacred Mountains** | Mountain grouping that includes Mount Song. |
| 계인 | **Buddhist precept seals** | Seals carved into the foreheads of Shaolin martial monks. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 괴력난신 | **supernatural powers** | Term for extraordinary and unnatural powers. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 시산혈해 | **sea of corpses and blood** | Description of the preceding months of bloodshed. |
| 만족 | **Man people** | An ethnic group mentioned by the Poison Flower Pavilion owner. |
| 묘시 | **the hour of the Rabbit** | Traditional time period following Insi. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 산동 | **Shandong** | Province on the suspected route into Shanxi. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 상산왕 | 황제 | younger brother addressing the Emperor | Your Majesty | deferential royal address | Shangshan addresses the Emperor as 폐하 while pleading for Taekyung. |

## Listed compact profiles

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 896
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is the Emperor’s twelve-year-old youngest younger brother and an exceptionally skilled young swordsman.
- **Personality:** Earnest and compassionate, he takes responsibility for his loyal subjects’ hardship, admires Jin Taekyung, seeks candid counsel, and shows composure beyond his years in the face of death and political danger.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s youngest younger brother; the late Emperor entrusted Hong Jin with his care. Zhu Bao admires Jin Taekyung, seeks to emulate him, and calls him a friend; the Emperor says he will take care of Zhu Bao.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 894
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃897화



그날은 모든 것이 평소와 달랐다.

늘 웃음과 음악이 끊이지 않던 거리는 고요했고, 아직 사라지지 않은 먹구름은 사람들의 머리 위로 그늘을 드리웠으며, 유례없는 폭우로 물이 불어난 운하(運河)는 이 상황을 대변하듯 불안하게 출렁였다.

그리고 그 끝이자 중심에, 황궁(皇宮)이 있었다.

그그그긍.

때는 어스름한 새벽녘, 육중한 쇳소리와 함께 열리는 거대한 철문을 보면서도 사람들은 이상함을 눈치채지 못했다.

황궁의 출입문은 언제나 자시(子時)에 닫히고, 묘시(卯時)에 열렸으니까.

머지않아 곧 동이 트면 여러 조정의 중신들이 황궁으로 향할 테고, 이 아름답고도 위험한 대도시의 주민들은 신분의 고하를 떠나 각자의 위치에서 새로운 하루를 시작할 터였다.

마치 정교하게 맞물린 톱니바퀴처럼.

처음부터 그렇게 정해진 순리라도 있는 듯이.

하지만 천천히 열리는 철문 틈새로 모습을 드러낸 눈부신 광채는, 오늘 하루의 시작이 결코 평소와 같지 않음을 뜻하는 증거였다.

“이, 이보게. 저거 설마…….”

“응?”

여느 때처럼 황궁 앞 대로변에 좌판을 깔고 있던 장사치는 동료 상인의 부름에 무심코 고개를 돌렸고, 이내 뱁새처럼 찢어진 눈을 화등잔만 하게 부풀렸다.

“그, 금의위(錦衣衛)?”

반사적으로 벌어진 입술 사이로 그 한마디가 튀어나온 순간.

“하!”

한목소리로 내지르는 짧은 기합성과 함께, 각자의 준마에 몸을 실은 일천의 금의위가 활짝 열린 철문 사이로 쏟아졌다.

두두두두!

새벽을 깨우는 말발굽 소리.

땅이 울린다. 아직 마르지 않은 빗물과 서늘한 새벽 공기에 가라앉아 있던 먼지가 피어오른다.

마치 하나의 화살처럼 쏘아진 일천의 인마(人馬)는 눈 깜짝할 사이에 황궁 앞 대로변을 가로질렀고, 이내 선두에 선 우두머리의 수신호에 맞춰 사방으로 흩어졌다.

천에서 수백으로. 수백에서 백으로. 백에서 수십으로.

그들은 정해진 바에 따라 분산하고, 또 분산했다.

남들보다 일찍 하루를 시작한 사람들을 이 갑작스러운 상황을 멍하니 지켜보았지만, 황도 전역을 한바탕 휩쓸며 지나간 황금빛 물결의 빈자리에 남아 있는 방(榜)을 보며 그 이유를 깨달았다.



명일(明日). 미시(未時).

황자 탄신(皇子誕辰) 대연회(大宴會). 개(開).



유려한 필체로 천하에 이름을 떨친 황실 서예가가 직접 작성한 수백여 장의 포고문의 첫 줄은 그렇게 시작되었고, 때아닌 수해(水害)로 시름 하고 있던 사람들의 표정은 일그러졌다.

“사흘? 이런 상황에서 무려 사흘이나 그 빌어먹을 연회를 개최한다고?”

“쉿. 목소리 좀 낮추게. 역모죄로 잡혀가고 싶나?”

“역모는 염병할. 평생을 소처럼 일해서 마련한 집에, 세간 살림까지 몽땅 잃은 마당에 뭐가 그리 무섭겠소?”

“옳소!”

“시팔, 민심이고 나발이고 알 거 없다 이건가? 제 자식 태어난 게 우선이다 이거야?”

누군가는 재산을, 누군가는 가족을 잃었다.

그리고 그들 모두는 가족보다 가깝던 이웃이다.

그렇기에 포고문을 읽고 흥분하는 이들을 말리는 사람들의 표정도 그리 좋을 수 없었다.

천자. 혹은 황제.

하늘이 내린 용의 핏줄이자, 만백성을 보듬어 살펴야 하는 지존이 어찌 이럴 수 있단 말인가.

이번 수해로 인해 소중한 것을 잃은 이들은 분노했고, 그런 그들을 지켜보던 또 다른 사람들은 불현듯 깨달았다.

지금 눈 앞에 펼쳐진 이 광경이, 분노하는 저들의 모습이 언젠가 자신에게 찾아올 수도 있다는 것을.

‘이 나라는…… 뭔가 잘못됐다.’

처음에는 그저 우러러만 보았다. 그들에게 있어 천자란 꿈에서도 볼 수 없는 높으신 분이었고, 하늘 위에 뜬 태양이나 다름없었으니까.

그러나 작금의 황제는 천륜(天倫)을 어긴 자였다.

제 부모를, 형제를, 수많은 충신과 그 일가를 몰살시키며 황위에 오른 인면수심의 괴물.

그렇기에 천심(天心)이 떠났을 것이다.

천하에 모르는 이가 없는 바로 그 소림사에서는 명망 높은 고승들이 죽어 나갔고, 사천에서는 물경 수천에 달하는 무림인들이 백주대낮에 시산혈해를 일으켰다.

그뿐인가.

호북에서는 이무기가 미쳐 날뛰었다는 믿을 수 없는 소문이 들려왔고, 척박한 남만 땅에 살아가던 야만인들은 거대한 군세를 이루어 북상(北上)했다는 흉흉한 이야기가 나돌았다.

거기에 더해 지난 일백 년 동안 쥐 죽은 듯이 엎드려 있던 북방의 이민족들이 준동의 기미를 내비치고, 이제는 유례없는 폭우가 황도를 덮치기까지 했다.

그렇다면 이와 같은 일련의 재앙들이 의미하는 바는 무엇인가.

‘하늘이 이 나라를 버렸다. 아니, 황제를 벌하려 한다.’

지금이 등 따뜻하고 배부른 태평성대(太平聖代)였다면 그 누구도 이와 같은 소문과 미신에 신경 쓰지 않았을 것이다.

열심히 흘린 땀의 대가로 얻은 집이, 사랑하는 가족이, 풍족한 양곡과 재물이 있다면 그것만으로 만족했을 테니까.

지난 십여 년간, 천하는 서호(西湖)의 수면처럼 잔잔했고 백성들은 새로운 천자의 통치에 생각만큼 큰 불만을 표하지 않았다.

천륜을 저버린 천자의 행보를 비난할 수는 있을지언정, 먹고 사는 것에는 그리 큰 차이가 없었으니까.

아니, 오히려 선황 시절의 평화로움 속에서 날뛰던 탐관오리들이 역모에 휘말려 숙청당하자 잘 죽었다며 좋아하는 이들도 있었다.

하지만 이제는 아니었다.

불과 이 년 남짓한 짧은 시간 동안 괴력난신(怪力亂神)이라 부를 수밖에 없는 기이한 현상들이 천하 곳곳에서 벌어졌고, 백성들에게 동정과 사랑을 받는 어린 왕이 황도에 소환되었으며, 신음하는 백성들을 외면한 천자는 후사를 축하하기 위해 막대한 재물을 쏟아부어 연회를 개최했다.

“이것이, 정녕 이것이 옳은 행동인가?”

낡은 죽립을 깊게 눌러쓴 어느 사내의 뇌까림은, 모두의 마음을 대변하고 있었다.

“민심이 곧 천심이요, 천심이 곧 민심이다. 한데 황상은 어찌하여 하늘과 백성을 저버린단 말인가.”

어느새 고요해진 좌중들 사이로 또렷하게 울려 퍼지는 목소리.

보이지 않는 공기가 무겁게 장내를 짓눌렀다.

그 숨 막히는 침묵 속에서 사람들은 이를 악물고 눈을 빛냈다. 어째서인지 유달리 선명하게 들려오는 사내의 목소리에 신경을 곤두세웠다.

“푸르른 창천의 기운이 쇠하고, 어두운 먹구름이 몰려오고 있구나. 머지않아 불어닥칠 비바람은 머지않아 천하를 집어삼킬 터.”

희한한 일이었다.

수백여 명이나 되는 사람들이 한자리에 모여 있음에도, 누구 하나 입을 떼지 않은 채 사내의 말에 귀를 기울이고 있었다.

평생을 까막눈으로 살아온 거친 인부. 하루 벌어 하루 먹고 사는 길거리 장사치. 아마도 살아온 세월만큼이나 높은 학식을 쌓아왔을 늙은 유생까지도.

그만큼 사내의 말과 목소리에는 알 수 없는 현기(玄機)와 신념이 깃들어 있었고, 모두의 마음을 끌어들이기에 충분했다.

그와 더불어, 묻지 않을 수 없는 궁금증도 함께.

“저어, 나리. 말씀하시는 도중에 송구스럽지만 이놈이 뭐 하나만 여쭤봐도 되겠습니까요?”

척 봐도 투박해 보이는 인부의 조심스러운 모습에, 죽립 사내가 고개를 끄덕였다.

“말씀하시오.”

“다름이 아니오라, 마지막에 말씀하셨던 그 비바람을 피하려면 소인이 어찌해야겠습니까?”

“산으로 향하시오.”

“예?”

한 치의 망설임도 없는 대답에 눈을 동그랗게 뜬 인부를 향해, 죽립 사내는 천천히 말을 이었다.

“천하에서 가장 높은 산을 찾아 그곳에 몸을 의탁하시오. 그곳에는 마르지 않는 개울이 있고, 탐스러운 열매와 뛰노는 짐승이 있으며, 집과 장작이 되어 줄 숲 또한 있으니 만백성을 품고도 남을 거요.”

처음 질문을 던진 인부는 어안이 벙벙했다.

아니, 이 자리에 모여 있는 대부분이 마찬가지였다.

천하에서 가장 높은 산이라니?

만백성을 품고도 남을 만큼 거대하고, 식량과 자원이 풍부한 산이 도대체 세상천지 어디에 있단 말인가.

인부가 잠시 할 말을 찾지 못하는 사이, 성질 급한 다른 이가 불쑥 입을 열었다.

“뉘신지는 모르겠으나 깊은 수행을 쌓으신 고인이신 것 같은데, 혹시 중원오악(中原五岳)을 말씀하시는 겁니까?”

몇몇 사람들이 아, 하는 탄성과 함께 고개를 끄덕였다.

천하에서 가장 높고 영험한 기운을 품었다는 다섯 개의 명산(名山)이라면, 충분히 그럴만하다는 수군거림도 함께.

“말씀하시는 그 산이 중원오악 중 어딥니까? 하남의 숭산(崇山)? 산동의 태산(泰山)? 섬서의 화산(華山)? 그도 아니면…….”

“모두 틀렸소. 본인이 말한 건 중원오악이 아니오.”

“예? 그게 무슨, 중원오악이 아니라면 도대체…….”

담담한 동시에 단호한 사내의 대답에 사람들의 말문이 막힌 그 순간. 어디선가 불쑥 늙수그레한 목소리가 들려왔다.

“한 곳이 남아 있지. 아니, 처음부터 그곳만이 유일했어.”

좌중의 시선이 모두 한 방향을 향해 쏠렸다.

빛바랜, 그러나 정갈한 의복을 걸친 늙은 유생이 우중충한 하늘을 보며 혼잣말처럼 뇌까렸다.

“상산(上山).”

“……!”

그 말에 담긴 의미를 알아차린 소수의 사람들은 눈을 부릅떴지만, 대부분은 여전히 혼란스러워했다.

적어도 늙은 유생의 뒷말이 들려오기 전까지는.

“그래, 그곳이라면 만백성을 품을 수 있겠지. 그 어떤 비바람도 중원오악을 집어삼킬지언정 감히 상산에는 닿지 못할 걸세. 그 산의 주인은 하늘의 보살핌을 받고 있고, 비와 낙뢰를 다스리는 용의 후손이니.”

순간, 세상이 멈춘 듯했다.

그 자리의 모든 이가 석상처럼 굳은 채 서로를 바라보았고, 이내 다 함께 같은 결론에 도달했음을 깨달았다.

상산.

중원오악보다 높고 넓으며, 만백성을 품을 수 있는 산.

그리고 하늘의 보살핌을 받는 용의 핏줄. 상산의 주인.

왜 몰랐을까. 어찌 이토록 멍청했을까.

사내는 처음부터 산 그 자체를 말한 것이 아니었다. 그의 한 마디 한 마디는 이 혼란스러운 천하를 품을 수 있는 한 사람을 가리키고 있었다.

‘상산왕(上山王)……!’

마치 한 줄기 벼락이 정수리를 관통한다면 이런 기분일까.

그들 모두는 감전당한 사람처럼 전신을 부르르 떨었다.

입을 벌린 채. 이를 악문 채. 주먹을 불끈 쥐고, 뜨겁게 달아오른 머릿속을 가라앉히기 위해 안간힘을 쓰며.

그러나 동시에, 지금껏 상상하지 못했던 미래를 떠올리며.

‘만약, 만약 상산왕 전하께서 보위에 오르신다면.’

이미 천심은 떠났고, 민심은 흔들린다.

그리고 과거 거대하고도 잔혹했던 숙청 속에서 살아남은 한 아이는 자신이 첫울음을 터트렸던 이곳으로, 황도로 돌아왔다.

그렇다면 이는 운명인가, 우연인가. 혹은 이미 한 번 천륜을 거스른 황제의 또 다른 흉계인가.

그도 아니라면…….

하늘이 내린 천명(天命)인가.

사람들은 감히 입을 열 엄두도 내지 못한 채 천천히 고개를 돌렸다.

이 의문에 대한 대답을 듣기 위해.

이 거대한 충격을 자신들에게 던져준 장본인을 마주하기 위해.

하지만 다음 순간, 그 기대와 흥분은 와르르 무너져 내렸다.

조금 전까지만 하더라도 죽립 사내가 서 있던 그곳은 텅 비어 있었다.
```

## Final English reading copy

```markdown
# Chapter 897

That day, everything was different from usual.

The streets, where laughter and music never seemed to stop, were quiet. The clouds that had yet to clear cast shadows over everyone’s heads, and the canals, swollen by unprecedented rainfall, churned uneasily as if reflecting the state of things.

At the end of it all, and at its center, stood the imperial palace.

Rumble.

It was the dim hour before dawn. Even as the massive iron gates swung open with a heavy metallic groan, no one noticed anything strange.

The imperial palace gates always closed at the hour of the Rat and opened at the hour of the Rabbit.

Before long, dawn would break. Ministers from the various courts would make their way to the palace, while the people of this beautiful, dangerous metropolis—high and low alike—began another day in their own places.

Like precisely meshing gears.

As if things had been set in motion that way from the start.

But the dazzling light that appeared through the slowly opening gates was proof that this day was not beginning as usual.

“H-Hey. Is that…?”

“Hm?”

A vendor who had set up his stall along the main road in front of the palace, as usual, turned at the call of a fellow merchant. His narrow eyes swelled wide.

“T-The Embroidered Uniform Guard?”

The moment those words slipped between his reflexively parted lips—

“Ha!”

With a short battle cry shouted in unison, a thousand Embroidered Uniform Guards mounted on their fine steeds poured through the wide-open gates.

Thud-thud-thud-thud!

Hooves thundered, waking the dawn.

The ground shook. Dust, settled by the cool morning air and rainwater that had yet to dry, rose into the air.

The thousand riders shot forward like a single arrow, racing across the main road in front of the palace in the blink of an eye. At a hand signal from the commander at the head of the formation, they scattered in every direction.

From a thousand to hundreds. Hundreds to a hundred. A hundred to dozens.

They split up, then split up again, exactly as planned.

The people who had started their day early watched this sudden turn of events in a daze. But when they saw the notices left behind by the golden tide that had swept across the entire capital, they understood why.



Tomorrow. The hour of the Goat.

The grand banquet for the imperial prince’s birthday. Begins.



That was how the first line of the hundreds of proclamations began, each written by the imperial court calligrapher whose elegant handwriting was renowned throughout the realm. The faces of the people already suffering from the untimely flood twisted with anger.

“Three days? He’s holding that damn banquet for three whole days in a situation like this?”

“Shh. Keep your voice down. Want to get arrested for treason?”

“Treason, my ass. We’ve worked like oxen our whole lives to buy a house, and now we’ve lost that and every last one of our belongings. What’s there to be afraid of?”

“Right!”

“Fuck, is it to hell with what the people think? His own kid’s birthday comes first, is that it?”

Some had lost their property. Others, their families.

And they were all neighbors who had been closer than family.

So the people trying to calm those furious at the proclamation didn’t look happy, either.

The Son of Heaven. Or the Emperor.

How could the supreme ruler, descended from the dragon appointed by Heaven and charged with caring for all his subjects, do such a thing?

Those who had lost what they treasured in the flood were furious. And the people watching them suddenly realized that they too might one day be standing there, furious over their own losses.

*This country… something’s gone wrong.*

At first, they had done nothing but look up to him. To them, the Son of Heaven was someone so exalted they couldn’t even imagine seeing him in a dream, no different from the sun shining high above the sky.

But the current Emperor was a man who had defied the natural order.

A heartless monster who’d seized the throne after wiping out his parents, his siblings, and countless loyal officials and their families.

And so Heaven’s favor must have turned away from him.

At the Shaolin Temple, known to everyone under Heaven, eminent monks had been dying. In Sichuan, thousands of martial artists had turned the broad daylight into a sea of corpses and blood.

And that wasn’t all.

Unbelievable rumors had reached them from Hubei of an imugi gone on a rampage. There were also sinister tales of the barbarians who lived in the harsh lands of Nanman forming a massive army and marching north.

On top of that, the northern tribes, which had lain low and silent for the past hundred years, were showing signs of unrest. And now unprecedented rainfall had struck the capital.

What could this string of disasters mean?

*Heaven has forsaken this country. No—the heavens are trying to punish the Emperor.*

If these had been peaceful, prosperous times, no one would have paid attention to rumors and superstitions like these.

If they had houses earned through hard work, beloved families, and ample grain and wealth, that alone would have been enough.

For more than a decade, the realm had been as calm as the waters of West Lake, and the people hadn’t voiced much displeasure with their new Son of Heaven—not as much as one might have expected.

They could condemn the Son of Heaven for defying the natural order, but their lives and livelihoods hadn’t changed all that much.

No—in fact, some had cheered when corrupt officials who’d run rampant during the late Emperor’s peaceful reign were caught up in the treason case and purged. Good riddance, they’d said.

But that was no longer the case.

In barely two years, strange events that could only be called supernatural powers had taken place all over the realm. A young prince beloved by the people had been summoned to the capital, and the Son of Heaven, turning his back on his suffering subjects, had spent a fortune to hold a banquet celebrating his offspring.

“Is this truly… is this really the right thing to do?”

The mutter of a man in a worn bamboo hat pulled low over his face spoke for everyone.

“Public sentiment is Heaven’s will, and Heaven’s will is public sentiment. So why has His Majesty turned his back on Heaven and his people?”

His voice rang clearly among the crowd, which had fallen quiet.

The invisible air pressed down on them, heavy and still.

In the suffocating silence, people clenched their teeth and their eyes shone. For some reason, they strained to hear every word of the man’s voice, which sounded unusually clear.

“The azure heaven’s power is waning, and dark clouds gather. The storm that will soon descend will soon swallow the realm whole.”

It was strange.

Though hundreds of people had gathered in one place, not a single one spoke. They all listened to the man.

The rough laborer who had spent his entire life unable to read. The street vendor who lived day to day. Even the elderly Confucian scholar, whose learning was likely as extensive as the years he’d lived.

The man’s words and voice held an inexplicable, profound insight and conviction. They were more than enough to draw everyone in.

Along with a question they couldn’t help asking.

“Um, sir. Forgive me for interrupting, but may this lowly man ask you something?”

At the laborer’s cautious approach, rough as he looked, the man in the bamboo hat nodded.

“Go ahead.”

“If it’s not too much trouble, what should a poor man like me do to escape the storm you mentioned?”

“Go to the mountain.”

“What?”

The laborer’s eyes widened at the answer, given without a hint of hesitation. The man in the bamboo hat went on slowly.

“Find the highest mountain in the realm and seek shelter there. It has a stream that never runs dry, luscious fruit and wild animals, and a forest that can provide houses and firewood. It is more than large enough to shelter all the people under Heaven.”

The laborer, who’d asked the first question, was dumbfounded.

As was most of the crowd gathered there.

The highest mountain in the realm?

Where in the world was there a mountain so vast it could shelter everyone, with an abundance of food and resources?

While the laborer searched for words, another man, more impatient, blurted out,

“I don’t know who you are, but you seem like a master who’s cultivated deeply. Do you mean the Five Sacred Mountains of the Central Plains?”

A few people nodded with a soft “Ah.”

The five famous mountains said to be the highest in the realm and filled with sacred energy—if he meant those, then it would make sense, they murmured.

“Which one of the Five Sacred Mountains do you mean? Mount Song in Henan? Taishan in Shandong? Huashan in Shaanxi? Or perhaps…”

“You’re all wrong. I didn’t mean the Five Sacred Mountains of the Central Plains.”

“What? What do you mean? If not the Five Sacred Mountains, then what—”

The man’s answer was calm but firm, and the crowd was left speechless. Just then, an elderly voice suddenly spoke from somewhere.

“There’s one place left. No, from the very beginning, it was the only place.”

Everyone’s gaze swung in the same direction.

An elderly Confucian scholar in faded but neat clothes gazed at the gloomy sky and murmured, almost to himself,

“Shangshan.”

“……!”

A few people understood what those words meant, and their eyes widened. Most remained confused.

At least, until the old scholar continued.

“Yes. That place could shelter all the people under Heaven. No matter how fiercely the storm swallowed the Five Sacred Mountains of the Central Plains, it would never dare reach Shangshan. The mountain’s master is under Heaven’s protection, a descendant of the dragon who commands rain and lightning.”

For a moment, it was as if the world had stopped.

Everyone there stood frozen like statues, looking at one another. Then, together, they realized they’d all reached the same conclusion.

Shangshan.

Higher and wider than the Five Sacred Mountains of the Central Plains, a mountain capable of sheltering all the people under Heaven.

And the dragon’s blood under Heaven’s protection. The master of Shangshan.

Why hadn’t they realized it? How could they have been so foolish?

The man hadn’t been talking about the mountain itself from the beginning. Every word he’d said pointed to one person who could shelter this chaotic realm.

*Prince Shangshan…!*

Was this what it felt like to be struck right through the crown of your head by a bolt of lightning?

Everyone’s whole body trembled as if they’d been electrocuted.

Mouths agape. Teeth clenched. Fists balled, as they fought to cool their heads, burning hot with excitement.

And yet, at the same time, they imagined a future they’d never dared picture before.

*What if… what if His Highness Prince Shangshan ascended the throne?*

Heaven’s favor had already turned away, and the people’s hearts were wavering.

And the child who’d survived that vast, brutal purge in the past had returned to the capital, to the very place where he’d let out his first cry.

Was this fate, or coincidence? Or was it another sinister plot by an Emperor who had already defied the natural order once?

Or perhaps…

Was it the Mandate of Heaven?

Daring not even to speak, the people slowly turned their heads.

They wanted an answer to that question.

They wanted to face the man who’d dropped this enormous shock on them.

But the next moment, all their anticipation and excitement came crashing down.

The place where the man in the bamboo hat had stood just moments ago was empty.
```
