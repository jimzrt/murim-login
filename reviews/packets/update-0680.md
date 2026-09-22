<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0680.txt",
      "sha256": "7f2ed4e34e990b73ae1ab0ec563f2086e8a2b9d24efa4b957d014d81664912dc",
      "bytes": 12861
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "6aa6c6fa6757ff52b919412b22baab6f446602a5fb12297b785171e04b8c5c9c",
      "bytes": 2442
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b351f5178dba4d41730778b0904769d9208406a8782b25a6eb5ac14ba5e3e006",
      "bytes": 203156
    },
    {
      "path": "characters/Black Hand.md",
      "sha256": "d904387e5d19b983c3672dcd189a3959a44060b603ab80710271ec0cf1f9cbd4",
      "bytes": 732
    },
    {
      "path": "characters/Great Snow Fiend.md",
      "sha256": "c613c7f80a2a227eba1ab85d92aa44b46635718659c04cd90ba1044f18974245",
      "bytes": 455
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "7a427cfb007d23814e4664863788773cb18138aee1b78bbb4232e382bb39339d",
      "bytes": 626
    },
    {
      "path": "characters/Muyaho.md",
      "sha256": "203120578f4bdb7ec0b7e79e2c7cdcbcdc97f8a92da9bb4cb87fa087760a3c86",
      "bytes": 648
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "032fab6a45f2d352c7e00e1761629d0c46f9ec2f1aa7998e55ccf842ae2b8f74",
      "bytes": 210448
    }
  ],
  "estimated_tokens": 9572
}
-->

