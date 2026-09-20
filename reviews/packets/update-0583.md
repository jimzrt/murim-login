<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0583.txt",
      "sha256": "90ef6d12cc90404e18a534cf209d54880e0aca90c14625235b77b0a292325fe1",
      "bytes": 14921
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "46415b3ad6f19569cb753230e9e16a3a354c50e9eb9bd51a850afafb80055278",
      "bytes": 2651
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "334b83569b27a711354d716803145b273dc680f836af901f0d5901e3b09c63c6",
      "bytes": 182801
    },
    {
      "path": "characters/Cheonwoo.md",
      "sha256": "39a1f4294d8f95e51fa4ca7980776df7fb00f1372f4ab53df613d1a1dfdd3f64",
      "bytes": 590
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "9adfd31aebcc9e9b39a1777be8bcb944c21c6651df30377610c35c7b886d19a3",
      "bytes": 553
    },
    {
      "path": "characters/Hwa-jong.md",
      "sha256": "626c5667dacb246b21af698193c887f30de05c9d4844516c59499faab423263b",
      "bytes": 562
    },
    {
      "path": "characters/Kim Hwajong.md",
      "sha256": "0df8e7fc55a7f51f38a0d9f3c327c7f49b3f903c45d82c9a962ecc2bed7ba6ba",
      "bytes": 538
    },
    {
      "path": "characters/Song Cheonwoo.md",
      "sha256": "02ddb466c41fa0c48a8be9cc3193ba5175d409b10334d74c03d3b99a367b11c6",
      "bytes": 1080
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "a8460e8720244793622bc6be0fcdc4a1530000a1c052cb94330af801f64ea05c",
      "bytes": 951
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "0b6e90e4e1075685ff28c89960f7acd0669a4a14e278c35fa8495f5d6e0bb0ea",
      "bytes": 180402
    }
  ],
  "estimated_tokens": 10954
}
-->

