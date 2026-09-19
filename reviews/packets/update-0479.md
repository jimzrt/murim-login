<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0479.txt",
      "sha256": "cf2e30502e57ae8be30095f66499f1fc0494e6b267d5eb2f5ba8f244b1a10a22",
      "bytes": 14093
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "4c6ee77797841dce203124a7386a5fec3809b14e47453da861a2831341541a68",
      "bytes": 2689
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "834c94431f8255d969947faa6a53e2198fe6725fbec90a6ae680418f289aee3a",
      "bytes": 153332
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "7808369c870cbe1cf77df0a5846eec98e3803869a1d26e94fd7a28dfee685f59",
      "bytes": 1006
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "57deca798f844ad56f4a7ee62709e39f4ac3c4e1e3807230669dc111375b5718",
      "bytes": 553
    },
    {
      "path": "characters/Honglan.md",
      "sha256": "7bacf71452b45c4ababae95a0f08fced1affe03a41c12962b078a6a09195000e",
      "bytes": 918
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "3e42cfdd50f88c326563e186aaadd95d5214af901ef83425715c4d0efe79ff7f",
      "bytes": 1542
    },
    {
      "path": "characters/Ju Wongong.md",
      "sha256": "c278c27ec3e69f2e0160de61bd74ae8239a212c1a123c566cd2ee982efb98349",
      "bytes": 681
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "d40025a4401ff767169989d4cbf12907a5d45bbc860b482d2b01374f2558628c",
      "bytes": 771
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "bb882cf37f97b20509363dde65c544ab530ac7be2754709b99da838a8410a1ae",
      "bytes": 147867
    }
  ],
  "estimated_tokens": 11126
}
-->

