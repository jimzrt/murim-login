<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0722.txt",
      "sha256": "5d3b8106aa717f9e338a93a6959ebe89cc8c67372f8ca90e2fd2ccf2f3d26c43",
      "bytes": 13062
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "744cf6a12cb5fec900a4c16705d0a9534fca39bc6b05c0aecf685eb2a1e4cf4e",
      "bytes": 1679
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "fad24bf831e409de23ad22d012a16ee7ec29c19d46976712201a788c54b29e39",
      "bytes": 208938
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "14f18092807e164b9603b44a976385a057ae4f59028066f97ad18ca5ab62de4e",
      "bytes": 935
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "1993c1e6cc8338562c8b074e8106199dd8dbd3ad7592443e548bb2879c1aa2bb",
      "bytes": 902
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "4e2f31b75831767fede98b5647376856ee7afe2bec71f9401ce841a8c3c29719",
      "bytes": 553
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "927edb8cd407cdca894271c469241b1dba9eb32bb14a233127a74b1baad48c40",
      "bytes": 1702
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8c9370e66f36ae1c5da9e5fb2bed205edcf0688392c7bf8f70a9318539923074",
      "bytes": 219239
    }
  ],
  "estimated_tokens": 9897
}
-->

# Durable State Update — Chapter 722

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 722. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 722. Profile updates may replace only one
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
  "chapter": 722,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 722,
    "continuity_sources": [722],
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
    "The Sacred Land is distinct from the Poisonblood Grounds and is Nanman's life-filled heart.",
    "The Sacred Land's Pond of Life heals living bodies and purifies evil or impure energy.",
    "Jin Taekyung completed Quest [Corrupted Divine Artifact] by immersing the corrupted sacred stone in the Pond of Life.",
    "The artifact's demonic qi was completely purified, and the artifact became a new sacred stone.",
    "The Pond of Life released its remaining life energy as rain across Nanman.",
    "The life-filled rain heals wounds and fatigue and causes flowers and sprouts to bloom.",
    "The new sacred stone will remain in Nanman with a new guardian spirit.",
    "Muyaho is the new guardian spirit and is affectionate toward Jin Taekyung.",
    "Jeok Cheongang wanted to take the new guardian spirit, but the Beast Miao King refused.",
    "The Nanman Beast Palace is being rebuilt after the Inner Palace's devastation and the Outer Palace's heavy damage.",
    "Jin Taekyung has established the Earth Mother Goddess as a public religious doctrine in Nanman.",
    "The Beast Miao King is publicly regarded as the Earth Mother Goddess's chosen priest."
  ],
  "continuity_sources": [
    721
  ],
  "open_questions": [
    "How will Muyaho's new role as guardian spirit develop?",
    "When will the Pond of Life recover its lost energy?"
  ],
  "safe_through": 721,
  "temporary_decisions": [
    "Render 대지모신 as Earth Mother Goddess.",
    "Render 목신 as Wood God and 화신 as Fire God.",
    "Render 제사장 as priest when used for the Beast Miao King.",
    "Render 알쓸잡신 as useless gods."
  ],
  "version": 1
}
```

## Exact glossary matches

| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 일신     | **One God**         |
| 십왕     | **Ten Kings**       |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 명성               | **Fame**                       |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 대한민국 | **Korea** | Country reference. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |
| 비도 | **throwing blade** | Mungyeong throws one past Taekyung's neck. |
| 대전쟁 | **Great War** | The long war that ended after the Great Cataclysm. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 대회의 | **Tribal Grand Council** | Nanman's council of great chieftains. |
| 궁주 | **Palace Lord** | Title Yohi uses after realizing that Heugung is the Beast Miao King. |
| 대지모신 | **Earth Mother Goddess** | New deity proclaimed by Jin Taekyung as Nanman's One God. |
| 목신 | **Wood God** | A local deity worshiped by one Nanman believer. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 백상 | 야수묘왕 | Nanman great chieftain to the Nanman Beast Palace Lord | Palace Lord | restrained and apologetic | Apologizes for causing the disturbance after the Beast Miao King stops the fight. |
| 백상 | 부족장 | Palace Lord to subordinate tribal chieftain | you | cold, final, and detached | Baeksang refuses the chieftain's plea for mercy and tells him not to consider the exchange unjust. |
| 야수묘왕 | 적천강 | junior allied master to legendary senior martial master | Old Master Jeok | formal-deferential | The Beast Miao King respectfully addresses Jeok while asking him to sit and consulting him about the demonic stone. |
| 적천강 | 야수묘왕 | senior allied martial master to Nanman Beast Palace Lord | you | blunt, commanding, and mocking | Jeok orders the Beast Miao King to stand aside and mocks his inability to destroy the corrupted artifact. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 718
- **Aliases:** None
- **Role:** Baeksang was the Palace Lord of the Nanman Beast Palace and sole Great Chieftain of Nanman, and he died by the Beast Miao King's hand after confessing to serving Dark Heaven's plan.
- **Personality:** Cold, rigid, meticulous, and strategically resolute, yet burdened by regret, grief over Hwi's death, and a final conflicted impulse to spare others from the coming bloodshed.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of Baekhwi, whom he believed the Great Snow Fiend killed but Dark Heaven has kept alive in a deep sleep; he cultivated Yohi with gold and influence and used her support to advance Dark Heaven's preparations.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 721
- **Aliases:** Heugung
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, Great Chieftain of the Miao people who has resumed leadership of Nanman after the rift disaster, and the priest publicly chosen by the Earth Mother Goddess.
- **Personality:** The Beast Miao King is boisterous and warmhearted toward Nanman's people, but their corruption and destruction awaken fierce grief and wrath in him.
- **Voice:** Low, growling, and forceful.
- **Relationships:** Baeksang was his sworn younger brother and childhood companion, and the Beast Miao King killed him at his request; Yayul Mok is his Young Palace Lord, Jeok Cheongang is an old acquaintance, and Jin Taekyung is Jeok's Disciple and ally.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 721
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 721
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

## Korean source

```text
＃722화



