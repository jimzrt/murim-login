<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0638.txt",
      "sha256": "d54e0d0b1ec31823a8c7f32b891906a9620f263259519512b3fd870ef9859076",
      "bytes": 13434
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "06a7253777127dd18d5f8b8342e7884da2e52ba4f881b3a9b8b5b91754077951",
      "bytes": 1650
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "8684e76629df999b84efb2232c2247c8dc8685e9b58655b77167bdc44ce3b26d",
      "bytes": 196623
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "a52819acb1d415c0ed31c37e48e2682e97babe190ae8097bcbd2bdf1475dce95",
      "bytes": 560
    },
    {
      "path": "characters/Jin-ho.md",
      "sha256": "28103cfdb40ea0c956922ed8305cabcf6a8ebbfae07ab864d807cecde2781151",
      "bytes": 565
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "2ee77e9a1d5d7d04bc6461137b6bdb37bcf4edf48b220c849a97822225533a4e",
      "bytes": 202599
    }
  ],
  "estimated_tokens": 9140
}
-->

# Durable State Update — Chapter 638

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 638. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 638. Profile updates may replace only one
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
  "chapter": 638,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 638,
    "continuity_sources": [638],
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
    "Jin Taekyung and the Beast Miao King have entered the inner Poisonblood Grounds after crossing its poisonous swamp.",
    "Poison Mist fills the inner region and conceals unknown life-forms and hostile presences.",
    "The Beast Miao King carries a poison-warding pearl, while Jin's Myriad-Poison Ring protects him from the Poison Mist.",
    "The Beast King Stone is a legendary Nanman Beast Palace sacred treasure said to command every ferocious beast, though its existence is uncertain.",
    "Dark Heaven is targeting sacred treasures, and Jin suspects its Nanman objective is connected to creating a rift.",
    "A dead Bai warrior was found wrapped in sticky thread inside the Poisonblood Grounds.",
    "Thousand-Year Spiders have surrounded Jin and the Beast Miao King.",
    "The active Quest provides no known mission or Reward and imposes death upon failure."
  ],
  "continuity_sources": [
    637
  ],
  "open_questions": [
    "Why was a Bai warrior inside the Poisonblood Grounds, and what killed him?",
    "What are the Thousand-Year Spiders, and how dangerous is the surrounding swarm?",
    "What lies deeper inside the Poisonblood Grounds?",
    "Is Dark Heaven's Nanman objective connected to the Beast King Stone or another sacred treasure?"
  ],
  "safe_through": 637,
  "temporary_decisions": [
    "Use Poisonblood Grounds for 독혈지.",
    "Use Beast King Stone for 수왕석.",
    "Use Thousand-Year Spider for 천년지주.",
    "Use Mr. Yayul for 야율 씨 in colloquial dialogue.",
    "Retain My Good Sir, Do Not Cross That Swamp for the chain Quest title."
  ],
  "version": 1
}
```

## Exact glossary matches

| 십왕     | **Ten Kings**       |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 보상               | **Reward**                     |
| 칭호               | **Title**                      |
| 대격변     | **Great Cataclysm**   |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 진호 | **Jin-ho** | Jin Taekyung's older male friend, addressed as Jin-ho hyung. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 고블린 | **goblin** | Monster species reported at the F-rank Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 허공답보 | **Stepping on Empty Air** | Technique that allows Jongni Chu to move through empty air as if climbing invisible stairs. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 무한 | **Wuhan** | Capital of Hubei Province near Dongting Lake. |
| 답보 | **stagnation** | Taekyung's current lack of progress in martial arts. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 독물 | **venomous beasts** | Venomous creatures associated with the Nanman Beast Palace. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 백족 | **Bai people** | Ethnic group encountered in Yeongin. |
| 독혈지 | **Poisonblood Grounds** | Hidden poisonous region created by the Five Poisons Sect inside Ailao Mountain. |
| 독무 | **Poison Mist** | Deep green mist covering the Poisonblood Grounds swamp. |
| 천년지주 | **Thousand-Year Spider** | Monster appearing at the end of the chapter. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 637
- **Aliases:** None
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, the great chieftain of the Miao people, and a master among the Ten Kings.
- **Personality:** Fierce and vigilant when confronting threats to the Nanman Beast Palace.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace and is responsible for the forces stationed at Ailao Mountain.

### Jin-ho.md

# Jin-ho (진호)

- **Safe through:** Chapter 613
- **Aliases:** None
- **Role:** A civil servant in the Hunter and Gate Management Department and Jin Taekyung's older friend.
- **Personality:** Blunt, vulgar, perceptive, and good-natured beneath his teasing.
- **Voice:** Casual, profane, teasing, and irreverent.
- **Relationships:** Jin-ho is Jin Taekyung's older friend and trusted confidant; he has inferred Taekyung's involvement in the masked group's campaign and agrees to keep it secret.

## Korean source

```text
＃638화



