<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0439.txt",
      "sha256": "3c2b3d315e5359bf51308dac4220723974bae86f97af005a4a594b3a3cbb8865",
      "bytes": 13558
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "5f3d4814799d6437c75b73b44f5bd5174e9d575ee7f9f020ee6236997026edc0",
      "bytes": 2049
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "6542e5948c0a0e06062b035673e74493aa492af66e03e95e2af3660191678da8",
      "bytes": 143402
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "cc13826f1ab71b574c06d58882199d4b3734401e1c1c9c654e7c0501907ba285",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "3f14f4214b1ddcf23eef76ffc68e448208c49de408c411c4481a3505b90effe9",
      "bytes": 1416
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "bb32e7a44919df20373b58a8f42ca0d2eb83b79db8de9e5d8e1c3e2a4e20fc69",
      "bytes": 622
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "bc8c79344a1b13062844571c7a4109b2beefc98822e0698ed6958d88115245bb",
      "bytes": 136527
    }
  ],
  "estimated_tokens": 9412
}
-->

# Durable State Update — Chapter 439

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 439. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 439. Profile updates may replace only one
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
  "chapter": 439,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 439,
    "continuity_sources": [439],
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
    "Mungyeong continues traveling with Jin Taekyung's group aboard the fast ship.",
    "Jin Taekyung has opened his Middle Dantian, and Jeok Cheongang has begun supervising his training.",
    "Taekyung's fabricated account attributes the opening of his Middle Dantian to a dream involving a sword-wielding old man identified as Lü Dongbin.",
    "Mungyeong suspects Taekyung's rapid advancement reflects demonic, heterodox arts, while Jeok rejects that conclusion.",
    "Jeok says Taekyung broke through the Supreme Peak wall and opened his Middle Dantian in only two years.",
    "Jeok describes Taekyung and the Sword Saint's Disciple as divine dragons beyond ordinary understanding.",
    "Jeok has ordered Taekyung to stay away from Mungyeong.",
    "The group is traveling toward Hubei, and Taekyung intends to alternate between the modern world and Murim during the journey.",
    "Taekyung has logged out aboard a private jet bound for Korea, with the Skeleton King present."
  ],
  "continuity_sources": [
    438
  ],
  "open_questions": [
    "Why does Mungyeong continue accompanying Jin Taekyung's group despite being unable to explain the impulse?",
    "How did Jin Taekyung actually open his Middle Dantian?",
    "What confidential matter is Jin Wikyung withholding?",
    "Are Taekyung's suspicions about the mysterious patterns and symbols found in both worlds correct?"
  ],
  "safe_through": 438,
  "temporary_decisions": [
    "Render 노부 as “this old man” or “I,” and 노야 as “Old Master.”",
    "Preserve Middle Dantian, Supreme Peak, Jiannan Chun, Sound Transmission, and divine dragons as established terminology.",
    "Keep Mungyeong's medical-apprentice voice restrained and his Slaughter Saint voice dry and blunt.",
    "Retain Taekyung's profanity and modern comic references in his narration and dialogue."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마정석     | **Magic Gem**         |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 평화 | **Peace Guild** | Guild name. |
| 대한민국 | **Korea** | Country reference. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 아마존 | **Amazon** | Region referenced in Taekyung's crude joke. |
| 청와대 | **Blue House** | Presidential office mentioned in an online comment about proposed legislation. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 대통령 | **President** | Title for Korea's head of state. |
| 주석 | **Chairman** | Political title used for Xiao Yang. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 438
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 438
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, and can perceive the texture of qi well enough to sever layered magic.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and student, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 438
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃439화



뻑!

이마를 정통으로 맞은 스켈레톤 킹의 신형이 휘청거렸다.

하지만 그것도 잠시뿐. 충격으로 쳐 올려진 머리를 멀쩡히 원위치시킨 녀석이 득의양양하게 웃었다.

“후후, 이 정도는 간지럽지도 않다.”

“아, 맞다. 너무 감쪽같아서 순간 헷갈렸네.”

이미 죽어 넋이라도 있고 없는 언데드 몬스터가 고통을 느낄 리가 있나. 정말이지, 매직 존슨이 전신 성형 하나는 기똥차게 해 놨다.

작게 혀를 차는 내 모습에 스켈레톤 킹이 어깨를 으쓱거렸다.

“이 몸을 나약한 인간과 동급으로 취급하면 곤란하다.”

“당연히 동급으로 취급 안 하지. 넌 언데드 몬스터잖아.”

“언데드 몬스터라니! 이 몸은 미국 조지아주 애틀랜타에서 나고 자란 스톤 킹이다!”

“야, 야!”

미친놈이 갑자기 소리를 지르고 난리야.

황급히 공력을 일으켜 소리를 차단한 나는, 곤히 잠들어 있는 사람들을 보며 안도의 한숨을 내쉬었다.

“애초에 영어도 잘 못하잖아.”

“인터넷에서 몇 가지를 배웠다. 단 두 마디만 할 줄 알면 의사소통에는 아무런 문제 없다더군.”

“해 봐.”

미국 조지아주 애틀랜타 토박이인 스톤 킹 씨가 당당하게 입을 열었다.

“하와유. 아임 파인 땡큐. 앤 유?”

“……너 이 새끼 한국인이지.”

얼굴은 할리우드인데, 구사하는 수준이나 발음은 신토불이다.

고개를 절레절레 내젓는 내 모습에 스켈레톤 킹이 충격받은 얼굴로 물었다.

“이, 이 몸의 영어가 그 정도로 엉망이란 말인가?”

“응. 그러니까 그냥 한국 혼혈아인 걸로 하자. 어차피 네 신상 궁금해할 사람도 없으니까.”

“그럼 조지아주 애틀랜타에 입양된 것으로…….”

“아니, 시벌. 애틀랜타에 꿀 숨겨놨냐? 세상 모든 보물이 그곳에 있어?”

“그래도 뭔가 있어 보이지 않나. 백인은 세계 각국의 여자들에게 인기가 좋다고 인터넷에서 봤다. 심지어 이 몸은 미남이지.”

“그럼 뭐 해, 고추도 안 서는데.”

“……!”

말문이 턱 막혀 있던 스켈레톤 킹이 바들바들 떨리는 손가락으로 나를 가리켰다.

“어떻게 그리 심한 말을!”

“더 심한 말도 할 수 있으니까 헛소리 그만하고. 몬스터인 거 들통나기 싫으면 이거나 끼고 다녀라.”

내가 인벤토리에서 소환한 물건을 건네받은 스켈레톤 킹이 분노도 잊은 채 고개를 갸웃거렸다.

“간악한 인간, 이게 뭐지?”

“매직 존슨이 준 선물. 미국에서 급하게 공수해 오느라 많이 늦었다더라.”

“그 고마운 인간이? 나한테 반지를?”

스켈레톤 킹이 심각한 표정으로 내가 준 반지를 바라보았다.

“혹시 이거, 인간들 사이에서 프러포즈라고 부르는 그것인가?”

“뭐래, 미친놈이. 그냥 통역 마법이 걸린 반지야.”

“흠. 고맙긴 하지만 생김새가 투박하구나. 다이아몬드처럼 반짝이는 것도 아니고. 왕의 품격에는 어울리지 않아.”

“매직 존슨이 친분이 있는 대마도사에게 특별 제작을 부탁한 거라 성능은 최상급. 부르는 게 값일걸.”

“다시 보니 고귀한 품격이 느껴지는군. 왕의 권위를 세울 수 있겠어.”

“…….”

이 새끼 진짜 얄밉네.

아무래도 스켈레톤 워로드였을 때보다 훨씬 강해지고, 훨씬 미친놈이 되어 버린 것이 틀림없다.

그러거나 말거나 뿌듯한 표정으로 자신의 중지에 반지를 끼운 녀석은 정장 안감에서 스마트폰을 꺼냈다.

저것 역시 매직 존슨에게 선물 받은, 마정석이 내장된 고가의 최신형 스마트폰이다.

“뭐 하냐.”

“고마운 인간에게 이 몸이 친히 감사 인사를 전해야겠다.”

“의외로 기본은 되어 있네. 문자 보내게?”

“간악한 인간.”

“응?”

스켈레톤 킹이 한심하다는 눈빛으로 나를 바라보며 말했다.

“요즘 세상에 누가 문자를 보내나? 당연히 SNS지.”

“……어, 그래.”

“이미 맞팔도 했다. 디엠 보내는 법도 배웠지.”

스켈레톤 킹의 스마트폰 화면을 바라본 나는 입을 딱 벌렸다.

세상에, 진짜였네. SNS 계정이 있는 언데드 몬스터라니. 이 어플은 본인 인증도 안 하나?

하지만 더욱 놀랄 일은 따로 있었다.

“……팔로워가 5천?”

“숫자를 정확히 말하도록. 5,134명이다. 일주일도 걸리지 않은 대기록이지.”

“아니, 뭔데 이거? 조작 아냐?”

“역시 잘생긴 게 최고 아니겠나. 이 몸의 얼굴을 프로필 사진으로 해 놨을 뿐인데 전 세계에서 무수한 맞팔의 요청이 쏟아지더군. 후후.”

거만한 표정으로 대답한 스켈레톤 킹이 매직 존슨을 향해 메시지를 보내기 시작했다.



Good human. I'm fine thank you. and you?



내용을 확인한 나는 작게 한숨을 내쉬었다.

“너, 다른 사람한테는 메시지 보내지 마라.”

“어째서?”

“보내지 말라면 보내지 마. 이 새끼야.”

조지아주 애틀랜타는 무슨.

경기도 조지아시 애틀랜타구 토박이라고 하는 게 더 신빙성 있겠다.

눈앞이 아찔해질 정도의 한국식 영어는 통역 마법으로도 어쩔 수 없는 모양이었다.

“이대로면 아마존 열대 우림에서 수백 년간 전통을 지키며 살아온 아카부타크치 부족도 네가 미국인이라고 생각 안 할걸.”

“음. 정확히 무엇을 말하는지는 모르겠지만 왠지 모르게 구체적이라서 더 열 받는군.”

“어쨌건 그렇게 해. 들통나면 골치 아픈 정도로 안 끝난다.”

현재의 내 이미지가 아무리 좋다고 해도 스켈레톤 킹의 정체가 알려진다면 상당한 후폭풍을 각오해야 할 것이 분명했다.

나는 고개를 돌리며 물었다.

“안 그래요, 최 팀장님?”

대각선 옆자리. 몇 분 전부터 홀로 잠에서 깨어 있던 최 팀장이 대답했다.

“그렇지 않아도 스켈레톤 킹…….”

“스톤 킹이다. 미스터 킹이라고 부르도록.”

단호하게 말을 잘라 낸 스켈레톤 킹을 빤히 바라보던 최 팀장이 한숨처럼 말을 이었다.

“어쨌건 미스터 킹의 거취에 관한 문제는 모든 가능성을 염두에 두고 있습니다. 우선 언론 및 각종 미디어에 대한 노출을 피하는 것이 최선이겠죠.”

“거부하겠다. 당당하게 세상에 모습을 드러낼 것이다.”

“그래? 최 팀장님, 해외 불법 밀입국자 처벌이 어떻게 되죠?”

최 팀장이 즉각 대답했다.

“볼 것도 없이 추방이죠. 벌금이나 징역도 각오해야 하고요.”

“그럼 마계 불법 밀입국자는요?”

“단 한 번도 전례가 없는 일이긴 한데, 경찰 대신 대규모 레이드 팀이 출동할 겁니다.”

“그렇대.”

말없이 눈동자를 뒤룩뒤룩 굴리던 스켈레톤 킹이 입을 열었다.

“……어쩔 수 없군. 아직 세상이 이 몸을 받아들일 준비가 되지 않았으니 한동안은 자중하도록 하지.”

“당연히 그래야지. 인벤토리에서 평생 자중하기 싫으면.”

“아, 알겠다.”

가장 큰 골칫덩이는 해결 완료.

이제 남은 두 번째 골칫덩이가 문제인데…… 이건 맨몸으로 부딪칠 수밖에 없다.

선택지가 없어서가 아니라 앞으로의 행보에 도움이 될 일이기 때문이다.

‘귀찮지만 어쩔 수 없지.’

조용히 좌석 팔걸이를 두드리며 생각에 잠겨 있던 내가 불쑥 입을 열었다.

“지금 국내 분위기는 어때요?”

최 팀장의 굵고 짧은 대답이 돌아왔다.

“미쳤습니다.”

“……그 정도예요?”

“누군가 사법고시에 합격하면 사는 동네와 모교에 현수막이 걸리고, 지역 신문에 토막 기사가 실립니다. 그런 사법고시 합격자가 한 해에 1500명이 넘는데, 하물며 진태경 씨는 어떻겠습니까?”

최 팀장은 딱 들어맞는 비유와 함께 허공을 클릭했다.

좌석에 설치된 홀로그램 화면은 수많은 인터넷 기사들로 빽빽하게 채워져 있었다.



[마침내 그가 돌아오다.]

[진태경, 그는 누구인가? 중국 국민들을 대표해 고개 숙인 샤오 양 주석. S급 헌터들의 경외 어린 환송…….]

[마지막까지 생존자들을 구출하기 위해 고군분투한 젊은 영웅, 마침내 조국의 품으로.]



국내 언론뿐만이 아니다. 이번 사건의 중심지였던 중국은 물론이고, 해외 각국에서 내 귀국과 향후 거취에 관한 기사를 쉴 새 없이 쏟아내고 있었다.

충분히 알고 있었고, 예상했던 일이었지만 5분 전 올라온 어느 인터넷 기사에 첨부된 사진을 보고는 입을 쩍 벌릴 수밖에 없었다.

“잠깐. 설마 저게 다 사람이에요?”

“몬스터는 아니니까 맞을 겁니다.”

“오메, 시벌…….”

인터넷 기사에 첨부된 사진에는 인천 공항을 물샐 틈 없이 메운 인파가 담겨 있었다.

수천 명? 아니, 수만 명이다.

멍하니 화면을 바라보는 내 귓가로 최 팀장의 목소리가 이어졌다.

“일대 교통이 마비되었고 군경 통제하에 카 퍼레이드도 준비되어 있습니다.”

“예? 카 퍼레이드요?”

“제가 말씀 안 드렸습니까?”

“지나가듯 말씀하셔서 농담인 줄 알았죠. 아니, 뭐 이렇게까지.”

최 팀장이 단호하게 고개를 저었다.

“이렇게까지 해야 합니다. 대한민국을 대표하는 새로운 S급 헌터니까요.”

“그래도 이건 너무 과한데, 이러다가 대통령도 오겠네.”

“아, 그건 정말 제가 말씀 못 드렸군요.”

“예?”

“옵니다. 오늘 오전에 청와대 쪽에서 먼저 연락 왔습니다. 기내에서 말씀드린다는 게 깜빡 조는 바람에 그만.”

순간 사고가 정지했다.

인천 공항에서 나를 기다리고 있는 수만 명의 인파. 마비된 도로와 화려한 카 퍼레이드. 거기에 대통령까지 온단다.

할 말을 잃은 채 침묵하던 나는 목소리를 쥐어 짜냈다.

“……진짜요? 농담 아니고?”

“예. 악수 한번 하고, 포토라인에 서서 함께 사진 찍자고 합니다.”

“아니, 최 팀장님. 저는 정치 잘 몰라요. 괜히 잘못 얽혔다가 문제 생기면 완전히 나가린데.”

“저도 진태경 씨의 생각은 알고 있습니다. 그래서 좋은 말로 거절하려 했는데, 저쪽에서도 단단히 마음먹은 모양입니다. 쉽지 않았어요.”

“그래도 거절하셨어야죠. 아무리 제가 평화 길드 소속이라고는 해도 그걸 최 팀장님이 마음대로 결정하시면 어떡합니까.”

아무리 서로 신뢰하는 관계이며 시간이 없었다고 해도, 이런 건 내게 양해를 구했어야 하는 일이다.

내 굳은 얼굴에 최 팀장이 미안한 듯한 표정으로 고개를 숙였다.

“죄송합니다. 세금 감면을 비롯한 여러 가지 좋은 조건을 제시하길래 진태경 씨께도 득이 될 거라 생각해서 그만.”

“됐고요, 지금이라도 전화하셔서 없던 일로…… 그런데 세금 감면이요?”

“네. 아크 리치에게 걸려 있던 현상금이 있지 않습니까. 중국 정부가 진태경 씨에게 지급하면 우리나라 법으로는 국내 거주자의 역외 소득에 해당되는데…….”

“잠깐. 그래서 내야 하는 세금이 총 어느 정도인 겁니까?”

“모르긴 몰라도 몇조는 내야 할 겁니다. 현상금만 무려 50조니까요. 정말 단순하게 생각해서 10퍼센트만 뗀다고 해도 어마어마한 액수죠. 물론 남을 액수가 훨씬 크지만요.”

“……그렇긴 한데.”

“진태경 씨께 양해를 구하지 않은 점. 다시 한번 사과드립니다. 이번 일은 없던 것으로 청와대 쪽에 전달하겠습니다.”

나는 딱딱하게 굳은 얼굴로 고개를 끄덕였다.

“팀장님. 두 번 다시 이런 일은 없어야 할 겁니다.”

그래, 곧 수십 조의 돈을 거머쥐게 될 나다. 당당하게 법에 따라 세금을 내도 엄청난 부자가 된다.

비록 저쪽에서 요구하는 조건이 별것 아니더라도, 고작 세금 감면을 위해 정치권과 얽힐 순 없다. 그건 피해야 한다.

‘그까짓 몇조. 시원하게 내면 그만이지.’

고민을 훌훌 털어 버린 나는 푹신한 좌석 시트에 몸을 기댔다.



* * *



펑, 퍼퍼펑!

인천 공항. 수백 대가 넘는 카메라가 동시에 플래시를 터트렸다.

철저한 통제 속에 마련된 포토라인에는 완전히 상반된 직업을 가진 두 사람이 환한 웃음을 지으며 악수를 나누고 있었다.

“진태경 씨. 정말 고생 많으셨습니다.”

“어휴, 별말씀을요. 대통령님도 요즘 바쁘시죠?”

그리고 그 광경을 지켜본 스켈레톤 킹은 생각했다.

‘이런 간악한 인간을 보았나.’

모든 것이 계획대로 되었다는 듯, 흐뭇하게 웃고 있는 최 팀장을 포함한 짤막한 소감이었다.
```

## Final English reading copy

```markdown
# Chapter 439

*Smack!*

The Skeleton King’s body staggered after taking the blow straight to the forehead.

But only for a moment. He reset his head, which had been knocked upward by the impact, and grinned smugly.

“Heh heh. That barely tickled.”

“Oh, right. It looked so convincing that I got confused for a second.”

Whether it had a soul or not, there was no way an undead monster that was already dead could feel pain. Magic Johnson really had done one hell of a job with his full-body plastic surgery.

As I clicked my tongue softly, the Skeleton King shrugged.

“You must not treat this king as an equal to a weak human.”

“Of course I don’t treat you as an equal. You’re an undead monster.”

“An undead monster? This king is Stone-King, born and raised in Atlanta, Georgia, United States!”

“Hey, hey!”

What the hell was wrong with this lunatic? Why was he suddenly shouting?

I hurriedly raised my internal energy to block the sound, then let out a sigh of relief as I looked at the people sleeping soundly.

“You couldn’t even speak English properly to begin with.”

“I learned several things from the Internet. They said communication would not be a problem as long as I knew only two phrases.”

“Go ahead, then.”

Mr. Stone-King, a proud native of Atlanta, Georgia, United States, opened his mouth.

“How are you. I’m fine, thank you. And you?”

“…You’re Korean, aren’t you, you bastard?”

He had a Hollywood face, but his skill and pronunciation were pure homegrown Korea.

As I shook my head in disbelief, the Skeleton King asked with a shocked expression,

“Is this king’s English truly that terrible?”

“Yeah. So let’s just say you’re Korean mixed-race. It’s not like anyone’s going to be curious about your personal details anyway.”

“Then I was adopted by a family in Atlanta, Georgia…”

“No, for fuck’s sake. Did you hide honey in Atlanta? Is every treasure in the world supposed to be there?”

“But it sounds impressive, does it not? I read on the Internet that white men are popular with women all over the world. Besides, this king is handsome.”

“What good is that when you can’t even get it up?”

“……!”

The Skeleton King, who had been rendered speechless, pointed at me with a trembling finger.

“How could you say something so cruel?”

“I can say worse, so stop talking nonsense. If you don’t want people finding out you’re a monster, wear this around.”

The Skeleton King accepted the object I had summoned from my Inventory and tilted his head, forgetting his anger.

“Vile human, what is this?”

“A gift from Magic Johnson. He said it took a long time because he had to rush it over from the United States.”

“That gracious human? A ring for me?”

The Skeleton King stared at the ring I had given him with a serious expression.

“Is this perhaps what humans call a proposal?”

“What the hell are you talking about, you lunatic? It’s just a ring with translation magic on it.”

“Hmm. I appreciate the gift, but its appearance is rather crude. It does not sparkle like a diamond, either. It is unbefitting of a king’s dignity.”

“Magic Johnson commissioned a grand mage he knows to make it specially, so its performance is top-class. It’s probably worth whatever they ask for it.”

“Now that I look again, I can sense its noble dignity. It should be enough to establish a king’s authority.”

“……”

What an irritating bastard.

There was no doubt about it. He had become far stronger—and far crazier—than he had been as the Skeleton Warlord.

Regardless, he slipped the ring onto his middle finger with a satisfied expression, then pulled a smartphone from the lining of his suit.

That, too, was an expensive, cutting-edge smartphone with a Magic Gem built into it, another gift from Magic Johnson.

“What are you doing?”

“This king must personally express his gratitude to the gracious human.”

“You’ve got better manners than I expected. Are you going to send him a text?”

“Vile human.”

“Huh?”

The Skeleton King looked at me as though I were pathetic and said,

“Who sends texts in this day and age? Naturally, one uses social media.”

“…Uh, sure.”

“I have already followed him, and he has followed me back. I have also learned how to send direct messages.”

I stared at the screen of the Skeleton King’s smartphone, my mouth falling open.

Holy shit. It was real. An undead monster with a social media account. Did this app not even require identity verification?

But something else was even more surprising.

“…You have five thousand followers?”

“State the number accurately. It is 5,134. A record achieved in less than a week.”

“What the hell? Is this fake?”

“Is being handsome not the greatest advantage? I merely used this king’s face as my profile picture, and countless follow-for-follow requests came pouring in from around the world. Heh heh.”

The Skeleton King answered with an arrogant expression and began sending a message to Magic Johnson.

> Good human. I'm fine thank you. and you?

After checking the message, I let out a small sigh.

“Don’t send messages to anyone else.”

“Why not?”

“If I say don’t, then don’t, you bastard.”

So much for Atlanta, Georgia.

Calling himself a native of Atlanta District, Georgia City, Gyeonggi Province, would have sounded more believable.

Apparently, even translation magic could do nothing about English this painfully Korean.

“At this rate, even the Akabutakchi tribe, who have lived in the Amazon rainforest for hundreds of years while preserving their traditions, won’t believe you’re American.”

“Hmm. I do not know exactly what you mean, but the oddly specific nature of it makes me even angrier.”

“Just do as I say. If your identity gets exposed, things won’t end with a little trouble.”

No matter how good my current image was, if the Skeleton King’s identity became known, we would clearly have to brace ourselves for considerable repercussions.

I turned my head and asked,

“Isn’t that right, Team Leader Choi?”

In the seat diagonally beside us, Team Leader Choi had been awake by himself for several minutes. He answered,

“I was already considering the matter of the Skeleton King—”

“Stone-King. Call me Mr. King.”

The Skeleton King cut him off firmly. Team Leader Choi stared at him for a moment, then continued with a sigh.

“In any case, we are considering every possibility regarding Mr. King’s future. For now, it would be best to avoid exposure to the press and other media.”

“I refuse. I will reveal myself to the world with pride.”

“Really? Team Leader Choi, what are the penalties for an illegal immigrant entering the country?”

Team Leader Choi answered immediately.

“Deportation, without question. You would also have to expect a fine or imprisonment.”

“What about an illegal immigrant from the Demon Realm?”

“It has never happened before, but instead of the police, a large-scale raid team would be dispatched.”

“You heard him.”

The Skeleton King’s eyes darted around as he remained silent, but eventually he spoke.

“…It cannot be helped. The world is not yet prepared to accept this king, so I shall exercise restraint for a while.”

“That’s what you should do. Unless you want to spend the rest of your life lying low in my Inventory.”

“A-All right.”

The biggest headache was now dealt with.

Now there was the second headache to deal with… But this one was something I had no choice but to face head-on.

Not because I had no other options, but because it would help with my plans going forward.

*It’s a pain, but it can’t be helped.*

I quietly tapped the armrest, lost in thought, then suddenly spoke.

“What’s the atmosphere like back home right now?”

Team Leader Choi gave me a short, heavy answer.

“It’s insane.”

“…That bad?”

“When someone passes the judicial exam, banners are hung in the neighborhood where they live and at their alma mater, and a short article is printed in the local newspaper. More than 1,500 people pass that exam in a single year. How much more attention would there be for you, Mr. Jin Taekyung?”

Along with that perfectly fitting comparison, Team Leader Choi clicked in midair.

The holographic screen installed in the seat filled with countless online articles.

[At Last, He Has Returned.]

[Who Is Jin Taekyung? Chairman Xiao Yang bows his head on behalf of the Chinese people. The reverent farewell of S-rank Hunters…]

[The Young Hero Who Fought to Rescue Survivors Until the Very End Finally Returns to the Arms of His Homeland.]

It wasn’t just the Korean media. China, the center of the incident, and countries around the world were all flooding the Internet with article after article about my return and what I would do next.

I had known this was coming and expected it, but I couldn’t help gaping when I saw a photograph attached to an online article posted five minutes earlier.

“Wait. Are all those people actually human?”

“They aren’t monsters, so they probably are.”

“Oh, shit…”

The photograph attached to the article showed a crowd packed so tightly around Incheon Airport that there wasn’t a single gap to be seen.

Thousands? No, tens of thousands.

As I stared blankly at the screen, Team Leader Choi’s voice continued.

“Traffic in the surrounding area has come to a standstill, and a car parade is being prepared under military and police control.”

“What? A car parade?”

“Did I not tell you?”

“You mentioned it in passing, so I thought you were joking. No, but… isn’t this a bit much?”

Team Leader Choi shook his head firmly.

“It has to be this much. You are Korea’s new representative S-rank Hunter.”

“Even so, this is excessive. At this rate, the President will show up too.”

“Ah, I really did fail to mention that.”

“What?”

“He is coming. The Blue House contacted us first this morning. I meant to tell you on the plane, but I dozed off and forgot.”

For a moment, my thoughts ground to a halt.

Tens of thousands of people waiting for me at Incheon Airport. Paralyzed roads and a spectacular car parade. And now the President was coming, too.

I remained silent, unable to find the words, then forced out a voice.

“…Really? You’re not joking?”

“Yes. They want to shake your hand once, stand with you at the photo line, and take a picture together.”

“Team Leader Choi, I don’t know anything about politics. If I get dragged into something by mistake and a problem arises, I’ll be completely screwed.”

“I know what you think, Mr. Jin Taekyung. That is why I tried to turn them down politely, but they seemed quite determined as well. It was not easy.”

“You should have turned them down anyway. Even if I am a member of Peace Guild, how could you make that decision on your own?”

No matter how much we trusted each other or how little time there had been, this was something he should have consulted me about.

Team Leader Choi lowered his head apologetically at my stiff expression.

“I’m sorry. They offered several favorable conditions, including tax breaks, so I thought it would benefit you as well.”

“Forget that. Call them right now and tell them it’s off… Wait. Tax breaks?”

“Yes. You know about the bounty that was placed on the Arch Lich. If the Chinese government pays it to you, then under Korean law, it would count as foreign-source income for a Korean resident…”

“Wait. So how much tax would I have to pay in total?”

“I cannot say for certain, but it would be several trillion. The bounty alone is fifty trillion. Even if we simplify things and assume only ten percent is withheld, it would still be an enormous amount. Of course, the amount left over would be much larger.”

“…That’s true.”

“Once again, I apologize for failing to ask for your understanding. I will tell the Blue House that this is no longer happening.”

I nodded with my face set hard.

“Team Leader. This must never happen again.”

Right. I was about to get my hands on tens of trillions. Even if I paid my taxes properly and in full, I would still become incredibly wealthy.

No matter how insignificant the conditions they were offering might be, I couldn’t get involved with politicians just to save a little on taxes. That was something I needed to avoid.

*A few trillion? I can just pay it and be done with it.*

I cast my worries aside and leaned back against the soft seat.

* * *

*Boom! Boom-boom-boom!*

Incheon Airport. Hundreds of cameras flashed at the same time.

At the photo line prepared under strict security, two men from completely different professions were shaking hands with bright smiles.

“Mr. Jin Taekyung. You’ve truly been through a lot.”

“Oh, it was nothing. You’ve been busy too, Mr. President?”

And as the Skeleton King watched the scene, he thought,

*What a vile human.*

It was a brief assessment that included Team Leader Choi, who was smiling contentedly as though everything had gone according to plan.
```
