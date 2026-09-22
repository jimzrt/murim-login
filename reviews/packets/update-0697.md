<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0697.txt",
      "sha256": "5443ae1ecb0891eda92459348c0b73ce033bbf309ce92c7cceae63dda57cf567",
      "bytes": 12511
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "1e5d7eb736edfef073d60786c74891c1b4206b3e0b5ed3f81c9b48501770d2c7",
      "bytes": 1553
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0fa0ce441bd7946bb616710f6f9fe8a15bb991f8a20474364f6e85f49dd22728",
      "bytes": 205252
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "2ed3f9d8ce800ef71349dc66bac9fad0043c9a97ec5b7c591ef788a4e0d440fb",
      "bytes": 895
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "0d7059c2684239d9d08d8a81cb5b42dc6d033029977f9309f95326f8b9a91517",
      "bytes": 553
    },
    {
      "path": "characters/Honglan.md",
      "sha256": "616cce791274a71526c83734a15f66ba84cb302302501c40143bde610293e5a4",
      "bytes": 973
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "1be2c509e25c71e808dc7db1d3588a4ae619c658e6781b9181491adab570a677",
      "bytes": 1877
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "109984fb4d41f359d20241e40227e6f09524d52c4dbdfe98e95340565025beee",
      "bytes": 622
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "e3f9a0e076662d606df85c2ee68edf4813a87789cc02f03d1d5782e23163ceb8",
      "bytes": 699
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "92d1657e5ec1e8fb2a2e1887352fe9009b5ec7cb9ccd9a76729d7c7c1e82381c",
      "bytes": 770
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "2ecb1a2fdc8474add244bce678bf427bb3593e3e34a8d750777c961f072d2fa7",
      "bytes": 787
    },
    {
      "path": "characters/White Tiger.md",
      "sha256": "7138608decf3bab3aa41b79c01dead91bd267fe6bfb62d99c27d80e9e365dd07",
      "bytes": 588
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "d7a950bd22d870784449d4da718548c992a6cc540fbbf96d167ff90c3c2286ee",
      "bytes": 214766
    }
  ],
  "estimated_tokens": 11249
}
-->

