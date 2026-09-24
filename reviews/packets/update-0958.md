<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0958.txt",
      "sha256": "f480a3a1e23862a0a497fbcb131ed249c80cf10140c4a45e108af5bd60390e8d",
      "bytes": 14377
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "bcbd6cf5ac1b6d2fbe5489fb244c610aad9b346cc138478836b1b72d8f6e75e4",
      "bytes": 2445
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "1137d196ebb7a3df40f3a1d1d2799f090a60df6cd515b0bab92da528b06e39b2",
      "bytes": 234528
    },
    {
      "path": "characters/Chinggen.md",
      "sha256": "99ec19fba492d85c4548f333d871a502f6efd2f63cc890661165038e50adf774",
      "bytes": 658
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "88af518d2b8bf85cabd837f9af8a94e3cc2f37c10372a35e747d84cac67c8bfe",
      "bytes": 759
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "350a614a9dfa92e27e3588d31ec50462af2d2f6808c19a6aade0494e45b618a4",
      "bytes": 1343
    },
    {
      "path": "characters/Temur.md",
      "sha256": "48c1ed5bd0304b5b58023932f629caa55f28dc463679b66c5c11131894a8d800",
      "bytes": 637
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "f18380de4b880cd91b8bdf8e0075931aa3ec0eaf4be50d892364049b4b1db919",
      "bytes": 268208
    }
  ],
  "estimated_tokens": 9949
}
-->