거미?

살면서 질리도록 많이 봤다. 대격변이라는 전쟁통에서도 꿋꿋하게 살아남은 희망 고시원에는 온갖 벌레가 들끓었고, 그중에서도 거미는 빼놓을 수 없는 단골손님이었으니까.

오죽하면 진호 형이 이런 말을 했을 정도다.



‘여기 건물주 이름이 혹시 파브르가 아닐까?’



죽은 지 이백 년이 되어 가는 곤충학자의 예토전생 설을 믿을 정도의 곤충 밀집도.

하지만 누가 그랬다. 인간은 적응의 동물이라고.

처음에는 시도 때도 없이 나타나는 거미에 질색하던 나는 일 년이 채 지나기도 전에 익숙해졌고, 몇 년 뒤에는 거미 종류를 알아볼 수 있을 만큼의 안목까지 생겼다.



‘형, 인사해. 얘는 유령거미야. 그 옆에는 무당거미.’

‘인사 같은 소리하네. 알겠으니까 저리 치워.’

‘그리고 얘는 브라질 떠돌이 거미.’

‘치우라고 했…… 아니 도대체 왜 브라질 떠돌이 거미가 희망 고시원을 떠도는 건데. 지금 이 상황이 말이 되는 거야?’

‘말이 안 될 건 없지. 난 어제 고블린이랑 싸우고 왔는데.’

‘아.’

‘그리고 얘는 타란툴라야. 새로 왔나 보네.’

‘악몽인가? 도대체 어째서 타란툴라가…….’



참으로 신비한 고시원 생태계. 나는 그곳에서 수많은 거미들과 꽃다운 청춘을 보냈고, 나중에는 이웃사촌처럼 지냈었다.

하지만 단언컨대, 지금 막 눈앞에 등장한 저 거미보다 흉측하고 거대한 것은 본 적이 없었다.

“……천년지주(千年蜘蛛)?”

야수묘왕의 입술 사이로 흘러나온 생소한 이름은 난생처음 듣는 것이었고, 그것의 정체는 타란툴라나 브라질 떠돌이 거미와는 차원이 달랐다.

‘저게 무슨…….’

누가 곰보다 큰 거미를 본 적이 있느냐 묻는다면, 나는 망설임 없이 고개를 끄덕이겠다.

지금 이 두 눈으로 똑똑히 목격하고 있으니까.

그것도 심지어 다섯 마리나.

스스스슥!

유령 같은 움직임. 뻣뻣한 털이 돋아난 여덟 개의 다리가 움직일 때마다 거대한 몸통이 거목을 타고 미끄러진다.

이어 크고 작은 괴물의 눈동자에 빠르게 가까워지는 우리가 비친 순간, 야수묘왕이 벼락같은 외침을 내질렀다.

“온다!”

그리고 다음 순간.

솨아아악!

머리 위로부터 쏟아진 희끄무레한 점액질이 반경 십여 장을 뒤덮는다.

야수묘왕의 외침 덕분에 아슬아슬하게 공격 범위를 벗어난 나는, 눈 앞에 펼쳐진 광경을 확인하고 눈을 크게 떴다.

치이익!

