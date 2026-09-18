<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0395.txt",
      "sha256": "cc819eb986972df3806ece7e8e73041e86fad5ee99de70e89ac85f606d2101b6",
      "bytes": 15002
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "3913796b36c23540b1b371838498f6281c13b8ce5b613781cebc71b4ffea6014",
      "bytes": 3063
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "e0bafef3495a98388b0f1c94b13c9f6bdb6ffb80e4cff9c31e840f7fa0e37511",
      "bytes": 134883
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "50d09fd35da45c3ce4ffc5ece4cd508706abff554a4cc981518d0d7d73152e09",
      "bytes": 533
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "7dd92b09056a3b32605d3d7375e57672c4c78a60ae315055fd08c6ec069d4a9e",
      "bytes": 1396
    },
    {
      "path": "characters/Wei Fenghu.md",
      "sha256": "4d6df4c1eef65fea6257e6a61eaeda973b3c2332feaf26fbfdf68a482607c3a3",
      "bytes": 555
    },
    {
      "path": "characters/Wu Heixing.md",
      "sha256": "50efef533012a34fc00520480533a07b48a6f42401a42e2eeb7ab339bf4b233c",
      "bytes": 735
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "a27bc883b998aad9cdaae44d31af0e75bf6d33189463577f7791eddf6b2a69e7",
      "bytes": 114784
    }
  ],
  "estimated_tokens": 10522
}
-->

