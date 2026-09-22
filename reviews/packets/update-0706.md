<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0706.txt",
      "sha256": "66037f58eb9b9571bfee5aabf228889bbf2ea1fb68d2f7219bfd05c76320a279",
      "bytes": 14994
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ea4ca4833ac8c7d6c579334e09d4691cca23e24944765109139ca74eed0b980f",
      "bytes": 2108
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "44efda40fb11818bced3bc50440faa3ea882ebde7307ad35d120ae460b9c7e4d",
      "bytes": 206699
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "06482081a7026af2bca8991b1dfe7fd79bd021374db10b07de4053daa60e9889",
      "bytes": 928
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "af1f3b216d62dc9a384c2dd82207040cdf116b2142620fed0f3b32c3b16e58ef",
      "bytes": 553
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "e3ab6dad7d2b27b7387547fa97377cee10bac33b7cc6a479d82e704ec69c8932",
      "bytes": 815
    },
    {
      "path": "characters/Wang Ho.md",
      "sha256": "a8b40030d5cc7c66ea9352a02274af0abcaf5248ec32a886059b37428909731c",
      "bytes": 489
    },
    {
      "path": "characters/White Tiger.md",
      "sha256": "4e76905ad621d3083acc66367c385dc5bc44939c8d25c8d21b836a19e2cbc2bc",
      "bytes": 603
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "c1bc45bc5b6686ae9866a499f07be1c2fba17ad90d86c37d772579eec9f5f4d8",
      "bytes": 216607
    }
  ],
  "estimated_tokens": 11159
}
-->

# Durable State Update — Chapter 706

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 706. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 706. Profile updates may replace only one
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
  "chapter": 706,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 706,
    "continuity_sources": [706],
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
    "Yayul Cheok has arrived at the Inner Palace and leads Jin Taekyung, the guardian spirit, and a large allied army against the Southern Heaven Demon Empress.",
    "Baeksang secretly trained the three-hundred-warrior Bai Baekcheon Unit in Wenshan and left its mobilization token and final instructions with Yayul Cheok.",
    "Wang Ho commands the Baekcheon Unit, which now serves under Yayul Cheok.",
    "The Beast King Stone awakened approximately three thousand Bai warriors, who joined Yayul Cheok after recognizing the correct path.",
    "Roughly thirteen thousand Nanman and Bai warriors now advance against the Southern Heaven Demon Empress and the mutants.",
    "The Southern Heaven Demon Empress's approximately five hundred elite subordinates were annihilated or captured.",
    "The mutants retreat before the sacred stone's power and recognize that the approaching coalition can defeat them.",
    "The guardian spirit carries Jin Taekyung and protects the advancing forces with sacred stone light.",
    "The Southern Heaven Demon Empress now raises a dragon tornado while facing the united forces."
  ],
  "continuity_sources": [
    705
  ],
  "open_questions": [
    "Can Yayul Cheok, Jin Taekyung, the guardian spirit, and the allied army defeat the Southern Heaven Demon Empress?",
    "Can the allied forces overcome the remaining mutants and end the Inner Palace crisis?",
    "What will happen when the Southern Heaven Demon Empress's dragon tornado fully confronts the advancing coalition?"
  ],
  "safe_through": 705,
  "temporary_decisions": [
    "Retain Fist Force, Force, Moving Formation, demonic martial arts, and Baekcheon Unit as established terminology.",
    "Render 궁주 as Palace Lord and 백천대주 as Commander of the Baekcheon Unit.",
    "Retain shichen for 시진 and the time it takes to drink a cup of tea for 일다경.",
    "Preserve Jin Taekyung's conversational profanity and the guardian spirit's terse, telepathic voice.",
    "Render 문산 as Wenshan, 태족 as Dai people, and 주군 as my lord."
  ],
  "version": 1
}
```

## Exact glossary matches

| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 대주     | **Squad Leader** / **Commander**             |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 경험치              | **EXP**                        |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 왕호 | **Wang Ho** | Commander of the Baekcheon Unit who arrives leading white-armored reinforcements. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 신성 | **Morning Star** | Term in the summons referring to the Master of Morning Star. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 권강 | **Fist Force** | Qi force projected through the Western Heaven Demon Lord's fist. |
| 소하 | **Xiao He** | Historical civil official invoked in the same exchange. |
| 변이체 | **mutant** | Taekyung's classification for the monster. |
| 영물 | **spiritual creature** | Known non-human creature contrasted with unheard-of monsters. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 애뇌산 | **Ailao Mountain** | Mountain crossed by the party on the route to the Nanman Beast Palace. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 독혈지 | **Poisonblood Grounds** | Hidden poisonous region created by the Five Poisons Sect inside Ailao Mountain. |
| 천년지주 | **Thousand-Year Spider** | Monster appearing at the end of the chapter. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 백천대 | **Baekcheon Unit** | Baeksang's secret elite unit, cultivated over decades and held in reserve. |
| 수호령 | **guardian spirit** | Ancient title for the Black Tiger. |
| 신석 | **sacred stone** | Stone said to have existed alongside the Black Tiger's birth. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 수호령 | 남천마후 | guardian_spirit_to_hostile_supernatural_opponent | you | terse, accusatory, and contemptuous | The guardian spirit tells the Southern Heaven Demon Empress that it knows her true essence and condemns her as a Fiend. |
| 남천마후 | 수호령 | hostile_supernatural_opponent_to_guardian_spirit | hideous beast | playful, taunting, and dismissive | She insults the guardian spirit while addressing it as a beast. |
| 왕호 | 야수묘왕 | Baekcheon Unit Commander to Nanman Beast Palace Palace Lord | Palace Lord | formal and deferential | Wang Ho bows and formally reports his arrival to the Beast Miao King. |

## Listed compact profiles

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 705
- **Aliases:** Heugung
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, and Great Chieftain of the Miao people; he has gathered roughly thirteen thousand allied warriors and now leads them against the Southern Heaven Demon Empress and the mutants.
- **Personality:** The Beast Miao King is boisterous and warmhearted toward Nanman's people, but their corruption and destruction awaken fierce grief and wrath in him.
- **Voice:** Low, growling, and forceful.
- **Relationships:** Baeksang is his sworn younger brother and childhood companion, Yayul Mok is his Young Palace Lord, Jeok Cheongang is an old acquaintance, and Jin Taekyung is Jeok's Disciple whom he now fights beside against the Southern Heaven Demon Empress.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 705
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 705
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress is Honglan, creator of the rift behind the Inner Palace; after her five hundred elites were annihilated, she faces the united Nanman forces and the approaching mutants while raising a dragon tornado.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

### Wang Ho.md

# Wang Ho (왕호)

- **Safe through:** Chapter 705
- **Aliases:** None
- **Role:** Wang Ho is the Commander of the Baekcheon Unit and leads its three hundred white-armored Bai warriors and beasts under Yayul Cheok.
- **Personality:** Not established.
- **Voice:** Formal and deferential when addressing the Palace Lord.
- **Relationships:** He commands the Baekcheon Unit and acknowledges Yayul Cheok as its Palace Lord.

### White Tiger.md

# White Tiger (백호)

- **Safe through:** Chapter 705
- **Aliases:** Whitey
- **Role:** The White Tiger is the guardian spirit of the sacred stone and leads the Sacred Land beasts, but both the stone's power and the White Tiger's strength are weakening under the rift's demonic qi.
- **Personality:** Irritable and contemptuous of Jin Taekyung's jokes.
- **Voice:** Telepathic, terse, and easily exasperated.
- **Relationships:** The White Tiger carries Jin Taekyung and Yohi, guards the sacred stone, and advances with Jin's forces.

## Korean source

```text
＃706화