땅, 바위, 풀. 그곳에 남겨 놓을 수밖에 없었던 이름 모를 백족 전사의 시신까지.

점액질에 닿은 모든 것들이 악취와 함께 녹아내리고 있었다. 마치 누군가가 염산이라도 쏟아부은 것처럼.

‘산성(酸性)?’

만약 저것의 정체를 모르고 피하지 않았거나 조금이라도 닿았다면, 점액질에 의하여 신체 일부가 즉시 녹아내렸을지도 모른다.

보는 것만으로도 등골이 서늘해지는 광경.

그러나 놀라고만 있기에는 현재 상황이 그리 순조롭지 않았다.

사사삭!

우거진 풀숲 사이. 짙은 안개 너머. 하늘마저 가린 거목 위.

곰보다 큰 덩치에 흉측하기로는 이루 말할 수 없는 다섯 마리의 독거미가 사방에서 우리를 옥죄어 오고 있었으니까.

“……포위망을 펼쳐?”

황당함이 담긴 내 중얼거림에 야수묘왕이 공력을 끌어올리며 대답했다.

“천년지주는 남만의 수많은 독물(毒物) 중에서도 왕이라 불리는 놈이다. 흉포하기 이전에 교활한 존재라, 과거 천 명에 달하는 전사들이 놈을 척살하고자 했으나 열흘 밤낮 동안 그들 중 절반을 죽이고 사라졌다는 기록도 있지.”

“무슨 거미 주제에. 아니지, 천년이나 묵은 놈들이니까 그럴 만도 하네요.”

“능히 천 년까지도 산다고 해서 천년지주라 부르는 것이다. 저것들이 얼마나 오래된 놈들인지는 아무도 모르지. 지금처럼 동시에 여러 마리가 나타난 것도 최초겠지만.”

남만에는 무수히 많은 독물들이 존재한다. 그런데 그중에서도 왕이라 불리는 괴물이 다섯 마리나 나타나다니.

나는 아직도 주위를 녹이고 있는 점액질을 바라보며 내심 중얼거렸다.

‘젠장, 제대로 걸렸네.’

미처 발견할 수 없었던 나머지 남만 전사들의 시신. 또 그들이 부리던 맹수들이 왜 감쪽같이 사라졌는지 알 것 같았다.

사냥을 통해 어느 정도 허기를 채운 뒤, 식량을 비축하기 위해 독혈지 깊숙한 곳으로 옮긴 거겠지.

‘앞서 죽었던 백족 전사처럼 거미줄로 꽁꽁 묶어서.’

필시 같은 방식으로 우리를 노리고 있을 거다.

하지만…….

‘그건 니들 생각이고.’

나는 소름 끼치는 소리와 함께 포위망을 좁히는 놈들을 바라보며, 텅 비어 있는 손을 허공으로 뻗었다.

‘인벤토리 오픈. 소환.’

띠링.

명령에 답하는 작은 종소리와 함께, 한계를 알 수 없는 무한의 창고가 스스로 문을 열어젖힌다.

만일의 상황을 대비하여 모아 왔던 수많은 병장기. 그중에서 새하얀 빛을 내뿜는 한 자루의 창이 손아귀에 붙잡혔다.

“내가 방금 뭘 잘못 본…….”

“잘못 보신 거 맞습니다. 삼단 접이식 창이라 평소에는 소매에 넣어둬요.”

순간 눈을 의심하는 야수묘왕을 뒤로하고, 나는 비스듬히 늘어트린 백염(白炎)의 창날을 향해 공력을 흘려보냈다.

스아아아.

시릴듯한 예기(銳氣)를 뿜어내는 창날 위로 유형화된 기의 불꽃이 피어오른다.

열양지기를 장작 삼아 일어난 푸른 불꽃이 일렁이자 주위를 에워싼 짙은 독무도, 사방을 점하며 서서히 옥죄여 오던 다섯 마리의 천년지주도 불에 덴 듯 움찔거렸다.

시시싯.

