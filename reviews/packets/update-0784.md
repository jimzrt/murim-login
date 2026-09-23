<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0784.txt",
      "sha256": "3e6d39d9682422ba011d6530d09385bb7560200343bbf339b51a736e1cc69001",
      "bytes": 13071
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "c9f3e471d7bebac6e59ce0d790c9d02c5af24d66de60737ff796e21373aa3f6a",
      "bytes": 498
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "47349c578ce3a378dc53173dec4002c0828b8095d08eadab83cdfaafdabfc433",
      "bytes": 223666
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "c7059d997def448c7982e1fcd52798f47d645afcf380ecc0eeadd26f9f40a704",
      "bytes": 817
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "4ac449a146238afdaf20588b9b4b0dd08d57c309b64127c466c313bb70996a09",
      "bytes": 2112
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "35b0b0c18e2ca869f556cd022ff8bb3dfa37db2a3fa0fb8a8e257ee8680ec094",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "ac358fbd06207505e5f9936c76ad4a058f817d96bbc68d81a8c8e1e494f0ae20",
      "bytes": 1384
    },
    {
      "path": "characters/Michael.md",
      "sha256": "f4cb3b7e466fd5a6a81a9b0ef1d5801f9fcb8055d37c8d4ac549c0f75b9c7bba",
      "bytes": 846
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8db9e79ef5ea3bb4279d4c11d5c9e6e23a49de5f2010abaf0bfb116c09d99a97",
      "bytes": 243344
    }
  ],
  "estimated_tokens": 10145
}
-->

