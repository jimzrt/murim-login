<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0568.txt",
      "sha256": "a5bb6a58bd070507f76bec53e35516ffbc04b7712fbf08a858ccb5f1b1168f87",
      "bytes": 14113
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "5d9c8da9305fe6b17c7bae10a198c42acb808291c4ac96d3c3c3ca71dfbbbc40",
      "bytes": 4024
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "9d179ef08cc7a36b41db24d451471123a13643b3f5a0ed159f7dabef6231a8d8",
      "bytes": 179677
    },
    {
      "path": "characters/Baek Hanseong.md",
      "sha256": "29a70ac42de0bfa25a39b5076dec758447c20ed1b2fe467cc5d8f34e7313df5f",
      "bytes": 741
    },
    {
      "path": "characters/Cheonwoo.md",
      "sha256": "1046ceac432ce4ad82f75290085c3f2a9f3ba2aec069c07a602da5d3b9f40c8f",
      "bytes": 590
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "7938fd03d823b51f7febb43051786c09c6e653e51f1530c6aff0b4ea60fe2ac7",
      "bytes": 898
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "134dbf9e85c154c93e848fea272121babd05fe52ed6abc8139af03940171846e",
      "bytes": 1147
    },
    {
      "path": "characters/Song Cheonwoo.md",
      "sha256": "cdb79c53e2eee7aa239710d9b918e4482c3f1d4ee6b560d663a416227b8fabf7",
      "bytes": 852
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "43b40b6713298f4152b190b5a370c4b864f8359ce56dc7f85d659b1d01acc7a3",
      "bytes": 174315
    }
  ],
  "estimated_tokens": 10621
}
-->