# Durable State Update — Chapter 479

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 479. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 479. Profile updates may replace only one
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
  "chapter": 479,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 479,
    "continuity_sources": [479],
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
    "Taekyung has mortally wounded the Mutated Water God Dragon with a spear through a one-scale gap at the back of its neck; the dragon's immediate fate remains unresolved.",
    "The dragon's mind cleared after its defeat and it communicated through mental intent, distinguishing that ability from ordinary Sound Transmission.",
    "The dragon transferred a Memory Fragment to Taekyung through its tears, placing him inside a fragmented record of its five hundred years.",
    "The Water God Dragon began as Dongting Lake's benevolent Two-Horned Beast, protected its subjects, ruled Dongting Lake and the Yangtze, and sought ascension without achieving it.",
    "A secluded region of Dongting Lake contained a Gate or rift emitting mana and ominous energy; exposed fish mutated under demonic qi.",
    "The dragon fought the mutated fish, then blocked the rift for seven days and nights and absorbed most of the demonic qi to protect its domain and subjects, losing its intelligence and becoming an evil beast.",
    "The dragon retained enough reason to emerge from the water and seek the culprit behind the corruption.",
    "At the end of the recovered memory, Taekyung recognizes Honglan at the corruption site; her purpose and involvement remain unresolved."
  ],
  "continuity_sources": [
    478,
    477
  ],
  "open_questions": [
    "What is the Dongting Fisherman's exact role within Dark Heaven, and how was he connected to the earlier destruction inside the secret refuge?",
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Did the Mutated Water Dragon destroy Donghu Stronghold and the related Yangtze River Channel League strongholds, and why was no Moving Formation trace left?",
    "Who created or controlled the Gate or rift that corrupted the Water God Dragon, and how is that power related to Dark Heaven?",
    "Why was Honglan present at the corruption site, and what role did she play in the Water God Dragon's mutation?"
  ],
  "safe_through": 478,
  "temporary_decisions": [
    "Render 광폭화 as Berserk and preserve the System Status distinction.",
    "Render 장수 돌침대 as Jangsu stone bed and 효자손 as hyojason, each with an explanatory footnote when used.",
    "Retain established jang and geun measurements, along with established renderings of live-fish sashimi and bone-in sashimi.",
    "Continue rendering 수염 as whiskers; distinguish Force, Sword Energy, Hellfire, and Water Breath.",
    "Render 의념 as mental intent when the dragon distinguishes it from 전음, which remains Sound Transmission."
  ],
  "version": 1
}
```

## Exact glossary matches

| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 하오문    | **Lower District Sect**          |
| 암천     | **Dark Heaven**                  |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 게이트     | **Gate**              |
| 소저      | **Young Lady**                                                  |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 홍란 | **Honglan** | Stage name of Ju Wongong's Lower District Sect singing courtesan; her real name is concealed. |
| 주원공 | **Ju Wongong** | Qingxia Hall leader who claims distant kinship with the Emperor. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 천기 | **heavenly patterns** | Celestial patterns Hong Dao studies to perceive major changes and omens. |
| 염라 | **Yama** | Buddhist lord of the underworld invoked as the one awaiting the dead. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 하오문도 | **Lower District Sect member** | Member of the Lower District Sect. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 권강 | **Fist Force** | Qi force projected through the Western Heaven Demon Lord's fist. |
| 염라대왕 | **Yama** | Expanded source form of the established underworld ruler term 염라. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 호북성 | **Hubei Province** | Province where the chapter’s Dark Heaven incidents occurred. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 청풍 | 미미 | handler_to_companion_snake | Mimi | cheerful-commanding | Cheongpung repeatedly calls and commands the Thousand-Year Poison Horned Snake. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 주원공 | 청풍 | Qingxia Hall young master to Huashan Divine Dragon | you | formal and guarded | Uses 그대 while tentatively offering Cheongpung an invitation to Dongting Lake. |
| 주원공 | 홍란 | employer to kept singing courtesan | Honglan | commanding | Orders Honglan to greet Taekyung and presents her as the singing courtesan he keeps at his side. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 477
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 478
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Honglan.md

# Honglan (홍란)

- **Safe through:** Chapter 478
- **Aliases:** None
- **Role:** Honglan is a Lower District Sect courtesan who uses a stage name while serving as Ju Wongong's singing courtesan.
- **Personality:** Discreet about her real identity and professionally alluring.
- **Voice:** Clear, pure, and alluring, with humble formal speech toward honored guests.
- **Relationships:** Honglan is kept at Ju Wongong's side as a singing courtesan, belongs to the Lower District Sect, lost her clan and parents overnight as a child, can respond to Taekyung through Sound Transmission, is the sole surviving eyewitness to the Dongting Lake attack who knows several possible locations of the Dongting Fisherman's hidden refuges, and appears in the Water God Dragon's memory at the Gate or rift that caused its corruption; her role there is unresolved.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 477
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin and Furnace Fire Pure Blue, and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, and pathologically afraid of water. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Ju Wongong.md

# Ju Wongong (주원공)

- **Safe through:** Chapter 459
- **Aliases:** Qingxia Hall young master
- **Role:** Ju Wongong is an exiled Qingxia Hall young master and a distant imperial relative of the Zhu ruling house who was punished for embezzling wealth while abusing his imperial authority.
- **Personality:** Entitled, status-conscious, theatrical, and amused by violence until his own protection is overcome.
- **Voice:** Pompous and imperious, with formal declarations of rank and authority.
- **Relationships:** His Qingxia Hall entourage and four Peak guards obey him; he asserts kinship with the Emperor.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 477
- **Aliases:** None
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, having passed the Divine Physician title to his Disciple, and he has reached the Returned to Youth realm.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple; Jeok Cheongang is an old acquaintance, and Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

## Korean source

```text
＃479화



세상이 무너지고, 이내 다시금 세워진다.

흉포함이 깃든 붉은 동공과 출렁이는 강물도, 아름답게 세공된 은빛 비녀도 사라졌다. 빈자리를 메운 것은 기억 밖의 현실이었다.

솨아아악.

나는 천천히 눈을 깜빡였다. 전신을 감쌌던 물의 장막이 흩어지고 뒤바뀐 주위의 광경이 또렷해졌다.

동시에 누군가 일시 정지 버튼을 누른 것처럼 정지되어 있던 시간이 흐르기 시작했다.

그리고 다음 순간. 쌓여 있던 둑이 한 번에 터진 듯, 주변의 서늘한 공기와 시스템 알림이 나를 덮쳤다.

띠링. 띠링. 띠링.



- [기억의 파편]이 해제되었습니다!

- [변이된 수신룡]이 이성을 되찾음에 따라, 퀘스트 정보가 갱신되었습니다!

- 갱신된 퀘스트 정보에 따라, 임무 성공을 인정합니다!

- 돌발 퀘스트, [타락한 영물]을 성공적으로 완료했습니다!

- 막대한 양의 경험치와 명성을 얻었습니다!

- 레벨 업!

- 레벨 업!



레벨 업 알림과 함께 신비로운 힘이 지쳐 있던 몸에 새로운 활력을 불어넣고 소모된 공력을 채워 넣었다

 하지만 어째서일까, 나는 숨조차 제대로 쉴 수 없었다.

