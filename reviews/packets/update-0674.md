<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0674.txt",
      "sha256": "2810e22a83cafab69f47eaa7794b135c2380d1ec6ff14dc5e1ecf7e1abcdfb7a",
      "bytes": 12596
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "a902e1daa8b31aee20f566a69528a701f844261a5eec3157ec0a66ae666f8713",
      "bytes": 1536
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "80b345a0c7646596083558bdf3d611b39dc2d916686d38b53e0fbcf0569fd8de",
      "bytes": 202786
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "bbf696eb9ad908d0db38183f238ef5d3cd1c27315c87aed7a2dda00b319ce8a4",
      "bytes": 1006
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "72bf3bc505e80f473b6d24fd7bebd0ac8679f553e417d3a518889a7a91dc3ccb",
      "bytes": 830
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "0ce036b4880974974a5bf72736b768aac274afa1b9f9d66a7030ab01ec1a9388",
      "bytes": 553
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "3b5ea43ce1128167dbc423dc1f32050352e0e3911355cea255e5a6f2d04421b6",
      "bytes": 667
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "308b8e386cc1aa5c3a71c0848c642140c96c3c98e815fc9b69ae7271ca3b4601",
      "bytes": 1464
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "0cc9bfda159ea0e86e42df5101adeb092ab5e6be638b5f68e3e319ad127ff963",
      "bytes": 1858
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "3c858fd81e3e44b3accd9b34de786a8a15356815e45a23a2ae896b0666a84039",
      "bytes": 622
    },
    {
      "path": "characters/Muyaho.md",
      "sha256": "57e5af68aaf8ef11cb33da93b34567ef62fdd809d4ece7cf19140f539652a250",
      "bytes": 580
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "f42dfd67596a031157abc532411bfc4f3dfca5a78b3f4e0d10485fc4aa058944",
      "bytes": 787
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "9e10dcc2bb8d5dec96e4c08958b7f9be19c53b59458cf2cec14e822f1d7f0f5b",
      "bytes": 208806
    }
  ],
  "estimated_tokens": 11307
}
-->

