<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0416.txt",
      "sha256": "3c2ea0682a8b25ec71df04eeda5e20b47ec080f9711bcd3c9af18a532931f080",
      "bytes": 14039
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "22907c78ed03acc5d6881c1b7de29aac27abbb21ea07424b2574e97cc1bf99bd",
      "bytes": 1440
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b8ee6d0b7bc11219702fb9a07a6525c55958b14ea5143c5a8c7d08eb04fb7753",
      "bytes": 138638
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "8395ee53ce5d439152acc3a56b3b084a8172dd33650b0c3f46fc6cb4f2852898",
      "bytes": 1270
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "43342a6b5e83dc2a695c9cd6e8f78c509f7846f0dda8e4f237b395443b34526f",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "82624739fea01a4352e4b1671917b5ad97c1bfcb1ba660fe68be75bea23f415b",
      "bytes": 1163
    },
    {
      "path": "characters/Lei Fei.md",
      "sha256": "2992a5a3aff06d48a6bd2d767ae60bf5c1579d8f6a3ceb44149497ba7a787d7f",
      "bytes": 893
    },
    {
      "path": "characters/Park Jihoon.md",
      "sha256": "9e2e7e6b5646a930e3189a638126c8edda303d5633b455245e369ad4c9d0ace1",
      "bytes": 1449
    },
    {
      "path": "characters/Wu Heixing.md",
      "sha256": "280b139466b905aed89a5ec3554910129d174dde86de566137376ac8212c57ca",
      "bytes": 762
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "f28c26c31a66e81ed6cacd0039c2b1b78794cd05f5723c0c770c2463955be870",
      "bytes": 128021
    }
  ],
  "estimated_tokens": 10875
}
-->