# Durable State Update — Chapter 697

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 697. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 697. Profile updates may replace only one
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
  "chapter": 697,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 697,
    "continuity_sources": [697],
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
    "Jin Taekyung and the beast army have entered the Outer Palace and destroyed five watchtowers.",
    "Yohi has returned alive and is advancing beside Jin without restraints.",
    "The guardian spirit and Muyaho are accompanying Jin and Yohi at the head of the beast army.",
    "Nearly one thousand Inner Palace archers have aimed at Jin's group, but their resolve is wavering.",
    "Baeksang has publicly acknowledged Yohi and admitted betraying everyone.",
    "Baeksang became an unforgivable turncoat to pursue a purpose over several decades.",
    "Baeksang's confession reveals relief and despair rather than a plea for forgiveness.",
    "Thunder and dark clouds have covered the battlefield, and an unidentified voice has announced that it is already too late."
  ],
  "continuity_sources": [
    696
  ],
  "open_questions": [
    "What purpose did Baeksang pursue for decades?",
    "What has caused the thunder and dark clouds to cover the battlefield?",
    "Who spoke after the sky darkened, and why is it already too late?",
    "Will Baeksang's confession stop the Nanman warriors from fighting for him?"
  ],
  "safe_through": 696,
  "temporary_decisions": [
    "Use Whitey for Jin's nickname 흰둥아.",
    "Use civil war for 내전 and fighting spirit for 전의.",
    "Use the quoted paraphrase “Do everything in your power, then leave the result to Heaven and wait” for 진인사대천명.",
    "Retain guardian spirit for 수호령 and Great Chieftain for 대족장."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 초식     | **form**                                         | Numbered technique movement                           |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 살기     | **killing intent**                               |                                                       |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 은인     | **Benefactor**                               |
| 일격     | **One Strike**                         |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 홍란 | **Honglan** | Stage name of Ju Wongong's Lower District Sect singing courtesan; her real name is concealed. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 호북성 | **Hubei Province** | Province where the chapter’s Dark Heaven incidents occurred. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 황족 | **Huang tribe** | Nanman tribe involved in a recently settled dispute. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 수호령 | **guardian spirit** | Ancient title for the Black Tiger. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 홍란 | 진태경 | Lower District Sect courtesan to honored guest | honored guest | humble and formal | Introduces herself with 소녀 and addresses Taekyung as 귀인. |
| 홍란 | 은인 | rescued_survivor_to_rescuer | Benefactor | humble-formal | Honglan addresses Taekyung as Benefactor after he rescued her. |
| 진태경 | 홍란 | pursuer_to_hostile_opponent | you fucking bitch | profane and threatening | Taekyung demands Honglan's location and threatens her while she speaks through Song Ho. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 정호 | 진태경 | Shaolin Discipline Hall Master to patient and Benefactor | Benefactor Jin | formal-polite | Jung Ho repeatedly uses 진 시주 and 시주. |
| 진태경 | 정호 | patient to Shaolin Discipline Hall Master | Monk | polite and familiar | Taekyung addresses Jung Ho as 스님. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 진태경 | 백호 | human ally to intelligent spiritual beast | you | casual and familiar | Converses with White Tiger after interpreting its warning. |
| 백상 | 남천마후 | Nanman Great Chieftain to hostile demon empress | Southern Heaven Demon Empress | formal and shocked | Baeksang directly identifies the woman who appears before him. |
| 남천마후 | 백상 | Dark Heaven controller to coerced Nanman leader | Great Chieftain Baeksang / Palace Lord | playful, taunting, and threatening | She repeatedly addresses Baeksang while mocking his grief, acknowledging his effort, and issuing her order. |
| 백호 | 진태경 | guardian_spirit_to_human_ally | you | terse and irritated | The White Tiger responds telepathically after Jin calls it Whitey and jokes about its former name. |
| 진태경 | 수호령 | human ally to guardian spirit | guardian spirit | quiet and commanding | Jin whispers that they should go as they advance toward Baeksang. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 696
- **Aliases:** None
- **Role:** Baeksang is the Palace Lord of the Nanman Beast Palace and sole Great Chieftain of Nanman, and he has publicly admitted betraying all Nanman people to pursue a purpose maintained for decades.
- **Personality:** Cold, rigid, meticulous, and strategically resolute, yet burdened by regret, grief over Hwi's death, and a final conflicted impulse to spare others from the coming bloodshed.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of deceased Baekhwi, whom the Great Snow Fiend killed; he cultivated Yohi with gold and influence and used her support to advance Dark Heaven's preparations.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 696
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Honglan.md

# Honglan (홍란)

- **Safe through:** Chapter 619
- **Aliases:** None
- **Role:** Honglan is a Lower District Sect courtesan who uses a stage name, served as Ju Wongong's singing courtesan, and identifies herself as the Southern Heaven Demon Empress.
- **Personality:** Discreet about her real identity and professionally alluring.
- **Voice:** Clear, pure, and alluring, with humble formal speech toward honored guests.
- **Relationships:** Honglan is kept at Ju Wongong's side as a singing courtesan, belongs to the Lower District Sect, lost her clan and parents overnight as a child, can respond to Taekyung through Sound Transmission, is the sole surviving eyewitness to the Dongting Lake attack who knows several possible locations of the Dongting Fisherman's hidden refuges, corrupted the benevolent imugi in Dongting Lake and used it to kill many people, and can enthrall people and command them.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 696
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, and the leader of the beast-army assault confronting Baeksang inside the Nanman Beast Palace.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 696
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 672
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 695
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress is the strategist directing Baeksang's defense of Nanman's Inner and Outer Palaces while advancing a grand plan scheduled to begin within three days.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and regards Jin's destruction of her trap with amused surprise.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 690
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion; he helped Jin escape the underground prison by blocking the stairs and overpowering the Bai warriors.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

### White Tiger.md

# White Tiger (백호)

- **Safe through:** Chapter 696
- **Aliases:** Whitey
- **Role:** The White Tiger is the guardian spirit of the sacred stone, restored to its former silver-white tiger form and leading Jin Taekyung and the vast beast army into the Outer Palace.
- **Personality:** Irritable and contemptuous of Jin Taekyung's jokes.
- **Voice:** Telepathic, terse, and easily exasperated.
- **Relationships:** The White Tiger carries Jin Taekyung and Yohi, guards the sacred stone, and advances with Jin's forces.

## Korean source

```text
＃697화



“어쩌나. 이미 늦어 버렸는데.”

나른한 목소리가 내 귓가를 파고든다. 아니, 나뿐만이 아니다. 이 자리의 모두가 그 음성을 들을 수 있었다.

치명적일 만큼 매혹적이고, 그 이상으로 위험한 어떤 존재의 등장을 알리는 효시(嚆矢)를.

“남천마후(南天魔后)!”

나는 벼락같은 외침과 함께 고개를 돌렸다. 예기치 못한 상황에 석상처럼 굳어 버린 모두의 머리 위, 드높게 하늘을 향해 솟아 있는 어느 전각 위에서 풍성한 옷자락이 흩날린다.

지상을 굽어보던 고양이 같은 눈매가 반달처럼 휘었다.

“어머, 이게 누구실까.”

낯선 여인의 얼굴. 그러나 잊을 수 없는 목소리와 특유의 느낌.

틀림없다. 나는 확신과 함께 씹어뱉듯이 목소리를 토해 냈다.

“나다, 이 썅년아.”

용암을 삼킨 것처럼 뱃속이 뜨겁게 끓어오른다. 창대를 굳게 말아쥔 손가락은 잘게 떨렸고, 가슴은 빠르게 두방망이질 치고 있었다.

백상을 마주했을 때와는 비교도 할 수 없을 만큼 거세게 휘몰아치는 감정의 격랑(激浪).

하지만 지금의 나를 사로잡은 것은, 단순한 적의와 분노뿐만이 아니었다.

‘강하다.’

이 정도였던가?

단지 시선을 마주친 것만으로도 가슴 한구석이 철렁 내려앉는 듯한 기분이다.

호북성에서의 사건 이후 어언 수개월.

나는 그간 얻은 깨달음만큼 상대의 진면목을 조금이나마 엿볼 수 있게 되었고, 오늘 다시 마주한 남천마후는 상상했던 것 이상의 괴물이었다.

이 자리의 그 누구도 짐작할 수 없는 경지.

그러나 내 눈은, 한껏 날 선 감각은 상대가 숨긴 힘을 더듬고 있었다.

부드럽게 휘어진 눈매에 가려진 흉포함과 가느다란 체구에 웅크린 거대한 어둠을.

“개 같은 년.”

“아하하! 역시. 역시!”

무엇이 그리 우스운지, 내게 욕설을 듣고도 배꼽을 잡으며 깔깔 웃은 남천마후가 나를 향해 입꼬리를 말아 올렸다.

“시원시원하시네요. 내가 이래서 은인을 좋아한다니까.”

“뭐라고?”

“벌써 잊었나요? 그날, 시신이 떠다니던 차가운 동정호에서 누가 날 구했는지.”

“……!”

잊을 수 있을 리가.

그 후로도 몇 번이나 그 순간을 떠올리며 후회했으니까.

이 손으로 직접 남천마후를 구했기 때문에?

틀렸다. 그날 내가 구한 것은 남천마후가 아닌 홍란이었으니까.

호북에서의 남천마후는 어떤 얼간이 황족이 총애하는 아름다운 가기(哥妓)에 불과했다.

처음부터 끝까지 의도적으로 내게 접근했고, 내가 오지 않았다 하여도 살아남았을 것이다.

다만 한 가지, 내가 유일하게 후회하는 것은…… 흉수를 눈앞에 두고도 알아보지 못한 멍청함이었다.

누군가에게는 유희(遊戲)와 다름없었던 농락을 알아차리지 못한 나 자신에 대한 분노. 그리고 더욱 큰 희생을 막지 못한 자책.

스륵.

“이제야 예의를 갖춰 인사드릴 수 있겠네요.”

풍성한 옷자락을 들어 올리며 홍란이, 아니. 남천마후가 사뿐히 고개를 숙였다.

“천녀(賤女), 홍란이 은인을 뵙습니다.”

그 순간. 나는 섬전처럼 일장(一掌)을 뻗었다.

화아악!

삽시간에 증발하는 수분.

끔찍한 열기를 머금은 화염신장(火焰神掌)의 장력이 남천마후에게 도달하기까지 걸린 시간은, 그야말로 찰나에 불과했다.

하지만.

서걱!

백상조차 쉽게 막지 못할 강대한 장력이, 두부처럼 반으로 갈라지기까지 걸린 시간은 그보다도 짧았다.

퍼어엉!

어느새 먹구름이 드리워진 하늘 아래, 방향을 잃은 채 두 갈래로 튕겨 나간 장력이 허공에서 폭발한다.

눈앞에서 벌어진 이 믿을 수 없는 광경에 곳곳에서 경악성이 흘러나왔다.

“이, 이게 무슨.”

“지, 지금 내가 뭘 본 거지? 지금 저 여인이…….”

“남천마후. 분명 남천마후라고 했어.”

이 자리에는 그 별호를 아는 이도, 모르는 이도 있다.

하지만 그런 사실은 중요하지 않다. 얼마 지나지 않아 모두가 알게 될 테니까.

남천마후가 누구인지. 얼마나 악랄하며 무시무시한 힘을 숨긴 괴물인지.

나는 차갑게 식은 눈빛으로 높게 솟은 전각 끄트머리를 응시했다.

그곳에는 괴물이라 칭하기에는 너무나도 아름다운 여인이 흐트러진 궁장을 정돈하고 있었다.

“흐음. 나름 예의를 차린 건데, 인사에 답하는 태도가 썩 마음에 들지는 않네요. 하지만 너그러운 마음으로 넘어가 드릴게요. 구명지은(救命之恩)을 입은 처지에 당장 은인의 눈깔을 파 버릴 수는 없으니까.”

천진난만한 목소리에 담긴 살기(殺氣)가 느껴진다. 오히려 마음이 차분해진 내가 대답했다.

“아가리 닥쳐.”

“말씀도 험하셔라. 아가리는 짐승한테나 쓰는 말이랍니다. 한 가지 예를 들자면…….”

흐려지는 말꼬리와 함께 남천마후의 시선이 미세하게 아래로 움직인다.

그리고 그 방향의 끝에, 어느덧 이빨을 드러낸 한 마리의 거대한 백호가 있었다.

“그래요. 바로 저 흉측한 짐승에게나 어울리는 단어죠.”

크르르릉.

낮은 울음소리를 토해 낸 수호령이 남천마후를 노려보았다. 바짝 긴장한 녀석의 근육이 느껴졌다.

- 흉측한 짐승이라……. 하면 너와 같은 인간은 뭐라 불러야 옳겠느냐?

지금까지의 의념(意念)이 전음과 같은 맥락이었다면, 이번에는 모두가 들을 수 있는 목소리와 같다.

내궁의 안팎을 둘러싼 수많은 전사가 흡, 하고 헛숨을 삼키는 가운데, 눈을 동그랗게 뜬 남천마후가 이내 피식 웃으며 나를 바라보았다.

“정정해야겠네요. 흉측할 뿐만 아니라, 흥미롭기까지 한 짐승으로.”

“글쎄.”

나는 창대를 쥔 손에 힘을 더하며 입을 열었다.

지금 이 순간에도 수십 가지의 움직임과 초식이 뇌리를 스치는 중이다.

가장 빠르고, 치명적인 일격으로 상대의 숨통을 끊어 낼 방법들이.

“잠시 후에는 더 흥미로워질 거야. 이 녀석이 네 목덜미를 물어뜯을 테니까.”

“짐승은 짐승일 뿐이에요. 하늘의 부름을 기다리던 어떤 어리석은 이무기도 마찬가지였죠.”

- 그는 어리석었던 것이 아니라, 그저 선했을 뿐이다. 수백 년간 쌓아 온 수행을 비롯한 자신의 목숨마저 희생할 만큼.

수호령이 청백색의 눈동자로 남천마후를 응시한다. 마치 모든 것을 꿰뚫어 볼 듯한 눈빛으로.

- 너를 안다.

남천마후의 입가에 엷은 미소가 맺혔다.

“썩 반가운 소식은 아닌데. 노린내 나는 짐승 따위에는 관심 없거든.”

- 이무기의 기억 속에서 너를 보았지. 한없이 어둡고, 악의로 가득 찬 어느 인간의 모습을.

“기억?”

- 세상을 이루는 모든 것은 본질과 흔적을 지니는 법. 그리고 그런 의미에서 기억 속의 너는…….

“아름다웠겠지. 눈이 부실 만큼.”

- 늙고 추악했다. 인간이라는 것이 믿기지 않을 만큼.

“……!”

- 그것이 네 본질이다. 자신의 본 모습을 부정하고, 증오하며 기나긴 세월을 연명해 온 악귀(惡鬼)와 다름없지.

수호령의 의념이 끝을 맺은 그 순간, 적막이 찾아왔다.

연이어 찾아온 충격에 웅성거리던 사람들도, 낮은 울음소리를 흘리던 수많은 맹수도 숨을 죽이고 몸을 낮추었다.

그리고 이 모든 것의 중심에, 한 사람이 있었다.

화아아아악!

풍성한 궁장의 소매가 터질 듯이 부풀어 오른다.

끔찍하리만치 거대한 기파가 태산 같은 압력으로 사방을 짓누르고, 살아 있는 모든 것을 얼어붙게 했다.

콰득. 콰드득.

바람이 멈춘다. 막대한 압력을 이기지 못한 전각의 지붕이 서서히 붕괴하기 시작한다.

“……그래?”

어느덧 씻은 듯이 사라진 입가의 미소. 깊게 가라앉은 눈동자가 발아래 펼쳐진 세상을 굽어보았다.

“늙고, 추악하다. 그래. 그렇단 말이지.”

담담하게 뇌까린 남천마후가 문득 고개를 돌려 나를 응시했다.

“여기까지 온 건 칭찬해 주지. 하루. 아니, 반나절만 빨랐다면 나조차도 결과를 장담할 수 없었을 테니까.”

다르다. 말투도. 분위기도.

하지만 오히려 내 마음은 차분해졌다.

사람이 무서운 것은 본색을 드러내지 않았을 때다. 마지막까지 갖고 있던 웃음과 여유를 잃었을 때, 비로소 틈이 생긴다.

‘더군다나.’

내게는 아직 감춰 둔 패가 있다. 최악의 상황이 눈앞에 들이닥친다 해도 힘을 발휘할 수 있는 한 수가.

그렇기에 말할 수 있었다.

“음. 이건 진짜 궁금해서 묻는 건데.”

바로 지금처럼.

“실제로는 얼굴이 얼마나 빻았길래 저런 말을 듣는 거지?”

“……!”

“혹시 전생에 절구였나?”

다음 순간.

“그 말, 후회하게 해주지.”

짧은 침묵을 깨트리는 서늘한 목소리와 함께, 수많은 먹구름이 하늘을 가렸다.

그리고…….

솨아아아악!

내궁의 뒤를 감싸 안은 거대한 절벽으로부터, 칠흑의 빛무리가 뿜어져 나오기 시작했다.

‘저건.’

보는 것만으로도 숨이 막히는 기이한 광경.

그래, 그건 ‘균열’이었다.



* * *



구구구구궁!

땅이, 세상이 흔들린다. 수백 년. 아니, 수천 년간 그 자리를 지키고 있었을 거대한 절벽이 굉음과 함께 벌어지기 시작한다.

“아. 아아…….”

그 기이하고도 두려운 광경에 누군가는 경악에 찬 신음을.

‘이리되었구나. 끝끝내.’

누군가는 절망 어린 뇌까림을 마음속으로 토해 냈고.

“끝이다. 전부.”

분노에 사로잡혀 있던 누군가는 환희에 찬 눈빛으로 자신이 이룩한 광경을 지켜보았다.

‘드디어. 드디어!’

남천마후는 조금 전 찾아왔던 분노조차 잊은 채 몸을 떨었다.

어찌 그러지 않을 수 있겠나.

기나긴 인고의 세월 끝에 거둔 결실이다.

호북성에서와는 비교도 할 수 없이 크고, 강력한 저 ‘균열’은 바로 자신의 작품이었고, 전지전능하신 천주의 뜻이 이 땅에 강림하는 순간이기도 했다.

콰아아아아아!

칼날과도 같은 광풍(狂風)이 사방을 휩쓴다. 서서히 벌어지는 절벽의 틈새 사이로, 지극히 어둡고 끈적한 기운이 세상을 갉아 먹으며 기어 나오기 시작했다.

생명을 오염시키고, 이 땅을 점령할 마기(魔氣)가!

- 크륵, 크르륵!

- 캬우우우!

“컥. 커헉!”

“이, 이보게! 갑자기 왜…… 크륵.”

아직 균열이 완전히 열리지 않았음에도, 그 힘은 이미 사방으로 뻗어 나가는 중이었다.

보라.

저 넘실거리는 어둠을. 새하얀 흰자위를 드러낸 채 몸부림치며, 새로운 변화를 기다리고 있는 수많은 짐승과 인간들을.

그리고 이제 곧 균열로 인한 변화가 시작될 것이다.

‘아니, 아니지.’

이것은 변화가 아닌, 진화(進化)다.

더욱 강력하고 아름다운 존재로 거듭나는 과정인 동시에, 전능하신 천주께서 하찮은 생명체들에게 내리는 축복.

어느덧 입가에 진득한 미소를 그린 남천마후의 시선이, 문득 한 사람에게 닿았다.

‘진태경.’

우뚝 선 채로 자신의 눈 앞에 펼쳐진 믿을 수 없는 아득한 광경을 바라보는 한 청년.

남천마후로서는 그 모습이 너무나도 우습고, 가여웠다.

단숨에 목을 잡아 뜯어 버리고 싶을 만큼.

‘넌…… 이곳에 오지 말았어야 했어.’

마음속으로 중얼거린 남천마후는 진태경을 향해 신형을 날렸다.

아니, 날리려던 바로 그 순간이었다.

화아아악!

어디선가 터져 나온 거대한 광휘가, 어둠을 집어삼켰다.
```

## Final English reading copy

```markdown
# Chapter 697

“What a shame. It’s already too late.”

A languid voice slipped into my ears.

No. It wasn’t just me. Everyone here could hear that voice.

The herald announcing the arrival of something dangerously enchanting—and even more dangerous than it was enchanting.

“The Southern Heaven Demon Empress!”

I whipped my head around at the thunderous shout.

Above the heads of everyone frozen like stone statues by the unexpected situation, voluminous robes fluttered atop a pavilion that rose high toward the sky.

The catlike eyes looking down at the ground curved like half-moons.

“Oh my, who could this be?”

An unfamiliar woman’s face.

But the voice and distinctive feeling were unforgettable.

There was no doubt.

With that certainty, I spat out the words as though chewing them.

“It’s me, you fucking bitch.”

My stomach seethed with heat, as if I had swallowed lava. The fingers gripping the spear shaft tightly trembled, and my heart pounded violently against my ribs.

A tidal wave of emotion raged through me—far more fiercely than when I had faced Baeksang.

But simple hostility and anger were not the only things that had seized me.

*She’s strong.*

Had she always been this strong?

Just meeting her gaze made my heart seem to drop into my stomach.

Several months had passed since the incident in Hubei Province.

The insight I had gained during that time allowed me to glimpse a little more of my opponent’s true nature. And the Southern Heaven Demon Empress I faced again today was a monster beyond anything I had imagined.

A realm no one else here could even begin to guess at.

Yet my eyes—and my senses, honed to their sharpest—were tracing the power she concealed.

The ferocity hidden behind those gently curved eyes.

The enormous darkness coiled within that slender frame.

“You fucking bitch.”

“Ahaha! Just as I expected. Just as I expected!”

Whatever she found so funny, the Southern Heaven Demon Empress clutched her stomach and laughed even after being cursed at. Then she curled up the corners of her mouth at me.

“You’re so refreshingly straightforward. That’s what I like about you, Benefactor.”

“What did you say?”

“Have you forgotten already? On that cold Dongting Lake, where corpses floated on the water, who was it that saved me?”

“……!”

As if I could forget.

I had regretted that moment countless times afterward.

Was it because I had saved the Southern Heaven Demon Empress with my own hands?

No.

The person I had saved that day had not been the Southern Heaven Demon Empress, but Honglan.

The Southern Heaven Demon Empress in Hubei had been nothing more than a beautiful singing courtesan favored by some idiot of the Huang tribe.

She had deliberately approached me from beginning to end, and even if I had not come, she would have survived.

There was only one thing I truly regretted.

My stupidity in failing to recognize the culprit even when she had been standing right in front of me.

My anger at myself for failing to realize I had been toyed with for someone else’s amusement.

And my guilt at failing to prevent an even greater sacrifice.

Rustle.

“At last, I can greet you properly.”

Lifting the voluminous hem of her robes, Honglan—or rather, the Southern Heaven Demon Empress—gracefully lowered her head.

“This lowly woman, Honglan, greets her Benefactor.”

At that moment, I thrust out one palm like a flash of lightning.

Fwoosh!

Moisture evaporated in an instant.

The force of the Flame Divine Palm, carrying horrific heat, reached the Southern Heaven Demon Empress in less than a heartbeat.

But—

Slice!

The powerful palm force, which even Baeksang could not have blocked easily, was split cleanly in two like tofu in even less time.

Boom!

Beneath the sky now covered by dark clouds, the divided palm force ricocheted off in opposite directions before exploding in midair.

Shocked voices rose from every direction at the unbelievable scene unfolding before them.

“W-what is this?”

“W-what did I just see? That woman just—”

“The Southern Heaven Demon Empress. She definitely said the Southern Heaven Demon Empress.”

Some people here knew that title. Others did not.

But that fact did not matter.

Before long, everyone would learn.

Who the Southern Heaven Demon Empress was.

How vicious she was, and what kind of terrifying power the monster concealed.

I stared coldly at the edge of the pavilion rising high above us.

A woman was standing there, straightening her disheveled court robes. She was far too beautiful to be called a monster.

“Hm. I did try to show some courtesy, but I can’t say I’m especially pleased with the way you answered my greeting. Still, I’ll let it pass out of my generous nature. I can’t gouge out my Benefactor’s eyes right away when I owe him a life-saving debt.”

I could feel the killing intent contained in her innocent voice.

Rather than being shaken, I grew calmer and answered.

“Shut your damn mouth.”

“What rough language. That word is only used for beasts. For example…”

Her voice trailed off as the Southern Heaven Demon Empress’s gaze shifted slightly downward.

At the end of that gaze was an enormous White Tiger baring its teeth.

“Yes. It’s a word that suits that hideous beast perfectly.”

Grrrrr.

The guardian spirit growled low and glared at the Southern Heaven Demon Empress. I could feel its muscles tense as it prepared itself.

—A hideous beast, is it? Then what should a human like you be called?

If the guardian spirit’s thoughts had followed the same pattern as Sound Transmission until now, this was different.

Its voice was like something everyone could hear.

As countless warriors surrounding the Inner Palace inside and out drew in sharp breaths, the Southern Heaven Demon Empress opened her eyes wide. Then she let out a quiet laugh and looked at me.

“I’ll have to correct myself. Not only a hideous beast, but an interesting one as well.”

“I doubt it.”

I tightened my grip on the spear shaft and opened my mouth.

Even now, dozens of movements and forms flashed through my mind.

Ways to cut off my opponent’s breath with the fastest, most lethal strike.

“You’ll find it even more interesting in a moment. This one’s going to bite through the back of your neck.”

“A beast is still a beast. The same was true of a certain foolish imugi that waited for Heaven’s call.”

—He was not foolish. He was merely kind. Kind enough to sacrifice even his life, along with the cultivation he had built over hundreds of years.

The guardian spirit stared at the Southern Heaven Demon Empress with its blue-white eyes, its gaze seeming to pierce through everything.

—I know you.

A faint smile appeared around the Southern Heaven Demon Empress’s lips.

“That isn’t particularly welcome news. I have no interest in some musk-reeking beast.”

—I saw you in the imugi’s memories. The form of a human who was endlessly dark and filled with malice.

“Memories?”

—Everything that makes up the world possesses an essence and traces. And in that sense, you in its memories were…

“Beautiful, I suppose. Dazzlingly so.”

—Old and hideous. So much so that it was hard to believe you were human.

“……!”

—That is your essence. You have denied and hated your true form, eking out a long existence. You are no different from a Fiend.

The moment the guardian spirit’s thoughts ended, silence descended.

The people who had been murmuring from shock, as well as the countless beasts that had been making low growls, held their breath and lowered their bodies.

And at the center of it all stood one person.

Fwoooooosh!

The sleeves of the voluminous court robes swelled as though they might burst.

A terrifyingly immense wave of qi pressed down in every direction with the weight of a mountain, making every living thing freeze in place.

Crack. Crack.

The wind stopped.

The roof of the pavilion, unable to withstand the tremendous pressure, began to collapse.

“…Is that so?”

The smile had vanished from her lips as though it had been washed away.

Her deeply sunken eyes looked down upon the world spread out beneath her feet.

“Old and hideous. Yes. So that’s how it is.”

The Southern Heaven Demon Empress muttered calmly, then suddenly turned her head and stared at me.

“I’ll praise you for making it this far. If you had been even a day—or no, half a day—earlier, even I couldn’t have guaranteed the outcome.”

She was different.

Her way of speaking. Her atmosphere.

Yet my mind grew calmer instead.

People were frightening when they did not reveal their true nature. When they lost the smile and composure they had maintained until the very end, a gap finally appeared.

*More importantly.*

I still had a hidden card.

A move I could bring into play even if the worst possible situation came crashing down before me—as long as I still had the strength to use it.

That was why I could say this.

“Hm. I’m asking because I’m genuinely curious.”

Just as I was doing now.

“How ugly is your face, really, for someone to say something like that to you?”

“……!”

“Were you a mortar in your past life?”

The next moment—

“I’ll make you regret those words.”

A cold voice shattered the brief silence, and countless dark clouds covered the sky.

And then…

Fwoooooosh!

From the enormous cliff embracing the rear of the Inner Palace, a mass of pitch-black radiance began to pour forth.

*That’s…*

It was a strange sight that made it difficult to breathe just by looking at it.

Yes.

It was a *rift*.

* * *

Rumble, rumble, rumble!

The earth trembled.

The world shook.

The enormous cliff that had stood in that place for hundreds—no, perhaps thousands—of years began to split apart with a tremendous roar.

“Ah. Ahhh…”

At the strange and terrifying sight, someone let out a shocked groan.

*So it has come to this. At long last.*

Someone else spat out a despairing mutter in the depths of their heart.

“It’s over. All of it.”

Someone who had been consumed by anger watched the scene they had created with eyes filled with rapture.

*At last. At last!*

The Southern Heaven Demon Empress trembled, having already forgotten even the anger that had seized her moments earlier.

How could she not?

This was the fruit she had harvested after enduring for so many long years.

That rift was incomparably larger and more powerful than the one in Hubei Province.

It was her own creation.

It was also the moment when the will of the omnipotent Lord of Heaven descended upon this land.

Kraaaaaaash!

A gale as sharp as a blade swept in every direction.

Through the widening gap in the cliff, an intensely dark and viscous energy began to crawl out, gnawing away at the world.

Demonic qi that would corrupt life and conquer this land!

—Krrk, krrrk!

—Kyaaaaa!

“Ghk. Guhk!”

“W-what’s happening all of a sudden—krrk!”

The rift had not even opened completely, yet its power was already spreading in every direction.

Look.

Look at that surging darkness.

At the countless beasts and humans writhing with their eyes rolled back to show their white sclera, waiting for a new change.

And soon, the change caused by the rift would begin.

*No. That’s not right.*

This was not change.

It was *evolution*.

It was the process of being reborn as more powerful and beautiful beings, as well as a blessing bestowed by the omnipotent Lord of Heaven upon lowly lifeforms.

The Southern Heaven Demon Empress’s gaze, a thick smile spreading around her lips, suddenly fell upon one person.

*Jin Taekyung.*

A young man stood tall, staring at the unbelievable, overwhelming spectacle unfolding before him.

To the Southern Heaven Demon Empress, his appearance was laughable and pitiful.

Enough to make her want to rip his throat out in one go.

*You… should never have come here.*

Muttering those words inwardly, the Southern Heaven Demon Empress launched herself toward Jin Taekyung.

No.

It was at the very moment she was about to launch herself that—

Fwoooooosh!

A tremendous radiance burst from somewhere and swallowed the darkness.
```
