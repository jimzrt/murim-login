<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0681.txt",
      "sha256": "b644849efdc160ddf28e5f31455b3949649d8ab46355e0b54641b068e6c1dd9b",
      "bytes": 12631
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "5222f71836388412c5355cc252379c215f96e5cb834272433d936380b6b548f8",
      "bytes": 2224
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b351f5178dba4d41730778b0904769d9208406a8782b25a6eb5ac14ba5e3e006",
      "bytes": 203156
    },
    {
      "path": "characters/Black Hand.md",
      "sha256": "bb58873013cccef460b91cc0e920f18181ad3917a4ddb92458e058ebc94e2c5a",
      "bytes": 732
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "5f673a104c7d781919e9c1027c02138a209cba463b0bcb769dbc39fc3d772193",
      "bytes": 553
    },
    {
      "path": "characters/Great Snow Fiend.md",
      "sha256": "b8756349322a413d324c4ad17dcbe75b57a12a2f880d811bac1c81bc284504c4",
      "bytes": 562
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "e5811ba80f34b35509283f6c591d28a8d92269d0bcc784a423c8dad7fe72dc6a",
      "bytes": 1702
    },
    {
      "path": "characters/Jin Hayeon.md",
      "sha256": "9b813dd9f19c0b4082ba764555eb0e15a532077d0ed6db6c6135a1352daf4fae",
      "bytes": 1518
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "60184edec2ab332a10f76c423eacc1c83760aaa9d776ef454871d82bb5394622",
      "bytes": 1858
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "c1fdd0cfb07f0ee1759e59d7bacaf53a2b111e185c67578fd81f19e9dd3c550b",
      "bytes": 622
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "032fab6a45f2d352c7e00e1761629d0c46f9ec2f1aa7998e55ccf842ae2b8f74",
      "bytes": 210448
    }
  ],
  "estimated_tokens": 11274
}
-->

