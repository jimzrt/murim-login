<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0786.txt",
      "sha256": "491e1a8cad2444b32c732495461a037fc5ba4544b7b62536d5ae289980d69d5d",
      "bytes": 18413
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "4b55764a3d4256cd2a67f76da5915587c969622cf0d70366a652ee0344590e40",
      "bytes": 661
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "47349c578ce3a378dc53173dec4002c0828b8095d08eadab83cdfaafdabfc433",
      "bytes": 223666
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "523824d72c0ec04d4e6b8f9217150791ff499cc794f6128c621be096a988f801",
      "bytes": 553
    },
    {
      "path": "characters/Felix.md",
      "sha256": "2d3c21e9d04c15a616153b39e5f0d4e3a08bf1822756a4feb43fd50faa506ffd",
      "bytes": 464
    },
    {
      "path": "characters/Huginn.md",
      "sha256": "60f4cfa8a822e9290d7889aa5d22b450ee929216fe233bd75714e07794c3a1ce",
      "bytes": 674
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "6c4f3c2bf30869f2460b477a2319b05dec1a10cb4846c92a618c82c7a6ae9873",
      "bytes": 2112
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "3ab6f51f600d2ddf5a5e5ca695bd022f661e8383988ae90a0b13e208c55b1fd3",
      "bytes": 622
    },
    {
      "path": "characters/Michael.md",
      "sha256": "81335fda13db3faa01086801bbf1b58b0de63b205949297374db2763c22d976f",
      "bytes": 841
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8d63f3850c1cfa0b4c1a97bd8a0f2335b332e89b0faa0c9cbde758a67674220c",
      "bytes": 243642
    }
  ],
  "estimated_tokens": 12609
}
-->