문득 그런 생각이 들었다.

‘난 이제 좀 빠져도 되지 않나.’

대의. 희생정신. 살신성인. 그 외 기타 등등.

하나같이 다 좋은 말이다. 적당히 따뜻하고, 그러면서도 약간은 낯간지럽고. 뭐 좋은 말이긴 한데…….

‘지금까지 많이 한 것 같은데, 그거.’

대의를 위해 이 저주받은 대륙판 그린벨트까지 왔고, 희생정신을 전신에 두르다 못해 문신처럼 새긴 채 싸웠다.

아니, 남만에서 전투를 치른 횟수를 생각하면 그냥 싸웠다고 표현하는 것도 억울하다.

말 그대로 존나게 싸웠다.

숲에서. 들에서. 늪과 밀림에서.

집채만 한 크기의 거미들의 몸뚱어리에 창날을 박아 넣었다. 공을 탐내어 쉴 새 없이 몰려드는 남만 전사들에게는 불과 주먹으로 응수했다.

거기에서 끝났으면 차라리 낫다.

독혈지에서는 초절정 고수 두 명을 동시에 상대하는 미친 상황까지 겪었고, 부상의 여파에서 완전히 벗어나기도 전에 남천마후라는 괴물과 맞붙어야 했다.

‘거기다가 일섬까지.’

일섬(一殲).

말 그대로 일격에 모조리 죽인다는 뜻인데, 요즘 들어서는 그 ‘모조리’에 나도 포함되어 있는 건가 하는 의문이 든다.

무슨 시벌. 이 한 방에 공력을 쏟아붓는 건지, 수명을 쏟아붓는 건지.

