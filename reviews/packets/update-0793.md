<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0793.txt",
      "sha256": "3c21a07da511b5e152c680cffae02b98e82f3dfe879ab14b4a2e33b2350463ef",
      "bytes": 13216
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "a01f72ef8ab18bc422bdef0b70ae0c42f354596618189ccc09e444cd18482ffd",
      "bytes": 1519
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b107ad8b032275926005814226705b9c99fd04942849ff404275ebe5d6ff70cc",
      "bytes": 223952
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "1b1b9163a5a8bedae2da2816b6f6ea53b648077c359430f3740eb19fc64aef3f",
      "bytes": 553
    },
    {
      "path": "characters/Huginn.md",
      "sha256": "10e41a3abe1064e3e8b7f7ff0ce2cf184fcd41c9f0d498794782c4567a6f98b1",
      "bytes": 674
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "d7bb9d6aab86499790d7734f207d65ba2a11b0c7450e0a9b1d04721c28d21103",
      "bytes": 1921
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "bb4485975afb61ad0cda810690d445075107f422bd9dd19b4b8ef187453111ab",
      "bytes": 622
    },
    {
      "path": "characters/Michael.md",
      "sha256": "bf5e558e949e7481c8229d7c9bfaf5651bd269e4a3dcb8ee58b0a19c1773bd51",
      "bytes": 820
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "8e76f46c0d5985126d2ff53d10a9893565d23a55cf98d47220cfcd540fc2a1a1",
      "bytes": 693
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "efe725efd25279c1f15fa45386a842b440ddc40827b49dfe9381ce06b41c4d11",
      "bytes": 245718
    }
  ],
  "estimated_tokens": 10424
}
-->

# Durable State Update — Chapter 793

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 793. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 793. Profile updates may replace only one
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
  "chapter": 793,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 793,
    "continuity_sources": [793],
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
    "Jin Taekyung is the World Hunter Federation's Alliance Leader.",
    "The Main Quest [Cataclysm] requires Jin to eliminate The Prophet within an unspecified time limit.",
    "The Prophet is hiding somewhere in the Middle East and possesses a large quantity of unrefined Magic Gems; Jin suspects they are preparing a major attack.",
    "The Federation and allied forces have deployed 100,000 Hunters to search for The Prophet.",
    "A Monster Wave is attacking the Skeleton King and Xiao Shen in the desert; skeletal eagles are searching for something bearing a human scent.",
    "The missing search squad was killed, and the Skeleton King believes its unknown killer has left the site.",
    "Chuck Hagel has been selected to command the multinational force at the main base; Jin has arrived there and is responding to an urgent Monster Wave request."
  ],
  "continuity_sources": [
    792
  ],
  "open_questions": [
    "Can Jin find and eliminate The Prophet before the Main Quest's time limit expires?",
    "What killed the search squad, and what trace is the Skeleton King investigating?",
    "Will the Skeleton King and Xiao Shen withstand the Monster Wave, and where is it attacking?",
    "When will The Prophet's attack begin, and what will the Cataclysm involve?"
  ],
  "safe_through": 792,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Do not identify the unknown killer or the human-scented trace until revealed."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 일신     | **One God**         |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 살기     | **killing intent**                               |                                                       |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 귀가      | **your family**                                                 |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 후긴 | **Huginn** | One of the two ravens associated with Odin in Norse mythology. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 여름이 | **Yeoreum** | Name Hayeon gives to the Level 2 kitten. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 메이지 | **Mage** | Skeleton subtype mentioned alongside Soldiers and Warriors. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 수능 | **college entrance exam** | National university entrance examination taken by Hayeon. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 암초 | **reef** | Reefs blocking the narrow water route. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 중동 | **Middle East** | Region associated with the terrorist group and reported experiments. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |
| 일본 | **Japan** | Country requesting emergency assistance and under Leviathan's attack. |
| 미합중국 | **United States** | Formal Korean reference used during the Defense Minister's imperialist rant. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 진태경 | 마법사 | rescuer assisting the operation | mage; otherwise you | polite emergency imperative | Taekyung orders the exhausted mage to request rescue under his name. |
| 후긴 | 진태경 | Odin Guild messenger to an Ares Guild ally and adversary | Mr. Jin | formal-polite, increasingly coercive | Huginn addresses Jin while questioning his presence and later warns him not to lose his temper. |
| 진태경 | 후긴 | Ares Guild ally to an Odin Guild messenger and adversary | Mr. Crow | insulting-casual and profane | Jin uses the crow nickname while mocking Huginn's theatrics and threatening posture. |
| 미카엘 | 후긴 | Odin Guild Master to personally selected fixer | Huginn | formal, familiar, and commanding | Michael calls Huginn by name while inviting him into the study. |
| 후긴 | 미카엘 | loyal retainer to Guild Master | Guild Master | formal-polite and deferential | Huginn reports the Swiss investigation, accepts Michael's orders, and promises to complete the mission. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 미카엘 | 진태경 | rival_to_target | you | quietly polite but threatening | Michael warns Jin to reconsider for the sake of Jin's monster friend. |
| 진태경 | 미카엘 | target_to_rival | Go fuck yourself | blunt and profane | Jin rejects Michael's proposal to resurrect the World Hunter Federation. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 792
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Huginn.md

# Huginn (후긴)

- **Safe through:** Chapter 788
- **Aliases:** None
- **Role:** Huginn is a powerful Odin Guild messenger, trusted field operative, and elite fixer personally selected and trained by Michael.
- **Personality:** Polished, condescending, calculating, overconfident, and absolutely loyal to his Guild Master.
- **Voice:** Formal and gentlemanly in presentation, indirect and theatrical at first, then blunt and coercive when delivering an ultimatum.
- **Relationships:** Huginn serves Odin Guild's Guild Master with absolute loyalty and acts as an adversary to Jin Taekyung and Choi Minwoo.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 792
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 792
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 792
- **Aliases:** None
- **Role:** Michael Silbert was the former Odin Guild Master, executed by Jin Taekyung after the World Hunter Federation’s first resolution.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 791
- **Aliases:** None
- **Role:** The Prophet is the mysterious leader of the revived Hasasin, a Middle Eastern terrorist organization preparing further attacks against apostates and Western heretics.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors, is revered by the followers, and secretly communicates with Michael Silbert through a magic mirror.

## Korean source

