<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1001.txt",
      "sha256": "6d0e1bf984c537e2a790269a6fa08ce6f43a7487917dfa98b39d4ebff2877aa6",
      "bytes": 13404
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "05abc3bd414cb7a70781b8f18cf782e7171af94a42fd9da97b00d2899ef4e4ec",
      "bytes": 1692
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d13308fe31a2c64daebd8b79b1737ef2a4f6a2f6e86338670363f6d7acf5174f",
      "bytes": 236719
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "3797e1504adf9f4cf92cc3a61b665eccba0937c1f08a7e1e5da445ab2a232f5a",
      "bytes": 760
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "fe5c64116f337cd20ffb8795d5613b759d94367484860471ffaaca53bdf0d83a",
      "bytes": 1374
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "b6428d2828420701084f58e7d10b19ba3ed07f0aa8b8348c2d050a35380d8efb",
      "bytes": 1392
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "4cb5dded0f13c81303341c28809394b3aaf9f2d7e1aa6ca09338f47887b535ca",
      "bytes": 937
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "54ad9e5e161e33255cf7ff3d794930d3701f78ffeec3ce6b4b52eda8ef054ce0",
      "bytes": 274397
    }
  ],
  "estimated_tokens": 10269
}
-->

# Durable State Update — Chapter 1001

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
1 and safe_through 1001. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1001. Profile updates may replace only one
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
  "chapter": 1001,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1001,
    "continuity_sources": [1001],
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
    "Taekyung’s group and the Zhongnan party are heading to Gansu together.",
    "Song Il and Hwangbo Eom have apologized, but their resentment remains; they have agreed to fight alongside the Murim against Dark Heaven.",
    "Gong Iljung says Zhongnan held back its main force to protect the sect.",
    "Dark Heaven’s army is reportedly advancing beyond the desert, but its destination is unknown; Qinghai, Gansu, and Tibet are possible routes into the Central Plains.",
    "Dark Heaven’s Moving Formations could transport forces into the Central Plains; their number and locations are unknown, and neutralizing them would require time and manpower.",
    "The Demon-Sealing Formation may be able to neutralize Moving Formations; Zhuge Feng’s clan used it to contain the rift at Dongting Lake.",
    "Sama Pyo’s Black Dragon Demon Gate in Gansu may be threatened by Dark Heaven’s advance through Xinjiang.",
    "The Nanman Beast Palace accepted the Murim Alliance’s request and is defending Sichuan alongside the still-intact Qingcheng and Emei.",
    "Jeok Cheongang has regained a middle-aged appearance and youth.",
    "Zhongnan sent only three hundred of its reported thousand reinforcements to Shanxi, and they arrived a day after the fighting ended."
  ],
  "continuity_sources": [
    999,
    1000
  ],
  "open_questions": [
    "Where will Dark Heaven’s advancing army strike, and what is its objective?",
    "What caused the System malfunction, and is it connected to the Lord of Heaven?",
    "Why did Sama Pyo’s father order him to return immediately?"
  ],
  "safe_through": 1000,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 종남파    | **Zhongnan Sect**                |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 기연     | **fortuitous encounter**                         | Use sparingly                                         |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 마적     | **mounted bandits**                              |                                                       |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 사제     | **Junior Brother**                           |
| 선배     | **Senior**                                   |
| 사천     | **Sichuan**            |
| 감숙     | **Gansu**              |
| 노부      | **this old man / I**                                            |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 노호검객 | **Roaring Fury Swordsman** | Fiery-tempered elder and top-five master of the Zhongnan Sect. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 태을무정검 | **Taeeul Merciless Sword** | Title of the Zhongnan Sect’s Second Martial Uncle, who is in Xi’an. |
| 이동진 | **Moving Formation** | Dark Heaven's inactive long-distance transportation formation. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 흑룡도 | **Black Dragon Saber** | Sama Pyo's sobriquet. |
| 종남 | **Zhongnan Sect** | Orthodox faction that fought in the historic battle. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 사마표 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | formal but sardonic | Sama Pyo addresses Jin as 각주 while questioning his account of the incident. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1000
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 999
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1000
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1000
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

## Korean source