그래도 나쁘지 않았다. 오늘이 인생 엔딩 보는 날인가 생각하던 찰나에 야수묘왕와 백천대가 등장했고, 야수묘왕의 도움으로 내상도 일부 회복한 데다가 이미 내궁 밖에 아군들이 득실거린다는 사실을 알게 되었으니까.

전세가 유리해졌다는 사실에 이제야 좀 숨통이 트이는 기분이었다.

웬 미친 호랑이가 급발진하기 전까지는.

쉬쉬쉭!

아니, 씹. 이 새끼 설마 주식이 콘푸로스트인가.

처음 애뇌산에서 맞닥트렸을 때부터 느꼈지만 수호령은 삼백 명의 백천대보다, 심지어 야수묘왕보다도 빨랐다.

이제는 폐허가 되어 버린 드넓은 내궁. 그리고 철벽처럼 앞을 가로막은 일천의 변이체.

그 너머에 존재하는 남천마후를 향해 은빛 동체가 바람처럼 쏘아진다.

동시에 머릿속에 울려 퍼진 수호령의 의념을 들은 나는 생각했다.

- 꽉 잡아라, 인간!

‘암살인가……?’

바로 그 순간이었다. 변이체들의 머리 위로, 거대하면서도 혼탁한 빛이 터져 나온 것은.

콰아아아아!

- 숙여라.

짤막한 의념과 함께 수호령이 신형을 기울였다. 힘이 실린 앞발이 지면을 밟고, 거대한 동체가 비스듬히 방향을 틀었다.

쐐액!

실로 영물다운, 아니 신수(神獸)라는 단어가 더 어울릴 법한 감각과 움직임.

강대한 공력이 실린 남천마후의 장력(掌力)이 목표를 잃고 지면을 후려쳤다.

꽈앙! 구구구궁!

폭발음과 함께 솟아오른 먼지구름.

그와 동시에 공간을 격하고 덮쳐 오는 무수한 파편을 향해, 나는 백염의 창날을 내리그었다.

쉭!

파공성을 일으킨 창날이 공간을 가르고, 장력의 충격파에 의해 튕겨진 무수한 파편들이 가루가 되어 흩날린다.

그리고 그 순간.

두두두두!

거대한 맹수의 등에 몸을 실은 수백의 인영(人影)이, 사방을 메운 어둠과 희뿌연 먼지구름을 뚫고 쏘아졌다.

엄청난 무게와 기세가 실린 삼각형의 쐐기진.

그 꼭짓점에 선 반백의 중년인, 야수묘왕이 일권(一拳)을 내질렀다.

후우웅, 쾅!

분노에 찬 외침도, 명령도 없다.

그러나 목소리 대신 터져 나온 녹색 권강(拳罡)은 단숨에 수십의 변이체를 짓이기며 공백을 만들었고, 삼백 개의 돌격창이 예리한 송곳이 되어 그 사이를 파고들었다.

콰드드드득!

핏물이 터져 나오고, 몸뚱이에서 떨어져 나간 사지가 하늘 높이 솟구친다.

일천 대 삼백. 인간과 맹수 대 괴물들의 전투.

서걱! 서걱!

쐐액, 푸푸푹!

“커헉!”

- 크아아아아!

끔찍한 비명과 절삭음이 사방에서 울려 퍼진다.

일제 돌격으로 어림잡아 수백에 달하는 변이체를 뭉개 버린 백천대를 기다리고 있던 것은 치열한 백병전(白兵戰)이었고, 야수묘왕은 그 너머에서 자신을 기다리고 있을 진정한 적을 향해 쏘아졌다.

“남천마후!”

포효와 함께 빛살처럼 나아간 신형. 곧이어 아득한 섬광을 실은 격돌의 여파가 지축을 뒤흔든다.

콰앙! 구구궁!

서로를 향해 얽혀드는 무수한 움직임과 날이 선 병장기들. 그들의 머리 위로 녹색 강기에 밀려 조금씩 흩어지는 어둠이 보였다.

‘남천마후는 이미 지쳤다. 야수묘왕이 우세해.’

그러나 백병전으로 돌입한 전장의 상황은 그리 좋지 못했다.

변이를 겪으며 더더욱 크고 강해진 맹수들은 일류 고수 못지않았고, 인간이었을 적의 무공을 고스란히 간직하고 있는 전사들은 전과는 비교할 수 없는 속도로 움직이며 백천대를 노렸다.

바로 지금처럼.

쉭, 서걱!

예리한 절삭음과 함께 변이체의 목이 솟구친다.

뒤늦게 자신의 등 뒤에서 벌어진 일을 알아챈 백천대 전사가 크게 뜨인 눈으로 나를 바라봤다.

“아무리 바빠도 뒤는 잘 살펴보셔야지.”

“고맙소. 한데 당신은……?”

야수묘왕, 그리고 백천대.

이 두 가지 갈림길에서 잠시 고민하던 나는 대답했다.

