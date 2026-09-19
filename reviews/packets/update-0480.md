<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0480.txt",
      "sha256": "27d936213df346b75551b31efcff7398cc310b79325f17e86b97a69c387248f0",
      "bytes": 13794
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "d1b5d844f759fdb84fa82f3a468d2c3ae6d1d3a9d08da6172cdf59119c0ac353",
      "bytes": 2562
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "3dcc6af57cd27b3f96cfa651d8fd4556ba676544b58b5746e8a6f3a66e9eee06",
      "bytes": 153787
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "7e24f371cb20788e9c46200ad1b79397c6ebb6ca3d7138ccb629fe6285b71d58",
      "bytes": 553
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "e88a51a323979279cdcc53c081160ce21f7f0ef895dc3f3c310af9129c927e47",
      "bytes": 771
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "7b2dc128f18c22576b85b43e0f1f610e892c29f2c8abfc4312edef5955605783",
      "bytes": 148573
    }
  ],
  "estimated_tokens": 8971
}
-->

# Durable State Update — Chapter 480

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 480. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 480. Profile updates may replace only one
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
  "chapter": 480,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 480,
    "continuity_sources": [480],
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
    "The Water God Dragon died after regaining its reason and giving Taekyung its purified Origin Essence, which humans call an inner core.",
    "The dragon's Memory Fragment showed its five-hundred-year history, including its benevolent rule of Dongting Lake and its sacrifice to contain the Gate's demonic qi.",
    "Taekyung identifies Honglan as the person who corrupted the benevolent Dongting Lake imugi and used it to kill many people.",
    "Honglan's silver hairpin carries a faint scent and was found in Taekyung's hair after the Memory Fragment ended.",
    "Honglan can enthrall people by seizing their emotions and souls; Officer Song is currently under her control and obeying her command to change the ship's destination.",
    "Taekyung has completed the Corrupted Spirit Beast Surprise Quest and acquired substantial EXP, Fame, and two Levels.",
    "The Gate or rift that corrupted the Water God Dragon remains connected to unresolved questions involving demonic qi and Dark Heaven.",
    "Honglan's motives, her exact relationship to Dark Heaven, and the full extent of her role in the Hubei incidents remain unresolved."
  ],
  "continuity_sources": [
    479,
    478
  ],
  "open_questions": [
    "What is the Dongting Fisherman's exact role within Dark Heaven, and how was he connected to the earlier destruction inside the secret refuge?",
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Did the Mutated Water Dragon destroy Donghu Stronghold and the related Yangtze River Channel League strongholds, and why was no Moving Formation trace left?",
    "Who created or controlled the Gate or rift that corrupted the Water God Dragon, and how is that power related to Dark Heaven?",
    "Why did Honglan corrupt the Water God Dragon and what is the full extent of her role in the Hubei incidents?"
  ],
  "safe_through": 479,
  "temporary_decisions": [
    "Render 광폭화 as Berserk and preserve the System Status distinction.",
    "Render 장수 돌침대 as Jangsu stone bed and 효자손 as hyojason, each with an explanatory footnote when used.",
    "Retain established jang and geun measurements, along with established renderings of live-fish sashimi and bone-in sashimi.",
    "Continue rendering 수염 as whiskers; distinguish Force, Sword Energy, Hellfire, and Water Breath.",
    "Render 원정 as Origin Essence, 내단 as inner core, and 꽃뱀 as flower snake with an explanatory footnote."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 상태               | **Status**                     |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 신령님 | **Mountain Spirit** | Jang-pal's mistaken address for the unnamed old man. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 오기조원 | **Five Qi Returning to Origin** | High martial realm displayed by Jeok Cheongang. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 의생 | **medical apprentice** | Mungyeong's occupation. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 무한 | **Wuhan** | Capital of Hubei Province near Dongting Lake. |
| 사공 | **boatman** | Old boatman piloting the ferryboat. |
| 호북성 | **Hubei Province** | Province where the chapter’s Dark Heaven incidents occurred. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 사공 | 신령 | terrified boatman to local lake spirit | Divine Spirit | terrified and deferential | The old boatman begs the Dongting Lake spirit to spare him. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 479
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 479
- **Aliases:** None
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, having passed the Divine Physician title to his Disciple, and he has reached the Returned to Youth realm.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple; Jeok Cheongang is an old acquaintance, and Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

## Korean source

```text
＃480화



“으음.”

주름이 자글거리는 눈가가 움찔거렸다. 신음과 함께 몸을 뒤척이던 노인은 한참이 지나서야 힘겹게 눈을 떴다.

‘이곳은……?’

축축하고 누렇게 찌든 벽지가 아니라, 부담스러울 만큼 새하얀 천장이 보인다.

잠시 상황을 파악하지 못한 채 멍하니 누워 있던 노인의 귓가에, 누군가의 차분한 목소리가 닿았다.

“정신이 드십니까?”

“으, 으응?”

목소리의 주인을 찾는 것은 그리 어려운 일이 아니었다.

화들짝 놀라 몸을 일으킨 노인은 작은 화로(火爐) 앞에 앉아 자신을 바라보는 한 청년을 발견할 수 있었다.

“뉘, 뉘십니까요?”

“의방(醫方)에는 결국 두 종류의 사람밖에 없습니다. 의생와 환자. 노인장께서는 아직 후자에 해당하는 분이시니 다시 자리에 누우시는 것이 좋겠군요.”

“아.”

노인은 그제야 이 낯선 공간이 의방이라는 사실을 깨달았다. 더불어 젊다 못해 어려 보이는 청년의 정체 역시도.

“의생 나리셨구먼요. 그런데 쇤네가 어째서 의방에…… 어이쿠.”

어리둥절한 표정으로 말을 잇던 노인은 문득 치미는 두통에 앓는 소리를 흘렸다.

이제야 알게 된 사실이지만, 가뜩이나 늙은 삭신은 안 쑤시는 곳이 없었고 땀에 흠뻑 젖은 채 파르르 떨리는 중이었다.

‘어이고, 대관절 이게 무슨 일이랴.’

머리를 부여잡고 끙끙거리는 노인을 구원해 준 것은, 어느새 방을 가로질러 다가온 젊은 의생이었다.

“지금부터 침을 놓아 드릴 테니, 진정하시고 천천히 호흡하십시오. 자, 하나. 둘…….”

투둑.

“어엇?”

노인은 눈을 동그랗게 떴다. 개미에 물린 것처럼 정수리가 따끔한가 싶더니, 두통이 씻은 듯이 사라져 버리는 것이 아닌가.

놀란 눈으로 자신을 바라보는 노인의 모습에 가느다란 세침(細針)을 든 젊은 의생이 빙긋 웃었다.

“괜찮으십니까?”

“예? 예.”

“그럼 다시 자리에 누우시지요. 이틀 동안 지켜본 바에 의하면 다행히 별문제는 없지만…… 그래도 아직은 몸을 움직이실 때가 아닙니다.”

“아, 알겠습니다요.”

참으로 신통하기 짝이 없는 의술에, 왠지 모르게 몸과 마음이 편안해지는 특유의 분위기까지.

가까이서 보니 생각보다 훨씬 더 어려 보였지만, 오히려 늙은 의생보다 노련하게 느껴질 지경이다.

“제가 잡아 드릴 테니, 몸에 힘을 푸시고 천천히 누우십시오.”

“예, 예에.”

홀린 듯이 자리에 누운 노인을 향해 젊은 의원이 손가락을 폈다.

“간단한 확인을 해 보아야겠습니다. 노인장, 지금 제가 손가락을 몇 개나 폈습니까?”

“세 개로 보입니다만.”

“지금은요?”

“두 개구먼요.”

“맞습니다. 노인장께서 사시는 곳과 존함, 춘추는 어찌 되십니까?”

“……그런 것도 말해야 합니까요?”

“정신이 완전하신지 확인하기 위해서입니다.”

“으음. 가만있어 보자.”

처음과 달리 이번에는 제법 머리를 굴려야 했다.

막 깨어난 노인의 상태는 아직 불안정했고, 그는 미세한 두통을 느끼며 천천히 입을 열었다.

“무한과 동정호 인근에서 평생을 살았고, 이름은 곽봉출입니다요. 워낙 대중없이 자란 탓에 정확한 나이는 모르지만 아마 고희(古稀)는 넘기지 않았을까 싶은뎁쇼.”

“곽 노인이셨군요. 춘추에 비해 매우 정정하신데. 무슨 일을 하십니까?”

“쇤네는, 그러니까. 그.”

눈살을 찌푸린 채 머뭇거리던 노인은 자신의 직업을 기억해 냈다.

“노 젓는 일을 합니다요.”

“뱃사공이시군요.”

“예에. 소싯적에는 상선의 수부 노릇을 했고, 제 배를 장만한 후로는 주로 동정호에서 선객들을 태우며 구경시켜 주는 일을 했습죠.”

어느새 노인, 아니 늙은 뱃사공은 옛 기억을 되짚으며 스스로 말을 이어 갔고, 그럴 때마다 젊은 의생은 부드러운 웃음과 함께 고개를 끄덕이며 맞장구쳐 주었다.

“같이 일하던 친한 형님이 있었는데, 그 형님이 쇤네에게 자고로 사내는 배를 장만하면 여자가 생긴다고 바람을 불어넣었습죠. 해서 큰맘 먹고 날렵한 놈으로다가 한 척을 장만했는데 그게 바로 백추(柏追)에서 만든 배였습니다요.”

“그렇습니까.”

“의생 나으리께서 백추를 아실랑가 모르겠네. 요즘에야 무한 나룻터에 가면 흔하게 찾아볼 수 있는 배지만, 제 젊을 때만 해도 백추에서 만든 선박을 모는 남자가 일등 신랑감이었습니다요. 아니면 아오디. 뱃머리에 동그라미 네 개 붙은 거.”

“오기조원 비슷한 느낌이로군요.”

“엥? 오기조원이 뭡니까요?”

“그런 게 있습니다. 넘어가시죠.”

“어쨌건 그때 장만했던 그놈이 참 날렵하고 예뻤지요. 여인네들도 많이 꼬시고. 언제는 옆 마을 과부 하나가 깊은 밤에 찾아와서 백추를 구경시켜 달라더니, 갑자기 옷고름을 확 풀어 버리는데……!”

“……조금만 더, 더 뒤로 넘어가시지요.”

젊은 의생은 나이답지 않은 인내심으로 이야기를 들어 주었고, 이야기가 계속되는 동안 견고하게 막혀 있던 기억의 둑은 서서히 허물어지기 시작했다.

그리고 아픈 몸도 잊고 신나게 말을 이어 가던 뱃사공은, 문득 떠오른 한 가지 기억과 함께 석상처럼 굳어 버렸다.

“……!”

그건 한 줄기 벼락이었고. 악몽과도 같은 기억이었다.

우르릉, 꽝!



‘크롸아아아아!’



귓가에 선명하게 울려 퍼지는 뇌성벽력과 분노에 찬 포효.

천천히 눈을 깜빡이자 검은 하늘을 등지고 선 거대한 존재의 모습이 눈앞을 스친다.

“으허억!”

자신도 모르게 튕기듯이 벌떡 일어난 뱃사공은 멍하니 허공을 응시했다.

“자, 자, 잠깐.”

떨리는 목소리와 부릅뜬 눈동자.

갑작스럽게 힘이 들어간 탓인지 다시금 삭신이 쑤셔 왔지만, 지금의 뱃사공에게 그런 것 따위는 안중에도 없었다.

기억의 둑이 허물어짐과 동시에 떠오른 기억들 때문이었다.

“의, 의생 나으리! 아까 전에 쇤네에게 뭐라고 하셨습니까요?”

“어떤 걸 말씀하시는지.”

“이틀! 이틀이 지났다고 그러지 않으셨습니까?”

덥석!

칠순을 넘긴 노인이라고는 믿기지 않을 만큼 강한 악력이 의생의 가느다란 팔목을 옥죄었다.

그러나 젊은 의생은 눈썹 하나 까딱하지 않고 차분하게 대답했다.

“그렇습니다만.”

“허어. 이런, 이런 일이!”

“진정하십시오. 노인장.”

“지, 지금 이럴 때가 아닙니다요. 어서 이 일을 사람들에게 알리고 높으신 분들에게 아뢰어야……!”

뱃사공은 반쯤 정신이 나간 상태였다.

그도 알아차리지 못하는 사이 땀에 흠뻑 젖은 전신은 덜덜 떨리고 있었고, 초점을 잃은 눈동자는 불안하게 사방을 훑었다.

마치 당장 무언가에 잡아먹히기라도 할 것처럼.

“한시라도 빨리 도망쳐야 합니다요. 어서!”

그때였다. 발작하듯 외치는 환자를 향해 젊은 의생이 손을 뻗은 것은.

스윽.

굳은살조차 배겨 있지 않은 새하얀 손이 약간 굽어 있는 등허리를 짚자, 따스한 온기가 흘러나와 환자의 내부를 가득 채웠다.

짐작할 수 없는 현상에 의해 비로소 안정을 되찾은 뱃사공이 숨을 헐떡였다.

“이, 이게 무슨.”

“틈틈이 익힌 잡기(雜技)라고 생각하시지요. 그리고 노인장.”

“흡.”

어째서일까, 의생의 깊고 투명한 눈동자와 눈을 마주친 뱃사공은 말문이 턱 막히는 것을 느꼈다.

그런 뱃사공을 물끄러미 응시하던 젊은 의생이 천천히 말을 이었다.

“노인장께서 걱정하시는 일은 결단코 일어나지 않을 것입니다. 아시겠습니까?”

“예?”

“간단합니다. 보고, 듣고, 겪었던 모든 것을 머릿속에서 지우십시오. 이틀 전 노인장께서는 관군을 따라 동정호에 불려 갔다가 몸 상태가 좋지 않아 쓰러지셨고, 바로 오늘 깨어나신 겁니다.”

“자, 잠시만 기다려 주십시오.”

“지금 제가 하는 말은 모두 사실입니다. 사실이 되어야 합니다. 그날 노인장께서는 어떤 선객도 태우지 않았고, 동정호의 신령도 보지 못했습니다.”

“……!”

뱃사공은 낙뢰에 맞은 사람처럼 몸을 부르르 떨었다.

눈앞의 젊은 의생이 건넨 말은 그만큼 충격적인 것이었다.

“그, 그 말씀은 의생 나으리께서도 신령님을 보셨다는……?”

“그럴 수도 있고, 아닐 수도 있지요. 하지만 단 하나 명심하셔야 할 것은…… 노인장께서 기억하시는 그 모든 일을 잊으셔야 한다는 겁니다.”

부드럽지만 칼날처럼 서늘한 목소리에, 뱃사공은 마른침을 삼켰다.

다음 순간, 방 안에 감도는 숨 막히는 침묵을 깨트린 것은 칠순이 넘은 노인이 가진 마지막 용기 덕분이었다.

“쇠, 쇤네를, 죽이실 생각이십니까요?”

“제가 말입니까? 아닙니다.”

천천히 고개를 내저은 젊은 의생이 말을 이었다.

“하지만 다른 누군가의 생각은 다를 수도 있겠지요. 당장 이를테면…… 흉흉한 소문을 원치 않는 호북성주라거나.”

“서, 성주께서!”

호북성주.

천자의 명을 받아 일성(一城)을 다스리는, 적어도 호북성 내에서는 왕이나 다름없는 존재다.

생각지도 못한 높으신 분의 등장에 반사적으로 외친 뱃사공은, 이내 자신의 실책을 깨닫고 눈앞이 캄캄해졌다.

‘이, 이런 멍청한 놈! 누가 듣기라도 하면 어쩌려고!’

그러나 그와는 반대로 젊은 의생의 안색은 편안했다.

두 사람이 나누는 대화가 이 방을 벗어나지 않도록 막은 장본인이기에 보일 수 있는 여유였다.

아니, 설령 새어 나간다고 하더라도 젊은 의생은 눈 하나 깜짝하지 않을 것이다.

이와 같은 조치는 그저 뱃사공의 목숨을 위한 것일 뿐이었다.

그 사실을 모르는 뱃사공은 잔뜩 숨죽인 목소리로 재차 입을 열었다.

“쇠, 쇤네는 살고 싶습니다요. 도대체 성주께서는 왜 이 보잘것없는 사공을 죽이려 하신단 말입니까.”

“홍수가 나고, 가뭄이 들고, 역병이 돌고. 사방에서 사람들이 죽어 나가면 곳곳에서 전란이 일어나지요. 그리고 왕후장상을 꿈꾸는 역도의 무리는 입을 모아 말합니다. 하늘의 뜻이 천자(天子)를 떠났다고. 이 썩어 빠진 나라를 뒤엎자고.”

작게 혀를 찬 젊은 의생이 몸을 일으키며 한 마디를 툭 내뱉었다.

“사람의 힘으로 어찌할 수 없는 재앙도 이럴진대, 산만큼 거대한 동정호의 신령이 미쳐 날뛰었다면 어찌 되겠습니까?”

“……!”

“수천이 죽었습니다. 장강과 동정호가 시신과 피로 채워졌고, 불야성을 이루던 거리는 어둠에 잠겼지요. 불안에 떠는 백성들의 이목이 호북성을 주시하는 지금, 노인장께서 보고 들은 바를 모두가 알게 된다면.”

뒷말은 이어지지 않았지만, 뱃사공은 숨 막히는 고요함 속에서 스스로 정답을 떠올렸다.

‘죽는다. 틀림없이.’

가난한 소작농 집안에서 태어나 까막눈으로 평생을 살아온 그였지만, 일흔이 넘도록 눈과 귀를 닫고 살지는 않았다.

오히려 수많은 선객을 배로 실어나르며 그들이 나누는 대화를 통해 세상 돌아가는 이치를 배울 수 있었다.

‘내, 내가 알고 있는 사실들을 입 밖에 내기라도 한다면.’

그때는 끝장이다.

옥좌에 앉은 천자도, 호북성주도 미쳐 버린 동정호의 신령이 수천의 인명을 해쳤다는 사실이 알려지길 원하지 않을 테니까.

아니, 어쩌면 당장 이 일에 관련된 모두를 제거할지도 모르는 일이다.

명문대파의 무림인이라면 모를까, 칠순 넘은 늙은 뱃사공 따위는 쥐도 새도 모르게 해치울 수 있다.

“허어. 허어어.”

그리고 혼이 나간 것처럼 숨을 토해내는 뱃사공을 향해, 구원의 동아줄이 내밀어졌다.

“모든 일을 기억에서 지우십시오. 배를 팔고, 입을 다문 채 남은 여생을 보내십시오. 하면 아무 일도 없을 겁니다.”

“그, 그게 정말입니까?”

“드릴 말씀은 그뿐입니다.”

젊은 의생은 그 말을 끝으로 자리에서 일어났다. 문을 향해 다가가는 그의 뒷모습을 넋 나간 눈빛으로 바라보던 뱃사공이 황급히 외쳤다.

“저, 정말 의생 나리가 맞습니까요?”

“물론입니다.”

딱 잘라 대답한 젊은 의생, 문경은 잡고 있던 문고리를 놓았다.

그리고 아직도 방 한구석에서 타오르는 화로와 그 위에서 천천히 끓고 있는 주전자를 가리키며 말을 이었다.

“제가 직접 끓인 탕약입니다. 하루 세 번. 식후에 드십시오. 꼭.”

마지막까지 환자를 챙기는 것은 의생의 의무다.
```

## Final English reading copy

```markdown
# Chapter 480

“Ugh.”

The wrinkled skin around the old man’s eyes twitched. He tossed and turned with a groan, then finally opened his eyes after a long while.

*Where is this…?*

Instead of damp, yellowing wallpaper, he saw a ceiling so starkly white that it was almost oppressive.

The old man lay there blankly, unable to make sense of the situation, until a calm voice reached his ears.

“Are you awake?”

“U-uh…?”

Finding the owner of the voice was not difficult.

The old man sat up with a start and saw a young man sitting before a small brazier and looking at him.

“Wh-who might you be?”

“There are ultimately only two kinds of people in a clinic: medical apprentices and patients. Since you still belong to the latter category, you should lie back down.”

“Ah.”

Only then did the old man realize that this unfamiliar place was a clinic. He also realized the identity of the young man, who looked barely more than a boy.

“So you’re a medical apprentice, sir. But why am I in a clinic… Ow.”

The old man had been speaking with a bewildered expression when a sudden headache rose through him, and he let out a groan.

Only now did he realize that his already-aged body ached everywhere, and that he was trembling, drenched in sweat.

*Good heavens. What on earth happened?*

The young medical apprentice had already crossed the room and came to his rescue.

“I’m going to place a few needles now. Relax and breathe slowly. All right. One. Two…”

*Tap.*

“Wha—?”

The old man’s eyes went round. The crown of his head prickled as though an ant had bitten him, and then his headache vanished as if it had been washed away.

The young medical apprentice smiled faintly as he held a slender needle and watched the old man stare at him in surprise.

“Are you all right?”

“Pardon? Yes.”

“Then lie back down. From what I’ve observed over the past two days, there doesn’t seem to be anything seriously wrong, fortunately… but you still shouldn’t be moving around yet.”

“Ah, I-I understand.”

His medical skills were nothing short of miraculous. On top of that, there was something about his presence that made both body and mind feel inexplicably at ease.

Up close, he looked much younger than expected, yet he seemed more seasoned than even an elderly medical apprentice.

“I’ll help you. Relax your body and lie down slowly.”

“Yes, yes.”

As the old man lay back down as though entranced, the young medical apprentice raised several fingers.

“I need to perform a simple check. Elder, how many fingers am I holding up?”

“It looks like three.”

“And now?”

“Two.”

“Correct. Where do you live, and what is your name and age?”

“…Do I have to tell you that too?”

“I need to make sure your mind is completely clear.”

“Hmm. Let me think.”

Unlike before, this required him to use his head a little.

The old man had only just awakened, and his condition was still unstable. Feeling a faint headache, he slowly opened his mouth.

“I’ve lived my whole life near Wuhan and Dongting Lake. My name is Gwak Bongchul. No one kept proper track when I was growing up, so I don’t know my exact age, but I reckon I must be past seventy.”

“So you’re Elder Gwak. You’re remarkably fit for your age. What do you do?”

“I… Well, I…”

The old man frowned and hesitated, but then he remembered his occupation.

“I row a boat.”

“You’re a boatman.”

“Yes. When I was young, I worked as a deckhand on a merchant ship. After buying my own boat, I mostly carried passengers around Dongting Lake and showed them the sights.”

Before long, the old man—no, the elderly boatman—began dredging up old memories and talking on his own. Each time he did, the young medical apprentice responded with a gentle smile and a nod.

“I had a close hyung I worked with. He told me that, ever since olden times, a man who bought a boat would soon find himself a woman. So I took the plunge and bought myself a sleek one. It was a boat made in Baekchu.”

“Is that so?”

“I wonder if you know Baekchu, sir. These days, you can find those boats everywhere at the Wuhan ferry docks, but when I was young, a man who piloted a vessel made in Baekchu was considered a first-rate husband prospect. Or an Audi. You know, the one with four circles on the bow.”

“That sounds somewhat like Five Qi Returning to Origin.”

“Huh? What’s Five Qi Returning to Origin?”

“It’s something. Let’s move on.”

“Anyway, that boat I bought back then was sleek and beautiful. It attracted plenty of women, too. Once, a widow from the neighboring village came to see me late at night and asked me to show her the Baekchu. Then she suddenly yanked her dress ties open…!”

“…Let’s skip a little farther ahead.”

The young medical apprentice listened with patience far beyond his years, and as the story continued, the dam blocking the boatman’s memories slowly began to crumble.

Then, as the boatman cheerfully continued talking without even noticing his aching body, one particular memory suddenly came back to him.

He froze like a stone statue.

“……!”

It was a bolt of lightning.

A memory like a nightmare.

*Rumble. Boom!*



*Graaaaaaah!*



Thunder and an enraged roar rang clearly in his ears.

He slowly blinked, and the figure of a massive being standing against a black sky flashed before his eyes.

“Gah!”

The boatman sprang upright without realizing it and stared blankly into the air.

“W-wait. Wait a moment.”

His voice trembled, and his eyes were wide open.

Perhaps because he had exerted himself so suddenly, every part of his body began aching again. But the boatman paid no attention to any of it.

The memories that had surfaced as the dam in his mind collapsed were all he could think about.

“Me-medical apprentice! What did you say to me earlier?”

“What are you referring to?”

“Two days! Didn’t you say that two days had passed?”

*Grab!*

A grip far too strong for a man over seventy clamped around the medical apprentice’s slender wrist.

But the young medical apprentice did not so much as twitch an eyebrow as he calmly replied,

“That is correct.”

“Good heavens. How could this happen?”

“Calm yourself, Elder.”

“T-this is no time to be calm. We must tell the people and report this to the higher-ups at once!”

The boatman was half out of his mind.

His entire body was drenched in sweat and trembling without his realizing it, while his unfocused eyes darted anxiously in every direction.

It was as though something might devour him at any moment.

“We have to get away as quickly as possible. Hurry!”

That was when the young medical apprentice reached out toward the patient shouting as though he were having a fit.

*Swish.*

A perfectly white hand, without even a callus, touched the old man’s slightly hunched back. Warmth flowed from the hand and filled his body.

The inexplicable phenomenon finally calmed the boatman, and he gasped for breath.

“Wh-what was that?”

“Think of it as a miscellaneous technique I’ve practiced from time to time. And, Elder.”

“Gasp.”

Why, he could not say, but the boatman met the medical apprentice’s deep, clear eyes and felt the words catch in his throat.

The young medical apprentice gazed at him for a moment before slowly continuing.

“The thing you’re worried about will never happen. Do you understand?”

“Pardon?”

“It’s simple. Erase everything you saw, heard, and experienced from your mind. Two days ago, you were summoned to Dongting Lake with the government troops, but you collapsed because you were feeling unwell. You woke up today.”

“P-please wait a moment.”

“Everything I’m telling you is true. It must become true. That day, you did not take any passengers, and you did not see the divine spirit of Dongting Lake.”

“……!”

The boatman shuddered as though he had been struck by lightning.

The young medical apprentice’s words were that shocking.

“D-does that mean you saw the divine spirit too, sir…?”

“That may be the case, or it may not. But there is one thing you must remember… You must forget everything you remember about those events.”

The boatman swallowed hard at the young man’s gentle yet blade-cold voice.

The next moment, the suffocating silence in the room was broken by the last bit of courage possessed by a man over seventy.

“D-do you intend to kill me?”

“Me? No.”

The young medical apprentice slowly shook his head and continued.

“But someone else may think differently. For example… the City Lord of Hubei Province, who would not want ominous rumors spreading.”

“T-the City Lord!”

The City Lord of Hubei Province.

An official who governed a city under the Son of Heaven’s orders—a figure who, at least within Hubei Province, was no different from a king.

The boatman cried out reflexively at the unexpected appearance of such a high-ranking person. Then he realized his mistake, and his vision went dark.

*What a stupid fool! What if someone heard me?*

Unlike him, however, the young medical apprentice’s expression remained relaxed.

It was the composure of someone who had ensured that none of their conversation could leave the room.

No—even if their words did leak out, the young medical apprentice would not bat an eye.

He had taken these precautions solely to preserve the boatman’s life.

Unaware of that fact, the boatman spoke again in a tightly hushed voice.

“I-I want to live. Why on earth would the City Lord want to kill an insignificant boatman like me?”

“When floods come, droughts strike, and plagues spread, people die in every direction, and wars break out everywhere. Then the rebels who dream of becoming kings and high officials speak with one voice. They say that the will of Heaven has left the Son of Heaven. That we should overthrow this rotten country.”

The young medical apprentice clicked his tongue softly, stood up, and tossed out one final remark.

“Even disasters beyond human power lead to this sort of thing. So what would happen if a divine spirit as enormous as a mountain went berserk in Dongting Lake?”

“……!”

“Thousands died. The Yangtze and Dongting Lake were filled with corpses and blood, and the streets that once shone like daylight were swallowed by darkness. With the frightened people watching Hubei Province, what do you think would happen if everyone learned what you saw and heard?”

He did not finish the sentence, but in the suffocating silence, the boatman arrived at the answer on his own.

*I’d die. Without a doubt.*

He had been born into a poor tenant farmer’s family and lived his entire life illiterate, but he had not spent more than seventy years with his eyes and ears closed.

If anything, carrying countless passengers by boat had allowed him to learn how the world worked by listening to their conversations.

*If I so much as speak the facts I know aloud…*

It would all be over.

Neither the Son of Heaven seated upon the throne nor the City Lord of Hubei Province would want people to learn that the mad divine spirit of Dongting Lake had killed thousands.

No, perhaps they would eliminate everyone involved in the matter immediately.

A martial artist from a prestigious sect might be another story, but an old boatman over seventy could be killed without anyone ever knowing.

“Good heavens. Oh, good heavens…”

As the boatman exhaled as though his soul had left his body, a lifeline was extended to him.

“Erase everything from your memory. Sell your boat and spend the rest of your life in silence. If you do that, nothing will happen.”

“W-will that really be enough?”

“That is all I have to say.”

The young medical apprentice finished speaking and rose from his seat. The boatman stared at his departing back with a dazed expression, then hurriedly called out.

“A-are you really a medical apprentice, sir?”

“Of course.”

The young medical apprentice, Mungyeong, answered without hesitation and released the doorknob.

Then he pointed to the brazier still burning in the corner of the room and the kettle slowly boiling atop it.

“I boiled that decoction myself. Three times a day. After meals. Make sure you take it.”

Caring for a patient until the very end was a medical apprentice’s duty.
```
