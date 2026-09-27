<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1130.txt",
      "sha256": "38727fe447d953ccf66719099ff1b2f3e1881beb7555506669f05915d4e66568",
      "bytes": 11909
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "fe2ceebeb6d836aae9679fa833df783526ca204bc66f561249c22be9455c31e9",
      "bytes": 752
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "307189767337c5394589bdcaa7f59f3e28cdf1da9d380fecae4d63447025be4b",
      "bytes": 245178
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "0df89ad6dccbef9d2e0b314b0ccd822b67438e132e9c29ff52a51e87ecc607fb",
      "bytes": 844
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "a15a3d74bd9308c04d376a997ef7ff2a6e32a704f081055f66c5bcd2a677cedc",
      "bytes": 760
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "db43448c791c9e85e6b48b9cbac22509d74b5c93efc98eb433a7c907063ac4c3",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "11b07fc26f3c041490e6daf29b3a564f2e24a42cf95001afa4fbeb680b99bbfd",
      "bytes": 623
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "a5d3d61e2339d630995f6a706169bc5f6be7b39afba1c4ffd564f089037b1146",
      "bytes": 290077
    }
  ],
  "estimated_tokens": 8854
}
-->

# Durable State Update — Chapter 1130

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
1 and safe_through 1130. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1130. Profile updates may replace only one
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
  "chapter": 1130,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1130,
    "continuity_sources": [1130],
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
    "Taekyung awakens in a boundless gray-white space after his apparent death.",
    "An unidentified old man can read Taekyung’s thoughts and says he has already helped him, but does not explain how.",
    "Taekyung retains his internal energy and martial techniques in the gray-white space.",
    "The old man attacks Taekyung and gives him a spear; their fight begins."
  ],
  "continuity_sources": [
    1129
  ],
  "open_questions": [
    "Who is the old man, and has he met Taekyung before?",
    "How did the old man help Taekyung, and what does he intend to begin?",
    "What is the gray-white space, and what happens to Taekyung there?"
  ],
  "safe_through": 1129,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 암천     | **Dark Heaven**                  |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 살기     | **killing intent**                               |                                                       |
| 일격     | **One Strike**                         |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 평화 | **Peace Guild** | Guild name. |
| 나려타곤 | **Narye tagon** | Humiliating idiom comparing a fighter's evasive roll to a lazy donkey rolling on the ground. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 공수납백인 | **Empty-Hand Seizes the Blade** | Technique for catching an opponent's weapon between bare fingers. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 허초 | **feint** | Deceptive attack Jongni Chu says he used against Cheongpung. |
| 염화일로 | **Flamefire Path** | Fire Gate Clan signature movement technique; Jeok Cheongang has reached its ninth stage. |
| 절체절명 | **Life-or-Death Crisis** | Sudden System Quest forcibly accepted during the confrontation at Mount Song. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |
| 재생 | **Regeneration** | The masked man's rapid recovery from shattered bones and severe wounds. |
| 천수 | **Tianshui** | City on Gansu’s eastern edge, bordering Shaanxi. |
| 미친놈 | **Madman** | Insult Great Sir adopts as a name; also appears in the System display. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 혈주 | hostile_opponent_to_hostile_opponent | you; you son of a bitch | insulting-casual | Taekyung insults the Blood Lord while challenging his claim that he will kill him. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1127
- **Aliases:** None
- **Role:** Deceased young-seeming high-ranking Dark Heaven figure who claimed command of its army after killing the Grand Mage.
- **Personality:** Cunning and controlling, he trusts his overwhelming power and relishes opponents who survive and resist him; he resents the Lord of Heaven’s attention to Taekyung and rationalizes his intended murder as loyalty, yet believes his choice is right.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He served the Lord of Heaven, killed the Grand Mage, and died after Jin Taekyung defeated him; at death, he recognized that the Lord had never valued his loyalty.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1127
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1128
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1128
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃1130화



빛은 밝히기 위해 존재하는 것만이 아니다.

때로는 모든 것을 지우고, 잊게 해 준다.

바로 지금 이 순간, 진태경의 시야를 새하얗게 뒤덮으며 날아드는 빛줄기처럼.

쉬이이이잉!

부풀어 오르는 섬광 속, 진태경의 눈빛이 깊게 가라앉았다.

일체의 잡념이나 의문 따위는 이미 머릿속에서 깨끗이 비웠다.

아니, 비울 수밖에 없었다.