“아군입니다. 제가 앞장설 테니 따르세요.”

어쩔 수 없는 선택이다.

그나마 한 사람, 한 사람이 최소 초일류의 경지에 올라 있는 백천대라 수적 열세인 상황에서도 이만큼 맞설 수 있는 거지. 이미 마기에 완전히 잠식당한 변이체들의 힘은 강력했다.

야수묘왕이라는 구심점이 사라진 이상, 나와 수호령이 선봉장의 역할을 해야 한다.

“……시바. 생각해 보니까 내가 왜.”

- 투덜거리면서도 잘만 싸우는 것처럼 보이는 건 기분 탓인가?

“솔직히 말해라. 너 나한테 원한 있지.”

퍼걱!

마기가 주는 흉포함인지, 아니면 지휘관을 지키고자 하는 충성심 때문인지.

뿌옇게 솟아오른 먼지구름 너머, 시야를 가득 메우며 달려든 변이체를 단번에 으스러트린 수호령이 되물었다.

- 원한?

“다 알아, 이 새끼야. 내가 애뇌산에 불 지른 것 때문에 이 악물고 급발진 한 거잖아.”

콰드드득!

한 번 휘두른 앞발에 네댓 마리의 목이 뜯겨 나간다. 호랑이 주제에 혀를 찬 수호령이 대답했다.

- 웃기지도 않는군.

“확실해?”

- 아니다.

“그럼 위층 살던 천년지주의 복수냐?”

- 그건 또 무슨 헛소리지?

“곰곰이 생각해 봤는데 아무리 봐도 수상해. 그런 말도 있잖아. 우리들의 다정한 이웃. 천년 스파이더…… 위!”

푸푹!

외침과 함께 뻗어 낸 백염의 창날이, 수호령의 머리 위로 그림자를 드리우며 달려든 호랑이의 머리를 정확히 관통했다.

크륵…….

순식간에 잦아드는 울음소리. 나는 단말마와 함께 숨이 끊긴 호랑이를 창날에 꽂은 상태로 크게 휘둘렀다.

후웅, 콰직!

족히 수백 근이 넘는 사체가 날아가 또 다른 변이체들을 짓이겼다.

“원한에 사무친 놈이 아니고서야, 나처럼 요양이 필요한 환자를 이런 난장판에 집어넣을 리 없어. 이게 내가 내린 결론이다.”

쉭! 서걱!

물 흐르듯 횡으로 휘두른 창날의 궤적을 따라, 다섯 개의 목이 솟구쳤다.

달려드는 속도 그대로 허물어지는 목 없는 시체들. 그 광경을 물끄러미 바라보던 수호령이 중얼거렸다.

- 내가 아는 그 환자와 다른 뜻인 것 같은데.

“미친놈인가. 지금 내 상태 안 보여?”

- 직접 보고 있으니 하는 말이다.

“그건 네가 내 상태를 몰라서 그래. 숨만 쉬어도 뼈마디가 쑤시는데.”

푸푹!

- 창으로 이곳저곳 잘만 쑤셔 대면서 그런 말 해 봤자 아무런 설득력도 없다.

“빌어먹을. 이건 그냥 어떻게든 살아 보려고…….”

- 혹시 알고 있나?

“뭐?”

- 넌 인간치고 거짓말이 너무 서툴러.

“그게 뭐…….”

말을 이을 틈조차 없었다.

퍼걱, 쉬이익!

피를 머금은 은빛 갈기가 흩날린다. 변이체를 머리를 터트리며 허공으로 솟구친 수호령이 하강과 동시에 앞발을 휘두른다.

갈고리처럼 날카로운 발톱에는 칼날 같은 바람과, 강기(罡氣)라 불려야 할 기운이 실려 있었다.

콰앙! 구구궁!

단 일격.

굉음과 진동 사이로 수십의 변이체가 피떡이 되어 튕겨 나가고, 그보다 많은 변이체들이 빈자리를 메우며 달려들었다.

쉬쉬쉭!

- 쿠에에엑!

괴성과는 어울리지 않는, 신속하면서도 맹렬한 움직임.

몇몇 변이체들의 병장기에서 줄기줄기 쏟아지는 검기(劍氣)는, 그들이 한때 남만에서도 이름난 전사였음을 알려 주는 증거다.

하지만…….

- 크아아앙!

오로지 신석(神石)을 위해 존재하는 수호자. 그 누구도 본 적 없을 거대한 백호의 포효에 변이체들의 몸이 덜컥 굳는다.

그와 동시에 미리 약속이라도 한 것처럼, 나는 백염을 비스듬히 내리그었다.

‘벤다. 단숨에.’

삼 갑자에 달하던 열양지기도, 투명한 창날을 휘감으며 타오르던 청백색의 화염도 이제는 찾아볼 수 없다.