‘홍란. 홍란이었어.’

그래, 그녀였다.

동정호의 참극으로부터 주원공과 함께 살아남은 하오문도. 한 나라를 좌지우지할 경국지색의 미녀.

내 머리카락에 꽂힌 이 비녀의 주인이, 선한 이무기를 타락시켜 동정호와 장강을 피로 물들게 한 장본인이자 호북성에서 벌어진 모든 사건의 원흉이었다.

왜 몰랐을까. 어디서부터 어디까지가 거짓이고 진실이었을까.

‘게이트, 마력, 홍란. 암천.’

찰나의 순간 머릿속을 스치는 수많은 의문과 생각들. 과부하가 걸린 두뇌가 터질 것만 같았다.

믿기지 않는 현실에 파르르 몸을 떨고 있던 나는, 이쪽을 향해 쏘아지는 세 사람의 신형을 발견할 수 있었다.

가장 선두에서 들이닥치고 있는 적천강의 일그러진 얼굴도.

“놈, 감히-!”

생각해 보면 누가 봐도 오해할 만한 그림이다.

나와 수신룡이 나눈 대화와 [기억의 파편]에 들어갔다 나온 시간은 아주 짧은 순간 동안 이루어졌고, 멀쩡하게 서 있던 내가 이상 행동을 보이기까지 했으니.

분노에 찬 적천강의 대갈일성에 정신이 번쩍 든 내가 벼락처럼 외쳤다.

“노야!”

“……!”

눈빛만으로도 서로의 의중을 알아차릴 수 있는 우리였다.

내 외침에 담긴 감정을 알아차린 적천강의 눈동자에 느낌표가 떠올랐다. 동시에 힘차게 나아가던 주먹의 끝이 방향을 틀었다.

후웅, 콰아아!

그야말로 털끝 하나 차이였다.

아슬아슬하게 수신룡을 비껴간 권강(拳罡)이 어느새 잔잔해진 수면을 강타한다.

열양지기에 실린 열기가 얼마나 강했는지, 단번에 반경 수 장의 공간에 존재하던 수분이 모조리 증발했다.

수신룡은 현재 죽음을 코앞에 둔 상태.

저런 일격을 맞았다면 마지막 대화를 나눌 시간조차 없었을 것이다.

“네 녀석, 어째서……!”

- 제자가 걱정되었나? 좋은 스승이로군.

“흡!”

수신룡이 흘려보낸 의념(疑念)은 내게만 전해진 것이 아닌 게 분명했다.

적천강은 짧게 헛숨을 들이키며 뒷걸음질 쳤고, 뒤이어 도착한 문경과 청풍도 귀신을 본 것 같은 표정으로 변했다.

“지금, 도대체 뭐였지?”

“어어, 미미도 이런 건 못 하는데.”

……취리릭.

수신룡의 깊고 맑은 눈동자에 우리의 모습이 비친다. 적천강이 떨리는 목소리로 물었다.

“네놈은, 네놈은 대관절 무엇이냐.”

- 누군가는 나를 신령이라 부르고, 누군가는 괴물이라 하더군. 그 질문에 대한 대답은 스스로 찾아보게.

그르릉.

힘겹게 숨을 내쉰 수신룡이 의념을 이어 갔다.

- 마지막으로 고맙다는 인사를 해야겠군. 그대들이 나서지 않았다면, 나는 마지막까지 추악한 악물로 남았을 터…….

또렷하게 뇌리에 울려 퍼지던 의념이 서서히 흐려진다.

어느덧 수신룡의 맑은 눈동자에서 빛이 빠져나가고 있었다.

‘죽는다고? 이렇게?’

나는 마지막 희망을 담아 문경을 바라봤지만, 신의(神醫)라는 또 다른 별호를 지닌 그는 굳은 얼굴로 고개를 가로저을 뿐이었다.

“이미 늦었다. 내가 아니라 대라신선(大羅神仙)이 온다 해도 멈출 수 없어.”

- 그대의 말이 옳네. 생과 사를 오가는 자여.

생과 사를 오가는 자.

한 사람의 정체를 정확히 꿰뚫는 한마디에, 문경의 가지런한 눈썹이 꿈틀거렸다.

“나를…… 알고 있나?”

- 비록 하늘에 오르지는 못했으나 오랜 세월 동안 수행을 쌓은 몸. 이 자리에 있는 그대들 모두를 몽중(夢中)에서 보았지.

