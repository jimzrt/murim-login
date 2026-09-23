<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0739.txt",
      "sha256": "b22948b038e16cf73f7c56a4cfe972c04d6f34a35d3b9552621bfc13a69534f2",
      "bytes": 12892
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "31fe6f5c9f482926783fcde1c452eba1cc53c57239b46644c56559efb5915e49",
      "bytes": 1964
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "3f63db835bbab8cfe9bbcbce484765f2cea7ad7c35ef104f9612eaab2eb79346",
      "bytes": 213800
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "01490ece5a875e039cc012bdbaf3011d1ccfeb8d7c12a01973fbdc652356e592",
      "bytes": 752
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "33084acd9d18b572b0b23a09516dc0acfe88f8882bdbeeac868922426a629dd4",
      "bytes": 553
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "c81a5cb70b924a403826c74e9d9c2d62d140e1992020322635fe910a4c66161b",
      "bytes": 817
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "1835f59af716050632ce818c5c05c96ab4345e3256738e5593e687ae91b1b092",
      "bytes": 667
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "e137c618ebc9861db52788f07520b440b22a8036a094ea79c2285397f8de6539",
      "bytes": 2011
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "a5588292dde8bef7e41e868ac496df492811764e2f6a22bb2e038473348e04a9",
      "bytes": 622
    },
    {
      "path": "characters/Michael.md",
      "sha256": "9bbdbc623f3f708f8a22090369fadee7adf46f9d10e32b577d9b4bf4da4e4407",
      "bytes": 744
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "9b6f11d9830c05cc2a7771b405b8021d729d407000f7cfd71b4d611903c6706d",
      "bytes": 626
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4eb7ae6b7f72df9de6e81f6db97c762f07d9c04a11af54cc3539586facd3838b",
      "bytes": 226542
    }
  ],
  "estimated_tokens": 10468
}
-->

