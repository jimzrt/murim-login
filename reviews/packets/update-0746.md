<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0746.txt",
      "sha256": "1e61eaaefe5116ac079b0b20638f94e0aacb36e9d6ba6b477aea41a8c696a459",
      "bytes": 13114
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "aef355a966f885350f3bb4438ae7072eabeed7d0b06a45adf5214f10f029f431",
      "bytes": 2447
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "3f774f28d804f5f09c356e3a6e310d49d8a66135a801ace3d996971dd72a25fb",
      "bytes": 215580
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "fc81beb5f3421e7364409040e1f9814672be00dc48a9b4257b73fb161d85d5eb",
      "bytes": 2011
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "fda7eb067ad902298e7349e5e9e76e8dc445d36f62814233dcf62887df30f2f9",
      "bytes": 622
    },
    {
      "path": "characters/Michael.md",
      "sha256": "5de380b8f036b3902aada0f8ce10ac59ab35d430c7ff2f553bb811d2951d65c5",
      "bytes": 858
    },
    {
      "path": "characters/Song Song.md",
      "sha256": "eebb80155306c7552142e216740b5c83a7c98075ba6b0ba30b4fe65ef41df30a",
      "bytes": 939
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "9b1604ad19144d89ac1088b2d3964f569a44b4f2f7ec613e26df8407e4d63087",
      "bytes": 644
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "20c3f46b71b5baf33904439e4807b7c5b429d84d83db8e2ae3027d09893d4a3a",
      "bytes": 228924
    }
  ],
  "estimated_tokens": 10531
}
-->