# Durable State Update — Chapter 680

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 680. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 680. Profile updates may replace only one
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
  "chapter": 680,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 680,
    "continuity_sources": [680],
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
    "The Beast Miao King sent Yayul Mok and others to the underground prison after choosing to stake his fate on keeping faith with Jin Taekyung and Baeksang.",
    "Namho believes Baeksang and Dark Heaven have likely seized the Inner Palace and may have intended the Blood Monk to eliminate the Beast Miao King's loyalists.",
    "The Han Chinese members of the reconnaissance squad are detained without harm, with their Sleep Acupoints struck.",
    "Namho plans to escort the Han Chinese to the Central Plains so the Murim Alliance and Sichuan's major sects can aid Nanman, a journey expected to take seven to ten days.",
    "The Yangtze River Channel League's swift ship has arrived unexpectedly at the reconnaissance squad's position, and an unidentified person has stepped ashore.",
    "Jin Taekyung is fighting the Black Hand Fist Demon and an unidentified twin-wheel Supreme Peak master in the Poisonblood Grounds.",
    "Muyaho's fur was cut by a twin wheel while Jin protected him.",
    "Jin has discarded White Flame temporarily and is launching the Flame-Extinguishing Divine Fist with blue-white flames.",
    "Yohi and Heugung remain captive and alive, awaiting the Southern Heaven Demon Empress's return.",
    "The Southern Heaven Demon Empress remains absent from the battlefield while her agents threaten Jin's allies."
  ],
  "continuity_sources": [
    679,
    678
  ],
  "open_questions": [
    "Who has arrived on the Yangtze River Channel League's swift ship, and why did it come directly to the reconnaissance squad's position?",
    "What is the identity and full strength of the Supreme Peak master wielding the twin wheels?",
    "Can Jin and Muyaho survive the battle against the two Supreme Peak masters?",
    "Can Namho's group reach the Central Plains and bring reinforcements before Nanman is overwhelmed?",
    "Will the Blood Monk act with Baeksang and Dark Heaven, and what will happen to the Beast Miao King's loyalists in the Inner Palace?"
  ],
  "safe_through": 679,
  "temporary_decisions": [
    "Use Black Hand Fist Demon for 흑수권마 while retaining Black Hand for 흑수.",
    "Preserve Jin's abrupt register changes and profanity as deliberate psychological provocation.",
    "Render 쌍륜 as twin wheels.",
    "Render 장 족장 and 고 족장 as Chief Jang and Chief Go.",
    "Use Flame-Extinguishing Divine Fist for 멸염신권."
  ],
  "version": 1
}
```

## Exact glossary matches

| 화왕     | **Fire King**                 | Jeok Cheongang |
| 무신     | **Martial God**               | —              |
| 암천     | **Dark Heaven**                  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 초식     | **form**                                         | Numbered technique movement                           |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 제자     | **Disciple**                                 |
| 노부      | **this old man / I**                                            |
| 흑수 | **Black Hand** | Sadistic Dark Heaven agent and Supreme Peak master. |
| 흑수권마 | **Black Hand Fist Demon** | Sobriquet revealed by Black Hand. |
| 대설귀 | **Great Snow Fiend** | Fiend who ruled Great Snow Mountain and killed Baekhwi and Venerable Wusang. |
| 무야호 | **Muyaho** | Yayul Mok's White Tiger's name; it means tiger of the mighty wilds. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 허공섭물 | **Seizing an Object Through Empty Space** | Technique Jeok Cheongang uses to lift Jang Taebo remotely. |
| 열화신공 | **Fire Gate Divine Technique** | Secret internal cultivation technique of the Fire Gate Clan, preserved through one-person succession without leakage. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 화룡신창 | **Fire Dragon Divine Spear** | Taekyung's spear technique, at the seventh stage in this chapter. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 화룡일미 | **Fire Dragon's Single Tail** | A form of the Fire Dragon Divine Spear. |
| 천격 | **Heavenly Strike** | A Fire Dragon Divine Spear form used by Taekyung against Hwangbo Eom. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 음한지기 | **Yin-Cold Qi** | Cold-aligned energy required in the treatment elixir. |
| 지풍 | **Finger Qi** | Invisible qi attack fired by the Western Heaven Demon Lord. |
| 듀라한 | **Dullahan** | Headless undead monster form taken by Yao Wei. |
| 마비 | **Paralyzed** | Status abnormality inflicted by Kraken's Ink. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 구천 | **Nine Springs** | Euphemism for the realm of the dead. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Black Hand.md

# Black Hand (흑수)

- **Safe through:** Chapter 679
- **Aliases:** Black Hand Fist Demon (흑수권마)
- **Role:** Black Hand is a sadistic Dark Heaven agent and Supreme Peak master acting under orders associated with the Southern Heaven Demon Empress.
- **Personality:** Black Hand is cruel, gleeful, predatory, and fascinated by the despair of his victims.
- **Voice:** Black Hand speaks in archaic first person with drunken mockery, humiliating insults, and casual threats.
- **Relationships:** Black Hand is the captor and torturer of Yohi and Heugung and an enemy of Jin Taekyung; a colder senior figure can command him to obey the Demon Empress's orders.

### Great Snow Fiend.md

# Great Snow Fiend (대설귀)

- **Safe through:** Chapter 662
- **Aliases:** None
- **Role:** A fiend who ruled Great Snow Mountain and killed Baekhwi and Venerable Wusang during the Great Faction War.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Enemy of Baeksang, Baekhwi, Venerable Wusang, the Beast Miao King, and the allied Southern Army.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 661
- **Aliases:** None
- **Role:** The Martial God is an unidentified legendary martial artist who defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone more than fifty years ago.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, appearing first as a white-bearded elder and later as a young boy; his identity, whereabouts, and possible connection to Cheon Taemin remain unknown.

### Muyaho.md

# Muyaho (무야호)

- **Safe through:** Chapter 679
- **Aliases:** White Tiger
- **Role:** Muyaho is Yayul Mok's enormous white tiger companion and a renowned Nanman spiritual creature currently accompanying Jin Taekyung through the Poisonblood Grounds.
- **Personality:** Muyaho is intelligent enough to understand speech, wary of threats, and strongly food-motivated.
- **Voice:** Muyaho communicates through growls, roars, and gestures rather than human speech.
- **Relationships:** Muyaho is Yayul Mok's cherished companion and currently carries Jin while aiding his escape.

## Korean source

```text
＃680화



느릿하게 흘러가는 세상 속.

주먹을 휘감으며 솟구친 청백색의 화염이, 찰나의 순간 스쳐 지나가는 모든 광경을 장작 삼아 타오른다.

내가 흑수권마의 심장을 향해 포탄처럼 내뻗은 일권(一拳)도.

금방이라도 튀어나올 듯 부릅뜬 눈동자로 황급히 손을 뻗는 놈의 모습도.

그럼에도 불구하고 힘없이 밀려 나가는 흑색 강기와 화염에 맞닿기 무섭게 산산이 흩어지는 호신강기도.

