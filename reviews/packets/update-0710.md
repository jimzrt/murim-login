<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0710.txt",
      "sha256": "66622a9037446c9f43807c0664d103b11f1333fc5a0fdc5ac86500b1e35f1733",
      "bytes": 14059
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "594010cdda2a58c4868c20dc497368ce6d98a17beb55abd94b9720bea448bb7a",
      "bytes": 1608
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "c1986676bc48fdff4fd48cf0f0b57f97ebad0bdfdd8467f01fb8d3155af76b6e",
      "bytes": 207119
    },
    {
      "path": "characters/Blood Monk.md",
      "sha256": "3811944f8256d2c8a00910210b4ee217031f3ad2889c7a6620b91339eb927160",
      "bytes": 589
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "3eea65f1c5fd0a7375946138bc89ad5588acfd5619e70bf6bbde884f9be7d4d1",
      "bytes": 553
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "03438dce1915e0f3607ff42fcb36389d3362808129867a55eecd9922d6fda7e4",
      "bytes": 1702
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "84c2be8b3cc7f2d1cb3ef93f1e3b686de68306e3cf3d5deccbe4eb179378d7c3",
      "bytes": 1941
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "e50ff32b9b14e3766bbb2dcdbb22785a881927cc725ef685d2eab39190648ebc",
      "bytes": 622
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "1ffd7c8bfcdf72969577ddcd80746219be600bed743162b947813ecf0bd28a15",
      "bytes": 915
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "6f15dee36d5a032caa90af77c98394a0c535306a63b90c78ecec925d6c2845d1",
      "bytes": 217728
    }
  ],
  "estimated_tokens": 11114
}
-->