# Durable State Update — Chapter 568

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 568. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 568. Profile updates may replace only one
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
  "chapter": 568,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 568,
    "continuity_sources": [568],
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
    "The worldwide Gate and monster crisis may mark the beginning of a second Great Cataclysm, and Taekyung intends to accelerate his project to protect Korea.",
    "Team Leader Choi says the crisis has exceeded the limit of national concealment and is prioritizing Gate defenses despite reducing Peace Guild's raid capacity.",
    "Choi is working with Song Cheonwoo against Go Jun's control of Ares Guild; Go Jun has ordered Song's extended family captured as leverage.",
    "Song Cheonwoo knows where Choi's maternal grandfather Cheon Taemin is located, while Cheon Taemin remains hidden from the world.",
    "Taekyung is a Supreme Peak master publicly recognized as S-rank-level while retaining an A-rank license, leads the Fire Dragon Pavilion's first Nanman mission, and is Peace Guild's wealthy modern-world patron.",
    "The six-member Fire Dragon Pavilion mission is entering Nanman through the Journey to Nanman Quest, whose reward is a linked quest and whose failure penalty is Can't Go to Nanman.",
    "Mungyeong ended Taekyung's direct training and assigned him the final task of incorporating martial principles into his learned martial arts; Cheongpung accompanies Mungyeong.",
    "Dark Heaven remains a monster-like threat capable of causing rifts and creating mutants, while the mechanism behind Jang Sam's transformation remains unresolved.",
    "The Mount Song Resolution restored the Murim Alliance with Mae Jonghak as Alliance Leader and Jeok Cheongang heading the Five Kings Hall; Zhuge Feng's Demon-Sealing Formation still blocks mana from the exposed Gate while Jang Taebo processes the Water God Dragon's remains.",
    "Go Jun has become increasingly ruthless and plans to lure Song Cheonwoo into a meeting after seizing Song's family in London; the substituted security detail can maintain control for up to four days.",
    "Go Se-won commands Ares Guild's thirty-member A-rank security team and remains obedient to Go Jun despite growing moral conflict over the orders.",
    "Taekyung's training was interrupted by an unidentified person applauding from behind him."
  ],
  "continuity_sources": [
    567,
    566
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "What will Taekyung's party find in Nanman, and what does the Southern Heaven Demon Empress intend there?",
    "What process created Jang Sam's mutant form, whether Dark Heaven's mutants can absorb human energy, and whether it relates to the Mutated Gate?",
    "What will result from the duel between Jeok Cheongang and Nangong Cheon, and why did Ju Hwaran and Sama Pyo's political engagement end?",
    "How will Song Cheonwoo respond to the capture of his family, and who is applauding Taekyung?"
  ],
  "safe_through": 567,
  "temporary_decisions": [
    "Render 건량 as dry rations, 광서 as Guangxi, 대별산 as Mount Daebyeol, 만리행 as Ten-Thousand-Li Journey, and 고잉메리호 as Going Merry.",
    "Render 반 시진 as half a shichen and retain Nanman, Nanman Beast Palace, Fire Dragon Pavilion, Great Hero, and Young Lady Ju.",
    "Render 남만행 as Journey to Nanman, 남만을 못 가 as Can't Go to Nanman, 면구 as disguise mask, 역용술 as disguise technique, 각주님 as Pavilion Master, 로그아웃 as Logout, and 동기화 as Synchronization.",
    "Render 일기당천 as One Against a Thousand, 거인의 포효 as Giant's Roar, 투로 as combat sequence, 타락한 엔트 as Corrupted Ent, 붉은 눈 as Red Eye, 치코리타 as Chikorita, 대마도사 as Grand Mage, 순간이동 as Teleportation, 텔레포트 as Teleport, 변이 게이트 as Mutated Gate, and 몬스터 웨이브 as Monster Wave.",
    "Render 현혹 마법 as enchantment magic, 장거리 텔레포트 마법진 as long-distance Teleportation magic circle, and retain Magic for 마법 when used generically."
  ],
  "version": 1
}
```

## Exact glossary matches

| 혁무진    | **Hyuk Mujin**     |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 도사      | **Daoist**                                                      |
| 대사      | **Master** for a senior Buddhist monk                           |
| 백한성 | **Baek Hanseong** | Twenty-seventh President of Korea and youngest president elected in Korean history. |
| 천우 | **Cheonwoo** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 송천우 | **Song Cheonwoo** | Ares Guild Director, former third-ranked Korean Hunter, and longtime European regional branch director. |
| 평화 | **Peace Guild** | Guild name. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 여포 | **Lü Bu** | Historical warrior used in Hyuk Mujin's exaggerated comparison. |
| 주모 | **Lady of the House** | Title used in Wipeng's remark that Jin Wikyung lacks a wife or household mistress. |
| 청와대 | **Blue House** | Presidential office mentioned in an online comment about proposed legislation. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 대통령 | **President** | Title for Korea's head of state. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 배리어 | **Barrier** | Team Leader Choi's protective spell. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 국장 | **national funeral** | State funeral reported for Lee Jungryong. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Baek Hanseong.md

# Baek Hanseong (백한성)

- **Safe through:** Chapter 564
- **Aliases:** None
- **Role:** Twenty-seventh President of Korea and the youngest president elected in Korean history; leads the government's public response to the Mutated Gate crisis and supports Jin Taekyung in public appearances.
- **Personality:** Confident, politically shrewd, composed, and willing to needle Lee Jungryong while advancing his anti-Ares stance.
- **Voice:** Polite, self-assured, calm, and lightly teasing.
- **Relationships:** Political counterpart to Lee Jungryong; cooperates with Ares Guild over the Chinese crisis while allowing the Peace Guild to participate at Xiao Yang's request.

### Cheonwoo.md

# Cheonwoo (천우)

- **Safe through:** Chapter 567
- **Aliases:** None
- **Role:** One of the five current Five Gates of Shanxi scions and a First Rate martial artist present at Honghwa Inn.
- **Personality:** Pampered and contemptuous toward Cheongpung's group as part of the five scions' collective mockery.
- **Voice:** Mocking in the group's exchange; no distinct individual speech is established.
- **Relationships:** Associates with Seongryong, Myeonghwa, Sohye, and Jintae as a group of current Five Gates scions.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 567
- **Aliases:** Team Leader Seok
- **Role:** Go Jun is Ares Guild's Vice Guild Master, Lee Jungryong's disciple and former Head of Security, and the de facto successor to Lee's Ares legacy who passed the S-rank Hunter qualification assessment with a very high score but lacks Lee's legitimacy.
- **Personality:** Disciplined and controlled under ordinary pressure, fiercely loyal to Lee Jungryong, but consumed by humiliation and rage when Ares Guild's authority is challenged.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Disciple and direct protégé of Lee Jungryong, Go Jun inherited Lee's Ares Guild legacy after his death and regards Jin Taekyung and Choi Minwoo as enemies seeking to take it away.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 552
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and a member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Song Cheonwoo.md

# Song Cheonwoo (송천우)

- **Safe through:** Chapter 567
- **Aliases:** Director Song
- **Role:** Ares Guild Director and former A-rank Hunter who reached third place among Korean rankers, briefly headed the Hunter training center, and led Ares Guild's European regional branch for twenty years; he now leads an internal faction capable of threatening Go Jun.
- **Personality:** Highly ambitious, honor-obsessed, politically calculating, and determined to use his final opportunity to reclaim influence before retirement.
- **Voice:** Not established.
- **Relationships:** Song Cheonwoo followed Cheon Taemin since before Team Leader Choi was born, was Lee Jungryong's former friend and rival, was exiled to Europe after Lee's victory, and is now aligned with Choi against Go Jun.

## Korean source

```text
＃568화