# Durable State Update — Chapter 958

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
1 and safe_through 958. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 958. Profile updates may replace only one
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
  "chapter": 958,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 958,
    "continuity_sources": [958],
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
    "The steppe army has begun its assault on Eight Spring Gorge; the defenders’ battle remains unresolved, and the Chinggen impostor has reached the cliffs to face the Dongting Fisherman.",
    "Jin Wikyung promised his defenders they will celebrate the next Double Ninth Festival together on Mount Heng.",
    "Temur knows the man beside Jamukha is Chinggen’s killer and impostor but conceals his knowledge.",
    "Jamukha has long awaited a call from “that person”; the person’s identity and purpose remain unknown.",
    "The Emperor remains gravely ill from Blood Soul Gu; saving him requires him to die once, and Taekyung’s quest to treat him remains unresolved.",
    "Jang Sam remains unconscious after his sudden rise in level and attack on Taekyung; the improved Temporary Strength Pill’s source, effects, and distribution remain unknown.",
    "The Martial God’s identity and connection to the chosen one and the Bow Saint remain unknown.",
    "The Eastern Heaven Demon Lord’s papers and silk pouch remain unexplained.",
    "The real Chinggen was killed; an impostor wearing his face continues to accompany Jamukha and is now attacking the Jin defenders.",
    "Jin Mukyung wields a sword forged by Jang Taebo from material comparable to Ten-Thousand-Year Cold Iron; the Jin forces also use armor made from the Water God Dragon’s remains.",
    "The Dongting Fisherman has recovered from his injuries, owes the Jin Family of Taiyuan for saving his life twice, and seeks revenge on Dark Heaven; his fight with the Chinggen impostor is unresolved.",
    "Taekyung resolves to trust his allies rather than try to bear every burden alone."
  ],
  "continuity_sources": [
    956,
    957
  ],
  "open_questions": [
    "How will the battle at Eight Spring Gorge fare, and who will prevail in the Dongting Fisherman’s fight with the Chinggen impostor?",
    "Who gave Jang Sam the silk pouch, and what are the improved pill’s effects and distribution?",
    "What is the Martial God’s identity and connection to the chosen one and the Bow Saint?",
    "What do the Eastern Heaven Demon Lord’s papers and silk pouch contain?",
    "What will the Chinggen impostor do, and what is their purpose?"
  ],
  "safe_through": 957,
  "temporary_decisions": [
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진무경    | **Jin Mukyung**    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 절정     | **Peak**          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 팔천협    | **Eight Spring Gorge** |
| 칭겐 | **Chinggen** | Northern Gaoyuan chieftain commanding one hundred tribespeople; restrains Temur. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 테무르 | **Temur** | Northern Gaoyuan chieftain commanding one hundred tribespeople; claims descent from the khans. |
| 평화 | **Peace Guild** | Guild name. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 수련동 | **training hall** | Building located roughly two hundred jang from the training ground. |
| 대초원 | **Great Steppe** | The steppe region from which Temur and Chinggen come. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 흑목조간 | **black-wood fishing rod** | The Dongting Fisherman's distinctive weapon; the broken rod is his only known trace. |
| 대족장 | **Great Chieftain** | Title used for the senior Nanman leader who supposedly ordered the inspection. |
| 자무카 | **Jamukha** | Khan of the western grasslands and the steppe army’s practical leader. |
| 텡그리 | **Tengri** | Deity invoked by the steppe people. |
| 케식 | **Keshik** | Elite warriors serving the Golden Clan. |
| 검귀 | **Sword Demon** | Title used for the kind of swordsman Mukyung is said to resemble. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 테무르 | 칭겐 | fellow_chieftain | Chinggen | familiar and argumentative | Temur addresses his fellow chieftain by name while defending their khan lineage. |
| 칭겐 | 테무르 | fellow_chieftain | Temur | familiar and cautioning | Chinggen uses Temur's name while warning him not to act rashly. |
| 칭겐 | 자무카 | fellow_khan_to_elder_khan | Khan Jamukha | formal-respectful | The impostor wearing Chinggen’s face addresses Jamukha with deference. |
| 테무르 | 자무카 | fellow_khan_to_elder_khan | Khan Jamukha | formal-respectful | Temur affirms Chinggen’s public praise of Jamukha. |

## Listed compact profiles

### Chinggen.md

# Chinggen (칭겐)

- **Safe through:** Chapter 957
- **Aliases:** None
- **Role:** The real Chinggen was a Khan of the eastern grasslands and Temur’s brother, but he was killed; an impostor wearing his face now fights the Jin defenders at Eight Spring Gorge.
- **Personality:** Prudent, restrained, and attentive to the danger posed by the gathering's other powers
- **Voice:** Measured, familiar, and cautioning
- **Relationships:** Temur was Chinggen’s cousin and sworn brother through the anda oath; an impostor wearing Chinggen’s face now accompanies Jamukha and deceives Temur.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 957
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 956
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Jin Mukyung is the second son of the Jin Family of Taiyuan, a Peak-level swordsman known as the Heaven Shaking Sword, and Commander of the Heaven Shaking Squad.
- **Personality:** Reserved and disciplined, Jin Mukyung is devoted to swordsmanship and seeks strength in service of his family.
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Jin Wikyung is his older brother and the Lesser Family Head who formed the Heaven Shaking Squad in his honor; Jin Taekyung is his younger brother, and Mukyung cherishes his promise to reunite with him.

### Temur.md

# Temur (테무르)

- **Safe through:** Chapter 954
- **Aliases:** None
- **Role:** Temur is a Khan of the northern grasslands, ruling alongside Chinggen over tens of thousands of horses and warriors.
- **Personality:** Hot-tempered, reckless, proud of his khan lineage, and inclined to dismiss distant threats while indulging in celebration.
- **Voice:** Blunt, heated, and confrontational
- **Relationships:** The real Chinggen was Temur’s cousin and sworn brother through the anda oath, but he was killed; an impostor wearing Chinggen’s face now deceives Temur.

## Korean source

```text
＃958화



콰아앙!

폭발음과 함께 전해지는 미약한 진동.

아득히 솟은 절벽 위, 어둠 속에서도 쉽게 구분할 수 있을 만큼 희뿌연 먼지구름이 피어오르는 광경을 지켜보던 자무카는 수염을 쓰다듬었다.

‘시작한 모양이군.’

자무카는 칭겐, 아니 정확히는 칭겐의 모습을 한 누군가에 대해 잘 알고 있었다.

잔인하고, 흉포하며, 또한 강하다.

위에서 어떤 누구와 맞닥뜨린다 하여도, 놈은 주어진 임무를 해낼 것이다. 그것도 아주 훌륭하게.

카앙! 콰드드득!

먼지구름 사이로 쉼 없이 번뜩이는 섬광과 함께 굉음이 뒤를 잇는다.

그 아래에서는 어느덧 갑옷을 벗고 갈고리와 단검을 든 유목민들은 궁수들의 견제가 느슨해진 틈을 타 절벽을 빠르게 기어오르고 있었다.

“쏴라!”

쉬쉬쉬쉭!

간간이 터져 나오는 외침과 함께 화살이 날아들고는 있으나 딱 거기까지다.

침착함과 정확성도, 좌우에서 빼곡하게 쏟아지던 화망(火網)도 조금 전과는 비교도 할 수 없을 만큼 흔들리고 있다.

서로를 마주한 두 개의 절벽을 점거하고 있던 일천의 궁수 중 절반은 이미 칭겐에 의해 손이 묶였고, 나머지 절반은 다시 한번 물밀듯이 협곡으로 밀려들고 있는 지상군까지 견제해야 했으니까.

헐거워진 그물은 언젠가 찢어지는 법.

자무카는 그 시기를 조금 더 앞당길 생각이었다.

“무칼. 제르메.”

“예.”

“하명하십시오.”

자무카의 나직한 부름에 호명된 사내 둘이 앞으로 나섰다.

복장부터가 다른 유목민들과는 확연하게 구분되는 그들은, 자무카가 오랜 세월 직접 단련시킨 친위대 중에서도 두각을 드러냈던 실력자들이었다.

자무카는 과거 초원을 넘어 대륙까지 지배했던 위대한 정복자를 따라, 이들을 오준오구(五駿五狗)라 불렀다.

이른바 다섯 마리의 준마와 다섯 마리의 충견.

뛰어난 지휘관인 동시에 용장인 열 명의 백인장은 지난 수십여 년간 자무카의 충복으로 살았다.

비록 며칠 전, 그중 한 사람을 허망하게 잃어야 했지만.

“저 위에 숨어 화살만 쏘아 대는 겁쟁이들이 있다. 어찌해야겠느냐?”

“놈들의 활을 꺾고 목을 베어 돌아오겠습니다.”

“하늘과 가까운 곳이니, 텡그리께서 지켜봐 주시겠군요.”

굳게 말아쥔 주먹으로 징이 박힌 갑주를 두드린 두 장수가 돌아섰다.

각각 일백의 케식을 이끌고 날아드는 화살을 쳐 내며 빠르게 절벽을 오르기 시작하는 그들의 뒷모습을 바라본 자무카가 재차 입을 열었다.

“티라운. 보오르추. 옹게.”

이번에는 셋이다.

자무카는 호명된 두 백인장에게 끊임없이 비명이 울려 퍼지는 협곡을 가리켰다.

“저곳에 너희의 형제를 죽인 자가 있다.”

“……!”

“……!”

“……!”

세 사람의 눈꼬리가 파르르 떨렸다.

그것은 비단 며칠 전 휘하의 케식 일백과 함께 선봉대를 이끌고 떠나, 목만 돌아온 의형제가 떠올랐기 때문만은 아니었다.

자존심.

지금 그들의 주군은 셋이 합공하여 앞서 죽은 의형제의 원한을 갚으라 말하고 있었다.

“칸이시여. 놈은 저 혼자만으로도 충분합니다.”

“그건 나 역시 마찬가지다, 티라운!”

“저, 옹게를 보내 주십시오!”

자무카는 앞다투어 나서는 세 명의 백인장을 물끄러미 응시했다.

불룩 튀어나온 관자놀이의 태양혈(太陽穴)과 번뜩이는 안광은 이들이 절정의 끝자락에 도달한 고수라는 증거.

그러나 자무카는 이들의 주군이자 스승.

그렇기에 누구보다 잘 안다.

며칠 전, 승전보 대신 되돌아온 수하의 목에 남은 상흔(傷痕)을 보았기에 이런 판단을 내릴 수밖에 없었다.

‘결코 호락호락한 놈이 아니다.’

한 사람을 보낸다면 영영 돌아오지 못할 것이고, 둘을 보낸다면 하나만 돌아올 것이며, 셋을 보낸다면 필시 놈의 목을 갖고 돌아올 터.

세 백인장의 호승심에도 자무카의 뜻이 흔들리지 않는 이유은 바로 그 때문이었다.

“가거라.”

어조는 침착하나 그 안에 담긴 온도는 서늘하다.

이건 명령이다. 거부할 수 없는.

더 이상 자무카의 뜻에 항거할 수 없다는 사실을 깨달은 세 백인장은 입술을 깨물고 돌아섰다.

그리고 앞서 절벽으로 떠난 동료가 그랬듯이 휘하의 케식을 이끌고 앞다투어 달려 나갔다.

말도 버린 채 쾌속하게 쏘아진 수백의 신형은 죽은 인마(人馬)의 시체와 바위를 타 넘으며 협곡을 가로질렀다.

거센 저항을 이어 가고 있는 산서인들이 아닌, 두려움으로 뒷걸음질 치는 아군을 첫 제물로 삼으며.

“이, 이건 아니야. 이건 아니라고!”

“검은 양 씨족은 지금 즉시 물러나라! 후퇴하여 전열을 가다듬……!”

서걱!

늙은 족장의 목이 허공으로 솟구친다.

대초원의 소집령에 의해 수백여 명이 참전했으나, 이제는 절반밖에 남지 않은 중소부족의 생존자들이 눈을 부릅떴다.

“조, 족장님!”

“네놈들이 어찌 감히!”

하지만 그런 그들을 기다리는 것은, 사방에서 들이닥친 수십의 창칼이었다.

쐐애애액, 푸푹!

“커헉!”

날붙이가 한 번 번뜩일 때마다 목과 팔다리가 땅에 나뒹군다.

돌격창과 신월도로 일백여 명 남짓한 부족원들을 순식간에 도륙한 케식들의 모습에 협곡 전체가 얼어붙었다.

저 멀리서 그 광경을 지켜보던 누군가도 함께.

“이, 이게 무슨 짓이오!”

지진이라도 난 것처럼 요동치는 목소리.

그러나 그런 테무르를 향해 되돌아온 음성과 눈빛은 초원의 삭풍보다도 건조했다.

“칸의 명령을 어기고 제멋대로 후퇴를 지시했으니 즉결 처분을 한 것뿐이다.”

“하, 하지만 저들은 내 휘하의…….”

“그래, 네 휘하에 속한 자들이지. 테무르 칸.”

자무카의 입술 사이로 다른 사람에게는 들리지 않는 목소리가 흘러나왔다.

- 그리고 저들을 거느린 네놈은, 지금 내 옆에 있고.

“……!”

“무슨 문제라도 있나? 혹시 모를 불만이 있다면 지금 말하도록.”

테무르는 심장을 움켜쥐는 듯한 압박감과 함께 불현듯 깨달았다.

눈앞의 상대가 정해 준 선은 여기까지라는 것을.

이 선을 조금이라도 넘어간다면, 자신 역시 죽음을 면치 못하리라는 것을.

“무, 문제없소.”

“목소리가 잘 들리지 않는군. 나도 늙은 모양이야.”

“없습……니다.”

두려움과 굴욕감에 휩싸인 채로 간신히 쥐어 짜낸 그 한마디에, 자무카의 고개가 비로소 끄덕여졌다.

“옳은 선택일세. 군율은 언제나 엄격해야 하는 법이지. 그렇지 않나?”

테무르는 대답 대신 부르르 몸을 떨었다.

죽은 칭겐의 시체 앞에서 목숨을 구걸할 때부터 예상했으나 애써 외면하고 있었던, 참혹한 미래는 어느덧 현실이 되어 눈 앞에 펼쳐지고 있었다.

차차차창!

크아아악!

절벽에서. 그리고 협곡에서.

지금 이 순간에도 쉴 새 없이 들려오는 날붙이의 마찰음과 비명은 대부분 그를 따라 참전한 부족원들의 것이다.

그러나 그저 꾸며 낸 거짓에 속아 충성과 복수를 다짐하던 그들은 눈을 감으면서도 알지 못할 것이다.

짧은 평화와 번영을 가져다준 젊은 두 대족장이, 이미 자신들을 배신했다는 것을.

‘아니, 배신자는 나뿐이다. 내가 저들을 죽음으로 몰아간 거야.’

테무르는 피가 흐르도록 이를 악물었다.

칭겐은 기개를 지키다 죽었고, 자신은 구차하게 살아남았다.

이번 일에 적극적으로 협조한다면 목숨도 살려 주고 칸의 지위를 계속해서 누릴 수 있도록 해 주겠다는 그 약속에 깜빡 속아 넘어갔다.

아니, 그건 핑계일 뿐이다.

그는 단지…….

‘살아남고 싶었다. 무슨 수를 써서라도.’

그래, 그것만이 진실이다.

그리고 그 결과가 바로 이것이다.

자신과 칭겐을 따르는 이만여 명의 부족원들을 화살받이로, 고기 방패로 앞세워 저 끔찍한 협곡을 넘어서는 것.

“빌어먹을.”

악문 잇새 사이로 흘러나온 테무르의 뇌까림에 자무카의 미간이 찌푸려진 그 순간이었다.

“칸이시여!”

다급한 외침과 함께 빠르게 가까워지는 인영.

그가 조금 전 세 명의 백인장과 함께 협곡으로 향했던 케식의 일원임을 알아본 자무카의 눈빛이 깊게 가라앉았다.

아니, 정확히는 그의 손에 들려 있는 병장기 때문이었다.

“이건…….”

돌격창. 신월도. 활.

척 보기에도 다른 유목민들이 가진 것과는 격이 다른 예기(銳氣)를 흩뿌리는 세 자루의 병장기는 자무카에게 있어 퍽 익숙한 것이었다.

그것은 친위대인 케식 중에서도 가장 뛰어난 성취를 보인 열 명의 백인장을 위해 특별히 제작한 하사품이었으니까.

그리고 이 병장기의 주인들이 어떤 운명을 맞이했는지는, 굳이 듣지 않아도 알 수 있었다.

“그 아이들은, 편히 갔느냐.”

자무카의 나직한 목소리에 유품이 되어 버린 병장기를 내려놓은 케식이 고개를 떨구었다.

“전사로서 용맹하게 싸웠으니, 분명 텡그리의 품에 안길 것입니다.”

“그래, 그렇군.”

자무카는 낮게 중얼거렸다.

누군가를 죽이고, 누군가에게 죽는다.

대초원의 전사라면 피할 수 없는 운명이다.

다른 모든 이들 역시도.

“그 외에 입은 피해는?”

저 물음에 담긴 뜻은 이미 이 자리의 모두가 안다.

지금도 협곡 어디에선가는 수십여 명의 유목민이 피를 흩뿌리며 쓰러지고 있지만, 그들의 목숨값은 어떤 계산에도 들어가지 않는다.

자무카가 신경 쓰는 것은 친위대의 피해뿐이었다.

“비록 세 분의 백인장께서 전사하셨으나 전체적인 사상자는 미미합니다. 이십여 명이 죽거나 다쳤을 뿐, 남은 인원들은 후위로 물러나 새로운 명령 하달을 기다리고 있습니다.”

지휘관이 셋이나 죽었는데 휘하 병력의 피해가 적다는 것은, 오직 하나만을 의미한다.

혼자만으로도 충분하다며 자신감을 드러냈던 백인장들의 모습을 떠올린 자무카는 실소를 흘렸다.

“내 명령을 어겼군.”

그 세 사람은 생사결(生死決)을 벌였음이 틀림없다.

돌아가면서 한 사람씩.

장수로서는 멍청하고, 전사로서는 용맹하게.

그리고 차례대로 태원진가의 젊은 검귀(劍鬼)에게 목숨을 잃었을 것이다.

“한심한 녀석들 같으니.”

차마 긍정할 수 없어 고개만 더욱 깊이 숙이는 케식을 말없이 내려다보던 자무카가 불현듯 입을 열었다.

“협곡에 남아 있는 케식에게 돌격을 명한다.”

“칸이시여. 그 말씀은…….”

“공석이 된 백인장 자리는 선임 십인장이 임시로 맡는다. 최대한 피해를 최소화하며 놈들을 지치게 만들어라.”

더 이상의 지원 병력은 없다.

아직 자무카의 곁에는 몇 명의 백인장이 더 남아 있었으나, 팔천협은 반드시 넘어서야 할 첫 번째 언덕에 불과하다.

그는 이 비좁은 협곡에서 더 이상의 전력을 낭비할 생각도, 언제 다시 미련한 짓을 벌일지 모르는 백인장들을 믿을 생각도 없었다.

그보다는 확실한 패를 원했다.

비록 자무카가 움켜쥔 고삐의 방향에 따라 바람처럼 내달리는 준마나 충견은 아니지만, 그와 같은 주인을 모시는 맹견(猛犬)을.

콰아아앙!

자무카는 담담한 눈빛으로 지켜보았다.

하늘과 땅을 떨어 울리는 거대한 굉음 속, 절벽의 일각과 함께 지상으로 쇄도하는 한 줄기의 붉은 섬광을.



* * *



솨아아.

머리카락을 스치는 바람이 시원하다.

동굴 안 깊숙이 자리 잡은 수련동에서는 느껴볼 수 없었던 상쾌함.

마치 바람에 흔들리는 갈대처럼, 진무경은 부드럽게 몸을 비틀었다.

슈확!

다섯 자루의 돌격창이 팔과 다리, 그리고 허리를 스치며 지나간다.

진무경이 손을 내뻗자 강철로 만들어진 창대를 타고 새하얀 은빛 검신이 미끄러졌다.

서걱!

또 다른 누군가의 죽음을 알리는, 서늘한 절삭음.

그와 동시에 창대에 실려 있던 힘과 무게가 사라진다.

진무경은 몸 곳곳을 스치듯이 교차한 그것을 그대로 부여잡고 쾌속하게 회전했다.

콰드드득!

비명은 없다. 자욱한 피 안개만 있을 뿐.

다섯 개의 창을 톱니로, 스스로의 몸을 회전축으로 삼아 반경 삼 장을 갈아버린 진무경은 자신의 주위에 그 어떤 적도 보이지 않는다는 사실을 깨달았다.

그리고 그 이유가, 비단 자신의 무위 때문만은 아니라는 것도 함께.

콰앙! 구구구궁!

협곡이 몸을 떨었다.

하늘이 쪼개지는 듯한 굉음과 함께 쏟아지는 크고 작은 수많은 암석들 사이로, 마치 살아 있는 생물처럼 휘어지는 붉은 빛줄기가 진무경의 눈동자에 비쳤다.

쩌엉!

검신을 두드리는 강렬한 충격.

손목까지 전해지는 아릿한 통증을 느끼며 물러나는 진무경의 귓가로, 한껏 흥이 오른 목소리가 파고들었다.

“어허, 아깝다. 조금만 더 손에 익었으면 나도 월척 한번 낚는 건데.”

칭겐.

검붉은 핏물로 흠뻑 젖어 있는 흑목조간(黑木釣竿)을 내던진 그는, 각기 길고 짧은 두 자루의 검을 곧추세우며 웃었다.

자신의 새로운 사냥감을 향해.
```

## Final English reading copy

```markdown
# Chapter 958

*Ka-boom!*

A faint tremor followed the explosion.

Jamukha stroked his beard as he watched a pale cloud of dust rise atop the distant cliffs, visible even in the darkness.

*Looks like they’ve started.*

Jamukha knew Chinggen—or, more precisely, the person wearing Chinggen’s face—well.

Cruel, savage, and strong.

No matter who he ran into up there, he would carry out his assigned task. And he would do it exceedingly well.

*Clang! Krrrunch!*

Flashes of light flickered without pause through the dust cloud, followed by more deafening crashes.

Below, the nomads had shed their armor and taken up hooks and daggers. As the archers’ fire slackened, they seized the opportunity and rapidly climbed the cliffs.

“Loose!”

*Fwish-fwish-fwish!*

Arrows continued to fly, accompanied by occasional shouts, but that was all.

The archers’ composure and accuracy—and the dense crossfire pouring down from both sides—had faltered beyond comparison with what they’d been moments before.

Of the thousand archers holding the two cliffs facing each other, half had already been tied up by Chinggen. The other half also had to keep the ground forces in check as they surged into the gorge once more.

A net stretched thin would eventually tear.

Jamukha intended to bring that moment a little closer.

“Mukal. Jerme.”

“Yes.”

“Give your orders, Khan.”

At Jamukha’s quiet summons, two men stepped forward.

Their clothing alone set them apart from the other nomads. Among the Keshik Jamukha had personally trained over many years, they were two of the most capable.

Following the example of the great conqueror who had once crossed the steppe and ruled the continent, Jamukha called them the Five Steeds and Five Hounds.

Five fine steeds and five loyal hounds.

The ten commanders of a hundred were outstanding leaders and fearsome warriors alike. For decades, they had been Jamukha’s most loyal servants.

Though only days ago, he had lost one of them in vain.

“There are cowards hiding up there, doing nothing but shooting arrows. What should we do?”

“We’ll break their bows, cut their throats, and return.”

“It’s close to the heavens. Tengri will be watching over us.”

The two commanders struck their studded armor with clenched fists, then turned away.

Jamukha watched them lead a hundred Keshik apiece, deflecting the arrows as they quickly began climbing the cliffs. Then he spoke again.

“Tiraun. Boorchu. Ongge.”

Three this time.

Jamukha pointed toward the gorge, where screams rang out without end.

“Your sworn brother’s killer is there.”

“……!”

“……!”

“……!”

The corners of the three men’s eyes twitched.

It wasn’t just because they remembered their sworn brother, who had left days ago at the head of the vanguard with a hundred Keshik under his command, only for his head to return without him.

It was pride.

Their lord was telling them to join forces and avenge the sworn brother who had died before them.

“Khan. I’m more than enough for him on my own.”

“The same goes for me, Tiraun!”

“Please send me, Ongge!”

Jamukha watched the three commanders step forward, one after the other.

Their bulging temples and sharp, shining eyes showed that these masters had reached the upper reaches of the Peak realm.

But Jamukha was both their lord and their teacher.

He knew them better than anyone.

A few days ago, his subordinate’s severed head had returned instead of news of victory. Jamukha had seen the wound on its neck, leaving him no choice but to make this decision.

*He’s no pushover.*

Send one man, and he wouldn’t return. Send two, and only one would make it back. Send three, and they would surely return with the man’s head.

That was why Jamukha’s resolve did not waver, despite the three commanders’ fighting spirit.

“Go.”

His voice was calm, but its chill was unmistakable.

This was an order. They could not refuse it.

Realizing there was no way to defy Jamukha, the three commanders bit their lips and turned away.

Then, like their comrades who had set off for the cliffs ahead of them, they led their Keshik forward at a run.

Hundreds of figures shot across the gorge at speed, having left their horses behind. They clambered over the bodies of men and mounts, and over rocks.

Their first victims were not the Shanxi defenders, who continued to resist fiercely, but their own allies, stumbling backward in fear.

“T-this isn’t right! This isn’t right!”

“Black Sheep Clan, withdraw at once! Fall back and regroup—!”

*Shhk!*

The old chieftain’s head flew into the air.

Hundreds had joined the battle after the Great Steppe’s call to arms, but now the survivors of the small clan—reduced to half their original number—stared wide-eyed.

“C-Chieftain!”

“How dare you!”

But dozens of spears and swords were already closing in from every direction.

*Fwoooosh! Thunk!*

“Guh—!”

With every flash of a blade, heads and limbs rolled across the ground.

The Keshik slaughtered a hundred or so clansmen in moments with their lances and scimitars. The entire gorge froze at the sight.

So did someone watching from far away.

“W-what are you doing?!”

Temur’s voice shook as if he were caught in an earthquake.

But the answer that came back, in both voice and gaze, was drier than the steppe’s bitter wind.

“They disobeyed the Khan’s orders and ordered a retreat on their own. We simply carried out the summary execution.”

“B-but they’re under my command—”

“That’s right. They’re your people, Khan Temur.”

A voice slipped between Jamukha’s lips, too quiet for anyone else to hear.

“And the man who commands them is standing right beside me.”

“……!”

“Is there a problem? If you have any complaints, speak now.”

Temur suddenly understood, under the pressure that felt like it was gripping his heart.

The other man had drawn a line, and that was as far as Temur was allowed to go.

If he crossed it even slightly, he would meet the same fate.

“N-no problem.”

“I can’t hear you very well. I must be getting old.”

“N-no problem.”

At last, Jamukha nodded at the words Temur forced out through his fear and humiliation.

“A wise choice. Military discipline must always be strict. Don’t you agree?”

Temur trembled instead of answering.

He had expected it when he begged for his life in front of Chinggen’s corpse, but had tried to look away. Now the terrible future he had feared was laid out before his eyes.

*Clang-clang-clang!*

*Raaaagh!*

From the cliffs. From the gorge.

The constant clashes of weapons and screams still ringing through the air mostly belonged to the clansmen who had followed him into battle.

But as they died, those men would never know that the two young Great Chieftains who had brought them a brief peace and prosperity had already betrayed them.

*No. I’m the only traitor. I’m the one who led them to their deaths.*

Temur clenched his teeth until they drew blood.

Chinggen had died with his courage intact. Temur had survived in shame.

He had fallen for the promise that if he cooperated fully, they would spare his life and let him keep his position as Khan.

No—that was just an excuse.

He had simply—

*Wanted to survive. No matter what it took.*

Yes. That was the only truth.

And this was the result.

Leading twenty thousand clansmen who followed him and Chinggen into that dreadful gorge as arrow fodder, as human shields.

“Damn it.”

Jamukha’s brow furrowed at the mutter that slipped through Temur’s clenched teeth. Just then—

“Khan!”

A figure approached at a run, accompanied by an urgent shout.

Jamukha recognized him as one of the Keshik who had headed into the gorge with the three commanders moments earlier. His gaze darkened at the sight of the weapons in the man’s hands.

A lance, a scimitar, and a bow.

Even at a glance, the three weapons gave off a cutting edge far beyond that of anything the other nomads carried. They were familiar to Jamukha.

They had been specially made as gifts for the ten commanders of a hundred who had excelled above all others among the Keshik, his personal guard.

Jamukha didn’t need to ask what fate had befallen their owners.

“Did those boys pass in peace?”

The Keshik lowered the weapons that had become keepsakes and bowed his head.

“They fought bravely as warriors. Surely they’re now in Tengri’s embrace.”

“Yes. I see.”

Jamukha murmured softly.

Kill someone, and be killed by someone.

That was the inescapable fate of a warrior of the Great Steppe.

And it was the same for everyone else.

“What of the other losses?”

Everyone present already understood what he meant.

Even now, dozens of nomads were bleeding and falling somewhere in the gorge, but their lives were not part of any calculation.

Jamukha cared only about the losses among his personal guard.

“Though three commanders of a hundred have fallen, our overall casualties are small. Only around twenty are dead or wounded. The rest have withdrawn to the rear and await new orders.”

Three commanders had died, but their troops had suffered few losses. That could only mean one thing.

Remembering the commanders’ confidence that each of them was enough on his own, Jamukha let out a quiet laugh.

“They disobeyed my order.”

There was no doubt those three had fought a life-and-death duel.

One after another.

Foolish as commanders, brave as warriors.

And one by one, they must have lost their lives to the young Sword Demon of the Jin Family of Taiyuan.

“Those pathetic fools.”

Jamukha silently looked down at the Keshik, who could only bow his head even lower rather than agree. Then, abruptly, he spoke.

“Order the Keshik still in the gorge to charge.”

“Khan. You mean—”

“The senior ten-man commanders will temporarily take the vacant posts of commanders of a hundred. Minimize our losses as much as possible and wear them down.”

There would be no more reinforcements.

Several other commanders of a hundred remained at Jamukha’s side, but Eight Spring Gorge was only the first hill they had to cross.

He had no intention of wasting more strength in this narrow gorge—or of trusting the commanders who might do something foolish again at any moment.

He wanted a sure bet instead.

Not a fine steed or loyal hound that raced like the wind according to the direction of Jamukha’s reins, but a vicious dog that served the same master as he did.

*Ka-boom!*

Jamukha watched calmly.

Amid the tremendous roar that shook heaven and earth, a streak of red light came hurtling down toward the ground along with a section of the cliff.

* * *

*Fwoosh.*

The breeze felt cool as it brushed his hair.

It was a refreshing sensation he could never have experienced in the training hall deep inside the cave.

Like a reed swaying in the wind, Jin Mukyung twisted his body with ease.

*Shwaack!*

Five lances grazed his arms, legs, and waist as they passed.

Jin Mukyung reached out, and a gleaming white-silver blade slid along the steel shaft of a lance.

*Shhk!*

A cold slicing sound announced another death.

At the same moment, the strength and weight behind the shaft vanished.

Jin Mukyung seized the shafts that had crossed past him, grazing his body, and spun rapidly.

*Krrrunch!*

There were no screams. Only a thick mist of blood.

Using the five spears as the teeth of a gear and his own body as its axis, Jin Mukyung ground everything within a three-*jang* radius to pieces. He realized there were no enemies left around him.

And he realized that it wasn’t solely because of his own skill.

*Ka-boom! Rrrumble!*

The gorge shook.

Amid a deafening roar that seemed to split the sky, enormous and small rocks came pouring down. A streak of red light, bending like a living creature, flashed across Jin Mukyung’s eyes.

*Clang!*

A powerful impact struck his sword.

As Jin Mukyung retreated, a dull ache running up to his wrist, an exuberant voice reached his ears.

“Now that’s a shame. If I’d gotten a little more used to it, I could’ve landed a whopper.”

Chinggen.

He tossed aside his black-wood fishing rod, soaked in dark red blood, and raised two swords, one long and one short. He smiled.

At his new prey.
```