어느덧 수십여 개로 나뉜 빛줄기가 살아 있는 것처럼 꿈틀거리며 전신의 요혈(要血)을 노리고 있었으니까.

‘허초(空招)가 아니다.’

동시에 본능적으로 느낄 수 있었다.

실체를 지닌 저 섬광 하나하나에, 지금껏 겪어 본 적 없는 무시무시한 파괴력이 담겨 있음을.

그러나 진태경이 내린 선택은, 후퇴가 아닌 전진이었다.

화륵, 쾅!

힘주어 뻗은 발끝을 따라 흐르는 화염.

한껏 자세를 낮춘 채, 빗발치는 섬광을 아슬아슬하게 피하며 쏘아지는 그의 모습을 본 노인이 고개를 끄덕였다.

“염화일로(炎火一路)라, 확실히 싸울 줄 아는군.”

그리고 이와 같은 노인의 칭찬에, 진태경은 자신만의 방식으로 대답했다.

스륵.

삽시간에 좁혀지는 공간 너머, 노인을 향해 나아가던 창이 잔상(殘像)에 휩싸여 파도치듯 일렁였다.

마치 거대한 용의 꼬리처럼.

화아악!

창날을 따라 피어오르는 군청색의 불길.

앞서 노인이 펼친 한 수와 같이, 단숨에 수십 개로 분화(分火)한 화염이 공간을 뒤덮으며 들이닥쳤다.

콰아아아!

유황불이 들끓는 지옥이 실재한다면 이런 광경일까.

하지만 용암과도 같은 그 끔찍한 열기 앞에서도, 평온하게 가라앉은 노인의 눈동자는 조금도 흔들리지 않았다.

절체절명의 위기 속, 창날을 향해 마주쳐가는 그의 양손 역시도.

콰드드득!

일순간, 진태경은 눈을 부릅떴다.

합장(合掌)하듯 그러모은 노인의 손바닥 사이로, 부르르 떨고 있는 창날이 그의 동공에 비치고 있었다.

“……어떻게?”

자신도 모르게 입 밖으로 튀어나온 의문.

그러나 단 한 번의 합장과 함께 자신을 향한 모든 화염을 날려 보낸 노인은, 되려 어리둥절한 표정으로 대답했다.

“응? 그냥 붙잡은 건데.”

“……!”

“그건 그렇고, 이번엔 더 뜨끈한 것으로 해 보게. 모처럼 노곤해지는 기분이라 썩 괜찮군.”

진태경은 문득 눈앞이 어지러워지는 것을 느꼈다.

전력을 다한 일격을 공수납백인(空手納白刃)으로 막아 낸 것부터가 미친놈인데, 이제는 강철마저도 녹여 버리는 수 갑자의 열양지기를 온천수 취급하다니.

‘뭐 이런 늙은이가 다 있지?’

지금껏 싸웠던 상대 중 가장 강했던 혈주(血主)조차도 이 정도는 아니었다.

아니, 턱없이 못 미쳤다.

혈주는 핏물을 원료로 삼아 재생에 가까운 회복력과 끝없는 공력을 손에 넣었지만, 그 무시무시한 권능에도 결국 한계는 있었으니까.

하지만 노인은 아니었다.

혈주와는 타고난 결이, 격이 달랐다.

인적 드문 호수처럼 잔잔한 눈빛에는 별다른 살의(殺意)조차도 느껴지지 않았으나, 단지 마주하는 것만으로도 전신을 얼어붙게 만드는 무언가가 있었다.

마치, 아무리 발버둥 쳐도 넘을 수 없는 거대한 벽을 마주한 듯한 느낌.

그리고 진태경의 뇌리를 스친 그 짧은 생각을, 노인은 또렷하게 들여다보고 있었다.

“머릿속에 잡념(雜念)이 그득한 것을 보아하니, 아직 살 만한 모양이군. 그렇다면…….”

그 순간.

파창!

붙잡혀 있던 창날이 산산이 부서지는 동시에, 부드럽게 나아간 노인의 손바닥이 진태경의 가슴에 닿았다.

퍼엉!

몸속 깊은 곳에서부터 울려 퍼지는 폭발음.

진태경은 눈앞을 새하얗게 물들이는 격통을 느끼며 한쪽 무릎을 꿇었다.

동시에 이명(耳鳴)으로 가득 찬 귓가를 유독 선명히 울리는, 노인의 속삭임을 들었다.

“그 잡념, 다시 비워 주지.”

“……!”

