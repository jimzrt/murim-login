<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0569.txt",
      "sha256": "c19094f0da8f900fe1f74a290dd4f33333e53a10943cf32d18dae9f4d7405aaa",
      "bytes": 12956
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "a4ae647023abe8541df51c55188644268a05a94f7ca20dee4813583f5e0b8464",
      "bytes": 4116
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "60009961a837d4bc273d80695994fb70393237c8141a5e4653024e090024b3f7",
      "bytes": 179767
    },
    {
      "path": "characters/Cheonwoo.md",
      "sha256": "c2de64aa2b435c0baf9b6f4fc91a1f199c17b2dec6b3db24ad14d75a67f7af1d",
      "bytes": 590
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "97cbb208917730025e98e035d30729b2f7afce7af0f4975834cdd2063d5234be",
      "bytes": 553
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "28a375b6c8e184ace3d3be6e84d35dd839b38244de62395f2998ba4eeb59174a",
      "bytes": 976
    },
    {
      "path": "characters/Go Se-won.md",
      "sha256": "a1967709012cf3072b5fb3ed4ed45e2618382a1368b06a52e87dd5cba5ab526f",
      "bytes": 736
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "8471a2c83f8f2a43a22679ad88babc855d6ccdfb35ea0c2b5f81296732f19e36",
      "bytes": 1182
    },
    {
      "path": "characters/Song Cheonwoo.md",
      "sha256": "88cb1ac8afd9bd73a134ab1bbc8788d309b2601fdc2c0fc93632eaaf81d340b1",
      "bytes": 899
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "2ec9ceffbb5657bb64169e21c2b7e71af7f443286bd46d81eff0b803397e70be",
      "bytes": 174845
    }
  ],
  "estimated_tokens": 10496
}
-->

