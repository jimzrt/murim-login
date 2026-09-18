<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0404.txt",
      "sha256": "1f47b986bbd324c8e154439524a2d65367ccf1b867b4787b1af811176bb1b1a5",
      "bytes": 14077
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "a0d051bb473dfb62933892f819f7366f8e16a1699f2a30da18b9245b0e819dcd",
      "bytes": 2196
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "14aa4b4212f88ac520e764f2962b4cfc8a2417ab730afa5b9d560f79471dfc47",
      "bytes": 135975
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "11fb110383316d37fbcebb0540673253a3de9989ac4293aa9044696270c8b08c",
      "bytes": 533
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "cf023303b14de751cabc05b1cdb9e76b88bbbae88474e61280286a0f097a169e",
      "bytes": 1212
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "2cf918d0c9d5f64f93ddd8b166e5bbbf63baad24e152a542227e453f44b36c0c",
      "bytes": 622
    },
    {
      "path": "characters/Lei Fei.md",
      "sha256": "9758daf3c0b4cd9a04d212cf8e1f611a55eaf7a293530c6a200200c77ea7c73d",
      "bytes": 893
    },
    {
      "path": "characters/Wei Fenghu.md",
      "sha256": "64b25e16d8074a6aa9fcfdab415ebe51f14f3ed8626959e21bc4620032fc5125",
      "bytes": 560
    },
    {
      "path": "characters/Wu Heixing.md",
      "sha256": "abff6d6445c69dccb32bc0cf6d357333111c031cacb17bfe6cc9b557b39ca1c3",
      "bytes": 735
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4a8430a800e9c2edb6a5109f4c65eff01aae8ecb124df8599d63131521c605dc",
      "bytes": 118089
    }
  ],
  "estimated_tokens": 10471
}
-->

