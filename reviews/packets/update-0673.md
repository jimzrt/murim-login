<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0673.txt",
      "sha256": "b4f1667ee755a5e117a5a681830904dc9186f8323d40b87155c948d352aacf73",
      "bytes": 15714
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "bd4207877828ca42827f4ec1c4e25974d159b22034808bff73955a878bdfbcac",
      "bytes": 2192
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "20240b3c73f403375624ae660702bf64c519e1d89049394ddc015fc50f02c400",
      "bytes": 202564
    },
    {
      "path": "characters/Baekhwi.md",
      "sha256": "02d76c4933c30291d0dd76a7af01209ddf518087d5af9cb418c27c5869ac8aa2",
      "bytes": 493
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "983cf972336e9b33ff8a1c7e32089969568ba2db5e4a271e383259691bb3db25",
      "bytes": 1006
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "2bedf864e7d3ee7202739bc786c88f88f57d206e9046e8d8d0c406a5286d7afe",
      "bytes": 830
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "d6637479a04423ef461266c7ec1d3f8e3171c85e6df468fda99b3dd0eae06640",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "77e19953aeea535baf8fd57f95b1af2ca88905a6a37903325bd432b7fd7e5d8e",
      "bytes": 1858
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "0cbc777a6adf879024dcc4159ad7c4db9115c1d2d3b43fb5387a009430738d4c",
      "bytes": 622
    },
    {
      "path": "characters/Yayul Cheok.md",
      "sha256": "233421123847ea20471f4e9b8b3f0aa9f16cd0555f67fc5401f72c61f8ed1ca6",
      "bytes": 902
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4045b33709c85492f6e5a040817a29f9f908e64bbead101e589c38cbc6fe4ca0",
      "bytes": 208612
    }
  ],
  "estimated_tokens": 12604
}
-->

