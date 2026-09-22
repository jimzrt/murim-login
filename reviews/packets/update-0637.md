<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0637.txt",
      "sha256": "1ec814eb99196e7431197a7e18976796bf9adaffffc3be000f4c2874ae3e1b18",
      "bytes": 13877
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "3ffb72ebbde07fc08340843ecb4d82b238b321d5e5dcc0b6bab6e074c67cd420",
      "bytes": 1695
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "81d1081a05e49c53a860fdf322d308196aa3e87b75a32564583c40e7c0d00329",
      "bytes": 196347
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "a6ca2e6329887a8d35f618cfcd6b67542c898fcfc61a6cf7e0b66f7007d18e93",
      "bytes": 529
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "1961c18fbbb49929ae523f7ba0af27c785f64fbe3b1506695b4995bb4802ec4e",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "0b942c361cdb9bcf538cecb5d3921f775eae93af54d730de033f588f7d8fed42",
      "bytes": 1936
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "e133c617707c489176a2848057482ed2b13910f5ccf29df32dbeccf56faae006",
      "bytes": 622
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "ce5a82c293c59d1f7cafa3604dd6622d175d940aba1a01a836cc504178d83738",
      "bytes": 528
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "bf22c5aeb9cf49fe7934cba13184f676193085e9390da0dd6461da8b570b2bb5",
      "bytes": 202406
    }
  ],
  "estimated_tokens": 11088
}
-->