# Durable State Update — Chapter 569

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 569. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 569. Profile updates may replace only one
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
  "chapter": 569,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 569,
    "continuity_sources": [569],
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
    "Choi is working with Song Cheonwoo against Go Jun's control of Ares Guild, while Song knows where Choi's maternal grandfather Cheon Taemin is located and Cheon Taemin remains hidden.",
    "Taekyung is a Supreme Peak master publicly recognized as S-rank-level while retaining an A-rank license, leads the Fire Dragon Pavilion's first Nanman mission, and is Peace Guild's wealthy modern-world patron.",
    "The six-member Fire Dragon Pavilion mission is entering Nanman through the Journey to Nanman Quest, whose reward is a linked quest and whose failure penalty is Can't Go to Nanman.",
    "Mungyeong ended Taekyung's direct training and assigned him the final task of incorporating martial principles into his learned martial arts; Cheongpung accompanies Mungyeong.",
    "Dark Heaven remains a monster-like threat capable of causing rifts and creating mutants, while the mechanism behind Jang Sam's transformation remains unresolved.",
    "The Mount Song Resolution restored the Murim Alliance with Mae Jonghak as Alliance Leader and Jeok Cheongang heading the Five Kings Hall; Zhuge Feng's Demon-Sealing Formation still blocks mana from the exposed Gate while Jang Taebo processes the Water God Dragon's remains.",
    "Go Jun has become increasingly ruthless, controls Ares Guild's legacy, and has seized Song Cheonwoo's children while calling the abduction protection.",
    "Go Se-won commands Ares Guild's thirty-member A-rank security team and remains obedient to Go Jun despite growing moral conflict over the orders.",
    "The Skeleton King was the person who applauded Taekyung and appeared as King Fury; Taekyung now trusts him enough to handle suitable emergencies alone and has granted him greater freedom.",
    "Taekyung has resumed isolated qi circulation and training while pursuing a new path suggested by a faint clue."
  ],
  "continuity_sources": [
    568,
    567
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "What will Taekyung's party find in Nanman, and what does the Southern Heaven Demon Empress intend there?",
    "What process created Jang Sam's mutant form, whether Dark Heaven's mutants can absorb human energy, and whether it relates to the Mutated Gate?",
    "What will result from the duel between Jeok Cheongang and Nangong Cheon, and why did Ju Hwaran and Sama Pyo's political engagement end?",
    "How will Song Cheonwoo respond after learning that Go Jun seized his children?"
  ],
  "safe_through": 568,
  "temporary_decisions": [
    "Render 건량 as dry rations, 광서 as Guangxi, 대별산 as Mount Daebyeol, 만리행 as Ten-Thousand-Li Journey, and 고잉메리호 as Going Merry.",
    "Render 반 시진 as half a shichen and retain Nanman, Nanman Beast Palace, Fire Dragon Pavilion, Great Hero, and Young Lady Ju.",
    "Render 남만행 as Journey to Nanman, 남만을 못 가 as Can't Go to Nanman, 면구 as disguise mask, 역용술 as disguise technique, 각주님 as Pavilion Master, 로그아웃 as Logout, and 동기화 as Synchronization.",
    "Render 일기당천 as One Against a Thousand, 거인의 포효 as Giant's Roar, 투로 as combat sequence, 타락한 엔트 as Corrupted Ent, 붉은 눈 as Red Eye, 치코리타 as Chikorita, 대마도사 as Grand Mage, 순간이동 as Teleportation, 텔레포트 as Teleport, 변이 게이트 as Mutated Gate, and 몬스터 웨이브 as Monster Wave.",
    "Render 현혹 마법 as enchantment magic, 장거리 텔레포트 마법진 as long-distance Teleportation magic, 킹 퓨리 as King Fury, and 배리어의 국장 in this context as Director of Barrier."
  ],
  "version": 1
}
```

## Exact glossary matches

| 이정룡    | **Lee Jungryong** |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 부길드장    | **Vice Guild Master** |
| 팀장      | **Team Leader**       |
| 귀가      | **your family**                                                 |
| 천우 | **Cheonwoo** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 고세원 | **Go Se-won** | Ares Guild Head of Security and Team Leader. |
| 송천우 | **Song Cheonwoo** | Ares Guild Director, former third-ranked Korean Hunter, and longtime European regional branch director. |
| 평화 | **Peace Guild** | Guild name. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 경호팀장 | **Head of Security** | Go Jun's security-team office under Lee Jungryong. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 텔레포트 | **Teleport** | Taekyung's label for the Blood Lord's unexplained disappearance. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 국장 | **national funeral** | State funeral reported for Lee Jungryong. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 이정룡 | 고준 | Master to Disciple | Go Jun | familiar and testing | Lee switches from Seok's office title to his personal name while considering whether he can defeat Taekyung. |
| 고준 | 이정룡 | Disciple to Master | Master | deferential | Go Jun responds to Lee's personal-name address as 스승님. |
| 팀원 | 석고준 | subordinate security-team member to security-team leader | Team Leader | fearful formal-polite | The team member repeatedly addresses Go Jun as 팀장님 while reporting the strange object. |
| 석고준 | 고세원 | Ares Vice Guild Master to Head of Security | you | curt and informal | Go Jun tells Go Se-won that he is later than usual when Se-won enters the wrecked office. |
| 고세원 | 석고준 | subordinate_to_Vice_Guild_Master | Vice Guild Master | formal-deferential | Uses 부길드장님 while trying to stop Go Jun from watching the broadcast. |
| 송천우 | 석고준 | adversary; captor of Song's children | you | shocked and confrontational | Song reacts directly to Go Jun's admission that he took the children. |

## Listed compact profiles

### Cheonwoo.md

# Cheonwoo (천우)

- **Safe through:** Chapter 568
- **Aliases:** None
- **Role:** One of the five current Five Gates of Shanxi scions and a First Rate martial artist present at Honghwa Inn.
- **Personality:** Pampered and contemptuous toward Cheongpung's group as part of the five scions' collective mockery.
- **Voice:** Mocking in the group's exchange; no distinct individual speech is established.
- **Relationships:** Associates with Seongryong, Myeonghwa, Sohye, and Jintae as a group of current Five Gates scions.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 567
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 568
- **Aliases:** Team Leader Seok
- **Role:** Go Jun is Ares Guild's Vice Guild Master, Lee Jungryong's disciple and former Head of Security, and the de facto successor to Lee's Ares legacy who passed the S-rank Hunter qualification assessment with a very high score but lacks Lee's legitimacy.
- **Personality:** Disciplined and controlled under ordinary pressure, fiercely loyal to Lee Jungryong, but consumed by humiliation and rage when Ares Guild's authority is challenged.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Disciple and direct protégé of Lee Jungryong, Go Jun inherited Lee's Ares Guild legacy after his death, regards Jin Taekyung and Choi Minwoo as enemies seeking to take it away, and has seized Song Cheonwoo's children as leverage while calling it protection.

### Go Se-won.md

# Go Se-won (고세원)

- **Safe through:** Chapter 567
- **Aliases:** Head of Security
- **Role:** Go Se-won is Ares Guild's Head of Security and a Team Leader with privileged access to restricted Section A.
- **Personality:** Composed and confident in public, he is mildly uncomfortable with Ares Guild's increasingly severe discipline but obeys its policy.
- **Voice:** Calm and deferential toward superiors, but blunt and decisive when issuing orders.
- **Relationships:** Go Se-won reports to Vice Guild Master Go Jun, commands Ares Guild's thirty-member security team, and is married with a young son, Sangho, while his wife is pregnant with their second child.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 567
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

### Song Cheonwoo.md

# Song Cheonwoo (송천우)

- **Safe through:** Chapter 568
- **Aliases:** Director Song
- **Role:** Ares Guild Director and former A-rank Hunter who reached third place among Korean rankers, briefly headed the Hunter training center, and led Ares Guild's European regional branch for twenty years; he now leads an internal faction capable of threatening Go Jun.
- **Personality:** Highly ambitious, honor-obsessed, politically calculating, and determined to use his final opportunity to reclaim influence before retirement.
- **Voice:** Not established.
- **Relationships:** Song Cheonwoo followed Cheon Taemin since before Team Leader Choi was born, was Lee Jungryong's former friend and rival, was exiled to Europe after Lee's victory, is aligned with Choi against Go Jun, and has had his children seized by Go Jun as leverage.

## Korean source

```text
＃569화