진태경에게는 뭐라 대답할 시간도, 고통을 가라앉힐 여유도 주어지지 않았다.

정확히는, 노인이 기다려 주지 않았다.

후웅!

묵직한 파공성과 함께 정수리 위로 떨어져 내리는 거대한 기운.

고통조차 잊게 만드는 그 무시무시한 기파(氣波)에, 진태경은 생각할 겨를도 없이 옆으로 몸을 굴렸다.

콰아아아앙!

하늘이 쪼개지는 듯한 굉음에 이어 들이닥친 충격파가 사방을 휩쓸었다.

붕 뜬 듯한 감각과 함께 저 멀리 나가떨어진 진태경의 등 뒤로, 순식간에 십여 장의 공간을 가로지른 노인이 모습을 드러냈다.

“좋은 판단이었어. 나려타곤(懶驢打滾)을 펼치지 않았다면 그대로 끝났을 테니.”

평소의 진태경이었다면, 눈앞의 적이 그 누구라 할지라도 말했을 것이다.

아가리 닥치라고.

하지만 이번만큼은 달랐다.

노인을 상대하기 위해서는 단 한 번의 심호흡조차, 티끌만 한 잡념조차 크나큰 사치라는 것을 그는 다시금 온몸으로 깨닫고 있었다.

“그 간단한 걸 이제야 알았나?”

……저 정체 모를 늙은이가 마음을 훤히 들여다보는 한, 지금 같은 이 빌어먹을 상황에서 영영 벗어날 수 없으리라는 사실도 함께.

“오, 이건 아주 큰 깨달음이로군. 그럼 이제 어쩔 셈인가?”

노인의 흥미로운 눈빛을 마주하며, 진태경은 자루만 남은 창을 지팡이 삼아 몸을 일으켜 세웠다.

천천히, 동시에 신중히.

그리고 마침내 두 다리로 우뚝 섰을 때, 그는 답을 찾을 수 있었다.

스륵.

불현듯 감기는 두 눈.

미친 짓이라는 생각도, 혹시 모를 두려움도 잠깐뿐이었다.

파르르 떨리던 눈꺼풀은 곧 미동도 하지 않게 되었고, 이미 어둡게 물든 시야는 눈으로부터 전달되던 정보를 차단했다.

그렇게, 진태경은 중요한 한 가지를 버림으로써 새로운 것을 얻을 수 있었다.

앞서 벌어졌던 암천과의 격전 속에서 미처 끝맺어지지 못했던 깨달음의 끈을.

또한 지금 이 상황을 타개할 수 있는 유일한 방법을.

그리고 이와 같은 진태경의 모습에, 노인은 다시 한번 흐릿한 미소를 베어 물었다.

“그래, 응당 이래야지.”

그 순간.

팟.

마치 약속이라도 한 듯, 청년과 노인은 서로를 향해 쏘아졌다.

화륵, 콰아앙!

진태경은 홀린 듯이 멸염신권(滅炎神拳)을 내뻗었다.

천년 거석마저 녹여 낼 듯한 열기가 회백색 공간을 휩쓸었지만, 그는 이미 알고 있었다.

더불어 느끼고 있었다.

노인은 이미 그곳에 존재하지 않는다는 것을.

소리마저 앞지른 속도로, 자신의 사각(斜角)을 파고드는 중이라는 사실을.

퍼엉!

진태경은 벼락처럼 신형을 비틀었다. 강맹하기 그지없는 한 줄기의 장력(掌力)이 조금 전 그의 머리가 있던 허공을 후려쳤다.

“훨씬 낫군.”

암전(暗轉)된 시야 속, 진태경은 쉴 새 없이 사방을 덮쳐 오는 노인의 공격들을 가까스로 피해 내며 호흡을 삼켰다.

기분 탓일까.

그 무엇보다 선명하던 노인의 목소리는. 어느덧 메아리보다 멀고 작게 들려오고 있었다.

“아직 들린다는 것이, 부족하다는 증거지.”

맞다. 그럴지도 모른다.

새삼스러운 일은 아니었다.

지금껏 늘 그래 왔으니까.

힘이 부족했기에 모두를 지키지 못했고, 그로 인한 죄책감과 불안감으로 깊은 밤마다 악몽을 꾸고는 했다.

그렇게 바람 앞의 촛불처럼 위태롭게 흔들리다, 이내 힘없이 사그라지고 말았다.

“허나, 그것은 욕심이다. 인간은 완전무결해질 수 없으니.”

진태경 역시 알고 있었다.