경계 가득한 울음소리와 움직임. 딱정벌레처럼 검고 각기 크고 작은 눈동자가 재빠르게 사방을 훑는다.

하지만 이제 와서 물러서기에는 늦었다.

놈들도. 우리도.

이미 주사위는 던져졌고, 남은 것은 어느 한쪽이 죽고 사는 것뿐이다.

그리고 오늘 이 자리에서 사냥당하는 것은, 우리가 아닌 놈들이 될 것이다.

“뭐 하냐.”

나는 푸른 화염이 일렁이는 창날을 겨누며 말을 이었다.

“후딱 안 들어오고.”

그 한마디가 신호탄이었다.

촤아아아악!

전후좌우. 그리고 머리 위 허공을 뒤덮으며 쏟아지는 희끄무레한 점액질의 파도를 향해, 나와 야수묘왕은 공간을 가르며 쏘아졌다.

쐐애애액!

전신을 스치는 바람. 호흡기관과 피부를 통해 스며들었던 독기(毒氣)는 힘없이 사그라지고, 은빛 창날을 휘감으며 솟구친 화염은 더욱더 크게 타오른다.

‘지금.’

화륵. 콰아아아!

단 한 번의 휘두름.

제 자리에서 원을 그리며 스치듯 내뿜은 횡격(橫擊)에, 사방을 점하고 쏟아지던 점액질이 증발한다.

그리고 그보다 앞서 허공을 격하고 쏘아진 야수묘왕의 일권(一拳)이 있었다.

퍼어엉! 치이이익!

거대한 폭발음과 함께 점액질이 사방으로 터져 나간다.

반경 수십 장의 뒤덮은 산성의 소나기. 하지만 털끝 하나 다치지 않은 나와 야수묘왕은 녹아내리는 모든 것을 뒤로하고 거침없이 나아갔다.

쐐애애액!

야수묘왕은 정면을 가로막은 천년지주를 향해. 나는 허공 위 거목에 매달린 또 다른 한 마리를 향하여.

어떤 약속이나 계획도 없었지만, 우리는 찰나에 마주친 눈빛만으로도 서로의 뜻을 읽었다.

덥석.

막 허공을 박찬 내 발끝에 닿은 커다란 손바닥.

팔순이 넘은 나이가 무색할 만큼 우람한 근육이 꿈틀거린 그때. 천둥 같은 고함과 함께 엄청난 거력이 투포환처럼 발을 밀어 냈다.

“가라!”

후우우웅!

전신을 통해 느껴지는 부유감.

평범한 허공답보(虛空踏步)와는 비교도 안 될 만큼 신속하고 강맹하게 허공으로 쏘아진 나는, 어느새 여덟 개의 다리를 지닌 거대한 괴물의 코앞을 향해 들이닥치는 중이었다.

- ……!

크고 작은 여러 개의 눈에서 읽히는 여러 가지 감정.

나는 마치 인간처럼 경악하는 천년지주를 향해 창날을 내리그었다.

쉭, 서걱!

허공을 가로지르는 한 줄기 불꽃과 함께 끈적한 핏물이 튄다.

동시에 강철보다 단단한 여덟 개의 다리 중 세 개를 제물로 바쳐 살아난 천년지주가 황급히 점액질을 뿜어냈다.

촤악! 치이익!

독과 상성인 열양지기와 재빠른 움직임으로 점액질을 피해 냈지만, 거리가 너무 가까웠던 것이 패착이다.

피부와 옷을 스친 것만으로도 몰려오는 화끈한 통증.

그러나 나는 고통에 신음하는 대신, 그 틈을 노려 도망치려는 놈의 거대한 몸통에 창날을 꽂아 넣었다.

콰득, 푸우욱!

일반적인 곤충과는 달리 절지동물에 속한 거미는 외골격이 얇아 몸이 단단하지 못하다.

제아무리 천년지주가 독물의 왕이라 불리는 존재라 한들, 강기(罡氣)마저 막아 낼 수는 없었다.

“내가 시발, 거미 한두 마리 잡아 본 줄 아냐? 네가 희망 고시원 살았으면 사돈에 팔촌까지 나한테 죽었어.”