# Durable State Update — Chapter 784

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 784. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 784. Profile updates may replace only one
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
  "chapter": 784,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 784,
    "continuity_sources": [784],
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
    "Michael Silbert is badly wounded in a crater after Jin Taekyung’s attacks; Jin has raised White Flame’s spearhead, but Michael’s fate is not shown.",
    "Other fighters are still battling nearby."
  ],
  "continuity_sources": [
    783
  ],
  "open_questions": [
    "What happens to Michael after Jin raises White Flame’s spearhead?"
  ],
  "safe_through": 783,
  "temporary_decisions": [
    "Keep magical power distinct from mana."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 이정룡    | **Lee Jungryong** |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 대격변     | **Great Cataclysm**   |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 용족 | **dragonkin** | Monster classification including wyverns and drakes. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 지풍 | **Finger Qi** | Invisible qi attack fired by the Western Heaven Demon Lord. |
| 화룡갑 | **Fire Dragon Armor** | Jin Taekyung's renamed bound armor, formerly the Black Dragon Armor. |
| 브레스 | **Breath** | Dragonkin power used by the Wyverns. |
| 황하 | **Yellow River** | River along which civilization began. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 국회의사당 | **National Assembly** | Government building visible from the skyscraper. |
| 정룡 | **Jungryong** | Cheon Taemin's trusted associate who joined the Peace Guild. |
| 재생 | **Regeneration** | The masked man's rapid recovery from shattered bones and severe wounds. |
| 파리 | **Paris** | The city containing Ares Guild's branch attacked at the chapter's end. |
| 브라질 | **Brazil** | Country containing Rio de Janeiro. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |
| 페르난두 | **Fernando** | One of Michael’s former supporters. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 이정룡 | 고준 | Master to Disciple | Go Jun | familiar and testing | Lee switches from Seok's office title to his personal name while considering whether he can defeat Taekyung. |
| 고준 | 이정룡 | Disciple to Master | Master | deferential | Go Jun responds to Lee's personal-name address as 스승님. |
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 고준 | 진태경 | Ares Guild combatant confronting the killer of his Master | you | hostile and informal | Go Jun uses 너 while demanding Jin confess to Lee Jungryong's death and threatening retaliation. |
| 진태경 | 고준 | dominant adversary confronting Lee Jungryong's Disciple | you | contemptuous and informal | Jin uses 너 and 놈 while overpowering Go Jun and ordering him to end the conflict with Lee Jungryong. |
| 기자 | 진태경 | Japanese reporter to celebrated foreign Hunter | Jin-sama | formal and reverent | Japanese reporters repeatedly address Jin with the honorific 사마. |
| 진태경 | 기자 | Hunter to Japanese reporter | reporter; you | blunt and insulting | Jin rebukes a reporter for talking back after criticizing Yamamoto's delayed arrival. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 미카엘 | 진태경 | rival_to_target | you | quietly polite but threatening | Michael warns Jin to reconsider for the sake of Jin's monster friend. |
| 진태경 | 미카엘 | target_to_rival | Go fuck yourself | blunt and profane | Jin rejects Michael's proposal to resurrect the World Hunter Federation. |

## Listed compact profiles

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 777
- **Aliases:** Team Leader Seok
- **Role:** Go Jun was Ares Guild's Vice Guild Master, Lee Jungryong's Disciple and former Head of Security, the de facto successor to Lee's Ares legacy, and a mutated monster who was killed by Jin Taekyung in Area A.
- **Personality:** Disciplined and controlled under ordinary pressure, fiercely loyal to Lee Jungryong, but consumed by humiliation and rage when Ares Guild's authority is challenged.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Go Jun inherited Lee Jungryong's Ares legacy after becoming his Disciple and regarded Jin Taekyung and Choi Minwoo as enemies before his death.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 783
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, and a publicly recognized S-rank-level Hunter who formally retains an A-rank license, as well as a traveler between Murim and another world resembling the realm of immortals and the Hunter who exposed Michael Silbert's ability to absorb monsters' magical power.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 783
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 780
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regarded Cheon Taemin as an older brother despite no blood relation and long held him in respect and fear; secretly supported the orphanage where Lee Dongseok grew up and was regarded by Dongseok as a father; operated as Ares Guild's senior authority beneath its Guild Master; concealed Taemin's condition with Song Cheonwoo and participated in purging aides who knew the truth.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 783
- **Aliases:** None
- **Role:** Michael Silbert is the Odin Guild Master and a public hero who absorbs monsters’ magical power; he is currently badly wounded after fighting Jin Taekyung.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

## Korean source

```text
＃784화



슈확!

희한한 일이었다.

나는 단지 창을 들어 올렸을 뿐인데, 지금 귓가를 파고드는 이 파공성은 어디에서 울려 퍼지는 걸까.

그리고…… 저 병신들은 무슨 자신감으로 내게 달려든 걸까.

찰나를 쪼개고 쪼갠 짧은 시간 속, 나는 돌아섬과 동시에 창날을 내리그었다.

후우웅. 카앙!

창날을 따라 터져 나온 압력에 십여 자루의 비수가 튕겨 나간 그 순간, 양옆으로 들이닥친 두 자루의 검이 내 상, 하체를 동시에 파고들었다.

쉭, 서걱!

불에 덴 것처럼 뜨겁다.

화룡갑의 내구도가 하락했음을 알리는 경고음과 함께 허벅지에서 적지 않은 핏줄기가 솟구친다.

하지만 이 모든 것이 S급 헌터 세 명의 기습을 막아 낸 대가라고 생각한다면 꽤 괜찮은 거래였다.

내가 일방적으로 퍼 준 것이 아닌, 그에 합당한 무언가를 주고받았다면 더더욱.

푸화아악!

뒤늦게 터져 나온 핏물이 지면을 적신다. 가슴이 쩍 갈라진 채 허물어지는 동료의 모습을 확인한 두 중년 남녀가 눈을 부릅떴다.

“도대체 언제……!”

“안 돼, 페르난두!”

워낙 한순간에 벌어진 일이라 상대가 누구인지 확인하는 것까진 무리였는데, 이렇게 마주하고 보니 더없이 익숙한 얼굴들이다.

각각 한 나라를 대표하고, 인류를 상징하는 S급 헌터들.

아니, ‘그랬던’ 자들.

“이게 누구야. 다 아는 사람들이네.”

헛웃음 섞인 내 인사에 중년 남녀가 마른침을 삼켰다.

섣부른 판단으로 내 가슴을 노렸던 브라질의 S급 헌터, 페르난두 루카스는 엄청난 양의 피를 쏟아내면서도 덜덜 떨리는 손으로 포션을 꺼내는 중이었다.

그 모습이 너무나도 필사적이라, 나는 멜로 영화 속 남주인공처럼 따뜻한 목소리로 말을 건넸다.

“그거 마시면, 나한테 뒈지는 거다?”

“……!”

“대신 다 마무리될 때까지 그 상태로 잘 버티고 있으면 치료해 줄게. 교도소도 좋은 곳으로 정해 주고. 자, 그럼 약속.”

페르난두 루카스는 고통조차 잊은 사람처럼 나를 멍하니 바라보았다.

그리고 번개 같은 속도로 손에 들고 있던 포션을 입 안에 쑤셔 넣었다.

그것도 마개도 따지 않은 병 채 그대로.

콰직! 푹!

벌어진 입 안으로 산산이 부서진 유리 조각과 포션 용액이 콸콸 흘러넘친다.

하지만 찢어진 장기도 눈 깜짝할 사이에 회복시키는 최상급 포션이라 할지라도, 이미 죽은 사람을 되살릴 만큼의 효력은 없었다.

“그러게, 마시지 말라니까.”

내 지풍(指風)에 의해 미간이 관통당한 페르난두 루카스의 시신을 보며 작게 중얼거린 그때.

앞서 저세상으로 떠난 그보다는 조금 더 운이 좋고, 훨씬 실력이 뛰어난 두 중년 남녀가 딱딱하게 굳은 얼굴로 입을 열었다.

“꼭…… 이렇게까지 해야겠나?”

“아직 늦지 않았어요, 진. 당신이 멈춘다면 우리도 이만 물러날게요. 굳이 여기서 더 희생을 늘릴 필요는 없잖아요?”

멈추라고? 희생을 더 늘릴 필요가 없어?

순간 말문이 막힌 나는 문득 주위를 둘러봤다.

그리고 지금 이 순간에도 피로 물들어 가는 의사당 내부와 바닥에 쓰러져 벌레처럼 꿈틀거리는 미카엘 실베르트.

마지막으로 그 앞에 선 두 남녀를 차례대로 바라본 뒤 창을 뻗었다.

내가 지금까지 배운 몇 안 되는 교훈 중 하나는, 병신 같은 말에 일일이 대꾸해 줄 필요는 없다는 거다.

쉭!

아무리 무공을 모른다 한들, 상대는 전투라면 이골이 난 S급 헌터들.

흡, 하고 헛숨을 들이키는 소리와 함께 아슬아슬하게 공격을 피해 낸 두 사람이 내 앞뒤로 내려앉았다.

그러나 아무런 예고도 없이 날아든 창날에, 그들의 눈빛은 한없이 무겁게 가라앉아 있었다.

“그래, 이게 대답인가?”

“잠깐. 괜히 자극하지 말아요. 지금은 우선 미카엘을 구하는 것이…….”

남자보다는 여자 쪽이 훨씬 더 영리하게 상황을 파악하고 있었지만, 헛웃음이 나오게 만드는 건 똑같았다.

‘도대체 그동안 무슨 짓을, 얼마나 많이 저질렀길래 이렇게까지 하나.’

분명 나 역시 아무것도 모르던 시절이 있었다.

오직 게이트와 고시원만을 기계처럼 오가던 시절. 헌터로서의 의무감보다는 돈을 벌기 위해 몬스터와 싸우면서도, 헌터가 타락했다는 말을 들으면 은연중 기분이 상했던 시절이.

하지만…… 이제는 너무 많은 것을 알아 버렸다.

그래서 더는 돌이킬 수 없었다.

저들이 얼마나 큰 업적을 쌓았건, 곧 다가올 전쟁에 얼마나 큰 전력이 되건 상관없다.

사회 깊숙이 뿌리내린 이 종양(腫瘍)들을 제거하지 않는다면, 몬스터와 싸우기 이전에 인류가 무너진다.

제2의 이정룡이, 석고준이, 미카엘 실베르트가 눈앞에 있었다.

모든 추악한 진실이 밝혀졌음에도 무기를 거꾸로 든 그 순간부터, 저들은 반드시 잘라 내야 할 종양이었다.

“기회는 이미 줬다. 선택은…… 당신들이 한 거야.”

한때는 동경과 존경의 대상이었던 그들을 향해, 나는 망설임 없이 달려 나갔다.

쐐애애액!



* * *



아이러니한 일이다. 인간을 괴롭게 만드는 것은 고통, 그 자체임에도 정작 죽음 앞에서는 그 고통이 느껴지지 않는다는 것은.

그리고…… 그 무감각이 어떤 끔찍한 고통보다 두렵다는 것은.

‘아.’

미카엘 실베르트는 멍하니 눈을 깜빡였다.

살짝 벌린 입에서는 신음조차 흘러나오지 못한다. 강대한 기운이 쉼 없이 솟구치던 팔과 다리에서는 힘이 빠져나가고 있었고, 몸을 흠뻑 적신 것으로도 모자라 출렁이는 핏물이 무디게 느껴졌다.

‘빌어먹을.’

이렇게 쓰러질 거였다면, 무엇을 위한 인생이었나.

크르륵. 쿨럭.

헛웃음 대신 피거품이 입 안에서 맴돌았다. 마치 쓰러지듯 고개를 옆으로 떨구자, 눈을 부릅뜬 채 굳어 있는 한 사내의 시체가 보였다.

익히 아는 얼굴이다.

페르난두 루카스.

그는 어릴 적부터 브라질 갱단에 소속되어 있던 불량배 출신으로 남미 하층민들의 열렬한 지지를 받았고, 미카엘 실베르트는 지난 십 년간 그에게 여러 가지 ‘호의’를 베풀었다.

물론 대중들이나 법원은 그 ‘호의’를 달리 해석하겠지만.

‘분명 시작은 소소했지.’

그러나 모든 것은 시간이 흐름에 따라 무뎌지고, 반복될수록 눈덩이처럼 불어났다.

강력한 경쟁자를 사고사로 위장해 제거하고, 연줄이 닿은 정치인을 통해 탈세 혐의를 덮어 주고, 브라질 하층민들의 영웅이 남몰래 갱단을 운영하며 막대한 부수입을 올린다는 기사를 준비 중이었던 어느 용감한 기자를 가족과 함께 납치한 적도 있었으니까.

지금 이 순간, 자신을 위해 곳곳에서 피를 흘리며 죽어 가는 다른 이들 역시 마찬가지였다.

‘아니, 나를 위해서가 아니겠지.’

미카엘 실베르트는 알고 있었다.

저들이 싸우는 이유는, 바로 저들 자신을 위해서라는 것을.

이제 와 모든 것을 인정하고 받아들이기에는, 저들이 잃어야 할 것들이 너무나도 많다는 사실을 알기 때문이라는 것을.

결국 그도, 저들도 같은 구덩이 안에 들끓던 오물이었을 뿐이다.

하지만 바로 그 덕분에, 적지 않은 시간 동안 저들의 욕망과 야망을 충족시켜 준 덕분에 미카엘 실베르트는 아주 잠깐의 시간을 벌 수 있었다.

그가 마지막까지 집착했던 인간의 굴레를 벗어던지고, 마왕(魔王)이라는 존재로 거듭날 수 있는 그 귀중한 시간을.

스륵. 촤르륵.

구덩이에 차올랐던 핏물이 파도처럼 출렁였다. 흐릿한 시야 속, 빛살처럼 허공을 가로지른 창날이 한 중년인의 목을 스치는 것이 보였다.

서걱!

철퍽, 쓰러지는 시신과 함께 데굴데굴 굴러온 얼굴과 눈이 마주쳤다.

마치 불에 지진 것처럼 까맣게 타들어 간 단면에서 풍겨 오는 혈향(血香)이, 초콜릿처럼 달콤하게 느껴지는 것은 단순한 착각만은 아닐 것이다.

푸흐흐.

미카엘 실베르트는 작게 웃었다. 비로소 소리 내어 웃을 수 있게 된 그의 오감(五感)이 서서히 또렷해졌다.

빠르게 뛰기 시작하는 심장 박동 소리가 천둥처럼 울려 퍼지는 듯했다.

쿵. 쿵쿵. 쿵쿵쿵!

빠른 템포의 심장 박동과 함께 구덩이에 고였던 핏물이 주인의 몸뚱어리로 몰려든다.

그러나 그 핏물의 색은 전처럼 붉지 않았다.

더 이상 그 누구도 인간의 것이라고 말할 수 없는, 진득하게 빛나는 녹색 핏물.

지금으로부터 삼십여 년 전, 피와 시체가 넘쳐 흐르던 파리에서 마주쳤던 미증유의 괴물이 흘린 그것과 같은 피가 미카엘 실베르트의 전신을 채웠다.

그 끝없는 마력도, 회복력도 함께.

쏴아아악!

핏물이 몸속 깊숙이 빨려 들어간다. 끊어진 근육이 이어지고, 부러진 뼈와 망가진 내장이 붙었다.

죽음 끝에서 생명을 되찾는 그를 축하하는 것처럼 짧은 비명이 울려 퍼졌다.

“커헉!”

한 생명의 부활을 알리는 축포인 동시에, 또 다른 한 생명의 죽음을 알리는 단말마.

가슴이 관통당한 중년 여인이 비틀거리며 뒷걸음질 친다.

훌륭한 전공을 쌓은 대격변의 영웅이자 미카엘 실베르트가 선택한 구렁텅이 속 오물답게, 죽음 앞에서도 한 자루 비수를 부서진 갑옷 틈새로 박아 넣은 그녀의 등줄기가 활처럼 휘었다.

퍼걱. 촤아아악!

빠져나가는 창날과 함께 피 분수가 솟구친 그 순간.

털썩.

썩은 통나무처럼 허물어진 시신 앞에, 철탑처럼 우뚝 선 청년의 모습이 미카엘 실베르트의 눈동자에 비쳤다.

- 진태경.

미카엘 실베르트가 진태경을, 아니 진태경이 미카엘 실베르트를 바라보았다.

더는 이전과 같은 회색도, 새하얀 흰자위조차 찾아볼 수 없는 완전한 어둠에 잠식된 까만 눈동자를 지닌 그를.

그리고…… 거대한 마력으로 이루어진 날개를 활짝 편 몬스터를.

화아아악!

반경 수백 미터에 달하는 국회의사당이, 서서히 끝을 향해 달려가고 있던 치열한 전장이 순간 고요해졌다.

모두가 경악했고, 침묵했다.

완전히 인간의 형태를 벗어난 미카엘 실베르트의 모습에.

그의 전신을 뒤덮은 비늘과 이마를 뚫고 튀어나온 두 개의 뿔이, 어둠을 닮은 거대한 날개를 본 순간 뇌리를 관통하듯 떠오른 한 몬스터의 이름에.

누군가의 입술 사이로 신음과도 같은 목소리가 흘러나왔다.

“……드래곤(Dragon).”

탄생과 함께 악몽과도 같은 힘을 부여받은 용족(龍族)의 뿌리이자 의미 그 자체.

바닥을 드러내지 않는 마력와 천지를 찢어발기는 힘, 막대한 재생력마저 지닌 최고(最古)이자 최악(最惡)의 몬스터.

더불어 사람들은 문득 잊고 있던 한 가지 사실을 떠올렸다.

지금의 미카엘 실베르트를 있게 만든 삼십여 년 전의 파리 대전투 당시, 네 명의 S급 헌터를 비롯한 일천의 목숨을 집어삼킨 것은 아직 다 자라지도 않았던 어린 드래곤이었다는 것을.

그리고 그 저주받은 생물이 지녔을 드래곤 하트(Dragon Heart)는, 어디에서도 발견되지 않았다는 것을.

- 그래, 이제야 알겠느냐.

미카엘 실베르트는 크게 소리 내어 웃었다.

포효와도 같은 그 소리에 국회의사당 전체가 흔들렸고, 피어(Fear)에 사로잡힌 몇몇 이들의 안색이 하얗게 질렸다.

하지만 한 사람은 아니었다.

후우우웅.

미카엘 실베르트의 이마 위로 솟아난 두 개의 뿔을 중심으로 모여드는 끔찍하리만치도 거대한 기운의 집합체. 브레스(Breath)를 보고 있음에도 진태경은 당황하지 않았다.

다만 그 광경을 물끄러미 바라보다, 한숨처럼 한 마디를 툭 내뱉을 뿐이었다.

“씨벌 새끼. 가뜩이나 몸도 안 좋은데…….”

그리고 다음 순간.

화아아악!

온 세상을 물들이며 쏟아지는 거대한 어둠과 창날을 타고 휘몰아친 청백색의 화염이 부딪쳤다.

고오오옹.

그 끝에, 눈부신 섬광이 있었다.
```

## Final English reading copy

```markdown
# Chapter 784

*Shwoosh!*

It was strange.

I’d only raised my spear. So where was this sharp whistle now piercing my ears coming from?

And what the hell gave those idiots the confidence to charge at me?

In that brief instant, split into even smaller fragments, I turned and brought my spearhead down.

*Whooom. Kaang!*

The pressure bursting along the spearhead knocked away a dozen or so daggers. At the same moment, two swords came slashing in from either side, aiming for my upper and lower body at once.

*Shhk, slice!*

It burned like I’d been scalded.

An alert sounded to tell me the durability of my Fire Dragon Armor had dropped, and a considerable stream of blood gushed from my thigh.

But if this was the price of fending off a surprise attack from three S-rank Hunters, it was a pretty good deal.

Even more so if I’d given as good as I got, instead of being the only one to take a hit.

*Pshaaa!*

Blood sprayed belatedly, soaking the ground. A middle-aged man and woman stared wide-eyed as they saw their comrade collapse, his chest split wide open.

“When did you—!”

“No, Fernando!”

It had all happened so quickly that I hadn’t had time to see who they were. But now that I was facing them, I recognized them all too well.

S-rank Hunters who each represented their country and stood as symbols of humanity.

Or rather, who *had*.

“Well, look who it is. I know all of you.”

At my greeting, tinged with a hollow laugh, the middle-aged pair swallowed hard.

Fernando Lucas, Brazil’s S-rank Hunter, had made the reckless choice to aim for my chest. Even as he spilled an enormous amount of blood, he was fumbling for a potion with trembling hands.

He looked so desperate that I spoke to him in a warm voice, like the male lead in a romance movie.

“Drink that, and I’ll kill you.”

“……!”

“But if you hang in there until this is all over, I’ll treat you. I’ll even make sure you get a nice prison. All right, then. Deal.”

Fernando Lucas stared at me blankly, as if he’d forgotten the pain.

Then, with lightning speed, he shoved the potion in his hand into his mouth.

Still in its bottle. Without even taking off the cap.

*Crack! Thud!*

Shattered glass and potion spilled into his open mouth.

But even the highest-grade potion, capable of restoring torn organs in the blink of an eye, couldn’t bring back someone who was already dead.

“I told you not to drink it.”

I murmured softly, looking at Fernando Lucas’s corpse, his forehead pierced by my Finger Qi. Just then, the two middle-aged Hunters beside him—slightly luckier than the man who’d gone to the next world first, and much more skilled—spoke with stiff faces.

“Did it really have to come to this?”

“It’s not too late, Jin. If you stop, we’ll withdraw. There’s no need for more sacrifices here, is there?”

Stop? No need for more sacrifices?

For a moment, I was at a loss for words. Then I looked around.

At the National Assembly, its interior still being stained red. At Michael Silbert, lying on the floor and twitching like an insect. Finally, at the two people standing before him.

Then I thrust out my spear.

One of the few lessons I’d learned by now was that you didn’t have to answer every stupid thing people said.

*Shhk!*

Even if they didn’t know martial arts, they were S-rank Hunters who’d seen more than enough combat.

With a sharp, startled gasp, the two barely evaded my attack and landed in front of and behind me.

But after the spearhead had come flying without warning, their eyes sank heavily.

“So this is your answer?”

“Wait. Don’t provoke him for no reason. Right now, we need to save Michael first—”

The woman understood the situation far better than the man did. But she was just as laughable.

*What the hell had they been doing all this time? How much had they done to bring things to this point?*

There’d been a time when I didn’t know anything, either.

A time when I’d gone mechanically back and forth between Gates and my goshiwon. A time when I fought monsters for money rather than out of a sense of duty as a Hunter, yet still felt vaguely offended whenever I heard someone say Hunters had fallen into corruption.

But…… now I knew too much.

And there was no going back.

It didn’t matter how great their achievements were, or how much strength they could contribute to the coming war.

If we didn’t cut out these tumors rooted deep in society, humanity would collapse before it even got the chance to fight the monsters.

Right before my eyes stood another Lee Jungryong, another Go Jun, another Michael Silbert.

The moment they turned their weapons against us despite the ugly truth having been exposed, they became tumors that had to be cut out.

“I already gave you a chance. The choice…… was yours.”

I charged without hesitation toward the people who’d once been the objects of my admiration and respect.

*Shweeeek!*


* * *


It was ironic. Pain itself was what tormented people, and yet they couldn’t feel it when death was near.

And…… that numbness was more frightening than any terrible pain.

*Ah.*

Michael Silbert blinked blankly.

His lips were slightly parted, but he couldn’t even groan. The strength was draining from his arms and legs, from which powerful energy had surged without pause. The blood that had soaked his body and was now sloshing around him felt dull and distant.

*Damn it.*

If he was going to fall like this, what had his life been for?

*Grrk. Cough.*

Instead of a hollow laugh, a bloody bubble welled in his mouth. His head tipped to the side as if he were collapsing, and he saw the corpse of a man frozen with his eyes wide open.

A familiar face.

Fernando Lucas.

He’d been a delinquent who belonged to a Brazilian gang from childhood, and he had the enthusiastic support of South America’s lower classes. Over the past ten years, Michael Silbert had done him various “favors.”

The public and the courts would, of course, interpret those “favors” differently.

*It started out small.*

But everything dulled with time, and each repetition made it grow like a snowball.

He’d eliminated a powerful rival and made it look like an accidental death. He’d used a politician with connections to him to bury tax-evasion charges. And once, he’d kidnapped a brave journalist along with his family when the journalist was preparing an article about how the hero of Brazil’s lower classes secretly ran a gang and made a fortune on the side.

The others now spilling blood and dying for him in every corner were no different.

*No. They weren’t doing this for me.*

Michael Silbert knew.

They were fighting for themselves.

They knew there was too much to lose if they admitted and accepted everything now.

In the end, he and the others had been no more than filth wallowing together in the same pit.

But thanks to that—thanks to how long he’d indulged their greed and ambition—Michael Silbert had bought himself a little time.

Precious time to cast off the bonds of humanity that he’d clung to until the end, and become something known as the Demon King.

*Slosh. Splash.*

The blood that had filled the crater rippled like a wave. Through his blurred vision, he saw a spearhead flash through the air and graze the neck of a middle-aged man.

*Slice!*

A body fell with a wet thud, and a head rolled over to meet his gaze.

The smell of blood wafting from the charred-black cross-section seemed as sweet as chocolate. That wasn’t merely his imagination.

*Heh-heh.*

Michael Silbert laughed softly. At last, he could laugh aloud, and his five senses slowly grew clear.

The sound of his heartbeat seemed to thunder in his ears.

*Thump. Thump-thump. Thump-thump-thump!*

As his heart pounded faster, the blood pooled in the crater rushed toward its owner’s body.

But it wasn’t red anymore.

It was a thick, gleaming green—the blood of something no one could call human.

The same blood as that of the unprecedented monster he’d encountered in Paris, more than thirty years ago, when the city had overflowed with blood and corpses, now filled Michael Silbert from head to toe.

Along with its endless magical power and Regeneration.

*Shhhh!*

The blood was sucked deep into his body. Severed muscles rejoined. Broken bones and ruined organs mended.

A short scream rang out, as if to celebrate his return to life from the brink of death.

“Kh-erk!”

It was a victory cry announcing the resurrection of one life—and a death rattle announcing the end of another.

A middle-aged woman staggered backward, her chest pierced through.

Like the filth in the pit Michael Silbert had chosen, she’d built up a splendid record of achievements as a hero of the Great Cataclysm. Even on the brink of death, she drove a dagger into a gap in his damaged armor. Her back arched like a bow.

*Crunch. Pshaaa!*

Blood spurted as the spearhead came free.

*Thump.*

In front of the corpse that had crumpled like a rotten log stood a young man, tall as an iron tower. Michael Silbert saw him.

—Jin Taekyung.

Michael Silbert looked at Jin Taekyung. Or rather, Jin Taekyung looked at Michael Silbert.

At him, with black eyes swallowed by absolute darkness—not the gray of before, not even the whites of his eyes remaining.

And…… at the monster spreading enormous wings made of magical power.

*Whooosh!*

The National Assembly, spanning hundreds of meters across, fell silent for a moment, along with the fierce battlefield that had been nearing its end.

Everyone was horrified. Everyone fell silent.

At the sight of Michael Silbert, who had completely lost the form of a human being.

At the scales covering his body, the two horns that had pierced through his forehead, and the name of a monster that flashed into their minds at the sight of the enormous wings resembling darkness.

A voice that sounded like a groan slipped between someone’s lips.

“……Dragon.”

The root and very embodiment of the dragonkin, a race born with nightmare-like power.

A monster of the highest order—the oldest and most evil—with magical power that never ran dry, strength that could tear apart heaven and earth, and tremendous Regeneration.

And people suddenly remembered something they’d forgotten.

During the great battle in Paris more than thirty years ago, the battle that made Michael Silbert who he was, it had been a young dragon—not even fully grown yet—that swallowed up a thousand lives, including those of four S-rank Hunters.

And the Dragon Heart that creature must have possessed had never been found anywhere.

—Yes. Do you understand now?

Michael Silbert laughed loudly.

His roar shook the entire National Assembly, and the faces of several people seized by Fear turned deathly pale.

But not one man’s.

*Whoooom.*

Jin Taekyung watched the dreadful mass of energy gathering around the two horns that had sprouted from Michael Silbert’s forehead. Even as he watched the Breath, he wasn’t flustered.

He merely looked on for a moment before tossing out a single word like a sigh.

“Fuck, you bastard. I’m already feeling like shit as it is……”

And then, the next moment—

*Whooosh!*

An immense darkness poured down, staining the whole world, and collided with the blue-white flames swirling along the spearhead.

*Gooooong.*

At the end of it all, there was a blinding flash.
```