```text
＃1001화



종남파와의 동행은 갑작스럽게 결정되었다.

장문인인 풍운검군이 먼저 합류를 제의했고, 내가 잠시 고심하던 사이에 불쑥 끼어든 적천강이 그 제안을 받아들였기 때문이었다.

“동행이라, 그것도 나쁘지 않겠지.”

“노, 아니 스승님.”

“뭣 하느냐. 어서 네 수하들을 준비시키지 않고. 풍운검군 자네도 저기 퍼질러 앉아있는 제자 놈들 궁둥짝부터 걷어차게.”

그렇게 번갯불에 콩 볶듯 순식간에 모든 준비가 끝났다.

반올림 좀 더해서 천여 명으로 불어난 일행은 감숙성을 향해 이동을 시작했고, 그들 중에는 썩 즐거워 보이지 않는 노호검객과 태을무정검 또한 포함되어 있었다.

“아까부터 저놈들 표정이 아주 죽상이구먼. 더도 말고 덜도 말고 딱 반년 전에만 만났어도 죽통부터 한 대 갈기는 건데.”

입맛을 다시며 중얼거리는 적천강의 모습에, 나는 작게 혀를 찼다.

“저 꼴 보기 싫었으면 제안을 받아들이지 말았어야죠.”

“그 때문이더냐? 네 녀석 입이 석 자나 튀어나온 이유가?”

“아니, 누가 입이 튀어나왔다고 그러세요?”

“정정하마. 이제는 넉 자까지 튀어나왔군.”

적천강의 놀림에 나는 고개를 절레절레 흔들었다.

그나마 종남파와 삼십여 장 정도의 거리를 두고 멀찍이 떨어져 후미를 맡은 덕분에, 이런 대화라도 대놓고 할 수 있다는 점이 유일한 장점이었다.

“예, 불만입니다. 됐어요?”

“거 참, 알다가도 모를 일이로군. 이럴 거면 껍데기뿐인 화해는 왜 했누?”

껍데기뿐인 화해.

그야말로 더할 것도, 뺄 것도 없는 정확한 표현이다.

이미 적천강이 지금껏 전음으로 오간 대화를 모두 들었을 거라 짐작하고 있던 나는, 별다른 놀라움 없이 입을 열었다.

“그야 당연히…….”

“필요하니까?”

“예.”

“필요에 의해 화해를 하고, 겉으로나마 웃는 얼굴로 지난 악연을 덮는다…… 네 녀석도 어느새 머리가 굵어졌구나.”

실로 묘한 어투다.

칭찬인지, 질책인지 헷갈리는 적천강의 한 마디에 말없이 물끄러미 바라보고만 있자니 그가 피식 웃었다.

“그리 깊게 생각할 것 없느니라. 단지 어느 방향으로든 한 단계 성장한 모습을 본 것 같아 기쁠 따름이니.”

“말씀하신 그 방향이, 혹 잘못되었다고 생각하시는 겁니까?”

“글쎄다. 중요한 것은 결과가 아니겠느냐.”

“보통은 과정이 결과 못지않게 중요하다고 하지 않나요? 결과보다도 과정을 중시하거나.”

“전자는 앞뒤 꽉 막힌 놈들이나 하는 소리고, 후자는 결과를 대차게 말아먹은 놈들이 즐겨 쓰는 개소리지.”

신랄할 정도로 단호하게 대답한 적천강이 말을 이었다.

“만약 노부가 보기에 네 녀석이 잘못을 저질렀다면 크게 혼쭐을 내었을 것이나, 아직까지는 썩 나쁘지 않다. 게다가 저 게을러터진 놈들을 감숙까지 소몰이하듯 몰고 가는 것도 괜찮겠지.”

아닌 게 아니라 지금 이 순간에도 종남파의 제자들은 뭐 빠지게 뛰는 중이다. 일방적으로 후미를 자처한 적천강이 출발 전 했던 선언 때문이었다.



‘지금 이 순간부터 감숙성에 도착하기 전까지, 조금이라도 뒤처지거나 뺀질대는 놈들은 노부가 친히 개인 면담을 해 주마.’



아득한 경지에 도달한 고인(古人)과의 개인 면담은 누구나 바라마지 않는 기연이겠지만, 그 상대가 화왕이라면 진짜 고인이 될 가능성이 농후하다.

쉬쉬쉬쉬쉭!

살길을 찾아 산기슭을 죽도록 내달리는 하이에나, 아니 종남파 제자들을 본 적이 있는가.

나는 있다.

그리고 젖 먹던 힘까지 쥐어 짜내어 내달리는 종남파 제자들의 모습을 흡족하게 지켜보던 적천강이, 돌연 힘차게 지면을 박찼다.

쾅! 쐐애액!

날카로운 굉음과 함께 삽시간에 늘어지는 신형.

잔상(殘像)과도 같은 그것을 남기며 삽시간에 가까워지는 적천강의 모습에, 헛숨을 들이킨 종남파 제자들 사이에서 다급한 외침이 터져 나왔다.

“뛰어!”

“따라잡히면 끝장이다!”

“사, 사형. 저는 틀렸습니다. 이 못난 사제는 괘념치 마시고 어서……!”

“안 돼! 포기하지 말거라! 살 수 있다!”

“…….”

그 광경을 본 내 소감은 짧고 명료했다.

아주 지랄 염병들을 해라.

“누가 보면 암천이라도 나타난 줄 알겠…… 어라?”

들불을 만난 메뚜기 떼처럼 도망치는 종남파 제자들을 보며 혀를 차던 그때, 문득 뭔가를 발견한 나는 눈매를 좁혔다.

동시에 깨달았다.

적천강이 돌연 속도를 높여 앞으로 나아간 진짜 이유를.

‘뭐지, 저건?’

어느덧 좁은 산길을 빠져나가며 나타난 언덕과 함께 탁 트인 시야.

문제는 그와 동시에 저 멀리에서 초옥(草屋) 백여 채가 옹기종기 모여 있는 작은 마을과 일단의 무리가 모습을 드러냈다는 것이었다.

그 머릿수만 일견해도 족히 수백,

자그마한 마을 어귀에 바글거리는 인파를 뒤늦게 발견한 혁무진도 눈을 크게 떴다.

“조장님. 저거 설마.”

귓가로 전해지는 다급한 목소리.

곧 이어지려는 뒷말을 짐작한 나는, 한 박자 앞서 입을 열었다.

“벌써부터 겁먹지 마. 적은 아닌 것 같으니까.”

“예? 그럼…….”

“전부 양민들이야.”

짤막하게 대답한 나는 잠시 생각하다가 덧붙였다.

“적어도 지금 당장 보이는 바로는.”

굳이 그런 말을 덧붙인 이유는, 사실 나도 완전히 확신할 수는 없기 때문이다.

지금까지의 행로를 살펴보았을 때, 현재 우리의 위치는 섬서에서 감숙으로 넘어가는 어느 경계선.

더군다나 암천은 이동진(移動陳)이라는 사술을 보유하고 있으니, 당장 이곳에서 양민으로 위장한 놈들과 맞닥트린다 해도 그리 놀라운 일은 아니다.

암천은 이미 한번 사천에서도 관군으로 위장했던 전력이 있었으니까.

‘감숙성에 변고가 있었다면 이미 소식이 전해지고도 남았을 텐데. 이런 산골짜기의 작은 마을에 저 많은 인파는 도대체 뭐지? 정말 이동진을 통해 기습을 준비한 건가?’

머릿속 의문이 꼬리에 꼬리를 물고 이어지던 그 순간이었다.

스릉.

불현듯 울려 퍼진 서늘한 소리.

고개를 돌리자 어느새 자신의 별호와도 같은 애병, 흑룡도(黑龍刀)를 뽑아 든 사마표가 그곳에 있었다.

“저들의 정체가 무엇이든, 미리 대비해서 나쁠 건 없겠지. 그렇지 않나, 각주?”

침착한 목소리와는 달리 깊게 가라앉은 두 눈동자.

감숙성에 가까워질수록 점점 더 무거운 분위기를 내뿜기 시작한 사마표의 모습에, 조용히 고개를 끄덕인 나는 말에 박차를 가했다.

두두두두!

힘차게 지면을 내달리는 초원마의 말발굽.

그 끝에 기다리고 있을 저 인파의 정체가 무엇인지는 모르겠지만, 적어도 한 가지만큼은 확실했다.

‘만약 암천이 준비한 기습이라 해도, 짓밟고 지나가면 그뿐이다.’

한바탕 치열한 전투가 벌어질지도 모르는 상황이었으나 심장 박동은 평소와 다르지 않았다.

이런 산골짜기에서 가로막히기에는, 이미 내가 너무나도 강해졌기에.



* * *



결론만 말하자면, 우려했던 불상사는 벌어지지 않았다.

아니, 정정한다.

적어도 아군에게만큼은 그랬다는 표현이 훨씬 정확할 테니까.

“놈들이, 놈들이 나타났다!”

“꺄아악!”

“어, 어서 모두 몸을 피하시오!”

사방에서 다급한 외침과 비명이 터져 나온 것은 어쩌면 당연한 일이었다.

마치 제방(堤坊)이 허물어지듯, 가파른 언덕을 넘어 쏟아지는 수상한 무리를.

그 숫자만 무려 일천에 가까운 데다, 심지어 몇몇은 이미 시퍼런 날붙이를 손에 들었으니 자그마한 마을 어귀에 모여 있던 수백의 인파에게는 그야말로 재앙이나 다름없었다.

그리고 결코 거짓으로 꾸며 낼 수 없는 그들의 반응에, 적천강과 함께 선두에서 쏘아지던 풍운검군이 벼락처럼 외쳤다.

“그만! 모두 멈추어라!”

쉬쉭!

다른 누구도 아닌 장문인의 명령이다.

공력이 실린 그 외침에 수많은 종남파의 제자들이 빠르게 속도를 줄이며 자리에서 멈춰섰지만, 예외는 어디에나 있는 법이었다.

쉭.

다른 이들과는 궤를 달리하는 미세한 파공성.

풍운검군의 명령에도 아랑곳하지 않고 바람처럼 쏘아지는 두 인영의 뒷모습에, 종남파의 제자들과 함께 속도를 줄이고 있던 나는 내심 혀를 찼다.

‘그래, 어쩐지 저럴 것 같더라.’

개 버릇 남 못 준다는 말이 괜히 나온 것이 아니다.

노호검객과 태을무정검.

장문인이고 나발이고, 먼저 입문한 사형이라는 이유로 풍운검군의 지시를 무시한 채 계속해서 나아가는 두 늙은 개를 향해 나는 지면을 박찼다.

슈확!

전신을 휘감는 광풍(狂風)과 함께 단번에 지워지는 수십여 장의 거리.

발걸음을 멈추지 않는 두 노도사의 뒷모습도, 그에 따라 양민들이 내지르는 비명도 가까워졌다.

그리고 바로 그 순간. 한 사람의 목소리가 나를 포함한 모두의 귓가를 파고들었다.

“멈춰.”

“……!”

“……!”

목에 힘을 주어 내지른 외침도, 별다른 공력도 실려 있지 않은 나직한 음성.

그러나 노호검객과 태을무정검의 발걸음을 묶기에는 그 한 마디만으로도 충분했다.

아니, 무엇보다 중요한 것은 그 말에 담긴 내용이 아니라 그 말을 한 누군가의 정체였다.

“네놈들은 귀가 먹었느냐? 어째, 쓸모없어 보이는데 이참에 하나 뜯어 줘?”

고작 몇 걸음 차이.

눈을 질끈 감은 어느 양민의 코앞에 멈춰 선 노호검객이 떨떠름한 얼굴로 입을 열었다.

“노 선배. 저는 그저 확인 차…….”

“물어본 것에나 대답해라. 떼 줘? 아니면 말아?”

“…….”

“귀만 먹은 줄 알았는데, 다시 보니 입까지 막혔군. 좋다. 몸이 불편한 사형 대신 네놈이 대신 대답해 보거라.”

불길이 일렁이는 눈동자.

그런 적천강의 시선을 마주한 태을무정검이 작게 고개를 숙였다.

“이들의 정체를 확실히 하고자 했을 뿐. 결코 다른 의도는 없었습니다. 만약 섣부른 행동으로 적 대협의 심기를 어지럽혔다면…….”

“어지럽히진 않았다. 대신 그보다 더 개판을 쳐놨지.”

“송구합니다.”

“그나마 한 놈은 주둥이라도 뚫려있군.”

태을무정검을 향해 눈살을 찌푸린 적천강이 작게 한숨을 내쉬었다.

“송구한 건 송구한 거고, 네놈들 때문에 지레 식겁한 저들에게나 사과해라.”

적천강의 말처럼, 발 빠른 몇몇과는 달리 미처 도망치지 못하고 제 자리에 얼어붙어 있던 양민들은 지금 이 순간에도 벌벌 떨고 있었다.

그리고 그중에서도 그나마 멀쩡해 보이는 한 사내가 서둘러 손을 내저었다.

“아이고, 괜찮습니다요. 워낙 급작스럽게 벌어진 일에 놀라기야 했지만…….”

노호검객과 태을무정검을 보며 말꼬리를 흐린 사내가, 적천강과 그 옆에 선 내게로 시선을 옮겼다.

“그, 맞으시지요? 무림맹의 협객분들.”

이 소란을 피워 놓고 협객이라고 하긴 민망하지만, 우선은 고개를 끄덕이자 사내는 물론이고 주위에 있던 양민들의 표정이 사르르 녹아내렸다.

“하이고. 십 년 감수했네.”

“무림맹이면, 그. 거기 아니오? 천인공노할 외적 놈들과 맞서 싸운다는.”

“거기 맞소. 사소한 오해가 있었던 모양이오.”

“염병. 난 또 뭐라고. 하마터면 죽는 줄 알았네.”

곳곳에서 안도의 한숨이 터져 나오던 그때, 가장 먼저 말을 꺼냈던 사내가 밝아진 안색으로 재차 입을 열었다.

“말로만 듣던 무림맹의 협객분들이시라니, 정말 천만다행입니다요. 저희는 웬 이상한 놈들이 나타나길래 그놈들인 줄 알…… 어이쿠. 또 이 주둥이가 방정이지. 이상한 놈들이라니.”

사내가 황급히 입을 틀어막았지만, 나나 적천강은 그런 말실수 따위에는 조금도 신경쓰지 않았다.

당장 누가 봐도 이상한 놈들이기도 했고, 그보다 더 중요한 말을 들었으니까.

“그놈들이라니, 그게 누굽니까?”

내 물음에, 사내가 망설임 없이 대답했다.

“누구긴 누굽니까요. 그 흉악하기 짝이 없는 마적단 놈들이지.”

뭐?
```