대지모신(大地母神).

이름에서부터 따스한 온기가 전해지는 이 유일신은, 등장과 동시에 남만 전체를 뒤집어 놓았다.

대한민국 아이돌 시장만큼이나 치열했던 남만의 종교 판을 싸그리 밀어 버린 화려한 데뷔.

그리고 시작된 신앙심의 물결.

아니, 광신(狂信)의 파도.

“대지모신! 대지모신!”

“모신천국! 불신지옥!”

대지모신을 믿는 이는 죽어서도 구원받을 것이요, 부정하는 이는 죽어 불구덩이에 처박히리라.

반나절 만에 대지모신의 아들딸이 된 이들은 구호를 외치며 시가행진을 벌이기 시작했고, 이는 곧 포교(布敎)로 이어졌다.

“거기, 잠깐.”

“왜, 왜 그러십니까?”

“혹시 어떤 신을 믿고 있나?”

“그, 그게…… 아, 있소! 난 대지모신을 믿는 몸이오!”

“모신천국.”

“예?”

“구호를 모르다니, 이교도다! 불신지오옥!”

“히이익! 개종! 개종하겠소!”

그리고 그 광경을 바라보던 적천강은 짧은 한마디로 소감을 대신했다.

“지랄 났군.”

적천강이야 결국 외부인이니 이 정도 반응에서 끝났지만, 엉겁결에 대지모신의 제사장이 된 야수묘왕은 반쯤 혼이 빠져나갔다.

“이, 이게 아닌데. 아니, 우리의 전통이…… 우리의 토속 신앙이…….”

하지만 그도 얼마 지나지 않아 지금 이 현상이 가진 의미를 깨닫기 시작했다.

“잠깐, 이거.”

골똘히 생각에 잠겨 있던 야수묘왕이 문득 중얼거렸다.

“나쁘지 않군. 아니, 오히려 좋아.”