지금의 내게 남은 건 한 줌이나 될까 싶은 공력과 물먹은 솜처럼 무거운 몸뚱어리. 그리고 유일하게 믿을 수 있는 백염이라는 신병이기가 전부다.

분명히 그것뿐인데…… 잘 모르겠다.

서걱!

쉼 없이 베고.

푸푹!

찌르고.

퍼걱!

휘두르며 변이체들과 싸우고 있는 이유를.

그러면서도 수호령의 등에서 떨어지지 않기 위해 고통을 호소하는 다리에 힘까지 줘 가며 버티고 있는 이유를.

아니, 어쩌면 어렴풋이 알 것 같기도 했다.

조금 전 수호령이 내게 했던 말의 의미도.

“……젠장.”

나도 모르게 흘러나온 욕설에, 수호령이 나직하게 웃었다.

- 말하지 않았느냐. 넌 거짓말이 서투르다고.

“…….”

- 네가 살고자 했다면, 처음부터 이 자리에 오지도 않았을 것이다. 하지만 넌 지쳤음에도 이 싸움을 멈추지 않는구나.

“됐다. 입 다물어.”

- 무엇 때문이냐? 너와 같은 인간에서 괴물로 전락해 버린 자들이 불쌍해서? 아니면 이들을 괴물로 만든 어느 추악한 인간의 숨통을 끊고 싶어서?

“……!”

머릿속에서 속삭이는 듯한 그 의념을 들은 순간, 숨이 막히고 가슴 깊숙한 곳에서 뜨거운 무언가가 울컥 차올랐다.

그러나 뻗어 나간 손은, 또 다른 변이체의 목을 향해 창을 찔러 가고 있었다.

푹!

투명한 창날이 살을 가르고 뼈를 끊는다. 흰자위 없이 새카맣게 물들어 있던 상대의 눈동자에서 서서히 걷혀 나가는 어둠이 보였다.

그리고 그 빈자리에 드리워진 죽음도.

털썩.

허물어지는 신형. 기괴하게 일그러진 얼굴로 숨이 끊긴 이름 모를 전사를 바라보던 나는 문득 중얼거렸다.

“고통을 느꼈을까.”

- 그래. 아마도.

퍼걱!

내가 움직임을 멈춘 틈을 노려 달려들던 표범이 포탄처럼 튕겨 나간다.

거대한 앞발을 휘둘러 변이체를 절명시킨 수호령이 담담하게 의념을 이어 나갔다.

- 하지만 그 짧은 고통의 순간 뒤에는, 크고 따뜻한 안식(安息)이 기다리고 있었을 것이다. 지금의 저들에게는 살아 있는 것 자체가 고통일 테니까.

“……!”

- 저들은 널 원망하지 않는다. 그러니 인간이여. 더 이상 스스로를 자책하지 말아라.

제기랄.

나도 안다. 난 최선을 다했다. 늘 죽음을 무릅쓰며 싸웠고 끔찍한 재앙을 막고자 여기까지 왔다.

하지만 언제나 그랬듯, 최선의 노력이 최선의 결과로 나타나지는 않았다.

‘막아야 했는데.’

끝끝내 막지 못했다. 많은 이들을 구했지만, 많은 이들 역시 구하지 못했다.

결국 내가 할 수 있는 일이라고는 최선을 다해 저들의 목숨을 끊어 주는 것밖에는 없다.

바로 지금처럼.

후우우웅!

온 힘을 다해 휘두른 창날이 바람을 찢고 공간을 가른다. 동시에 일섬의 여파를 고스란히 감당해야 했던 전신이 비명을 지른다.

순간 눈앞이 새하얗게 물들 정도의 격통.

그러나 나는 이를 악물고 참아 냈다. 무시무시한 힘과 속도를 머금은 한 자루의 창을, 한때 나와 같은 인간이었을 그들을 향해 쏟아냈다.

콰드드득!

창날이 그린 거대한 궤적. 그 끝에서 휘몰아친 광풍(狂風)이 검붉은 핏물을 머금었다.

잘려 나간 목과 사지가 솟구치고, 무수한 죽음과 안식이 뒤를 이었다.

띠링. 띠링. 띠링.

처음이다. 경험치 획득을 알리는 저 맑은 종소리에 귀를 막고 싶어진 것도. 피를 뿌리며 허물어지는 적들의 모습이 이토록 서글프게 느껴진 것도.

하지만 나는 움직임을 멈추지 않았다.

서걱. 서걱. 서걱!

베고. 베고. 또 벴다.

앞길을 가로막는 모든 것들이 사라질 때까지. 창날이 텅 빈 허공을 가를 때까지.

후웅!

세상이 기울어진다.

아니, 창날에 실린 힘을 이기지 못한 몸뚱어리가 기울어진다.