# Durable State Update — Chapter 746

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 746. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 746. Profile updates may replace only one
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
  "chapter": 746,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 746,
    "continuity_sources": [746],
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
    "The Prophet commands the revived Hasasin and is preparing another judgment after the earlier attacks called Allah's Judgment.",
    "The Prophet can create a transparent concealment barrier that cannot be detected by science or Magic.",
    "The Prophet possesses at least ten unrefined S-rank Magic Gems that retain their original power.",
    "The retired Grand Mage Siegfried Wassmann was found dead in his sealed hideout after his life force was apparently drained by unknown magic.",
    "Michael Silbert remains the strongest suspect in Siegfried's death and possesses unexplained overwhelming power after a painful transformation.",
    "Jin has accepted the Supreme Peak Quest Unknown Death, whose mission is to discover the truth behind Siegfried's death.",
    "Mana levels and magical power continue rising, while mutation Gate phenomena occur dozens of times daily.",
    "Michael and Huginn continue manipulating media coverage to undermine Jin's public support.",
    "Magic Johnson is investigating stolen research materials from Siegfried's laboratory.",
    "Huginn has completed an undisclosed operation whose consequences are expected within three days.",
    "An enormous ancient monster has awakened in the deep sea, and a colossal tsunami is now approaching Tokyo with an unknown entity's cry.",
    "The Prophet's identity, age, and gender remain unknown, while Al-Nizar is established as the loyal S-rank Hunter leading the Hasasin."
  ],
  "continuity_sources": [
    745
  ],
  "open_questions": [
    "Who killed Siegfried Wassmann, by what magic, and why?",
    "How did Michael Silbert learn about A Area and Cheon Taemin's condition, and did he order Siegfried's death?",
    "What role do The Prophet, the revived Hasasin, and their planned judgment play in the terrorist campaign and Siegfried's death?",
    "What is Huginn's undisclosed operation, and can its consequences actually bring Jin down?",
    "What is the identity and purpose of the ancient monster, and is it connected to the tsunami and unknown cry approaching Tokyo?"
  ],
  "safe_through": 745,
  "temporary_decisions": [
    "Render 선지자 as The Prophet.",
    "Render 스켈레톤 킹 as Skeleton King.",
    "Render A구역 as A Area.",
    "Render 마력 as magical power, distinct from mana.",
    "Render 지크프리트 바스만 as Siegfried Wassmann and 실베르트 as Silbert."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 송송이    | **Song Song**     |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 제자     | **Disciple**                                 |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 평화 | **Peace Guild** | Guild name. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 강원도 | **Gangwon Province** | Province named in Taekyung’s joke about the Minotaur’s next life. |
| 일산 | **Ilsan** | Location of the Store and Lafesta |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 스위스 | **Switzerland** | Country associated with the watchmaker. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 한강 | **Han River** | River associated with the bridge-collapse incident Lee Jungryong recalls. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 신력 | **divine strength** | Superhuman strength attributed to Taekyung. |
| 꺽정 | **Kkeokjeong** | Jin's injured ally, addressed as Uncle Kkeokjeong. |
| 무한 | **Wuhan** | Capital of Hubei Province near Dongting Lake. |
| 텔레포트 | **Teleport** | Taekyung's label for the Blood Lord's unexplained disappearance. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 강강수월래 | **Ganggangsullae** | Traditional Korean circle dance and folk song used in Taekyung's word-chain joke. |
| 펜타곤 | **Pentagon** | Headquarters of the United States Department of Defense and source of intelligence about terrorist experiments. |
| 스카이 | **Sky** | American epithet for Cheon Taemin. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 리자드 | **Charmeleon** | Game-monster comparison. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |
| 오딘 | **Odin** | The name of the world's greatest Guild, invoking the Norse god. |
| 파리 | **Paris** | The city containing Ares Guild's branch attacked at the chapter's end. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 도쿄 | **Tokyo** | City visible behind Huginn's departing ship. |
| 도쿄만 | **Tokyo Bay** | Port area where Sugihara Gyoiku works. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 송송이 | guild_member_to_guild_member | Miss Song | formal-polite | Taekyung repeatedly uses 송이 씨 while introducing himself and attempting to court Song Song. |
| 송송이 | 진태경 | guild_member_to_guild_member | Taurus | casual-teasing | Song Song refers to Taekyung by his zodiac sign when calling him to the meal. |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |

## Listed compact profiles

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 743
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, a traveler between Murim and another world resembling the realm of immortals, and the creator of the beginner-accessible Smiling Mana Cultivation Method.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, trusted manager of media and official arrangements, and now the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 743
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 744
- **Aliases:** None
- **Role:** Michael Silbert is the Guild Master of Odin Guild, a public hero who helped suppress five Monster Waves, the hidden architect of a coordinated terrorist campaign designed to isolate Ares Guild, and the leader of a Guild controlling more than two hundred effectively owned Gates through permanent leases.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, and regards Jin Taekyung as a serious adversary.

### Song Song.md

# Song Song (송송이)

- **Safe through:** Chapter 732
- **Aliases:** Miss Song
- **Role:** Founding member of the Peace Guild; B-rank healer whose buff magic is powerful enough to be mistaken for an A-rank healer's; Healer Team Leader and temporary head of the Peace Guild's emergency rescue team, which is piloting free public-safety rescues for medium- and low-grade Gates in the capital region.
- **Personality:** Calm, practical, capable, and attentive; speaks briefly and handles domestic work with practiced skill
- **Voice:** Calm, concise, polite, and capable of devastatingly blunt candor
- **Relationships:** Works alongside Team Leader Choi, Butler Kim, Im Kkeokjeong, and Jin Taekyung as a member of the Peace Guild; Jin recruited her to help run its emergency rescue team, while she remains his same-age friend and guildmate after rejecting his confession.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 745
- **Aliases:** None
- **Role:** The Prophet is the mysterious leader of the revived Hasasin, a Middle Eastern terrorist organization preparing further attacks against apostates and Western heretics.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors and is revered as a sacred figure by the followers.

## Korean source

```text
＃746화



일상으로 돌아간다는 것은 대부분의 경우 안정을 뜻한다.

그러나 베일에 싸인 지크프리트 바스만의 죽음 직후, 각자의 자리로 돌아간 우리는 숨 가쁜 시간을 보내야 했다.

“강원도 속초의 C급 게이트에서 마력 분포도가 빠르게 증가 중입니다. 현재 2단계…… 3단계 진입! 변이 게이트 상황입니다!”

“현재 지원 가능한 인원은?”

“강원도 지부에 4개 팀이 대기 중이고, 속초시청과 연결된 텔레포트 마법진을 이용하면 5분 내로 현장 투입 가능합니다.”

“바로 출동시키도록 하세요. 자칫하면 몬스터 웨이브로 이어질 수 있으니, 생존자 구출과 빠른 진압을 최우선 목표로 합니다.”

복귀 이후의 상황은 말 그대로 최악이었다.

불과 몇 년 전까지만 하더라도 달에 한 번을 넘지 않던 변이 게이트가 하루에도 서너 건씩 발생했고, 이마저도 국내에 한정된 수치였다.

주가 대신 단 하루도 빠짐없이 상향선을 찍는 마력 분포도.

모든 방송국은 예능 프로그램 방영을 축소했으며, 새롭게 신설된 재난 속보 채널에서는 각 분야의 전문가들이 나와 치열한 토론을 펼쳤다.

- 사실 많은 분들이 간과하시는 것이, 마력 분포도 상승은 매년 꾸준히 있었던 일입니다. 오히려 대격변 직후에 비교하면 현재의 수치는 낮은 편에 속하죠. 이번 사태만 마무리되면 금방 진정 될 테니 국민 여러분들께서는 걱정 마시고…….

- 금방 진정된다니 이 무슨 말도 안 되는. 그리고 대격변 직후랑 지금을 비교하면 어떡합니까? 막말로 ‘승리의 날’에 마왕 잡고 나서, 인류가 무기 내려놓고 다 같이 강강수월래라도 돌았어요? 그때만 해도 한강 공원에 나가 보면 리자드맨이 있었어요. 남아 있던 몬스터 군단 처리하는 데만 일 년 가까이 걸린 거 모릅니까?

- 나는 일산 살아서 한강 공원에 리자드맨 있는 거 못 봤습니다. 내 말이 맞아요.

- 뭐 이런 병신…….

- 어허, 이 사람이. 나보다 나이도 한 살 어리던데 욕은 하지 말지.

- 한 살 어리긴 이 씨발럼아. 부모님이 출생 신고 늦게 했다. 됐냐?

- 사회자 양반. 이거 이대로 보고 있을 거요?

이제는 백발 성성한 학계의 권위자들이 TV에서 얼굴을 붉히고, 서로의 주장을 건 타이틀 매치를 펼치는 것도 그리 놀라운 축에 들지 못했다.

그들이 서로의 멱살을 잡는 그 순간에도, 옆 채널 뉴스에서는 세계 어딘가에서 발생한 변이 게이트나 몬스터 웨이브 속보를 알리고 있었으니까.

그리고 그 참혹한 현장 속에서, 나는 최선을 다해 고군분투했다.

서걱!

백염(白炎)의 창날이 갑옷보다 단단한 가죽과 뼈를 부드럽게 가른다.

몇 놈째 인지 모를 거대한 괴물은 제자리에 우뚝 멈춰 서더니, 이내 천천히 돌아섬과 동시에 세로로 갈라졌다.

스륵, 쿵!

3m에 달하던 거체가 정확히 절반으로 나뉘어 쓰러진 그 순간. 나는 몇 발자국 앞에서 넘어져 있던 한 남자와 눈이 마주쳤다.

간발의 차로 목숨을 건진 그의 손에는, 붉은 페인트로 쓰여진 플라스틱 피켓이 들려 있었다.

[국제범죄자 진태경을 체포하라!!!]

음.

이런 경우에는 어떻게 반응해야 하나 고민하다가, 그냥 씁쓸하게 웃어 버렸다.

아무리 싫어도 느낌표를 세 개나 쓰는 건 좀 너무한데, 하는 시답잖은 생각과 함께.

“괜찮아요?”

“……아.”

“약간 긁힌 것 빼고는 무사해 보이기는 하는데, 혹시 모르니까 계속 앉아 계세요. 어차피 다 끝났으니까 곧바로 구조팀 올 겁니다.”

나는 입술만 달싹이는 남자를 두고 돌아섰다.

불과 삼십 분 남짓한 시간 만에 초토화된 거리에는 죽은 몬스터들의 사체와 사람들의 시신이 뒤섞여 있었다.

감각을 곤두세워 주위를 탐색했지만, 더 이상의 생기(生氣)는 느껴지지 않았다.

‘이렇게까지 피해가 커질 일은 아니었는데.’

안타까운 일이다. 이 평화로운 소도시에서 몬스터 웨이브가 발생한 것도.

그리고…… 나를 지탄하기 위해 모인 수백 명의 시위대가 이 거리를 집회 장소로 선택한 것도.

철벅. 철벅.

나는 붉고 푸른 핏물이 뒤섞인 웅덩이를 밟으며 거리를 가로질렀다.

그새 냄새를 맡고 모여든 하이에나들은 이때를 놓치지 않고 카메라와 마이크를 들고 달려들었다.

“이번 몬스터 웨이브에 대해 어떻게 생각하십니까?”

“누구보다 빠르게 도착해서 몬스터 웨이브를 진압하셨습니다! 우선 저 역시 한 사람의 인간으로서 깊은 감사를 표하고…….”

“저들은 당신을 지탄하기 위해 모인 시위대였습니다. 혹시 이 몬스터 웨이브가 당신을 지지하는 누군가에 의해 인위적으로 발생했을 가능성은…….”

“미스터 스카이는 왜 아직도 모습을 드러내지 않는 겁니까! 얼마 전 사망한 지크프리트 바스만의 죽음과 당신은 어떤 연관이 있죠?”

“진, 한마디 해 주시죠!”

마치 사방에서 오물이 쏟아지는 듯한 기분.

나를 옹호하는 이도 있었지만, 그보다는 자극적인 제목을 뽑아내는 것에 혈안이 된 기자들이 훨씬 많았다.

그리고 아마도 저들 가운데 상당수는, 이러한 질문을 하는 대가로 다른 누군가에게 상당한 액수의 돈을 받고 있을 터였다.

예를 들자면…….

‘오딘 길드라든지.’

익히 짐작하고 있던 사실이다. 처음 최 팀장에게 그에 관한 이야기를 들었을 때도 크게 놀랍진 않았다.

언론 장악을 통한 여론 악화.

여론의 막강한 지지를 받고 있던 나와 아레스 길드를 노골적으로 흙탕물에 처박는 건 어지간해서는 시도할 수 없는 일이었다.

하지만 미카엘 실베르트는 충분히 그럴 만한 권력과 명분을 갖춘 놈이었다.

문제는, 최소한 언론에 한해서만큼은 그의 시도가 상상 이상으로 잘 먹혀 들고 있다는 점이고.

“선지자는 아직도 모습을 드러내지 않고 있습니다. 어딘가에서 당신을 지켜보고 있을 선지자에게 한 말씀 부탁드립니다!”

“아레스 길드가 일일 평균 3.6회의 상황을 진압할 때, 오딘 길드는 6.5회를 해결한다는 통계가 나왔습니다. 이에 대해 하실 말씀 없으십니까?”

“진태경 씨. 진태경 씨!”

“거기 당신! 질문 수준이 왜 그 따위야! 당신들이 그러고도 기자야!”

“모두 뒤로 물러나십시오. 당장!”

혼돈 그 자체였다.

더 많은 기삿거리와 사례금을 받기 위해 달려드는 기자들. 그리고 그런 기자들을 막아서는 경찰과 헌터들.

나는 내장이 뒤틀리는 듯한 기분을 느끼며 그들 사이를 빠져나갔다. 머릿속에서 울려 퍼지는 듯한 누군가의 목소리를 들으며.

- 너희 인간들은…… 참으로 개판이군.

몬스터에게 이런 말을 들을 날이 올 줄이야.

하지만 뭐라 대꾸할 말이 생각나지 않았다.

아니, 어쩌면 피켓을 본 그 순간부터 힘이 빠져서였을 수도 있겠다.

“입 다물어. 시끄럽다.”

그리 많은 공력을 사용하지 않았음에도 정신적 피로는 상당하다.

인벤토리에 넣어 둔 스켈레톤 킹을 향해 짤막하게 대답한 나는 챙겨 두었던 매직 스크롤을 꺼내어 찢었다.

찌익. 파아앗!

텔레포트 마법의 발현과 동시에 특유의 감각이 전신을 휩쓴다.

순식간에 뒤바뀌는 주위의 풍경. 빠르게 회복되는 시야 속에서 익숙한 얼굴이 보였다.

“빨리 왔네? 조금 전에 너 복귀한다고 연락받았었는데.”

짙은 피로가 배어 있는 목소리. 눈가에는 전에 없던 다크서클을 드리운 송송이는 불쑥 손수건부터 꺼내 내밀었다.

“우선 얼굴부터 닦아. 피 묻었어.”

손수건과 송송이를 번갈아 바라보던 나는 입맛을 다셨다.

“궁금해서 묻는 건데, 클린 마법은 뒀다가 국 끓여 먹냐?”

“마법을 무슨 동전 넣어서 쓰는 줄 알아? 포션 빨아서 마나는 채울 수 있어도 소모된 정신력은 못 채워. 요즘 가뜩이나 잠 부족한데 입 닥치고 손수건 쓰자.”

수면 부족의 결정적인 원인이 누구인지 알기 때문에 할 말이 없다.

잠자코 피를 닦은 뒤 손수건을 건네자, 더러워진 그것을 받아 든 송송이가 조용히 주문을 외웠다.

“클린(Clean).”

“……?”

솨아악.

먼지와 핏물이 순식간에 빠져나가며 깨끗해진 손수건.

어이없다는 표정으로 바라보는 나를 향해, 송송이가 천연덕스럽게 눈을 깜빡였다.

“왜? 이거 명품이야.”

그 당당한 한 마디에, 그리고 분명 이 상황을 노렸을 송송이의 모습에 나는 참지 못하고 실소를 흘렸다.

“허.”

“이제야 좀 웃네. 조금 전까지 TV에서는 아주 죽을상을 하고 있더니.”

“보고 있었어?”

“실시간 중계로 다 봤지. 미친 기자 새끼들이 개소리하는 것도 들었고.”

“……뭐, 그러려니 해야지. 따지고 보면 이 사단이 벌어진 것에 대해 내 책임도 어느 정도는 있으니까.”

송송이가 문득 눈살을 찌푸렸다.

“너까지 개소리할래?”

“…….”

“멀쩡해진다 싶더니 또 왜 이러실까. 그렇게 자책하고 싶으면 그놈들이나 죽이고 나서 실컷 해.”

그거야말로 내가 바라마지 않는 일이다.

하지만 그게 어디 쉽나. 당장 스위스에 다녀온 이후로 사흘이라는 시간이 흘렀음에도 크게 달라진 것은 없었다.

매직 존슨의 조사는 아직 결과를 내지 못하는 중이었고, 선지자의 종적은 온갖 마법과 위성 감시로도 잡아낼 수 없었으며, 미카엘 실베르트가 이끄는 오딘 길드는 나날이 상한가를 치고 있었으니까.

“너무 자책하지도, 걱정하지도 마. 너뿐만 아니라 다른 사람들도 열심히 노력하는 중이야. 특히 꺽정 아저씨는 어제도 당장 파리로 가서 미카엘 목을 따 버리겠다고 길길이 날뛰더라.”

“그. 천군만마를 얻은 것처럼 든든하긴 한데, 그랬다간 꺽정 아저씨 목이 따일걸.”

“어, 안 그래도 그대로 얘기해 줬지.”

“……이걸 그대로?”

“응, 사실이니까. 아무튼, 얘기 듣더니 좀 시무룩해하긴 했는데, 금방 납득하더라고.”

그래, 그것만으로도 고맙다.

나는 송송이와 이런저런 이야기들을 주고받으며 걸었다.

그리고 저택에서 철통같은 경호를 받으며 머무르고 있는 어머니와 하연이에 대한 소식을 끝까지 들었을 때쯤, 최 팀장이 기다리고 있던 집무실에 도착했다.

“오셨습니까.”

송송이 이상으로 피곤에 찌든 모습. 언제나 깔끔하게 정리되어 있던 집무실 내부는 어지러웠고, 책상 위에는 빈 커피잔이 가득했다.

“먼 길 다녀오시느라 고생하셨습니다. 그런데…….”

나와 송송이를 번갈아 본 최 팀장이 목소리를 낮췄다.

“다른 한 분은?”

“걱정마세요. 같이 왔으니까.”

- 여기 있다.

너무 오랫동안 처박아 뒀나.

나는 목소리만 들어도 뿔이 잔뜩 나 있는 녀석을 인벤토리에서 꺼냈다.

정확히는 허리에 찬 아공간 주머니를 뒤지는 척하면서, 명령어를 읊었다.

‘인벤토리 오픈. 소환.’

그리고 다음 순간 뿅 하고 나타난 건장한 백인 청년의 모습에, 송송이가 중얼거렸다.

“와, 순산했네.”

“입 다물어라. 아름답지만 버릇없는 인간 계집아. 감히 이 몸을 그런 것에 비유하…….”

“고마워. 기분 확 좋아진다.”

“이런 빌어먹을.”

퉁명스럽게 욕설을 내뱉는 스켈레톤 킹의 얼굴에는 불만이 가득했지만, 이건 우리로서도 어쩔 수 없는 일이었다.

‘이미 어느 정도 정체가 밝혀졌다고는 해도, 최대한 숨겨야 하니까.’

과거와 신분을 세탁했지만, 이 세상에 완벽이라는 단어는 존재하지 않는다. 전 세계를 통틀어 최고의 보안을 갖추었다고 알려진 펜타곤 역시 같은 방식으로 뚫렸다.

이런 상황이니 우리 역시 녀석의 노출을 최대한 막을 수밖에.

하지만 다음 순간 들려온 최 팀장의 한 마디에, 나는 스켈레톤 킹이라는 패를 꺼내야 한다는 것을 깨달았다.

“지금으로부터 삼 분 전, 도쿄만이 무너졌습니다.”
```

## Final English reading copy

```markdown
# Chapter 746

Returning to everyday life usually means stability.

But immediately after the mysterious death of Siegfried Wassmann, we returned to our respective positions only to face a frantic stretch of time.

“The magical-power distribution in the C-rank Gate in Sokcho, Gangwon Province, is rising rapidly. It’s currently at Stage Two…… entering Stage Three! It’s a mutation Gate!”

“How many people can we deploy right now?”

“Four teams are on standby at the Gangwon Province branch. If we use the Teleport Magic circle connected to Sokcho City Hall, they can be sent to the site within five minutes.”

“Send them out immediately. This could lead to a monster wave if we’re not careful, so make rescuing survivors and quickly suppressing the situation our top priorities.”

The situation after our return was, quite literally, the worst.

Until only a few years ago, mutation Gates had occurred no more than once a month. Now, three or four were appearing every day—and that figure was limited to Korea alone.

Instead of stock prices, the magical-power distribution chart was hitting an upward trend every single day without fail.

Every broadcasting station cut back on entertainment programming, while the newly established disaster-breaking-news channels featured experts from every field engaging in fierce debates.

“Many people overlook the fact that the rise in magical-power distribution has been happening steadily every year. Compared to the period immediately after the Great Cataclysm, the current figure is actually on the low side. Once this situation is over, things will calm down quickly, so there’s no need for the public to worry—”

“Calm down quickly? What kind of nonsense is that? And how can you compare things to immediately after the Great Cataclysm? To put it bluntly, after we killed the Demon King on the ‘Day of Victory,’ did humanity put down its weapons and all dance Ganggangsullae together?[^1] Back then, you could go to Han River Park and see lizardmen. Do you not remember that it took nearly a year just to deal with the monster armies that remained?”

“I live in Ilsan, so I never saw lizardmen in Han River Park. I’m right.”

“What a fucking moron…”

“Come on, now. You’re a year younger than me, so watch your language.”

“A year younger, my ass, you fucking bastard. My parents filed my birth registration late. Happy now?”

“Mr. Host, are you really going to sit there and watch this?”

It was no longer particularly surprising to see silver-haired authorities in academia turn red in the face on television and engage in title matches over their respective arguments.

Even as they grabbed one another by the collars, the news on the next channel was reporting breaking developments about mutation Gates or monster waves somewhere in the world.

And in the middle of those horrific scenes, I did my best to struggle through them.

*Shhk!*

The spearhead of White Flame smoothly cut through leather and bone harder than armor.

The enormous monster—I had no idea how many I’d killed by then—stopped dead in its tracks. Then it slowly turned around and split in two from top to bottom.

*Shff. Thud!*

The moment its three-meter-tall body fell, divided into two perfectly equal halves, I locked eyes with a man who had fallen a few steps away.

He had survived by the narrowest margin, and in his hand was a plastic picket sign with red-painted letters.

**ARREST INTERNATIONAL CRIMINAL JIN TAEKYUNG!!!**

*Hmm.*

I wondered how I was supposed to react in a situation like this, then simply gave him a bitter smile.

Even if he hated me that much, using three exclamation marks was going a little too far.

“Are you okay?”

“……Ah.”

“You look fine apart from a few scratches, but stay seated just in case. It’s all over anyway, so the rescue team will be here soon.”

I turned away from the man, who was only moving his lips.

In the street, reduced to a wasteland in barely thirty minutes, the corpses of dead monsters were mixed together with human bodies.

I sharpened my senses and searched the surroundings, but I could no longer feel any signs of life.

*It wasn’t supposed to cause this much damage.*

It was a tragedy that a monster wave had occurred in this peaceful little city.

And it was also a tragedy that the hundreds of protesters who had gathered to condemn me had chosen this street as their rallying point.

*Splash. Splash.*

I crossed the street, stepping through puddles where red and blue blood had mixed together.

Hyenas that had gathered after catching the scent wasted no time rushing in with cameras and microphones.

“What do you think about this monster wave?”

“You arrived faster than anyone else and suppressed the monster wave! First of all, as a fellow human being, I’d like to express my deepest gratitude—”

“These people had gathered to condemn you. Is it possible that this monster wave was artificially caused by someone who supports you—”

“Why has Mr. Sky still not shown himself? What connection do you have to the death of Siegfried Wassmann, who died recently?”

“Jin, give us a statement!”

It felt as though filth were pouring down on me from every direction.

There were people defending me, but far more reporters were frantic to come up with sensational headlines.

And many of them had probably been paid a considerable amount of money by someone else in exchange for asking questions like these.

For example…

*The Odin Guild.*

It was something I had already more or less expected. Even when Team Leader Choi first told me about it, I hadn’t been particularly surprised.

Worsening public opinion through media control.

Blatantly dragging me and the Ares Guild, which enjoyed overwhelming public support, through the mud was not something just anyone could attempt.

But Michael Silbert had enough power and justification to do exactly that.

The problem was that, at least where the media was concerned, his efforts were working far better than I had imagined.

“The Prophet still hasn’t revealed himself. What would you like to say to The Prophet, who is surely watching you from somewhere?”

“Statistics show that while the Ares Guild suppresses an average of 3.6 incidents per day, the Odin Guild resolves 6.5. Do you have anything to say about that?”

“Mr. Jin Taekyung! Mr. Jin Taekyung!”

“Hey, you! What kind of question is that? Do you call yourselves reporters?”

“Everyone, move back. Now!”

It was pure chaos.

Reporters rushing forward in pursuit of more articles and payment. Police officers and Hunters trying to hold those reporters back.

I slipped through them, feeling as though my insides were twisting, while listening to someone’s voice echoing in my head.

“You humans… are a real shitshow.”

I never thought I would live to hear something like that from a monster.

But I couldn’t think of anything to say in response.

No—maybe I had simply lost all my strength the moment I saw that picket sign.

“Shut up. You’re loud.”

Even though I hadn’t used that much internal energy, the mental exhaustion was considerable.

I gave the Skeleton King, stored in my Inventory, a brief answer, then pulled out the Magic Scroll I had brought along and tore it.

*Riiip. Fwoosh!*

The moment the Teleport Magic activated, its distinctive sensation swept through my entire body.

The scenery around me changed in an instant. As my vision quickly recovered, I saw a familiar face.

“You got back quickly. I only heard a little while ago that you were returning.”

Song Song’s voice was thick with exhaustion. Dark circles that hadn’t been there before hung beneath her eyes, and she immediately pulled out a handkerchief and held it out to me.

“Wipe your face first. There’s blood on it.”

I looked back and forth between the handkerchief and Song Song, then smacked my lips.

“I’m asking because I’m curious, but are you saving your Clean Magic to make soup with?”

“Do you think Magic works by putting coins into it? You can chug potions to replenish mana, but you can’t replenish mental energy that’s already been spent. I’m already not getting enough sleep these days, so shut up and use the handkerchief.”

I had nothing to say, since I knew exactly who the main reason for her lack of sleep was.

I silently wiped away the blood and handed the handkerchief back. Song Song accepted the dirty cloth and quietly chanted a spell.

“Clean.”

“……?”

*Whooosh.*

The dust and blood vanished in an instant, leaving the handkerchief spotless.

Song Song blinked innocently at me as I stared at her in disbelief.

“What? It’s designer.”

That shameless remark—and the fact that Song Song had clearly planned for this situation—made me snort despite myself.

“Ha.”

“You’re finally smiling. You looked like you were about to die on TV a little while ago.”

“You were watching?”

“I watched the whole thing live. I even heard those insane reporter bastards spouting bullshit.”

“……Well, I suppose I have to put up with it. If you think about it, I am partly responsible for this whole mess.”

Song Song suddenly furrowed her brow.

“Are you going to spout bullshit too?”

“……”

“Just when I thought you were getting back to normal, what’s this? If you want to blame yourself that badly, kill those bastards first and then beat yourself up all you want.”

That was exactly what I wanted to do.

But it wasn’t as though that would be easy. Three days had already passed since our trip to Switzerland, and almost nothing had changed.

Magic Johnson’s investigation had yet to produce any results. The Prophet’s whereabouts could not be traced even with every kind of Magic and satellite surveillance. And the Odin Guild, led by Michael Silbert, continued to soar higher by the day.

“Don’t blame yourself or worry too much. Other people are working hard too, not just you. Uncle Kkeokjeong in particular was running around like a madman yesterday, saying he was going to fly straight to Paris and cut Michael’s head off.”

“That… It’s reassuring to have an entire army on our side, but if he did that, Uncle Kkeokjeong would be the one losing his head.”

“Yeah, I told him exactly that.”

“You told him that?”

“Yeah. It’s true. Anyway, he looked a little dejected after hearing it, but he accepted it pretty quickly.”

That alone was something to be grateful for.

Song Song and I walked along, exchanging various bits of conversation.

By the time I had finished hearing all the news about my mother and Hayeon, who were staying at the mansion under ironclad security, we arrived at the office where Team Leader Choi was waiting.

“You’re back.”

He looked even more exhausted than Song Song. The office, which was always kept neat and orderly, was a mess, and the desk was covered with empty coffee cups.

“Thank you for your hard work on such a long trip. But…”

Team Leader Choi looked back and forth between Song Song and me, then lowered his voice.

“Where is the other person?”

“Don’t worry. He came with us.”

“I’m here.”

Had I left him cooped up for too long?

I took the Skeleton King out of my Inventory, pretending to rummage through the subspace pouch at my waist as I recited the command.

*Inventory open. Summon.*

The next moment, a sturdy young white man popped into existence.

Song Song muttered,

“Wow. Smooth delivery.”

“Shut your mouth, beautiful but ill-mannered human female. How dare you compare this body to such a thing…”

“Thanks. That really brightens my mood.”

“You damn…”

The Skeleton King’s face was full of displeasure as he muttered a curse, but there was nothing we could do about it.

*Even if his identity has already been exposed to some extent, we have to hide him as much as possible.*

We had scrubbed his past and identity clean, but the word “perfect” did not exist in this world. Even the Pentagon, known to have the best security in the world, had been breached in the same way.

Given the circumstances, we had no choice but to limit his exposure as much as possible.

But when I heard Team Leader Choi’s next words, I realized that I had to play the Skeleton King.

“Three minutes ago, Tokyo Bay collapsed.”[^2]

[^1]: Ganggangsullae is a traditional Korean circle dance and folk song.

[^2]: The Korean wording literally says that Tokyo Bay “collapsed,” preserving the alarming ambiguity of the announcement.
```