- 키이이이잇!

비명 같은 외침과 함께 몸부림치는 거대한 동체.

나는 재차 쏘아지는 점액질을 피하고, 옆구리를 향해 휘둘려진 다리를 맨손으로 잡아 뜯었다.

콰드득!

- 키에에엣!

한 번은 당할 수 있어도, 같은 방식으로 두 번은 당하지 않는다.

나는 이제 몸부림을 넘어 경련하는 천년지주의 머리를 향해 창날을 내리꽂았다.

푸푹!

갈 곳 없이 움직이던 다리가 힘을 잃고, 거대한 몸뚱어리가 경직된다.

동시에 짐작을 확신으로 바꿔 주는 알림이 뒤를 이었다.

띠링.



- [Lv.117 천년지주]를 처치했습니다!

- 상당량의 경험치와 명성을 획득했습니다!

- [천년지주]는 수많은 독물 중에서도 특별한 존재. 그에 따른 추가 보상이 주어집니다!

-희귀한 업적, [가리지 않는 사냥충]을 달성했습니다!

- 향후 곤충 형태의 적을 상대할 시, 추가 능력치를 얻습니다!



기다렸다는 듯이 쏟아지는 시스템 알림.

하지만 지금은 허공에 떠오른 홀로그램 창 속 내용을 일일이 확인할 만큼 여유로운 상황이 아니다.

당장 내가 딛고 서 있는 거목 아래에서는 야수묘왕이 일 대 다수의 혈투를 벌이는 중이었다.

치이이익!

“이 찢어 죽여도 시원치 않을 놈들! 감히 내 머리카락을!”

“…….”

이런 상황에도 머리카락을 신경 쓰다니.

야수묘왕이 걸친 의복은 이미 반쯤 녹아내려 피부가 곳곳에 비쳤고, 풍성하던 머리카락은 점액질에 거의 다 녹아내린 뒤다.

그래도 십왕이라는 칭호에 걸맞게 벌써 한 마리를 처치하고, 동시에 세 마리를 상대하고 있는 야수묘왕이었다.

뻐억!

정정. 이제 두 마리.

그리고 야수묘왕이 광폭한 기세로 뻗은 일권이 한 마리의 천년지주를 박살 낸 순간. 거목을 박찬 나는 한 줄기 벼락처럼 지상을 향해 내리꽂혔다.

쉬이이익! 콰직!

천년지주의 몸통을 두부처럼 파고든 창날.

동시에 단전에서 끌어올린 강대한 열양지기가 놈의 몸 안에서 솟구친다.

화륵. 퍼어엉!

폭발음과 함께 거대한 동체가 산산조각으로 터져 나갔다.

엄청난 양의 체액이 뿜어짐과 동시에 증발하고, 도저히 형체를 알아볼 수 없는 사체 위에 남은 것은 새로운 시스템 알림뿐이었다.

띠링.



- [Lv.109 천년지주]를 처치했습니다!

- 상당량의 경험치와 명성을 획득했습니다!

- 매우 희귀한 존재를 추가적으로 처치했으므로 보너스 경험치를 획득합니다!

- 레벨 업!



스아아아.

보이지 않는 치유의 빛이 전신을 스친다.

점액질에 의하여 녹아내렸던 피부와 소모된 공력이 회복되고, 조금씩 사그라지던 창날의 불꽃이 언제 그랬냐는 듯 거세게 타올랐다.

화륵.

- 시시시싯…….

그리고 어둠 속의 푸른 화염을 두렵게 바라보던 마지막 천년지주가 택한 방법은, 다름 아닌 도주였다.

파파팟!

동시에 땅을 박찬 여덟 개의 다리. 동시에 허공을 향해 뛰어오른 거대한 동체가 보이지 않는 무언가를 밟고 사뿐히 내려앉는다.

바로 그때였다. 어둠을 밝히는 화염 너머로 반짝이는 무언가가 눈에 들어온 것은.

‘거미줄?’