짝짝짝.

힘찬 박수 소리. 동시에 아까 전부터 인지하고 있던 누군가의 목소리가 울려 퍼졌다.

“대단하군, 대단해.”

또각. 광택이 흐르는 검은 구두가 이쪽을 향해 움직인다.

주름 하나 없이 칼처럼 각이 선 정장 하의. 위에는 무릎까지 내려오는 가죽 코트를 입은 그가 내 앞에서 걸음을 멈췄다.

“미스터 진, 익히 들었지만…… 여기까지 온 보람이 있군. 생각했던 것 이상이야.”

갑작스럽게 찾아온 이 상황이 혼란스럽다. 이해할 수 없다는 듯한 내 표정에, 그가 느긋한 표정으로 대답했다.

“그렇게 당황할 필요 없네. 때가 온 것뿐이니까.”

“때가 왔다고?”

“그래, 이 세상에 영웅이 자네뿐일 줄 알았나?”

“뭐라고?”

“지금부터 자네는 더 거대한 세상의 일원이 된 거야. 아직까지는 그걸 모르고 있을 뿐이지.”

“……!”

찌릿한 전류가 전신을 타고 흐른다. 침음성을 흘린 나는 불청객을 노려보았다.

“너, 뭐야?”

“내 정체를 아는 사람은 그리 많지 않지.”

피식 실소를 흘린 그가 말을 이었다.

“나로 말할 것 같으면…….”

“아니, 뭐 하는 새끼냐고.”

“어?”

이게 아닌데 하는 표정으로 눈을 동그랗게 뜨는 그. 아니, 놈의 얼굴을 말없이 바라보던 내가 손을 내저었다.

“됐다. 계속 지껄여 봐. 준비한 대사 남았잖아.”

“그래도 될까?”

“물론이지. 마저 해.”

큼. 소리 내어 목을 가다듬은 놈이 사뭇 진지한 눈빛으로 말을 이었다.

“내 이름은 킹 퓨리. 배리어의 국장…….”

뻑!

“억.”

아구창을 처맞은 그놈. 스켈레톤 킹이 취한 사람처럼 비틀거린다. 나는 그 틈을 놓치지 않고 연달아 죽빵을 후려갈겼다.

뻑! 뻑! 쩍!

“억! 으억! 잠깐만! 잠깐만! 내 턱뼈!”

“잠깐 같은 소리 하네. 시벌 놈이.”

이 새끼는 좀 맞아야 한다.

누구는 이런 시국에도 밝은 미래를 위해 불철주야 조뺑이를 치고 있는데, 뜬금없이 튀어나와서 영화 캐릭터 코스프레라니.

왜 갑자기 안 입던 가죽 코트를 쳐 입고 왔나 했다.

“재밌니? 히어로 영화가 그렇게 재밌어?”

정신없이 맞고 있던 스켈레톤 킹이 돌연 표정을 굳히며 엄지를 치켜세웠다.

“존잼.”

“…….”

“삼천만큼 싫어해.”

“아니, 이 새끼가.”

“잠깐만! 뼈에 금 갔다!”

뻑! 뻑!

“네가 그러고도 사람이냐? 어?”

“나, 난 몬스터다!”

“이 새끼는 꼭 지 하고 싶을 때만 몬스터라고 염병을 떠네. 종족이 뷔페니? 이지선다야?”

뻑! 뻑!

“잠깐만! 진짜 잠깐만 멈춰 봐라. 이번에는 안와골절이다!”

“…….”

몬스터 주제에 제법 정확한 진단명 보소.

전문성이 느껴지는 의학 용어에 잠깐 주먹이 멈칫하자. 잽싸게 몸을 빼서 도망친 스켈레톤 킹이 치욕으로 몸을 부르르 떨었다.

“간악한 인간 같으니. 네놈은 사람도 아니다.”

“세상에. 내가 지금 몬스터 새끼한테 뭘 들은 거야.”

“마귀 같은 놈. 훗날 심판의 날이 도래하면 지옥에 떨어질지어다.”

“혹시 너 요새 교회 다니니? 단어 선택이 예사롭지 않은데.”

순간 멈칫한 스켈레톤 킹이 헛기침을 내뱉었다.

“크흠. 인간 여자가…….”

“뭐?”

“예쁜 인간 여자가 먼저 말을 걸었다. 요 앞 횡단보도에서 만났는데. 따라오면 다 같이 노래도 부르고, 맛있는 것도 먹는다고 하더군.”

“……그래서?”

“갔지. 그다지 재미는 없었지만 나름 나쁘지 않았다. 목사라는 자가 이 몸의 존귀함을 알아봤는지 하사품까지 바쳤거든.”

“세상에, 하느님.”