그리고 다음 순간, 수호령의 등 위에서 굴러 떨어지려는 내 몸을 누군가의 투박한 손이 붙들었다.

“끝났소. 그만하시오.”

백천대주 왕호.

경악과 놀라움이 담긴 그의 목소리에 거친 숨을 몰아쉬며 주위를 둘러보았다.

어느새 절반도 넘게 줄어든 백천대와, 사방에 고인 피 웅덩이에 잠긴 무수한 시신들이 보인다.

하지만…….

‘아니야.’

그의 말은 틀렸다.

이 싸움은, 오늘의 재앙은 끝나지 않았다.

적어도 한 사람의 숨통을 완전히 끊어 놓지 않는 한은.

“가자.”

- ……인간이여.

“끝내야 해.”

갈라진 입술 사이로 흘러나온 목소리에, 뭐라 대답하려던 수호령이 무겁게 신형을 내뻗는다.

쉬쉭!

전신을 휩쓰는 바람. 우리가 향하는 그 길의 끝에는, 피를 토하면서도 살고자 몸부림치는 한 사람이.

아니, 괴물이 있었다.
```

## Final English reading copy

```markdown
# Chapter 706

A thought suddenly occurred to me.

*Can’t I sit this one out now?*

The greater good. A spirit of self-sacrifice. Self-sacrifice unto death. And so on.

They were all good words. Warm enough, but also a little embarrassing. They were good words, sure, but…

*I feel like I’ve done plenty of that already.*

I had come all the way to this cursed continent-sized greenbelt for the greater good, and I had fought while wearing my spirit of self-sacrifice over my entire body—so thoroughly that it might as well have been tattooed onto me.

No, considering how many battles I had fought in Nanman, even calling it fighting felt unfair.

I had fought a fucking lot.

In forests. On plains. In swamps and jungles.

I had driven spearheads into the bodies of spiders the size of houses. Against the Nanman warriors who swarmed toward me without pause, hungry for glory, I had answered with fire and fists.

It would have been better if things had ended there.

At the Poisonblood Grounds, I had found myself in the insane situation of facing two Supreme Peak masters at once. And before I had even fully recovered from those injuries, I had been forced to fight a monster known as the Southern Heaven Demon Empress.

*And then there was One Annihilation.*

One Annihilation.

It literally meant killing everything with a single strike, but lately, I had begun to wonder whether *everything* included me.

What the fuck was I pouring into that one blow? My internal energy—or my lifespan?

Still, things had not turned out too badly. Just when I had been wondering whether that was the day I would see the ending of my life, the Beast Miao King and the Baekcheon Unit had appeared. With the Beast Miao King’s help, I had partially recovered from my Internal Injury, and I had also learned that allies were already swarming outside the Inner Palace.

The fact that the battle had turned in our favor finally let me breathe a little easier.

At least until a certain insane tiger suddenly accelerated.

Whoosh!

No, fuck. Was this guy’s staple food Frosted Flakes?

I had sensed it from the first time we encountered him on Ailao Mountain, but the guardian spirit was faster than the three hundred members of the Baekcheon Unit—and even faster than the Beast Miao King.

Across the vast Inner Palace, now reduced to ruins, one thousand mutants formed a wall like an iron rampart.

Toward the Southern Heaven Demon Empress beyond them, the guardian spirit’s silver body shot forward like the wind.

As I heard the guardian spirit’s thought echo through my mind, I thought,

—Hold on tight, human!

*Is this an assassination attempt…?*

It happened at that exact moment.

A massive, murky light burst above the heads of the mutants.

Kraaaaaaash!

—Duck.

Along with the brief thought, the guardian spirit tilted its body. Its powerful forepaw struck the ground, and its enormous body changed direction at an angle.

Whoosh!

Its senses and movements were truly worthy of a spiritual creature—or rather, the term *divine beast* seemed even more appropriate.

The Southern Heaven Demon Empress’s palm strike, packed with tremendous internal energy, missed its target and slammed into the ground.

Boom! Rumble, rumble!

A cloud of dust rose with the explosion.

At the same time, I brought the spearhead of White Flame down toward the countless fragments that flew through the air and came crashing toward us.

Whoosh!

The spearhead split the air with a shrill whistle. The countless fragments thrown outward by the impact of the palm strike were reduced to powder and scattered on the wind.

And then—

Thud-thud-thud-thud!

Hundreds of figures mounted on enormous beasts shot through the surrounding darkness and the pale cloud of dust.

A triangular wedge formation carrying tremendous weight and momentum.

At its tip, a middle-aged man with half-gray hair thrust out one fist.

The Beast Miao King.

Fwoom! Boom!

There was no furious shout. No command.

But the green Fist Force that erupted in place of his voice crushed dozens of mutants in an instant, opening a gap. Three hundred charging spears became sharp awls and drove into it.