그리고…… 그 너머에서 공간을 가로지르며 다가온 눈부신 섬광까지도.

콰아아앙!

거대한 굉음과 진동.

모든 것이 한순간에 벌어지고, 한순간 만에 끝난 그곳에 뜨거운 열풍(熱風)이 불어닥쳤다.

아니, 반경 수십여 장이 마찬가지였다.

열양지기로 말미암은 열기와 수증기가 만들어 낸 안개가 곳곳을 잠식하고, 시야를 가로막았다.

솨아아아.

나는 제자리에 우뚝 선 채, 희뿌연 안개를 바라보았다. 그 너머에서 한 줄기 음성이 흘러나오기 전까지.

“실로 놀랍구나. 생각했던 것 이상이야.”

진심인 듯 미약한 탄성이 묻어 나오는 음성. 나는 허공섭물(虛空攝物)로 백염을 끌어당기며 담담하게 대꾸했다.

“내가 나이에 비해 좀 치는 편이긴 하지. 아마 천마(天魔)나 무신(武神)도 이 정도는 아니었을걸.”

“광오하군. 허나 인정하마. 네게는 그렇게 말할 수 있는 자격이 충분하니.”

“자격 운운하고 자빠졌네. 쫄려서 훼방 놓은 주제에 그딴 말을 지껄여?”

입술 밖으로 흘러나오는 목소리는 태연했지만, 나는 내심 속이 쓰렸다.

‘빌어먹을.’

마지막 순간 시야에 들어온 그 섬광.

호리호리한 노인이 날려 보낸 것이 분명한 쌍륜이 아니었다면, 흑수권마는 막대한 내상을 입거나 그 자리에서 절명했을지도 몰랐다.

‘이미 예상은 했지만…… 날아드는 타이밍이 너무 절묘했어.’

짧은 순간, 내게 주어진 선택지는 두 가지뿐이었다.

쌍륜에 목이 잘려 듀라한(Dullahan) 후보생이 되는 대신 흑수권마를 끝장내거나, 놈을 놓아주고 나도 살거나.

물론 내 선택은 당연하게도 후자였다.

허공에서 방향을 꺾은 일권으로 쌍륜을 후려쳤고, 흑수권마는 감히 그 틈을 노릴 생각도 하지 못하고 황급히 몸을 뺐다.

눈 깜짝할 사이에 시작되고 끝난 짧은 격돌.

언뜻 보면 서로 간에 팽팽한 동수를 이룬 것 같아도 이건 내게 있어 막심한 손해다.

한번 호된 맛을 본 흑수권마는 처음과는 비교도 할 수 없을 만큼 조심스럽고, 철저하게 나를 상대할 테니까.

상대의 방심은 어떤 것보다 큰 약점이지만, 그 방심을 이용할 기회는 처음 한 번뿐이다.

‘이대로면…….’

쉽지 않다. 아니, 너무 어려운 싸움이 되어 버린다.

나는 안개 너머 숨어 있는 신형을 더듬으며 입을 열었다.

“우리 흑손이. 나보다 반백 년을 더 사는 동안 무공을 똥꾸멍으로 익힌 흑손이. 어디 숨어 있니?”

그냥 씹어 버리면 어쩌나 싶었는데, 흑수권마는 상대의 말에 성심성의껏 대답해 주는 훌륭한 인성의 소유자였다.

“……아가리 닥쳐라.”

“기분 탓인가. 처음보다 목소리가 훨씬 작아진 것 같은데. 불맛 좀 보니까 불알까지 쪼그라들었나?”

“……놈. 노부가 한 번 방심한 틈을 노렸다고 아주 기세가 등등하구나. 네놈에게 그런 기회가 또 올 성싶으냐?”

나는 피식 웃었다.

흑수권마의 무위를 생각하면 방심한 틈을 노렸다는 게 아주 틀린 말은 아니지만, 저건 후기지수나 할 소리다.

나이를 먹을 만큼 처먹은 노괴(老怪)가 아니라.

“말하면서도 스스로가 병신 같지? 응?”

“이 찢어 죽여도 시원치 않을……!”

“그만.”

이어지려던 흑수권마의 외침이 차가운 음성에 가로막힌다. 아직도 사방에 자욱한 안개 너머에서 호리호리한 신형이 드러났다.