# Durable State Update — Chapter 583

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 583. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 583. Profile updates may replace only one
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
  "chapter": 583,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 583,
    "continuity_sources": [583],
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
    "Song Cheonwoo says Cheon Taemin suddenly collapsed more than twenty years ago and has remained unconscious, but no one knows why.",
    "Song Cheonwoo and Lee Jungryong concealed Taemin's condition, waited two years, conducted experiments, and purged aides who knew the truth.",
    "Hwa-jong was not told about Taemin's condition and remains loyal to Choi Minwoo.",
    "Song claims Taemin is still alive, but his location is unknown and Area A is only suspected.",
    "Choi Minwoo has confirmed Song's account enough to treat Taemin's status as genuine while continuing to investigate.",
    "Busan's Kraken has been eliminated, but more than one thousand Mermen remain across Haeundae and Gwangalli while the Peace Guild and other forces contain the disaster.",
    "Go Jun seized Song Cheonwoo's children as leverage and used the threat to force Song to attack Choi Minwoo.",
    "Go Jun used an S-grade Magic Gem to artificially cause the Busan Monster Wave and sent Kim Ho-jung to Busan.",
    "Go Jun intends to kill Choi Minwoo through Song Cheonwoo and may be relying on another unidentified being.",
    "Song Cheonwoo was killed after falling into an abyss and being attacked by an unidentified monster.",
    "The unused object in Song Cheonwoo's pocket released darkness that became light after his death.",
    "The B-grade Yeti's Winter Range Gate in Pyeongchang opened a Monster Wave; Behemoth emerged, and Choi Minwoo, Kim Hwajong, and twenty Peace Guild Hunters confronted it while civilians fled."
  ],
  "continuity_sources": [
    582,
    581
  ],
  "open_questions": [
    "What caused Cheon Taemin's collapse, and what happened during his more than twenty years of unconsciousness?",
    "Is Cheon Taemin actually being kept in Area A of Ares Guild headquarters?",
    "What is the unidentified being involved in Go Jun's plan, and is it connected to the monster that killed Song Cheonwoo?",
    "What was the object Song Cheonwoo kept unused in his pocket, and what did its release of darkness and light accomplish?",
    "What will happen in the confrontation between Behemoth and Choi Minwoo's group, and can the civilians below Pyeongchang be protected?"
  ],
  "safe_through": 582,
  "temporary_decisions": [
    "Use Yeti's Winter Range for 예티의 겨울 산맥, Behemoth for 베히모스, and Behemos for 베헤모스.",
    "Use Stone King for 스톤 킹 and Skeleton King for 스켈레톤 킹.",
    "Use Area A for A구역.",
    "Use Hwa-jong for 화종.",
    "Use Hero's Soul for 영웅의 혼, Hyung for 형님, and S-grade Magic Gem for S급 마정석."
  ],
  "version": 1
}
```

## Exact glossary matches

| 김화종    | **Kim Hwajong**   |
| 최민우    | **Choi Minwoo**   |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 일격     | **One Strike**                         |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 힐러      | **healer**            |
| 마법사     | **mage**              |
| 도사      | **Daoist**                                                      |
| 천우 | **Cheonwoo** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 화종 | **Hwa-jong** | Butler Kim's personal name. |
| 송천우 | **Song Cheonwoo** | Ares Guild Director, former third-ranked Korean Hunter, and longtime European regional branch director. |
| 평화 | **Peace Guild** | Guild name. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 도련님 | **Young Master** | Address used for Team Leader Choi by Butler Kim. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 전광 | **Quick Attack** | Shortened form of Warlordmon’s rapid-movement command. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 신력 | **divine strength** | Superhuman strength attributed to Taekyung. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 쓰촨 | **Sichuan** | Variant spelling used for the region associated with the pattern Jin recognizes. |
| 텔레포트 | **Teleport** | Taekyung's label for the Blood Lord's unexplained disappearance. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 부산 | **Busan** | City where the Haeundae Gate crisis occurs. |
| 경기도 | **Gyeonggi Province** | Province where Pocheon is located. |
| 크라켄 | **Kraken** | Sea monster leading the Monster Wave; newly identified in this chapter. |
| 평창 | **Pyeongchang** | Location in Gangwon Province where the Gate is situated. |
| 베히모스 | **Behemoth** | Mythical monster emerging from the Pyeongchang Gate. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 화종 | 최민우 | butler_to_Young_Master | Young Master | formal and deferential | Butler Kim consistently addresses Choi Minwoo with the established deferential title. |
| 송천우 | 화종 | former_allies | Hwa-jong | familiar and informal | Song uses Hwa-jong's personal name, prompting Hwa-jong to reject the familiarity. |
| 화종 | 송천우 | former_allies_now_hostile | you | formal and cold | Hwa-jong challenges Song's right to expect Choi's trust and rejects their former intimacy. |
| 송천우 | 최민우 | older_former_ally_to_younger_former_ally | Minwoo | familiar and informal | Song addresses Choi by his given name while discussing the meeting place and surveillance. |
| 팀장 | 중년인 | Hunter_team_leader_to_stranger | Boss | casual and polite | The Team Leader mistakes disguised Song for an ordinary raid customer and warns him not to proceed. |
| 최민우 | 화종 | Young Master to butler | Butler Kim | formal and respectful | Choi refers to Hwa-jong as 김 집사님 while discussing the concealed truth. |
| 최민우 | 송천우 | temporary ally to rival | Regional Director | formal and cutting | Choi uses 지사장님 while condemning Song's survival and concealment. |

## Listed compact profiles

### Cheonwoo.md

# Cheonwoo (천우)

- **Safe through:** Chapter 582
- **Aliases:** None
- **Role:** One of the five current Five Gates of Shanxi scions and a First Rate martial artist present at Honghwa Inn.
- **Personality:** Pampered and contemptuous toward Cheongpung's group as part of the five scions' collective mockery.
- **Voice:** Mocking in the group's exchange; no distinct individual speech is established.
- **Relationships:** Associates with Seongryong, Myeonghwa, Sohye, and Jintae as a group of current Five Gates scions.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 581
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hwa-jong.md

# Hwa-jong (화종)

- **Safe through:** Chapter 582
- **Aliases:** Butler Kim
- **Role:** Hwa-jong is Choi Minwoo's loyal butler and personal escort.
- **Personality:** Loyal, vigilant, and uncompromising toward perceived threats to Choi Minwoo.
- **Voice:** Formal and deferential toward Choi Minwoo, cold and openly hostile toward Song Cheonwoo.
- **Relationships:** Hwa-jong serves Choi Minwoo and was formerly close to Song Cheonwoo, but their relationship ended over loyalty and ambition.

### Kim Hwajong.md

# Kim Hwajong (김화종)

- **Safe through:** Chapter 582
- **Aliases:** Butler Kim
- **Role:** Kim Hwajong is a Level 80 mage known as Butler Kim and Choi Minwoo's loyal butler and personal escort.
- **Personality:** Gentle and composed
- **Voice:** Gentle and measured
- **Relationships:** Kim Hwajong formerly instructed Im Chunsoo, who remains terrified of and obedient to him, and serves Choi Minwoo as butler and personal escort, having become Choi's only family.

### Song Cheonwoo.md

# Song Cheonwoo (송천우)

- **Safe through:** Chapter 582
- **Aliases:** Director Song
- **Role:** Ares Guild Director and former A-rank Hunter who reached third place among Korean rankers, briefly headed the Hunter training center, and led Ares Guild's European regional branch for twenty years; after being forced to attack Choi Minwoo to protect his hostage family, he fell into an abyss and was killed by an unidentified monster.
- **Personality:** Highly ambitious, honor-obsessed, politically calculating, and determined to use his final opportunity to reclaim influence before retirement.
- **Voice:** Not established.
- **Relationships:** Song Cheonwoo followed Cheon Taemin since before Team Leader Choi was born, was Lee Jungryong's former friend and rival, helped conceal Taemin's condition and purge aides who knew the truth, negotiated the European regional director position to save himself and his family, and had his children seized by Go Jun as leverage that forced him to attack Choi Minwoo.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 582
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Cheon Taemin's only living blood relative, a formidable aura-wielding swordsman who wields Hero's Soul, and is mobilizing every available power to unseat Go Jun from Ares Guild leadership.
- **Personality:** Strategic, candid, controlled, and possessive of the power and influence he intends to inherit.
- **Voice:** Dry, formal, and direct, with calm candor and carefully chosen metaphors.
- **Relationships:** Choi Minwoo is Cheon Taemin's maternal grandson and only living blood relative, was kept out of public knowledge by Lee Jungryong, is closely integrated with Jin Taekyung's family, seeks to acquire the Ares Guild intact, and now knows that Song Cheonwoo and Lee concealed Taemin's collapse and purged aides while he investigates Taemin's fate.

## Korean source

```text
＃583화