## Final English reading copy

```markdown
# Chapter 1001

Traveling with the Zhongnan Sect was decided all of a sudden.

Their Sect Leader, the Wind-and-Cloud Sword Lord, had proposed joining forces, and Jeok Cheongang had accepted before I could finish thinking it over.

“Traveling together, huh? That’s not a bad idea.”

“Old—no, Master.”

“What are you standing around for? Get your subordinates ready. And you too, Wind-and-Cloud Sword Lord—start by kicking those lazy disciples of yours in the ass.”

Just like that, all the preparations were finished in the blink of an eye.

Our party had swelled to around a thousand, rounding up a bit, and we set off toward Gansu. Among them were the Roaring Fury Swordsman and the Taeeul Merciless Sword, neither of whom looked particularly pleased.

“Those two have looked like they’re on their deathbeds for a while now. If we’d met them just six months earlier, no more, no less, I’d have cracked them across the jaw first thing.”

Jeok Cheongang smacked his lips as he muttered, and I clicked my tongue softly.

“If you couldn’t stand the sight of them, you shouldn’t have accepted the offer.”

“Is that why your lips are sticking out three inches?”

“Who said my lips were sticking out?”

“Correction. They’re sticking out four inches now.”

I shook my head at Jeok Cheongang’s teasing.

The one small upside was that we’d taken the rear, keeping a good thirty jang between us and the Zhongnan Sect. At least we could have this conversation without everyone hearing.

“Yes, I’m annoyed. Happy now?”

“Honestly, I can’t make heads or tails of you. If that’s how you feel, why bother making up when it was nothing but an empty gesture?”

An empty gesture.

There was no more and no less to it. It was exactly the right way to put it.

I’d already guessed that Jeok Cheongang had heard everything that had passed between us through Sound Transmission, so I answered without much surprise.

“Well, obviously…”

“Because we need to?”

“Right.”

“You make peace because you need to, then cover up old grudges with smiles, at least on the surface… You’ve grown up, haven’t you?”

There was something odd about his tone.

Not sure whether Jeok Cheongang was praising me or scolding me, I stared at him in silence. He gave a quiet laugh.

“Don’t overthink it. I’m just glad to see you’ve grown in one direction or another.”

“Do you think the direction you mentioned might be the wrong one?”

“Who can say? What matters is the outcome, doesn’t it?”

“Isn’t the process usually considered just as important as the outcome? Sometimes more important?”

“The first is what people say when they’re narrow-minded, and the second is bullshit people use when they’ve completely botched the outcome.”

Jeok Cheongang answered with cutting certainty, then went on.

“If I thought you’d done something wrong, I’d have given you a proper scolding. But so far, you haven’t done too badly. Besides, it might be nice to herd those lazy bastards all the way to Gansu like cattle.”

He wasn’t wrong. Even now, the Zhongnan Sect Disciples were running for their lives. It was all because of what Jeok Cheongang had declared before we set out, after unilaterally claiming the rear.

“From this moment until we reach Gansu, if any of you fall behind or try to slack off, this old man will personally have a private talk with you.”

A private lesson with an elder who’d reached a distant realm would be a fortuitous encounter anyone would pray for—unless the teacher was the Fire King. In that case, there was a good chance you’d become a dead man.

Whoosh, whoosh, whoosh!

Have you ever seen a pack of hyenas—or rather, Zhongnan Sect Disciples—race for their lives along a mountainside, desperate to survive?

I have.

Jeok Cheongang watched with satisfaction as the Zhongnan Sect Disciples ran with every last bit of strength they could squeeze out. Then, without warning, he kicked off the ground.

Boom! Whoooosh!

A sharp boom rang out as his figure stretched away in an instant.

Jeok Cheongang’s afterimage seemed to remain behind as he rapidly closed in. The Zhongnan Sect Disciples sucked in their breath, and panicked shouts rang out among them.

“Run!”

“If he catches us, we’re finished!”

“S-Senior Brother, I can’t go on. Don’t worry about this useless Junior Brother—just go on without me…”

“No! Don’t give up! We can survive!”

“……”

My thoughts on the scene were short and clear.

You’re all making a damn spectacle of yourselves.

“Anyone would think Dark Heaven had shown up or someth—huh?”

I clicked my tongue at the Zhongnan Sect Disciples fleeing like locusts from a wildfire. Then I spotted something and narrowed my eyes.

At the same time, I realized the real reason Jeok Cheongang had suddenly sped ahead.

*What’s that?*

We emerged from the narrow mountain path, and a hill opened up the view.

The problem was that, at the same time, a small village appeared in the distance, its hundred or so thatched cottages huddled together—and a crowd of people gathered around it.

At a glance, there had to be several hundred of them.

Hyuk Mujin, who’d spotted the crowd milling around the entrance to the little village a moment later, widened his eyes.

“Captain. Could that be…”

His urgent voice reached my ears.

Guessing what he was about to say, I answered a beat ahead of him.

“Don’t panic already. They don’t look like enemies.”

“Huh? Then…”

“They’re all civilians.”

I gave him a brief answer, thought for a moment, then added,

“At least, from what we can see right now.”

I added that because I wasn’t completely sure myself.

Judging by the route we’d taken, we were now somewhere along the border between Shaanxi and Gansu.

On top of that, Dark Heaven had the dark art known as the Moving Formation. It wouldn’t be all that surprising if we ran into people disguised as civilians here.

Dark Heaven had already disguised its people as government troops in Sichuan once before.

*If something had happened in Gansu, word would’ve reached us by now. So what’s this crowd doing in a tiny mountain village? Are they really preparing an ambush using a Moving Formation?*

Questions chased one another through my mind.

Then, all of a sudden, I heard a chilling sound.

Shing.

I turned and saw Sama Pyo. He’d drawn the Black Dragon Saber, the weapon that shared its name with his sobriquet.

“Whatever they are, there’s no harm in being prepared, is there, Pavilion Master?”

His voice was calm, but his eyes were dark and intent.

The closer we got to Gansu, the heavier the atmosphere around Sama Pyo had become. I quietly nodded and urged my horse on.

Thud, thud, thud, thud!

My grassland horse’s hooves thundered across the ground.

I didn’t know who the crowd waiting ahead of us really was, but one thing was certain.

*Even if Dark Heaven prepared an ambush, all we have to do is trample them and keep going.*

We might be headed into a fierce battle, but my heartbeat was no different from usual.

I’d become far too strong to be stopped in some mountain valley like this.

* * *

In the end, the disaster I’d feared never happened.

No—I should correct that.

It would be much more accurate to say that, at least for our side, it didn’t.

“They’re here! They’ve shown up!”

“Aaaah!”

“E-Everyone, get out of the way!”

It was only natural that urgent shouts and screams erupted all around us.

Nearly a thousand suspicious people came pouring over the steep hill, like water bursting through a broken embankment. Some of them already had gleaming blades in their hands. To the hundreds gathered around the entrance to the little village, it must have looked like a catastrophe.

At their very real reaction, the Wind-and-Cloud Sword Lord, racing at the head of the group alongside Jeok Cheongang, shouted like a thunderclap.

“Enough! Everyone, stop!”

Whoosh!

It was an order from none other than the Sect Leader.

At his shout, reinforced with internal energy, countless Zhongnan Sect Disciples quickly slowed and stopped where they were. But there were always exceptions.

Whoosh.

A faint rush of air, on a completely different trajectory from the rest.

Two figures shot forward like the wind, ignoring the Wind-and-Cloud Sword Lord’s command. I’d been slowing down along with the Zhongnan Sect Disciples, and I clicked my tongue to myself.

*Yeah. Somehow I knew they’d do that.*

They say old habits die hard for a reason.

The Roaring Fury Swordsman and the Taeeul Merciless Sword.

Those two old dogs kept going, disregarding the Wind-and-Cloud Sword Lord’s orders because he was their Junior Brother, Sect Leader or not. I kicked off the ground after them.

Whoosh!

A gale wrapped around me, and I covered dozens of jang in a single instant.

The backs of the two old Daoists, who hadn’t slowed their pace, came closer. So did the civilians’ screams.

And right then, one person’s voice reached the ears of everyone there, including me.

“Stop.”

“……!”

“……!”

It was a low voice, neither shouted with force nor backed by any particular internal energy.

But that one word was enough to stop the Roaring Fury Swordsman and the Taeeul Merciless Sword in their tracks.

More than anything, what mattered wasn’t what the word meant. It was who had said it.

“Are you deaf? You look useless enough already. Want me to rip one of your ears off while I’m at it?”

The Roaring Fury Swordsman had stopped only a few steps away from a civilian who stood frozen with his eyes squeezed shut. His face stiff, he began to speak.

“Senior, I was only trying to make sure…”

“Answer what I asked. Should I take it off or not?”

“……”

“I thought you were just deaf, but now it looks like your mouth’s been sealed shut too. Fine. You answer for your Senior Brother, who can’t manage it himself.”

Fire flickered in Jeok Cheongang’s eyes.

The Taeeul Merciless Sword met his gaze and bowed his head slightly.

“I only wanted to confirm who they were. I had no other intention. If my rash action upset you, Great Hero Jeok…”

“You didn’t upset me. You just made an even bigger mess.”

“I apologize.”

“At least one of you has a working mouth.”

Jeok Cheongang frowned at the Taeeul Merciless Sword, then let out a small sigh.

“Apologize to the people you scared half to death, not me.”

Just as Jeok Cheongang said, several civilians hadn’t managed to run away in time and were still trembling where they stood.

One man, who looked more or less all right, hurriedly waved his hands.

“Oh, it’s fine, sir. It all happened so suddenly that we were startled, but…”

The man trailed off as he looked at the Roaring Fury Swordsman and the Taeeul Merciless Sword, then shifted his gaze to Jeok Cheongang and me.

“Y-You’re… the heroes of the Murim Alliance, aren’t you?”

It was hard to call ourselves heroes after causing such a commotion, but I nodded anyway. The man’s expression—and those of the civilians around him—softened at once.

“Good grief. That took ten years off my life.”

“The Murim Alliance… Isn’t that the place fighting those wicked foreign invaders?”

“That’s right. There seems to have been a little misunderstanding.”

“Damn it. I thought we were done for.”

Just as sighs of relief rose from all sides, the man who’d spoken first brightened and continued.

“To think you’re the heroes of the Murim Alliance we’ve heard so much about. What a relief. We saw a bunch of strange-looking people show up and thought they were the ones… Whoops. There I go, running my mouth again. Calling you strange-looking…”

The man hurriedly clapped a hand over his mouth, but neither Jeok Cheongang nor I cared about that slip of the tongue.

Anyone could see they looked strange. More importantly, he’d said something else.

“Who did you think they were?”

The man answered without hesitation.

“Who else? That vicious gang of mounted bandits.”

What?
```