도대체 수신룡이 꾸었다는 꿈에서는 무슨 일이 벌어지고 있었을까.

수신룡은 장장 오백 년을 살아온 이무기다. 힘을 다하여 죽음을 앞둔 상태라 해도, 짐작할 수 없는 깊이와 신비로움이 그에게는 있었다.

인간이 알 수 없는 그 무언가를 응시하듯, 우리의 어깨너머 허공을 바라보던 수신룡이 의념을 흘려보냈다.

- 아쉽게도 내게 허락된 것은 여기까지일세. 비록 천기를 누설할 수는 없지만…… 그래, 마지막 가는 길에 한 가지 선물을 남기는 것 정도는 괜찮겠지.

선물?

우리 중 누군가 의문을 표할 틈조차 주어지지 않았다.

다음 순간, 피로 흠뻑 젖은 수신룡의 입가에서 흘러나온 희미한 빛무리에 나는 눈을 크게 떴다.

스으으윽.

그건 은은한 빛을 뿌리는 진주였다.

마치 보이지 않는 손이 들어 올린 것처럼 수신룡의 입가를 빠져나와 허공으로 두둥실 떠오른 그것은 스스로 몸을 떨었다.

후우웅.

공기를 타고 전해지는 진동.

동시에 진주의 상당 부분을 차지하고 있던 검은 얼룩이 녹아내리듯 사라진다. 그럴 때마다 진주의 크기가 눈에 띌 만큼 작아지기 시작했다.

‘이건…….’

단지 눈으로 보이는 것만이 전부가 아니다.

나는 진주가 품고 있는 기운의 크기와 깊이를 느낄 수 있었고, 눈 앞에 펼쳐진 광경에서 정화(淨化)라는 단어를 떠올릴 수 있었다.

그리고 마침내 일련의 변화가 모두 끝났을 때. 누군가의 입술 사이로 숨길 수 없는 탄성이 흘러나왔다.

“아아.”

스아아아.

어느덧 진주는 처음과는 비교도 되지 않을 만큼 환한 빛을 뿌리고 있었다.

비록 크기는 일반적인 단환과 비슷할 만큼 확연히 줄어들었지만, 불순물을 모두 정화한 기운의 결정체는 한없이 맑고 깊은 기운을 품고 있었다.

‘정순하다.’

실로 강력한 기운의 결정체.

나를 포함한 모두가 경이로운 눈빛으로 그것을 바라보던 그때.

스르륵.

천천히 허공을 유영한 기운의 결정체가 내 앞에서 멈추었다. 동시에 수신룡의 의념이 울려 퍼졌다.

- 내 원정(元淨)일세. 인세에서는 내단이라고도 부르더군.

“……!”

- 비록 과거에 비하면 보잘것없으나 반드시 큰 힘이 될 터. 부디 필요한 곳에 써 주게.

거절할 이유가 없는 제안.

떨리는 눈빛으로 기운의 결정체를 바라보던 나는 손을 뻗어 그것을 붙잡았다.

띠링.



- [수신룡의 원정]을 획득하셨습니다!



귓가에 울려 퍼지는 시스템 알림.

자신의 모든 것을 넘겨준 수신룡은 천천히 눈을 깜빡였다.

어느새 맑게 갠 하늘을 바라보는 눈동자에는 희미한 웃음이 깃들어 있었다.

- 그래, 여기까지로군…….

그르릉.

흐릿해지는 의념과 함께, 용이 되지 못한 이무기의 마지막 숨결이 피에 젖은 입가에서 흘러나왔다. 그리고 이내 모든 것이 멈추고 고요해진다.

나는 손을 뻗어 차갑게 굳어 버린 수신룡의 눈을 감겨 주었다.

‘고생했습니다.’

[기억의 파편]을 통해 수신룡의 삶을 지켜본 나다.

그는 일반적인 영물이라 부를 수 없는 신비로운 존재였고, 자신을 희생하여 더욱 큰 재앙을 막은 선한 존재였다.

그러니 적어도 마지막 순간만큼은 스스로 죽음을 맞이할 권리가 있다.

레벨업을 위한 희생양이 아닌, 자연스러운 죽음을.

하지만 한 사람. 아니 한 년만큼은 무슨 일이 벌어져도 예외다.

‘……홍란.’

나는 머리카락을 고정하고 있던 은비녀를 뽑았다.

