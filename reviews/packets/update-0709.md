<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0709.txt",
      "sha256": "7fef6603f243dda763bd99f1540488c8d753f2064a59177678d58448bbffdc89",
      "bytes": 13103
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "7d61ff422076659f36343c135a4afa9234a9c9b4633467329a9889bd326f12ea",
      "bytes": 1671
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "c1986676bc48fdff4fd48cf0f0b57f97ebad0bdfdd8467f01fb8d3155af76b6e",
      "bytes": 207119
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "f83527a73f870fa846a447f0a82a7e264ac00af730de8ce847aecfd38c1f9412",
      "bytes": 944
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "ea35fae5d0d8584807949eac27bc28293c766c24ff4e9943352bb48a37da004e",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "fb38bc24c3fdad96e53acbc4e129f376e315874ebe69c3b90da81d421f364ce8",
      "bytes": 1890
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "c86d2592b74224ea7ee032487e7aa1a4e6f2842d8f9ace0114acf59ec092be60",
      "bytes": 622
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "2ebce9daf0dbd3a4bcc594dfecc7d35500000c7b414733d085dd04708d4a3bb8",
      "bytes": 828
    },
    {
      "path": "characters/Wang Ho.md",
      "sha256": "629a37bdde1f0a056e8810d28819dbf096ff3c2932bcbef74636096384d79aa2",
      "bytes": 534
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "6f15dee36d5a032caa90af77c98394a0c535306a63b90c78ecec925d6c2845d1",
      "bytes": 217728
    }
  ],
  "estimated_tokens": 11179
}
-->

