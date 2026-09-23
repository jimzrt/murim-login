<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0785.txt",
      "sha256": "358bbeb589ab7bfe609bed41ed07b133954e93be2dc03239b836540a4d3802d1",
      "bytes": 13868
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "74645f46556b8b2cde8c901d2979d6b4cec468517087aab89f99775c1ebc92b7",
      "bytes": 697
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "47349c578ce3a378dc53173dec4002c0828b8095d08eadab83cdfaafdabfc433",
      "bytes": 223666
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "1412ac8e4ca52dbaac1630b0dfaaf7813b5f3115a3c2ffcd5aa6290f0e552074",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "e109c8e9bd557ef47d434ede4eb258901736939d6b8d90e3e643db4add645a35",
      "bytes": 2112
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "a036d3a5e47da905d4919c89327bbf8236fea0e86fb05ed448ebc42992f40eb6",
      "bytes": 622
    },
    {
      "path": "characters/Michael.md",
      "sha256": "2b1626da7e8befdbe4cac58c47c6374e5051af6a3438cd59d7a7372804ce564a",
      "bytes": 842
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "4e9c0f4df7451430433d4ecedbd3cdd3b877d78a2f5ecf5c8b1c923b106f44bf",
      "bytes": 645
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8db9e79ef5ea3bb4279d4c11d5c9e6e23a49de5f2010abaf0bfb116c09d99a97",
      "bytes": 243344
    }
  ],
  "estimated_tokens": 9909
}
-->

