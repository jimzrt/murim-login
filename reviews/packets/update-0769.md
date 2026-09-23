<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0769.txt",
      "sha256": "bbf4365e778d26ddaf3f9592eac1114a89b2f14863d9cf3b45797ee427b294a0",
      "bytes": 13131
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "306f918d13b9ea7b16fca3c0fc2bfd65177a0ddf9c512a4be7ccf5054b5d0152",
      "bytes": 1739
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b642569400cfefa186d9fb39f61b7044eaf85531a43b1f69bc1db84603fc672f",
      "bytes": 221882
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "b44cb86cbdbb32f35aa595693762ca28db7a08f4be395856e183799487ab78d9",
      "bytes": 553
    },
    {
      "path": "characters/Huginn.md",
      "sha256": "5a8569d35806eecb4fb8f040ba2b06f2c893077d448fe53a36635072cb91ac2c",
      "bytes": 674
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "3c4f4ea31fc3ceb562cc2548376616813a760d547339f1c691b7ab84cabf4e64",
      "bytes": 2017
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "1f5dbe7dbc9d9e325fe04c407c39420bac621feeaa1ef6881618036dba579843",
      "bytes": 622
    },
    {
      "path": "characters/Leviathan.md",
      "sha256": "c9892a6fc8d1ed65fa84f4ff43e07c9a83226080bfb1a17f7dad48b2194d4de2",
      "bytes": 666
    },
    {
      "path": "characters/Michael.md",
      "sha256": "b1f157163220be0ed5a4f3e6f9aab019cf3100dda6b118585c9adf160edb5342",
      "bytes": 935
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "d6f8b8f134e8d331c3f88bc7a75de3d287aa213210d8d4c531a0d9e42ea9c7b9",
      "bytes": 644
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "62dfef7a1387e12bad96883ae0b19aca93fc615c81d7bcedf2769c9664b77a5d",
      "bytes": 238974
    }
  ],
  "estimated_tokens": 10549
}
-->