# Durable State Update — Chapter 709

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 709. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 709. Profile updates may replace only one
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
  "chapter": 709,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 709,
    "continuity_sources": [709],
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
    "Baeksang has been flung away with catastrophic injuries after stabbing the Southern Heaven Demon Empress, and his fate remains unresolved.",
    "The Southern Heaven Demon Empress survived the explosion, remains severely injured, and is burning through her remaining life while retaining some innate qi.",
    "Yayul Cheok is unconscious after shielding Jin Taekyung and has sword fragments embedded throughout his body.",
    "The White Tiger is gravely wounded after shielding Jin Taekyung, while the sacred stone has diminished to child-fist size.",
    "Wang Ho and more than a hundred surviving Baekcheon warriors are confronting the Southern Heaven Demon Empress.",
    "The Nanman Beast Palace is badly damaged but did not completely collapse.",
    "Jin Taekyung has chosen to run toward the Southern Heaven Demon Empress instead of fleeing."
  ],
  "continuity_sources": [
    708
  ],
  "open_questions": [
    "Will Baeksang survive his injuries?",
    "Will Yayul Cheok and the White Tiger survive their wounds?",
    "Can Jin Taekyung stop the Southern Heaven Demon Empress before her remaining life force is exhausted?",
    "What will happen to the diminished sacred stone and the guardian spirit?",
    "How many members of the Baekcheon Unit will survive the confrontation?"
  ],
  "safe_through": 708,
  "temporary_decisions": [
    "Render 경천동지 as cataclysm.",
    "Retain innate qi, Force, divine artifact, sacred stone, Baekcheon Unit, and Fiend.",
    "Preserve the guardian spirit's telepathic dialogue with em dashes.",
    "Preserve Jin Taekyung's first-person conversational voice."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 살기     | **killing intent**                               |                                                       |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 대주     | **Squad Leader** / **Commander**             |
| 일격     | **One Strike**                         |
| 귀가      | **your family**                                                 |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 왕호 | **Wang Ho** | Commander of the Baekcheon Unit who arrives leading white-armored reinforcements. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 선천지기 | **innate qi** | Vital energy said to be damaged by the pill's aftereffects. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 심맥 | **heart meridian** | Meridian severed by an infiltrator to commit suicide. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 소하 | **Xiao He** | Historical civil official invoked in the same exchange. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 백천대 | **Baekcheon Unit** | Baeksang's secret elite unit, cultivated over decades and held in reserve. |
| 수호령 | **guardian spirit** | Ancient title for the Black Tiger. |
| 백천대주 | **Commander of the Baekcheon Unit** | Title used for Wang Ho. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 미미 | rescuer to companion snake | Mimi or Mimi-chan | informal, pleading | Taekyung calls to Mimi while asking the snake to carry him and the survivors. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 진태경 | 수호령 | human ally to guardian spirit | guardian spirit | quiet and commanding | Jin whispers that they should go as they advance toward Baeksang. |
| 수호령 | 남천마후 | guardian_spirit_to_hostile_supernatural_opponent | you | terse, accusatory, and contemptuous | The guardian spirit tells the Southern Heaven Demon Empress that it knows her true essence and condemns her as a Fiend. |
| 남천마후 | 수호령 | hostile_supernatural_opponent_to_guardian_spirit | hideous beast | playful, taunting, and dismissive | She insults the guardian spirit while addressing it as a beast. |
| 수호령 | 진태경 | guardian spirit to human ally | Human | terse and alarmed | The guardian spirit cries out to Jin as the Southern Heaven Demon Empress sends him crashing into the ground. |
| 왕호 | 야수묘왕 | Baekcheon Unit Commander to Nanman Beast Palace Palace Lord | Palace Lord | formal and deferential | Wang Ho bows and formally reports his arrival to the Beast Miao King. |
| 왕호 | 진태경 | baekcheon_unit_commander_to_allied_combatant | you | formal and concerned | Wang Ho catches Jin as he begins to fall and tells him to stop because the battle is over. |
| 야수묘왕 | 남천마후 | allied_Ten_Kings_master_to_hostile_Demon_Empress | you | cold and threatening | The Beast Miao King addresses the Southern Heaven Demon Empress while promising to tear off her limbs and kill her. |
| 남천마후 | 천주 | devoted_servant_to_revered_master | Lord of Heaven | reverent and prayerful | The Southern Heaven Demon Empress prays that the Lord of Heaven will remember her loyalty and love. |

## Listed compact profiles

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 708
- **Aliases:** Heugung
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, and Great Chieftain of the Miao people; after shielding Jin Taekyung from the Southern Heaven Demon Empress's explosion, he lies unconscious with sword fragments embedded throughout his body.
- **Personality:** The Beast Miao King is boisterous and warmhearted toward Nanman's people, but their corruption and destruction awaken fierce grief and wrath in him.
- **Voice:** Low, growling, and forceful.
- **Relationships:** Baeksang is his sworn younger brother and childhood companion, Yayul Mok is his Young Palace Lord, Jeok Cheongang is an old acquaintance, and Jin Taekyung is Jeok's Disciple whom he now fights beside against the Southern Heaven Demon Empress.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 708
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 708
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, and a publicly recognized S-rank-level Hunter who formally retains an A-rank license; after surviving the Southern Heaven Demon Empress's explosion, he refuses to flee and runs toward her.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 708
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 708
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress is Honglan, creator of the rift behind the Inner Palace; she survives the explosion that follows Baeksang's ambush, retains some innate qi, and attacks the Baekcheon Unit while burning through her remaining life.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

### Wang Ho.md

# Wang Ho (왕호)

- **Safe through:** Chapter 708
- **Aliases:** None
- **Role:** Wang Ho is the Commander of the Baekcheon Unit; after the explosion, he leads more than a hundred surviving Baekcheon warriors in confronting the Southern Heaven Demon Empress.
- **Personality:** Not established.
- **Voice:** Formal and deferential when addressing the Palace Lord.
- **Relationships:** He commands the Baekcheon Unit and acknowledges Yayul Cheok as its Palace Lord.

## Korean source

```text
＃709화



쐐애애액!

가파른 속도로 쏘아지던 진태경의 신형이 미미하게 흔들렸다.

언제나 솜털처럼 가볍던 팔다리는 축 늘어진 채 고통을 호소하고, 지면을 밟는 발끝은 전과는 비교도 할 수 없이 무겁게 느껴진다.

실로 극심한 일섬의 여파.

야수묘왕의 도움이 아니었다면 지금쯤 제대로 서 있는 것조차 불가능했을 게 뻔했다.

만약 필사적인 의지로 버텼다 해도, 남천마후가 쏟아 낸 그 파괴적인 힘 앞에서는 분명 목숨을 잃었을 것이다.

하지만…… 살아남았다.

가장 여력이 부족했던 진태경을 구하기 위해 야수묘왕이, 수호령이 죽음을 무릅쓰며 몸을 내던졌고 그 뜻을 이어받은 백천대는 지금 이 순간도 목숨을 내던지고 있다.

짙은 어둠을 향해. 그들로서는 대적할 수 없는 악귀(惡鬼)를 향해.

퍼걱!

단 일격.

피를 머금은 악귀의 손이 뼈와 살을 부수고 가슴을 관통한다.

이름 모를 한 사람의 생명이 그렇게 사그라지고, 그 빈 자리를 채운 것은 또 다른 누군가다.

‘도대체 왜.’

진태경은 저들을 알지 못하고, 저들 역시 진태경을 알지 못한다.

그런데도 저들 모두는 기꺼이 목숨을 내던지고 있었다.

끊임없이 죽어 나가는 동료들의 빈 자리를 메우고, 자신들의 힘으로는 막을 수 없는 죽음을 향해 달려들고 있다.

그리고 그런 백천대의 모습이, 어두컴컴한 동굴 속에서 애써 웃음 짓던 한 사람과 겹쳐졌다.



‘먼저 가라. 태경아.’



도망쳤기에 살아남을 수 있었고, 살아남았기에 수도 없이 후회했다. 만약 그때로 돌아간다면 진태경은 이렇게 말했을 것이다.

“난 안 가, 절대로.”

악문 잇새 사이로 흘러나온 목소리에 백천대주 왕호가 고개를 돌린다.

누구의 것인지 모를 핏물을 흠뻑 뒤집어쓴 그가, 빠르게 가까워지는 신형을 발견하고 눈을 부릅떴다.

진태경은 이곳에 남아 있어서는 안 된다.

주군인 야수묘왕이, 왕호 자신을 비롯한 일백의 백천대가 목숨을 바쳐 얻어 낸 귀중한 시간이다.

어떻게든 살아남는 것이 그에게 주어진 유일한 사명이었을 터였다.

그런데 제 발로 위험을 찾아오다니.

“지금 이게 무슨……!”

경호성을 토해 낸 왕호가 다급히 코앞까지 다가온 진태경을 막아선 그때, 못 박힌 손이 그의 어깨를 짚었다.

동시에 귓가를 파고드는 나지막한 목소리.

“같이 좀 살자.”

“……!”

“씨이발. 같이 좀 살아남자고!”

순간, 왕호의 몸이 덜컥 굳었다.

모르겠다. 같이 죽자는 것이 아니라 살아남자는 진태경의 그 외침에, 불처럼 타오르면서도 축축하게 젖어 있는 그의 눈빛에 말문이 막혔다.

자신을 뒤로한 채 죽음을 향해 달려가는 저 어린 청년을, 도저히 막을 수 없었다.

그리고 깨달았다.

어째서 야수묘왕이, 십만에 달하는 부족민을 이끌어야 할 자신의 주군이 그러한 선택을 했는지.

‘이것 때문이었습니까? 바로 이런 모습 때문에, 당신의 안위보다 저 청년을 지키고자 하신 겁니까?’

함께 죽기 위해 돌아왔다면, 그것은 필부(匹夫)의 용맹에 불과하다.

그러나 진태경이 돌아온 이유는 함께 싸우기 위해서다. 한 사람이라도 더 많은 이들을 구하고, 모두가 살아남기 위해서였다.

츠츠츠!

금방이라도 꺼질 것 같던 검기(劍氣)가 힘을 되찾는다. 푸른 기운에 뒤덮인 검신을 곧추세운 왕호가 달려 나갔다.

그리고 이제는 채 절반도 남지 않은 수하들을 향해 외쳤다.

“저 악귀를 죽여라!”

그것은 아주 작지만 큰, 마음가짐의 차이였다.

막아서느냐. 혹은 죽이느냐.

지금까지의 남천마후는 그들의 전력으로는 죽일 수 없는 존재였다. 아니, 모두가 그렇게 착각하며 죽음을 받아들였다.

하지만 이제는 다르다.

지금부터는 남천마후를 죽이기 위한 싸움. 자신들이 살기 위한 싸움이다.

그 중심에, 그 모든 것을 깨닫게 해준 한 청년이 있었다.

“남천마후!”

분노로 가득 찬 포효와 함께, 진태경의 발끝에서 미약한 불꽃이 솟구쳤다.

쾅!

작은 폭발음과 함께 움푹 꺼진 지면이 거미줄처럼 갈라진다.

그 반동으로 더욱 빠르게 쏘아지는 신형의 끝에는, 피와 어둠으로 점철된 악귀가 있었다.

서걱! 촤아아악!

혼탁한 어둠이 깃든 수도(手刀)에 누군가의 몸뚱어리가 반으로 갈라진다.

사방으로 흩뿌려지는 핏물 너머, 공간을 가르며 자신을 향해 쇄도하는 진태경의 모습을 확인한 남천마후는 기쁘게 웃었다.

‘우둔한 아이야. 너의 그 무모함이, 내게는 마지막 기회가 되었구나.’

조금 전까지의 그녀는 격분하고 있었다.

목숨을 담보로 한 선천지기(先天之氣)는 시시각각 소모되고 있었고, 죽음을 불사한 채 앞길을 막아선 일백의 백천대는 끊임없이 죽어 가면서도 남은 힘을 갉아먹었으니까.

하지만 이제는 웃을 수 있었다. 가장 중요한 사냥감이, 참으로 멍청하게도 제 발로 죽을 자리를 찾아왔으니.

“이제 잔챙이들은…… 모조리 꺼져라.”

콰아아아!

혼탁한 장력(掌力)이 앞길을 막아선 전사들을 휩쓸었다. 핏물을 뿜어내며 사방으로 튕겨 나가는 신형들.

그렇게 순간 텅 비어 버린 공간 너머에서 파공성이 일었다.

쐐애애액! 쾅!

섬광처럼 짓쳐 든 한 자루의 철창을 맨손으로 튕겨 낸 남천마후가 수도를 내리그었다.

슈화아악!

공간이 갈라지고 칼날 같은 바람이 휘몰아친다. 그러나 진태경의 신형은 어디에도 없었다.

‘위!’

깨달음과 함께 남천마후의 신형이 흐릿해졌다. 뒤늦게 허공으로부터 내리그어진 투명한 창날이 그녀의 잔상을 갈랐다.

서걱!

아니, 창날이 갈라 낸 것은 잔상뿐만이 아니었다.

이마를 타고 또르르 굴러떨어지는 핏방울을 느낀 남천마후의 표정이 살짝 굳었다.

‘빠르다.’

어떻게 보면 당연한 일이었다.

초절정에 오른 무인이라면 이미 초인(超人)이라 불러도 부족함이 없으니까.

그러나 그들이 초인이라 불릴 수 있는 이유는, 무공에 대한 깨달음 외에도 막강한 공력이 있기 때문이다.

오랜 수련으로 단련된 신체 능력을 더욱 극대화시킬 수 있는 공력이.

‘그런데 어떻게…….’

분명 대부분의 공력을 소모한 진태경이, 이토록 빠르고 강한 힘을 낼 수 있단 말인가.

쉬쉬쉬쉭!

창끝이 흔들린다. 수십여 개로 불어난 창영(槍影)이 남천마후의 전신을 향해 쏟아졌다.

예상했던 범위를 아득하게 뛰어넘는 속도와 힘. 하지만 남천마후는 물러서지 않았다.

“네놈 따위가 감히……!”

끓어오르는 듯한 음성과 함께 하나뿐인 손이 공간을 격하고 쏘아진다.

수많은 전사의 핏물을 머금은 일장이 코앞까지 들이닥친 창영을 뒤덮었다.

콰아아아!

거짓이 아무리 많더라도, 결국 드러날 진실은 하나뿐.

수십여 개에 달하던 창영이 장력에 휩쓸려 사라진다. 혼탁한 어둠에 휩싸인 남천마후의 손이 투명한 창날을 붙잡았다.

서걱!

만년한철(萬年寒鐵). 천하의 그 어떤 것보다 단단하며 예리하다는 금속이 강기를 찢고 살갗을 가른다. 그와 동시에 엄습해 오는 통증.

그러나 남천마후는 도리어 웃어 보였다.

‘잡았다.’

그 순간.

쏴아아아악!

창날을 타고 흘러 들어간 남천마후의 기운이, 진태경의 내부를 휩쓸었다.

퍼엉!

“……!”

들썩이는 신형. 야수묘왕의 도움으로 잠시 가라앉혔던 내부가 다시 한번 진탕된다.

그러나 진태경은 울컥, 솟구치는 핏물을 삼키며 창대를 쥔 손에 힘을 더했다.

콰드득!

남천마후의 손에 붙잡힌 백염의 창날이 회전과 동시에 더욱 앞으로 나아간다.

순식간에 너덜너덜해진 손아귀, 그리고 엄습하는 고통에 남천마후가 눈을 부릅떴다.

“너…….”

하지만 그녀의 말이 끝까지 이어지기도 전에, 날카로운 파공성이 울려 퍼졌다.

쉬이이익!

바람을 가르며 날아드는 한 자루의 검. 푸른 검기에 휩싸인 검의 주인은, 다름 아닌 백천대주 왕호였다.

서걱!

황급히 몸을 비틀었지만, 이미 늦었다.

전과는 비교도 할 수 없을 만큼 약해진 호신강기는 검기를 막아 낼 수 없었고, 남천마후는 베어 나간 옆구리로부터 전해지는 고통을 느끼며 다리를 차올렸다.

쐐애애액, 콰직!

채찍처럼 휘둘려진 발끝이 왕호의 복부를 파고들었다. 포탄처럼 쏘아진 그의 신형이 십여 장 밖으로 튕겨 나갔다.

콰앙!

충돌의 여파와 함께 솟구치는 먼지구름. 그러나 남천마후를 향해 달려든 것은, 왕호 한 사람뿐만이 아니었다.

파파팟!

전후좌우. 남천마후를 둘러싼 모든 방향을 점하며 쇄도하는 신형들.

이제 스무 명도 채 남지 않은 백천대의 전사들은 마지막 힘을 쥐어 짜내어 쇄도했다.

이 싸움을 끝내기 위해. 하나뿐인 목숨을 바쳐서라도 저 악귀의 몸에 창칼을 박아넣기 위해.

쉬쉬쉬쉭!

강맹한 파공성이 바람에 뒤섞이던 그 순간.

콰아아앙!

마치 폭풍과도 같은 기운이 터져 나와, 사방에서 날아들던 모든 것을 휩쓸었다.

그리고 그 중심에 우뚝 선 누군가의 입술 사이로, 끝끝내 참지 못한 핏물이 흘러나왔다.

쿨럭.

아득해진 시야 속, 남천마후는 파르르 떨리는 눈으로 자신의 앞에 무릎을 꿇은 한 청년을 바라보았다.

금방이라도 꺼질 듯이 흐릿한 눈동자.

그러나 창대를 굳게 말아쥔 채 앞으로 내민 두 손은 흔들림이 없었고, 그 끝에는 남천마후의 가슴 어림을 파고든 투명한 창날이 있었다.

“커……헉!”

남천마후는 검붉은 핏물을 게워 내며 숨을 헐떡였다.

막아야 했다. 막을 수 있을 것이라 생각했다. 그러나 막지 못했다.

‘도대체. 도대체 어떻게 움직일 수 있었지?’

전사들을 향해 장력을 쏟아내기 직전, 남천마후는 분명 진태경을 향해 다시 한번 공력을 흘려보냈다.

두 번 다시 일어나지 못하도록, 이번에는 확실히 숨이 끊어지도록.

하지만 진태경은 쓰러지지 않았고, 죽지도 않았다.

이미 심맥이 갈기갈기 찢어졌음이 분명한데도. 마지막까지 놓지 않은 창을 남천마후의 가슴에 박아넣었다.

“진태……경.”

끊어질 듯한 목소리가 남천마후의 입술을 비집고 흘러나온 그 순간.

스르륵. 툭.

피에 젖은 진태경의 양손이 창대에서 미끄러졌다. 힘없이 뒤로 젖혀진 고개와 흐릿해진 눈동자.

그와 동시에 남천마후는 느꼈고, 들을 수 있었다.

느리지만 분명하게 진태경에게 다가오는 죽음을.

그리고 죽음을 앞둔 이라고는 믿을 수 없을 만큼 환한 그의 목소리를.

“드디어 잡았다. 이…… 개 같은 년.”

“……!”

그 순간, 남천마후는 전신의 털이 곤두서는 듯한 감각에 사로잡혔다.

그것은 어떤 상황에서도 흔들리지 않을 일념(一念)을 지닌 한 인간에 대한 두려움이었고, 공포였다.

‘……두려워? 두려워한다고? 내가? 저놈을?’

있을 수 없는 일이었다. 천주가 아닌 누군가를 두려워한다는 것도. 그 대상이 죽음을 앞둔 핏덩이라는 것도.

‘죽여야 해. 이 손으로 직접, 놈의 숨통을 끊어야 해.’

넋 나간 듯이 마음속으로 뇌까린 남천마후는 천천히 손을 들어 올렸다.

아마 그녀 역시 죽음을 피하지 못할 것이다. 그러나 놈을, 진태경의 숨통을 끊어놓지 않는다면 죽어서도 편안히 눈을 감지 못할 것만 같았다.

‘죽어라.’

이 괴물아.

미처 토해 내지 못한 그 한 마디와 함께, 남천마후는 마지막 힘을 실은 수도(手刀)를 내리그었다.

쉬익!

그리고 혼탁한 어둠의 기운이 진태경의 정수리를 파고들려던 그 순간.

쐐애애애액! 퍼걱!

어디선가 날아온 한 줄기의 섬광이, 남천마후의 하나뿐인 팔을 집어삼켰다.

동시에 누군가의 서늘한 목소리가 얼어붙은 그녀의 귓가를 파고들었다.

“감히 누구의 몸에 손을 대려는 것이냐, 이 호로 잡년아.”
```

## Final English reading copy

```markdown
# Chapter 709

Screeeeeech!

Jin Taekyung’s figure, shooting forward at breakneck speed, wavered slightly.

His limbs, which were usually as light as down, hung limp and cried out in pain, while his toes felt incomparably heavier than before each time they touched the ground.

The aftermath of that devastating One Annihilation.

If not for the Beast Miao King’s help, there was no doubt Jin would have been unable even to stand properly by now.

Even if he had endured through sheer desperation, the destructive power unleashed by the Southern Heaven Demon Empress would certainly have taken his life.

And yet… he had survived.

To save Jin Taekyung, who had been in the worst condition of them all, the Beast Miao King and the guardian spirit had thrown themselves into danger, risking their lives. Carrying on their resolve, the Baekcheon Unit was still staking their lives at this very moment.

Toward the deep darkness.

Toward a Fiend they had no way of opposing.

Crack!

One strike.

The blood-soaked hand of the Fiend shattered bone and flesh before punching through a chest.

The life of someone whose name Jin did not know guttered out just like that, and someone else stepped forward to fill the empty space.

*Why?*

Jin Taekyung did not know them, and they did not know Jin Taekyung.

And yet every one of them was willingly throwing away their life.

They filled the empty places left by their comrades, who were dying one after another, and charged toward a death they did not have the strength to stop.

And the sight of the Baekcheon Unit overlapped with that of someone who had forced a smile in the darkness of a cave.

*Go on ahead, Taekyung.*

He had survived because he ran, and because he survived, he had regretted it countless times. If he could return to that moment, Jin Taekyung would have said this.

“I’m not going. Never.”

At the voice that slipped through his clenched teeth, Wang Ho, Commander of the Baekcheon Unit, turned his head.

Soaked in blood whose owner could not be identified, he widened his eyes when he spotted the rapidly approaching figure.

Jin Taekyung should not have remained here.

This was precious time that his lord, the Beast Miao King, and the hundred warriors of the Baekcheon Unit—including Wang Ho himself—had staked their lives to secure.

His only mission must have been to survive by any means necessary.

And yet he had come looking for danger of his own accord.

“What the hell is going on…!”

Just as Wang Ho cried out in alarm and moved to block Jin Taekyung, who had rushed right up to him, a nail-pierced hand came down on his shoulder.

At the same time, a low voice pierced his ear.

“Let’s live through this together.”

“……!”

“Fucking hell. I said let’s survive together!”

Wang Ho’s body abruptly went rigid.

He did not know what to say.

Jin Taekyung was not calling for them to die together. He was crying out that they should survive together, his eyes burning like fire even as they glistened with tears.

Wang Ho could not stop that young man from leaving him behind and running toward death.

And then he understood.

Why the Beast Miao King—his lord, who had to lead nearly one hundred thousand tribespeople—had made that choice.

*Was this why? Was it because of this very sight that you wanted to protect that young man more than your own safety?*

If Jin had returned so they could die together, it would have been nothing more than foolhardy courage.

But Jin Taekyung had returned so they could fight together. To save as many people as possible, even if it was only one more, and for everyone to survive.

Tsstsst!

The Sword Energy that had seemed ready to go out regained its strength. Wang Ho straightened the blade enveloped in blue qi and charged forward.

Then he shouted to his subordinates, fewer than half of whom now remained.

“Kill that Fiend!”

It was a tiny yet enormous difference in mindset.

Would they hold her back?

Or would they kill her?

Until now, the Southern Heaven Demon Empress had been an existence they could not kill with their combined strength. No—all of them had mistaken that for the truth and accepted their deaths.

But now it was different.

From this moment on, this was a fight to kill the Southern Heaven Demon Empress.

A fight for their own survival.

At its center stood one young man who had made them realize all of this.

“Southern Heaven Demon Empress!”

Along with his roar, full of rage, a faint flame sprang up from Jin Taekyung’s toes.

Boom!

With a small explosion, the sunken ground split apart like a spiderweb.

Propelled by the recoil, his figure shot forward even faster.

At its end waited a Fiend stained with blood and darkness.

Slice! Shraaaaaak!

A body was cleaved in two by a hand blade wreathed in murky darkness.

Beyond the blood spraying in every direction, the Southern Heaven Demon Empress saw Jin Taekyung tearing through space as he charged toward her—and smiled delightedly.

*You foolish child. Your recklessness has become my final chance.*

Until a moment ago, she had been furious.

Her innate qi, which had been fueled by her life, was being consumed with every passing moment. The hundred warriors of the Baekcheon Unit who had blocked her path without regard for their own lives continued to die, gnawing away at what little strength she had left.

But now she could smile.

Her most important prey had come searching for the place where he would die, foolishly walking there on his own two feet.

“Now, all you small fry… get the hell out of my way.”

Roooooar!

Murky palm Force swept over the warriors blocking her path.

Their figures were flung in every direction, spitting blood.

And then, beyond the space that had emptied in an instant, a sound split the air.

Screeeeeech! Boom!

The Southern Heaven Demon Empress knocked away an iron spear that shot toward her like a flash of light with her bare hand, then swung down with her hand blade.

Whoooosh!

Space split apart, and blade-like wind whipped through it.

But Jin Taekyung’s figure was nowhere to be seen.

*Above!*

The moment she realized it, the Southern Heaven Demon Empress’s figure blurred.

A transparent spearhead slashed down from the sky too late to catch her, cutting through her afterimage.

Slice!

No. The spearhead had cut through more than just an afterimage.

The Southern Heaven Demon Empress felt a drop of blood roll down her forehead.

Her expression hardened slightly.

*Fast.*

In a way, it was only natural.

A martial artist who had reached the Supreme Peak could already be called superhuman without exaggeration.

But the reason they could be called superhuman was not merely their enlightenment in martial arts. It was also their overwhelming internal energy.

Internal energy that could further maximize physical abilities honed through years of training.

*Then how…?*

Jin Taekyung had clearly spent most of his internal energy. How could he still produce such fast, powerful attacks?

Shk-shk-shk-shk!

The spear tip trembled.

Dozens of spear shadows multiplied and poured toward every part of the Southern Heaven Demon Empress’s body.

Their speed and power far exceeded anything she had expected.

But the Southern Heaven Demon Empress did not retreat.

“How dare you, you little brat…!”

Along with her voice, which seemed to boil with rage, her only hand split the air and shot forward.

The palm strike, steeped in the blood of countless warriors, swallowed the spear shadows rushing toward her face.

Roooooar!

No matter how many falsehoods there were, in the end, only one truth would emerge.

The dozens of spear shadows vanished as they were swept away by the palm Force.

The Southern Heaven Demon Empress’s hand, shrouded in murky darkness, seized the transparent spearhead.

Slice!

Ten-Thousand-Year Cold Iron—the metal said to be harder and sharper than anything beneath heaven—tore through the Force and cut into her flesh.

At the same time, pain surged through her.

But the Southern Heaven Demon Empress smiled instead.

*I’ve got it.*

At that moment—

Shwaaaaaaak!

Her qi flowed along the spearhead and swept through Jin Taekyung’s insides.

Boom!

“……!”

His body jolted.

The internal injuries that had briefly settled with the Beast Miao King’s help were shaken once again.

But Jin Taekyung swallowed the blood surging up his throat and tightened his grip on the spear shaft.

Crack!

The White Flame spearhead caught in the Southern Heaven Demon Empress’s hand rotated and drove farther forward.

Her grip was shredded in an instant, and pain rushed through her.

The Southern Heaven Demon Empress’s eyes widened.

“You…”

But before she could finish, a sharp sound of splitting air rang out.

Shiiiiing!

A sword came flying through the wind.

The owner of the sword, wrapped in blue Sword Energy, was none other than Wang Ho, Commander of the Baekcheon Unit.

Slice!

The Southern Heaven Demon Empress twisted her body in haste, but it was already too late.

Her Body-Protecting Qi had weakened beyond comparison to before and could not stop the Sword Energy.

Feeling the pain radiating from her slashed flank, the Southern Heaven Demon Empress kicked upward.

Screeeeeech—crack!

Her foot, swung like a whip, drove into Wang Ho’s abdomen.

His figure shot away like a cannonball and flew more than ten jang.

Boom!

A cloud of dust rose with the force of the impact.

But Wang Ho was not the only one who had charged toward the Southern Heaven Demon Empress.

Pat-pat-pat!

Figures rushed in from every direction—front, back, left, and right—taking positions around the Southern Heaven Demon Empress.

The fewer than twenty remaining warriors of the Baekcheon Unit charged forward, squeezing out the last of their strength.

To end this fight.

To drive their spears and blades into that Fiend’s body, even if it cost them their lives.

Shk-shk-shk-shk!

At that moment, when the fierce sounds of weapons tearing through the air mingled with the wind—

Kraaaaaash!

Energy like a storm exploded outward, sweeping away everything flying in from every direction.

And from between the lips of the person standing tall at its center, blood that could no longer be held back began to flow.

Cough.

Through her fading vision, the Southern Heaven Demon Empress looked at the young man kneeling before her with trembling eyes.

His eyes were dim, as though they might go out at any moment.

But his hands, thrust forward while gripping the spear shaft tightly, did not tremble.

At their end was a transparent spearhead driven into the vicinity of the Southern Heaven Demon Empress’s chest.

“Guh…!”

The Southern Heaven Demon Empress vomited dark-red blood and gasped for breath.

She should have blocked it.

She thought she could block it.

But she had failed.

*How? How was he still able to move?*

Just before unleashing her palm Force toward the warriors, the Southern Heaven Demon Empress had clearly sent her internal energy into Jin Taekyung once more.

This time, she had made certain that his breath would stop, so he could never rise again.

But Jin Taekyung had neither fallen nor died.

Even though his heart meridian had undoubtedly been torn to shreds, he had driven the spear he had held until the very end into the Southern Heaven Demon Empress’s chest.

“Jin Tae…kyung.”

At the moment her broken voice slipped through her lips—

Slide. Thud.

Jin Taekyung’s blood-soaked hands slipped from the spear shaft.

His head tipped backward helplessly, and his eyes grew hazy.

At the same time, the Southern Heaven Demon Empress felt it.

She could hear it, too.

Death was approaching Jin Taekyung slowly but surely.

And she heard his voice, bright beyond belief for someone standing before death.

“I finally caught you, you goddamn bitch.”

“……!”

At that moment, a sensation like every hair on the Southern Heaven Demon Empress’s body standing on end seized her.

It was fear.

Terror of a human being who possessed an unwavering resolve that would not falter under any circumstances.

*…Afraid? I’m afraid? Me? Of that bastard?*

It was impossible.

It was impossible that she could fear anyone who was not the Lord of Heaven.

And it was impossible that the object of that fear could be a mere brat standing on the brink of death.

*I have to kill him. With this hand, I have to cut off his breath myself.*

Muttering the words in a daze, the Southern Heaven Demon Empress slowly raised her hand.

She would probably be unable to escape death either.

But if she did not cut off Jin Taekyung’s breath, she felt that she would never be able to close her eyes in peace, even after death.

*Die.*

*You monster.*

With that one word she did not have the chance to spit out, the Southern Heaven Demon Empress swung down her hand blade with the last of her strength.

Shk!

And at the moment the murky darkness was about to bore into the crown of Jin Taekyung’s head—

Screeeeeech! Crack!

A streak of light flew in from somewhere and swallowed the Southern Heaven Demon Empress’s only arm.

At the same time, a cold voice pierced her frozen ear.

“Just whose body do you think you’re laying a hand on, you fucking bitch?”
```