# Durable State Update — Chapter 681

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 681. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 681. Profile updates may replace only one
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
  "chapter": 681,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 681,
    "continuity_sources": [681],
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
    "The Great Snow Fiend, former ruler of Great Snow Mountain, has revealed himself as the slender twin-wheel master fighting Jin in the Poisonblood Grounds.",
    "The Great Snow Fiend and Black Hand Fist Demon are attacking Jin Taekyung together.",
    "Jin is wielding White Flame and using blue-white fire techniques against them.",
    "The Great Snow Fiend's Finger Qi has pierced Jin's shoulder, and his Yin-Cold Qi has clashed with Jin's Flame Divine Palm.",
    "Muyaho remains alive beside Jin despite losing much of his fur to the twin wheels.",
    "The Yangtze River Channel League's swift ship has arrived at the reconnaissance squad's position with an unidentified person aboard.",
    "The Han Chinese reconnaissance members remain detained without harm, with their Sleep Acupoints struck.",
    "Namho plans to escort the Han Chinese to the Central Plains so the Murim Alliance and Sichuan's major sects can aid Nanman.",
    "Yohi and Heugung remain captive and alive, awaiting the Southern Heaven Demon Empress's return.",
    "The Southern Heaven Demon Empress remains absent while her agents threaten Jin's allies."
  ],
  "continuity_sources": [
    680,
    679
  ],
  "open_questions": [
    "Can Jin survive and prevail against the Great Snow Fiend and Black Hand Fist Demon?",
    "Why did the Great Snow Fiend intervene to protect or coordinate with the Black Hand Fist Demon?",
    "Who arrived on the Yangtze River Channel League's swift ship, and why did it come directly to the reconnaissance squad's position?",
    "Can Namho's group reach the Central Plains and bring reinforcements before Nanman is overwhelmed?",
    "Will the Blood Monk act with Baeksang and Dark Heaven, and what will happen to the Beast Miao King's loyalists in the Inner Palace?"
  ],
  "safe_through": 680,
  "temporary_decisions": [
    "Use Great Snow Fiend for 대설귀.",
    "Keep Black Hand Fist Demon and Black Hand distinct for 흑수권마 and 흑수.",
    "Preserve Jin's abrupt register changes and profanity as deliberate psychological provocation.",
    "Render the old man's cold energy as Yin-Cold Qi and his shoulder-piercing attack as Finger Qi."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 진하연    | **Jin Hayeon**    |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 태원진가   | **Jin Family of Taiyuan**        |
| 열화문    | **Fire Gate Clan**               |
| 종남파    | **Zhongnan Sect**                |
| 소림     | **Shaolin**                      |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 장문인    | **Sect Leader**                              |
| 선배     | **Senior**                                   |
| 일격     | **One Strike**                         |
| 헌터      | **Hunter**            |
| 태원     | **Taiyuan**            |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 귀가      | **your family**                                                 |
| 흑수 | **Black Hand** | Sadistic Dark Heaven agent and Supreme Peak master. |
| 흑수권마 | **Black Hand Fist Demon** | Sobriquet revealed by Black Hand. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 대설귀 | **Great Snow Fiend** | Fiend who ruled Great Snow Mountain and killed Baekhwi and Venerable Wusang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 평화 | **Peace Guild** | Guild name. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 한서불침 | **Unaffected by Cold and Heat** | Condition attributed to Taekyung after opening both vessels. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 음양쌍괴 | **Yin-Yang Twin Freaks** | Shared epithet of Flame Tiger and Han Su. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 소림혈사 | **Shaolin Bloodshed** | Past incident cited by Hwangbo Eom. |
| 음양 | **Yin and Yang** | Paired energies whose harmony has been disrupted in Jeok Cheongang. |
| 음한지기 | **Yin-Cold Qi** | Cold-aligned energy required in the treatment elixir. |
| 사혈 | **lethal acupoint** | An acupoint whose strike can kill. |
| 지풍 | **Finger Qi** | Invisible qi attack fired by the Western Heaven Demon Lord. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 독혈지 | **Poisonblood Grounds** | Hidden poisonous region created by the Five Poisons Sect inside Ailao Mountain. |
| 대설산 | **Great Snow Mountain** | Mountain where Baeksang's wartime account reaches its next episode. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 진태경 | 진하연 | older_brother_to_younger_sister | Jin Hayeon | blunt-familiar; deliberately stern | Taekyung uses Hayeon's full name to make her hesitate while defending his implausible explanation for sleeping forty-two hours. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 엄마 | son_to_mother | Mom | casual and startled | Jin cries out to his mother as she charges at him during the hospital visit. |
| 엄마 | 진태경 | mother_to_son | my son | warm and affectionate | Taekyung's mother praises him during the public welcome. |
| 진태경 | 백호 | human ally to intelligent spiritual beast | you | casual and familiar | Converses with White Tiger after interpreting its warning. |
| 진태경 | 흑수 | hostile_martial_opponent | Black Hand | mocking and profane | Jin sarcastically addresses Black Hand after hearing his sobriquet. |
| 흑수 | 진태경 | hostile_Dark_Heaven_agent_to_enemy_martial_artist | Blazing Flame Divine Dragon Jin Taekyung | taunting and murderous | Black Hand identifies Jin while claiming that killing him will make the sobriquet famous. |

## Listed compact profiles

### Black Hand.md

# Black Hand (흑수)

- **Safe through:** Chapter 680
- **Aliases:** Black Hand Fist Demon (흑수권마)
- **Role:** Black Hand is a sadistic Dark Heaven agent and Supreme Peak master acting under orders associated with the Southern Heaven Demon Empress.
- **Personality:** Black Hand is cruel, gleeful, predatory, and fascinated by the despair of his victims.
- **Voice:** Black Hand speaks in archaic first person with drunken mockery, humiliating insults, and casual threats.
- **Relationships:** Black Hand is the captor and torturer of Yohi and Heugung and an enemy of Jin Taekyung; a colder senior figure can command him to obey the Demon Empress's orders.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 679
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Great Snow Fiend.md

# Great Snow Fiend (대설귀)

- **Safe through:** Chapter 680
- **Aliases:** None
- **Role:** The Great Snow Fiend is the former ruler of Great Snow Mountain and a fiend who killed Baekhwi and Venerable Wusang during the Great Faction War; he is now fighting Jin Taekyung alongside the Black Hand Fist Demon.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Enemy of Baeksang, Baekhwi, Venerable Wusang, the Beast Miao King, and the allied Southern Army.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 676
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Hayeon.md

# Jin Hayeon (진하연)

- **Safe through:** Chapter 552
- **Aliases:** Hayeon; Taekyung’s younger sister
- **Role:** High-school senior who has completed the college entrance exam and believes she missed a perfect score by one English question
- **Personality:** Sharp-tongued, academically gifted, impatient with Taekyung’s evasions, warmer beneath the teasing, and intensely fond of cats
- **Voice:** Bratty, fast, blunt sibling banter; turns brighter when discussing school and her interests
- **Relationships:** Taekyung’s younger sister; daughter of Taekyung’s mother

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 679
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, and an escaped prisoner still facing public execution at noon in two days.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 679
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃681화



순간, 그런 생각이 들었다.

흑수권마가 없었다면. 내가 지풍(指風)을 피했더라면.

하필이면 쌍장이 맞닿은 그 순간, 지풍이 관통한 어깨에서 통증이 올라오지 않았다면.

상대가 익힌 무공이 음한지기(陰寒之氣)라는 것을 알았더라면.

만약, 만약 그랬다면…….

지금쯤 서 있는 것은 누구였을까.

하지만 의문에 대한 답을 찾을 만한 시간은 주어지지 않았다.

콰창!

얼어붙은 불꽃이 사그라지고, 화염마저 집어삼킨 음한지기가 터질 듯이 부풀어 오른다.

공간을 뒤흔드는 미증유(未曾有)의 공력 너머, 새하얀 빛에 휩싸인 누군가의 손이 내 가슴을 짚었다.

툭.

그 순간, 내 머릿속을 채운 건 한 가지 생각뿐이었다.

차갑다.

콰아아앙!

사방으로 휘몰아친 냉기의 폭풍.

그 중심에 있던 나를 덮친 것은, 전신을 후려치는 맹렬한 바람과 빠르게 스쳐 지나가는 주위의 풍경. 그리고 등을 통해 전해지는 어마어마한 반발력이었다.

콰드드득!

나무. 바위. 풀. 거기에 더해 재수 없이 휘말린 알 수 없는 생물들까지.

죽어 있던 것이든, 산 것이든 상관없었다.

오발된 포탄처럼 뒤로 튕겨 나간 내 신형과 맞닥트린 모든 것들은 온통 꺾이고, 부서지고, 터져 버렸으니까.

다만 내 의지가 조금도 반영되지 않은 그 길의 중간에 두터운 석벽(石壁)이 가로막고 있었다는 것은, 불행이자 다행이었다.

콰앙! 드드득!

몽롱한 와중에도 느껴지는 격통.

매 순간 시야를 휙휙 스쳐 지나가던 풍경이 드디어 멈췄지만, 그건 수십 여장을 튕겨 나가 석벽 깊숙이 박혀 버린 나 역시 마찬가지다.

‘빌어……먹을.’

안간힘을 다해 쥐어 짜낸 목소리는 입술 사이로 흘러나오지 못했다.

세상은 붉으면서도 흐릿했고, 귀에서는 끊임없이 이명(耳鳴)이 울려 퍼지고 있었다.

삐빅! 삐빅! 삐빅!

아무리 그래도 이명치고는 좀 독특한데.

“……시벌.”

나는 허탈한 뇌까림과 함께 고개를 들었다.

평소의 맑은 종소리가 아닌, 위험을 뜻하는 경고음과 함께 십여 개가 넘는 홀로그램 창이 허공에 떠올라 있었다.

‘된통 당했구만. 아주.’

나도 모르게 쓴웃음이 흘러나온다.

온갖 부상을 여파로 쉴 새 없이 올라오는 통증.

신체 내부로 침투한 음한지기의 냉기에 파르르 떨리는 손발은 한서불침(寒暑不侵)의 경지를 무색하게 만들었다.

‘일어나야 하는데. 다시 싸워야 하는데…….’

내 바람과 달리, 나사가 느슨해진 몸뚱어리는 쉽사리 말을 듣지 않는다.

춥고, 피곤했다.

지금 당장 눈을 감으면 오랜만에 푹 잘 수 있을 것 같았다.

그래. 어떤 꿈이나 깨우는 사람도 없이, 허리가 아플 때까지 자고 나면 모든 게 나아져 있을 거다.

깨어났을 때쯤에는 전신을 엄습하는 통증도, 말을 듣지 않는 이 빌어먹을 몸뚱어리도 멀쩡해질 것이고, 따뜻한 극세사 이불 안에서 꼼지락거리며 스마트폰을 보고 있으면 문틈으로 엄마의 목소리가 들려오겠지.

- 진태경, 진하연. 밥 다 차려 놨으니까 얼른 나와.

그럼 나는 어기적어기적 일어나 부엌으로 향할 테고, 앞서 들려온 말과는 달리 텅 비어 있는 식탁에 수저와 반찬을 놓으며 식사를 준비할 것이다.

등 돌린 엄마의 어깨너머에서 풍겨 오는 구수한 된장찌개 냄새를 맡으면서.

‘아, 좋다.’

단지 떠올리는 것만으로도 마음이 평화로워지는 생각들.

나도 모르게 올라가는 입꼬리와는 반대로 눈꺼풀은 자꾸만 아래로 향했다.

스윽.

얼굴을 훑고 지나가는 까슬까슬하고, 축축한 무언가.

천천히 눈을 뜬 내 시야에 가장 먼저 들어온 것은, 날카로운 이빨과 맑은 청백색 눈동자였다.

- 끼이잉.

눈이 마주치기 무섭게 강아지처럼 낑낑거리는 백호의 모습에 피식 실소가 흘러나온다.

“……너냐?”

- 끙. 끄응.

비록 알아듣지는 못해도 충분히 느껴졌다. 저 울음소리에 무슨 뜻이 담겨 있는지. 어떤 말을 전하고 싶어 하는지.

“후우.”

호흡과 함께 찾아오는 통증.

마치 긴 꿈에서 깨어난 기분이다. 뇌리를 스친 생각은 길었지만 지나쳐 온 순간은 짧았다.

두께를 가늠할 수 없는 석벽 깊숙이 처박힌 몸 위로 부서진 돌가루가 떨어진다.

일격을 허용한 지 불과 수 초. 아직 시간은 있다.

턱.

나는 오한으로 인해 덜덜 떨리는 손으로 바닥을 짚으며 중얼거렸다.

“그만 울어라. 나 아직 안 죽었다.”

녀석을 향한 대답인 동시에 스스로에게 던지는 한 마디.

맞다. 나는 아직 죽지 않았고, 잠시 식어 버린 불씨라 할지라도 몇 번이고 다시 타오를 수 있다.

바로 지금처럼.

화아아악.

하단전으로부터 끌어올린 공력이 수백 개의 혈도를 뜨겁게 달구며 사지백해로 퍼져 나간다.

내상으로 흐트러진 내부를 임시 봉합하는 과정에서 불같은 통증이 엄습하고, 목구멍 사이로 무언가가 울컥 솟구쳤다.

쿨럭.

입술 사이로 검붉은 핏물이 흘러넘쳤지만, 신경 쓰지 않았다. 저건 죽은 피. 즉 사혈(死血)이니까.

그리고 내 몸 안을 좀먹고 공력의 흐름을 방해하던 그것은 땅에 닿기가 무섭게 새하얀 서리를 덧씌웠다.

파스슥.

음한지기. 그것도 지금껏 본 적 없는 극한의 음한지기다.

과거 소림혈사 당시, 암천의 무인들을 이끌고 소림사 경내를 급습했던 음양쌍괴(陰陽雙怪) 중 한 사람이었던 음괴(陰怪)도 이 정도는 아니었다.

“……그래, 그렇다 이거지.”

작게 뇌까린 나는 망설임 없이 몸을 일으켰다.

투두둑, 갑작스러운 움직임에 몸 곳곳에 붙어 있던 나뭇잎과 돌가루가 떨어지고, 아릿한 통증이 올라온다.

그러나 그와 반대로 신체 내부는 새롭게 퍼져 나간 온기로 가득했다. 한기로 인해 덜덜 떨리던 손도, 흐릿하던 시야도 밝아져 있었다.

서서히 가까워지는 두 인영을 알아볼 수 있을 만큼.

사박.

늪에서 사막, 사막에서 서리 낀 땅이 되어 버린 독혈지를 천천히 가로지르는 발걸음.

몇 걸음 뒤에서 득의양양한 표정을 짓고 있는 흑수권마가 있었지만, 내 시선은 오직 한 사람에 못 박혀 있었다.

‘염병할 늙은이.’

그리고 마치 자신이 만들어 낸 풍경화를 감상하듯, 느긋하게 걸음을 옮기는 노인을 응시하며 백염을 비스듬히 곧추세운 그 순간이었다.

“의외로군. 이 정도면 분명 움직이지 못할 것이라 생각했는데.”

노인이 불쑥 입을 열었다.

아니, 이제는 나 역시 그의 별호를 안다. 사실은 기억해 냈다는 표현이 더 정확할지도 모른다.

“그건 대설귀(大雪鬼), 당신 같은 늙은이나 그런 거고.”

“젊음은 좋은 것이지. 허나 어찌하여 모르느냐. 이런 상황에서는 더욱 고통스러워질 뿐이라는 것을.”

지금껏 그래 왔듯, 한 치의 흔들림도 없이 대답한 대설귀가 말을 이었다.

“이미 싸움은 끝났다. 지금이라도 순순히 투항한다면 목숨만은 살려 주지. 처음이자 마지막 제의다.”

“선배! 그게 무슨 소리요!”

당연하게도 내가 한 말이 아니다. 와락 얼굴을 일그러트린 흑수권마의 반발에 대설귀가 고개를 가로저었다.

“마후(魔后)께서 내게 직접 내리신 명이다. 만약 놈을 살려 보낸다면 장차 큰 화근이 되겠지만, 가급적이면 생포하라 하셨지. 그리고 이미 승기는 우리 쪽에 있다.”

“아무리 그렇다 해도……!”

“입 닥쳐라.”

“……!”

“네 마음을 모르는 바가 아니지만, 이건 천(天)의 일이다. 더 이상 반문했다가는 내가 용서치 않겠다.”

서릿발 같은 기세와 어조. 제아무리 반쯤 맛이 간 흑수권마라 할지라도 더 이상 반발하는 건 미친 짓이다.

“이런 개 같은…….”

이를 악문 놈의 잇새로 흘러나온 중얼거림을 가볍게 무시한 대설귀가 내게 손을 내밀었다.

“승패가 뻔한 싸움을 이어 가는 것은 멍청한 짓이지. 차라리 투항하여 후일을 도모해라. 하면 열화문도, 태원진가도 명맥을 보존시킬 수 있다.”

대설귀를 물끄러미 응시하던 내가 대답했다.

말이 아닌, 행동으로.

쉬잉!

허공에 울려 퍼지는 날카로운 파공성.

정확히 반보를 움직여 창격(槍格)을 피해 낸 대설귀가 담담하게 입을 열었다.

“분명히 말했을 텐데. 처음이자 마지막 제의라고.”

“그래서?”

“제법 영민한 줄 알았더니, 끝끝내 어리석은 길을 택하는군. 이미 승기가 기울었음을 느끼지 못했느냐?”

“승기라.”

작게 중얼거린 내가 말을 이었다.

“솔직히 나도 살고 싶긴 한데, 그거 조금 기울었다고 항복하거나 도망칠 만한 놈은 아니거든. 누구와는 달리.”

순간 멈칫한 대설귀가 무언가를 깨달은 듯, 작게 고개를 끄덕였다.

“날 아는군.”

“백설기인지, 대설귀인지 하는 별호 정도는 들어봤지.”

“너 같은 어린아이가 쉽게 들을 수 있는 별호는 아닐 테니…… 화왕(火王) 적천강. 네 스승이 말해 주더냐?”

“그럼 시발 천마가 말해 줬겠니?”

어깨를 으쓱한 내가 말을 이었다.

“만약 음한지기에 쌍륜을 쓰는 호로새끼를 만나면, 그놈이 바로 대설귀거나 그 후인일 거라고 말씀하셨지. 당신의 손으로 직접 쳐 죽이고 싶었는데, 종남파 전대 장문인을 죽인 뒤 흔적도 없이 사라져서 안타깝다고도 하셨고.”

“그 부분은 나 역시 안타깝게 생각한다. 정마대전 당시 노부가 네 스승을 만났더라면, 화왕을 죽이고 천하에 이름을 떨칠 수 있었을 테니.”

“기껏해야 대설귀 대신 빙신(氷神)이었겠지. 이 빙신 새끼야.”

“……!”

처음으로 반응이 왔다. 미약하지만 확실하게 미간을 찌푸리는 대설귀의 모습에 나는 피식 웃었다.

“그래도 자존심은 있는 모양이네. 아니, 그때 도망친 걸 보면 아예 없는 것 같기도 하고.”

“후일을 도모했을 뿐이다. 노부는 중과부적(衆寡不敵)의 상황에서 목숨을 걸 만큼 멍청하지 않으니까.”

사실, 내가 들은 정보를 토대로 생각해도 당시 대설귀의 판단은 냉정하면서도 적절했다.

종남파의 전대 장문인을 죽여 지휘 통계를 엉망으로 만들고, 그 틈에 대설산을 빠져나가 홀연히 자취를 감추었으니까.

하지만…….

“뭐 어쩌라고.”

“뭐라?”

“당신은 결국 겁이 나서 도망친 것뿐이야. 죽는 게 싫었으니까. 죽는 게 무서웠으니까. 그래서 오랫동안 모습을 드러내지 않았던 거고.”

“……네놈.”

“뭐라 할 건 아니지. 나도 죽는 게 싫으니까. 하지만 그 정도로 나이를 처먹었으면, 인정하기 싫은 부분에서도 가끔은 솔직해져야지. 안 그래?”

대설귀에 미간에 깊은 골이 아로새겨진다. 동시에 강대한 음한지기가 일어나 주위를 짓눌렀다.

“잘 들었다. 마지막 유언, 훗날 네 스승을 만나면 전해 주마.”

유언이라.

‘어쩌면 그럴지도 모르지.’

나는 깊이 심호흡했다. 상대는 흔하게 찾아볼 수 있는 어중이떠중이가 아니다.

더군다나 내상을 입은 상황에서 초절정 고수 둘을 상대하는 것은 자살 행위나 다름없다.

죽음? 당연히 두렵다.

나는 헌터가 된 이래 늘 죽음을 두려워했고, 무림에 와서도 마찬가지였다.

하지만…… 마음속에 죽음이라는 단어를 한 걸음 받아들인 지금은 평소와 달랐다.

‘뭐든 할 수 있다. 무엇이든.’

살아남기 위해서가 아니라, 죽이기 위한 싸움.

그렇기에, 지금 이 순간 나는 목숨을 아끼지 않고 달려들 수 있었다.

쐐애애액!
```

## Final English reading copy

```markdown
# Chapter 681

For an instant, a thought crossed my mind.

*What if the Black Hand Fist Demon hadn’t been there? What if I had avoided the Finger Qi?*

*What if the pain hadn’t risen from the shoulder pierced by the Finger Qi at the exact moment our palms met?*

*What if I had known that my opponent’s martial arts were based on Yin-Cold Qi?*

*If—if things had gone that way…*

*Who would be standing here by now?*

But I was given no time to find the answer to those questions.

KRAK!

The frozen flames died away, and the Yin-Cold Qi that had swallowed even the flames swelled as though it might burst.

Beyond the unprecedented internal energy that shook the surrounding space, someone’s hand, engulfed in pure-white light, pressed against my chest.

Tap.

At that moment, only one thought filled my mind.

*Cold.*

KRAAANG!

A storm of cold energy swept in every direction.

What struck me at its center was a fierce wind battering my entire body, the scenery flashing past at incredible speed, and an immense force of recoil transmitted through my back.

KRRRUNCH!

Trees. Rocks. Grass.

And even some unknown creatures unfortunate enough to be caught up in it.

It did not matter whether they had been alive or dead.

Everything my body collided with as it was flung backward like a misfired shell was bent, shattered, and blown apart.

However, the fact that a thick stone wall stood across the middle of that path—one over which I had not possessed the slightest control—was both unfortunate and fortunate.

KWAANG! RRRUMBLE!

Even through the haze, I could feel the excruciating pain.

The scenery that had whipped past my vision every moment finally stopped. But so had I, after being flung several dozen jang[^1] and embedded deep inside the stone wall.

*Goddamn it.*

The voice I squeezed out with all my strength never made it past my lips.

The world was red and blurry, while a constant ringing filled my ears.

BEEP! BEEP! BEEP!

Even for tinnitus, that was a little unusual.

“…Fuck.”

I raised my head with a hollow mutter.

More than a dozen holographic windows floated in the air, accompanied not by the clear bell tones I was accustomed to, but by warning sounds signaling danger.

*I really got the shit kicked out of me.*

A bitter laugh escaped me.

Pain kept surging from every injury.

My hands and feet trembled from the Yin-Cold Qi that had invaded my body, making a mockery of my realm of Unaffected by Cold and Heat.

*I have to get up. I have to fight again…*

But unlike my wishes, my body—as if all its screws had come loose—refused to listen.

I was cold.

And tired.

If I closed my eyes right now, I felt as though I could sleep soundly for the first time in a long while.

Yes. If I slept until my back hurt, with no dreams and no one to wake me, everything would have gotten better.

By the time I woke up, the pain assaulting my entire body would be gone, and this goddamn body that refused to listen would be fine again. Then, as I wriggled beneath a warm microfiber blanket and looked at my smartphone, I would hear Mom’s voice through the crack in the door.

—Jin Taekyung, Jin Hayeon. I’ve set the table, so come out already.

Then I would stagger to the kitchen and prepare the meal, setting out spoons and side dishes on the empty table despite what I had just heard her say.

All while breathing in the savory scent of soybean-paste stew wafting from beyond Mom’s shoulder as she stood with her back to me.

*Ah. This is nice.*

Just thinking about it brought peace to my heart.

The corners of my mouth rose without my realizing it, while my eyelids kept sinking lower.

Sss…

Something rough and damp brushed across my face.

When I slowly opened my eyes, the first things I saw were sharp teeth and clear blue-white eyes.

—Whine.

At the sight of the White Tiger whining like a puppy the moment our eyes met, a quiet laugh escaped me.

“…Was it you?”

—Whine. Whiiine.

Although I could not understand him, I could feel it clearly enough—the meaning contained in those cries, and what he wanted to tell me.

“Phew.”

Pain came with my breath.

It felt as though I had awakened from a long dream. The thoughts that had flashed through my mind had been long, but the moments I had passed through had been brief.

Broken stone dust rained down over my body, buried deep inside the stone wall whose thickness I could not even estimate.

Only a few seconds had passed since I took the blow.

There was still time.

Thud.

With a hand trembling from the cold, I pressed it against the ground and muttered,

“Stop crying. I’m not dead yet.”

It was an answer for him, but it was also something I said to myself.

That was right. I was not dead yet, and even if my flame had briefly gone cold, it could flare up again and again.

Just as it was doing now.

Fwoooosh.

The internal energy drawn up from my lower dantian heated hundreds of acupoints before spreading throughout my limbs and bones.

As I temporarily sealed my insides, thrown into disarray by my internal injuries, a searing pain swept over me, and something surged up in my throat.

Cough!

Dark red blood spilled from between my lips, but I paid it no attention.

That was dead blood.

In other words, blood that had already been rendered useless.

And the substance that had been gnawing away at my body and interfering with the flow of my internal energy was covered in pure-white frost the instant it touched the ground.

Fsssh.

Yin-Cold Qi.

And not merely Yin-Cold Qi, but an extreme form of it unlike anything I had ever seen.

During the Shaolin Bloodshed, the Yin Freak—one of the Yin-Yang Twin Freaks who had led Dark Heaven’s martial artists in a surprise attack on Shaolin Temple—had not possessed anything like this.

“…Yeah. So that’s how it is.”

After muttering under my breath, I rose without hesitation.

Tududuk.

At my sudden movement, leaves and stone dust that had clung to various parts of my body fell away, and a dull pain rose through me.

But in contrast, a new warmth filled my insides.

The hand that had been trembling from the cold and my blurry vision had both improved enough for me to recognize the two figures slowly drawing near.

Step.

Footsteps slowly crossed the Poisonblood Grounds, which had changed from a swamp into a desert, and from a desert into frost-covered land.

The Black Hand Fist Demon followed several paces behind, wearing a triumphant expression, but my gaze was fixed on only one person.

*That damn old man.*

And just as I held White Flame at a slant and stared at the old man walking leisurely as if admiring a landscape painting he had created himself, he suddenly spoke.

“Unexpected. I was certain that would leave you unable to move.”

The old man had spoken without warning.

No, I knew his sobriquet now, too. Though perhaps it would be more accurate to say I had remembered it.

“That might be true for old men like you, Great Snow Fiend.”

“Youth is a fine thing. But why do you not understand? In a situation like this, it will only make things more painful.”

As he had until now, the Great Snow Fiend answered without the slightest wavering and continued.

“The fight is already over. If you surrender obediently now, I will spare your life. This is the first and last offer.”

“Senior! What are you talking about?”

Naturally, that was not me.

At the Black Hand Fist Demon’s protest, his face twisting violently, the Great Snow Fiend shook his head.

“The Demon Empress gave me that order herself. If I let the bastard live, he will become a great source of trouble in the future, but she told me to capture him alive if possible. And the upper hand is already ours.”

“Even so…”

“Shut your mouth.”

“…”

“I know how you feel, but this is Heaven’s business. If you question me again, I will not forgive you.”

His aura and tone were as cold as a blade of frost.

No matter how half-mad the Black Hand Fist Demon was, continuing to resist would be insanity.

“This fucking…”

The Great Snow Fiend casually ignored the mutter that slipped between the Black Hand Fist Demon’s clenched teeth and held out a hand toward me.

“It is foolish to continue a fight whose outcome is obvious. Surrender instead and live to fight another day. If you do, the Fire Gate Clan and the Jin Family of Taiyuan will be allowed to preserve their lineages.”

I stared at the Great Snow Fiend and answered.

Not with words, but with action.

Whoosh!

A sharp sound of air splitting rang through the air.

The Great Snow Fiend moved exactly half a step and avoided my spear strike before speaking calmly.

“I believe I made myself clear. This is the first and last offer.”

“So?”

“I thought you were fairly clever, but you have chosen the foolish path in the end. Can you not feel that the upper hand has already shifted?”

“The upper hand.”

I muttered the words and continued.

“Honestly, I do want to live. But I’m not the kind of bastard who surrenders or runs away just because things have tilted a little. Unlike some people.”

The Great Snow Fiend paused for a moment, then gave a small nod as though he had realized something.

“You know me.”

“I’ve heard of a sobriquet or two. White Rice Cake, Great Snow Fiend, something like that.”[^2]

“A sobriquet like mine is not something a child like you could easily have heard… Fire King Jeok Cheongang. Did your master tell you?”

“Then do you think the fucking Heavenly Demon told me?”

I shrugged and continued.

“He told me that if I ever met some bastard using twin wheels and Yin-Cold Qi, that bastard would either be the Great Snow Fiend or his successor. He also said it was unfortunate that he never got to kill you with his own hands, because you killed the former Sect Leader of the Zhongnan Sect and disappeared without a trace.”

“I feel the same regret. If this old man had met your master during the Great Faction War, I could have killed the Fire King and made my name resound throughout the world.”

“At best, you’d have been the Ice God instead of the Great Snow Fiend, you fucking idiot.[^3]”

[^3]: “Ice God” (*bingsin*) puns on *byeongsin*, a harsh Korean insult roughly meaning “fucking idiot.”

“…”

For the first time, he reacted.

It was faint, but the Great Snow Fiend’s brow definitely furrowed.

A quiet laugh escaped me.

“So you do have some pride after all. Then again, seeing as you ran away back then, maybe you don’t have any at all.”

“I merely lived to fight another day. This old man is not foolish enough to risk his life when outnumbered.”

In fact, based on what I had heard, the Great Snow Fiend’s judgment at the time had been cold but appropriate.

He had killed the former Sect Leader of the Zhongnan Sect, thrown the chain of command into chaos, then used the confusion to escape from Great Snow Mountain and vanish without a trace.

But…

“So what?”

“What?”

“In the end, you just ran away because you were scared. Because you didn’t want to die. Because you were afraid of death. That’s why you stayed hidden for so long.”

“You bastard.”

“It’s not like I’m criticizing you. I don’t want to die either. But once you’ve lived that many years, you should be honest every now and then—even about the things you don’t want to admit. Don’t you think?”

Deep furrows appeared on the Great Snow Fiend’s brow.

At the same time, powerful Yin-Cold Qi rose and pressed down on the surroundings.

“I heard you well. If I meet your master in the future, I shall deliver your last words to him.”

*Last words.*

*Maybe that’s how it will be.*

I took a deep breath.

My opponent was no ordinary nobody.

Moreover, facing two Supreme Peak masters while suffering from internal injuries was little different from committing suicide.

Death?

Naturally, I was afraid.

Ever since becoming a Hunter, I had always feared death. The same was true even after coming to the Murim.

But…

Now that I had taken one step toward accepting the word *death* in my heart, I was different from before.

*I can do anything. Anything.*

This was not a fight to survive.

It was a fight to kill.

And because of that, at this moment, I could throw myself forward without sparing my life.

SHWAAAAAK!

[^1]: A *jang* is a traditional Korean unit of length, roughly three meters.

[^2]: The insult riffs on *baekseolgi*, a white Korean steamed rice cake, and the Great Snow Fiend’s sobriquet.
```
