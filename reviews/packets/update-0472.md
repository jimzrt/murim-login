<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0472.txt",
      "sha256": "c102c23a70d4b7ab816d708fd997eae2dcec25011283da852a679010e189e5d2",
      "bytes": 12943
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "8f13b74ba57c17ff4e5739f0665d1666eb46eadfbf4e649670b6f4cf01ebabf0",
      "bytes": 3235
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "30e6ba49128079e0c23bac2c431896b8d8e15f9d946e31a02c7616bbd3f432ea",
      "bytes": 152895
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "8377b5e8bec5f674783770c26e624c099d8f955d968499df486920d6ea0fe3e9",
      "bytes": 1006
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "bb7f0ed5fd026f28bd0321771848c2eadc9f415d3ed940542f5321408b8a60e8",
      "bytes": 553
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "d2eec0f479055c86b03c718cb1f67cfecc7d0009454beff1e6e0f2901df49639",
      "bytes": 1542
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "1cf12a3023851ac823bab82b9a39a5463617efbc2d3fca2331faaeb82620db3f",
      "bytes": 734
    },
    {
      "path": "characters/Zhuge Feng.md",
      "sha256": "f4b4d7742478744dddaaf733a65086a7645bb358574807280b25dd276a9f66b7",
      "bytes": 626
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "02c75e82577b427aa72f777610f13623d2bfa8352fe24570f94fb4b00282bace",
      "bytes": 147215
    }
  ],
  "estimated_tokens": 10794
}
-->