Kra-crack!

Blood burst into the air, and severed limbs flew high above the ground.

One thousand against three hundred. Humans and beasts against monsters.

Slice! Slice!

Whoosh, stab-stab-stab!

“Guh!”

—Kraaaaaaang!

Horrible screams and the sounds of cutting rang out in every direction.

What awaited the Baekcheon Unit after their initial charge crushed hundreds of mutants was a fierce close-quarters battle. Beyond it, the Beast Miao King shot toward the true enemy waiting for him.

“Southern Heaven Demon Empress!”

His body surged forward like a streak of light alongside his roar. A moment later, the aftermath of their collision, carrying a distant flash of light, shook the foundations of the earth.

Boom! Rumble!

Countless movements tangled together, along with sharp weapons flashing in every direction. Above their heads, the darkness slowly scattered under the pressure of the green Force.

*The Southern Heaven Demon Empress is already exhausted. The Beast Miao King has the advantage.*

But the battlefield that had descended into close combat was not going well.

The beasts that had grown even larger and stronger through mutation were no weaker than First Rate masters. The warriors who retained all the martial arts they had possessed as humans moved at speeds incomparable to before as they targeted the Baekcheon Unit.

Just like now.

Whoosh, slice!

A mutant’s head flew into the air with a sharp cutting sound.

Only belatedly realizing what had happened behind him, the Baekcheon warrior stared at me with wide eyes.

“No matter how busy you are, you should watch your back.”

“Thank you. But you are…?”

The Beast Miao King, or the Baekcheon Unit.

As I hesitated for a moment between those two choices, I answered,

“I’m an ally. I’ll lead the way, so follow me.”

It was a choice I could not avoid.

The Baekcheon Unit could stand against such overwhelming numbers because every single one of its members had reached at least the realm of a Supreme First Rate master. The mutants, whose bodies had been completely consumed by demonic qi, were powerful.

With the Beast Miao King no longer acting as their rallying point, the guardian spirit and I had to take the lead.

“…Shit. Now that I think about it, why the hell am I—”

—Am I imagining it, or do you seem to fight just fine while complaining?

“Tell me honestly. You have a grudge against me, don’t you?”

Crack!

Whether driven by the ferocity granted by demonic qi or by loyalty to the commander it sought to protect, a mutant charged out of the hazy dust cloud and filled my vision—only for the guardian spirit to crush it in a single blow.

—A grudge?

“Don’t play dumb, you bastard. You accelerated like your life depended on it because I set fire to Ailao Mountain.”

Kra-crack!

Four or five heads tore free under a single sweep of its forepaw. The guardian spirit clicked its tongue—despite being a tiger—and answered,

—How ridiculous.

“Are you sure?”

—No.

“Then is this revenge for the Thousand-Year Spider that lived upstairs?”

—What nonsense are you spouting now?

“I thought about it carefully, and the whole thing is suspicious. You know what they say. *Our friendly neighborhood Thousand-Year Spider… up!*”

Stab!

With my shout, the spearhead of White Flame shot out and pierced straight through the head of the tiger that had leaped toward us, casting a shadow over the guardian spirit’s head.

Grrrk…

The cry quickly faded away. With the tiger’s life extinguished in its death rattle and its body still impaled on my spearhead, I swung it with all my strength.

Fwoom! Crack!

The carcass, weighing several hundred pounds at least, flew through the air and crushed other mutants.

“Unless you’re consumed by a grudge, why would you throw a patient who needs to recuperate into a mess like this? That’s the conclusion I reached.”

Whoosh! Slice!

Five heads flew into the air along the path of the spearhead as I swept it sideways like flowing water.

The headless corpses collapsed at the same speed they had charged. The guardian spirit stared blankly at the sight and muttered,

—I think you mean a different kind of patient from the one I know.

“Are you insane? Can’t you see my condition?”

—I’m saying this because I’m looking at it directly.

“That’s only because you don’t understand my condition. Even breathing makes my bones ache.”

Stab!

—You keep stabbing meaty things here and there with your spear. Don’t say that as though it’s convincing.

“Damn it. I’m only doing this because I’m trying to survive somehow…”

—Do you know something?

“What?”

—For a human, you are remarkably bad at lying.

“What does that—”

I did not even have time to finish.

Crack! Whoosh!

A silver mane wet with blood scattered through the air. The guardian spirit leaped upward after bursting a mutant’s head, then swung its forepaw as it descended.

Its hooklike claws carried blade-sharp wind and an energy that could only be called Force.

Boom! Rumble!

One strike.

Amid the thunderous sound and the vibrations, dozens of mutants were sent flying as bloody pulp, and even more mutants rushed forward to fill the empty space.

Whoosh!

—Kweeeek!