```text
＃793화



전 세계가 눈에 불을 켜고 사방을 이 잡듯이 뒤지는 상황에, 선지자가 수많은 이목이 있는 대도시로 숨어들었을 가능성은 제로에 가깝다.

따라서 본대를 중심으로 중동 전역에 펼쳐진 촘촘한 수색망은 낙후된 지역을 집중적으로 감시하고 있었고, 우리가 곧바로 향한 목적지 역시 마찬가지였다.

도로라고 부르기도 민망할 정도로 거친 길의 좌우에 펼쳐진 황야.

망망대해와도 같은 사막과 암초처럼 군데군데 심어진 작은 숲.

그리고 그곳에, 익숙한 얼굴들이 나를 기다리고 있었다.

“본대에서 오신 분들 맞…… 어?”

청년보다는 소년에 가까운 앳된 얼굴 위로 놀라움이 스친다. 나를 멍하니 바라보던 샤오 쉔이 비명처럼 외쳤다.

“진 선생님!”

“빌어먹을. 저 중국인 꼬마는 왜 저렇게 목청이 큰 거야?”

만일의 사태를 대비하여 최 팀장 대신 동행한 척 헤이글이 한숨을 푹 내쉬며 말을 이었다.

“부탁인데, 저 녀석 좀 어떻게 할 수 없나? 마주칠 때마다 자네 얘기뿐이야. 이제는 귀가 아플 지경이라고.”

“음, 얘가 저를 많이 따르긴 하죠.”

“따르는 것도 정도가 있지. 윌슨도 저 정도는 아니었어.”

“윌슨이 누군데요.”

“우리 집 개. 잠깐 며칠 자리를 비우고 돌아갈 때마다 미친놈처럼 달려들었지. 내가 침입자인 줄 알았나 봐.”

“그 정도면 그냥 윌슨의 성격이 더러웠던 건 아닐까요?”

“삼 년 전에 죽었어. 여름이었지.”

“…….”

시발. 치트키 두 개를 동시에 써 버리다니.

탈룰라와 여름 감성이 합쳐지니 숨이 턱 막힌다. 지금 막 단거리 육상선수처럼 달려온 샤오 쉔이 반갑게 느껴질 정도였다.

“어, 어떻게 진 선생님처럼 누추하신 분이 이 귀한 곳까지!”

“반대야.”

“아.”

석상처럼 굳어 버린 샤오 쉔의 어깨를 두드려 준 나는 주위의 풍경을 훑었다.

확실히 누추한 곳이긴 하다.

온 사방이 찐득찐득한 핏물과 악취로 뒤덮여 있었으니까.

그리고 내가 작은 호수처럼 고여 있는 피 웅덩이를 바라보던 그때, 익숙한 목소리가 귓가를 파고들었다.

“느려 터졌군. 뭐 하다가 이제 와?”

고개를 돌리자 짙은 어둠을 뚫고 걸어오는 누군가의 인영이 보인다.

그 어깨너머로 섬뜩하게 빛나는 몬스터들의 무수한 안광(眼光)과 함께.

스릉.

수행원이라는 명목으로 동행한 수십여 명의 헌터가 반사적으로 무기를 뽑아 들었지만, 가볍게 손을 내저어 그들을 제지한 나는 담담하게 대답했다.

“최대한 빨리 온 거야.”

“오자마자 헛소리군. 못해도 일주일은 기다린 것 같은데.”

“물론 오래 자긴 했지.”

“그래서, 감히 이 몸을 이런 거지 같은 동네에 던져 두고 맘 편히 쉬었나?”

“뭐, 비슷해.”

“제기랄.”

사박. 사박.

투덜거리는 목소리와는 달리, 어느덧 가까워진 얼굴에는 감추지 못한 반가움이 번지고 있다.

나는 일주일 만에 마주한 스켈레톤 킹을 향해 인사를 건넸다.

“아직 살아 있었네.”

“살아 있지. 이미 오래전에 죽은 몸이지만.”

서당 개 삼 년이면 풍월을 읊는다더니.

나는 능숙하게 받아치는 스켈레톤 킹을 보며 피식 웃었다.

녀석의 어깨너머에는 대강 눈대중으로 훑어도 천 마리가 훌쩍 넘어가는 몬스터 군단이 우뚝 서 있었다.

물론 정확히는, 언데드 군단이겠지만.

“보아하니 상황은 대충 마무리된 것 같고. 남은 놈들은?”

“없다. 한 놈도 남김없이 처리했어.”

스켈레톤 킹의 말에 나는 고개를 끄덕였다.

녀석이 그렇다고 하면 그런 거다.

몸 안에 공존하는 두 개의 기운을 조절하여 철저히 정체를 감추고 있던 미카엘 실베르트조차 스켈레톤 킹의 의심을 받은 적이 있다.

비록 그 자신은 원치 않았겠지만, 몬스터인 스켈레톤 킹이야 말로 마력에 관해서는 최고의 전문가라 할 수 있었다.

‘능력도 발군이고.’

무림에서 초절정 고수는 일인군단(一人軍團)이라 불린다.

물론 초절정 고수와는 비교할 수 없으나 현대에서의 S급 헌터가 받는 대접 역시 크게 다르지 않다.

하나같이 평범한 인간이나 헌터와는 궤를 달리하는 초인들.

그러나 그런 이들 속에서도 스켈레톤 킹의 능력은 특출났다.

단신으로 몬스터 군단을 제압하는 것은 어지간한 S급 헌터라면 충분히 할 수 있는 일이지만, 30분도 안 되는 짧은 시간 내에 아무런 사상자도 없이 마무리 짓는 건 아무에게나 가능한 일이 아니었다.

“이게 바로 이몬제몬이라는 건가.”

“이몬제몬? 무슨 소리냐.”

“사자성어 모르냐. 지혜로우신 옛 조상님들께서 전해 주신…….”

“필요 없다. 이 몸은 위대한 미합중국의 시민이니까.”

“내 기억이 잘못된 게 아니라면, 분명히 몇 달 전만 해도 Alligator를 아리가또로 읽었던 것 같은데.”

“일본계 미국인이다.”

“…….”

“곤니찌와.”

진짜 미친 새낀가.

능수능란하게 족보를 갈아 끼우는 스켈레톤 킹을 떨떠름하게 바라봤지만, 딱히 할 말은 없었다.

혼자서 몬스터 웨이브를 막아 냈는데, 욕 보다는 칭찬이라도 해 주는 게 당연한 거니까.

하지만 한숨을 내쉬며 돌아서려던 그 순간. 문득 떠오른 한 가지 의문이 뇌리를 스쳤다.

‘왜 지원 요청을 한 거지?’

스켈레톤 킹은 강자다. 마력이 허락하는 한에서 끝없이 언데드 군단을 만들어 낼 수도 있고, 일신의 무력 자체도 결코 약하지 않다.

그런데 왜?

단지 샤오 쉔을 지키기 위해서?

아니면…….

‘다른 무언가 때문에?’

나는 반쯤 돌아섰던 몸을 틀어 스켈레톤 킹을 바라봤다.

그러한 생각들이 얼굴 위로 고스란히 드러났는지, 녀석 역시 조금 전까지만 해도 볼 수 없던 가라앉은 눈빛으로 나를 응시하고 있었다.

“뭐야?”

“음.”

“뭐냐고.”

잠시 침묵하던 스켈레톤 킹이 대답했다.

“이 몸도 모른다.”

“뭐?”

“무엇의 소행이었는지. 어떻게 그럴 수 있는지 아무리 고민해 봐도 알 수 없었다. 나름대로 찾기 위해 애썼지만, 그것은 이미 흔적도 없이 사라진 후였어.”

“그것이라니. 도대체 무슨 소리…….”

“직접 보면 이 몸의 말을 이해할 수 있을 거다. 너 역시 기억하고 있을 테니까.”

기억이라니. 뭘?

내가 의문에 사로잡힌 그때.

“가져와라.”

쿵. 쿠웅.

스켈레톤 킹의 손짓에 머리가 사라진 세 마리의 언데드 오우거가 육중한 걸음걸이로 다가오더니, 이내 덩치와 어울리지 않는 조심스러운 손길로 손에 든 무언가를 내려놓았다.

그리고 한때 인간이었음이 분명한 스무 구의 시신을 본 순간.

나는 스켈레톤 킹이 했던 말의 의미를 본능적으로 깨달았다.

“……시발.”

악문 잇새 사이로 신음처럼 흘러나온 욕설이 서늘한 사막의 공기와 뒤섞인다.

어느덧 곁으로 다가와 시신들을 확인한 척 헤이글이, 입에 물고 있던 시가를 툭 떨어트렸다.

“Holy Shit.”

아니, 모두가 마찬가지였다.

“이건 도대체…….”

“빌어먹을. 헨리?”

곳곳에서 동시다발적으로 튀어나오는 탄식과 욕설.

아무런 소리도 내지 않는 이들은 그저 경악에 사로잡혔을 뿐이다.

시신들의 상태가 그만큼 처참하게 훼손되어 있어서?

틀렸다.

나도, 그들도 헌터로 살아오며 끔찍한 광경은 수도 없이 보았다.

몬스터의 악취와 짙은 피비린내가 진동하는 전장에서 사지가 날아간 것 따위로는 눈 하나 깜짝하지 않는다.

하지만 그런 이들조차 지금 같은 형태의 죽음은 처음으로 목격했을 것이다.

물론, 나를 비롯한 극소수의 사람들은 제외하고.

“Fuck. 진, 이거 설마.”

“네. 맞아요.”

나는 애써 담담하게 대답했다.

그리고 조금씩 흩어지는 먹구름 사이로 쏟아지는 달빛 아래, 마치 미라처럼 모든 생기(生氣)를 잃고 전신의 뼈와 가죽이 말라붙은 시신들을 바라보며 말을 이었다.

불과 한 달 전, 이름 없는 은거지에서 이와 같은 방식으로 죽음을 맞이했던 누군가를 떠올리며.

“지크프리트 바스만.”

인류에 단 셋밖에 없는. 아니, 없었던 위대한 대마도사 중 하나.

그를 죽인 무언가가, 바로 이 사막에 있었다.

띠링.



* * *



가는 길도, 돌아오는 길도 거리는 같았지만 내게는 비교도 되지 않을 만큼 짧게 느껴졌다.

머릿속을 가득 채운 생각 때문에.

‘도대체 어떻게?’

나뿐만이 아니다. 모두가 확신했다.

지크프리트 바스만을 죽인 것은 미카엘 실베르트라고.

이유? 간단했다.

그는 대마도사다. 그것도 전투 마법에 특화된 워 메이지(War Maje)인 매직 존슨과는 달리, 전형적인 학구파에 속한 대마도사.

매직 존슨이 지크프리트 바스만을 A구역의 설계자로 의심한 것 역시 그래서였다.

그는 마법진을 기반으로 한 각종 결계 마법과 몬스터 연구의 대가였으니까.

그런 뛰어난 마법사가, 그것도 폐쇄적이기까지 한 인물이 자신의 은신처를 대충 방수포로 감싸 놨을 리가 있나.

A구역과 마찬가지로 그의 은신처 역시 온갖 결계로 은폐되어 있었고, 그 수많은 마법을 뚫고 들어갈 만한 강자는 전 세계에서도 손에 꼽는다.

그리고 그 몇 안 되는 강자 중에서도 그를 죽일 마음을 품은 사람은 미카엘 실베르트, 그놈뿐이었고.

하지만…….

‘잘못 짚었어.’

시신들을 본 순간 깨달았다.

내가, 우리가 틀렸다는 사실을.

적어도 지크프리트 바스만이 죽던 그 날, 대마도사의 은신처를 찾아간 사람은 미카엘 실베르트가 아니다.

만약 그의 숨통을 끊은 것이 놈이었다면, 지금 이 순간 내 시야 한 구석을 차지한 저 퀘스트 창 역시 진작 사라졌어야 했을 테니까.



퀘스트



[알 수 없는 죽음]



은둔해 있던 대마도사, 지크프리트 바스만이 알 수 없는 이유로 죽음을 맞이했습니다.

그러나 모든 것에는 원인이 있는 법.

그가 어떻게, 누구에 의해 죽었는지 밝혀 내십시오.



등급 : 초절정

제한 : 진태경

임무 : 죽음에 관한 진실 알아내기 (미완료)

보상 : ???

실패 : ???





시스템은 만능이 아니다.

단지 가야 할 방향만을 넌지시 알려 줄 뿐 목적지까지 얼마나 남았는지, 그 길 중간에 어떤 함정이 있는지는 알려 주지 않는다.

아마도 그래서였을 것이다.

깨어난 직후 여러 시스템 메시지와 퀘스트창을 확인하면서도 이에 대해서는 별다른 이상함을 눈치채지 못한 것은.

그저 미카엘 실베르트에게서 그의 죽음에 관한 완전한 진실을 알아내지 못했으니, 아직까지도 퀘스트가 마무리되지 않고 있다고만 생각했다.

내게 있어 [격변]이라는 메인 퀘스트는 당장 뽑아내야 할 뿌리였고, 그 밖의 모든 것은 단순한 잔가지에 불과했으니까.

그것이 결정적인 패착이었다.

잔가지도, 뿌리도 역할이 다를 뿐 결국 한 몸이다.

뿌리를 타고 오르면 가지에 닿고, 가지를 훑어 내리면 땅속 깊숙한 곳에 숨어 있는 뿌리가 나온다.

아직 드러나지 않았을 뿐.

지금 당장은 숨겨져 있다 해도 언젠가는 찾을 수 있는 것이다.

그리고 그런 의미에서 본대로 귀환한 내가 가장 찾아간 한 사람은, 미카엘 실베르트라는 병든 나무에서 가장 커다란 가지 중 하나였다.

“두 시간 전쯤 사람이 죽었어. 한 명도 아니고, 스무 명.”

자리에 앉자마자 대뜸 건넨 한 마디에, 탁자 너머로 보이는 수척한 얼굴 위로 희미한 미소가 스쳤다.

“성격도 급하군. 손님을 불러놓고 커피 한 잔 정도는 괜찮지 않나?”

커피. 미소. 손님.

나는 바짝 말라붙은 입술을 핥았다.

이상하게도 화는 나지 않는다. 아니, 시작과 동시에 인내심의 한계에 다다랐을지도 모른다.

“한 가지만 물을 테니까 잘 듣고 대답해라, 이 까마귀 새끼야.”

나는 살기에 굳어 버린 후긴을 향해, 오는 길 내내 머릿속을 떠나지 않던 그 생각을 내뱉었다.

“선지자가, 지크프리트 바스만을 죽였나?”
```