“이제 아셨어요? 원래 하나로 뭉치는 데는 종교만 한 게 없습니다.”

지금이야 수복 중이니 모두가 힘을 합쳐 으쌰으쌰 힘을 내고 있다 하더라도, 현재의 남만야수궁이 분열되었다는 것은 부정할 수 없는 사실이다.

“지금 뇌옥에 처박아 놓은 부족장들, 솔직히 어떻게 처리해야 할지 고민하셨잖아요?”

“……그래. 아무리 죄를 지었다 해도 결국 놈들 역시 한 부족을 이끌어 온 수장이니까.”

쓸데없는 고구마식 인정(人情)이 발동해서 살려 둔 게 아니다.

결국 남만야수궁의 본질은 서른두 개 부족의 연합체고, 이번 일에 가담한 부족장들의 숫자는 자그마치 스무 명이 넘는다.

하지만 배신자라는 명목하에 놈들의 목을 친다면, 분명 반감을 갖는 이들이 생길 수밖에 없다.

가재는 게 편이고, 팔은 안으로 굽는 법이니까.

“당장은 민심(民心)이 놈들의 처형을 원하고 있지만, 분명 시간이 지나면 문제가 생길 게다. 아직은 수면 위로 모습을 드러내지 않았을 뿐이야.”

기억이란 미화되기 마련이다.

당장 어느 정도 시간이 흐르고 어수선해졌던 분위기가 안정되고 나면, 아마 사람들은 이렇게 수군거리기 시작할 것이다.

‘그래도 우리 부족장이 사람은 괜찮았는데.’

‘맞아. 백상의 꾐에 빠져서 어쩔 수 없었던 거야.’

‘생각해 보면 좀 이상해. 그렇게 많은 부족장들이 다 같이 가담했다는 게 말이 되나?’

안 봐도 훤히 그려진다.

하나둘씩 모여 조심스럽게 나누던 대화는 남만야수궁 전체로 퍼져 나갈 테고, 결국 또 다른 분열을 불러일으킬 것이다.

“거기에 더해 이번 일에 연루된 배신자를 족장으로 둔 부족민들은 다른 이들로부터 보이지 않는 멸시를 받게 되겠지. 이는 부족 간의 반감으로 이어질 테고.”

“그렇다고 그놈들을 죄다 풀어 줄 수도 없고요.”

“부귀영화에 눈이 멀어 이미 한번 남만을 배신한 놈들이다. 두 번이 어렵겠느냐?”

그렇기에 야수묘왕은 배반자들의 처우에 관해 고심할 수밖에 없었을 것이다.

그들을 처리하면서 동시에 남만이 분열하지 않을 최적의 방법을 생각하고 또 생각해야 했다.

적어도 대지모신이라는, 전대미문의 기적을 선보인 유일신이 나타나기 전까지는 그랬다.

“지금이야말로 적기(適期)다. 법에 따라 놈들의 죄를 낱낱이 밝혀 처형하고, 이 땅의 잡초들을 모조리 뿌리 뽑을 수 있는!”

법? 처형?

주먹을 불끈 쥔 야수묘왕의 모습에, 나는 작게 혀를 찼다.

“아직 감을 못 잡으셨네.”

“뭐라?”

“법도 좋지만, 이건 심판입니다. 신의 심판.”

“신의…… 심판?”

“뇌옥에 처박혀 있는 놈들은 암천이라는 악귀와 결탁하여 이 땅을 타락시키려 한 배신자들이고, 야율 대협은 유일한 제사장으로서 대지모신의 신탁을 받은 거라고요. 저 새끼들 싸그리 죽여서 남만을 정화하라고.”

“……!”

“……!”

야수묘왕은 물론이고, 옆에서 대화를 듣고 있던 적천강까지 눈을 부릅뜬 채 나를 바라본다.

그들의 눈빛에서 생각이 고스란히 읽혔다.

‘아니, 이걸 이렇게?’

‘와. 진짜 미친놈인가?’

이런 순진한 양반들 같으니.

