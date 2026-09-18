<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0408.txt",
      "sha256": "59074fef93bcbcf41b97590518138d2b3440d1795666d59071fb325860b61fae",
      "bytes": 15187
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "4a3cb70713077c3327c19116ce35eab7c0b92b144de29a00542ae5e19c27cc3c",
      "bytes": 2009
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a7d57746878eedf44546a5ff45ecb57ce09c9013a7f31a6553b9f5b400786954",
      "bytes": 137079
    },
    {
      "path": "characters/Heo Jun.md",
      "sha256": "381915adb7960a6a1337e20ebf1f9154d37678a13891b33dd4a457be7f4a7e34",
      "bytes": 716
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "7b5762f4d18424c6a146f7193c4fe06616effd61f48073cacfa53648a6e60309",
      "bytes": 667
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "6f4347e094822ccb1031f33ee77a7846ff74ecf26cf2202071150dae5395077a",
      "bytes": 1212
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "491b1c69b168ca81acefed77c86d7b1721faa41df8b677d86492f01280bdc1aa",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "54f618daf17f6a2156ac9f3848836c3c04be759a90bd643b8d0b708c7b8b82b6",
      "bytes": 1163
    },
    {
      "path": "characters/Wei Fenghu.md",
      "sha256": "4d7e1e1fe17f08c908e0a581df044137646bf20800ba52db1fbfa603fd52b1f6",
      "bytes": 560
    },
    {
      "path": "characters/Wu Heixing.md",
      "sha256": "f234fb8aa8cb213edf39ed1370f938e4a223b2cb2b66420ee38bf956d1c9c7a1",
      "bytes": 735
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "20756313769990dd62f395528ba5e0e496d7f7ac35c1999054a04cc95fc16279",
      "bytes": 121531
    }
  ],
  "estimated_tokens": 11550
}
-->

