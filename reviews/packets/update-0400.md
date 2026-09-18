<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0400.txt",
      "sha256": "31e1623263025e520234ae9976a8812ca32f40a434eb0ca61b358840a93434b5",
      "bytes": 13787
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "7d7ffdeb355994ed3bcbf0fc74d9e8ac18f7484e1a146acfb29e38bb6a46bd9e",
      "bytes": 1567
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "9356a5eb829c9c20a0bb5c2df0ef8bd7c2efb50dea2feb0e895821b8155ce641",
      "bytes": 135533
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "92fba6d7dd3ef09a8114441a50396e8641700cae7543467037dd443e47d3659b",
      "bytes": 533
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "269f339ead728580c6f608976b6d9654f9d1c3199ed92bfd79cd0d13cb781225",
      "bytes": 1212
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "2810106ce2183aa3d1bb5c01839390f80785f67af8e48ba223d49c40711df60a",
      "bytes": 622
    },
    {
      "path": "characters/Lei Fei.md",
      "sha256": "523f80f9847cea39efd11489043a3b4b54f22b63392481053403cd6d18330882",
      "bytes": 535
    },
    {
      "path": "characters/Wei Fenghu.md",
      "sha256": "4dc22a79295375a8bf173c99add947e85dd09f23467a2372cc2d8db4b946a5a6",
      "bytes": 555
    },
    {
      "path": "characters/Wu Heixing.md",
      "sha256": "45f43a9a8c1282495dd2142487b5e655cf7de500098243f7e38bad05e4186f2a",
      "bytes": 735
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "1758147bba0415175ed3d9e4120ba262fdeacc057390647188969d7e9c623713",
      "bytes": 117143
    }
  ],
  "estimated_tokens": 9832
}
-->