쿵.

등 뒤에서 문이 닫히는 소리가 천둥처럼 울려 퍼졌다. 동시에 일흔이라는 나이가 무색할 만큼 건장한 체구를 지닌 그, 송천우의 신형이 비틀거렸다.

스륵, 탁.

강대한 마나도, 지금까지 산전수전을 겪으며 쌓아 올린 경륜도 지금만큼은 무소용이다.

벽면을 붙잡고 바닥만 빤히 노려보는 그의 시야에, 한 쌍의 검은 구두가 불쑥 비집고 들어왔다.

“괜찮으십니까?”

귓가를 파고드는 사무적인 목소리. 고개를 들어 구두의 주인을 확인한 송천우가 이를 악물었다.

“지금 이게…… 괜찮아 보이느냐?”

불꽃이 튀는 그의 눈동자에, 경호팀장 고세원이 고개를 숙였다.

“불편하게 들리셨다면 죄송합니다.”

“마음에도 없는 소리는 집어치워라. 당장 네놈의 목을 꺾어 버리기 전에!”

“그다지 권하고 싶은 방법은 아니군요. 득은 없고, 실만 있을 겁니다.”

고세원은 말과 함께 손을 부드럽게 내저었다.

심상치 않은 기색을 눈치채고 저 멀리 복도 끝에서 막 걸음을 떼려던 경호팀원들이 움직임을 멈췄다.

“제 밑에 있는 친구들인데, 지사장님께서도 아시다시피 실력이 꽤 좋습니다. 상황이 닥치면 물불 안 가리는 면모도 있고요.”

“네놈…….”

“오해 없으시길 바랍니다. 더 이상 상황을 악화시키지 않으셨으면 하는 마음에 드리는 말씀입니다.”

콰득.

벽을 짚은 손아귀에 힘이 실리자 강화 마법이 걸린 대리석 벽면이 거미줄처럼 갈라졌다.

핏발 선 눈으로 고세원을 노려보던 송천우가 씹어 뱉듯이 입을 열었다.

“그래서 이 일과는 아무런 상관도, 죄도 없는 우리 애들을 납치했나?”

“그런 것치고는 방비가 철두철미하더군요. 지사장님께서도 일말의 가능성 정도는 염두에 두셨다는 뜻이겠죠.”

경호팀 전원이 습격했음에도 두 명의 사망자가 발생했다.

아레스 길드 내에서도 최정예로 꼽히는 그들의 수준을 생각한다면, 두 명의 사망자 앞에는 ‘무려’라는 두 글자가 붙어야 한다.

“가족분들의 일에 관해서는 저도 유감스럽게 생각합니다만. 사전에 의심하셨다면 그 이상의 전력을 투입해서라도 지켰어야 했습니다.”

“……!”

“괜한 말을 했군요. 죄송합니다.”

고세원의 말은 진심이었다. 송천우는 이미 죽을 날을 받아 둔 늙은 사자나 다름없는 상황. 굳이 자신이 나서서 가슴에 비수를 꽃을 필요까지는 없었다.

