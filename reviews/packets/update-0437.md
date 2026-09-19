<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0437.txt",
      "sha256": "0e94316a6d77b04c6ea69b064419d449267f0517c45cfbdded4cfdb7fb897b85",
      "bytes": 13433
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "340ca7766638a04f435b59ddb9b23cb653c6b7e1ebaf100b24aeb544ded10b24",
      "bytes": 1826
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "945ce754f100dc7a8d502c6552abbe3da5c467344da56039829bdf7199b57504",
      "bytes": 142897
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "ba6e917ebf20d351d996df61bcbdca5eeac22c66a3db19837ef26f9173ef8a4a",
      "bytes": 533
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "a0df94ac450ef18b8698b7de4f7217ffb5b8a0af3079c3bcb8c4ef81d59f4127",
      "bytes": 1416
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "121716fb3539abefa588b3762de546d4de167bf5cdc94cfbe81de86418d92293",
      "bytes": 1239
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "bf7f6e20ece56290ba4f0f4cf0dd4c5797dc3848ff7ef47c6eb573945804c118",
      "bytes": 622
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "f8613ac4aca713a17ac23c3cc58430a58e0b16988629ecd6aa212d77832a336b",
      "bytes": 666
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "bc8c79344a1b13062844571c7a4109b2beefc98822e0698ed6958d88115245bb",
      "bytes": 136527
    }
  ],
  "estimated_tokens": 10314
}
-->