뇌리를 스친 한 줄기 생각과 함께, 나와 야수묘왕은 도주하는 천년지주를 쫓아 달려나갔다.
```

## Final English reading copy

```markdown
# Chapter 638

Spiders?

I’d seen more than enough of them in my life. Even during the war-torn Great Cataclysm, all kinds of bugs had stubbornly survived inside Hope goshiwon[^1]—and spiders had been among its most regular guests.

[^1]: A goshiwon is an inexpensive Korean housing arrangement consisting of extremely small rooms with shared facilities.

Jin-ho hyung had even said this once:

> “Could the landlord of this building be Fabre, by any chance?”

The kind of insect density that could make you believe an entomologist dead for nearly two hundred years had been brought back to life.

But someone once said that humans were creatures of adaptation.

At first, I had been disgusted by the spiders that appeared at all hours of the day. Before even a year had passed, I had grown used to them, and a few years later, I had developed enough expertise to identify different species.

> “Hyung, say hello. This one’s a ghost spider. The one next to it is a Joro spider.”
>
> “Enough with the greetings. I know what they are, so get them away from me.”
>
> “And this one’s a Brazilian wandering spider.”
>
> “I said get it away—wait, why the hell is a Brazilian wandering spider wandering around Hope goshiwon? Does this situation make any sense?”
>
> “It’s not like it can’t make sense. I fought a goblin yesterday.”
>
> “Ah.”
>
> “And this one’s a tarantula. Looks like it just moved in.”
>
> “Is this a nightmare? Why on earth is there a tarantula…?”

What a mysterious goshiwon ecosystem.

I had spent the flower of my youth there among countless spiders, and eventually, I had lived alongside them like neighbors.

But I could say this with certainty: I had never seen anything as hideous or enormous as the spider that had just appeared before my eyes.

“……A Thousand-Year Spider?”

The unfamiliar name that slipped between the Beast Miao King’s lips was one I had never heard before, and the creature itself was on an entirely different level from a tarantula or a Brazilian wandering spider.

*What the hell is that……*

If someone asked whether I had ever seen a spider bigger than a bear, I would nod without hesitation.

Because I was looking at one with my own two eyes.

Five of them, in fact.

*Skritch, skritch!*

Their movements were ghostlike. Every time their eight stiff, hair-covered legs moved, their enormous bodies slid along the trunks of the great trees.

Then, the moment our reflections—rapidly drawing closer—appeared in the eyes of the monsters, both large and small, the Beast Miao King shouted like a thunderclap.

“It’s coming!”

And the next moment—

*Shhhhhaaa!*

Pale, viscous slime poured down from overhead and covered a radius of more than ten zhang.

Thanks to the Beast Miao King’s warning, I had barely escaped the attack’s range. When I looked at the scene unfolding before me, my eyes widened.

*Hissss!*

The ground, the rocks, the grass—even the unidentified Bai warrior’s corpse that we had been forced to leave behind—

Everything touched by the slime was melting away with a foul stench, as though someone had poured acid over it.

*Acid?*

If I hadn’t dodged it despite not knowing what it was—or if even a little had touched me—the slime might have instantly melted away part of my body.

Just looking at it sent a chill down my spine.

But our current situation was not favorable enough for me to stand around being shocked.

*Skritch, skritch!*

Between the thick grass.

Beyond the dense mist.

Atop the great trees that hid even the sky.

Five venomous spiders, each larger than a bear and indescribably hideous, were closing in around us from every direction.

“……Are they forming a perimeter?”

The Beast Miao King answered my incredulous mutter as he raised his internal energy.

“Among the countless venomous beasts of Nanman, the Thousand-Year Spider is called a king. More than being ferocious, it is a cunning creature. There is even a record of a thousand warriors once trying to exterminate one, only for it to kill half of them over ten days and nights before vanishing.”

“What do you mean, it’s just a spider? No, wait. They’ve been around for a thousand years, so I suppose that makes sense.”

“They are called Thousand-Year Spiders because they are capable of living for as long as a thousand years. No one knows how old those creatures truly are. The simultaneous appearance of multiple ones like this may also be a first.”