# Durable State Update — Chapter 404

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 404. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 404. Profile updates may replace only one
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
  "chapter": 404,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 404,
    "continuity_sources": [404],
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
    "Wei Fenghu and more than four thousand Hunters have reached the Western Front, where Jin Taekyung annihilated the monster army and survived the ten-percent teleportation.",
    "Wei Fenghu understands that Lei Fei died after completing his final mission; Jin delivered Lei Fei's love, apology, and praise, and Wei entrusted Lei Fei's sword to Jin.",
    "Lei Fei's wife and daughter were moved to safety while he was missing.",
    "Team Leader Choi and Shao Shen remain unconscious because of accumulated physical and mental fatigue, although their injuries were healed by top-grade potions.",
    "Hero's Soul is a Supreme Peak sword that can grant Hero's Power to someone it recognizes as having an upright character.",
    "Hero's Soul rejected Jin and removed Hero's Power when he formed an evil intention.",
    "The Skeleton Warlord absorbed some of the mana released when Lei Fei disappeared and confirms that only a faint trace of Lei Fei's soul remains in Hero's Soul.",
    "The Skeleton Warlord has no memories of its own past and has begun questioning what kind of being it once was.",
    "Jin has been summoned by a minister of state.",
    "The wider war against the Arch Lich remains unresolved despite the Western Front victory."
  ],
  "continuity_sources": [
    403,
    402
  ],
  "open_questions": [
    "Who is Lei Fei's unidentified lord, what is the lord's origin, and how does the lord relate to the Arch Lich's objective?",
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "What awaits Jin to the west, and how can the ongoing war be ended?",
    "What kind of being was the Skeleton Warlord before it became an undead commander?",
    "What specific situation will allow Jin to draw out Hero's Power more strongly?"
  ],
  "safe_through": 403,
  "temporary_decisions": [
    "Render 나이트메어 as Nightmare.",
    "Use black knight for 검은 기사 and keep it distinct from Death Knight and Death Knight Lord.",
    "Render 언령 as word-spell.",
    "Render 영웅의 혼 as Hero's Soul and 영웅의 힘 as Hero's Power.",
    "Preserve Jin's blunt, profane combat voice."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 제자     | **Disciple**                                 |
| 생도     | **cadet**                                    |
| 상태               | **Status**                     |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 대격변     | **Great Cataclysm**   |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 레이페이 | **Lei Fei** | Concealed Chinese S-rank Hunter and head of the Public Security Armed Forces Department in Sichuan Province. |
| 웨이펑후 | **Wei Fenghu** | Minister of National Defense under China's Central Military Commission. |
| 우헤이싱 | **Wu Heixing** | Chinese S-rank Hunter who provokes Jin and nearly draws his sword. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 탈주 | **Escape** | Song associated with Won Myunghoon. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 인민해방군 | **People's Liberation Army** | Chinese military deployed to seal off the catastrophe area. |
| 국방부 | **Ministry of National Defense** | Government ministry referenced in Taekyung's comparison about the steady passage of time. |
| 중화 | **Zhonghua** | Patriotic term used in Shao Shen’s rallying speech. |
| 가고일 | **Gargoyle** | Flying monster species accompanying the Wyverns. |
| 데스나이트 | **Death Knight** | Undead commander type serving under the Black Knight. |
| 공안무력부 | **Public Security Armed Forces Department** | Chinese security organization ordered to assemble during the attack. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 웨이펑후 | 진태경 | senior_military_official_to_ally | Mr. Jin | formal-polite | Wei Fenghu addresses Jin while inviting him to walk to the operations headquarters. |
| 진태경 | 웨이펑후 | Foreign Hunter to senior military official | General, Commander, or Supreme Leader | Polite but flustered | Jin jokingly cycles through grand titles while trying to interrupt Wei's emotional request. |
| 우헤이싱 | 진태경 | hostile S-rank Hunter to foreign Hunter and provocation target | peninsula bangzi | insulting and confrontational | Wu repeatedly addresses Jin with anti-Korean slurs. |
| 데스나이트 | 인간 | enemy combatants | human | contemptuous and commanding | Used in the Death Knight's warnings to Jin. |
| 데스나이트 | 로드 | subordinate to commanding lord | Lord | fearful and deferential | The Death Knight calls to the Death Knight Lord after Jin overwhelms the army. |
| 레이페이 | 웨이펑후 | nephew_to_maternal_uncle_and_adoptive_father | Uncle; later Father | childlike-familiar | Lei Fei calls Wei Fenghu his uncle and later acknowledges him as his father. |
| 진태경 | 레이페이 | former ally and fellow Hunter | Lei Fei | blunt and solemn | Jin addresses Lei Fei by name before telling him to rest. |
| 레이페이 | 진태경 | former ally and fellow Hunter | you | familiar and respectful | Lei Fei uses 자네 and 하게 while asking Jin to help him fulfill his final mission. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 403
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who has sworn never to kill again.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 403
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force and crossed the wall into true mastery.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother; Jeok Cheongang is his Master; Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and student; his mother and sister Hayeon are among those he protects.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 403
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lei Fei.md

# Lei Fei (레이페이)

- **Safe through:** Chapter 403
- **Aliases:** None
- **Role:** Lei Fei is a concealed Chinese S-rank Hunter and former head of the Public Security Armed Forces Department in Sichuan Province who recovered his human identity after becoming a level-120 undead Death Knight Lord and died fulfilling his final mission.
- **Personality:** Lei Fei's recovered memories show him as dutiful, honorable, family-oriented, and willing to serve as an unseen guardian.
- **Voice:** His human voice is formal and earnest, becoming warm and playful with family.
- **Relationships:** Wei Fenghu is his maternal uncle who raised him as a son; Lei Fei married an unnamed flower-shop owner and had a daughter, trained alongside Wu Heixing, and was corrupted by the Arch Lich before Jin Taekyung restored his identity.

### Wei Fenghu.md

# Wei Fenghu (웨이펑후)

- **Safe through:** Chapter 403
- **Aliases:** None
- **Role:** Wei Fenghu is the Minister of National Defense under China's Central Military Commission and a four-star general.
- **Personality:** Courteous, reserved, and authoritative.
- **Voice:** Formal and measured, addressing Jin as Mr. Jin.
- **Relationships:** Wei Fenghu is Lei Fei’s maternal uncle who raised him as his own son; after Lei Fei’s death, he entrusted Lei Fei’s sword to Jin Taekyung.

### Wu Heixing.md

# Wu Heixing (우헤이싱)

- **Safe through:** Chapter 400
- **Aliases:** None
- **Role:** Wu Heixing is a Chinese S-rank Hunter known for frequent media exposure and scandal who secretly practices martial arts, including an internal-energy cultivation technique and fist-and-foot martial arts.
- **Personality:** Arrogant, status-conscious, abusive, and fiercely proud of his power, he responds to humiliation with anger, jealousy, and fear.
- **Voice:** Loud, insulting, entitled, and dependent on national and political status.
- **Relationships:** He is openly hostile toward Jin Taekyung and Faye Chen, and resents Jin receiving Chairman Shao Yang's attention.

## Korean source

```text
＃404화



「후우.」

캄캄한 밤.

복귀와 동시에 장비를 벗어 던진 청년이 자리에 털썩 주저앉았다. 거친 숨을 몰아쉬는 그에게 다가온 한 중년인이 음료수를 건넸다.

「힘들어 보이는군. 마셔.」

산시성(山西省)에서 차출된 헌터라는 공통점이 있는 두 사람은 오는 길에 그럭저럭 친분을 쌓은 상태였다.

익숙한 얼굴과 손에 들린 캔 음료를 확인한 청년이 떨떠름한 목소리로 중얼거렸다.

「보급으로 나온 거예요? 처음 보는 음료수 같은데.」

「해외 구호 물품으로 온 거야. 우리나라 건 아니지.」

「음, 혹시 탄산 없어요?」

「싫으면 말고.」

덥석.

슬그머니 뒤로 빠지는 중년인의 손을 잡아챈 청년이 진지한 얼굴로 말했다.

「아저씨. 제가 세상에서 제일 좋아하는 게 보급 음료수라는 걸 말씀드렸던가요?」

「아니.」

「그럼 지금부터 알게 되시겠군요.」

「좋아, 바로 그 자세야.」

「잘 먹을게요.」

딸칵.

캔 음료를 따서 한 모금 들이킨 청년의 표정이 미묘하게 변했다. 하지만 그가 뭐라 할 새도 없이, 중년인이 물음을 던졌다.

「제3구역 수색 마치고 오는 길이지?」

「……크읍, 네.」

「힘들었겠군.」

청년은 어깨를 으쓱하는 것으로 대답을 대신했다. 탈의한 상반신은 아직 마르지 않은 식은땀으로 흥건했고, 뺨에는 초록색 핏물이 튀어 있었다.

「몬스터의 피로군. 전투라도 있었나?」

「아뇨. 빌딩을 지나가고 있었는데 빌어먹을 가고일 사체가 떨어졌어요. 아마 옥상에 걸쳐져 있었나 봐요.」

「난리가 났겠군.」

「그걸 말이라고 하세요? 1, 2년 차 햇병아리들은 피를 뒤집어쓰자마자 구토에 오줌까지 지렸어요.」

「자네는?」

「제가 이래 봬도 7년 차 헌터 아닙니까. 눈 하나 깜짝 안 했죠.」

중년인의 시선이 청년의 특정 부위를 향해 스르륵 내려갔다. 군청색 바지의 살짝 얼룩진 부분을 물끄러미 바라보던 그가 고개를 끄덕였다.

「음. 그렇군.」

「……땀입니다.」

「난 아무 말도 안 했어. 그런데 자네를 보니까 왠지 눈에 땀이 맺힐 것 같아.」

「……사실 조금 지렸어요. 티 나요?」

「응.」

「제기랄.」

욕설을 내뱉으며 캔 음료를 기울이는 청년을 말없이 바라보던 중년의 사내는 불쑥 물었다.

「생존자는 발견했나?」

「……!」

「자네 쪽도 마찬가지였군.」

말이 끝나기 무섭게 딱딱하게 굳는 청년의 표정에, 그는 한숨을 내쉬었다.

그 역시 이미 한차례 수색에 참여했다. 그건 정말이지 악몽 같은 경험이었다.

시선이 닿는 곳마다 몬스터에 의해 갈기갈기 찢겨 나간 시신들이 쌓여 있었고 끔찍한 악취에 머리가 쪼개지는 것 같았으니까.

아마 두 사람은 오늘 본 광경을 평생토록 잊지 못할 것이다.

「……도무지 상상이 안 가요. 얼마나 치열한 전투였을지.」

「그런 상상은 할 필요 없어. 자네가 뭘 생각하든 그 이상이었을 테니까.」

국방부장 웨이펑후를 따라 이곳에 온 4천 명의 헌터들은 편제에 따라 나뉘어 소도시를 수색했다. 그리고 그들이 사용한 모든 수색 장비들은 한 가지 결과만을 계속해서 내놓았다.

생존자 전무(全無).

전투 초기 겁에 질려 도망쳤던 삼천 명의 인민해방군을 제외한 모두가 싸늘한 시신으로 누웠다. 뿔뿔이 흩어진 비겁한 탈주병들이 얼마나 살아남았는지는 아직 알려지지 않았다.

「이래서야 사상자 집계라는 말도 못 쓰겠군요. 사망자 집계가 더 맞는…….」

「말조심해. 아직은 모르는 거니까.」

「음, 죄송합니다. 제가 실언을 했네요.」

「알면 됐어. 그리고…….」

경솔한 청년의 발언을 뚝 자른 사내가 말을 이었다.

「사상자 집계가 맞아. 생존자들이 있으니까.」

「……아.」

청년은 잠시 잊고 있던 것을 떠올렸다. 이 처참한 지옥도에서 살아남은 세 사람의 존재를.

「공안무력부 연대장이라고 했었나요? 그 어린 친구.」

「맞아. 한국에서 온 젊은 선생도 살아남았지.」

「그리고 그…….」

앞서 언급된 두 사람도 영웅적인 행보를 보인 것은 맞지만, 마지막 남은 한 사람에 비하면 태양 앞의 반딧불에 불과하다.

마른침을 꿀꺽 삼키는 청년을 대신해 중년인이 말을 이었다.

「그래, 그 사람. 아니, 그분도 계시지.」

그의 목소리에는 숨길 수 없는 경외심이 깃들어 있었다. 자신보다 한참이나 어린 청년을 그분이라 칭하면서도 아무런 거부감이 들지 않는 이유는, 그가 이룩한 업적이 얼마나 위대한지 알기 때문이다.

「자네는 믿어지나? 한 사람의 헌터가 그렇게 강할 수 있다는 것이.」

그 역시 잔뼈가 굵은 베테랑 헌터다. 그렇기에 S급 헌터가 얼마나 괴물 같은 존재들인지 어렴풋이 예측 정도는 할 수 있었다.

하지만 진태경이 보여 준 활약은 정말이지…… 헌터, 아니 인간의 힘이라고는 믿기지 않을 정도였다.

「자그마치 일만에 달하는 몬스터 군단이야. 데스나이트 두 기에, S급 헌터에 버금가거나 그 이상으로 강하다는 데스나이트 로드도 있었다고.」

중년인은 잔뜩 흥분한 목소리로 빠르게 말을 이어갔다.

「그에 비해 아군 헌터의 숫자는? 고작 천 명이었어. 인민해방군이 있긴 했지만 그마저도…….」

「최전선이 무너지자 절반 가까이 도망쳐 버렸죠. 나머지는 용감하게 싸웠지만 몬스터들에게 학살당했고. 저도 들어서 압니다.」

「진태경이 도착했을 때 헌터들이 몇 명이나 남아 있었을 것 같나? 천 명? 아니, 그 절반도 남지 않았을 거란 데에 내 목숨을 걸지!」

만일 진태경이 도착했던 당시의 상황을 직접 목격했더라면, 그는 놀란 나머지 심정지를 일으켰을지도 모른다.

그토록 깊은 경외심을 품은 그조차도 진태경이 홀로 몬스터 군단과 대적했을 거란 생각은 하지 못했다.

「하나같이 지치고 다친 수백의 헌터를 이끌고 열 배가 훌쩍 넘는 수의 몬스터 군단을 전멸시킨 거지! 이게, 이게 말이 된다고 생각하나?」

그리고 그런 사내를 바라보던 청년은 영 떨떠름한 표정이었다.

「안 된다고 생각하는데요.」

「그래, 하지만 그분은 그걸 해냈다고!」

「어, 아저씨. 찬물 끼얹어서 죄송한데, 아직 제대로 밝혀진 사실이 없지 않나요?」

「뭐?」

「제 생각에는 진태경이…….」

「진태경이 아니라 진 선생!」

고리눈을 뜨고 호통 치는 중년인의 모습에 흠칫한 청년이 헛기침을 내뱉었다.

「크흠. 그러니까 저도 진 선생이 대단한 강자인 건 인정하는데, 아무래도 과장이 좀 섞이지 않았나, 뭐 그런 생각인 거죠.」

「과장? 전장에 남겨진 흔적을 보고도 그런 말이 나와? 진 선생이 아니면 누가…….」

「거참, 너무 열만 내지 마시고 조금 더 냉정하게 바라보세요. 아저씨 말이 전부 사실이라면, 진 선생이 파이 첸이나 우헤이싱보다 강하다는 것 아닙니까.」

「그들에게 순서를 매기고 싶지는 않지만, 이번 몬스터 웨이브에서 보여 준 전공으로는 진 선생이 제일이지. 그래서?」

「파이 첸이 홍콩계라 그렇지, 대격변에서 수많은 전공을 세운 영웅이고 우헤이싱은 사고를 많이 쳐도 중화가 낳은 진정한 천재라고요. 그런 두 사람보다 진태경이 앞선다? 이건 선을 넘은 거죠.」

중년인은 허탈과 한심함이 가득 담긴 눈빛으로 청년을 응시했다.

「선을 넘은 건 네 녀석이야.」

「예?」

「하고 싶은 말이 고작 그거냐? 중화제일(中華第一)을 부르짖으면서 위대한 승리를 쟁취하고, 인민을 구한 영웅을 깎아내리는 거?」

청년의 얼굴이 와락 일그러졌다.

「말이 나왔으니 말인데, 진태경이 오늘 구한 인민이라고 해 봐야 두 명. 아니지, 그나마 다른 하나는 한국인이니 하나밖에 없습니다. 그마저도 상처 하나 입지 않은 멀쩡한 몸이었다고요. 제 나라 사람만 지키겠답시고 싸운 거죠. 설마 최상급 포션이라도 썼겠습니까?」

「말을 말아야겠군. 찬사를 보내지는 못할망정 이따위 푸대접이라니. 진 선생이 보면 뭐라 할지…….」

절레절레 고개를 저은 중년인이 자리에서 일어난 그 순간이었다.

“글쎄요. 제 생각에는 도와줄 필요가 없는 개씨벌놈이라고 했을 것 같은데.”

「……!」

「……!」

기척도 없이 다가온 누군가의 목소리에, 두 사람은 화들짝 놀라 고개를 돌렸다.

그들이 마주한 것은, TV와 대중매체를 통해 익숙해진 한 사람의 얼굴이었다.

「……딸꾹.」

머리 하나는 더 큰 그를 올려다보던 청년은 딸꾹질을 시작했고.

「지, 지, 지, 지, 지지진!!」

중년인은 버퍼링이라도 걸린 사람처럼 말을 잇지 못했다.

그런 두 사람을 바라보던 진태경은 사람 좋은 웃음과 함께 입을 열었다.

“거기 젊은 분은 착한 중국인 되기 싫으면 딸꾹질 멈추시고. 아저씨는 지진을 멈춰 주세요. 대지진으로 아크 리치 쓰러트릴 생각 아니시면.”

「딸, 헙.」

「저, 저, 정말 당신입니까?」

진태경이 살짝 고개를 끄덕였다.

“그냥 지나가려고 했는데, 영 거슬리는 소리가 들리는 바람에.”

「……그, 그게…….」

영 거슬리는 소리를 한 장본인이자, 딸꾹질을 멈추고 사시나무처럼 몸을 떨기 시작한 청년을 향해 진태경이 물었다.

“몇 살?”

「스, 스물아홉입니다.」

“나보다 나이 많네. 반말할게.”

「……예?」

“뭐.”

「아, 아닙니다.」

반말이 아니라 쌍욕을 해도 할 말이 없다.

멀리에서나 스치듯 목격했던, 바로 그 진태경이 자신의 말을 모두 들었다고 생각하니 청년은 손발이 저려 오고 눈앞이 새하얗게 물드는 것을 느꼈다.

「죄, 죄송합니다.」

“죄송할 거 없어. 뒷담화라는 게 원래 그렇지 뭐. 난 이해해.”

「가, 감사합니다.」

진태경의 온화한 미소에 그의 마음이 사르륵 녹아내리려던 그때였다.

“감사할 것도 없어. 뒷담화라는 게 원래 깔 때는 좋아도 걸리면 좆 되는 거거든.”

「……!」

“지금 내 등 뒤에 한 사람이 있을 거야. 보여?”

청년은 천천히, 아주 천천히 눈동자를 굴렸다.

과연, 십여 미터 떨어진 곳에서 악마의 얼굴을 한 장년인이 그를 향해 무시무시한 기세를 피워 올리는 중이었다.

“중앙 군사위원회 소속 A급 헌터시래. 네 얘기를 굉장히 흥미롭게 들으셨는지 나한테 허리를 자꾸 숙이시던데, 빨리 달려가서 파스라도 붙여 드려.”

「예, 옛!」

비명처럼 대답한 청년은 잽싸게 달려갔고, 마나가 실린 조인트에 진짜 비명을 내질렀다.

그 모습에 피식 웃으며 떠나려던 진태경이 문득 발걸음을 멈췄다.

“아, 한 가지 잘못 알고 계신 사실이 있는데요.”

「저, 저 말입니까?」

반쯤 넋이 나가 있던 중년인이 퍼뜩 정신을 차렸다.

「죄송하지만 그게 뭔지…….」

“저 혼자 한 일이 아닙니다.”

「예?」

“모두가 죽어라 싸웠어요. 제가 왔을 때는 이미 거의 다 끝나 있더라고요. 다른 사람들에게도 그렇게 알려 주세요.”

「그, 그게 정말입니까?」

“물론이죠. 아, 혹시 가족이 있으신가요?”

「예에. 딸 셋에 아들 다섯…….」

“애국자시네. 몇 년 뒤에는 축구 팀 만들어도 되겠어요.”

뭔가를 곰곰이 생각하던 진태경이 불쑥 물었다.

“전투 부대 소속은 아니시죠?”

「……역시 바로 아시는군요.」

중년인은 부끄러운 듯 고개를 숙였다.

「보시다시피 E급 헌터라 전투에서는 제외되었습니다. 아마 사상자 집계에 투입될 듯합니다.」

“그럼 한 가지만 부탁해도 될까요?”

「저, 저야 영광입니다. 진 선생님.」

“그럼 사망자 명단에 한 사람을 포함시켜 주세요. 시신을 찾지 못할 테니 특별히 부탁드리겠습니다.”

「그분의 성함이……?」

“레이페이, 레이페이(雷霈)입니다.”

그 말이 마지막이었다.

제자리에 서서 멀어지는 진태경의 뒷모습을 한참이나 바라보던 중년인은 참았던 숨을 내쉬었다.

마지막으로 봤던 진태경의 표정은, 아마 오랫동안 뇌리에 박혀 있을 것 같았다.

‘무슨 눈빛이…….’

반드시 해내고야 말겠다는 결의(決意).

진태경을 향해 연신 감탄을 토해 내던 중년인은 청년이 두고 간 캔 음료를 들이켜 목을 축였다. 그리고 형용할 수 없는 맛에 눈살을 찌푸렸다.

“퉤엣!”

버디언?

한국 음료 같은데, 더럽게 맛이 없었다.



* * *



「왔소, 진 선생.」

나를 기다리고 있던 사람은 웨이펑후뿐만이 아니었다.

회의실 안에 놓인 다섯 개의 모니터. 그리고 화면 속에 앉아 있는 다섯 명의 S급 헌터들.

나는 담담한 목소리로 말문을 열었다.

“전쟁을 끝내러 갑시다.”

바야흐로, 이 모든 일의 원흉을 처치해야 할 때였다.
```

## Final English reading copy

```markdown
# Chapter 404

“Phew.”

It was pitch-black outside.

The moment he returned, the young man threw off his equipment and dropped heavily into a seat. As he struggled to catch his breath, a middle-aged man approached and handed him a drink.

“You look exhausted. Drink this.”

The two men had bonded somewhat on the way here over their shared status as Hunters drafted from Shanxi Province.

The young man recognized the familiar face and eyed the can in the middle-aged man’s hand, then muttered dubiously.

“Did this come from the supplies? I don’t think I’ve seen this drink before.”

“It came in as foreign relief supplies. It’s not from our country.”

“Hmm. Do you have anything carbonated?”

“If you don’t want it, never mind.”

The middle-aged man began to withdraw his hand, but the young man quickly grabbed it and spoke with a solemn expression.

“Sir. Have I ever told you that canned ration drinks are my favorite thing in the world?”

“No.”

“Then you’re about to learn.”

“Good. That’s the spirit.”

“I’ll enjoy it.”

Click.

The young man opened the can and took a sip. His expression changed subtly.

But before he could say anything, the middle-aged man asked a question.

“You’re coming back from searching Sector Three, aren’t you?”

“……Urk, yes.”

“It must have been rough.”

The young man answered with a shrug. His bare upper body was drenched in cold sweat that had not yet dried, and green blood had splattered across his cheek.

“Monster blood. Did you get into a fight?”

“No. I was passing by a building when a damn gargoyle corpse fell on me. I guess it had been caught on the roof.”

“That must have caused quite a commotion.”

“Do you really have to ask? The rookies with only a year or two under their belts started vomiting and pissing themselves the moment they were covered in blood.”

“And you?”

“I may not look it, but I’m a seven-year Hunter. I didn’t even blink.”

The middle-aged man’s gaze slowly lowered toward a certain part of the young man’s body. He stared at the slightly stained area of the navy-blue pants, then nodded.

“Hmm. I see.”

“……It’s sweat.”

“I didn’t say anything. But looking at you is making my eyes feel sweaty.”

“……Actually, I did piss a little. Is it obvious?”

“Yes.”

“Damn it.”

The young man swore and tilted back the canned drink. The middle-aged man watched him in silence before abruptly asking a question.

“Did you find any survivors?”

“……!”

“So it was the same on your side.”

The young man’s expression stiffened the instant the words left the man’s mouth. The middle-aged man let out a sigh.

He had already taken part in one search himself.

It had been a truly nightmarish experience.

Everywhere he looked, corpses torn apart by monsters had been piled up, and the horrific stench had made him feel as if his head were splitting open.

The two of them would probably never forget what they had seen that day.

“……I can’t even imagine how fierce the battle must have been.”

“You don’t need to imagine it. Whatever you think it was, it was worse.”

The four thousand Hunters who had come here with Minister of National Defense Wei Fenghu had been divided according to their units and sent to search the small city. Every piece of search equipment they used kept producing the same result.

No survivors.

Everyone except the three thousand members of the People’s Liberation Army who had fled in terror at the beginning of the battle lay cold and dead. No one yet knew how many of the cowardly deserters who had scattered had survived.

“At this rate, we can’t even call it a casualty count. A death toll would be more accurate……”

“Watch what you say. We don’t know that yet.”

“Mm. I’m sorry. I spoke carelessly.”

“If you know that, it’s fine. And……”

The middle-aged man cut off the young man’s thoughtless comment and continued.

“A casualty count is the correct term. There are survivors.”

“……Oh.”

The young man remembered the three people he had momentarily forgotten—the three who had survived this gruesome hell.

“You mean the regimental commander of the Public Security Armed Forces Department? That young fellow?”

“That’s right. The young man from Korea survived too.”

“And then there’s……”

The two people mentioned earlier had certainly shown heroic courage, but compared to the last person, they were no more than fireflies before the sun.

The middle-aged man continued in place of the young man, who swallowed hard.

“Yes, that man. No—that person survived too.”

Unmistakable awe colored his voice. He felt no discomfort calling a young man far younger than himself “that person,” because he knew how great the man’s achievements had been.

“Can you believe it? That one Hunter could be so strong?”

He was a veteran Hunter with years of experience. Because of that, he could at least vaguely imagine what monsters S-rank Hunters truly were.

But Jin Taekyung’s performance had been so incredible that it was difficult to believe it had been the work of a Hunter—or even a human being.

“It was a monster army numbering nearly ten thousand. There were two Death Knights, and even a Death Knight Lord said to be as strong as or stronger than an S-rank Hunter.”

The middle-aged man continued rapidly, his voice filled with excitement.

“And how many allied Hunters were there? Only a thousand. The People’s Liberation Army was there too, but even they……”

“Nearly half of them ran away when the front line collapsed. The rest fought bravely, but the monsters slaughtered them. I heard about it myself.”

“How many Hunters do you think were still alive when Jin Taekyung arrived? A thousand? No, I’d stake my life that fewer than half of them were left!”

If he had witnessed the situation when Jin Taekyung arrived with his own eyes, he might have suffered cardiac arrest from the shock.

Even the middle-aged man, who revered Jin so deeply, had not imagined that Jin Taekyung had faced the monster army alone.

“He led hundreds of exhausted, wounded Hunters and annihilated a monster army more than ten times their size! Do you think that makes any sense?”

The young man looked at him with a thoroughly dubious expression.

“I don’t think it does.”

“Exactly. But that person did it!”

“Uh, sir. Sorry to pour cold water on you, but nothing’s actually been confirmed yet, has it?”

“What?”

“I think Jin Taekyung……”

“Not Jin Taekyung. Mr. Jin!”

The middle-aged man opened his eyes wide and shouted. The young man flinched and cleared his throat.

“Ahem. I mean, I admit that Mr. Jin is an incredible powerhouse, but I can’t help thinking that the story may have been exaggerated a little.”

“Exaggerated? You saw the traces left on the battlefield and you still say that? If it wasn’t Mr. Jin, then who……”

“For goodness’ sake, don’t get so worked up. Look at it a little more calmly. If everything you’re saying is true, then that means Mr. Jin is stronger than Faye Chen or Wu Heixing.”

“I don’t want to rank them, but based on the achievements shown during this monster wave, Mr. Jin is clearly the best. So?”

“Faye Chen may be from Hong Kong, but she’s a hero who accomplished countless great feats during the Great Cataclysm. And even if Wu Heixing causes plenty of trouble, he’s a true genius born from Zhonghua. Jin Taekyung surpassing those two? That’s crossing a line.”

The middle-aged man stared at the young man with a gaze full of disbelief and contempt.

“You’re the one who crossed the line.”

“What?”

“Is that all you have to say? You shout about Zhonghua being number one, then belittle the hero who achieved a great victory and saved the people?”

The young man’s face twisted.

“Since we’re talking about it, Jin Taekyung only saved two people today. No, the other one was Korean, so he only saved one of our people. And that person was perfectly healthy, without a single injury. He fought just to protect the people of his own country. Do you really think he used a top-grade potion?”

“There’s no point talking to you. You can’t even offer praise, and this is how you repay him……”

The middle-aged man shook his head and stood up.

The middle-aged man shook his head and rose from his seat. At that moment, a voice spoke up.

“Maybe he would’ve said you were a fucking asshole who wasn’t worth helping.”

“……!”

“……!”

The two men spun around in shock at the voice that had approached without making a sound.

Standing before them was a face they had grown familiar with through television and the mass media.

“Hic.”

The young man, looking up at a man a full head taller than himself, began to hiccup.

“J-J-J-J-Jin!”

The middle-aged man stuttered like he’d started buffering.

Jin Taekyung looked at the two of them and spoke with a friendly smile.

“You there, young man—stop hiccupping if you don’t want to become a good Chinese person. And you, sir, stop the earthquake—unless you’re planning to use a great one to bring down the Arch Lich.”

“Hic—”

“A-Are you really him?”

Jin Taekyung gave a slight nod.

“I was just passing by, but I heard a particularly irritating sound.”

“……Th-That……”

Jin Taekyung turned toward the young man—the source of the irritating sound, who had stopped hiccupping and begun trembling like a leaf.

“How old are you?”

“I-I’m twenty-nine.”

“You’re older than me. I’ll speak casually.”

“……What?”

“What?”

“N-No, sir.”

Even if Jin Taekyung swore at him instead of merely speaking casually, the young man would have had no grounds to complain.

He had only ever seen Jin Taekyung from a distance or in passing. Now that he realized Jin had heard everything he had said, his hands and feet began to tingle, and his vision went white.

“I-I’m sorry.”

“You don’t have to apologize. That’s how backbiting works. I understand.”

“Th-Thank you.”

Just as Jin Taekyung’s gentle smile began to melt the young man’s heart, he continued.

“There’s nothing to thank me for. Backbiting is fun when you’re tearing someone down, but once you get caught, you’re fucked.”

“……!”

“There should be someone behind me right now. Do you see him?”

The young man slowly—very slowly—shifted his eyes.

Sure enough, more than ten meters away, a middle-aged man with the face of a demon was glaring at him, radiating a terrifying aura.

“They say he’s an A-rank Hunter with the Central Military Commission. He must have found your story very interesting, because he keeps bowing to me. Run over and put a pain-relief patch on him.”

“Y-Yes, sir!”

The young man answered with a shriek and darted over, only to let out a real scream when a mana-infused kick struck his shin.

Jin Taekyung chuckled at the sight and began to leave, but then he suddenly stopped.

“Ah, there’s one thing you’ve got wrong.”

“M-Me?”

The middle-aged man, who had been standing there half-dazed, suddenly came to his senses.

“I’m sorry, but what is it?”

“I didn’t do it alone.”

“What?”

“Everyone fought like hell. By the time I arrived, the battle was almost over. Make sure you tell the others that too.”

“Is that really true?”

“Of course. Oh, do you have a family?”

“Yes. Three daughters and five sons……”

“You’re quite the patriot. In a few years, you could put together a soccer team.”

Jin Taekyung seemed to think about something, then abruptly asked another question.

“You’re not part of a combat unit, are you?”

“……You knew right away.”

The middle-aged man lowered his head in embarrassment.

“As you can see, I’m an E-rank Hunter, so I was excluded from combat. I’ll probably be assigned to tally the casualties.”

“Then can I ask you for one favor?”

“It would be my honor, Mr. Jin.”

“Then please include one person on the list of the dead. We won’t be able to find his body, so I’m asking you to make a special exception.”

“What is his name?”

“Lei Fei. Lei Fei.”

That was the last thing Jin Taekyung said.

The middle-aged man remained rooted in place, staring at Jin’s back as he walked away. At last, he released the breath he had been holding.

He felt certain that Jin Taekyung’s expression the last time he saw him would remain etched in his memory for a long time.

*What was that look in his eyes……?*

The resolve to see something through no matter what.

The middle-aged man, who had repeatedly expressed his awe at Jin Taekyung, picked up the canned drink the young man had left behind and took a swallow to wet his throat.

Then he frowned at its indescribable flavor.

“Ptooey!”

Burdian?

It looked like a Korean drink, but it tasted fucking awful.

* * *

“You’ve come, Mr. Jin.”

Wei Fenghu was not the only one waiting for me.

Five monitors stood inside the conference room. Sitting on the screens were five S-rank Hunters.

I opened my mouth in a calm voice.

“Let’s go end the war.”

At long last, it was time to eliminate the culprit behind all of this.
```