# Durable State Update — Chapter 769

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 769. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 769. Profile updates may replace only one
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
  "chapter": 769,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 769,
    "continuity_sources": [769],
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
    "The UN General Assembly approved the reestablishment of the World Hunter Federation after a full vote.",
    "Baek Hanseong opposed an immediate decision and cast the final vote after recognizing that the proposal could no longer be stopped.",
    "Worldwide panic has produced riots, economic disruption, and threats against governments; France has suffered five large-scale riots and partial destruction of the Louvre.",
    "Michael Silbert's warning about a second Great Cataclysm helped ignite the global panic and unrest.",
    "Baek Hanseong and Choi Minwoo tried to delay the UN decision to buy time because Choi identified the situation as a war.",
    "Russia and the United States opposed or cautioned against the Federation because of its vast authority and uncertain leadership, while Zhonghua supported Baek's call for caution."
  ],
  "continuity_sources": [
    768
  ],
  "open_questions": [
    "How will the reestablished World Hunter Federation exercise its enormous authority, and who will control it?",
    "What war did Choi Minwoo identify, and how will Jin Taekyung and Choi prepare for it?",
    "How will Michael Silbert exploit the Federation's reestablishment and the worldwide unrest?",
    "How will governments and populations respond now that the Federation has been approved?"
  ],
  "safe_through": 768,
  "temporary_decisions": [
    "Render 세계 헌터 연맹 as World Hunter Federation.",
    "Render 대격변 as Great Cataclysm and 두 번째 대격변 as second Great Cataclysm.",
    "Render 중화인민국 as Zhonghua People's Republic.",
    "Render 종신 대통령 as president for life.",
    "Render 마법 포션 as magical potion."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 후긴 | **Huginn** | One of the two ravens associated with Odin in Norse mythology. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 레비아탄 | **Leviathan** | Ancient S-rank sea monster associated with Asmodeus. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 러시아 | **Russia** | Country associated with Sorkovache and the imperial-style sofa. |
| 영국 | **United Kingdom** | Country associated with BCC. |
| 대통령 | **President** | Title for Korea's head of state. |
| 뮌헨 | **Munich** | Second word in one of the necromantic chants. |
| 시리 | **City** | Second word in one of the necromantic chants. |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |
| 쓰촨 | **Sichuan** | Variant spelling used for the region associated with the pattern Jin recognizes. |
| 화기 | **fire qi** | The fire nature imparted to internal energy by the Fire Gate Divine Technique. |
| 부산 | **Busan** | City where the Haeundae Gate crisis occurs. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 프랑스 | **France** | Country containing Paris and Luxembourg Gardens. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |
| 일본 | **Japan** | Country requesting emergency assistance and under Leviathan's attack. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 진태경 | 대통령 | Hunter_to_President | Mr. President | formal-polite | Taekyung addresses the President respectfully during their airport greeting. |
| 대통령 | 진태경 | President_to_Hunter | Mr. Jin Taekyung | formal-polite | The President addresses Taekyung by name at the airport photo line. |
| 후긴 | 진태경 | Odin Guild messenger to an Ares Guild ally and adversary | Mr. Jin | formal-polite, increasingly coercive | Huginn addresses Jin while questioning his presence and later warns him not to lose his temper. |
| 진태경 | 후긴 | Ares Guild ally to an Odin Guild messenger and adversary | Mr. Crow | insulting-casual and profane | Jin uses the crow nickname while mocking Huginn's theatrics and threatening posture. |
| 미카엘 | 후긴 | Odin Guild Master to personally selected fixer | Huginn | formal, familiar, and commanding | Michael calls Huginn by name while inviting him into the study. |
| 후긴 | 미카엘 | loyal retainer to Guild Master | Guild Master | formal-polite and deferential | Huginn reports the Swiss investigation, accepts Michael's orders, and promises to complete the mission. |
| 진태경 | 레비아탄 | enemy and hunted monster | Leviathan; you | insulting-casual | Jin orders Leviathan to leave and dismisses its attempt to kill the Skeleton King. |
| 레비아탄 | 진태경 | attacking enemy | you bastard | enraged-insulting | Leviathan directly curses Jin while resisting his attacks. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 미카엘 | 진태경 | rival_to_target | you | quietly polite but threatening | Michael warns Jin to reconsider for the sake of Jin's monster friend. |
| 진태경 | 미카엘 | target_to_rival | Go fuck yourself | blunt and profane | Jin rejects Michael's proposal to resurrect the World Hunter Federation. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 768
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Huginn.md

# Huginn (후긴)

- **Safe through:** Chapter 766
- **Aliases:** None
- **Role:** Huginn is a powerful Odin Guild messenger, trusted field operative, and elite fixer personally selected and trained by Michael.
- **Personality:** Polished, condescending, calculating, overconfident, and absolutely loyal to his Guild Master.
- **Voice:** Formal and gentlemanly in presentation, indirect and theatrical at first, then blunt and coercive when delivering an ultimatum.
- **Relationships:** Huginn serves Odin Guild's Guild Master with absolute loyalty and acts as an adversary to Jin Taekyung and Choi Minwoo.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 768
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, and a publicly recognized S-rank-level Hunter who formally retains an A-rank license, as well as a traveler between Murim and another world resembling the realm of immortals and the principal Hunter opposing Michael Silbert's terrorist campaign.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, trusted manager of media and official arrangements, and now the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 768
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Leviathan.md

# Leviathan (레비아탄)

- **Safe through:** Chapter 767
- **Aliases:** None
- **Role:** Leviathan was an ancient S-rank sea monster and ruler of the sea who was killed by Jin Taekyung after the deep-sea hunt, leaving a final warning that the Cataclysm was approaching.
- **Personality:** Ravenous, domineering, and driven by instinctive hunger for magical power and food.
- **Voice:** Its spoken voice is not established; it communicates in Demon Realm language.
- **Relationships:** Leviathan once served the Demon King Asmodeus, its master, and withdrew into the deep sea after Asmodeus fell.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 768
- **Aliases:** None
- **Role:** Michael Silbert is the Guild Master of Odin Guild, a public hero who helped suppress five Monster Waves, the hidden architect of a coordinated terrorist campaign, and a feared rival whose warning about a second Great Cataclysm triggered worldwide panic and pressure to reestablish the World Hunter Federation.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, and regards Jin Taekyung as a serious adversary.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 761
- **Aliases:** None
- **Role:** The Prophet is the mysterious leader of the revived Hasasin, a Middle Eastern terrorist organization preparing further attacks against apostates and Western heretics.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors and is revered as a sacred figure by the followers.

## Korean source

```text
＃769화



아무리 냉철한 이성의 소유자라 해도 매 순간 평정심을 유지할 수는 없다.

미카엘 실베르트가 자신이 동요하고 있다는 사실을 깨달은 것은 연거푸 세 잔의 커피를 내리고 난 후였다.

‘동요한다고? 내가?’

이는 그에게 있어서도 꽤 놀라운 일이었고, 그 놀라움은 곧 불쾌감으로 변했다.

지도자는 흔들리는 모습을 보여서는 안 된다. 적에게도, 아군에게도. 심지어는 스스로에게도 마찬가지다.

이 전쟁에서 반드시 승리하기 위해서는 조금의 허점도 보여서는 안 되니까.

치열한 전투 도중 사람의 움직임이 무뎌지는 것은, 자신이 상처 입었다는 사실을 깨달은 그 순간부터다.

미카엘 실베르트는 어떤 고통도 무시할 수 있어야 비로소 모든 것을 가질 수 있다고 생각했고, 그 생각대로 살아왔다.

아주 오래전, 죽음의 문턱에서 살아 돌아온 그 날부터.

하지만 그랬던 그가 오늘 같은 동요를 보이는 이유는 두 가지였다.

하나는 원대한 꿈에 거의 다다랐다는 떨림.

또 다른 하나는…….

‘아마 그놈 때문이겠지.’

커피 잔이 뿜어내는 김 사이로 한 사람의 얼굴이 스쳐 지나간다.

자신보다 한참이나 젊고, 말도 안 되는 짧은 시간 만에 대중의 사랑을 독차지했으며 결국 가장 까다로운 장애물이 되어 버린 한 청년이.

‘진태경.’

입 안에서 맴도는 그 이름과 함께 목 언저리에서 느껴지는 미약한 통증.

슥.

미카엘 실베르트가 목을 빈틈없이 감싼 폴라티를 조심스럽게 내리자, 목 언저리에 선명히 각인된 검붉은 상처가 보였다.

한순간 스며든 열기로 인하여 일그러진 피부.

장장 십여 년 만에 처음으로 입은 상처이자, 며칠 전 진태경이 남기고 간 흔적을 더듬던 그때였다.

지이이잉.

어디선가 울리는 진동음에 채 아물지 않은 상흔(傷痕)을 어루만지던 손끝이 흔들렸다.

본능적으로 옷깃을 끌어 올려 상처를 덮은 미카엘 실베르트는 스마트폰 화면에 뜬 이름을 바라보았다.



[임마누엘]



세상에 임마누엘이라는 이름을 가진 사람들은 많다.

그러나 후긴이라는 다리를 거치지 않고 그에게 직접 연락할 수 있는 임마누엘은 단 한 사람뿐이다.

달칵.

― 축하드립니다. 길드장님.

통화가 연결되자마자 들려오는 프랑스 대통령의 목소리에, 소리 내어 웃은 미카엘 실베르트는 자신의 앞에 놓인 세 잔의 커피를 곧장 바닥을 향해 기울였다.

그 안에 담겨 있던 자신의 초조함과 동요도, 뿌옇게 솟아오르던 김 사이로 슬며시 비치던 한 사람의 얼굴도 함께.

그리고 그렇게 모든 것을 쏟아 낸 뒤 텅 빈 잔에 남은 것은 오직 환희와 승리감뿐이었다.

‘내가…… 이겼다.’

왕좌가 마련됐으니, 이제 남은 것은 화려한 대관식.

지금 이 순간 미카엘 실베르트는 문득 궁금해졌다.

소식을 접한 진태경이 어떤 표정을 짓고 있을지.

눈앞에 선하게 떠오르는 그 광경에 입꼬리가 꿈틀거렸다.



* * *



이상한 일이다.

절대 일어나서는 안 되는 일이 현실로 이루어졌음에도, 지금 내 마음은 이상하리만치 담담했다.

그리고 그럴 수 있었던 가장 큰 이유 중 하나는 아마도 충분히 예견했던 상황이었기 때문이었다.

“씨벌.”

그래도 할 건 해야지. 야호라고 할 수는 없으니까.

습관처럼 쌍욕을 내뱉은 나는 지금 막 문을 열고 들어온 최 팀장을 바라보았다.

“결국…… 막지 못한 겁니까?”

최 팀장이 무겁게 고개를 끄덕였다.

“한계가 분명했습니다.”

“생각지도 못한 러시아까지 도왔는데도?”

“설령 이번 총회에서 중립을 지킨 영국이 저희와 뜻을 함께했어도 결과는 그리 달라지지 않았을 겁니다. 지금은 이미 전시(戰時) 상황이나 마찬가지니까요.”

정치에는 심 봉사나 다름없는 나조차도 상임이사국이 얼마나 막강한 권한을 지녔는지는 알고 있다.

TV에 나와 떠들어 대는 전문가들이 말하는 국제 정세라는 것이 결국 나라 간의 파워 게임(Power Game)이라는 것도.

어차피 이곳도 또 다른 무림이나 다름없다.

무림인들이 가문과 무공을 내세운다면 강대국은 군사, 경제, 그리고 생산력을 비롯한 각종 자원으로 자신들을 과시하며 약소국들을 찍어 누른다.

그리고 이번 UN 총회에는 강대국 중의 강대국인 상임이사국이 무려 다섯이나 힘을 합쳐 세계 헌터 연맹 재설립을 반대했다.

평소였다면 좋고 싫고를 떠나 그들이 지닌 힘과 영향력이 미치는 많은 국가가 부속품처럼 그 뜻을 따라갔을 것이다.

그러니까, 평소였다면.

“이미 콩고, 시리아, 에티오피아와 미얀마를 비롯한 20여 개국은 내전 발발 직전입니다. 곳곳에서 민심을 명분으로 쿠데타 세력이 일어나고 있으니, 그들로서는 하루라도 빨리 결정을 짓고 싶었겠죠. 다른 국가의 상황도 크게 다르지 않고요.”

“빌어먹을.”

“공포가 법치(法治)를 무너트리고 있습니다. 미카엘 실베르트가 원했던 상황이었겠죠.”

이건 정치를 떠나 생존의 문제다.

당장 본인들의 집이 잿더미가 되게 생겼는데 힘 좋고 덩치 큰 떡대 여러 명이 소화전 앞을 가로막고 조금만 기다려 보라고 한다면 누가 고분고분하게 돌아갈까.

나 역시 그들의 입장을 충분히 이해했다.

다만…….

‘알고 보니 그 소화기의 정체가 화염 방사기라는 건 전혀 다른 문제지.’

인정한다.

세계 헌터 연맹은 반드시 필요하다.

지난 대격변 당시, 끔찍한 불길이 사방으로 번지는 상황에서 그들은 훌륭한 소방관 역할을 해 주었으니까. 누구보다 헌신적인 영웅으로서 최선을 다했으니까.

하지만 미카엘 실베르트는 아니다.

사람들 몰래 불을 지른 장본인이 새로운 소방관으로 임명된다니, 그것만 한 블랙 코미디가 어디 있겠나.

그렇기에 나는 사흘 전, 모두의 앞에서 말했었다.

놈을 막아야 한다고. 앞으로 허락된 시간 안에 모든 힘을 다해 미카엘 실베르트의 발목을 붙잡아야 한다고.

그리고 이제, 뒤집어 놓았던 모래시계의 모래알이 끝나 가고 있었다.

그것도 불과 사흘 만에.

“이건…… 이건 너무 이르지 않나.”

방 안에는 나와 최 팀장만 있는 것이 아니었다.

신음처럼 중얼거린 스켈레톤 킹이 손에 들고 있던 서류를 힘껏 움켜쥐었다.

손아귀에서 형편없이 구겨진 종이 사이로 프린팅되어 있는 낯익은 얼굴이 보인다. 지금보다 더 젊고, 더 인간적인 표정으로 카메라를 바라보는 남자.

바로 미카엘 실베르트였다.

정확히는, 수십 년 전의 미카엘 실베르트.

지난 사흘간, 우리는 지금까지 지크프리트 바스만의 은거지에서 가져온 모든 자료와 미카엘 실베르트의 지난 행적을 조사했다.

놈을 저지할 수 있을 만한 단서를 찾기 위해서.

그러나 미카엘 실베르트는 전 세계에서도 손꼽히는 유명 인사. 대격변 당시부터 수십 년간 차곡차곡 쌓여 온 정보는 너무나도 방대했고, 시간은 우리를 기다려 주지 않았다.

“막을 수 없는 거냐?”

나는 스켈레톤 킹의 물음에 아무런 대답도 하지 못했다.

은거지에서 나온 자료를 담당한 매직 존슨이 지금쯤 무언가를 발견했을지도 모르지만, 그 가능성은 희박했다.

이미 사흘 전에 홀로그램으로 찾아왔을 당시에도 그는 모든 자료를 열 번도 넘게 검토하고, 또 검토한 뒤였으니까.

결국 지금 내가 할 수 있는 대답은 절망에 가까운 짐작뿐이었다.

“그래. 아마도.”

“……!”

“지금까지 나온 결과는, 이미 모두가 아는 사실을 재확인한 것뿐이야.”

그 말을 끝으로 무거운 침묵이 내리깔린 그때.

파르르 떨리는 눈빛으로 산더미처럼 쌓인 서류 더미를 응시하던 스켈레톤 킹이 불쑥 입을 열었다.

“아니, 방법이라면 남아 있다.”

“방법이…… 있다고?”

“아주 간단하고 손쉬운 방법이다. 어렵게 돌아갈 필요조차 없는.”

그리고 다음 순간, 귓가를 파고든 스켈레톤 킹의 한 마디는 내가 조금도 예상치 못했던 것이었다.

“간악한 인간이여, 네가 이 몸을 소멸시키면 된다.”

“뭐?”

처음에는 잘못 들은 줄 알았다.

하지만 멍하니 반문하는 나를 향해, 스켈레톤 킹은 침착한 목소리로 말을 이어 갔다.

“물론 지금 당장은 아니다. 모두의 앞에서, 중요한 인간들이 지켜보는 앞에서 이 몸의 정체를 밝히고 소멸시켜라. 그래야 확실한 효과를 볼 수 있을 테니.”

“……!”

“간단한 해결책이지 않나. 놈의 요구를 들어줄 수밖에 없을 만큼 강한 약점을 잡혔다면, 그 약점을 없애면 된다. 적당한 이유와 함께.”

얼음장 같은 기운이 등골을 타고 흐른다. 전신의 솜털이 곤두섰다.

평소와 같이 마주하고 있지만, 눈앞에 보이는 녀석이 그 어느 때보다 낯설게 느껴졌다.

깊게 가라앉은 눈빛. 흐릿하게 맺힌 미소. 담담한 목소리까지.

그 모든 것 하나하나가.

“이 몸은 몬스터다. 너희 인간에게는 악(惡) 그 자체나 다름없는 존재이며, 하찮은 인간의 시선 따위는 얼마든지 속이고 접근할 수 있을 정도로 교활하기도 하지.”

스켈레톤 킹이 씩 웃었다.

“너, 인간이여. 이제 와 고백하건대 사실 너는 그리 간악하지 않다. 단지 무식하게 강하고 훨씬 더 멍청할 뿐이다. 다른 인간들도 그 사실을 알고 있으니 직접 행동으로 보여 준다면 그리 어렵지 않게 납득할 것이다.”

쿵. 쿵. 쿵.

심장이 거세게 뛴다.

수많은 생각이 머릿속을 헤집고, 나도 모르는 사이에 벌어진 입에서는 차마 토해 내지 못한 목소리들이 맴돌았다.

‘이런 미친…….’

단 한 번도 생각해 보지 않았고, 그렇기에 더욱 충격이었다.

그리고 일순간 얼어붙은 내 귓가로, 한 사람의 음성이 송곳처럼 파고들었다.

“가능성이 있습니다.”

“최 팀장님!”

본능적으로 터져 나온 내 고함에도 최 팀장은 털끝 하나 움찔하지 않았다.

그는 딱딱하게 굳은 얼굴로 말을 이었다.

“약점은, 그것이 노출되고 적이 이용할 수 있을 때 비로소 약점이라 부를 수 있습니다. 스스로 제거한다면 아무런 문제도 생기지 않습니다.”

“도대체 지금 무슨…….”

“대중들은 여전히 진태경 씨를 사랑합니다. 비록 테러리스트 집단의 토벌로 말미암아 선지자의 등장을 불러오긴 했으나 그것은 더 큰 선의(善意)를 위해서였고, 수많은 비난에도 온 힘을 다해 사람들을 구했으니까요. 특히 레비아탄과 뮌헨에서의 몬스터 웨이브에서 진태경 씨가 보여 준 희생정신은…….”

“그만!”

다시 한번 터져 나온 고함에 비로소 입이 닫힌다.

그러나 최 팀장의 침묵은 그리 오래가지 못했다.

“그럼 어쩌실 생각입니까?”

“……!”

“다른 방법이 있습니까? 미카엘 실베르트가 세계 헌터 연맹을, 전 세계를 손아귀에 넣는 것을 막을 방법이 있습니까?”

숨이 막혔다.

순간 말문을 잃은 나를 향해, 최 팀장은 어딘가에 억누르고 있던 말들을 쉼 없이 쏟아 냈다.

“스켈레톤 킹을 아무도 모르는 먼 곳으로, 혹은 누구도 찾지 못할 곳에 숨길 수도 있겠지요. 하지만 미카엘 실베르트가 진실을 밝힌다면 사람들이 그 사실을 믿어 주겠습니까?”

“하지만 저 녀석은…….”

“예, 맞습니다. 그는 분명 많은 사람들을 구했습니다. 쓰촨에서, 부산에서, 일본과 뮌헨에서도 우리와 함께 싸웠습니다. 어쩌면 그로 인해 목숨을 건진 이들이 수십만이 넘을지도 모릅니다. 하지만!”

쿵.

강하게 내디딘 발걸음과 함께, 최 팀장의 얼굴이 눈앞으로 성큼 다가온다.

수많은 감정이 뒤섞인 한 쌍의 눈동자와 힘 있는 목소리가 뒤를 이었다.

“사람들은 믿지 않습니다.”

그리고 그의 마지막 한 마디는, 꺼져 가는 모닥불처럼 힘없이 사그라졌다.

“스켈레톤 킹은, 그는 몬스터니까요.”
```

## Final English reading copy

```markdown
# Chapter 769

Even the most clearheaded person in the world could not maintain their composure every moment of every day.

Michael Silbert realized he was shaken only after brewing three cups of coffee in a row.

*Shaken? Me?*

It was quite a shock even to him, and that shock soon turned into displeasure.

A leader must never show weakness. Not to their enemies or their allies. Not even to themselves.

To win this war at all costs, he could not reveal the slightest opening.

During a fierce battle, a person's movements began to grow sluggish from the moment they realized they had been wounded.

Michael Silbert believed he could possess everything only if he could ignore any pain, and he had lived according to that belief.

Ever since the day, long ago, when he had returned from the threshold of death.

But there were two reasons he was shaken like this today.

One was the tremor that came from nearly reaching his grand dream.

The other was…

*It’s probably because of that bastard.*

A face passed through the steam rising from the coffee cups.

The face of a young man much younger than himself, who had claimed the public’s love in an absurdly short time and ultimately become the most troublesome obstacle of all.

*Jin Taekyung.*

Along with the name lingering in his mouth came a faint pain around his throat.

Swish.

When Michael Silbert carefully lowered the turtleneck covering his neck completely, a clearly imprinted, dark-red wound came into view.

Skin warped by heat that had seeped in for only an instant.

It was the first wound he had suffered in more than a decade, and he had been tracing the mark Jin Taekyung had left behind several days earlier when—

Bzzzt.

The sound of a vibration rang from somewhere, and the fingertips stroking the wound that had yet to heal trembled.

Michael Silbert instinctively pulled up his collar to cover the injury, then looked at the name appearing on his smartphone screen.

[Emmanuel]

There were many people in the world named Emmanuel.

But only one Emmanuel could contact him directly without going through Huginn.

Click.

“Congratulations, Guild Master.”

The moment the call connected, the voice of the President of France came through. Michael Silbert laughed aloud and immediately tipped the three cups of coffee in front of him toward the floor.

Along with them, he poured out his anxiety and agitation—and the face that had faintly appeared through the hazy steam.

After everything had been spilled, the only things remaining in the empty cups were joy and triumph.

*I… won.*

The throne had been prepared. All that remained now was a magnificent coronation.

At that moment, Michael Silbert suddenly wondered what expression Jin Taekyung was wearing after hearing the news.

His lips twitched at the scene that rose vividly before his eyes.

* * *

It was strange.

Even though something that absolutely should not have happened had become reality, my heart was strangely calm.

One of the main reasons was probably that I had expected this situation well enough.

“Fuck.”

Still, I had to do what needed to be done. It wasn’t like I could shout, *Yay!*

After letting out a string of curses out of habit, I looked at Team Leader Choi, who had just opened the door and entered.

“In the end… you couldn’t stop it?”

Team Leader Choi nodded heavily.

“Our limits were clear.”

“Even though Russia helped us? Russia, of all countries?”

“Even if the United Kingdom, which remained neutral during this General Assembly, had joined us, the result would not have been very different. We’re already in a situation practically identical to wartime.”

Even someone as blind to politics as I was knew how much authority the permanent members of the Security Council possessed.

I also knew that the international situation experts on television kept talking about was ultimately just a power game between nations.

This place was no different from another Murim, anyway.

If martial artists flaunted their families and martial arts, Great Nations displayed their power through military strength, economies, production capacity, and all kinds of resources, using them to crush weaker countries beneath them.

And during this UN General Assembly, five of the greatest powers in the world—all permanent members of the Security Council—had joined forces to oppose the reestablishment of the World Hunter Federation.

Under normal circumstances, regardless of whether they liked the proposal, the many countries influenced by those nations would have followed their will like mere appendages.

That was, if things had been normal.

“More than twenty countries, including Congo, Syria, Ethiopia, and Myanmar, are on the verge of civil war. Coup factions are rising in various places under the pretext of representing public sentiment. They must have wanted to reach a decision as quickly as possible. The situations in other countries aren’t much different.”

“Damn it.”

“Fear is destroying the rule of law. This must be the situation Michael Silbert wanted.”

This was a matter of survival, apart from politics.

If several big, powerful men blocked the fire hydrant while your house was about to burn to ashes and told you to wait just a little longer, who would obediently turn around and leave?

I understood their position perfectly well.

However…

*It was an entirely different matter if that fire extinguisher turned out to be a flamethrower.*

I admitted it.

The World Hunter Federation was absolutely necessary.

During the last Great Cataclysm, when terrible flames had spread in every direction, they had played the role of excellent firefighters. They had done their best as heroes more devoted than anyone else.

But Michael Silbert was different.

What could be a greater black comedy than the person who had secretly started the fire being appointed as the new firefighter?

That was why, three days ago, I had said it in front of everyone.

We had to stop him. Within the time we had been given, we had to use every ounce of our strength to hold Michael Silbert back.

And now, the grains of sand in the hourglass we had turned over were running out.

After only three days.

“This is… isn’t this too soon?”

It wasn’t just Team Leader Choi and me in the room.

The Skeleton King muttered like a groan and crushed the documents in his hand with all his strength.

A familiar face was visible on the badly crumpled paper between his fingers—a man looking at the camera with an expression younger and more human than the one he wore now.

It was Michael Silbert.

More precisely, Michael Silbert from several decades ago.

Over the past three days, we had investigated every piece of material brought from Siegfried Wassman’s hideout, along with Michael Silbert’s past actions.

We were searching for a clue that could stop him.

But Michael Silbert was one of the most famous people in the entire world. The information that had accumulated over decades, ever since the Great Cataclysm, was simply too vast, and time was not waiting for us.

“Can’t we stop him?”

I could not answer the Skeleton King’s question.

Magic Johnson, who had been put in charge of the material from the hideout, might have discovered something by now, but the possibility was slim.

Even when he had come to us by hologram three days earlier, he had already gone over all the material more than ten times—and then gone over it again.

In the end, the only answer I could give was a guess bordering on despair.

“Yeah. Probably not.”

“……!”

“Everything we’ve found so far has only reconfirmed facts everyone already knew.”

The moment I finished speaking, a heavy silence settled over the room.

The Skeleton King stared at the mountains of documents with trembling eyes before suddenly opening his mouth.

“No. There is still one way.”

“There’s… a way?”

“It is a very simple and easy method. There is no need to take a difficult route.”

The next moment, the Skeleton King said something that I had never expected.

“Wicked human, you need only erase this body.”

“What?”

At first, I thought I had heard him wrong.

But as I stared blankly at him, the Skeleton King continued in a calm voice.

“Of course, not right away. Reveal this body’s identity in front of everyone, before the important humans watching, and then erase me. Only then will it have a definite effect.”

“……!”

“It is a simple solution, is it not? If you have been caught by a weakness so serious that you have no choice but to comply with his demands, then eliminate the weakness. Along with a suitable explanation.”

An icy chill ran down my spine. Every hair on my body stood on end.

I was facing him as usual, but the guy before me felt more unfamiliar than ever.

His deeply sunken gaze. His faint smile. Even his calm voice.

Every last one of them.

“This body is a monster. To you humans, I am practically evil itself, and I am also cunning enough to deceive the eyes of insignificant humans and approach them whenever I wish.”

The Skeleton King grinned.

“You, human. I confess now that you are not particularly devious. You are merely absurdly strong and much stupider. The other humans know that about you as well, so if you demonstrate it through your actions, they should have little trouble accepting it.”

Boom. Boom. Boom.

My heart pounded violently.

Countless thoughts tore through my mind, and voices I could not bring myself to let out circled inside my open mouth.

*This is fucking insane…*

I had never once considered such a thing, which was why it shocked me even more.

Then, as I froze for an instant, a voice pierced my ears like a needle.

“It is a possibility.”

“Team Leader Choi!”

My shout burst out instinctively, but Team Leader Choi did not flinch in the slightest.

His face rigid, he continued.

“A weakness can only be called a weakness when it is exposed and the enemy can exploit it. If you eliminate it yourself, no problem will arise.”

“What the hell are you talking about right now…”

“The public still loves you, Mr. Jin Taekyung. Although the extermination of the terrorist group brought about the appearance of The Prophet, it was done for the sake of a greater good, and you gave everything you had to save people despite the countless accusations thrown at you. In particular, the self-sacrifice you showed against Leviathan and during the Monster Wave in Munich…”

“Enough!”

My second shout finally made him close his mouth.

But Team Leader Choi’s silence did not last long.

“Then what do you intend to do?”

“……!”

“Is there another way? Is there any way to stop Michael Silbert from taking the World Hunter Federation—and the entire world—into his hands?”

I could barely breathe.

The moment I lost my voice, Team Leader Choi poured out the words he had been holding back somewhere inside him without pause.

“We could hide the Skeleton King in some distant, unknown place—or somewhere no one could find him. But if Michael Silbert revealed the truth, would people believe it?”

“But he…”

“Yes, that’s right. He has definitely saved many people. He fought alongside us in Sichuan, Busan, Japan, and Munich. The number of people who survived because of him may exceed several hundred thousand. But!”

Thud.

As he stepped forward forcefully, Team Leader Choi’s face drew close before my eyes.

A pair of eyes filled with countless tangled emotions was followed by a powerful voice.

“People don’t believe it.”

And his final words faded weakly, like a dying campfire.

“Because the Skeleton King… he’s a monster.”
```