언데드 몬스터가 교회라니. 실화냐.

내가 할 말을 잃은 그때, 스켈레톤 킹이 40년 전 아재 스타일로 바짝 세운 코트 깃을 슬쩍 내렸다.

“후후, 보거라.”

앞에서 귀를 의심했다면, 이번에는 눈을 의심했다.

코트 깃 사이로 당당히 모습을 드러낸 것은, 다름 아닌 싸구려 십자가 목걸이였다.

“이것이 바로 존귀한 왕의 상징이니라.”

“…….”

퇴마의 상징 아니냐.

혹시 목사가 아니라 엑소시스트를 만난 건 아닐까 하는 생각이 잠깐 들었지만, 매직 존슨의 환영 마법은 한 치의 이질감도 찾을 수 없을 만큼 완벽했다.

어느새 기하급수적으로 불어난 스켈레톤 킹의 SNS 팔로워들이 바로 그 증거다.

찰칵.

“……이 와중에 셀카 찍고 자빠졌네. 스마트폰 부숴 버릴까.”

“내 돈 주고 내가 산 거다. 간악한 인간은 뭐라 할 자격이 없으니 입 다물고 있도록.”

자본주의에 적응한 몬스터라니, 이거야말로 진정한 괴물이 아닐까.

더군다나 내돈내산이라니까 뭐라 할 말이 없다. 심지어 뒷광고 받은 것도 아니고, 최근 평화 길드에서 정산 받은 금액으로 정당하게 값을 치르고 구매한 거다.

“이 몸도 이제 인간들 사이에서는 제법 고소득자다. 듣자 하니 이 세상의 백성들은 연봉으로 계급을 나눈다던데, 나는 6억씩이나 되지. 후훗. 그것도 무려 향후 십 년 동안이나!”

“…….”

노예 10년 어서 오고.

헌터로 치면 S급에 충분히 들어가고도 남는 스켈레톤 킹을 중급 헌터 연봉으로 부려먹다니.

최 팀장의 악랄함에 혁무진의 불알을 탁 치고 싶은 마음이다.

“뭐냐, 그 표정은.”

“아냐. 아무것도. 신경 쓰지 말고 앞으로 돈 많이 벌어라.”

눈을 가늘게 뜬 스켈레톤 킹이 나를 위아래로 훑었다.

“수상하군. 지금뿐만이 아니라, 요 며칠 동안 낌새가 이상했어.”

“누구? 교회에 간 언데드 몬스터?”

“너 말이다! 이 간악한 인간이여!”

버럭 외친 스켈레톤 킹이 말을 이었다.

“게이트에서도 자꾸 생각에 잠겨 있지를 않나. 교양이라고는 손가락 관절만큼도 없는 인간이 그림도 그리고 메모까지 하지. 심지어는 어제 긴급 구조팀 호출도 거절해서 이 몸이 직접 왕림해야 했다!”

몬스터치고는 제법 눈치가 빠르다. 아마 근래 들어 가장 자주 붙어 있던 놈이라 그럴지도 모르지.

턱을 긁적인 나는 한바탕 열변을 토한 스켈레톤 킹을 향해 반문했다.

“무슨 말 하려는지 알겠는데. 그래서?”

“어?”

“뭐 어쩌라고, 인마. 나는 생각하면 안 되냐? 그림 좀 그리고 메모하면 안 돼?”

“그, 그건 아니긴 한데.”

순간 주춤한 스켈레톤 킹이 바로 반박을 시작했다.

“다른 건 그렇다 쳐도 긴급 구조팀 호출은…….”

“미룰 만하니까 미루지. 내가 없어도 너 있잖아.”

“어, 어?”

“변이 게이트 터진 것도 아니었고, 마력 수치 상승량 보니까 이만하면 괜찮겠다 싶어서 나 대신 너 보낸 거야.”

“이, 이 몸을 너 대신?”

입을 벌린 채 눈을 깜빡이던 스켈레톤 킹이 더듬거리는 목소리로 물었다.

“왜?”

“믿고 맡길 만하니까.”

“……!”

“그동안은 혹시 몰라서 같이 다니긴 했는데, 뭐 옆에서 직접 본 것도 있고. 주위 사람들 얘기 들어보면 혼자 보내도 되겠다 싶었지.”

스켈레톤 킹은 명실상부한 네임드 몬스터다.

한때 워로드라 불리던 시절에도 강한 능력을 가지고 있었지만, 아크 리치와의 전투를 통해 더욱 강력한 존재로 거듭났다.

‘어중간한 네임드 몬스터로는 저놈한테 못 비비지.’

지금까지 곁에서 직접 지켜본 바로는 육체적 능력도 뛰어난 데다가, 자신만의 권능으로 일인군단(一人群團)을 세울 수도 있는 녀석이다.