# Durable State Update — Chapter 785

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 785. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 785. Profile updates may replace only one
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
  "chapter": 785,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 785,
    "continuity_sources": [785],
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
    "Michael Silbert has transformed into a dragon-like monster with enormous magical power and regeneration; his clash with Jin Taekyung ends in a blinding flash, with the result unknown.",
    "Jin Taekyung has a bleeding thigh wound and damaged Fire Dragon Armor; the battle at the National Assembly is unresolved."
  ],
  "continuity_sources": [
    784
  ],
  "open_questions": [
    "What was the outcome of the clash between Jin Taekyung and Michael Silbert?",
    "What is the full extent and nature of Michael Silbert’s transformation?"
  ],
  "safe_through": 784,
  "temporary_decisions": [
    "Keep magical power distinct from mana."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 최민우    | **Choi Minwoo**   |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 교관 | **Instructor** | Kim Hwajong's former Hunter Training Center role and address. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 국회의사당 | **National Assembly** | Government building visible from the skyscraper. |
| 펠릭스 | **Felix** | Prince of the United Kingdom. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |
| 크로노스 | **Kronos** | Guild led by Fabian. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 최민우 | 진태경 | trusted allied team leader to younger allied Hunter | Mr. Jin | formal-polite and concerned | Choi warns Jin about the danger of the operation and affirms his deep trust. |
| 진태경 | 최민우 | younger allied Hunter to allied team leader | Team Leader Choi | polite, familiar, and teasing | Jin jokes with Choi while acknowledging and dismissing his concern. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 미카엘 | 진태경 | rival_to_target | you | quietly polite but threatening | Michael warns Jin to reconsider for the sake of Jin's monster friend. |
| 진태경 | 미카엘 | target_to_rival | Go fuck yourself | blunt and profane | Jin rejects Michael's proposal to resurrect the World Hunter Federation. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 781
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 784
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, and a publicly recognized S-rank-level Hunter who formally retains an A-rank license, as well as a traveler between Murim and another world resembling the realm of immortals and the Hunter who exposed Michael Silbert's ability to absorb monsters' magical power.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 784
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 784
- **Aliases:** None
- **Role:** Michael Silbert is the Odin Guild Master and former public hero, now transformed into a dragon-like monster with immense magical power and regeneration.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 781
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Jin Taekyung's meticulous intelligence and operations lead, a trusted ally and natural leader capable of guiding the reestablished World Hunter Federation.
- **Personality:** Calm, pragmatic, meticulous, and emotionally steady under pressure.
- **Voice:** Measured, professional, and reassuring without minimizing responsibility.
- **Relationships:** A trusted ally and operational adviser to Jin Taekyung, and the maternal grandson of Cheon Taemin.

## Korean source

```text
＃785화



그것은 울림이었다.

단순한 굉음을 넘어, 귓가를 먹먹하게 만드는 울림.

고오오옹.

어둠과 화염이 충돌한다. 동시에 뒤섞인다.

강대하기 그지없는 두 개의 기운이 바람과 공기, 잔해를 빨아들이며 서서히 부풀어 오르는 광경을 지켜보던 모두의 머릿속에 붉은 경고등과 함께 한 단어가 스쳐 지나갔다.

궤멸(潰滅).

일찍이 느껴 본 적 없는 저 거대한 힘 앞에서는 전부 무의미하게 느껴졌다.

만약 저것이 이대로 터진다면 반경 수백 미터에 존재하는 모든 것들이 잿가루가 될 것이다.

아니, 국회의사당은 물론이고 이 도시 전체까지 그 여파가 미칠지도 몰랐다.

‘이대로면…… 민간인들까지 다친다.’

하지만 모두가 그렇게 생각하는 것은 아니었다.

비록 같은 위기를 느꼈을지라도 각자가 처한 상황은 달랐으니까.

이 자리의 누군가가 저 밖의 사람들이 살아가는 세상을 지키기 위해 싸우고 있다면, 또 다른 누군가는 오직 자신들의 세상을 지키기 위해 무기를 거꾸로 들었다.

그리고 근본부터 엇나간 그 한 가지 차이는, 곧이어 각기 다른 행동으로 나타났다.

“쳐!”

쉬쉬쉭!

벼랑 끝에 선 이상, 더는 물러설 곳도 없다.

미카엘 실베르트를 택한 배신자들은 이미 열세에 몰린 상황 속에서 벌어진 이변(異變)을 놓치지 않고 마지막 몸부림을 펼쳤다.

머릿수는 이미 절반으로 줄어들었으나, 독기가 서린 오러는 그 어느 때보다 흉험하게 번뜩였다.

카가가각!

커다란 타워 실드가 쪼개지고, 지면이 두부처럼 갈라진다.

잠시라도 방심한다면 목숨을 잃을 만한 일격들이 사방에서 쇄도했지만, 그 누구도 뒤로 물러서지 않았다.

그들은 헌터(Hunter)였으니까.

비록 저 배신자들에게는 그저 빛바랜 말뿐일지라도, 그들은 헌터라는 단어의 의미를 지켰고 앞으로도 지켜 나갈 터였다.

그것이 그들의 의무였고, 힘의 책임이었으니까.

“미스터 존슨!”

기합처럼 외친 최민우가 온 힘을 다해 검을 휘둘렀다.

이미 혈인(血人)이나 다름없게 된 주인의 모습과는 달리, 반월처럼 뻗어 나간 눈부신 오러가 허공에 우뚝 선 거구의 흑인을 스치듯 지나가며, 그를 향해 쏘아지던 수십 발의 화살을 갈랐다.

서걱!

단숨에 토막 난 화살의 잔해가 눈앞에서 흩어진다.

하지만 사방에서 벌어지는 이 긴박한 위기 앞에서도, 심호흡과 함께 마나를 끌어 올리던 매직 존슨은 내심 중얼거렸다.

‘그냥 존슨이라고 부르라니까.’

오늘 이 전투가 끝난다면, 끝없이 흐르는 피가 멎고 나면 다시 한번 최민우에게 말할 생각이었다.

이제는 정말 말 편히 해도 된다고.

손가락이 피투성이가 되도록 활시위를 당기고 있는 파이 첸과 고귀한 신분에도 불구하고 피를 뒤집어쓴 채 싸우고 있는 펠릭스 왕자. 또 지금 막 크로노스 길드장의 팔을 무식하게 뽑아 버린 척 헤이글의 어깨를 두드려 주고 싶었다.

아니, 살아남은 헌터들 모두와 거나하게 취해 웃으며 떠들고 싶었다.

그리고 틀림없이 그 자리에는…….

‘그래, 진. 네가 있겠지.’

닿지 못할 목소리가 울림에 파묻혀 흩어진다.

어느덧 국회의사당을 가득 메운 눈부신 섬광 너머, 한 청년의 모습이 흐릿하게 매직 존슨의 시야를 스쳐 지나갔다.

그런 그를 향해, 재앙의 중심을 향해 망설임 없이 달려 나가는 누군가의 뒷모습도.

촤라라라락!

새하얀 무언가가 파도처럼 휘몰아친다.

진태경과 미카엘 실베르트.

물러날 수 없는 대척점에 선 두 존재의 주위를 빈틈없이 가로막은 그것이 완성되는 순간.

매직 존슨은 희미한 웃음과 함께 전신의 마나를 일깨웠다.

그리고 온 세상을 감싸듯, 국회의사당 전체로 퍼트리며 입을 열었다.

“앱솔루트 쉴드(Apsolute Shield).”

대마도사의 막대한 마나를 집어삼키며 완성된 마법이 반경 수백 미터를 뒤덮은 그 순간.

화아아악.

마침내 터져 나온 아득한 섬광이, 모두의 시야를 물들였다.



* * *



찰나를 쪼개고 쪼갠 시간의 틈새 속.

꽈앙! 구구구구궁!

고통스럽게 느껴질 만큼 거대한 굉음과 함께 세상이 뒤흔들렸다. 칠흑 같은 어둠과 번쩍이는 불빛이 수없이 눈앞에서 명멸(明滅)하고, 무수한 감각이 전신을 통해 전해진다.

아프다. 뜨겁다. 서늘하다. 축축하다.

그리고…… 무겁다.

지금 이 순간에도 전신을 짓누르는 이 무게를 견딜 수 없을 만큼.

후욱. 훅.

호흡이 가쁘다. 나는 흐릿한 시야를 회복하려 애쓰며 창대를 지면에 박아넣어 몸을 지탱했다.

푹.

이럴 때만큼은 창을 무기로 택한 것이 다행이라는 생각이 든다.

문득 처음 헌터 훈련소에 입소했을 당시, 빨간 모자를 쓴 조교가 무기를 분출해 주며 해 주었던 말도 함께.



‘그냥 창 써라. 창이 최고야.’

‘어. 죄송하지만 이유가 무엇인지 여쭤봐도 되겠습니까.’

‘너 각성 등급 뭐냐.’

‘F급입니다.’

‘그래. 답 나왔네. 어차피 너희 같은 좆밥들 싸움에선 사정거리가 최고다. 본 교관이 써 보니까 알겠더라. 또 중요한 건…….’

‘중요한 건?’

‘멋있잖아.’

‘잘 못 들었습니다……?’

‘멋있다고. 자, 봐라. 만약에 네가 적을 만났어. 그리고 일대일로 존나게 싸웠어. 서로 모든 힘을 쏟아서 손가락 하나 까딱할 수 없는 거지. 그럼 이 상황에서 검 든 놈이 쓰러질까. 창 든 놈이 쓰러질까.’

‘하체 부실한 놈이 먼저 쓰러질 것 같습니다.’

‘틀렸다. 검 든 놈이 먼저 쓰러진다. 반드시.’

‘혹시 어째서인지 이유를 좀…….’



그 순간 조교가 근엄한 표정으로 했던 한 마디를, 아직도 잊지 못하겠다.



‘창을 든 놈은 지팡이로 쓸 수 있잖아.’

‘예?’

‘일단 땅이든 벽이든 한 번 콱 박아 넣으면 무조건 지탱할 수 있어. 하지만 검 쓰는 놈은 쓰러질 수밖에 없지. 왜? 길이가 짧거든. 바로 거기서 승부가 결정 나는 거야. 쓰러진 놈과 서 있는 놈. 어떠냐, 영화의 한 장면 같지 않냐?’

‘아.’

‘좋아. 그럼 네가 쓸 무기로 뭘 선택할지 결정했나?’

‘예, 정했습니다.’

‘뭐냐?’

‘활입니다.’

‘엎드려.’



병신같고 케케묵은 기억이다.

나는 곧장 병기고에 구비되어 있던 창대로 엉덩이를 스무 대쯤 처맞았고, 거의 반강제로 그 창을 생애 첫 무기로 지급받았다.

그리고 다음 날 첫 훈련 시간에 검을 차고 나온 그 조교를 보며 세상의 이치 중 하나를 깨달았다.

이 바닥에는, 실로 어마어마한 씨벌놈들이 득실거린다는 것을.

하지만 나 같은 훈련병들 놀려먹는 재미로 훈련소에 처박혀 있었을 그 조교도 당시에는 짐작조차 할 수 없었을 것이다.

시시껄렁한 그 농담 한마디로 인해, 내가 지금 이 자리에 서 있을 수 있다는 것을.

그때 봤던 F급 헌터가, 불과 십여 년 뒤 미카엘 실베르트를 무릎 꿇리게 되리라는 것을.

쿵.

귓가를 파고드는 육중한 소리와 함께, 나는 고개를 들었다.

흐릿한 시야 속, 한쪽 무릎을 꿇은 채 떨고 있는 놈이 보인다.

마력으로 이루어진 날개도, 검게 빛나던 비늘도 더 이상 찾아볼 수 없게 된 미카엘 실베르트는 나를 바라보며 숨을 헐떡였다.

- 개, 개 같은…….

쿨럭.

기침과 함께 내장 조각이 섞인 핏물이 폭포수처럼 쏟아졌다.

모든 마력을 소진한 몸뚱어리는 주인의 바람과는 달리, 앞서 보였던 기적 같은 회복력을 보여 주지 않았다.

아니, 이제 두 번 다시 그럴 일은 없을 것이다.

놈은, 미카엘 실베르트는…….

‘오늘. 내 손에 죽을 테니까.’

소리 내어 말할 힘도 없다. 닿지 않을 그 말을 마음속으로 중얼거린 나는 이를 악물며 백염을 붙잡고 몸을 바로 세웠다.

그리고 놈을 향해 걸었다.

저벅.

한 걸음, 한 걸음마다 부서질 듯한 통증이 전신을 엄습해 온다.

혹은 이미 부서졌거나.

삐빅. 삐빅. 삐비빅!

희한한 일이다.

고막이 터져 나간 귓가는 먹먹해진 지 오래인데, 시스템이 전해주는 경고음은 여전히 크고 시끄러웠다.

‘이거, 이 정도면 몸뚱어리가 어지간히 작살난 모양인데.’

헛웃음이 나왔지만 상관없었다.

도대체 내가 언제부터 몸 상태 걱정하고 싸웠다고.

그보다는 미카엘 실베르트를 완전히 쓰러트렸다는 사실이, 그리고 이 엄청난 여파 속에서도 반가운 얼굴들이 멀쩡하게 살아남았다는 사실이 기뻤다.

물론 내 기쁨이, 모두가 느끼는 감정은 아니겠지만.

“진태겨어엉!”

지금 나를 향해 달려드는 저 중년의 거한, 크로노스 길드장도 그중 하나였을 것이다.

실로 치열했던 전투였다는 것을 증명하듯 누구인지 모를 강자에게 한쪽 팔을 잃은 그는 자신의 인생이 끝장났다는 사실을 받아들이지 못하고 내게 달려들었다.

그러나 뒤이어 등 뒤에서 들려온 강맹한 파공성과 함께 결국엔 그 사실을 받아들일 수밖에 없게 됐다.

퍼엉!

무식하리만치 커다란 워 해머(War Hammer)가 스치듯 지나가자, 크로노스 길드장의 얼굴이 사라졌다.

썩은 통나무처럼 털썩 쓰러지는 그의 시체 뒤로 마치 투포환 선수처럼 자세를 취하고 있는 척 헤이글이 보였다.

아주 잠깐, 나를 빤히 바라보던 그는 피식 웃으며 돌아섰다. 그리고 남아 있는 배신자들을 향해 뛰어들었다.

얼어붙은 그들의 마음을 훈훈하게 녹일 뜨거운 한 마디와 함께.

“어디 한 번 끝까지 놀아 보자, 이 개자식들아.”

먹먹한 귓가로 함성과 비명이 뒤섞였다. 누군가는 피를 흩뿌리며 쓰러지고, 누군가는 그 시체를 밟으며 나아간다.

이미 승기(勝機)는 기울었다.

설령 운명의 여신이 나타나 이 저울추를 되돌린다 해도, 그마저 쓰러트리면 그만이다.

어느새 코앞까지 다가온 나를 바라보며 일어나려 애쓰는 저 괴물처럼.

저벅.

언제 여기까지 온 걸까.

나는 문득 걸음을 멈췄다. 그리고 평생지기를 만나러 지팡이를 짚고 먼 길을 걸어온 노인처럼, 힘겨우면서도 반갑게 인사를 건넸다.

“안녕. 나 왔다.”

캉!

대답 대신 돌아온 것은 아직도 새파랗게 빛나는 검신이다.

하지만 드래곤 본이라는 희대의 재료로 벼려 낸 예리함으로도 만년한철을 베어 낼 수는 없었고, 그 검에 실려 있던 힘과 속도는 턱없이 부족했다.

이미 중환자나 다름없는 나조차 우습게 막아 낼 수 있을 만큼.

그에 더해 이 무례한 답변을 돌려줄 수 있을 만큼.

퍽, 우드득.

미카엘 실베르트가 눈을 부릅떴다. 양팔이 으스러지는 통증에 딱 벌어진 입에서는 차마 토해 내지도 못한 비명이 핏물과 함께 들끓고 있었다.

크륵. 크르륵.

간헐적으로 터져 나온 핏물이 얼굴이 튀었다.

하지만 어째서일까.

분명 지금까지 놈이 한 짓을 생각한다면 지금 내 코로 스며드는 혈향(血香)은 달콤해야 할 텐데, 내가 느낄 수 있는 건 끔찍한 악취뿐이었다.

아마도 그래서였을 것이다.

문득 손을 멈춘 것은. 피와 눈물로 검게 물든 저 눈동자에 비친 내 얼굴이, 괴물처럼 일그러져 보였던 것은.

“……그래, 이게 네가 그토록 갖고 싶던 세상이냐?”

알고 있다.

어떤 물음을 던지더라도 내가 원하는 대답은 돌아오지 않는다는 사실을.

어떤 대답으로도 이 터질 것 같은 마음과 감정을 진정시킬 수 없다는 것을.

하지만…… 그렇게라도 듣고 싶었다. 나는 들어야 했다.

놈이 품었던 그 같잖은 야망으로 죽어 간 수많은 이들을 위해서라도.

“대답해라.”

덥석.

나는 하나밖에 남지 않은 미카엘 실베르트의 뿔을 움켜잡고 그대로 일으켜 세웠다. 물밀듯이 밀려오는 통증을 참으면서도, 시시각각 죽어 가는 놈을 향해 속삭였다.

“무슨 말이라도 해 봐. 어서.”

그리고 다음 순간.

나는 알 수 있었다.

놈에게서 사라진 또 하나의 뿔이 어디에 있었는지. 왜 주위 어디에도 보이지 않았는지.

퍽.

둔탁한 파육음과 함께 어디선가 솟구치듯 내질러진 뿔이, 누군가의 손바닥을 관통했다.

하지만 마땅히 흘러나와야 했을 핏물도, 고통을 인내하는 신음도 없었다.

다만 그 빈자리를 채운 것은, 내 어깨너머를 향한 미카엘 실베르트의 떨리는 눈동자와 목소리였다.

- 감히, 감히 네놈 같은 몬스터…….

“틀렸다. 처음이자 마지막으로 알려 줄 테니 똑똑히 명심하도록.”

그리고 귓가에 닿은 그 익숙한 목소리에, 나는 내 뒤에 서 있는 이의 정체를 깨닫고 소리 내어 웃었다.

“이 몸의 이름은 스톤 킹이다, 이 끔찍한 괴물아.”
```

## Final English reading copy

```markdown
# Chapter 785

It was a resonance.

More than a simple roar—a resonance that made their ears ring.

*Gooooong.*

Darkness and flames collided. At the same time, they swirled together.

As everyone watched the two incomparably powerful forces suck in wind, air, and debris, slowly swelling, a single word flashed through their minds beneath a red warning light.

Annihilation.

In the face of that immense power, unlike anything they had ever felt, everything seemed meaningless.

If it burst as it was, everything within a few hundred meters would be reduced to ash.

No—not just the National Assembly. The fallout might reach the entire city.

*At this rate…… even the civilians will get hurt.*

But not everyone thought that way.

Even if they all felt the same crisis, their circumstances were different.

Some here were fighting to protect the world where everyone outside lived. Others had turned their weapons against them for the sole purpose of protecting their own world.

And that one fundamental difference soon showed itself in the actions each side took.

“Get them!”

*Shhk-shhk-shhk!*

With their backs against the cliff, there was nowhere left to retreat.

The traitors who had chosen Michael Silbert seized the chance presented by this sudden turn of events, even as they were already outnumbered, and made one last desperate stand.

Their numbers had already been cut in half, but the malice in their auras gleamed more viciously than ever.

*Krrrraack!*

A massive tower shield split apart, and the ground cracked like a block of tofu.

Strikes came rushing in from every direction, each one lethal if they let their guard down for even a moment. Yet no one stepped back.

Because they were Hunters.

Even if the word meant nothing more to those traitors than a faded slogan, they had upheld what it meant to be a Hunter—and they would continue to do so.

It was their duty. The responsibility that came with their strength.

“Mr. Johnson!”

Choi Minwoo shouted like a battle cry and swung his sword with all his might.

Unlike its owner, who was now little more than a man drenched in blood, the dazzling crescent of aura shot across the air, passing close to the towering Black man standing there and cleaving through the dozens of arrows flying toward him.

*Shhk!*

The arrows fell apart in an instant, their severed remains scattering before him.

But even amid the urgent crisis unfolding all around him, Magic Johnson drew a deep breath and gathered his mana, muttering to himself.

*Just call me Johnson, already.*

When this battle was over, when the endless flow of blood had finally stopped, he would tell Choi Minwoo again.

He really could speak casually with him now.

He wanted to clap Pai Chen on the shoulder, still drawing his bowstring until his fingers were raw with blood; Prince Felix, fighting drenched in blood despite his noble status; and Chuck Hagel, who had just brutally ripped off the Kronos Guild Master’s arm.

No—he wanted to drink and laugh and talk with every Hunter who survived.

And there was no doubt that…….

*Yeah, Jin. You’ll be there.*

His voice, unable to reach anyone, was swallowed by the resonance and faded away.

Beyond the dazzling light that now filled the National Assembly, a young man’s figure flickered faintly across Magic Johnson’s vision.

And there was someone else running without hesitation toward him, toward the heart of the disaster.

*Chrrrrrrk!*

Something white as snow swept in like a wave.

The moment it finished forming, sealing off every gap around the two beings standing at an impassable crossroads—Jin Taekyung and Michael Silbert—Magic Johnson gave a faint smile and awakened the mana throughout his body.

Then he spread it across the entire National Assembly, as if to envelop the whole world, and spoke.

“Absolute Shield.”

The spell, completed by devouring the Grand Mage’s vast reserves of mana, covered a radius of several hundred meters.

*Whooosh.*

At last, a blinding flash burst forth, filling everyone’s vision.


* * *


In the sliver of time between moments, split thinner and thinner—

*Bam! Rumble-rumble-rumble!*

The world shook with a roar so immense it hurt. Pitch-black darkness and flashes of light flickered before my eyes over and over, while countless sensations coursed through my body.

It hurt. It was hot. It was cold. It was wet.

And…… it was heavy.

So heavy that I could barely bear the weight crushing down on me even now.

*Huff. Huff.*

My breathing was ragged. I struggled to clear my blurred vision, then drove the shaft of my spear into the ground to support myself.

*Thump.*

In moments like this, I was glad I’d chosen a spear as my weapon.

It reminded me of what the Instructor in the red cap had said when I first entered the Hunter Training Center, handing out weapons from the armory.

*“Just use a spear. Spears are the best.”*

*“Yes. Sorry, but may I ask why?”*

*“What’s your Awakening Grade?”*

*“F-rank.”*

*“Right. There’s your answer. In a fight between weaklings like you, reach is everything. I know because I’ve used one myself. Another important thing is……”*

*“What’s important?”*

*“It looks cool.”*

*“Sorry, I didn’t quite catch that……?”*

*“I said it looks cool. Now, listen. Say you run into an enemy. You fight like hell, one-on-one. You both pour out all your strength until you can’t even move a finger. In that situation, who’s going to fall over—the guy with the sword or the guy with the spear?”*

*“I’d guess the one with weak legs.”*

*“Wrong. The guy with the sword falls over first. Guaranteed.”*

*“Could you perhaps explain why……?”*


I still couldn’t forget what the Instructor had said then, with a solemn expression.

*“The guy with the spear can use it as a cane.”*

*“Excuse me?”*

*“You jam it into the ground or a wall, and it’ll hold you up. But the guy with the sword is bound to fall over. Why? It’s short. That’s where the fight’s decided. One guy’s down, the other’s still standing. What do you think? Sounds like a scene from a movie, doesn’t it?”*

*“Oh.”*

*“Good. So, have you decided what weapon you’re going to use?”*

*“Yes, I have.”*

*“What is it?”*

*“A bow.”*

*“Get down.”*


It was a stupid, dusty old memory.

I’d gotten about twenty whacks on the ass with a spear shaft from the armory, then been practically forced to accept that spear as my first weapon.

And when I saw that Instructor show up to our first training session the next day with a sword at his side, I learned one of the truths of the world.

This line of work was crawling with some truly incredible assholes.

But even that Instructor, who must’ve stuck around the training center for the fun of messing with recruits like me, couldn’t have guessed back then.

That because of his stupid little joke, I’d be standing here now.

That the F-rank Hunter he’d seen back then would make Michael Silbert kneel just a little over ten years later.

*Thump.*

I raised my head at the heavy sound that pierced my ears.

Through my blurry vision, I saw a man trembling on one knee.

Michael Silbert, whose magical-power wings and gleaming black scales had both disappeared, stared at me, panting.

“Y-you bastard…….”

*Cough.*

With a cough, a torrent of bloody fluid mixed with bits of his organs poured out.

His body had spent all its magical power, and, despite his hopes, it showed none of the miraculous recovery it had displayed before.

No. It would never do that again.

He—Michael Silbert—was going to……

*Die today. By my hand.*

I didn’t have the strength to say it out loud. I muttered the words where no one could hear them, gritted my teeth, and used White Flame to straighten up.

Then I walked toward him.

*Thud.*

Every step sent pain crashing through my body, as if I were about to break apart.

Or perhaps I already had.

*Beep. Beep. Beep-beep!*

It was strange.

My eardrums had burst, and my ears had been ringing for a while, but the System’s warning beeps were still loud and annoying.

*Looks like my body’s pretty thoroughly wrecked.*

I let out a hollow laugh, but it didn’t matter.

Since when had I worried about my condition before a fight?

I was happier that I’d finally brought Michael Silbert down—and that, despite the immense aftermath, all those familiar faces had made it through alive.

Of course, not everyone felt the same joy I did.

“Jin Taekyung!”

That middle-aged giant charging at me now, the Kronos Guild Master, was one of them.

As proof of how fierce the fighting had been, he’d lost an arm to some powerful fighter I couldn’t identify. Unable to accept that his life was over, he charged at me.

But the fierce whoosh that came from behind me forced him to accept it after all.

*Boom!*

An absurdly huge War Hammer swept past, and the Kronos Guild Master’s face disappeared.

Behind his corpse, which crumpled like a rotten log, Chuck Hagel stood posed like a shot-putter.

After staring intently at me for a brief moment, he let out a short laugh and turned away. Then he charged the remaining traitors.

With a warm little line to thaw their frozen hearts.

“Let’s see you keep playing to the very end, you sons of bitches.”

Cheers and screams mingled in my ringing ears. Some fell, spraying blood; others stepped over their bodies and pressed on.

The tide had already turned.

Even if the goddess of fate showed up to tip the scales back, all we had to do was take her down, too.

Like the monster struggling to rise as I came within a few steps of him.

*Thud.*

When had I gotten this close?

I suddenly stopped. And, like an old man leaning on his cane after a long journey to visit a lifelong friend, I greeted him, weary but glad to see him.

“Hey. I’m here.”

*Clang!*

In reply, all I got was the still-brilliant blue gleam of his sword.

But even the sharp edge forged from Dragon Bone—a material without peer—couldn’t cut through Ten-Thousand-Year Cold Iron. And the strength and speed behind the sword were nowhere near enough.

Not enough to get past even me, a man who was practically a hospital patient.

Not enough to stop me from returning that rude answer.

*Thud. Crunch.*

Michael Silbert’s eyes flew wide open. His arms crumpled, the pain so intense that a scream, mixed with blood, bubbled up from his gaping mouth before he could even let it out.

*Grrk. Grrrk.*

Blood spurted intermittently, splattering my face.

But why?

If I thought about what he’d done up until now, the scent of blood seeping into my nose should have been sweet. But all I could smell was something revolting.

Maybe that was why I suddenly stopped.

Why my own face, reflected in those eyes darkened by blood and tears, looked twisted like a monster’s.

“……So this is the world you wanted so badly?”

I knew.

No matter what I asked, he wouldn’t give me the answer I wanted.

No answer could calm this heart and these emotions threatening to burst out of me.

But…… I still wanted to hear it. I had to hear it.

For the countless people who had died because of the pathetic ambition he’d held on to.

“Answer me.”

*Grab.*

I seized Michael Silbert by his one remaining horn and hauled him upright. Enduring the pain flooding over me, I whispered to him as he died by the second.

“Say something. Anything. Come on.”

And in the next moment—

I realized where his other horn had gone. Why it was nowhere to be seen.

*Thump.*

With a dull, wet sound, the horn shot up from somewhere and pierced someone’s palm.

But there was no blood, though blood should have poured out. No groan of pain held back.

All that filled the empty space was Michael Silbert’s trembling eyes, fixed over my shoulder, and his voice.

“How dare you… How dare a monster like you…….”

“Wrong. I’ll tell you this once, and only once, so you’d better remember it.”

At that familiar voice reaching my ears, I realized who was standing behind me and laughed out loud.

“My name is Stone King, you hideous monster.”
```