하지만 설령 욕심이 아닌 탐욕이라 할지라도 상관없었다.

그저 누군가를 살리고, 그 자신도 살고 싶었을 뿐이었다.

단지, 보다 평화로운 세상에서 소중한 이들과 함께 살아가고 싶었다.

“모두가 그것을 꿈꾸지. 비록 현실은 잔인하지만.”

노인은 담담한 음성과 달리 계속해서 진태경을 압박했다.

채찍처럼 휘어지는 발끝이, 비스듬히 내리긋는 수도(手刀)가, 부드럽게 내뻗은 손바닥이 모두 검이요 창이었다.

그 한 수, 한 수에 진득한 살기 따위는 담겨 있지 않았으나, 육신뿐만 아니라 영혼마저 소멸시킬 듯한 기운으로 넘쳐흘렀다.

“혹시 모르지. 이대로 완전한 안식에 드는 것이, 자네에게는 좋은 일일지도.”

그 순간이었다.

연거푸 물러서던 진태경의 발걸음이 못 박힌 듯 멈춰 선 것은.

콰아아앙!

허공에서 부딪히는 두 개의 주먹.

도무지 나이를 짐작할 수 없을 만큼 주름진 노인의 일권(一拳)에는 감히 항거하기 힘들 만큼 거대한 힘이 담겨 있었지만, 진태경은 서서히 밀려 나가는 발끝을 힘주어 버텨 냈다.

“지금 그 말, 무슨 뜻이지?”

악물린 잇새 사이로 흘러나온 진태경의 물음에, 노인이 침착한 어조로 대꾸했다.

“글쎄, 무슨 뜻이라고 생각하나?”

“……설마.”

“이미 아는 것 같으니 다행이군. 더는 시간이 없으니 이쯤에서 결정짓도록 하세.”

뜻 모를 통보에 진태경이 반문하려던 그때, 힘이 더해진 노인의 주먹이 그를 밀어 냈다.

꽈앙!

포탄처럼 튕겨 나가는 신형. 

그리고 허공에서 가까스로 균형을 되찾은 진태경은, 지면에 착지함과 동시에 자신을 둘러싼 공간의 울림을 느꼈다.

우우웅.

보이지 않는다. 하지만 그려진다.

저 멀리, 자신을 향해 겨누어진 무형(無形)의 검이.

날붙이 따위가 아닌, 오직 기운으로 이루어진 그것을 쥔 노인의 모습이.

“피해 보게. 만약 피할 수 없다면…… 여기까지인 거겠지.”

그 말에 담긴 의미를, 진태경은 더는 묻지 못했다.

아니, 감히 눈을 뜰 수조차 없었다.

간신히 부여잡은 지금의 이 감각을 잠시라도 잃는다면, 야트막한 잡념이라도 끼어든다면 전신이 조각날 것만 같은 기분이 들었으니까.

그리고 그 판단은 옳았다.

고오오옹.

일순간, 천천히 들어 올려지는 노인의 두 손을 따라 회백색 공간이 몸을 떨었다. 

동시에 진태경의 칠흑 같은 시야 속 어딘가에서부터, 희미한 빛줄기가 흘러들어왔다.

‘이건, 뭐지?’

지금껏 단 한 번도 느껴본 적 없는 감각.

정확히는 세 가지의 공력을 합친 뒤에서야 매우 드물게 찾아왔던, 그렇게 잠시 머물다 흐릿해졌던 감각이었다.

이성 따위는 존재하지 않는, 그야말로 본능의 영역.

머리가 명령을 내리기 전에 몸이 먼저 움직이는, 아니 그 너머에 존재하는 또 다른 영역.

여섯 번째 감각과 맞닿은 그것이 진태경의 정신을 지배하고 있었다.

마침내 노인의 손끝을 따라 내리그어진, 무형의 검을 똑바로 직시한 채.

스아아악!

마치 온 세상이 갈라지는 듯한 절삭음이 울려 퍼진 그 순간.

화아악.

진태경은 보았다.

깊은 밤처럼 어두운 그의 시야를 밝히는, 한 줄기의 빛을.

그리고 동시에, 홀린 듯이 걸음을 내디뎠다.

서걱!
```

## Final English reading copy

```markdown
# Chapter 1130

Light doesn’t exist only to illuminate.

Sometimes it wipes everything away and lets you forget.

Just like the beam of light flying toward Jin Taekyung at this very moment, covering his vision in pure white.

Whoooooosh!