십왕(十王)이고 나발이고, 일평생을 무공에만 매진해 온 양반들이라 그런가 아직 세상 물정을 모른다.

남만야수궁을 오랫동안 이끌어 왔을 야수묘왕도 적천강에 비해 정치적 감각이 크게 뛰어나진 않았다.

‘그러니까 백상 일파가 기승을 부렸지.’

하지만 내가 누군가.

자랑스러운 대한민국의 국민이다.

치킨집보다 교회가 많고, 지하철역 근처에만 가도 십자가를 짊어진 21세기식 순교자들을 볼 수 있는 나라에서 평생을 살아온 사람이다.

나는 아직 제사장으로서의 자각이 부족한 야수묘왕에게, 그가 가진 힘을 일깨워 주기로 마음먹었다.

“자, 제가 하는 말 따라 하세요.”

멍하니 나를 바라보던 야수묘왕이 엉겁결에 말을 받았다.

“자, 제가 하는 말 따라 하세요.”

“아니, 그거 말고요. 지금부터 시작합니다.”

“아, 으응.”

“나는 제사장이다.”

“나는 제사장이다.”

“대지모신은 신이고.”

“대지모신은 신이고.”

“잘하셨습니다. 그럼 이어서 말씀해 보세요.”

“나는 제사장이다. 대지모신은 신이고.”

“좋습니다. 반복해 보세요.”

“나는 제사장이다. 대지모신은 신이고. 나는 제사장이다. 대지모신은 신이고. 나는…… 무적이다!”

“……?”

그, 뭔가 가르쳐 준 거랑 좀 다른 것 같긴 한데.

어쨌든 대지모신의 제사장으로 각성한 야수묘왕은 전율로 몸을 떨었고, 남만 개혁을 위한 위대한 첫걸음을 내디뎠다.

“자애로우신 대지모신의 이름으로, 대회의를 소집한다!”

“…….”

“…….”

제사장 다 됐구만.



* * *



대회의는 눈 깜빡할 사이에 시작되었다.

그만큼 대회의에 참석할 수 있는 부족장들의 숫자가 적은 이유도 있었지만, 굳이 전령을 보내지 않았더라도 상관은 없었을 것이다.

그들은 이미 급조한 회의실에서 야수묘왕을 기다리고 있었으니까.

“궁주님!”

“헛소문이지요? 헛소문이라고 하십시오!”

“갑자기 대지모신이라니, 그게 무슨 말씀이십니까!”

“아니 시팔, 부족민들이 미쳐 날뛰고 있습니다. 정마대전 때 마교도들을 보는 것 같아요!”

“어불성설입니다! 평생을 믿어 온 목신을 저버리란 말씀이십니까!”

그리고 황당과 경악이 뒤섞인 얼굴로 야수묘왕에게 득달같이 달려든 그들은, 대지모신이라는 신규 브랜드 런칭이 시장에 불러올 마케팅 효과를 듣자마자 진중한 어투로 선언했다.

“부족장인 저부터 솔선수범해야지요. 개종하겠습니다.”

“저희 대회의는 궁주님을 지지합니다.”

“와, 하나가 된 남만!”

“목신이 뭡니까? 신 하면 역시 대지모신이지.”

윗대가리들이라 그런지, 역시 눈치가 빠르다.

물론 눈치 없이 이에 반발하여 야수묘왕을 찾아온 이들도 있었다.

“궁주! 이게 말이나 되오!”

“대관절 대지모신은 무엇이며, 모신천국 불신지옥이라는 헛소리는 어디서 나온 거요?”

“독이다! 궁주가 남만에 독을 풀었다!”

“우리 제사장들이 가만히 있을 것 같소! 차라리 죽었으면 죽었지, 결코 이 사태를 묵과하지 않을 것이오!”

하나같이 늙을 대로 늙은, 수십여 명의 제사장들.

일평생 기존의 토속신을 모셔 왔던 그들은 나이가 무색할 만큼 쩌렁쩌렁한 목소리로 야수묘왕에게 들이댔다.

