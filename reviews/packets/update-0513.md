<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0513.txt",
      "sha256": "caaa3e8a66f1cb46e45dda5b54a8ce466fbed62266fa5c7cd786a2b02ac31e4d",
      "bytes": 13630
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "8dbb6023c483a55a4c543a828250ea3805473fef7a94f445ee4885d2cda5017a",
      "bytes": 3701
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "c204be7cea3e939d1cb4ec9415566ec63b805e18aa46da5b7eab6a1691676800",
      "bytes": 163748
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "1d94818c2e72ed4532ec49aff490fb040134443f1750000fe111f8bebbc010c8",
      "bytes": 553
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "d55e1b559aab842913d6859ee4f86aff71a3a23ad89553d949f27b82a0965ae8",
      "bytes": 154523
    }
  ],
  "estimated_tokens": 9370
}
-->

# Durable State Update — Chapter 513

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 513. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 513. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 513,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 513,
    "continuity_sources": [513],
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
    "Jeok Cheongang's Heart Demon and the dark memories binding him have been expelled; he has entered a new realm and achieved Returned to Youth.",
    "Mungyeong is the Slaughter Saint and former Divine Physician, a Returned to Youth Supreme Peak master and the greatest assassin in history; Mu Song and five Water Dragon Stronghold subordinates know he is exceptionally powerful but not that he is the Slaughter Saint.",
    "Mungyeong is training Taekyung to refine the stability and precision of the violent internal energy produced by the Fire Gate Divine Technique through Rising on Duckweed, Crossing Water.",
    "Zhuge Feng's Demon-Sealing Formation blocks all mana from the exposed Gate by drawing in natural qi, but whether it is permanent and repeatable remains unresolved.",
    "Jang Taebo is the Jin Family of Taiyuan's Master of Ironcraft Hall and is summoning renowned artisans to process the Water God Dragon's remains.",
    "The New Murim Alliance has been publicly announced from Mount Song; Shaolin, Huashan, the Nine Sects and One Gang, and the Five Great Families are moving to join it.",
    "Taekyung has abandoned the shark shortcut and intends to reach Henan by his own strength.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Mukyung remains secluded in the training hall after losing to Cheongpung, refusing to emerge until he achieves a great accomplishment.",
    "Mu Song wants to aid the Murim Alliance, but the Seafaring King alone decides the Yangtze River Channel League's major matters; the League and Green Forest Alliance may become rear threats.",
    "The North Sea Ice Palace remains isolationist, while Jeok Cheongang believes the Nanman Beast Palace will probably support orthodox Murim because of its historical goodwill toward the Fire Gate Clan.",
    "A stranger capable of walking across the Yangtze's surface has approached Taekyung after he released the trained sharks."
  ],
  "continuity_sources": [
    512
  ],
  "open_questions": [
    "Will the Demon-Sealing Formation remain effective permanently, and can equivalent formations be installed repeatedly if more Gates appear?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "Will the Nanman Beast Palace, North Sea Ice Palace, Yangtze River Channel League, and Green Forest Alliance support, ignore, or oppose the New Murim Alliance?",
    "Who is the stranger walking across the Yangtze, and why has he approached Taekyung?"
  ],
  "safe_through": 512,
  "temporary_decisions": [
    "Render 새외무림 as Outer Murim, 새외 as Outer Lands, 북해빙궁 as North Sea Ice Palace, 야수묘왕 as Beast Miao King, and retain Nanman Beast Palace for 남만야수궁.",
    "Render 소뢰음사 as Small Thunderclap Temple, 광풍사 as Mad Wind Society, 포달랍궁 as Potala Palace, 오독문 as Five Poisons Sect, 독곡 as Poison Valley, 천축 as India, and 갠지스강 as Ganges River.",
    "Render 파사국 as Persia, 회교도 as Muslims, 영웅건 as hero headband, 대막 as great desert, 귀염권 as Ghost Flame Fist, and 장성 as Great Wall.",
    "Retain sa-eo for 사어, shark for 상어, Old Master for 노야, this old man/I for 노부, Shark Water-Ski Team for 수상스키단, and swift ship for 쾌조선.",
    "Render 신 무림맹 as New Murim Alliance, 하후검가 as Hahou Sword Family, and 사마외도 as demonic and heterodox arts."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 소림     | **Shaolin**                      |
| 삼류     | **Third Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 낭인     | **wandering martial artist**                     |                                                       |
| 정파     | **orthodox faction**                             |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 상태               | **Status**                     |
| 하남     | **Henan**              |
| 감숙     | **Gansu**              |
| 본문      | **our sect / this sect**                                        |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소저      | **Young Lady**                                                  |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 은자 | **silver nyang** | Silver currency unit. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 하남성 | **Henan Province** | Province containing Luoyang. |
| 숭산 | **Mount Song** | Mountain where Shaolin Temple is located. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 서협 | **Xixia** | Place in southwestern Henan where the Yangtze tributary ends. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 511
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

## Korean source

```text
＃513화



장강의 지류와 맞닿은 하남성 서협(西峽)은 오늘도 수많은 이들로 인산인해였다.

나루터는 크고 작은 선박으로 가득 찼고, 갖가지 물건을 쌓아놓은 장사치들은 눈에 불을 켜고 흥정을 벌였다.

“자. 싸다, 싸! 정력에 좋은 사향(麝香)이 은자 한 냥!”

“그딴 거 필요 없소.”

“거기 지나가시는 아리따운 소저! 면경(面鏡) 하나 필요하시지 않습니까!”

“그딴 거 안 사요.”

“……지랄 같은 연놈들일세.”

온갖 소음이 울려 퍼지는 저잣거리.

그러나 어떤 장소의 분위기를 좌우하는 것은 결국 그 장소에 어떤 종류의 사람들이 모여 있느냐다.

그런 의미에서 때마침 지나가던 젊은 무인 하나를 습관처럼 붙잡은 장사치는 상대를 잘못 고른 셈이었다.

“이보시오. 보아하니 숭산으로 향하시는 무림 협객 같으신데, 잘 벼린 병장기가 필요하지 않…… 헉!”

변죽 좋게 말을 이어 가던 장사치가 헛숨을 삼켰다.

맨 처음 그의 시선을 잡아끌었던 잘생긴 얼굴은 이제 눈에 들어오지도 않았다.

젊은 무인의 검푸른 비단 무복에 검은 실로 아로새겨진 세 글자와 용 무늬를 본 순간, 장사치는 자신도 모르게 신음 같은 외침을 토해 냈다.

“흐, 흑룡마문(黑龍魔門)!”

“……!”

그리 크지 않은 외침이었음에도, 흑룡마문이라는 네 글자는 시끌벅적하던 대로(大路)를 단번에 침묵의 구렁텅이로 밀어 넣기에 충분했다.

“흐, 흑룡마문이라면.”

“틀림없네. 감숙성(甘肅省)에서 맹위를 떨치고 있다는 그 사파 놈들이야.”

“전날 늦게 하남에 당도했다는 소문은 들었는데…… 설마하니 입맹(入盟)을 위해서인가.”

침묵이 번지는 것은 순식간이었다.

목청껏 소리치던 장사치들과 인근을 배회하던 양민들, 그리고 병장기를 차고 무리 지어 이동하던 무림인들까지.

모두 하던 일을 멈추고 외침이 들려온 곳을 향해 시선을 집중했다.

그리고 수많은 이들의 이목 속에서, 흑룡마문의 젊은 무인은 상인을 향해 빙긋 웃어 보였다.

“상인치고는 눈썰미가 제법이구려. 본문의 표식까지 알아볼 정도면.”

“그, 그것이…….”

“무림과는 별 연관이 없어 보이는데. 본래 감숙 사람이신가? 아니면…… 손님으로 받은 삼류 칼잡이들이 늘어놓은 풍월을 주워들었거나.”

장사치의 어깨너머, 좌판에 가지런히 진열된 각종 병장기를 힐끗 바라본 젊은 무인이 혀를 찼다.

“하나같이 줘도 안 가질 싸구려뿐이로군. 어디, 가장 좋은 것으로 하나 줘 보시오.”

“예, 예?”

“당신이 장사치라는 걸 깜빡했구려. 그럼 가장 좋은 것 말고, 가장 비싼 것으로.”

“아, 알겠습니다.”

장사치는 후들거리는 손으로 가장 깊숙한 곳에 넣어 둔 철궤(鐵櫃) 하나를 꺼내어 열었다.

그럴듯한 검갑도 없이 덩그러니 놓인 한 자루의 검을 확인한 젊은 무인이 휘파람을 불었다.

“호, 이런 곳에 있을 만한 물건이 아닌 듯한데.”

두 사람을 주시하던 이들, 특히 무림인들은 젊은 무인의 말에 자신도 모르게 고개를 끄덕였다.

비록 상당히 오래되어 보이기는 했으나 검신은 오색 창연한 빛을 띠고 있었고, 날 역시 예리함을 잃지 않은 상태였다.

능히 명검(名劍)이라 불러도 손색이 없는 물건.

몇몇 무림인의 눈동자에 탐욕이 어리는 것을 느낀 장사치가 잔뜩 어깨를 움츠렸다.

“도, 돌아가신 선친께서 물려주신 겁니다.”

“선친께서 무림인이었소?”

“그, 그럴 리가 있겠습니까. 다만 어찌 연이 닿아 검을 소유하게 되셨는데, 남들에게는 비밀로 하고 대대로 가보로 삼으라는 말씀만…….”

“그럴 만도 하군. 이 정도 검이라면 탐내는 자가 한둘이 아니었을 테니.”

탐욕이 과하면 피를 부르는 법.

대부분의 무림인은 명검을 얻기 위해 은자 수백 냥을 지불하는 대신 무력으로 빼앗는 걸 선택할 것이다.

명검을 살 만한 은자를 마련하는 것보다, 싸구려 철검을 들이대는 것이 훨씬 효과적이니까.

“선친께서 퍽 현명한 분이셨구려.”

“예, 예에.”

“하지만 당신은 선친의 지혜를 물려받지 못한 모양이오. 이런 물건을 턱 하니 내놓은 걸 보면.”

“그, 그건……!”

말을 잇지 못하는 장사치의 모습에, 젊은 무인은 피식 실소를 흘렸다.

그는 장사치가 차마 말하지 못하고 속으로 삼킨 말이 무엇인지, 이미 정확히 꿰뚫고 있었다.

상대는 흑룡마문에 속한 사파 무림인.

당장 목에 칼이 들어왔으니 앞뒤 생각할 겨를이 없었을 것이다. 어설프게 다른 물건을 내놓았다가 목이 날아갈 수도 있겠다는 두려움이 장사치의 사고를 마비시킨 거다.

장사치에게는 난생처음 겪는 일이었겠지만, 젊은 무인에게는 익숙한 상황이었다.

“이해하오. 나를 마주한 대부분의 이들은 당신처럼 생각하고 행동하거든.”

꿀 먹은 벙어리처럼 입을 다문 장사치를 위아래로 훑은 젊은 무인이 말을 이었다.

“해서, 내 당신을 구해 주겠소.”

장사치의 눈동자에 의혹이 스쳤다.

“그, 그 말씀은…….”

“내가 값을 치르고 가져가겠다는 말이지.”

“아!”

장사치의 얼굴이 환하게 밝아졌다.

그렇지 않아도 그의 속마음은 새카맣게 타들어 가던 중이었다.

우선 살고 보자는 생각에 물건을 꺼내 놓긴 했는데, 명검의 존재를 눈으로 확인한 이들이 한둘이 아니었다.

눈앞의 젊은 무인이 떠난다면 근본 없는 떠돌이 낭인과 좀도둑이 냄새를 맡고 모여들 것이 분명했다.

하지만 이 자가 검을 사 간다면 모든 것이 해결된다.

물론 값으로 받은 은자를 탐낼 놈들이 있으니 가까운 시일 내에 근방을 떠나야겠지만, 목숨도 지키고 넉넉한 재산도 챙겨 타지에서 풍요로운 삶을 누릴 수 있을 것이다.

계산을 끝마친 장사치는 즉각 허리를 굽혔다.

“대, 대협께서 그리해 주신다면 정말 바랄 것이 없겠습니다!”

“영 맹탕은 아니군.”

피식 웃은 젊은 무인이 품에서 꺼낸 전낭을 좌판 위로 던졌다.

철그럭. 묵직한 소리를 내며 떨어진 전낭을 열어본 장사치가 눈을 깜빡였다.

“대, 대협. 이건.”

철궤에서 검을 꺼내 이리저리 살펴보던 젊은 무인이 힐끗 시선을 던졌다.

“왜 그러시오?”

“그, 그것이. 아무래도 금액을 잘못 생각하신 듯합니다.”

“잘못 생각했다?”

고개를 갸웃거리는 젊은 무인의 모습에, 장사치는 마른침을 꿀꺽 삼켰다.

그러나 그가 물려받은 명검은 집안의 가보인 데다, 그 값어치만 따져도 족히 은자 수백 냥은 받아낼 물건이었다.

그에 비하면 전낭 안에 들어있는 금액은 터무니없이 적었다.

“아, 아무래도 은자 스무 냥으로는 좀…….”

“글쎄, 내 생각은 좀 다른데.”

“예, 예?”

“그 정도면 충분할 거요. 당신 목숨값을 뺐으니까.”

삽시간에 가라앉은 젊은 무인의 목소리에, 주위의 공기가 싸늘하게 얼어붙었다.

호기심과 두려움이 뒤섞인 표정으로 상황을 지켜보던 양민들은 몸을 부르르 떨었고, 그간 동고동락하던 이웃 장사치들은 애써 그 광경을 외면했다.

하지만 이 자리의 모두가 그런 것만은 아니었다.

“흑룡마문의 위세가 대단하긴 한 모양이군. 대가리에 피도 안 마른 애새끼까지 이렇게 설쳐 대는 것을 보면.”

거친 목소리와 함께 인파가 좌우로 갈라졌다. 그 사이로 걸어 나온 한 중년인이 젊은 무인을 향해 누런 이를 드러내며 씩 웃었다.

“긴말 안 하마. 손에 들고 있는 그 검 얌전히 내려놓고, 썩 꺼져라.”

젊은 무인이 눈을 깜빡였다.

“지금 그거, 나한테 한 말이오?”

“허어, 이놈 보게. 그럼 누구한테 했을까.”

“아, 오해는 하지 마시오. 분명 제대로 듣긴 했는데…….”

중년인을 위아래로 훑어본 젊은 무인이 천천히 말을 이었다.

“설마 당신 따위가 그런 말을 당당히 지껄일 수 있을 거라고는 미처 생각하지 못했거든.”

“……따위? 지껄여?”

아주 잠깐, 멍하니 젊은 무인을 응시하던 중년인이 박장대소했다.

“따위라. 으하, 으하하하! 이거 보기보다 사람 웃기는 재주가 있는 놈이군.”

“그것 참 희한하구려. 감숙에서는 아무도 내게 그런 재주가 있다는 걸 알려 주지 않았는데.”

“아해야, 네 이름이 무어냐?”

“딱히 알려 줄 이유도, 그럴 생각도 없소. 이만 갈 길 가시오.”

“표정이 영 아닌데, 겁이라도 집어먹었느냐?”

“그렇다기보단…… 사실 당신 따위와 말 섞는 것 자체가 썩 불쾌한 편이라.”

“허허.”

입은 소리 내어 웃고 있지만, 중년인의 눈동자는 섬뜩하게 빛나고 있었다.

그리고 터질듯한 근육과 온갖 흉터로 가득한 팔이 움직이려던 그 순간, 젊은 무인이 불쑥 입을 열었다.

“그쯤 하지, 혈곤(血棍).”

“……!”

자신의 별호를 들은 중년인, 혈곤 도상호의 신형이 움찔 떨렸다.

뿐만아니라, 두 사람의 대치를 지켜보던 무림인들 역시 놀라움을 감추지 못했다.

혈곤에 대한 정보는 제법 알려져 있었으니 중년인의 외양과 허리춤에 매여진 붉은 곤을 보고 정체를 추측하는 것은 그리 어려운 일이 아니다.

그들이 놀란 가장 큰 이유는 바로 젊은 무인의 태도 때문이었다.

흑룡마문의 복장을 한 애송이. 뛰어난 절정 고수인 혈곤을 한참 밑으로 내려다보는 말투와 태도.

그리고 이상함을 느낀 것은 당사자인 혈곤도 마찬가지였다.

“나를…… 알고 있었느냐?”

“들어 봤지. 은자만 주면 거지 밑구멍도 핥는다는 놈이 있다는 것 정도는.”

“……!”

어느새 뒤바뀐 말투와 모욕적인 언사.

분노로 눈을 부릅뜬 혈곤을 향해, 젊은 무인이 천천히 말을 이었다.

“이렇게 만나 보니 내가 들은 말이 사실인 듯한데, 당신에게 제안 하나 할까.”

“제, 제안?”

“은자를 줄 테니 내 발등을 핥아라. 하면 목숨은 살려 주지.”

“이, 이놈이 감히!”

혈곤의 신형이 부르르 떨렸다.

그는 누구도 무시할 수 없는 무위를 갖춘 절정 고수. 당장이라도 달려가 저 애새끼의 머리통을 깨부수고 싶었다.

다만 흑룡마문이라는 네 글자가 그의 발목을 붙잡았다.

새파랗게 젊은 나이에 저토록 평온한 태도. 이대로 생사결이 벌어진다면 결코 좋지 않을거라는 직감이 그를 망설이게 했다.

“……제기랄.”

결국 반쯤 들어올린 애병을 내려놓는 혈곤의 모습에, 젊은 무인이 빙긋 웃었다.

“은자가 좋긴 좋은 모양이야. 이제 내 발등을 핥을 차례인가?”

“놈, 닥치지 못할까!”

심후한 공력이 담긴 외침이 사방을 후려쳤다.

아직 무공이 일천한 삼류 무림인들은 신음을 뱉으며 뒷걸음질 쳤고, 공포에 질린 양민들이 비명을 내질렀다.

그런 극심한 혼란 속에서, 혈곤은 핏발 선 눈동자로 젊은 무인을 노려보았다.

“네놈이 얼마나 대단한 신분인지는 모르나, 언제고 반드시 오늘 일을 후회하게 될 것이다.”

젊은 무인이 작게 혀를 찼다.

“단단히 화가 난 모양이군. 하지만 그쯤 하는 게 좋을 것 같은데.”

“나, 혈곤 도상호! 은혜는 잊어도 원한은 잊지 않는다. 비록 오늘은 이렇게 물러나지만, 다음에 보는 날이 네놈의 제삿날…….”

퍽!

피가 사방으로 튀었다.

머리가 으스러진 채 숨이 끊긴 혈곤의 시신을 바라본 젊은 무인이 한숨을 내쉬었다.

“어지간하면 피를 보지 않으려 했는데. 조금 더 참지 그랬나.”

도대체 언제 나타난 것일까.

거대한 대초자곤(大梢子棍)을 휘둘러 혈곤의 머리통을 박살 낸 팔 척의 사내가 어눌한 목소리로 대답했다.

“감히, 소문주, 모욕. 속하, 참지 않을 것.”

“뭐, 혈곤 정도면 괜찮으려나. 정파라고 하기에도 뭐한 놈이니.”

젊은 무인이 작게 혀를 찬 그때, 뒤늦게 상황을 인지한 사람들이 비명과 함께 사방으로 흩어지기 시작했다.

“사, 사람이 죽었다!”

“꺄아아아악!”

“이런 미친……!”

무림인들도 갑작스럽게 벌어진 상황에 굳어 있던 바로 그 순간. 도망치는 사람들 너머로 무언가를 발견한 젊은 무인이 문득 중얼거렸다.

“그래, 말썽이 생길 줄 알았다니까.”

그의 시선 끝에, 황색 가사(袈裟)를 걸친 일단의 승려들이 이쪽을 향해 다가오고 있었다.

“소림사(少林寺)라…….”
```

## Final English reading copy

```markdown
# Chapter 513

Xixia in Henan Province, situated along a tributary of the Yangtze, was packed with people again today.

The ferry landing was crowded with boats of every size, while merchants with all kinds of goods piled around them haggled with fire in their eyes.

“Come on! Cheap, cheap! Musk that’s good for your virility, only one silver nyang!”

“I don’t need that crap.”

“Young Lady, you’re looking lovely! Would you like a hand mirror?”

“I’m not buying that crap.”

“…What a pair of fucking assholes.”

The marketplace rang with every kind of noise.

But in the end, the atmosphere of a place was determined by the kind of people who gathered there.

In that sense, the merchant who habitually grabbed hold of a passing young martial artist had chosen the wrong target.

“Sir. Judging by your appearance, you seem to be a martial hero on your way to Mount Song. Perhaps you need a well-honed weapon—gasp!”

The merchant, who had been chatting away with impressive smoothness, swallowed a startled breath.

The handsome face that had first caught his attention had vanished from his thoughts.

The moment he saw the three characters embroidered in black thread across the young martial artist’s dark blue silk uniform, along with the dragon pattern, the merchant let out a cry that sounded almost like a moan.

“B-Black Dragon Demon Gate!”

“……!”

Though the cry had not been particularly loud, the four-character name Black Dragon Demon Gate was enough to plunge the bustling thoroughfare into a pit of silence.

“B-Black Dragon Demon Gate?”

“They’re the unorthodox bastards who’ve been making such a name for themselves in Gansu.”

“I heard they arrived in Henan late yesterday… Could they be here to join the alliance?”

The silence spread in an instant.

The merchants who had been shouting at the tops of their lungs, the commoners wandering nearby, and even the martial artists traveling in groups with weapons at their waists—

Everyone stopped what they were doing and focused their attention on the source of the cry.

Under the gaze of countless people, the young martial artist from the Black Dragon Demon Gate smiled faintly at the merchant.

“You have a decent eye for a merchant. To recognize even our sect’s insignia.”

“Th-that’s…”

“You don’t seem to have much connection to Murim. Are you originally from Gansu? Or perhaps… you picked up a few scraps of knowledge from the Third Rate swordsmen who came here as customers.” 

The young martial artist glanced over the merchant’s shoulder at the various weapons arranged neatly on the stall and clicked his tongue.

“Every last one is so cheap I wouldn’t take it even for free. Bring me the best one.”

“Pardon?”

The young martial artist sighed.

“I forgot you were a merchant. In that case, bring me the most expensive one instead of the best.”

“Y-yes, understood.”

With trembling hands, the merchant pulled out and opened an iron chest hidden deep in the stall.

When the young martial artist saw the lone sword lying inside without even a decent scabbard, he whistled.

“Hm. That doesn’t look like the sort of thing that should be in a place like this.”

The people watching the two of them—especially the martial artists—nodded without realizing it.

Although the sword looked quite old, its blade shone with a dazzling array of colors, and its edge had lost none of its sharpness.

It was a weapon that could easily be called a famed sword.

Sensing greed appearing in the eyes of several martial artists, the merchant hunched his shoulders.

“M-my late father passed it down to me.”

“Was your late father a martial artist?”

“Th-that’s impossible. Somehow, he came to own the sword, but he only told me to keep it secret from others and preserve it as a family heirloom for generations…”

“That makes sense. A sword of this quality would have attracted more than a few greedy eyes.”

Excessive greed led to bloodshed.

Most martial artists would choose to take a famed sword by force rather than pay several hundred silver nyang for it.

After all, thrusting a cheap iron sword at someone was far more effective than gathering enough silver to buy a famed sword.

“Your late father must have been quite wise.”

“Y-yes, yes, he was.”

“But it seems you didn’t inherit his wisdom. Not if you’re displaying something like this so openly.”

“Th-that’s…!”

The merchant could not continue, and the young martial artist let out a quiet laugh.

He had already seen straight through the words the merchant could not bring himself to say and had swallowed instead.

His customer was a martial artist from the Black Dragon Demon Gate, an unorthodox faction.

With a knife at his throat, the merchant had not had time to think things through. Fear had paralyzed his judgment—the fear that if he brought out some other item clumsily, his head might be severed.

It was the first time the merchant had ever experienced such a situation.

For the young martial artist, however, it was familiar.

“I understand. Most people who face me think and act exactly as you did.”

The young martial artist looked the merchant up and down. The merchant sat with his mouth shut, like someone who had swallowed his tongue.

“So I’ll save you.”

Suspicion flickered across the merchant’s eyes.

“Wh-what do you mean?”

“I mean I’ll pay for the sword and take it.”

“Ah!”

The merchant’s face brightened.

His heart had already been burning with anxiety.

He had taken the sword out because he had decided that surviving came first, but more than a few people had seen the famed sword with their own eyes.

Once the young martial artist in front of him left, rootless wandering martial artists and petty thieves would surely smell the opportunity and gather around.

But if this man bought the sword, everything would be solved.

Of course, there would be people who coveted the silver he received in payment, so he would have to leave the area soon. Still, he could preserve his life, secure a comfortable fortune, and enjoy a prosperous life somewhere else.

Having finished his calculations, the merchant immediately bowed deeply.

“G-Great Hero, if you would do that, I could ask for nothing more!”

“You’re not completely empty-headed.”

The young martial artist gave a faint laugh and tossed a money pouch from his robes onto the stall.

Clink.

The merchant opened the pouch after it landed with a heavy sound and blinked.

“G-Great Hero. This is…”

The young martial artist, who had taken the sword from the iron chest and was examining it from every angle, glanced over.

“What is it?”

“Well, I’m afraid you may have miscalculated the amount.”

“Mis-calculated?”

As the young martial artist tilted his head, the merchant swallowed hard.

The famed sword he had inherited was a family heirloom, and merely judging by its value, it was worth at least several hundred silver nyang.

Compared to that, the amount inside the pouch was absurdly small.

“Twenty silver nyang is a little…”

“Well, I see it differently.”

“Pardon?”

“That should be enough. I deducted the price of your life.”

The young martial artist’s voice sank in an instant, and the air around them turned cold.

The commoners watching with expressions mingling curiosity and fear shuddered, while the neighboring merchants who had shared his ups and downs all this time deliberately looked away.

But not everyone there was willing to remain silent.

“The Black Dragon Demon Gate must have quite a reputation if even some wet-behind-the-ears brat is throwing his weight around like this.”

With that rough voice, the crowd split apart. A middle-aged man walked through the opening, grinning at the young martial artist and baring yellow teeth.

“I won’t waste words. Put down the sword in your hand and get the hell out of here.”

The young martial artist blinked.

“Were you speaking to me?”

“Ha! Look at this brat. Who else would I be talking to?”

“Ah, don’t misunderstand. I heard you perfectly well…”

The young martial artist slowly looked the middle-aged man up and down before continuing.

“I simply never imagined that someone like you could say something like that so boldly.”

“…Someone like me? Say something like that?”

For a brief moment, the middle-aged man stared blankly at the young martial artist.

Then he threw back his head and roared with laughter.

“Someone like me? Ha! Hahaha! You’re funnier than you look.”

“That’s strange. No one in Gansu ever told me I had that talent.”

“Boy, what’s your name?”

“I have no particular reason to tell you, and no intention of doing so. Go on your way.”

“You don’t look so good. Are you frightened?”

“It’s not that… It’s just that I find speaking with someone like you rather unpleasant.”

“Heh.”

The middle-aged man laughed aloud, but his eyes gleamed ominously.

His arm, bulging with muscles and covered in scars, was just beginning to move when the young martial artist suddenly spoke.

“That’s enough, Blood Cudgel.”

“……!”

The middle-aged man’s body jerked at the sound of his sobriquet.

Blood Cudgel Do Sangho.

The martial artists watching the confrontation were equally unable to hide their surprise.

There was quite a bit of information circulating about Blood Cudgel, so it was not difficult to guess his identity from the middle-aged man’s appearance and the red cudgel hanging at his waist.

What surprised them most was the young martial artist’s attitude.

A brat dressed in the Black Dragon Demon Gate’s uniform, speaking and acting as if he were looking down on the outstanding Peak master Blood Cudgel from a great height.

Blood Cudgel himself felt something was strange.

“You… knew who I was?”

“I’ve heard of you. I know there’s a man who’ll lick a beggar’s ass as long as he’s paid in silver.”

“……!”

At some point, he had dropped his polite speech and begun hurling insults.

Blood Cudgel’s eyes widened with rage, and the young martial artist continued slowly.

“Now that I’ve met you in person, what I heard seems to be true. How about I make you an offer?”

“An offer?”

“I’ll give you silver. Lick the top of my foot, and I’ll let you live.”

“H-how dare you!”

Blood Cudgel’s body trembled.

He was a Peak master with martial prowess no one could ignore. He wanted to rush forward that instant and smash the brat’s head open.

But the four characters Black Dragon Demon Gate held him back.

The young man was so impossibly young, yet his attitude was so calm. Blood Cudgel hesitated because he had a gut feeling that if this turned into a life-and-death duel, the outcome would not be good for him.

“…Damn it.”

In the end, Blood Cudgel lowered the weapon he had half-raised.

The young martial artist smiled.

“You must really like silver. Is it time to lick my foot now?”

“You bastard, shut your mouth!”

The shout, packed with profound internal energy, lashed out in every direction.

Third Rate martial artists with shallow cultivation groaned and staggered backward, while terrified commoners screamed.

Amid the extreme chaos, Blood Cudgel glared at the young martial artist with bloodshot eyes.

“I don’t know how important you are, but you’ll regret what happened today someday.”

The young martial artist clicked his tongue softly.

“You seem pretty angry. But you should stop there.”

“I, Blood Cudgel Do Sangho! I may forget a favor, but I never forget a grudge. Though I’m retreating like this today, the next time we meet will be the day of your funeral—”

Thud!

Blood sprayed in every direction.

The young martial artist looked at Blood Cudgel’s corpse, its head crushed and its life extinguished, and sighed.

“I tried not to draw blood if I could help it. You should have held back a little longer.”

When had he appeared?

An eight-foot-tall man who had crushed Blood Cudgel’s head with a swing of his massive two-section staff answered in a halting voice.

“Dare… insult Young Sect Leader. This subordinate… will not tolerate it.”

“Well, Blood Cudgel may be acceptable. It’s not as if he could really be called orthodox.”

The young martial artist clicked his tongue softly.

Only then did the people who had belatedly understood what had happened begin scattering in every direction with screams.

“A person’s been killed!”

“Aaaah!”

“What the hell…!”

The martial artists were frozen by the sudden turn of events.

At that exact moment, the young martial artist spotted something beyond the fleeing people and muttered to himself.

“See? I knew there’d be trouble.”

At the end of his gaze, a group of monks wearing yellow kasayas was approaching them.

“So it’s Shaolin Temple…”
```