이런 부분에 한해서는 현존하는 S급 헌터 중 누구도 스켈레톤 킹을 따라잡지 못한다.

아니지, 매직 존슨처럼 전장을 지배한다는 대마도사라면 또 모르겠다.

‘거기에 나까지.’

이 정도만 해도 능히 혼자서 게이트를 쓸어 버릴 수 있는 언데드 여포.

그리고 이토록 강한 스켈레톤 킹을 굳이 옆에 끼고 데리고 다닌 이유는 딱 하나뿐이었다.

‘미친 수준의 사회성 결여.’

제 입으로 정체를 밝힌 적이 없을 뿐이지, 스스로 본 투 비 몬스터라는 걸 사방팔방에 티내고 다니는 놈이다.

이런 놈을 지난번 청와대 공식 기자회견에 데려갔으면 백한성 대통령에게 ‘인간 수컷’ 운운했을 것이고, 주모를 총사령관으로 한 광복군이 일어나 저 코쟁이 새끼의 신상을 캐자며 태극기를 펄럭였을 것이 분명하다.

하지만 이제는…….

“이 형은 안심했다. 교회도 가고, 짜식. 앞으로는 조금 자유롭게 살도록.”

툭툭.

어깨를 두드리는 따스한 손길에 스켈레톤 킹이 눈을 크게 떴다. 아니, 어쩌면 그것은 앞서 내가 말한 한 단어 때문일지도 모른다.

“자, 자유?”

“그래. 이제 믿고 맡길 수 있는 수준까지 왔으니 그 정도 자유는 줘야지.”

“간악한 인간이여. 날 감시하는 것 아니었나?”

“감시?”

피식 웃은 내가 말을 이었다.

“중국에서 내 목숨을 살려 준 너를?”

“그건…….”

“물론 너도 내게 빚이 있겠지. 우리 둘 모두 굳이 말하지는 않겠지만, 늘 고맙게 생각한다는 것만 알아 둬.”

“……!”

금색 눈꺼풀이 잘게 떨렸다. 뭐라 형용키 어려운 표정으로 나를 바라보던 스켈레톤 킹이 축축하게 젖은 눈으로 입을 뗐다.

“간악한 인간이여.”

“오, 쒯. 아무 말도 하지 마.”

“그래도 이 말은 꼭 해야겠다.”

“하지 마. 진짜. 난 이런 분위기 안 좋아해.”

어디선가 잔잔한 BGM이 들려오는 듯하다. 거북함에 먼 산을 바라보는 내 귓가에, 스켈레톤 킹의 목소리가 닿았다.

“그럼 나 오늘 클럽 가도 되나?”

“…….”

“지금까지 그 마법사에게 속아서 게이바만 두 번 갔다. 이번에는 반드시 클럽에서 존귀한 부비부비를 성공하고 싶다.”

“…….”

존귀한 부비부비 같은 소리 하고 자빠졌네.

내 감성이나 돌려내. 개자식아.

“부탁이다, 간악한 인간이여. 자정 전에는 기필코 돌아오겠다!”

“그래, 가.”

“저, 정말?”

“응. 가. 뒤지고 싶으면.”

“…….”

“미친놈이 클럽 같은 소리 하고 자빠졌네. 가서 무슨 사고를 치려고.”

게이바만 두 번 갔다는 말에 마음이 좀 약해지긴 했지만, 스켈레톤 킹은 아직 그 정도로 사회화가 완료되지는 않았다.

내가 클럽을 한 번도 못 가 본 놈이라 이러는 건 아니다.

……정말이다.

“왜! 어째서! 이렇게 잘생겼는데!”

스켈레톤 킹이 비통 어린 음성으로 울부짖던 그때, 놈이 손에 들고 있던 스마트폰이 진동했다.

지이잉.

화면을 확인한 녀석의 얼굴이 처참하게 일그러진다. 무엇 때문인지는 안 봐도 홀로그램이다.

“긴급 호출 왔냐?”

“……빌어먹을.”

타이밍 한 번 기가 막힌다. 뒤이어 호출 내용을 확인한 나는 고개를 들어 스켈레톤 킹을 빤히 응시했다.

“뭐 해, 안 가고.”

“싫다, 간악한 인간이여. 이번엔 네가 가라.”

“무슨 소릴. 보면 바로 견적 나와. 이 정도면 너 혼자서 가도 충분해.”

“제기랄. 왜 네놈은 여기서 놀고, 이 몸은 일하는 것이냐!”

놀아? 누가?

하지만 스켈레톤 킹이 알 리가 없다. 내가 무슨 일을 하고 있는지.

피식 웃은 나는 대답 대신 손을 치켜들었고, 낌새를 눈치챈 녀석은 잽싸게 문밖으로 빠져나갔다.