최 팀장. 평창. 몬스터 웨이브.

갑작스럽게 들이닥친 세 가지의 키워드에 머리가 혼란스럽다.

하지만 전광판을 가득 메운 자료 화면은 내게 고민할 시간마저 빼앗아갔다.

- 콰아아아!

- 꺄아아아악!

- 누, 눈사태다!

비명을 내지르며 도망치는 사람들.

스키 장비를 벗을 생각도 하지 못한 채 뒤뚱뒤뚱 움직이다가 넘어지는 그들의 뒤로, 엄청난 양의 눈과 조각난 암석이 쏟아져 내린다.

- 콰앙!

파도처럼 덮쳐오는 눈더미에 수십여 명이 흽쓸리고, 굉음과 함께 붉은 피가 튀었다.

암석에 의해 무너진 건물이 화염에 휩싸인다. 그리고 넘실거리는 불길 너머에, 이 모든 일의 근원지가 있었다.

- 구구구구궁!

아직 해가 떨어지지 않았음에도 그곳의 하늘은 어두웠다.

이름 모를 산봉우리에 내려앉은 검은 구름.

그 사이로 눈 부신 빛이 번쩍일 때마다 엄청난 진동과 굉음이 터져 나왔다.

‘몬스터 웨이브.’

나는 본능적으로 깨달았다. 빛과 어둠이 공존하는 저곳에서, 수천 명의 운명을 결정지을 격돌이 일어나고 있다는 사실을.

그리고…… 최 팀장과 김 집사를 비롯한 평화 길드의 헌터들이 목숨을 걸고 네임드 몬스터와 맞서고 있다는 것을.

얼굴이 보이지 않는 아나운서의 목소리가 노이즈에 섞여 들려왔다.

- 현재 정부는 경기도 평창 일대를 재난 지역으로 선포하고, 긴급 지원 병력을 파견했습니다. 한편 부산에서 발생한 몬스터 웨이브는…….

더 이상 들을 이유도, 여유도 없다.

다급하게 돌아선 나는 얼빠진 표정으로 고층 빌딩의 전광판을 바라보고 있던 헌터들을 향해 외쳤다.

“마법사!”

“예, 예?”

“마법사 앞으로 나오세요! 텔레포트로 평창에 가야 합니다! 지금 당장!”

공력이 실린 외침에, 악몽에서 깬 것처럼 화들짝 놀란 헌터들 중 몇몇이 쭈뼛거리며 손을 들었다.

A급 마법사 한 명에 B급 여섯 명. 하지만 앞으로 나선 것과는 별개로 그들의 안색은 어두웠다.

“죄, 죄송합니다만. 저희만으로는 텔레포트 시전이 어렵습니다.”

“뭐라고요?”

“다들 몬스터를 상대한 직후라 마나 피로도가 극심한 데다가, 또 텔레포트 마법진을 그려야 하는데 현 상황에서는…….”

말꼬리를 흐린 마법사들이 주위를 바라본다. 곳곳에 널려 있는 희생자들의 시신과 몬스터의 사체들. 갈아엎다시피 난장판이 된 도로.

상위 마법사들 사이에서도 어렵기로 유명한 텔레포트 마법을 시전 할 여건으로는 최악이라고 할 수 있었다.

상황을 지켜보던 스켈레톤 킹이 일그러진 얼굴로 입을 열었다.

“이 멍청한 인…… 놈들아. 네놈들은 지금 여건을 따질 상황이라고 생각하느냐? 하세요? 씨부랄. 더럽게 어렵네.”

간신히 화를 억누르고 있음에도 흘러나오는 흉흉한 기세에 마법사들이 침을 꿀꺽 삼켰다.

“하, 하지만 지금은 어쩔 수 없습니다. 너무 위험하단 말입니다.”

“무리예요. 설령 희박한 확률로 성공한다고 해도 부산에서 평창까지는 250km가 넘는 다고요. 그런 장거리를 단번에 건너뛸 수는 없어요.”

“해 봐! 어떻게든 시도해 보라고!”

스켈레톤 킹의 외침은 바로 내가 하고 싶은 말이었다.

하지만 동시에 마법사들이 괜히 앓는 소리를 내는 것이 아니라는 것도 안다. 그들은 매직 존슨이 아니니까.