# Durable State Update — Chapter 739

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 739. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 739. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that
are absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
Before returning JSON, verify every `speaker` and `addressee` value contains at
least one Hangul character; use the Korean source spelling even when the same
person's English name appears in the reading copy. If no valid new pair exists,
return `"address_pairs": []`.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 739,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 739,
    "continuity_sources": [739],
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
    "Ten coordinated Monster Waves struck major cities and landmarks worldwide within twenty-four hours.",
    "Michael Silbert publicly posed as the hero who suppressed five waves while concealing his role in the terrorist campaign.",
    "The attacks targeted crowded sites, corporate headquarters, and major Guild branches to isolate Ares Guild.",
    "Jin and Team Leader Choi believe a final strike against Ares Guild is imminent.",
    "A hidden Prophet commands the fanatical organization behind the ten completed missions.",
    "The Prophet intends to reveal what caused the disasters, but the Prophet's identity and final plan remain unknown.",
    "Michael and Huginn engineered the terrorist operation through an alliance with Middle Eastern fanatics.",
    "The forced Quest Chain of Terror Attacks remains active and cannot be refused.",
    "Cheon Taemin remains unconscious.",
    "Idle Bystander continues to reduce Jin's abilities by ten percent during its thirty-day duration."
  ],
  "continuity_sources": [
    738
  ],
  "open_questions": [
    "What is the source and reach of Michael's unusually reliable intelligence, including his knowledge of the Pentagon's operations?",
    "What were the gifts delivered by Huginn, and what purpose did they serve?",
    "How did Odin Guild obtain or prepare its Mana Cultivation Method?",
    "Why is Michael so certain that Cheon Taemin will not intervene?",
    "Who is the Prophet, and what final action will be used to isolate Ares Guild and reveal the alleged cause of the disasters?"
  ],
  "safe_through": 738,
  "temporary_decisions": [
    "Render 최 팀장 as Team Leader Choi and 미카엘 실베르트 as Michael Silbert.",
    "Render 매직 존슨 as Magic Johnson.",
    "Render 선지자 as the Prophet and 인샬라 as Inshallah.",
    "Render 수수방관 as Idle Bystander.",
    "Render 연쇄 테러 as Chain of Terror Attacks."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 천태민    | **Cheon Taemin**  |
| 상태               | **Status**                     |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 마정석     | **Magic Gem**         |
| 공자      | **Young Master**                                                |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 시벌좌 | **Lord Fuck** | Crude online nickname created from Taekyung's accidental broadcast profanity. |
| 와이번 | **Wyvern** | High-tier dragonkin monster. |
| 신성 | **Morning Star** | Term in the summons referring to the Master of Morning Star. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 이강희 | **Lee Kanghee** | Chief editorial writer whose column condemns Jin Taekyung. |
| 아프리카 | **Africa** | Region where terrorist organizations are reportedly conducting Gate and Magic Gem experiments. |
| 중동 | **Middle East** | Region associated with the terrorist group and reported experiments. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 오딘 | **Odin** | The name of the world's greatest Guild, invoking the Norse god. |
| 파리 | **Paris** | The city containing Ares Guild's branch attacked at the chapter's end. |
| 항공자위대 | **Air Self-Defense Force** | Japanese force whose crashed aircraft caused secondary damage. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 고준 | 진태경 | Ares Guild combatant confronting the killer of his Master | you | hostile and informal | Go Jun uses 너 while demanding Jin confess to Lee Jungryong's death and threatening retaliation. |
| 진태경 | 고준 | dominant adversary confronting Lee Jungryong's Disciple | you | contemptuous and informal | Jin uses 너 and 놈 while overpowering Go Jun and ordering him to end the conflict with Lee Jungryong. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 737
- **Aliases:** Slayer; Sky (the American epithet used for him)
- **Role:** Cheon Taemin is Ares Guild Master and the world's greatest Hunter, known as the Slayer for killing the Demon King and creating the first Mana Cultivation Method during the Great Cataclysm, and he remains unconscious after more than twenty years in a wired mechanical capsule at his former mansion.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 738
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 735
- **Aliases:** Team Leader Seok
- **Role:** Go Jun was Ares Guild's Vice Guild Master, Lee Jungryong's Disciple and former Head of Security, the de facto successor to Lee's Ares legacy, and a mutated monster who was killed by Jin Taekyung in Area A.
- **Personality:** Disciplined and controlled under ordinary pressure, fiercely loyal to Lee Jungryong, but consumed by humiliation and rage when Ares Guild's authority is challenged.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Go Jun inherited Lee Jungryong's Ares legacy after becoming his Disciple and regarded Jin Taekyung and Choi Minwoo as enemies before his death.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 738
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 738
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, a traveler between Murim and another world resembling the realm of immortals, and the creator of the beginner-accessible Smiling Mana Cultivation Method.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, trusted manager of media and official arrangements, and now the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 738
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 738
- **Aliases:** None
- **Role:** Michael is the Guild Master of Odin Guild, a public hero who helped suppress five Monster Waves, and the hidden architect of a coordinated terrorist campaign designed to isolate Ares Guild.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, and regards Jin Taekyung as a serious adversary.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 738
- **Aliases:** None
- **Role:** The Prophet is the mysterious leader of a hidden Middle Eastern terrorist organization whose ten warriors carried out the day's coordinated attacks.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors and is revered as a sacred figure by the followers.

## Korean source

```text
＃739화



단 하루 만에 발생한 열 번의 몬스터 웨이브는 전 세계를 충격과 공포로 몰아넣기에 충분했다.

더군다나 사건의 발생지는 이름만 들어도 아는 각 나라의 수도, 혹은 대도시들.

오딘 길드를 선두로 한 여러 거대 길드가 신속하게 몬스터 웨이브를 진압했지만, 그로 인한 피해는 실로 막대했다.

현재까지 집계된 사망자만 수천 명에 이르는 끔찍한 대참사.

사람들은 각자의 집이나 비상 대피소에서 모든 촉각을 곤두세웠고, 미카엘 실베르트는 전 세계의 이목이 집중된 이때를 놓치지 않았다.

“파리에서의 첫 몬스터 웨이브 발생 당시, 저희 오딘 길드가 입수한 영상입니다.”

그리고 마침내 공개된 CCTV의 영상을 확인한 사람들은 다시 한번 충격에 휩싸였다.



[오딘 길드장 미카엘 실베르트, “이것은 몬스터 웨이브 이전에, 치밀하게 계획된 테러다.”]

[재해(災害)가 아닌 인재(人災)]

[악의가 불러온 재앙]

[폭탄과 마정석으로 무장한 10인의 살인마들. 공개된 CCTV 속 자살 테러범들은 누구?]

[전문가들의 CCTV 분석 결과, “그들은 각각 정제되지 않은 여러 개의 A급 마정석을 소지하고 있었고, 마력 분포도가 높은 게이트 인근 지역을 노려 테러를 저질렀다”]

[끔찍한 데자뷰에 몸서리치는 세계. “South Korea의 일을 기억하라”]

[폭탄 반입 및 정제되지 않은 A급 마정석들, 명백한 국제법 위반]

[폭탄과 마정석의 출처는 아프리카와 중동]



무수한 뉴스가 사방에서 쏟아졌다.

이번 몬스터 웨이브가 막을 수 없는 자연재해가 아닌, 테러로 인한 참극이라는 사실이 밝혀지자 사람들은 분노와 허탈함에 사로잡혔고 인터넷은 포화 상태에 빠졌다.



뭐라 할 말이 없다. ㄹㅇ미친놈들이네.

└ 진짜 도라이 새끼들인가.



반드시. 진실을. 만천하에 밝혀서. 모조리 교수형에. 처해야 합니다.



그 와중에 외국 기사 보니까 사우스 코리아 어쩌구 하던데. 이거 얼마 전에 있었던 석고준 사건 언급하는 건가요?

└ ㅇㅇ 맞음. 글고 지금 그거 때문에 한국 싫어하는 새끼들이 입에 거품 물고 떠드는 중임. 만악의 근원이 한국이라고.

└ ??않이 시발 어이가 업네. 애초에 천태민 아니었으면 살아 있지도 못할 새기들이;

└ 근데 어느 나라 애들이 그런 개소리하고 다니냐?

└ 짜장. 와사비.

└ 아.

└ 아니 닛본은 원래 그런 놈들이니까 그렇다 치는데, 중궈런 새끼들은 왜 그럼? 시벌좌한테 도움받은 건 벌써 다 잊음?

└ “중국.”

└ 단어 하나에 모든 게 담겨 있네.

└ 그래도 중국이 전에 도움받은 게 있어서 그런지, 확실히 일본보다 훨씬 덜함. 댓글로 시벌좌 욕하는 애들 IQ 추적해서 참교육시키는 애들도 있던데.

└ ;;나 아이큐 110인데 그걸로 위치 추적 가능하냐?

└ 다른 건 모르겠고 외국 커뮤에서도 한국 욕하는 애들 보이긴 하더라. 천태민이랑 진태경이 국격 열심히 높여 놨는데 석故준 씹새끼가 다 말아먹음.

└ 진태경이 한국의 격을 높였다고? 확실해? 그런 것치고는 오늘 통 안 보이던걸wwwwwwwwww.

└ 니네 항공자위대도 와이번한테 처맞은 이후로는 안 보이더라. 물론 도쿄 타워 무너지는 건 잘 봤음.

└ 와사비 어서 오고.

└ 시벌좌가 몸이 열 개쯤 되냐 쪽바리 새꺄; 그리고 TV 좀 봐라. 오늘 태경이 뒤지게 뛰어다녔다. 한발 늦었지만 어떻게든 한 사람이라도 살리겠다고 그러는 거 보니까 내 맘이 다 뭉클해지더라.

└ 역시 한국을 비판하면 무조건 일본인 취급인가www 안타깝지만 난 한국인인걸?

└ 앞으로도 한국인인 척하고 싶으면 키보드에서 w키 좀 빼라;;



분탕 종자한테 관심 줘 봤자 시간 낭비임. 지금 가장 중요한 건 테러범들이 어디 소속인지, 그리고 무슨 이유로 이런 짓을 벌였는지 알아내는 거지.

└ 테러범들이 다 아랍권이니까 뻔함. 알 카에다 아니면 IS겠지.

└ 그렇게 뻔하면 왜 아직까지 피해국들이 공동 성명이나 공식 발표를 미루고 있겠냐. 이 부분에 대해서는 확실한 확인 작업을 거쳐야 하는 게, 현재 알 카에다나 IS 쪽은 피해가 심각함.

└ 나도 윗 댓글에 동의함. 몇 주 전에 쟤들 본진 개털리고 지도자도 죽어서 교체 됐었음ㅇㅇ



중동과 아프리카를 휩쓸었던 피바람에 대해서는 이미 모르는 사람이 없었다.

얼굴과 이름, 심지어는 성별조차 알려지지 않은 의문의 자경단.

그들에 의해 테러리스트와 반군 집단의 수뇌부는 목이 날아갔고, 한순간에 지도층을 잃은 두 세력은 치열한 내부다툼 끝에 엄청난 피해를 입고 백기를 내걸어야 했다.



그럼 더 확실해진 거 아님? 힘이 약해지긴 했어도 지도자까지 잃었으면 복수하겠답시고 전 세계에 테러 벌일 만하지.

└ 잼민이들 많아서 모르나 본데, 911테러 때 미국 개빡치니까 후세인도 한번 쫄아서 자기들 아니라고 발뺌했었음. 얼마 전에는 앞으로 테러 안 할 테니까 제발 그만하라고 사실상 항복 선언 했고. 그런데 이번 테러에 연루된 나라만 미국 포함 10개국임. 이게 말이 된다고 생각하냐?

└ 아무리 미쳐도 불가능하지. 심지어 지금 중동 테러 집단 지도자들은 온건파에 속하는 애들이라던데.

└ 뭐지 진짜.



이는 비단 한국 네티즌들만이 품고 있는 의문이 아니었고, 세계 각국의 뉴스란과 커뮤니티는 치열한 갑론을박으로 달아올랐다.

그리고 그 의문에 대한 답은, 얼마 지나지 않아 한 영상에 담겨 전 세계로 송출되었다.

- 나, 선지자의 이름으로 선언한다.

흐릿한 조명 아래. 로브를 깊숙이 눌러쓴 정체불명의 인물.

노이즈 낀 화면 속에서 스스로를 선지자(先知者)라 칭한 그는 자신의 앞에 놓인 두 개의 목을 가리키며 말을 이었다.

- 자신의 안위를 위해 신념을 저버린 배교자(背敎者)들을 이 신성한 땅에서 지우고, 오직 합당한 복수와 정의를 세상에 바로 세울 것이다.

사람들이 목의 주인들을 알아보는 것은 그리 어렵지 않았다.

그들은 전 세계에서 가장 위험한 테러리스트 집단을 이끄는 우두머리였고, 불과 얼마 전 굴욕적인 항복 선언을 발표했으니까.

IS. 그리고 알 카에다.

처참하게 참수당한 전(前) 지도자들의 앞에서, 선지자는 천천히 입술을 뗐다.

- 신께서 함께하시는 이상, 우리는 멈추지 않을 것이다. 오늘을 시작으로 너희를 심판하고 벌할 것이다.

“……!”

“……!”

영상을 지켜보던 사람들은 자신도 모르게 숨을 삼켰다.

심판이라니. 오늘의 끔찍한 참극이 시작에 불과하다니.

하지만 믿을 수 없다는 듯이 눈을 부릅뜬 이들은 본능적으로 깨닫고 있었다.

스스로를 선지자라 칭한 저 정체불명의 인물은 결코 허언(虛言)을 하고 있지 않다는 것을.

당장 지금이라도 세계 어디에서 폭탄을 터트리고, 또 다른 재앙을 불러일으키리라는 것을.

그리고 다음 순간.

선지자의 마지막 한마디가 얼어붙은 사람들의 귓가를 파고들었다.

- 인샬라. 이 모든 것이 너희로부터 비롯되었음을 알아라.

치지직.

시끄러운 노이즈와 함께 짧은 영상이 끝났다.

아니, 모두가 끝났다고 생각한 그때. 또 다른 화면이 전송되기 시작했다.

달빛마저 흐릿한 어두운 밤.

핏물과 시체로 가득한 사막에 우뚝 선 한 사람이 문득 고개를 들었다. 복면 사이로 언뜻 보이는 얼굴은, 모두가 아는 누군가를 닮아 있었다.



* * *



스켈레톤 킹은 텅 빈 복도를 가로질렀다.

은빛 쟁반을 손에 든 그의 시선은 다른 한 손에 들린 스마트폰의 화면에 고정되어 있었다.



[피로 얼룩진 7일]

[스페인 마드리드에서 발생한 몬스터 웨이브. 또 다시 테러?]

[유령처럼 자취를 감춘 희대의 테러리스트, “선지자”.]

[영상 분석 결과 99.99% 일치. 젊은 영웅의 또 다른 신분.]

[조국일보 이강희 논설주간. “헛된 영웅심이 불러온 참극.”]

[팽팽한 여론. 영웅심에 도취 된 범죄자인가, 어둠의 자경단인가.]



“……빌어먹을 인간 놈들.”

스켈레톤 킹은 자신도 모르게 욕설을 중얼거렸다.

잠깐 확인한 것만으로도 인터넷 뉴스란의 상황은 개판이었다.

1면을 차지한 것은 노골적인 비난과 자극적인 제목의 기사뿐이었고, 그 안에서는 네티즌들 간의 치열한 싸움이 이어지고 있었다.



ㅋㅋ기레기 새끼 제목 뽑는 수준 봐라.

└ ㅇㅈ 조회수 늘리려고 환장함. 내용도 별거 없고 죄다 짜깁기.

└ 그런데 제목만 보면 아주 틀린 말은 아니지 않나.

└ 솔직히 나도 시벌좌 좋아하긴 하는데, 이번에는 섣부르게 움직인 게 맞는 것 같음.



이건 비난받아도 할 말 없지.

└ 뭘 할 말이 없냐. 몇 주 전에 알 카에다 등등 개털었을 때 니네 다 좋아했잖아. 누군지는 몰라도 그 새끼들 쓸어 버려서 속 시원하다고.

└ 그게 잘했다는 뜻은 아니지.

└ 그땐 좋고 지금은 아니야? 미친놈일세ㅋㅋ

└ 상황이 바뀌었잖아. 막말로 지금 죽은 사람이 몇 명임? 국뽕도 좋고 개인적인 팬심도 좋은데, 진태경이 한 행동으로 인해서 얼마나 심각한 상황이 벌어졌는지를 보셈.



나는 진태경 저 새끼 사고 칠 줄 알았다ㅇㅇ 젊은 영웅이니 포스트 천태민이니 하면서 띄워 줄 때부터 거들먹거리는 거 보기 싫었음.

└ ;;;이건 진짜 개소리네. 도대체 언제 거들먹거렸냐. 언론에서 한창 띄워 줄 때도 추리닝 입고 돌아다니던 형인데.



중립 기어 박고 한마디 하자면 개인적으로는 그냥 안타깝다. 진태경이 피에 굶주린 살인마라서 그런 짓을 벌였겠냐?

└ 그럼 뭔데.

└ 사건 당시 시기를 보면 마나 연공법 공개 직전이다. 막말로 중동 테러리스트랑 아프리카 반군 집단에 소속된 각성자가 한둘이냐? 걔들이 마나 연공법 익혀서 테러 포함 온갖 범죄 저지르면 그거 누가 감당하냐?

└ 그렇다고 살인을 정당화할 수는 없지.

└ 그래, 네 말이 맞다. 하지만 정확하게 짚고 넘어가자. 그땐 모두가 정당화했고 상상 이상의 미친놈 하나 나타나니까 다들 빛의 속도로 태세전환 하는 것뿐임.

└ 국내고 해외고 그때 당시에는 하나같이 자경단 빨아 줬었다. 누군지는 모르겠지만 참 잘했어요. 굳이 알려고 하지 맙시다. 딱 그 분위기였는데 반전된 거지.



진태경 빠돌이들 많네ㅋㅋ 그래 봤자 결국 전 세계적으로 비난받고 있잖아.

└ 팩트는 여론 조사 결과 시벌좌 옹호하는 사람들이 더 많음. 자극적인 제목으로 기사가 양산되니까 그렇게 보이는 것뿐이지.



이해가 안 되는 건, 이 상황이 됐는데도 얼굴 한번 안 비추는 천태민임. 진태경도 벌써 며칠째 잠수 중이고.

└ 사고 치고 나 몰라라 하는 거지. ㄹㅇ 역겨움ㅋㅋ 그에 비해 오딘 길드 봐라. 킹갓미카엘이 과거고 미래다.



인터넷 기사에 달린 댓글을 읽어 가던 스켈레톤 킹은 문득 생각했다.

‘만약 진실을 알게 되면, 저 댓글을 단 인간들이 무슨 표정을 지을까.’

하지만 스켈레톤 킹은 알고 있었다. 어차피 전부 부질없는 생각이라는 것을.

적어도 지금 당장은 아무런 진실도 밝힐 수 없었다. 도리어 역풍(逆風)을 맞고 완전히 침몰할 수도 있다.

지금껏 그가 겪은 인간들의 사회는 생각보다 훨씬 더 복잡하고, 답답했다.

‘멍청한 인간들.’

고개를 절레절레 저은 스켈레톤 킹은 거대한 문 앞에서 발걸음을 멈췄다.

어제 가져다 놓았던 은쟁반이 그대로 있는 것을 발견하고 한숨을 푹 쉰 그가 조심스럽게 문고리를 잡아당겼다.

달칵.

서서히 열리는 문 너머로, 가부좌를 튼 채 앉아 있는 한 사람의 등이 보였다.
```

## Final English reading copy

```markdown
# Chapter 739

Ten Monster Waves in a single day were more than enough to plunge the entire world into shock and terror.

What made it worse was that the attacks had occurred in capitals or major cities whose names were known around the world.

Several major Guilds, led by Odin Guild, had swiftly suppressed the Monster Waves, but the resulting damage was immense.

It was a horrific catastrophe. The confirmed death toll alone had already reached several thousand.

People kept their senses on high alert in their homes or emergency shelters, and Michael Silbert did not miss the opportunity to seize the attention of the entire world.

“This is footage Odin Guild obtained when the first Monster Wave occurred in Paris.”

And when people finally saw the CCTV footage that had been released, they were once again thrown into shock.

> **Odin Guild Master Michael Silbert: “Before this was a Monster Wave, it was a meticulously planned terrorist attack.”**

> **Not a natural disaster, but a man-made one**

> **A calamity born of malice**

> **Ten killers armed with bombs and Magic Gems. Who are the suicide terrorists shown in the released CCTV footage?**

> **Following expert analysis of the CCTV footage: “Each of them possessed several unrefined A-rank Magic Gems, and they carried out the attacks by targeting areas near Gates with high mana concentrations.”**

> **The world shudders at a horrifying déjà vu: “Remember what happened in South Korea.”**

> **Bringing in bombs and unrefined A-rank Magic Gems was an obvious violation of international law**

> **The bombs and Magic Gems came from Africa and the Middle East**

Countless news reports poured in from every direction.

Once it became clear that the Monster Waves had not been unstoppable natural disasters but tragedies caused by terrorism, people were consumed by anger and emptiness, and the internet reached saturation point.

> Nothing to say. These guys are seriously insane.

>> Are they really crazy fuckers?

> The truth must be revealed to the whole world. Every last one of them must be hanged.

> I was reading a foreign article, and it kept mentioning South Korea. Is it talking about the Go Jun incident from a little while ago?

>> Yeah, that’s right. And because of that, the people who hate Korea are foaming at the mouth and shouting that Korea is the root of all evil.

>> What the fuck? This is ridiculous. They wouldn’t even be alive if it weren’t for Cheon Taemin in the first place.

>> But which country’s people are going around saying such bullshit?

>> Jjajang. Wasabi.[^1]

>> Oh.

>> I can understand Japan, since they’ve always been like that, but why are those Chinese bastards doing it? Have they already forgotten that Lord Fuck helped them?

>> “China.”

>> That one word says everything.

>> Still, maybe because China received help from him before, it’s definitely much less extreme than Japan. There are even people tracking the IQs of those who curse Lord Fuck in the comments and teaching them a lesson.

>> I’m IQ 110. Can you track my location with that?

>> I don’t know about anything else, but I have seen people bashing Korea on foreign forums too. Cheon Taemin and Jin Taekyung worked hard to raise Korea’s standing, but that dead bastard Go Jun ruined it all.

>> Jin Taekyung raised Korea’s standing? Are you sure? You wouldn’t know it from the fact that he hasn’t shown his face at all today, lololololol.

>> Your Air Self-Defense Force hasn’t shown its face since getting beaten up by a Wyvern, either. Though I did get a good look at Tokyo Tower collapsing.

>> Welcome, wasabi.

>> Does Lord Fuck have ten bodies, you Japanese bastard? Watch some TV. Taekyung ran himself ragged today. He was a step late, but seeing him try to save even one person somehow really moved me.

>> So criticizing Korea automatically makes someone Japanese now, lol? Unfortunately, I’m Korean.

>> Take the W key off your keyboard if you want to keep pretending to be Korean;;

[^1]: Food-based shorthand used here as derogatory references to Chinese and Japanese people.

There was no point paying attention to trolls. The most important thing now was finding out who the terrorists belonged to and why they had committed such acts.

> The terrorists are all from the Arab world, so it’s obvious. It has to be either Al Qaeda or IS.

>> If it’s so obvious, why are the affected countries still delaying a joint statement or official announcement? This absolutely needs to be verified. Al Qaeda and IS have both suffered serious losses recently.

>> I agree with the comment above. A few weeks ago, their main bases were completely wrecked and their leader was killed and replaced.

No one was unaware of the bloodbath that had swept through the Middle East and Africa.

A mysterious group of vigilantes whose faces, names, and even genders were unknown.

They had beheaded the leaders of the terrorist and rebel groups, and the two factions, suddenly deprived of their leadership, suffered enormous losses in the fierce internal struggles that followed and were forced to raise the white flag.

> Doesn’t that make it even more obvious? They may have been weakened, but if they lost their leader, they could easily have carried out terrorist attacks around the world in the name of revenge.

>> There are probably a lot of elementary school kids here who don’t know this, but when the United States got seriously pissed off during the 9/11 attacks, Hussein got scared and denied that it was them. A little while ago, they practically surrendered and begged people to stop, saying they wouldn’t commit any more terrorist attacks. But this terrorist attack involved ten countries, including the United States. Do you really think that makes sense?

>> No matter how crazy they are, that’s impossible. Besides, I heard the current leaders of the Middle Eastern terrorist groups belong to the moderate faction.

>> What the hell is going on?

This was not a question held only by Korean netizens. News sites and online communities around the world were heated by fierce arguments for and against.

And before long, the answer to that question was broadcast across the world in a single video.

—I declare in the name of the Prophet.

Beneath dim lighting stood an unidentified figure with a robe pulled deeply over their head.

In the grainy footage, the figure called themself the Prophet and pointed to the two heads placed in front of them before continuing.

—I will erase the apostates who abandoned their convictions for the sake of their own safety from this sacred land, and establish rightful vengeance and justice throughout the world.

It was not difficult for people to recognize the owners of the heads.

They were the leaders of the most dangerous terrorist organizations in the world, and only a short while ago, they had announced a humiliating surrender.

IS.

And Al Qaeda.

Before the horribly beheaded former leaders, the Prophet slowly parted their lips.

—As long as God is with us, we will not stop. Beginning today, we will judge and punish you.

“……!”

“……!”

The people watching the video caught their breath without realizing it.

Judgment.

Today’s horrific tragedy was only the beginning.

Those who widened their eyes as if they could not believe it nevertheless realized instinctively.

The unidentified figure who called themself the Prophet was not making empty threats.

Even now, they could detonate a bomb somewhere in the world and bring about another disaster.

And then.

The Prophet’s final words pierced the ears of the frozen audience.

—Inshallah. Know that all of this began with you.

*Crackle.*

The short video ended amid a burst of harsh static.

No—just when everyone thought it had ended, another screen began transmitting.

It was a dark night in which even the moonlight was hazy.

A lone figure standing in a desert filled with blood and corpses suddenly raised their head. The face glimpsed through the mask resembled someone everyone knew.

* * *

The Skeleton King crossed an empty corridor.

Holding a silver tray in one hand, he kept his gaze fixed on the smartphone in the other.

> **Seven Days Stained with Blood**

> **Monster Wave in Madrid, Spain. Terrorism Again?**

> **The Notorious Terrorist Who Vanished Like a Ghost: “The Prophet”**

> **Video Analysis Shows a 99.99% Match. Another Identity of a Young Hero**

> **Joguk Ilbo Chief Editorial Writer Lee Kanghee: “A Tragedy Born of Pointless Heroism”**

> **Public Opinion on a Knife-Edge: A Criminal Intoxicated by Heroism, or a Vigilante of Darkness?**

“……Damn humans.”

The Skeleton King muttered a curse without realizing it.

Even from the brief glance he had taken, the state of the online news pages was a complete mess.

The front page was filled with nothing but openly condemnatory articles and sensational headlines, while fierce battles between netizens raged beneath them.

> Lol, look at the level of these garbage reporters’ headlines.

>> For real. They’re desperate to increase their views. The articles say nothing and are all stitched together from scraps.

>> But if you only look at the headline, it isn’t entirely wrong, is it?

>> Honestly, I like Lord Fuck too, but I think he really did act rashly this time.

> This deserves criticism. There’s nothing he can say for himself.

>> What do you mean, there’s nothing he can say? A few weeks ago, when he completely wrecked Al Qaeda and the others, you were all cheering. Whoever he was, you said it felt great to see him wipe those bastards out.

>> That doesn’t mean what he did was right.

>> So it was fine then but not now? You’re fucking crazy, lol.

>> The situation has changed. Seriously, how many people are dead now? Nationalist hype and personal fandom are all well and good, but look at how serious the situation has become because of what Jin Taekyung did.

> I knew that bastard Jin Taekyung would cause trouble. I hated watching him get full of himself from the moment people started hyping him up as a young hero and the next Cheon Taemin.

>> That’s complete bullshit. When was he ever full of himself? Even when the media was hyping him nonstop, hyung still walked around in a tracksuit.

> Putting it neutrally, I personally just think it’s unfortunate. Do you really think Jin Taekyung did that because he was some bloodthirsty killer?

>> Then why did he do it?

>> Look at the timing. It was right before the Mana Cultivation Method was released. Seriously, do you think there are only one or two Awakened among the Middle Eastern terrorists and African rebel groups? Who was supposed to deal with them if they learned the Mana Cultivation Method and started committing every kind of crime, including terrorism?

>> That still doesn’t justify murder.

>> Fine, you’re right. But let’s be precise. Everyone justified it back then. Now that one unbelievably insane bastard has appeared, you’re all switching sides at the speed of light.

>> At the time, people both at home and abroad were universally praising the vigilantes. “Whoever you are, great job. Let’s not bother finding out who they are.” That was the atmosphere, and now it has completely reversed.

> There are a lot of Jin Taekyung fanboys here, lol. That doesn’t change the fact that he’s being condemned around the world.

>> The fact is, polls show that more people support Lord Fuck. It only looks otherwise because sensational headlines are being mass-produced.

> What I don’t understand is Cheon Taemin. Even now, he hasn’t shown his face once. Jin Taekyung has been missing for several days too.

>> He caused trouble and is pretending it has nothing to do with him. Seriously disgusting, lol. Just look at Odin Guild. King-God Michael is the past and the future.

As he read through the comments beneath the online articles, the Skeleton King suddenly wondered:

*If they learned the truth, what kind of expressions would the humans who posted those comments make?*

But the Skeleton King knew that it was all a pointless thought.

At least for now, there was no way to reveal the truth. On the contrary, they might be completely sunk by the backlash.

The society of humans he had experienced so far was far more complicated and frustrating than he had expected.

*Stupid humans.*

The Skeleton King shook his head and stopped in front of a massive door.

When he discovered that the silver tray he had brought yesterday was still sitting there, he let out a deep sigh and carefully pulled on the doorknob.

*Click.*

Beyond the slowly opening door, he saw the back of someone sitting cross-legged.
```