# Durable State Update — Chapter 673

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 673. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 673. Profile updates may replace only one
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
  "chapter": 673,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 673,
    "continuity_sources": [673],
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
    "Jin has chosen to follow Yohi's Tracking Scent and is moving southeast after retracing the route toward the Nanman Beast Palace.",
    "Jin has escaped the underground prison, but the Logout function remains blocked and Nanman's forces are searching for him.",
    "Muyaho has carried Jin for roughly three shichen through Nanman's rugged terrain and continues traveling with him despite exhaustion.",
    "Taishan stayed behind with the others after Jin ordered him to flee through the reconnaissance chieftains and the Water Dragon Stronghold's swift ships; Taishan promised to wait five nights for Jin's return.",
    "Jin has credible information about the Nanman Beast Palace's internal situation from interrogating fifty or so Nanman warriors.",
    "Jin warned that harming the surviving Miao warriors would bring delayed retaliation and released the interrogated warriors to spread fear.",
    "Jin has deliberately lit a forest beacon near the Outer Palace to draw Baeksang's net over heaven and earth toward himself.",
    "The surviving Miao warriors remain under Jin's protection.",
    "The Beast Miao King's fate and the fate of the remaining rescuers remain unresolved."
  ],
  "continuity_sources": [
    672
  ],
  "open_questions": [
    "What will Yohi's Tracking Scent lead Jin to, and where are Yohi and Heugung?",
    "Did the Beast Miao King survive Baeksang's Sword Force?",
    "Will Wonhu and the remaining Miao warriors survive Baeksang's forces?",
    "Will Taishan and the others escape Nanman through the Water Dragon Stronghold within five nights?",
    "Can Jin survive after drawing Baeksang's pursuit toward himself?"
  ],
  "safe_through": 672,
  "temporary_decisions": [
    "Use Great Chieftain for 대족장 and Palace Lord for 궁주.",
    "Use Sword Force for 검강 and half a shichen for 반 시진.",
    "Use Outer Palace for 외궁 and Yohi's Tracking Scent for 요희의 추종향.",
    "Use Thousand-Li Tracking Scent for 천리추종향 and Ten-Thousand-Li Tracking Scent for 만리추종향.",
    "Preserve Jin's sardonic, profane, and intimidating voice in threats and interrogation."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 남만야수궁  | **Nanman Beast Palace**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 상태               | **Status**                     |
| 명성               | **Fame**                       |
| 정마대전   | **Great Faction War**         |
| 백휘 | **Baekhwi** | Baeksang's deceased only child. |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 야율척 | **Yayul Cheok** | Beast Miao King and lord of the Nanman Beast Palace. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 소조귀 | **Little Tide Demon** | Wang Pil's sobriquet. |
| 무한 | **Wuhan** | Capital of Hubei Province near Dongting Lake. |
| 향아 | **Hyang** | Young female medical apprentice at the clinic. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 묘족 | **Miao people** | Ethnic group the Escort Bureau expects to encounter near Yunnan. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 마비 | **Paralyzed** | Status abnormality inflicted by Kraken's Ink. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 백족 | **Bai people** | Ethnic group encountered in Yeongin. |
| 애뇌산 | **Ailao Mountain** | Mountain crossed by the party on the route to the Nanman Beast Palace. |
| 요족 | **Yao people** | One of Nanman's four great tribes, led by Yohi. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 천년지주 | **Thousand-Year Spider** | Monster appearing at the end of the chapter. |
| 외궁 | **Outer Palace** | The outer compound of the Nanman Beast Palace. |
| 대회의 | **Tribal Grand Council** | Nanman's council of great chieftains. |
| 서요부 | **Western Yao Estate** | Yohi's residence in the western part of the Inner Palace. |
| 대설산 | **Great Snow Mountain** | Mountain where Baeksang's wartime account reaches its next episode. |
| 대족장 | **Great Chieftain** | Title used for the senior Nanman leader who supposedly ordered the inspection. |
| 소궁주 | **Young Palace Lord** | Title used for Yayul Mok as heir of the Nanman Beast Palace. |

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
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 백상 | 야수묘왕 | Nanman great chieftain to the Nanman Beast Palace Lord | Palace Lord | restrained and apologetic | Apologizes for causing the disturbance after the Beast Miao King stops the fight. |
| 백상 | 백휘 | father_to_deceased_child | Hwi | emotionally charged and possessive | Baeksang directly invokes his deceased child's name while confronting Jin. |

## Listed compact profiles

### Baekhwi.md

# Baekhwi (백휘)

- **Safe through:** Chapter 662
- **Aliases:** None
- **Role:** Baekhwi was Baeksang's only child, would have become the Beast Miao King's son-in-law, and was killed without leaving a corpse during the Great Snow Mountain battle.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Baeksang's only child; would have been the Beast Miao King's son-in-law if he had lived.

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 672
- **Aliases:** None
- **Role:** Baeksang is the middle-aged great chieftain of the Bai people, one of Nanman's four most powerful great tribes, and one of only two Supreme Peak masters in Nanman.
- **Personality:** Cold, rigid, meticulous, politically resolute, and strategically manipulative, with enduring grief over Hwi's death and a guarded but still powerful bond with his sworn elder brother that now leaves him visibly conflicted.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of his deceased only child Baekhwi, whom the Great Snow Fiend killed during the Great Faction War; despite his bond with Yayul Cheok, he has chosen to oppose the Beast Miao King's escape and has surrounded Wonhu's remaining force with Bai warriors.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 671
- **Aliases:** None
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, the great chieftain of the Miao people, a master among the Ten Kings, and one of only two Supreme Peak masters in Nanman.
- **Personality:** The Beast Miao King is fierce and vigilant, yet pragmatic and willing to sacrifice his position to protect Nanman's survival and the greater cause over personal revenge.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace, is Baeksang's sworn elder brother and childhood companion, and is Yayul Mok's father while jointly risking their positions to rescue Jin Taekyung and prevent war with the Central Plains.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 671
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 671
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, and an escaped prisoner still facing public execution at noon in two days.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 671
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Yayul Cheok.md

# Yayul Cheok (야율척)

- **Safe through:** Chapter 643
- **Aliases:** Beast Miao King
- **Role:** Yayul Cheok is the over-eighty Beast Miao King, lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, and great chieftain of the Miao people.
- **Personality:** Boisterous, warmhearted, forthright, playful, and politically conscious of the tribal coalition he leads.
- **Voice:** Rough, loud, convivial, and teasing, becoming authoritative when discussing Nanman's laws or political decisions.
- **Relationships:** Jeok Cheongang is an old acquaintance whom he respects; Baeksang is his sworn younger brother and childhood companion, and they fought together during the Great Faction War; Yayul Mok serves as his Young Palace Lord; Jin Taekyung is Jeok's Disciple whom he welcomes into the Nanman Beast Palace.

## Korean source

```text
＃673화



이는 정마대전 이후, 처음으로 찾아온 격동의 시기였다.

천하의 중심이라 불리는 중원에도, 그리고 중원으로부터 수천 리나 떨어진 머나먼 남만에도.

“헉, 허억. 다들 그 소식 들었소?”

“숨 좀 고르고 말하게. 이번에는 무슨 일인가?”

하루가 다르게 새롭게 퍼져 나가는 소문들에, 남만인들은 더 이상 처음만큼 놀라지 않았다.

아니, 정확히는 여기에서 더 놀랄 것도 없다고 생각했다.

그도 그럴 것이, 지난 한 달 남짓한 시간 동안 있었던 일들은 정마대전이 종결된 이후 남만에서 일어난 모든 사건을 합한 것보다 거대한 충격의 연속이었으니까.

한족에 의한 묘족 마을 몰살.

지난 수십 년간 잠잠했던 애뇌산에서 갑작스럽게 나타난 천년지주의 습격.

남만야수궁 역사상 처음으로 내궁(內宮)에 입성한 것으로도 모자라, 서른두 명의 부족장만이 자리할 수 있는 대회의에 참석한 어느 젊은 한족에 관한 이야기까지.

연달아 벌어진 새로운 사건들이 끝이 여기까지였다면 차라리 괜찮았을 것이다.

그러나 불과 사흘 전 요서부에서 백여 명에 달하는 요족 전사들이 참혹하게 살해당하고, 막대한 상징성을 지닌 두 명의 대족장이 실종되면서 상황은 급류를 타기 시작했다.



‘흉수! 요서부의 흉수가 밝혀졌소! 바로 그 젊은 한족이 흉수였소! 진태경 말이오!’

‘잠깐. 잠깐만 기다려 보게. 전날 애뇌산에서 진태경이 전사들을 구했던 것을 벌써 잊었나? 아직 확실히 밝혀진 것도 없는 상황에 섣불리 판단하기에는…….’

‘섣부르긴 무슨. 그 한족 놈들이 오고 나서부터 안 좋은 일들만 생겼네. 더 두고 볼 것도 없어!’

‘옳소!’



분노를 이길 수 있는 것은 이성뿐이지만, 이미 이성이 마비된 많은 남만인의 외침에 몇몇 이들의 목소리는 힘없이 파묻혔다.



‘한족들을 저자로 끌어내어 오체분시하라!’

‘백상 대족장님! 반드시 놈들을 처벌해 주십시오!’



매해 대회의가 열릴 때마다 거리에 깔려 있던 풍악과 웃음소리는 더 이상 찾아볼 수 없었다.

분노에 가득 찬 외침이 사방에서 울려 퍼졌고, 그들의 외침에는 언제나 두 사람의 이름이 포함되어 있었다.

진태경. 그리고 백상.

출신 성분과 나이, 이름만큼이나 두 사람의 위상은 달랐다.

남만인으로서는 당연한 일이었다.

한 사람은 머나먼 중원에서 온 이방인. 그것도 결코 용서받지 못할 참극을 저지른 죄인인 데 반하여, 다른 한 사람은 이 땅에서 묘족 다음으로 강성한 백족을 이끄는 대족장이었으니.

남만인들은 천하에 명성을 떨칠 만한 무위와 소탈한 인품을 지닌 자신들의 궁주를 여전히 존경하고 사랑했지만, 서요부의 일로 신뢰에 금이 가는 것은 어쩔 수 없었다.

근래 일어난 모든 불행한 사건의 원흉인 한족들을 내궁으로 들인 것은 다름 아닌 궁주, 야율척이었으니까.

그러나 백상 대족장에게 환호를 보내던 이들조차 날이 밝기 무섭게 흘러나온 새로운 소식을 접하자 당황할 수밖에 없었다.

“뭐, 뭐라고?”

“내가 지금 뭘 잘못 들은 건가?”

흔들리는 동공과 당혹감에 물든 얼굴.

소식을 접한 모두는 같은 눈빛, 같은 표정으로 이 믿기지 않는 이야기를 마음속으로 계속 중얼댈 수밖에 없었다.

‘궁주께서…… 간밤에 백상 대족장을 해하려 한 뒤 실패하자 도주하셨다고?’

처음에는 모두 터무니없는 헛소문이라고 생각했다. 그들이 아는 궁주는, 묘족의 대족장 야율척은 그런 사람이 아니었으니까.

그는 훌륭한 궁주이기 이전에 좋은 사람이었고, 누구보다 남만을 아끼는 이 땅의 토착민이었으니까.

하지만 그런 생각이 무색할 만큼, 곧이어 들려온 소식은 남만인들이 가진 믿음과 의문을 구렁텅이로 밀어 넣기에 충분했다.

“백상 대족장이 임시 궁주로 취임한다니. 그게 무슨 소린가!”

“나, 나도 잘 모르겠네. 허나 내궁에서 방(訪)을 붙였어. 우리가 들은 앞서 들은 소식 그대로 적혀 있더군.”

“이 무슨 말도 안 되는! 그게 가당키나 한가!”

“아직 끝이 아니야. 심지어 궁주께서는 소궁주와 휘하의 정예 전사 수십을 동원하여 뇌옥을 급습. 흉수 진태경을 비롯한 한족들을 풀어 줬다더군.”

“……!”

“나도 믿기 힘들지만…… 정황이 워낙 뚜렷해. 궁주께서 오래전부터 한족들에게 우호적이었던 것은 부정할 수 없는 사실이고, 진태경과 소궁주를 비롯한 한족들의 행방도 묘연하네. 간밤에 소집된 대회의에서는 이를 남만 전체에 반하는 배반으로 규정하고 총동원령을 내렸다더군.”

“뭣이. 총동원령?”

“그래, 임시 궁주 건과 함께 결정되었다고 들었네. 남만은 어지럽힌 역도들을 쫓아 처단하겠다는 거겠지. 당연하게도 최우선 목표는 한족 진태경과 궁주. 아니, 전(前) 궁주일 테고.”

“전 궁주라니. 자네 지금 무슨 소리를 하는 겐가!”

“모르겠네. 아직까지도 혼란스러워. 하지만 우리 같은 일개 부족민들이 어찌 더 자세한 내막을 알 수 있겠나. 대회의의 결정을 따를 뿐이지.”

내궁의 직인이 선명히 찍혀 있는 방의 내용은 삽시간에 퍼져 나갔고, 남만인들의 반응은 세 갈래로 나뉘었다.

야수묘왕의 배신을 믿는 자. 결단코 믿지 않는 자.

또한 진실을 찾으려는 의심이나 노력 없이, 새롭게 주어진 현실에 순응하는 자.

그리고 이 극심한 혼란의 소용돌이 속에서, 각기 크고 작은 부상을 입은 오십여 명의 전사들이 서문(西門)을 통해 외궁으로 귀환했다.

사시나무처럼 몸을 떠는 그들의 얼굴에는 지울 수 없는 공포가 깃들어 있었고, 흔들리는 눈동자에는 십 리 밖에서도 보이던 거대한 화염의 잔재가 선명히 남아 있었다.

“괴, 괴물…….”

누군가의 입술 사이로 흘러나온 목소리는, 머리 위로 쏟아지는 강렬한 햇빛이 무색할 만큼 얼어붙어 있었다.

정오 무렵이었다.



* * *



백상은 커다란 면경(面鏡)에 비친 자신의 모습을 바라보았다.

칠순을 넘긴 나이가 무색할 만큼 젊고 수려한 외모와 균형 잡힌 체구. 거기에 새하얀 호리(狐狸)의 털로 만들어진 의복까지.

누가 본다면 마치 일국(一國)의 지배자와 같은 위엄과 자태라며 감탄할 만한 모습이었으나, 백상의 시선은 줄곧 차갑게 굳은 자신의 얼굴에 못 박혀 있었다.

‘이런 얼굴을 하고 있었던가. 그토록 오랜 시간 동안.’

지난 수십여 년의 세월을 되짚어 보아도 기억나지 않는다. 자신이 진심으로 웃었던 것이 언제인지.

이제는 먼지로 뒤덮인 옛 기억을 다시 한번 꺼내 들여다볼 뿐이다.

‘그래, 그때가 마지막이었지.’

문득 떠오른 어느 날의 기억이 서늘하던 눈동자를 녹인다.

치열했던 전투에서의 승리 후, 그들에게 주어진 며칠 간의 달콤한 휴식.

아버지를 따라 마교를 물리치겠다며 따라나섰던 당찬 소년은 어느덧 헌앙한 청년이 되어 있었고, 어릴 적부터 활발했던 탓에 언제나 상처투성이였던 소녀는 아름다운 여인으로 자라났다.

청년의 이름은 휘(輝). 여인의 이름은 향(香).

두 사람은 이름만큼이나 빛나고 향기로웠다. 피와 죽음이 난무하는 전장의 틈바구니에서 피어오른 한 쌍의 꽃이었고, 어릴 적부터 함께 자란 서로를 견원지간(犬猿之間)이라 칭하면서도 종종 사람들의 눈을 피해 함께 걸었다.

아마 두 사람은 몰랐을 것이다.

승리와 술에 취한 사람들 사이를 조심스레 빠져나와, 희미한 달빛이 쏟아지는 언덕을 함께 거닐던 그때. 자신들을 지켜보는 눈길이 있었음을.



‘……너 또 왔냐?’

‘……그러는 형님은 왜 또 왔소?’

‘몰라서 물어? 휘, 저 늑대 같은 놈이 내 연약하고 아리따운 향아를 건드릴까 싶어서 감시하러 왔다.’

‘이거 진짜 궁금해서 묻는 건데, 진심이오?’

‘당연히 진심이지.’

‘그럼 사흘 전 벌어진 전투에서 소조귀(小鳥鬼)가 죽은 건 알고 있겠구려.’

‘소조귀? 음탕함이 무공이라면 천마 귀싸대기도 때린다는 그 새끼?’

‘맞소.’

‘딸 가진 애비로서 언제 한번 손 봐주려고 했는데 잘됐군. 그런데 갑자기 왜 그런 얘길 해?’

‘그놈. 향아가 죽였소.’

‘…….’

‘앞서 휘아가 소조귀를 상대하다가 검상을 입었는데, 갑자기 나타난 향아가 어디서 주웠는지 모를 쌍부(雙斧)로 소조귀의 머리통을 찍었다더군.’

‘…….’

‘그러고도 분이 안 풀렸는지 이미 죽은 놈 불알을 터트리고, 온갖 욕설을 퍼부으면서 시신을 난도질해 놨다고 했소. 휘아의 표현을 빌리자면 황궁 숙수가 신들린 솜씨로 고기를 다지는 것 같았다던데.’

‘……거짓말이야. 내 향아가 그럴 리 없어.’

‘휘아를 제외해도 본 사람만 다섯 명이오. 그중 세 사람은 그날의 충격 때문에 아직 말도 못 하는 상태고.’

‘잘됐군. 그럼 계속 입 닥치고 있으라고 해. 아니면 내가 직접 손을 써서 입을 막는 수가 있…… 오. 안 돼.’

‘무슨 마두도 아니고…… 헉.’



그날, 저 멀리 어둠 속에 웅크리고 있던 의형제는 의도치 않게 목격하고 말았다.

자신들이 목숨처럼 끔찍이 아끼는 두 아이가 천천히 서로를 향해 고개를 기울이는 그 광경을.



‘고개 돌려. 빨리!’

‘형님부터 목소리 낮추시오! 그리고 이미 돌렸소!’

‘오, 제발. 세상에. 내가 지금 뭘 본 거지?’

‘뭘 보긴. 눈은 남만에 두고 왔소? 입 맞추…… 읍. 읍읍.’

‘백상 너 이 음흉한 새끼. 늑대 같은 아들놈을 시켜서 감히 이런 흉계를 꾸며? 그리도 궁주가 되고 싶더냐?’

‘으읍. 푸하! 내가 궁주라니, 그게 무슨 미친 소리요? 형님이나 내가 죽고 난 후라면 모를까.’

‘오호라, 그래. 네가 못 이룬 꿈, 아들을 통해 이루겠다 이거냐? 이대로면 향아가 다음 대 궁주가 될 수 있으니까 냉큼 낚아채서 집안일만 시키겠다. 이거 아냐?’

‘돌겠네, 진짜.’

‘마지막 기회다. 어서 순순히 인정해.’

‘아니오. 아니라고!’

‘정말 아니야? 하늘에 걸고?’

‘하늘에 걸고!’

‘좋아, 믿어 주지. 그럼 올해 안에 혼례 치를 준비해.’

‘도대체 아니라고 몇 번을 말해야…… 뭐? 지금 뭐라고 했소?’

‘뭐는 반말이고. 서로 좋아 죽는 어린 것들 혼례 치를 준비나 하라고.’

‘…….’

‘아, 뭘 얼빠진 얼굴로 쳐다보고만 있어? 네 녀석도 다 짐작하고 있었으면서. 혹시 싫으냐?’

‘시, 싫을 리가 있겠소. 형님 말대로 이미 짐작하고 있었던 부분인데. 그런데 이게 뭐랄까. 허어.’

‘그럼 됐어. 긴말 필요 없다. 겨울 전에 서쪽 전선이 안정되면 혼례를 치른 뒤 남만으로 돌려보내자고. 그리고 생각만으로도 기분이 이상해지긴 하지만…… 만약 아이라도 들어서면 저 녀석들도 고집을 꺾고 순순히 돌아가겠지.’

‘아이라. 허, 허허. 세월이 벌써 그렇게 됐소?’

‘나보다도 어린놈이 늙은이 행세는. 됐고. 한 가지만 약속해라.’

‘약속이라면 무슨?’

‘향아 저 아이, 내게는 누구보다 사랑스럽고 불쌍한 아이다. 못난 애비 때문에 오라비를 둘이나 잃고 많이 힘들어했어.’

‘형님…….’

‘빌어먹을. 그러니까 내가 하고 싶은 말은……. 제기랄.’

‘그만하시오. 무슨 말을 하고 싶은지 다 알고 있으니까. 귀한 아이이니, 귀하게 대해 달라는 것 아니오?’

‘…….’

‘걱정할 것 없소. 휘아는 틀림없이 그럴 테니. 단지 아녀자가 아니라 동반자로, 때로는 벗으로 함께 늙어 갈 거요.’

‘휘아, 그 녀석이라면 믿을 수 있긴 하지.’

‘만약 형님이 휘아를 믿을 수 없거들랑, 향아를 믿으면 되오.’

‘뭐?’

‘향아 성미를 좀 보시오. 휘아가 조금이라도 섭섭하게 했다간 소조귀 꼴이 날 게 뻔하……!’

‘백상, 이 자식이 감히 내 향아를 뭘로 보고!’



마지막 외침은 명백한 실수였다.

수줍게 첫 입맞춤을 나누던 남녀는 황급히 서로에게서 떨어졌고, 두 의형제는 온 힘을 다해 도망쳐야 했으니까.

그리고 한적한 어느 개울가에 도착해서 서로를 향해 한마디를 쏘아붙이려다가…….

‘그래, 웃었지. 세상이 떠나가도록.’

무엇 때문에 그리 크게 웃었는지, 이제는 기억나지 않는다. 다만 혼비백산한 서로의 얼굴이 우스웠기 때문만은 아니었을 것이다.

아마 어릴 적부터 함께 자란 두 아이가 맺어진다는 것이, 마찬가지로 평생 함께한 의형제가 마침내 한 집안으로 이어진다는 사실이 기뻐서가 아니었을까.

‘향아, 그 아이가 그리 떠나지 않았다면. 그랬다면…….’

모든 것이 바뀌었을지도 모른다. 그러나 동시에 백상은 알고 있었다.

자신의 마음속에 울려 퍼진 이 생각은 허무한 바람에 불과하다는 것을.

남만인 모두의 경사가 될 혼례를 기다리던 그해 겨울.

모두의 바람과 달리 서부 전선은 안정되지 않았고, 일만에 달하는 마교의 군세는 찬바람과 함께 불어닥쳤다.

그리고…… 꽃이 시들었다.

야율향. 꽃처럼 아름답고 강철처럼 단단하던 그녀가 전장에서 시든 그날 이후, 백휘의 얼굴에서는 빛이 사라졌다.

분명 그런 이유에서였을 것이다.

대설산에서의 마지막 전투가 벌어지던 그 날. 그가 무언가에 홀린 듯이 적들을 베고, 또 베며 더욱 큰 위험으로 발을 내디딘 것은.

백상은 그 후에도 종종 생각하곤 했다. 어쩌면 그 아이는, 좁은 협곡 어딘가에서 피어 있는 꽃 한 송이를 본 것은 아닐까 하고.

‘정말 그랬던 것이냐?’

언제나 그렇듯, 대답이 돌아오지 않는 물음을 던진 백상은 뿌옇게 물든 면경을 바라보았다.

아니, 지금 그가 보고 있는 온 세상이 그러했다.

툭. 투둑.

구름 한 점 없이 맑은 하늘. 하지만 어디선가 떨어지는 빗방울.

그리고 다음 순간, 백상의 귓가를 파고드는 누군가의 목소리.

“어머, 나중에 다시 와야 하나?”

백상은 천천히 돌아섰다. 붉게 충혈된 그의 눈동자에, 유령처럼 나타난 한 여인이 비쳤다.

“……남천마후(南天魔后).”

백상의 부름에 여인, 남천마후는 활짝 웃었다. 꽃처럼 화사하고, 독사처럼 사악한 웃음이었다.
```

## Final English reading copy

```markdown
# Chapter 673

This was the first turbulent period to descend upon the world since the end of the Great Faction War.

It had come to the Central Plains, known as the center of the world, and to distant Nanman, thousands of li away from the Central Plains.

“Gasp, pant… Did everyone hear the news?”

“Catch your breath before you talk. What is it this time?”

With new rumors spreading by the day, the Nanman people were no longer as shocked as they had been at first.

No, to be precise, they had begun to think there was nothing left that could surprise them.

And for good reason. The events of the past month or so had been one massive shock after another—greater than the combined impact of every incident that had occurred in Nanman since the Great Faction War ended.

The massacre of a Miao village by Han Chinese.

The attack of a Thousand-Year Spider that had suddenly appeared from Ailao Mountain, which had remained quiet for decades.

And the story of a young Han Chinese man who had not only entered the Inner Palace for the first time in the history of the Nanman Beast Palace, but had even attended the Tribal Grand Council, where only thirty-two tribal chieftains were permitted to sit.

If the series of new incidents had ended there, perhaps things would have been manageable.

But when more than a hundred Yao warriors were brutally killed in the Western Yao Estate just three days earlier, and two Great Chieftains of immense symbolic importance went missing, the situation began rushing forward like a torrent.

*The culprit! The culprit behind the Western Yao Estate incident has been revealed! It was that young Han Chinese man! Jin Taekyung!*

*Wait. Just wait a moment. Have you already forgotten that Jin Taekyung saved the warriors at Ailao Mountain the day before? Nothing has even been conclusively established yet. It’s too soon to make a judgment…*

*Too soon? Ever since those Han Chinese bastards came here, nothing but bad things have happened. There’s no reason to wait any longer!*

*You’re right!*

Only reason could overcome anger, but the voices of those few people were helplessly buried beneath the shouts of many Nanman people whose reason had already gone numb.

*Drag the Han Chinese out into the street and dismember them!*

*Great Chieftain Baeksang! You must punish those bastards!*

The festive music and laughter that had filled the streets every year when the Tribal Grand Council convened could no longer be heard.

Angry shouts echoed from every direction, and two names were always included in those cries.

Jin Taekyung. And Baeksang.

Their status differed as greatly as their origins, ages, and names.

For the Nanman people, this was only natural.

One was an outsider from the distant Central Plains—a criminal who had committed a tragedy that could never be forgiven. The other was the Great Chieftain who led the Bai people, the strongest tribe in this land after the Miao people.

The Nanman people still respected and loved their Palace Lord, who possessed martial prowess renowned throughout the world and an unpretentious personality. But it was impossible for their trust not to crack over the Western Yao Estate incident.

After all, it was none other than the Palace Lord, Yayul Cheok, who had brought the Han Chinese responsible for every recent misfortune into the Inner Palace.

Yet even those who had cheered for Great Chieftain Baeksang could not help but become flustered when they heard the new rumors that emerged at daybreak.

“What, what did you say?”

“Did I… Did I hear that wrong?”

Their pupils trembled, and their faces were filled with bewilderment.

Everyone who heard the news could only keep repeating the unbelievable story in their minds, wearing the same expression and the same look in their eyes.

*The Palace Lord… tried to harm Great Chieftain Baeksang last night, failed, and then fled?*

At first, they all thought it was a ridiculous false rumor. The Palace Lord they knew—the Great Chieftain of the Miao people, Yayul Cheok—was not that kind of person.

Before he was an excellent Palace Lord, he was a good man. More than anyone else, he was a native of this land who cared for Nanman.

But the news that followed was enough to plunge the beliefs and questions of the Nanman people into an abyss.

“Baeksang is taking office as the temporary Palace Lord? What does that mean?”

“I-I don’t know either. But the Inner Palace posted a notice. It said exactly what we heard.”

“What kind of nonsense is this? How could that possibly be true?”

“That’s not all. Apparently, the Palace Lord even mobilized the Young Palace Lord and dozens of elite warriors under his command to raid the underground prison and release the culprit, Jin Taekyung, along with the other Han Chinese.”

“……!”

“I can hardly believe it either, but the circumstances are remarkably clear. It’s an undeniable fact that the Palace Lord has been friendly toward the Han Chinese for a long time. And the whereabouts of Jin Taekyung, the Young Palace Lord, and the other Han Chinese are unknown. The Tribal Grand Council was convened last night, and they apparently declared this a betrayal against all of Nanman and issued a general mobilization order.”

“What? A general mobilization order?”

“That’s right. I heard it was decided along with the matter of the temporary Palace Lord. They must intend to hunt down and execute the rebels who have thrown Nanman into chaos. Naturally, the highest-priority targets are the Han Chinese Jin Taekyung and the Palace Lord. No—the former Palace Lord.”

“Former Palace Lord? What are you talking about?”

“I don’t know. I’m still confused myself. But how could ordinary tribesmen like us know the details? We can only follow the Tribal Grand Council’s decision.”

The contents of the notice, stamped clearly with the Inner Palace’s seal, spread in an instant, and the Nanman people’s reactions split into three groups.

Those who believed the Beast Miao King had betrayed them.

Those who refused to believe it under any circumstances.

And those who, without questioning or making any effort to seek the truth, simply submitted to the new reality placed before them.

Then, amid this whirlwind of extreme confusion, more than fifty warriors returned to the Outer Palace through the western gate, each carrying injuries of varying severity.

Their bodies trembled like aspens, and their faces bore an indelible terror. The remains of the enormous flames visible from ten li away were still etched clearly in their wavering eyes.

“Mon… monster…”

The voice that slipped between someone’s lips was frozen solid, despite the blazing sunlight pouring down overhead.

It was around noon.

* * *

Baeksang stared at his reflection in a large mirror.

He had a youthful, handsome appearance and a well-balanced physique that belied his age of more than seventy. He was even dressed in garments made from the pure white fur of a fox.

Anyone who saw him might have marveled at his dignity and bearing, saying he looked like the ruler of an entire kingdom.

But Baeksang’s gaze remained fixed on his own coldly hardened face.

*Was I wearing this expression all this time? For so many years?*

Even when he looked back over the past several decades, he could not remember when he had last laughed sincerely.

Now, he could only take out those old memories covered in dust and examine them once more.

*Yes. That was the last time.*

A memory from one particular day surfaced, and the chill in his eyes began to melt.

After a victory in a fierce battle, they had been given several days of sweet respite.

The bold boy who had set out after his father, determined to defeat the Demonic Cult, had already grown into a handsome young man. And the girl who had been lively since childhood—and therefore always covered in scrapes and bruises—had grown into a beautiful woman.

The young man’s name was Hwi. The woman’s name was Hyang.

The two of them were as radiant and fragrant as their names. They were a pair of flowers that had bloomed amid a battlefield overflowing with blood and death. Though they called each other dog-and-monkey enemies despite having grown up together, they would sometimes walk together while avoiding the eyes of others.

They probably had not known.

Back then, when they had carefully slipped away from the people drunk on victory and alcohol and walked together along a hill drenched in faint moonlight, someone had been watching them.

*…You came again?*

*…Why did you come again, hyung?*

*Do you ask because you don’t know? I came to keep watch in case Hwi, that wolf-like bastard, tried anything with my frail and beautiful Hyang.*

*I’m asking because I’m genuinely curious. Are you serious?*

*Of course I’m serious.*

*Then you must know that Little Tide Demon died in the battle three days ago.*

*Little Tide Demon? That bastard who could slap the Heavenly Demon across the face if lust were martial arts?*

*That’s right.*

*As a father with a daughter, I’d been meaning to teach him a lesson someday. Good riddance. But why are you suddenly bringing this up?*

*That bastard. Hyang killed him.*

*……*

*Apparently, Hwi was fighting Little Tide Demon and suffered a sword wound. Then Hyang suddenly appeared and smashed Little Tide Demon’s head with a pair of axes she had picked up from somewhere.*

*……*

*And apparently, that still didn’t satisfy her. She crushed the dead bastard’s balls, hurled every curse imaginable at him, and hacked his corpse to pieces. In Hwi’s words, it looked like an imperial palace chef mincing meat with uncanny skill.*

*…That’s a lie. My Hyang would never do that.*

*Even excluding Hwi, five people saw it. Three of them still can’t speak because of the shock.*

*Good. Then tell them to keep their mouths shut. Otherwise, I might have to personally do something to seal their lips… Oh. No.*

*You’re not some kind of fiend… Gasp.*

That day, the sworn brothers crouching far away in the darkness had unintentionally witnessed it.

The sight of the two children they cherished more dearly than their own lives slowly tilting their heads toward each other.

*Turn around. Quickly!*

*Lower your voice first, hyung! And I already turned around!*

*Oh, please. Good heavens. What did I just see?*

*What else? Did you leave your eyes in Nanman? They were kissing—mmph. Mmph!*

*Baeksang, you conniving bastard! You sent that wolf-like son of yours to set up a scheme like this? Do you want to become Palace Lord that badly?*

*Mmph! Hah! Me, Palace Lord? What kind of insane nonsense is that? Maybe after you or I die, but not now.*

*Oh, I see. You intend to fulfill the dream you couldn’t achieve through your son? Since Hyang could become the next Palace Lord, you’ll snatch her up and make her do nothing but housework. Isn’t that it?*

*I’m going insane. Seriously.*

*This is your last chance. Admit it while you still can.*

*No. I said no!*

*Really? Swear it to the heavens.*

*I swear it to the heavens!*

*Fine. I believe you. Then prepare for them to hold their wedding this year.*

*How many times do I have to say it isn’t… What? What did you just say?*

*Don’t ‘what’ me. Just get ready to marry off those youngsters who are crazy about each other.*

*……*

*Why are you just staring at me with that blank expression? You had already figured it out too. Unless you dislike it?*

*D-Dislike it? Of course not. As you said, I had already figured it out. But this is… What should I call it? Huh.*

*Then that settles it. No need for a long discussion. If the western front stabilizes before winter, let’s have them marry and send them back to Nanman. And although the thought makes me feel strange… if they have a child, those two will give up their stubbornness and return willingly, won’t they?*

*A child. Heh… Hehehe. Has so much time really passed already?*

*You’re younger than me, yet you’re pretending to be an old man. Enough. Promise me one thing.*

*What do you want me to promise?*

*That girl Hyang. To me, she is more precious and pitiful than anyone. Because of her worthless father, she lost two older brothers and suffered terribly.*

*Hyung…*

*Damn it. What I’m trying to say is… Shit.*

*Stop. I already know what you’re trying to say. She’s a precious child, so you want me to treat her preciously, don’t you?*

*……*

*You have nothing to worry about. Hwi will certainly do that. He’ll grow old with her not merely as a woman, but as a companion—and sometimes as a friend.*

*I suppose I can trust Hwi.*

*If you can’t trust Hwi, then trust Hyang.*

*What?*

*Look at Hyang’s temper. If Hwi so much as disappoints her, he’ll end up like Little Tide Demon. No doubt abou—!*

*Baeksang, you bastard! How dare you think of my Hyang as—!*

That last shout had been an obvious mistake.

The young man and woman, who had been sharing their first shy kiss, hurriedly pulled away from each other, and the two sworn brothers had to flee with all their strength.

Then, when they reached a quiet stream and were about to hurl a word at each other…

*Yes. We laughed. Loud enough to shake the world.*

He could no longer remember why they had laughed so loudly. It had not been merely because each other’s panic-stricken faces had looked so funny.

Perhaps it had been because they were happy that the two children who had grown up together since childhood were finally being joined together—and that the sworn brothers who had spent their entire lives together would at last become one family.

*Hyang… If she hadn’t left us like that. If only…*

Everything might have changed.

But at the same time, Baeksang knew.

The thought echoing inside his heart was nothing more than a futile wish.

That winter, when they had been waiting for the wedding that would have become a celebration for all the Nanman people—

Contrary to everyone’s hopes, the western front did not stabilize. An army of ten thousand Demonic Cult forces swept in with the cold wind.

And then… the flower withered.

After Yayul Hyang—the woman who had been as beautiful as a flower and as strong as steel—withered on the battlefield, the light vanished from Baekhwi’s face.

That must have been the reason.

On the day of the final battle at the Great Snow Mountain, he had cut down the enemy again and again as though possessed by something, stepping into ever greater danger.

Even afterward, Baeksang sometimes wondered.

Perhaps that child had seen a single flower blooming somewhere in a narrow ravine.

*Was that really what happened?*

As always, Baeksang asked a question that would receive no answer, then stared at the mirror, now gone hazy.

No. That was how the entire world before him looked now.

Drip. Drip.

The sky was clear, without a single cloud. Yet raindrops were falling from somewhere.

And then, in the next moment, someone’s voice pierced Baeksang’s ears.

“Oh my. Should I come back later?”

Baeksang slowly turned around.

Reflected in his bloodshot eyes was a woman who had appeared like a ghost.

“…Southern Heaven Demon Empress.”

At Baeksang’s call, the woman—the Southern Heaven Demon Empress—smiled broadly.

It was a smile as radiant as a flower and as wicked as a viper.
```