# Durable State Update — Chapter 472

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 472. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 472. Profile updates may replace only one
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
  "chapter": 472,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 472,
    "continuity_sources": [472],
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
    "A forced System Quest, Corrupted Spirit Beast, remains active for Taekyung; Logout is disabled until it ends.",
    "The Quest requires Taekyung to defeat the Mutated Water God Dragon; its Grade is Supreme Peak and failure means death or an equivalent penalty.",
    "The Mutated Water God Dragon was once a noble spirit beast that waited to ascend in deep river water before an unknown power corrupted it into an evil beast.",
    "Taekyung and Cheongpung are fighting the dragon together; Taekyung has a shoulder injury and minor Internal Injury but remains combat-capable.",
    "Cheongpung is highly resistant to the dragon's Fear and is protecting Taekyung while using the Zaha Divine Technique.",
    "Jeok Cheongang and Mungyeong have joined the battle after partially overcoming the dragon's Fear; Zhuge Feng remains affected to some degree.",
    "The dragon uses extreme speed, black scales, hundreds of three-jang whiskers, and targeted attacks against exposed flesh; its black horn has been cut in half and its waist struck.",
    "Taekyung has charged the dragon's falling maw and is thrusting White Flame, wreathed in blue fire, toward its eye.",
    "The Dongting Fisherman remains severely injured, immobilized by Taekyung's seals, and held alive for interrogation about Dark Heaven.",
    "The ferryboat was destroyed by the dragon's falling boulders; the Dongting Fisherman and old boatman remain alive but unconscious.",
    "Honglan is recovering, while Ju Wongong remains unconscious under guard after passing the most dangerous stage of his injuries.",
    "Jin Wikyung is acting as an inspector for the new Murim Alliance and is cooperating with Taekyung's investigation."
  ],
  "continuity_sources": [
    471,
    470
  ],
  "open_questions": [
    "What is the Dongting Fisherman's exact role within Dark Heaven, what information will he reveal, and what caused his involuntary movement and terrified warning?",
    "What caused the earlier deliberate destruction inside the refuge, and how was it connected to the Dongting Fisherman or another intruder?",
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Who destroyed Donghu Stronghold and the related Yangtze River Channel League strongholds, why was no Moving Formation trace left, and was the destruction a diversion?",
    "What unknown power corrupted the Water God Dragon, what are its true origin and purpose, and what is the sharp armor-hard object carried by Jeok Cheongang?"
  ],
  "safe_through": 471,
  "temporary_decisions": [
    "Render 타락한 영물 as Corrupted Spirit Beast and 악물 as evil beast.",
    "Render 기암괴석 as bizarre boulder and preserve jang and geun measurements.",
    "Preserve Taekyung's dry contemporary humor, blunt profanity, and game-like System terminology; retain Cheongpung's dreamy, innocent, increasingly profane voice.",
    "Continue rendering 화룡일미 as Fire Dragon's Single Tail, 강기 as Force, 백염 as White Flame, and 피어 as Fear.",
    "Render the dragon's 수염 as whiskers and its attack descriptions with direct, fast-moving physical imagery."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 살성     | **Slaughter Saint**           | —              |
| 제갈세가   | **Zhuge Clan**                   |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 내공     | **internal energy**                              |                                                       |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 가주     | **Family Head**                              |
| 일격     | **One Strike**                         |
| 노부      | **this old man / I**                                            |
| 본가      | **our family / this family**                                    |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 제갈풍 | **Zhuge Feng** | Current Family Head of the Zhuge Clan. |
| 평화 | **Peace Guild** | Guild name. |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 천기 | **heavenly patterns** | Celestial patterns Hong Dao studies to perceive major changes and omens. |
| 제갈무후 | **Zhuge Wuhou** | Honorific title for Zhuge Liang in the Three Visits allusion. |
| 반로환동 | **Returned to Youth** | Possible explanation for an apparently young Supreme Peak master. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 사량발천근 | **Four Ounces Deflecting a Thousand Catties** | Principle Jongni Chu cites for redirecting force rather than opposing it directly. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 괴력난신 | **supernatural powers** | Term for extraordinary and unnatural powers. |
| 유령환살보 | **Ghost Illusory Slaughter Step** | Movement technique used by the Slaughter Saint. |
| 동정채 | **Donghu Stronghold** | Stronghold where Mu Song's Uncle Hwang is based. |
| 와룡객 | **Crouching Dragon Guest** | Epithet of Zhuge Feng. |
| 장강일도 | **Yangtze One Saber** | Hwang Chung's sobriquet. |
| 비처 | **secret refuge** | Hidden retreat of the Dongting Fisherman. |
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
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 적천강 | 제갈풍 | senior_martial_artist_to_old_acquaintance | you / ill-mannered brat | blunt, familiar, and teasing | Jeok treats Zhuge Feng as the younger acquaintance he remembers from childhood. |
| 제갈풍 | 적천강 | younger_old_acquaintance_to_legendary_senior | Senior | respectful but relaxed | Zhuge Feng recalls Jeok's earlier visit and addresses him as an old senior. |
| 제갈풍 | 문경 | old acquaintance to revealed legendary assassin | Slaughter Saint | excited and respectful | Zhuge Feng identifies Mungyeong by his established sobriquet after recognizing his identity. |
| 문경 | 제갈풍 | legendary_senior_to_younger_family_head | you; burden | blunt, insulting, and commanding | Mungyeong orders Zhuge Feng onto his back and dismisses his objections. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 471
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 471
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 471
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin and Furnace Fire Pure Blue, and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, and pathologically afraid of water. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 471
- **Aliases:** None
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, having passed the Divine Physician title to his Disciple, and he has reached the Returned to Youth realm.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, while Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

### Zhuge Feng.md

# Zhuge Feng (제갈풍)

- **Safe through:** Chapter 471
- **Aliases:** Crouching Dragon Guest
- **Role:** Zhuge Feng is the current Family Head of the Zhuge Clan and father of its Lesser Family Head, Zhuge Gyun.
- **Personality:** Analytical and disarmingly casual, he treats comfort and time as principles while delivering grave intelligence with unsettling directness.
- **Voice:** Clear, calm, polished, and conversational, with understated humor and pointed questioning.
- **Relationships:** Zhuge Gyun is his son, and Zhuge Gonghu was his grandfather.

## Korean source

```text
＃472화



푸푹!

눈동자를 가르며 파고드는 열기는 뜨거웠고 이어지는 고통은 감각을 마비시킬 만큼 차가웠다.

불길처럼 번지는 통증에, 변이된 수신룡은 고통으로 가득 찬 포효를 내질렀다.

- 크롸아아아아!

아름드리나무 십여 그루를 한데 뭉쳐 놓은 듯한 몸통의 두께와 삼십여 장을 훌쩍 넘기는 길이.

마치 작은 산을 연상시키는 거대한 동체가 미친 듯이 몸부림치자 엄청난 여파가 주변을 휩쓸었다.

꽈앙! 콰과과과광!

앞서 날려 보낸 기암괴석이 수백, 수천 개의 조각으로 나뉘어 터져 나가고 흙과 물의 장벽이 솟구쳤다.

마치 집중 포격을 맞은 것처럼 사방이 초토화되는 가운데, 이 혼란 사이를 쾌속하게 가로지르는 존재들이 있었다.

쉬쉬쉭!

누군가는 괴물을 향해 달려들고, 누군가는 괴물의 몸부림을 피해 멀찍이 물러난다. 제갈세가의 당대 가주, 와룡객 제갈풍은 그중 후자에 속했다.

비로소 이성을 되찾게 된 그는 아연한 시선으로 눈앞의 광경을 바라보았다.

‘천기(天氣)가 일그러지는 것으로도 모자라, 이제는 괴력난신의 존재까지 나타나는가.’

제갈풍은 영물, 혹은 악물이라 불리는 것들에 관한 숱한 지식을 갖고 있었으나 저 용을 닮은 괴물은 모든 상식을 파괴했다.

아마 오늘 이 자리에 벌어진 일이 세상에 알려진다면, 무림뿐만 아니라 천하가 경악에 휩싸일 것이 분명했다.

‘어찌 이런 일이…….’

아직도 완전히 가시지 않은 두려움으로 인해 몸을 부르르 떠는 제갈풍을 향해 한 사람이 입을 열었다.

“다른 분들과 함께 이곳에 계세요. 엄폐물 뒤에 숨어서 최대한 안전하게.”

무림인이라면 그 말을 들은 순간 자존심이 상할 수밖에 없다. 무림인이라는 족속은 자신의 무공과 검 한 자루에 목숨을 걸고 도산검림(刀山劍林)을 주유하는 자들이니까.

제갈풍은 딱딱하게 굳은 얼굴로 상대를 바라보며 입을 열었다.

“내가 누구인가?”

“네?”

“내가 누구인지 아느냐 물었네.”

청풍이 대답했다.

“네. 제갈퐁 대협.”

“제갈퐁이 아니라 제갈풍일세. 여하튼 자네 역시 내가 제갈세가의 가주라는 것을 모르지 않을 터.”

“어어, 알고 있긴 한데요…….”

“한데, 자네는 제갈세가의 가주에게 겁쟁이처럼 숨으라는 것인가?”

고민하던 청풍이 고개를 끄덕였다.

“그편이 훨씬 안전하니까요.”

“좋아. 그럼 꼼짝 말고 여기에 있어야겠군.”

“네?”

“이곳이 안전하다고 하지 않았나? 괜히 개죽음당하는 것보다야 겁쟁이가 훨씬 낫지.”

“……?”

“그런 눈으로 볼 것 없네. 단지 오늘은 내가 나서야 할 싸움이 아닐 뿐이니까. 본가의 선조이신 제갈무후(諸葛武侯)께서 선봉에서 적들을 베어 넘기지 않으신 것과 같은 이치지.”

제갈풍은 자신의 위치와 해야 할 일들을 정확히 알고 있었다.

그는 무인의 자존심에 목숨을 걸기에는 너무나도 냉철한 사람이고, 수많은 가솔을 거느린 일가의 가주니까.

“이 거대한 전란은 이제 막 시작되었으니, 향후 벌어질 전투에서 내 가치를 증명할 날이 오겠지. 그러니 이만 가 보도록 하게. 이들은 내가 잘 보호하고 있을 테니.”

묘한 눈빛으로 제갈풍을 바라보던 청풍이 목례와 함께 돌아섰다.

이내 한 줄기의 바람이 되어 멀어지는 청년의 뒷모습을 바라보는 제갈풍의 눈동자는 깊게 가라앉아 있었다.

‘그래, 또 다른 난세의 시작이로구나.’

오십여 년간 이어졌던 평화는 막을 내렸다. 검게 물든 하늘에는 먹구름이 가득하고, 새로운 바람이 사방에서 불어오고 있었다.

저 멀리 전장을 향해 쏘아지는 청풍 역시 그 바람 중 하나다.

‘무후(武侯)시여. 적어도 오늘만큼은 이 불민한 후손이 나설 자리가 없을 듯합니다.’

제갈풍이 마음속으로 작게 뇌까리던 그때, 등 뒤에서 넋 나간 목소리들이 나누는 대화가 귓가를 파고들었다.

“저기 괴물이 보이는데. 꿈인가?”

“꿈은 아닌 것 같은데요. 아니다. 꿈인 것 같기도 하고.”

“그런데 혁가 너, 바지가 왜 그렇게 축축해?”

“비 오잖아요. 젖었나 봐요.”

“빗물치고는 샛노란데.”

“그럴 수 있죠.”

“그런가? 거 참 희한하네. 그나저나 이거 진짜 꿈 아닌가?”

“꿈은 아닌 것 같은데요. 아니다. 꿈일지도 몰라요.”

“그런데 혁가 너, 바지가 왜 그렇게 축축…….”

“…….”

도무지 종잡을 수 없는 대화를 듣고 있던 제갈풍은 오줌 지린내를 피해 슬쩍 걸음을 옮겼다.

흙과 모래가 쌓이고 쌓여 작은 동산을 만들어 낸 언덕 위.

그의 시선이 향하는 곳에서는 신화 속 한 장면을 옮겨다 놓은 듯한 전투가 벌어지고 있었다.



* * *



쉭, 서걱!

한 줄기의 은빛 선이 공간을 가르자 덮쳐오던 모든 것들이 베어졌다.

파팟! 허깨비처럼 사라진 문경의 신형이 허공에 떠오른 돌조각을 밟고 솟구친 순간.

후우우웅!

물보라와 먼지구름을 헤치며 덮쳐오는 거대한 무언가.

그것의 정체가 흑색 비늘로 뒤덮인 꼬리라는 사실을 깨닫기까지는 그리 오랜 시간이 필요하지 않았다.

‘빠르다. 생각했던 것 이상으로.’

엄청난 크기의 체구가 믿어지지 않을 만큼 쾌속한 움직임. 문경은 호흡과 함께 소검을 힘껏 움켜쥐었다.

츠츠츠츠!

조용하게, 그러나 섬전과도 같은 속도로 끌어올린 공력이 소검을 휘감았다.

천하의 어떤 것보다 파괴적이고 예리한 힘. 강기가 검신을 타고 솟구쳤다.

극쾌(極快)의 묘리를 담은 일 초가 고금제일 살수의 손끝을 타고 흘러나왔다.

‘단숨에 벤다.’

그리고 다음 순간, 덮쳐 오는 꼬리를 향해 비스듬히 일검을 내리그은 문경은 자신의 오판을 깨달았다.

서걱.

분명 베었음에도 전해지는 반발력이 터무니없이 강하다.

소검에 실린 강기가 베어야 하는 것은 흑색 비늘뿐만이 아니었다.

강철만큼이나 단단한 비늘에 숨겨진 것은 무쇠 같은 살과 근육. 그리고 엄청난 강도를 자랑하는 뼈였다.

‘이런.’

문경은 내심 혀를 찼다.

강기. 그것도 다름 아닌 고금제일 살수의 깨달음이 녹아든 강기다.

이 괴물의 몸뚱어리가 제아무리 단단하다 해도 그의 강기라면 단숨에 베어 버릴 수 있었다.

다만 문제는 두께였다.

직경만 이 장에 이르는 무지막지한 꼬리의 두께.

거기에 예상을 훌쩍 뛰어넘는 피륙의 강도까지 더한다면…….

‘일격으로 단번에 베어 내는 것은 무리겠군.’

평소였다면 모를까, 피어의 잔재에서 완전히 벗어나지 못한 그는 자신의 무위가 제 실력을 발휘하지 못할 것이라는 사실을 누구보다 잘 알고 있었다.

‘그렇다면.’

문경은 판단과 동시에 검파를 잡은 손목을 비틀었다.

비늘을 베고 살과 근육을 갈라가던 검날이 부드럽게 회전하며, 검의 옆면으로 꼬리에 실린 힘을 흘려보냈다.

카가각, 후웅!

작고 호리호리한 신형이 허공으로부터 튕겨져 나갔다.

쾅!

허공에서 신형을 뒤집은 문경이 유령환살보라는 이름과 어울리지 않는 거친 움직임으로 내려서자, 옆에서 날아드는 기암괴석을 일장으로 녹여 버린 적천강이 놀리듯이 중얼거렸다.

“반로환동 하더니 무공도 어린애가 됐나?”

“힘과 속도. 모두 예상치를 훌쩍 뛰어넘는군. 사량발천근(四兩撥千斤)의 묘리로도 완전히 흘리지 못했어.”

“혓바닥도 길어졌고.”

문경이 건조한 눈빛으로 적천강을 힐끗 바라보았다.

“도발하는 것이라면 이쯤에서 그만두지. 시기가 영 좋지 않은 것 같은데.”

“도발이 아니라 엄연한 사실이야. 아까 노부가 한 대 치니까 저놈이 픽 쓰러지는 꼴 못 봤어?”

“그건 내가 먼저 놈의 뿔을 자른 상황에서…….”

취리리리릭! 콰앙!

터져 나온 굉음이 이어지려던 문경의 목소리를 집어삼켰다.

약속이라도 한 것처럼 동시에 신형을 날린 두 사람은, 살아 있는 생물처럼 꿈틀거리는 빛줄기를 바라보며 혀를 찼다.

조금 전만 해도 그들이 있던 자리는 온통 초토화가 되어 있었다.

“보면 볼수록 해괴한 놈이로다. 악물(惡物) 주제에 강기를 구사해?”

“강기라고 하기에는 부족하고, 검기라고 하기에는 너무 강하다. 분명 내공심법은 아닌데…… 오랜 세월 축적된 기운으로 이런 기예를 구사한다는 것만으로도 믿을 수 없을 지경이야.”

기운을 품는 것과 기운을 활용, 발산하는 것은 궤를 달리한다.

그런 의미에서 눈앞의 괴물은 두 사람이 갖고 있던 상식을 아득히 뛰어넘었다.

‘장강일도와 동정채를 전멸시킨 것도 저것의 소행인가.’

재차 날아드는 공격을 피한 문경은 심유한 눈빛으로 괴물을 바라보았다.

그는 최소 두 명 이상의 초절정 고수가 동정채를 습격했다고 짐작했지만, 저 상상치도 못한 괴물을 마주하니 비로소 어찌 된 일인지 알 것 같았다.

‘저 괴이한 수염과 거대한 몸집…… 틀림없다. 시신들에 남아 있던 흔적과 유사해.’

꼬리와 수염을 이용하여 닥치는 대로 뭉개고 베어 버렸을 광경이 눈앞에 선했다.

더불어 모두가 물고기 떼에 의해 훼손되었다고 생각한 장강일도의 시신에 대한 의문도 풀렸다.

‘죽어서 뜯어 먹힌 것이 아니라, 뜯어 먹혔기에 죽었던 거였어.’

그 누가 상상이나 했겠는가.

용을 닮은 거대한 괴물이 뱃길로도 막혀 있는, 오직 물고기들만이 오갈 수 있는 물속 깊숙한 지류를 통해 살육을 저질렀다는 것을.

모습을 드러내지 않으니 목격자가 없는 것도 당연한 일이었으리라.

“괴물이 따로 없군.”

인정할 수밖에 없었다. 저 괴물은 수백의 절정 고수, 혹은 초절정 고수 두 세명과 비견될 만한 힘을 지닌 괴력난신의 존재다.

그리고 그런 문경의 탄식에 적천강은 고개를 끄덕여 동의를 표했다.

“맞아. 괴물이지.”

“이런 불가사의한 존재가 정말 있을 줄이야.”

“볼 때마다 놀라운 놈이야. 그래서 미련이 생기고는 하지. 더, 조금 더 노부에게 시간이 있었다면 어땠을까, 하는 미련.”

“지금 무슨…….”

그제야 문득 무언가를 떠올린 문경이 적천강을 바라보았다. 감출 수 없는 세월이 서린 노인의 주름진 얼굴에는 미소가 가득했다.

“이봐, 살성. 그거 알고 있나?”

후우우웅!

천하를 쪼갤 듯한 기세로 떨어져 내리는 거대한 그림자.

자신의 자그마한 체구 위로 떨어져 내리는 흑색 꼬리를 올려다보던 적천강이 천천히 말을 이었다.

“그놈은 말이야. 노부가 지금껏 살아오며 본 것 중 가장 기이하고 무서운 괴물이라네.”

“위험……!”

문경이 눈을 부릅뜬 그 순간.

콰과과광! 푸화아아악!

거대한 굉음과 진동이 반경 수십여 장을 뒤덮었다.

그리고 그 모든 것의 중심에서, 털끝 하나 다치지 않은 채 우뚝 선 적천강이 모습을 드러냈다.

원래 서 있던 자리에서 단 한 걸음도 움직이지 않은 그와 달리, 흑색 비늘로 뒤덮인 꼬리는 한참 벗어난 곳을 직격한 후였다.

“그래, 그렇고 말고. 역시 괴물은 괴물로 상대해야 제격인 게야.”

“……!”

투두두둑.

껄껄 소리 내어 웃는 적천강의 머리 위, 괴물의 검푸른 핏물이 비바람과 섞여 쏟아져 내렸다.

괴물의 거대한 동체를 향해 고개를 돌린 문경과 막 전장으로 복귀한 청풍은 마침내 볼 수 있었다.

- 그워어어어어!

몸부림치는 괴물과, 까마득한 높이에 있는 놈의 머리에 대롱대롱 매달린 채 맨손으로 수염을 잡아 뜯는 누군가의 모습을.

“민머리! 대머리! 맨들맨들 빡빡이!”

뽁! 뽁! 뽀보보보복!

- 크뤄어어어어어!

수신룡의 구슬픈 비명이 비바람을 뚫고 울려 퍼졌다.
```

## Final English reading copy

```markdown
# Chapter 472

*Puhuk!*

The heat boring through the pupil was scorching, while the pain that followed was cold enough to numb the senses.

The Mutated Water God Dragon let out a roar filled with agony as the pain spread through its body like flames.

—Kraaaaaaaaaah!

Its torso was as thick as a dozen or so full-grown trees bundled together, and its length easily exceeded thirty *jang*.

When the enormous body, reminiscent of a small mountain, thrashed about madly, a tremendous shock wave swept through the surrounding area.

*Kwang! Kwagwagwagwang!*

The bizarre boulders it had hurled earlier exploded into hundreds and thousands of fragments, while barriers of dirt and water surged into the air.

As every direction was reduced to a wasteland as though it had been subjected to concentrated bombardment, several figures raced swiftly through the chaos.

*Shh-shh-shik!*

Some charged toward the monster, while others retreated a considerable distance to avoid its thrashing. Zhuge Feng, the current Family Head of the Zhuge Clan and the Crouching Dragon Guest, belonged to the latter group.

At last, his reason returned, and he stared at the scene before him in bewilderment.

*It isn’t enough that the heavenly patterns are becoming distorted. Now beings of supernatural powers are appearing too?*

Zhuge Feng possessed an abundance of knowledge about the creatures called spirit beasts or evil beasts, but this dragon-like monster shattered every bit of common sense.

If word of what had happened here today reached the outside world, there was no doubt that not only the Murim but the entire world would be thrown into an uproar.

*How could something like this happen…?*

Zhuge Feng’s body trembled from fear that still had not completely faded when someone spoke to him.

“Stay here with the others. Hide behind cover and keep yourselves as safe as possible.”

Any martial artist would have felt his pride wounded upon hearing those words. Martial artists were people who staked their lives on their martial arts and a single sword as they roamed mountains of blades and forests of swords.

Zhuge Feng looked at the other person with a stiff expression and opened his mouth.

“Who am I?”

“Pardon?”

“I asked if you know who I am.”

Cheongpung answered.

“Yes. Great Hero Zhuge Pong.”

“It’s Zhuge Feng, not Zhuge Pong. In any case, you do know that I’m the Family Head of the Zhuge Clan.”

“Uh, yes, I do know that…”

“And yet you’re telling the Family Head of the Zhuge Clan to hide like a coward?”

Cheongpung thought about it, then nodded.

“That would be much safer.”

“Good. Then I should stay right here without moving.”

“Pardon?”

“Didn’t you say this place was safe? Better to be a coward than die a pointless death.”

“…?”

“Don’t look at me like that. It’s simply that this isn’t a battle I need to fight today. It’s the same reason Zhuge Wuhou, our family’s ancestor, did not stand at the vanguard and cut down the enemy.”

Zhuge Feng knew exactly where he stood and what he needed to do.

He was too clearheaded to wager his life on a martial artist’s pride, and as a Family Head, he was responsible for countless members of his household.

“This vast war has only just begun. The day will come when I can prove my worth in the battles ahead. So go on. I’ll protect these people.”

Cheongpung regarded Zhuge Feng with a strange look, then turned away with a small bow.

As the young man disappeared into the distance like a gust of wind, Zhuge Feng’s gaze grew somber.

*Yes. The beginning of another age of chaos.*

The peace that had lasted for more than fifty years had come to an end. The sky had turned black with clouds, and new winds were blowing in from every direction.

Cheongpung, shooting toward the distant battlefield, was one of those winds.

*Wuhou. At least today, it seems there is no place for this unworthy descendant to step forward.*

Just as Zhuge Feng muttered those words quietly to himself, a conversation in dazed voices behind him pierced his ears.

“I can see a monster over there. Is this a dream?”

“I don’t think it’s a dream. No. Maybe it is a dream.”

“But Hyuk, why are your pants so wet?”

“It’s raining. They must have gotten wet.”

“That’s a very bright yellow for rainwater.”

“That can happen.”

“Can it? How strange. Anyway, isn’t this really a dream?”

“I don’t think it’s a dream. No. Maybe it is a dream.”

“But Hyuk, why are your pants so wet—”

“…”

Zhuge Feng listened to the utterly incoherent conversation, then quietly moved away to escape the smell of urine.

On a hill formed by dirt and sand that had piled up into a small mound, he looked toward a battlefield that resembled a scene taken straight from mythology.

* * *

*Shhk, schk!*

When a silver line cleaved through space, everything rushing toward him was cut apart.

*Papat!*

The instant Mungyeong’s figure vanished like an illusion and then sprang upward after stepping on a fragment of stone suspended in the air—

*Whoooooosh!*

Something enormous came hurtling through the spray and clouds of dust.

It did not take long for him to realize that it was a tail covered in black scales.

*It’s fast. Faster than I expected.*

Its movements were impossibly swift for a body of such tremendous size. Mungyeong gripped his short sword tightly as he drew a breath.

*Tsstsstssts!*

Quietly, yet at a speed as sudden as lightning, internal energy surged upward and wrapped around the short sword.

A power more destructive and sharper than anything in the world. Force rose along the blade.

A technique containing the principles of extreme swiftness flowed from the fingertips of the greatest assassin of all time.

*I’ll cut it in one stroke.*

The next moment, Mungyeong brought his sword down diagonally toward the incoming tail—and realized that he had miscalculated.

*Schk.*

Although he had clearly cut it, the resistance transmitted through the blade was absurdly strong.

The Force imbued in his short sword had to cut through more than black scales.

Hidden beneath scales as hard as steel were flesh and muscles like wrought iron, along with bones boasting tremendous strength.

*Damn.*

Mungyeong clicked his tongue inwardly.

Force. And not just any Force, but Force infused with the enlightenment of the greatest assassin of all time.

No matter how hard the monster’s body was, his Force should have been able to cut through it in a single stroke.

The problem was its thickness.

The tail was a monstrous two *jang* in diameter.

Add to that the toughness of its flesh, which far exceeded his expectations…

*Cutting through it in one strike is impossible.*

Under normal circumstances, it might have been different. But he had not yet completely escaped the remnants of Fear, and he knew better than anyone that his martial prowess would not be at its full strength.

*In that case…*

At the same time as he made his decision, Mungyeong twisted the wrist gripping the sword hilt.

The blade, which had cut through the scales and was splitting the flesh and muscles beneath them, rotated smoothly. Its side diverted the force carried by the tail.

*Ka-ga-gak! Whoom!*

His small, slender figure was flung backward through the air.

*Kwaang!*

Mungyeong twisted his body in midair and landed with a rough movement that did not suit the name of the Ghost Illusory Slaughter Step. Beside him, Jeok Cheongang melted an incoming bizarre boulder with a single palm strike and muttered mockingly.

“Did your martial arts become childish too after you Returned to Youth?”

“Its strength and speed both far exceeded my expectations. Even with the principles of Four Ounces Deflecting a Thousand Catties, I couldn’t completely redirect it.”

“Your tongue got longer, too.”

Mungyeong gave Jeok Cheongang a dry sidelong glance.

“If you’re trying to taunt me, stop here. The timing seems rather poor.”

“It isn’t a taunt. It’s an undeniable fact. Didn’t you see that thing crumple when this old man hit it once?”

“That was after I had already cut its horn…”

*Chiririririk! Kwang!*

A thunderous explosion swallowed Mungyeong’s continuing words.

The two men launched themselves away at the same time, as though they had made an agreement, and clicked their tongues while staring at the streak of light writhing like a living creature.

Only moments ago, the place where they had been standing had been completely devastated.

“The more I see, the more bizarre that thing becomes. An evil beast that can use Force?”

“It isn’t strong enough to be called Force, yet it’s too powerful to be called Sword Energy. It’s clearly not a cultivation technique, but the fact that it can use an art like this with energy accumulated over countless years is difficult to believe.”

Possessing energy and utilizing or releasing it were fundamentally different matters.

In that respect, the monster before them had far surpassed the common sense of both men.

*Was that thing also responsible for wiping out Yangtze One Saber and Donghu Stronghold?*

Mungyeong avoided the attack flying toward him once again and stared at the monster with profound eyes.

He had assumed that at least two Supreme Peak masters had attacked Donghu Stronghold. But after encountering that unimaginable monster, he finally felt that he understood what had happened.

*Those bizarre whiskers and that enormous body… There’s no mistake. They resemble the traces left on the corpses.*

He could picture the scene clearly: the monster crushing and cutting everything in its path with its tail and whiskers.

At the same time, the mystery surrounding the corpse of Yangtze One Saber, which everyone had thought had been damaged by schools of fish, was solved.

*He wasn’t torn apart and eaten after he died. He died because he was torn apart and eaten.*

Who could ever have imagined it?

That an enormous dragon-like monster had committed such a slaughter through a deep tributary blocked even to boats, a waterway that only fish could enter and leave.

Since it had never revealed itself, it was only natural that there had been no witnesses.

“It’s a monster, all right.”

He had no choice but to admit it. That monster possessed enough power to rival hundreds of Peak masters—or two or three Supreme Peak masters. It was a being of supernatural powers.

Jeok Cheongang nodded in agreement with Mungyeong’s lament.

“That’s right. It’s a monster.”

“I never thought such an inexplicable being truly existed.”

“That one never ceases to amaze me. That’s why I can’t help wondering what it would have been like if this old man had had more time. Just a little more time.”

“What are you—”

Mungyeong suddenly remembered something and looked at Jeok Cheongang. The old man’s wrinkled face, marked by the passage of countless years, was filled with a smile.

“Hey, Slaughter Saint. Do you know something?”

*Whoooooosh!*

A gigantic shadow descended with enough momentum to split the world apart.

Jeok Cheongang looked up at the black tail falling toward his small body and slowly continued.

“That one is the strangest and most terrifying monster this old man has ever seen.”

“Look out!”

Mungyeong’s eyes widened.

*Kwa-gwa-gwa-gwang! Fwoooosh!*

A tremendous roar and vibration spread across a radius of several dozen *jang*.

And at the center of it all, Jeok Cheongang stood tall without a single hair on his body harmed.

Unlike him, who had not moved even one step from where he had originally been standing, the black-scaled tail had struck the ground far away.

“Yes, that’s right. A monster should be fought by a monster.”

“……!”

*Thud-thud-thud.*

Above Jeok Cheongang’s head, where he laughed aloud, the monster’s dark-blue blood poured down mixed with the rain and wind.

Mungyeong turned toward the monster’s enormous body, and Cheongpung, who had just returned to the battlefield, looked in the same direction.

At last, they saw it.

The thrashing monster—and someone hanging from its head at a dizzying height, tearing out its whiskers with his bare hands.

“Baldy! Bald! Smooth, shiny, shaved head!”

*Ppok! Ppok! Ppobobobok!*

—Kroooooooooah!

The Water God Dragon’s mournful cry rang out through the rain and wind.
```
