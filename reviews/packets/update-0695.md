<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0695.txt",
      "sha256": "cfcde0532d4b257b9f775f7af1e1b9274952bd78ab846c05a16cd4e9c781c012",
      "bytes": 12375
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "01f191d264db9be357039e549df4debdc9236f03242f1584937e46f5f8a4685b",
      "bytes": 2587
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "513c6fafe9f1840a6e447ad7562b1e3ec4fe9fa5309e776d08b3dfd0909660d4",
      "bytes": 204873
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "46f58db7416d6a3d5fb4632f4ce14c0ae59f489e37e038d9fa611df4b32b37ad",
      "bytes": 925
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "6abdc9bd2d630beb9bf93e6bb35a947ae86c3b49c7c37e81a26e14b02e8c9340",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "dcbdd390a5618ac505e5c3cd7aab90351a969eaf00c6bd10d54198bb84eb2984",
      "bytes": 1897
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "df7878805cad6b9db667b2efb3390120c4212046eb4ff2e59a769cf578a46c16",
      "bytes": 622
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "2d967ade3bac233a85d769396cdc0d0a175143ab3fe19a44c8032e8203a73660",
      "bytes": 770
    },
    {
      "path": "characters/Yayul Cheok.md",
      "sha256": "66a31563150d02f96b2204230fc65821321f9301cc4fb1a276e838d04f3022e9",
      "bytes": 902
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "a4e9c72628e156fa9a73692a9dc268fc12f57f15d7061a662f5b43ab83ec60e0",
      "bytes": 670
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ec2dbe39fe4b779680987a12566d8b8d92255e115a8c3f4dfd6f84f470f9327d",
      "bytes": 213692
    }
  ],
  "estimated_tokens": 11076
}
-->