‘안타까움에 튀어나온 말이라고 하면, 이자는 믿을까.’

그도 가장이다. 마흔이 넘어 처음으로 본 아들도, 몇 달 후 태어날 둘째는 벌써부터 눈에 넣어도 아프지 않았다.

고세원은 자식들의 안전과 행복을 위해서라면 목숨도 바칠 수 있었다. 그것이 아버지고, 부모였으니까.

하지만 송천우는 자신의 야심과 가족들의 안위를 저울추에 올려놨다.

하긴, 최악의 상황을 생각했다면 석고준을 적으로 돌릴 시도조차 안 했을 것이다.

‘……내가 할 수 있는 말은 아니지만.’

고세원은 스스로가 병신 같은 악당처럼 느껴졌다.

근 십수 년 동안 헌터보다는 해결사라 부를 만한 인생을 살아온 그다.

이정룡의 눈에 들어 경호팀에 들어온 이후 주 표적은 몬스터가 아닌 사람이었으니까.

팀원들에게 송천우의 가족들을 납치하라는 명령을 내리고 깔끔하게 뒤처리를 한 것도 그였다.

‘그런 주제에 누구에게 훈계질을.’

결국 모두가 같은 똥통 속의 똥일 뿐이다.

송천우는 은퇴를 앞두고 야심에 불타올라 위험을 자초했고, 석고준은 수단과 방법을 가리지 않고 칼을 휘둘렀으며, 고세원은 상관이 휘두르는 검이 되어 송천우의 가족을 납치했다.

‘나쁜 놈들 간의 전쟁. 끝에 남은 건 승자와 패자뿐이지.’

그리고 자신은 부속품에 불과하다.

고세원이 씁쓸하게 입맛을 다시던 그때.

와락!

칠순 노인의 것이라곤 생각하기 힘든 단단한 손아귀가 그의 멱살을 붙들었다.

“팀장님!”

“됐다. 자리나 지켜.”

팀원들을 만류한 고세원이 머리 하나는 큰 송천우를 덤덤하게 응시했다.

“이미 말씀드렸습니다. 득보다 실이 많을 거라고.”

“네놈, 네놈들이 감히 내 새끼들을……!”

“부 길드장님께서 안에서 듣고 계실 겁니다. 두 분이서 무슨 대화를 나누셨는지는 모르겠습니다만, 그래도 추가적인 희생은 없었으면 합니다.”

“……!”

가족들의 명줄을 틀어쥔 석고준의 심기를 거스르지 말라는 뜻.

그 말에 담긴 의미를 즉각 알아차린 송천우의 눈꺼풀이 잘게 떨렸다.

이를 악문 채 고세원을 노려보던 그의 손아귀에서 스르륵 힘이 풀렸다.

“잘 생각하셨습니다.”

“……주둥이 닥쳐라. 마음 같아서는 당장 네놈의 면상을 뭉개 버리고 싶으니까.”

“그러시겠죠.”

고세원의 입가에 씁쓸한 미소가 스쳤다. 자신 같았어도 그와 같은 반응을 보였을 테니까.

그리고 냉정하게 평가했을 때, 송천우는 현역에서 물러난 지 이십 년이 지난 지금에도 충분히 대단한 실력자였다.

지닌바 능력이 야심에 비해 모자랐을 뿐. 한때나마 이정룡의 정적(政敵)이었다는 것만으로도 그를 설명하기에는 충분하다.

‘그래서 굳이 이런 지저분한 방법을 택한 거고.’

이번에 석고준이 택한 방식은 마음에 들지 않지만, 지저분한 만큼 효과는 확실하다.

빠른 시일 내에 송천우는 제거될 것이다. 누구도 의심을 품지 못할 만큼 아주 자연스럽게.

“따라오십시오. 밖까지 안내해 드리겠습니다.”

목례를 취한 고세원이 먼저 걸음을 옮기자, 고개를 돌려 굳게 닫힌 문을 한차례 노려본 송천우가 뒤를 따랐다.

저벅. 저벅.

고세원이 팀원들을 물린 탓에 복도에는 두 사람의 걸음 소리만 울려 퍼졌다.

그리고 짧게 이어지는 적막함을 깨트린 것은 송천우의 한마디였다.

“아까 했던 말. 사실이냐?”

“……?”

“석고준과 내가 무슨 대화를 나눴는지 모르겠다고 한 것, 사실이냐고 물었다.”

잠시 말에 담긴 뜻을 생각하던 고세원이 묵묵히 고개를 끄덕였다.