적천강이 입을 열기 전까지는.

“네놈들이 묵과하지 못하면, 뭐 어쩔 셈이더냐.”

“뭐라?”

“허어어. 어린 노무 새끼가 어른한테 말본새 보소.”

“궁주! 저 방자한 자를 당장 처벌하시오! 감히 듣도 보도 못한 잡놈 주제에 주둥아리를 함부로…….”

“화왕.”

“……?”

“……?”

“그게 노부의 별호다. 화왕 적천강.”

“……!”

“……!”

“백 살까진 봐주마. 그 아래로는 전부 대가리 박아.”

화왕 적천강의 명성, 아니 성질머리는 중원뿐만이 아니라 남만에도 익히 잘 알려져 있었다.

“저기, 궁주?”

“아, 비 한번 시원하게 내린다.”

“…….”

마지막 동아줄인 야수묘왕마저 먼 산을 쳐다보자, 제사장들은 망설임 없이 대가리를 박고 앞으로 대지모신에 관해서는 무조건 입 닥치고 있을 것을 맹세했다.

“사실 말이 좋아 제사장이지, 그분들을 우리가 본 적도 없는데 뭘. 다들 그렇지 않소?”

“허허허. 맞지, 맞아. 한데 대지모신께서는 이리 손수 기적도 보여 주시고 말이야. 얼마나 대단하신지.”

“저어, 그런데 궁주. 혹시 대지모신 쪽에 남는 자리 없나? 물론 제사장은 궁주가 맡고, 다른 직책이라도…….”

“크흐흠. 그 말이 나왔으니 말인데, 결국 우리가 모시는 분들도 다 이 땅과 밀접한 연관이 있지 않소? 그러니 우리가 좀 힘을 합쳐도 되지 않을까 싶은데…….”

“옳소! 대지모신은 이 땅의 어머니시니까, 사실상 모든 신을 낳으신 분 아니겠소?”

밥그릇 빼앗기기 싫은 제사장들과 완전한 남만 통합을 원하는 야수묘왕이 손잡고 벌이는 환상의 콜라보레이션.

진지한 논의 끝에 대지모신은 수십 명의 잡신을 거느린 신으로 거듭났고, 종교 전쟁을 원하지 않던 나 역시 약간의 도움을 주었다.

“복잡해지는 것 같은데, 그냥 이참에 하나 만들죠.”

“뭘 말이냐?”

“그 뭐…… 일단은 성경(聖經)이라고 해야 하나?”

“성경?”

“그게 무엇인가?”

“이 땅의 역사, 신의 말씀. 대충 그렇게 보시면 됩니다.”

“오오. 오오오!”

“실로 신이 내린 인재로다!”

그 후로는 뭐, 몇 가지 힌트만 던져 주고 방관했다.

사람들은 마감이 코앞에 닥친 웹소설 작가처럼 머리를 싸매고 설정을 쥐어짜기 시작했다.

그리고 지난 열흘 동안 뇌옥에 갇혀 있던 배반자들은 마침내 모두의 앞에 끌려 나왔다.

“사, 살려 주시오!”

“백상의 꾀임에 빠졌을 뿐이오! 난 결코 암천과 결탁하지 않았소!”

그러나 용서도, 자비도 없었다.

솨아아아아.

자애로우신 대지모신께서 이 땅을 위해 내리신 축복.

언제부턴가 성우(聖雨)라 불리게 된 빗줄기 아래에서 사람들은 심판을 부르짖었고, 망나니의 칼이 번뜩였다.

서걱!

그것으로 끝이었다. 한때 이 땅을 이끌었던 배반자들의 시신은 짐승들에게 던져졌다.

하염없이 내린 빗줄기가 그들이 흘린 핏물을 씻어 냈다.

그리고 사람들은 그제서야 불현듯 깨달았다.

비로소 자신들이 하나가 되었다는 것을.

함께 재앙을 이겨 내고, 믿을 수 없는 기적을 보고 겪었으며, 마침내 대지모신의 따뜻한 품 안에서 한 가족이 되었다는 것을.