# Durable State Update — Chapter 695

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 695. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 695. Profile updates may replace only one
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
  "chapter": 695,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 695,
    "continuity_sources": [695],
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
    "Jin Taekyung, Yohi, and Muyaho remain in the hidden healing realm deep within the Poisonblood Grounds.",
    "The healing pond saved Muyaho from the brink of death and restored Jin's severe injuries.",
    "The Black Tiger is an ancient guardian spirit born alongside the sacred stone and protects the hidden land beneath Ailao Mountain, formerly the Sacred Land.",
    "The sacred stone sustains the land's abundance, and its power to rule beasts is only one of its abilities.",
    "The Beast King Stone was a powerless stone created by Nanman's first Palace Lord as a legend to unite the tribes; the actual sacred stone was never his possession.",
    "Human wars drained the sacred stone's power, while the Black Tiger watched without intervening and later regretted failing to save the first Palace Lord.",
    "The Black Tiger possesses the Water God Dragon's Origin Essence and wants to use it to restore the sacred stone.",
    "The System changed the Black Tiger's designation to guardian spirit, revealed the Hidden Sacred Land, and created the hidden Quest Last Chance.",
    "Jin must decide whether to strengthen the Ancient Sacred Stone with the Water God Dragon's Origin Essence.",
    "A pillar of light appeared around the hidden realm after Yohi and Muyaho witnessed a tremor and the awakening of birds and beasts.",
    "Jin still intends to find an exit and return to Nanman before the Southern Heaven Demon Empress's attack causes further deaths.",
    "The System's unidentified discovery remains unresolved."
  ],
  "continuity_sources": [
    694
  ],
  "open_questions": [
    "Will Jin accept the System's offer to strengthen the Ancient Sacred Stone with the Water God Dragon's Origin Essence?",
    "What consequences will follow from the hidden Quest Last Chance, the pillar of light, and the unidentified figure atop the White Tiger?",
    "How can Jin, Yohi, and Muyaho leave the hidden realm?",
    "Is Heugung truly dead?",
    "What is the System's unidentified discovery?"
  ],
  "safe_through": 694,
  "temporary_decisions": [
    "Render 수왕석 as Beast King Stone, 신석 as sacred stone, and 고대의 신석 as Ancient Sacred Stone.",
    "Render 애뇌산의 망령 as Apparition of Ailao Mountain and 수호령 as guardian spirit.",
    "Render 숨겨진 성지 as Hidden Sacred Land and 마지막 기회 as Last Chance.",
    "Render 흑호's 의념 as telepathic dialogue with em dashes and a calm, ancient voice.",
    "Render 영기 as spiritual energy and 원정 as Origin Essence."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 중원     | **Central Plains**                               |                                                       |
| 정마대전   | **Great Faction War**         |
| 귀가      | **your family**                                                 |
| 도사      | **Daoist**                                                      |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 야율척 | **Yayul Cheok** | Beast Miao King and lord of the Nanman Beast Palace. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 오독문 | **Five Poisons Sect** | Formerly dominant Nanman faction destroyed by the Fire Gate Clan. |
| 대전쟁 | **Great War** | The long war that ended after the Great Cataclysm. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 요족 | **Yao people** | One of Nanman's four great tribes, led by Yohi. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 외궁 | **Outer Palace** | The outer compound of the Nanman Beast Palace. |
| 대족장 | **Great Chieftain** | Title used for the senior Nanman leader who supposedly ordered the inspection. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 궁주 | **Palace Lord** | Title Yohi uses after realizing that Heugung is the Beast Miao King. |
| 수호령 | **guardian spirit** | Ancient title for the Black Tiger. |
| 신석 | **sacred stone** | Stone said to have existed alongside the Black Tiger's birth. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 야율척 | 진태경 | Nanman_Beast_Palace_Palace_Lord_to_Jeok_Cheongang's_Disciple | you / Disciple of Old Master Jeok / Jin Taekyung | rough, testing, and later welcoming | Yayul Cheok questions Taekyung as a suspected culprit, strikes him as a test, and then welcomes him after recognizing Jeok's Disciple. |
| 진태경 | 야율척 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Palace_Lord | Great Hero Yayul Cheok | formal and deferential | Taekyung gives Yayul Cheok a formal greeting as the nineteenth successor of the Fire Gate Clan. |
| 요희 | 진태경 | Yao great chieftain to Murim Alliance pavilion master | Jin Taekyung | casual and probing | Identifies him by his full name while allowing him to keep the mask on. |
| 진태경 | 요희 | Fire Dragon Pavilion pavilion master to Yao great chieftain | you | guarded and blunt | Answers Yohi's probing questions directly while warning her about Ju Hwaran. |
| 백상 | 요희 | Bai great chieftain to Yao great chieftain | Yohi | cold and formal | Calls to Yohi from outside the tent at the chapter's end. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 진태경 | 백호 | human ally to intelligent spiritual beast | you | casual and familiar | Converses with White Tiger after interpreting its warning. |
| 백상 | 남천마후 | Nanman Great Chieftain to hostile demon empress | Southern Heaven Demon Empress | formal and shocked | Baeksang directly identifies the woman who appears before him. |
| 남천마후 | 백상 | Dark Heaven controller to coerced Nanman leader | Great Chieftain Baeksang / Palace Lord | playful, taunting, and threatening | She repeatedly addresses Baeksang while mocking his grief, acknowledging his effort, and issuing her order. |
| 진태경 | 부족장 | captor to captured tribal chieftain | tribal chieftain | casual, coercive, and mocking | Jin promises to spare the captured chieftain if he answers questions properly. |
| 부족장 | 진태경 | captured tribal chieftain to overpowering enemy | Jin Taekyung | alarmed and desperate | The chieftain recognizes Jin by name while fleeing and then begs for his life. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 694
- **Aliases:** None
- **Role:** Baeksang is the Palace Lord of the Nanman Beast Palace, the sole Great Chieftain of Nanman, and the ruler who has expelled the Inner Palace attendants, gathered ten thousand warriors, and declared the grand plan complete.
- **Personality:** Cold, rigid, meticulous, and strategically resolute, yet burdened by regret, grief over Hwi's death, and a final conflicted impulse to spare others from the coming bloodshed.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of deceased Baekhwi, whom the Great Snow Fiend killed; he cultivated Yohi with gold and influence and used her support to advance Dark Heaven's preparations.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 694
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 694
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, and an escaped prisoner who has awakened inside an unexplained healing realm after lying unconscious in its pond.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 694
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 694
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress is the strategist directing Baeksang's defense of Nanman's Inner and Outer Palaces while advancing a grand plan scheduled to begin within three days.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and regards Jin's destruction of her trap with amused surprise.

### Yayul Cheok.md

# Yayul Cheok (야율척)

- **Safe through:** Chapter 694
- **Aliases:** Beast Miao King
- **Role:** Yayul Cheok is the over-eighty Beast Miao King, lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, and great chieftain of the Miao people.
- **Personality:** Boisterous, warmhearted, forthright, playful, and politically conscious of the tribal coalition he leads.
- **Voice:** Rough, loud, convivial, and teasing, becoming authoritative when discussing Nanman's laws or political decisions.
- **Relationships:** Jeok Cheongang is an old acquaintance whom he respects; Baeksang is his sworn younger brother and childhood companion, and they fought together during the Great Faction War; Yayul Mok serves as his Young Palace Lord; Jin Taekyung is Jeok's Disciple whom he welcomes into the Nanman Beast Palace.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 693
- **Aliases:** None
- **Role:** Yohi is the female Great Chieftain of the Yao people, one of Nanman's four great tribes, and is currently separated from Heugung in an unexplained enclosed realm with her internal energy restored.
- **Personality:** Yohi is charismatic, proud, perceptive, and fiercely resistant to Heugung's betrayal and coercion.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people, hates Heugung after his betrayal, and is being coerced to support his false account by the threat against Boshan and her people.

## Korean source

```text
＃695화



처음에는 그 누구도 신경 쓰지 않았다.

아니, 다른 것에는 신경 쓸 틈조차 없었다고 해야 옳았다.

최근 연이어 벌어진 굵직한 사건들과 총동원령에 의해 하루가 다르게 불어나는 군세(軍勢)는 외궁에 거주하는 일반 부족민들조차 숨죽이게 했고, 물경 일만에 달하는 전사와 맹수들은 내궁에서 자신들의 새로운 궁주를 기다리고 있었으니까.

그러나 이러한 상황 속에서도, 자신의 자리를 지키는 이들 역시 있었다.

“죽겠네요. 날은 덥고, 분위기는 뒤숭숭하고. 이럴 거면 차라리 널널한 동문(東門)이나 서문(西門)에 배치됐어야 했는데.”

순찰을 마치고 온 젊은 후배의 투덜거림에, 북문(北門) 성벽에 기대어 앉아 있던 나이 지긋한 중년 전사가 혀를 찼다.

“쯧쯧, 잘하는 짓이다. 앞길 창창한 젊은 놈이 벌써부터 농땡이 피울 생각이나 하고.”

“순찰 다녀오는 동안 그늘에 앉아 계신 분이 할 말입니까?”

“난 늙었잖아. 그리고 이럴 때 아니면 언제 쉬어?”

“하긴, 뭐. 틀린 말도 아니네요.”

남만야수궁에는 총 세 개의 관문이 존재한다. 동, 서, 그리고 그들이 위치한 북문.

남문은 처음부터 없었다. 내궁의 후방에 펼쳐진 깎아지른 듯한 높은 절벽은 그 어떤 관문보다 단단했으니까.

“순찰은, 외궁은 어때?”

“저잣거리에도 쥐새끼 한 마리 안 보입니다.”

“……그렇겠지. 다들 불안할 테니까.”

중년 전사는 한숨을 내쉬었다.

현재 내궁에 결집한 전사들의 숫자만 물경 일만이다. 가히 소국(小國)이라 칭해도 부족함이 없는 군세.

이 정도 숫자의 전사들이 모인 것은 오십여 년 전, 정마대전 이후 처음 있는 일이다.

역사는 반복되는 법.

나이든 이들은 과거를 떠올리며 입을 다물었고, 부모는 아이를 끌어안고 문을 걸어 잠갔다.

곧 거대한 전란이 벌어질 것이라는 불안감이 사방에 팽배했다.

“그런데…… 정말 중원과 전쟁을 치르는 겁니까?”

조심스러운 후배의 물음에, 중년 전사가 나직이 대답했다.

“글쎄. 하지만 그전에 한 가지는 확실하지.”

“뭔데요?”

“중원에서 전쟁을 치르기 전에, 바로 이곳 남만에서 피를 흘려야 한다는 것.”

“……!”

“너도 알다시피 전(前) 궁주께서는 살아 계시고, 그분에 동조하는 다섯 부족장이 외궁을 떠났다. 높으신 분들은 중원으로 향하기 전에 내부를 정리하려 하겠지.”

이건 중년 전사뿐만 아니라, 어느 정도의 생각과 연륜이 있는 이들이라면 짐작하고 있는 바였다.

내전(內戰). 그것도 삼백여 년 만의 내전이 그들을 기다리고 있다는 것을.

중원으로 향하는 길을 지나기 위해서는 불과 며칠 전까지 동고동락하던 동료의 시체와 피를 밟아야 한다는 것을.

“…….”

언제나 가볍던 젊은 전사의 얼굴에 그늘이 드리워진다.

외궁을 떠난 다섯 개 부족민 중에는 그와 어릴 적부터 함께한 절친한 벗들 역시 포함되어 있었다.

어두워진 후배의 모습을 지켜보던 중년 전사가 조용히 몸을 일으켰다.

“어디 가시게요?”

“농땡이도 피울 만큼 피웠으니, 성벽이나 한번 슥 돌아보고 오련다. 하도 안 움직였더니 몸이 쑤셔서.”

“그러지 마시고 그냥 쉬시죠. 어차피 성벽 쪽은 다른 조가 맡고 있을…….”

“그놈들이 경계라도 제대로 서겠느냐? 죄다 우리처럼 슬그머니 내려와서 그늘에나 앉아 있겠지. 윗분들한테 걸리면 결국 수문장인 나만 욕 처먹기 딱 좋다.”

틀린 말은 아니었다. 이방인의 출입이 전무하던 탓에 평소에도 경계가 그리 삼엄한 편은 아니지만, 일만에 달하는 군세가 주둔한 뒤로는 더욱 그러했다.

아무리 죽고 싶어 환장한 놈이라 할지라도, 지금 남만야수궁에 쳐들어오는 것은 자살 행위나 다름없으니까.

게다가…….

‘심란하겠지, 모두들.’

생각 외로 전의(戰意)에 불타오르는 이들은 그리 많지 않았다.

이제는 남만을 배반한 역도로 낙인찍힌 야율척은 모두에게 존경받는 궁주였고, 남만야수궁이라는 깃발 아래에서 삼백여 년간 함께하며 서로에게 동화된 부족민들은 코앞까지 들이닥친 내전과 대전쟁을 꺼렸다.

하지만 어쩌겠나. 위에서 까라면 까는 거지.

“후우.”

한숨을 내쉰 중년 전사는 성벽 위로 올라갔다. 그가 예상했던 대로 성벽 위는 잠잠했다.

아니, 그나마 한 놈이 남아 있긴 했다. 코까지 골며 자고 있어서 문제지만.

‘……그래. 지금이라도 쉬어 둬라.’

폭풍전야(暴風前夜)의 상황. 어쩌면 이 한심한 수하 놈들이 쉴 수 있는 것도 오늘이 마지막일지도 모른다.

고개를 절레절레 내저은 중년 전사는 성벽에 우뚝 선 채 먼 곳을 응시했다.

때는 정오.

이미 중천에 오른 태양은 숨 막히는 열기를 뿜어냈고, 북문 밖으로 펼쳐진 너른 목초지와 외궁이 훤히 내려다보이는 높은 언덕은 아지랑이에 의해 일렁였…….

‘잠깐.’

뭐지? 잘못 본 건가?

중년 전사는 한 줄기 의문과 함께 눈을 크게 떴다.

하지만 그가 몇 번이나 눈을 깜빡이고, 소매로 거칠게 눈을 문질러도 그가 바라보고 있는 광경은 변하지 않았다.

“……이게 무슨.”

자신도 모르는 사이에 입술을 비집고 흘러나온 넋 나간 목소리.

그리고 중년 전사의 시선이 닿은 방향의 끝에서, 거대한 백호가 걸음을 내디뎠다.

사박.

은빛에 가까운 새하얀 터럭. 커다란 앞발이 풀을 스치며 나아간다. 동시에 어디선가 불어온 바람이 언덕 뒤 숲을 휩쓸었다.

솨아아아아.

빽빽하게 얽힌 나뭇가지가, 그 끝에 수없이 매달린 잎사귀가 흔들린다. 그리고 울창한 숲이 드리운 그늘 아래에서, 또 다른 숲이 움직인다.

구궁.

땅이 울리고, 공기가 요동치고, 바람이 흩어졌다. 세로로 길게 찢어진 수많은 눈동자가 섬뜩한 안광(眼光)을 발한다.

“……!”

중년 전사의 입이 서서히 벌어졌다.

맹수. 그것도 헤아릴 수 없을 만큼 아득한 숫자의 맹수였다.

그저 한 사람의 평범한 전사인 그로서는 짐작조차 할 수 없었다.

저 숲 뒤에 얼마나 많은 맹수가 도사리고 있을지. 날카로운 이빨과 발톱을 지닌 저 포식자들이 도대체 어디에서 나타났는지.

하지만 한 가지는 짐작할 수 있었다.

보는 것만으로도 오한이 드는 맹수들의 대군(大群)을 이끄는 것이, 어쩌면 자신과 같은 사람일지도 모른다는 것.

쉬이이이익!

시원한 바람과 함께 목초지를 가로지르는 크고 작은 은빛 신형.

어느덧 두 마리로 늘어난 백호는 커다란 철문 앞에서 걸음을 멈추었다. 자신들이 등에 태운 일남일녀(一男一女)와 함께.

‘저, 저건.’

중년 전사의 동공이 흔들렸다.

아마 그가 아닌 다른 이였다면, 저 일남일녀의 정체를 곧장 알아채지 못했을 것이다.

그러나 그는 지난 십 년간 북문을 책임진 수문장이었고, 두 사람의 얼굴을 본 순간 철퇴로 뒤통수를 얻어맞은 듯한 충격을 느꼈다.

어찌 모를 수 있겠는가.

여인은 남만에서 단 넷뿐인 대족장이요. 다른 한 청년은…….

‘진태경.’

그저 떠올리는 것만으로도 숨이 막히는 이름 석 자.

틀림없었다.

바로 그자다. 오독문의 멸문 이후, 장장 수백 년 만에 이 땅을 찾아온 이방인. 남만에 드리워진 거대한 폭풍 속의 눈.

바로 그가, 진태경이 스스로 남만야수궁을 찾았다.

그것도 수많은 맹수와 그가 납치했다고 알려진 요족의 대족장, 요희와 함께.

‘도, 도대체 이게 어찌 된…….’

하지만 중년 전사의 의문이 채 완성되기도 전에, 굳게 닫혀 있던 한 사람의 입술이 열렸다.

“한 가지 충고하자면. 거기서 손 떼는 게 좋을 거야.”

“……!”

본능적으로 경종(警鐘)을 울리려던 중년 전사가 얼어붙는다. 그 모습을 바라보며, 진태경은 내심 안도의 한숨을 내쉬었다.

‘다행이다. 늦지 않아서.’

저 이름 모를 전사의 얼굴을 본 순간 알았다. 아직 암천의 흉계가 시작되지 않았음을.

‘균열’이 열렸다면, 이미 이곳은 사람이 살 수 없는 지옥도(地獄道)로 변해 있었을 테니까.

그러나 이 고요함. 불길함마저 느껴지는 고요함 속에서 심지가 타들어 가는 폭탄이 느껴졌다.

“안 그러냐. 흰둥아?”

엉덩이에 깔린 거대한 몸뚱어리가 움찔거린다.

신석의 수호령. 그 이름에 걸맞게 과거의 모습을 되찾은 백호가 의념을 흘려보냈다.

- ……이 몸을 그따위 이름으로 부르다니.

“예전이었으면 검둥이였어. 물론 난 인종차별주의자가 아니지.”

- 도대체 무슨 말을 지껄이는지 감도 안 잡히는군. 미친 인간 같으니.

미친놈이라. 그래. 살면서 그런 말 꽤 들었지.

내심 중얼거린 진태경은 피식 웃으며 손에 든 창날을 늘어트렸다.

앞으로의 일에 대한 두려움? 없을 리가.

하지만 숱한 사선을 넘어 이곳까지 왔고, 주어진 상황에 최선을 다했다.

백상. 남천마후. 암천.

이제 그 누가 막아서더라도 상관없다. 그저 목숨을 걸고 맞서 싸울 뿐.

‘그래. 목숨을 걸고.’

이건 수만, 수십만. 아니 어쩌면 그 이상의 목숨이 걸린 전투다.

어쩌면 그 과정에서 피가 강물을 이루고 시체가 산을 이룰지도 모른다.

그러나…….

‘해내야 해.’

누군가 그런 말을 했다.

진인사대천명(盡人事待天命). 사람이 할 수 있는 일을 다 한 후에는, 하늘에 결과를 맡기고 기다린다고.

하지만 진태경의 생각은 달랐다. 하늘의 뜻마저 바꿀 수 있어야, 비로소 의지(意志)라 부를 수 있다.

‘안 그렇습니까.’

고개를 들어 하늘을 바라본다. 대답 대신 뜨겁고, 눈부신 햇빛이 돌아온다. 이런 날에는 더더욱 죽을 수 없다.

물론 어떤 날씨에도 마찬가지다. 그는 죽는 것이 싫었고, 죽을 생각도 없었다.

설령…… 이 철문 뒤에 천주(天主)가 기다린다 해도.

쉭, 서걱!

순간, 섬광처럼 공간을 격하고 날아든 청백색의 강기가 거대한 철문을 반으로 갈랐다.

눈부신 은빛 백호로 거듭난 수호령이 천지를 울리는 포효를 토해 낸다.

- 크와아아아앙!

세상을 집어삼킬 듯 벌어진 맹수의 아가리 속에 숨어있던 것은, 강철보다 단단한 이빨과 붉은 혓바닥뿐만이 아니었다.

화아아아악!

휘황한 빛줄기.

순간 눈부신 광휘(光輝)가 세상을 물들인다.

수호령이 입안에 머금고 있던 신석(神石)으로부터 솟구친 빛의 기둥이 성벽을 넘어 하늘을 관통했다.

콰아아아!

백 리. 아니 어쩌면 천리 밖에서도 보일 거대한 빛의 기둥.

모두가 그 기이한 힘을, 경이로운 광경을 볼 수 있었다.

내궁에 결집해 있던 일만의 전사들도. 그리고 언덕을 메운 아득한 숫자의 맹수들도.

- 캬우우우우!

- 크아아앙!

포효와 함께 보이지 않던 둑이 허물어졌다. 주인의 명령을 기다리고 있던 맹수들이 파도가 되어 드넓은 초목지를 덮친다.

구구구궁!

두두두두두!

뜨거운 햇빛 아래, 땅이 흔들리고 바람이 흩어졌다. 그리고 그 선두에 한 사람이 있었다.

“가자.”

입술 사이로 흘러나온 나직한 한 마디.

동시에 수호령이 힘차게 땅을 박찼다.

쐐애애액!

남만의 운명을 결정지을, 대전쟁의 시작이었다.
```

## Final English reading copy

```markdown
# Chapter 695

At first, no one paid any attention.

No—it would be more accurate to say that no one had even had time to worry about anything else.

The major incidents that had occurred one after another recently, along with the general mobilization order, had caused the military forces to swell by the day. Even the ordinary tribespeople living in the Outer Palace had been reduced to holding their breath, while nearly ten thousand warriors and beasts of prey waited in the Inner Palace for their new Palace Lord.

Even so, there were still those who remained at their posts amid the chaos.

“I’m going to die. It’s hot, and the atmosphere is a mess. If this was how things were going to be, I should’ve been stationed at the East or West Gate, where things are nice and quiet.”

At the young junior’s grumbling after returning from patrol, a middle-aged warrior with graying hair, sitting with his back against the wall of the North Gate, clicked his tongue.

“Tsk, tsk. Look at you. You’re still young and have your whole life ahead of you, yet you’re already thinking about slacking off.”

“Is that something you can say after sitting in the shade while I was out on patrol?”

“I’m old, aren’t I? And if I don’t rest at a time like this, when am I supposed to?”

“Well, I suppose you’re not wrong.”

The Nanman Beast Palace had three gates in total: the East, the West, and the North Gate where they were stationed.

There had never been a South Gate. The sheer cliff rising behind the Inner Palace was sturdier than any gate could have been.

“How was the patrol? What about the Outer Palace?”

“There wasn’t even a single rat in the marketplace.”

“……Of course there wasn’t. Everyone must be nervous.”

The middle-aged warrior sighed.

There were nearly ten thousand warriors gathered in the Inner Palace alone. It was an army large enough to be called a small country without exaggeration.

Not since the Great Faction War more than fifty years earlier had so many warriors gathered in one place.

History had a way of repeating itself.

The older people kept their mouths shut as they remembered the past, while parents pulled their children close and barred their doors.

Anxiety filled the air on all sides—the anxiety that a massive war would soon break out.

“But… are we really going to war with the Central Plains?”

At the young junior’s cautious question, the middle-aged warrior answered quietly.

“Who knows? But one thing is certain.”

“What?”

“Before we fight a war in the Central Plains, blood will have to be spilled right here in Nanman.”

“……!”

“You know that the former Palace Lord is still alive, and that the five tribal chieftains who support him left the Outer Palace. The higher-ups will want to settle things internally before heading to the Central Plains.”

This was not something only the middle-aged warrior had guessed. Anyone with a certain amount of sense and life experience would have arrived at the same conclusion.

A civil war.

A civil war for the first time in more than three hundred years was waiting for them.

To pass through the road leading to the Central Plains, they would have to walk over the corpses and blood of comrades with whom they had shared hardship until only a few days ago.

“……”

The shadow that had always been absent from the young warrior’s carefree face now settled over it.

Among the tribespeople who had left the Outer Palace were several close friends who had grown up with him.

Watching the junior’s darkened expression, the middle-aged warrior quietly rose to his feet.

“Where are you going?”

“I’ve slacked off enough. I’m going to take a quick look around the walls. My body’s aching from sitting still for too long.”

“Don’t bother. Just keep resting. The other squad should be covering the walls anyway—”

“Do you think those idiots will stand watch properly? They’ll all sneak down here like us and sit in the shade. If the higher-ups catch us, I’m the gate captain, so I’ll be the only one who gets my ass chewed out.”

He was not wrong. Since outsiders almost never entered, the guards had never been particularly strict even in normal times. After an army of nearly ten thousand had taken up position, they had become even more lax.

Even someone desperate to die would have been committing suicide by attacking the Nanman Beast Palace now.

Besides…

*Everyone must be troubled.*

There were not as many people burning with fighting spirit as one might expect.

Yayul Cheok, now branded a traitor who had betrayed Nanman, was a Palace Lord respected by everyone. And the tribespeople, who had lived together beneath the banner of the Nanman Beast Palace for more than three hundred years and grown accustomed to one another, were wary of the civil war and Great War that had arrived at their doorstep.

But what could they do? When the people above gave the order, those below had to obey.

“Whew.”

The middle-aged warrior let out a sigh and climbed onto the wall. Just as he had expected, the top of the wall was quiet.

Well, there was at least one man left behind. The problem was that he was asleep and snoring loudly.

*…Fine. Get some rest while you still can.*

This was the calm before the storm. Perhaps today would be the last day these pathetic subordinates of his could rest.

Shaking his head, the middle-aged warrior stood tall atop the wall and stared into the distance.

It was noon.

The sun, already high overhead, radiated suffocating heat, and the high hill overlooking both the broad pasture beyond the North Gate and the Outer Palace shimmered in the heat haze—

*Wait.*

What was that? Had he seen it wrong?

A question flashed through the middle-aged warrior’s mind, and his eyes widened.

But no matter how many times he blinked or roughly rubbed his eyes with his sleeve, the scene before him did not change.

“What… is this?”

The dazed words slipped from his lips before he even realized it.

At the far end of the direction in which the middle-aged warrior was looking, a massive White Tiger took a step forward.

Step.

Its fur was pure white, almost silver. Its enormous forepaw brushed through the grass as it advanced. At the same time, a wind that had come from somewhere swept through the forest behind the hill.

Whoosh!

The densely tangled branches swayed, along with the countless leaves hanging from their ends. And beneath the shade cast by the thick forest, another forest began to move.

Rumble.

The ground shook, the air trembled, and the wind scattered. Countless pairs of vertically slit eyes gave off a chilling gleam.

“……!”

The middle-aged warrior’s mouth slowly fell open.

Beasts of prey.

An unimaginably vast number of beasts of prey.

As nothing more than an ordinary warrior, he could not even begin to guess how many beasts lurked beyond that forest or where those predators, with their sharp teeth and claws, had appeared from.

But he could guess one thing.

The being leading that army of beasts, which sent chills down his spine simply by looking at it, might perhaps be a person like himself.

Whoosh!

Large and small silver figures raced across the pasture with the cool wind.

By then, the number of White Tigers had increased to two. They stopped before the enormous iron gate, along with the man and woman riding on their backs.

*Th-that’s…*

The middle-aged warrior’s pupils trembled.

If he had been anyone else, he might not have recognized the identities of the man and woman at once.

But he had been responsible for the North Gate for the past ten years. The moment he saw their faces, he felt as though he had been struck in the back of the head with an iron club.

How could he not know?

The woman was one of Nanman’s only four Great Chieftains, while the other young man was…

*Jin Taekyung.*

Just thinking of those three syllables made it difficult to breathe.

There was no doubt.

It was him. The outsider who had come to this land for the first time in hundreds of years after the destruction of the Five Poisons Sect. The eye of the enormous storm hanging over Nanman.

He—Jin Taekyung—had come to the Nanman Beast Palace of his own accord.

And he had brought with him countless beasts of prey and Yohi, the Great Chieftain of the Yao people, who was said to have been abducted by him.

*Wh-what in the world is going on…?*

But before the middle-aged warrior could finish his question, one person’s tightly closed lips opened.

“A word of advice. You’d better take your hand off that.”

“……!”

The middle-aged warrior froze just as he instinctively began to sound the alarm. Watching him, Jin Taekyung inwardly let out a sigh of relief.

*Thank God. I’m not too late.*

The moment he saw the face of that unknown warrior, he knew. Dark Heaven’s sinister scheme had not begun yet.

*If the Rift had opened, this place would already have been transformed into a hell where no human could live.*

And yet, within this stillness—a stillness so quiet that it felt ominous—he sensed a bomb with its fuse burning down.

“Right, Whitey?”

The enormous body beneath his backside flinched.

The guardian spirit of the sacred stone. True to that name, the White Tiger, which had regained its former appearance, sent its thoughts outward.

—…How dare you call this body a name like that?

“You would’ve been Blackie before. Of course, I’m not a racist.”

—What in the world are you babbling about? You sound like a mad human.

A madman, huh? Yeah. I’d heard that one a fair number of times in my life.

Muttering inwardly, Jin Taekyung gave a quiet laugh and lowered the spearhead in his hand.

Fear of what lay ahead? Of course he had it.

But he had crossed countless thresholds between life and death to reach this place, and he had done everything he could with the situation he had been given.

Baeksang. The Southern Heaven Demon Empress. Dark Heaven.

It no longer mattered who stood in his way. He would simply stake his life and fight back.

*That’s right. Stake my life.*

This was a battle with tens of thousands, hundreds of thousands—perhaps even more—of lives on the line.

Blood might flow like rivers, and corpses might pile up into mountains.

But…

*I have to do it.*

Someone had once said:

*Do everything in your power, then leave the result to Heaven and wait.*

But Jin Taekyung thought differently. Only when a person could even change the will of Heaven could it truly be called *Will*.

*Isn’t that right?*

He raised his head and looked up at the sky. In place of an answer, scorching, dazzling sunlight poured down.

On a day like this, he could not afford to die.

Of course, that applied in any weather. He hated dying, and he had no intention of dying.

Even if…

the Lord of Heaven were waiting behind this iron gate.

Swish! Slash!

In an instant, a blue-white Force tore through the air like a flash of light and split the enormous iron gate in two.

The guardian spirit, reborn as a dazzling silver White Tiger, released a roar that shook Heaven and Earth.

—GRAAAAAAAWR!

Hidden inside the predator’s jaws, opened wide enough to swallow the world, were not only teeth harder than steel and a red tongue.

Fwoosh!

A brilliant beam of light.

In an instant, blinding radiance dyed the world.

A pillar of light surged from the sacred stone held inside the guardian spirit’s mouth, passed over the fortress walls, and pierced the sky.

BOOOOM!

It was a pillar of light large enough to be seen from a hundred li away. Perhaps even a thousand.

Everyone could see that strange power, that wondrous sight.

The ten thousand warriors gathered in the Inner Palace.

And the immeasurable number of beasts filling the hill.

—Kyaaaaaaau!

—GRAAAWR!

With their roars, an unseen dam broke.

The beasts that had been waiting for their master’s command became a wave and swept across the vast grassland.

Rumble, rumble, rumble!

Thud, thud, thud!

Beneath the blazing sunlight, the earth shook and the wind scattered.

And at the very front of it all was one man.

“Let’s go.”

The quiet words slipped between his lips.

At the same time, the guardian spirit powerfully kicked off the ground.

Whooosh!

The Great War that would decide Nanman’s fate had begun.
```