사박.

끔찍한 열기로 바싹 익은 진흙이, 노인의 발끝에서 모래처럼 바스라진다.

양손에 톱니바퀴처럼 칼날이 돋아난 륜을 든 그가 가볍게 소매를 떨쳤다.

솨아아아.

한풍(寒風)이 뜨거운 열기 위에 내려앉고, 시야를 가리던 안개를 밀어 내자 온갖 독으로 들끓는 늪지대에서 사막으로 변모해 버린 주위의 광경이 드러났다.

“이게 말로만 듣던 열화신공(烈火神功)이군. 대단해. 이 정도면 몇 성의 경지인 거지?”

순수한 감탄을 실어 묻는 노인을 향해, 나는 창날을 늘어트리며 대꾸했다.

“삼천이십오 성.”

“터무니없는 숫자로 느껴지는 건 착각인가?”

“무학의 경지는 원래 끝도 없지.”

“우문현답(愚問賢答)이로군. 화왕이 제자를 잘 키웠어.”

“이 정도면 훌륭하게 키운 거 맞지. 그런데 당신 부모님은 왜 자식새끼를 이따위로 키웠대?”

몸 쪽 꽉 찬 회심의 패드립. 그러나 노인은 흔들리지 않았다.

“글쎄, 나중에 저승에 갈 일이 있으면 물어보도록 하지.”

사박.

마치 산보하듯 나아가는 걸음. 나는 거리를 재며 대답했다.

“말이 나온 김에 오늘 찾아뵙는 건 어때.”

“아쉽구나. 당분간은 그 근처에도 갈 일이 없을 듯해서.”

“그런 거 미루면 안 좋아. 부모님이 구천에서 얼마나 화가 나시겠어. 자식이랍시고 뭐 빠지게 키워 놨더니 찾아오지도 않고.”

“이번에는 잘못 짚었다. 노부는 천애 고아라 딱히 누군가의 보살핌을 받지 못했으니, 불효자 소리 들을 일도 없지.”

사박.

어느새 세 번째 걸음.

앞서 쌍륜에 털을 밀린 탓에 위엄 가득한 백호에서 애견 미용 실패한 뽀삐가 되어 버린 무야호가 낮은 울음소리를 토해 냈고, 나는 노인의 손안에서 천천히 돌아가기 시작하는 쌍륜을 응시하며 중얼거렸다.

“그럼 저승 가도 왜 이렇게 키웠냐고 물어보질 못하겠네. 어차피 얼굴을 몰라서.”

“듣고 보니 그렇군. 좋은 조언 고맙네.”

“그럼 지금 당신 뒤에서 살금살금 꽁무니나 따라오고 있는 저 병신은?”

흑수권마는 짤막한 욕설을 내뱉었고, 노인은 침착하게 대답했다.

“흑수(黑手), 저 친구도 비슷한 처지지.”

“진심으로 궁금해서 묻는 건데, 암천 필수 조건인가? 아니면 뭐 유행이야?”

노인은 대답 대신 다시 한번 걸음을 내디뎠다.

사박.

그리고 유난히도 선명한 그 소리가 귓가를 파고든 그 순간. 나는 볼 수 있었다. 노인의 양손에 들려 있던 쌍륜이 뿜어내는 푸른 광휘를.

츠츠츠! 쉬잉!

미세한 파공성과 함께 날아드는 두 갈래의 빛줄기.

마치 살아 있는 뱀처럼, 기괴망측한 움직임으로 날아드는 쌍륜의 아래로는 광기에 번들거리는 눈동자를 한 흑수권마가 쇄도하고 있었다.

쐐애애애액!

두 방향. 아니, 세 방향에서 동시에 시작된 공격.

- 크아아앙!

등 뒤에서 터져 나오는 백호의 포효와 함께, 나는 전력을 다해 백염의 창날을 내리그었다.

쾅!

굉음과 함께 전해지는 거센 반발력. 쌍륜 중 하나를 걷어 낸 나는 사각에서 불어오는 바람을 느끼고 고개를 틀었다.

쉬익, 서걱!

그야말로 한 끗 차이.

강기에 의해 잘려 나간 머리카락이 허공에 흩날리던 그때. 어느덧 삼 장 앞까지 들이닥친 흑수권마가 너덜너덜한 양 소매를 떨쳤다.