“그렇군. 하긴, 조사해 본 바로는 네놈도 책사와는 거리가 멀지.”

“그게 무슨.”

“생각했던 것만큼 신임받는 수하는 아닌 모양이군. 아니면 최측근에게도 숨기고 싶던가.”

미간을 찌푸린 고세원의 모습에, 송천우가 힘없는 실소를 흘렸다.

“이봐, 고세원이.”

잠깐 사이 십 년. 아니 이십 년은 늙어 버린 그가 허탈한 목소리로 말을 이었다.

“사람에게는 무릇 정도라는 게 있는 법이야. 알고 있나?”

“……부길드장님을 비난하시는 거라면. 그쯤에서 멈추라고 말씀드리고 싶군요.”

“비난이라, 생각했던 것 이상으로 부드러운 단어군. 석고준 그놈에게 쓰기에는 턱없이 부족해.”

“심정은 이해합니다. 하지만 이 일에 관련된 그 누구도 서로를 욕할 수 없습니다. 저 역시 지사장님께서도 그리 깨끗하게 살아오지 않으셨다는 것 정도는 알고 있고요.”

“허허, 그렇지. 한때는 나 역시 목적을 위해 수단과 방법을 가리지 않았던 적이 있었지. 하지만 이 정도까지는 아니었어.”

실성한 듯 공허한 웃음을 터트리는 송천우의 모습에, 고세원은 문득 입을 다물었다.

지금 그가 말하고자 하는 것이 비단 납치에 관한 것만이 아니라는 것을 깨달은 것이다.

‘뭐지?’

쿵쿵. 가슴이 뛰고 전류가 등골을 훑고 지나간다.

이건 경고다. 들어서는 안 된다는 위험 신호. 하지만 그의 몸은 생각과 반대로 움직이고 있었다.

“뭡니까. 지사장님께서 말씀하시는 그 정도라는 것이.”

“최소한의 본분도 잊어버린, 괴물.”

“네?”

저벅.

송천우의 발걸음이 우뚝 멈췄다. 밖으로 향하는 텔레포트 마법진을 말없이 바라보던 그가 말을 이었다.

“인간과 괴물의 경계. 석고준 그놈은…… 이미 괴물이 되어 버렸어.”

문득 노인의 텅 빈 눈빛이 허공을 훑었다.

찬란했던 과거의 기억을 더듬던 송천우는 마법진을 향해 힘없이 걸음을 내디뎠다.

간절함이 담긴 한 마디를 남긴 채.

“내가 자네에게 했던 행동에 대해서는 사과하겠네. 그러니 부디, 그 아이들이 덧없이 죽는 것만큼은 막아 주게.”

그것이 마지막이었다.

파앗!

고세원이 뭐라 되물을 새도 없이, 텔레포트 마법이 발현되며 눈부신 광채가 한 사람의 신형을 집어삼켰다.

홀로 남은 채 혼란스러운 눈빛으로 송천우가 서 있던 자리를 바라보던 고세원은 문득 고개를 돌렸다.

온통 새하얀 대리석으로 이루어진 복도.

그리고 끝없이 이어진 복도 끝에 굳게 닫힌 문과, 그 안에서 흡족한 기분으로 와인을 홀짝이고 있을 누군가.

‘도대체…… 무슨 일을 벌이신 겁니까.’

고세원은 마음 깊은 곳 어딘가를 향해 중얼거렸다.

언제나 환했던 A구역이, 오늘만큼은 어둠이 가득한 구렁텅이처럼 느껴졌다.



* * *



연무장. 현대에서는 트레이닝 룸이라고 부르는 이곳에 얼마나 틀어박혀 있었는지 모르겠다.

하루. 이틀. 어쩌면 사흘.

사방이 가로막혀 있고 온도가 조절되는 이곳에서 무공에 몰두하다 보니 시간의 흐름을 제대로 느낄 수 없었다.

스마트폰이 있어도 들여다보지 않으니 알 수 없었고, 그런 내 사정을 어렴풋이 알았는지, 평화 길드의 누구도 나를 찾아오거나 연락하지 않았다.

“…….”

말하다 보니까 아싸가 따로 없지만. 그건 절대 아니다.

……아마도 아닐 거다.

‘스켈레톤 킹. 그 녀석도 그 후로는 한 번도 안 찾아왔고.’