# Durable State Update — Chapter 408

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 408. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 408. Profile updates may replace only one
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
  "chapter": 408,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 408,
    "continuity_sources": [408],
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
    "The five allied fronts have halted two hundred kilometers from Suining City after forcing the Arch Lich's territory back to the city.",
    "Daniel Inoue is the sole survivor of the intelligence team sent into Suining City and reports a monster army of roughly thirty thousand by direct observation, with the actual number possibly twice that or more.",
    "Most of the Arch Lich's remaining monsters are expected to be mid- or low-level, while the allied forces also have more troops than previously expected.",
    "The coalition's leaders are preparing for a final battle against the Arch Lich and its preserved monster army.",
    "Jin Taekyung has proposed gathering the strongest fighters into a suicide squad to eliminate the Arch Lich.",
    "The undead army is expected to collapse if the Arch Lich is destroyed.",
    "Magic Johnson has summoned Jin Taekyung and Team Leader Choi to the coalition's strategic meeting.",
    "Lee Jungryong continues to act as Jin Taekyung's adversary but redirects their confrontation toward planning for the final battle."
  ],
  "continuity_sources": [
    407
  ],
  "open_questions": [
    "Who is Lei Fei's unidentified lord, what is the lord's origin, and how does the lord relate to the Arch Lich's objective?",
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "Why has the Arch Lich withheld itself from the war, and what is it preparing now?",
    "What kind of being was the Skeleton Warlord before it became an undead commander?",
    "What specific situation will allow Jin to draw out Hero's Power more strongly?"
  ],
  "safe_through": 407,
  "temporary_decisions": [
    "Render 영웅의 혼 as Hero's Soul and 영웅의 힘 as Hero's Power.",
    "Render 기동전 as mobile warfare.",
    "Render 쑤이닝시 as Suining City.",
    "Render 결사대 as suicide squad.",
    "Render 머리를 치다 as take out the head in the context of killing the Arch Lich."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 허준     | **Heo Jun**        |
| 이정룡    | **Lee Jungryong** |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 부길드장    | **Vice Guild Master** |
| 마법사     | **mage**              |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 웨이펑후 | **Wei Fenghu** | Minister of National Defense under China's Central Military Commission. |
| 우헤이싱 | **Wu Heixing** | Chinese S-rank Hunter who provokes Jin and nearly draws his sword. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 소원 | **Sowon** | Name called out by Im Kkeokjeong during the Wyvern attack. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 영국 | **United Kingdom** | Country associated with BCC. |
| 전광석화 | **Quick Attack** | Warlordmon’s rapid-movement command; used as a Pokémon-style gag. |
| 전광 | **Quick Attack** | Shortened form of Warlordmon’s rapid-movement command. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 국방부 | **Ministry of National Defense** | Government ministry referenced in Taekyung's comparison about the steady passage of time. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 마법사 | 이정룡 | Ares Guild mage subordinate to Vice Guild Master | Vice Guild Master | formal-deferential | Lee's five direct A-rank mages greet him and receive instructions for concealing the battle. |
| 웨이펑후 | 진태경 | senior_military_official_to_ally | Mr. Jin | formal-polite | Wei Fenghu addresses Jin while inviting him to walk to the operations headquarters. |
| 진태경 | 골골 | captor_to_subordinate_undead | Bones | mocking-casual | Jin uses the mocking nickname while treating the Skeleton Warlord like a pet. |
| 진태경 | 웨이펑후 | Foreign Hunter to senior military official | General, Commander, or Supreme Leader | Polite but flustered | Jin jokingly cycles through grand titles while trying to interrupt Wei's emotional request. |
| 우헤이싱 | 진태경 | hostile S-rank Hunter to foreign Hunter and provocation target | peninsula bangzi | insulting and confrontational | Wu repeatedly addresses Jin with anti-Korean slurs. |
| 우헤이싱 | 이정룡 | younger S-rank Hunter to senior Ares Guild authority | Mr. Lee | formal and deferential | Wu addresses Lee respectfully despite his usual hostility toward Koreans. |
| 웨이펑후 | 이정룡 | senior military official to senior foreign S-rank Hunter | Mr. Lee | formal and concerned | Wei asks Lee whether something is wrong. |
| 필릭스 | 이정룡 | British prince to senior S-rank Hunter | Jungryong Lee | formal through a translation device | Felix permits Lee to omit His Highness and gives his own preferred form of address. |
| 진태경 | 필릭스 | Korean S-rank Hunter addressing a British prince | His Highness | mock-formal and sarcastic | Felix demands formal address, and Jin complies by calling him His Highness while continuing to mock him. |
| 진태경 | 우헤이싱 | adversarial S-rank Hunters | you idiot | insulting-casual | Mocks Wu's cowardice and orders him to stop complaining. |

## Listed compact profiles

### Heo Jun.md

# Heo Jun (허준)

- **Safe through:** Chapter 328
- **Aliases:** Uncle Heo, Chief Escort
- **Role:** Former Chief Escort of the Yongbong Escort Bureau and Ju Hwaran's uncle, Heo Jun secretly colluded with Zhongnan for two years before Ju Hwaran exposed his betrayal and killed him with a sword strike.
- **Personality:** Deceitful, greedy, manipulative, and fiercely self-preserving beneath a long-maintained paternal facade.
- **Voice:** Formal, paternal, calm, and quietly reassuring.
- **Relationships:** He is Ju Hwaran's uncle and former Chief Escort, but his two-year betrayal of her and the Yongbong Escort Bureau has shattered their bond.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 394
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 407
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force and crossed the wall into true mastery.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother; Jeok Cheongang is his Master; Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and student; his mother and sister Hayeon are among those he protects.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 407
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 407
- **Aliases:** None
- **Role:** Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who directs Ares Guild operations.
- **Personality:** Outwardly genial, calm, and humorous; calculating, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

### Wei Fenghu.md

# Wei Fenghu (웨이펑후)

- **Safe through:** Chapter 407
- **Aliases:** None
- **Role:** Wei Fenghu is the Minister of National Defense under China's Central Military Commission and a four-star general.
- **Personality:** Courteous, reserved, and authoritative.
- **Voice:** Formal and measured, addressing Jin as Mr. Jin.
- **Relationships:** Wei Fenghu is Lei Fei’s maternal uncle who raised him as his own son; after Lei Fei’s death, he entrusted Lei Fei’s sword to Jin Taekyung.

### Wu Heixing.md

# Wu Heixing (우헤이싱)

- **Safe through:** Chapter 407
- **Aliases:** None
- **Role:** Wu Heixing is a Chinese S-rank Hunter known for frequent media exposure and scandal who secretly practices martial arts, including an internal-energy cultivation technique and fist-and-foot martial arts.
- **Personality:** Arrogant, status-conscious, abusive, and fiercely proud of his power, he responds to humiliation with anger, jealousy, and fear.
- **Voice:** Loud, insulting, entitled, and dependent on national and political status.
- **Relationships:** He is openly hostile toward Jin Taekyung and Faye Chen, and resents Jin receiving Chairman Shao Yang's attention.

## Korean source

```text
＃408화



“결사대.”

진태경의 입에서 그 단어가 흘러나온 순간, 우헤이싱은 치밀어오르는 분노도 잊은 채 소리칠 뻔했다.

‘야, 이 미친 빵즈 새끼야!’

결사대(決死隊).

말 그대로 죽음을 각오하고 달려들겠다는 것 아닌가.

아직 정확한 숫자조차 파악되지 않은 몬스터 군단을 어찌어찌 돌파한다 쳐도, 그 뒤에는 아크 리치라는 진짜 괴물이 기다리고 있다. 상상만으로도 머리털이 쭈뼛 섰다.

‘이건, 이건 미친 짓이야.’

얼마나 많은 사상자가 나오건 우헤이싱에게는 상관없는 일이었다.

어차피 인구수만 10억이 넘는 대국 아닌가. 십만, 백만이 사라진다 한들 한 줌에 불과하다.

오히려 저 빌어먹을 빵즈 놈이 결사대의 선봉이 되어 장렬하게 산화한다면 쌍수를 들고 기뻐해 줄 용의도 있다.

하지만…….

“최정예를 모아 머리를 칩시다.”

저 말은, 그 결사대에 우헤이싱 본인도 포함된다는 뜻이었다. 그리고 그는 위험을 무릅쓸 생각이 눈곱만큼도 없었다.

「그런 말도 안 되는 헛소리 집어치우…….」

참지 못하고 자리에서 벌떡 일어난 우헤이싱이 입을 연 그 순간이었다.

“오, 그것참 좋은 방법이군.”

「……!」

우헤이싱은 말을 잇지 못하고 눈을 부릅떴다.

그가 진태경의 손을 들어 주리라고는 생각하지 못했다.

다른 사람도 아닌 바로 그, 이정룡이.

「지, 지금 뭐라고 하셨습니까?」

“좋은 방법이라고 했네.”

이정룡이 부드럽게 웃으며 말을 이었다.

“이 전투는 속전속결로 끝내야 해. 아크 리치는 지금 이 순간에도 새로운 언데드를 만들어 내고 있을 터, S급 헌터들이 주축이 되어 나아가 놈을 처단한다면 대부분이 언데드로 이루어진 몬스터 군단은 붕괴할 것이고 사상자도 줄어들겠지.”

「이, 이 선생님.」

“자네도 나와 같은 생각일 것 같은데. 여기 자리한 다른 분들처럼 말이야. 그렇지 않나, 우헤이싱 군?”

「다른 사람들이라니, 그 무슨…….」

우헤이싱은 그제야 당황한 얼굴로 주위를 둘러봤다.

웨이펑후를 비롯한 중국 고위 장성들은 물론이고, 파이 첸과 매직 존슨. 필릭스 왕자까지 작게 고개를 끄덕이며 대화를 주고받고 있었다.

「으음. 확실히…….」

「아군의 병력을 증강한다고 한들, 그건 아크 리치도 마찬가지일 테니 시간을 끌수록 전투 규모만 더 키울 뿐입니다.」

「A급 헌터와 그 외 베테랑들을 선별하여 일면에 배치하고, S급 헌터를 선두로 내세워 돌파한다면……?」

「위험도가 높긴 하지만, 그만큼 가능성이 있는 작전이군.」

「아크 리치가 제아무리 강력한 네임드 몬스터라고는 하나, S급 헌터들이 합공을 가한다면 승산은 충분해.」

귓가에 전해져 오는 대화 내용에, 우헤이싱의 얼굴이 새하얗게 질렸다.

‘이것들이 지금 제정신인가?’

이런 미친 작전을 긍정적으로 바라보다니, 단체로 돌아 버린 것이 틀림없다.

믿고 있던 이정룡까지 무슨 이유에서인지 진태경의 손을 들어 준 상황.

죽어도 결사대에 포함되고 싶지 않았던 우헤이싱은 황급히 진태경을 향해 입을 열었다.

「자, 잠깐! S급 헌터들이 모두 빠져나간다면 그만큼 전력에 큰 구멍이 생길 텐데?」

“헉.”

헛숨을 들이킨 진태경이 놀란 눈빛으로 우헤이싱을 바라보았다.

“와, 너도 가끔은 생각이라는 걸 하는구나?”

「…….」

“네 말이 맞아. 확실히 몇 명 정도는 남는 게 좋겠지.”

저 빌어먹을 빵즈 놈.

하지만 지금은 화내고 있을 때가 아니다. 우헤이싱은 울컥 치미는 분노를 참으며 말을 이었다.

「그, 그렇지. 그러니 만일의 사태를 대비하여 내가…….」

진태경이 이어지려는 말을 뚝 잘라 먹으며 매직 존슨을 향해 물었다.

“남아 주셔야 할 것 같은데. 존슨 생각은 어떠세요?”

「음. 나?」

이게 무슨 시츄에이션인가. 우헤이싱은 필사적으로 끼어들었다.

「매, 매직 존슨을? 마법사 한 명 정도는 같이 가는 게 좋지 않을까?」

“당연히 좋지. 좋은데…….”

우헤이싱을 향해 사람 좋게 웃어 보인 진태경이 말을 이었다.

“그럼 후방은 어쩔래?”

「응?」

“아크 리치가 텔레포트로 아군 뒤통수치면 어떡할 거냐고. 네가 막을래?”

「…….」

“아크 리치가 아무리 강력해도 대마법사가 남아서 마법을 방해하면 그런 짓은 벌이지 못하겠지. 그리고 매직 존슨의 광범위 마법이라면 전황을 뒤집을 한 수가 될 수도 있고.”

구구절절 맞는 말이다. 순간 말문이 턱 막힌 우헤이싱의 모습에 진태경이 혀를 찼다.

“마, 생각하고 씨부려. 맨날 인터넷에서 후방 주의 움짤. 뭐 그딴 거나 보지 말고 진짜 전쟁에서의 후방을 생각하라고.”

「……!」

석상처럼 굳어 버린 우헤이싱을 무시한 진태경이 매직 존슨에게 물었다.

“어떻게 생각하세요?”

「네 말이 맞아, 진. 그럼 나 혼자만 남는 건가?」

가만히 상황을 지켜보던 웨이펑후 국방부장이 불쑥 입을 열었다.

「아크 리치는 마지막 전투를 위해 상위 몬스터들을 대거 남겨 두었을 거요. 아군이 보유한 A급 헌터의 숫자보다 훨씬 많지. 최소한 팽팽한 전황을 유지하기 위해서는 S급 헌터 둘이 더 필요하오.」

끝난 것이 아니다. 아직 두 자리나 남았다. 희망을 발견한 우헤이싱이 목을 가다듬었다.

「그럼 어쩔 수 없이 제가 남아야겠…….」

「다른 분들이 양해해 주신다면, 우선 필릭스 왕자를 제외했으면 하오만.」

“예?”

「미안하게도 자세한 사정은 말할 수 없으나, 복잡한 문제가 있소.」

필릭스는 그냥 S급 헌터가 아니라 영국의 상징이나 다름없는 왕족이다. 그것도 어중간한 방계가 아닌 왕위 계승 서열 3위.

이 자리의 모두는 웨이펑후가 말하지 못한 ‘자세한 사정’이 영국과의 외교 문제라는 것을 알았다.

“뭐, 아버지가 영국 국왕인데 그럴 수도 있지. 그럼 왕자님 빠지시고.”

진태경의 말에 필릭스 왕자가 불편한 얼굴로 입을 열었다.

「내 자의가 아니라는 걸 알아줬으면 좋겠군. 다만 태어날 때부터 왕실에 매인 몸인지라 아바마마의 명을 거스를 수는…….」

“괜찮아. 난 신경 안 써. 내가 제시한 작전에 영국 계승 서열 4위가 무슨 일이라도 당하면 걸쩍지근하니까 오히려 좋지.”

「3위다! 그리고 내게 말할 때는 예의를 갖추도록.」

“어, 그래. 동메달 축하하고. 그럼 혹시 적폐의 온상이신 필릭스 왕자 전하께서 인맥빨로 빠지시는 것에 이의 있으신 분?”

자신도 모르게 손을 번쩍 치켜들려던 우헤이싱은, 다음 순간 들려온 파이 첸과 이정룡의 대답에 동작을 멈췄다.

「난 상관없어.」

“동의하네.”

고개를 끄덕인 진태경이 우헤이싱을 지그시 바라봤다.

“넌?”

「나, 나?」

“딱 하나 남은 놈이 그렇게 물어보면 내가 뭐라고 해 줘야 할까. 보라돌이, 뚜비, 뽀. 셋 중에 하나 골라 봐.”

도무지 빠져나갈 구석이 없다. 매직 존슨과 필릭스 왕자는 엄연한 외국인인 데다 합당한 이유가 있었고, 파이 첸과 이정룡마저 동의해 버린 상황이니까.

눈을 질끈 감았다 뜬 우헤이싱이 중얼거렸다.

「……동의.」

“대답 똑바로 해라. 그따위로 대답하면 동의보감인지 뭔지 어떻게 알아 처먹어. 허준이야?”

「동의……한다.」

“오케이.”

그야말로 전광석화와도 같은 속도. 아직 한 자리가 남아 있었지만 우헤이싱은 불길함을 느꼈다.

그리고 그 불길함이 확신으로 변하기까지는 그리 오랜 시간이 걸리지 않았다.

“남은 한 자리는 파이 첸. 당신이 채워 주었으면 싶소만.”

하지만 우헤이싱이 당황한 이유는, 마지막 빠져나갈 구멍을 막아 버린 것이 진태경도 아닌 이정룡이었기 때문이었다.

‘도대체 저 늙은이는 무슨 생각을 하고 있는거지?’

진태경에게 처참하게 짓밟혔던 그 날, 이정룡과 나누었던 대화를 똑똑히 기억하고 있는 우헤이싱으로서는 배신감마저 들 정도였다.

‘분명 힘을 합치자고 제안해 놓고, 이렇게 내 뒤통수를 쳐?’

으득, 이를 가는 우헤이싱을 힐끗 바라본 파이 첸이 술잔을 기울였다.

「글쎄요, 이 선생. 내가 위험을 즐기는 그런 부류는 아니지만, 나 대신 저 애송이를 남기는 게 더 성공 확률이 높지 않겠어요?」

“아니오, 파이 첸. 사상자를 줄이기 위해서는 그대가 남는 것이 더 보탬이 될 거요.”

「이 선생이 저 녀석을 몰라서 그래요. 보고 있으면 없던 애국심까지 생기더라니까?」

“걱정할 것 없소. 내가 있으니.”

담담하지만 확신에 찬 말투. 이정룡이기에, 이정룡이라서 할 수 있는 말이다.

이 자리의 누구도 부정할 수 없는 자신감을 내비친 옛 영웅의 시선이 한 사람에게 닿았다.

“그리고 진태경. 자네도 있지. 그렇지 않나?”

감정을 알 수 없는 깊게 가라앉은 눈빛.

말없이 이정룡의 시선을 마주하던 진태경이 입술을 뗐다.

“우리 부길드장님. 당연한 말을 어렵게 하는 재주가 있으시네.”

“자네 또한 결사대에 참여하겠다는 의미로 알아들어도 되겠지?”

“물론입니다.”

“용맹하군. 영웅적이고. 그런 의미에서 내 자네에게 선봉을 양보하지.”

“좋네요. 저도 이참에 루이 암스트롱처럼 명언 하나 남길 수 있는 겁니까? 이건 한 명의 인간에게는 작은 발걸음이지만, 몬스터들에게는 천마 군림보다. 뭐 그런 식으로.”

“역사서에 실릴 명언 치고는 거친데. 그리고 이름이 틀렸어. 루이 암스트롱이 아니라 닐 암스트롱이야.”

“가방끈이 상당히 기시네요. 그래 봤자 제 휴지끈보다는 못하겠지만.”

종잡을 수 없는 진태경의 대답에 사람들은 머리가 지끈거렸고, 우헤이싱은 절망했다.

불과 한 달 전까지만 해도 수십의 미녀들에게 둘러싸여 호화 선상 파티를 즐기던 그가, 이제는 죽음을 각오한 결사대에 포함된 것이다.

그리고 바로 다음 순간이었다.

- 내가 자네를 배신했다고 생각하나?

「……!」

- 받아들이게. 아무런 위험도 없을 거라 약속하지.

이어 귓가를 파고드는 전음(傳音)에 우헤이싱이 천천히 고개를 들었다.

만면에 부드러운 미소를 띤 이정룡이 그를 바라보며 말을 이어 가고 있었다.

“그는 맡은 바 임무를 잘 해낼 거요. 내 장담하지.”

진태경이 느릿하게 의자 팔걸이를 두드리며 대답했다.

“얼마나 훌륭하게 임무를 해낼지…… 그것참 기대되네요.”



* * *



다소 길었던 회의가 끝났다.

결사대는 S급 헌터를 위시하여 A급 상위 헌터, 그리고 B급의 베테랑들로 구성될 것이고 지휘부는 해당 인원을 선별하느라 눈코 뜰 새 없이 바쁠 것이다.

그리고 회의 내내 침묵을 지키고 있던 스켈레톤 워로드는, 내게 배정된 서부 전선의 텐트로 돌아오자마자 엄숙한 목소리로 선언했다.

- 본 사령관은 이번 싸움에서 빠지겠다.

“응, 조까.”

- 이유라도 물어봐라, 이 간악한 인간아.

“그래, 뭔데?”

- 언데드 군단의 사령관으로서 동족을 상대하는 것이 꺼려지는구나.

나는 어이없는 표정으로 대꾸했다.

“뭔 개소리야. 지금까지 동족들 기운 쪽쪽 빨아 먹으면서 영양 보충한 놈이 누군데.”

- ……앗.

“우리 솔직해지자. 그냥 아크 리치 무서워서 가기 싫다고 하면 내가 욕이라도 하냐?”

- 할 거잖아.

“시벌놈이…… 앗.”

불신이 더더욱 깊어진 스켈레톤 워로드가 말했다.

- 어쨌든 본 사령관은 더 이상 이 전쟁에 관여하고 싶지 않다. 그날의 약속을 지켜다오.

“그날의 약속?”

- 이런 간악한 인간을 보았나! 두 인간을 지켜 주는 대신, 무슨 부탁이든 들어 주겠다 약속하지 않았느냐?!

“아.”

오랜만에 말문이 턱 막히네.

분명 그런 약속을 했었다. 어지간하면 기억 상실증에 걸린 사람처럼 얼렁뚱땅 넘어가겠는데, 이번만큼은 양심상 모른 척할 수가 없었다.

“음. 소원이 뭔데?”

스켈레톤 워로드가 기다렸다는 듯이 외쳤다.

- 내게 자유를 다오!

“자유?”

- 그렇다. 너, 간악한 인간은 지금껏 본 사령관을 모욕하고 학대했다! 그 횟수가 자그마치 408회나 된다!

“……혹시 동물 인권 보호 단체 출신이야?”

- 약속을 이행하라, 본 사령관은 비로소 자유를 찾으리라!

자유라. 이정룡에 관한 생각으로 머릿속이 복잡해서, 이런 소원이라고는 순간 생각하지 못했다.

잠시 고민하던 나는 대답했다.

“그래, 준다. 자유.”

- 오오, 오오오오!

“그럼 잘 가라.”

- 어?

그리고 망설임 없이 인벤토리에서 놈의 해골을 꺼내 텐트 밖으로 던졌다.

수천 명의 헌터들이 바글거리는 그곳에.

딱!

뭔가에 맞는 소리와 함께 텐트 주위가 어수선해진다. 사방에서 고함이 울리고 마법이 작렬하는 굉음이 울려 퍼졌다.

“몬스터! 몬스터의 습격이다!”

“죽여!”

쾅! 콰광!

얼마나 흘렀을까. 5분? 10분?

스슥, 슥. 난데없이 텐트 밑단이 들썩이더니, 검은 광택이 흐르는 두개골 하나가 데굴데굴 굴러와 내 발 앞에서 멈췄다.

“오, 이게 누구야.”

- …….

“자유로운 영혼의 소유자, 스켈레톤 워로드가 여기에는 어쩐 일로?”

- 그, 인간…….

해골의 텅 빈 동공 안에서 붉은 안광이 애처롭게 일렁였다.

언데드 주제에 울먹이고 있다고 생각하면 착각인가. 스켈레톤 워로드가 물기 어린 목소리로 말을 이었다.

- 소원…… 취소해도 될까?

“어이구, 물론이지.”

나는 상담원처럼 경쾌한 어조로 말을 이었다.

“근데 소원권은 교환, 환불 불가능인 거 알지?”

- …….

“이리 와, 골골아.”

폴짝.

스켈레톤 워로드가 내 품 안으로 힘없이 뛰어들었다.
```

## Final English reading copy

```markdown
# Chapter 408

“A suicide squad.”

The moment the words left Jin Taekyung’s mouth, Wu Heixing forgot his rising anger and nearly shouted.

*You crazy bangzi bastard!*

A suicide squad.

Wasn’t that exactly what it meant—to charge in prepared to die?

Even if they somehow broke through the monster army without knowing its exact numbers, the real monster called the Arch Lich was waiting behind it. The mere thought made the hair on Wu Heixing’s head stand on end.

*This… this is insane.*

It didn’t matter to Wu Heixing how many casualties there were.

China was a Great Nation with a population of over a billion, after all. Even if a hundred thousand or a million people disappeared, they would amount to no more than a handful.

In fact, if that damn bangzi became the vanguard of the suicide squad and died a glorious death, Wu Heixing would be more than happy to celebrate with both hands raised.

But…

“Let’s gather our very best and take out the head.”

That meant Wu Heixing himself would be included in the suicide squad. And he had no intention of taking even the slightest risk.

“Cut that ridiculous bullshit—”

Unable to hold back any longer, Wu Heixing shot to his feet and opened his mouth.

“Oh, that’s an excellent idea.”

“……!”

Wu Heixing stared wide-eyed, unable to continue.

He had never imagined that Lee Jungryong would support Jin Taekyung.

Not anyone else, but Lee Jungryong himself.

“W-What did you just say?”

“I said it was an excellent idea.”

Lee Jungryong continued with a gentle smile.

“We need to end this battle as quickly as possible. The Arch Lich is likely creating new undead even now. If the S-rank Hunters lead the advance and destroy it, the monster army—made up mostly of undead—will collapse, and our casualties will be reduced.”

“M-Mr. Lee.”

“You seem to think the same way I do. Just like everyone else here. Isn’t that right, Mr. Wu?”

“Everyone else? What are you talking about?”

Only then did Wu Heixing look around in confusion.

Not only Wei Fenghu and the other high-ranking Chinese generals, but also Faye Chen, Magic Johnson, and even Prince Felix were nodding slightly and exchanging opinions.

“Hmm. Certainly…”

“Even if we reinforce our forces, the Arch Lich will be doing the same. The longer we drag this out, the larger the battle will become.”

“What if we select A-rank Hunters and other veterans and deploy them at the front, then lead the breakthrough with the S-rank Hunters?”

“It’s certainly dangerous, but it’s an operation with a real chance of success.”

“No matter how powerful a Named Monster the Arch Lich is, we have a good chance if the S-rank Hunters launch a concentrated assault.”

Wu Heixing’s face went white as the conversation reached his ears.

*Have these people lost their minds?*

They were looking favorably upon this insane operation. They must have all gone crazy.

Even Lee Jungryong, whom Wu Heixing had trusted, was supporting Jin Taekyung for some reason.

Wu Heixing, who absolutely did not want to be included in the suicide squad, hurriedly turned toward Jin Taekyung.

“W-Wait! If all the S-rank Hunters leave, wouldn’t that create a massive hole in our forces?”

“Huh.”

Jin Taekyung sucked in a startled breath and looked at Wu Heixing in surprise.

“Wow. You do use your brain once in a while.”

“……”

“You’re right. We should probably leave a few people behind.”

*That damn bangzi.*

But this was no time to be angry. Suppressing his surge of fury, Wu Heixing continued.

“R-Right. So, to prepare for any unforeseen circumstances, I—”

Jin Taekyung abruptly cut him off and turned toward Magic Johnson.

“It seems like you should stay behind. What do you think, Johnson?”

“Me?”

What kind of situation was this? Wu Heixing desperately tried to intervene.

“Magic Johnson? Wouldn’t it be better to have at least one mage come with us?”

“Of course that would be good. It would—but…”

Jin Taekyung smiled pleasantly at Wu Heixing.

“What about the rear?”

“Huh?”

“I’m asking what you’ll do if the Arch Lich teleports behind our lines and attacks us from the rear. Will you stop it?”

“……”

“No matter how powerful the Arch Lich is, it won’t be able to pull something like that if a great mage remains behind to interfere with its magic. And Magic Johnson’s wide-area magic could become the move that turns the tide of battle.”

Every word was perfectly reasonable. Wu Heixing’s mouth snapped shut, and Jin Taekyung clicked his tongue.

“Think before you run your mouth. Stop looking at those ‘watch your rear’ GIFs on the internet and think about the rear in an actual war.”

“……!”

Ignoring Wu Heixing, who had frozen like a statue, Jin Taekyung asked Magic Johnson,

“What do you think?”

“You’re right, Jin. So I’m the only one staying behind?”

Defense Minister Wei Fenghu, who had been silently observing the situation, suddenly spoke.

“The Arch Lich must have left a large number of high-level monsters behind for the final battle. There are far more of them than the number of A-rank Hunters on our side. To maintain an evenly matched battlefield, we need at least two more S-rank Hunters.”

It wasn’t over yet. There were still two positions open.

Wu Heixing, who had found a glimmer of hope, cleared his throat.

“Then, as a last resort, I’ll have to stay—”

“If the others have no objections, I would like to leave Prince Felix out first.”

“What?”

“I’m sorry, but I cannot explain the details. There is a complicated issue involved.”

Felix was not merely an S-rank Hunter. He was practically a symbol of the United Kingdom—a member of the royal family. And not some insignificant branch of it, either. He was third in line to the throne.

Everyone present understood that the “complicated issue” Wei Fenghu could not explain was a diplomatic problem with the United Kingdom.

“Well, his father is the King of the United Kingdom, so I suppose that’s possible. Then the prince is out.”

At Jin Taekyung’s words, Prince Felix spoke with an uncomfortable expression.

“I hope you understand that this is not my own choice. However, since I have been bound to the royal family since birth, I cannot disobey my royal father’s command—”

“It’s fine. I don’t care. I’d actually prefer it this way, since it would leave a bad taste in my mouth if the United Kingdom’s fourth in line to the throne got hurt during the operation I proposed.”

“Third! And show proper respect when speaking to me.”

“Oh, right. Congratulations on the bronze medal. Then, does anyone object to His Highness Prince Felix, a living hotbed of entrenched privilege, sitting this one out on the strength of his connections?”

Wu Heixing unconsciously started to raise his hand, but stopped at the answers that came from Faye Chen and Lee Jungryong.

“I don’t mind.”

“I agree.”

Jin Taekyung nodded and looked pointedly at Wu Heixing.

“What about you?”

“Me?”

“When the one remaining guy asks that, what am I supposed to say? Tinky Winky, Dipsy, or Po. Pick one.”

There was no way out.

Magic Johnson and Prince Felix were foreigners, and they had legitimate reasons. Faye Chen and Lee Jungryong had even agreed.

Wu Heixing squeezed his eyes shut, then opened them and muttered,

“…I agree.”

“Answer properly. If you answer like that, how the hell am I supposed to know whether you mean agreement or Donguibogam[^1]? Are you Heo Jun?”

“…….”

“I… agree.”

“Okay.”

It happened at Quick Attack speed.

One position still remained, but Wu Heixing felt a sense of foreboding.

And it didn’t take long for that foreboding to become certainty.

“I would like Faye Chen to fill the final position.”

But what had thrown Wu Heixing into confusion was that it wasn’t Jin Taekyung who had blocked his last escape route.

It was Lee Jungryong.

*What in the world is that old man thinking?*

Wu Heixing vividly remembered the conversation he had shared with Lee Jungryong on the day Jin Taekyung had trampled him so thoroughly that he still felt humiliated.

*He clearly suggested that we join forces. And now he’s stabbing me in the back like this?*

Faye Chen glanced at Wu Heixing, who was grinding his teeth, and tipped back his liquor glass.

“Well, Mr. Lee, I’m not the sort of person who enjoys danger. But wouldn’t our odds of success be higher if we left that brat behind instead of me?”

“No, Faye Chen. To reduce casualties, it will help us more if you stay.”

“You don’t know that kid. Just looking at him makes even someone who never had any patriotism develop some.”

“Don’t worry. I’ll be here.”

His tone was calm, but filled with certainty.

It was something Lee Jungryong could say because he was Lee Jungryong.

The gaze of the old hero, radiating confidence that no one present could deny, settled on one person.

“And Jin Taekyung. You’re here too, aren’t you?”

His eyes were deeply sunken, impossible to read.

Jin Taekyung silently met Lee Jungryong’s gaze before parting his lips.

“Our dear Vice Guild Master. You certainly have a talent for making obvious things sound complicated.”

“May I take that to mean you will also be joining the suicide squad?”

“Of course.”

“Brave. Heroic, even. In that case, I’ll yield the vanguard to you.”

“Great. Does that mean I get to leave behind a famous quote like Louis Armstrong? Something like, ‘This is one small step for one human being, but the Heavenly Demon’s Reign for monsters.’”

“That’s a bit rough for a quote destined for the history books. And you got the name wrong. It wasn’t Louis Armstrong. It was Neil Armstrong.”

“That’s an impressive amount of schooling. Still, it’s nothing compared to the length of my tissue roll.”

The people around them developed pounding headaches trying to follow Jin Taekyung’s answers, while Wu Heixing fell into despair.

Until barely a month ago, he had been enjoying a lavish yacht party surrounded by dozens of beautiful women.

Now he had been assigned to a suicide squad prepared to die.

And then, in the very next moment—

—Did you think I betrayed you?

“……!”

—Accept it. I promise there won’t be any danger.

As the Sound Transmission pierced his ears, Wu Heixing slowly raised his head.

Lee Jungryong was looking at him with a gentle smile as he continued speaking.

“He’ll carry out his assigned duty well. I guarantee it.”

Jin Taekyung slowly tapped the armrest of his chair as he replied,

“I’m really looking forward to seeing just how brilliantly he performs his duty.”

* * *

The somewhat lengthy meeting came to an end.

The suicide squad would be led by S-rank Hunters, with high-level A-rank Hunters and B-rank veterans making up the rest. The command staff would be working around the clock to select the members.

The Skeleton Warlord had remained silent throughout the meeting. But the moment we returned to the tent assigned to me on the western front, it solemnly declared,

“This commander will sit out this battle.”

“Yeah, fuck off.”

“At least ask why, you treacherous human.”

“Fine. Why?”

“As the commander of the undead army, I find it distasteful to fight my own kind.”

I answered with a dumbfounded expression.

“What the fuck are you talking about? Who’s been sucking the energy out of his own kind to replenish himself until now?”

“…Oh.”

“Let’s be honest. If you said you just didn’t want to go because you were scared of the Arch Lich, would I curse at you?”

“You would.”

“You son of a—… Oh.”

The Skeleton Warlord’s distrust of me deepened even further as it spoke.

“In any case, this commander no longer wishes to participate in this war. Honor the promise you made that day.”

“The promise I made that day?”

“Have you ever seen such a treacherous human? Didn’t you promise that, in exchange for protecting two humans, you would grant any request I made?”

“Oh.”

It had been a while since I’d been rendered speechless.

I had definitely made that promise. Normally, I would have brushed it off like someone pretending to have amnesia, but this time, I couldn’t ignore it in good conscience.

“Fine. What is your wish?”

The Skeleton Warlord shouted as though it had been waiting for the question.

“Give me freedom!”

“Freedom?”

“That is correct. You, treacherous human, have insulted and abused this commander all this time! The total is no less than 408 times!”

“…Are you from an animal rights group?”

“Honor your promise! This commander shall finally find freedom!”

Freedom.

My mind was already complicated enough with thoughts of Lee Jungryong, so I hadn’t expected a wish like this.

After thinking for a moment, I answered,

“Fine. I’ll give you freedom.”

“Ooh! Ooooooh!”

“Then goodbye.”

“Huh?”

Without hesitation, I pulled the Skeleton Warlord’s skull from my Inventory and threw it outside the tent.

Into the middle of the thousands of Hunters swarming around outside.

Clack!

The sound of it hitting something rang out, and the area around the tent erupted into chaos. Shouts rang out from every direction, followed by the booming detonation of magic.

“Monster! Monster attack!”

“Kill it!”

Boom! Kaboom!

How much time passed?

Five minutes? Ten?

Rustle, rustle.

The bottom edge of the tent suddenly began to shift. Then a black, glossy skull rolled in and stopped at my feet.

“Oh, look who it is.”

“……”

“What brings the Skeleton Warlord, proud owner of a free spirit, here?”

“You… human…”

A red glow flickered pitifully in the skull’s empty eye sockets.

Was I imagining it, or was an undead actually whimpering?

The Skeleton Warlord continued in a tearful voice.

“Can I… take back my wish?”

“Oh, of course.”

I continued in a bright customer-service voice.

“But you know wish coupons can’t be exchanged or refunded, right?”

“……”

“Come here, Bones.”

Hop.

The Skeleton Warlord feebly jumped into my arms.

[^1]: *Donguibogam* is a landmark medical encyclopedia compiled by Heo Jun. The joke plays on the similarity between *dongui* (“agreement”) and the title *Donguibogam*.
```