# Durable State Update — Chapter 674

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 674. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 674. Profile updates may replace only one
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
  "chapter": 674,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 674,
    "continuity_sources": [674],
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
    "Nanman has issued a general mobilization order and placed Baeksang in the temporary position of Palace Lord.",
    "Jin Taekyung and the former Palace Lord Yayul Cheok are officially treated as the highest-priority fugitives after the prison raid and release of the Han Chinese prisoners.",
    "The Western Yao Estate massacre remains publicly attributed to Jin despite unresolved evidence.",
    "Baeksang is grieving Yayul Hyang's death and Baekhwi's fate after their intended marriage was destroyed by the Great Faction War.",
    "The Southern Heaven Demon Empress has appeared before Baeksang."
  ],
  "continuity_sources": [
    673
  ],
  "open_questions": [
    "What does the Southern Heaven Demon Empress want from Baeksang?",
    "Where are Jin Taekyung, Yayul Cheok, Yayul Mok, and the released Han Chinese prisoners?",
    "Can Baeksang maintain control of the Nanman Beast Palace as temporary Palace Lord?",
    "Who actually killed the Yao warriors and caused the disappearance of the two Great Chieftains?"
  ],
  "safe_through": 673,
  "temporary_decisions": [
    "Use Great Chieftain for 대족장 and Palace Lord for 궁주.",
    "Use temporary Palace Lord for 임시 궁주 and former Palace Lord for 전 궁주.",
    "Use Western Yao Estate for 요서부.",
    "Use Yayul Hyang for 야율향, Hwi for 휘 and 휘아, and Hyang for 향 and 향아.",
    "Preserve Baeksang's restrained grief and the sworn brothers' rough, teasing banter in the flashback."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 십왕     | **Ten Kings**       |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 중원     | **Central Plains**                               |                                                       |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 대사      | **Master** for a senior Buddhist monk                           |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 무야호 | **Muyaho** | Yayul Mok's White Tiger's name; it means tiger of the mighty wilds. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 인시 | **Insi** | The traditional time period from three to five in the morning. |
| 묘시 | **the hour of the Rabbit** | Traditional time period following Insi. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |
| 대족장 | **Great Chieftain** | Title used for the senior Nanman leader who supposedly ordered the inspection. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 진태경 | 백호 | human ally to intelligent spiritual beast | you | casual and familiar | Converses with White Tiger after interpreting its warning. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 백상 | 야수묘왕 | Nanman great chieftain to the Nanman Beast Palace Lord | Palace Lord | restrained and apologetic | Apologizes for causing the disturbance after the Beast Miao King stops the fight. |
| 백상 | 남천마후 | Nanman Great Chieftain to hostile demon empress | Southern Heaven Demon Empress | formal and shocked | Baeksang directly identifies the woman who appears before him. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 673
- **Aliases:** None
- **Role:** Baeksang is an over-seventy Great Chieftain of the Bai people, one of Nanman's four most powerful great tribes, and one of only two Supreme Peak masters in Nanman.
- **Personality:** Cold, rigid, meticulous, politically resolute, and strategically manipulative, with enduring grief over Hwi's death and a guarded but still powerful bond with his sworn elder brother that now leaves him visibly conflicted.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of his deceased only child Baekhwi, whom the Great Snow Fiend killed during the Great Faction War; despite his bond with Yayul Cheok, he has chosen to oppose the Beast Miao King's escape and has surrounded Wonhu's remaining force with Bai warriors.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 673
- **Aliases:** None
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, the great chieftain of the Miao people, a master among the Ten Kings, and one of only two Supreme Peak masters in Nanman.
- **Personality:** The Beast Miao King is fierce and vigilant, yet pragmatic and willing to sacrifice his position to protect Nanman's survival and the greater cause over personal revenge.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace, is Baeksang's sworn elder brother and childhood companion, and is Yayul Mok's father while jointly risking their positions to rescue Jin Taekyung and prevent war with the Central Plains.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 673
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 671
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 665
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and a member of the Fire Dragon Pavilion; he is currently bound and unconscious under the reconnaissance squad's guard after being struck at a Sleep Acupoint.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 673
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, and an escaped prisoner still facing public execution at noon in two days.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 673
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Muyaho.md

# Muyaho (무야호)

- **Safe through:** Chapter 672
- **Aliases:** White Tiger
- **Role:** Muyaho is Yayul Mok's enormous white tiger companion and a renowned Nanman spiritual creature.
- **Personality:** Muyaho is intelligent enough to understand speech, wary of threats, and strongly food-motivated.
- **Voice:** Muyaho communicates through growls, roars, and gestures rather than human speech.
- **Relationships:** Muyaho is Yayul Mok's cherished companion and currently carries Jin while aiding his escape.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 672
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion; he helped Jin escape the underground prison by blocking the stairs and overpowering the Bai warriors.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃674화



이 세상에는 상리(常理)로는 이해할 수 없는 현상이 종종 벌어지고는 한다.

지금 이 순간, 붉게 충혈된 백상의 눈동자에 비친 한 여인도 그중 하나였다.

“……남천마후(南天魔后).”

단둘만이 존재하는 공간을 나직하게 울리는 목소리.

여인, 남천마후는 활짝 웃었다.

“오랜만이네요, 백상 대족장님.”

한없이 아름답고, 그 이상으로 요사스러운 그녀의 미소에 백상의 가슴이 덜컥 내려앉았다.

‘도대체 어떻게.’

삼엄한 경계를 뚫고 잠입한 것은 그리 놀라운 일이 아니다. 하지만 초절정의 경지에 다다른 그가 기척조차 느끼지 못했다니.

남천마후를 처음으로 알게 된 것은 어언 삼십 년도 전의 일이다.

자식을 잃은 슬픔으로 반쯤 미쳐 있었던 과거에 비교하면 많은 것이 달라졌지만, 저 요녀(妖女)와의 격차는 조금도 좁혀지지 않았다는 것을 깨닫자 마음이 무거워졌다.

“……이곳에는 어쩐 일로?”

굳은 얼굴로 입을 연 백상의 모습에, 남천마후가 짐짓 토라진 표정을 지었다.

“왜, 혹시 저를 마주하는 것이 싫으신가요?”

장난기가 다분하게 섞여 있는 물음이었지만, 남천마후를 눈앞에 둔 이상 한 치의 방심도 있어서는 안 된다.

애써 마음을 가라앉힌 백상이 대답했다.

“당신이 직접 찾아오리라고는 생각하지 못했을 뿐이오. 평소였다면 전령(傳令)이나 밀마(密摩)를 통해 전했을 테니까.”

남천마후는, 아니 암천(暗天)은 항상 그랬다.

이름도, 얼굴도 드러나지 않은 흑의인을 만나거나, 예상치 못한 어느 장소에서 그들이 남긴 밀마를 발견하는 것은 백상에게 있어 이미 익숙해진 일이었다.

그와 동시에…… 결코 거부할 수 없는 일이기도 했다.

“나흘 후면 다시 약속했던 날이오. 굳이 당신이 이곳까지 걸음 하지 않았더라도 내가 찾아갔을 터인데.”

지난 수십여 년 동안이나 반복했던 일이다.

백상은 매달 초하루, 인시와 묘시 사이에 암천과 전서를 주고받았고 석 달에 한 번씩은 누구에게도 알리지 않고 홀로 그들을 찾아갔었다.

“사흘 후? 어머, 벌써 시간이 그렇게 됐나?”

하지만 마치 까맣게 잊고 있었다는 듯 눈을 동그랗게 뜨는 남천마후의 모습에, 백상은 저절로 주먹에 힘이 들어가는 것을 느꼈다.

“당신…….”

“농담이에요, 농담. 어울리지 않게 발끈하시기는. 이럴 때 보면 우리 대족장님, 의외로 귀여운 면이 있으시다니까.”

“……!”

“사실 겸사겸사 왔어요. 최근 들어 많은 일이 있기도 했고, 드디어 남만의 지배자가 되셨으니 직접 축하해 주고 싶었달까? 그런데…….”

남천마후가 입가를 가리며 웃었다.

“누가 알았겠어요. 그토록 냉철한 백상 대족장님. 아니, 신임 궁주님의 눈물을 보게 될 줄은.”

위로 솟구친 입꼬리와는 달리 깊게 가라앉아 있는 남천마후의 눈빛.

백상은 마음 한구석이 서늘해지는 것을 느끼며 입술을 뗐다.

“별것 아니오. 면경(面鏡)을 보고 있자니, 잠시 옛 생각이 났을 뿐.”

“아하. 거울 속 자신을 꼭 닮은 아들이 생각나서?”

“……그 이야기는 여기까지 했으면 좋겠군. 중요한 것은 과거가 아닌 앞으로의 일이니까.”

“뭐, 우리 궁주님께서 그러시다면야. 좋은 마음가짐이에요.”

싱긋 웃은 남천마후가 말을 이었다.

“한편으로는 살짝 아쉽기도 하네요. 난 또, 선물을 받고 감동해서 눈물이라도 흘린 줄 알았지.”

백상이 딱딱한 음성으로 대꾸했다.

“면경을 선물해 준 것은 고맙게 생각하고 있소. 잘 쓰지.”

“됐어요. 그래도 궁주 취임 기념으로 나름 힘들게 구한 건데, 엎드려 절받는 기분이네.”

백상을 흘겨본 남천마후는 천천히 창가로 다가갔다.

내궁에서도 가장 높은 언덕 위에 우뚝 선 궁주전(宮主殿)의 아래로는 수많은 전각과 가옥이 한눈에 내려다보였다.

“와, 경치 좋네요. 역시 궁주가 기거하는 곳이라 달라. 앞으로는 이런 경치를 매일 보시겠어요?”

“아직은 임시 궁주일 뿐이오.”

“임시라……. 정말 그렇게 생각하시는 건 아니죠?”

“…….”

“우리 궁주님. 다 아시는 분이 왜 이러실까.”

입을 다문 백상을 향해 눈웃음을 건넨 남천마후는 창밖 풍경을 바라보았다.

내리쬐는 햇살과 어디선가 불어오는 시원한 바람. 그리고 구름 한 점 없이 푸르른 하늘.

오랜만에 마주한 쾌청한 날씨에, 남천마후는 문득 기분이 유쾌해지는 것을 느꼈다.

어찌 그렇지 않겠나.

이토록 맑은 하늘을, 곧 한 줄기 빛도 존재하지 않는 암흑으로 물들일 수 있을 텐데.

솨아아아.

활짝 열린 창으로 밀려드는 바람에 섬단 같은 머리카락이 출렁인다.

눈을 감은 채 미소 짓던 남천마후가 불현듯 입술을 뗀 것은, 그로부터 촌각이 흐른 뒤였다.

“알고 있죠? 대사(大事)가 마무리 단계에 접어들었다는 것을.”

“……!”

귓가를 파고드는 그녀의 나직한 목소리에, 백상의 눈꺼풀이 파르르 떨렸다.

지금 그의 눈앞에는 지난 수십여 년의 세월과 한 사람의 얼굴이 눈앞을 스쳐 지나가고 있었다.

“물론……이오.”

“모든 것이 순조로워요. 몇 가지 사소한 문제만 빼면.”

순간 백상은 짐작했고, 뒤이어 남천마후의 입술 사이로 흘러나온 두 사람의 이름을 듣고 자신의 짐작이 맞았음을 깨달았다.

“야수묘왕. 그리고 진태경.”

비스듬히 턱을 괸 남천마후는, 창밖에서 줄지어 들어오는 남만 전사들을 바라보며 말을 이었다.

“솔직히 말하자면, 사소한 것 이상이죠. 한 사람은 십왕(十王)에 속할 만큼 뛰어난 무위를 지닌 초절정 고수. 게다가 다른 한 사람은, 네. 바로 그 진태경이고요.”

백상은 그녀의 뒷모습을 바라보며 생각했다. 드디어 올 것이 왔다고.

아마 이것이 오랜 시간 동안 모습을 드러내지 않던 남천마후가 직접 이 자리에 온 이유일 것이다.

“미안하오.”

“미안하다니. 뭐가요?”

“그럴 수밖에 없지 않겠소. 그건 명백한 내 실수였으니.”

“흐음.”

흥얼거리듯 작게 중얼거린 남천마후가 말을 이었다.

“맞아요. 하지만 우리의 실수이기도 하죠. 나 역시 야수묘왕이 그런 악수를 둘 것이라고는 생각하지 못했거든요. 그리고…….”

힐끗 뒤를 돌아본 남천마후의 시선이 머무른 곳은, 다름 아닌 백상의 왼팔이었다.

새하얀 호리(狐狸)의 털로 만들어진 장포로 가려진 그곳은, 전날 밤과 달리 공허했다.

“우리 신임 궁주님께서 나름대로 애쓰셨다는 건 알았으니까.”

이미 출혈은 멈췄으나, 강기에 의해 절단된 단면으로부터 올라오는 통증만큼은 단기간에 어쩔 수 없는 것.

백상은 불현듯 느껴지는 통증을 참으며 대꾸했다.

“나로서는 대적할 수 없었소. 주위에 대기 중이던 모든 병력을 동원했음에도 포위망을 빠져나가더군.”

“말석이긴 하지만 십왕은 십왕이니까요. 아니면 그를 살린 것이…… 아직도 의형제라는 이름으로 남아 있는 한 줄기 온정(溫情)일 수도 있고.”

“그건…….”

“아닌가요? 단언코?”

잠시 침묵하던 백상이 입을 열었다.

“어쩌면, 그래. 그랬을 거요. 최소한 그의 뒤를 쫓을 만큼의 시간 정도는 벌 수 있었을지 모르지.”

“지금 스스로가 무슨 말을 하고 있는지, 알고 있나요?”

“물론. 하지만 이것 하나만큼은 단언할 수 있소. 두 번 다시 그런 일은 벌어지지 않는다는 것.”

깊게 가라앉은 백상의 눈동자를 물끄러미 응시하던 남천마후가 가볍게 한숨을 내쉬었다.

“후우. 다행이네요.”

“뭐가 말이오?”

“솔직하게 말해 줘서요. 만약 인정하지 않는다면, 조만간 사지를 갈기갈기 찢어 죽이려고 했는데.”

“……!”

“진심으로 다행이에요. 비록 우리 자주 본 사이는 아니지만, 그래도 난 궁주가 꽤 마음에 들었거든요.”

소녀처럼 부끄러운 미소를 지은 남천마후가 말을 이었다.

“왜 그런 거 있잖아요. 물에 빠진 개미 새끼가 어떻게든 살아 보겠다고 발버둥 치는 걸 보면 응원하고 싶은 그런 거. 아, 물론 궁주가 개미 새끼라는 말은 아니에요. 그건 제가 표현이 서툴러서.”

백상은 전신의 피가 차갑게 식는 듯한 기분이 사로잡혔다.

지금 그의 몸과 마음을 짓누른 것은 수치심, 모멸감 따위는 집어삼킬 만큼 거대한 두려움이었다.

동시에 다시 한번 깨달았다.

눈앞의 이 여인은, 진정 위험한 존재라는 것을.

암천에게 있어 자신은 쉽게 조종할 수 있는 꼭두각시이며 목줄을 건 가축, 혹은 그 이하의 존재라는 것을.

하지만…….

‘이것이 내가 택한 길이다.’

그것이 냉혹한 현실이었다.

그는 오래전 남천마후가, 암천이 내민 손을 잡았고 그 대가로 희망을 얻었다.

바로 그 희망이 자식을 잃은 슬픔으로 무너진 그를 일으켜 세웠고, 계속 살아가야 할 이유를 주었다.

그렇기에 그는 스스로 이 길을 끝내지 못한다.

기호지세(騎虎之勢). 호랑이의 등에 올라탄 이상, 혼신의 힘을 다하여 달려갈 뿐이다.

털썩.

남만인 중 그 누구도 믿지 못할 광경. 그러나 지금 궁주전에서 벌어지는 이 광경은 모두 현실이었다.

남만야수궁의 새로운 궁주이자, 광활한 남만의 지배자는 한쪽 무릎을 꿇어 예를 표했다.

세상 그 무엇보다 아름다울 것 같은 한 여인을 향해.

“부디 명령을 내려 주십시오, 마후(魔后).”

백상을 굽어보던 남천마후는, 창가에서 쏟아지는 햇빛을 받으며 나른하게 웃었다.

“이래서 당신이 마음에 든다니까.”

남천마후는 창밖을 향해 손을 뻗었다.

새로운 궁주의 총동원령에 응하여 끊임없이 밀려오는 남만의 전사들과 그들의 머리 위로 펼쳐진 푸른 하늘을 움켜쥘 듯이.

“사흘. 사흘 안에 야수묘왕을 찾아 화근을 제거해. 진태경은…….”

혹은 단숨에 암흑으로 물들여 버릴 듯이.

“우리가 처리한다.”

이미 모든 것이 마무리 단계에 접어든 지금, 남천마후는 믿어 의심치 않았다.

남만으로부터 열린 길이, 중원을 향한 교두보가 되리라는 것을.

그 끝에 세상 만물을 지배하는 전능하신 천주(天主)의 재림이 기다리고 있을리라는 것을.



* * *



혁무진의 불알을 걸고 장담한다.

그건 아마도 남만 역사상, 아니 무림 역사상 초유의 봉화(烽火)였을 것이다.

화륵. 콰아아아!

태산에게 다른 이들을 맡기고 남쪽으로 향한 지 이틀째. 나는 일곱 번째 산을 불태우고 있었다.

아, 물론 목초지도 포함이다.

“잠깐, 일곱이 아니라 여덟 번짼가?”

크르릉.

“하긴. 그게 중요한 게 아니지.”

나는 불만스러운 표정을 짓고 있는 백호를 무시했다.

새하얗던 녀석의 털은 피와 검댕으로 지저분해져 있었다.

물론 녀석의 몸에서 흐른 피는 아니다. 여섯 번쯤 추격대를 격퇴하다 보니 어쩔 수 없이 일어난 불상사일 뿐.

하지만 무야호의 투정도 얼마 지나지 않아 들리지 않게 될 것이다.

아니, 더 이상 우리 둘 다 그런 것 따위는 신경 쓰지 못하게 되리라는 것이 옳겠다.

저벅.

백호의 커다란 앞발이 진흙을 밟았다.

그리고 줄곧 바람처럼 내달리던 녀석이 검은 숲을 바라보며 작은 울음소리를 흘린다는 건, 오직 한 가지 의미만을 뜻했다.

그래.

“여기구나.”

어둠에 물든 산을 바라보며, 나는 중얼거렸다.
```

## Final English reading copy

```markdown
# Chapter 674

There were often phenomena in this world that could not be understood through common sense.

The woman reflected in Baeksang’s bloodshot eyes at this very moment was one of them.

“…Southern Heaven Demon Empress.”

His voice quietly echoed through the space where only the two of them existed.

The woman—the Southern Heaven Demon Empress—smiled broadly.

“It’s been a while, Great Chieftain Baeksang.”

Her smile was infinitely beautiful and even more bewitching. Baeksang’s heart sank.

*How?*

It was not particularly surprising that she had infiltrated the place despite its strict security. But how could he, a man who had reached the Supreme Peak realm, have failed to sense even her presence?

It had been more than thirty years since Baeksang had first learned of the Southern Heaven Demon Empress.

Many things had changed since the days when he had been half-mad with grief over the loss of his child. But realizing that the gap between him and that demoness had not narrowed in the slightest weighed heavily on his heart.

“…What brings you here?”

At Baeksang’s stiff question, the Southern Heaven Demon Empress deliberately made a sulky face.

“What? Do you not like seeing me?”

Her question was filled with playfulness, but with the Southern Heaven Demon Empress standing before him, Baeksang could not afford to let his guard down even a fraction.

Baeksang forced himself to calm down before answering.

“I simply did not expect you to come in person. Under normal circumstances, you would have sent word through a messenger or a secret message.”

The Southern Heaven Demon Empress—or rather, Dark Heaven—had always been that way.

Meeting black-clad figures whose names and faces were never revealed, or discovering secret messages they had left in unexpected places, had long since become familiar to Baeksang.

At the same time, they were things he could never refuse.

“In four days, it will be the day we promised to meet again. Even if you had not gone to the trouble of coming all the way here, I would have gone to see you.”

It was something they had repeated for several decades.

On the first day of every month, Baeksang exchanged missives with Dark Heaven between Insi and the hour of the Rabbit. Once every three months, he would go to see them alone without informing anyone.

“Three days from now? Oh my, has it already been that long?”

The Southern Heaven Demon Empress widened her eyes as though she had completely forgotten. Baeksang felt his fist tighten on its own.

“You…”

“I’m joking, I’m joking. Getting worked up over something so out of character for you. When I see you like this, our Great Chieftain has a surprisingly cute side.”

“…!”

“I came for a few reasons. A lot has happened lately, and now you’ve finally become the ruler of Nanman, so I thought I should congratulate you in person. But…”

The Southern Heaven Demon Empress covered her mouth as she laughed.

“Who would have thought? The famously cold-blooded Great Chieftain Baeksang. No—the new Palace Lord. I never expected to see you in tears.”

The corners of her mouth were lifted, but her gaze had sunk deep.

Baeksang felt a chill creep into one corner of his heart and parted his lips.

“It was nothing. Looking at the mirror simply brought back some old memories for a moment.”

“Oh, because you thought of the son who looked exactly like you in the mirror?”

“…I would prefer to end that subject here. What matters is not the past, but what lies ahead.”

“Well, if that is what our Palace Lord wishes. That is a good attitude.”

The Southern Heaven Demon Empress smiled sweetly before continuing.

“Still, I’m a little disappointed. I thought you had been moved to tears by the gift.”

Baeksang replied in a rigid voice.

“I appreciate the mirror you gave me. I use it well.”

“That’s enough. I went to quite a bit of trouble to find it as a gift commemorating your appointment as Palace Lord, but this feels like I’m being thanked only because I demanded it.”

The Southern Heaven Demon Empress shot Baeksang a sidelong glance before slowly walking toward the window.

Below the Palace Lord’s Hall, which stood atop the highest hill in the Inner Palace, countless pavilions and houses spread out in full view.

“Wow, what a view. It really is different from a place where the Palace Lord lives. You’ll be looking at this scenery every day from now on, won’t you?”

“I am still only the temporary Palace Lord.”

“Temporary… You don’t really think that, do you?”

“…”

“My Palace Lord. Why are you pretending when you know everything?”

The Southern Heaven Demon Empress gave the silent Baeksang a smile with her eyes before turning her gaze toward the view outside.

Sunlight poured down, a cool breeze blew in from somewhere, and the sky was a vivid blue without a single cloud.

The clear weather she had encountered for the first time in a while suddenly put the Southern Heaven Demon Empress in a pleasant mood.

How could it not?

Soon, she would be able to stain this impossibly clear sky with darkness in which not even a single ray of light remained.

Whoooosh.

The wind rushed in through the wide-open window, sending her fine, silky hair rippling.

The Southern Heaven Demon Empress had been smiling with her eyes closed. Moments later, she suddenly parted her lips.

“You know, don’t you? That the great undertaking has entered its final stage.”

“……!”

Her quiet voice pierced his ears, and Baeksang’s eyelids trembled.

The decades that had passed and the face of one person flashed before his eyes.

“Of course… I do.”

“Everything is proceeding smoothly. Except for a few minor problems.”

Baeksang immediately guessed what she meant. Then, when the Southern Heaven Demon Empress spoke the names of two people, he realized that his guess had been correct.

“The Beast Miao King. And Jin Taekyung.”

Resting her chin lightly on one hand, the Southern Heaven Demon Empress continued while watching Nanman warriors file in outside the window.

“To be honest, they are more than minor problems. One of them is a Supreme Peak master whose martial prowess is great enough to place him among the Ten Kings. And the other one is, yes. That Jin Taekyung.”

Watching her back, Baeksang thought that the inevitable had finally arrived.

This was probably why the Southern Heaven Demon Empress, who had not revealed herself for such a long time, had come here in person.

“I am sorry.”

“Sorry? For what?”

“How could I not be? It was clearly my mistake.”

“Hmm.”

The Southern Heaven Demon Empress hummed softly as though singing under her breath before continuing.

“That’s right. But it was our mistake as well. I never expected the Beast Miao King to make such a terrible move either. And…”

The Southern Heaven Demon Empress glanced over her shoulder. Her gaze came to rest on Baeksang’s left arm.

Unlike the previous night, the arm hidden beneath a robe made of pure white fox fur was empty.

“I knew our new Palace Lord had made an effort in his own way.”

The bleeding had already stopped, but the pain rising from the severed end, cut through by Force, could not be dealt with in such a short time.

Baeksang endured the sudden pain before answering.

“I was no match for him. Even after I mobilized every soldier waiting nearby, he managed to break through the encirclement.”

“He may be the last among them, but one of the Ten Kings is still one of the Ten Kings. Or perhaps what saved him was… the last thread of warmth remaining under the name of sworn brothers.”

“That…”

“Isn’t that right? Are you absolutely certain?”

After a brief silence, Baeksang opened his mouth.

“Perhaps. Yes, perhaps it was. At the very least, I might have been able to buy enough time to pursue him.”

“Do you know what you are saying right now?”

“Of course. But there is one thing I can say with certainty. Nothing like that will ever happen again.”

The Southern Heaven Demon Empress stared at Baeksang’s deeply sunken eyes for a moment before letting out a soft sigh.

“Phew. That’s a relief.”

“What is?”

“That you answered honestly. If you had refused to admit it, I was planning to tear you limb from limb and kill you before long.”

“……!”

“I’m genuinely relieved. Even though we haven’t met very often, I’ve come to like you quite a lot, Palace Lord.”

The Southern Heaven Demon Empress smiled shyly like a young girl before continuing.

“You know how sometimes, when you see a tiny ant that has fallen into the water struggling desperately to survive, you want to root for it? Ah, of course, I’m not saying you’re an ant. I’m just bad at expressing myself.”

Baeksang felt as though all the blood in his body had turned cold.

The fear bearing down on his body and mind was vast enough to swallow his shame and humiliation whole.

At the same time, he realized once again.

*This woman before me is truly dangerous.*

To Dark Heaven, he was nothing more than an easily controlled puppet, a leashed animal—or something even less than that.

But…

*This is the path I chose.*

That was the cold reality.

Long ago, the Southern Heaven Demon Empress—the Dark Heaven—had reached out her hand to him, and Baeksang had taken it. In exchange, he had received hope.

That very hope had raised him back up after he collapsed beneath the grief of losing his child. It had given him a reason to continue living.

That was why he could not bring this path to an end himself.

He was riding a tiger. Now that he was on its back, all he could do was race onward with all his strength.

Thud.

It was a sight no Nanman person could have believed.

Yet what was happening inside the Palace Lord’s Hall was all real.

The new Palace Lord of the Nanman Beast Palace, the ruler of the vast Nanman, dropped to one knee and bowed.

He did so before a woman who seemed capable of being more beautiful than anything else in the world.

“Please give me your orders, Demon Empress.”

The Southern Heaven Demon Empress looked down at Baeksang and smiled languidly in the sunlight pouring through the window.

“This is why I like you.”

The Southern Heaven Demon Empress stretched out a hand toward the window.

It was as though she meant to seize the Nanman warriors endlessly pouring in response to the new Palace Lord’s general mobilization order, along with the blue sky spread above their heads.

“Three days. Find the Beast Miao King and eliminate the source of trouble within three days. As for Jin Taekyung…”

Or perhaps to turn it all into darkness in a single breath.

“We will deal with him.”

Now that everything had entered its final stage, the Southern Heaven Demon Empress had no doubt that the path opened from Nanman would become a bridgehead toward the Central Plains.

At its end, the return of the omnipotent Lord of Heaven, who ruled all things in the world, would be waiting.

* * *

I’ll stake Hyuk Mujin’s balls on it.

That was probably the most unprecedented signal fire in the history of Nanman—or perhaps in the history of the entire Murim.

Whoosh. Fwoooosh!

It was the second day since I had entrusted the others to Taishan and headed south. I was burning the seventh mountain.

Oh, the pasture too, of course.

“Wait. Was it the seventh one, or the eighth?”

Growl.

“On second thought, that’s not what matters.”

I ignored the White Tiger’s displeased expression.

Its once-white fur was filthy with blood and soot.

Of course, the blood had not come from its body. After repelling pursuit squads about six times, this kind of unfortunate accident had been unavoidable.

But before long, Muyaho’s complaints would no longer be audible.

No—to be more precise, neither of us would be able to care about things like that anymore.

Step.

The White Tiger’s enormous forepaw stepped into the mud.

And the fact that the creature that had been running like the wind all this time let out a small cry while staring at the black forest could only mean one thing.

That’s right.

“It’s here.”

I muttered while gazing at the mountain shrouded in darkness.
```