녀석이 생각보다 잘 해결해 내고 있다는 증거이니 희소식이긴 한데, 그만큼 긴급 구조팀이 바빠졌으며 이상 현상을 보이는 게이트가 많아졌다는 뜻이니 마냥 기뻐할 수는 없는 일이다.

그리고 그런 의미에서, 내가 시도하는 일이 거의 마무리 되어 가고 있다는 건 분명 확실한 희소식이 맞았다.

‘물론 아직까지는 미완성이지만.’

처음 시도해 보는 것이라 그런지, 지금까지의 과정은 결코 쉽지 않았다.

어쩌면 일촉즉발과도 같은 현재 상황에 맞물려 그만큼 뛰어난 것을 만들어야 한다는 부담감도 한몫했을 것이다.

‘지금까지만 해도 충분히 괜찮을 것 같기는 한데…….’

그냥 이대로 확 질러 버릴까.

지금까지 수십, 수백 번이나 떠올렸던 그 고민을 다시 머릿속에서 반복하던 그때.

익숙한 기계음과 함께 굳게 닫혀 있던 트레이닝 룸의 출입문이 열렸다.

“여기 있었군. 마침 자네의 도움이 필요해.”

뚜벅. 뚜벅.

물광을 낸 군화. 파란색 쫄쫄이와 해골 문양이 새겨진 방패.

나는 남극 세종 기지 건물 위에 쌓인 눈보다 차가운 시선으로 놈을 바라보았다.

“저 시벌 놈 보게, 저거.”

“킹 퓨리 국장에게 이야기는 들었겠지?”

“……이제는 1인 2역도 하냐?”

“후후. 역시 미합중국의 시민이라면 응당 킹틴 아메리카 아니겠나.”

“이 새끼는 자꾸 이름을 지 멋대로 바꾸네. 다시 빙하로 돌아가고 싶을만큼 처맞으려고.”

“하루 종일도 할 수 있어.”

쉬익, 쾅!

빛살처럼 쏘아보낸 백염의 창날이 놈의 목을 스쳐 트레이닝 룸의 벽을 관통한다.

자루까지 박힌 창과 나를 번갈아 바라보던 스켈레톤 킹이 중얼거렸다.

“하루 종일은 무리겠는데…….”

“개소리 집어치우고. 뭐하러 왔어? 참고로 심심해서 들른 거면 죽는다. 진짜.”

스켈레톤 킹이 황급히 대답했다.

“그, 그거 아니다. 임무다. 임무!”

“임무?”

“그렇다. 간악한 인간이여.”

고개를 끄덕인 녀석이 말을 이었다.

“평범한 변이 게이트가 아니다. 엄청난 마력 수치야.”

“……!”

빌어먹을.
```

## Final English reading copy

```markdown
# Chapter 569

*Boom.*

The sound of the door closing behind him rang out like thunder. At the same time, Song Cheonwoo’s sturdy frame—one that made it hard to believe he was seventy—staggered.

*Slide. Tap.*

His powerful mana and the experience he had built up after weathering countless hardships were useless at that moment.

As he clutched the wall and glared at the floor, a pair of black dress shoes suddenly intruded into his field of vision.

“Are you all right?”

The businesslike voice pierced his ears. Song Cheonwoo raised his head to confirm the owner of the shoes and gritted his teeth.

“Does this look all right to you?”

At the fire flashing in his eyes, Head of Security Go Se-won bowed his head.

“I’m sorry if that sounded insensitive.”

“Spare me the empty words. Before I break your neck!”

“I wouldn’t recommend that. You’d gain nothing and only stand to lose.”

As he spoke, Go Se-won gently waved one hand.

The security-team members who had just begun moving from the far end of the hallway, having noticed that something was wrong, stopped where they were.

“They’re my men. As you know, Director, they’re quite capable. And when the situation calls for it, they don’t care what they have to do.”

“You…”

“Please don’t misunderstand me. I’m saying this because I don’t want you to make the situation any worse.”

*Crack.*

As strength surged through the hand braced against the wall, the marble surface—reinforced with magic—split like a spiderweb.

Song Cheonwoo glared at Go Se-won with bloodshot eyes and spat out the words through clenched teeth.

“So you kidnapped my children even though they had nothing to do with this and had committed no crime?”

“They were exceptionally well guarded for people who supposedly had nothing to do with it. That means you had at least considered the possibility, Director.”

Even though the entire security team had launched the attack, two of them had died.

Considering the level of the elite Hunters who were regarded as the best Ares Guild had to offer, those two deaths deserved the words *no fewer than* in front of them.