쾅!

그렇게 요란한 소리를 내며 닫힌 문은, 석양이 지고 다음 날 아침이 될 때까지 두 번 다시 열리지 않았다.

그리고……

스으읍. 후우.

쉬익, 펑!

고요하면서도 고립된 그 공간 속에서, 나는 끊임없이 운기조식과 수련을 반복했다.

그것은 아른거리는 실마리를 손에 쥔 채, 지금껏 가 보지 않았던 새로운 길을 찾는 긴 여정이었다.



* * *



파리한 안색, 떨리는 손끝.

언제부터였을까. 이야기를 듣던 도중 뒷덜미를 타고 흐른 식은땀 한 방울이 툭, 하고 떨어진다.

“지, 지금 뭐라고 했느냐?”

일흔이라는 나이가 믿어지지 않는 장대한 체구와 중년의 얼굴을 한 그였지만, 입술 사이로 흘러나온 목소리는 죽음을 코앞에 둔 이의 그것처럼 희미했다.

조금 전 누군가의 입을 통해 듣게 된 이야기는 그만큼 충격적인 내용을 담고 있었다.

“그, 그러니까…….”

들은 이야기를 다시 떠올리는 것만으로도 눈앞이 아찔하다. 겨우 정신을 다잡은 노인은 떨리는 목소리를 가까스로 끄집어냈다.

“우리, 우리 애들을…… 네가 납치했다고?”

“납치는 어감이 좀 그렇네요. 누가 들으면 오해하겠습니다.”

“네, 네놈이 감히.”

“그러니까…… 보호라고 해 둡시다.”

온갖 화려한 만찬이 차려진 테이블 너머. 경쾌한 어조로 대답한 석고준이 스테이크를 베어 물었다.

레어로 조리한 소고기의 육즙이 각진 턱을 타고 흘러내리고, 그와 함께 흘리듯 덧붙인 한 마디가 노인의 귓가를 후벼 판다.

“우선은, 말입니다.”

“……!”

노인, 송천우의 얼어붙은 얼굴을 보며 석고준은 기분 좋게 웃었다.
```

## Final English reading copy

```markdown
# Chapter 568

*Clap, clap, clap.*

A vigorous round of applause rang out. At the same time, the voice of the person I had sensed for a while now echoed through the room.

“Impressive. Very impressive.”

*Click.*

Shiny black dress shoes moved toward me.

He wore suit pants with razor-sharp creases and not a wrinkle in sight. Over them, he had donned a leather coat that reached down to his knees. He stopped in front of me.

“Mr. Jin, I’ve heard a great deal about you…… but coming all the way here was worth it. You’re even more impressive than I expected.”

The sudden situation left me confused. At the look on my face, which clearly said I had no idea what was going on, he answered with a relaxed expression.

“There’s no need to be so flustered. The time has simply come.”

“The time has come?”

“Yes. Did you think you were the only hero in this world?”

“What?”

“From this moment on, you’ve become part of a much greater world. You simply don’t know it yet.”

“……!”

A sharp current ran through my entire body. I let out a low groan and glared at the unwelcome guest.

“What the hell are you?”

“There aren’t many people who know my true identity.”

He gave a quiet laugh and continued.

“If I were to introduce myself……”

“No, I’m asking what the hell you’re doing.”

“Huh?”

His eyes went round, his face showing that this wasn’t how things were supposed to go. I silently stared at his face, then waved a hand.

“Never mind. Keep going. You still have lines left, don’t you?”

“Would that be all right?”

“Of course. Finish it.”

“Ahem.”

He audibly cleared his throat, then continued with a deeply serious look in his eyes.

“My name is King Fury. Director of Barrier……”

*Wham!*

“Urgh.”

I punched him square in the face.

The Skeleton King staggered like a drunk. I didn’t let the opportunity pass and hammered him with a series of punches.

*Wham! Wham! Crack!*

“Urgh! Ugh! Wait! Wait! My jawbone!”

“Like hell I’m waiting, you bastard.”

This guy needed to get beaten up.

While some people were working their asses off day and night to build a bright future even in times like these, he had suddenly popped up dressed like a movie character.

I’d wondered why he had shown up wearing a leather coat he never usually wore.

“Are you having fun? Are superhero movies really that entertaining?”

The Skeleton King, who had been taking hits without a break, suddenly hardened his expression and raised his thumb.

“Totally fucking awesome.”

“…….”

“I hate them three thousand.”

“What the hell is wrong with you?”

“Wait! You cracked one of my bones!”

*Wham! Wham!*

“How can you call yourself human? Huh?”

“I—I’m a monster!”

“This bastard only starts screaming about being a monster when he wants to. Is your species a buffet? Are you choosing between two options?”