예민한 후각으로도 간신히 알아차릴 만큼 은은한 향을 내뿜는 그것을 말없이 응시하다가, 아직도 혼란스러워하는 적천강을 향해 입을 열었다.

“뱀 잡으러 가실래요?”

“이게 도대체 무슨 일인지 말을…… 뭐라? 뱀?”

“예. 꽃뱀이요.”



* * *



군선(軍船)의 갑판 위에서 울려 퍼진 맑은 웃음소리에 모두의 시선이 집중되었다.

아니, 사람들의 시선이 모인 이유는 비단 웃음소리 때문만은 아니었다.

이미 눈이 달린 사내라면 배에 오르기 전부터 힐끔힐끔 쳐다보던 중이었으니까. 그만큼 대단한 미모를 지닌 여인이었다.

“허어, 웃음소리조차 아름답군.”

관군 복장을 한 중년인이 한탄하듯 중얼거리자, 옆에 있던 동료가 핀잔을 주었다.

“이 모습을 자네 마누라가 봤어야 했는데.”

“재수 없는 소리 집어치우게. 차라리 염라대왕이랑 눈을 마주치고 말지.”

“나이도 먹을 만큼 먹었고, 토끼 같은 자식 놈이 다섯이나 있으면서 이러긴가?”

“그러는 자네는?”

“난 아직 자식이 없어.”

“마누라는 있잖나.”

동료 관군이 엄숙하게 선언했다.

“곧 없어질 거야.”

“……단단히 미쳤군. 제정신인가?”

“내가 뭐 어때서? 사내라면 한 번쯤은 노려 볼 만하지.”

“내 장담하건대, 그럴 일은 없을 걸세.”

“벌써부터 초치는 건가?”

“아니. 자네보다 훨씬 더 젊고, 잘생기고 능력도 좋은 인간이 지금 선수를 쳤거든.”

그의 말은 사실이었다. 이미 시원시원한 이목구비를 지닌 군관이 거침없는 발걸음으로 여인을 향해 다가가고 있었다.

“소저. 즐거운 일이라도 있으신가 봅니다.”

군선의 책임자인 송 군관은 새하얀 이빨을 드러내며 씩 웃었다.

부유한 집안에 인물도 훤칠한 그다. 눈앞의 여인이 살면서 한두 번 볼까 말까 한 경국지색의 미녀라고는 하지만 나름대로 자신은 있었다.

‘대갓집 규수도 아니고, 기껏해야 일개 가기(歌妓)인데 뭘.’

그리고 그런 송 군관의 생각은, 다음 순간 속절없이 허물어져 내렸다.

“네, 있네요. 아주 즐거운 일이.”

영혼이 정화되는 것처럼 깨끗한 목소리. 수국(水菊)이 만개한 듯한 웃음.

그녀에게선 요염하면서도 청초하고, 청초하면서도 범접할 수 없는 아름다움이 흘러나온다.

송 군관은 자신도 모르게 말을 더듬었다.

“그, 그, 그렇습니까.”

그런 송 군관의 모습에 여인, 홍란은 입을 가리며 웃었다.

반달처럼 휘어지는 눈매에 쉴 틈 없이 곁눈질하던 주위의 관군들이 애끓는 신음을 흘렸다.

‘저놈들이 감히.’

수하들을 향해 눈을 부라린 송 군관은 쿵쿵 뛰는 가슴을 안고 입을 열었다.

“아쉽군요. 소저와 함께 즐거움을 나눌 수 있다면 좋을 터인데…….”

의도적으로 흐리는 말꼬리에 홍란이 싱긋 웃었다.

“글쎄요. 소녀가 괜한 말로 우리 송 군관님의 마음을 어지럽힐 것 같아 조심스럽네요.”

우리? 송 군관님?

틀림없다. 이건 호감이 있는 남녀 관계에서나 보인다는 녹광(綠光)이다.

용기백배한 송 군관이 우렁차게 외쳤다.

“선조의 명예를 걸고 절대! 그럴 일은 없을 겁니다!”

“어머, 용맹하기도 하셔라. 그럼 특별히 송 군관님께만 알려 드릴게요. 잠시 귀 좀…….”

“네, 넵!”

송 군관이 두근거리는 심장 박동을 느끼며 홍란을 향해 귀를 내민 다음 순간, 달콤하면서도 따뜻한 숨결이 그의 귓가를 간지럽혔다.

“실은, 소녀가 동정호에 사는 이무기를 이용해서 수많은 사람을 죽였거든요.”