# Durable State Update — Chapter 416

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 416. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 416. Profile updates may replace only one
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
  "chapter": 416,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 416,
    "continuity_sources": [416],
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
    "The coalition is engaged in a frontal battle with tens of thousands of monsters advancing through dense fog.",
    "Magic Johnson is severely exhausted after using three massive area-of-effect spells, while Faye Chen continues to fight effectively.",
    "Ares Guild and the Western Front suicide squad have formed up and are advancing through the monster army.",
    "Jin Taekyung, Lee Jungryong, and Wu Heixing are advancing together as a three-S-rank strike force toward the Arch Lich.",
    "Jin Taekyung has received Hero's Soul from Team Leader Choi and is approaching a dark-shrouded city beyond the battlefield.",
    "The Skeleton Warlord is unusually unsettled and currently refuses to absorb monster mana."
  ],
  "continuity_sources": [
    415,
    414
  ],
  "open_questions": [
    "Can Jin Taekyung, Lee Jungryong, and Wu Heixing break through the monster army and reach the Arch Lich?",
    "What awaits the coalition in the city shrouded in darkness?",
    "Why has the Skeleton Warlord become unsettled and stopped wanting to absorb mana?"
  ],
  "safe_through": 415,
  "temporary_decisions": [
    "Render 아크 리치 as Arch Lich.",
    "Render 결사대 as suicide squad.",
    "Render 일인군단 as one-person army.",
    "Render 영웅의 혼 as Hero's Soul.",
    "Render 포메이션 J as Formation J, with its joke explained as “Just fucking fight.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 이정룡    | **Lee Jungryong** |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 퀘스트              | **Quest**                      |
| 로그인              | **Login**                      |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 부길드장    | **Vice Guild Master** |
| 대격변     | **Great Cataclysm**   |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 레이페이 | **Lei Fei** | Concealed Chinese S-rank Hunter and head of the Public Security Armed Forces Department in Sichuan Province. |
| 박지훈 | **Park Jihoon** | Current name of Taekyung's former middle-school classmate; Hunter in Myeongdong Guild Team 1. |
| 우헤이싱 | **Wu Heixing** | Chinese S-rank Hunter who provokes Jin and nearly draws his sword. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 라이칸스로프 | **Lycanthrope** | B-rank Gate monster species. |
| 소원 | **Sowon** | Name called out by Im Kkeokjeong during the Wyvern attack. |
| 메이지 | **Mage** | Skeleton subtype mentioned alongside Soldiers and Warriors. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 영국 | **United Kingdom** | Country associated with BCC. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 데스나이트 | **Death Knight** | Undead commander type serving under the Black Knight. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 박지훈 | 진태경 | former_middle_school_classmates | Taekyung | casual-familiar and teasing | Uses 태경아 and 너 while reconnecting after eleven years. |
| 진태경 | 박지훈 | former_middle_school_classmates | you | casual-familiar and teasing | Uses 너 while joking about Jihoon's wealth, appearance, and school memories. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 박지훈 | 이정룡 | Disciple to master | Master | terrified and pleading | Jihoon cries out to Lee as Master after Taekyung begins stabbing him. |
| 이정룡 | 박지훈 | master to Disciple | Disciple | commanding, protective, and enraged | Lee restrains himself to protect Jihoon while ordering Taekyung to stop and later carries Jihoon's mutilated body. |
| 우헤이싱 | 진태경 | hostile S-rank Hunter to foreign Hunter and provocation target | peninsula bangzi | insulting and confrontational | Wu repeatedly addresses Jin with anti-Korean slurs. |
| 우헤이싱 | 이정룡 | younger S-rank Hunter to senior Ares Guild authority | Mr. Lee | formal and deferential | Wu addresses Lee respectfully despite his usual hostility toward Koreans. |
| 데스나이트 | 인간 | enemy combatants | human | contemptuous and commanding | Used in the Death Knight's warnings to Jin. |
| 진태경 | 레이페이 | former ally and fellow Hunter | Lei Fei | blunt and solemn | Jin addresses Lei Fei by name before telling him to rest. |
| 레이페이 | 진태경 | former ally and fellow Hunter | you | familiar and respectful | Lei Fei uses 자네 and 하게 while asking Jin to help him fulfill his final mission. |
| 진태경 | 우헤이싱 | adversarial S-rank Hunters | you idiot | insulting-casual | Mocks Wu's cowardice and orders him to stop complaining. |
| 이정룡 | 우헤이싱 | senior S-rank Hunter to younger allied S-rank Hunter | Mr. Wu | polished and formally coaxing | Lee publicly draws Wu into agreement with the suicide-squad plan. |
| 진태경 | 결사대 | commander_to_subordinates | you bastards | blunt and commanding | Jin orders the suicide squad to exploit the opening and wipe out the surrounding monsters. |

## Listed compact profiles

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 415
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force and crossed the wall into true mastery.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and student, his mother and sister Hayeon are among those he protects, and the Skeleton Warlord is his captive undead commander.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 415
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 415
- **Aliases:** None
- **Role:** Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who directs Ares Guild operations.
- **Personality:** Outwardly genial, calm, and humorous; calculating, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

### Lei Fei.md

# Lei Fei (레이페이)

- **Safe through:** Chapter 415
- **Aliases:** None
- **Role:** Lei Fei is a concealed Chinese S-rank Hunter and former head of the Public Security Armed Forces Department in Sichuan Province who recovered his human identity after becoming a level-120 undead Death Knight Lord and died fulfilling his final mission.
- **Personality:** Lei Fei's recovered memories show him as dutiful, honorable, family-oriented, and willing to serve as an unseen guardian.
- **Voice:** His human voice is formal and earnest, becoming warm and playful with family.
- **Relationships:** Wei Fenghu is his maternal uncle who raised him as a son; Lei Fei married an unnamed flower-shop owner and had a daughter, trained alongside Wu Heixing, and was corrupted by the Arch Lich before Jin Taekyung restored his identity.

### Park Jihoon.md

# Park Jihoon (박지훈)

- **Safe through:** Chapter 290
- **Aliases:** Park Jihwang
- **Role:** Hunter in Team 1 of Myeongdong Guild and its covert enforcer; killed Team Leader Jung Hyunwoo after detecting wrongdoing; Jin Taekyung's former middle-school classmate; attended Hankuk University's Business Administration department but has not graduated since awakening; son of a family that has run a Hunter-related business for more than thirty years; gave a taunting, equivocal response when Taekyung accused him of sending the twenty-eight Black Hunters and threatened to end Taekyung and the Peace Guild if Taekyung advanced farther; possesses a separate phone for secret communications, knows hand-to-hand combat comparable to a Peak master's grappling technique, and used a potion to recover from Taekyung's assault before fighting beside Park Tae Seop against him; secret Disciple of Lee Jungryong who was left alive after Taekyung severed both arms and severely injured his leg and shoulder
- **Personality:** Outgoing and teasing in conversation; privately says that he and Taekyung were not close
- **Voice:** Casual, sociable, and teasing with an old classmate
- **Relationships:** Former Garam Middle School classmate of Jin Taekyung; boyfriend of an unnamed woman; works under Myeongdong Guild Master Park Tae Seop while openly challenging the Guild Master's authority

### Wu Heixing.md

# Wu Heixing (우헤이싱)

- **Safe through:** Chapter 415
- **Aliases:** None
- **Role:** Wu Heixing is a Chinese S-rank Hunter known for frequent media exposure and scandal who secretly practices martial arts, including an internal-energy cultivation technique and fist-and-foot martial arts.
- **Personality:** Arrogant, status-conscious, abusive, and fiercely proud of his power, he responds to humiliation with anger and protects himself even while his allies die.
- **Voice:** Loud, insulting, entitled, and dependent on national and political status.
- **Relationships:** He is openly hostile toward Jin Taekyung and Faye Chen, and resents Jin receiving Chairman Shao Yang's attention.

## Korean source

```text
＃416화



수만에 달하는 군세가 얽힌 치열한 전장을 가로질러 돌파한다는 것은 불가능에 가까운 일이다.

하지만…….

「휘몰아쳐라. 블리자드(Blizard)!」

「존슨. 너무 무리하는 거 아니에요? 이러면 나도 가만히 있을 수 없잖아.」

대격변의 전쟁 영웅이자, 세계 최고의 워 메이지와 궁사가 엄청난 위력의 광역 마법과 낙뢰와도 같은 화살을 퍼붓고.

「여왕 폐하를 위하여!」

“Long Live The Queen!”

혜성처럼 등장한 S급 헌터이자 영국의 왕자가 최정예 왕실 기사단을 이끌고 돌격한다면.

「포메이션 J! 모조리 쓸어버려라!」

“Fucking Jonna fight!”

“에에에에! 이꾸요잇!!!”

숭고한 희생을 각오하고 이 자리까지 온 수백의 결사대가 한 몸이 되어 나아간다면.

콰아아아아아!

콰드드드득! 서걱!

길은 열린다.

그것은 단 세 사람을 위한 길.

이 전쟁을 끝내기 위한 마지막 활로(活路)였고, 그들은 한 줄기 섬광이 되어 수만의 몬스터를 가로질렀다.

촤아아아악!

두 개의 검과 한 자루의 창에서 뿜어져 나온 휘황한 빛무리가 몬스터를 휩쓸었다.

날카로운 송곳니를 들이댄 라이칸스로프의 머리가 허공으로 솟구치고, 6m에 달하는 거대한 체구의 보스 몬스터, 트윈 헤드 오우거의 사지가 분리되었다.

각기 군단을 지휘하던 데스나이트 다섯 기가 나타나 막아섰지만 달라지는 것은 없었다.

- 군. 주. 의. 이. 름. 으. 로.

- 죽. 음. 을. 내. 리. 노. 라.

진태경이 한마디를 툭 내뱉었다.

“둘, 둘, 하나. 괜찮죠?”

이정룡이 고개를 끄덕였다.

“그렇게 하지.”

「잠깐. 그게 뭐……!」

우헤이싱이 반문하기도 전에, 두 사람은 이미 달려나가고 있었다.

단 두 걸음으로 순식간에 거리를 좁힌 그들은 망설임 없이 손에 쥔 검과 창을 휘둘렀다.

쾅!

일 합. 채찍처럼 휘어진 강기(罡氣)를 막아낸 데스나이트의 신형이 휘청인다.

마력을 뿜어내던 검이 산산이 부서지는 광경에, 데스나이트의 안광이 부릅떠졌다.

- 어. 떻……!

쾅! 퍼걱!

이 합. 삼 합. 그리고.

서걱!

끝을 알리는 번개 같은 일격.

갑옷과 함께 잘려나간 상반신이 천천히 미끄러졌다. 깊게 눌러쓴 투구 사이, 바람 앞의 촛불처럼 일렁이던 안광이 사라졌다.

각자 맡은 데스나이트의 신형이 땅에 닿기도 전에 진태경과 이정룡은 또 다른 적을 향해 달려 나가고 있었다.

「빌어먹을! 나도 있다!」

거기에 더해 한발 늦게 합세한 우헤이싱까지.

남아 있던 세 기의 데스나이트는 운명은 이미 예견된 것이나 다름없었다.

지휘관들의 소멸을 목격한 몬스터들은 본능적으로 두려움을 느끼며 물러났다.

‘더, 더, 더.’

서걱! 촤아아악!

진태경은 주위에 있는 모든 것들은 베고 부수며 나아갔다. 그리고 어느 순간 깨달았다.

‘없다.’

끝없이 앞길을 가로막던 몬스터는 이제 어디에도 보이지 않았다. 망가진 도로와 양옆으로 늘어선 광야.

그 끝에는 짙은 안개에 휩싸인 도시가 그들을 기다리고 있었다.



* * *



나와 이정룡. 우헤이싱은 아크 리치가 있을 도시를 향해 맹렬한 속도로 나아갔다.

- 간악한 인간이여. 본 사령관에게는 오랜 소원이 있다.

뭔데.

- 그건 바로…… 고향으로 돌아가 평온한 일상을 즐기는 것이다.

너 기억 없어서 고향이 어딘지도 모르잖아.

- ……어떻게 그런 심한 말을.

아, 미안하다. 그런 의도는 아니었는데. 그래서 고향이 어딘데.

- 내가 처음으로 정신을 차린 곳. 바로 한국이다. 나는 그곳을 마음의 고향으로 삼기로 했다.

“…….”

도시를 향해 달려가던 나는 멈칫했다.

‘미친놈인가.’

몬스터 주제에 국적 취득이라니. 게이트를 통한 불법 밀입국자 언데드 주제에 못 하는 말이 없다. 이렇게까지 하는 의도야 뻔하지만.

- 그러니까 제발 돌아가자.

싫은데.

- 아까부터 머리가 어지럽고 속이 울렁거린다.

신기하네. 나도 너랑 대화할수록 비슷한 증세가 일어나는 것 같은데.

- 아직 안 늦었다! 제발 멈춰! 저곳으로 가면 정말 돌이킬 수 없다!

아니지.

‘이미 늦었어.’

나는 내심 중얼거리며 걸음을 내디뎠다. 도시로 진입하자 불길하리만치 짙은 안개와 싸늘한 공기가 가장 먼저 반겨 준다.

동시에 지금까지 수없이 느꼈던 익숙한, 하지만 무언가 다른 기운이 전신을 스쳤다.

“이건…….”

끈적하고 불쾌한 기운. 내가 그것의 정체를 깨닫기까지는 그리 오랜 시간이 걸리지 않았고, 그건 이정룡과 우헤이싱 역시 마찬가지였다.

「이, 이 선생님.」

“그래, 그렇군.”

가라앉은 눈빛으로 주위를 둘러보던 이정룡이 입술을 뗐다.

“게이트(Gate)야. 어디서 그 많은 몬스터가 쏟아져 나오나 했더니, 그만한 이유가 있었어.”

이정룡의 짐작은 틀렸다. 정확히는 절반의 정답이라고 해야겠지. 작게 고개를 저은 나는 그의 말을 정정해 주었다.

“아직 게이트화가 완전히 진행된 건 아닌 것 같은데요.”

마른침을 꿀꺽 삼킨 우헤이싱이 물었다.

「네가 그걸 어떻게 알지?」

“그냥. 느낌상.”

「뭐?」

“못 믿겠으면 말고.”

「……뭐 이런 놈이.」

내 예상대로 우헤이싱은 어이없다는 표정을 지었지만, 이정룡은 달랐다.

나를 바라보는 그의 눈빛에 서린 감정은 분명 의심과 놀라움이었다.

“자네가 어떻게 그걸?”

“알고 계셨습니까?”

“방금 떠올렸지. 아주 오래전, 대격변 시절 북미에서 느꼈던 감각이었네.”

“그렇군요.”

“하지만 대격변 이후로는 단 한 번도 일어나지 않았던 현상일세. 어떻게 알았나?”

“말씀드렸다시피, 그냥 감입니다. 왠지 그럴 것 같았어요.”

“그럴 것 같았다라…….”

단호한 대답에 이정룡이 알 수 없는 눈빛으로 나를 바라본다.

하지만 내가 할 수 있는 말은 여기까지다. 어차피 사실을 말해 준다 하더라도 이해할 수 없을 테니까.

‘시스템창을 보여 줄 수 있는 것도 아니고.’

나는 고개를 들어 허공을 힐끗 바라보았다. 그곳에는 도시에 진입하자마자 눈앞에 생성된 시스템 메시지가 떠올라 있었다.

띠링.



- ???급 게이트, [어둠에 잠식된 도시]에 진입했습니다!

- 당신은 [아크 리치]의 본거지에 침입했습니다!

- 마력에 잠식된 도시는 이미 하나의 거대한 게이트로 변화 중입니다. 모든 일의 근원인 아크 리치를 처치하여 도시의 변화를 멈추고, 앞으로 일어날 재앙을 막으십시오.

- 퀘스트, [죽음에서 돌아온 자]가 생성되었습니다!

- 퀘스트가 종료되기 전까지 [로그인] 기능을 이용할 수 없습니다!



‘게이트화(化)라니.’

교과서에서나 읽었던 과거의 사건이다. 이정룡은 짙은 안개 너머를 바라보며 입을 열었다.

“게이트화는 대격변 때도 드문 현상이었지. 그러기 위해서는 매우 강력한 몬스터가 주축이 되어 마력을 뿌리내려야 하니 말일세.”

매우 강력한 몬스터라면 두고 볼 것도 없다. 나는 불쑥 한마디를 내뱉었다.

“아크 리치.”

“그래, 놈이 틀림없어. 이 도시를 마력으로 오염시켜 하나의 거대한 게이트로 만들고 있는 거겠지. 지금껏 전장에 모습을 드러내지 않은 이유도 그 때문인 것이 분명해.”

지금까지 전장에서 모습을 드러낸 몬스터의 숫자만 하더라도 20만에 달한다.

그것만으로도 엄청난 재앙이나 다름없었는데, 만약 게이트화가 완전히 끝나게 된다면?

‘끝장이야.’

분명 최후의 승자는 인간이 되겠지만, 수많은 도시가 파괴되고 수십, 아니 어쩌면 수백만 이상의 사람들이 죽을 것이다. 더 늦기 전에 막아야 했다.

“시간이 얼마 없습니다. 서둘러야 합니다.”

내 말에 이정룡이 고개를 끄덕였다.

“가급적이면 몬스터를 피해 이동하도록 하지. 놈을 상대하려면 조금이라도 힘을 아껴야 할 테니. 우헤이싱, 자네도.”

「……예.」

우리는 짙은 안개를 헤치며 나아가기 시작했다.

지난번 레이페이와 일전을 벌였던 소도시와 달리 아크 리치가 본거지로 삼은 이곳은 열 배가 넘는 면적을 자랑했고, 번화의 흔적이 남아 있었다.

무너진 고층 빌딩의 숲. 한때 도시에서 가장 화려했을, 하지만 이제는 황폐해진 번화가…….

우리는 최대한 신속하고 조용히 걸음을 옮겼다.

감각을 한껏 곤두세운 채 이동하기를 한참, 선두에서 일행을 이끌던 이정룡이 문득 입을 열었다.

“그거 알고 있나?”

“그렇게 말씀하시면 저야 모르죠. 그리고 스무고개를 하기에는 딱히 좋은 타이밍이 아닌 것 같은데요.”

즉각 내뱉은 내 대답에 이정룡이 낮은 웃음을 흘렸다.

“요즘 유난히 자네에 대해 생각하고는 하네.”

“지금 저한테 고백하시는 겁니까? 이것도 타이밍이 별론데.”

“어떤 의미에서는 그럴 수도 있겠지. 뭐랄까, 자네가 언젠가 날 뛰어넘으리라는. 그런 생각 말일세.”

“별로 신경 안 쓰셔도 될 텐데요. 어차피 십 년이 지나도 저는 부길드장님 발끝도 따라잡지 못할 겁니다.”

“하하. 정말 그렇게 생각하나?”

“아뇨. 그냥 듣기 좋으시라고 던져 봤습니다.”

“변함없이 솔직하군. 처음 자네를 만났던 그때처럼.”

“확실히 첫 소개팅 자리치고는 분위기가 영 별로였죠.”

나는 기억력이 그리 좋지 못한 편이지만, 그와의 첫 만남은 아직도 생생하게 떠오른다. 그리고 그것은 이정룡 역시 마찬가지인 듯했다.

“우리는 악연(惡緣)으로 시작되었지. 생각할수록 안타까운 일일세.”

“그러게 말입니다. 누군가의 팔을 자르는 것이 아니라, 처음부터 대화로 풀었다면 나름대로 훈훈하게 시작할 수 있었을 텐데요.”

“박지훈, 그 아이가 혈기에 실수를 저질렀어. 내 사과함세.”

“그게 어디 제자만의 잘못이겠습니까.”

“허허, 그렇군. 제대로 가르치지 못한 내 잘못도 있는 게지.”

나는 앞서 나가는 이정룡의 뒷모습을 바라보았다. 표횰한 움직임으로 건물 사이를 뛰어넘는 그는 지금 어떤 표정을 짓고 있을까.

나직하게 웃음을 흘리던 이정룡이 말을 이어 갔다.

“민우. 그 아이와는 많이 가까워진 것 같던데.”

“그럭저럭 친합니다.”

“의외로 죽이 맞는 모양이군.”

“돈을 많이 주거든요.”

“비즈니스 관계라, 듣던 와중에 반가운 말일세. 그럼 나도 자네와 친해질 수 있을까?”

나는 실소를 흘리며 대답했다.

“한 7년 전쯤인가? 헌터 훈련소에서 간식으로 단팥빵을 먹었는데, 너무 맛있어서 눈물이 났거든요. 그런데 사회에 나와서 먹으니까 별로더라고요. 그 후로는 잘 안 먹습니다.”

“이제는 배가 부르다?”

“이미 몇 대가 놀고먹을 만큼 벌었습니다. 이미 배는 꽉 찼는데, 꾸역꾸역 넣어 봤자 뭐 합니까. 배 터져서 죽지.”

“틀렸네. 사람은 언제나 배고픈 동물이야. 아무리 쑤셔 넣어도 만족할 줄을 모르지. 왜 그런지 알고 있나?”

“음. 혹시 폭식증을 앓고 계십니까?”

이정룡이 부드러운 목소리로 말을 이었다.

“탐욕 때문이야. 더 많은 돈, 명예. 혹은 이성. 끊임없이 욕심내고 갈구하지.”

“부길드장님처럼 말입니까?”

“그렇지. 나처럼.”

이정룡은 소리 내어 웃었다. 제법 커다란 웃음소리가 짙은 안개 너머로 퍼져 나갔지만, 그는 전혀 신경 쓰지 않는 모습이었다.

“웃으면 복이 오긴 하는데, 이 경우에는 몬스터가 오지 않을까 싶은데요.”

“이 근방에는 몬스터가 없어. 자네도 알고 있지 않나.”

“뭐, 좀 더 주의하자는 말입니다.”

쉬이이익!

악취가 섞인 바람이 전신을 스쳤다.

빌딩에서 빌딩으로. 이십여 미터의 거리를 뛰어넘은 우리는 계속해서 달렸다.

몬스터의 기척은 느껴지지 않았고, 보이는 건물은 점점 더 줄어들었다.

“지금부터는 속도를 줄이도록 하지.”

“어둡네요. 좁고.”

“조금만 참게. 그보다 한 가지만 더 물어봐도 되겠나?”

“뭐든지요.”

“민우, 그 아이가 이번 작전에 대해 뭐라 하던가?”

“별말은 없었고…….”

나는 이정룡과 우헤이싱을 번갈아보며 천천히 말을 이었다.

“위험하니 가지 말라 하더군요.”

“정확히는?”

“못 믿을 사람들과 가지 마라. 뭐 그런 거였죠.”

이정룡의 입가에 맺힌 웃음이 짙어졌다.

“자네도 나와 저 친구를 의심하나?”

“아뇨.”

“그럼?”

“그보다는…….”

나는 웃으며 말을 이었다.

“그보다는…… 확신이죠.”

“확신?”

“예.”

나는 웃으며 말을 이었다.

“이 씨벌 새끼들이 아크 리치보다는 내 뒤통수에 더 관심이 있구나. 뭐 그런 확신이요.”

이정룡의 발걸음이 우뚝 멈췄다.
```

## Final English reading copy

```markdown
# Chapter 416

Breaking through a fierce battlefield where an army numbering in the tens of thousands was locked in combat was nearly impossible.

But…

“Rage forth. Blizzard!”

“Johnson. Aren’t you pushing yourself too hard? If you keep this up, I can’t just stand by either.”

If the war hero of the Great Cataclysm and the world’s greatest War Mage and archer unleashed area-of-effect magic of tremendous power and arrows like bolts of lightning…

“For Her Majesty the Queen!”

“Long Live The Queen!”

If an S-rank Hunter who had appeared like a comet—the prince of the United Kingdom—led the kingdom’s elite royal knights into a charge…

“Formation J! Wipe them all out!”

“Just fucking fight!”

“Yeeeeeeah! Let’s gooo!!!”

And if the hundreds of members of the suicide squad who had come this far prepared to make a noble sacrifice advanced as one…

*Roooooar!*

*Crack-crack! Slash!*

A path opened.

A path meant for only three people.

It was the last way out that could end the war, and they crossed through the tens of thousands of monsters like a streak of light.

*Shraaaaaaash!*

A dazzling storm of light erupted from two swords and a single spear, sweeping through the monsters.

The head of a Lycanthrope that had bared its sharp fangs shot into the air, while the limbs of the six-meter-tall boss monster, the Twin-Headed Ogre, were torn apart.

Five Death Knights who had each been commanding a legion appeared and moved to block them, but nothing changed.

—In. The. Name. Of. Our. Lord.

—Let. Death. Descend.

Jin Taekyung tossed out a single remark.

“Two, two, one. Sound good?”

Lee Jungryong nodded.

“Let’s do that.”

“Wait. What the—!”

Before Wu Heixing could finish objecting, the other two had already dashed forward.

They closed the distance in an instant with only two steps, then swung the sword and spear in their hands without hesitation.

*Boom!*

The first exchange. The Death Knight staggered after blocking the Force that had curved like a whip.

Its eyes widened at the sight of the magic-infused sword shattering into pieces.

—How…!

*Boom! Crunch!*

The second exchange. The third. And then—

*Slash!*

A lightning-fast One Strike that signaled the end.

The upper half of the Death Knight’s body, armor and all, slowly slid away. Between the gaps of its deeply lowered helmet, the light in its eyes flickered like a candle before the wind, then vanished.

Before the bodies of the Death Knights they had each taken responsibility for even touched the ground, Jin Taekyung and Lee Jungryong were already charging toward another enemy.

“Damn it! I’m here too!”

Wu Heixing joined them a moment late.

The fate of the three remaining Death Knights was already as good as sealed.

The monsters that witnessed their commanders’ destruction instinctively felt fear and retreated.

*More. More. More.*

*Slash! Shraaaaaash!*

Jin Taekyung cut and smashed his way through everything around him as he advanced. Then, at some point, he realized it.

*They’re gone.*

The monsters that had endlessly blocked their path were nowhere to be seen anymore. Only a ruined road and vast plains stretching out on either side remained.

At the end of them, a city shrouded in thick fog awaited them.

* * *

Lee Jungryong, Wu Heixing, and I raced toward the city where the Arch Lich was waiting.

—Wicked human. This commander has a long-held wish.

*What is it?*

—It is to return to my homeland and enjoy a peaceful daily life.

*You don’t even remember where your homeland is.*

—…How could you say something so cruel?

*Ah, sorry. I didn’t mean it like that. So, where is your homeland?*

—The first place where I regained consciousness. Korea. I have decided to make it the homeland of my heart.

“…”

I faltered as I ran toward the city.

*Is he insane?*

A monster trying to obtain citizenship. An undead illegal immigrant who had slipped into the country through a Gate, and yet he had no shortage of things to say. His intention was obvious, of course, even if he was going this far.

—So please, let’s turn back.

*No.*

—My head has felt dizzy and my stomach has been churning for a while now.

*That’s strange. The more I talk to you, the more I think I’m developing similar symptoms.*

—It isn’t too late yet! Please stop! If we go in there, there really will be no turning back!

*No.*

*It’s already too late.*

I muttered the words inwardly and took another step.

As we entered the city, unnaturally thick fog and frigid air greeted us first.

At the same time, a familiar energy that I had felt countless times before—but somehow different—brushed across my entire body.

“This is…”

It was a sticky, unpleasant energy. It did not take me long to realize what it was, and Lee Jungryong and Wu Heixing reached the same conclusion.

“Mr. Lee…”

“Yes. I see.”

Lee Jungryong swept his surroundings with a somber gaze, then spoke.

“It’s a Gate. I wondered where so many monsters were pouring out from, and now we know. There was a reason for it.”

Lee Jungryong’s guess was wrong.

Or rather, it would be more accurate to say he was half right.

I gave a small shake of my head and corrected him.

“I don’t think the Gate transformation is complete yet.”

Wu Heixing swallowed hard and asked,

“How do you know that?”

“Just a feeling.”

“What?”

“If you don’t believe me, never mind.”

“…What kind of person says something like that?”

As I expected, Wu Heixing looked dumbfounded. Lee Jungryong, however, was different.

The emotion in his gaze as he looked at me was clearly a mixture of suspicion and surprise.

“How did you know?”

“You already knew?”

“I just realized it. It was a sensation I felt in North America a very long time ago, during the Great Cataclysm.”

“I see.”

“But it hasn’t happened even once since the Great Cataclysm. How did you know?”

“As I said, it’s just a feeling. I had a hunch.”

“You had a hunch…”

Lee Jungryong looked at me with an unreadable expression after my firm answer.

But that was all I could say. Even if I told him the truth, he would not be able to understand it anyway.

*It’s not as if I can show him the System window.*

I raised my head and glanced at the empty air. A System message had appeared before my eyes the instant we entered the city.

*Ding.*

> **System**
>
> You have entered a ???-Grade Gate, **City Consumed by Darkness**!
>
> You have infiltrated the stronghold of the **Arch Lich**!
>
> The city consumed by mana is already transforming into one enormous Gate. Defeat the Arch Lich, the source of everything, to stop the city’s transformation and prevent the catastrophe that will follow.
>
> Quest **One Who Returned from Death** has been created!
>
> You cannot use the **Login** function until the Quest ends!

*Gate transformation.*

It was something I had only read about in textbooks—a phenomenon from the distant past.

Lee Jungryong gazed beyond the thick fog and spoke.

“Gate transformations were rare even during the Great Cataclysm. For one to occur, an extremely powerful monster had to serve as its core and anchor its mana in the area.”

There was no need to consider which extremely powerful monster that might be.

I blurted out a single name.

“The Arch Lich.”

“Yes. It has to be him. He must be contaminating the city with mana and turning it into one enormous Gate. That must also be why he has not shown himself on the battlefield until now.”

The number of monsters that had revealed themselves on the battlefield so far was close to two hundred thousand.

That alone was an unprecedented catastrophe. But if the Gate transformation were to be completed…

*We’re finished.*

Humanity would undoubtedly emerge victorious in the end, but countless cities would be destroyed, and hundreds of thousands—no, perhaps millions—of people would die.

We had to stop it before it was too late.

“We don’t have much time. We need to hurry.”

Lee Jungryong nodded at my words.

“We should avoid the monsters as much as possible. We’ll need to conserve even the smallest amount of strength to face him. Mr. Wu, you as well.”

“…Yes.”

We began moving through the thick fog.

Unlike the small city where I had fought Lei Fei last time, this place—the Arch Lich’s stronghold—covered more than ten times the area and still bore traces of having once been a bustling city.

A forest of collapsed skyscrapers. A downtown district that must once have been the most dazzling part of the city, but was now desolate…

We moved as quickly and quietly as possible.

After traveling for some time with our senses stretched to their limits, Lee Jungryong, who had been leading the group, suddenly spoke.

“Did you know?”

“If you put it like that, of course I don’t. And this doesn’t seem like a particularly good time to play Twenty Questions.”

Lee Jungryong let out a low laugh at my immediate answer.

“These days, I find myself thinking about you more than usual.”

“Are you confessing your feelings to me? This is a bad time for that too.”

“In a sense, perhaps I am. How should I put it? I find myself thinking that you will surpass me someday.”

“You don’t have to worry about that. Even after ten years, I won’t be able to catch up to your heels, Vice Guild Master.”

“Haha. Do you really think so?”

“No. I just said it because I thought you’d like to hear it.”

“You’re as honest as ever. Just like when I first met you.”

“That first blind date was certainly a strange atmosphere.”

My memory was not particularly good, but I could still remember my first meeting with him vividly.

And it seemed Lee Jungryong felt the same way.

“We began as enemies bound by a bad fate. The more I think about it, the more regrettable it seems.”

“Tell me about it. If we had talked things out from the start instead of cutting someone’s arm off, we might have been able to begin on relatively friendly terms.”

“Park Jihoon, that boy, made a mistake in the heat of the moment. I apologize.”

“How could that have been the Disciple’s fault alone?”

“Heh. I see. Then it was also my fault for failing to teach him properly.”

I watched Lee Jungryong’s back as he moved ahead of us. He leaped between buildings with effortless movements, and I wondered what expression he was wearing now.

Lee Jungryong let out another quiet laugh and continued.

“You seem to have grown quite close to Minwoo.”

“We’re reasonably friendly.”

“You two seem to get along surprisingly well.”

“He pays me a lot.”

“A business relationship. That’s good to hear. Then do you think I could become close to you as well?”

I answered with a snort of laughter.

“Maybe seven years ago? I ate red bean bread as a snack at Hunter training camp. It tasted so good that I cried. But when I ate it after entering society, it wasn’t very good. I haven’t really eaten it since.”

“So now you’re full?”

“I’ve already earned enough for several generations to live without working. My stomach is already full, so what’s the point of forcing more down? I’ll just burst and die.”

“You’re wrong. Humans are always hungry creatures. No matter how much they stuff themselves, they never know satisfaction. Do you know why?”

“Hmm. Do you happen to suffer from binge-eating disorder?”

Lee Jungryong continued in a gentle voice.

“Greed. More money, more honor, or the opposite sex. We constantly desire and crave more.”

“Like you, Vice Guild Master?”

“That’s right. Like me.”

Lee Jungryong laughed aloud. His fairly loud laughter spread through the thick fog, but he did not seem concerned in the slightest.

“Laughter is supposed to bring good fortune, but in this case, don’t you think it might bring monsters instead?”

“There aren’t any monsters in this area. You know that too, don’t you?”

“Well, I’m just saying we should be a little more careful.”

*Whoooooosh!*

A foul-smelling wind brushed across my entire body.

From building to building. Leaping across gaps of more than twenty meters, we continued running.

We could not sense any monsters, and the buildings around us gradually grew fewer.

“Let’s slow down from here.”

“It’s dark. And narrow.”

“Bear with it for a little longer. More importantly, may I ask you one more thing?”

“Anything.”

“What did Minwoo say about this operation?”

“He didn’t say much…”

I looked at Lee Jungryong and Wu Heixing in turn before continuing slowly.

“He told me not to go.”

“More precisely?”

“Don’t go with people you can’t trust. Something like that.”

The smile around Lee Jungryong’s mouth deepened.

“Do you suspect me and that fellow too?”

“No.”

“Then?”

“If anything…”

I continued with a smile.

“If anything, I’m certain.”

“Certain?”

“Yes.”

I kept smiling as I went on.

“These fucking bastards are more interested in the back of my head than the Arch Lich. That’s what I’m certain of.”

Lee Jungryong’s footsteps stopped dead.
```