## Final English reading copy

```markdown
# Chapter 793

With the whole world tearing the place apart with its eyes peeled, the chances of The Prophet slipping into a major city full of people were close to zero.

So the tight search net spread across the Middle East, centered on the main force, was focused on monitoring underdeveloped areas. The place we headed to right away was no exception.

Wasteland stretched out on either side of a road so rough it was embarrassing to call it one.

A desert as vast as an open sea, dotted here and there with small patches of trees like reefs.

And there, familiar faces were waiting for me.

“You’re with the main force, righ—huh?”

Surprise crossed a face so young he looked more like a boy than a young man. Xiao Shen stared at me, dumbstruck, then shouted as if he were screaming.

“Mr. Jin!”

“Damn it. Why does that Chinese kid have to be so loud?”

Chuck Hagel, who’d come along in Team Leader Choi’s place in case anything happened, let out a deep sigh and continued.

“Do me a favor. Can’t you do something about that kid? Every time we run into each other, all he talks about is you. My ears are about to fall off.”

“Well, he is pretty attached to me.”

“There’s a limit to how attached someone can be. Wilson wasn’t even that bad.”

“Who’s Wilson?”

“My dog. Every time I was away for a few days and came home, he’d come at me like a maniac. Probably thought I was an intruder.”

“Maybe Wilson just had a bad temper?”

“He died three years ago. It was summer.”

“……”

Shit. He’d just pulled out two cheat codes at once.

The combination of the Talullah[^1] moment and summertime sentimentality nearly took my breath away. I was relieved to see Xiao Shen, who’d just run over like a sprinter, if only by comparison.

[^1]: A Korean internet meme about awkwardly backpedaling after unwittingly insulting someone’s loved one.

“H-how could someone as shabby as Mr. Jin come all the way to a place this precious?”

“It’s the other way around.”

“Oh.”

I patted Xiao Shen on the shoulder. He’d frozen like a statue. Then I took in the scenery around us.

It was definitely a shabby place.

Everywhere was covered in sticky blood and filled with a foul stench.

Just as I was looking at a pool of blood the size of a small lake, a familiar voice reached my ears.

“You’re slow as hell. What took you so long?”

I turned around and saw a figure walking out of the darkness.

Over his shoulder shone countless eerie monster eyes.

*Shing.*

Dozens of Hunters accompanying us as our supposed entourage reflexively drew their weapons. I stopped them with a casual wave and answered evenly.

“I got here as fast as I could.”

“Already talking nonsense. I’ve been waiting at least a week.”

“Sure, I did sleep for a long time.”

“So you left this great king in a shithole like this and took your sweet time resting?”

“More or less.”

“Damn it.”

*Scuff. Scuff.*

Despite his grumbling, his face had drawn close, and he couldn’t hide how glad he was to see me.

I greeted the Skeleton King, whom I hadn’t seen in a week.

“You’re still alive.”

“I am. Though I died a long time ago.”

They say a dog that spends three years at a village school will recite poetry.

I gave a quiet laugh at the Skeleton King’s quick retort.

Over his shoulder stood an army of monsters—well over a thousand, even by a rough estimate.

Though, technically, they were an army of the undead.

“Looks like things have mostly wrapped up. What about the rest?”

“There aren’t any. I took care of every last one.”

I nodded at the Skeleton King’s words.

If he said so, then that was that.

Even Michael Silbert, who’d kept his identity completely hidden by controlling the two energies coexisting inside him, had once aroused the Skeleton King’s suspicions.

Whether he wanted it or not, the Skeleton King was the foremost expert on magical power.

*And he’s damn good at it.*

In Murim, a Supreme Peak master is called a one-man army.

An S-rank Hunter in the modern world might not compare to a Supreme Peak master, of course, but they weren’t treated all that differently.

Every one of them was a superhuman, on a different level from ordinary people and Hunters.

Even among such people, the Skeleton King’s abilities stood out.

An S-rank Hunter worth their salt could take down an army of monsters alone. But finishing the job in less than thirty minutes without a single casualty wasn’t something just anyone could do.

“So that’s *i-mon-je-mon*—monsters against monsters.[^2]”

“*I-mon-je-mon*? What are you talking about?”

[^2]: Jin twists a Korean four-character idiom about using one enemy against another, replacing its middle syllables with “monster.”

“You don’t know the old four-character idiom? The one our wise ancestors passed down to us…”

“I don’t need it. I’m a citizen of the great United States of America.”

“If my memory’s right, a few months ago you were reading ‘alligator’ as ‘arigatou.’”

“I’m Japanese American.”

“……”

“Konnichiwa.”

Is this guy insane?

I stared at the Skeleton King, who could swap out his family tree at the drop of a hat, with some bemusement. But I didn’t have much to say. He’d held off a Monster Wave by himself. The least I could do was praise him instead of cursing him out.

But just as I was sighing and turning away, a question suddenly crossed my mind.

*Why had he called for backup?*

The Skeleton King was powerful. As long as his magical power held out, he could create an endless army of the undead, and his own fighting ability was no joke.

So why?

Just to protect Xiao Shen?

Or…

*Was it because of something else?*

I turned back to face the Skeleton King, halfway through turning away.

Maybe those thoughts showed plainly on my face. He was watching me, too, with a somber look I hadn’t seen on him a moment ago.

“What?”

“Hmm.”

“What is it?”

After a brief silence, the Skeleton King answered.

“Even this great king doesn’t know.”

“What?”

“No matter how much I thought about what did it, or how it could have happened, I couldn’t figure it out. I did my best to look for it, but it had already disappeared without a trace.”

“What do you mean, ‘it’? What the hell are you talking ab—”

“You’ll understand when you see for yourself. You’ll remember it, too.”

Remember what?

As I struggled to make sense of that—

“Bring them here.”

*Thud. Thud.*

At the Skeleton King’s gesture, three undead ogres with their heads missing approached with heavy steps. Then, with hands surprisingly careful for their size, they lowered what they were carrying.

And the moment I saw the twenty bodies—bodies that had clearly once belonged to humans—I instinctively understood what the Skeleton King had meant.

“……Shit.”

The curse slipped through my clenched teeth like a groan, mixing with the cool desert air.

Chuck Hagel had come over to inspect the bodies. The cigar in his mouth fell to the ground.

“Holy shit.”

And he wasn’t the only one.

“What the hell is this…?”

“Damn it. Henry?”

Sighs and curses erupted all around us at once.

Those who made no sound were simply struck dumb with horror.

Was it because the bodies had been so horribly mutilated?

No.

I—and the others—had seen countless horrific sights in our lives as Hunters.

On a battlefield reeking of monsters and thick with the stench of blood, losing a limb wasn’t enough to make us bat an eye.

But even people like us had never seen anyone die like this before.

Well, except for a very small handful of people, myself included.

“Fuck. Jin, is this…?”

“Yes. It is.”

I answered as calmly as I could.

Then, beneath the moonlight spilling through the clouds as they slowly broke apart, I looked at the bodies. They’d lost every trace of vitality, like mummies, their bones and skin dried against their frames.

I thought of someone who’d died the same way just a month ago, in an unnamed hideout.

“Siegfried Wassmann.”

One of the three great Grand Mages of humanity—or, rather, one of the three who had been.

Whatever had killed him was here in this desert.

*Ding!*

* * *

The distance was the same going there and coming back, but the return trip felt incomparably shorter.

My head was full of questions.

*How could this have happened?*

I wasn’t the only one. Everyone was certain.

Michael Silbert had killed Siegfried Wassmann.

Why? Simple.

Siegfried Wassmann was a Grand Mage—and unlike Magic Johnson, a War Mage specializing in combat magic, he was a scholar through and through.

That was why Magic Johnson suspected Siegfried Wassmann of being the architect of Area A.

He was a master of all kinds of barrier magic based on magic circles, and an expert on monsters.

Would a mage that skilled—and that reclusive—have just wrapped a tarp around his hideout?

Like Area A, his hideout had been concealed behind all kinds of barriers. Only a handful of people in the entire world were strong enough to break through all those spells.

And among those few, Michael Silbert was the only one who’d wanted him dead.

But…

*We got it wrong.*

The moment I saw the bodies, I realized it.

I—and all of us—had been wrong.

At least on the day Siegfried Wassmann died, it wasn’t Michael Silbert who’d gone to the Grand Mage’s hideout.

If he’d been the one to finish him off, the Quest window taking up a corner of my vision right now should have disappeared long ago.



> **System**
>
> **Quest**
>
> **An Unknown Death**
>
> The reclusive Grand Mage, Siegfried Wassmann, has died for unknown reasons.
>
> But everything has a cause.
>
> Discover how he died and who killed him.
>
> **Grade:** Supreme Peak
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Discover the truth behind his death (Incomplete)
>
> **Reward:** ???
>
> **Failure:** ???



The System wasn’t all-powerful.

It only pointed you vaguely in the right direction. It didn’t tell you how far you were from your destination or what traps lay along the way.

That was probably why, even after checking all the System messages and Quest windows when I woke up, I hadn’t noticed anything strange about this one.

I’d simply assumed the Quest hadn’t been completed because I hadn’t learned the full truth about his death from Michael Silbert.

To me, the Cataclysm Main Quest was the root I needed to pull out right away. Everything else was just a branch.

That was my crucial mistake.

Branches and roots had different jobs, but they were still part of the same tree.

Follow the root upward and you’d reach the branches. Trace a branch downward and you’d find the root hidden deep underground.

It just hadn’t come to light yet.

Even if something was hidden for now, sooner or later I could find it.

And in that sense, the first person I went to see after returning to the main force was one of the largest branches on the sick tree that was Michael Silbert.

“Someone died about two hours ago. Not just one person—twenty.”

At the words I blurted out as soon as I sat down, a faint smile crossed the gaunt face across the table.

“You’re in a hurry. Can’t a guest have a cup of coffee first?”

Coffee. A smile. A guest.

I licked my parched lips.

Strangely, I wasn’t angry. No—maybe my patience had been running out from the very start.

“I’m going to ask you one thing, so listen carefully and answer, you crow bastard.”

I spoke to Huginn, frozen by my killing intent, and let out the question that hadn’t left my mind all the way back.

“Did The Prophet kill Siegfried Wassmann?”
```