Countless venomous beasts existed in Nanman.

And yet, five monsters called kings had appeared all at once.

I looked at the slime that was still melting everything around us and muttered inwardly.

*Damn it. We really walked right into this.*

The corpses of the remaining Nanman warriors that we had failed to find.

I thought I understood why the ferocious beasts they had commanded had vanished without a trace.

After filling their bellies to some degree through hunting, they must have carried the corpses deeper into the Poisonblood Grounds to stockpile food.

*Bound tightly in spiderwebs, just like the Bai warrior who died earlier.*

They were certainly planning to hunt us the same way.

But—

*That’s what you think.*

I stretched my empty hand into the air as the creatures closed their perimeter with a horrifying sound.

*Open Inventory. Summon.*

*Ding.*

In response to my command, the limitless warehouse with no known end opened its doors by itself.

Among the countless weapons I had collected in preparation for emergencies, my hand closed around a spear radiating a pure white light.

“Did I just see something wrong……?”

“You did. It’s a three-section folding spear, so I usually keep it in my sleeve.”

Leaving the Beast Miao King behind as he stared at me in disbelief, I sent my internal energy into the White Flame spearhead hanging at an angle.

*Fwoooosh.*

Flames of tangible qi bloomed over the spearhead, which radiated a chilling sharpness.

As the blue flames kindled by Scorching Yang Qi flickered, the dense Poison Mist surrounding us and the five Thousand-Year Spiders that had marked out positions around us and were slowly tightening their noose both flinched as though they had been burned.

*Hissss.*

Their cries and movements were filled with caution. Their eyes, black like beetles and varying in size, darted rapidly in every direction.

But it was too late to retreat now.

For them.

For us.

The die had already been cast. All that remained was for one side to live and the other to die.

And the ones being hunted here today would not be us.

“What are you waiting for?”

I aimed the spearhead, its blue flames wavering, and continued.

“Get in here already.”

Those words were the signal.

*Shhhhhaaa!*

Toward the waves of pale slime pouring down from the front, back, left, right, and the air overhead, the Beast Miao King and I shot forward, cutting through space.

*Whoooosh!*

The wind brushed past my entire body.

The venom that had seeped in through my respiratory tract and skin weakened helplessly, while the flames surging around the silver spearhead blazed even more fiercely.

*Now.*

*Fwoosh! Kwoooong!*

With a single swing.

The horizontal strike I unleashed in a circle from where I stood caused the slime falling from every direction to evaporate as it grazed past.

And before that, the Beast Miao King’s fist had already shot through the air.

*Boom! Hissss!*

With a tremendous explosion, the slime burst in every direction.

An acidic downpour covered a radius of several dozen zhang.

But the Beast Miao King and I, unharmed down to the tips of our hair, continued forward without hesitation, leaving everything melting behind us.

*Whoooosh!*

The Beast Miao King headed toward the Thousand-Year Spider blocking his path.

I headed toward another one clinging to a great tree in midair.

We had made no agreement and formed no plan, but the glance we exchanged in that brief instant was enough for us to understand each other’s intentions.

*Grab.*

A large palm caught the tip of my foot just as I kicked off into the air.

The muscles in the Beast Miao King’s arm rippled, making his age of more than eighty seem meaningless. With a thunderous roar, tremendous strength launched my foot away like a shot put.

“Go!”

*Whoooosh!*

I felt weightless throughout my entire body.

I shot into the air faster and more powerfully than ordinary Stepping on Empty Air could ever compare to, and before I knew it, I was hurtling straight toward the face of a massive monster with eight legs.

—……!

A multitude of emotions could be read in its many eyes, both large and small.

I brought the spearhead down toward the Thousand-Year Spider, which was staring at me in shock almost like a human.

*Swish! Slash!*

A streak of flame cut across the air, followed by a spray of sticky blood.

At the same time, the Thousand-Year Spider that had sacrificed three of its eight legs—each harder than steel—to survive hurriedly spat out slime.