“노오옴!”

구구구구궁!

활짝 펼쳐진 두 손에서 터져 나온 장력(掌力)이 공간을 뒤흔든다.

나는 파도처럼 덮쳐 오는 흑색 강기를 향해 부드럽게 창날을 밀어 넣었다.

화룡신창. 일 초식.

화룡일미(火龍一尾).

화륵, 쏴아아악!

청백색의 불꽃이 출렁인다. 흑색 장력을 가르고 거침없이 쏘아지는 화룡의 꼬리에, 대경한 흑수권마가 경호성을 토해 내며 신형을 틀었다.

서걱!

예리한 절삭음. 그러나 나와는 달리 흑수권마는 머리카락이 잘려 나가는 것 정도로 끝나지 않았다.

부지불식간에 잘려 나간 놈의 뭉툭한 코끝에서, 선혈이 뚝뚝 떨어지고 있었다.

“네, 네놈이 감히…….”

확실히 알았다. 흑수권마는 열 번을 더 싸운다 하더라도 나를 이길 수 없다는 것을.

저 늙은 괴물의 드높은 자존심과 그의 마음에 내재된 분노는 이성을 마비시키고, 그 미세한 균열은 내게 있어 곧 기회다.

‘지금.’

파팟!

단 일보(一步).

흑수권마와 나 사이에 놓인 수 장의 거리가 단숨에 지워지고, 십여 개가 넘는 움직임이 뇌리를 스친다.

그중 한 가지를 택하는 건 아주 손쉬운 일이다.

쉬익!

하늘로부터 땅까지. 미세한 파공음과 함께 내리그어지는 창날 위로 청백색의 화염이 피어오른다.

화룡신창. 이 초식.

‘천격(天挌).’

화륵. 콰아아아!

눈덩이는 구를수록 거대해지고, 물살은 더해지면 파도가 되는 법.

허공을 가로지르는 한 줄기의 화염을 올려다보던 흑수권마의 눈동자가 부릅떠진다.

“흡……!”

경호성과 함께 쳐올리는 쌍장(雙掌). 다급하게 끌어올린 장력이 화염과 부딪쳐 사그라진 그 짧은 순간, 푸른 섬광이 좌우에서 날아들었다.

쉬이이잉!

목. 그리고 가슴.

이건 움직임만으로는 피할 수 없는 공격이다. 나는 찰나의 판단과 함께 흑수권마를 향하던 창날을 비틀어 휘둘렀다.

쾅!

제아무리 나라 하더라도 불가항력(不可抗力)이라는 네 글자는 극복하지 못한다.

촤아악!

엄청난 반발력과 함께 중심을 잃은 몸이 속절없이 밀려 나간 그때, 누군가의 희끗한 신형이 유령처럼 들이닥쳤다.

쉬릭!

한마디 말도, 호흡도 없었다.

지금까지 후방에서 쌍륜만을 날려 보내던 노인은 냉정하면서도 담담하게, 그러나 정확한 속도와 흐름으로 자신만의 전투를 시작했다.

지금 이 순간처럼.

슈확! 푸푹!

뜨겁고, 서늘하다.

마지막 순간 신형을 비틀었음에도 결과는 크게 달라지지 않았다.

나뭇가지처럼 길고 말라비틀어진 손가락의 끝에서 터져 나온 지풍(指風)은 내 어깨를 꿰뚫었고, 노인을 향해 나아가던 백염의 창날은 방향을 잃고 흔들렸다.

그리고 힘을 잃은 창날을 피하는 것은, 노인에게 있어 너무나도 손쉬운 일이었다.

쉬익!

덧없이 허공을 가르는 창날.

이를 악문 나는 신형을 바로 세우며 남은 한 손을 펼쳤다. 동시에 열기와 함께 화염이 들끓는 그것을 노인의 가슴을 향해 내질렀다.

화륵. 후우우웅!

막아서는 모든 것을 불사르며 나아가는 화염신장(火焰神掌)이 노인의 눈동자에 비친다.

이루 말할 수 없이 뜨겁고, 쉼 없이 타오르는 열기.

하지만 여전히 차갑게 식은 노인의 눈동자를 본 나는, 알 수 없는 한기(寒氣)를 느꼈다.