# Durable State Update — Chapter 437

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 437. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 437. Profile updates may replace only one
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
  "chapter": 437,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 437,
    "continuity_sources": [437],
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
    "Mungyeong's Slaughter Saint identity remains concealed beneath his medical-apprentice persona, though Jeok Cheongang recognizes it.",
    "Mungyeong continues traveling with Jin Taekyung's group without understanding why he feels compelled to remain with them.",
    "Jin Taekyung has opened his Middle Dantian, and Jeok Cheongang knows about it.",
    "Taekyung's recent martial insight requires Jeok's instruction, and he intends to investigate mysterious patterns and symbols found in both worlds.",
    "The group will travel by water only as far as Sichuan, with Mu Song offering to escort them with his subordinates.",
    "Jin Wikyung is withholding an important matter for a later private discussion.",
    "Cheongpung has secured a planned stop at Guang'an for more dumplings by invoking Mae Jonghak's supposed instruction."
  ],
  "continuity_sources": [
    436,
    435
  ],
  "open_questions": [
    "Why does Mungyeong continue accompanying Jin Taekyung's group despite being unable to explain the impulse?",
    "How did Jin Taekyung open his Middle Dantian?",
    "What confidential matter is Jin Wikyung withholding?",
    "Are Taekyung's suspicions about the mysterious patterns and symbols found in both worlds correct?"
  ],
  "safe_through": 436,
  "temporary_decisions": [
    "Render 노야 as “Old Master” and 스승님 as “Master” for Taekyung's address to Jeok Cheongang.",
    "Keep Mungyeong's medical-apprentice voice polite and concerned, while his Slaughter Saint voice remains terse and threatening.",
    "Preserve the established renderings Middle Dantian, Slaughter Saint, Three Saints, Water Dragon Stronghold, and Guang'an.",
    "Retain the chapter's strong profanity and Taekyung's vulgar slang in confrontational dialogue."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 살성     | **Slaughter Saint**           | —              |
| 소림     | **Shaolin**                      |
| 무당파    | **Wudang**                       |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 기연     | **fortuitous encounter**                         | Use sparingly                                         |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 제자     | **Disciple**                                 |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 대사      | **Master** for a senior Buddhist monk                           |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 명문혈 | **Mingmen acupoint** | Acupoint into which Jeok Cheongang sends internal energy while treating Hong Dao. |
| 절체절명 | **Life-or-Death Crisis** | Sudden System Quest forcibly accepted during the confrontation at Mount Song. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 문경 | young_martial_artist_to_medical_apprentice | Young Hero | formal-polite | Taekyung addresses the non-martial Mungyeong as 소협 while praising his actions. |
| 문경 | 진태경 | young_passenger_to_younger_martial_artist | Young Hero | deferential | Mungyeong uses 소협 while asking Taekyung for help boarding the ship. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 435
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who has sworn never to kill again.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 435
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, and can perceive the texture of qi well enough to sever layered magic.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and student, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 436
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm, authoritative, and politically capable in public; protective and affectionate toward Taekyung beneath a stern mask. Takes responsibility for his people, acts decisively under pressure, and prioritizes family survival.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Taekyung's eldest brother and future Family Head; Taekyung trusts him as a martial-arts mentor and family protector. Member and acting leader of the Jin Family of Taiyuan. Commands Wipeng and the family's forces. Has worked with Jeok Cheongang, who trained Taekyung under Wikyung's arrangement. Jin Mukyung is his younger brother and a potential successor alongside Taekyung.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 435
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 436
- **Aliases:** None
- **Role:** Mungyeong is the legendary physician known as the Divine Physician and former Slaughter Saint, and he has sworn never to kill again.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, while Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

## Korean source

```text
＃437화



쾌조선은 이름에서 알 수 있듯이 속도를 우선시하여 만들어진 배다.

체급으로 따졌을 때 일반 전투선이 헤비급이라면, 쾌조선은 그보다 아래인 웰터급 정도?

그렇다 보니 선체의 크기는 그리 크지 않았고, 그건 남들의 눈을 피해 있을 만한 곳이 딱히 없다는 뜻이었다.

“어이쿠.”

“진 대협. 이곳에는 어쩐 일로 오셨습니까요?”

선체 후미에서 경계를 빙자한 농땡이를 피우던 수적 두 명이 나를 알아보고 허리를 굽실거렸다.

나는 근엄하게 고개를 끄덕이며 입을 열었다.

“살려…….”

그 순간, 뾰족한 무언가가 등허리의 명문혈을 쿡 찔렀다.

“살려, 펴 가세요.”

“예?”

“살펴 가시라고. 잠깐 이 친구랑 나눌 이야기가 있어서.”

“아, 그러시군요.”

안 돼. 수긍하지 마. 제발 의심해 줘.

나는 있는 힘껏 부릅뜬 눈으로 옆구리에 바짝 붙어 있는 문경을 곁눈질하며 말을 이었다.

“꼭! 살펴 가세요! 누가 나에 대해 물어보면 문경이랑 함께 있다고 알려 주고!”

“어. 알겠습니다요.”

“아니, 알겠다가 아니라. 그렇지! 내 스승님! 스승님께서 날 찾으시면…….”

“그럴 일은 없을 것 같군요.”

문경이 맑게 웃으며 내 말을 잘라먹었다.

“진위경 대협과 긴히 나눌 이야기가 있으신 것 같던데. 여하간 저희는 잠시 진료를 보러 온 참이니 신경 쓰지 마시고 가십시오. 선실에서 쉬고 계시면 후에 알려 드리겠습니다.”

“그럼 우리야 좋지.”

지루한 경계 근무 중에 합법적 농땡이만큼 달달한 게 없다.

덕분에 시원한 그늘 아래에서 꿀을 빨게 된 수적들은 웃으며 자리를 떴고, 내가 마지막 희망을 담아 날리려던 전음은 문경의 한마디에 가로막혔다.

“목숨이 서너 개쯤 되나 보지?”

“…….”

“두 가지 선택지가 있다. 지금부터 노부가 묻는 모든 말에 순순히 답하거나, 원치 않다면 조용히 입을 다무는 것.”

나는 혹시나 하는 마음을 물었다.

“두 번째 선택지를 고르면 어떻게 됩니까?”

“호북으로 가게 될 거다.”

“그거 괜찮…….”

막 대답하려던 찰나, 문경이 담담하게 말을 이었다.

“장강 밑바닥에 가라앉은 채로 호북까지 떠내려가겠지. 조용히.”

“……살생 끊으셨다고 하셨던 것 같은데.”

“그것은 노부의 의지에 달린 것. 네가 상관할 바가 아니다.”

아니 시벌, 무슨 금연하는 것도 아니고…….

어이가 없어진 내가 재차 따졌다.

“신의씩이나 되시는 분이 살해 협박을 하세요?”

“전(前) 신의다. 그 이름은 이미 제자에게 물려준 지 오래고. 그래서 대답은?”

나는 문경을 노려보았다.

“제가 이 정도의 협박에 굴할 것 같습니까?”

“물론.”

“정확히 보셨군요. 모든 질문에 성심성의껏 답하겠습니다.”

“…….”

순간 할 말을 잃었는지 답이 없던 문경이 침묵 끝에 입을 열었다.

“별 희한한 놈을 다 보겠군.”

“남들이 보기에는 피차일반일 것 같은데요. 전 무림을 대상으로 전서구 설문 조사 돌려보세요. 누가 더 이상한 놈인지.”

“놈?”

“혀가 꼬였네요. 죄송합니다.”

문경이 흘려보내는 기세에 전신의 피부가 곤두선다.

마른침을 꿀꺽 삼키는 나를 말 없이 바라보던 문경이 한마디를 툭 내뱉었다.

“중단전(中丹田).”

“예?”

“며칠 전, 아니 한나절 전만 하더라도 네 중단전은 닫혀 있었다. 한데 무슨 술수를 부렸기에 하룻밤 사이 그와 같은 대공(大功)을 이룬 것이냐.”

이거였구나. 나를 따로 불러낸 이유가.

‘눈치챘다는 건 알고 있었지만.’

무공의 경지는 완벽한 수직 구조다.

이는 높은 자리에 앉아 그 밑의 모든 풍경을 내려다보는 것과 같다.

화왕과 살성은 무림이라는 험난한 산맥에서도 가장 높은 봉우리에 오른 희대의 강자들.

이미 진태경이라는 존재가 무림에 태어나기도 전에 중단전을 열었던 이들이니 내 변화를 눈치챈 것은 당연했다.

문제는…….

‘이걸 뭐라 대답해.’

자다가 방귀를 뀐 것도 아니고 중단전이 개방됐다. 다른 사람들은 피나는 수련, 혹은 생사(生死)를 오가는 극한의 상황에서나 얻을 수 있는 깨달음이다.

잠깐 망설이던 나는 문경의 손에 들린 대침을 보고 얼른 대답했다.

“그냥, 되던데요.”

“뭐라?”

“그냥 됐어요.”

“……그걸 지금 믿으라고 하는 소리냐?”

당연히 아니지.

그래서 무협 소설에서 흔하게 나오던 클리셰를 집어넣었다.

“사실, 이상한 꿈을 꾸긴 했습니다.”

주위 눈치를 살피며 목소리를 내리깔자, 문경의 미간이 좁혀졌다.

“꿈?”

“예. 굉장히 나이가 많아 보이는 백발의 노인이 갑자기 다짜고짜 검을 휘두르지 뭡니까. 그때는 꿈인지도 모르고 우선 피하고 봤죠.”

창이든 검이든 효자손이든 상관없다. 어차피 온갖 미신이 판치는 세상 아닌가.

우선 신선 같은 느낌을 주는 백발의 노인이 꿈에 나왔다는 것부터 흥미를 유발하기에 충분했다.

아니나 다를까, 문경이 웹소설 독자 같은 표정으로 물었다.

“그래서?”

“젖먹던 힘까지 끌어올려서 맞서는데, 도저히 상대가 안 되더라고요. 제가 어떤 공격을 해도 아무렇지 않게 피해 내고, 어떻게든 피하려고 해도 귀신처럼 슥 다가와서 검으로 삭. 슥삭하면 으억! 느낌 오세요?”

“꿈인 걸 몰랐단 말이냐?”

“알아차릴 시간도 없었습니다. 게다가 통증이 너무 생생했어요. 순식간에 수백 번을 베이면서 아, 이렇게 죽는구나 싶었는데 피 한 방울 안 나오길래 그제야 꿈인 걸 안 거죠.”

“계속해라.”

“그런데 이게 사람 미치게 하더라고요. 계속해서 검에 베이는데 아프기는 더럽게 아프고, 꿈인 걸 알아봤자 도무지 깨어나지를 않으니까요.”

“그래, 그렇지.”

문경은 자신이 베이기라도 한 것처럼 몸을 움찔거렸다.

이 양반, 의외로 리액션이 좋네.

살성이라는 무시무시한 이름 뒤에 숨어 있는 웹소설 독자로서의 본능을 재확인한 나는 거침없이 말을 이어 갔다.

“그렇게 시간이 얼마나 흘렀는지도 모르겠습니다. 며칠? 몇 달? 시간이 흐르는 것도 잊은 채 수도 없이 베이고 휘두르다 보니, 갑자기 묘한 감각이 찾아오더군요.”

“자세히 설명해라. 어떻더냐?”

이것만큼은 자세히, 사실 그대로 설명할 수 있다. 아크 리치와의 전투 속에서 내가 직접 겪었던 일이니까.

일반인이 들었다면 이게 무슨 뜬구름 잡는 듯한 묘사지? 라고 생각할 법한 내 표현을 들은 문경이 작게 중얼거렸다.

“깨달음. 기연(機緣)을 얻었군.”

“와, 소름. 그분도 비슷하게 말씀하셨는데.”

“네게 따로 말을 남겼단 말이냐?”

“네. 저를 보면서 처음으로 웃으시더니 그러시더라고요. 이 기연은 네게 주는 복이니 더욱 정진하라고.”

“그게 끝이냐?”

“예?”

“다른 말은?”

“어, 그게…….”

잠깐만. 이건 내 예상에 없었는데.

애초에 짧은 시간 동안 쥐어 짜낸 내용이라 처음 정해 놨던 내용은 이미 끝났다.

하지만 문경은 연참을 요구하고, 내게는 남은 비축분이 없다.

문제는 문경은 일반 독자가 아니라 살성이라는 거다.

‘여기에서 끝내면 어떻게 될까.’

어떻게 되긴, 장강 밑바닥에 가라앉은 채로 호북까지 떠내려가겠지.

나는 문경의 가늘어지는 눈빛에 황급히 입을 열었다.

“한마디 더 하시긴 했습니다.”

“뭐라 하시더냐?”

“그게 그러니까…….”

에라 시벌, 모르겠다.

마른침을 꿀꺽 삼킨 내가 조심스럽게 입을 열었다.

“아파야 무림인이다.”

“뭐라?”

“지, 진짜 그러셨어요. 저 한마디 딱 던지고 검에 올라타더니 슝 날아가셨…….”

“현기(賢氣)가 느껴지는군.”

“예?”

문경의 손에 들려있는 대침을 예의주시하던 나는 얼빠진 음성을 흘렸다.

‘아니, 이건 또 뭔 소리야.’

고개를 들자 침음성을 흘리며 작게 고개를 끄덕이는 문경의 모습이 보인다.

신음처럼 알아들을 수 없는 말을 중얼거리던 그가 불쑥 입을 열었다.

“여암(呂岩)이다.”

“위암이나 폐암은 아는데요. 혹시 어디 아프세요?”

“……여암을 모른다고?”

나를 정신병자 보듯 바라본 문경이 말을 이었다.

“여암. 자는 동빈(洞賓). 도호는 순양자(純陽子). 자신만의 도를 얻어 신선의 경지에 오른 그를, 사람들은 검선(劍仙)이라 부르지.”

“잠깐, 그 여동빈이요?”

“이제야 알아듣는군.”

여암은 몰라도 검선 여동빈은 안다. 무당파의 장삼봉, 소림사의 달마대사와 더불어 무협 소설의 단골 삼 대장이니까.

문경은 세상 진지한 표정으로 나를 바라보며 말을 이어갔다.

“네가 꿈에서 보았다는 그 노인이 바로 여동빈일 것이다. 마지막에 어검술(馭劍術)로 사라졌으니 검선이 틀림없겠지.”

“어…… 그렇네요.”

그냥 더 멋있을 것 같아서 그렇게 지어낸 건데, 이게 이렇게 되네.

여동빈이라는 이름의 신선이 있다는 건 소설을 통해 알고 있었지만, 어검술의 달인인지는 지금 처음 알았다.

‘코에 걸면 코걸이, 귀에 걸면 귀걸이라더니.’

지금이 딱 그 상황이다.

꿈, 아니 소설 속의 노인을 여동빈으로 규정한 문경은 세상 진지한 태도로 자신도 모르는 사이 끼워 맞추기를 하고 있었다.

“혹 수염이 가슴께까지 내려오더냐?”

“예.”

“키는.”

“작으시던데요.”

“놈! 얼마나 작냐고 묻는 것이다.”

“아, 그냥 작으셨어요. 계속 정신없이 베이는데 그런 거 볼 틈이 어디 있습니까.”

어지간한 건 고개를 끄덕끄덕하고 넘어갔지만, 아찔한 위기의 순간도 있었다.

“검 외에는 뭘 지니고 계셨지?”

“그 뭐냐. 검집이요.”

“죽고 싶으냐? 그건 당연한 것이고, 그 외에는 아무것도 없었느냐?”

“……그런 것 같은데요.”

내 대답을 들은 문경의 안광이 깊숙이 가라앉았다.

“여동빈은 검만 패용하고 있지 않다. 늘 오른손에 도가의 먼지떨이를 들고 다니지.”

“……!”

“설마 지금껏 거짓을 고했던 것이냐?”

절체절명의 위기다.

도대체 왜 검선이라는 양반이 먼지떨이를 들고 다니는지는 모르겠지만, 지금 당장으로서는 문경의 의심을 피하는 것이 급선무다. 나는 얼굴색 하나 변하지 않고 대답했다.

“전부 사실인데요.”

“한데 어찌하여 여동빈의 평소 모습과 네 말이 엇갈리느냐?”

“오늘은 먼지떨이를 놓고 온 것 같은데요.”

“그게 무슨 개소…….”

“아니, 여동빈 보신 적 있으세요?”

“……!”

“전 봤는데.”

그래, 시벌. 내가 봤다는데 어쩔 거야.

나는 여세를 몰아 순간 말문이 막힌 문경을 거세게 밀어붙였다.

“그리고 제가 여동빈이라고 했습니까? 전 그냥 늙은 할아버지인 줄 알았는데 그쪽이 먼저 여동빈이라면서요.”

“그쪽?”

“지금 그게 문제가 아니고, 사실이 그렇잖습니까. 솔직히 저는 여동빈이든 김동빈이든 상관없습니다. 꿈에서 정체 모를 할아버지를 만났고, 기연을 얻은 게 전부인데…… 무슨 죄지은 것마냥 쥐잡듯이 잡으시니까 저는 진짜, 하.”

“…….”

“여기 눈물 맺힌 거 보이세요? 진짜 저도 사내대장부로서 이러기 싫은데, 지금은 억울해서 눈물이 다 나와요.”

사실 무서워서 그런 거다.

내가 무슨 죄를 지었다고 이런 협박까지 당하면서 거짓말을 지어내야 하는지에 대한 자괴감까지 더해지니 이윽고 눈물 한 방울이 또르륵 굴러떨어졌다.

‘이게 인생이냐.’

아까는 아래로 지리고, 지금은 위로 지렸다. 연기로 시작했는데 어느덧 실화가 되어 버린 내 모습에, 표정 변화가 거의 없던 문경의 낯빛에 당황이 스쳤다.

“놈. 무슨 수작이냐.”

“하, 또 저러네. 나 안 해. 때려치워. 대답 다 했으니까 간다.”

“간다?”

“몰라. 알아서 해. 죽이든 살리든 예토전생을 시키든 마음대로 해.”

막 걸음을 옮기려던 바로 그 순간, 강대한 기세를 흩뿌리며 한 사람이 나타났다.

“지금, 이게 무슨 개 같은 짓거리냐?”

화왕과 살성의 시선이 허공에서 부딪쳤다.
```

## Final English reading copy

```markdown
# Chapter 437

As its name suggested, a fast ship was built with speed as its top priority.

If an ordinary warship was a heavyweight in terms of size, then a fast ship was something closer to a welterweight.

As a result, the ship’s hull wasn’t particularly large. Which meant there weren’t many places to hide from everyone else.

“Oh, dear.”

“Great Hero Jin. What brings you here?”

Two river bandits who had been slacking off at the stern under the pretense of standing guard recognized me and bowed deeply.

I nodded gravely and opened my mouth.

“Save me…”

At that moment, something sharp poked me right in the Mingmen acupoint at the small of my back.

“Save—stay alert as you go.”

“What?”

“I said, stay alert as you go. I need to discuss something with this fellow for a moment.”

“Oh, I see.”

*No. Don’t agree. Please be suspicious.*

I continued speaking while shooting an urgent sidelong glance at Mungyeong, who was pressed tightly against my side with his needle at my back.

“Be sure to take care on your way! If anyone asks about me, tell them I’m with Mungyeong!”

“Uh, understood.”

“No, not ‘understood.’ Say, right! My master! If my master comes looking for me…”

“I don’t think that’s likely.”

Mungyeong cut me off with a clear smile.

“Your Master seemed to have something important to discuss with Great Hero Jin Wikyung. In any case, we’ve only come to see a patient for a moment, so please don’t concern yourself with us. Go on and rest in the cabin. I’ll let you know afterward.”

“Then that works for us.”

There was nothing sweeter than legally slacking off in the middle of a boring guard shift.

The river bandits, now free to enjoy the shade, smiled and left. The Sound Transmission I had been preparing to send as my last hope was blocked by a single sentence from Mungyeong.

“You seem to have three or four lives.”

“…”

“You have two choices. Answer every question this old man asks from now on, or quietly keep your mouth shut if you don’t want to.”

I asked, just in case.

“What happens if I choose the second option?”

“You’ll go to Hubei.”

“That doesn’t sound too ba—”

Just as I was about to answer, Mungyeong calmly continued.

“You’ll drift all the way to Hubei while sunk at the bottom of the Yangtze. Quietly.”

“…I thought you said you had given up killing.”

“That depends on this old man’s will. It’s none of your concern.”

*What the fuck? It isn’t like he’s quitting smoking…*

Unable to believe what I was hearing, I challenged him again.

“You’re the Divine Physician. Are you really threatening to kill me?”

“I’m the former Divine Physician. I passed that name on to my Disciple long ago. So? What’s your answer?”

I glared at Mungyeong.

“Do you really think I’ll give in to a threat like this?”

“Of course.”

“You read me perfectly. I’ll answer every question with the utmost sincerity.”

“…”

Mungyeong seemed to have lost his words for a moment. After a long silence, he finally spoke.

“I’ve met all kinds of strange men, but you’re something else.”

“From everyone else’s perspective, I’d say we’re no different. Send a messenger-pigeon survey to all of Murim and ask which one of us is the bigger freak.”

“Freak?”

“My tongue slipped. Sorry.”

The aura Mungyeong let loose made every hair on my body stand on end.

He silently stared at me as I swallowed hard, then tossed out a single word.

“Middle Dantian.”

“Huh?”

“Until a few days ago—no, until half a day ago—your Middle Dantian was closed. What trick did you pull to accomplish such a great feat overnight?”

*So this was why he had called me aside.*

*I knew he had noticed.*

Martial realms were arranged in a perfect vertical structure.

It was like sitting at a high point and looking down at every landscape beneath you.

The Fire King and the Slaughter Saint were extraordinary powerhouses who had climbed to the highest peaks in the rugged mountain range known as Murim.

They had opened their Middle Dantians long before a person named Jin Taekyung had even been born. Naturally, they had noticed my change.

The problem was…

*What am I supposed to tell him?*

It wasn’t as though I had farted in my sleep and somehow opened my Middle Dantian. Other people could only gain that kind of enlightenment through blood-soaked training or extreme situations where they hovered between life and death.

I hesitated for a moment, then spotted the large acupuncture needle in Mungyeong’s hand and answered quickly.

“It just happened.”

“What?”

“It just opened.”

“Are you telling me to believe that?”

*Obviously not.*

So I inserted a cliché commonly found in martial arts novels.

“Actually, I did have a strange dream.”

I lowered my voice and glanced around us. Mungyeong’s brow furrowed.

“A dream?”

“Yes. A white-haired old man who looked incredibly ancient suddenly started swinging a sword at me without warning. At the time, I didn’t even realize it was a dream, so I just focused on dodging.”

It didn’t matter whether it had been a spear, a sword, or a back-scratcher. This was a world where all kinds of superstition ran rampant.

The appearance of a white-haired old man with the air of an immortal was interesting enough to pique anyone’s curiosity.

Sure enough, Mungyeong asked with an expression like a webnovel reader waiting for the next update,

“And then?”

“I summoned every last ounce of strength I had and fought back, but I couldn’t even come close to matching him. No matter what attack I used, he dodged it without a care. And whenever I tried to get away, he would glide up to me like a ghost and slash me with his sword. Swish, slash—ugh! You know the feeling?”

“You didn’t realize it was a dream?”

“I didn’t have time to realize anything. Besides, the pain was incredibly vivid. I was cut hundreds of times in an instant and thought, *So this is how I die.* But not a single drop of blood came out. That was when I realized it was a dream.”

“Continue.”

“But it was driving me insane. I kept getting cut by that sword, and it hurt like hell. Even after I realized it was a dream, I couldn’t wake up.”

“Yes. Exactly.”

Mungyeong flinched as if he had been cut himself.

*This guy has surprisingly good reactions.*

Having confirmed the instinct of the webnovel reader hiding behind the terrifying name of Slaughter Saint, I continued without hesitation.

“I don’t even know how much time passed. Days? Months? I lost all sense of time as I was cut countless times and kept swinging back. Then, all of a sudden, a strange sensation came over me.”

“Explain it in detail. What was it like?”

This part, at least, I could describe in detail and tell him the truth. It was something I had personally experienced in my battle with the Arch Lich.

Mungyeong heard my explanation—one that an ordinary person might have dismissed as some vague, airy description—and muttered quietly.

“Enlightenment. You gained a fortuitous encounter.”

“Wow, I’ve got goose bumps. He said something similar.”

“He left you a message?”

“Yes. He looked at me and smiled for the first time, then said that this fortuitous encounter was a blessing he was giving me and that I should devote myself to my training even more.”

“Was that all?”

“Huh?”

“Did he say anything else?”

“Uh, well…”

*Hold on. I didn’t plan for this.*

I had come up with the story by squeezing my brain dry in a short amount of time. I had already used up everything I’d prepared.

But Mungyeong was demanding another installment, and I had no material left in reserve.

The problem was that Mungyeong wasn’t an ordinary reader.

He was the Slaughter Saint.

*What happens if I end it here?*

What would happen? I’d sink to the bottom of the Yangtze and drift all the way to Hubei.

Under Mungyeong’s narrowing gaze, I hurriedly opened my mouth.

“He did say one more thing.”

“What did he say?”

“Well, that is…”

*Fuck it. I don’t know.*

I swallowed dryly and cautiously spoke.

“You have to suffer to be a Murim man.”

“What?”

“He really said that. He said exactly that, then climbed onto his sword and flew away…”

“I can sense profound wisdom.”

“Huh?”

I let out a stupid sound while keeping a wary eye on the large needle in Mungyeong’s hand.

*What the hell is he talking about now?*

When I raised my head, I saw Mungyeong murmuring under his breath and nodding slightly as though he were groaning.

After muttering something unintelligible, he suddenly spoke.

“It was Lü Yan.”[^1]

“I know about stomach cancer and lung cancer, but… are you sick somewhere?”

[^1]: The Korean reading of Lü Yan’s name, *Yeo-am*, ends in *am*, the Korean word for “cancer”—hence Taekyung’s misunderstanding.

“…You don’t know Lü Yan?”

Mungyeong looked at me as though I were insane, then continued.

“Lü Yan. His courtesy name was Dongbin, and his Taoist name was Chunyangzi. He attained his own Dao and reached the realm of an immortal. People called him the Sword Immortal.”

“Wait. You mean Lü Dongbin?”

“You finally understand.”

I might not have known Lü Yan, but I knew Sword Immortal Lü Dongbin. Along with Jang Samfeng of Wudang and the Shaolin Temple’s Bodhidharma, he was one of the three perennial fixtures of martial arts novels.

Mungyeong continued, his expression deadly serious.

“The old man you saw in your dream must have been Lü Dongbin. He vanished using sword-riding sorcery at the end, so he must have been the Sword Immortal.”

“Uh… I suppose so.”

I had only made it up because it sounded cooler, but somehow it had turned into this.

I knew from novels that there was an immortal named Lü Dongbin, but this was the first time I had heard that he was a master of sword-riding sorcery.

*If you hang it on your nose, it becomes a nose ring; if you hang it on your ear, it becomes an earring.*

That was exactly the situation I was in.

Having decided that the old man in my dream—or rather, the old man in my story—was Lü Dongbin, Mungyeong was fitting everything together with absolute seriousness without even realizing it.

“Did his beard reach down to his chest?”

“Yes.”

“How tall was he?”

“He was short.”

“Boy! I’m asking how short!”

“Oh, he was just short. I was being cut to pieces the whole time. When would I have had the chance to look at something like that?”

Mungyeong nodded and let most of it pass, but there was one dangerously close call.

“What did he carry besides the sword?”

“What was it… His scabbard.”

“Do you want to die? Of course he had that. Was there nothing else?”

“…I think that was all.”

The light in Mungyeong’s eyes sank deep.

“Lü Dongbin did not carry only a sword. He always held a Taoist fly-whisk in his right hand.”

“…”

“Have you been lying to this old man all along?”

It was a life-or-death crisis.

I had no idea why a man known as the Sword Immortal would walk around carrying a fly-whisk, but my top priority was avoiding Mungyeong’s suspicions. Without letting a single change cross my face, I answered.

“Everything I said was true.”

“Then why does your description contradict Lü Dongbin’s usual appearance?”

“He must have left his fly-whisk behind today.”

“What kind of bullshi—”

“No, wait. Have you ever seen Lü Dongbin?”

“…”

“I have.”

*Fuck, I’m the one who saw him. What are you going to do about it?*

Seizing the advantage, I pressed Mungyeong hard while he was momentarily at a loss for words.

“And did I say he was Lü Dongbin? I thought he was just some old man. You were the one who called him Lü Dongbin first.”

“You?”

“That isn’t the point. That’s what happened, isn’t it? Honestly, I don’t care whether he was Lü Dongbin or Kim Dongbin. I met some unidentified old man in a dream and gained a fortuitous encounter. That’s all. But you’re hounding me like I’ve committed some terrible crime, so I really…”

“…”

“Can you see the tears in my eyes? I really don’t want to do this as a man, but I’m so wronged that I’m actually crying.”

The truth was, I was scared.

The self-loathing over having to invent lies while being threatened like this—despite having committed no crime—only made things worse. Before long, another tear rolled down my cheek.

*Is this what life is?*

I had wet myself below earlier, and now I was wetting myself above.

I had started all this as an act, but it had somehow become real. For the first time, bewilderment crossed Mungyeong’s nearly expressionless face.

“You little bastard. What trick are you pulling?”

“Ugh, you’re doing it again. I’m done. I quit. I answered everything, so I’m leaving.”

“You’re leaving?”

“I don’t care. Do whatever you want. Kill me, spare me, use Impure World Reincarnation[^2] on me—whatever.”

[^2]: Impure World Reincarnation is a resurrection technique from *Naruto*.

Just as I was about to take a step, someone appeared while scattering a powerful aura.

“What the hell is this dogshit?”

The gazes of the Fire King and the Slaughter Saint collided in midair.
```