중국 쓰촨에서 마법진도 없이 나를 혼잡한 전장으로 보내 주었던 검은 피부의 대마도사는 지금 대륙 너머에 있을 것이다.

‘빌어먹을.’

움켜쥔 주먹에서 내 것인지, 아니면 몬스터의 것인지 모를 찐득한 핏물이 뚝뚝 떨어졌다. 어쩌면 둘 다일지도 모르겠다.

“다른 방법은 없습니까?”

가장 상급자로 보이는 중년 헌터가 초조한 목소리로 대답했다.

“그렇지 않아도 조금 전 본부에 연락했습니다. 부산 내에 있는 헌터들 중에서 텔레포트를 시전할 수 있는 상위 마법사를 수배 중이긴 한데…….”

흐려지는 말꼬리. 어두운 안색.

현재 상황을 알리기에는 그것만으로도 충분하다. 상급자에게 거듭 서두를 것을 부탁한 나는 이를 악물었다.

‘빌어먹을.’

상대는 네임드 몬스터. 심지어 크라켄과 동급이거나 그 이상의 존재다.

자료 화면만으로도 그 강대함이 전해질 만큼의 괴물을 상대로 저들이 얼마나 더 버틸 수 있을까. 몇이나 살아남을 수 있을까.

‘조금만. 조금만 더 버텨 주십시오.’

닿지 않을 부탁을 내심 중얼거리며, 나는 가부좌를 틀고 앉았다.

지금은 마법사를 찾기 전까지 조금이라도 소모된 힘을 보충해야 할 때다.

“후우.”

나는 끓어오르는 불안과 분노를 가라앉히며 눈을 감았다. 캄캄한 어둠이 눈 앞을 가린다.

동시에 이보다 짙은 어둠 속에서 싸우고 있을 얼굴들이 눈앞에 스쳤다.

‘제발…… 살아남아라.’

내가 갈 때까지.

후우우웅.

간절한 바람이 실린 웅혼한 공력이 전신 사지 백해로 뻗어 나갔다.



* * *



공간을 가르고 휘둘려진 코는 길고 거대했다.

마치 코끼리를 연상케 하는 그것은 날아드는 마법과 화살을 튕겨 내고, 이내 지상을 향해 쇄도했다.

후우우웅-!

사람들의 머리 위로 드리워진 짙은 그림자. 이를 악문 최민우가 몸을 날리며 외쳤다.

“산개!”

파파팟!

바람처럼 솟구친 신형들이 사방으로 흩어진다. 헌터라는 피라미드 계급도에서 가장 윗자리를 차지한 상위 헌터다운 움직임.

그러나 이 자리에 모인 이들이 A급 헌터라면, 그들이 마주한 적은 태고적 신화에 등장하는 네임드 몬스터였다.

- 그아아아아!

베히모스(Behemoth).

깊은 심연을 딛고 현세에 강림한 마수가 울부짖는다. 영혼과 움직임을 사로잡는 강력한 피어(Fear)가 흩어지던 헌터들을 뒤흔들었다.

“헉!”

“흡……!”

[영웅의 혼]이 뿜어내는 빛의 범위를 벗어난 평화 길드의 두 헌터가 헛숨을 삼켰다.

풍부한 실전 경험과 굳건한 정신력이 없었다면 당장 혼절하거나 미쳐 버렸을지도 모른다.

하지만 피어가 불러온 찰나의 혼돈만으로도, 교활한 마수는 원했던 결과를 얻을 수 있었다.

“안 돼!”

위험을 감지한 최민우의 외침보다, 베히모스가 반 박자 더 빨랐다. 그리고 그것이 두 사람의 운명을 결정지었다.

후웅, 콰직!

허공으로부터 일어난 돌풍이 대지를 내리찍었다.

상급 방어 마법이 부여된 갑옷과 극한까지 단련된 근육. 끈질긴 생명력. 그 무엇으로도 막을 수 없는 힘은 모든 것을 부수고 짓눌렀다.

“꺽. 커헉!”

단말마와 함께 검붉은 핏물이 터져 나온다. 전신의 뼈와 살은 물론, 내장까지 터져 나간 상황에서는 최상급 포션도 무소용이었다.

찰나의 순간, 빛이 사라져 가는 두 쌍의 눈동자와 시선이 마주친 최민우는 이를 악물었다.

‘또……!’

죽었다. 죽고, 또 죽었다.

거대한 앞발에 밟혀 죽고, 엄니에 꿰여 죽고, 휘둘려진 코에 전신이 으스러져 죽었다.

그렇게 자신과 김화종을 포함한 스물두 명의 헌터 중 절반이 넘는 인원이 처참한 죽음을 맞이했다.

만약 소지하고 있던 포션이 없었다면 그보다 더 많은 죽음을 이 눈으로 지켜봐야 했을 것이다.

이제는 그 포션마저도 이제 얼마 남지 않았지만.

‘빌어먹을.’