그것이야말로 진정한 기적이었다.

서른두 갈래로 나뉘어 있던 부족민들을 마침내 합심(合心)하게 만든 기적.

그리고 숲에 존재하던 모든 병든 나무와 잡초를 베어 낸 숲지기는 모두의 앞에서 이렇게 외쳤다.

“지금 이 순간부터 우리는, 오롯이 하나가 된 남만인(南蠻人)이다!”

“와아아아아!”

한목소리로 내지르는 함성이 온 사방을 울린다.

그것은 마치, 곧 다가올 대전쟁을 예고하는 전사들의 포효와 같았다.
```

## Final English reading copy

```markdown
# Chapter 722

The Earth Mother Goddess.

Warmth seemed to radiate from the name alone, and this One God turned all of Nanman upside down the moment she appeared.

It was a spectacular debut that swept away Nanman’s religious scene—once every bit as fiercely competitive as Korea’s idol market.

And then came the wave of faith.

No, the tide of fanaticism.

“Earth Mother Goddess! Earth Mother Goddess!”

“Mother Goddess Heaven! Unbeliever Hell!”

Those who believed in the Earth Mother Goddess would be saved even after death, while those who denied her would die and be thrown into a pit of flames.

Within half a day, those who had become the Earth Mother Goddess’s sons and daughters began marching through the streets, shouting slogans. Before long, that led to proselytizing.

“Hey, you. Wait a moment.”

“Why, why do you ask?”

“Do you happen to believe in any god?”

“Well, um… Ah, yes! I believe in the Earth Mother Goddess!”

“Mother Goddess Heaven.”

“Pardon?”

“You don’t know the slogan? You’re a heretic! Unbeliever Heeell!”

“Eek! I’ll convert! I’ll convert!”

Jeok Cheongang, who had been watching the spectacle, summed up his thoughts in a single short sentence.

“What a fucking shitshow.”

Since Jeok Cheongang was ultimately an outsider, his reaction ended there. But the Beast Miao King, who had somehow become the Earth Mother Goddess’s priest, was half out of his mind.

“This, this isn’t right. No, our traditions… Our native faith…”

But it didn’t take him long to realize what this phenomenon meant.

“Wait a moment. This…”

The Beast Miao King, who had been lost in deep thought, suddenly muttered,

“Not bad. No, this is actually great.”

“You get it now? Nothing brings people together like religion.”

Nanman was in the middle of rebuilding itself, and everyone was working together and cheering each other on. Even so, there was no denying that the current Nanman Beast Palace was divided.

“You’ve been wondering how to deal with the tribal chieftains we’ve thrown into the underground prison, haven’t you?”

“…Yes. No matter how many crimes they committed, they were still the heads of their tribes.”

It wasn’t some pointless, frustrating sense of human sympathy that had made him spare them.

The Nanman Beast Palace was, at its core, an alliance of thirty-two tribes. And more than twenty of those tribes’ chieftains had taken part in this affair.

But if they cut off all their heads under the pretext that they were traitors, some people were bound to grow resentful.

People naturally took their own side.

“For now, the people want them executed, but there will definitely be problems once some time passes. They just haven’t surfaced yet.”

Memories were bound to become embellished over time.

Once things had settled down and the current chaos had faded, people would probably begin whispering things like this:

*Our chieftain was still a decent man.*

*That’s right. He couldn’t help it after falling for Baeksang’s schemes.*

*Come to think of it, something feels strange. Does it really make sense that so many chieftains all took part in it together?*

It was easy to picture.

The conversations that began in small groups, spoken cautiously among themselves, would spread throughout the Nanman Beast Palace and eventually create another division.

“On top of that, the tribes whose chieftains were traitors involved in this affair will be subjected to the other tribes’ silent contempt. That will lead to resentment between the tribes.”

“But we can’t just release all of them, either.”

“They were blinded by wealth and glory and betrayed Nanman once already. Do you think betraying us a second time would be difficult?”