“예?”

“그런데 그 이무기가 방금 죽어 버렸지 뭐예요. 그 사실이 아쉽기도 하지만 한편으로는 즐겁네요.”

천천히 고개를 든 송 군관이 멍한 표정으로 홍란을 바라보았다.

눈앞의 이 여인이 도대체 무슨 말을 하는지, 자신이 무슨 말을 들었는지 감도 잡히지 않았다.

“소저, 그게 무슨…….”

“들으신 그대로예요. 송 군관님은 절 이해하실 거라 믿어요.”

어째서일까. 나른하게 들리는 홍란의 목소리에 송 군관의 표정이 몽롱해졌다.

그건 단순히 여인의 향한 사내의 연심이 아니었다. 거부할 수도 없는 이끌림이었고, 한 사람의 감정과 영혼을 사로잡는 쇠사슬이나 다름없었다.

“그렇죠, 송 군관님?”

“……물론입니다. 그렇고 말고요.”

“잘됐네요.”

홀린 듯이 고개를 끄덕이는 송 군관을 만족스럽게 바라본 홍란은 넓게 펼쳐진 강물을 바라보았다.

그리고 자신의 포로가 된 사내에게 부탁을, 아니 첫 명령을 내렸다.

“우리, 목적지를 바꿀까요?”
```

## Final English reading copy

```markdown
# Chapter 479

The world collapsed, then was rebuilt once more.

The red pupils filled with ferocity, the surging river water, and the beautifully carved silver hairpin all vanished. What filled their absence was reality outside the memory.

*Whoooooosh.*

I slowly blinked. The curtain of water that had wrapped around my entire body scattered, and the changed surroundings came into clear view.

At the same time, time—which had been frozen as though someone had pressed a pause button—began to move again.

And then, in the next moment, the cold air around me and the System notifications came crashing down like a dam that had burst all at once.

*Ding. Ding. Ding.*

> **System**
>
> **Memory Fragment** has ended!
>
> The Quest information has been updated because the **Mutated Water God Dragon** has regained its reason!
>
> In accordance with the updated Quest information, the mission is recognized as successful!
>
> Surprise Quest, **Corrupted Spirit Beast**, has been successfully completed!
>
> You have gained a tremendous amount of EXP and Fame!
>
> **Level Up!**
>
> **Level Up!**

Along with the Level Up notifications, a mysterious power breathed new vitality into my exhausted body and replenished my depleted internal energy.

But why was it that I could barely breathe?

*Honglan. It was Honglan.*

Yes. It had been her.

The Lower District Sect member who had survived the Dongting Lake tragedy alongside Ju Wongong. A breathtaking beauty capable of swaying an entire nation.

The owner of the hairpin stuck in my hair was the one who had corrupted the benevolent imugi and stained Dongting Lake and the Yangtze with blood—the mastermind behind every incident that had taken place in Hubei Province.

*Why hadn’t I realized it? Where had the lies begun, and where had the truth ended?*

*Gate. Mana. Honglan. Dark Heaven.*

Countless questions and thoughts flashed through my mind in an instant. My overloaded brain felt as though it might burst.

As I trembled at the unbelievable reality, I spotted three figures shooting toward me.

I also saw Jeok Cheongang’s distorted face at the very front.

“You bastard, how dare you—!”

Come to think of it, the scene looked like something anyone would misunderstand.

The conversation I had shared with the Water God Dragon and the time I had spent inside the Memory Fragment had both taken place in an incredibly brief instant. And then, after standing there perfectly fine, I had suddenly begun acting strangely.

Jeok Cheongang’s furious bellow snapped me back to reality, and I shouted like a bolt of lightning.

“Old Master!”

“……!”

We were the kind of people who could understand each other’s intentions with nothing more than a glance.

The moment Jeok Cheongang recognized the emotion in my shout, an exclamation mark appeared in his eyes. At the same time, the fist he had been driving forward forcefully changed direction.

*Whoom, kwaaaaaang!*

It had been a difference of no more than a hair’s breadth.

The Fist Force that had narrowly missed the Water God Dragon slammed into the surface of the lake, which had already grown calm.

The heat carried by the Scorching Yang Qi was so intense that every drop of moisture within a radius of several jang evaporated in an instant.

The Water God Dragon was currently at death’s door.

If it had taken an attack like that, there would not even have been time for one final conversation.

“You bastard, why—!”

—Were you worried about your Disciple? What a good Master.