최민우는 이를 악물었다. 어느샌가 부서진 어금니에서 올라오는 통증은 희미했고, 찢어진 입술에서 흐르는 핏물도 느껴지지 않았다. 단지 분노와 의지만이 남아 있을 뿐이다.

그리고 그 두 개의 감정이, 최민우로 하여금 절망하여 쓰러지지 않게 했다. 두려움을 이겨 내고 베히모스를 향해 달려들게 했다.

“도련님!”

쉭!

김화종의 애탄 외침을 뒤로하고, 마나가 실린 발걸음이 대지를 박찼다.

빛살처럼 쇄도하는 그의 머리 위로 강맹한 파공성이 울려 퍼졌다. 최민우는 혼신의 힘을 다하여 신형을 비틀었다.

후웅, 꽈앙!

땅이 흔들린다. 지면을 뒤덮었던 눈발이 흩날리고 부서진 암석 조각이 이마를 할퀴었다. 시야를 가로막는 핏물은 붉었고, 최민우의 양손에 들린 검은 새하얀 광휘를 내뿜었다.

화아아악, 서걱!

자욱하던 어둠이 갈라졌다.

공간을 가른 빛줄기가 기둥처럼 서 있는 두 개의 앞다리를 베어 내자, 쩍 갈라진 상흔에서 막대한 양의 핏물이 터져 나왔다.

푸화아아악!

녹색의 핏물을 전신에 뒤집어쓴 최민우가 참았던 숨을 토해 냈다.

피하고 싶었으나, 피할 수 없었다.

비틀거리는 베히모스의 두 다리처럼, 짧은 순간 많은 힘을 쏟아낸 그의 신형도 흔들리고 있었다.

“네 개의 다리 중 두 개라…….”

최민우는 온통 녹색으로 물든 시야 속에서 작게 중얼거렸다.

열다섯 명의 헌터. 그리고 자신의 목숨값에 비하면 턱없이 비싼 금액이다.

그러나 고통에 찬 베히모스의 비명은 듣기에 썩 나쁘지 않았다.

- 그아아아아아아! 인. 간!

“……듣고 있다. 뭐라는 건지는 모르겠지만.”

최민우는 힘없이 대꾸했다.

잊고 있던 피로와 고통이 한꺼번에 몰려드는 듯했다. 손에 들린 [영웅의 혼]에서는 광휘가 금방이라도 꺼질 듯이 사그라들고 있었다.

‘조금만 더 버텨 주지. 조금만 더.’

그러나 너무 큰 욕심이었다.

송천우와의 혈전부터 시작된 피로는 지금까지 차근차근 누적되었고, 힐러의 죽음과 포션이 동나며 막을 수 없게 된 출혈과 부상은 그를 무너트리고 있었다.

스으윽.

세상이 기울었다.

아니, 기울고 있는 것은 세상이 아니라 최민우였다.

서서히 뒤집히는 시야 속에서, 그는 자신을 향해 날아드는 거대한 무언가를 보았다.

후우우웅!

전신을 으스러트릴 바람을 느끼며, 최민우는 눈을 감았다.



* * *



콰앙!

굉음과 함께, 유일했던 빛이 사라졌다.

주위에 자욱한 검은 안개 사이로 눈과 흙이 뒤섞인 구름이 피어올랐다.

구구구궁!

어느 때보다 강력했던 베히모스의 일격에, 산 전체가 몸을 떨었다.

살아남은 평화 길드의 헌터들은 절망 가득한 눈빛으로 그 광경을 바라보았다.

미약하게나마 가슴에 품었던 그들의 희망은 빛과 함께 사라진 후였다.

앞장서서 그들을 이끌었던 한 젊은이와 함께.

‘끝났다. 모든 것이.’

모두가 직감했다.

비록 이 세상은 끝나지 않겠지만, 적어도 그들이 바라보던 세상은 오늘, 이 자리에서 끝날 것이다.

그러나 마지막을 앞둔 그들의 마음은 이상하리만치 덤덤했다.

적어도 의무를 다했기 때문이다. 사람으로서의, 헌터로서의 의무.

부와 명예에 취해 잠시 잊고 있던 사명감을 아낌없이 쏟아부었기에 후회는 없었다.

“씨발, 엊그제 집 계약했는데.”

누군가의 중얼거림에 헌터들 사이로 실소가 터져 나왔다.

“저 미친 새끼.”

“쫄리면 가라. 안 붙잡는다.”

그러나 누구도 움직이지 않았다. 처음 말문을 열었던 헌터조차 마찬가지였다.

덜덜 떨리는 자신의 다리를 물끄러미 바라본 그가 툭 내뱉었다.

“어떻게 갑니까. 차라리 싸우다 죽고 말지.”

모두가 같은 마음이었다. 자신들의 등 뒤에는 아직 대피 중인 수천여 명의 사람들이 있다.

앞서 죽어 간 동료와 마지막까지 베히모스를 향해 쇄도했던 최민우는 바로 그들을 지키기 위해 죽은 것이다.

“우리는 돈도 많고, 가오도 있지.”

“그나저나 죽기 딱 싫은 날씨네. 좆 같은 안개 때문에 하늘이 안 보여.”