That was why the Beast Miao King had been forced to agonize over how to deal with the traitors.

He had to find the best way to punish them while preventing Nanman from splitting apart.

At least, that had been the case until the One God known as the Earth Mother Goddess appeared and performed an unprecedented miracle.

“Now is the perfect time. We can expose every one of their crimes according to the law, execute them, and tear out every weed from this land!”

The law? Executions?

As the Beast Miao King clenched his fists, I clicked my tongue softly.

*He still doesn’t get it.*

“What?”

“The law is fine, but this is a judgment. God’s judgment.”

“God’s… judgment?”

“The men rotting in the underground prison are traitors who joined hands with the Fiend known as Dark Heaven to corrupt this land. And Great Hero Yayul, as the one and only priest, received a divine revelation from the Earth Mother Goddess. She told him to kill every last one of those bastards and purify Nanman.”

“……!”

“……!”

The Beast Miao King wasn’t the only one to stare at me with wide eyes. Jeok Cheongang, who had been listening to our conversation, did the same.

Their thoughts were written plainly in their eyes.

*Wait, he’s spinning it like that?*

*Wow. Is this guy seriously insane?*

What a pair of naïve old men.

Ten Kings be damned—perhaps because they had spent their entire lives focused solely on martial arts, they still knew nothing about the ways of the world.

Even the Beast Miao King, who had led the Nanman Beast Palace for so long, wasn’t much more politically savvy than Jeok Cheongang.

*No wonder Baeksang’s faction ran rampant.*

But who was I?

A proud citizen of Korea.

I had spent my entire life in a country with more churches than fried-chicken restaurants, where you could see twenty-first-century martyrs carrying crosses whenever you went near a subway station.

I decided to awaken the power within the Beast Miao King, who still lacked any awareness of himself as a priest.

“Now, repeat after me.”

The Beast Miao King, who had been staring blankly at me, reflexively echoed my words.

“Now, repeat after me.”

“No, not that. We’re starting now.”

“Ah. Uh-huh.”

“I am a priest.”

“I am a priest.”

“The Earth Mother Goddess is a god.”

“The Earth Mother Goddess is a god.”

“Good job. Now continue.”

“I am a priest. The Earth Mother Goddess is a god.”

“Excellent. Repeat it.”

“I am a priest. The Earth Mother Goddess is a god. I am a priest. The Earth Mother Goddess is a god. I am… invincible!”

“……?”

That seemed a little different from what I had taught him.

Regardless, the Beast Miao King, awakened as the Earth Mother Goddess’s priest, trembled with a shiver of excitement and took the first great step toward reforming Nanman.

“In the name of the benevolent Earth Mother Goddess, I hereby convene the Tribal Grand Council!”

“…….”

“…….”

He really had become a priest.

* * *

The Tribal Grand Council began in the blink of an eye.

Partly because so few tribal chieftains were able to attend, but even if no messengers had been sent, it probably wouldn’t have mattered.

They were already waiting for the Beast Miao King in a hastily prepared meeting room.

“Palace Lord!”

“It’s a false rumor, isn’t it? Please say it’s a false rumor!”

“What do you mean, the Earth Mother Goddess all of a sudden?”

“Fuck, the tribespeople have gone completely insane. They look just like the Demonic Cultists during the Great Faction War!”

“This is utter nonsense! Are you telling us to abandon the Wood God we have worshiped all our lives?”

But the moment they heard about the marketing effect that launching a new brand called the Earth Mother Goddess would have on the market, those who had rushed at the Beast Miao King with faces full of disbelief and shock declared in solemn tones,

“As tribal chieftain, I must set an example. I shall convert.”

“Our council supports you, Palace Lord.”

“Wow, Nanman has become one!”

“What’s the Wood God? When it comes to gods, it has to be the Earth Mother Goddess.”

They were the people at the top, after all. They knew which way the wind was blowing.

Of course, some people who lacked that sense had also come to confront the Beast Miao King.

“Palace Lord! How can this make any sense?”