*Wham! Wham!*

“Wait! Stop for real this time! I’ve got an orbital fracture!”

“…….”

For a monster, he had a surprisingly accurate diagnosis.

My fist hesitated for a moment at the professional medical terminology. The Skeleton King quickly pulled away and fled, his entire body trembling with humiliation.

“You vile human. You aren’t even a person.”

“My God. What did I just hear from a monster?”

“You devilish creature. When Judgment Day arrives, may you fall into hell.”

“Have you been going to church lately? Your choice of words is unusually sophisticated.”

The Skeleton King paused and coughed awkwardly.

“Ahem. A human woman……”

“What?”

“A beautiful human woman spoke to me first. I met her at the crosswalk up ahead. She said that if I followed her, we could all sing together and eat delicious food.”

“……And?”

“So I went. It wasn’t particularly fun, but it wasn’t bad. A man called a pastor must have recognized the nobility of my person, because he even offered me a gift.”

“My God.”

An undead monster going to church.

Was this for real?

Just as I ran out of things to say, the Skeleton King lowered the coat collar he had turned up in the style of a middle-aged man from forty years ago.

“Heh heh. Behold.”

If I had doubted my ears before, now I doubted my eyes.

Peeking proudly out from between the coat collars was none other than a cheap cross necklace.

“This is the symbol of a noble king.”

“…….”

Wasn’t that a symbol of exorcism?

For a moment, I wondered if he had met an exorcist rather than a pastor. But Magic Johnson’s Illusion Magic was so perfect that I couldn’t find even the slightest hint of incongruity.

The Skeleton King’s followers on social media, which had multiplied exponentially, were proof of that.

*Click.*

“You’re taking selfies at a time like this? Should I smash your smartphone?”

“I bought it with my own money. A vile human has no right to say anything, so keep your mouth shut.”

A monster who had adapted to capitalism.

Wasn’t that the definition of a true monster?

Besides, he had bought it with his own money, so I had nothing to say. It wasn’t even secretly sponsored. He had paid for it legitimately with the money he had recently received from the Peace Guild.

“I’m quite a high-income earner among humans now. I hear that the people of this world divide themselves into classes based on their annual income. Mine is as much as six hundred million won. Heh heh. And that’s for the next ten years!”

“…….”

Welcome to ten years of slavery.

The Skeleton King was more than qualified to enter the S-rank if he were a Hunter, yet they were working him for the annual salary of a mid-level Hunter.

Team Leader Choi’s cruelty made me want to give Hyuk Mujin’s balls a sharp tap.

“What is that expression?”

“Nothing. Don’t worry about it. Just keep making lots of money.”

The Skeleton King narrowed his eyes and looked me up and down.

“Suspicious. It isn’t only now. Your behavior has been strange these past few days.”

“Who? The undead monster who went to church?”

“I’m talking about you, you vile human!”

The Skeleton King shouted angrily, then continued.

“You keep sinking into thought even in Gates. A man with not so much as a finger joint’s worth of culture draws pictures and even takes notes. Yesterday, you even refused an emergency rescue team call, forcing this king to make the journey himself!”

He was surprisingly perceptive for a monster. Maybe it was because he had been the one closest to me most often lately.

I scratched my chin, then countered the Skeleton King, who had just finished his impassioned speech.

“I know what you’re trying to say. So what?”

“Huh?”

“What do you want me to do about it? Am I not allowed to think? Am I not allowed to draw a few pictures and take some notes?”

“I—I’m not saying that.”

The Skeleton King faltered for a moment, then immediately began arguing back.

“Even if we set all that aside, the emergency rescue team call……”

“I delegated it because I could. Even if I wasn’t there, they still had you.”

“Wha—what?”

“It wasn’t a Mutated Gate, and when I saw how much the mana level had risen, I figured it would be fine. So I sent you instead of going myself.”

“Y—you sent me instead?”

The Skeleton King blinked with his mouth hanging open, then stammered out a question.

“Why?”

“Because I can trust you to handle it.”

“……!”

“Until now, I kept going with you just in case. But I’d seen what you could do firsthand, and after listening to what the people around us had to say, I figured you could go alone.”

The Skeleton King was a Named Monster in every sense of the word.

He had possessed powerful abilities even back when he was called a Warlord, but after his battle with the Arch Lich, he had evolved into an even more powerful being.

*An ordinary Named Monster wouldn’t stand a chance against that guy.*

From everything I had directly witnessed while fighting alongside him, he possessed excellent physical abilities. On top of that, he could use his own Authority to create a one-man army.

In that regard, none of the S-rank Hunters currently alive could match the Skeleton King.

Well, a Grand Mage who could dominate a battlefield like Magic Johnson might be another story.

