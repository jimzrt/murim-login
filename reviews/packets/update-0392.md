<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0392.txt",
      "sha256": "efeac7bbb72f41575be8c4a82f11dd52dda0e0f51fdc2c9c6e56f1d609a6f8cd",
      "bytes": 13618
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "f9c4f59392b70a25e07e774106f2ac5e2e1fed64d63dbb8ed075ffa76a28138a",
      "bytes": 3831
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2deaf603ca224e11e1c45166395b281a6f8688385f7305169cd823743b4a2e18",
      "bytes": 134702
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "654bccf7357ca2914147526f48a0619b6ff4bbe60a6f7d06b5184d88bbf4732b",
      "bytes": 667
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "019ee40c7d4ef83a6520167ef7114dc3516053978a574e066627ebc58048425e",
      "bytes": 1168
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "7bc35048c80dbf1848bd03611031a20af7997e7a114c84e069315f7d84f66345",
      "bytes": 622
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "727ef8ca23383251d0a59aa0d17d46641b84c010c253ce2c342d0d8dcd0c3394",
      "bytes": 112175
    }
  ],
  "estimated_tokens": 9695
}
-->

# Durable State Update — Chapter 392

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 392. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 392. Profile updates may replace only one
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
  "chapter": 392,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 392,
    "continuity_sources": [392],
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
    "Jin Taekyung has crossed the wall into true mastery, while Choi Minwoo has become substantially stronger and more refined.",
    "The Arch Lich's three incomplete Liches were destroyed at Chengdu International Airport, and their testimony identified the Arch Lich as responsible for the undead army's actions.",
    "The Skeleton Warlord cannot raise undead deeper inside the current battlefield because the Arch Lich's control grows stronger there.",
    "Jin's western-front force annihilated more than a thousand monsters in about two hours without a fatality; allied losses were twenty-three severely wounded and thirty lightly wounded.",
    "Public Security Armed Forces Hunters spearhead the western-front advance, while the following military destroys and transports corpses to prevent undead resurrection and rescues civilians.",
    "General Liao commands the 13th Group Army of the Chengdu Military Region and has used his authority to order questionable operations; he is implicated in a military procurement corruption scandal.",
    "Sichuan Province remains under martial law amid a Monster Wave exceeding 100,000 monsters, at least 300,000 initial casualties, magical communications interference, and a large undead army controlled by the Arch Lich.",
    "Wei Fenghu remains China's Minister of National Defense and the Chairman's right-hand man; Lei Fei remains unconfirmed dead or alive after disappearing with his department's Hunters.",
    "United Nations peacekeeping forces and international S-rank Hunters remain engaged on the Sichuan front, with Faye Chen having prevented an east-west breach from spreading.",
    "Wu Heixing remains hostile toward Jin, while Lee Jungryong is seeking an undisclosed discussion with him.",
    "A black knight commanding ten Death Knights massacred Zhang Wei's force near Suining City, then withdrew after sparing a hidden family with a child; Jin remains under the nonrefusable Sudden Quest The Desperate War Situation."
  ],
  "continuity_sources": [
    391,
    390
  ],
  "open_questions": [
    "Who is the Arch Lich, who is the black knight commanding the Death Knights, and why did the black knight spare the hidden family and withdraw?",
    "What happened to Lei Fei and the Hunters who disappeared with him?",
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "Who is the unidentified person directing Aehyang, and what are they planning?",
    "What important discussion does Lee Jungryong intend to have with Wu Heixing?"
  ],
  "safe_through": 391,
  "temporary_decisions": [
    "Render 열화신룡 as Blazing Flame Divine Dragon, distinct from Huashan Divine Dragon; use Mimi and Mimi-chan for 미미 and 미미쨩, and Third Fiend and Three Fiends for 삼괴.",
    "Render 진인 as Perfected One, 도우 as Fellow Daoist, 신니 as Venerable Nun, 환영진 as illusion formation, and 이동진 as Moving Formation; use Archmage and War Mage for 대마법사 and 워 메이지.",
    "Render 독룡각 as Poison Dragon Pavilion, 가주 대행 as Acting Family Head, 화룡갑 as Fire Dragon Armor, and 공안무력부 as Public Security Armed Forces Department.",
    "Render 사기 as death energy, 의념 as conveyed thoughts, 데스나이트 as Death Knight, 골골 as Bones, 아크 리치 as Arch Lich, 최상급 포션 as Top-Grade Potion, and 상급 포션 as high-grade potion.",
    "Render 전하 as His Highness, 돌발 퀘스트 as Sudden Quest, 다급해진 전황 as The Desperate War Situation, and 꽌시 as guanxi with an explanatory footnote; preserve Jin's vulgar historical and cultural jokes."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 신법     | **movement technique**                           |                                                       |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 마혈 | **Paralysis Acupoint** | System condition label for temporary paralysis. |
| 아혈 | **Mute Acupoint** | System condition label preventing speech. |
| 태자 | **Crown Prince** | Title of the Emperor's older brother who was reportedly assassinated. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 슬로우 | **Slow** | Spell cast five times in succession by Carus. |
| 수혈 | **Sleep Acupoint** | Acupoint whose successful strike prevents the target from resisting sleep. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 근력 | **Strength** | System attribute increased by Jin Taekyung. |
| 태자당 | **Crown Prince Party** | The faction associated with General Liao. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |

## Listed compact profiles

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 368
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 390
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force and crossed the wall into true mastery.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother; Jeok Cheongang is his Master; Cheongpung is his trusted companion and only true martial rival; his mother and sister Hayeon are among those he protects.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 390
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃392화



‘빌어먹을. 더, 더 빨리.’

쐐애애애액!

젖먹던 힘까지 쥐어짜 신법을 발휘했다. 주위의 풍경이 스쳐 지나갈 때마다 폐허로 변한 도시가 빠르게 가까워졌다.

하지만 모든 일의 결과는, 도착하기도 전에 알 수 있었다. 아니, 누군가가 알려 주었다고 해야 맞겠다.

삐빅.



- [???]가 목표를 완수하고 사라졌습니다.

- 돌발 퀘스트, [예상치 못한 습격]이 취소되었습니다.

- 당신은 퀘스트를 완수하지 못했습니다. 실패 패널티로 랜덤 스탯이 10 감소합니다.

- [근력]이 10 감소합니다.



시스템 알림을 듣는 순간, 팽팽하게 조여 오던 긴장이 탁 풀렸다.

퀘스트를 실패해서도, 스탯이 감소했기 때문도 아니다. 이것이 의미하는 바를 알기 때문이다.

그리고 도시에 가까워질수록 느껴지는 적막함과 잠시 후 눈 앞에 펼쳐진 현장은 짐작을 확신으로 바꿔 주었다.

“…….”

사방에 가득한 피와 참혹하게 널브러진 시신들. 지금껏 숱한 전투를 치르며 죽음에 익숙해진 나조차도 순간 몸이 굳을 정도였다.

‘도륙(屠戮).’

그래, 이건 도륙이다. 터트리고, 찢어발기고, 뭉개 버렸다.

살아있는 인간을 마치 개미처럼 잡아 죽인 흔적에 숨이 막혔다.

엄연한 타국 사람이자 생면부지인 나도 이럴진대, 뒤따라 도착한 공안 무력부 헌터들이 느낀 슬픔과 분노는 말로 표현할 수 없었다.

「장 웨이! 랑랑!」

「어, 어떤 새끼들이냐! 어떤 새끼들이…… 크흐흑!」

「안 돼! 으아아아!」

서로의 등을 맡기던 동료들이다. 싸늘한 시신이 되어 누워 있는 사람 중에는 이들의 형제도, 연인도 있었다.

끝없는 통곡과 고함이 울려 퍼지는 가운데, 말없이 우뚝 서 있던 한 사람이 문득 걸음을 내디뎠다.

저벅, 저벅.

그의 공허한 걸음 소리가 유난히도 크게 들리는 것은, 평소의 모습과 달리 아무런 감정도 느껴지지 않는 무감각한 표정 때문일지도 몰랐다.

곁에 서 있던 최 팀장이 나지막한 목소리로 나를 불렀다.

“진태경 씨.”

“압니다. 저도.”

하기 싫어도 해야 할 일이 있다. 바로 지금이 그랬고, 나는 힘겹게 입술을 뗐다.

“쉔.”

「…….」

“샤오 쉔!”

저벅, 저벅, 저벅.

힘주어 부른 외침에도 샤오 쉔의 발걸음은 멈추지 않았다. 부하들을 죽인 흉수들을 찾아 어딘지 모를 장소로 걸어갈 뿐이다.

결국 내가 직접 다가가 어깨를 붙잡아야 했다.

탁.

“멈춰.”

생기가 느껴지지 않는 퍼석한 목소리가 흘러나왔다.

「……놓으십시오. 가야 합니다.」

“어디로?”

「어디?」

텅 빈 눈동자로 주위를 둘러본 샤오 쉔이 말을 이었다.

「모르겠어요. 하지만 어딘가에는 있을 겁니다.」

“너…….”

「쫓아야 합니다. 무슨 수를 써서라도 찾아서, 복수할 겁니다.」

“……!”

순간 말문이 막혔다.

지금 내 눈에 비친 그는 샤오 쉔이 아니었다. 바로 몇 년 전의 나였다.

그렇기에 해야 할 말을 쉽사리 꺼낼 수 없었다.

‘어떤 심정인지 아니까.’

죽이고 싶고, 죽고 싶을 거다.

가까운 이들의 죽음이 남긴 감정은 분노와 슬픔만이 아니다. 살아남은 자에게는 그 두 가지를 합친 것보다 무거운 죄책감이 기다리고 있다.

백 명의 목숨이 남기고 간 죄책감은, 스물한 살의 젊은이가 감당하기에는 너무나도 버거운 무게였다.

‘빌어먹을.’

혀끝에서 맴도는 욕설을 삼킨 나는 녀석의 어깨를 힘주어 잡았다.

“늦었어.”

「…….」

“이미 늦었다고. 지금 당장은 놈들을 찾지 못해. 이건 짐작이 아니라 확신이야.”

시스템 알림이 알려 준 사실이니 틀림없다. 내 확신에 찬 눈빛을 마주한 샤오 쉔이 멍하니 중얼거렸다.

「늦었군요. 정말 늦어 버렸어요.」

“인정하기 싫지만…… 그래. 그게 현실이다.”

나는 녀석이 참았던 분노와 슬픔을 터트릴 줄 알았다.

몇 년 전의 내가 그랬던 것처럼 소리 내어 울고, 눈에 보이는 건 뭐든지 때려 부술 줄 알았다.

하지만 틀렸다. 샤오 쉔이 복수하고자 하는 대상은 몬스터뿐만이 아니었다.

드르르륵. 쿵.

이제야 도시로 진입하는 전차들.

작은 점이었던 것이 점점 커지며 다가오는 진군 행렬을 바라보던 샤오 쉔의 눈동자가 불꽃처럼 타오르고 있었다.

「그렇다면, 저놈이라도 죽여야겠습니다.」

‘저놈’이 누굴 가리키는 것인지는 명백했다.

랴오 상장. 이 개 같은 명령을 내린 장본인.

놈의 같잖은 명령 하나로 백 명의 헌터와 수백의 군인들이 죽었다. 내 생각에도 반드시 대가를 치러야 할 놈이 분명했다.

하지만…….

“시발, 미안하다.”

나는 참담한 심정을 느끼며 손을 뻗었다.

이상함을 느낀 샤오 쉔이 피하려 했지만, 미끄러지듯 움직인 내 손은 이미 녀석의 혈도를 스친 후였다.

툭. 투두둑!

마혈(痲穴), 아혈(啞穴), 그리고 수혈(睡穴).

전신이 마비되고 목소리가 막힌 샤오 쉔을 기다리고 있는 것은 깊은 수마(睡魔)였다.

쏟아지는 졸음을 참으려 안간힘을 쓰는지, 녀석의 눈꺼풀이 파르르 떨린다.

“지금은…… 우선 푹 자라. 저들의 죽음은 네 잘못이 아니야.”

스륵.

끝내 굳게 닫히는 눈꺼풀. 마지막으로 본 샤오 쉔의 눈에 담긴 것은 분명한 의문이었다.

‘왜, 어째서?’

그리고 그 의문은 샤오 쉔 한 사람만의 것이 아니었다.

「연대장님!」

「진태경, 당신!」

후우우웅! 쉬쉭!

분노에 찬 외침과 함께 다섯 줄기의 파공성이 일었다.

샤오 쉔의 휘하에서 중대장이라 불리는 A급 헌터들.

나는 거침없이 쇄도해 오는 그들을 향해 손을 떨쳤다.

펑!

압축된 공기가 터져 나가는 소리와 함께, 나를 노리고 날아들던 병장기가 황급히 방향을 틀었다.

허공을 격하고 날아간 장력(掌力)을 간신히 막아낸 중대장들의 신형이 주르륵 밀려난다.

내가 힘을 조절해서 망정이지, 마음 단단히 먹었다면 이 정도로 끝나진 않았을 거다.

“다들 진정해. 나도 이렇게까지 하고 싶진 않았으니까.”

「큭!」

「이게 도대체 무슨 짓거리요!」

「당신, 감히 연대장님을……!」

「호의를 이런 식으로 갚다니!」

흉흉한 분위기 속, 최 팀장이 나지막한 목소리와 함께 앞으로 나섰다.

“진태경 씨는 호의에 대한 보답을 한 것뿐입니다.”

「뭐, 뭐라고?」

“그대로 내버려 뒀다면 분노한 샤오 연대장은 랴오 상장을 죽였겠지요.”

「……랴오 상장은 죽어 마땅한 놈이오. 연대장님이 아니더라도 우리가 직접 나섰을 테고.」

“동의합니다. 하지만 귀국의 중앙위원회가 어떻게 생각할지는 모르겠군요. 특히 랴오 상장이 속해 있는 태자당에서는 더더욱.”

「……!」

“상대는 한 전선을 책임지는 최고 사령관. 그를 죽인다면 개인의 문제로 끝나지 않을 겁니다.”

최 팀장은 공안 무력부의 헌터들을 차례대로 훑었다.

천 명을 헤아리는 대병력이다. 나는 거기까지 헤아리지 않았지만, 이런 사건에 연루된다면 그들 역시 낭패를 피할 수 없다.

“오늘 일을 잊으라는 말씀은 드리지 않겠습니다. 그저 지금은 때가 아니라는 겁니다.”

흉흉하던 분위기가 가라앉기 시작하는 것이 느껴졌다.

현실적이면서도 감정에 기반을 둔 최 팀장의 말에, 공격에 가담하지 않았던 중대장 중 한 사람이 입을 열었다.

「동의하오. 당장 놈을 처리하는 건 일도 아니지만…… 그랬다가는 뒷일을 감당하기 힘들 거요.」

「…….」

「기억하시오. 우리의 형제들이 죽은 건 랴오 상장 때문만이 아니라는 걸.」

참혹한 시산혈해의 광경을 둘러본 그가 뿌득, 이를 갈았다.

「잠시만. 아주 잠시만 기다립시다. 곧 때가 올 거요.」

「허어.」

「……이런 제기랄!」

하늘을 보며 한탄하는 사람도, 치밀어 오르는 슬픔과 화를 참지 못하는 사람도 있다. 하지만 모두가 암묵적으로 동의한 것만은 분명했다.

마침내 사태가 일단락되자 최 팀장이 안도의 한숨을 내쉬었다.

“한시름 놨군요. 진태경 씨께서 샤오 연대장을 막아 주셔서 다행입니다.”

“……뭘요.”

다행. 다행이라, 이걸 다행이라고 해야 하나.

어쩔 수 없었다는 걸 알면서도 입맛이 씁쓸했다. 나는 샤오 쉔이 느꼈을 분노와 슬픔을 알고 있으니까.

“그보다 생존자들이 있는 것 같던데.”

“중년 부부와 아이 한 명이 남아 있더군요. 극도의 긴장 때문에 혼절한 상태라, 우선은 따로 옮겨 휴식을 취하게 하는 중인 것 같습니다.”

“다른 생존자는요?”

“곧 찾겠지요.”

눈살을 찌푸린 최 팀장이 내 어깨너머를 바라보며 말을 이었다.

“무능하기 짝이 없는 사령관의 명령이 떨어지면 말입니다.”

드르르륵.

요란한 소리를 내며 전진하던 장갑차가 이십여 미터 앞에서 움직임을 멈췄다.

잠시 후 삼엄한 호위 속, 살이 포동포동하게 오른 랴오 상장이 모습을 드러냈다.

「이, 이게 도대체…….」

눈 앞에 펼쳐진 참혹한 광경에 안 그래도 뽀얗던 피부가 창백하게 질린다.

허리를 굽히고 한참이나 헛구역질하는 모습을 보니, 혐오감과 동시에 저놈도 사람이었구나 하는 생각이 문득 들었다.

‘개새끼. 그래도 죄책감은 있나 보지.’

아마 이 자리의 모두가 나와 같은 생각을 떠올렸을 것이다.

하지만 다음 순간, 이어진 랴오 상장의 한 마디에 나는 잊고 있던 깨달았다.

저런 종류의 인간은, 늘 상상을 뛰어넘는다는 것을.

「아, 안 돼. 실패하면 안 되는 작전이었는데!」

“……!”

세상이 느려진 것 같았다. 슬로우 모션처럼, 사람들의 얼굴 위로 떠오르는 경악과 분노가 보인다.

나를 향해 손을 내뻗는 최 팀장의 움직임과 다급한 외침도.

“진태경 씨!”

하지만 이미 늦었다.

그가 내 이름을 외쳤을 때, 나는 이미 20여 미터의 공간을 뛰어넘어 랴오 상장의 앞에 도달해 있었다.

‘작전이라. 작전…….’

도무지 실소를 참을 수가 없었다.

마치 귀신을 바라보듯 멍한 얼굴로 나를 올려다보는 놈을 향해 손을 뻗었다.

콰드득! 우득!

그야말로 한순간이었다.

나는 공력 한 올 실려 있지 않은 힘으로 놈의 양팔을 부러트리고 무릎뼈를 으스러트렸다.

‘마지막 이성이 남아 있는 걸 다행으로 여겨라.’

딱 벌어진 입, 부릅뜬 눈. 그리고 뒤이어 터져 나온 돼지 멱따는 듯한 비명.

「끄아아아아아악!!!」

나는 눈을 까뒤집은 채 털썩 쓰러져 고통으로 경련하는 놈에게 침을 탁 뱉고 돌아섰다.

혼백이 빠져나간 얼굴로 바라보는 참모에게 한마디 해 주는 것도 잊지 않았다.

“좆 같으면 상부에 보고하세요. 이 시벌 놈들아.”

고개를 절레절레 흔든 최 팀장이 상급 포션을 들고 다가왔다.



* * *



의자는 거대했고, 또 기괴했다.

인간과 몬스터의 뼈를 이용해 만든 의자이니 당연했다.

그러나 의자의 주인만큼 기괴하고, 두려움을 자아내지는 못했다.

딱, 따닥.

살점 하나 묻어 있지 않은 손가락이 팔걸이를 장식한 두개골을 두드린다.

3미터를 훌쩍 넘어가는 큰 키와 골격. 그 위를 덮은 흑색 로브가 안개처럼 일렁였다.

그 모습은 마치 권좌에 앉은 왕과 같았고, 그리 틀린 말도 아니었다.

아크 리치(Arch Lich).

그야말로 언데드의 군주이자 죽음을 다스리는 왕이라 부를 만한 존재였다.

그러나 아크 리치 스스로는 그렇게 생각하지 않았다. 진정한 왕은 따로 있으며, 자신은 왕의 충실한 신하일 뿐이었으니까.

하지만…….

‘아직 일렀던가.’

아크 리치는 문득 아쉬움을 느꼈다.

실로 강대한 마력을 보유한 그였지만, 본래 지니고 있던 힘에 비하면 아직 한참이나 부족했다. 게다가 생각보다 쉽지 않은 전황까지.

말없이 생각에 잠겨 있던 아크 리치가 입을 열었다.

- 듣고 있느냐. 나의 종아.

어둠 속에 부복하고 있던 존재가 대답했다.

- 예. 군주시여.

- 전선을 물려라. 인간의 군대를 끌어들인다.

- 명을 받드옵니다.

- 가거라. 내 힘이 미치는 모든 군단에 명을 전하라.

자리에서 일어난 검은 기사가 천천히 물러났다.

마지막 순간, 붉게 타오르는 그의 안광에 아크 리치가 앉아 있는 의자가 담겼다.

딱. 따닥.

팔걸이에 장식된 두개골은 성인의 것이라고 하기에는 한없이 작았다.
```

## Final English reading copy

```markdown
# Chapter 392

*Damn it. Faster. Faster.*

Whoooooosh!

I squeezed out every last ounce of strength and activated my movement technique. Each time the scenery flashed past, the ruined city drew closer at terrifying speed.

But I could tell how things had ended before I even arrived. No—I should say someone had told me.

Beep.



> **System**
>
> ??? has completed its objective and disappeared.
>
> Sudden Quest, **Unexpected Assault**, has been canceled.
>
> You failed to complete the Quest. As a failure penalty, a random stat decreases by 10.
>
> **Strength** decreases by 10.

The moment I heard the System notification, the tension that had been wound tight inside me abruptly released.

It wasn’t because I had failed the Quest, nor because my stat had decreased. I knew what this meant.

The silence I felt as I drew closer to the city, followed by the scene that unfolded before my eyes moments later, changed my suspicion into certainty.

“……”

Blood covered the area in every direction, and corpses lay scattered in horrifying positions. Even I, who had grown accustomed to death after fighting countless battles, froze for a moment.

*Massacre.*

Yes. This was a massacre. They had blown people apart, torn them to pieces, and crushed them.

The sight of living humans having been hunted down and killed like ants made it hard to breathe.

If even I, an outsider from another country who had never met these people, felt that way, then the grief and rage of the Hunters from the Public Security Armed Forces Department who arrived behind me could not be expressed in words.

「Zhang Wei! Langlang!」

「W-Who the hell did this? Who the hell…? Sob…」

「No! Aaaaaah!」

These were the comrades who had entrusted each other with their backs. Among the people lying there as cold corpses were their brothers and their lovers.

Amid the endless wailing and shouting, one person who had been standing silently suddenly took a step forward.

Thud. Thud.

Perhaps his hollow footsteps sounded especially loud because, unlike his usual self, his face was utterly numb and devoid of emotion.

Team Leader Choi, standing beside me, called my name in a low voice.

“Mr. Jin.”

“I know. Me too.”

Sometimes there were things you had to do even when you didn’t want to. This was one of those times, and I painfully forced my lips apart.

“Shen.”

「…….」

“Shao Shen!”

Thud. Thud. Thud.

Despite my forceful shout, Shao Shen’s footsteps did not stop. He simply continued walking toward some unknown place in search of the criminals who had killed his subordinates.

In the end, I had to approach him myself and grab his shoulder.

Smack.

“Stop.”

A dry, lifeless voice spilled out.

「……Let go. I have to go.」

“Where?”

「Where?」

Shao Shen looked around with empty eyes before continuing.

「I don’t know. But they must be somewhere.」

“You…”

「I have to chase them. I’ll find them somehow, no matter what it takes, and I’ll have my revenge.」

“……!”

For a moment, I was unable to speak.

The man I saw before me was not Shao Shen. He was me, a few years ago.

That was why I couldn’t easily say what needed to be said.

*Because I know how he feels.*

He wanted to kill them, and he probably wanted to die as well.

The feelings left behind by the deaths of those close to you weren’t only rage and grief. For the survivor, there was guilt waiting—heavier than those two emotions combined.

The guilt left behind by a hundred deaths was far too heavy for a twenty-one-year-old young man to bear.

*Damn it.*

I swallowed the curse circling the tip of my tongue and tightened my grip on his shoulder.

“You’re too late.”

「…….」

“It’s already too late. We can’t find them right now. This isn’t a guess. I know it for certain.”

The System notification had told me so. There was no way I could be wrong.

Shao Shen met my confident gaze and muttered blankly.

「I’m too late. It really is too late.」

“I don’t want to admit it either, but… yes. That’s reality.”

I thought he would finally let his suppressed rage and grief erupt.

Just as I had done years ago, I thought he would cry out loud and smash anything he could see.

But I was wrong. The object of Shao Shen’s desire for revenge wasn’t limited to the monsters.

Rattle-rattle. Thud.

The tanks were only now entering the city.

As Shao Shen watched the advancing column draw closer from a distant speck, his eyes burned like flames.

「Then I suppose I’ll have to kill that bastard, at least.」

It was obvious who *that bastard* referred to.

General Liao. The man responsible for issuing this goddamn order.

Because of a single ridiculous order from that bastard, a hundred Hunters and hundreds of soldiers had died. Even I thought he was someone who absolutely had to pay the price.

But…

“Fuck. I’m sorry.”

Feeling wretched, I reached out.

Shao Shen sensed something was wrong and tried to evade me, but my hand moved fluidly and had already brushed his acupoints.

Tap. Tap-tap!

The Paralysis Acupoint, the Mute Acupoint, and the Sleep Acupoint.

Shao Shen’s entire body went rigid, his voice was cut off, and deep sleep began to overtake him.

His eyelids trembled as though he were struggling with all his strength to resist the drowsiness pouring over him.

“For now… get some proper sleep. Their deaths weren’t your fault.”

Sshk.

In the end, his eyelids closed firmly. The last thing I saw in Shao Shen’s eyes was unmistakable confusion.

*Why? How come?*

And Shao Shen wasn’t the only one who felt that way.

「Regimental Commander!」

「Jin Taekyung, you!」

Whoooooosh! Shing!

Along with furious shouts, five sounds of air being split apart rang out.

They were A-rank Hunters under Shao Shen’s command, men called company commanders.

I swept a hand toward them as they charged without hesitation.

Boom!

With the sound of compressed air exploding outward, the weapons flying at me abruptly changed direction.

The company commanders barely blocked the palm force that had torn through the air toward them, and their bodies slid backward across the ground.

It was fortunate that I had restrained my strength. If I had truly steeled myself, things would not have ended this easily.

“Everyone, calm down. I didn’t want to go this far either.”

「Kgh!」

「What the hell do you think you’re doing?!」

「How dare you lay a hand on the regimental commander…!」

「This is how you repay his kindness?!」

As the atmosphere grew more hostile, Team Leader Choi stepped forward and spoke in a low voice.

“Mr. Jin is only repaying the favor.”

「W-What did you say?」

“If we had left him alone, the enraged Regimental Commander Shao would have killed General Liao.”

「……General Liao deserves to die. Even if our regimental commander hadn’t done it, we would have taken matters into our own hands.」

“I agree. But I don’t know what your country’s Central Committee would think of that—especially the Crown Prince Party, which General Liao belongs to.”

「……!」

“The man you’re talking about is the supreme commander responsible for an entire front. If you kill him, it won’t end as a personal matter.”

Team Leader Choi looked over the Hunters from the Public Security Armed Forces Department one by one.

They were a force numbering around a thousand. I hadn’t thought that far ahead, but if they became involved in an incident like this, they wouldn’t be able to avoid trouble either.

“I’m not telling you to forget what happened today. I’m only saying that now isn’t the time.”

I could feel the hostile atmosphere beginning to settle.

Team Leader Choi’s words were both practical and grounded in emotion. One of the company commanders who had not joined the attack finally spoke.

「I agree. Dealing with that bastard right now would be easy, but… if we did, it would be difficult to deal with the consequences.」

「…….」

「Remember this. Our brothers didn’t die solely because of General Liao.」

After looking around at the horrific sea of corpses and blood, he ground his teeth.

「Let’s wait a little. Just a little longer. The time will come soon.」

「Haaah.」

「……Damn it all!」

Some people looked up at the sky and lamented. Others failed to contain the grief and rage surging inside them.

But it was clear that they had all reached the same tacit agreement.

Once the situation finally came to an end, Team Leader Choi let out a relieved sigh.

“We can finally breathe. It’s fortunate that you stopped Regimental Commander Shao, Mr. Jin.”

“……It was nothing.”

Fortunate. Was this really something we should call fortunate?

Even knowing that there had been no other choice, I was left with a bitter taste in my mouth. I knew the rage and grief Shao Shen must have felt.

“More importantly, it seemed there were survivors.”

“There was a middle-aged couple and one child. They apparently fainted from extreme tension, so they’re being moved somewhere else to rest for now.”

“Are there any other survivors?”

“We’ll find them soon enough.”

Team Leader Choi frowned and looked over my shoulder as he continued.

“Once the order comes down from that utterly incompetent commander, at least.”

Rattle-rattle.

The armored vehicle advancing with a deafening racket stopped about twenty meters ahead of us.

A moment later, under heavy escort, the plump General Liao emerged.

「W-What in the world…?」

At the horrific sight before him, his already fair complexion turned deathly pale.

Watching him bend over and retch for quite some time, I felt disgusted—but I also found myself thinking that he was human after all.

*You bastard. I guess you do feel some guilt.*

Everyone here had probably been thinking the same thing as me.

But the next words General Liao spoke reminded me of a lesson I had forgotten.

People like him always exceeded the limits of imagination.

「N-No. The operation wasn’t supposed to fail!」

“……!”

The world seemed to slow down.

Like a slow-motion scene, I saw shock and rage rise across the faces of the people around me.

I saw Team Leader Choi reaching out toward me and shouting urgently.

“Mr. Jin!”

But it was already too late.

By the time he called my name, I had already crossed the twenty-odd meters and arrived in front of General Liao.

*An operation. An operation…*

I couldn’t hold back a laugh.

I reached out toward the man staring up at me with a blank face, as though he were looking at a ghost.

Crack! Crunch!

It happened in an instant.

Using nothing but physical strength, without a single thread of internal energy, I broke both his arms and crushed his kneecaps.

*Consider yourself lucky I still have a shred of reason left.*

His mouth hung open. His eyes bulged wide.

Then a scream like a pig being slaughtered burst from him.

「Aaaaaaaaargh!!!」

I spat at him as he rolled his eyes back, collapsed to the ground, and convulsed in pain, then turned away.

I didn’t forget to say one thing to the staff officer staring at me with a face drained of all spirit.

“Report it to your superiors if you’ve got a fucking problem, you bastards.”

Team Leader Choi shook his head repeatedly and approached with a high-grade potion.

* * *

The chair was enormous and bizarre.

That was only natural. It had been made from human and monster bones.

But it was not as bizarre or terrifying as its owner.

Tap. Tap-tap.

A finger without a trace of flesh tapped the skull decorating the armrest.

The figure stood well over three meters tall, with an enormous frame. A black robe draped over it rippled like mist.

It looked like a king seated upon a throne, and that wasn’t entirely wrong.

The Arch Lich.

It was an existence worthy of being called the lord of the undead and the king who ruled over death.

But the Arch Lich itself did not think that way. There was a true king elsewhere, and it was merely his loyal servant.

But…

*Was it still too soon?*

The Arch Lich suddenly felt a pang of regret.

It possessed truly formidable magical power, but it was still far weaker than the strength it had once possessed. On top of that, the situation on the battlefield was proving more difficult than expected.

After silently sinking into thought, the Arch Lich opened its mouth.

“Are you listening, my servant?”

The being kneeling in the darkness answered.

“Yes, my lord.”

“Pull back the front line. We’ll draw the human army in.”

“I obey.”

“Go. Deliver my command to every legion within the reach of my power.”

The black knight rose and slowly backed away.

At the final moment, the Arch Lich’s chair was reflected in his eyes, which burned red.

Tap. Tap-tap.

The skull decorating the armrest was far too small to have belonged to an adult.
```