“What, exactly, is the Earth Mother Goddess, and where did this nonsense about Mother Goddess Heaven and Unbeliever Hell come from?”

“It’s poison! The Palace Lord has spread poison throughout Nanman!”

“Do you think our priests will stand by and watch? We would rather die than let this situation pass!”

They were dozens of priests, all old—very old.

They had worshiped the traditional local gods all their lives, yet their voices rang out with tremendous force as they confronted the Beast Miao King.

At least, until Jeok Cheongang opened his mouth.

“If you can’t let it pass, what exactly are you going to do about it?”

“What did you say?”

“Huh. Would you look at the way this young bastard talks to his elders.”

“Palace Lord! Punish that insolent man at once! How dare some nobody we’ve never heard of open his mouth so carelessly—”

“Fire King.”

“……?”

“……?”

“That’s my sobriquet. Fire King Jeok Cheongang.”

“……!”

“……!”

“I’ll let those a hundred or older off. Everyone younger, put your heads to the floor.”

The fame of the Fire King Jeok Cheongang—or rather, his temper—was well known not only in the Central Plains but also throughout Nanman.

“Palace Lord?”

“Ah, what a lovely downpour.”

“…….”

When even the Beast Miao King, their final lifeline, looked off toward a distant mountain, the priests immediately got down with their heads to the floor and swore that from then on, they would keep their mouths shut about the Earth Mother Goddess no matter what.

“Honestly, we’re called priests, but we’ve never even seen the gods we serve. Isn’t that right?”

“Hahahaha. Yes, exactly. But the Earth Mother Goddess has personally shown us a miracle like this. How extraordinary is she?”

“Um, Palace Lord. Is there perhaps any room left on the Earth Mother Goddess’s side? Of course, you would remain the priest. But perhaps another position…”

“Ahem. Since you brought it up, the gods we serve are all closely connected to this land, aren’t they? So perhaps we could join forces a little…”

“Exactly! The Earth Mother Goddess is the mother of this land, so in a sense, she gave birth to all the gods, didn’t she?”

It was a fantastic collaboration between the priests, who didn’t want to lose their livelihoods, and the Beast Miao King, who wanted to unify Nanman completely.

After a serious discussion, the Earth Mother Goddess was reborn as a god commanding dozens of useless gods. Since I had no desire for a religious war, I offered a little assistance as well.

“This is getting complicated. Why don’t we just make one while we’re at it?”

“Make what?”

“Well… I suppose we should call it a Bible for now?”

“A Bible?”

“What is that?”

“The history of this land. The word of God. You can think of it roughly that way.”

“Oh!”

“Such a gifted man, surely sent by the gods!”

After that, I simply tossed out a few hints and watched from the sidelines.

The people began racking their brains to cobble together the lore like webnovel authors staring down an imminent deadline.

And at last, the traitors who had spent the past ten days locked in the underground prison were dragged out before everyone.

“P-please spare me!”

“I only fell for Baeksang’s schemes! I never joined hands with Dark Heaven!”

But there was no forgiveness. No mercy.

Ssshhhhhh.

The blessing the benevolent Earth Mother Goddess had bestowed upon this land.

Beneath the rain, which at some point had come to be called the Sacred Rain, the people cried out for judgment, and the executioner’s blade flashed.

Slash!

That was the end of it. The bodies of the traitors who had once led this land were thrown to the beasts.

The endless rain washed away the blood they had spilled.

And only then did the people suddenly realize.

They had finally become one.

They had overcome a catastrophe together, witnessed and experienced an unbelievable miracle, and at last become one family within the warm embrace of the Earth Mother Goddess.

That was the true miracle.

The miracle that had finally united the tribespeople who had been divided into thirty-two factions.

And the forest keeper, who had cut down every diseased tree and weed in the forest, shouted before them all:

“From this moment on, we are the people of Nanman—wholly united as one!”

“Waaaaaah!”

The roar they raised with one voice echoed in every direction.

It sounded like the war cry of warriors heralding the Great War that was soon to come.
```
