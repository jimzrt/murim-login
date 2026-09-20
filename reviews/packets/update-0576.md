<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0576.txt",
      "sha256": "2f5930071b484182d92e11d9ac3918db986ccab2d073ddff4962860cf10b055e",
      "bytes": 15395
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "88a77791fbcbecd2ad00cc4ee8991af77121fe3f7455cf1b7cd8c5a0777f0194",
      "bytes": 1431
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0f849fae61e36ce32e6889bb198356858689d613f5f9f6a8bcbaa3ec9fa2a1d6",
      "bytes": 181965
    },
    {
      "path": "characters/Cheonwoo.md",
      "sha256": "25b625de177ef209cab8dafade869bf0b1e16f19480c6c0c21a200e50a009e62",
      "bytes": 590
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "0012f88c1b67b949e2e98a8737d3e154972cb5380d4f3383bf9d115f83a3d44a",
      "bytes": 553
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "6475a143705704e7b33f17abc7bb07f2a2cbd4df4fe5ae018b3134fc639de040",
      "bytes": 976
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "a19b71d3a10907ff6b7d6c5614eb25935f0f67832951f6b483e360a1e0b30dff",
      "bytes": 2280
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "4beea7c9c2a409985f8199608bae3087f48295895fb7270eee55dac3ea8f0957",
      "bytes": 622
    },
    {
      "path": "characters/Song Cheonwoo.md",
      "sha256": "5f92be25e39b4db659d748b05089d6c7e940ac03ae319524746b69e3b2b208e3",
      "bytes": 899
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "f71a6a666c527c7be13ec1de574347ef4f68b7f45ab3bf4304583231e065481b",
      "bytes": 761
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "b90b891de480d6e034d32a7f1d6358749cd0744515a23fcf4ca2151d10c5dc62",
      "bytes": 178011
    }
  ],
  "estimated_tokens": 11794
}
-->