# Durable State Update — Chapter 395

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 395. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 395. Profile updates may replace only one
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
  "chapter": 395,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 395,
    "continuity_sources": [395],
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
    "Jin Taekyung is Level 121, has the Undead Hunter Title, and keeps the strengthened Skeleton Warlord in his Inventory under the mocking name Bones.",
    "Jin has crossed the wall into true mastery and can use overwhelming physical force without internal energy when he restrains himself.",
    "The Arch Lich's three incomplete Liches were destroyed at Chengdu International Airport, and their testimony identified the Arch Lich as responsible for the undead army's actions.",
    "The Skeleton Warlord cannot raise undead deeper inside the current battlefield because the Arch Lich's control grows stronger there.",
    "Sichuan Province remains under martial law amid a Monster Wave exceeding 100,000 monsters, at least 300,000 initial casualties, magical communications interference, and a large undead army.",
    "The Sudden Quest The Desperate War Situation remains active, while the Unexpected Assault was canceled and its failure cost Jin 10 Strength.",
    "The Arch Lich remains weaker than its former self, serves a separate true king, and has ordered the black knight to withdraw the undead legions.",
    "Monster armies withdrew overnight from every front in Sichuan Province except the western front, which remains deeply penetrated because of Jin's advance.",
    "The western-front force suffered a major massacre near the city, Wei Fenghu remains China's Minister of National Defense, and Lei Fei remains missing with his unit.",
    "Faye Chen remains hostile toward Wu Heixing, while Wu Heixing intends to act against Jin after recalling his conversation with Lee Jungryong.",
    "Team Leader Choi has engineered favorable rumors about Jin's confrontation with General Liao by paying soldiers and leveraging existing hostility toward Liao.",
    "Magic Johnson commands the southern front, has temporarily withdrawn personnel for a military conference in Chengdu, and has a strongly flirtatious interest in Team Leader Choi."
  ],
  "continuity_sources": [
    394,
    393
  ],
  "open_questions": [
    "Who is the Arch Lich's true king, who is the black knight, and why did the undead legions withdraw now?",
    "What happened to Lei Fei and the Hunters who disappeared with him?",
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "What is Wu Heixing planning after recalling his conversation with Lee Jungryong?",
    "What does Shao Shen know about the consequences of Jin's confrontation with General Liao?"
  ],
  "safe_through": 394,
  "temporary_decisions": [
    "Render 파이 첸 as Faye Chen and 매직 존슨 as Magic Johnson.",
    "Render 형님 as hyung when Shao Shen addresses Jin Taekyung, and retain Mr. Jin for 진태경 씨 in Team Leader Choi's formal address.",
    "Preserve the hostile, profane tone of Faye Chen's confrontation with Wu Heixing.",
    "Render 마이클 존슨 as Michael Johnson and retain Rao Yang for 롸우양.",
    "Preserve Jin's dry first-person humor, sports-car metaphors, and crude Lord Fuck wordplay."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 이정룡    | **Lee Jungryong** |
| 기루     | **pleasure house**                               |                                                       |
| 상태               | **Status**                     |
| 매력               | **Charm**                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 웨이펑후 | **Wei Fenghu** | Minister of National Defense under China's Central Military Commission. |
| 우헤이싱 | **Wu Heixing** | Chinese S-rank Hunter who provokes Jin and nearly draws his sword. |
| 평화 | **Peace Guild** | Guild name. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 근위대 | **royal guard** | Guard unit protecting Prince Shangshan. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 주석 | **Chairman** | Political title used for Xiao Yang. |
| 국방부 | **Ministry of National Defense** | Government ministry referenced in Taekyung's comparison about the steady passage of time. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 마법사 | 이정룡 | Ares Guild mage subordinate to Vice Guild Master | Vice Guild Master | formal-deferential | Lee's five direct A-rank mages greet him and receive instructions for concealing the battle. |
| 우헤이싱 | 이정룡 | younger S-rank Hunter to senior Ares Guild authority | Mr. Lee | formal and deferential | Wu addresses Lee respectfully despite his usual hostility toward Koreans. |
| 웨이펑후 | 이정룡 | senior military official to senior foreign S-rank Hunter | Mr. Lee | formal and concerned | Wei asks Lee whether something is wrong. |
| 필릭스 | 이정룡 | British prince to senior S-rank Hunter | Jungryong Lee | formal through a translation device | Felix permits Lee to omit His Highness and gives his own preferred form of address. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 394
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who has sworn never to kill again.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 394
- **Aliases:** None
- **Role:** Vice Guild Master of Ares Guild; one of Korea's two S-rank Hunters; effective wielder of Ares Guild's authority in place of its Guild Master; Supreme Peak-level martial artist; gave Park Jihoon his initial orders and is Jihoon's master; visited the Peace Guild's hospital after Taekyung demanded an apology, brought compensation, and demanded the captives after negotiations.
- **Personality:** Outwardly genial, calm, and humorous; calculating, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

### Wei Fenghu.md

# Wei Fenghu (웨이펑후)

- **Safe through:** Chapter 388
- **Aliases:** None
- **Role:** Wei Fenghu is the Minister of National Defense under China's Central Military Commission and a four-star general.
- **Personality:** Courteous, reserved, and authoritative.
- **Voice:** Formal and measured, addressing Jin as Mr. Jin.
- **Relationships:** Wei Fenghu is Lei Fei’s maternal uncle who raised him as his own son, and he has asked Jin Taekyung to bring Lei Fei back if he is found.

### Wu Heixing.md

# Wu Heixing (우헤이싱)

- **Safe through:** Chapter 393
- **Aliases:** None
- **Role:** Wu Heixing is a Chinese S-rank Hunter known for frequent media exposure and scandal who secretly practices martial arts, including an internal-energy cultivation technique and fist-and-foot martial arts.
- **Personality:** Arrogant, status-conscious, abusive, and fiercely proud of his power, he responds to humiliation with anger, jealousy, and fear.
- **Voice:** Loud, insulting, entitled, and dependent on national and political status.
- **Relationships:** He is openly hostile toward Jin Taekyung and Faye Chen, and resents Jin receiving Chairman Shao Yang's attention.

## Korean source

```text
＃395화



「따라와.」

매직 존슨이 우리를 이끌고 향한 곳은 다름 아닌 병원 옥상이었다.

헬기도, 제트기도 보이지 않는 텅 빈 착륙장을 훑어본 내가 물었다.

“아무것도 없는데요?”

「아니지. 내가 있잖아.」

매직 존슨의 대답은 짧고 간결했지만, 그 말에 담긴 의미는 결코 간단한 것이 아니었다.

나와 같은 생각을 했는지, 최 팀장의 눈이 살짝 커진다.

“미스터 존슨. 혹시?”

「그래, 우린 텔레포트(Teleporte) 마법으로 이동할 거야.」

텔레포트. 쉽게 말해서 순간이동.

매직 존슨은 마치 세발자전거를 타자는 듯이 편안하게 얘기했지만, 텔레포트 마법이 극악한 난이도로 악명이 높다는 건 익히 알려진 사실이었다.

마법 발현을 위해 충족시켜야 하는 까다로운 조건들은 둘째 치고, 까딱 좌표라도 어긋나는 날에는 골로 가기 쉬웠다.

단 한 걸음 차이로 사과나무나 바위와 한 몸이 될 수도 있다니, 끔찍한 일이지.

“……그냥 제트기 타고 가면 안 될까요?”

「놉.」

단호하게 대답한 매직 존슨이 눈을 가늘게 떴다.

「헤이, 진. 설마 지금 나를 못 믿는 건 아니겠지? 나 매직 존슨이야. 직접 보여 줘야 믿겠어?」

“…….”

당신이 그런 말 하니까 더 이상하게 들리잖아.

그가 보여 주려는 게 텔레포트 마법이건 존슨이건 상관없다. 나는 그저 제트기를 타고 평화롭게 이동하고 싶을 뿐이다.

내 간절한 눈빛을 알아챈 최 팀장이 입을 열었다.

“미스터 존슨. 아시겠지만 이곳은 아크 리치의 힘이 닿는 곳입니다. 마법 방해는 물론이고 통신도 원활하지 않아요.”

「아, 그거였군. 난 또 뭐라고.」

매직 존슨이 피식 웃었다.

「두 사람은 내가 여기에 어떻게 왔다고 생각해?」

“어?”

“설마?”

「맞아. 텔레포트로 왔어. 약간 거슬리기는 했지만, 이 매직 존슨을 묶어 둘 수는 없지.」

딱!

매직 존슨이 손가락을 튕기자 허공에서 불기둥이 솟구친다. 숨 쉬듯 자연스러운 마법의 발현. 지금까지 마력 방해 때문에 제대로 마법을 사용할 수 없었던 공안 무력부의 마법사들과는 대조적인 모습이다.

“처음부터 가능했던 겁니까?”

「당연히 아니지. 지금까지 마력 방해가 있어도 어지간한 마법은 그럭저럭 쓸 수 있었는데, 텔레포트 같은 마법은 너무 위험해서 시도해 볼 엄두도 안 나더라고.」

“그럼…….”

「아크 리치. 놈의 힘이 아주 조금씩 줄어들고 있었어. 특히 어젯밤을 기점으로 방해 요소가 상당 부분 사라지게 되었지. 뭐, 아직도 통신 상태는 개판인 것 같지만.」

전 세계를 통틀어 셋밖에 없다는 대마법사이기에 할 수 있는 소리고, 가능한 일이다.

흰 이빨을 드러내며 웃어 보인 매직 존슨이 우리를 향해 손을 내밀었다.

「이 정도면 나를 믿기에는 충분한 것 같은데. 안 그래?」

“그러시다면야, 뭐.”

별다른 망설임 없이 손을 맞잡은 나와 달리, 최 팀장은 조용히 뒤로 물러났다.

“최 팀장님?”

“전 남겠습니다.”

「왜 그래, 최?」

“아직 처리해야 할 일이 있어서요. 어차피 발언권이 미비한 저로서는 가서 들으나, 전해 들으나 매한가지입니다.”

최 팀장은 언제나 냉정하게 상황을 바라본다. 스스로 흐름을 바꿀 수 없다면, 후 순위의 일을 끌어당겨 해결한다.

나는 잘못된 생각이라 말해 주고 싶었지만 잠자코 고개를 끄덕였다.

‘틀린 말은 아니니까.’

발언권이 강한 S급 헌터들 역시 결국은 대부분이 타국의 용병이며 빌려온 칼일 뿐이다.

그렇기에 샤오 양 주석이나 웨이펑후 국방부장도 전체 지휘권은 자신들에게 있음을 분명히 못 박았었다.

「최가 빠지다니! 이럴 수는 없어! 진은 매력이 없다고!」

“…….”

진짜 못 박아 버리고 싶네. 아니, 한편으로는 다행인가?

한참을 징징거리던 매직 존슨은 아쉬움 가득한 얼굴로 최 팀장에게 작별 인사를 건넸다.

「어쩔 수 없지. 그럼 다음에 봐, 최.」

“살펴 가십시오.”

「살펴 가긴 뭘. 어차피 한순간인데.」

어깨를 으쓱해 보인 매직 존슨이 내게 물었다.

「헤이, 진. 준비됐어?」

“네.”

「내 손 꽉 잡아. 놓치지 않게.」

“……깍지는 왜 끼세요. 그냥 손바닥만 잡으면 안 돼요?”

이런 건 연인들끼리나 하는 거 아닌가.

이십 대 후반의 모태솔로인 나로서는 거구의 흑인과 깍지 손을 낀다는 게 불편할 수밖에 없었다.

떨떠름해하는 내게 매직 존슨이 상냥한 어조로 말했다.

「원한다면 풀어도 좋아. 그런데 이동 중에 손을 놓치면 죽을 수도 있어.」

나는 어렸을 적 첫사랑을 떠올리며 매직 존슨의 손을 단단히 붙잡았다.

“갑시다, 달링.”

매직 존슨이 정색하며 대답했다.

「미안한데 진은 내 취향 아니야. 그 정도로 세게 잡을 필요는 없으니까 힘 좀 풀어 줄래?」

“……아, 예.”

「그럼, 간다?」

입을 열어 대답하려던 그때.

쏴아아아악!

‘흡!’

숨이 턱 막히고 팽팽한 공기가 전신을 조여 왔다.

흐릿해지는 시야 속에서 최 팀장의 모습이 신기루처럼 일렁이더니 이내 사라진다.

뒤집히는 땅과 하늘, 그리고 마침내 찾아온 엄청난 해방감.

“푸하!”

참았던 숨을 토해 낸 나는 깊이 숨을 들이마셨다. 폐부 깊숙이 스며드는 시원한 공기. 눈을 깜빡이자 잠시 흐릿했던 시야가 또렷해진다.

체감상으로는 1초 남짓한 시간이 흘렀을 뿐인데, 전혀 다른 풍경과 사람들이 그곳에 있었다.

「마지막 손님이 오셨군.」

중앙 군사위원회 국방부장 웨이펑후, 일주일 사이 십 년은 늙어 버린 듯한 그가 다가와 내 어깨를 두드렸다.

「모두 기다리고 있소. 함께 들어갑시다.」

“자, 잠깐만요.”

「응?」

“다가오지…… 우웨에에에에엑!”

촤아아악!

참고로 나는 키가 큰 편이다. 웨이펑후보다 머리 두 개 정도.

듬성듬성한 노장군의 정수리를 향해 토사물을 쏟아 내는 내게, 매직 존슨의 목소리가 들려왔다.

「아, 멀미 증상이 심해진다는 걸 말 안 해 줬구나. 미안해, 진. 미안해요, 웨이펑후.」

“그런 건 진작 말해 줬어야, 우웨에에엑!”

「……하.」

회의에 참석하기까지는 아주 약간의 시간이 추가로 소요되었다.



* * *



커다란 대회의실. 어두컴컴한 그곳에서는 홀로그램 영상이 흘러나오는 중이었다.

한 사람의 시선이 고스란히 담긴 영상에 복잡한 조종간과 강화유리 밖으로 흩어지는 구름이 담긴다. 하강과 동시에 보이기 시작하는 까마득한 점들도.

지상을 메운 그것들은 오와 열도 없이 파도처럼 밀려드는 중이었다.

‘몬스터.’

나는 이 시선의 주인이 전투기 파일럿이라는 사실을 어렵지 않게 알 수 있었다. 헤드캠을 착용한 그가 어딘가로 무전을 보냈다.

- 여기는 YANU-4885. 반복한다. YANU-4885. 목표 확인. 조준 완료.

- 사격을 허가한다.

치직, 치지직.

노이즈 낀 무전이었지만 알아듣기에는 무리가 없었다. 깊이 심호흡한 파일럿을 망설이지 않고 임무를 수행했다.

구궁.

작은 흔들림과 함께 전투기에 탑재되어 있던 미사일이 쏘아졌다. 순식간에 하나의 점이 되어 쏘아진 그것이 진군하는 몬스터 군단의 중심에 작렬하려던 그 순간.

쏴아아악.

놈들의 머리 위, 텅 빈 허공에서 난데없이 나타난 검은 소용돌이가 미사일을 집어삼켰다.

- 흐읍!

파일럿이 다급함이 느껴지는 헛숨과 함께 조종간의 붉은색 버튼을 눌렀다. 하지만…….

콰앙! 치지직.

갑자기 들이닥친 굉음과 함께 영상은 끊겼다. 홀로그램이 사라지고, 웨이펑후 국방부장이 무거운 표정으로 입을 열었다.

「다른 분들은 어떻게 보시오?」

매직 존슨이 시가에 불을 붙이며 대답했다.

「텔레포트 마법이군요. 발사된 미사일을 기체 위로 이동시켰어요.」

「미스터 존슨. 당신이라면 가능하오?」

곰곰이 생각에 잠겨 있던 그가 입을 뗐다.

「어렵지 않죠. 하지만 저 정도로 신속하고 정확하게 할 자신은 없습니다.」

「대마법사인 당신이라 해도 말이오?」

「……음.」

살짝 고개를 끄덕인 매직 존슨이 시가 연기를 내뿜었다.

그 역시 역사에 남을 전공을 세운 S급 헌터. 그만큼 자신의 실력에 자부심이 있었을 테니, 아크 리치라는 몬스터에게 뒤진다는 사실이 마음에 들지는 않을 것이다.

하지만 이 자리는 자존심을 위해 마련된 자리가 아니다. 현실을 직시해야 한다.

「그럼 화력 지원은 기대하기 어렵게 됐네. 큰 거 한 방 잘못 쐈다가는 대참사가 벌어질 테니까.」

파이 첸이 가느다란 손가락으로 술잔을 건드리며 말을 이었다.

「어느 정도 예상은 했지만…… 이렇게 된 이상 지상에서 결판을 내는 수밖에.」

「지금대로라면 전황은 차차 나아질 것이다. 본 왕자가 이끄는 대영제국의 왕실 근위대가 몬스터 군단을 박살 냈으니까. 그보다 지금 그대가 마시고 있는 술, 혹시 로마네콩티 45년 산인지?」

「아닌데.」

「흠. 마실 줄 모르는군.」

필릭스 왕자의 말에 파이 첸이 눈을 치켜떴다.

「어머, 이 어린애가 뭐라는 거야. 얘, 정신 좀 차려. 대영제국은 오래전에 해체됐고 몬스터들이 물러난 건 너희가 몇 번 승리해서가 아냐. 네 맞은편에 있는 저 녀석 덕분이지.」

필릭스 왕자가 힐끗 나를 바라봤다.

「서부 전선에서 큰 공을 세웠다는 이야기는 들었네만…… 진정 그 말들이 모두 사실인가?」

내가 거짓말이라도 친다는 거야, 뭐야.

나는 어이없는 표정으로 필릭스 왕자를 바라보았다.

“그럼 사실이지, 구라겠냐? 믿기 싫으면 믿지 마.”

「그토록 큰 공을 세운 것은 칭찬해 줄 만하지만, 언행이 상당히 불손하군. 필릭스 전하라고 지칭하고, 항상 경어를 쓰도록.」

나는 선선히 그 요구를 들어주었다.

“전하, 혹시 피쉬 앤 칩스를 잘못 쳐 드셨습니까?”

「으음. 용맹무쌍하나 무례하기 짝이 없는 자로군.」

“…….”

무례하기 짝이 없기는 개뿔이. 불알 한 짝을 없애 버릴까 보다.

참고로 일주일 전쯤에 한 번 털렸던 놈은 입을 꾹 다물고 눈도 마주치려 하지 않는다.

‘조용해지니까 좋긴 한데 뭔가 찝찝하단 말이지.’

우헤이싱의 멍청함이라면 적어도 몇 번 정도는 더 덤벼들 줄 알았는데, 생각 이상으로 겁이 많거나 내가 사람을 잘못 본 모양이다.

무엇보다 지금 당장엔 우헤이싱보다 더 신경 쓰이는 사람이 있었다.

“아까부터 조용하신데, 뭐 하실 말씀 없으세요?”

똬리를 튼 뱀, 이정룡이 부드럽게 웃는다.

“신경 써 줘서 고맙지만 난 괜찮네. 가타부타 말없이 고용주의 뜻에 따르는 게 용병의 미덕이거든.”

“아하, 그러시구나.”

“간단한 이치지.”

나는 따라 웃으며 입을 열었다.

“하지만 그런 것 치고는 활약이 좀 부진하시던데요. 북부 전선 쪽 전황이 영 신통치 않던데. 그것도 고용주의 뜻입니까?”

“……!”

내 한마디에, 좌중이 찬물을 뒤집어쓴 것처럼 조용해졌다. 자신을 향해 모여드는 사람들의 시선에 이정룡이 턱을 쓰다듬었다.

“그 말은 불쾌하군. 나와 아레스 길드는 최선을 다했어.”

“최선이라. 정말입니까?”

“지난 일주일 동안 열 번을 싸워 아홉 번을 이겼네. 비록 안타깝게도 한 차례 패배하긴 했지만, 이 정도면 뛰어난 전공이라고 생각하네만.”

10전 9승 1패. 수치로 보면 뛰어난 전공인 것은 맞다.

그러나 이틀 전, 북부 전선의 패배 소식을 들은 나와 최 팀장은 동시에 헛웃음을 터트렸었다.

‘교활한 노인네.’

이정룡은 전 세계에서 손꼽히는, 아니 무림의 기준으로도 엄청난 강자다. 저자의 성격상 모든 실력을 드러냈을 리는 없을 테니 세간의 인식보다 더 강하다고 봐야 한다.

그런 인간이, 뭐?

‘안타까운 패배 같은 소리 하네.’

다른 사람은 몰라도 나는 확신할 수 있다.

이정룡이 나섰음에도 졌다는 것은, 처음부터 끝까지 의도된 패배라는 것을.

엄청난 사상자를 내는 와중에도 온전히 퇴각한 아레스 길드원들이 바로 그 증거다.

‘어차피 입증하지 못할 테니 심증(心證)이라고 해야 맞겠지.’

그것이 지금 이정룡이 여유로울 수 있는 이유이기도 했다. 그가 느슨하게 팔짱을 끼며 입을 열었다.

“그날의 패배에 대해서는 안타깝게 생각하지만 섣부른 비난은 삼가 줬으면 좋겠군. 명백한 패배 요인이 있으니 말일세.”

“명백한 패배 요인?”

“그 상황에서 누가 데스나이트(Death Knight)가 나타날 거라 생각했겠나. 사령관이 죽으니 혼란을 걷잡을 수 없더군.”

“데스나이트라면…….”

“어젯밤 서부 전선에서도 나타났다고 들었는데. 아닌가?”

그 말에 문득 떠오르는 것이 있었다. 소도시에서 구조된 민간인 부부의 증언.

열 마리의 데스나이트가 천 명에 가까운 병력을 도륙했으며, 그 우두머리인 검은 기사는 무슨 이유에선지 자신들을 죽이지 않고 떠났다는 이야기였다.

나는 그 이야기를 듣고 검은 기사라는 놈이 유난히도 마음에 걸렸었다.

“그럼 북부 전선에 나타났다는 놈들 중에 혹시…….”

이정룡을 향한 내 말은 끝까지 이어지지 못했다.

복도를 질주하는 다급한 발소리와 함께, 중국 장교로 보이는 누군가가 문을 박차고 들어왔기 때문이었다.

쾅!

「헉, 헉. 비상, 비상입니다!」

그가 거친 숨을 몰아쉬며 말을 이었다.

「몬스터 군단이 진격했다는 소식입니다! 각 전선에서 전투가 벌어지고 있습니다!」

“……뭐?”
```

## Final English reading copy

```markdown
# Chapter 395

“Follow me.”

Magic Johnson led us to none other than the hospital rooftop.

After sweeping my eyes across the empty landing pad, where there wasn’t a helicopter or jet in sight, I asked,

“There’s nothing here.”

“Nope. I’m here.”

Magic Johnson’s answer was short and simple, but the meaning behind it was anything but.

Team Leader Choi’s eyes widened slightly, as if he had arrived at the same conclusion I had.

“Mr. Johnson. Don’t tell me…”

“That’s right. We’re going to travel by teleportation magic.”

Teleportation. In simple terms, instant travel.

Magic Johnson spoke as casually as if he were suggesting we take a ride on a tricycle, but everyone knew that teleportation magic was infamous for its extreme difficulty.

The finicky conditions that had to be met to cast the spell were one thing. If your coordinates were even slightly off, you could easily end up dead.

Apparently, being one step off could leave you fused with an apple tree or a boulder. Horrifying.

“Can’t we just take a jet?”

“Nope.”

Magic Johnson answered firmly and narrowed his eyes.

“Hey, Jin. You don’t actually distrust me, do you? I’m Magic Johnson. Do I have to show you before you’ll believe me?”

“……”

*You saying that somehow makes it sound even stranger.*

Whether what he intended to show us was teleportation magic or Johnson himself, I didn’t care. I simply wanted to travel peacefully by jet.

Team Leader Choi noticed my desperate expression and spoke up.

“Mr. Johnson. As you know, this area is within the Arch Lich’s sphere of influence. Not only is magic disrupted, but communications are unreliable as well.”

“Ah, so that’s what this is about. I thought it was something else.”

Magic Johnson let out a quiet laugh.

“How do you think I got here?”

“Huh?”

“Don’t tell me…”

“That’s right. I came by teleportation. It was a little irritating, but nothing can keep Magic Johnson down.”

Snap!

Magic Johnson snapped his fingers, and a pillar of flame shot up from the empty air. It was the effortless manifestation of magic, as natural as breathing. The contrast between him and the mages of the Public Security Armed Forces Department, who had been unable to use magic properly because of the magical interference, was striking.

“You could do that from the beginning?”

“Of course not. Until now, I could use most ordinary spells well enough even with the magical interference, but teleportation is too dangerous. I didn’t even dare try it.”

“Then…”

“The Arch Lich. Its power had been gradually weakening. In particular, a considerable portion of the interference disappeared after last night. Though communications still seem to be a complete mess.”

It was something he could say—and accomplish—because he was one of only three archmages in the entire world.

Magic Johnson showed us his white teeth as he held out a hand.

“That should be enough for you to trust me, don’t you think?”

“Well, if you put it that way.”

Unlike me, who took his hand without much hesitation, Team Leader Choi quietly stepped backward.

“Team Leader Choi?”

“I’ll stay here.”

“Why, Choi?”

“There are still things I need to take care of. Besides, with my limited voice in the matter, listening in person or hearing about it afterward will make little difference.”

Team Leader Choi always looked at the situation coldly. If he couldn’t change the course of events himself, he pulled forward matters of secondary importance and resolved them instead.

I wanted to tell him that he was mistaken, but I quietly nodded.

*He wasn’t wrong.*

Even the S-rank Hunters with powerful voices were, in the end, mostly mercenaries from other countries—borrowed blades.

That was why Chairman Shao Yang and Minister Wei Fenghu had made it clear that overall command belonged to them.

“Choi’s dropping out? This can’t be happening! Jin has no Charm!”

“……”

*I really want to put a nail through him. On second thought, maybe this is a good thing.*

After whining for quite some time, Magic Johnson said goodbye to Team Leader Choi with a deeply disappointed expression.

“Can’t be helped. See you next time, Choi.”

“Take care.”

“Take care of what? It’ll only be an instant anyway.”

Magic Johnson shrugged and looked at me.

“Hey, Jin. Ready?”

“Yes.”

“Hold my hand tight. Don’t let go.”

“……Why are we interlocking fingers? Can’t I just hold your palm?”

*Isn’t this something lovers do?*

As a guy in his late twenties who had been single his entire life, I couldn’t help feeling uncomfortable about interlocking fingers with a huge Black man.

Magic Johnson spoke to me in a gentle voice as I grimaced.

“You can let go if you want. But if you lose your grip during the journey, you might die.”

I thought of my first love from childhood and gripped Magic Johnson’s hand firmly.

“Let’s go, darling.”

Magic Johnson answered with a stern expression.

“Sorry, but Jin isn’t my type. You don’t have to squeeze that hard, so could you ease up?”

“……Oh. Right.”

“Then, shall we go?”

Just as I opened my mouth to answer—

Whoooooosh!

*Gasp!*

My breath caught in my throat, and taut air squeezed my entire body.

Through my blurring vision, Team Leader Choi’s figure wavered like a mirage before disappearing.

The earth and sky turned upside down, and then an incredible sense of release finally washed over me.

“Bwah!”

I let out the breath I had been holding and drew in a deep breath. Cool air seeped deep into my lungs. I blinked, and my briefly blurred vision cleared.

It felt as if barely a second had passed, yet an entirely different landscape and different people stood around me.

“Our last guest has arrived.”

Wei Fenghu, Minister of National Defense under China’s Central Military Commission, approached and patted me on the shoulder. He looked as if he had aged ten years in the past week.

“Everyone is waiting. Let us go inside together.”

“W-wait a second.”

“Yes?”

“Don’t come any closer…”

“Uweeeeeegh!”

Splash!

For the record, I’m fairly tall. About two heads taller than Wei Fenghu.

As I vomited all over the thinning-haired old general’s crown, Magic Johnson’s voice reached me.

“Ah, I forgot to mention that the motion sickness gets worse. I’m sorry, Jin. I’m sorry, Wei Fenghu.”

“You should’ve told me that earlier, uweeegh!”

“……Hah.”

It took a little longer before I was able to attend the meeting.

* * *

The large conference room was dim, and a holographic video was playing in the darkness.

The footage captured everything from a single person’s perspective: a complicated control panel, clouds scattering beyond reinforced glass, and the tiny, distant specks that began to appear as the aircraft descended.

The things covering the ground surged forward like waves, without ranks or formation.

*Monsters.*

It wasn’t difficult to tell that the owner of this viewpoint was a fighter pilot. Wearing a head-mounted camera, the pilot transmitted a radio message to someone.

—This is YANU-4885. I repeat, YANU-4885. Target confirmed. Locked on.

—You are cleared to fire.

Crackle. Crackle.

The radio was filled with static, but the words were still clear enough to understand. The pilot took a deep breath and carried out the mission without hesitation.

Rumble.

With a slight tremor, a missile mounted on the fighter jet launched. It became a single dot as it streaked away, about to strike the center of the advancing monster army—

Whoosh!

A black vortex suddenly appeared in the empty air above their heads and swallowed the missile.

—Hngh!

With an urgent gasp, the pilot pressed a red button on the control panel. But then—

Boom! Crackle.

The footage cut out amid a thunderous roar that suddenly crashed through the room.

The hologram disappeared, and Minister Wei Fenghu spoke with a grave expression.

“What do the rest of you think?”

Magic Johnson lit a cigar before answering.

“It was teleportation magic. The missile was teleported above the aircraft.”

“Mr. Johnson. Would that be possible for you?”

Magic Johnson, who had been deep in thought, finally spoke.

“It wouldn’t be difficult. But I can’t say I’d be able to do it that quickly and accurately.”

“Even for an archmage such as yourself?”

“……Hmm.”

Magic Johnson nodded slightly and exhaled cigar smoke.

He, too, was an S-rank Hunter who had accomplished feats that would go down in history. He must have been proud of his abilities, so he couldn’t have been pleased to learn that he had been outdone by a monster called the Arch Lich.

But this meeting had not been arranged to protect anyone’s pride. We had to face reality.

“Then it looks like fire support will be difficult. If one of the big shots goes wrong, it could cause a catastrophe.”

Faye Chen continued, lightly touching her wineglass with one slender finger.

“I expected something like this to a certain extent, but now that it’s come to this, we have no choice but to settle things on the ground.”

“The situation will gradually improve if things continue as they are. The royal guard of the British Empire, led by this prince, crushed the monster army. More importantly, that wine you’re drinking—is it perhaps a 1945 Romanée-Conti?”

“No.”

“Hm. You don’t know how to drink.”

Faye Chen glared at Prince Felix.

“Oh, my. What is this child talking about? Get a grip. The British Empire was dissolved long ago, and the monsters didn’t retreat because you won a few battles. They retreated because of that fellow sitting across from you.”

Prince Felix glanced at me.

“I heard that you distinguished yourself greatly on the western front…but are all those stories truly accurate?”

*What, does he think I’m lying?*

I stared at Prince Felix with an incredulous expression.

“Then they’re true, aren’t they? What, you think I made it all up? If you don’t want to believe me, don’t.”

“You may deserve praise for accomplishing such a great feat, but your words and conduct are remarkably insolent. Address me as His Highness and always speak respectfully.”

I readily agreed to his demand.

“His Highness, did you eat your fish and chips wrong?”

“Hmm. A man of unmatched courage, but utterly lacking in manners.”

“……”

*Utterly lacking in manners, my ass. I might just take one of his balls off.*

For the record, the guy I had beaten up about a week ago kept his mouth shut and refused even to meet my eyes.

*It’s nice that he’s quiet, but something about it feels unsettling.*

With Wu Heixing’s level of stupidity, I had expected him to come at me at least a few more times. Maybe he was more cowardly than I’d thought—or maybe I’d misjudged him.

More than anyone else, though, there was someone I found more irritating than Wu Heixing at that moment.

“You’ve been quiet for a while. Don’t you have anything to say?”

Lee Jungryong, a snake coiled in wait, smiled gently.

“Thank you for your concern, but I’m fine. A mercenary’s virtue is following the employer’s wishes without comment.”

“Oh, is that so?”

“It’s a simple principle.”

I smiled along with him and spoke.

“But for someone who says that, your performance seemed a little lacking. The situation on the northern front doesn’t look very good. Was that the employer’s wish, too?”

“……!”

At my single remark, the entire room fell silent as if someone had dumped cold water over everyone’s heads. As the gazes of those around him gathered, Lee Jungryong stroked his chin.

“That remark is unpleasant. Ares Guild and I did our best.”

“Your best? Really?”

“We fought ten times over the past week and won nine. Though we unfortunately suffered one defeat, I would consider that an impressive military record.”

Ten battles, nine wins, one loss. By the numbers, it was certainly an impressive record.

But two days ago, when Team Leader Choi and I heard the news of the northern front’s defeat, we had both let out hollow laughs.

*What a sly old man.*

Lee Jungryong was one of the strongest men in the world—or, by Murim standards, an incredibly powerful martial artist. Given his personality, there was no way he had revealed all his abilities. He was probably even stronger than the public believed.

And someone like that had the nerve to say—

*“Unfortunately suffered a defeat,” my ass.*

I couldn’t say this about anyone else, but I was certain.

The fact that Lee Jungryong had joined the battle and still lost meant the defeat had been intentional from beginning to end.

The Ares Guild members, who had withdrawn intact even amid the enormous casualties, were proof of that.

*Since I can’t prove it, I suppose it’s only a suspicion.*

That was also why Lee Jungryong could remain so relaxed. He loosely folded his arms and spoke.

“I regret that day’s defeat, but I would appreciate it if you refrained from making hasty accusations. There was an obvious reason for our loss.”

“An obvious reason?”

“Who could have expected a Death Knight to appear in that situation? Once the commander died, the confusion became impossible to control.”

“If you mean the Death Knights…”

“I heard they appeared on the western front last night as well. Is that not so?”

His words suddenly brought something to mind: the testimony of the civilian couple rescued from the small city.

Ten Death Knights had slaughtered nearly a thousand troops, and their leader, the black knight, had left without killing the couple for some unknown reason.

The black knight had bothered me ever since I heard that story.

“Then among the ones that appeared on the northern front, could one of them perhaps—”

My question to Lee Jungryong never reached its end.

Someone who looked like a Chinese officer came bursting through the door, accompanied by the urgent sound of footsteps racing down the corridor.

Bang!

“Huff, huff. Emergency! Emergency!”

He continued while gasping for breath.

“We have received word that the monster army has advanced! Fighting has broken out on every front!”

“……What?”
```