“근데 저 코끼리 새끼는 왜 갑자기 가만히 있지?”

몇 안 남은 이들이 각오를 다지며 베히모스를 향해 달려들려던 바로 그 순간이었다.

“죽을 필요 없네.”

나직한 목소리와 함께, 짙은 안개가 흩어졌다. 심연과도 같은 어둠을 몰아낸 것은 빛이 아닌 불꽃이었다.

화아아악!

맹렬한 불꽃과 함께 안개를 가르며 등장한 한 사람이 덧붙였다.

“적어도 자네들은.”

잘게 떨리는 사람들의 눈동자에 반백의 중년인이 비쳤다.

최민우를 쫓아 안개 사이로 사라졌던 김화종의 모습은, 처음과는 많이 달라져 있었다.

“……길드장님, 팔이.”

“괜찮네.”

왼팔이 뜯겨 나간 김화종은 지친 얼굴로 빙긋 웃었다.

비록 한쪽 팔을 잃었지만, 더욱 소중한 것을 구할 수 있었기에 나올 수 있는 웃음이었다.

그는 오른팔로 안고 있던 한 사람을 헌터들에게 넘겨주며 말을 이었다.

“자네들은 당장 이곳을 빠져나가게. 도련님과 함께.”

“하, 하지만.”

“길드장 명령일세.”

그르르르륵.

간발의 차로 놓친 먹잇감을 발견한 마수가 낮은 웃음소리를 흘린다.

김화종의 입가에 서려 있던 웃음기가 사라졌다.

“어서!”

“……!”

순간 터져나온 강렬한 호통에, 선택권이 없음을 깨달은 헌터들이 이를 악물었다.

축 늘어진 최민우를 넘겨받은 그들은 짧은 목례와 함께 신형을 날렸다.

쉬쉬쉬쉭!

가파른 경사를 미끄러지는 신형. 그 모습을 말없이 바라보던 김화종의 입가에, 다시금 희미한 웃음이 맺혔다.

‘무사하셔야 합니다. 반드시.’

닿지 않을 작은 중얼거림과 돌아섰을 때, 하나밖에 남지 않은 손에서는 겁화(劫火)가 일렁이고 있었다.

“와라. 이 개 좆 같은 새끼야.”

- 그아아아아!

마수의 거대한 눈동자와 화염이 깃든 시선이 허공에서 맞부딪친다.

모두를 떠나보내고 스스로 벼랑 끝에 선 노집사는, 어쩌면 마지막이 될지도 모르는 주문을 읊었다.

“지옥의 겁화여. 이곳에 임하라.”

헬 파이어(Hell Fire).

구구구구궁!
```

## Final English reading copy

```markdown
# Chapter 583

Team Leader Choi. Pyeongchang. Monster Wave.

The three keywords that had suddenly come crashing in left my mind in turmoil.

But the footage filling the electronic billboard left me no time to think.

—Kwooooom!

—Aaaahhh!

“An avalanche!”

People fled, screaming.

They stumbled along awkwardly without even thinking to take off their ski equipment, then fell as an enormous amount of snow and shattered rock came pouring down behind them.

—BOOOM!

Dozens of people were swept away by the snowdrift that surged over them like a wave, and red blood sprayed through the thunderous roar.

Buildings crushed beneath the rocks were engulfed in flames. And beyond those rolling flames lay the source of it all.

—Ruuuumble!

Although the sun had not yet set, the sky above that place was dark.

Black clouds had settled over an unfamiliar mountain peak.

Every time dazzling light flashed through them, tremendous vibrations and thunderous booms erupted.

*A Monster Wave.*

I understood instinctively.

In that place where light and darkness coexisted, a clash was taking place that would decide the fate of thousands.

And… Team Leader Choi, Butler Kim, and the Peace Guild Hunters were risking their lives against a named monster.

The voice of an announcer whose face was not visible came through the static.

—The government has declared the Pyeongchang area of Gyeonggi Province a disaster zone and dispatched emergency support forces. Meanwhile, the Monster Wave that occurred in Busan…

I had neither the reason nor the time to listen any further.

I spun around and shouted at the Hunters staring blankly at the electronic billboard on the high-rise building.

“Mages!”

“Y-Yes?”

“Mages, step forward! We have to get to Pyeongchang with Teleport! Right now!”

A few of the startled Hunters, jolted awake as if from a nightmare by the shout infused with internal energy, timidly raised their hands.

One A-grade mage and six B-grade mages. But despite stepping forward, their expressions were grim.

“I-I’m sorry, but it would be difficult for us to cast Teleport on our own.”

“What did you say?”

“We’ve all just fought monsters, so our mana fatigue is severe. On top of that, we need to draw a Teleport magic circle, and under the current circumstances…”

The mages let their voices trail off and looked around.

The corpses of victims and monsters lay scattered everywhere. The roads had been turned upside down.

Even among high-ranking mages, Teleport was famous for being difficult to cast. This was the worst possible environment in which to attempt it.