# Durable State Update — Chapter 576

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 576. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 576. Profile updates may replace only one
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
  "chapter": 576,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 576,
    "continuity_sources": [576],
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
    "The Kraken is dead, and Taekyung's poison and paralysis have been cured by the Myriad-Poison Ring.",
    "Taekyung still does not know who empowered and released the Kraken or engineered the Monster Wave.",
    "Busan remains in a large-scale rescue and cleanup operation while monster battles continue throughout the city.",
    "Choi Minwoo regards Jin Taekyung's family and their shared meals as home and family.",
    "President Baek Hanseong seeks to align Jin Taekyung and Choi Minwoo against Ares Guild while pursuing greater political power.",
    "Song Cheonwoo has called Choi Minwoo with an urgent, unexplained matter."
  ],
  "continuity_sources": [
    575
  ],
  "open_questions": [
    "Who empowered and released the Kraken, and did that person engineer the Monster Wave?",
    "What urgent matter does Song Cheonwoo need to discuss with Choi Minwoo?",
    "What further consequences will follow from the Busan Monster Wave?",
    "When and how will Choi Minwoo reunite with Cheon Taemin?"
  ],
  "safe_through": 575,
  "temporary_decisions": [
    "Use King of the Black Sea Kraken for 검은 바다의 왕 크라켄.",
    "Use Monster Wave and extra-large named monster for the established disaster terminology.",
    "Use tteokguk, sujeonggwa, and kimchi stew for the Korean dishes.",
    "Retain System labels Myriad-Poison Ring, Poisoned, and Paralyzed."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 최민우    | **Choi Minwoo**   |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 장비               | **Equipment**                  |
| 매력               | **Charm**                      |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 청해     | **Qinghai**            |
| 천우 | **Cheonwoo** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 송천우 | **Song Cheonwoo** | Ares Guild Director, former third-ranked Korean Hunter, and longtime European regional branch director. |
| 평화 | **Peace Guild** | Guild name. |
| 대한민국 | **Korea** | Country reference. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 강원도 | **Gangwon Province** | Province named in Taekyung’s joke about the Minotaur’s next life. |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 청와대 | **Blue House** | Presidential office mentioned in an online comment about proposed legislation. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 도련님 | **Young Master** | Address used for Team Leader Choi by Butler Kim. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 광안 | **Guang'an** | Sichuan location where the party boards Mu Song's ship. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 부산 | **Busan** | City where the Haeundae Gate crisis occurs. |
| 해운대 | **Haeundae** | Busan district containing Siren's Black River and its beach. |
| 크라켄 | **Kraken** | Sea monster leading the Monster Wave; newly identified in this chapter. |
| 머맨 | **Merman** | Sea monster species serving under the Kraken. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 사장님 | visitor_to_restaurant_owner | Boss | polite but sarcastic | Maintains a superficially respectful address while baiting the owner during the confrontation. |
| 사장님 | 진태경 | restaurant_owner_to_employee_son | you / you little punk | condescending-aggressive | Uses hostile informal forms while trying to intimidate Taekyung. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 석고준 | 최민우 | Ares security leader to rival Guild Master | Team Leader Choi Minwoo | formal but barbed | Uses 평화 길드 최민우 팀장님 while belittling Choi and blaming the Peace Guild for Taekyung's apparent death. |
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 최민우 | 진태경 | trusted allied team leader to younger allied Hunter | Mr. Jin | formal-polite and concerned | Choi warns Jin about the danger of the operation and affirms his deep trust. |
| 진태경 | 최민우 | younger allied Hunter to allied team leader | Team Leader Choi | polite, familiar, and teasing | Jin jokes with Choi while acknowledging and dismissing his concern. |
| 고준 | 진태경 | Ares Guild combatant confronting the killer of his Master | you | hostile and informal | Go Jun uses 너 while demanding Jin confess to Lee Jungryong's death and threatening retaliation. |
| 진태경 | 고준 | dominant adversary confronting Lee Jungryong's Disciple | you | contemptuous and informal | Jin uses 너 and 놈 while overpowering Go Jun and ordering him to end the conflict with Lee Jungryong. |
| 송천우 | 석고준 | adversary; captor of Song's children | you | shocked and confrontational | Song reacts directly to Go Jun's admission that he took the children. |

## Listed compact profiles

### Cheonwoo.md

# Cheonwoo (천우)

- **Safe through:** Chapter 575
- **Aliases:** None
- **Role:** One of the five current Five Gates of Shanxi scions and a First Rate martial artist present at Honghwa Inn.
- **Personality:** Pampered and contemptuous toward Cheongpung's group as part of the five scions' collective mockery.
- **Voice:** Mocking in the group's exchange; no distinct individual speech is established.
- **Relationships:** Associates with Seongryong, Myeonghwa, Sohye, and Jintae as a group of current Five Gates scions.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 575
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 569
- **Aliases:** Team Leader Seok
- **Role:** Go Jun is Ares Guild's Vice Guild Master, Lee Jungryong's disciple and former Head of Security, and the de facto successor to Lee's Ares legacy who passed the S-rank Hunter qualification assessment with a very high score but lacks Lee's legitimacy.
- **Personality:** Disciplined and controlled under ordinary pressure, fiercely loyal to Lee Jungryong, but consumed by humiliation and rage when Ares Guild's authority is challenged.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Disciple and direct protégé of Lee Jungryong, Go Jun inherited Lee's Ares Guild legacy after his death, regards Jin Taekyung and Choi Minwoo as enemies seeking to take it away, and has seized Song Cheonwoo's children as leverage while calling it protection.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 575
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, can command coordinated raids against powerful monsters, serves as one of the two pavilion masters of the Alliance Leader's direct Fire Dragon Pavilion, leads its first mission to Nanman, and is the Peace Guild's wealthy patron in the modern world.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 575
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Song Cheonwoo.md

# Song Cheonwoo (송천우)

- **Safe through:** Chapter 575
- **Aliases:** Director Song
- **Role:** Ares Guild Director and former A-rank Hunter who reached third place among Korean rankers, briefly headed the Hunter training center, and led Ares Guild's European regional branch for twenty years; he now leads an internal faction capable of threatening Go Jun.
- **Personality:** Highly ambitious, honor-obsessed, politically calculating, and determined to use his final opportunity to reclaim influence before retirement.
- **Voice:** Not established.
- **Relationships:** Song Cheonwoo followed Cheon Taemin since before Team Leader Choi was born, was Lee Jungryong's former friend and rival, was exiled to Europe after Lee's victory, is aligned with Choi against Go Jun, and has had his children seized by Go Jun as leverage.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 575
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Cheon Taemin's only living blood relative and is positioning himself to take control of the Ares Guild after Lee Jungryong's death.
- **Personality:** Strategic, candid, controlled, and possessive of the power and influence he intends to inherit.
- **Voice:** Dry, formal, and direct, with calm candor and carefully chosen metaphors.
- **Relationships:** Maternal grandson and only living blood relative of Cheon Taemin; was kept out of public knowledge by Lee Jungryong, is closely integrated with Jin Taekyung's family, and seeks to acquire the Ares Guild intact.

## Korean source

```text
＃576화



달칵.

짧은 통화가 끝났다. 스마트폰에서 흘러나오던 신호음은 멈췄지만, 귓가로 올라간 손은 쉽게 내려가지 않았다.

최민우는 갈등 어린 눈빛으로 청와대 관저 앞에 펼쳐진 녹지원(綠地園)을 가로질렀다.

처음과 달리 느려진 발걸음은 머릿속을 가득 메운 어떤 생각 때문이었다.

‘송천우가 나를 만나고자 한다. 그것도 지금 당장.’

송천우. 아레스 길드라는 철옹성으로 자신을 들여보내 줄 트로이의 목마.

그의 연락을 기다린 것은 사실이지만, 하필 오늘. 그것도 당장 만나자고 할 줄은 몰랐다.

최민우는 짧았던 통화 내용을 떠올리며 내심 중얼거렸다.

‘어떻게 해야 할까.’

그때, 최민우의 발걸음이 우뚝 멈췄다.

어느덧 그의 앞에는 두 갈래 길이 펼쳐져 있었다. 마치 마음에 생겨난 또 하나의 갈림길처럼.

‘부산. 그리고 송천우.’

시간이 없다. 선택해야 한다. 깊게 가라앉은 눈빛으로 두 갈래 길을 응시하던 최민우는 마침내 발걸음을 뗐다.

사박, 추위에 얼어붙은 잔디가 구두 굽 아래에서 바스라졌다. 비록 두 갈래로 나뉘었지만 결국 모든 길은 출구로 통했다.

청와대 경호실과 붙어 있는 정문 밖에는 이미 낯익은 얼굴이 그를 기다리고 있었다.

“도련님.”

김 집사를 향해 눈인사를 건넨 최민우는 정문을 나섰다.

길가에는 잘 빠진 리무진 한 대와 검은색 SUV 다섯 대. 그리고 이십여 명의 헌터가 기다리고 있었다.

이제 상당한 규모를 자랑하는 평화 길드 내에서도 정예라 불리기에 손색이 없는 실력자들.

이미 착용하고 있는 갖가지 장비는 만반의 전투태세를 갖추었다는 증거다.

이어 들려온 김 집사의 한 마디는 짐작을 확신으로 바꿔주었다.

“모셔 가기 위해 대기 중이었습니다.”

“미안합니다. 자리가 자리인지라 미처 확인하지 못했군요. 그보다 진태경 씨가 네임드 몬스터를 처치했다고 들었는데, 현재 상황은?”

“말씀하신 대로 이번 웨이브로 등장한 네임드 몬스터인 크라켄은 제거되었고, 약 일천 개체가 넘는 머맨(Merman)이 해운대와 광안리로 퍼져 나간 상황입니다.”

김 집사의 대답을 들은 최민우가 낮게 뇌까렸다.

“피해가 극심하겠군요.”

비록 서울만큼은 아니지만, 부산은 대한민국 제2의 도시라는 이름에 걸맞게 오백만에 달하는 인구를 보유한 대도시.

최근 마력 상승에 힘입어 더욱 강해진 몬스터가 그런 곳에 천 마리나 등장했다는 것은 말 그대로 재앙이다.

하지만 김 집사는 침착하게 고개를 저었다.

“기뻐해야 할 일은 아니지만…… 다행히 사상자의 숫자는 예상했던 수치보다 극히 적습니다.”

“진태경 씨가 크라켄을 처치했다고 해도, 일천이나 되는 머맨을 모두 막을 수는 없을 텐데요.”

“스켈, 아니. 스톤 킹이 있었습니다.”

“아.”

언제나 오만하고 자신만만한 표정을 짓는 금발 외국인의 얼굴이 눈앞을 스친다. 최민우는 작은 탄성과 함께 고개를 끄덕였다.

‘그가 있다면 가능하지.’

몬스터와 미국인 사이에서 정체성 혼란을 겪고 있는 언데드 몬스터의 존재는 극소수에게만 허락된 비밀.

그리고 최민우는 그가 결코 S급 헌터에 뒤떨어지지 않는 강자라는 사실 역시 알고 있었다.

“예. 다행히 그 두 분의 활약 덕분에 피해 규모는 그리 크지 않습니다.”

천운이라고 할 수밖에 없다. 진태경과 스켈레톤 킹은 일인군단(一人群團)이라 부르기에 부족함이 없는 강자들이니까.

게다가 지닌 바 능력에 비해 여러 가지 제약이 있는 스켈레톤 킹과 달리, 진태경은 대한민국. 아니 전 세계에서도 최고로 꼽히는 실력자다.

‘……한 사람을 제외하고는, 말이지.’

내심 중얼거린 최민우가 입을 열었다.

“그보다 우리 평화 길드는?”

“약 5분 전, 긴급 구조팀 및 준비되어 있던 세 개 팀을 부산으로 파견했습니다. 부산에 위치한 길드와 휘하 헌터들은 물론, 외부 지원군도 전력을 다해 피해 확산을 막는 중입니다.”

국내에 존재하는 게이트와 각 지방의 길드 및 헌터 숫자를 줄줄이 꿰고 있는 최민우다.

몇 번 눈동자를 깜빡인 것으로 계산을 끝마친 그가 불쑥 입을 열었다.

“적어도 두 시간 안에 진압 완료. 맞습니까?”

“그렇습니다. 물론 진압 후에도 피해자 구출 및 시간이 많이 소요되겠지만…….”

“그럼 현재 상황으로서는 진태경 씨나 스톤 킹의 호출은 무리겠군요.”

“실례지만 도련님, 호출이라니 그게 무슨.”

“아닙니다. 출발합시다.”

그러나 나직하게 끊어 내는 말과 달리, 리무진으로 걸음을 옮기는 최민우의 입술은 달싹이고 있었다.

이제는 메시지 마법이 아닌, 전음(傳音)이라 불려야 마땅할 그것이 김 집사의 귓가를 파고든다.

- 그가 만남을 요청해 왔습니다.

“……!”

김 집사의 눈동자가 잘게 흔들렸다. 이름을 말하지 않아도 ‘그’가 누구를 지칭하는 것인지는, 충분히 알아들을 수 있었다.

- 송천우가 말입니까?

- 네.

- 도련님. 위험할지도 모릅니다. 어차피 부산 몬스터 웨이브도 마무리 중이니 차라리 길드 하우스로…….

- 제 외할아버님의 신변에 관한 이야기를 하더군요. 석고준이 함정을 파고 있다는 이야기도 함께.

딱딱하게 굳은 김 집사의 얼굴을 바라본 최민우가 조용히 전음을 이었다.

- 그를 만나야겠습니다. 지금 당장.



* * *



강원도 평창에 위치한 B급 게이트, [예티의 겨울 산맥]은 헌터들에게 있어 그리 매력적인 레이드 장소는 아니었다.

제아무리 뛰어난 신체 능력에 마법 장비가 있다고는 해도, 발이 푹푹 꺼지는 설산(雪山)에서 털북숭이 거인들과 싸우는 건 썩 유쾌한 일이 아니니까.

하지만 그렇다고 해서 모두가 [예티의 겨울 산맥]을 기피하는 것은 아니었다.

최근 잇따라 마력이 상승하는 상황 속에서도 그곳을 찾는 헌터들은 존재했고, 지금 막 리프트를 타고 내려온 일단의 무리 역시 그런 축에 속했다.

“젠장. 갑자기 출입 금지라니.”

“그러게요. 근데 팀장님. 저희 오늘 수당 나와요?”

“……예티보다 더한 놈일세, 이거. 마력 상승 때문에 게이트 진입도 못 했는데 수당은 개뿔이. 양심에 털 났어?”

“에이. 괜히 기대했네. 그런데 위에 있던 사람들은 누구예요? 마스크 쓰고 있던 잘생긴 남자는 좀 눈에 익은 것 같기도 하고.”

“모르지. 그걸 내가 어떻게 알…… 응?”

투덜거리며 내려오는 삼십여 명의 헌터들. 그중 선두에서 걸어가고 있던 팀장이 문득 눈을 동그랗게 떴다.

그의 시선 끝에, 빠르지도 느리지도 않은 걸음으로 길을 올라오는 한 사람이 있었다.

“쯧쯧. 저 양반도 허탕치겠구만.”

척 보아하니 저 사람도 레이드를 위해 온 것이 분명하다. 팀장은 40대쯤으로 보이는 중년인에게 말을 걸었다.

“예티. 레이드?”

불쑥 던진 두 단어에, 순간 멈칫한 중년인이 말없이 고개를 끄덕였다. 작게 혀를 찬 팀장이 말을 이었다.

“사장님 쪽도 오늘 허탕이시네. 올라가지 마세요. 위에 막혔습니다.”

“…….”

“뭐 갑자기 마력 수치가 상승했다나 뭐라나. 여하튼 출입 금지래요. 우리도 지금 그것 때문에 빠꾸 친 거고.”

“…….”

“……저기요? 제 얘기 못 들으셨어요?”

이상함을 느낀 팀장이 눈살을 찌푸린 그때, 한마디 대꾸도 없이 이야기만 듣고 있던 중년인이 그들을 슥 지나쳤다.

저벅. 저벅.

멀어져 가는 중년인의 모습에, 팀장이 중얼거렸다.

“뭐야, 저 인간?”

하지만 팀장의 호의는 중년인에게 있어 쓸데없는 참견에 불과했다.

덜컹.

작은 흔들림과 함께 리프트를 타고 올라간 그는 자신을 기다리고 있던 수십 쌍의 시선을 발견할 수 있었다.

그중 상당한 수준으로 보이는 헌터가 불청객을 막아섰다.

“죄송하지만, 마력 수치 상승으로 인하여 게이트에 진입할 수 없…….”

“제 손님입니다.”

순간 들려온 나직한 목소리에, 벽처럼 서 있던 이십여 명의 헌터들이 좌우로 길을 텄다.

그리고 그들이 만들어 낸 길의 끝에는 두 사람이 있었다.

“늦으셨군요.”

최민우의 고저 없는 목소리에 환영 마법으로 모습을 바꾼 중년인, 송천우는 꾹 다물고 있던 입술을 뗐다.

“조심해야 했으니까. 그리고 이 장소도 민우 네가 정한 것이 아니냐.”

“먼저 게이트에서 만나자고 한 사람은 제가 아닙니다. 그렇다면 장소 정도는 제가 정해도 상관없겠죠.”

“도청이나 혹시 모를 감시를 피하기 위해서는 어쩔 수 없었다. 게이트 안으로 들어가면 모두 무용지물이니.”

“그럼 문제없겠군요. 이 게이트는 평화 길드 소유입니다. 서로 조심하기에 적격인 곳이죠.”

“……서로? 날 의심한다는 뜻이냐?”

송천우의 물음에 대답한 것은 최민우가 아닌, 그 뒤에 조용히 서 있던 김 집사였다.

“그럼 도련님이 도대체 어떤 이유로 당신을 믿어야 합니까?”

“이보게. 화종이.”

“함부로 제 이름을 부르지 마십시오. 우리 관계는 이미 오래전에 끝났습니다.”

“……!”

빙하처럼 차가운 눈빛에 송천우의 눈꺼풀이 파르르 떨렸다.

한때는 호형호제하던 시절도 있었지만, 충성과 야망이라는 갈림길에서 헤어진 그들이다.

두 사람 사이에 싸늘한 냉기가 내려앉은 그때, 나직한 목소리가 울려 퍼졌다.

“그보다 먼저 나눠야 할 이야기가 있는 것으로 압니다만.”

부드럽지만 핵심을 찌르는 한 마디.

동시에 물러난 두 사람을 번갈아 바라본 최민우가 돌아섰다. 마력장이 일렁이는 게이트 입구가 그곳에 있었다.

“두 분은 저와 함께 게이트 안으로. 다른 길드원들은 혹시 모를 외부의 침입을 차단할 겁니다.”

최민우가 가장 먼저 걸음을 내디뎠고, 김 집사와 송천우가 뒤를 따랐다.

쏴아아악.

서늘하고 끈적한 마력이 전신을 감싼다. 다시 눈을 떴을 때, 세 사람의 눈앞에는 온통 새하얗게 물든 세상이 펼쳐져 있었다.

예티의 겨울 산맥.

사방을 가득 채운 눈더미, 가파른 경사를 지닌 그곳 어디에선가 몬스터의 괴성이 울려 퍼졌다.

- 콰우우우우!

그러나 세 사람은 혹한의 추위와 소름 끼치는 괴성에도 무덤덤했다.

한낱 예티에게 겁을 먹기에는 그들의 수준이 너무 높았고, 그보다 앞서 이곳을 찾은 이유는 레이드가 아닌 밀담(密談)을 나누기 위해서였으니까.

“이제 말씀하십시오. 제 외할아버님의 신변에 대해서. 그리고 석고준이 준비하고 있다는 함정에 관한 정보를.”

단도직입적인 최민우의 말에 송천우가 쓴웃음을 지었다.

“비록 오래 지켜보지는 못했지만…… 여전하구나, 그 성격은.”

“본론만 간단히. 그리 어려운 부탁은 아니라고 생각합니다만.”

송천우는 얕은 숨을 내쉬었다. 바람을 뚫고 피어오르는 새하얀 입김 사이, 부쩍 늙은 목소리가 섞여들었다.

“잠시 함께 걷지 않겠느냐? 단둘이 이야기하고 싶다.”

김 집사는 미간을 좁혔고, 최민우는 덤덤하게 대답했다.

“굳이 그럴 필요까지 있겠습니까.”

“날 의심하는 모양이군.”

“신뢰할 이유도 없지요.”

“이 게이트는 나도, 아레스도 아닌 평화 길드의 소유다. 네가 직접 정한 장소인데 어떻게 함정이 있겠느냐?”

“…….”

“유일한 협력자를 상대로 수작을 부릴 만큼 멍청하지는 않다.”

설산 어딘가를 응시하던 최민우가 문득 고개를 돌렸다.

한 치의 흔들림조차 없는 송천우의 눈동자를 물끄러미 들여다보던 그가 나직하게 입을 열었다.

“그러시죠.”

“도련님.”

“걱정하지 마십시오. 멀리 가지 않을 테니.”

“……그럼 뒤에서 거리를 두고 따르겠습니다.”

고개를 끄덕인 송천우가 허리춤에 찬 무기를 천천히 뽑아 들었다.

“그것까지 막을 수는 없겠지. 마음대로 하게.”

“당신……!”

“오해하지는 말고.”

푹.

김 집사가 우려했던 일은 벌어지지 않았다.

보란 듯이 자신의 무기를 눈 깊숙이 박아넣은 송천우의 모습에, 최민우가 먼저 걸음을 내디뎠다.

서벅. 서벅.

나란히 걷는 두 사람의 발걸음을 따라 눈이 바스라졌다.

그렇게 몇 걸음이나 걸었을까, 굳게 닫혀 있던 송천우의 입술이 달싹였다.

“아레스 길드 본사에는 극소수만이 출입할 수 있는 비밀 구역이 있다.”

“A구역을 말씀하시는 겁니까?”

“……!”

예상치 못한 되물음에 송천우의 눈이 크게 뜨였다.

최민우가 침착한 목소리로 말을 이었다.

“비밀 구역의 존재와 명칭 정도는 알고 있었습니다. 그 이상은 무리였지만 말입니다.”

“……수완이 대단하군. 어떻게 알았지?”

“상상하시는 것 이상으로 많은 공을 들였지요. 그리고 지금 제게 필요한 건 칭찬이 아니라 더 세부적인 정보입니다. 그것이 제 외할아버님의 신변과 어떤 연관이 있습니까?”

“그곳에 그분이 계시니까.”

사박.

그분. 누군가를 지칭하는 두 글자에, 막힘없이 나아가던 발걸음이 우뚝 멈췄다.

잠시 침묵하던 최민우가 재차 걸음을 뗐다.

“확실한 정보는 아니겠군요.”

“왜 그렇게 생각하지?”

“지사장님께서는 이미 오래전에 아레스 길드의 중심에서 밀려나신 분이니까요.”

“……아프군. 하지만 네 말이 사실이다. 정확한 정보는 아니지.”

“외할아버님께서 굳이 그곳에 계시는 이유 또한 찾지 못하겠습니다. 아니, 이해할 수 없습니다.”

“이유라…….”

작게 한숨을 내쉰 송천우가 말을 이었다.

“이해할 수 없을 것이다. 너를 포함한 모두는 그분께 무슨 일이 벌어졌는지 모르고 있으니.”

“그게 무슨…….”

의문 어린 표정으로 되묻던 최민우는, 다음 순간 들려온 한마디에 우뚝 굳었다.

“이십 년도 더 지난 일이다. 그분께서 의식을 잃은 것은.”

“……!”
```

## Final English reading copy

```markdown
# Chapter 576

*Click.*

The short call ended. The signal ringing from the smartphone stopped, but the hand Choi Minwoo had raised to his ear did not come down easily.

With a conflicted look in his eyes, Choi Minwoo crossed the Green Garden spread out before the Blue House residence.

Unlike before, his steps had slowed because of a certain thought filling his mind.

*Song Cheonwoo wants to meet me. And he wants to meet right now.*

Song Cheonwoo.

The Trojan horse who would let him enter the impregnable fortress known as the Ares Guild.

It was true that he had been waiting for Song's contact, but he had not expected it to come today—or for Song to demand a meeting immediately.

Choi Minwoo recalled the brief conversation and muttered inwardly.

*What should I do?*

Then Choi Minwoo's footsteps stopped dead.

Two paths had opened before him. It was as though another fork had appeared in his heart.

*Busan. And Song Cheonwoo.*

There was no time. He had to choose.

Choi Minwoo stared at the two paths with deeply sunken eyes. At last, he began walking.

*Crunch.*

The frozen grass crumbled beneath the heels of his dress shoes. Though the path had split in two, every road ultimately led to the exit.

Outside the main gate, beside the Blue House security office, a familiar face was already waiting for him.

“Young Master.”

Choi Minwoo greeted Butler Kim with a nod before stepping through the gate.

A sleek limousine, five black SUVs, and around twenty Hunters were waiting by the roadside.

They were all skilled enough to be called the elite of the Peace Guild, which now boasted considerable strength.

The various pieces of Equipment they already wore were proof that they were fully prepared for battle.

Butler Kim's next words turned Choi Minwoo's suspicion into certainty.

“We were waiting to escort you.”

“I’m sorry. Given where I was, I failed to check in time. More importantly, I heard that Mr. Jin Taekyung defeated a named monster. What is the current situation?”

“As you said, the named monster that appeared during this wave, the Kraken, has been eliminated. However, over a thousand Mermen have spread throughout Haeundae and Gwangalli.”

Choi Minwoo muttered in a low voice after hearing Butler Kim's answer.

“The damage must be severe.”

Busan might not have been as large as Seoul, but it was still a major city with a population approaching five million, worthy of being called Korea's second-largest city.

The appearance of a thousand monsters—monsters made even stronger by the recent rise in magic power—in such a place was nothing short of a disaster.

But Butler Kim calmly shook his head.

“It is not something we should celebrate, but fortunately, the number of casualties is far lower than expected.”

“Even if Mr. Jin Taekyung defeated the Kraken, he could not have stopped all one thousand Mermen.”

“There was Skel—no. The Stone King was there.”

“Ah.”

The face of the blond foreigner who always wore an arrogant, self-assured expression flashed before Choi Minwoo's eyes. He gave a small exclamation and nodded.

*If he was there, it was possible.*

The existence of the undead monster suffering an identity crisis between monster and American was a secret known only to a very small number of people.

Choi Minwoo also knew that the Stone King was a powerful being who was in no way inferior to an S-rank Hunter.

“Yes. Fortunately, thanks to the efforts of those two, the damage is not particularly severe.”

It could only be called good fortune.

Jin Taekyung and the Skeleton King were both powerful enough to be called one-man armies.

And unlike the Skeleton King, who was subject to various restrictions despite his abilities, Jin Taekyung was one of the strongest people in Korea.

No—in the entire world.

*Except for one person…*

Choi Minwoo muttered inwardly before speaking.

“What about our Peace Guild?”

“Approximately five minutes ago, we dispatched an emergency rescue team and three prepared teams to Busan. The Guilds and Hunters based in Busan, as well as outside reinforcements, are doing everything they can to prevent the damage from spreading.”

Choi Minwoo knew the number of Gates in Korea, along with the number of Guilds and Hunters in every region, by heart.

He finished his calculations after blinking several times and asked abruptly,

“Containment will be complete within two hours at the latest. Correct?”

“That is correct. Of course, rescuing the victims after containment will also take considerable time, but…”

“Then, given the current situation, calling in Mr. Jin Taekyung or the Stone King would be difficult.”

“Forgive me, Young Master, but what do you mean by calling them?”

“It is nothing. Let us depart.”

Despite his quiet, decisive reply, Choi Minwoo's lips moved as he walked toward the limousine.

What now deserved to be called Sound Transmission rather than message magic pierced Butler Kim's ear.

—He has requested a meeting.

“……!”

Butler Kim's eyes trembled slightly. Even without a name, there was no mistaking whom *he* referred to.

—Song Cheonwoo?

—Yes.

—Young Master. It may be dangerous. The Busan Monster Wave is already nearing its end. It would be safer to go to the Guild House instead—

—He spoke about my maternal grandfather's safety. He also said that Go Jun was laying a trap.

Choi Minwoo looked at Butler Kim's rigid face and continued the Sound Transmission quietly.

—I have to meet him. Right now.

* * *

The B-rank Gate in Pyeongchang, Gangwon Province, known as *Yeti's Winter Range* was not a particularly appealing raid site for Hunters.

No matter how outstanding their physical abilities were or how much Magic Equipment they possessed, fighting furry giants on a snow-covered mountain where their feet sank deep with every step was hardly pleasant.

That did not mean everyone avoided *Yeti's Winter Range*, however.

Even amid the recent, successive rises in magic power, some Hunters still visited the Gate. The group that had just ridden the lift down belonged to that category.

“Damn it. Why did they suddenly prohibit entry?”

“I know. But, Team Leader, are we getting paid today?”

“……You’re worse than a yeti. We couldn’t even enter the Gate because of the rise in magic power, and you’re asking about pay? Don’t you have any conscience?”

“Aw, I got my hopes up for nothing. By the way, who were those people up there? The handsome guy wearing the mask looked kind of familiar.”

“I don’t know. How would I know—huh?”

The thirty-odd Hunters were coming down while grumbling. The Team Leader walking at the front suddenly opened his eyes wide.

At the end of his gaze, a man was walking up the path at neither a fast nor slow pace.

“Tsk, tsk. Looks like he’s going to strike out too.”

It was obvious at a glance that the man had come for a raid. The Team Leader spoke to the middle-aged man who looked to be in his forties.

“Yeti raid?”

The middle-aged man stopped for a moment at the two words thrown abruptly at him, then nodded without a word.

The Team Leader clicked his tongue and continued.

“Looks like you’re striking out too, Boss. Don’t go up. It’s blocked.”

“……”

“They say the magic power reading suddenly went up or something. Anyway, entry’s prohibited. That’s why we got turned back too.”

“……”

“……Sir? Did you hear me?”

The Team Leader frowned when he sensed something strange. Without answering a single word, the middle-aged man who had merely listened to him walked past the group.

*Step. Step.*

As the middle-aged man's figure receded, the Team Leader muttered,

“What the hell was that guy?”

To the middle-aged man, however, the Team Leader's goodwill was nothing more than needless meddling.

*Clatter.*

The man rode the lift up with a slight jolt and found dozens of pairs of eyes waiting for him.

A Hunter who appeared to be quite powerful stepped forward to block the unwelcome visitor.

“Sorry, but due to the rise in the magic power reading, you cannot enter the Gate—”

“He’s my guest.”

At the quiet voice that interrupted him, the twenty-odd Hunters standing like a wall split apart to make way.

At the end of the path they created stood two people.

“You’re late.”

At Choi Minwoo's flat voice, the middle-aged man whose appearance had been changed by an illusion spell—Song Cheonwoo—finally parted his tightly closed lips.

“I had to be careful. And wasn’t this place chosen by you, Minwoo?”

“I was not the one who asked to meet at a Gate first. In that case, I see no problem with choosing the location myself.”

“We had no choice if we wanted to avoid wiretapping and possible surveillance. Once we enter the Gate, all of that becomes useless.”

“Then there should be no problem. This Gate belongs to the Peace Guild. It is an ideal place for both of us to be cautious.”

“……Both of us? Are you saying you suspect me?”

Butler Kim, who had been standing quietly behind Choi Minwoo, answered instead.

“Then why should the Young Master trust you?”

“Come now, Hwa-jong.”

“Do not presume to call me by my name. Our relationship ended long ago.”

“……!”

At Butler Kim's eyes, cold as a glacier, Song Cheonwoo's eyelids trembled.

There had been a time when the two men had treated each other like brothers. But they had parted ways at the fork between loyalty and ambition.

As an icy chill settled between them, a quiet voice rang out.

“More importantly, I believe there is something we need to discuss first.”

With that gentle but incisive remark, Choi Minwoo looked back and forth between the two men, who had both taken a step away from each other.

The Gate entrance, shimmering with a field of magic power, stood behind him.

“You two will enter the Gate with me. The other Guild members will prevent any possible intrusion from outside.”

Choi Minwoo took the first step. Butler Kim and Song Cheonwoo followed him.

*Whoooooosh.*

Cold, sticky magic power wrapped around their entire bodies. When they opened their eyes again, a world drenched in white stretched out before them.

*Yeti's Winter Range.*

Snowdrifts filled every direction. Somewhere amid the steep slopes, a monster's roar rang out.

—Kraaaaaaaar!

Yet the three men remained unmoved by the bitter cold and chilling roar.

They were far too powerful to be frightened by a mere yeti. More importantly, they had come here not for a raid, but to have a private conversation.

“Speak now. About my maternal grandfather's safety. And about the trap Go Jun is preparing.”

At Choi Minwoo's direct demand, Song Cheonwoo gave a bitter smile.

“Although I have not watched you for long… your personality has not changed.”

“Get to the point. I do not think that is a difficult request.”

Song Cheonwoo let out a shallow breath. His white breath rose through the wind, mingling with his suddenly aged voice.

“Would you walk with me for a while? I want to speak with you alone.”

Butler Kim furrowed his brow, while Choi Minwoo answered calmly.

“Is that really necessary?”

“You seem to suspect me.”

“I have no reason to trust you, either.”

“This Gate belongs neither to me nor to Ares, but to the Peace Guild. You chose it yourself. How could there be a trap?”

“……”

“I am not foolish enough to scheme against my only collaborator.”

Choi Minwoo had been staring at some distant point in the snowy mountains when he suddenly turned his head.

He gazed silently into Song Cheonwoo's eyes, which showed not the slightest hint of wavering, then spoke in a low voice.

“Very well.”

“Young Master.”

“Do not worry. I will not go far.”

“……Then I will follow at a distance from behind.”

Song Cheonwoo nodded and slowly drew the weapon at his waist.

“I suppose you cannot stop even that. Do as you please.”

“You……!”

“Do not misunderstand.”

*Thud.*

What Butler Kim had feared did not happen.

Song Cheonwoo deliberately drove his weapon deep into the snow. Choi Minwoo took the first step.

*Crunch. Crunch.*

The snow crumbled beneath the footsteps of the two men walking side by side.

How many steps had they taken?

Song Cheonwoo's tightly closed lips finally moved.

“There is a secret area inside the Ares Guild headquarters that only a very small number of people can enter.”

“Are you referring to Area A?”

“……!”

Song Cheonwoo's eyes widened at the unexpected question.

Choi Minwoo continued in a calm voice.

“I knew about the existence and name of the secret area. Anything beyond that was impossible, however.”

“……Your abilities are impressive. How did you find out?”

“I put in more effort than you can imagine. And what I need from you now is not praise, but more detailed information. What connection does it have to my maternal grandfather's safety?”

“Because that person is there.”

*Crunch.*

At the two words referring to someone, the footsteps that had been moving forward without hesitation stopped dead.

After a brief silence, Choi Minwoo began walking again.

“That information is not certain.”

“Why do you think that?”

“You were pushed out of the Ares Guild's inner circle long ago, Director Song.”

“……That hurts. But what you say is true. It is not certain information.”

“I have also been unable to find any reason for my maternal grandfather to be there. No—I cannot understand it.”

“A reason……”

Song Cheonwoo let out a small sigh before continuing.

“You would not be able to understand. No one, including you, knows what happened to him.”

“What does that—”

Choi Minwoo turned to him with a questioning expression. Then, at the next words, he froze.

“It happened more than twenty years ago. That person lost consciousness.” 

“……!”
```