*Splatter! Hissss!*

Thanks to the Scorching Yang Qi that countered the poison and my quick movements, I avoided the slime.

But the distance had been too close.

The pain that flared up just from it brushing against my skin and clothes was scorching.

Instead of groaning from the pain, however, I took advantage of the opening and drove the spearhead into the creature’s enormous body as it tried to flee.

*Crack! Thrust!*

Unlike ordinary insects, spiders are arthropods with thin exoskeletons, so their bodies are not especially hard.

No matter how much the Thousand-Year Spider was called the king of venomous beasts, it could not block Force.

“Fuck, you think I’ve only killed one or two spiders? If you’d lived in Hope goshiwon, your whole extended family—in-laws and eighth cousins included—would’ve died by my hand.”

—Kiiiiiieet!

The enormous body writhed with a scream.

I avoided the slime that shot toward me again, then grabbed and tore off the leg swinging toward my side with my bare hands.

*Crack!*

—Kieeeet!

I might have fallen for it once, but I would not fall for the same trick twice.

The Thousand-Year Spider was no longer merely struggling—it was convulsing. I drove the spearhead down into its head.

*Thrust!*

The legs that had been moving aimlessly lost their strength, and the enormous body stiffened.

At the same time, a notification followed, turning my guess into certainty.

*Ding.*

> **System**
>
> - Defeated **Lv. 117 Thousand-Year Spider**!
> - Gained a substantial amount of **EXP** and **Fame**!
> - **Thousand-Year Spider** is a special existence among countless venomous beasts. An additional **Reward** will be granted accordingly!
> - Achieved the rare achievement **Indiscriminate Hunting Bug**!
> - When facing insect-form enemies in the future, you will gain additional stats!

System notifications poured out as though they had been waiting for me.

But I was in no position to inspect every line in the holographic window floating in the air.

Below the great tree where I was standing, the Beast Miao King was in the middle of a one-against-many bloodbath.

*Hissss!*

“You bastards! Even tearing you to pieces wouldn’t be enough! How dare you do this to my hair!”

“……”

He was worried about his hair even in a situation like this.

The clothes worn by the Beast Miao King had already melted away halfway, revealing his skin in several places, and almost all of his once-thick hair had been eaten away by the slime.

Even so, true to his title as one of the Ten Kings, he had already killed one and was fighting three at once.

*Wham!*

Correction.

Two now.

The moment the Beast Miao King’s fist, thrown with a savage aura, smashed one of the Thousand-Year Spiders apart, I kicked off the great tree and plunged toward the ground like a bolt of lightning.

*Whooosh! Crack!*

The spearhead pierced through the Thousand-Year Spider’s body like tofu.

At the same time, the powerful Scorching Yang Qi I had drawn up from my dantian surged through the creature’s body.

*Fwoosh. Boom!*

With an explosive roar, its enormous body burst into pieces.

A tremendous amount of bodily fluid sprayed out and evaporated at the same time. On top of the corpse, now impossible to recognize, only a new System notification remained.

*Ding.*

> **System**
>
> - Defeated **Lv. 109 Thousand-Year Spider**!
> - Gained a substantial amount of **EXP** and **Fame**!
> - Because you additionally defeated an extremely rare existence, you gained bonus **EXP**!
> - **Level Up!**

*Fwoooosh.*

Invisible healing light swept over my entire body.

The skin melted by the slime and the internal energy I had expended were restored, while the flames on the spearhead, which had been slowly dying down, suddenly blazed as fiercely as though they had never weakened.

*Fwoosh.*

—Sssssss……

And the method chosen by the last Thousand-Year Spider, which had been staring fearfully at the blue flames in the darkness, was none other than escape.

*Pat-pat-pat!*

All eight legs kicked off the ground at once.

Its enormous body leaped into the air and then landed lightly after stepping on something invisible.

That was when I caught sight of something glittering beyond the flames illuminating the darkness.

*A spiderweb?*

With that thought flashing through my mind, the Beast Miao King and I charged after the fleeing Thousand-Year Spider.
```