“Gasp!”

It was obvious that the mental intent the Water God Dragon had sent out had not reached me alone.

Jeok Cheongang sucked in a short breath and took a step backward. Mungyeong and Cheongpung arrived immediately afterward, their expressions changing as though they had seen a ghost.

“What in the world was that just now?”

“Uh, even Mimi can’t do something like that.”

……*Shlick.*

Our reflections appeared in the Water God Dragon’s deep, clear eyes. Jeok Cheongang asked in a trembling voice.

“What in the world are you?”

—Some call me a divine spirit. Others call me a monster. You will have to find the answer to that question yourself.

*Grrr.*

The Water God Dragon exhaled with difficulty and continued sending its mental intent.

—As my final act, I should thank you. If you had not stepped forward, I would have remained an ugly evil beast until the very end…

The mental intent that had rung clearly inside our minds gradually faded.

By then, the light was draining from the Water God Dragon’s clear eyes.

*Is it dying? Just like this?*

I looked at Mungyeong with the last of my hope, but the man who also bore the sobriquet Divine Physician merely shook his head with a grim expression.

“It’s already too late. Even if a Great Firmament Immortal came in my place, it couldn’t stop this.”

—You speak the truth, one who walks between life and death.

At those words, which had precisely seen through one man’s identity, Mungyeong’s neatly arranged brows twitched.

“You… know me?”

—Although I failed to ascend to the heavens, I am a being that cultivated for a long time. I saw all of you here in my dreams.

What exactly had been happening in the dreams the Water God Dragon claimed to have?

The Water God Dragon was an imugi that had lived for five hundred years. Even though it now stood on the verge of death with all its strength exhausted, there remained within it a depth and mystery beyond my imagination.

As though gazing at something beyond human understanding, the Water God Dragon stared into the empty air over our shoulders and sent out its mental intent.

—Unfortunately, this is as far as I am permitted to go. Although I cannot reveal the heavenly patterns… yes, I suppose it would be all right to leave behind one gift on my final journey.

A gift?

None of us were given time to express our questions.

In the next moment, my eyes widened at the faint cloud of light spilling from the blood-soaked corner of the Water God Dragon’s mouth.

*Shhhhhhh.*

It was a pearl that cast off a gentle glow.

As though lifted by an invisible hand, it slipped out from the corner of the Water God Dragon’s mouth and floated into the air. Then it trembled on its own.

*Whoom.*

A vibration traveled through the air.

At the same time, the black stain that had occupied a considerable portion of the pearl melted away and vanished. Whenever it did, the pearl began to shrink noticeably.

*This is…*

What I could see with my eyes was not all there was to it.

I could feel the size and depth of the energy contained within the pearl, and the sight unfolding before me brought one word to mind.

*Purification.*

And finally, when all the changes had come to an end, an irrepressible exclamation escaped someone’s lips.

“Ah.”

*Shhhhhhh.*

By then, the pearl was radiating a light far brighter than before.

Although its size had clearly diminished until it was about the same as an ordinary pill, the crystal of energy, now purified of every impurity, contained an infinitely clear and profound power.

*So pure.*

A truly powerful crystal of energy.

Just as all of us were gazing at it with awe—

*Slither.*

The crystal of energy slowly drifted through the air and stopped in front of me. At the same time, the Water God Dragon’s mental intent rang out.

—This is my Origin Essence. Humans call it an inner core.

“……!”

—Although it is insignificant compared to what it once was, it will surely become a great source of power. Please use it where it is needed.

There was no reason to refuse such an offer.

I stared at the crystal of energy with trembling eyes, then reached out and caught it.

*Ding.*

> **System**
>
> **Water God Dragon’s Origin Essence** acquired!

The System notification rang in my ears.

After giving me everything it possessed, the Water God Dragon slowly blinked.

Its eyes, gazing at the sky that had cleared without a trace, held a faint smile.

—Yes. This is where it ends…

*Grrr.*

Along with the fading mental intent, the final breath of the imugi that had failed to become a dragon escaped from its blood-soaked mouth.

Then, everything came to a stop, and silence descended.

I reached out and closed the Water God Dragon’s eyes, which had grown cold and stiff.

*You’ve been through a lot.*

I was the one who had watched the Water God Dragon’s life through the Memory Fragment.

It was a mysterious being that could not be called an ordinary divine spirit beast, and a benevolent existence that had sacrificed itself to prevent an even greater disaster.