As the flash swelled, Jin Taekyung’s gaze sank low.

He cleared every stray thought and question from his mind.

No—he had no choice.

Dozens of beams had split off and were writhing as if alive, aiming for the vital points all over his body.

*It’s no feint.*

He could feel it instinctively.

Every one of those solid beams held terrifying destructive power unlike anything he’d ever experienced.

But Jin Taekyung chose to advance, not retreat.

Fwoosh—BOOM!

Flames streamed along his feet as he thrust them forward.

Keeping low, he darted through the downpour of flashes, narrowly evading them. The old man watched him and nodded.

“The Flamefire Path. You certainly know how to fight.”

Jin Taekyung answered the old man’s praise in his own way.

Ssshh.

Across the space closing in an instant, his spear surged toward the old man, engulfed in afterimages and rippling like a wave.

Like the tail of a colossal dragon.

Whoooosh!

Indigo flames blossomed along the spearhead.

Just like the old man’s move moments earlier, the flames split into dozens in an instant, blanketing the space as they surged forward.

KWA-BOOM!

If a hell where sulfurous flames boiled were real, would it look like this?

Yet even before that awful, lava-like heat, the old man’s calm eyes didn’t waver in the slightest.

Nor did his hands as he brought them together to meet the spearhead amid that life-or-death crisis.

Crack!

For an instant, Jin Taekyung’s eyes flew wide.

Between the old man’s palms, pressed together as if in prayer, the spearhead trembled. Jin Taekyung saw it in his own eyes.

“……How?”

The question slipped out before he knew it.

But the old man had blown away every flame aimed at him with a single joining of his palms. He answered with a puzzled expression.

“Hm? I just grabbed it.”

“……!”

“Anyway, try something hotter this time. This is making me pleasantly drowsy. Not bad.”

Jin Taekyung felt his vision swim.

The old man was already a madman for stopping his full-power strike with Empty-Hand Seizes the Blade. And now he was treating several jiazi of Scorching Yang Qi—hot enough to melt steel—as if it were hot spring water.

*What kind of old man is this?*

Even the Blood Lord, the strongest opponent he’d faced until now, hadn’t come close.

Not even remotely.

The Blood Lord had used blood as a source to gain near-Regeneration and endless internal energy. But even that terrifying power had its limits.

The old man was different.

His very nature, his level, was different from the Blood Lord’s.

There was no particular killing intent in his eyes, as tranquil as a secluded lake. Yet something about him froze Jin Taekyung from head to toe just by being there.

It felt like facing an enormous wall he could never climb, no matter how desperately he struggled.

And the old man was looking straight into that brief thought that had flashed through Jin Taekyung’s mind.

“Your head’s full of stray thoughts. You must still have some life left in you. In that case……”

At that moment—

CRASH!

The spearhead in the old man’s grasp shattered to pieces, and his palm glided forward to touch Jin Taekyung’s chest.

BOOM!

An explosion rang out from deep within his body.

Jin Taekyung dropped to one knee, pain bleaching his vision white.

At the same time, amid the ringing in his ears, the old man’s whisper came through with unnerving clarity.

“I’ll clear those stray thoughts away for you again.”

“……!”

Jin Taekyung wasn’t given time to answer—or even to steady himself against the pain.

More precisely, the old man didn’t wait.

Whoosh!

A massive force descended toward his crown, accompanied by a heavy rush of air.

The energy wave was so terrifying it made him forget even the pain. Jin Taekyung rolled to the side without time to think.

KWA-BOOM!

A shock wave swept the surroundings after a roar like the sky splitting apart.

Jin Taekyung felt himself thrown far away, as if weightless. Behind him, the old man appeared, having crossed more than ten jang in an instant.

“That was a good decision. If you hadn’t used Narye tagon, it would’ve been over right there.”

Normally, Jin Taekyung would have told any enemy standing before him to shut the hell up.

But this time was different.

His whole body had reminded him that facing the old man made even a single deep breath—or the smallest stray thought—a luxury he couldn’t afford.

“You only just figured out something that simple?”

……And that so long as this mysterious old man could see right through his mind, he’d never escape this damned situation.

“Oh, that’s quite an insight. So what will you do now?”

Meeting the old man’s interested gaze, Jin Taekyung used the spear, now nothing but a shaft, as a cane to get back to his feet.

Slowly, and carefully.

And when he finally stood upright on both legs, he found his answer.

Ssshh.

His eyes closed without warning.

The thought that it was madness, the fear of what might happen—both lasted only a moment.