# Durable State Update — Chapter 786

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 786. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 786. Profile updates may replace only one
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
  "chapter": 786,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 786,
    "continuity_sources": [786],
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
    "Michael Silbert is defeated and dying; his transformation and regeneration are gone after exhausting his magical power.",
    "Jin Taekyung is gravely injured but still standing after the clash.",
    "Magic Johnson shielded the National Assembly and the surrounding area with Absolute Shield.",
    "Stone King has appeared behind Jin; Michael's missing horn pierced Stone King's palm."
  ],
  "continuity_sources": [
    785
  ],
  "open_questions": [
    "Will Michael die, and what will Stone King do?"
  ],
  "safe_through": 785,
  "temporary_decisions": [
    "Keep magical power distinct from mana."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 살기     | **killing intent**                               |                                                       |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 귀가      | **your family**                                                 |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 필릭스 | **Felix** | British prince and S-rank Hunter. |
| 후긴 | **Huginn** | One of the two ravens associated with Odin in Norse mythology. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 평화 | **Peace Guild** | Guild name. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 뮌헨 | **Munich** | Second word in one of the necromantic chants. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 골골이 | **Bones** | Jin’s familiar nickname for the Skeleton Warlord and its new Skeleton King form. |
| 골골 | **Golgoli** | Jin's nickname for the Skeleton King. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 프랑스 | **France** | Country containing Paris and Luxembourg Gardens. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |
| 슈마허 | **Schumacher** | Surname of Germany's S-rank Hunter Joel Schumacher. |
| 위버 | **Über** | Name used when Jin addresses the Skeleton King. |
| 위버멘쉬 | **Übermensch** | Title used by the German Hunters for Jin Taekyung. |
| 조엘 | **Joel** | Given name of Joel Schumacher. |
| 서울 | **Seoul** | Location announced for the World Hunter Federation's inaugural ceremony. |
| 한국 | **Korea** | Destination of the international Hunters and Guild Masters. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 골골 | captor_to_subordinate_undead | Bones | mocking-casual | Jin uses the mocking nickname while treating the Skeleton Warlord like a pet. |
| 진태경 | 필릭스 | Korean S-rank Hunter addressing a British prince | His Highness | mock-formal and sarcastic | Felix demands formal address, and Jin complies by calling him His Highness while continuing to mock him. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 필릭스 | 진태경 | British prince and S-rank Hunter to allied Korean S-rank Hunter | Jin | lofty and aristocratic | Felix addresses Jin while discussing royal duty and their teleport. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 골골 | 진태경 | subordinate_undead_to_captor_and_master | human | mocking, reluctant, and familiar | Calls Jin 인간 and 간악한 인간 while complaining about being deceived into searching Area A. |
| 후긴 | 진태경 | Odin Guild messenger to an Ares Guild ally and adversary | Mr. Jin | formal-polite, increasingly coercive | Huginn addresses Jin while questioning his presence and later warns him not to lose his temper. |
| 진태경 | 후긴 | Ares Guild ally to an Odin Guild messenger and adversary | Mr. Crow | insulting-casual and profane | Jin uses the crow nickname while mocking Huginn's theatrics and threatening posture. |
| 미카엘 | 후긴 | Odin Guild Master to personally selected fixer | Huginn | formal, familiar, and commanding | Michael calls Huginn by name while inviting him into the study. |
| 후긴 | 미카엘 | loyal retainer to Guild Master | Guild Master | formal-polite and deferential | Huginn reports the Swiss investigation, accepts Michael's orders, and promises to complete the mission. |
| 진태경 | 슈마허 | rescuer to endangered allied Hunter | you | casual and blunt | Jin asks Schumacher whether he intends to die after arriving between him and the Minotaur Lord. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 미카엘 | 진태경 | rival_to_target | you | quietly polite but threatening | Michael warns Jin to reconsider for the sake of Jin's monster friend. |
| 진태경 | 미카엘 | target_to_rival | Go fuck yourself | blunt and profane | Jin rejects Michael's proposal to resurrect the World Hunter Federation. |
| 필릭스 | 존슨 | prince_to_allied_grand_mage | Mr. Johnson | formal-polite | Felix uses a respectful address while speaking with Magic Johnson. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 785
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Felix.md

# Felix (필릭스)

- **Safe through:** Chapter 781
- **Aliases:** Prince Felix
- **Role:** British prince and S-rank Hunter who joins the reinforcement force against the Arch Lich.
- **Personality:** Haughty, self-important, and conscious of royal duty.
- **Voice:** Formal, lofty, and aristocratic.
- **Relationships:** Travels with Faye Chen and Magic Johnson and is allied with Jin Taekyung.

### Huginn.md

# Huginn (후긴)

- **Safe through:** Chapter 772
- **Aliases:** None
- **Role:** Huginn is a powerful Odin Guild messenger, trusted field operative, and elite fixer personally selected and trained by Michael.
- **Personality:** Polished, condescending, calculating, overconfident, and absolutely loyal to his Guild Master.
- **Voice:** Formal and gentlemanly in presentation, indirect and theatrical at first, then blunt and coercive when delivering an ultimatum.
- **Relationships:** Huginn serves Odin Guild's Guild Master with absolute loyalty and acts as an adversary to Jin Taekyung and Choi Minwoo.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 785
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, and a publicly recognized S-rank-level Hunter who formally retains an A-rank license, as well as a traveler between Murim and another world resembling the realm of immortals and the Hunter who exposed Michael Silbert's ability to absorb monsters' magical power.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 785
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 785
- **Aliases:** None
- **Role:** Michael Silbert is the defeated former Odin Guild Master, dying after his transformation and regeneration vanished when he exhausted his magical power.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

## Korean source

```text
＃786화



“이 몸의 이름은 스톤 킹이다, 이 끔찍한 괴물아.”

그 한 마디를 씹어뱉듯이 토해 낸 순간, 스켈레톤 킹은 비로소 깨달았다.

오랜 시간 자신을 괴롭히던 문제의 답을 찾아냈음을.

모두가 잠든 밤에도 잠들지 못하고, 모두가 각자의 삶을 살아가는 와중에도 홀로 죽어 있던 나날들.

그리고 몸과 마음을 사슬처럼 옭아맨 한 가지 고민.

나는 누구인가.

아무리 생각해도 해결되지 않았던 그 물음에 대한 답은, 바로 스켈레톤 킹 자신에게 있었다.

‘그래, 그랬구나.’

스켈레톤 킹은 마음속으로 뇌까렸다.

한 사람의 어깨너머로 보이는 새카만 눈동자에, 그의 황금빛 왕관이 토해 내는 광휘가 비치고 있었다.

“너는, 도대체 무엇이 되고 싶었던 것이냐.”

툭 던진 그 물음에 미카엘 실베르트의 눈동자가 파르르 떨렸다.

스켈레톤 킹은 차분한 목소리로 말을 이어갔다.

“한때는 미치도록 궁금했다. 이제는 기억나지 않는 과거를 찾으려 애썼고, 현재의 나를 무엇이라 불러야 할지 몰랐다.”

그래서였다.

어느 날 만난 한 인간을 따라 죽음과 어둠만이 가득했던 숲을 빠져나와, 낯선 세상으로 발을 내디딘 것은.

“너희가 살아가는 이 세상에서 답을 찾고 싶었다. 그럴 수 있을 거라 믿었다.”

하지만 아니었다. 바퀴 달린 거대한 쇳덩이가 굴러가고, 나무보다도 거대한 건물이 빼곡히 늘어선 그곳에조차 그가 찾던 답은 없었다.

결국 답을 찾기 위해 숲을 떠난 스켈레톤 킹에게 있어, 인간들이 살아가는 이 세상 역시 또 다른 숲이었다.

“숨을 쉴 수도 없고, 잠을 잘 수도 없었다. 다른 인간들이 말하는 시원한 바람과 식사의 맛도 느끼지 못한다. 심지어는 아주 작고 희미한 고통마저도.”

처음 알았다.

고통을 느끼지 못하는 것 자체가 고통이 될 수 있다는 사실을. 그리고 어떤 종류의 고통은, 진실 그 자체에 있다는 것을.

몬스터(Monster).

그것이 스켈레톤 킹이 스마트폰을 받게 된 날, 처음으로 인터넷에 검색해 본 단어였다. 인간들의 세상에서 가장 많이 들어 본 말 중 하나이자, 자신과 같은 존재를 지칭하는 단어.

그렇게 그는 의문을 넘어, 지금껏 경험한 적 없는 새로운 감정을 느끼기 시작했다.

그건 괴로움이었다.

본연의 의지와는 상관없이 괴물로 깨어났다는 것에 대한 괴로움.

처음으로 대화와 감정을 나누고 가까워지기 시작한 이들에게 있어, 자신은 그저 괴물에 지나지 않을지도 모른다는 두려움.

“나만큼은 아닐 거라 부정하고 싶었다. 그렇기에 너희와 함께, 너희를 위해 최선을 다해 싸웠다. 그것이 옳은 일이라 믿었으니까.”

그 믿음은 지금까지도 변함없었다.

만약 그렇지 않았다면, 오늘 이 자리에서 스스로를 희생할 생각 역시 품지 않았을 것이다.

스켈레톤 킹은 자신이 아끼는 인간들이, 이 세상보다 먼저 무너지길 원하지 않았다.

인간들은 생각 이상으로 복잡한 생명체들이었다. 몬스터처럼, 혹은 몬스터보다도 더한 끔찍한 분노와 살의(殺意)를 품은 이들도 있었다.

하지만 인간은 동시에 절제와 사랑을 알고 있었다. 그들은 각자의 의지에 따라 생각하고 움직였다.

사소한 분쟁으로 수많은 생명이 죽거나 다치고, 핏덩이에 불과한 어린아이가 길거리에 버려지는 일이 생겨도 그들을 보듬어 안는 것 역시 인간이었다.

그런 이유에서였다.

스켈레톤 킹이 그들과 같은 인간이 되고 싶었던 것은.

괴물이 아닌 한 사람의 이웃으로. 친구로서 한 울타리 안에 받아들여지고 싶었던 것은.

그리고 그것이 불가능하다는 것을 깨닫고 절망했던 것은.

하지만…….

“이제는 아니야.”

스켈레톤 킹은 담담하게 뇌까리며 자신의 손등을 꿰뚫은 뿔을 그러쥐었다.

콰득.

이미 앞서 처참히 꺾이고 부서졌음에도, 서서히 회복해 나가던 누군가의 손아귀가 뿔과 함께 붙잡힌다.

미카엘 실베르트의 악문 잇새로 끓어오르는 듯한 음성이 흘러나왔다.

- 이런다고, 이런다고 한낱 몬스터에 불과한 네놈이 인간이 될 거라 생각……!

“상관없다.”

- 뭐?

“알고 있다. 나는 몬스터이기에 인간이라 불릴 수 없고, 인간들과 함께하기에 몬스터라 부를 없는 존재.”

스켈레톤 킹은 희미하게 웃었다.

“한데, 무엇이 문제란 말이냐. 그것만으로도 충분한 것을.”

- ……!

“끔찍하고도 가엾은 괴물아. 다시 한번 이 몸을 소개하마.”

미카엘 실베르트의 부릅뜬 눈을 바라보며, 스켈레톤 킹은 천천히 말을 이었다.

“나는 검은 숲은 주인이자 모든 언데드의 군주요, 너희 인간을 위해 싸운 이 세상의 영웅이다. 스켈레톤 킹이라 불러도 좋고, 스톤 킹이라 불러도 상관없다. 어떤 이름으로 이 몸을 지칭한다 한들, 그 또한 내 존재의 의미니까. 다만…….”

툭.

문득 들어 올려진 스켈레톤 킹의 손이, 한 사람의 어깨를 짚었다.

“내가 이 세상에서 처음으로 얻은 이름은, 네놈에게 알려 주지 않겠다.”

왜냐하면.

그건 오직 친구만이 부를 수 있는 이름이니까.

“그렇지 않으냐, 진태경. 이 간악한 인간아.”



* * *



무슨 말을 해야 할지 모르겠다.

이제야 정신을 차린 저놈에게 웃을까. 화를 낼까. 아니면 평소처럼 있는 힘껏 뒤통수를 후려쳐 줄까.

나는 마치 말하는 법을 잊어버린 사람처럼, 그렇게 짧지만 깊은 고민에 빠져 있다가 불쑥 입을 열었다.

“골골아, 이 병신 새끼야.”

골골이.

어느 날 마주친 검은 숲의 언데드에게 붙여 준 첫 번째 이름.

평소였으면 그렇게 부르지 말라고 지랄발광을 떨었을 텐데, 오늘만큼은 고분고분한 대답이 돌아왔다.

“인정하마. 이 몸이 병신이었다.”

“…….”

“두 번 다시 의심하지 않으마.”

빌어먹을.

말문이 막혔다. 할 말이 없다. 하지만 어째서인지 답답함은 조금도 들지 않는다.

그냥…… 시원했다.

가슴 한구석을 짓누르던 바위가 사라진 것처럼. 이제야 마지막까지 좁혀지지 않던 녀석과 나 사이의 거리가 사라진 것처럼.

그래, 그거면 된 거다.

나는 후련한 마음을 느끼며 주먹을 뻗었다.

뻑!

내게 머리채를 휘어 잡힌 채, 반쯤 넋이 나간 얼굴로 서 있던 미카엘 실베르트의 면상이 뒤로 젖혀진다.

하지만 나는 놈이 쓰러지는 것조차 허락하지 않았다.

뻑, 뻑. 우직.

높은 콧대가 주저앉고, 너덜너덜한 입술 사이로 이빨이 우수수 쏟아졌다.

실핏줄이 터져 나간 놈의 눈동자에서 피인지 눈물인지 모를 것들이 뺨을 타고 흘러내릴 때까지.

파르르 경련하던 사지가 힘을 잃고 축 늘어질 때까지.

콰직. 우드득.

쉼 없이 때리고, 부수고, 짓이겼다.

몸을 움직일 때마다, 발과 주먹이 놈을 후려칠 때마다 채 가시지 않은 일섬(一殲)의 여파와 함께 엄청난 격통이 전신을 휩쓸었지만 상관없었다.

만약 누군가가 손목을 붙잡지 않았더라면, 나는 미카엘 실베르트를 그 자리에서 패 죽였을지도 몰랐다.

덥석.

“그만하십시오, 진태경 씨. 아직은 아닙니다.”

피로에 젖은 익숙한 목소리.

무의식중에 고개를 돌린 나는 눈을 깜빡였다. 핏물을 전신에 뒤집어쓴 최 팀장이 그곳에 서 있었다.

아니, 모두가.

“진, 다 끝났어. 드디어…… 다 끝났다고.”

척 헤이글의 부축을 받으며 걸어온 매직 존슨은 힘없이 웃고 있었지만, 운명을 건 전투에서 승리했다는 기쁨은 찾아볼 수 없었다.

한때 전우였던 이들을 죽여야 했던 영웅의 미소는 어둡고 씁쓸했다.

어느덧 내려앉은 적막 속, 내 주위를 에워싼 모든 이들처럼.

“아.”

탄성인지, 신음인지 모를 목소리가 입술 밖으로 흘러나온다.

그제야 고개를 들어 주위를 둘러본 나는 앞서 들었던 말들이 모두 사실임을 깨달았다.

솨아아아.

진한 혈향을 머금은 바람이 불었다.

시선에 닿는 곳마다 주인을 잃은 무기와 시체가 가득했다.

바닥에 고인 피 웅덩이는 신발을 적셨고, 한때 영웅들의 상징이자 세계를 구원했던 거대한 원탁은 산산이 부서져 잔해만이 남아 있었다.

그래. 끝났다.

인류의 운명을 건 첫 전투가.

사명(使命)과 사욕(私慾)의 전투가. 인간과 괴물들의 전투가 끝내 막을 내렸다.

이 안에서도.

그리고, 이곳에서는 보이지 않는 피가 흘렀을 저 밖에서도.

끼이이익. 쿵.

이미 반쯤 부서져 있던 출입문이 육중한 소리를 내며 쓰러진다. 뒤이어 지친 발걸음들이 쓰러진 문을 타 넘었다.

철컥. 철컥.

피에 흠뻑 젖은 갑옷과 무기들.

혈인(血人)이나 다름없는 몰골을 한 이들이 줄지어 들어오는 모습에 살아남은 헌터 중 상당수가 무기에 손을 가져갔지만, 때맞춰 입을 연 최 팀장의 한 마디에 움직임을 멈췄다.

“어떻게 됐습니까?”

선두에 선 두 사람 중 아직 솜털도 가시지 않은 청년이 군인 같은 말투로 대답했다.

“모두 죽이거나 생포했습니다. 후긴이라는 자 때문에 생각했던 것 이상으로 피해가 컸지만…… 평화 및 아레스 길드와 힘을 합쳐 제압한 뒤 주위의 환영 마법을 해제하고 조금 전 한국 정부에 알렸습니다. 아, 여기 계신 슈 선생님께서도 크게 활약하셨고요.”

“두 분 모두 고생하셨습니다. 여러분이 저희를 믿고 도와주시지 않았다면 어려운 싸움이 되었을 겁니다.”

진심이 담긴 최 팀장의 말에, 앞서 청년에게 ‘슈 선생’으로 불린 30대 사내가 고개를 저었다.

“난 그저 위버멘쉬(Übermensch)의 판단과 선택을 믿었을 뿐입니다. 그날 뮌헨에서 본 그의 모습은…… 거짓 없는 초인 그 자체였으니까.”

이쪽을 향하는 사내의 시선에, 나는 그를 향해 고개를 까딱여 가볍게 인사를 건넸다.

그 옆에서 뭔가를 기대하는 눈빛으로 나를 바라보는 청년에게도.

‘조엘 슈마허. 샤오 쉔.’

두 사람은 내게 빚이 있었고, 오늘 그 보답을 이자까지 쳐서 돌려주었다.

아마 다른 이들은 꿈에도 몰랐을 것이다.

뮌헨에서의 부상을 핑계로 발족식 참석을 정중히 거절한 조엘 슈마허가 극비리에 한국으로 입국했다는 것을.

그리고 그런 그와 공안 무력부의 헌터들을 이끌고 온 샤오 쉔이, 만반의 준비를 끝마친 평화 및 아레스 길드의 최정예와 합류했다는 사실도.

나는 문득 며칠 전 최 팀장에게 들었던 질문을 떠올렸다.



‘어느 철두철미한 사람이 있습니다. 진태경 씨는 그의 가장 큰 약점이 드러나는 순간이 언제라고 생각하십니까?’



대답은 어렵지 않았다. 이미 몇 번이나 지켜보았고, 나 스스로도 그와 같은 실수를 범한 적이 있으니까.



‘모든 것이 성공했다고 생각했을 때.’



정답이었다.

어쩌면 미카엘 실베르트는 만약의 상황을 경계하면서도, 한편으로는 자신의 승리를 확신했던 것 같다.

평소의 그였다면 서울 대신 본진이라 할 수 있는 프랑스, 혹은 지지 기반이 확실한 다른 곳을 발족식의 개최지로 택했을 테니까.

하지만 그 작은 방심이, 이 역사적인 장소에서 자신의 이름을 덧칠하고 싶다는 그 알량한 욕심이 놈의 거대한 야망을 무너트렸다.

그리고 지금 이 순간.

나는 똑똑히 들을 수 있었다.

“우리가, 승리했습니다.”

고요해진 공기를 타고 울려 퍼지는 최 팀장의 한 마디와 함께, 산산조각 나듯 허물어지는 누군가의 추악한 야망을.

더불어 내게 남은 일이 무엇인지 깨달았다.

‘……그래.’

모든 것을 끝내기 위해서는, 이 모든 것이 시작된 출발선을 지워야 한다.

오늘 이 자리에서 앞서 다가올 거대한 전쟁에 수많은 걸림돌이 되었을 배신자들을 처단했듯이.

근원이 되는 뿌리를 뽑아야 새로운 잡초가, 이 가시나무의 곁가지들이 자라나지 않을 테니까.

‘미카엘 실베르트.’

우드득.

발치에 쓰러진 놈의 가슴을 짓밟자 뼈가 어긋나는 소리가 울려 퍼진다.

울컥, 솟구친 핏물을 토해 내며 정신을 차린 미카엘 실베르트가 흐릿한 눈빛으로 주위를 훑었다.

- 결국…… 그렇게 됐나.

꺼질 듯한 목소리와는 달리 침착한 어조.

아마도 주위를 확인한 순간 본능적으로 직감했을 것이다.

오른팔이나 다름없는 후긴과 그가 긴 세월 공들여 양성한 친위대는 이곳에 영영 올 수 없게 되었다는 것을.

- 모두 죽였나?

나는 담담하게 대꾸했다.

“죽을 놈은 죽고, 살 놈은 살았지.”

- 후긴은 후자겠군. 알아낼 것이 많은 친구니까.

“잘 알고 있네.”

- 그럼 부탁 하나 하지.

부탁이라.

별것도 아닌 그 단어에, 불현듯 기분이 더러워진 나는 놈의 얼굴을 걷어찼다.

퍽.

홱 돌아가는 고개와 함께 흩뿌려지는 핏줄기.

하지만 이제는 고통조차 느껴지지 않는지, 신음 하나 없이 입안에 가득 찬 핏물을 뱉어 낸 미카엘 실베르트는 꿋꿋이 말을 이었다.

- 후긴에게 전해 주게. 지금까지 고마웠고, 더 이상은 충성하지 않아도 된다고. 자네가 이 부탁을 들어준다면 피차 편해질 걸세. 적어도 너저분하고 지루한 고문과 심문쯤은 생략할 수 있을 테니까.

“그건 평생 충성한 수하를 위한 배려냐, 아니면 마지막 유언(遺言)이냐?”

- 둘 다가 되겠지. 지금 자네 눈빛을 보아하니, 잠시 후면 이 자리가 내 무덤이 될 것 같거든.

나는 소리 없이 웃고 있는 미카엘 실베르트를 말없이 내려다보았다.

그리고 다시 한번 확신했다.

놈을 처단하는 것에 있어, 단 한 줌의 여지조차 남겨선 안 된다는 것을.

법? 재판?

그 제도들은 인간을 위해 만들어진 것이지. 괴물을 위한 것이 아니다.

괴물은 괴물답게 죽어야 한다.

더는 발버둥 칠 수조차 없도록. 놈이 지난 수십 년간 이 땅에 심어 놓은 종양들이 저 괴물을 구명할 아주 자그마한 가능성조차 사라지도록.

그러나 동시에 이것은 적법한 심판(審判)이다.

모든 진실을 지켜보고, 피 흘리며 싸운 이 자리의 모두가 증인이자 배심원이요, 검사이자 판사니까.

그리고 지금 이 순간부터, 그들과 나는 비로소 ‘우리’가 된다.

인종. 성별. 나이와 국경.

심지어 종족마저 초월하여 하나의 깃발 아래에 설 것이다.

세계 헌터 연맹이라는 이름으로.

“미카엘 실베르트.”

문득 입술 사이로 흘러나온 목소리가 적막을 깨트린다. 공력을 싣지 않았음에도 목소리는 공간을 메우며 퍼져나갔다.

넓고 또렷하게, 계속해서.

“지금 이 순간을 기하여, 세계 헌터 연맹은 네게 주어진 모든 자격을 박탈하고 배신자를 즉결처분한다. 누구든 이의가 있다면 앞으로 나서라.”

그 순간, 최 팀장이 대답했다.

“없습니다.”

뒤이어 매직 존슨이 대답했다.

“모든 것은 규율대로.”

필릭스 왕자는 대답 대신 기품 있게 고개를 숙였고, 파이 첸과 척 헤이글은 손에 들고 있던 각자의 무기를 부딪쳤다.

카앙!

처참한 폐허 너머로 깊은 울림이 뻗어 나간다.

흐르는 시간 속. 어느덧 하나에서 수십, 수십에서 수백으로 불어난 병장기가 시퍼런 불똥을 토해 냈다.

어떤 이는 하나밖에 남지 않은 손으로 갑옷을 두드렸고, 백발 성성한 원로는 피 묻은 지팡이로 지면을 찍었다.

쿵. 쿵. 쿵쿵쿵.

세상이 뒤흔들렸다. 고여 있던 핏물이 사방으로 튀었다.

누구도 이의를 제기하지 않았고, 모두가 동의했다.

세계 헌터 연맹의 첫 번째 결의안에.

인간으로 태어나 괴물이 되어 버린 배신자의 죽음에.

그리고 끊임없이 울려 퍼지는 깊은 울림 속, 나는 미카엘 실베르트를 응시하며 물었다.

“이의 있나?”

잠시 침묵하던 놈이 대답했다.

- 없네. 처음에는 살기 위해, 그 후에는 갖기 위해 있는 힘껏 발버둥 쳤을 뿐이야.

“마지막으로 남길 말은?”

- 이제 자네 차례야. 어디 한 번 있는 힘껏 발버둥 쳐 보게. 나는 저 위에서 내려다보고 있을 테니.

비웃음 섞인 그 말을 들으며, 나는 그 어느 때보다 무겁게 느껴지는 창대를 들어 올렸다.

그리고 수백 쌍의 눈동자가 지켜보는 앞에서, 힘차게 창날을 내리꽂았다.

푸욱!

정확히 목젖을 가르며 파고든 창날.

크륵, 입 밖으로 흘러나오지 못한 신음과 함께 미카엘 실베르트의 전신이 덜컥 굳었다.

나는 빠르게 생명이 빠져나가는 괴물의 눈동자를 바라보다, 잠시 미뤄 두었던 마지막 한 마디를 건넸다.

“당신 말대로 똑똑히 지켜봐. 위가 아니라, 저 발아래 밑바닥에서.”

- ……!

마지막 순간 부릅뜬 눈동자는 분노 때문일까. 아니면 더는 막을 수 없는 죽음 때문일까.

어쩌면, 둘 다였을 것이다.

띠링. 띠링. 띠링.

무수한 종소리와 광휘가 내 안에서 샘솟았다.
```

## Final English reading copy

```markdown
# Chapter 786

“My name is Stone King, you hideous monster.”

The moment he spat out those words as if biting them off, the Skeleton King finally understood.

He had found the answer to the question that had tormented him for so long.

The days when he couldn’t sleep even as everyone else slept, when he was alone in death while everyone else lived their own lives.

And the one question that bound his body and mind like chains.

*Who am I?*

No matter how hard he’d thought about it, he’d never found an answer. But the answer had been there all along, within the Skeleton King himself.

*So that’s how it was.*

The Skeleton King muttered to himself.

In the black eyes he saw over a man’s shoulder, the radiance cast by his golden crown was reflected.

“What, exactly, did you want to become?”

At that offhand question, Michael Silbert’s eyes trembled.

The Skeleton King continued in a calm voice.

“There was a time when I was desperate to know. I tried to find a past I can no longer remember, and I didn’t know what to call who I am now.”

That was why.

One day, he had followed a human he met out of a forest filled with nothing but death and darkness, and set foot in an unfamiliar world.

“I wanted to find the answer in the world you live in. I believed I could.”

But he couldn’t. Even there, amid enormous metal boxes on wheels and buildings that towered higher than trees, the answer he sought was nowhere to be found.

To the Skeleton King, who had left the forest to find an answer, the world inhabited by humans was simply another forest.

“I can’t breathe or sleep. I can’t feel what other humans call the cool breeze or the taste of food. I can’t even feel the faintest, smallest pain.”

He learned for the first time.

That the inability to feel pain could itself be painful. And that some kinds of pain lay in the truth itself.

*Monster.*

That was the first word the Skeleton King had searched online the day he got a smartphone. It was one of the words he’d heard most often in the human world, and the word used to describe a being like him.

And so, his questions gave way to a new emotion, one he’d never experienced before.

It was anguish.

Anguish over having awakened as a monster against his own will.

Fear that to the people with whom he’d first begun to share conversations and feelings, and grow close, he might be nothing more than a monster.

“I wanted to deny that I was like them. So I fought alongside you, and for you, with everything I had. Because I believed it was the right thing to do.”

That belief hadn’t changed, even now.

If it had, he wouldn’t have considered sacrificing himself here today.

The Skeleton King didn’t want the humans he cared about to fall before the world did.

Humans were more complicated creatures than he’d ever imagined. Some harbored hideous rage and killing intent, just like monsters—or worse than monsters.

But humans also knew restraint and love. They thought and acted according to their own will.

When countless lives were lost or injured over petty disputes, when children no bigger than infants were abandoned in the street, humans were also the ones who took them in and embraced them.

That was why.

The Skeleton King had wanted to become a human like them.

Not a monster, but a neighbor. A friend accepted into the same community.

And it was why he’d despaired when he realized that was impossible.

But…

“Not anymore.”

The Skeleton King murmured calmly and gripped the horn piercing the back of his hand.

*Crack.*

He caught the hand gripping the horn as well—a hand that had been horribly bent and broken earlier but was slowly healing.

A voice that sounded as if it were boiling over slipped between Michael Silbert’s clenched teeth.

“You think, you think a mere monster like you can become human just by doing this…?”

“It doesn’t matter.”

“What?”

“I know. I’m a monster, so I can’t be called human. And because I live among humans, I can’t be called a monster.”

The Skeleton King smiled faintly.

“So what’s the problem? That’s enough for me.”

“……!”

“You wretched, pitiful monster. Let me introduce myself once more.”

Looking into Michael Silbert’s wide eyes, the Skeleton King spoke slowly.

“I am the master of the Black Forest, the ruler of all the undead, and a hero of this world who fought for you humans. You can call me the Skeleton King or the Stone King. Whatever name you use for me, it’s part of who I am. But…”

*Tap.*

The Skeleton King’s hand rose and came to rest on a man’s shoulder.

“I won’t tell you the first name I ever received in this world.”

Because…

It was a name only a friend could use.

“Isn’t that right, Jin Taekyung? You conniving human.”


* * *


I didn’t know what to say.

Should I laugh at the bastard, now that he’d finally come to his senses? Get angry? Or smack him upside the head as hard as I could, like I usually did?

Like someone who’d forgotten how to speak, I sank into a brief but deep debate before suddenly opening my mouth.

“Golgoli, you stupid son of a bitch.”

Bones.

The first name I’d given the undead of the Black Forest when we met.

Usually, he’d have thrown a fit and told me not to call him that. But today, he answered meekly.

“I admit it. I was a stupid son of a bitch.”

“……”

“I won’t doubt you again.”

Damn it.

I was speechless. I had nothing to say. But for some reason, I didn’t feel the least bit frustrated.

I just… felt relieved.

Like a stone weighing on my chest had disappeared. Like the distance between me and the guy—the distance that had never quite closed until now—had finally vanished.

Yeah. That was enough.

Feeling lighter, I threw a punch.

*Thwack!*

Michael Silbert’s face, slack with shock as I held him by the hair, snapped back.

But I wouldn’t even let him fall.

*Thwack, thwack. Crack.*

His proud nose caved in. Teeth poured out through his mangled lips.

Blood or tears streamed down his cheeks from eyes veined with burst capillaries.

His limbs, twitching in spasms, went limp.

*Crack. Crunch.*

I kept hitting him, breaking him, crushing him.

Every time I moved, every time my fists and feet slammed into him, the lingering aftermath of One Annihilation sent excruciating pain through my whole body. But I didn’t care.

If someone hadn’t grabbed my wrist, I might have beaten Michael Silbert to death right there.

*Grab.*

“Please stop, Mr. Jin. Not yet.”

A familiar voice, worn with exhaustion.

I turned my head without thinking and blinked. Team Leader Choi stood there, drenched from head to toe in blood.

No—all of them did.

“Jin, it’s over. It’s finally… finally over.”

Magic Johnson walked over with Chuck Hagel supporting him. He smiled weakly, but there was no joy in his expression at having won the battle that had decided their fate.

The hero’s smile, after having to kill people who’d once been his comrades, was dark and bitter.

Just like the silence that had settled over us, and everyone surrounding me.

“Oh.”

A sound escaped my lips, neither quite a gasp nor a groan.

Only then did I lift my head and look around. I realized that everything I’d been told was true.

*Whoooosh.*

A wind heavy with the smell of blood swept past.

Everywhere I looked, weapons without owners and bodies lay scattered.

Pools of blood on the floor soaked our shoes. The enormous Round Table, once a symbol of the heroes who had saved the world, had been shattered, leaving only ruins behind.

Yeah. It was over.

The first battle for humanity’s fate.

The battle between duty and self-interest. The battle between humans and monsters had finally come to an end.

In here.

And out there, where blood had been spilled beyond our sight.

*Eeeeeek. Boom.*

The entrance, already half broken, fell with a heavy crash. Tired footsteps followed, stepping over the fallen door.

*Clank. Clank.*

Armor and weapons soaked in blood.

At the sight of those figures filing in, looking no different from people drenched in gore, quite a few of the surviving Hunters reached for their weapons. But they stopped at Team Leader Choi’s timely question.

“How did it go?”

One of the two people at the front—a young man who still had peach fuzz on his face—answered in a military tone.

“We killed or captured them all. We took more casualties than expected because of a man named Huginn, but we joined forces with the Peace and Ares Guilds and subdued him. Then we dispelled the illusion magic surrounding the area and informed the Korean government a little while ago. Oh, and Mr. Shu here played a major role, too.”

“You’ve both worked hard. It would have been a difficult fight if you hadn’t trusted us and helped.”

At Team Leader Choi’s heartfelt words, the man in his thirties whom the young man had called “Mr. Shu” shook his head.

“I simply trusted the Übermensch’s judgment and choices. The man I saw in Munich that day was… a superhuman in every sense of the word.”

When the man looked my way, I gave him a slight nod in greeting.

And I did the same for the young man beside him, who watched me with an expectant look.

*Joel Schumacher. Xiao Shen.*

They owed me, and today they’d paid me back with interest.

The others probably had no idea that Joel Schumacher, who’d politely declined the invitation to the inaugural ceremony on the grounds of his injuries in Munich, had secretly entered Korea.

Or that Xiao Shen had brought the Hunters from the Public Security Ministry’s armed forces with him, and joined up with the elite forces of the Peace and Ares Guilds, who had finished making all the preparations.

I suddenly remembered a question Team Leader Choi had asked me a few days ago.

*“There’s a very thorough person. When do you think his greatest weakness is exposed, Mr. Jin?”*

The answer wasn’t hard. I’d seen it happen several times, and I’d made the same mistake myself.

*“When he thinks everything has gone according to plan.”*

The answer was right.

Perhaps Michael Silbert had been on guard against the possibility of something going wrong, but at the same time, he’d been certain of his victory.

If he’d been acting like himself, he would have chosen France—his stronghold—or somewhere else with a firm support base, instead of Seoul, for the inaugural ceremony.

But that little lapse, that petty desire to put his name on this historic place, had brought down his grand ambition.

And now, at this very moment—

I could hear it clearly.

“We’ve won.”

Along with Team Leader Choi’s words, echoing through the silent air, someone’s hideous ambition crumbled to pieces.

And I realized what I still had to do.

*…Yeah.*

To end everything, I had to erase the starting line where it all began.

Just as we had executed the traitors here today, the people who would have stood in the way of the great war to come.

I had to pull out the root. Otherwise, new weeds—and offshoots of this thorn tree—would keep growing.

*Michael Silbert.*

*Crack.*

I stomped on the chest of the man collapsed at my feet. The sound of bone shifting rang out.

Michael Silbert came to with a rush of blood spilling from his mouth and looked around with bleary eyes.

“So… it ended like this.”

His voice was fading, but his tone was composed.

He had probably realized it instinctively the moment he looked around.

That Huginn, his right-hand man, and the private army he had spent so many years training would never make it here.

“Did you kill them all?”

I answered evenly.

“The ones who were going to die died. The ones who were going to live lived.”

“Huginn must be one of the latter. He’s a useful man to question.”

“You know it.”

“Then I have a favor to ask.”

A favor.

At that unremarkable word, I suddenly felt disgusted and kicked him in the face.

*Thwack.*

His head snapped to the side, blood spraying through the air.

But maybe he couldn’t feel pain anymore. Without so much as a groan, Michael Silbert spat the blood filling his mouth and stubbornly continued.

“Tell Huginn this for me. I’m grateful for everything he’s done, and he doesn’t have to serve me anymore. If you do me this favor, we’ll both be better off. At least you can skip the unpleasant, tedious torture and interrogation.”

“Is that a kindness for a retainer who’s been loyal his whole life, or your last words?”

“Both, I suppose. Judging by your eyes, this is about to become my grave.”

I silently looked down at Michael Silbert, smiling without a sound.

And I was certain once more.

I couldn’t leave so much as the slightest opening when it came to executing him.

The law? A trial?

Those institutions were made for humans, not monsters.

Monsters should die like monsters.

So they could never struggle again. So that even the tiniest chance of the tumors he’d planted in this land over the past several decades saving that monster would disappear.

And yet, this was a lawful judgment.

Everyone here had witnessed the truth and fought through the bloodshed. They were witnesses and jurors, prosecutors and judges.

And from this moment on, they and I would finally become *us*.

Race. Sex. Age and borders.

We would stand together beneath one flag, even surpassing species.

In the name of the World Hunter Federation.

“Michael Silbert.”

My voice slipped between my lips, breaking the silence. I wasn’t channeling any internal energy, yet it filled the space and spread.

Loudly and clearly. On and on.

“From this moment forward, the World Hunter Federation revokes all your qualifications and summarily executes you as a traitor. Anyone who objects, step forward.”

Team Leader Choi answered at once.

“No objections.”

Magic Johnson followed.

“Everything according to the rules.”

Prince Felix bowed with dignity instead of answering, while Pai Chen and Chuck Hagel struck their weapons together.

*Clang!*

A deep resonance rang out beyond the devastated ruins.

As time passed, the weapons grew from one to dozens, then from dozens to hundreds, sending blue sparks flying.

One person pounded his armor with the only hand he had left. A white-haired elder struck the ground with his bloodied cane.

*Boom. Boom. Boom-boom-boom.*

The world shook. Pooled blood splashed in every direction.

No one objected. Everyone agreed.

To the World Hunter Federation’s first resolution.

To the death of a traitor born human and turned into a monster.

Amid the deep resonance that rang on and on, I stared at Michael Silbert and asked,

“Any objections?”

After a brief silence, he answered.

“None. At first, I fought with all my strength to survive. After that, I fought to get what I wanted.”

“Any last words?”

“It’s your turn now. Go on, struggle with everything you have. I’ll be watching from up there.”

As I listened to his mocking words, I lifted my spear. It felt heavier than ever before.

Then, in front of hundreds of pairs of eyes, I drove the spearhead down with all my strength.

*Thrust!*

The spearhead pierced straight through his throat.

With a choking sound that never made it out of his mouth, Michael Silbert’s body stiffened.

I looked into the monster’s eyes as life quickly drained away, then delivered the last words I’d put off until now.

“Just like you said, watch closely. Not from up above—from the very bottom, beneath my feet.”

“……!”

Did his eyes widen in anger at the last moment? Or because he could no longer stave off death?

Perhaps it was both.

*Ding. Ding. Ding.*

Countless chimes and radiance welled up inside me.
```