‘이건.’

정체를 알 수 없는 불안감. 그리고 내 전신을 사로잡은 불길한 직감은, 곧 현실로 드러났다.

스윽.

찰나를 쪼개고 쪼갠 짧은 순간 속, 노인이 느릿느릿 손을 뻗는다.

아니, 느린 것은 그뿐만이 아니다.

그의 가슴을 향해 나아가는 내 일장도, 서로의 등 뒤에서 달려오는 흑수권마와 백호도 마찬가지다.

그리고…… 주름진 노인의 손에서 흘러나온 냉기(冷氣)와 함께, 멈춰 있던 시간이 흐르기 시작했다.

콰득! 파츠츠츠측!

마침내 서로를 향해 맞닿은 두 개의 손바닥.

청백색의 불꽃과 새하얀 냉기가 부딪치고 섞여든다.

콰드드득!

모든 것이 온통 뜨겁고, 차가웠다.

각기 다른 색을 지닌 두 개의 빛이 눈앞에서 쉴 새 없이 명멸하고, 미증유(未曾有)의 공력이 사방을 부수고 뒤흔들었다.

구구구구궁!

천지가 갈라지는 듯한 굉음.

그리고 나는 보았다. 동시에 들을 수 있었다.

“소개가 늦었구나.”

서서히 꺼져 가는 불꽃을 짓누르는 강대한 음한지기와.

“노부는 대설귀(大雪鬼)라 한다.”

새하얀 입김 사이로 흘러나오는 차가운 음성을.

콰창!
```

## Final English reading copy

```markdown
# Chapter 680

In a world flowing sluggishly by.

Blue-white flames surge around my fist, burning every scene that flashes past in an instant as kindling.

The punch I thrust like a cannonball toward the Black Hand Fist Demon’s heart.

The sight of him hurriedly reaching out with his eyes bulging as though they might pop from their sockets at any moment.

The black Force being pushed away helplessly despite that, and the Body-Protecting Qi shattering the instant it touched the flames.

And…

Even the dazzling flash that came slicing through the space beyond them.

KWA-AAANG!

A tremendous roar and vibration.

Everything happened in an instant, and ended just as quickly. Then a blast of hot air swept across the place.

No—the same was true for everything within a radius of several dozen jang.[^1]

Mist born from the heat and steam of Scorching Yang Qi spread everywhere, blocking my view.

Whoosh…

I stood perfectly still and stared into the hazy mist.

At least, I did until a voice drifted out from beyond it.

“What an astonishing display. It is even more impressive than I expected.”

There was a faint note of genuine admiration in his voice. I used Seizing an Object Through Empty Space to pull White Flame back and answered calmly.

“I’m pretty good for my age. I doubt even the Heavenly Demon or Martial God was this good.”

“How arrogant. Still, I will acknowledge it. You possess every right to speak that way.”

“Listen to you going on about rights. You got scared and interfered, so what the hell are you talking about?”

My voice sounded composed, but inside, I was bitter.

*Damn it.*

That flash that had entered my field of vision at the last moment.

If it had not been for the twin wheels thrown by the slender old man, the Black Hand Fist Demon might have suffered severe internal injuries—or died on the spot.

*I knew it was possible…but the timing was too perfect.*

In that brief moment, I had been left with only two choices.

Either finish off the Black Hand Fist Demon at the cost of letting the twin wheels take my head and turn me into a Dullahan candidate, or let him go and save my own life.

Naturally, I had chosen the latter.

I changed the direction of my punch in midair and struck the twin wheels aside. The Black Hand Fist Demon did not even dare try to take advantage of the opening. He hurriedly pulled back.

It had been a brief clash that began and ended in the blink of an eye.

At a glance, it might have looked like we had fought to an even draw. But this was a tremendous loss for me.

After getting a taste of how harshly I could hit him, the Black Hand Fist Demon would face me far more cautiously and thoroughly than before.

An opponent’s carelessness was the greatest weakness of all, but you only got one chance to exploit it.

*At this rate…*

This would not be easy.

No. It had become an incredibly difficult fight.

I felt around for the figure hiding beyond the mist and opened my mouth.

“Our Black Hand. Black Hand, who is fifty years older than me yet learned martial arts through his asshole. Where are you hiding?”