Skeleton King, who had been watching the situation, opened his mouth with a twisted expression.

“You stupid hu—bastards. Do you really think this is the time to worry about conditions? Do it. Please? Fuck. This is ridiculously hard.”

Despite barely holding back his anger, the murderous aura leaking from him made the mages swallow hard.

“B-But there’s nothing we can do right now. It’s too dangerous.”

“It’s impossible. Even if we succeeded against all odds, Busan to Pyeongchang is more than 250 kilometers. We can’t cross that kind of distance in a single jump.”

“Try it! Somehow, just try!”

Skeleton King’s shout was exactly what I wanted to say.

But I also knew the mages weren’t complaining for no reason. They weren’t Magic Johnson.

The dark-skinned Grand Mage who had sent me from Sichuan in China to a chaotic battlefield without even a magic circle was probably somewhere beyond the continent by now.

*Damn it.*

Sticky blood dripped from my clenched fist. I couldn’t tell whether it was mine or the monsters’. Maybe it was both.

“Isn’t there any other way?”

A middle-aged Hunter who appeared to be the highest-ranking person there answered in an anxious voice.

“We already contacted headquarters. We’re currently trying to locate a high-ranking mage among the Hunters in Busan who can cast Teleport, but…”

His voice trailed off. His expression was dark.

That was enough to tell me everything I needed to know about the situation.

After repeatedly urging the superior to hurry, I clenched my teeth.

*Damn it.*

Their opponent was a named monster. Something equal to—or even stronger than—the Kraken.

How much longer could they hold out against a monster whose might was conveyed even through the footage? How many of them would survive?

*Just a little longer. Please, hold out just a little longer.*

Muttering an unspoken plea that would never reach them, I sat down cross-legged.

For now, I had to replenish even a little of my depleted strength while we searched for a mage.

“Whoo.”

I closed my eyes, calming the anxiety and rage boiling inside me. Darkness covered my vision.

At the same time, the faces of those fighting in an even deeper darkness flashed before my eyes.

*Please… survive.*

Until I get there.

Whoooosh.

A profound internal energy carrying my desperate wish spread through my entire body, every limb and bone.

* * *

The trunk that swung through space was long and enormous.

It resembled an elephant’s trunk. It deflected the incoming magic and arrows, then rushed toward the ground.

Whoooosh!

A dense shadow fell over the people’s heads.

Choi Minwoo gritted his teeth, threw himself forward, and shouted.

“Scatter!”

Fwap-fwap-fwap!

The figures that had shot upward like the wind scattered in every direction.

It was movement befitting high-level Hunters at the very top of the Hunter hierarchy.

But if the people gathered here were A-grade Hunters, the enemy they faced was a named monster from ancient mythology.

—GRAAAAAAAH!

Behemoth.

The monster that had descended into the mortal world from the depths of the abyss let out a roar.

The powerful Fear that seized the soul and movement shook the Hunters as they scattered.

“Gasp!”

“Hk…!”

Two Peace Guild Hunters who had stepped outside the range of the light radiating from **Hero’s Soul** swallowed sharp breaths.

Without their wealth of real-combat experience and iron wills, they might have fainted or gone insane on the spot.

But even the momentary chaos brought on by Fear was enough for the cunning monster to achieve the result it wanted.

“No!”

Behemoth was half a beat faster than Choi Minwoo’s shout of warning.

And that determined the fate of the two men.

Whoom—CRUNCH!

A gust of wind erupted from empty air and slammed into the earth.

Superior defensive magic enchanted their armor. Their muscles had been trained to the extreme. Their vitality was tenacious.

But nothing could stop that force. It shattered and crushed everything in its path.

“Ghk. Cough!”

Dark red blood burst out with their dying cries.

Their bones, flesh, and even internal organs had been crushed. Not even the highest-grade potion could help them now.

For an instant, Choi Minwoo’s eyes met the two pairs of eyes in which the light was fading. He gritted his teeth.

*Again…!*

They had died. Died, and died again.

They had been trampled beneath enormous forelegs, pierced by tusks, and crushed from head to toe by the swinging trunk.

Of the twenty-two Hunters—including himself and Kim Hwajong—more than half had met gruesome deaths.

If they had not been carrying potions, he would have had to watch even more people die with his own eyes.

But now, even those potions were almost gone.

*Damn it.*

Choi Minwoo gritted his teeth.

The pain rising from his broken molar had faded before he knew it, and he could no longer feel the blood flowing from his split lips.

Only rage and determination remained.

Those two emotions kept Choi Minwoo from collapsing in despair. They helped him overcome his fear and charge toward Behemoth.

“Young Master!”

Whoosh!

Leaving Kim Hwajong’s anguished shout behind, Choi Minwoo’s mana-infused foot kicked off the earth.

A powerful sound of splitting air rang above his head as he rushed forward like a ray of light.

Choi Minwoo twisted his body with every ounce of strength he possessed.

Whoom—BOOOM!

The ground shook.

Snow that had covered the earth scattered, and shards of shattered rock scraped across his forehead.