Their movements were swift and ferocious, completely at odds with their grotesque cries.

Sword Energy pouring in streams from the weapons of several mutants was proof that they had once been warriors renowned even in Nanman.

But…

—Kraaaaaaang!

The guardian of the sacred stone, existing solely for its sake.

At the roar of the enormous White Tiger, a creature no one else had ever seen, the mutants’ bodies froze.

At the same time, as though we had arranged it beforehand, I brought White Flame down at an angle.

*Cut them. All at once.*

The Scorching Yang Qi that had amounted to three jiazi was gone. So was the blue-white flame that had once wound around the transparent spearhead and burned.

All I had left now was a body as heavy as waterlogged cotton, along with a small amount of internal energy—so little that I wondered whether it could fill even one handful—and the only divine weapon I could still trust: White Flame.

That was all, without a doubt, but…

I did not know.

Slice!

Why I kept cutting without pause.

Stab!

Why I kept stabbing.

Crack!

Why I kept swinging my spear as I fought the mutants.

Why, even then, I forced strength into my aching legs to keep from falling off the guardian spirit’s back.

No. Perhaps I dimly understood.

Even the meaning behind what the guardian spirit had said to me moments earlier.

“…Damn it.”

At the curse that slipped from my lips before I could stop it, the guardian spirit laughed softly.

—I told you. You are bad at lying.

“…”

—If you wanted to live, you would never have come here in the first place. And yet, even though you are exhausted, you refuse to stop fighting.

“Enough. Shut up.”

—Why is that? Because you pity those who were once human like you before falling into monsters? Or because you want to kill the vile human who turned them into monsters?

“……!”

The moment I heard the thought that seemed to whisper inside my head, I found it hard to breathe. Something hot surged up from deep inside my chest.

But the hand I thrust forward was still driving my spear toward another mutant’s throat.

Thrust!

The transparent spearhead tore through flesh and severed bone. I saw the darkness slowly recede from the opponent’s eyes, which had been stained completely black without a trace of white.

And in that empty space, I saw death settle in.

Thud.

The body collapsed. I stared at the unknown warrior whose life had ended with his face twisted grotesquely, then muttered,

“Did he feel pain?”

—Yes. Probably.

Crack!

A leopard that had charged at me the moment I stopped moving was sent flying like a cannonball.

The guardian spirit swung its massive forepaw and killed the mutant, then continued in a calm voice.

—But after that brief moment of pain, a great and warm rest must have been waiting. For those people, simply being alive must be agony.

“……!”

—They do not resent you. So, human. Stop blaming yourself.

Damn it.

I knew that. I had done my best. I had always fought while risking death, and I had come all this way to stop a terrible disaster.

But as always, the best effort did not necessarily produce the best result.

*I should have stopped it.*

In the end, I had failed to stop it. I had saved many people, but I had also failed to save many others.

Ultimately, the only thing I could do was end their lives with everything I had.

Just like now.

Fwoooooosh!

The spearhead I swung with all my strength tore through the wind and split the air. At the same time, my entire body, which had endured the full aftermath of One Annihilation, screamed.

A burst of agony so intense that my vision turned white.

But I gritted my teeth and endured it. I sent a single spear packed with terrifying strength and speed toward the people who had once been human like me.

Kra-crack!

The spearhead carved a huge arc through the air. At its end, a raging gale became soaked in dark red blood.

Severed heads and limbs flew through the air, followed by countless deaths and moments of rest.

Ding. Ding. Ding.

This was the first time.

The first time I had wanted to cover my ears at the clear ringing of the chimes announcing EXP gained. The first time the sight of my enemies collapsing while spraying blood had felt so unbearably sorrowful.

But I did not stop moving.

Slice. Slice. Slice!

I cut.

I cut again.

And I cut once more.

Until everything blocking the road ahead had disappeared. Until the spearhead cut through nothing but empty air.

Fwoom!

The world tilted.

No—the body that could not withstand the force carried by the spearhead tilted.

And in the next moment, just as I began to roll from the guardian spirit’s back, a rough hand caught me.

“It’s over. Please stop.”

Commander of the Baekcheon Unit Wang Ho.

Breathing harshly at the astonishment and shock in his voice, I looked around.

The Baekcheon Unit had been reduced by more than half. Countless corpses lay submerged in pools of blood gathered in every direction.

But…

*No.*

He was wrong.

This fight—and today’s disaster—was not over.

Not until I had snuffed out one particular person’s life for good.

“Let’s go.”

—…Human.

“We have to finish it.”

At my voice, which slipped through cracked lips, the guardian spirit seemed about to answer. Instead, it pushed its heavy body forward.

Whoosh!

Wind swept over my entire body.

At the end of the road we were traveling, one person was struggling to live despite vomiting blood.

No.

There was a monster.
```