I wondered if he might simply ignore me, but the Black Hand Fist Demon possessed an admirable character and answered my words with complete sincerity.

“…Shut your damn mouth.”

“Is it just me, or is your voice much quieter than before? Did tasting a little fire shrink your balls too?”

“…You bastard. You’re awfully full of yourself just because you caught me off guard once. Do you really think you’ll get another chance like that?”

I let out a quiet laugh.

Considering the Black Hand Fist Demon’s martial prowess, it was not entirely wrong to say I had taken advantage of his carelessness. But that was something a young prodigy might say.

Not an old monster who had lived long enough to rot with age.

“You sound like a fucking idiot even while saying that. Don’t you?”

“You—tearing you limb from limb wouldn’t be enough…!”

“Enough.”

The Black Hand Fist Demon’s shout was cut off by a cold voice.

A slender figure emerged from beyond the mist that still blanketed the area.

Step.

The mud, baked hard by the terrible heat, crumbled like sand beneath the old man’s toes.

He held a wheel in each hand, blades jutting from them like the teeth of gears, and lightly shook his sleeves.

Whoosh…

A cold wind settled over the scorching heat and pushed away the mist blocking my vision.

The scene around us was revealed. The poisonous marshland had been transformed into a desert.

“So this is the Fire Gate Divine Technique I have heard so much about. Impressive. At what stage has it reached?”

The old man’s question was filled with genuine admiration.

I lowered the spearhead and answered.

“Three thousand twenty-five stages.”

“Is it my imagination, or does that seem like a ridiculous number?”

“The realm of martial arts has no end.”

“A foolish question met with a wise answer. The Fire King raised his Disciple well.”

“He did raise me well, didn’t he? But why did your parents raise their child like this?”

A killer parent insult, right on the inside corner.

But the old man did not so much as waver.

“I suppose I shall ask them if I ever have occasion to visit the realm of the dead.”

Step.

He advanced as though he were taking a leisurely stroll.

I measured the distance between us and answered.

“Since we’re on the subject, why not go visit them today?”

“Unfortunately, I doubt I will be going anywhere near there for some time.”

“You shouldn’t put things like that off. How angry must your parents be in the Nine Springs? They worked themselves half to death raising you, and now you won’t even visit.”

“This time, you have guessed wrong. I am an orphan with no family in this world. I received no one’s care, so I have no reason to be called an unfilial son.”

Step.

That was his third step.

Muyaho, who had gone from a majestic White Tiger to Poppy after a botched pet-grooming job because the twin wheels had shaved off his fur, let out a low growl.

I watched the twin wheels slowly begin to spin in the old man’s hands and muttered.

“Then you won’t be able to ask them why they raised you like this even after you get to the Nine Springs. You don’t know what they look like, after all.”

“Now that you mention it, that is true. Thank you for the advice.”

“Then what about that idiot sneaking along behind you?”

The Black Hand Fist Demon spat out a brief curse, and the old man answered calmly.

“Black Hand. That friend is in a similar situation.”

“I’m asking because I’m genuinely curious. Is that a requirement for joining Dark Heaven? Or is it some kind of trend?”

The old man did not answer. Instead, he took another step.

Step.

At that moment, the unusually clear sound pierced my ears.

I saw it.

The blue radiance pouring from the twin wheels in the old man’s hands.

Hiss! Whoosh!

Two streaks of light flew toward me with faint sounds of splitting air.

The twin wheels flew in grotesque, unnatural movements like living snakes.

And beneath them, the Black Hand Fist Demon came charging forward, his eyes gleaming with madness.

SHWAAAAAAK!

The attack began from two directions.

No—from three directions at once.

“GRAAAH!”

Along with the roar of the White Tiger exploding behind me, I swung White Flame’s spearhead down with all my strength.

KWAANG!

A violent rebound traveled through me with the deafening impact.

I knocked one of the twin wheels away, then felt wind blowing in from my blind spot and turned my head.

Whoosh—shhk!

It had missed by no more than a hair.

As hair sliced apart by Force scattered through the air, the Black Hand Fist Demon, who had already rushed to within three jang of me, shook his tattered sleeves.

“Youuu!”

Rumble-rumble-rumble!

Palm Force erupted from his wide-open hands and shook the space around us.

I gently thrust the spearhead toward the black Force rolling over me like a wave.