“I do regret what happened to your family. But if you suspected something in advance, you should have protected them by deploying even more forces.”

“……!”

“I shouldn’t have said that. I apologize.”

Go Se-won’s words had been sincere. Song Cheonwoo was already in a situation no different from that of an old lion who had been given a date for his death. There was no need for Go Se-won to step forward and drive a dagger into his heart as well.

*If I say those words simply slipped out because I felt sorry for him, will he believe me?*

He was a father too. His first son, born after he turned forty, and his second child, due in a few months, were already unimaginably precious to him.

Go Se-won could give his life for the safety and happiness of his children. That was what it meant to be a father. To be a parent.

But Song Cheonwoo had placed his ambition and his family’s safety on opposite sides of a scale.

Then again, if he had considered the worst-case scenario, he would never have tried to make Go Jun his enemy in the first place.

*……It isn’t my place to say that.*

Go Se-won felt like a pathetic villain.

For nearly fifteen years, he had lived a life that was better described as that of a fixer than a Hunter.

Ever since Lee Jungryong had taken notice of him and brought him into the security team, his primary targets had not been monsters but people.

He was the one who had ordered his men to kidnap Song Cheonwoo’s family and then cleaned up the aftermath.

*And I have the nerve to lecture someone else.*

In the end, they were all just pieces of shit in the same cesspool.

Song Cheonwoo had been consumed by ambition on the verge of retirement and brought danger upon himself. Go Jun had wielded his blade without regard for means or methods. And Go Se-won had become the sword in his superior’s hand and kidnapped Song Cheonwoo’s family.

*A war between bastards. In the end, all that remains are the victor and the defeated.*

And he was nothing more than a component.

Just as Go Se-won was bitterly savoring that thought—

*Lunge!*

A powerful hand that was hard to believe belonged to a seventy-year-old man seized him by the collar.

“Team Leader!”

“Enough. Stay at your posts.”

Go Se-won restrained his men and calmly looked up at Song Cheonwoo, who was a full head taller than him.

“I already told you. You’ll suffer more losses than gains.”

“You bastards dare lay a hand on my children…”

“The Vice Guild Master is listening inside. I don’t know what the two of you discussed, but I hope there won’t be any more unnecessary sacrifices.”

“……!”

In other words, do not provoke Go Jun, who held the lives of his family in his grasp.

Song Cheonwoo immediately understood the meaning behind those words, and his eyelids began to tremble.

He continued glaring at Go Se-won with his teeth clenched, but the strength gradually seeped out of his grip.

“You made the right choice.”

“……Shut your mouth. I want nothing more than to smash your face in right now.”

“I’m sure you do.”

A bitter smile crossed Go Se-won’s lips. He would have reacted the same way in Song Cheonwoo’s position.

And by any objective assessment, Song Cheonwoo was still an extraordinary fighter, even though twenty years had passed since he retired from active service.

His abilities had simply fallen short of his ambition. The fact that he had once been Lee Jungryong’s political rival was enough to explain what kind of man he was.

*That’s why he chose such a filthy method.*

Go Jun’s method this time displeased him, but for all its filthiness, its effectiveness was undeniable.

Song Cheonwoo would be eliminated soon. Naturally—so naturally that no one would suspect a thing.

“Follow me. I’ll escort you outside.”

Go Se-won gave a slight bow and walked ahead. Song Cheonwoo glanced once more at the tightly closed door, then followed him.

*Step. Step.*

Because Go Se-won had sent his team members away, only the footsteps of the two men echoed through the hallway.

The silence that followed was broken by Song Cheonwoo’s voice.

“What you said earlier. Was it true?”

“……?”

“You said you didn’t know what Go Jun and I had discussed. Was that true?”

Go Se-won thought for a moment about the meaning behind the question, then quietly nodded.

“I see. Then again, according to what I investigated, you’re hardly the strategist type.”

“What does that mean?”

“You’re apparently not as trusted a subordinate as I thought. Or perhaps he wanted to hide it even from his closest aide.”

At the sight of Go Se-won frowning, Song Cheonwoo let out a weak, hollow laugh.

“Go Se-won.”

In the brief span of time between one breath and the next, he seemed to have aged ten years. No—twenty. He continued in a desolate voice.

“There’s such a thing as a line a person shouldn’t cross. You know that?”

“……If you’re going to criticize the Vice Guild Master, I’d like to ask you to stop there.”