The blood blocking his vision was red, and the sword Choi Minwoo held in both hands radiated a pure white brilliance.

Fwoooosh—slash!

The dense darkness split apart.

When the ray of light that cut through space sliced through the two forelegs standing like pillars, an enormous amount of blood burst from the deep, split wounds.

Fwoooosh!

Choi Minwoo, drenched from head to toe in green blood, exhaled the breath he had been holding.

He had wanted to avoid it, but he couldn’t.

Like Behemoth’s staggering legs, his own body was shaking after releasing so much strength in such a short moment.

“Two of its four legs…”

Choi Minwoo muttered faintly through his completely green-tinted vision.

Fifteen Hunters.

And compared to the price of his own life, it was an absurdly expensive exchange.

Still, Behemoth’s scream of pain was not unpleasant to hear.

—GRAAAAAAAH! Hu. Man!

“…I’m listening. I just don’t know what you’re saying.”

Choi Minwoo answered weakly.

The fatigue and pain he had forgotten came rushing over him all at once.

The brilliance radiating from **Hero’s Soul** in his hand was fading as though it might go out at any moment.

*Hold out a little longer. Just a little longer.*

But that was too much to ask.

The fatigue that had begun with his bloody battle against Song Cheonwoo had steadily accumulated until now.

The healer’s death and the depletion of their potions had left the bleeding and injuries unchecked, and they were bringing him down.

Ssssh.

The world tilted.

No—the world was not tilting.

Choi Minwoo was.

Through his slowly overturning field of vision, he saw something enormous flying toward him.

Whoooosh!

Feeling the wind that would crush his entire body, Choi Minwoo closed his eyes.

* * *

BOOOM!

With a thunderous crash, the only light disappeared.

A cloud of snow and dirt rose through the dense black mist surrounding them.

Ruuumble!

Under Behemoth’s most powerful strike yet, the entire mountain trembled.

The surviving Peace Guild Hunters watched the sight with eyes filled with despair.

The hope they had held in their hearts, however faintly, had vanished along with the light.

Along with the young man who had led them from the front.

*It’s over. Everything is over.*

They all realized it instinctively.

The world might not end, but at least the world they knew would end here, today.

And yet, strangely enough, their hearts were calm as they faced the end.

At least they had fulfilled their duty—their duty as human beings and as Hunters.

They had poured out all their sense of mission, which wealth and fame had briefly made them forget.

They had no regrets.

“Fuck. I just signed a house contract the day before yesterday.”

A snort of laughter escaped the Hunters at someone’s mutter.

“That crazy bastard.”

“If you’re scared, leave. Nobody’s stopping you.”

But no one moved.

Not even the Hunter who had spoken first.

He stared blankly at his trembling legs, then tossed out,

“How are we supposed to leave? I’d rather die fighting.”

Everyone felt the same way.

Thousands of people were still evacuating behind them.

The comrades who had died before them, and Choi Minwoo, who had charged toward Behemoth until the very end, had died to protect those people.

“We’ve got plenty of money, and we’ve got our pride.”

“Still, what a lousy day to die. I can’t even see the sky because of this shitty fog.”

“By the way, why is that elephant bastard suddenly standing still?”

It was just as the few remaining Hunters steeled themselves and prepared to charge Behemoth.

“You don’t need to die.”

With that quiet voice, the dense fog scattered.

What drove away the abyss-like darkness was not light, but flame.

Fwoooosh!

A man appeared through the fog amid fierce flames and continued,

“At least you don’t.”

The trembling eyes of the Hunters reflected a middle-aged man with half-gray hair.

Kim Hwajong, who had disappeared into the fog after chasing Choi Minwoo, looked very different from when he had first entered.

“…Guild Master, your arm.”

“I’m fine.”

Kim Hwajong’s left arm had been torn away, but he smiled faintly through his exhaustion.

It was the smile of someone who had lost one arm but managed to save something far more precious.

He handed the person he had been carrying in his right arm over to the Hunters and continued,

“You must leave this place immediately. With the Young Master.”

“But…”

“That is an order from the Guild Master.”

Grrrrr.

The monster let out a low laugh after finding the prey it had missed by a hair.

The smile faded from Kim Hwajong’s lips.

“Go!”

“...!”

At the fierce shout that erupted in an instant, the Hunters realized they had no choice and clenched their teeth.

They took Choi Minwoo’s limp body and launched themselves away with a brief bow.

Shhhh-shhhh-shhk!

Their figures slid down the steep slope.

Kim Hwajong watched them silently, then another faint smile appeared at the corners of his mouth.

*You must be safe. You have to be.*

When he turned away after murmuring the small plea that would never reach them, hellfire flickered in his one remaining hand.

“Come at me, you fucking bastard.”

—GRAAAAAAAH!

Behemoth’s enormous eyes and Kim Hwajong’s flame-filled gaze collided in midair.

The old butler, who had sent everyone away and placed himself at the edge of the cliff, began to recite a spell that might be his last.

“Hellfire of hell. Descend upon this place.”

**Hell Fire.**

Ruuuuumble!
```