*And then there’s me.*

Even without considering anything else, the undead Lü Bu was more than capable of sweeping through a Gate by himself.

There had been only one reason I had deliberately kept such a powerful Skeleton King at my side.

*His absolutely insane lack of social skills.*

He had never revealed his identity in so many words, but he went around advertising to everyone that he had been born to be a monster.

If I had taken him to the official Blue House press conference last time, he would have referred to President Baek Hanseong as a “human male.” Then the Liberation Army, led by the Lady of the House, would surely have risen up, waving Korean flags and demanding that they investigate the identity of that long-nosed bastard.

But now……

“This hyung is relieved. You even went to church, kid. From now on, try living a little more freely.”

*Pat, pat.*

The Skeleton King’s eyes widened at the warmth of my hand as I patted his shoulder. Or perhaps it was because of the one word I had just used.

“F—freely?”

“Yes. You’ve reached the point where I can trust you with things, so I should give you that much freedom.”

“Vile human. Weren’t you watching me?”

“Watching you?”

I gave a quiet laugh and continued.

“After you saved my life in China?”

“That was……”

“Of course, you owe me something too. Neither of us needs to say it out loud, but just know that I’m always grateful.”

“……!”

His golden eyelids trembled faintly. The Skeleton King stared at me with an expression difficult to describe, then opened his mouth with moist eyes.

“Vile human.”

“Oh, shit. Don’t say anything.”

“But I have to say this.”

“Don’t. Seriously. I don’t like this kind of atmosphere.”

It felt as if soft background music were playing somewhere. Uncomfortable, I looked off toward a distant mountain, and the Skeleton King’s voice reached my ears.

“Then can I go to a club tonight?”

“…….”

“I’ve been tricked by that mage and gone to a gay bar twice already. This time, I absolutely want to achieve a noble grinding session at a club.”

“…….”

A noble grinding session, my ass.

Give me back my emotions, you bastard.

“Please, vile human. I swear I’ll return before midnight!”

“Fine. Go.”

“R-really?”

“Yeah. Go. If you want to die.”

“…….”

“Crazy bastard. A club, my ass. What kind of trouble are you planning to cause?”

Hearing that he had gone to a gay bar twice did make me feel a little sorry for him, but the Skeleton King still wasn’t socially developed enough for that.

It wasn’t because I had never been to a club myself.

……It really wasn’t.

“Why? How can this happen when I’m so handsome!”

Just as the Skeleton King let out a sorrowful howl, the smartphone in his hand began to vibrate.

*Bzzzz.*

The moment he checked the screen, his face twisted miserably. I didn’t need to look to know why. The answer might as well have been projected as a hologram.

“Did you get an emergency call?”

“……Damn it.”

The timing was unbelievable. After checking the contents of the call, I raised my head and stared directly at the Skeleton King.

“What are you waiting for? Why aren’t you going?”

“I refuse, vile human. You go this time.”

“What are you talking about? You can tell what the situation is as soon as you look at it. This is more than manageable for you alone.”

“Damn it. Why are you playing around here while I’m the one working?”

Playing around? Who was playing around?

But there was no way the Skeleton King could know what I was doing.

I gave a quiet laugh and raised a hand instead of answering. The moment he noticed what I meant, he quickly slipped out the door.

*Bang!*

The door closed with a resounding crash.

It did not open again from sunset until the following morning.

And then……

*Inhale. Exhale.*

*Whoosh. Boom!*

In that quiet, isolated space, I endlessly repeated circulating my qi and training.

It was a long journey in search of a new path I had never traveled before, holding on to a faint thread of understanding in my hands.

* * *

A pale complexion. Trembling fingertips.

When had it begun?

Partway through listening to the story, a bead of cold sweat ran down the back of his neck and dropped with a soft *plop*.

“W-what did you just say?”

He had the imposing build of a man whose age of seventy seemed impossible, along with the face of a middle-aged man. But the voice that slipped between his lips was as faint as that of someone standing on the brink of death.

The story he had just heard from another person contained information that was every bit as shocking as that.

“Th-that is……”

Even remembering what he had heard made his vision swim. The old man barely pulled himself together and forced out his trembling voice.

“You—you kidnapped our children?”

“‘Kidnapped’ is a rather unpleasant way to put it. Someone might misunderstand.”

“H-how dare you.”

“So let’s call it protection.”

Beyond a table covered with all manner of elaborate dishes, Go Jun answered in a light tone and bit into a steak.

Juice from the rare-cooked beef ran down his angular jaw. Along with it, the single remark he added as though in passing dug into the old man’s ears.

“For now, at least.”

“……!”

As he watched the old man—Song Cheonwoo—stare back with a frozen expression, Go Jun smiled pleasantly.
```