So at least in its final moment, it had the right to meet its own death.

Not die as a sacrifice for someone else’s Level Up, but experience a natural death.

But there was one person—no, one bitch—for whom none of that mattered.

*…Honglan.*

I pulled the silver hairpin from my hair.

I silently stared at the object, which gave off a faint scent that even my sensitive sense of smell could barely detect, then spoke to the still-confused Jeok Cheongang.

“Want to go catch a snake?”

“Tell me what the hell is going on… What? A snake?”

“Yes. A flower snake.”[^1]

[^1]: In Korean slang, a “flower snake” is a woman who seduces men and exploits them.

* * *

A clear peal of laughter rang out across the deck of the military ship, drawing everyone’s attention.

Actually, the laughter was not the only reason people were looking.

Any man with eyes had already been sneaking glances at her before even boarding the ship. She was that beautiful.

“Good heavens. Even her laughter is beautiful.”

When a middle-aged man in a military uniform muttered wistfully, the colleague beside him scolded him.

“Your wife should have seen you just now.”

“Stop saying such unlucky things. I’d rather lock eyes with Yama.”

“You’re old enough to know better, and you have five children as cute as rabbits. Are you seriously acting like this?”

“What about you?”

“I don’t have children yet.”

“You have a wife.”

His fellow officer solemnly declared,

“I won’t have one soon.”

“……You’re completely insane. Have you lost your mind?”

“What’s wrong with me? A man ought to take a shot at it at least once.”

“I guarantee you that will never happen.”

“Are you trying to ruin my mood before I’ve even started?”

“No. Someone much younger, better-looking, and more capable than you has already made the first move.”

His words were true. A military officer with broad, handsome features was already walking boldly toward the woman.

“Young Lady. I assume something pleasant has happened?”

Officer Song, the commander of the military ship, flashed his bright white teeth and grinned.

He came from a wealthy family and was handsome himself. Although the woman before him was the kind of breathtaking beauty he might see once or twice in his entire life, he still had a fair amount of confidence.

*She isn’t the daughter of some great household. She’s just a mere singing courtesan.*

And the moment after he thought that, Officer Song’s confidence crumbled without a trace.

“Yes, something pleasant happened. Something very pleasant.”

Her voice was so pure it seemed to cleanse the soul. Her smile was like a hydrangea in full bloom.

A seductive yet pristine beauty flowed from her—pristine, yet too lofty for anyone to approach.

Officer Song began stammering without realizing it.

“D-do you, do you mean it?”

At his flustered appearance, the woman—Honglan—covered her mouth and laughed.

Her eyes curved like half-moons, and the officers who had been sneaking glances at her without pause let out anguished groans.

*How dare those bastards.*

Officer Song glared at his subordinates, then opened his mouth with his heart pounding.

“It’s a shame. It would be wonderful if I could share that pleasure with you, Young Lady…”

Honglan smiled faintly at his deliberately trailing words.

“I’m not sure. I’m afraid I might trouble our Officer Song’s heart with careless words, so I’m hesitant.”

*Our? Officer Song?*

There was no doubt. This was the green light that supposedly appeared only between a man and a woman who had feelings for each other.

Filled with courage, Officer Song shouted loudly.

“On the honor of my ancestors, that will absolutely never happen!”

“Oh my, how brave you are. Then I’ll tell you specially, Officer Song. Could you bring your ear a little closer…?”

“Yes, yes!”

Officer Song felt his heart pounding as he leaned his ear toward Honglan.

Then her sweet, warm breath tickled his ear.

“The truth is, I used the imugi living in Dongting Lake to kill a great many people.”

“What?”

“But that imugi just died. It’s a shame, in a way, but at the same time, I’m glad.”

Officer Song slowly raised his head and stared blankly at Honglan.

He had no idea what this woman before him was talking about, or what he had just heard.

“Young Lady, what does that—”

“It’s exactly what you heard. I believe you’ll understand me, Officer Song.”

Why was it? Honglan’s languid voice caused Officer Song’s expression to grow hazy.

This was not merely a man’s romantic feelings toward a woman. It was an irresistible attraction, nothing less than a chain that seized a person’s emotions and soul.

“Isn’t that right, Officer Song?”

“……Of course. Naturally.”

“That’s wonderful.”

Honglan looked with satisfaction at Officer Song as he nodded as though under a spell, then gazed out over the wide river.

And she gave the man who had become her captive a request—or rather, her first command.

“Shall we change our destination?”
```