# Durable State Update — Chapter 400

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 400. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 400. Profile updates may replace only one
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
  "chapter": 400,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 400,
    "continuity_sources": [400],
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
    "Jin Taekyung is fighting the Level 135 Death Knight Lord after overwhelming the surrounding monster army.",
    "Jin killed an attacking Death Knight and heavily damaged the Death Knight Lord, breaking his armor, wrist, sword, and helmet.",
    "The Death Knight Lord's sword cut Jin's chest, but Jin remains able to fight.",
    "The Fire Dragon Armor is approximately fifty percent restored and mitigated part of the Death Knight Lord's attack.",
    "Jin recognizes the Death Knight Lord's exposed face as resembling the missing Lei Fei, without confirming that they are the same person.",
    "The Skeleton Warlord is guarding Choi and Shao at Jin's command.",
    "Lei Fei remains missing with his unit after the first Monster Wave."
  ],
  "continuity_sources": [
    399
  ],
  "open_questions": [
    "Is the Death Knight Lord actually Lei Fei, and what is the black knight's identity and origin?",
    "What is the significance of the black knight's memories and the child and shoe he recalls?",
    "Who is the lord served by the black knight, and what is the Arch Lich's larger objective?",
    "What will happen in Jin Taekyung's confrontation with the Death Knight Lord?",
    "What happened to the Second Fiend assigned to the Qingcheng attack?"
  ],
  "safe_through": 399,
  "temporary_decisions": [
    "Render 나이트메어 as Nightmare.",
    "Use black knight for 검은 기사 and keep it distinct from Death Knight and Death Knight Lord.",
    "Preserve Jin's blunt, profane combat voice."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 일격     | **One Strike**                         |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 레이페이 | **Lei Fei** | Concealed Chinese S-rank Hunter and head of the Public Security Armed Forces Department in Sichuan Province. |
| 웨이펑후 | **Wei Fenghu** | Minister of National Defense under China's Central Military Commission. |
| 우헤이싱 | **Wu Heixing** | Chinese S-rank Hunter who provokes Jin and nearly draws his sword. |
| 평화 | **Peace Guild** | Guild name. |
| 나비 | **Nabi** | Name used for the black kitten Familiar. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 오성홍기 | **Five-Starred Red Flag** | China's national flag. |
| 중화인민공화국 | **People's Republic of China** | Formal country name shouted by the Chinese Hunters. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 오성 | **Oseong** | One half of the paired Joseon-era names used in Taekyung's joke. |
| 중화 | **Zhonghua** | Patriotic term used in Shao Shen’s rallying speech. |
| 가오핑구 | **Gaoping District** | District of Nanchong City where the Sichuan Monster Wave began. |
| 공안무력부 | **Public Security Armed Forces Department** | Chinese security organization ordered to assemble during the attack. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 웨이펑후 | 진태경 | senior_military_official_to_ally | Mr. Jin | formal-polite | Wei Fenghu addresses Jin while inviting him to walk to the operations headquarters. |
| 진태경 | 웨이펑후 | Foreign Hunter to senior military official | General, Commander, or Supreme Leader | Polite but flustered | Jin jokingly cycles through grand titles while trying to interrupt Wei's emotional request. |
| 우헤이싱 | 진태경 | hostile S-rank Hunter to foreign Hunter and provocation target | peninsula bangzi | insulting and confrontational | Wu repeatedly addresses Jin with anti-Korean slurs. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 398
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who has sworn never to kill again.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 399
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force and crossed the wall into true mastery.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother; Jeok Cheongang is his Master; Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and student; his mother and sister Hayeon are among those he protects.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 399
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lei Fei.md

# Lei Fei (레이페이)

- **Safe through:** Chapter 399
- **Aliases:** None
- **Role:** One of China's concealed S-rank Hunters and head of the Public Security Armed Forces Department stationed in Sichuan Province, currently missing with his unit after the first Monster Wave.
- **Personality:** No personality traits are established.
- **Voice:** No voice traits are established.
- **Relationships:** Wei Fenghu is his maternal uncle and raised him as his own son.

### Wei Fenghu.md

# Wei Fenghu (웨이펑후)

- **Safe through:** Chapter 396
- **Aliases:** None
- **Role:** Wei Fenghu is the Minister of National Defense under China's Central Military Commission and a four-star general.
- **Personality:** Courteous, reserved, and authoritative.
- **Voice:** Formal and measured, addressing Jin as Mr. Jin.
- **Relationships:** Wei Fenghu is Lei Fei’s maternal uncle who raised him as his own son, and he has asked Jin Taekyung to bring Lei Fei back if he is found.

### Wu Heixing.md

# Wu Heixing (우헤이싱)

- **Safe through:** Chapter 398
- **Aliases:** None
- **Role:** Wu Heixing is a Chinese S-rank Hunter known for frequent media exposure and scandal who secretly practices martial arts, including an internal-energy cultivation technique and fist-and-foot martial arts.
- **Personality:** Arrogant, status-conscious, abusive, and fiercely proud of his power, he responds to humiliation with anger, jealousy, and fear.
- **Voice:** Loud, insulting, entitled, and dependent on national and political status.
- **Relationships:** He is openly hostile toward Jin Taekyung and Faye Chen, and resents Jin receiving Chairman Shao Yang's attention.

## Korean source

```text
＃400화



처음 진태경과 격돌했던 그 순간, 검은 기사는 본능적으로 깨달았다.

‘강하다.’

눈앞의 젊은 인간은 실로 엄청난 강자였다. 자신이 전력을 다한다 해도 승패를 장담할 수 없는, 혹은 그 이상의 힘을 지닌 자.

일진일퇴를 거듭하며 그런 생각은 더더욱 굳어졌다.

‘힘든 싸움이 되겠군.’

그러나 검은 기사는 겁먹지도, 물러서지 않았다.

그는 군주의 가장 충실한 종이며, 명령을 완수해야 할 사명을 가진 자였다.

이건 한계를 초월한 강자들의 싸움이다. 아주 약간의 차이로도 승패를 뒤집을 수 있었다.

‘포기하지 않는다면 기회는 온다.’

검은 기사는 그 사실을 잘 알고 있었다.

그건 훈련을 받던 어린 시절부터 늘 되새기던 말이었고, 그는 셀 수 없이 많은 전투에서 살아남으며 강자로 거듭날 수 있었다.

‘……내가?’

또다시 찾아온 혼란. 마음이 흐트러지자 손발이 어지러워졌다.

그리고 상대는 그 틈을 놓칠 만큼 약하고 허술한 자가 아니었다.

쉭, 서걱!

창날이 죽은 육신을 가르고.

퍼벙!

푸른 화염이 가슴을 후려쳤다.

손에 잡힐 것만 같은 그 열기 속에서, 검은 기사는 문득 어떤 감각을 느꼈다. 그 감각의 이름은 고통이었다.

‘이게 무슨…….’

검은 기사를 당황하게 만든 것은 고통이 느껴져서가 아니라, 분명 낯설어야 할 감각이 너무나도 익숙하다는 것이었다.

‘이 기억들은…… 도대체 뭐지?’

가슴이 욱신거리고 머리가 지끈거린다.

쉴 새 없이 쏟아지는 공격을 허용하며 비틀거리는 검은 기사의 눈앞에, 도무지 정체를 알 수 없는 누군가의 기억들이 빠르게 스쳤다.

‘이, 이럴 수가!’

‘마나 적응도가 엄청납니다. 역대 최고 수치예요!’

‘지금 즉시 중화 육성 훈련에 투입해야 합니다!’

흥분된 어조로 떠드는 새하얀 옷을 입은 인간들. 그리고 어둡고 각진 제복을 걸친 중년인.

‘중화 육성 훈련? 저 아이를 헌터로 키우겠다는 말이오?’

‘당연히 그래야 하지 않겠습니까. 고작 열세 살에 파이 첸과 비등한 마나 적응도를 지닌 아이입니다. S급 헌터, 그것도 본국 최고의 헌터가 될 자질이 충분합니다!’

‘거절하겠소.’

‘예, 예?’

‘아니, 중장 동지. 그게 무슨 말씀이십니까? 이 아이는…….’

‘그만.’

중년인이 가라앉은 목소리로 말을 이었다.

‘하나뿐인 외조카요. 내가 누이에게 약속했던 건 저 아이를 행복하게 만들어 주겠다는 것이었지, 헌터로 만들어 위험에 빠트리겠다는 것이 아니었소.’

‘헌터는 숭고한 직업입니다. 저 아이가 S급 헌터가 된다면 인민 전체의 흥복이 될 것입니다!’

‘그들이 얼마나 숭고한 일을 하는지는 알고 있소. 하지만 그렇게 내 매형도…….’

멈칫, 말을 멈춘 중년인이 고개를 저었다.

‘뭐라 해도 내 뜻은 바뀌지 않소. 상부의 지침이 없었다면 검사도 받지 않았을 터. 우리는 이만 가 볼 테니 알아서들 하시오.’

‘중장 동지, 중장 동지!’

등 뒤에서 울려 퍼지는 외침을 뒤로한 채 성큼성큼 다가온 중년인이 억지웃음과 함께 손을 내밀었다.

‘오래 기다렸지? 자, 이만 가자꾸나.’

검은 기사는, 아니 기억의 주인으로 짐작되는 그는 중년인의 손을 붙잡았다.

하얗고 자그마한 손.

이내 아이의 맑은 목소리가 흘러나왔다.

‘삼촌.’

‘응?’

‘저, 헌터가 되고 싶어요.’

순간 중년인의 얼굴 위로 만감이 교차한다.

입술을 깨물며 바라보기를 한참, 이내 근심 어린 한숨을 내쉬는 그의 뒤로 한껏 표정이 밝아진 인간들이 다가왔다.

‘중화 육성 훈련은 심혈을 기울여 제작한 프로젝트입니다. 안전도 철저하고, 효과도 확실합니다. 같은 나이인 우헤이싱도 잘 해내고 있고요.’

‘아이의 마음이 바뀐다면 언제든지 중단시키겠습니다.’

가장 나이가 많아 보이는 인간이 중년인의 어깨에 손을 올리며 말했다.

‘부디 우리를 믿고 맡겨 주시오. 웨이펑후 중장 동지.’

웨이펑후, 웨이펑후…….

검은 기사의 머릿속에서 끊임없이 메아리치는 이름. 너무나도 낯익고 그리운 그의 이름.

퍼벙!

가슴이 욱신거리는 것은 공격을 허용했기 때문일까, 아니면 또 다른 이유일까.

비틀거리는 검은 기사의 눈앞에 또 다른 기억들이 떠올랐다.

‘어른들이 칭찬해 주니까 네가 최고인 것 같냐?’

나비넥타이에 까만 정장. 반짝거리는 구두를 신은 소년이 뾰족한 눈초리로 그를 노려본다.

‘착각하지마. 최고는 나야. 넌 그다음이라고!’

검은 기사의 시야가 갸우뚱 기울어지더니, 이내 천진난만한 목소리가 흘러나왔다.

‘그래. 그럼 그렇게 하자.’

‘뭐?’

‘난 이 등도 좋아. 삼 등도 괜찮고, 꼴등이라고 해도 상관없어.’

날카로운 인상의 소년이 입을 떡 벌렸다.

‘너, 바보냐? 지금 훈련소 꼴등인 장 웨이보다 형편없는 놈이 되고 싶은 거야?’

‘하지만 장 웨이는 착하고 다른 사람도 잘 도와주는걸? 그 녀석은 훌륭한 헌터가 될 거야.’

‘이, 이익! 너 지금 나 놀리는 거지!’

‘어어? 아닌데. 난 그냥 네가 좋다면 뭐든…… 앗!’

쿠당탕!

갑자기 덤벼든 소년을 제압하는 건 순식간이었다. 밑에 깔린 소년이 발버둥 치며 외친다.

‘내가 최고야! 이 우헤이싱은 뭐든 최고라고!’

하나의 기억이 사라지면 또 다른 기억이 떠오른다. 마치 누군가 잔잔한 연못에 차례차례 돌을 던지는 것처럼.

알 수 없는 누군가의 기억은 계속해서 검은 기사의 머릿속을 어지럽혔다.

‘수석 교육생, ■■■■은 앞으로.’

커다란 공간을 메운 소수의 사람.

어째서인지 제대로 들리지 않는 호명에 몸이 저절로 움직인다.

저벅. 저벅.

절도 있게 나아가는 걸음은 보폭이 넓었고, 보이는 시야는 높았다.

어느새 훌쩍 성장하여 청년이 된 그에게, 제복을 걸친 장년인이 다가와 훈장을 걸어 주었다.

낯익은 얼굴. 첫 기억에서 마주친 적 있던 그가 작게 속삭였다.

‘후회하지 않겠느냐?’

‘후회하지 않습니다. 앞으로도 그랬고, 이후로도 변하지 않을 겁니다.’

‘대부분의 사람들은 네 존재를 모를 것이다. 어쩌면 평생을 그림자처럼 살아야 할지도 모른다.’

‘헌터의 다른 이름은 수호자라 배웠습니다. 드러나지 않는다고 해서 제 명예가 사라지는 것은 아닙니다.’

‘지금껏 해 주지 못한 말이 있다.’

어깨를 붙잡은 장년인의 손에 힘이 들어갔다.

‘네가 자랑스럽구나. 훌륭히 자라 주어 고맙다.’

‘감사합니다. 외삼촌. 아니…… 아버지.’

환한 미소와 함께 장년인의 눈가가 축축하게 젖어 들었다.

주름진 볼 위를 미끄러진 눈물 한 방울이 단상 위로 툭 떨어진 그 순간, 새로운 기억이 떠올랐다.

‘계십니까?’

따스한 어느 봄날에 찾은 그곳은 자그마한 꽃집이었다. 화사한 꽃들을 둘러보며 안을 기웃거리는 그에게, 그녀가 다가왔다.

‘어서 오세요!’

통통 튀는 걸음걸이와 고양이처럼 새치름한 눈매.

소리는 얼마나 경쾌하고 밝은지. 또 얼마나 아름다운지…….

앳된 청년 시절을 지나서 보다 원숙해진 검은 기사는, 아니 한 사내는 가슴이 쿵쿵 뛰었다.

‘손님?’

‘아니, 저, 그게. 꼬, 꽃을 사러 왔는데 말입니다.’

‘부모님 드리시려고요? 아니면 애인?’

‘부, 부모님입니다. 그, 엄밀히 말하면 부모님은 아니고 절 키워 주신 외삼촌이신데…….’

‘으흠. 그러시구나. 그런데 말투가 되게 딱딱하네요. 혹시 군인이세요?’

‘비, 비슷하지 말입니다.’

이상한 기억이었다. 말이 뚝뚝 끊기고 눈앞이 자꾸만 하얗게 물드는.

정신을 차렸을 때 그는 화사한 꽃 한 다발을 품에 안은 채 멍하니 병실에 들어서고 있었다.

‘녀석. 가벼운 폐렴이니까 굳이 올 필요 없다 하지 않았…… 그런데 그건 뭐냐?’

장년인, 웨이펑후의 물음에 그가 넋 나간 목소리로 대답했다.

‘꽃이요.’

‘혹시 그게 병문안 선물이냐?’

‘네.’

‘그러니까 지금. 내 병문안 선물로 국화를 사 왔다고?’

‘네에…… 어?’

‘이런 배은망덕한 놈을 봤나! 야, 이놈아!’

촥! 촤악!

사내는 꽃다발에 얻어맞으면서도 웃었다. 자신의 멍청함에 실소가 흘러나왔고, 국화를 닮은 그녀가 생각나서 웃을 수밖에 없었다.

그 후 빠르게 흘러가는 기억 속에서, 그는 매일같이 꽃집에 들렀다.

‘아, 안녕하십니까!’

‘어서 오…… 어머, 또 오셨네요?’

‘하하.’

‘국화 맞죠? 새하얀 거.’

봄, 여름, 가을, 겨울.

네 번의 계절이 지났을 때, 두 사람의 관계는 더 이상 꽃집 주인과 손님이 아니었다.

‘할 말이 있어.’

‘뭔데?’

‘나랑 결혼해 줄래?’

‘……아.’

‘행복하게 해 줄게.’

그건 지금까지의 기억 중 가장 길었다.

일 초가 십 년, 백 년처럼 느껴질 만큼 오랜 침묵이 끝난 후, 그녀가 입을 열었다.

‘나도 할 말 있어.’

‘아니, 그 전에 내 대답부터…….’

‘나, 임신했어.’

‘어?’

쿵, 쿵쿵. 쿵쿵쿵!

사내의 심장은 거세게 요동쳤고, 검은 기사는 고통으로 몸부림쳤다.

‘아아, 아아아!’

머리가 쪼개질 듯이 아팠고 누군가의 손이 몸 안을 쥐어짜는 것 같았다.

상상조차 해 본 적 없는 고통과 함께 또 다른 기억이 빈자리를 비집고 들어왔다.

‘응애, 응애애!’

‘이, 이 아이가…….’

‘아빠가 된 걸 축하해. 여보.’

새로운 생명의 탄생. 그리고 성장.

‘압바. 압바바!’

‘여보. 여보! 방금 들었어? 벌써 아빠를 부르다니, 우리 애 천재 아닐까?’

‘기저귀나 좀 갈아 줄래?’

‘잠깐만 기다려봐. 다시 한번 들어보고.’

‘압바, 어무아!’

‘으하하! 그래! 우리가 네 아빠고 엄마다!’

포대에 싸여 꼬물거리던 아기가 뒤집기를 성공하던 날. 처음으로 네발로 기어가고, 걸어가던 그 날…….

사내는 세상을 다 가진 것처럼 행복했다.

그러나 계속되던 꿈같은 나날이 악몽으로 변하는 데에는 그리 오랜 시간이 걸리지 않았다.

‘가오핑구에서 마력 수치가 급등했습니다!’

‘가오핑구? 계속해서 연락 취하고, 만일을 대비해 2연대 소집해 출동시킨다.’

‘부, 부장님. 통신이 끊겼습니다.’

‘뭐?’

예고 없이 벌어진 재앙.

황급히 휘하의 병력을 소집한 사내는 문제의 근원지로 향했고, 믿을 수 없는 광경을 마주했다.

‘캬우우우우!’

‘모, 모두 도망…… 컥!’

퍼걱! 콰아아아앙!

평화롭던 도시의 하늘에는 불길이 솟구쳤고, 지상에는 셀 수도 없이 많은 몬스터가 인간들을 도륙하고 있었다.

비명과 죽음이 흘러넘치는 땅. 믿기 힘든 대학살의 현장 앞에서 사내는 검을 뽑았다.

‘공안무력부(公安武力部)!’

츠츠츠!

검신을 휘감으며 솟구친 오러 블레이드가 찬란하게 빛났다.

사내의 외침에 일천여 명의 헌터들이 먹먹한 함성으로 응답했다.

그들은 인류의 방패이자 수호자다. 단 한 걸음도 물러설 수 없었다.

‘모조리 쓸어 버려라!’

‘와아아아! 중화인민공화국 만세!’

갑옷에 붉은 오성홍기를 새긴 그들은 파도처럼 나아갔고, 이내 하얀 포말 대신 피를 뿌리며 산산이 부서졌다.

‘겁화의 불꽃으로 멸망하라, 파이어 레인(Fire Rain).’

키이이잉.

아가리를 벌린 잿빛 하늘. 쏟아지는 화염의 비 아래에서, 사내는 사랑하는 아내와 다섯 살이 된 딸을 떠올렸다.

그리고 ‘그 존재’와 마주했다.



‘도망쳤다면 살 수 있었을 텐데.’

‘널 죽이겠다.’

‘고결하구나. 이름이 무엇인가, 인간.’

‘나는…….’



* * *



“……레이페이?”

귓가를 파고든 진태경의 목소리에, 검은 기사의 몸이 덜컥 굳었다.

막혔던 둑이 허물어지며 모든 것이 재조립되기 시작한다.

인간으로 살아온 36년간의 기억이 해일처럼 쏟아져 눈 앞을 가렸다.

- 나는, 나는…….

도대체 무엇인가.

혼란과 고통으로 몸을 떠는 검은 기사의 머릿속에, 천둥 같은 외침이 울려 퍼졌다.

- 너는 내 가장 충실한 종이자 군단의 총사령관. 군주가 명하노니, 잿가루가 되어 스러질 때까지 네 본분을 다하라!

- ……!

그것은 거부할 수 없는 언령(言靈).

바람 앞의 촛불처럼 휘청이던 붉은 안광이 거세게 타올랐다.

일격을 남겨 둔 채 쓰러져 있던 검은 기사, 아니 레이페이의 전신에서 엄청난 마력이 솟구쳤다.

콰아아아!
```

## Final English reading copy

```markdown
# Chapter 400

At the very first moment he clashed with Jin Taekyung, the black knight instinctively realized it.

*Strong.*

The young human before him was an unbelievably powerful opponent. Someone whose strength was so great that even if the black knight gave it everything he had, he could not guarantee victory—or perhaps someone even stronger than that.

As they traded attack and defense again and again, the thought only grew firmer.

*This will be a difficult fight.*

But the black knight was neither frightened nor willing to retreat.

He was his lord’s most loyal servant, a being entrusted with the mission of carrying out his orders.

This was a battle between powerful beings who had transcended their limits. Even the slightest difference could turn victory into defeat.

*If I do not give up, an opportunity will come.*

The black knight knew that well.

It was something he had repeated to himself ever since he was a child in training, and surviving countless battles had allowed him to grow into a powerful warrior.

*…Me?*

Confusion came over him again. As his mind grew disordered, his hands and feet grew clumsy.

And his opponent was neither weak nor careless enough to miss such an opening.

Whoosh, scrape!

The spearhead tore through dead flesh.

Boom!

Blue flames slammed into his chest.

Amid that heat, so intense it seemed close enough to grasp, the black knight suddenly felt something.

The name of that sensation was pain.

*What is this…?*

What disconcerted the black knight was not the fact that he could feel pain, but that a sensation which should have been completely unfamiliar felt so terribly familiar.

*What are these memories…?*

His chest throbbed, and his head pounded.

As the black knight staggered under the relentless barrage of attacks, memories belonging to someone whose identity he could not possibly determine flashed rapidly before his eyes.

*This, this can’t be!*

“His mana adaptability is incredible. It’s the highest figure we’ve ever recorded!”

“He needs to be placed in the Zhonghua Development Training program immediately!”

Humans in dazzling white clothes chattered in excited voices. Standing among them was a middle-aged man dressed in a dark, angular uniform.

“Zhonghua Development Training? Are you saying you intend to raise that child as a Hunter?”

“Of course. He’s only thirteen years old, yet his mana adaptability is comparable to Faye Chen’s. He has more than enough potential to become an S-rank Hunter—the best Hunter in the country!”

“I refuse.”

“Pardon me?”

“No, Comrade Lieutenant General. What do you mean? This child…”

“Enough.”

The middle-aged man continued in a subdued voice.

“He is my only nephew. I promised my sister that I would make the boy happy, not turn him into a Hunter and put him in danger.”

“Being a Hunter is a noble profession. If that child becomes an S-rank Hunter, he will be a blessing to the entire people!”

“I know how noble the work they do is. But that is how my brother-in-law also…”

The middle-aged man suddenly stopped and shook his head.

“No matter what you say, I will not change my mind. If there had been no directive from above, I would not even have had him tested. We will be leaving now, so handle the rest yourselves.”

“Comrade Lieutenant General! Comrade Lieutenant General!”

Leaving the shouts echoing behind him, the middle-aged man strode over with a forced smile and held out his hand.

“You’ve been waiting long, haven’t you? Come on, let’s go.”

The black knight—or rather, the man who seemed to be the owner of these memories—grasped the middle-aged man’s hand.

A small, pale hand.

Then a clear child’s voice rang out.

“Uncle.”

“Yes?”

“I… I want to become a Hunter.”

A complicated array of emotions crossed the middle-aged man’s face.

After staring at the child while biting his lip for a long time, he let out a worried sigh. Then the humans whose expressions had brightened considerably approached him.

“Zhonghua Development Training is a project we developed with painstaking care. Its safety measures are thorough, and its effectiveness is proven. Wu Heixing, who is the same age, is doing well too.”

“If the child changes his mind, we will stop the training at any time.”

The oldest-looking man placed a hand on the middle-aged man’s shoulder.

“Please trust us and leave him in our care, Comrade Lieutenant General Wei Fenghu.”

Wei Fenghu. Wei Fenghu…

The name echoed endlessly through the black knight’s mind. A name that felt so familiar, and so dearly missed.

Boom!

Was the throbbing in his chest caused by the attack he had taken, or was there another reason?

As the staggering black knight stared ahead, more memories appeared before his eyes.

“You think you’re the best just because the adults praise you?”

A boy in a bow tie and black suit glared at him with sharp eyes. His polished shoes gleamed.

“Don’t get confused. I’m the best. You’re second!”

The black knight’s vision tilted to one side, and then an innocent voice rang out.

“Okay. Let’s do that, then.”

“What?”

“I like being second, too. Third is fine, and I don’t care if I come in last.”

The sharp-featured boy’s mouth fell open.

“Are you stupid? Do you want to become worse than Zhang Wei, the last-place trainee at the training camp?”

“But Zhang Wei is kind and helps other people, too. He’ll become a great Hunter.”

“Y-You’re making fun of me right now, aren’t you?”

“Huh? No. I just… whatever you want is fine with me—ah!”

Crash!

Subduing the boy who suddenly lunged at him took only an instant. The boy pinned beneath him struggled and shouted.

“I’m the best! Wu Heixing is the best at everything!”

When one memory disappeared, another appeared in its place, as though someone were tossing stones one after another into a still pond.

The memories of that unknown person continued to throw the black knight’s mind into confusion.

“Top trainee, ■■■■, step forward.”

A small number of people filled a vast space.

For some reason, he could not hear the name being called clearly, but his body moved on its own.

Step. Step.

His disciplined stride was long, and his field of view was high.

By then, he had grown into a young man. An older man in uniform approached and pinned a medal to his chest.

It was a familiar face. The same man he had seen in the first memory whispered quietly.

“Will you not regret this?”

“I have no regrets. I did not regret it before, and I never will.”

“Most people will not know that you exist. You may have to live your entire life like a shadow.”

“I was taught that another name for a Hunter is a guardian. My honor does not disappear simply because I remain unseen.”

“There is something I have not been able to tell you until now.”

The older man’s hand tightened around his shoulder.

“I’m proud of you. Thank you for growing up so well.”

“Thank you, Uncle. No… Father.”

The older man’s eyes grew damp beneath his bright smile.

At the moment a single tear slid down his wrinkled cheek and fell onto the platform, another memory surfaced.

“Hello? Is anyone there?”

On a warm spring day, the place he visited was a small flower shop. As he looked around at the bright flowers and peered inside, she approached him.

“Welcome!”

She walked with a buoyant step, and her eyes had the prim, coy look of a cat.

Her voice was so lively and bright. And so beautiful…

The black knight—or rather, a man who had passed through his youthful years and grown more mature—felt his heart pound.

“Are you a customer?”

“No, I, um… I came to buy some fl-flowers.”

“For your parents? Or your girlfriend?”

“My parents. Strictly speaking, they aren’t my parents. It’s my uncle who raised me…”

“I see. But you speak very stiffly. Are you a soldier?”

“S-Something like that, ma’am.”

It was a strange memory. His words kept breaking off, and everything before his eyes repeatedly turned white.

When he came to his senses, he was walking dazedly into a hospital room with a bright bouquet of flowers in his arms.

“You fool. I told you there was no need to come when it was only mild pneumonia… What’s that?”

At Wei Fenghu’s question, he answered in a dazed voice.

“Flowers.”

“Is that a get-well gift?”

“Yes.”

“So you bought chrysanthemums as a get-well gift for me?”

“Yes… Huh?”

“You ungrateful brat! Hey, you!”

Smack! Smack!

The man laughed even as he was beaten with the bouquet. A quiet laugh escaped him at his own stupidity, and he could not help laughing because she reminded him of chrysanthemums.

After that, the memories began to flow rapidly. He visited the flower shop every day.

“Ah, h-hello!”

“Welcome—oh my, you’re back again?”

“Haha.”

“Chrysanthemums, right? The pure white ones.”

Spring, summer, autumn, winter.

By the time four seasons had passed, the relationship between the two was no longer that of a flower-shop owner and her customer.

“I have something to say.”

“What is it?”

“Will you marry me?”

“…Ah.”

“I’ll make you happy.”

That was the longest of all the memories so far.

After a silence so long that a single second felt like ten years, or even a hundred, she finally opened her mouth.

“I have something to say, too.”

“No, before that, let me hear your answer…”

“I’m pregnant.”

“What?”

Thump. Thump-thump. Thump-thump-thump!

The man’s heart pounded violently, and the black knight writhed in pain.

“Ahhh! Aaaah!”

His head hurt as if it were splitting apart, and it felt as though someone were wringing out his insides with their hands.

Along with pain he had never even imagined, another memory forced its way into the empty space.

“Waaah! Waaah!”

“T-This child…”

“Congratulations on becoming a father, honey.”

The birth of a new life.

And its growth.

“Dada. Dada-da!”

“Honey, honey! Did you hear that? Our baby’s already saying ‘Dada.’ Could our baby be a genius?”

“Could you change the diaper?”

“Wait a moment. Let me hear it one more time.”

“Dada, Momma!”

“Hahaha! That’s right! We’re your daddy and mommy!”

The day the baby, bundled in a swaddling cloth and squirming helplessly, succeeded in rolling over.

The day he first crawled on all fours, and the day he first walked…

The man was happy as if he had gained the entire world.

But it did not take long for those dreamlike days to turn into a nightmare.

“The mana level in Gaoping District has spiked!”

“Gaoping District? Keep trying to contact them, and mobilize and deploy the Second Regiment as a precaution.”

“D-Director, we’ve lost communications.”

“What?”

A disaster that struck without warning.

The man hurriedly assembled the forces under his command and headed for the source of the problem. There, he encountered a sight he could not believe.

“Kyawwwww!”

“E-Everyone, run… Ghk!”

Slash! KABOOM!

Flames rose into the sky above the peaceful city, while countless monsters slaughtered the humans on the ground.

In that land overflowing with screams and death, the man drew his sword before the unbelievable scene of carnage.

“Public Security Armed Forces Department!”

Zzt!

An aura blade rose around the blade, shining brilliantly.

More than a thousand Hunters answered the man’s cry with a resonant roar.

They were humanity’s shield and guardians. They could not retreat even a single step.

“Wipe them all out!”

“Long live the People’s Republic of China!”

With the Five-Starred Red Flag engraved on their armor, they advanced like a wave. Soon, instead of white foam, they broke apart in a spray of blood.

“Perish in the flames of hellfire, Fire Rain.”

Kiiiiing.

The ash-gray sky opened its maw.

Beneath the rain of falling flames, the man thought of his beloved wife and his five-year-old daughter.

And then he came face-to-face with *that being*.

“If you had run, you could have lived.”

“I’ll kill you.”

“How noble. What is your name, human?”

“I am…”

* * *

“…Lei Fei?”

At the sound of Jin Taekyung’s voice in his ear, the black knight’s body abruptly went rigid.

As a dam finally gave way, everything began to reassemble.

Thirty-six years of memories from his life as a human poured out like a tidal wave, obscuring his vision.

—I am, I am…

What in the world was he?

As the black knight trembled in confusion and pain, a thunderous voice rang out in his mind.

—You are my most loyal servant and the supreme commander of my legion. Your lord commands you: fulfill your duty until you crumble and wither into ash!

—……!

It was an irresistible word-spell.[^1]

The red eye-light that had been wavering like a candle before the wind flared fiercely.

The black knight—or rather, Lei Fei—who had fallen with one strike still remaining, now erupted with tremendous mana from his entire body.

KRAAAAAASH!

[^1]: A command imbued with supernatural power.
```