“Criticize? That’s a much gentler word than I expected. It’s far too mild for that bastard Go Jun.”

“I understand how you feel. But no one involved in this matter has the right to condemn anyone else. I know that you haven’t lived a particularly clean life either, Director.”

“Hah. That’s true. There was a time when I didn’t care what means I used to achieve my goals. But I never went this far.”

At Song Cheonwoo’s empty, almost deranged laughter, Go Se-won suddenly fell silent.

He realized that Song Cheonwoo was not talking only about the kidnapping.

*What is this?*

His heart pounded. Electricity ran down his spine.

This was a warning. A danger signal telling him not to listen.

But his body moved contrary to his thoughts.

“What do you mean by that line, Director?”

“A monster who has forgotten even the most basic duty of being human.”

“What?”

*Step.*

Song Cheonwoo abruptly stopped walking. He stared silently at the Teleportation magic circle leading outside, then continued.

“The boundary between humans and monsters. That bastard Go Jun…… has already become a monster.”

For a moment, the old man’s empty gaze swept across the air.

As he rummaged through the memories of a brilliant past, Song Cheonwoo weakly stepped toward the magic circle.

He left behind one final plea.

“I apologize for what I did to you. So please, stop those children from dying a meaningless death.”

That was the last thing he said.

*Flash!*

Before Go Se-won could ask what he meant, Teleportation magic manifested, and dazzling radiance swallowed Song Cheonwoo’s body.

Left alone, Go Se-won stared at the spot where Song Cheonwoo had been standing with a bewildered look in his eyes. Then he suddenly turned his head.

A hallway made entirely of pure white marble.

At the end of the hallway that stretched endlessly ahead stood a tightly closed door. Behind it was someone who was probably sipping wine in satisfaction.

*What in the world…… have you done?*

Go Se-won muttered toward something deep inside his heart.

Section A, which was always filled with light, felt like a pit overflowing with darkness today.

* * *

I had no idea how long I had been shut away in the training ground—a place people in the modern world called a training room.

A day. Two days. Maybe three.

With walls surrounding me on every side and the temperature regulated, I had become so absorbed in martial arts that I could not properly feel the passage of time.

Even though I had a smartphone, I never looked at it, so I had no way of knowing. Perhaps they vaguely understood my situation, because no one from the Peace Guild came to see me or contacted me.

“…….”

Now that I put it that way, I sounded like a complete loner. But that was absolutely not the case.

……Probably not.

*The Skeleton King hasn’t come to see me even once since then, either.*

It was good news that he seemed to be handling things better than expected, but that also meant the emergency rescue team had grown busier and that more Gates were exhibiting abnormal phenomena. It was not something I could simply celebrate.

And in that sense, the fact that what I was attempting was almost complete was definitely good news.

*Of course, it’s still unfinished.*

Perhaps because it was my first attempt, the process so far had been far from easy.

The pressure of having to create something exceptional while the current situation was on the verge of exploding may have contributed as well.

*What I have so far seems good enough……*

Should I just take the plunge and go with it?

I was repeating that same dilemma in my head—the one that had occurred to me dozens, perhaps hundreds, of times—when the tightly closed door to the training room opened with a familiar mechanical sound.

“So this is where you were. I need your help, as it happens.”

*Step. Step.*

Polished combat boots. A blue skin-tight suit and a shield emblazoned with a skull.

I looked at him with a gaze colder than the snow piled atop the King Sejong Station building in Antarctica.

“Look at that fucking bastard.”

“You heard from Director King Fury, didn’t you?”

“……Are you playing two roles now?”

“Heh heh. Surely any citizen of the United States of America should be King-tin America.”

“This bastard keeps changing his name however he wants. I’m going to beat you so badly you’ll want to go back to the glacier.”

“I can do this all day.”

*Whoosh! Boom!*

The White Flame spearhead shot out like a streak of light, grazed his neck, and pierced through the wall of the training room.

The Skeleton King stared back and forth between me and the spear embedded in the wall all the way to its shaft, then muttered.

“Doing this all day might be a little difficult……”

“Cut the bullshit. Why are you here? And for the record, if you just stopped by because you were bored, you’re going to die. I mean it.”

The Skeleton King hurriedly answered.

“N-no, it’s not that. It’s a mission. A mission!”

“A mission?”

“That is correct, wicked human.”

He nodded and continued.

“It is not an ordinary Mutated Gate. The magic power reading is enormous.”

“……!”

Damn it.
```