Fire Dragon Divine Spear. First form.

Fire Dragon’s Single Tail.

Fwoosh—shaaaa!

Blue-white flames surged.

The tail of the fire dragon tore through the black Palm Force and shot forward without hesitation. The Black Hand Fist Demon, astonished, twisted his body with a startled cry.

Shhk!

A sharp cutting sound.

But unlike me, the Black Hand Fist Demon did not get away with losing only a few strands of hair.

Blood dripped from the blunt tip of his nose, sliced away without him realizing it.

“You—you dare…”

I knew it for certain now.

Even if we fought ten more times, the Black Hand Fist Demon could never defeat me.

The pride of that ancient monster, along with the anger buried in his heart, had numbed his reason.

That tiny crack was an opportunity for me.

*Now.*

Flash!

One step.

The distance of several jang between the Black Hand Fist Demon and me vanished in an instant, and more than ten possible movements flashed through my mind.

Choosing one of them was easy.

Whoosh!

From the heavens to the earth.

Blue-white flames rose along the spearhead as it slashed downward with a faint sound of splitting air.

Fire Dragon Divine Spear. Second form.

*Heavenly Strike.*

Fwoosh—KWA-AAANG!

A snowball grew larger the farther it rolled, and a current became a wave when more water joined it.

The Black Hand Fist Demon looked up at the streak of flame cutting across the air, and his eyes flew wide.

“Guh…!”

With a startled cry, he raised both palms.

The Palm Force he desperately dragged upward collided with the flames and faded away.

In that brief moment, blue flashes flew in from the left and right.

SHWIIIIING!

His neck.

And his chest.

This was an attack that could not be avoided through movement alone.

With a split-second decision, I twisted the spearhead aimed at the Black Hand Fist Demon and swung it.

KWAANG!

Even someone like me couldn’t overcome the verdict contained in those four characters: *force majeure*.

SHRAAAK!

The tremendous rebound made me lose my balance and sent me helplessly sliding backward.

At that moment, someone’s pale figure rushed in like a ghost.

Shrik!

There was no word.

Not even a breath.

Until now, the old man had done nothing but throw twin wheels from the rear. But now, with a cold and composed demeanor—and with precise speed and flow—he began his own battle.

Just as he did now.

SHWAAK! THUD!

It was hot.

And cold.

Even though I twisted my body at the last moment, the result did not change much.

Finger Qi erupted from the tips of fingers long and withered as tree branches and pierced my shoulder.

The White Flame spearhead moving toward the old man lost its direction and wavered.

And avoiding the weakened spearhead was far too easy for the old man.

Whoosh!

The spearhead passed pointlessly through empty air.

I clenched my teeth, straightened my body, and opened my remaining hand.

At the same time, flames roiling with heat surged from it as I thrust my palm toward the old man’s chest.

Fwoosh—whoooom!

The Flame Divine Palm advanced while burning everything in its path.

The old man’s eyes reflected the flames.

An indescribably intense heat that continued to burn without pause.

But when I saw that the old man’s eyes remained cold, I felt an inexplicable chill.

*This is…*

An unease whose source I could not identify.

And the ominous instinct that seized my entire body soon revealed itself as reality.

Sss…

Within that brief moment, split into even smaller fractions of time, the old man slowly extended his hand.

No.

He was not the only thing moving slowly.

My palm advancing toward his chest was moving slowly as well.

So were the Black Hand Fist Demon and the White Tiger, each charging in from behind one of us.

And…

Along with the cold energy flowing from the old man’s wrinkled hand, the time that had stopped began to move again.

KRAK! SHHHHTZZZ!

At last, our two palms met.

Blue-white flames collided and mingled with pure-white cold.

KRRRUMBLE!

Everything was burning hot.

And freezing cold.

Two lights of different colors flashed relentlessly before my eyes, while unprecedented internal energy shattered and shook everything around us.

Rumble-rumble-rumble!

A roar like heaven and earth splitting apart.

And then I saw it.

At the same time, I heard it.

“My introduction came rather late.”

The powerful Yin-Cold Qi pressed down on the flames as they slowly died away.

“I am called the Great Snow Fiend.”

The cold voice drifted through a cloud of pure-white breath.

KRAAASH!

[^1]: A *jang* is a traditional Korean unit of length, roughly three meters.
```