His trembling eyelids soon grew still. His vision was already dark, shutting out the information his eyes had been sending him.

By giving up one important thing, Jin Taekyung had gained something new.

The thread of enlightenment left unfinished during the fierce battle against Dark Heaven.

And the only way to overcome the situation he was in now.

Seeing Jin Taekyung like this, the old man once again wore a faint smile.

“Yes. That’s how it should be.”

At that moment—

Pop.

As if on cue, the young man and the old man shot toward each other.

Fwoosh—BOOM!

As if entranced, Jin Taekyung thrust out the Flame-Extinguishing Divine Fist.

Heat that seemed capable of melting even a thousand-year-old boulder swept through the gray-white space. But he already knew.

He could feel it, too.

The old man was no longer where he’d been.

He was moving faster than sound, slipping into Jin Taekyung’s blind spot.

BOOM!

Jin Taekyung twisted like lightning. A powerful palm strike slammed through the air where his head had been a moment earlier.

“Much better.”

In the darkness of his vision, Jin Taekyung barely dodged the old man’s attacks as they kept closing in from every direction, swallowing a breath.

Was it just his imagination?

The old man’s voice, once clearer than anything else, had grown more distant and faint than an echo.

“The fact that you can still hear me means you’re not there yet.”

He was right. Maybe.

It wasn’t anything new.

It had always been like this.

He hadn’t been strong enough to protect everyone, and the guilt and anxiety that followed had given him nightmares deep into the night.

He’d wavered like a candle in the wind, then finally gone out without a fight.

“But that is greed. Humans cannot become perfect.”

Jin Taekyung knew that, too.

But even if it wasn’t mere desire but greed, he didn’t care.

He’d only wanted to save someone—and to live himself.

He’d simply wanted to live in a more peaceful world, together with the people he cherished.

“Everyone dreams of that, though reality is cruel.”

Despite his calm voice, the old man kept pressing Jin Taekyung.

A foot that bent like a whip, a hand blade that slashed diagonally, a palm that thrust forward smoothly—all were swords and spears.

None of those moves carried any deep killing intent, yet each overflowed with an energy that seemed capable of erasing not just his body but his very soul.

“Who knows? Perhaps entering perfect rest just like this would be a good thing for you.”

That was when it happened.

Jin Taekyung’s retreating steps came to a sudden stop, as if nailed to the ground.

KWA-BOOM!

Two fists collided in midair.

The impossibly wrinkled old man’s fist carried a force almost too great to withstand, but Jin Taekyung braced himself even as his feet slowly slid back.

“What do you mean by that?”

The old man answered Jin Taekyung’s question, forced out between clenched teeth, in a calm voice.

“Tell me. What do you think I mean?”

“……You can’t be saying—”

“Good. It seems you already know. We’re out of time, so let’s settle this now.”

Just as Jin Taekyung was about to ask what he meant, the old man’s fist gathered more force and shoved him away.

KWA-BOOM!

His body shot backward like a cannonball.

Jin Taekyung barely regained his balance in midair. The moment he landed, he felt the space around him resonate.

Hmmm.

He couldn’t see it. But he could picture it.

Far away, an invisible sword pointed straight at him.

The old man holding it—not a blade, but something made entirely of energy.

“Try to dodge it. If you can’t…… then this is as far as you go.”

Jin Taekyung couldn’t ask what the words meant.

No—he couldn’t even bring himself to open his eyes.

He felt that if he lost the sensation he’d barely managed to grasp, even for an instant, or if the slightest stray thought crept in, his whole body would be torn to pieces.

And that judgment was right.

Gooooong.

The gray-white space trembled as the old man’s hands slowly rose.

At the same time, a faint beam of light flowed into some corner of Jin Taekyung’s pitch-black vision.

*What is this?*

A sensation he’d never felt before.

Or rather, it had come to him only very rarely after he combined three forms of internal energy, lingering briefly before fading.

It belonged to a realm where reason didn’t exist—pure instinct.

A realm where the body moved before the mind could give an order. No, somewhere beyond that.

It was taking hold of Jin Taekyung’s mind, touching on the sixth sense.

At last, he stared straight at the invisible sword slashing down from the old man’s fingertips.

Sssshing!

At the instant a sound like the whole world splitting apart rang out—

Whoooosh.

Jin Taekyung saw it.

A single beam of light, brightening his vision as dark as the deep night.

And at the same time, he stepped forward as if entranced.

Shhk!
```
