<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0390.txt",
      "sha256": "a1bcaccbd2507329f2a526bef5f113e1f7f4f7fa26590954f27528428a261900",
      "bytes": 13695
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "afd67ef57e5a8a3e52dcbb651e904405cda6080c6c5a06fda8e6f230e32e166d",
      "bytes": 3859
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "1f1c60a51174ea325e76aa51e1b18e50edd00f53d125aac9b22396d948a6995c",
      "bytes": 134273
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "5a13376797e57817a0b85a3dec0fa7101ec0a538c1dbc9688774eac8de55ffa8",
      "bytes": 1168
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "02ed01a65e9afbc185f5adfe9a0ba59f86842a5808fb4cbb6c91e5f059311673",
      "bytes": 622
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "7037497293e9771d0680f46310931c5ca31b4dc180e648da87554ccc6b4edbe7",
      "bytes": 111202
    }
  ],
  "estimated_tokens": 9559
}
-->

# Durable State Update — Chapter 390

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 390. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 390. Profile updates may replace only one
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
  "chapter": 390,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 390,
    "continuity_sources": [390],
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
    "Wei Fenghu is China's Minister of National Defense under the Central Military Commission, a four-star general, and the current Chairman's right-hand man; Lei Fei remains unconfirmed dead or alive after disappearing with his department's Hunters.",
    "Sichuan Province is under martial law amid a Monster Wave exceeding 100,000 monsters, at least 300,000 initial casualties, magical communications interference, and a large undead army controlled by the Arch Lich.",
    "United Nations peacekeeping forces and international S-rank Hunters are engaged on the Sichuan front; Faye Chen prevented an east-west breach from spreading.",
    "Shao Yang is Chairman of China, Chairman of the Chinese Communist Party's Central Military Commission, and General Secretary; he has addressed the United Nations Security Council over the catastrophe.",
    "Faye Chen is an older S-rank Hunter and Great Cataclysm hero with a former film career, a low media profile, and a playful but composed manner toward Jin.",
    "Wu Heixing is an S-rank Hunter hostile toward Jin who secretly uses Sound Transmission and martial arts, including an internal-energy cultivation technique and fist-and-foot martial arts; he remains deeply resentful of Lei Fei and Jin.",
    "Lee Jungryong is the de facto head of the Ares Guild and one of the world's three strongest S-rank Hunters; he has recognized Jin's breakthrough and is now seeking an undisclosed discussion with Wu Heixing.",
    "Jin Taekyung completed Circulate Your Qi and slightly advanced the realm of Fire Gate Divine Technique.",
    "Jin Taekyung is under the nonrefusable Sudden Quest The Desperate War Situation and must reach the front quickly to defeat the enemies."
  ],
  "continuity_sources": [
    389,
    388
  ],
  "open_questions": [
    "Who is the Arch Lich, and what will happen after Jin Taekyung destroys its three servants?",
    "What happened to Lei Fei and the Hunters who disappeared with him?",
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "Who is the unidentified person directing Aehyang, and what are they planning?",
    "What important discussion does Lee Jungryong intend to have with Wu Heixing?"
  ],
  "safe_through": 389,
  "temporary_decisions": [
    "Render 열화신룡 as Blazing Flame Divine Dragon, distinct from Huashan Divine Dragon; use Mimi and Mimi-chan for 미미 and 미미쨩, and Third Fiend and Three Fiends for 삼괴.",
    "Render 진인 as Perfected One, 도우 as Fellow Daoist, 신니 as Venerable Nun, 환영진 as illusion formation, and 이동진 as Moving Formation; use Archmage and War Mage for 대마법사 and 워 메이지.",
    "Render 독룡각 as Poison Dragon Pavilion, 가주 대행 as Acting Family Head, 화룡갑 as Fire Dragon Armor, and 공안무력부 as Public Security Armed Forces Department.",
    "Render 사기 as death energy, 의념 as conveyed thoughts, 데스나이트 as Death Knight, 골골 as Bones, 아크 리치 as Arch Lich, 최상급 포션 as Top-Grade Potion, and 상급 포션 as high-grade potion.",
    "Render 시벌좌 as Lord Fuck, 반도의 빵즈 as peninsula bangzi, 짱깨 as chink, 주석 동지 as Chairman Comrade, 전하 as His Highness, and 다급해진 전황 as The Desperate War Situation; preserve Jin's vulgar historical and cultural jokes."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 시스템              | **System**                     |
| 경험치              | **EXP**                        |
| 퀘스트              | **Quest**                      |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 귀가      | **your family**                                                 |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 중상 | **Severe Injury** | System condition label causing a major drop in all stats. |
| 주모 | **Lady of the House** | Title used in Wipeng's remark that Jin Wikyung lacks a wife or household mistress. |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 청두 | **Chengdu** | Administrative capital of Sichuan Province and destination airport city. |
| 천격 | **Heavenly Strike** | A Fire Dragon Divine Spear form used by Taekyung against Hwangbo Eom. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |

## Listed compact profiles

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 389
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force and crossed the wall into true mastery.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother; Jeok Cheongang is his Master; Cheongpung is his trusted companion and only true martial rival; his mother and sister Hayeon are among those he protects.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 389
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃390화



촤아아악!

강기가 스쳐 지나간 자리, 솟구치는 목들과 함께 뜨거운 핏물이 뿜어져 나온다.

나는 볏짚처럼 쓰러지는 오우거의 몸뚱이를 밟고 높이 솟아올랐다. 목덜미에 닿는 햇볕이 따스하다.

‘거, 싸우기 딱 좋은 날씨네.’

때는 정오. 장소는 나무 한 그루 없는 황무지.

운집해 있는 천여 마리의 몬스터들 한가운데에 태양을 등진 내 그림자가 비친다.

급강하와 동시에 내리그어지는 창날의 움직임까지도.

‘천격(天格).’

콰아아아앙!

화룡의 발톱이 지상을 할퀴었다.

하늘이 쪼개지는 듯한 굉음. 지면이 수 미터 깊이로 주저앉고 흙과 돌 부스러기가 사방으로 비산한다.

전장의 중심에서 일어난 열풍(熱風)의 회오리가 칼날이 되어 몬스터들을 휩쓸었다.

콰아아아!

띠링. 띠링. 띠링…….

흙먼지로 인해 뿌옇게 물든 시야 속, 몬스터 처치를 알리는 시스템 알림과 함께 녹색 핏물이 투두둑 쏟아진다.

가볍게 손을 내젓자 먼지구름이 흩어지고 멍한 얼굴로 나를 응시하는 몬스터들이 보였다.

- 취릭?

- 크륵?

도대체 이게 무슨 상황인지 모르겠다는 듯한 눈빛들. 깊게 숨을 들이쉰 나는 공력을 실은 외침을 토해 냈다.

“쓸어-!”

그리고 다음 순간.

「와아아아아아!」

귀가 먹먹해지는 함성과 함께, 어느새 들이닥친 천여 명의 헌터들이 파도처럼 몬스터 군단을 덮쳤다.

콰드드드득!

퍼버벅!

속수무책으로 허물어지는 몬스터들을 보며 한 가지 확신이 들었다.

‘이 전투, 이겼다.’

농사가 끝났으니 이제 추수를 해야 할 때.

나는 보스 몬스터로 보이는 트윈 헤드 오우거를 향해 걸음을 옮겼다.

내 금쪽같은 경험치. 아니, 아군의 피해를 최소화하기 위해서였다.

「저놈이 우두머리다! 원거리 부대!」

“야, 야! 손 떼! 내가 처리할 테니까 털끝 하나 건드리지 마!”

하늘에 맹세컨대, 정말 요만큼의 사심도 없다.

“…….”

음, 곰곰이 생각해 보니까 맹세할 필요까지는 없을 것 같다.

- 간악한 인간이여. 부산물을 차지하려는 네 속셈이 뻔히 들여다보인다. 내 군단을 학살할 때도 탐욕을 숨기지 않았지!

“닥치고 네 할 일이나 하지? 빨리 언데드로 동족상잔 시작해.”

- 안 그래도 그러려고 했다. 자라나라 해골해…… 어?

“왜 그래?”

- 왜 내 힘이 통하지 않는 거지? 혹시 버그인가?

“……그런 단어는 또 어디서 주워들은 거야.”

점점 현대화가 진행 중인 스켈레톤 워로드가 낙담한 목소리로 말했다.

- 안으로 들어올수록 아크 리치의 지배력이 강해지는 것 같다. 아아, 군단 없는 사령관이라니. 실로 통탄을 금치 못하겠구나. 이래서야 죽은 것이나 다름없어!

“…….”

이 새끼는 본인을 뭐라고 생각하는 거지.

이제는 이미 죽어 있다고 말해 주는 것도 지겹다. 나는 내심 한숨을 내쉬며 우두머리를 향해 달려들었다.



* * *



「대승입니다! 이번에도 대승이에요!」

샤오 쉔이 발갛게 달아오른 얼굴로 외쳤다. 지금까지 열 번도 넘게 본 광경이라 이제는 나와 최 팀장도 그러려니 하고 넘기는 분위기다.

‘뭐, 신날 만도 하지.’

자그마치 천여 마리의 몬스터 대군을 전멸시키기까지 겨우 두 시간 남짓.

그것도 단 한 사람의 사망자도 없이 마무리 지었으니 기념비적인 승리인 것은 맞다. 이런 상황에서는 오히려 덤덤한 것이 이상한 거지.

「저희 쪽 피해는 중상자 스물셋, 경상자 서른 명이 전부입니다. 아, 이건 정말……!」

오줌 마려운 강아지처럼 몸을 부르르 떤 샤오 쉔이 반짝거리는 눈동자로 나를 바라봤다.

「어떻게 매번 이럴 수 있는 겁니까?」

“음. 그건 내가 강하기 때문이 아닐까.”

내 대답에 최 팀장이 살짝 어이없다는 눈빛을 보냈다.

“왜요?”

“아니. 보통 이럴 때는 운이 좋다거나, 뭐 그런 겸양의 말을 하지 않습니까?”

“보통은 그렇죠. 근데 운이 좋은 게 아니라 정말 강해서 이런 걸 어떡합니까. 안 그러냐, 쉔?”

샤오 쉔이 엄청난 속도로 고개를 끄덕였다.

「맞습니다! 형님은 최고십니다!」

“녀석. 훌륭한 아부의 표본이로구나.”

“…….”

주거니 받거니 하는 우리의 모습에 최 팀장이 고개를 절레절레 저었다.

“뭐요.”

“아닙니다. 하긴, 이래야 진태경 씨답긴 하죠.”

뭐지, 묘하게 기분 나쁘게 들리는데.

어깨를 으쓱한 나는 샤오 쉔을 향해 물었다.

“그보다 본부 쪽은?”

「아, 그렇지 않아도 전투 시작 전에 연락을 취했습니다.」

연락을 취했다는 건, 휘하에 있는 헌터 몇 명을 미리 보내 놨다는 뜻이다.

요즘 같은 세상에 전령(傳令)이 웬 말이냐 싶겠지만, 어쩔 수 없다. 마법으로 통신과 위성 감시가 불가능한 상황이니 죽어라 뛰거나 차량을 이용하는 수밖에.

그래도 조명탄을 포함한 여러 문물이 있으니 다행이다.

“또 한참 걸리겠군.”

「뒤따라오는 중이었으니 그리 오래 걸리지는 않을 겁니다.」

“피곤하겠지만 천막이라도 쳐서 애들 쉬게 해. 금방 끝나긴 했어도 전투 끝나면 진이 쏙 빠진다.”

「대형 몬스터 정도는 우리 쪽에서 처리해 놔야 하지 않을까요? 아무래도 본부가 옮기기에는 힘들 것 같아서…….」

“그것도 맞는 말이긴 하지.”

본부란 우리와 함께 움직이는 군 병력을 말한다.

나를 포함한 공안 무력부 소속 헌터들이 선봉에서 몬스터를 무찌르면, 뒤따라온 군 병력이 해당 지역과 몬스터 사체들을 ‘청소’하는 방식이었다.

굳이 청소라고 표현하는 이유는 그 목적이 부산물 노획이 아니기 때문이다.

이건 말 그대로 청소다. 내가 맡은 서부 전선의 군대는 죽은 몬스터들이 언데드로 부활할 수 없도록 사체를 토막 내고, 후방으로 옮기는 역할을 가장 많이 했다.

「저어, 형님.」

“응, 왜?”

「그간 부끄러워서 말씀드리지 못했었는데…… 현재 몇몇 고위 장교들 사이에서 이런저런 말이 나오고 있는 것 같습니다.」

“말? 무슨 말?”

샤오 쉔이 내 눈치를 살피며 조심스럽게 속삭였다.

「그, 본인들이 맡은 역할에 불만이 조금…….」

“……?”

저게 도대체 무슨 소리지.

샤오 쉔의 말을 이해하기까지는 제법 긴 시간이 필요했다. 무거운 침묵이 흐른 뒤, 나는 설마 하는 마음으로 입술을 뗐다.

“혹시 자기들도 몬스터 사체 그만 치우고 공을 세우고 싶다. 뭐 그런 거야?”

「……예.」

“아니, 이런 미친 새끼들을 봤나.”

쌍욕이 절로 튀어나오는 상황이다. 다른 전선에서는 군인들이 하루가 멀다고 죽어 나가는데, 몬스터 사체 치우기가 지겹다니.

가만히 듣고 있던 최 팀장이 침착하게 입을 열었다.

“당황하지 마십시오. 짱깨가 짱깨 했을 뿐입니다.”

저게 천 명에 가까운 중국인들 앞에서 할 소린가 싶지만, 중국인과 짱깨는 엄연히 다른 인종이다.

착한 중국인의 대표인 샤오 쉔의 얼굴은 어느새 부끄러움으로 붉어져 있었다.

「죄, 죄송합니다. 다만 장교들 전부는 아니고, 일부 인원들이 그런 불만을 품은 것으로 알고 있습니다.」

“일부 인원들이라. 그렇겠지. 그런데 한 가지 궁금한 게 있는데…….”

나는 눈살을 찌푸리며 샤오 쉔의 어깨너머를 가리켰다.

“그 일부 인원에, 저기 오는 저 인간도 포함되어 있냐?”

저 멀리, 백여 대의 장갑차와 전차가 먼지구름을 일으키며 이곳을 향해 다가오고 있었다.



* * *



드르륵, 덜컹!

황폐해진 도로를 달리는 차량이 위아래로 들썩인다. 앉아 있는 군용 차량의 창밖으로 엉망이 된 논과 밭, 무너진 민가가 드문드문 보이기 시작했다.

뒷정리가 끝난 후 나는, 아니 ‘우리’는 인근 소도시로 향하는 중이었다.

「하하, 정말 고생 많았소이다. 진 선생!」

꽉 조인 벨트로도 감출 수 없는 뱃살. 태양 아래 번쩍이는 정수리.

입고 있는 군복과 견장에 박힌 별 세 개가 아니었다면, 내가 눈앞의 장년인과 만날 일은 없었을 것이다.

「안 그래도 오늘 아침 상부에 연락이 닿았소. 진 선생의 승전보에 유엔 안보리는 물론이고 전 세계가 난리가 났어요! 내 무슨 소리인지는 모르겠지만, 한국에서는 오늘을 주모 기일이라 부른다던데…….」

시종일관 떠들어 대는 헛소리를 듣는 건 여기까지다. 나는 참지 못하고 불쑥 입을 열었다.

“주모가 뒤졌는지 살았는지, 그런 건 관심 없고요. 하나만 물어봐도 됩니까?”

「지, 진 선생?」

중국 정식 편제로는 청두군구(成都軍球). 그중에서도 일곱 개의 사단, 여단이 속한 제 13집단군 총사령관인 랴오 상장은 불안한 눈빛으로 날 바라봤다.

「왜, 왜 이러시오? 무슨 일이라도 있었소?」

“오늘 제가 이상한 이야기를 들어서요. 지금 좀 예민해졌네요.”

「누가 감히 진 선생의 심기를! 뭐든 물어보시오.」

“아, 예. 제가 여쭤볼 건 다름이 아니고…….”

나는 기름기로 번들거리는 랴오 상장의 얼굴을 빤히 바라보며 말을 이었다.

“공을 세우고 싶은 몇몇 장교들의 불만이 상당하다던데…… 혹시 알고 계셨나 해서요.”

「크흠.」

알고 있었군. 그걸 알면서도 가만히 놔뒀다니. 하도 어이가 없으려니 이제는 오히려 덤덤해진다.

그래도 명색이 아군이자 타국의 쓰리스타. 나는 최대한 침착하고 공손한 어조로 물었다.

“그 씨팔 새끼들 면상 좀 볼 수 있습니까?”

「크흐흠!」

“아니 시부럴 거, 어떤 정신 나간 놈들이 이 시국에 공을 세우고 싶다고 지랄을 해요. 막말로 지들이 나가서 싸울 것도 아니고, 일반 병사들 앞에 세우고 뒤에서 지휘봉이나 휘두를 거 아닙니까.”

「크흐흐흠!」

“몬스터 사체 치우기 귀찮다는 게 무슨 개소립니까. 왜요, 하도 보니까 정겹고 친근해져서 본인들도 사체가 되고 싶대요? 진짜 뒈져 봐야 정신을 차리지. 개 같은 거.”

「크흐흐흐흠!」

“그런 새끼들 있으면 그냥 와서 말하라고 해요. 장비 입혀서 선봉에 세워 줄 테니까. 고기 방패로 쓰면 딱이겠…….”

열변을 토하던 나는 문득 입을 닫았다. 랴오 상장의 이마에서 식은땀이 스프링클러처럼 쏟아지는 중이었다.

「…….」

“…….”

이 인간도 그 정신 나간 놈 중에 하나구만.

지하 벙커에서 핵을 쏘니 마니, 염병을 할 때부터 보통 미친놈은 아니구나 싶었는데. 정말 상당한 수준으로 미쳐 있는 게 분명하다.

“……장군님. 제정신입니까?”

「그, 그러니까 이게. 우리도 뭔가를 보여 줘야 한다. 뭐 그런 게 조금은…….」

“아니, 피해 없이 쭉쭉 잘 가고 있는데 여기서 뭘 더 보여 줘요. 헌터들이 앞에서 길 뚫고, 군대는 뒤에서 뒷수습하면서 민간인들 구하고. 잘하고 있는데 뭘 더 보여 주냐고.”

우두둑.

손가락 관절을 꺾는 내 모습에 랴오 상장이 황급히 손을 내저었다.

「어, 어허! 우리 서로 간에 반말은 하지 맙시다. 내 연배로 보나 계급으로 보나, 진 선생에게 이런 대접을 받을 사람이 아니오.」

“아주 그냥, 대접으로 대가리를 깨 버릴까.”

「뭐, 뭣이?」

“아닙니다. 잘못 들으신 거예요. 어쨌든 알겠고, 허튼 생각하지 마십시오. 지금부터는 사상자는 최소로, 민간인들 구출하면서 천천히 진격하자고요. 아시겠습니까?”

「…….」

이 인간 반응이 왜 이래?

대답 대신 눈깔을 뒤룩뒤룩 굴리는 랴오 상장을 보는 순간, 등골이 서늘해졌다.

설마…….

“이미 명령을 내린 겁니까?”

「그, 그게. 내가 지금 군납 비리 건에 연루되어 있기도 하고. 독자적으로 뭔가를 해내야 하는 시점이라…….」

“야 이 개새끼야!”

쾅!

내 발길질에 방탄 처리 되어 있는 문짝이 뜯겨 나갔다. 앞 좌석에 앉아 있던 운전병이 황급히 브레이크를 밟았다.

끼이이익!

“히익!”

잔뜩 몸을 웅크린 채 벌벌 떨던 랴오 상장이 더듬거리는 목소리로 대답했다.

「우, 우리가 지금 가고 있는 소도시에 몬스터가 있을 것 같아서 예비대로 운용 중이던 공안 무력부 헌터들을 조금 투입시켰…….」

더 들을 필요도 없었다. 내가 뭐라 다그치기도 전에, 어느새 가까워진 도시로부터 굉음이 울려 퍼졌으니까.

콰아아앙!

거대한 폭발. 솟구치는 불꽃과 연기.

그리고…….

띠링.

돌발 퀘스트를 알리는 시스템 알림이 있었다.
```

## Final English reading copy

```markdown
# Chapter 390

Whoosh!

Where the Force brushed past, hot blood spurted from rising necks.

I stepped on the body of an ogre collapsing like a bundle of straw and soared high into the air. Sunlight warmed the back of my neck.

*Perfect weather for a fight.*

It was noon. The location was a wasteland without a single tree.

In the middle of more than a thousand gathered monsters, my shadow appeared with the sun at my back.

So did the movement of the spearhead descending with my dive.

*Heavenly Strike.*

Boom!

The fire dragon’s claw raked the ground.

A deafening roar like the sky itself was splitting apart. The earth sank several meters deep, and dirt and fragments of stone flew in every direction.

A whirlwind of hot air that erupted in the middle of the battlefield transformed into blades and swept across the monsters.

Boom!

> **System**
>
> Ding. Ding. Ding…

Through the dust-blurred haze, green blood pattered down alongside the System notifications announcing the monsters’ deaths.

I casually waved a hand, scattering the cloud of dust. The monsters staring at me with dazed expressions came into view.

“Chirrik?”

“Krruk?”

Their eyes seemed to ask what in the world was happening. Drawing in a deep breath, I let out a shout loaded with internal energy.

“Wipe them out—!”

And then—

“Waaaaaaaaah!”

Along with an ear-deafening roar, more than a thousand Hunters who had arrived before I knew it descended on the monster army like a wave.

Crunch!

Wham!

As I watched the monsters collapse helplessly, one certainty took shape in my mind.

*We’ve won this battle.*

The farming was over. Now it was time to harvest.

I headed toward the Twin-Headed Ogre that looked like the boss monster.

It was for the sake of my precious EXP. No—for the sake of minimizing allied casualties.

“That one’s the leader! Ranged unit!”

“Hey, hey! Hands off! I’ll handle it, so don’t touch a single hair on its head!”

I swear to heaven, I didn’t have even the slightest ulterior motive.

……

Well, now that I thought about it, there was no need to swear.

“You despicable human. Your scheme to claim the spoils is obvious. You didn’t even hide your greed while slaughtering my army!”

“Shut up and do your job, will you? Hurry up and start having the undead slaughter their own kind.”

“I was already going to. Grow, skeletons, gro—huh?”

“What’s wrong?”

“Why isn’t my power working? Is this a bug?”

“……”

“Where did you even pick up a word like that?”

The increasingly modernized Skeleton Warlord spoke in a dejected voice.

“It seems the Arch Lich’s control grows stronger the farther inside we go. Ah, a commander without an army. I cannot express the depth of my sorrow. At this rate, I am as good as dead!”

……

What did this bastard think he was?

I was tired of telling him that he was already dead. Suppressing an inward sigh, I charged toward the leader.

* * *

“It’s a crushing victory! Another crushing victory!”

Shao Shen shouted with a face flushed red. Team Leader Choi and I had now seen this scene more than ten times, so we simply took it in stride.

*Well, I suppose he has reason to be excited.*

It had taken barely two hours to annihilate an army of more than a thousand monsters.

And we had finished the battle without a single fatality. It really was a monumental victory. In a situation like this, acting calm would be stranger.

“Our casualties are only twenty-three severely wounded and thirty lightly wounded. Ah, this is really…!”

Shao Shen trembled like a puppy that needed to pee and looked at me with shining eyes.

“How can this happen every time?”

“Hmm. Maybe it’s because I’m strong.”

Team Leader Choi gave me a look of mild disbelief.

“Why?”

“Usually, wouldn’t you say something modest, like that you were lucky?”

“That’s usually how it goes. But what can I do when it isn’t because I’m lucky? I’m actually that strong. Right, Shen?”

Shao Shen nodded at tremendous speed.

“That’s right! Hyung is the best!”

“You rascal. You’re a splendid example of flattery.”

……

Watching us trade lines back and forth, Team Leader Choi slowly shook his head.

“What?”

“Nothing. I suppose this is very much like you, Mr. Jin.”

What was that supposed to mean? Somehow, it sounded unpleasant.

I shrugged and asked Shao Shen,

“More importantly, what about headquarters?”

“Ah, I contacted them before the battle began.”

Contacting them meant that he had dispatched several Hunters under his command in advance.

In a world like this, one might wonder why anyone was still using messengers, but there was no choice. With magic making communication and satellite surveillance impossible, our only options were to run like hell or use vehicles.

At least we still had various modern conveniences, including flares.

“They’ll take a while, then.”

“They were following behind us, so it shouldn’t take too long.”

“You’re probably tired, but pitch some tents and let the men rest. The battle ended quickly, but fighting drains you completely.”

“Shouldn’t we take care of at least the large monsters ourselves? They’d probably be difficult for headquarters to move…”

“That’s a fair point.”

By headquarters, he meant the military forces moving along with us.

When the Hunters of the Public Security Armed Forces Department, myself included, defeated the monsters at the front, the military forces following behind would ‘clean up’ the area and the monster corpses.

The reason I called it cleaning up was that the goal wasn’t to collect byproducts.

This was cleaning in the literal sense. The army assigned to the western front had spent most of its time cutting up the dead monsters and transporting them to the rear so they couldn’t be resurrected as undead.

“Um, hyung.”

“Yeah? What is it?”

“I was too embarrassed to mention this before, but… it seems some of the high-ranking officers have been saying various things.”

“Saying what?”

Shao Shen studied my expression before whispering cautiously.

“They’re a little dissatisfied with the roles they’ve been assigned…”

……

What in the world was he talking about?

It took me quite a while to understand Shao Shen’s words. After a long, heavy silence, I finally parted my lips with a sinking feeling.

“Don’t tell me they want to stop cleaning up monster corpses and distinguish themselves by making some kind of achievement.”

“……”

“Yes.”

“Would you look at these crazy bastards.”

The situation was enough to make curses spill from my mouth. Soldiers were dying every day on the other fronts, and these people were tired of cleaning up monster corpses?

Team Leader Choi, who had been listening quietly, spoke in a calm voice.

“Don’t be surprised. A chink did what chinks do.”

I wondered whether that was really something to say in front of nearly a thousand Chinese people, but Chinese people and chinks were, strictly speaking, different races.

Shao Shen, the representative of all good Chinese people, had turned red with embarrassment.

“I-I’m sorry. But as far as I know, it isn’t all the officers. Only some of them are dissatisfied.”

“Some of them. Naturally. But there’s one thing I’m curious about…”

I frowned and pointed over Shao Shen’s shoulder.

“Does that ‘some’ include the man coming over there?”

In the distance, more than a hundred armored vehicles and tanks were approaching us, kicking up clouds of dust.

* * *

Rattle, clunk!

The vehicle driving along the ruined road bounced up and down. Through the window of the military vehicle I was sitting in, I began to see wrecked rice paddies and fields, along with collapsed homes scattered here and there.

After the cleanup was finished, I—or rather, ‘we’—were on our way to a nearby small city.

“Haha, you’ve really worked hard, Mr. Jin!”

The paunch that even his tightly fastened belt couldn’t conceal. His bald crown gleaming beneath the sun.

If not for the military uniform he wore and the three stars on his shoulder, I would never have had any reason to meet the middle-aged man before me.

“I contacted the higher-ups this morning, as it happens. Your victory report has thrown not only the United Nations Security Council but the entire world into an uproar! I don’t know what it means, but apparently Korea calls today the Lady of the House’s memorial day….”[^1]

That was enough of his nonstop nonsense. Unable to hold back any longer, I abruptly opened my mouth.

“I don’t care whether the Lady of the House is dead or alive. May I ask you one thing?”

“Mr. Jin?”

General Liao, commander in chief of the 13th Group Army of the Chengdu Military Region, which included seven divisions and brigades, looked at me uneasily.

“Why—why are you acting like this? Did something happen?”

“I heard something strange today, so I’m a little sensitive.”

“Who dared upset you, Mr. Jin? Ask me anything.”

“Right. What I wanted to ask was…”

I continued while staring at General Liao’s greasy, glistening face.

“I heard that some officers are extremely dissatisfied because they want to distinguish themselves. I was wondering if you knew anything about that.”

“Ahem.”

So he did know.

The fact that he had known and still left things alone was so absurd that I had become numb to it.

Still, he was technically an ally and a three-star general from another country. I asked as calmly and politely as possible.

“Could I see the faces of those fucking bastards?”

“Ahem!”

“I mean, what kind of insane idiots are throwing a fit about wanting to distinguish themselves at a time like this? To put it bluntly, it’s not as if they’re going to go out and fight themselves. They’ll just stand behind ordinary soldiers and wave their batons around while giving orders, won’t they?”

“Ahem!”

“What the hell do they mean, they’re tired of cleaning up monster corpses? What, they’ve seen so many that the bodies have become familiar and comforting, and now they want to become corpses themselves? They really won’t come to their senses until they actually die. Goddamn idiots.”

“Ahem!”

“If there are people like that, tell them to come see me. I’ll put Equipment on them and place them at the front. They’d make perfect meat shields—”

I suddenly stopped in the middle of my tirade. Cold sweat was pouring from General Liao’s forehead like water from a sprinkler.

……

This man was one of those insane idiots too.

I had suspected he wasn’t a normal lunatic ever since he had started babbling about whether to launch a nuclear weapon from an underground bunker. Now it was clear that he was insane to an impressive degree.

“…General. Are you in your right mind?”

“I-I mean, we also need to show them something. Just a little…”

“What more do you want to show them? We’ve been advancing steadily without taking casualties. The Hunters are clearing the path ahead, while the army follows behind, cleans up, and rescues civilians. We’re doing a good job. What more are you trying to show them?”

Crack.

At the sight of me popping my knuckles, General Liao hurriedly waved his hands.

“Now, now! Let’s not use informal speech with each other. Considering both my age and my rank, I’m not someone who should be treated this way by you, Mr. Jin.”

“How about I show you some respect by smashing a bowl over your head?”

“What did you say?”

“Nothing. You must have heard me wrong. Anyway, I understand. Don’t entertain any foolish ideas. From now on, let’s advance slowly, keeping casualties to a minimum while rescuing civilians. Understood?”

……

Why was this man reacting like that?

The moment I saw General Liao’s eyes rolling around instead of answering, a chill ran down my spine.

*No way…*

“Have you already given the order?”

“Well, the thing is, I’m currently implicated in a military procurement corruption scandal. This is the point where I need to accomplish something independently…”

“You fucking bastard!”

Bang!

My kick tore the armored door from its hinges. The driver in the front seat hurriedly slammed on the brakes.

Screeeeeech!

“Eek!”

General Liao huddled up and trembled before answering in a stammering voice.

“I-I thought there might be monsters in the small city we’re heading toward, so I deployed some of the Public Security Armed Forces Hunters who had been held in reserve…”

I didn’t need to hear anything more. Before I could even press him for details, a tremendous roar rang out from the city, which had already drawn close.

Boom!

A massive explosion. Flames and smoke shot into the sky.

And then—

Ding.

A System notification announced a Sudden Quest.

[^1]: In Korean internet slang, the “Lady of the House” is a tavern proprietress; calling a day her memorial day is a joke about celebrating a victory with drinks.
```