# Durable State Update — Chapter 637

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 637. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 637. Profile updates may replace only one
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
  "chapter": 637,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 637,
    "continuity_sources": [637],
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
    "Jin Taekyung and the Beast Miao King have entered the hidden Poisonblood Grounds inside Ailao Mountain.",
    "The Poisonblood Grounds is a deadly former Five Poisons Sect facility containing venomous creatures, lethal poisons, and a poisonous swamp.",
    "The Poisonblood Grounds outer region is covered by Poison Mist that penetrates through breathing and skin.",
    "The Beast Miao King seeks vengeance for the Nanman Beast Palace warriors who died in the Poisonblood Grounds.",
    "Baeksang's grandfather, a former Palace Lord and legendary Bai warrior, died inside the Poisonblood Grounds.",
    "Jin's Myriad-Poison Ring removes the Poisoned status abnormality caused by the Poison Mist.",
    "The Beast Miao King is currently affected by Mildly Poisoned and has received Jin's High-Grade Poison-Warding Pearl.",
    "Jin accepted the chain Quest My Good Sir, Do Not Cross That Swamp."
  ],
  "continuity_sources": [
    636
  ],
  "open_questions": [
    "What lies deeper inside the Poisonblood Grounds?",
    "Can Jin and the Beast Miao King cross the poisonous swamp and survive the inner region?",
    "What caused the earlier Nanman expeditions, including Baeksang's grandfather, to be completely wiped out?",
    "Is Dark Heaven or the Southern Heaven Demon Empress connected to what awaits inside the Poisonblood Grounds?"
  ],
  "safe_through": 636,
  "temporary_decisions": [
    "Use Poisonblood Grounds for 독혈지.",
    "Use Beast Bai King for 야수백왕.",
    "Use Myriad-Poison Immunity for 천독불침.",
    "Retain the colloquial wording of My Good Sir, Do Not Cross That Swamp for the chain Quest title."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 일신     | **One God**         |
| 십왕     | **Ten Kings**       |
| 소림     | **Shaolin**                      |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 중원     | **Central Plains**                               |                                                       |
| 문주     | **Sect Leader**                              |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 사천     | **Sichuan**            |
| 정마대전   | **Great Faction War**         |
| 대사      | **Master** for a senior Buddhist monk                           |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 사천당문 | **Sichuan Tang Clan** | Martial clan cited for its poison-based cleansing method. |
| 아마존 | **Amazon** | Region referenced in Taekyung's crude joke. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 중독 | **Poisoned** | System status abnormality caused by the poisons. |
| 녹옥불장 | **Green Jade Buddha Staff** | Ancient Shaolin sacred treasure carried by Hong Dao. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 불장 | **Buddhist Staff** | Generic term in Hong Dao's final words; the specific treasure is 녹옥불장. |
| 태산북두 | **Mount Tai and Northern Dipper of the Murim** | Honorific description of Shaolin's standing in the Murim. |
| 삼도천 | **Sanzu River** | Buddhist river associated with the boundary between life and death; footnote on first use. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 전광석화 | **Quick Attack** | Warlordmon’s rapid-movement command; used as a Pokémon-style gag. |
| 전광 | **Quick Attack** | Shortened form of Warlordmon’s rapid-movement command. |
| 수능 | **college entrance exam** | National university entrance examination taken by Hayeon. |
| 당문 | **Tang Clan** | Short form for the Sichuan Tang Clan. |
| 소림혈사 | **Shaolin Bloodshed** | Past incident cited by Hwangbo Eom. |
| 만독지환 | **Myriad-Poison Ring** | Quest title concerning a legendary treasure said to detoxify any poison. |
| 피독주 | **poison-warding pearl** | Poison-neutralizing artifact carried by the black-clad attackers. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 새외 | **Outer Lands** | Lands outside the Central Plains and its Murim. |
| 오독문 | **Five Poisons Sect** | Formerly dominant Nanman faction destroyed by the Fire Gate Clan. |
| 대전쟁 | **Great War** | The long war that ended after the Great Cataclysm. |
| 경상도 | **Gyeongsang-do** | Region used in Taekyung's joke about the word Mundi. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 백족 | **Bai people** | Ethnic group encountered in Yeongin. |
| 애뇌산 | **Ailao Mountain** | Mountain crossed by the party on the route to the Nanman Beast Palace. |
| 독혈지 | **Poisonblood Grounds** | Hidden poisonous region created by the Five Poisons Sect inside Ailao Mountain. |
| 독무 | **Poison Mist** | Deep green mist covering the Poisonblood Grounds swamp. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |

## Listed compact profiles

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 636
- **Aliases:** None
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace and the great chieftain of the Miao people.
- **Personality:** Fierce and vigilant when confronting threats to the Nanman Beast Palace.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace and is responsible for the forces stationed at Ailao Mountain.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 636
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 633
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance; he is a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license, and he has completed an unnamed cultivation technique designed for even the lowest-rank Hunter to learn without making it easily abusable.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 633
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 635
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

## Korean source

```text
＃637화



처음이었다.

이 정도로 길고 넓은 늪지대를 건너는 것도.

독무를 산 공기처럼 마셔 가며 인간이 아닌 것들과 싸우는 것도.

촤악!

난데없이 등 뒤에서 울려 퍼진 소리. 나는 부드럽게 몸을 선회하며 곧게 세운 수도(手刀)를 내리그었다.

서걱!

언뜻 보이는 몸길이만 해도 어림잡아 삼 장 이상.

그러나 날카로운 이빨도, 철갑처럼 두꺼운 가죽도 수도에 서린 기운을 막기에는 역부족이다.

아마존 관련 다큐멘터리에서 봤을 법한 거대한 악어가 반으로 갈라져 검게 물든 수면 위로 떨어졌다.

철벅!

비릿한 혈향과 그보다 더 고약한 악취가 흘러나왔지만, 잠깐 속이 메스꺼웠을 뿐 생각보다는 훨씬 괜찮았다.

이미 오물보다 더한 악취를 풍기는 점액질이며 핏물 따위를 전신 곳곳에 뒤집어쓴 지 오래였기 때문이었다.

‘무슨 이열치열(以熱治熱)도 아니고.’

남만 리빙 포인트 개꿀팁. 악취가 걱정되면, 더 고약한 악취에 익숙해지면 된다.

“……시발 거.”

잠깐 현타가 왔지만, 2교대 상하차보다 거지 같은 독혈지는 짧은 현자 타임마저도 허락하지 않았다.

쉬릭!

늪지대 사이에 숨어 있던 뱀이 목을 향해 화살처럼 튀어 오른다.

그리고 검고 날카로운 독니를 드러낸 놈이 내 허벅지를 향하여 입을 쩍 벌린 그 순간.

뻑!

거목의 나뭇가지처럼 두꺼운 손가락이 세모꼴의 대가리를 날려 버렸다.

의심의 여지가 없는 절명. 힘없이 떨어지는 뱀의 꼬리를 붙잡아 늪지대에 패대기친 야수묘왕이 진중한 표정으로 입을 열었다.

“긴당을 늦투디 마다.”

“긴당. 뭐요?”

“됴심하다고.”

“……아, 예.”

대충 해석하자면 긴장을 늦추지 마라. 조심해라. 뭐 그런 뜻인데.

팔순을 넘긴 남만 최고의 전사가 여덟 살짜리 초등학생보다 어설픈 발음이 된 건 입 한가득 물고 있는 피독주(避毒珠) 때문이었다.

“그이 다와따.”

방금 발음은 진짜 익숙한데.

혹시 고향이 경상도 쪽인지 물어보고 싶었지만 꾹 참았다. 그럴 상황도 아닐뿐더러, 야수묘왕의 말처럼 정말 늪지대가 끝나고 있기 때문이었다.

하지만 그렇다고 해서 상황이 호전된 것은 아니었다.

‘퀘스트 창 오픈.’

띠링.



퀘스트



[님아, 그 늪을 건너지 마오]



당신은 독혈지에 진입했습니다.

옛 오독문이 본거지로 삼았던 애뇌산, 그중에서도 가장 깊숙하고도 은밀하게 숨겨져 있던 이 장소에는 알 수도 없고, 알려지지도 않았던 생명체들이 살아가고 있습니다.

독이 스며든 운무(雲霧)와 수많은 망자의 넋으로 가득한 저주받은 땅.

이 너머에 무엇이 당신을 기다리고 있을지는 그 누구도 답해 주지 못합니다. 직접 눈으로 보고, 확인하는 수밖에는.



등급 : 초절정

제한 : 진태경

임무 : ???

보상 : ???

실패 : 사망





“…….”

이건 진짜 몇 번을 봐도 어이가 없네.

이렇게 간결한 퀘스트 창은 오랜만에 본다. 임무도, 보상도 명확하지 않지만 실패하면 넌 확실히 뒤짐이라니.

하지만 생각해 보면 늘 비슷했다. 현대의 게이트에서도, 무림에 와서도 마찬가지였던 것 같다.

‘이기면 살고, 지면 죽는다.’

간단하면서도 잔인한 논리였다.

헌터나 무림인이나, 결국 언제나 삼도천에 한 다리 걸쳐 놓고 살아가는 이들이니까.

그리고 지금껏 그랬듯이, 나는 이번에도 죽을 생각이 없었다.

철벅.

늪지대가 끝나자 비교적 무른 지면이 나타났다. 고약한 악취를 풍기는 점액질이 나와 야수묘왕의 발걸음을 따라 땅에 떨어질 때마다, 가뜩이나 거무스름한 주위의 땅이 더욱 검게 물드는 것이 보인다.

“지독하군.”

피독주를 뱉어 낸 야수묘왕이 주위를 둘러보며 말을 이었다.

“이런 끔찍한 곳은 태어나서 두 번째야.”

“첫 번째는 어딘데요?”

“정마대전. 가는 곳마다 지옥도가 펼쳐져 있었지.”

수십만에 달하는 이들이 서로를 죽고 죽인 초유의 대전쟁과 비교할 정도니, 독혈지가 어떤 곳인지는 덧붙일 설명이 필요 없었다.

솨아아아.

온통 검게 물든 땅을 뒤덮으며 다가오는 독무(毒霧). 그 스산한 광경에 야수묘왕이 침음성을 삼켰다.

“빌어먹을. 이럴 줄 알았으면 어렸을 때 독공(毒功)이라도 수련해 뒀어야 했는데.”

“이럴 줄 몰랐으니까 안 익히신 것 아닙니까?”

야수묘왕이 아쉬운 얼굴로 고개를 끄덕였다.

“맞다. 일신의 무공이면 충분하다고 생각했지. 그렇기 때문에 남들은 다 배우는 맹수 조련술도 익히지 않았던 거고.”

“그건 그렇죠. 필요 없는 걸 뭐하러 배웁니까.”

갑작스럽게 동질감이 느껴진다.

현대에 수포자와 영포자가 있다면, 남만에는 독포자와 맹포자가 있었다. 참고로 나는 수능 당시 전 과목을 모두 포기했다.

”그나저나 남만인들은 기본적으로 독공을 익히는 줄 알았는데요.”

“그럼 남만야수궁이 아니라 남만독궁이지 않았겠느냐?”

“……오.”

“중원인들의 편견이다. 남만 땅의 특성상 독을 쉽게 접할 수 있는 건 사실이지만, 대부분의 부족은 주로 맹수들을 다룬다. 오독문이 발호한 이후에는 더더욱 독을 배척하게 되었고. 본 궁 대대로 내려왔다는 신물(神物)만 보아도 알 수 있는 사실이다.”

“아. 그렇습니…… 예?”

지금 뭐라고?

순간 멈칫한 내가 야수묘왕을 빤히 바라보자, 그가 눈살을 찌푸리며 반문했다.

“왜?”

“아니, 방금 하신 말씀이요.”

“독공을 배척하게 되었다는 것? 심각한 피해를 입은 본 궁으로서는 당연한 일이었다.”

“그거 말고요. 신물 말입니다, 신물.”

“아. 그걸 말한 거였군. 나는 또 뭐라고.”

야수묘왕은 대수롭지 않게 대답했지만, 내 입장에서는 아, 그렇구나. 하고 넘어갈 만한 문제가 아니었다.

“남만야수궁에도 신물이 있었습니까?”

“전통이 있는 세력이라면 신물 하나쯤은 있는 법이지. 직접 보고 겪은 바에 의하면 중원의 경우에는 더더욱 심하더군.”

틀린 말은 아니다. 어지간한 중견 문파는 물론, 동네 무관에서도 있어 보이기 위해 낡은 철검 한 자루를 신물이랍시고 걸어 놓으니까.

하지만 그중에서도 진짜 신물이라 불릴 만한 물건이 있었다.

천년 간 명맥을 이어온 무림의 태산북두, 소림사의 신물인 녹옥불장(綠玉佛杖)이 바로 그것이었다.

그리고 암천은 무슨 이유에서인지 바로 그 신물들을 노리고 있다. 소림혈사(少林血史)라는 대사건을 일으키면서까지.

‘그런데 남만야수궁에도 그와 같은 신물이 있었다니.’

내가 알기로 남만야수궁의 역사는 삼백 년이 넘는다.

수십 개의 부족이 연합한 이 새외의 세력은 오독문과의 투쟁에서 생겨났고, 긴 싸움 끝에 남만의 패자가 되었다.

신물 하나쯤 있어도 이상할 건 없지만…… 중요한 건 이토록 중요한 이야기를 지금 처음 듣는다는 것이었다.

“그, 남만야수궁에 신물이 있다는 이야기는 못 들어 봤는데요.”

애써 침착하게 입을 연 나를 향해, 야수묘왕이 고개를 끄덕였다.

“당연하다. 본 궁이 세워진 지 얼마 되지 않아 사라졌으니까.”

“예?”

“아니, 애초에 없었을 수도 있겠군. 수왕석(獸王石)의 존재는 대대로 궁주들에게 전설처럼 내려져 오는 이야기라 실제 했는지에 대한 여부조차 확실하지 않다.”

“수왕석…….”

이름부터 범상치 않다. 내 나직한 뇌까림에 고개를 끄덕인 야수묘왕이 말을 이었다.

“앞서 말했듯이 전설 같은 이야기다. 천하의 모든 맹수를 따르게 할 수 있다는, 초대 궁주께서 지니고 계셨다는 신물이지. 오독문의 개파조사였던 초대 문주와의 일전에서 양패구상(兩敗毆傷)한 이후에는 사라졌다더군.”

돌멩이 하나에 천하의 모든 맹수를 다스릴 수 있는 불가사의한 힘이 서려 있다니. 말 그대로 전설이 따로 없다.

게다가 수백 년 전부터 구전(口傳)을 통해 내려오는 이야기.

당장 지금부터 작업을 시작한다면, 수백 년 후에는 나도 알에서 태어났다고 우길 수 있겠다.

‘뭐, 일단은 수왕석의 존재도 염두에 둬야겠지만…….’

지금으로서는 남천마후의 목적이 존재 여부조차 확실치 않은 전설 속의 수왕석이라는 것보다, 남만에 ‘균열’을 일으킨다는 쪽에 신빙성이 쏠릴 수밖에 없다.

“그런데 말이다.”

“예?”

불쑥 입을 연 야수묘왕이 나와 독무를 번갈아 바라보며 머뭇머뭇 말을 이었다.

“그거. 하나 더 없느냐?”

여기서 말하는 ‘그거’는 다름 아닌 만독지환이다.

나는 단호하게 대답했다.

“없습니다.”

“그럼 잠깐 빌리…….”

“어이, 야율 씨. 헛소리 말고 피독주나 물어.”

“……지금 뭐라고?”

“아. 순간 말이 헛나왔습니다. 중독되기 싫으면 피독주 물고 계세요.”

야수묘왕은 떨떠름한 눈빛으로 나를 노려봤지만, 이내 별말 없이 커다란 피독주를 입에 물었다.

비록 말석이라고는 하나 그는 십왕(十王)에 속할 만큼의 고수.

드높은 경지에 오른 무위와 웅혼한 공력을 지닌 만큼 독에 쉽게 당할 리는 없지만, 최소한의 예방책은 늘 필요한 법이다.

‘상급 피독주 정도면, 어지간한 독은 침투 못 하겠지.’

물론 사천당문의 신물인 만독지환을 끼고 있는 나야 말할 것도 없다.

그런 나를 부러운 눈빛으로 바라본 야수묘왕이 독무 속으로 발걸음을 옮겼다.

저벅.

유난히 크게 울려 퍼지는 발걸음 소리.

온 사방을 뒤덮은 진녹색의 안개는 한 치 앞도 알아볼 수 없을 만큼 짙었고, 이상하리만치 고요했다.

‘마치, 사냥감을 지켜보는 것처럼.’

희한한 일이었다. 짙은 독무 사이로 이곳을 바라보는 무언가의 시선이 느껴지는데도, 오히려 늪지대에 있을 때보다 주위가 잠잠하다는 것은.

그리고 이런 분위기를 느낀 것은 나뿐만이 아니었다.

- 십여 장 밖. 북서쪽 작은 풀숲. 알고 있느냐?

귓가를 파고드는 전음. 내가 작게 고개를 끄덕였다.

- 바위 옆 풀숲 말입니까?

- 그래. 뭔가가 있다. 혹시…….

나는 애뇌산의 망령을 떠올렸다. 놈에게서 느꼈던 유령 같은 기척과 빛살과도 같은 움직임을.

- 놈은 아닙니다. 만약 놈이라고 해도 이 거리라면 잡을 수 없을 거고요.

- 그건 하기 나름 아니겠느냐.

동시에 야수묘왕이 번개처럼 일장(一掌)을 뻗었다.

파앙!

압축된 공기가 터져 나가고 짙은 안개가 찰나의 순간 흩어진다.

일시적으로 밝아진 시야 너머로 쏘아진 막강한 장력이 풀숲을 폭풍처럼 휩쓰는 것이 보였다.

그리고…….

“커헉!”

비명이 있었다. 맹수가 아닌, 틀림없는 인간의 비명이.

“……!”

“……!”

일순간, 크게 뜨인 눈으로 서로를 마주본 나와 야수묘왕은 비명의 근원지를 향해 전광석화처럼 쇄도했다.

쐐애애액!

안개를 가로지르는 찰나의 시간 속, 많은 생각이 뇌리를 스쳤다.

그리고 그런 내 머릿속에 가장 먼저 떠오른 두 글자는 바로 암천(暗天)이었다.

‘놈들이다.’

남만의 금지인 애뇌산. 그중에서도 독혈지에 왜 사람이 있겠나.

찌릿한 무언가가 전신을 관통하는 듯했다.

나는 크게 요동치는 심장을 느끼며 십여 장의 거리를 순식간에 좁혔다.

그리고 풀숲에서 튕겨 나간 비명의 주인을 확인한 순간, 나도 모르게 얼빠진 음성을 흘렸다.

“이게 무슨……?”

입가에 묻은 검붉은 핏물. 부릅뜬 눈.

그건 틀림없는 인간의 시신이었지만, 나와 또 다른 누군가에게는 익숙하기 그지없는 복장을 하고 있었다.

“……백족의 전사가 왜 여기에.”

의문이 실린 야수묘왕의 공허한 목소리처럼, 조금 전까지만 하더라도 살아 있었던 시신의 정체는 바로 백족의 전사였다.

그리고 수의(壽衣)처럼 새하얀 옷을 걸친 채 숨이 끊어진 그의 몸뚱어리는 끈적하고 질긴 무언가로 칭칭 휘감겨 있었다.

‘밧줄. 아니, 실?’

도무지 이해할 수 없는 상황 속, 나와 야수묘왕의 눈동자가 크게 뜨인 바로 그때였다.

파슥. 파스스슥.

도대체 언제. 어디에 숨어 있던 것일까.

사방에서 다가오는 수많은 기척과 동시에, 문득 머리 위로 내려앉은 어둠을 느끼고 고개를 든 나는 마침내 볼 수 있었다.

스스스슥!

나이를 짐작할 수 없을 만큼 거대한 나무 위에서 유령처럼 내려오는 어떤 존재들을.

검은 몸통과 수많은 다리. 뻣뻣한 털이 달린 그것을 발견한 야수묘왕이 신음처럼 중얼거렸다.

“……천년지주(千年蜘蛛).”

독혈지의 괴물이 나타났다.
```

## Final English reading copy

```markdown
# Chapter 637

This was a first.

The first time I had crossed a swamp this long and wide.

The first time I had fought things that weren’t human while breathing Poison Mist like ordinary air.

*Splash!*

A sudden sound rang out behind me. I smoothly pivoted and brought down my straightened hand like a blade.

*Slash!*

Even its visible body length alone was easily more than three zhang.

But neither its sharp teeth nor its armor-thick hide could stop the qi imbued in my knife-hand.

The enormous crocodile looked like something I might have seen in a documentary about the Amazon. It split in half and fell onto the blackened surface of the water.

*Splash!*

A fishy scent of blood and an even more vile stench wafted out, but I only felt nauseated for a moment. It was much more bearable than I expected.

That was because I had already been covered from head to toe in slime and blood that smelled worse than sewage.

*This isn’t exactly fighting fire with fire.*

Nanman Life Pro Tip: If you’re worried about a bad smell, get used to an even worse one.

“……Fuck.”

I briefly came back to reality, but the Poisonblood Grounds, shittier than a two-shift loading-and-unloading job, didn’t even allow me a short moment of clarity.

*Swish!*

A snake hidden in the marsh shot toward my neck like an arrow.

And the moment the creature exposed its black, razor-sharp fangs and opened its jaws wide toward my thigh—

*Whack!*

Thick fingers, like the branches of a great tree, blew away its triangular head.

There was no doubt it was dead. The Beast Miao King grabbed the snake’s limp tail, slammed it into the swamp, and spoke with a serious expression.

“Dohn’ led yer gar’ down.”

“Don’t let my what?”

“Be gareful.”

“……Ah. Right.”

Roughly translated, he meant, Don’t let your guard down. Be careful. Something like that.

Nanman’s greatest warrior, now over eighty years old, was speaking less clearly than an eight-year-old because his mouth was stuffed with the poison-warding pearl.

“Almos’ dere.”

That pronunciation sounded awfully familiar.

I wanted to ask if his hometown was somewhere around Gyeongsang-do, but I held back. Not only was this no time for that, the swamp really was coming to an end, just as the Beast Miao King had said.

That didn’t mean our situation had improved, though.

*Open Quest Window.*

*Ding.*

> **System**
>
> **Quest**
>
> **My Good Sir, Do Not Cross That Swamp**
>
> You have entered the Poisonblood Grounds.
>
> In Ailao Mountain, once the headquarters of the former Five Poisons Sect, this place was hidden more deeply and secretly than anywhere else. Unknown and undiscovered life-forms dwell here.
>
> A cursed land filled with poisonous mist and the spirits of countless dead.
>
> No one can tell you what awaits you beyond this point. You have no choice but to see it with your own eyes and find out.
>
> **Grade:** Supreme Peak
>
> **Restriction:** Jin Taekyung
>
> **Mission:** ???
>
> **Reward:** ???
>
> **Failure:** Death

“……”

No matter how many times I looked at it, this was ridiculous.

It had been a long time since I had seen a Quest window this concise. The mission and reward were both unclear, but if I failed, I was definitely fucked.

Then again, it had always been similar. It had been the same in the modern world’s Gates, and it seemed to be the same after I came to the Murim.

*Win and live. Lose and die.*

It was a simple yet brutal logic.

Hunters and Murim practitioners alike were people who always lived with one foot in the Sanzu River.[^1]

And just as I had until now, I had no intention of dying this time either.

*Splash.*

When the swamp ended, relatively soft ground appeared. Every time the foul-smelling slime fell to the ground in the wake of my and the Beast Miao King’s footsteps, I could see the already blackish earth around us becoming even darker.

“Vile.”

The Beast Miao King spat out the poison-warding pearl and continued as he looked around.

“This is only the second place this horrible I’ve seen in my life.”

“What was the first?”

“The Great Faction War. Everywhere we went, hell was spread before our eyes.”

Since he was comparing this place to a war in which hundreds of thousands of people had killed one another, there was no need to elaborate on what kind of place the Poisonblood Grounds was.

*Fwoooosh.*

Poison Mist rolled toward us, covering the earth that had been dyed completely black. The Beast Miao King swallowed a groan at the grim sight.

“Damn it. If I had known this would happen, I should have trained in poison arts when I was young.”

“You didn’t know this would happen. Isn’t that why you didn’t learn them?”

The Beast Miao King nodded regretfully.

“That is true. I thought my own martial arts would be enough. That was also why I never learned the beast-taming techniques everyone else studied.”

“That makes sense. Why learn something you don’t need?”

I suddenly felt a strange sense of kinship.

If the modern world had people who gave up on math and people who gave up on English, Nanman had people who gave up on poison and people who gave up on beast taming. For the record, I had given up on every subject when I took the college entrance exam.

“Come to think of it, I thought people from Nanman all learned poison arts by default.”

“If that were true, wouldn’t this be the Nanman Poison Palace rather than the Nanman Beast Palace?”

“……Oh.”

“That is a prejudice held by people from the Central Plains. It is true that the nature of Nanman’s land means we encounter poison easily, but most tribes primarily deal with ferocious beasts. After the Five Poisons Sect rose to power, we rejected poison even more strongly. You can tell just by looking at the sacred treasure passed down through our Palace for generations.”

“Oh. Is that so…… Wait?”

What did he just say?

I stopped for a moment and stared at the Beast Miao King. He frowned and looked back at me.

“What?”

“No, it’s what you just said.”

“That we came to reject poison arts? For a Palace that suffered such severe damage, it was only natural.”

“Not that. I mean the sacred treasure. The sacred treasure.”

“Ah. That was what you meant. I thought you were asking about something else.”

The Beast Miao King answered as if it were nothing, but from my perspective, it wasn’t something I could simply brush off with an *Oh, I see.*

“The Nanman Beast Palace had a sacred treasure?”

“Any faction with a long tradition should have at least one sacred treasure. Judging by what I have personally seen and experienced, that is even more true of the Central Plains.”

He wasn’t wrong. Even small- and mid-sized sects, not to mention ordinary martial arts schools in the neighborhood, hung up an old iron sword and called it a sacred treasure to give themselves an air of importance.

But among those objects, there were also things that truly deserved to be called sacred treasures.

The Green Jade Buddha Staff, the sacred treasure of Shaolin Temple—the Mount Tai and Northern Dipper of the Murim, whose lineage had continued for a thousand years—was one such object.

And for some reason, Dark Heaven was targeting those very sacred treasures.

They had even caused the major incident known as the Shaolin Bloodshed to do so.

*But there was a sacred treasure like that in the Nanman Beast Palace too?*

As far as I knew, the history of the Nanman Beast Palace stretched back more than three hundred years.

This Outer Lands faction, formed through the alliance of dozens of tribes, had emerged from its struggle against the Five Poisons Sect and become the ruler of Nanman after a long war.

There was nothing strange about it having a sacred treasure or two, but……

The important thing was that I was only hearing about something this important for the first time.

“I’ve never heard that the Nanman Beast Palace had a sacred treasure.”

The Beast Miao King nodded at me as I forced myself to speak calmly.

“Of course not. It disappeared not long after the Palace was founded.”

“What?”

“Actually, it might never have existed in the first place. The existence of the Beast King Stone is a story passed down from Palace Lord to Palace Lord like a legend. We cannot even be certain that it was real.”

“The Beast King Stone……”

Its name alone was extraordinary. The Beast Miao King nodded at my quiet murmur and continued.

“As I said, it is a legendary tale. A sacred treasure said to have been carried by the First Palace Lord, one that could make every ferocious beast under heaven obey him. It supposedly disappeared after the First Palace Lord and the founding Sect Leader of the Five Poisons Sect grievously wounded each other in battle.”

A single pebble supposedly held the miraculous power to rule over every ferocious beast under heaven. It was nothing short of a legend.

And it was a story passed down by word of mouth for hundreds of years.

If I started working on it right now, then in a few hundred years, I could insist that I had been born from an egg.

*Well, I still have to keep the existence of the Beast King Stone in mind……*

For now, though, it was far more credible that the Southern Heaven Demon Empress intended to create a “rift” in Nanman than that her goal was the Beast King Stone, a legendary object whose existence was not even certain.

“Come to think of it……”

“Yes?”

The Beast Miao King suddenly spoke. He looked back and forth between me and the Poison Mist, then continued hesitantly.

“That. Do you have another one?”

The “that” he was referring to was none other than the Myriad-Poison Ring.

I answered firmly.

“No.”

“Then let me borrow it for a moment……”

“Hey, Mr. Yayul. Cut the nonsense and hold the poison-warding pearl in your mouth.”

“……What did you just say?”

“Ah. My tongue slipped for a moment. If you don’t want to get poisoned, keep the poison-warding pearl in your mouth.”

The Beast Miao King shot me a displeased look, but then put the large poison-warding pearl in his mouth without another word.

Though he held the lowest seat, he was still a master powerful enough to belong among the Ten Kings.

With martial prowess that had reached such a lofty realm and vast internal energy, he was not likely to succumb easily to poison. But a minimum level of prevention was always necessary.

*A High-Grade Poison-Warding Pearl should keep most ordinary poisons from penetrating.*

Of course, there was no need to mention me, since I was wearing the sacred treasure of the Sichuan Tang Clan—the Myriad-Poison Ring.

The Beast Miao King looked at me enviously before stepping into the Poison Mist.

*Step.*

The sound of his footsteps echoed unusually loudly.

The deep green mist covering every direction was so dense that I could not see even an inch ahead, and yet the surroundings were strangely quiet.

*As if something is watching its prey.*

It was strange. I could feel the gaze of something looking at us through the dense Poison Mist, and yet the area was quieter than it had been in the swamp.

And I was not the only one who sensed the atmosphere.

—A small patch of grass ten or so zhang away, to the northwest. Do you sense it?

A Sound Transmission pierced my ear. I gave a small nod.

—The grass beside the rock?

—Yes. There is something there. Could it be……

I thought of Ailao Mountain’s Wraith. The ghostlike presence I had felt from it, and its ray-like movements.

—It isn’t the wraith. Even if it were, we couldn’t catch it from this distance.

—That depends on how we go about it.

At the same time, the Beast Miao King thrust out one palm like lightning.

*Boom!*

Compressed air exploded, and the thick mist scattered for a brief instant.

Beyond the temporarily brightened field of vision, I saw the powerful palm force sweep through the grass like a storm.

And then……

“Guh!”

There was a scream. Not the cry of a beast, but unmistakably the scream of a human.

“……!”

“……!”

Our eyes widened as we looked at each other. Then the Beast Miao King and I shot toward the source of the scream with lightning speed.

*Whoooosh!*

In the brief instant it took to cut through the mist, countless thoughts flashed through my mind.

But the first two words that came to me were Dark Heaven.

*It’s them.*

Who else could be inside Ailao Mountain, the forbidden land of Nanman—and specifically the Poisonblood Grounds?

Something sharp seemed to pierce through my entire body.

Feeling my heart pound violently, I closed the distance of more than ten zhang in an instant.

And the moment I confirmed the owner of the scream who had been flung out of the grass, a dazed voice slipped from my lips.

“What the hell……?”

Dark red blood stained the corner of his mouth. His eyes were wide open.

There was no doubt that he was a human corpse, but he was wearing clothing that was painfully familiar to both me and someone else.

“……Why is a Bai warrior here?”

Like the Beast Miao King’s hollow voice, filled with confusion, the identity of the corpse that had been alive only moments ago was none other than a Bai warrior.

His body, dressed in white garments like a burial shroud, had been tightly wrapped in something sticky and tough.

*Rope. No, thread?*

In a situation I could not begin to understand, the Beast Miao King and I stared wide-eyed.

That was when—

*Rustle. Rustle-rustle.*

When had they gotten there? Where had they been hiding?

Along with the countless presences approaching from every direction, I suddenly felt darkness settle over my head. I looked up.

And at last, I saw them.

*Hissss!*

Some beings descended like ghosts from a tree so enormous that it was impossible to guess its age.

They had black bodies, countless legs, and stiff hair covering them. The Beast Miao King discovered them and muttered like he was groaning.

“……Thousand-Year Spiders.”

The monster of the Poisonblood Grounds had appeared.

[^1]: The Sanzu River is a Buddhist river associated with the boundary between life and death.
```