# Durable State Update — Chapter 710

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 710. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 710. Profile updates may replace only one
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
  "chapter": 710,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 710,
    "continuity_sources": [710],
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
    "Jin Taekyung has returned to the battlefield and is fighting beside the Baekcheon Unit so they can survive together.",
    "Fewer than twenty Baekcheon Unit warriors remain in the assault on the Southern Heaven Demon Empress.",
    "Jin Taekyung has driven White Flame through the Southern Heaven Demon Empress's chest.",
    "Jin Taekyung's heart meridian is torn and he is at the brink of death.",
    "The Southern Heaven Demon Empress is critically wounded and continues burning through her remaining innate qi.",
    "The Southern Heaven Demon Empress attempts to kill Jin Taekyung before she dies.",
    "An unidentified attacker has destroyed the Southern Heaven Demon Empress's only arm."
  ],
  "continuity_sources": [
    709
  ],
  "open_questions": [
    "Will Jin Taekyung and the Southern Heaven Demon Empress survive their mutually fatal injuries?",
    "Who is the unidentified attacker who intervened against the Southern Heaven Demon Empress?",
    "Will Baeksang survive his catastrophic injuries?",
    "Will Yayul Cheok and the White Tiger survive their wounds?",
    "What will happen to the diminished sacred stone and the guardian spirit?"
  ],
  "safe_through": 709,
  "temporary_decisions": [
    "Render 경천동지 as cataclysm.",
    "Retain innate qi, Force, divine artifact, sacred stone, Baekcheon Unit, and Fiend.",
    "Preserve the guardian spirit's telepathic dialogue with em dashes.",
    "Preserve Jin Taekyung's first-person conversational voice.",
    "Render 심맥 as heart meridian and 수도 as hand blade."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 중원     | **Central Plains**                               |                                                       |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 레벨               | **Level**                      |
| 귀가      | **your family**                                                 |
| 혈승 | **Blood Monk** | Sobriquet of the unidentified bald martial artist active in Guizhou. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 선천지기 | **innate qi** | Vital energy said to be damaged by the pill's aftereffects. |
| 광염 | **light-flames** | Violet manifestation surrounding Cheongpung when he uses the Zaha Divine Technique. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 근골 | **Muscles and Bones** | System attribute increased by 2 during the climb. |
| 노환 | **infirmities of old age** | Jeok Cheongang's age-related illness. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 선장 | **Zen staffs** | Staff weapons carried by the Hundred and Eight Arhats. |
| 대라신선 | **Great Firmament Immortal** | Legendary immortal invoked by Mungyeong as unable to stop the dragon's death. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 적천강 | 남천마후 | legendary_martial_master_to_hostile_demon_empress | you bitch | blunt and threatening | Threatens to punish her and Lord of Heaven. |
| 남천마후 | 적천강 | hostile_demon_empress_to_legendary_martial_master | Fire King Jeok / you | flattering and mocking | Addresses Jeok Cheongang as the Fire King while praising Lord of Heaven. |
| 남천마후 | 천주 | devoted_servant_to_revered_master | Lord of Heaven | reverent and prayerful | The Southern Heaven Demon Empress prays that the Lord of Heaven will remember her loyalty and love. |

## Listed compact profiles

### Blood Monk.md

# Blood Monk (혈승)

- **Safe through:** Chapter 679
- **Aliases:** None
- **Role:** The Blood Monk is an unidentified, apparently middle-aged bald and beardless martial artist who carries a steel Zen staff and has killed several hundred people in Guizhou; his current destination is unknown.
- **Personality:** Unknown; the captured witness who described him was unable to provide further information before dying.
- **Voice:** Not established.
- **Relationships:** His connection to Dark Heaven and Nanman is unknown.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 709
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 701
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 709
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, and a publicly recognized S-rank-level Hunter who formally retains an A-rank license; he returned to fight the Southern Heaven Demon Empress, drove White Flame through her chest, and now stands at death's door with his heart meridian torn.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 709
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 709
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress is Honglan, creator of the rift behind the Inner Palace; she survives the explosion that follows Baeksang's ambush, retains some innate qi, is critically wounded after Jin Taekyung drives White Flame through her chest, and loses her only arm to an unidentified attacker while attempting to kill him.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

## Korean source

```text
＃710화



느껴진다. 눈앞까지 드리운 죽음이.

흐릿해진 시야는 사물의 형체조차 제대로 분간하지 못하고, 날카롭던 감각은 몸뚱어리를 떠날 준비를 끝마치고 있다.

그 어둡고 몽롱한 의식 속에서, 진태경은 생각했다.

틀림없다.

이건 꿈이다. 아니면 가까워진 죽음과 함께 찾아온 환청이거나.

그렇지 않고서야, 지금 등 뒤에서 들려오는 이 목소리를 설명할 방법이 없었다.

“감히 누구의 몸에 손을 대려는 것이냐, 이 호로 잡년아.”

그럼에도…… 닮았다.

신경질적으로 들릴 만큼 카랑카랑한 목소리도, 저 걸쭉한 욕설도 한 사람을 떠올리게 만든다. 그런 일은 벌어지지 않을 거라는 사실을 아는데도. 말도 안 되는 생각이라 자책하면서도 헛된 희망을 품게 만든다.

‘정말 죽을 때가 됐나.’

공허한 뇌까림이 마음속에서 울려 퍼지던 그 순간.

“그래서…… 네놈은 언제까지 그리 넋 놓고 있을 셈이냐?”

“……!”

스르륵 감기려던 진태경의 눈꺼풀이 우뚝 멈췄다.

찰나 지간 찾아온 거대한 충격에 닫혀 가던 정신이 깨어나고, 멀어진 감각들이 돌아온다.

‘설마.’

아니다. 아닐 것이다.

그건 있을 수 없는 일이니까. ‘그’는 머나먼 중원 어딘가에 있어야 할 사람이었으니까.

하지만 누군가 그랬다.

인간을 무너트리는 것도, 다시 일으켜 세우는 것도 결국 희망이라고. 그렇기에 진태경은 보이지 않는 희망의 끈을 붙잡으며 눈을 떴다.

그리고 볼 수 있었다.

“아. 아아…….”

양팔을 모두 잃은 채, 신형을 비틀거리는 남천마후의 모습을.

그리고 경악과 의문에 사로잡힌 그녀의 옆에 비스듬히 꽂혀 있는 한 자루의 선장(禪杖)을.

쩔그럭.

선장에 매달린 고리가 요란한 소리를 토해 낸다.

불그스름하게 달아오른 그것으로부터 흘러나온 열양지기(熱陽之氣)를 느낀 진태경이 흐릿한 미소와 함께 입을 열었다.

“거…… 일찍 좀 오시지.”

바로 옆에서 귀를 기울여야만 들을 수 있을 만큼 희미한 목소리.

그러나 선장의 주인은 달랐다.

그는 수백여 장 밖이어도, 아니 설령 수백 리를 떨어져 있다 하더라도 진태경의 목소리를 들을 수 있을 것이다.

귀가 아닌 마음으로.

하나뿐인 제자를 향한 마음으로.

“좀 늦을 수도 있지, 어린놈이 구박은.”

마음과는 달리 퉁명스럽게 대답한 혈승(血僧), 아니 화왕(火王) 적천강이 걸음을 내디뎠다.

저벅.

그리고 다음 순간.

화륵.

모든 무대가 끝나고 찾아온 암전(暗轉) 속에서, 그 어떤 것보다 크고 맹렬한 불꽃이 솟구쳤다.

콰아아아아!

화염신장(火焰神掌).

끔찍한 열기를 머금은 불길의 파도가 어둠을 살라 먹으며 나아간다. 거침없으며 끝없이, 오직 한 존재를 불태우기 위해서.

‘아.’

남천마후는 텅 빈 눈으로 다가오는 열기를 바라보았다.

외마디 신음도, 비명도 입 밖으로 흘러나오지 않는다. 발은 못 박힌 것처럼 지면에 고정되어 있었고, 양팔의 고통은 멀게만 느껴졌다.

‘피해야 하는데. 어떻게든 피해야 하는데…….’

머리에서 계속되는 외침을 몸이 받아들이지 못한다.

아니, 어쩌면 하나뿐이었던 팔을 잃은 그 순간 모든 것이 끝났을지도 모른다.

섬광이라 착각할 만큼 빠르고, 강대한 열기를 머금고 있던 한 자루의 선장이 잿가루로 만든 것은 그녀의 팔뿐만이 아니다.

선천지기(先天之氣).

오직 한 사람의 최후를 장식하기 위하여 남겨 두었던 그 마지막 한 줌의 힘마저 앗아 가 버렸다. 무심히, 그리고 무참히.

이제는 한 걸음 내뻗을 힘조차 남아 있지 않은 자신을 관조하며, 남천마후는 비로소 깨달았다.

‘끝이구나.’

실로 길었던 인생. 그 시작이 정확히 어디쯤이었는지는 모르겠으나, 오늘 이 자리가 그녀의 마침표일 것이다.

그럼에도 마지막까지 남은 후회가 있다면, 그것은 진태경의 숨통을 직접 끊어 놓지 못한 것에 대한 아쉬움뿐이리라.

‘하지만…… 괜찮아.’

왜, 어떤 운명의 장난으로 화왕 적천강이 이곳에 왔는지는 모른다.

그러나 자신이 이곳에서 쓰러지는 것처럼, 진태경 역시 죽음을 피할 수 없을 것이다.

설령 화왕이 아니라 대라신선(大羅神仙)이 온다 해도 그 사실은 변치 않는다.

이 흔들리지 않을 한 가지 확신이, 불길을 받아들이는 남천마후의 마음을 편안케 했다.

‘천주시여.’

마음속에서 나지막하게 울려 퍼지는 부름.

상념은 길었으나 순간은 짧았고, 무릎 꿇은 진태경의 머리 위로 쏘아진 불꽃은 남천마후를 향해 아가리를 벌렸다.

화아아악!

어둠을 녹이며 쏟아지는 광염(光焰)을 바라보며, 남천마후는 눈을 감았다.

아니, 눈을 감으려 했다.

모든 것이 새하얗게 물들던 그때, 손 하나 까딱할 힘조차 남아 있지 않은 몸뚱어리를 덮치는 누군가의 신형이 아니었다면 그러했을 것이다.

와락!

찰나를 쪼개고 쪼갠 짧은 순간 속, 남천마후는 똑똑히 볼 수 있었다.

“……!”

죽음을 앞두고 창백하게 질린 진태경의 얼굴과, 느려진 세상 속에서 서서히 벌어지는 그의 입술을.

그리고.

콰득!

목으로부터 전해지는 아릿한 고통과 함께, 남천마후의 시야가 어둠으로 물들었다.



* * *



그것은 피할 수 없는 현실인 동시에, 섬광과도 같은 깨달음이었다.

‘지금 남천마후가 죽으면, 나도 죽는다.’

지금까지 나보다 윗줄의 강자들과 맞붙으면서도 살아남을 수 있었던 가장 큰 이유는, 레벨 업으로 말미암은 회복 덕분이었다.

제아무리 근골이 뛰어나고 여러 능력치를 높여 놔도 확실한 죽음만큼은 막지 못한다.

지금의 나처럼 혈도가 박살 나고, 원위치에서 올바른 기능을 수행해야 할 십이지장이 휴가 나온 군인처럼 위수 지역을 벗어난 경우에는 더더욱 그렇다.

그런데 이런 상황에서 남천마후가 내가 아닌 다른 사람의 손에 죽는다?

그럼 나까지 좆 되는 거다.

결국, 마지막 순간 내게 주어진 선택지는 하나뿐이었다.

몸빵.

‘시발.’

나직한 욕설을 삼키며, 나는 젖먹던 힘까지 쥐어 짜내어 몸을 튕겼다.

아니, 간신히 몸을 일으켜 남천마후의 신형을 덮쳤다고 하는 것이 더 옳은 표현일 것이다.

와락!

“……!”

체념한 듯 감겨가던 눈이 부릅떠지는 것이 보였다.

경악과 의문. 두 가지 감정이 소용돌이치는 남천마후의 눈동자가 목소리를 대신하여 묻는 듯했다.

도대체 왜?

하지만 대답해 줄 이유도, 그럴 만한 시간도 없다.

그 정도의 여유와 힘이 남아 있었다면 몇 걸음 뒤에 떨어진 백염을 주웠거나, 인벤토리에서 다른 무기를 꺼내 남천마후의 심장에 박아 넣었을 것이다.

그런데…… 빌어먹을. 당장이라도 끊어질 것 같은 정신을 붙잡으며 할 수 있는 최선의 공격이라곤, 결국 이것뿐이다.

콰득!

검버섯이 핀 주름진 피부가 힘없이 뜯겨 나간다. 비릿한 핏물이 입안을 가득 채우고, 바싹 마른 입술을 축축하게 적셨다.

지금까지 겪은 모든 전투를 통틀어, 가장 원초적이며 원시적인 공격. 그렇기에 어느 때보다 간절했던 일격.

그리고 남천마후의 목울대를 한입 가득 물어뜯은 나는, 다음 순간 등 뒤로 전해지는 어마어마한 열기를 느꼈다.

비명과도 같은 누군가의 외침도 함께.

“안-!”

화륵, 퍼어어엉!

등줄기를 강타하는 엄청난 충격. 이어지려던 외침마저 집어삼킨 굉음이 끔찍한 열기와 함께 사방을 휩쓸었고, 나는 붕 뜬 듯한 부유감(浮游感)을 느끼며 튕겨 나갔다.

‘아.’

누가 그랬던가. 인간이 느낄 수 있는 통증 중 가장 큰 고통은, 불에 의한 작열통(灼熱痛)이라고.

그리고 그 말은 틀림없는 사실이었다.

비명조차 새어 나올 수 없는 끔찍한 고통이 전신을 사로잡는다.

새하얗게 물든 시야는 한 치 앞도 분간할 수 없었고, 거대한 충격을 이기지 못하고 튕겨 나간 몸뚱어리는 그저 맹렬한 속도로 바람을 가를 뿐이었다.

쐐애애애액, 콰앙!

영원히 계속될 것만 같던 세찬 파공성이 끝나고, 거칠고 단단한 무언가가 전신을 후려친다.

아니, 빛살처럼 쏘아진 내 몸이 잔해를 부수며 틀어박혔다고 하는 것이 옳았다.

쿨럭.

발은 기침과 함께 이제 얼마 남지도 않았을 핏물이 입가를 타고 흘러나온다.

이미 터져 나간 고막에서는 벌 떼 우는 소리가 요란하고, 흐릿한 시야 너머에서는 힘없이 널브러진 남천마후의 모습과 누군가의 인영이 아지랑이처럼 일렁이고 있었다.

“안 돼-!”

그리고, 비명과도 같은 외침이 울려 퍼진 그 순간.

띠링.

귓가를 파고드는 맑은 종소리와 함께, 따스한 온기가 나를 감싸 안았다.



* * *



쐐애애액!

지금 이 순간. 전력을 다해 신형을 내딛는 적천강의 마음은 절망으로 가득했다.

‘안 돼. 안 된다.’

한 걸음, 한 걸음이 무겁다.

백 년이 넘는 세월을 살아오며 늙어 버린 가슴은 그 어느 때보다 가파르게 요동쳤고, 빠르게 가까워지는 한 사람에게 못 박힌 눈동자는 파르르 떨리고 있었다.

진태경.

그의 생애 두 번째이자, 하나뿐인 제자.

그리고 죽음만을 바라던 자신에게 어느 날 문득 찾아와, 살아가야 할 이유를 깨닫게 해 주었던 유일한 불씨.

‘그런데. 그런데 도대체 왜!’

당장이라도 피를 토할 것만 같은 심정이었다.

그가 남천마후를 향해 쏘아 보냈던 것은 자그마치 십이성(十二成)의 경지에 이른 화염신장이다.

한데 강철마저 녹여 버리는 그 끔찍한 열기를, 난데없이 진태경이 막아선 것이다.

‘이 미친놈. 멍청한 놈 같으니!’

이유는 모른다. 아니, 이유 따윈 중요하지 않았다. 미처 토해 내지 못한 욕설 역시 적천강 자신을 향한 것이었다.

진태경의, 하나뿐인 제자의 선택은 언제나 옳았고 그만한 이유가 있었으니까.

그저 자신의 성급한 판단으로 진태경을 잃게 되었다는 슬픔과 자책만이 적천강의 마음을 갈기갈기 찢어 놓았다.

“안 돼!”

비명과도 같은 외침과 함께, 늙은 스승의 발걸음이 마침내 제자의 앞에서 멈추었다.

“태경아! 이놈아!”

간절함이 담긴 부름에도 들려오지 않는 대답.

힘없이 눈을 감은 채, 금방이라도 끊길 것처럼 미약한 호흡을 내뱉는 진태경의 모습을 확인한 적천강의 가슴이 쿵, 하고 내려앉았다.

‘아.’

눈앞이 아득해지는 충격.

본래의 형태를 거의 찾아볼 수 없을 정도로 산산이 부서진 갑옷과 기이하게 뒤틀린 사지.

거기에 더해 화염신장의 열기를 이기지 못하고 녹아내리거나 부서진 살과 뼈까지.

갑옷 덕분인지 기적적으로 숨이 붙어 있지만, 그뿐이다.

이제 저 어린것에게 남아 있는 시간은 촌각(寸刻)에 불과했다.

적천강이 온 힘을 다해 공력을 불어 넣는다 해도, 그 사실은 달라지지 않는다.

아니, 오히려 고통만 길어질 것이다.

툭.

진태경의 완맥을 집으려던 손이 허공에서 파르르 떨렸다.

‘……죽어? 죽는다고? 저 녀석이?’

이 믿을 수 없는 현실 속, 차마 눈앞에서 죽어 가는 진태경을 지켜볼 수 없던 적천강은 눈을 질끈 감았다.

지금껏 수많은 죽음을 겪어 왔던 그다.

때로는 먼 발치에서 눈으로 지켜보았고, 혹은 이 손으로 직접 누군가의 숨통을 끊기도 했다.

하지만…… 진태경의 죽음은, 저 아이의 죽음은 다르다.

이제 고작 약관을 넘겼을 뿐이다. 늙은 자신과는 달리 앞으로 살아갈 날도, 누려야 할 행복도 차고 넘쳤다.

“한데 무엇이…… 무엇이 그리 급하여 벌써 떠나느냐. 왜!”

적천강은 피를 토해 내는 심정으로 부르짖었다.

자신의 무공에 의해 반쯤 녹아내린 진태경의 손을 잡고서. 그 처참한 부상의 흔적이 남아 있는 손을 붙잡고 하염없이 울었…….

‘응?’

문득 이상한 촉감을 느낀 적천강은 눈을 떴다.

축축하게 젖은 그의 두 눈에 진태경의 손이 비친다.

태어난 지 얼마 되지 않은 아기처럼 뽀얗고, 그 와중에 핏줄까지 울뚝불뚝 서 있는 손등이.

“……?”

이상한 일이다. 조금 전에는 분명히 살이 녹아 눌어붙어 있었는데. 심지어 뼈도 좀 보였던 것 같은데.

‘뭐지, 이거.’

아무리 생각해 봐도 둘 중 하나다. 그 염병할 노환이 재발했거나, 그게 아니면…….

꿀꺽.

저도 모르게 마른침을 삼킨 적천강은 슬며시 고개를 들었다.

그리고 다음 순간, 그는 볼 수 있었다.

흥미로운 눈빛으로 자신을 바라보고 있는 한 쌍의 눈동자를.

“……?”

“……?”

“……!”

“……!”

짧은 눈빛 교환과 함께 우뚝 굳어 버린 적천강을 향해, 진태경이 쑥스러운 듯이 손가락을 꼬물거렸다.

“그, 우선 손부터 좀 빼고 얘기할까요?”
```

## Final English reading copy

```markdown
# Chapter 710

He could feel it. The death hanging right before his eyes.

His blurred vision could no longer distinguish even the shapes of things, and his once-sharp senses had finished preparing to leave his body.

Within that dark, hazy consciousness, Jin Taekyung thought.

*No doubt about it.*

*This is a dream. Or maybe a hallucination brought on by the death drawing near.*

There was no other way to explain the voice coming from behind him.

“Just whose body do you think you’re laying a hand on, you fucking bitch?”

And yet… it sounded so much like him.

The shrill voice, sharp enough to sound irritable, and those thick curses both brought one person to mind. Even though he knew that person could not possibly be here. Even while he scolded himself for entertaining such an absurd thought, it filled him with foolish hope.

*Has it really come time for me to die?*

At the exact moment that empty mutter echoed through his mind—

“So… how long do you intend to keep sitting there with your head in the clouds?”

“……!”

Jin Taekyung’s eyelids, which had been slowly closing, stopped abruptly.

A massive shock that arrived in an instant awakened his fading consciousness, and his distant senses returned.

*No way.*

*No. It can’t be.*

That was impossible. *He* was supposed to be somewhere in the distant Central Plains.

But someone had once said that hope was what broke human beings down—and what raised them back up again. So Jin Taekyung clung to that invisible thread of hope and opened his eyes.

And then he saw.

“Ah. Aah…”

The Southern Heaven Demon Empress, staggering with both arms gone.

And a single Zen staff planted at an angle beside her as she stood gripped by shock and confusion.

Clatter.

The rings hanging from the Zen staff gave off a terrible racket.

Feeling the Scorching Yang Qi flowing from the staff, which had been heated to a reddish glow, Jin Taekyung opened his mouth with a faint smile.

“Well… you could’ve come a little sooner.”

His voice was so faint that it could be heard only by someone listening right beside him.

But the owner of the Zen staff was different.

He could have heard Jin Taekyung’s voice even from several hundred jang away. No—even from several hundred ri away.

Not with his ears.

With his heart.

With the heart he held for his one and only Disciple.

“I can be a little late, can’t I? What’s with the abuse, you brat?”

Contrary to what he felt inside, Blood Monk—or rather, Fire King Jeok Cheongang—answered gruffly as he took a step forward.

Thud.

And then, the next moment—

Whoosh!

In the blackout that came after the entire stage had ended, a flame larger and more ferocious than anything else burst into being.

Kraaaaaash!

Flame Divine Palm.

A wave of fire filled with horrifying heat advanced through the darkness, devouring it as it went. Without hesitation and without end, it moved for the sole purpose of burning one being.

*Ah.*

The Southern Heaven Demon Empress stared at the approaching heat with hollow eyes.

Neither a groan nor a scream escaped her lips. Her feet were fixed to the ground as though nailed there, and the pain in her missing arms felt distant.

*I have to dodge. Somehow, I have to dodge…*

Her body could not accept the cry that continued inside her head.

No—perhaps everything had ended at the moment she lost her one remaining arm.

The Zen staff that had moved so quickly she could have mistaken it for a flash of light, carrying overwhelming heat, had turned more than just her arm into ash.

Her innate qi.

Even that final handful of strength she had saved to adorn the end of only one person’s life had been stolen away. Indifferently, and mercilessly.

As she observed herself, with not even enough strength left to take a single step, the Southern Heaven Demon Empress finally understood.

*It’s over.*

Her life had been truly long. She did not know exactly where it had begun, but this place, today, would be the period at its end.

Even so, if she had one regret left until the very end, it would only be that she had failed to personally cut off Jin Taekyung’s breath.

*But… it’s all right.*

She did not know why, or because of what trick of fate, Fire King Jeok Cheongang had come here.

But just as she would fall here, Jin Taekyung would be unable to escape death either.

Even if the one who had come was not the Fire King but the Great Firmament Immortal, that fact would not change.

That one unshakable certainty soothed the heart of the Southern Heaven Demon Empress as she accepted the flames.

*Lord of Heaven.*

The call echoed softly within her heart.

Her thoughts had been long, but the moment was brief. The flames shot over Jin Taekyung’s kneeling head opened their maw toward the Southern Heaven Demon Empress.

Whoooosh!

As she watched the light-flames pouring down and melting the darkness, the Southern Heaven Demon Empress closed her eyes.

No—she tried to close them.

And she would have, if someone had not suddenly thrown themselves over her body—too drained to move so much as a finger—just as everything turned white.

Whump!

Within that brief instant, split and split again into smaller pieces, the Southern Heaven Demon Empress saw everything clearly.

“……!”

Jin Taekyung’s face, pale with the approach of death, and his lips slowly parting in a world that had grown sluggish.

And then—

Crack!

Along with a sharp pain spreading from her throat, the Southern Heaven Demon Empress’s vision was swallowed by darkness.

* * *

It was both an unavoidable reality and an enlightenment that came like a flash of light.

*If the Southern Heaven Demon Empress dies now, I die too.*

The greatest reason I’d been able to survive while fighting experts a level above me was the recovery that came with leveling up.

No matter how outstanding my Muscles and Bones were or how many stats I’d raised, they couldn’t stop certain death.

Especially not when, like now, my acupoints had been blown apart and my duodenum—which was supposed to perform its proper function in its proper place—had gone AWOL like a soldier wandering outside his assigned area.

But what if the Southern Heaven Demon Empress died at someone else’s hands in a situation like this?

Then I’d be fucked too.

In the end, the only choice left to me in that final moment was one.

Tank it.

*Fuck.*

Swallowing a low curse, I squeezed out every last ounce of strength and threw myself forward.

No—it would be more accurate to say that I barely managed to raise my body and throw myself over the Southern Heaven Demon Empress.

Crack!

“……!”

I saw her eyes, which had been closing as though in resignation, snap open.

Shock and confusion swirled within the Southern Heaven Demon Empress’s eyes. They seemed to ask a question in place of her voice.

*Why?*

But I had neither a reason to answer nor the time to do so.

If I’d had that much strength and leisure left, I would have picked up White Flame, which had fallen a few steps away, or pulled another weapon from my Inventory and driven it into the Southern Heaven Demon Empress’s heart.

But… damn it. While clinging to consciousness that felt ready to snap at any moment, this was the best attack I could manage.

Crack!

Wrinkled skin mottled with age spots tore away helplessly. The metallic tang of blood filled my mouth, wetting my parched lips.

Of all the attacks I had used in every battle I’d fought so far, this was the most primal and primitive.

Which was why it was more desperate than any attack before it.

And after taking a huge bite out of the Southern Heaven Demon Empress’s throat, I felt an enormous heat reach me from behind.

Along with someone’s scream.

“No—!”

Whoosh! Boom!

An immense impact struck my back. The roar that swallowed even the scream that had been about to continue swept through the surroundings along with horrifying heat, and I felt my body float before I was thrown away.

*Ah.*

Who had said that the greatest pain a human being could feel was burning pain?

They had been absolutely right.

Horrifying pain, too terrible even for a scream to escape, seized my entire body.

My vision had turned pure white, leaving me unable to distinguish even an inch in front of me, and my body, thrown away by the massive impact, did nothing but cut through the air at tremendous speed.

Screeeeeech—boom!

The fierce sound of air splitting, which seemed as though it would continue forever, finally ended, and something rough and hard struck my entire body.

No. It would be more accurate to say that my body, shot forward like a ray of light, smashed through the rubble and buried itself in it.

Cough.

With a cough, what little blood I had left trickled from the corner of my mouth.

My eardrums had already burst, and the buzzing of a swarm of bees roared in my ears. Beyond my blurred vision, the Southern Heaven Demon Empress lay sprawled helplessly, while someone’s silhouette wavered like a heat haze.

“No!”

And at the moment a scream-like cry rang out—

Ding.

Along with the clear ringing of a bell in my ear, a gentle warmth enveloped me.

* * *

Screeeeeech!

At that moment, Jeok Cheongang threw himself forward with all his strength, his heart filled with despair.

*No. It can’t be.*

Each step was heavy.

His heart, aged by more than a century of life, was pounding more violently than ever, and his eyes, fixed on the person rapidly drawing closer, trembled.

Jin Taekyung.

The second—and only—Disciple of his life.

The one and only ember who had suddenly entered the life of a man who had wanted nothing but death and made him realize that he had a reason to live.

*But why? Why the hell would he do that?*

He felt as though he were about to vomit blood.

What he had unleashed at the Southern Heaven Demon Empress was the Flame Divine Palm, driven to a staggering twelve-tenths of its normal limit.

And Jin Taekyung had suddenly blocked that horrifying heat, powerful enough to melt steel.

*You crazy bastard. You stupid bastard!*

He did not know why. No, the reason did not matter.

The curses he had been unable to spit out were directed at himself as well.

The choice made by Jin Taekyung, his one and only Disciple, had always been right. There had always been a reason for it.

But the sorrow and self-reproach of losing Jin Taekyung because of his own hasty judgment tore Jeok Cheongang’s heart to shreds.

“No!”

Along with that scream, the old Master’s footsteps finally stopped before his Disciple.

“Taekyung! You bastard!”

But no answer came to his desperate call.

Jeok Cheongang saw Jin Taekyung lying there with his eyes closed, breathing so faintly that it seemed his breath might stop at any moment, and his heart sank with a heavy thud.

*Ah.*

The shock made his vision swim.

An armor shattered so thoroughly that almost none of its original shape remained. Limbs twisted at unnatural angles.

And on top of that, flesh and bones that had melted or broken beneath the heat of the Flame Divine Palm.

Perhaps thanks to the armor, he was miraculously still breathing.

But that was all.

The time remaining to that young boy amounted to no more than moments.

That fact would not change even if Jeok Cheongang poured every last bit of his internal energy into him.

No—it would only prolong his pain.

Tap.

The hand reaching to take Jin Taekyung’s wrist pulse trembled in midair.

*…Dying? He’s dying? That boy?*

Unable to bear watching Jin Taekyung die before his eyes in this unbelievable reality, Jeok Cheongang squeezed his eyes shut.

He had witnessed countless deaths throughout his life.

Sometimes he had watched from far away. Sometimes he had personally cut off someone’s breath with these hands.

But… Jin Taekyung’s death was different.

That child’s death was different.

He had barely passed twenty. Unlike Jeok Cheongang, he had an abundance of days left to live and happiness left to enjoy.

“Then what could have been… what could have been so urgent that you had to leave already? Why!”

Jeok Cheongang cried out as though he were spitting blood.

He held Jin Taekyung’s hand, which had been half melted by his own martial arts. Holding that hand, still bearing the marks of those horrific injuries, he wept his heart out…

*Huh?*

Jeok Cheongang opened his eyes when he felt something strange beneath his fingers.

His tear-filled eyes reflected Jin Taekyung’s hand.

The back of it was pale and smooth like a newborn baby’s, and yet the veins stood out in thick ridges.

“……?”

It was strange. A moment ago, the flesh had clearly been melted and fused together.

He even thought he had seen some of the bone.

*What the hell is this?*

No matter how he thought about it, there were only two possibilities.

Either those damned infirmities of old age had returned, or else…

Gulp.

After swallowing dryly without realizing it, Jeok Cheongang slowly raised his head.

And then, the next moment, he saw.

A pair of eyes gazing back at him with interest.

“……?”

“……?”

“……!”

“……!”

After a brief exchange of glances, Jeok Cheongang froze rigidly.

Facing him, Jin Taekyung wiggled his fingers sheepishly.

“Um, how about you let go of my hand first, then we talk?”
```
